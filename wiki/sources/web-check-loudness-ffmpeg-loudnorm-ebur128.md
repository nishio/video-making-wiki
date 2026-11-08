---
type: source
summary: ffmpeg の loudnorm（EBU R128 の正規化）と ebur128（測定）の公式文書・ソースコードと、loudnorm の作者 Kyle Swanson の解説（2016）。loudnorm は既定 linear=true だが、measured_* を全部渡し、かつ「入力の LRA ≤ 目標の LRA」「入力の True Peak＋利得 ≤ 目標の TP」のときだけ線形になり、それ以外は黙って dynamic（192 kHz に上げる AGC＋リミッタ）になる。西尾の経験の `loudnorm=I=-16:TP=-1.5:LRA=11` は作者のブログの 1 パスの例そのもの
video_types: [any]
url: https://ffmpeg.org/ffmpeg-filters.html#loudnorm
author: FFmpeg project（文書・ソース）／Kyle Swanson（loudnorm の作者、k.ylo.ph）
published: unknown（ffmpeg-filters.html は git master から生成。最新安定版は FFmpeg 9.0.2、2026-09-18）／2016-04-04（Swanson のブログ）
retrieved: 2026-11-09
sources:
  - https://ffmpeg.org/ffmpeg-filters.html （8.97 loudnorm、20.10 ebur128 の節を全文読んだ。2026-11-09 取得）
  - https://raw.githubusercontent.com/FFmpeg/FFmpeg/master/libavfilter/af_loudnorm.c （init と query_formats を読んだ。線形に切り替わる条件と 192 kHz の扱い）
  - http://k.ylo.ph/2016/04/04/loudnorm.html （Kyle Swanson「loudnorm」2016-04-04。全文を読んだ）
  - https://ffmpeg.org/download.html （FFmpeg 9.0.2 "Lei"、2026-09-18 リリース）
---

# ffmpeg の loudnorm・ebur128（ラウドネスの測定と 2 パスの合わせ込み）

## 何の文献か

- **ffmpeg の公式文書**（ffmpeg-filters.html）: ffmpeg.org の文書は開発版（git master）から生成されたもの。2026-11-09 時点の最新安定版は **FFmpeg 9.0.2（2026-09-18）**。手元の版で `ffmpeg -h filter=loudnorm` を見て食い違いを確かめる必要がある（例: `stats_file` オプションが入った版は確かめていない）
- **af_loudnorm.c**（FFmpeg のソース、master）: 文書に書かれた条件を実装で確かめるために読んだ
- **Kyle Swanson「loudnorm」**（2016-04-04、作者の個人ブログ）: フィルタを設計・実装した本人の説明。設計意図の記述で、他者の検証ではない
- 既存の [[web-torcoli-2019-background-ducking]] が loudnorm の要点（measured_* を全部渡さないと dynamic、192 kHz）を書いている。このページはその先の**手順と条件**を足す

## 書いてあること

### loudnorm（文書 8.97）

- 「EBU R128 loudness normalization. Includes both dynamic and linear normalization modes. Support for both single pass (livestreams, files) and double pass (files) modes.」
- 目標: `I`（既定 −24.0、範囲 −70〜−5）、`LRA`（既定 7.0、1〜50）、`TP`（既定 −2.0、−9〜0）
- 1 パス目の測定値: `measured_I`・`measured_LRA`・`measured_TP`・`measured_thresh`。`offset`（リミッタの前にかける利得）
- `linear`: 「`measured_I`, `measured_LRA`, `measured_TP`, and `measured_thresh` must all be specified. **Target LRA shouldn't be lower than source LRA and the change in integrated loudness shouldn't result in a true peak which exceeds the target TP. If any of these conditions aren't met, normalization mode will revert to dynamic.** … Default is `true`.」
- 「In dynamic mode, to accurately detect true peaks, the audio stream will be upsampled to 192 kHz. Use the `-ar` option or `aresample` filter to explicitly set an output sample rate.」
- `print_format`（summary / json / none、既定 none）、`stats_file`（print_format が要る。`-` で標準出力）、`dual_mono`（モノラルをステレオで聞く前提の補正）

### ソースで確かめたこと（af_loudnorm.c、master）

- `init()` の中で、`linear` が真で、measured_* の 4 つが既定値のままでなく、かつ `measured_tp + (target_i − measured_i) <= target_tp` と `measured_lra <= target_lra` を両方満たすときだけ `LINEAR_MODE` になる。そのとき `offset` は `target_i − measured_i` で**上書きされる**（ユーザーの offset 指定は線形のときは使われない、と読める）
- `query_formats()` は、LINEAR_MODE でないときだけ入力の標本化周波数を 192000 に固定する。**線形のときは 192 kHz に上げない**。dynamic のとき出力が 192 kHz になるので `-ar 48000` が要る

