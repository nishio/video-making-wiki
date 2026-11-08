---
type: source
summary: MIT の OSS の画面収録アプリ OpenScreen（getopenscreen/openscreen、v2.2.2 2026-11-04。元の siddharthvaddem/openscreen は v1.5.0 で archive され、作者の承認で引き継がれた）の README と CLI の docs（2026-10-24 更新）。Windows で動き、CLI で `record`（既定でシステムのカーソルを隠してデータとして録る）→ プロジェクトの JSON にズーム区間・文字を書き足す → `export --auto-zoom` で、窓を開かずに書き出せる。個人・商用とも無料と書いている
video_types: [promo, embed]
url: https://github.com/getopenscreen/openscreen
author: getopenscreen（OpenScreen の引き継ぎ先）／Siddharth Vaddem（元の作者）
published: v2.2.2 は 2026-11-04。CLI の docs は 2026-10-24 更新
retrieved: 2026-11-09
sources:
  - https://github.com/getopenscreen/openscreen/blob/main/README.md
  - https://getopenscreen.com/docs/cli/（Last updated Oct 24, 2026）
  - https://github.com/siddharthvaddem/openscreen/blob/main/README.md（archive 済み、v1.5.0 2026-06-06）
---

# OpenScreen — CLI でズーム区間を書いて書き出せる MIT の収録アプリ

## 何の文献か

- OSS の画面収録・編集アプリの README と CLI の docs。元の作者の README は「OpenScreen is your free, open-source alternative to Screen Studio」「If you don't want to pay $29/month for Screen Studio」と書く。元の repo（star 約 40,000）は v1.5.0（2026-06-06）の後に archive され、「Development moved here with his approval, under the same name and the same MIT license」（引き継ぎ先、star 約 6,700）
- 引き継ぎ先は「OpenScreen is under active development — expect rough edges and occasional breaking changes, including to the `.openscreen` project format and the CLI」と書く
- 道具の作者の文書で、測定は無い

## 書いてあること

### 機能（README）

- ウィンドウか画面全体、マイクとシステム音、カメラの重ね。「Auto or manual zooms with adjustable depth, duration, easing, and pixel-precise position; auto-zoom follows your cursor as you work」。カーソルの大きさ・平滑化・クリックの効果。端末内で作る字幕（オフライン）。背景、モーションブラー、切り詰め、区間ごとの速度、文字・矢印・画像の注釈
- 書き出しは MP4 か GIF、「rendered and encoded on the GPU (Metal on macOS, D3D11 on Windows, Vulkan on Linux) with an automatic CPU fallback」
- 対応言語に日本語がある（UI）
- 元の README: 「100% free for both personal and commercial use」「OpenScreen has no paid tiers」
- Windows の要件: version 1903 以降、Intel 第 8 世代／Ryzen 2000 以降。推奨は Windows 11 と Intel 第 12 世代／Ryzen 4000 以降

### CLI（docs/cli）

