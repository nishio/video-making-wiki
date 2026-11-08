---
type: source
summary: ffmpeg の loudnorm 2 パスを自動でやる Python の CLI「ffmpeg-normalize」（Werner Robitza、MIT ライセンス、v1.43.0 が 2026-10-14 に PyPI へ）。既定は EBU R128 の 2 パス・目標 −23 LUFS・LRA 7・TP −2、映像はコピー、出力は MKV と PCM。dynamic に黙って落ちるのを避ける `--keep-loudness-range-target` と `--auto-lower-loudness-target` を持ち、組み込みの preset `streaming-video` は −14 LUFS、`podcast` は −16 LUFS
video_types: [any]
url: https://github.com/slhck/ffmpeg-normalize
author: Werner Robitza（slhck）ほか 24 名の貢献者
published: 2026-10-14（PyPI の v1.43.0 のアップロード日）／文書は日付なし
retrieved: 2026-11-09
sources:
  - https://github.com/slhck/ffmpeg-normalize （README。raw で全文を読んだ）
  - https://raw.githubusercontent.com/slhck/ffmpeg-normalize/master/LICENSE （MIT、Copyright (c) Werner Robitza）
  - https://pypi.org/pypi/ffmpeg-normalize/json （版 1.43.0、requires_python >=3.10、license_expression MIT）
  - https://slhck.info/ffmpeg-normalize/usage/normalization-options/ （linear と dynamic、fallback の条件と回避）
  - https://slhck.info/ffmpeg-normalize/usage/presets/ （組み込み preset）
  - https://slhck.info/ffmpeg-normalize/usage/cli-options/ （既定値）
  - https://slhck.info/ffmpeg-normalize/usage/file-input-output/ （出力の容器と音声コーデック）
  - https://slhck.info/ffmpeg-normalize/advanced/faq/ （「loudnorm を自分で 2 回回せばよいのでは」への答え）
  - https://slhck.info/ffmpeg-normalize/getting-started/requirements/ （ffmpeg 7.x 推奨）
---

# ffmpeg-normalize（loudnorm の 2 パスを自動でやる CLI）

## 何の文献か

- オープンソースの道具の README と公式文書（作者のサイト slhck.info）。作者 Werner Robitza は README の貢献者表から 24 名とともに保守している。効果の測定ではなく、機能と既定値の説明
- GitHub の API は CyEC2 からは rate limit で読めず、star 数・最終 push 日は取れていない。版と日付は PyPI による（**v1.43.0、2026-10-14 アップロード**）。README の What's New は 1.42.0 までを書いている
- ライセンス: リポジトリの LICENSE は MIT（「Copyright (c) Werner Robitza」）。PyPI の license_expression も MIT

## 書いてあること

### 何をするか

- 「normalizes media files to a certain loudness level using the EBU R128 loudness normalization procedure. It can also perform RMS-based normalization …, or peak normalization」
- 「EBU R128 loudness normalization — **Two-pass by default**, with an option for one-pass dynamic normalization」「Video file support — Process video files while preserving video streams」
- FAQ「Couldn't I just run `loudnorm` with ffmpeg?」への答え: 「You absolutely can. However, a single-pass `loudnorm` uses dynamic mode by default … For linear normalization …, you need two passes … This is exactly what `ffmpeg-normalize` automates. It also handles edge cases like adjusting the target LRA and loudness to avoid silent fallback to dynamic mode」

### 既定値（CLI options）

- `-t/--target-level` 既定 **−23**（LUFS）、`-lrt` 既定 **7.0**、`-tp` 既定 **−2.0** dBTP
- `-c:v` 既定 **copy**（映像は再符号化しない）
- `-ar`: 「Will use input sample rate by default, except for EBU normalization, which will change the input sample rate to 192 kHz」。`--dynamic` の説明は「Dynamic mode will automatically change the sample rate to 192 kHz」
- 出力の既定は `normalized/<名前>.mkv`、音声は容器が PCM を持てれば PCM（大きくなる）。`.mp4` に書くなら AAC が選ばれる（v1.41.0 以降、ffmpeg のその容器の既定コーデック）
- `-p/--print-stats` で両パスの統計を JSON に、`-n/--dry-run` で正規化せず測るだけ

### linear が dynamic に落ちる条件と回避（normalization-options）

- 落ちるのは (1) 入力の LRA が目標の LRA より大きいとき、(2) 目標に上げると True Peak が上限を超えるとき、と書く。「At this time, the `loudnorm` filter in ffmpeg does not provide a way to force linear mode」
- 回避: `--keep-loudness-range-target`（目標 LRA を入力の LRA にする）、`--keep-lra-above-loudness-range-target`（入力が上回るときだけ）、`--auto-lower-loudness-target`（TP を超えないよう目標 I を自動で下げる）、`--lower-only`（上げない）
- 推奨の組み合わせ: `ffmpeg-normalize input.wav --keep-loudness-range-target --auto-lower-loudness-target`
- 線形の利点として「preserves the original dynamic range」「avoids potential artifacts or pumping effects」と書く（作者の説明。聴感の比較は示していない）

