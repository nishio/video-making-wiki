---
type: source
summary: 無音・動きの少なさ・黒コマ・字幕の一致で自動的に切る CLI auto-editor（WyattBlue/auto-editor、最新 31.8.0＝2026-10-30、Nim 製の単体バイナリ）の README・docs・リリースノート・ソース。公式の位置づけは本編集の前の「first pass」で、切った結果を動画として書き出すほか、Premiere・Resolve・Final Cut・Shotcut・Kdenlive 用のタイムラインや JSON のタイムライン（v3）として人の編集に渡せる。repo は Public Domain だが、バイナリはライセンスキーなしだと 3200×1800 を超える書き出しを縮め、複数素材のエディタ書き出しを止める
video_types: [talk, promo, embed]
url: https://github.com/WyattBlue/auto-editor
author: WyattBlue（Basswood-io）
published: 31.8.0 は 2026-10-30（GitHub Releases）。docs の options のページは「Version 31.6.1 Generated: 2026-09-07」
retrieved: 2026-11-09
sources:
  - https://github.com/WyattBlue/auto-editor/blob/master/README.md
  - https://github.com/WyattBlue/auto-editor/releases（31.6.0〜31.8.0 のリリースノート）
  - https://auto-editor.com/installing
  - https://auto-editor.com/docs/cookbook
  - https://auto-editor.com/ref/options
  - https://auto-editor.com/ref/edit
  - https://auto-editor.com/docs/subcommands/whisper
  - https://auto-editor.com/docs/v3
  - https://github.com/WyattBlue/auto-editor/tree/master/skills（auto-editor、auto-editor-transcribe、auto-editor-export の SKILL.md）
  - https://github.com/WyattBlue/auto-editor/blob/master/src/license.nim、src/render/format.nim、src/conductor.nim、src/main.nim（ライセンスキーの扱い）
  - https://app.auto-editor.com/、https://app.auto-editor.com/download（有料のアプリ版）
---

# auto-editor — 無音・動きで「最初の荒切り」を自動でする CLI

## 何の文献か

- OSS の CLI の README・公式 docs（auto-editor.com）・GitHub のリリースノート・ソースコード。作者の文書で、切り方の良し悪しの測定は無い
- repo: star 約 5,800、最終 push 2026-11-08、言語は Nim。最新リリースは **31.8.0（2026-10-30）**。その前は 31.7.2（10-03）、31.7.0（10-02）、31.6.0（09-06）と、月 1〜2 回出ている（GitHub API、2026-11-09）
- 同じ作者の会社 Basswood-io が、GUI のアプリ版（App 6.3.0）とブラウザ版を有料で出している

## 書いてあること

### 何をする道具か

- README:「Before doing the real editing, you first cut out the "dead space" which is typically silence. This is known as a "first pass". Cutting these is a boring task, especially if the video is very long.」。**本編集の前の荒切りを自動でする**、が作者の位置づけ
- 最小は `auto-editor path/to/your/video.mp4` で、`video_ALTERED.mp4` を書く（cookbook）
- `--preview`（別名 `--stats`）で「Show stats on how the input will be cut and halt」、書き出す前に何がどれだけ切られるかを見られる（options）
- 「See What Auto-Editor Cuts Out」: `--when-active cut --when-inactive nil` で、普段切る側だけを書き出せる（README）。**切られた部分を人が見て確かめる**ための逆の書き出し

### 何を基準に切るか（`--edit`、ref/edit）

| 方法 | 何を「残す側」とするか | 既定値 |
|---|---|---|
| `audio` | 時間の区切りごとの「loudest sample ... divided by the max value a sample can be」が threshold 以上 | `threshold=0.04`、`stream=all`。`-19dB` のように dB でも書ける |
| `motion` | 幅 400px に縮め、灰色にし、ぼかし（blur 9）、前のコマとの差が threshold 以上。`x y w h` で画面の一部だけを見られる | `threshold=0.02` |
| `blackdetect` | 画素の threshold 以上が黒（輝度 0.10 以下）。`not` で黒コマを切る | `threshold=0.98` |
| `subtitle` / `regex` | 字幕の行が正規表現に一致する時間 | — |
| `word` | 字幕の行にその語が「whole word」で現れる時間 | `ignore-case=#t` |