### Kyle Swanson のブログ（2016）

- 仕組み: 「a specially designed loudness-tuned AGC followed by a transparent look-ahead true peak limiter」。AGC は目標の LRA の範囲を超えたときだけ動き、包絡はガウス核で平滑化。無音の判定には R128 の相対ゲートを使う。True Peak のリミッタは 192 kHz に上げ、100 ms の先読み
- 例として「`-16.0 LUFS IL` with a maximum true peak of `-1.5 dBTP`, values which are within the AES streaming loudness recommendation」と書き、1 パスの例に **`ffmpeg -i in.wav -af loudnorm=I=-16:TP=-1.5:LRA=11 -ar 48k out.wav`** を挙げている
- 2 パス: 1 回目 `loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json -f null -` で `input_i`・`input_tp`・`input_lra`・`input_thresh`・`target_offset` が JSON で出る。2 回目にそれを `measured_I=…:measured_LRA=…:measured_TP=…:measured_thresh=…:offset=…:linear=true:print_format=summary -ar 48k` で渡す
- **ブログの 2 パスの例自体が `Normalization Type: Dynamic` で終わっている**（入力 LRA 18.06 LU > 目標 11 なので、上の条件で線形にならない）。作者は「For precise integrated loudness, always use dual-pass mode and supply the offset parameter」「Maximum true peak is always guaranteed」「LRA … is not guaranteed」と書いている

### ebur128（文書 20.10）

- 測定用。既定で 10 Hz で M（0.4 秒）・S（3 秒）・I・LRA をログに出し、終わりに Summary を出す
- `peak=true` で True Peak（オーバーサンプリング、`TPK`）。`metadata=1` で 100 ms ごとのフレームに `lavfi.r128.*` のメタデータを付ける（`ametadata=print` で書き出せる）
- `target` の説明に「material published online may prefer a level of -16LUFS (e.g. for use with podcasts or video platforms)」とある（ffmpeg 文書の記述で、規格ではない）
- 例: `ffmpeg -nostats -i input.mp3 -filter_complex ebur128 -f null -`
- 測るのは double の標本形式に変換したもの。出力に流すなら後ろに `aformat`/`aresample` が要る、と書く

## この wiki への含意

- **経験の `loudnorm=I=-16:TP=-1.5:LRA=11`（[[exp-html-capture-pipeline]]・[[exp-democracy-river-video]] 英語版）は Swanson のブログの 1 パスの例と一字一句同じ**。1 パスなら dynamic（AGC＋リミッタ）で、`mix.py` で作った声と BGM の差を時間とともに動かしうる。`-ar` を付けていなければ出力は 192 kHz の可能性がある（AAC に入れるときに 48 kHz 等へ変わったかは経験ページからは分からない）。経験ページは単パスか 2 パスかを書いていない（[[web-torcoli-2019-background-ducking]] の Open Question と同じ）
- **2 パスにしても線形になるとは限らない**: 入力の LRA が 11 を超える、または上げ幅で True Peak が −1.5 を超えると dynamic に戻る。ナレーション＋BGM で BGM を声の間だけ下げた mix は、場面の区切りで LRA が広がりうる（推測）。summary の `Normalization Type` を必ず見る
- **promo**: R 128 s1 の「Short-term の最大は目標の +5 LU まで」（[[web-ebu-r128-itu-bs1770]]）は `ebur128=metadata=1` の S の最大で確かめられる。[[exp-sutra-hype-editions]] のドロップのような作りを測る手段
- **talk**: 声と BGM の差（Torcoli らの「音楽で 10 LU 以上」）は、ステム（声だけ・BGM だけ）を別々に ebur128 で測れば数字になる（下の手順）
- **embed**: 会場で流す動画同士の大きさを揃えるなら、全部を同じ統合値・同じ TP に 2 パスで揃えておく（推論。会場での釣り合いは別問題、[[narration-bgm-sound]]）

## 着手の仕方（未検証。galleria で確かめる）

