---
type: analysis
summary: 第 3 回サーベイ（2026-11-09）から、2026-11-10 から着手できることを効く順に並べたもの。項目ごとに、何をするか・増える表現手段・型・機械と必要なもの・galleria で打てる手順・動いたと言える確かめ方・所要の見込み・終わりの条件・西尾が決めること・最終的な「動画の作り方の解説動画」のどの部分の材料になるかを書く。手順はすべて未検証（galleria で確かめる）。最後に、その解説動画の型と構成の案と、着手前に決めること
video_types: [promo, talk, embed]
sources:
  - web-check-*.md、web-means-*.md、web-embed-*.md、web-nonscreen-*.md、web-rights-*.md（第 3 回）
  - concepts/expression-means.md、concepts/checks-and-finishing.md
  - exp-html-capture-pipeline.md、exp-sutra-hype-editions.md、exp-galleria-tts-and-singing.md、exp-qualia-video.md
---

# 明日から着手できること（2026-11-10）

西尾の指示: 「サーベイの足りない領域にしっかりサーベイをかけて。明日からすぐ具体的に着手が可能な水準で。」

追加の言葉: 「最終的に「動画の作り方の解説動画」を作るか」（[[origin-2026-11-09]]）。これは成果物の**候補**で、まだ決まっていない。そこで各項目に「解説動画のどの部分の材料になるか」を一言添えた。最後の節は、その解説動画の案。

## 前提

- **手順はすべて未検証（galleria で確かめる）**。CyEC2 では何も入れず、何も動かしていない。コマンドは各ページの「着手の仕方」を要約したもので、全文と推測で補った所はそのページにある。
- galleria の作業場は WSL の `~/video-tools-trial` を想定している。GPU を使う項目は「GPU 要・VRAM の見込み」だけを書いた（lease の仕組みは通す前提）。
- 西尾の動画の書き出し元（`~/sutra-videos`、`~/nishio-showreel` など）は Mac にある。galleria に要るときは Mac から scp で渡す。公開済みの動画はダウンロードしない。
- アカウント・課金・API キーが要る項目は「要」と書き、決めるのは西尾。
- 所要はどれも推測。
- 一覧の背景は [[expression-means]]（手段）と [[checks-and-finishing]]（検査）にある。
- 第 3 回のサーベイ全体のまとめ（足りない領域の判断、経験と文献の食い違い、読めなかったもの）は [[survey-2026-11-round3-summary]]。

## 明日の 1 時間でやるならこれ

**1. 般若心経アゲアゲ版 R3 の閃光を、実フレームで測る。**

理由:
- 公開済みの動画に安全上の疑いがある。第 2 回で境目になりうると分かり（[[design-fundamentals]]）、レビューは R1 しか通っていない（[[exp-sutra-hype-editions]]）。
- 費用 0、アカウント不要、GPU 不要で、1 時間で合否の目処が付く。
- 道具の確かめ（陽性対照）から一度に回せる。

## 一覧（効く順）

| # | 何をするか | 型 | 機械 | 費用・アカウント | 所要（推測） | 第 2 回の次の手 |
|---|---|---|---|---|---|---|
| 1 | 閃光を測る（R3） | promo、embed | gW | 0・不要 | 1〜2 時間 | 次の手 1 |
| 2 | フォントを作品に同梱し、Mac と galleria で同じ絵を出す | any | gW＋Mac | 0・不要 | 1 時間 | （3・4 の前提） |
| 3 | 流しっぱなしの embed を一本（20〜60 秒、一概念） | embed | Mac（既存の方式）、図は gW | 0・不要 | 半日〜1 日 | 次の手 2 |
| 4 | 作品の promo を、実物の収録＋コードで描く重ねで一本 | promo | gW | 0・不要 | 半日〜1 日 | 次の手 3 |
| 5 | 仕上げの検査を一度に回す（音量の 2 パス・コンタクトシート・色） | any | gW | 0・不要 | 1〜2 時間 | — |
| 6 | 台本を正にした字幕（整列・BudouX・ASS の焼き込み・SRT） | talk、embed | gW（GPU） | 0・不要 | 半日 | — |
| 7 | 読み辞書を repo で管理する（AivisSpeech） | talk、embed | gWin | 0・不要 | 30 分〜1 時間 | — |
| 8 | 映像を理解するモデルに批評させる（Gemini の音あり・音なし・音だけ、ローカルの Qwen3-VL） | talk、embed | gW、gWin | Gemini は要キー・費用 | 半日 | — |
| 9 | ACE-Step 1.5 で 60 秒のインストを作る | promo、talk | gW（GPU） | 0・不要 | 1〜2 時間 | — |
| 10 | GSAP＋SVG と three.js を 1 コマずつ撮る | any | gW、gWin（GPU） | 0・不要 | 半日 | — |
| 11 | 公開前の確認表（素材 12 項目と規約の版）と C2PA の試し | any | どこでも、gW | 0・不要 | 1〜1.5 時間 | — |

（gW は galleria の WSL、gWin は galleria の Windows）

## 1. 閃光を測る（般若心経アゲアゲ版 R3）

- **何をするか**: 書き出し元の mp4 を、IRIS（Python 版）と自前の画素ごとの近似の 2 つで測る。
- **増える表現手段**: 拍に合わせて光らせる演出を、公開前に数字で足切りできる。
- **型**: promo（主）、embed（ループ）。
- **機械・必要なもの**:
  - 機械は galleria の WSL。
  - 入れるのは `iris-pse-detection==1.1.2`（MIT、2026-01-22）、numpy、ffmpeg（既存）。
  - GPU 不要、費用 0、アカウント不要。