- 「OpenScreen's command-line interface is built into the desktop app's own executable」。Windows はインストーラ版の `Openscreen.exe`（`%LOCALAPPDATA%\Programs\Openscreen\` など）。**Microsoft Store 版は場所が更新ごとに変わるので CLI には使えない**
- `record`: 「It drives the same recording hook as the desktop app」。ポインタのデータが取れたときは `<video>.cursor.json`（「cursor-telemetry file that the editable cursor and `--auto-zoom` read」）を書く
  - `--window <title>`（タイトルに含む最初のウィンドウ）、`--display <n>`、`--mic`、`--system-audio`、`--camera`、`--duration <seconds>`、`--project <out.openscreen>`、`--json`（NDJSON）
  - `--cursor <editable-overlay|system>`: 「editable-overlay (default) hides the system pointer and records it as data, so the editor can restyle it. system draws the pointer into the video」
  - Windows: 「Capture goes through the Windows Graphics Capture helper, from Windows 10 build 19041 ... Windows never delivers SIGTERM: use Ctrl+C, stdin `stop`, or `--duration`」。強制終了すると project ファイルは書かれない
- `export`: 「Renders a project to MP4 or GIF with the native compositor the editor uses」。`--quality <medium|good|source>`、`--fps <24|30|60>`、`--auto-zoom`（「Before rendering, add zooms on the recorded clicks, with the same engine as the editor's automatic zooms. Existing zooms are kept, and new ones keep clear of them」）、`--audio <file> --audio-mode <mix|replace>`（TTS のナレーションを差し替えられる）
- **自動化の例（docs の「an automated product demo」）**: `record --window "MyProduct" --mic --duration 20 --project demo.openscreen` → node でプロジェクトの JSON の `editor.zoomRegions` に `{ id, startMs, endMs, depth: 3, focus: { cx: 0.5, cy: 0.4 }, focusMode: "manual", source: "manual" }` を足し、`annotationRegions` に文字を足す → `captions` → `export --auto-zoom`。「depth runs from 1 to 6 (1.25× to 5×; 3 is 1.8×), and cx and cy place the zoom center as fractions of the frame」
- 他の道具で撮った動画も `{"version":2,"media":{"screenVideoPath":...},"editor":{}}` の最小のプロジェクトで書き出せる。「Without cursor telemetry, `--auto-zoom` has nothing to work from」
- 向かない場合（docs の明記）: 画面の無いサーバーで録る、安定した版の API が要る、「CLI MP4 exports are H.264, and the MP4 bitrate is not adjustable」、字幕ファイルが要る（「Captions are burned into the video only」）
- `pack` は project と参照する素材を 1 フォルダにまとめる（CI の成果物向け）。MCP サーバー（`openscreen mcp`）と、PR にデモ動画を付ける skill（openscreen-demo）もある

## この wiki への含意

- **「寄る位置を台本から渡す」がこの道具でできる**。zoomRegions は時刻（ms）・倍率・中心（画面に対する割合）の JSON で、Playwright の台本が記録したクリックの時刻と座標（[[web-means-capture-playwright-screencast]] の clicks.json）からそのまま作れる（推測。座標を画面の割合に直すだけ）。他の道具で撮った MP4 を最小のプロジェクトに入れて書き出せるので、**Playwright で撮った take.mp4 に、OpenScreen の描画のズーム・背景・文字を付ける**組み合わせが成り立つ（推測。未確認）
- **西尾の方式との関係**: 西尾は文字・図を自分の canvas で描く（[[exp-html-capture-pipeline]]）。OpenScreen の annotationRegions の文字はアプリの描画で、日本語の書体・組版を細かく決められるかは分からない。文字の重ねは西尾の方式、ズームと枠は OpenScreen、と役を分けるのが無難（推測）
- **字幕は焼き込みのみ**: 学会の video preview は .srt の字幕ファイルを必須にしている（[[web-promo2-uist-chi-video-guides]]）。OpenScreen の字幕はそこには使えない
- **ライセンスの点で Cap より始めやすい**: MIT で、元の作者が商用も無料と書いている（[[web-means-capture-cap]] は商用に有料のライセンス）。ただし開発中で形式が変わると明記しているので、プロジェクトの JSON を書くスクリプトは版を固定して使う

## 着手の仕方（未検証。galleria で確かめる）

- **表現できるようになること**: 撮った画面録画（OpenScreen で撮っても、Playwright・OBS で撮っても）に、指定した時刻と位置への滑らかなズーム、背景と枠、カーソルの描き直しを、CLI だけで付けて書き出す。効く型: promo、embed
- **機械**: galleria Windows（インストーラ版。Store 版は CLI に使えない）。Electron なので画面のあるセッションが要る（docs）
- **入れるもの・費用**: OpenScreen v2.2.2（GitHub Releases の `Openscreen.Setup.2.2.2-x64.exe`）。費用 0、アカウント不要（README に記述なし）。MIT
- **成熟度**: 引き継ぎ後 v2.x で活発（最終 push 2026-11-08）。project 形式と CLI は変わりうる、と作者が明記
- **最小の手順（PowerShell）**:
  ```powershell
  $os = "$env:LOCALAPPDATA\Programs\Openscreen\Openscreen.exe"
  & $os sources --json
  & $os record --window "Chrome" --duration 15 --project $HOME\video-tools-trial\os\demo.openscreen --json
  # 手でクリックしながら 15 秒
  & $os export $HOME\video-tools-trial\os\demo.openscreen -o $HOME\video-tools-trial\os\auto.mp4 --auto-zoom --fps 30 --json
  ```
  台本から寄る場合は、docs の node の例のとおり `editor.zoomRegions` を書き足してから `export`（`--auto-zoom` なし）
- **動いたと言える確かめ方**: `record` の NDJSON の最後に `done` の event、録画の隣に `*.cursor.json` ができる（できなければ Windows でクリックが録れていない）。`auto.mp4` を 1 秒ごとのコマに切り（`ffmpeg -i auto.mp4 -vf fps=1,scale=480:-1 f%03d.png`）、クリックの時刻のあたりで寄っていれば成功。zoomRegions を手で書いた版は、書いた startMs〜endMs で寄っていれば成功
- **所要の見込み（推測）**: 導入 15 分、自動ズームの確認 30 分、JSON を書く版 1 時間

## Open Questions

- Windows で `cursor.json` にクリックが入るか（macOS は Accessibility の許可が要ると docs が書く。Windows の条件は書かれていない）
- Playwright の CDP 入力のクリックは cursor.json に入らないはず（OS の入力でないため。推測）。入らないなら zoomRegions を台本から書く
- annotationRegions の文字で日本語の書体を選べるか
- 他の道具で撮った VFR の素材を入れたとき、書き出しの fps（`--fps`）でどう扱われるか