### preset（v1.36.0〜）

- `podcast`: EBU R128、−16 LUFS、LRA 7、TP −2.0（「using the AES recommended standard」）
- `streaming-video`: EBU R128、**−14 LUFS**、LRA 7、TP −2.0（「the standard loudness level for video content」）
- `music`: RMS −20 dB、batch
- 自作は `~/.config/ffmpeg-normalize/presets/<名前>.json`（Windows は `%APPDATA%\ffmpeg-normalize\presets\`）

### 動かすのに要るもの

- Python 3.10 以上と ffmpeg（「ffmpeg 7.x is recommended, although it works with 5.x and above」）。`pip3 install ffmpeg-normalize` か `uvx ffmpeg-normalize …`。ディストリのパッケージの ffmpeg は古いことが多いので静的ビルドを勧める
- FAQ: 話し声には ffmpeg の `speechnorm` フィルタ（1 パス）も見よ、と書く

## この wiki への含意

- **2 パスの手順（[[web-check-loudness-ffmpeg-loudnorm-ebur128]]）を自分で書く代わりになる**。とくに「dynamic に黙って落ちる」を `--keep-loudness-range-target --auto-lower-loudness-target` で避け、`--print-stats` の `normalization_type` で確かめられる
- **preset の数値は作者の選択で、規格ではない**: `streaming-video` の −14 LUFS は、YouTube の公式ヘルプに数値が無い（[[web-aes-td1004-streaming-loudness]]）ことと合わせて、「通説の値」として扱う。経験の −16（[[exp-html-capture-pipeline]]）は `podcast` preset の値に当たる
- **既定の TP −2.0 と経験の −1.5**: preset を使うと経験より 0.5 dB 厳しくなる。どちらでも配信の推奨（−1 dBTP 以下）は満たす（[[web-aes-td1004-streaming-loudness]]）
- **映像はコピー**なので、HTML から撮った mp4（[[exp-html-capture-pipeline]]）の仕上げに最後にかけても画は変わらない。ただし出力の既定が MKV＋PCM なので、`-o out.mp4 -c:a aac -b:a 192k` を付ける
- 声と BGM の釣り合い（ダッキング）は扱わない。全体を揃える道具で、ステムごとの差は [[web-check-loudness-ffmpeg-loudnorm-ebur128]] の手順 4 で測る

## 着手の仕方（未検証。galleria で確かめる）

- **何が表現できるようになるか / 効く型**: 書き出した動画の音量を 1 行で配信向けの値に揃える。複数本（シリーズ・embed で続けて流す動画）を同じ大きさに揃える（any。embed は流しっぱなしで続けて流すとき特に）
- **機械・入れるもの**: galleria WSL。`uvx ffmpeg-normalize`（uv は WSL にある。v1.43.0、MIT、費用・アカウントなし）。ffmpeg は既存のもの（7.x 以上を推奨と文書）
- **成熟度**: 2026-10 に 1.43.0。README の What's New に 1.34〜1.42 の機能追加が並び、更新は続いている（star 数は今回取れず）
- **最小の手順**（WSL、`~/video-tools-trial/loud`）:
  ```sh
  ffmpeg -version | head -1
  uvx ffmpeg-normalize --version
  # 測るだけ（正規化しない）
  uvx ffmpeg-normalize in.mp4 -p -n -f
  # 経験と同じ目標で、線形を保つように
  uvx ffmpeg-normalize in.mp4 -t -16 -tp -1.5 --keep-loudness-range-target --auto-lower-loudness-target \
      -c:a aac -b:a 192k -ar 48000 -o out.mp4 -p > stats.json
  # preset で（−14 LUFS、TP −2）
  uvx ffmpeg-normalize in.mp4 --preset streaming-video -c:a aac -b:a 192k -ar 48000 -o out_14.mp4
  ```
- **動いたと言える確かめ方**: `stats.json` の 2 パス目の `normalization_type` が `"linear"`、`output_i` が目標（`--auto-lower-loudness-target` が効いたときは目標より低い値になる。その差も記録する）、`output_tp` ≤ −1.5。別に `ffmpeg -nostats -i out.mp4 -filter_complex ebur128=peak=true -f null -` の Summary で I と True Peak が一致する。`ffprobe` で映像ストリームの codec・bit_rate が in.mp4 と同じ（コピーされた）
- **所要の見込み**（推測）: 初回の uvx の取得込みで 10〜20 分

## Open Questions

- `--auto-lower-loudness-target` で目標が下がった場合、−16 を狙って −17〜−18 になることがありうる。配信先で並んだときの差をどこまで許すか（西尾が決めること）
- `streaming-video` preset の −14 の根拠を作者は書いていない
- `-ar` の説明（EBU 正規化は 192 kHz に変える）と ffmpeg 本体のソース（線形なら上げない。[[web-check-loudness-ffmpeg-loudnorm-ebur128]]）の差。`-ar 48000` を常に付ければ実害はない