- **手順（WSL）**。全文は [[web-check-flash-ea-iris]] と [[web-check-flash-ffmpeg-signalstats-photosensitivity]]。
  ```bash
  mkdir -p ~/video-tools-trial/iris && cd ~/video-tools-trial/iris
  uv venv && . .venv/bin/activate && uv pip install iris-pse-detection==1.1.2 numpy
  # 陽性対照: 全画面 5Hz・全画面 2Hz・左 20% だけ 5Hz の合成動画（ffmpeg -f lavfi … geq）を作り、それぞれ iris に通す
  # 本番: Mac から書き出し元を送る（scp ~/sutra-videos/output/<アゲアゲ版>/<動画>.mp4 galleria:~/video-tools-trial/iris/hype.mp4）
  ffprobe -v error -show_entries stream=r_frame_rate,avg_frame_rate,nb_frames hype.mp4   # CFR か確かめる
  iris hype.mp4 -j -o results/ ; echo "exit=$?"
  python3 -I summarize.py results/hype/framedata.csv                                       # 秒ごとの表
  ffmpeg -i hype.mp4 -vf scale=192:108,format=rgb24 -f rawvideo - | python3 -I flashcount.py   # 自前の近似（ITU と WCAG の両方の面積）
  ```
- **動いたと言える確かめ方**:
  - 全画面 5Hz で Fail（`LuminanceFrameResult=3`）が出て、2Hz で PASS か警告が出る。
  - 左 20% の版で、近似の `lum_itu` が約 0.2、`lum_wcag` が約 1.0 になる。
  - `framedata.csv` の行数が nb_frames ±1。
- **終わりの条件**:
  - R3 の区間（R1 の約 64 秒を 128/176 倍すると約 47 秒、という推測）について、次を表にして exp-sutra-hype-editions の Updates に書く。
    - 1 秒に 7 遷移以上の秒があるか。
    - 5 秒続く失敗があるか。
  - 合格なら記録して終わり。不合格なら、直すか（叩きつけの光を弱める・面積を減らす・青の輝度を下げる）、注意書きを付けるかを決める。
- **西尾が決めること**:
  - ITU と WCAG のどちらの面積の基準で合否を言うか。全画面の動画では WCAG が約 9 倍厳しい（[[web-check-flash-peat-harding-fpa]]）。
  - 不合格のとき、公開中の動画をどうするか。
  - Harding の判定まで欲しいなら、hardingtest.com（£30 から、動画を外部に上げる）を使うか。
- **解説動画の材料**: 「検査」の場面の実演になる。
  - ただし閃光の試験動画そのものを画面に出すと、解説動画が閃光を含んでしまう。見せるのは秒ごとの表・グラフと、合成動画の「1 コマの静止画」だけにする。
  - 「BPM を上げた版こそ測る」は、R1 だけのレビューが見落とした、という経験談の形で語れる。

## 2. フォントを作品に同梱し、Mac と galleria で同じ絵を出す

- **何をするか**:
  - OFL の日本語フォントを版を固定して取得し、作品のフォルダに置いて `@font-face` で直接指す。
  - 台本の全字が入っているかを照合する。
- **増える表現手段**:
  - 描く機械を選ばなくなる。Mac の Hiragino 頼みをやめる（[[exp-html-capture-pipeline]]）。
  - 極太の明朝（Noto Serif CJK JP Black、Zen Old Mincho Black）が使える。[[exp-polis-magi-op]] のマティス-EB は個人契約の範囲でしか使えないので、その置き換えになる（[[web-means-font-morisawa-fonts-bizplus-mojimo]]）。
- **型**: any。3・4・6 の前提。
- **機械・必要なもの**: galleria の WSL と Mac。fonttools（uv で一時に）。費用 0、アカウント不要。
- **手順（WSL）**。全文は [[web-means-font-sil-ofl-noto-zen-mincho]] と [[web-means-font-fontconfig-noto-cjk-linux]]。
  ```bash
  mkdir -p ~/video-tools-trial/fonts && cd ~/video-tools-trial/fonts
  curl -LO https://github.com/notofonts/noto-cjk/releases/download/Serif2.003/07_NotoSerifCJKjp.zip && unzip 07_NotoSerifCJKjp.zip -d noto-serif-cjk-jp-2.003
  curl -L -o ZenOldMincho-Black.ttf https://github.com/google/fonts/raw/main/ofl/zenoldmincho/ZenOldMincho-Black.ttf
  sha256sum *.ttf noto-serif-cjk-jp-2.003/*/*.otf > SHA256SUMS
  # fonttools で台本の全字が cmap にあるかを照合 → 試験の HTML を Mac と galleria で 1 コマずつ撮る
  ```
- **動いたと言える確かめ方**:
  - 照合の結果が「missing: none」。
  - `document.fonts.check` が true。
  - 2 台の PNG を並べて、字の位置と太さが揃っている（差分画像がほぼ 0）。
- **終わりの条件**: 3・4 の作品フォルダに `fonts/` と `SHA256SUMS` があり、galleria で撮った静止画が Mac と一致する。
- **西尾が決めること**: どのフォントを標準にするか（ゴシックは Noto Sans JP か BIZ UD、明朝は Noto Serif か Zen）。
- **解説動画の材料**: 「文字」の場面。同じ HTML を 2 台で撮った並べ比べで、豆腐とフォールバックの差がそのまま絵になる。

## 3. 流しっぱなしの embed を一本（第 2 回の次の手 2）

- **何をするか**:
  - 発表の中で話し手が流しっぱなしにする、20〜30 秒（上限 60 秒）の一概念の動画を作る。
  - それに合わせて、話し手が流す前に言う一言と、流している間の台本を作る。
