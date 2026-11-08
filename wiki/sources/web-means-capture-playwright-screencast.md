---
type: source
summary: Playwright の公式ドキュメントとリリースノート（v1.59〜v1.65、2026-04〜11）。ブラウザ内の操作を台本どおりに動かして録画する API が、recordVideo（コンテキスト全体）に加えて page.screencast（開始・停止・章の表示・操作の注釈・フレームの受け取り）になり、v1.61 でカーソルの描画、v1.64 で fps 指定（既定 25）と VP9 化が入った。「録画にカーソルが映らない」は 2020 年からの Issue で、2026-07 に組み込みの注釈で閉じられた。shot-scraper 1.10 の `video` コマンドはこれを YAML の台本で包む
video_types: [promo, embed]
url: https://playwright.dev/docs/videos
author: Microsoft（Playwright チーム）／Simon Willison（shot-scraper）／Conner K. Ward（screenstudio-alt の設計文書、比較のため）
published: 2026-11-05（Playwright v1.65.0 のリリース）／shot-scraper 1.10 は 2026-06-30
retrieved: 2026-11-09
sources:
  - https://github.com/microsoft/playwright/blob/main/docs/src/videos.md（docs の原稿。main を取得）
  - https://github.com/microsoft/playwright/blob/main/docs/src/api/class-screencast.md
  - https://github.com/microsoft/playwright/blob/main/docs/src/api/params.md（context-option-recordvideo の節）
  - https://github.com/microsoft/playwright/blob/main/docs/src/release-notes-js.md（Version 1.59・1.61・1.64 の節）
  - https://github.com/microsoft/playwright/issues/1374（「[Feature] Mouse helper」2020-03-13〜）
  - https://github.com/simonw/shot-scraper/blob/main/docs/video.md と GitHub Releases 1.10（2026-06-30）
  - https://github.com/connerkward/screenstudio-alt-skill/blob/main/docs/ARCHITECTURE.md（recordVideo の可変フレームレートについての記述）
---

# Playwright の録画（recordVideo と page.screencast）

## 何の文献か

- **Playwright の公式ドキュメントの原稿とリリースノート**（microsoft/playwright の main、2026-11-09 取得）。道具の作者による説明で、画質などの測定は無い。最新リリースは v1.65.0（2026-11-05）。Python 版は v1.64.1（2026-10-22）。main の docs には未リリースの v1.66 の項目も混ざっているので、版を確かめて使う
- **GitHub Issue #1374**: 録画やスクリーンショットにマウスの位置を出してほしい、という 2020-03-13 からの要望。利用者のコメントと、2026-07-16 の開発者（yury-s）の回答を読んだ
- **shot-scraper の docs/video.md**: Playwright を包む CLI（Simon Willison）。`video` コマンドは 1.10（2026-06-30）で入った。既存ページ [[web-promo2-vhs-shot-scraper-demos-as-code]] はスクリーンショットの撮り直しまでで、動画は扱っていない
- **screenstudio-alt の ARCHITECTURE.md**: 個人の OSS。recordVideo を使わない理由を書いている（比較のため 1 段落だけ使う）

## 書いてあること

### 2 つの録画の入口

- **recordVideo（コンテキストの option）**: 「Videos are saved upon browser context closure」。`browser.newContext({ recordVideo: { dir: 'videos/' } })` で、そのコンテキストの全ページを録る。閉じるまでファイルは出来ない（videos.md）
- **大きさの既定に注意**: 「The video size defaults to the viewport size scaled down to fit 800x800」。viewport を指定しないと 800×450。「The video of the viewport is placed in the top-left corner of the output video, scaled down to fit if necessary. You may need to set the viewport size to match your desired video size」（videos.md、params.md）。1920×1080 で撮るなら viewport と size の両方に 1920×1080 を書く
- **page.screencast（v1.59、2026-04-01）**: 「record video with precise start/stop control, as an alternative to the recordVideo option」。`page.screencast.start({ path: 'video.webm' })` 〜 `stop()`。`onFrame` を渡すと JPEG のフレームを受け取れ、`path` と併用できる。v1.61 から `onFrame` に「when the frame was presented by the browser」の `timestamp`（Unix エポックのミリ秒）が付く（class-screencast.md、release-notes v1.61）
- **重ねる表示**: `showChapter(title, {description, duration})` は「centered on the page with a blurred backdrop. Useful for narrating video recordings」、既定 2000ms。`showOverlay(html)` は任意の HTML を重ねる（class-screencast.md）。リリースノートはこれを「Agentic video receipts」（エージェントが作業の証拠として動画を残す）の用途として紹介している