- **何が表現できるようになるか / 効く型**: 音の大きさを数字で決めて揃える（any）。声と BGM の差を測って直す（talk・embed）。短尺の瞬間的な大きさを見張る（promo）
- **機械**: galleria WSL（ffmpeg は WSL にあると brief に記録。版は `ffmpeg -version` で確かめる）。Windows 側の ffmpeg でも同じだが、フィルタ引数のパスで `\` と `:` が壊れる（[[exp-galleria-ffmpeg-measurement-and-delivery]]）ので WSL を使う。費用・アカウントなし。ffmpeg 本体は LGPL/GPL（ビルドによる）。出力物の利用に制約はない（ライセンス条文は今回読んでいない）
- **成熟度**: loudnorm は 2016 年から ffmpeg 本体に入っている。最新安定版 9.0.2（2026-09-18）
- **最小の手順**（WSL。作業場 `~/video-tools-trial/loud`。ファイル名は例）:
  1. 現状を測る（動画でも wav でも可）:
     ```sh
     ffmpeg -hide_banner -nostats -i in.mp4 -filter_complex ebur128=peak=true -f null - 2>&1 | tail -n 14
     ```
  2. 1 パス目（測るだけ。JSON は標準エラーの最後に出る）:
     ```sh
     ffmpeg -hide_banner -nostats -i in.mp4 -vn -af loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json -f null - 2> pass1.log
     python3 - <<'EOF' > pass1.json
     import re,json; t=open('pass1.log').read(); print(json.dumps(json.loads(t[t.rfind('{'):t.rfind('}')+1])))
     EOF
     cat pass1.json   # input_i, input_tp, input_lra, input_thresh, target_offset
     ```
  3. 2 パス目（値は pass1.json から。映像はコピー）:
     ```sh
     ffmpeg -hide_banner -i in.mp4 -c:v copy -af loudnorm=I=-16:TP=-1.5:LRA=11:measured_I=<input_i>:measured_LRA=<input_lra>:measured_TP=<input_tp>:measured_thresh=<input_thresh>:offset=<target_offset>:linear=true:print_format=summary -ar 48000 -c:a aac -b:a 192k out.mp4 2> pass2.log
     grep -A12 "Input Integrated" pass2.log
     ```
     `Normalization Type: Dynamic` と出たら、`LRA=` を `input_lra` 以上（例: `LRA=20`）にするか、`I=` を下げて `input_tp + (I − input_i) ≤ TP` を満たすようにして 2 回目をやり直す（条件はソースの init() から。推測で補った手順）
  4. ステムで声と BGM の差を測る（mix の材料が別ファイルである前提。BGM はダッキング後の、mix に入る状態のもの）:
     ```sh
     for f in voice.wav bgm_ducked.wav; do echo $f; ffmpeg -hide_banner -nostats -i $f -filter_complex ebur128 -f null - 2>&1 | grep -E "^\s+I:"; done
     ```
     差 = I(voice) − I(bgm)。これは全体の統合値の差で、Torcoli らの「LD」の定義と同じかは原典未読で確かめていない（[[web-torcoli-2019-background-ducking]]）。声が鳴っている区間だけの差を見たいなら、`ebur128=metadata=1,ametadata=print:key=lavfi.r128.S:file=voice_S.txt` で両ステムの S を 100 ms ごとに書き出し、声の S が −40 LUFS を超える時刻だけで差の中央値を取る（推測の手順）
  5. 短尺の S の最大（promo）:
     ```sh
     ffmpeg -hide_banner -nostats -i out.mp4 -vn -af ebur128=metadata=1,ametadata=print:key=lavfi.r128.S:file=S.txt -f null -
     grep -o "lavfi.r128.S=[-0-9.]*" S.txt | cut -d= -f2 | sort -g | tail -1
     ```
- **動いたと言える確かめ方**: 2 パス目の summary に `Normalization Type: Linear`、`Output Integrated` が目標 ±0.5 LU 以内（作者は offset を渡せば精確と書く）、`Output True Peak` が TP 以下。手順 1 を out.mp4 にかけて Summary の `I:` と `Peak:` が同じ値になる。`ffprobe -v error -show_entries stream=sample_rate -select_streams a out.mp4` が 48000
- **所要の見込み**（推測）: 1 本 1〜2 分の動画なら各パス数秒〜十数秒。手順を shell 関数にまとめるまで 30 分〜1 時間

## Open Questions

- 経験の mix（democracy-river 英語版）が 1 パスだったか、出力の標本化周波数がいくつだったか。`ffprobe` と手順 1 で実物を測れば分かる（galleria から Mac の repo を読むなら Mac 側で）
- 文書の「dynamic のときだけ 192 kHz」（現行文書・ソース）と、ffmpeg-normalize の CLI 文書の「EBU 正規化は入力を 192 kHz に変える」（[[web-check-loudness-ffmpeg-normalize]]）は言い方が違う。後者は dynamic に落ちる場合を含めた安全側の書き方か。実物で確かめる
- `stats_file` がどの版から入ったかは確かめていない。9.0.2 で使えれば手順 2 の python は要らない
- ナレーション＋BGM の mix で、線形のまま `LRA=11` を満たすか。満たさないなら LRA の目標を上げるのと dynamic を受け入れるのとどちらが良いか（R 128 は 1 分未満で LRA を使うなと書く。[[web-ebu-r128-itu-bs1770]]）