- **増える表現手段**: 一概念を段階的に組み立てて見せる映像と、話し手との分担の組。
- **型**: embed。
- **題材の条件**（[[web-nonscreen-cell-iop-nejm-video-abstract-guides]]、[[web-nonscreen-rsa-animate-turkay-2022-whiteboard]]）:
  - (a) 時間とともに中身が変わる構造がある。抽象的な図形だけの案は伝わらなかった。
  - (b) 既にある図 1 枚から始められる（Figure360 の「図にある要素だけ」）。
  - (c) 何が映るかを一言で言える。
  - 候補は「LLM Wiki の ingest でページが育つ流れ」や「THINKLET の 30 秒の処理の流れ」など。
- **作りの決まり**（文献からの案）:
  - 動画にナレーションも BGM も入れない。話し手が上に乗る版は録音ナレーションを禁止する（VIS 2015、[[web-embed-siggraph-ieeevis-chi-fast-forward]]）。サウンドトラック付きは使うな（Anderson、[[web-embed-ted-anderson-yc-demo-day]]）。
  - 画面の文字は 1 秒 4 字以内。研究の上限は 6 字（[[web-check-ja-toyokura-yamada-2017-subtitle-4-chars]]）。
  - 2 秒以上画面が変わらない間を作らない（Figure360）。
  - どの 1 秒から見ても何の話か分かるようにする。展示の映像では、半分より前に離れるのが普通（[[web-embed-serrell-smithsonian-museum-video]]）。
- **会場での流し方**:
  - 流す前に、話し手が何が映るかを一言言う（Ladner、[[web-embed-ladner-sigaccess-chi-video-in-talks]]）。
  - Keynote の「Start movie on click」を外して自動で再生する。
  - 無音であることは画面か口で伝える。
  - 予備の写しを別の機械か USB に置く（[[web-embed-evangelist-2006-apple-keynote]]）。
  - 3 つの発表ソフトに共通して通る形は、H.264＋AAC の .mp4・1080p。ループを公式に書いているのは Keynote だけ（[[checks-and-finishing]] の仕様表）。
- **機械・必要なもの**:
  - 描画: Mac の既存の canvas の方式（入れるもの無し）。
  - 段階表示の図を道具で作るなら galleria の WSL に `@mermaid-js/mermaid-cli`＋`puppeteer`（Mermaid の step、v12.3.0）か D2 v0.9.0（steps）。SVG なので撮影は `page.screenshot` で、`toDataURL` は使えない（[[web-means-diagram-mermaid]]、[[web-means-diagram-d2]]）。
  - データを動かすなら、既存の `renderFrame(f)` に `d3@7.9.2` の interpolate・ease を足すだけ（[[web-means-diagram-d3-transition-veltman]]）。
  - 費用 0、アカウント不要。
- **手順**（Mac。既存の repo の src を写して使う）:
  ```bash
  node capture.mjs stills 3 10 20          # 山場の静止画
  node capture.mjs video                   # -> out/video_noaudio.mp4
  ffprobe -v error -show_entries format=duration:stream=codec_type,codec_name,width,height -of compact out/video_noaudio.mp4
  ffmpeg -i out/video_noaudio.mp4 -vf freezedetect=n=0.003:d=2 -map 0:v -f null - 2>&1 | grep freeze_start
  ffmpeg -i out/video_noaudio.mp4 -vf "fps=1,scale=480:-1,tile=6x10" -frames:v 1 out/sheet.png
  ```
- **動いたと言える確かめ方**:
  - duration が 20〜60 秒で、音声のストリームが無い。H.264・1920×1080。
  - `freeze_start` が出ない。
  - コンタクトシートのどのマスからでも、何の話か分かる。
  - 1 の閃光の検査を 2 周つないだ版で通す（ループで流すなら）。
  - Keynote で自動で再生する。
- **終わりの条件**:
  - 台本と合わせて 5 回通し、時間内に収まる。
  - 概念を知らない人 1 人に見せて、一文で説明し返せる。
  - 単独で流す版（TTS のナレーションを別トラックに、.srt を別ファイルに、音楽なし）も同じ素材から書き出す（`ffmpeg -i video_noaudio.mp4 -i narration.wav -c:v copy -c:a aac -shortest`）。
- **西尾が決めること**: 題材、流している間に話すか黙るか、どの発表で流すか。
- **解説動画の材料**:
  - 「embed」の場面そのものになる。この動画を解説動画の中で流しっぱなしで流し、その前後で「流す前に一言」を実演すれば、手段とその説明が一致する。
  - 題材を「LLM Wiki の ingest」にすれば、この wiki 自体が育つ様子が映る。

## 4. 作品の promo を、実物の収録＋コードで描く重ねで一本（第 2 回の次の手 3）

- **何をするか**:
  - Playwright で作品の Web 画面を台本どおりに撮る。クリックの時刻と座標は `clicks.json` に残す。
  - 重ねる文字・強調・図は、西尾の canvas の方式で同じ時刻に描き、透明 PNG で重ねる。
  - 広める 30 秒版と、理解させる版を分ける（[[work-promotion-video]]）。
- **増える表現手段**:
  - 実物の画面に、カーソル・クリックの印・章見出し・寄りを付けた素材。
  - 作品が変わったら、同じ台本で撮り直せる。
- **型**: promo（主）、embed。
- **機械・必要なもの**:
  - galleria の WSL に `playwright@1.65.0` と Chromium（`npx playwright install --with-deps chromium`。sudo が要る）。
  - 日本語の画面なら日本語フォント（2）。
  - 寄りを OpenScreen で作るなら galleria の Windows に v2.2.2（MIT。Store 版は CLI に使えない）。
  - 費用 0、アカウント不要。