### カーソルと操作の注釈

- Issue #1374（2020-03-13）: 「one would see where the mouse is ... and where it clicks」。2021 年に一度閉じられたが再開。利用者は Puppeteer 由来の mouse-helper（`addInitScript` で注入）や npm の `mouse-helper` で代用していた。2026-02 のコメントは「programmatically create videos for educational purposes using playwright.. mouse MUST be visible」と書く
- 2026-07-16 の開発者の回答: 「Playwright now renders action annotations natively ... draws a cursor that animates between action points — in headed mode and in recorded videos」
- `showActions`（v1.59）: 操作した要素を囲み、操作名（例: click）を字幕のように出す。`position`（6 か所）、`duration`（既定 500ms）。`cursor`（v1.61）は `"pointer"`（既定）で「renders a mouse pointer that animates from the previous action point to the next one」、`"none"` で消す。`style`（v1.64）は `point`（クリック点の印）・`highlight`（要素の枠）・`title`（操作名）を CSS で書く。`point` と `highlight` は「Not shown when omitted」（class-screencast.md）
- v1.64（2026-10-07）: 「The cursor stays visible at the last action point, survives navigations and travels along a natural, eased path」
- recordVideo の側にも同じ `showActions` がある（JS のみ。Python 等の params は dir・size・fps だけ）（params.md）

### フレームレートと符号化（v1.64）

- `fps` を recordVideo・`TestOptions.video`・`Screencast.start` に追加。**既定は 25**。「Higher frame rates make animations and scrolling smoother at the cost of more CPU spent on encoding ... The video can only contain as many distinct frames as the browser produces; Firefox and WebKit currently capture up to 25 frames per second」（class-screencast.md）
- 「Videos are encoded with VP9 instead of VP8, which takes less CPU and produces smaller files」。出力は WebM（release-notes v1.64）

### 実時間の録画であること（screenstudio-alt の記述）

- screenstudio-alt の作者は、自分のデモ動画を recordVideo で撮らず、1 コマずつシークしてスクリーンショットを撮った理由を「`recordVideo` captures at the browser's `requestAnimationFrame` cadence — a variable frame rate with timing jitter. Forcing that VFR stream into a CFR mp4/gif duplicates and drops frames unevenly, most visible as a stutter/"skip" during fast motion」と書いている（ARCHITECTURE.md）。v1.64 の `fps` 指定より前の記述か後かは書かれていない

### shot-scraper video（1.10、2026-06-30）

- YAML の台本（storyboard）で「scenes」を並べ、各 scene に `click`・`type`（`delay_ms` で 1 文字ずつ）・`fill`・`press`・`scroll`（`duration` で滑らかに）・`pause`・`wait_for`・`wait_for_url`・`open`・`screenshot`・`sh`・`python`・`javascript` を書く。`shot-scraper video storyboard.yml` で WebM、`--mp4` で ffmpeg による MP4 も（docs/video.md）
- 「Playwright videos do not show the system cursor. Add `cursor: true` to inject a visible cursor dot and click rings into the page while recording」。色・点の大きさ・輪の大きさを指定できる
- `viewport` の既定は 1280×720、`fps` の既定は 25（`--fps 60` で上書き）。`server:` で台本の間だけ開発サーバーを立て、URL が応答するまで最大 30 秒待つ（1.11）。`sh:`/`python:` が失敗したら非ゼロで終わる
- Puppeteer の `Page.screencast()` は「obsolete」になり `Page.record()`（CDP の `Page.startScreenRecording`、MP4）へ移った（既存ページ [[web-timesnap-timecut-hyperframes-webcodecs]]。Puppeteer の最新は v25.16.0、2026-10-22）