- 組み合わせは `(or audio:0.03 motion:0.06)` のような式。`--edit:N` と `--when:N` で 255 までの組を作れ、例として「無音は切り、話は残し、大きな音の所だけ 1.5 倍速」（`--edit:2 audio:-12dB --when:2 speed:1.5`）がある（README）
- 切らずに速める: `-w:0 speed:8`（cookbook の「Speed through silence instead of cutting it」）
- 間合い: `--margin`（既定 0.2s）は「Set sections near "loud" as "loud" too if section is less than LENGTH away」。前後で別の値（`0.3s,1.5sec`）も書ける。`--smooth`（既定 `0.2s,0.1s`）は最小のカット長と最小のクリップ長（options）
- 手で範囲を指定: `--cut`、`--keep`（「leaved "as is", overriding other actions」）、`--set-speed`、`--set-action`（options）
- cookbook の調整の言い方:「Raise the threshold to cut more, lower it to keep more」。**閾値は人が素材を見て決める**前提の書き方

### 字幕で切る（whisper サブコマンド）

- `auto-editor whisper <file> <model>` は whisper.cpp の ggml モデルで書き起こす。`-l/--language`（例に `ja` がある、既定 auto）、`--format text|srt|json`、`-sw/--split-words`、`--threads`（既定 4）（docs/subcommands/whisper）
- その SRT で切る: `auto-editor whisper video.mp4 ggml-medium.en.bin --format srt -o video.srt` → `auto-editor video.mp4 --edit subtitle`。「Auto-Editor understands `video.srt` is related to `video.mp4`」（cookbook）
- 31.7.0（2026-10-02）で同梱の whisper.cpp を 1.9.4 に上げた（リリースノート）。skill（auto-editor-transcribe）は、モデル名に「parakeet」を含めると NVIDIA Parakeet、`apple` で macOS 26 以降の Apple の書き起こしを使える、と書く。Parakeet は `--language` を受け付けない
- 31.8.0 で `burn`（.srt / .ass を焼き込む。「They stay on their words through cuts and speed changes」）と `text` の action が入った

### 人の編集ソフトに渡す（README、auto-editor-export skill）

| `--export` | 先 | 出力 |
|---|---|---|
| `premiere` | Premiere Pro（FCP7 XML） | `.xml` |
| `resolve` | DaVinci Resolve（FCPXML） | `.fcpxml` |
| `final-cut-pro` | Final Cut Pro | `.fcpxml` |
| `shotcut` / `kdenlive` | Shotcut / Kdenlive | `.mlt` / `.kdenlive` |
| `edl` | CMX 3600 EDL | `.edl` |
| `clip-sequence` | 残す区間ごとの別ファイル | 動画 |
| `v1` / `v2` / `v3` | auto-editor 自身のタイムライン | JSON |

- **v3 は JSON の非線形タイムライン**（docs/v3）: `timebase`、`resolution`、`v`（映像のレイヤー）・`a`（音声のレイヤー）にクリップ `{src, start, dur, offset, stream, effects}`。`auto-editor input.v3 -o output.mkv` でそのまま描画でき、FCP7 XML から v3 への変換もできる。「partially-stable. Breaking changes can be made to feature level changes, but not patch level changes」
- 31.8.0 で「Exporting to an editor warns about the actions and tracks its format can't hold」
- ソースには OpenTimelineIO（.otio）の書き出し（src/exports/otio.nim、「compatible with Adobe Premiere Pro」）もあるが、README と export の skill の表には載っていない

### AI エージェントから使う

- README の「Skills」に `npx skills add WyattBlue/auto-editor`。repo の `skills/` に auto-editor・auto-editor-effects・auto-editor-export・auto-editor-transcribe・auto-editor-transitions の 5 つの SKILL.md がある。auto-editor の skill は「Use when someone wants to ... remove silence, shorten a recording ...」と書き、`--preview`「use it to sanity-check before a long render」を勧める

### 入れ方・ライセンス・費用