- **手順（WSL）**。`record.mjs` の全文は [[web-means-capture-playwright-screencast]]。
  ```bash
  mkdir -p ~/video-tools-trial/pw-capture/out && cd ~/video-tools-trial/pw-capture
  npm init -y && npm i -D playwright@1.65.0 && npx playwright install --with-deps chromium
  node record.mjs <作品の URL>          # page.screencast.start({fps:60}) + showActions + showChapter、clicks.json を書く
  ffmpeg -i out/take.webm -vf fps=30 -c:v libx264 -crf 18 -pix_fmt yuv420p -movflags +faststart out/take.mp4
  # 寄り: clicks.json から式を作る（ffmpeg の zoompan は揺れるので、元のコマから補間付きで切り出す方式か OpenScreen の zoomRegions）
  # 重ね: capture.mjs で透明 PNG の連番を出し、ffmpeg の 2 つ目の入力にして overlay（推測）
  ```
  - YAML で書くなら `shot-scraper video storyboard.yml --fps 60 --mp4`（1.10 以降）。
- **動いたと言える確かめ方**:
  - ffprobe で 1920×1080 になっていて、`avg_frame_rate` が 25 を超えているかを記録する。
  - clicks.json の t の時刻で 1 コマ切り出すと、クリックの印がその座標に出ている。
  - 重ねた文字が、クリックと同じコマで出ている。
- **終わりの条件**:
  - 30 秒版が 1 本ある。
  - 「時間と因果を偽っていない」ことを確かめた。読み込みの待ちを詰めていないか、詰めたなら字幕で言うか（[[web-promo2-gemini-nikola-staged-demos]]、[[exp-thinklet-reading-demo-video]]）。
  - 5 の検査を通した。
- **西尾が決めること**:
  - どの作品のどの画面を撮るか。未公開の内容や個人情報が映らないか。
  - 寄りに有料の Cap を使うか、MIT の OpenScreen にするか。Cap は、雇い主の製品のデモも「商用」に入ると書いている（[[web-means-capture-cap]]）。
- **解説動画の材料**: 「実物の収録」の場面。解説動画の題材を、この wiki のページや作った道具の画面にすれば、Playwright で撮った画面そのものが「台本で撮る」の説明になる。

## 5. 仕上げの検査を一度に回す（音量の 2 パス・コンタクトシート・色）

- **何をするか**:
  - 既存の動画（英語版など）の音量を測る。
  - ffmpeg-normalize で、線形の 2 パスに揃え直す。
  - 同じ動画からコンタクトシートを作り、色の札と範囲を点検する。
- **増える表現手段**:
  - 音量を数字で決める。声と BGM の差を測る。
  - 全編を 1 枚で見渡す（人にも、8 の批評役にも渡せる）。
- **型**: any。
- **機械・必要なもの**: galleria の WSL、ffmpeg（既存）、`uvx ffmpeg-normalize`（MIT、1.43.0）、`uvx --from daltonlens daltonlens-python`（任意）。費用 0、アカウント不要。
- **手順（WSL）**。全文は [[web-check-loudness-ffmpeg-loudnorm-ebur128]]、[[web-check-loudness-ffmpeg-normalize]]、[[web-check-spec-ffmpeg-contact-sheet-select-tile-drawtext]]、[[web-check-color-ffmpeg-signalstats-limiter-ebu-r103]]。
  ```bash
  ffmpeg -nostats -i in.mp4 -filter_complex ebur128=peak=true -f null -          # 今の I・LRA・TP
  uvx ffmpeg-normalize in.mp4 -t -16 -tp -1.5 --keep-loudness-range-target --auto-lower-loudness-target \
      -c:a aac -b:a 192k -ar 48000 -o out.mp4 -p                                  # stats の normalization_type を見る
  # ステム（voice.wav、bgm.wav）を別々に ebur128 で測り、声と BGM の差を出す
  ffmpeg -i out.mp4 -vf "drawtext=fontfile=<Noto Sans JP>:text='%{pts\:hms} #%{n}':x=8:y=8:fontsize=28:fontcolor=white:box=1,fps=1,scale=384:-2,tile=6x5" -fps_mode passthrough sheet_%02d.png
  ffprobe -v error -select_streams v -show_entries stream=color_space,color_primaries,color_transfer,color_range out.mp4
  ```
- **動いたと言える確かめ方**:
  - normalization_type が linear。ebur128 の I と TP が目標どおり。sample_rate が 48000。
  - シートの左上が `00:00:00.000 #0` で、60fps なら 2 マス目が #60 前後。
  - 札が bt709。
- **終わりの条件**:
  - この一連を 1 本のスクリプト（`check.sh in.mp4`）にまとめる。以後の作品の書き出しで毎回回し、結果をテキストで残す。
  - [[exp-html-capture-pipeline]] の 1 パスの `loudnorm` を、このスクリプトに置き換える。
- **西尾が決めること**:
  - 目標を −16 にするか −14 にするか（[[narration-bgm-sound]]）。
  - 声と BGM の差を 10 LU 以上にするか（Torcoli）。
- **解説動画の材料**:
  - 「仕上げ」の場面。コンタクトシートはそれ自体が絵になる。
  - 1 パスでは黙って dynamic になる、は「数字で確かめないと分からない落とし穴」の例として語れる。
  - 解説動画自身のコンタクトシートを、解説動画の中に出せる。

## 6. 台本を正にした字幕（整列・BudouX・ASS の焼き込み・SRT）

