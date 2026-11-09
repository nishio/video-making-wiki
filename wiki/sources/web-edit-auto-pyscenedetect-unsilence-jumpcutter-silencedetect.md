---
type: source
summary: auto-editor に近い OSS の 4 つを、2026-11-09 時点の README・docs・リリースで比べたもの。PySceneDetect（BSD-3、v0.7.3＝2026-11-08）は「場面の切れ目」を検出して ffmpeg で分割する道具で、無音で詰める道具ではない。unsilence（MIT、1.0.9＝2022-11）と jumpcutter（MIT、作者が更新しないと明記）は止まっている。ffmpeg の silencedetect は入れ物なしで無音の区間を記録に出せるが、切るのは自分で書く
video_types: [talk, promo, any]
url: https://github.com/Breakthrough/PySceneDetect
author: Brandon Castellano ほか（PySceneDetect）／Tim-Luca Lagmöller（unsilence）／carykh（jumpcutter）／FFmpeg developers（silencedetect）
published: PySceneDetect v0.7.3 は 2026-11-08。unsilence 1.0.9 は 2022-11-03。jumpcutter の最終 push は 2024-02-28。ffmpeg-filters の文書は取得日の版
retrieved: 2026-11-09
sources:
  - https://github.com/Breakthrough/PySceneDetect（README.md、v0.7.3 のリリースノート）
  - https://www.scenedetect.com/cli/
  - https://www.scenedetect.com/download/
  - https://github.com/lagmoellertim/unsilence（README.md、Releases）
  - https://github.com/carykh/jumpcutter（README.md）
  - https://ffmpeg.org/ffmpeg-filters.html#silencedetect（8.107 silencedetect、8.108 silenceremove）
---

# PySceneDetect・unsilence・jumpcutter・ffmpeg silencedetect — auto-editor の周りの OSS

## 何の文献か

- 4 つとも作者の README・公式 docs。測定は PySceneDetect の benchmark ページ（未読）以外にない
- 比べた数字は GitHub API（2026-11-09）: PySceneDetect star 約 5,400・最終 push 2026-11-08、unsilence 約 600・最終 push 2023-03-28、jumpcutter 約 3,100・最終 push 2024-02-28（リリースなし）

## 書いてあること

### PySceneDetect（場面の切れ目の検出）

- 「Video Cut Detection and Analysis Tool」。**映像の切り替わり（カット・フェード）を見つける**道具で、音は見ない（README）
- CLI: `scenedetect -i video.mp4 split-video`（「Split input video on each fast cut using ffmpeg」）、`save-images`（各場面のコマを保存）、`list-scenes`（CSV）。検出器は `detect-content`（速いカット）、`detect-adaptive`（カメラの速い動きに強い二段。**指定しなければこれが既定**）、`detect-threshold`（フェードイン・アウト）（scenedetect.com/cli）
- 例の出力: `goldeneye-Scenes.csv` と `goldeneye-Scene-001-01.jpg` のような各場面の始め・中・終わりのコマ（cli）
- v0.7.3（2026-11-08）: `save-images -i 2s --max-images 10` で場面の長さに応じた枚数、`save-edl` の NTSC での時刻のずれ、OTIO の尺、可変フレームレートの最後の場面、などの修正（リリースノート）。EDL・OTIO の書き出しがある
- 入れ方: `pip install --upgrade scenedetect`、GUI のない機械なら `scenedetect-headless`（opencv-python-headless に依存）。Python 3.10 以上。分割には ffmpeg か mkvmerge。Windows のインストーラ・ポータブル ZIP、全部入りの Docker イメージ `ghcr.io/breakthrough/pyscenedetect` もある（download、README）
- BSD 3-Clause

### unsilence（無音を切る・速める）

- 「Console Interface and Library to remove silent parts of a media file」。無音を切るか、無音だけを 6〜8 倍に速める用途を挙げる（README）
- README の例: MIT OCW の講義 9:45 → 7:56（-18.8%）
- `pipx install unsilence`、Python 3.7 以上、ffmpeg 4.2.4 以上。MIT
- 最新リリース 1.0.9 は **2022-11-03**、最終 push 2023-03-28。止まっている

### jumpcutter（元祖）

- carykh の 2019 年ごろの実験。README は「I'm not going to be actively updating this GitHub repo」と書き、商用の jumpcutter.com を案内している
- 「it saves every frame of the video as an image file in a temporary folder. If your video is long, this could take a LOT of space」（README）
- 更新されない repo で、長い動画では一時ファイルが膨らむと作者が書いている。いま選ぶ理由は見当たらない

### ffmpeg の silencedetect（入れ物なしでやる）

- 「This filter logs a message when it detects that the input audio volume is less or equal to a noise tolerance value for a duration greater or equal to the minimum detected noise duration」。`noise`（既定 -60dB）、`duration`（既定 2 秒）、`mono`。例: `ffmpeg -i silence.mp3 -af silencedetect=noise=0.0001 -f null -`（ffmpeg-filters 8.107）
- 出るのは **記録（log）の silence_start / silence_end / silence_duration だけ**。動画を切るのは、その時刻を読んで trim / concat するスクリプトを自分で書く
- silenceremove（8.108）は音声のフィルタで、始め・途中・終わりの無音を取り除く。音声だけを縮めるので、そのまま映像付きの素材に使うと映像と音がずれる（推測。フィルタが音声専用であることからの読み）