- 推奨は GitHub Releases のバイナリ（Windows・macOS・Linux）をダウンロードして名前を `auto-editor`（Windows は `auto-editor.exe`）にするだけ。「the binaries are unsigned」。**pip 版はもう出していない**、apt の版は「very old」（installing）。31.8.0 の資産は `auto-editor-linux-x86_64`、`auto-editor-windows-x86_64.exe` など。yt-dlp があれば URL を入力にできる
- README:「Everything in this repository is under the Public Domain」（LICENSE は Unlicense）。「Binary artifacts in the "Releases" section may be under various open source licenses」
- **ただしバイナリにはライセンスキーの検査がある**（ソースを読んだ。実行はしていない）:
  - `src/render/format.nim`: キーなしで描画するとき、解像度が 3200×1800 を超えると `--scale` を下げて収め、「Rendering video without a license is limited to 3200x1800」と warning を出す。複数素材の描画は 720×576 まで
  - `src/conductor.nim`: 「Timeline/project exports that draw from more than one source remain a paid feature」。素材 1 本のエディタ書き出しは対象外
  - `src/main.nim`: `add` action（別の動画・音楽を重ねる）はキーが要る
  - キーは `-k/--license-key` か環境変数 `AE_PRIVATE_LK`
- 有料のアプリ版: 「One-time purchase ... Plans start at $23.99」。無料の評価は「6 exports up to 3200×1800」、時間制限なし。ブラウザ版は「The online editor does all the work locally in your browser. Your media never leaves your computer」（app.auto-editor.com、2026-11-09 時点）

## この wiki への含意

- **何を AI に任せられるか**: 無音・動きの少ない所・黒コマを切る、無音だけ速める、話した語で残す、の荒切り（公式）。ただしこれは閾値の規則で、「AI」は whisper.cpp の書き起こしだけ。LLM に編集させる形にするなら、Claude Code が skill に沿って CLI を回すか、v3 の JSON を書いて描画させる（公式の skill と v3 の仕様はある。組み合わせて動くかは未確認）
- **何が人の判断として残るか**: 作者自身が「first pass」と呼び、本編集は人がする前提。閾値と `--margin` は素材ごとに人が決め、`--preview` と「切った側だけの書き出し」で確かめる作り（公式の書き方からの読み）
- **[[exp-thinklet-reading-demo-video]] と食い違う所**: THINKLET のデモで西尾は、実機の約 30 秒の処理待ちを削らずにナレーションで説明に変えた。無音で切る道具は、まさにその待ちを「dead space」として切る。画面も動かない待ちなら `motion` でも切られる（推測）。待ちを残すなら `--keep` でその区間を守るか、`-w:0 speed:N` で切らずに速める。**何が無駄で何が見せ場かは道具には分からない**
- **[[exp-thinklet-reading-demo-video]] と一致する所**: 西尾は Premiere で編集した。auto-editor は荒切りを Premiere の XML で渡せるので、「荒切りは自動、仕上げは Premiere」の分担がそのまま作れる（素材 1 本ならキー不要）
- **talk の収録（LT・講演の録画、画面収録の解説）に一番効く**。言いよどみの「間」を詰める用途。promo の切り抜きの「どこを選ぶか」には効かない（それは [[web-edit-auto-opusclip]]、[[web-edit-auto-openshorts-ai-youtube-shorts-generator-supoclip-autoclip]]）
- 字幕の時刻: 31.8.0 の `burn` は「切っても速めても字幕が語に付いていく」と書く。台本を正にした字幕（[[web-check-subs-whisperx-stable-ts-faster-whisper]]）を作ってから auto-editor で切る順か、切ってから字幕を作る順かは、galleria で確かめる

## 着手の仕方（未検証。galleria で確かめる）