- **何をするか**:
  - TTS の音声と台本から、台本どおりの文字で時刻付きの字幕を作る。
  - BudouX で文節に分けて改行し、ASS で焼き込む。
  - 同じ正本から、YouTube 用の SRT・VTT を出す。
- **増える表現手段**: 字幕を、台本の書き換えから自動で作り直せる。配信先に字幕ファイルも渡せる。
- **型**: talk、embed。
- **機械・必要なもの**:
  - galleria の WSL（GPU）。整列には `stable-ts` 2.19.1 か Qwen3-ForcedAligner-0.6B（Apache-2.0）、改行には `budoux` 0.10.3、ffmpeg（libass）、2 のフォント。
  - RTX 5080 には CUDA 12.8 版の PyTorch が要る見込み（推測）。GPU 要、VRAM の見込みは数 GB（推測）。
  - 費用 0。
- **手順（WSL）**。全文は [[web-check-subs-whisperx-stable-ts-faster-whisper]]、[[web-check-subs-qwen3-forcedaligner-mfa-reazonspeech]]、[[web-check-subs-budoux]]、[[web-check-subs-ffmpeg-libass-youtube-caption-files]]。
  - stable-ts の `model.align(audio, script_text, language='ja', original_split=True)` で SRT を出す。
  - BudouX で 1 行 13 字に詰め、ASS（`WrapStyle: 2`、`\N`）に変換する。
  - `ffmpeg -i v.mp4 -vf "ass=subs.ass:fontsdir=fonts" out.mp4` で焼き込む。
  - 比べるなら、VOICEVOX の音声は正解の時刻が取れるので、行の開始時刻の誤差の中央値を、stable-ts・Qwen3-ForcedAligner・WhisperX・MFA で並べる。
- **動いたと言える確かめ方**:
  - SRT の文字が台本と一字一句同じ。
  - 焼き込んだ静止画に豆腐が無く、2 行が文節で割れている。
  - 行の開始時刻の誤差が 100ms 以内（目安。担当の案）。
- **終わりの条件**: 3 か 4 の作品で、字幕の文字と時刻を手で直さずに済んだ。
- **西尾が決めること**: YouTube に字幕ファイルを上げるか、焼き込みだけにするか。
- **解説動画の材料**: 解説動画自身の字幕を、この手順で作る。「字幕」の場面では、台本・音声・整列の結果を並べて見せられる。

## 7. 読み辞書を repo で管理する（AivisSpeech）

- **何をするか**:
  - 既に入っている AivisSpeech Engine 1.2.0 で、読みを直したい語を辞書に登録する。
  - `GET /user_dict` を `user_dict.json` に書き出して、repo に置く。
  - 合成のスクリプトに `POST /import_user_dict?override=true` を足す。
- **増える表現手段**: 読み違いの直しを、台本と一緒に版管理できる。流しっぱなしの embed では、読み違いを話し手がその場で補えない。
- **型**: talk、embed。
- **機械・必要なもの**: galleria の Windows（既存のエンジン）。入れるもの無し、費用 0。
- **手順（PowerShell）**: [[web-means-voice-voicevox-aivisspeech-user-dictionary]] の手順どおり。
- **動いたと言える確かめ方**:
  - 登録の前と後で、`audio_query` のモーラ列が変わる。
  - 再起動しても辞書が残る。
  - [[exp-qualia-video]] で聞き違えた所（`こえつき`／`こえしつ`）を、人が聴いて直ったと判定する。
- **注意**: AivisSpeech は、モーラの pitch と長さを無視する。複合語・英単語では辞書が効かないことがある。アクセントまで直すなら VOICEVOX の AquesTalk 風記法か、Google の yomigana（要アカウント、[[web-means-voice-google-azure-openai-elevenlabs-tts]]）。
- **終わりの条件**:
  - 辞書と、その hash が作品の manifest にある。
  - 三層の運用（台本の narration 欄 → 辞書 → 区間の上書き）のどこで直すかを、台本の決まりとして書いた。
- **西尾が決めること**: どの語を辞書に入れ、どの語を台本の書き換えで直すか。
- **解説動画の材料**: 「声」の場面。直す前と後の読み上げを並べて聞かせる。

## 8. 映像を理解するモデルに批評させる

- **何をするか**:
  - (a) Gemini に、同じ下書きを 3 本の形で見せる。音あり（そのまま）、音なし（`ffmpeg -an`）、音だけ（`-vn`）。
  - (b) ローカルの Qwen3-VL-8B に、5 のコンタクトシートを見せる。
  - (c) 過去に人が指摘した誤りの種類ごとに問いを作り、再現率を測る。誤りの種類は「268群って何？」（Gyazo）、「飾りが多すぎる」（qualia v3）、字幕と読み上げの食い違い、1 秒を超えて止まる所。
- **増える表現手段**: 通しで見て聞く批評役。第 2 回の「モデルは聞けない・通しで見られない」への手当てになる（[[after-opus55]]）。
- **型**: talk（主）、embed（音なし版で要旨を言い直させる）。
- **機械・必要なもの**:
  - (a) は galleria の WSL に `google-genai`。**要: API キー・費用**。1 分の動画で 1 回 1〜3 セント程度（担当の見積もり）。無料枠に入れた動画は人が読むことがあるので、未公開の作品は有料枠でだけ入れる（[[web-means-critic-gemini-video-understanding]]）。
  - (b) は galleria の Windows に llama.cpp（CUDA 版）、Qwen3-VL-8B の Q8_0（8.71GB）と mmproj（1.16GB）。Apache-2.0、費用 0。GPU 要、VRAM 約 10GB（[[web-means-critic-qwen3-vl-open-vlms]]）。