## この wiki への含意

- **何を AI に任せられるか**: どれも学習した AI ではなく閾値の規則。PySceneDetect は「画面が大きく変わった所」、silencedetect と unsilence は「音が小さい所」を機械的に見つける（公式）。どこで切るかの提案までで、どれを残すかは決めない
- **何が人の判断として残るか**: 閾値と、見つかった区間のどれを使うか。PySceneDetect の公式の例も、まず `list-scenes save-images` で CSV とコマを見てから分割する順で書いている
- **PySceneDetect の使い道は「詰める」でなく「見る・分ける」**: スライドを映した講演の録画なら、スライドが替わった所が場面の切れ目として出るはず（推測。スライドの替わりは画面全体が変わるので detect-content に掛かる）。その CSV は、切り抜きの候補の区切り、コンタクトシート（[[web-check-spec-ffmpeg-contact-sheet-select-tile-drawtext]]）、映像を理解するモデルに渡す前の下見（[[web-means-critic-gemini-video-understanding]]）に使える。切り抜きの OSS の OpenShorts も、書き起こしと並べて PySceneDetect の場面の切れ目を LLM に渡している（[[web-edit-auto-openshorts-ai-youtube-shorts-generator-supoclip-autoclip]]）
- **無音を詰めるなら auto-editor 一択**（[[web-edit-auto-auto-editor]]）: unsilence・jumpcutter は止まっていて、auto-editor は月 1〜2 回出ていて、エディタへの書き出しまである。silencedetect は「何秒の無音がどこに何回あるか」を測るのに使う。ffmpeg だけで済むので、検査（[[web-check-loudness-ffmpeg-loudnorm-ebur128]] と同じ流れ）に足しやすい
- **[[exp-shortmovie-draft-generator]] との関係**: 2 は Whisper のセグメントの時刻を正にした。silencedetect の無音の区間は、セグメントの切れ目が本当に発話の切れ目か（話の途中で切れていないか）を確かめる別の物差しになる（推測）

## 着手の仕方（未検証。galleria で確かめる）

- **表現できるようになること**: 録画のどこで画面が替わり、どこが黙っているかの一覧（CSV・記録）を、見る前に作る。場面ごとの分割ファイル。効く型: talk（講演・LT の録画の下見）、promo（素材選び）
- **機械**: galleria WSL。GPU 不要
- **入れるもの・費用**: PySceneDetect 0.7.3（`scenedetect-headless`）。ffmpeg は既にある。費用 0、アカウント不要。BSD-3 / LGPL・GPL（ffmpeg の構成による）
- **成熟度**: PySceneDetect は活発（前日にリリース）。unsilence・jumpcutter は止まっているので入れない
- **最小の手順（WSL）**:
  ```bash
  mkdir -p ~/video-tools-trial/scene && cd ~/video-tools-trial/scene
  uv tool install scenedetect-headless   # README は pip。uv tool は推測
  scenedetect version
  # 試験素材: 赤 3 秒 → 青 3 秒 → 緑 3 秒（式は推測）
  ffmpeg -f lavfi -i color=c=red:s=640x360:d=3:r=30 -f lavfi -i color=c=blue:s=640x360:d=3:r=30 \
    -f lavfi -i color=c=green:s=640x360:d=3:r=30 -filter_complex "[0][1][2]concat=n=3:v=1:a=0" -c:v libx264 -pix_fmt yuv420p cuts.mp4
  scenedetect -i cuts.mp4 detect-content list-scenes save-images split-video
  # 無音の区間（auto-editor の試験素材 test.mp4 を流用）
  ffmpeg -hide_banner -i ../ae/test.mp4 -af silencedetect=n=-40dB:d=0.5 -f null - 2>&1 | grep -E "silence_(start|end)"
  ```
- **動いたと言える確かめ方**: `cuts-Scenes.csv` に 3 行（開始 0・3・6 秒あたり）、`cuts-Scene-001.mp4`〜`003.mp4` ができる。silencedetect の記録に `silence_start: 2` → `silence_end: 4` のような組が 5 回並ぶ（2 秒鳴って 2 秒黙る素材なので）。本番は自分の LT の録画で、CSV の切れ目がスライドの替わり目と合っているかを人が数枚見て確かめる
- **所要の見込み（推測）**: 30 分

## Open Questions

- スライドの講演録画で、話者の小窓（カメラ）の動きが detect-content の誤検出を生まないか。`detect-adaptive`（既定）の方がよいか
- 画面収録（スクロール・タイピング）では切れ目が多すぎるはず（推測）。画面収録に使うなら `motion`（auto-editor）の方が向くか
- benchmark のページ（scenedetect.com/benchmarks）は未読。検出器ごとの精度の数字はそこにある