## この wiki への含意

- **「実物を台本どおりに動かして撮る」の Web 版の本命**。VHS が端末の中で閉じる作品向けだったのに対し（[[web-promo2-vhs-shot-scraper-demos-as-code]]）、Web アプリ・ブラウザで動く研究のデモはこれで撮れる。[[work-promotion-video]] の暫定の答え 1（作品の中身は実物から取る）の手段が、2026 年の版で「カーソルが映らない」という最大の欠点を手放した
- **西尾の方式（[[exp-html-capture-pipeline]]）との違い**: 西尾の方式は自分で描いた canvas を `renderFrame(f)` で 1 コマずつ撮るので、何度撮っても同じ絵になる（決定論的）。Playwright の録画は実時間なので、通信・LLM の応答・アニメーションの速さで毎回少しずつ違う。**決定論的に撮れるのは自分で時間を握れる描画だけ**で、作品の実物は実時間で撮るしかない。重ねる文字・図は西尾の方式で後から描き、実物の収録と分けて合成するのが筋（[[work-promotion-video]] の答え 2）
- **可変フレームレートは経験と一致する懸念**: galleria で「画面録画は VFR になりやすい」を実際に踏んでいる（[[exp-galleria-ffmpeg-measurement-and-delivery]]）。screenstudio-alt の作者の指摘も同じ。収録したら最初に ffprobe で `r_frame_rate` と `nb_frames / duration` を比べ、CFR に直してから編集する
- **操作名の字幕（showActions の title）は promo には邪魔になりうる**。「Click getByRole(...)」のような開発者向けの文字が映る。テストの証拠用の機能なので、promo では `point` だけ出し、title は消すか小さくする（消し方は未確認。下の Open Questions）
- **embed（流しっぱなし）向き**: 台本に `pause` で間を書けるので、話し手が止めずに語れる長さに合わせて撮り直せる。THINKLET のデモのような実機の処理待ちは無いが、Web アプリの待ちは `wait_for` で台本に書ける（[[exp-thinklet-reading-demo-video]] は待ちを説明に変えた。Playwright なら待ちを短く見せる編集をせずに済むが、その分を隠すと [[web-promo2-gemini-nikola-staged-demos]] の問題に近づく）

## 着手の仕方（未検証。galleria で確かめる）