- **手順**:
  - (a) モデル `gemini-3.8-flash`、fps 2 で、「狙いを一文で」「分かりにくい箇所を MM:SS 付きで」と聞く。
  - (b) `llama-mtmd-cli -m <gguf> --mmproj <mmproj> --image sheet.png -ngl 99 -p "…"` を回す。
- **聞き方**: 点数ではなく、1 回に 1 種類の誤りを、時刻付きで聞く。2〜3 回回して、共通の指摘だけを残す（[[web-means-critic-video-bench-spotlight]]）。
- **動いたと言える確かめ方**:
  - 3 本の一文の要旨を、台本の狙いと並べた表ができる。
  - 数字を 1 つ仕込んだ版で、モデルがその時刻を指摘できる。
  - Gyazo の版で、人の指摘と同じ時刻・同じ種類の指摘がいくつ出るか（再現率）と、直した版での誤検出の数を数える。
- **終わりの条件**:
  - 何を批評役に任せ、何を機械の検査（[[checks-and-finishing]]）と人に残すかを決められる程度の数字が出る。
  - 研究の予想は「同期・停止・動きは任せられない」で、これを確かめる（[[web-means-critic-omni-judge-audiojudge]]）。
- **西尾が決めること**: Gemini の API キーと有料枠を作るか。どの作品を外部のモデルに入れてよいか。
- **解説動画の材料**: 「批評」の場面。解説動画の下書きそのものを批評役に見せ、時刻付きの指摘と、それを人がどう扱ったかを見せる。「モデルが言えた要旨は、人に伝わることの代わりにならない」（[[web-means-critic-edupanel-paper2video]]）も、ここで語れる。

## 9. ACE-Step 1.5 で 60 秒のインストを作る

- **何をするか**: 尺と BPM を指定して、歌の無い BGM を手元で作る。
- **増える表現手段**: 権利の確かなオリジナルの曲。numpy の合成（[[exp-html-capture-pipeline]]）より音楽らしい曲になる。
- **型**: promo（主）、talk（声の下に置く）。embed は BGM を入れない（3）。
- **機械・必要なもの**:
  - galleria の WSL。GPU 要、VRAM の見込みは 12〜16GB の帯（公式の表で LM 1.7B 推奨の段）。
  - 重みは MIT、生成物の商用可。費用 0、アカウント不要（[[web-means-sound-ace-step-yue2-diffrhythm]]）。
- **手順（WSL）**:
  ```bash
  cd ~/video-tools-trial && git clone https://github.com/ACE-Step/ACE-Step-1.5.git && cd ACE-Step-1.5 && uv sync && uv run acestep   # Gradio :7860
  ```
  - RTX 5080 と PyTorch の CUDA 版が合うかは未確認。
- **動いたと言える確かめ方**:
  - ffprobe で、長さが指定の ±1 秒以内。
  - ebur128 で無音でない。
  - 歌が入っていないことを耳で確かめる。
- **終わりの条件**:
  - 1 本を 3 か 4 の作品の BGM に使い、5 の検査を通した。
  - 生成の条件（モデルの版・seed・プロンプト）を、素材の台帳に記録した。
- **西尾が決めること**: 生成した曲を公開する動画に使うか。AI の生成物としての開示をどうするか（下の「権利と開示」）。
- **解説動画の材料**: 解説動画自身の BGM にし、「音」の場面で、生成の条件と台帳を見せる。

## 10. GSAP＋SVG と three.js を 1 コマずつ撮る

- **何をするか**:
  - (a) GSAP の paused timeline を `tl.seek(f/FPS)` で止め、page.screenshot で撮る。
  - (b) three.js の `render(t)` を、galleria の Windows の Chrome で GPU を使って撮る。
- **増える表現手段**:
  - (a) 文字ごとの出現、線を描く、形の変形。SplitText・DrawSVG・MorphSVG が無料になった。
  - (b) 3D の場面、GPU で描く粒子。粒子系の「1 分に約 10 分」が速くなるかもしれない（推測）。
- **型**: any（3D は流行の作品で promo の側に偏っていた）。
- **機械・必要なもの**:
  - (a) galleria の WSL に `gsap@3.15.1` と `puppeteer`。
  - (b) galleria の Windows に `three@0.187.0` と `puppeteer-core`。GPU 要。
  - 費用 0、アカウント不要。GSAP は無料・商用可だが、OSS ではない独自の許諾（[[web-means-3d-gsap-svg-seek]]）。
- **手順**: [[web-means-3d-gsap-svg-seek]]、[[web-means-3d-threejs-headless-webgl]]。
  - (b) は `--use-gl=angle` で起動し、最初に `UNMASKED_RENDERER_WEBGL` をログに出す。
- **動いたと言える確かめ方**:
  - (a) 同じ f を順番を変えて 2 回撮り、`cmp` で一致する。
  - (b) ログに "NVIDIA" か "RTX 5080" が出る。PNG が黒くない。4 秒・120 コマの mp4 ができる。
- **終わりの条件**: どちらかを 3 か 4 の 1 場面に使った。
- **西尾が決めること**: GSAP の条文を良しとするか。条文に動画への書き出しの明記は無い。
- **解説動画の材料**: 「道具」の場面。同じ場面を canvas・SVG（GSAP）・three.js で描いて並べ、撮り方の違い（`toDataURL` か `page.screenshot` か）を見せる。

## 11. 公開前の確認表と C2PA（権利と開示の下ごしらえ）