- **表現できるようになること**: 画面収録・講演の録画の無音・止まった所を自動で詰めた版を、数分で作る。Premiere / Resolve に荒切りのタイムラインとして渡す。効く型: talk（主）、embed・promo の素材の下ごしらえ
- **機械**: galleria WSL（`auto-editor-linux-x86_64`）か galleria Windows（`auto-editor-windows-x86_64.exe`）。GPU 不要（whisper も `--threads` の CPU。GPU を使うかは docs に記述なし）
- **入れるもの・費用**: auto-editor 31.8.0 のバイナリ 1 つ。費用 0、アカウント不要。Public Domain（ただし上のキーの制限: 1 本の素材で 3200×1800 以下なら効かない。4K の収録は縮められる）。字幕で切るなら ggml の Whisper モデル（Hugging Face の ggerganov/whisper.cpp）
- **成熟度**: 2026 年は月 1〜2 回のリリース。v3 のタイムラインは「partially-stable」
- **最小の手順（WSL）**:
  ```bash
  mkdir -p ~/video-tools-trial/ae && cd ~/video-tools-trial/ae
  curl -L -o auto-editor https://github.com/WyattBlue/auto-editor/releases/download/31.8.0/auto-editor-linux-x86_64
  chmod +x auto-editor && ./auto-editor --version
  # 試験素材: 2 秒鳴って 2 秒黙る、を 20 秒（ffmpeg の式の書き方は推測）
  ffmpeg -f lavfi -i "testsrc=d=20:s=1280x720:r=30" \
    -f lavfi -i "aevalsrc=exprs=if(lt(mod(t\,4)\,2)\,0.5*sin(2*PI*440*t)\,0):d=20:s=48000" \
    -shortest -c:v libx264 -pix_fmt yuv420p -c:a aac test.mp4
  ./auto-editor test.mp4 --preview
  ./auto-editor test.mp4 -o test_cut.mp4
  ./auto-editor test.mp4 --export premiere -o test.xml
  ./auto-editor test.mp4 --export v3 -o test.v3
  # 本番の素材（自分の LT の録画など）で、切る側だけも書き出して見比べる
  ./auto-editor talk.mp4 --margin 0.3s,0.5s -o talk_cut.mp4
  ./auto-editor talk.mp4 --when-active cut --when-inactive nil -o talk_removed.mp4
  # 日本語の字幕で切る（モデル名は推測。多言語版を使う。.en は英語専用）
  ./auto-editor whisper talk.mp4 ggml-large-v3-turbo.bin -l ja --format srt -o talk.srt
  ./auto-editor talk.mp4 --edit subtitle -o talk_speech.mp4
  ```
- **動いたと言える確かめ方**:
  - `--version` が `31.8.0`
  - `ffprobe -v error -show_entries format=duration -of csv=p=0 test_cut.mp4` が 20 秒より短い。margin 0.2 秒なら残るのは 0–2.2、3.8–6.2、7.8–10.2、11.8–14.2、15.8–18.2 秒で、合計 **約 11.8 秒**の見込み（計算による。smooth の効き方で少しずれうる）
  - `test.xml` を Premiere に読み込み、クリップが 5 つ並ぶ。`test.v3` は `python3 -m json.tool test.v3` で読め、`v` の配列にクリップ 5 つ
  - 本番の素材は `talk_removed.mp4` を見て、残すべき「間」（強調の溜め、デモの待ち）が入っていないか人が確かめる。キーの制限に当たると stderr に「without a license is limited to」が出る
- **所要の見込み（推測）**: 導入と試験素材 20 分。本番の素材で閾値を決めるのに 30 分〜1 時間

## Open Questions

- 日本語の字幕で `word` が使えるか。「whole word」の判定は語の間の空白を前提にしているように読め、空白の無い日本語では効かないかもしれない（推測）。`subtitle` の正規表現なら文字列の一致なので動くはず（推測）
- `--edit subtitle` に pattern が要るか、docs の間で食い違う。ref/edit は `pattern: String` を引数に持ち、cookbook と transcribe の skill は pattern なしで「字幕のある所を全部残す」と書く
- 同梱の whisper.cpp が GPU（CUDA）を使うか、docs に記述がない
- Public Domain の repo と、バイナリのキーの検査の関係。ソースから自分でビルドすればキーの検査も入る（ソースにあるので）。「無料で使える範囲」は 1 本・3200×1800 以下・`add` なし、と読んだが、版で変わりうる（`LICENSE_PERIOD_YEARS` などの定数がある）
- 31.8.0 の `burn` で焼いた日本語の字幕が、指定した書体で組めるか（`--font` の扱い）
- 西尾の「3 秒延長」（[[exp-shortmovie-draft-generator]]）と auto-editor の既定 margin 0.2 秒は一桁違う。どちらが日本語の話し言葉の切りに合うかは、同じ素材で比べないと分からない