- **表現できるようになること**: Web アプリ・ブラウザのデモを、台本（JS か YAML）で書いた操作どおりに、カーソル・クリックの印・章の見出しつきで録画し、作品が変わったら同じ台本で撮り直す。効く型: promo（作品紹介の実物の部分）、embed（講演に埋める 10〜30 秒の操作の流れ）
- **機械**: galleria WSL（headless でよい。画面が要らない）。日本語の画面を撮るなら WSL に日本語フォントが要る（無いと豆腐になる。推測。`sudo apt install fonts-noto-cjk`）。Windows 側の node で動かせば Windows のフォントで撮れる
- **入れるもの**: Node（galleria にあり）＋ npm の `playwright@1.65.0` ＋ Chromium（`npx playwright install --with-deps chromium`、`--with-deps` は sudo で依存を入れる）。YAML で書くなら `uv tool install shot-scraper`（1.12、2026-09-13）＋ `shot-scraper install`。費用 0、アカウント不要。ライセンス: Playwright・shot-scraper とも Apache-2.0（GitHub API の license 欄。条文は読んでいない。撮った動画の利用に条件は付かない、と読むのが普通だが確かめていない）
- **成熟度**: Playwright はほぼ毎月リリース（v1.59〜v1.65 が 2026-04〜11）。page.screencast は v1.59 で入ったばかりで、`fontSize` が v1.64 で非推奨になるなど API が動いている
- **最小の手順（WSL）**:
  ```sh
  mkdir -p ~/video-tools-trial/pw-capture/out && cd ~/video-tools-trial/pw-capture
  npm init -y && npm i -D playwright@1.65.0
  npx playwright install --with-deps chromium
  ```
  `record.mjs`（公式の API の組み合わせ。クリックの記録と t0 の取り方は推測）:
  ```js
  import { chromium } from 'playwright';
  import fs from 'node:fs';
  const browser = await chromium.launch();
  const context = await browser.newContext({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  const page = await context.newPage();
  await page.goto(process.argv[2]);
  let firstFrameMs = null;
  await page.screencast.start({ path: 'out/take.webm', size: { width: 1920, height: 1080 }, fps: 60,
    onFrame: ({ timestamp }) => { firstFrameMs ??= timestamp; } });
  await page.screencast.showActions({ cursor: 'pointer',
    style: { point: 'width:22px;height:22px;border-radius:50%;background:rgba(255,80,0,.85)' } });
  const clicks = [];
  async function click(sel) {               // クリック位置と時刻を自分で記録する（後で寄る位置に使う）
    const b = await page.locator(sel).boundingBox();
    clicks.push({ ms: Date.now(), x: b.x + b.width / 2, y: b.y + b.height / 2, sel });
    await page.locator(sel).click();
  }
  await page.screencast.showChapter('1. 起動', { duration: 1500 });
  await page.waitForTimeout(1500);
  // await click('text=はじめる'); ... ここに台本
  await page.waitForTimeout(1000);
  await page.screencast.stop();
  fs.writeFileSync('out/clicks.json', JSON.stringify(clicks.map(c => ({ ...c, t: (c.ms - firstFrameMs) / 1000 })), null, 1));
  await browser.close();
  ```
  ```sh
  node record.mjs https://example.com/
  ffprobe -v error -show_entries stream=width,height,r_frame_rate,avg_frame_rate,nb_frames -show_entries format=duration out/take.webm
  ffmpeg -i out/take.webm -vf fps=30 -c:v libx264 -crf 18 -pix_fmt yuv420p -movflags +faststart out/take.mp4
  ```
  YAML で書く場合は shot-scraper の docs の「Complete example」をそのまま `storyboard.yml` にして `shot-scraper video storyboard.yml --fps 60 --mp4`
- **動いたと言える確かめ方**: `out/take.webm` ができ、ffprobe で 1920×1080・duration が台本の合計（待ち込み）に近い。`avg_frame_rate` が 60 に近いか、どこまで落ちたかを記録する（25 を超えるかが v1.64 の効き目）。`ffmpeg -ss <クリックの t> -i out/take.mp4 -frames:v 1 x.png` で、クリックの印が clicks.json の座標に出ていれば、時刻の合わせ方が正しい
- **所要の見込み（推測）**: 導入 30 分、1 本目の台本 1〜2 時間。以後の撮り直しは数分

## Open Questions

- `showActions` の操作名（title）を出さずに点だけ出す方法。`style.title` に `display:none` を書けば消えるか（docs は `point`・`highlight` だけ「省略で出ない」と書く）
- `fps: 60` で headless の Chromium が実際に何 fps 出すか、galleria で測る。screenstudio-alt の言う「VFR で速い動きにつかえ」が v1.64 以降も残るか
- page.screencast の録画開始と `onFrame` の最初の timestamp の関係（最初のフレーム＝動画の 0 秒か）は docs に書かれていない。clicks.json の時刻合わせはこの前提に依る
- recordVideo と page.screencast は同時に使うと「the existing configuration takes precedence」で size が無視されうる（class-screencast.md）。どちらか片方に揃える