- **何をするか**:
  - (a) [[exp-nishio-showreel]] の MANIFEST に、素材の確認 12 項目と「規約を読んだ日・版」の欄を足す（[[web-rights-cc-ofl-asset-license-checklist]]）。既存の作品 1 本で埋めてみる。
  - (b) c2patool で mp4 に C2PA を付けて読み、再エンコードで残るかを測る（[[web-rights-c2pa-c2patool-content-credentials]]）。
- **増える表現手段**: 機械が読める AI の開示。素材と規約の版の台帳。台帳は Content ID の申し立てへの異議の根拠になる（[[web-means-sound-pixabay-youtube-audio-library-freesound]]）。
- **型**: any。
- **機械・必要なもの**:
  - (a) はどこでもでき、道具も要らない。
  - (b) は galleria の WSL に c2patool v0.28.6 の Linux 版。費用 0、アカウント不要。同梱の証明書は試験用で、信頼リストに無い。
- **手順**: (b) は `c2patool in.mp4 -m manifest.json -o signed.mp4`（`digitalSourceType` を指定）→ `c2patool signed.mp4` で読む → ffmpeg で再エンコードした版と `-c copy` の版を作る → もう一度読む。
- **動いたと言える確かめ方**:
  - (a) 全項目が埋まるか、「不明」と明示される。
  - (b) JSON に `c2pa.created` と指定した digitalSourceType が出る。再エンコード後にマニフェストが消えるか壊れるかを記録する。
- **所要（推測）**: (a) 30 分、(b) 30〜60 分。
- **西尾が決めること**: 下の一覧。
- **解説動画の材料**: 結びの「出す前に」の場面。解説動画自身の MANIFEST（使ったモデル・声・BGM の条件）を画面に出せば、CLAUDE.md の「動画ではモデル名を明示する」の実演にもなる。

## 権利と開示: 着手の前に西尾が決めること

法律の助言ではなく、条文と公式の記述を並べた結果（rights 担当、2026-11-09 時点）。

**開示**:
- 合成音声（AivisSpeech・VOICEVOX）のナレーションを、YouTube で「AI use = Yes」にするか。YouTube が開示不要の例に挙げているのは「自分の声の複製」だけ（[[web-rights-youtube-genai-disclosure]]）。
- Instagram・Facebook のリールに TTS の動画を出すときに、AI info を付けるか。Meta は「リアルな AI の声で語るリール」を、ラベルが要る例に挙げる。TikTok は、汎用の TTS ナレーションを開示不要と明記している。扱いが逆（[[web-rights-tiktok-meta-aigc-labels]]）。
- VOICEVOX の歌声の曲を、AI 生成の音楽として開示するか。
- 画面・説明欄に焼き込む、モデル名・声の名前の定型文。
- AI が書いたコードで描くモーションを名指しした規則は、どの配信先にも無い。YouTube は台本・インフォグラフィックの生成支援と字幕を開示不要としている。西尾の方式は対象外と読むのが自然（担当の読み）。

**C2PA**:
- 自分の動画に C2PA を付けるか。付けるなら digitalSourceType をどれにするか。信頼リストに載る証明書に費用をかけるか。
- YouTube は C2PA を含む動画に自動で AI ラベルを付け、作り手はそれを外せない。生成クリップ（Veo・Kling）の来歴を残すか、消えるに任せるか。
- YouTube に限定公開で上げて、出方を確かめるか（外に出る行為）。

**音楽**:
- BGM の基本方針。自作（ACE-Step・numpy）、PD の曲を自分で鳴らす、素材サイト、既存曲のどれにするか。確認が少ないのは、自作と、PD を自分で鳴らすこと（[[web-rights-public-domain-music-imslp-musopen]]）。
- 既存曲について:
  - 包括契約が許すのは作詞・作曲の利用だけで、原盤は別に許諾が要る。
  - 替え歌は作詞者・作曲者の意向の確認が要る。
  - 宣伝の動画は、広告目的複製の手続きが要る。
  - X は、JASRAC・NexTone の UGC の一覧に無い（[[web-rights-jasrac-nextone-ugc-music]]）。
  - 「残酷な般若心経のテーゼ」の替え歌は、確認を取ったか・取るか（[[exp-sutra-songs-on-music]]）。
- 自分の動画を Content ID で守るつもりがあるか。素材集の多くは、Content ID への登録を禁じている。

**用途の禁止**:
- 般若心経・Polis の系列で、政治・宗教の用途を禁じる素材と声を避けるか。対象は OpenTracks（旧 DOVA-SYNDROME）と、AivisSpeech の ACML の声（[[web-rights-cc-ofl-asset-license-checklist]]、[[web-means-sound-soundeffect-lab-maoudamashii-opentracks]]）。

**様式**:
- アニメ OP のような様式を借りるとき、どこまで写すか。作風はアイデアで保護されないが、特定の作品の創作的表現が直接感じ取れれば侵害になりうる（文化庁 2024、[[web-rights-bunkacho-ai-copyright-style]]）。
- 書体のマティス-EB は、mojimo の個人契約の範囲だけで使える（[[web-means-font-morisawa-fonts-bizplus-mojimo]]）。

**名義**:
- 個人と会社のどちらの名義で出すか。次のどれも、名義で使えるかが変わる。
  - Remotion の Company License（[[web-remotion]]）
  - Cap の商用の定義
  - ElevenLabs の個人プラン
  - Live2D の売上の境
  - Fish の年商の境

**運用**:
- 素材の規約を読んだ日・版を、どう残すか（手元に保存するか、Internet Archive か）。
- 実在の人・場所のリアルな生成カットを作るか。作るなら、どの配信先でも要ラベル。EU AI 規則 50 条も関わる（[[web-rights-x-linkedin-niconico-eu-ai-act]]）。

## 「動画の作り方の解説動画」（候補。決まったことではない）

西尾の言葉: 「最終的に「動画の作り方の解説動画」を作るか」。以下は案で、題材・尺・相手・出す場所は決まっていない。

### 型の候補

- **主は talk**。作り方は手順と判断の理由が中身なので、止めて見返せる解説プレゼン風が合う。
  - 尺の見積もりは、6〜7 モーラ／秒（[[web-check-ja-speech-rate-mora]]）。
  - 台本の骨格は「動機 → 仕組み → 結び」（[[talk]]）。
- **広める版と理解させる版を分ける**（第 2 回、[[work-promotion-video]]）。
  - promo の版: 30〜60 秒。作った手段の見せ場を拍に乗せて並べる。
  - talk の版: 理解させる本体。
- **embed の版**: 発表の中で流す 20〜60 秒。「流しっぱなしの embed はこう作る」を、その作りのまま流す（3）。
- 三つを同じ素材から書き出せば、それ自体が「三つの型は別物」（[[three-video-types]]）の実演になる。

### 自己言及の並べ方（手段で作った場面が、その手段の説明になる）

上の各項目の「解説動画の材料」を工程順に並べると、解説動画の各場面を、その場面で説明する手段で作れる。

| 場面 | 作る手段 | 見せるもの | 項目 |
|---|---|---|---|
| 工程の全体図 | D2・Mermaid の段階表示 | 工程が一つずつ組み上がる図 | 3 |
| 台本と声 | AivisSpeech＋辞書 | 読み違いの直す前と後 | 7 |
| 文字 | 同梱したフォント | 2 台で同じ絵になる比較 | 2 |
| 図と動き | canvas・GSAP・three.js | 同じ場面を 3 つの描き方で | 10 |
| 実物 | Playwright の収録 | この wiki と道具の画面を台本で撮ったもの | 4 |
| 音 | ACE-Step | この動画自身の BGM と台帳 | 9 |
| 字幕 | 整列＋BudouX＋ASS | この動画自身の字幕ができる過程 | 6 |
| 検査 | IRIS・ebur128・コンタクトシート | この動画自身の検査結果（閃光の試験動画は出さず、表とグラフだけ） | 1、5 |
| 批評 | Gemini・Qwen3-VL | この動画の下書きへの時刻付きの指摘と、人の判断 | 8 |
| 型の違い | 同じ素材から 3 つの版 | promo・embed・talk の版を並べる | 3、4 |
| 出す前に | MANIFEST・C2PA | この動画自身の使ったモデル・声・BGM と開示 | 11 |

### 構成案の候補

- **案 A: 工程順「1 本の動画ができるまで」**（talk、5〜7 分の見込み）
  - 冒頭 30 秒で、完成した promo の版を見せてから問いを置く。「これはどう作られたか」。
  - 上の表の順に、各場面 30〜45 秒。
  - 結びで、人の一言が合格条件だったこと（[[experience-lessons-2026-11]]）と、機械と批評役に任せられないもの（同期・停止・閃光・伝わるか）を言う。
  - 利点: 手段の網羅。
  - 欠点: 長く、手段の一覧になりやすい（[[exp-gyazo-resumption-video]] の「主役を決める」と逆向き）。
- **案 B: 一つの題材を三つの型に作り分ける**（talk、3〜4 分＋promo 30 秒＋embed 30 秒）
  - 同じ概念（例えば「LLM Wiki の ingest」）を promo・embed・talk の 3 つの版で作り、作り分けの判断を説明する。
    - 時計は、拍か声か、話し手が乗るか。
    - 音は、無音か BGM か。
    - 文字の速さ。
  - 手段は、作り分けに要るものだけを出す（収録・図・声・字幕・検査）。
  - 利点: 西尾の起点の問い「それぞれ別だよな感」（[[origin-2026-11-09]]）に直接答える。
  - 欠点: 手段の幅（3D・音楽生成・批評役）は出にくい。
- どちらの案でも、Opus 5.5 期の作り方の記録（[[after-opus55]]、[[exp-timeline-2026]]）の扱いを決める必要がある。CLAUDE.md の「動画ではモデル名を明示する」に従い、使ったモデル名を画面に出す。

### 着手の前に西尾が決めること

- **誰に見せるか**: 未踏ジュニアの文脈（安川さんとの話）か、LLM Wiki の勉強会か、一般か。これで前提の知識と語彙が決まる。
- **尺と型**: 案 A か案 B か。talk 本体の尺。promo・embed の版を作るか。
- **どこに出すか**: YouTube（通常か Shorts か）、X、発表の中で流すか。仕様は [[checks-and-finishing]] の表にある。
- **声**: AivisSpeech などの TTS か、西尾本人の声（録音か、声の複製か。[[web-means-voice-elevenlabs-google-openai-voice-clone-consent]]）か。
- **AI の関与の開示**: 台本・声・BGM・コードのどこを AI がやったかを、どこまで書くか（下の「権利と開示」）。
- **題材の公開範囲**: 画面に映す wiki・作品・道具に、未公開の内容や第三者の情報が無いか。この wiki は private repo（CLAUDE.md の「置かないもの」）。

## Open Questions

- 1〜10 の所要は、すべて推測。galleria の GPU（lease）の空きで、6・8・9・10 は前後する。
- 3 と 4 を galleria で描くなら、puppeteer-core と Chrome が galleria の WSL にあるかを先に確かめる（2 と合わせて）。
- 解説動画の案 A と案 B は、どちらも西尾の経験の「主役を決めて尺を割く」（[[exp-gyazo-resumption-video]]）とどう両立するかが未解決。
