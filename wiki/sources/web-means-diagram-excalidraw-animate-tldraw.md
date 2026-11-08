---
type: source
summary: 手描き風の図を「描いていく順に」見せる道具の一次資料（Excalidraw・excalidraw-animate・tldraw の README・ソース・ライセンス）。excalidraw-animate は Excalidraw の SVG に SMIL の animate 要素を足して要素を順に描き、時刻は svg.setCurrentTime で外から決められる。付属の WebM 書き出しは画面共有の実時間録画。tldraw は図の道具としては使えるが、SDK は独自ライセンスで本番利用にはライセンスキーが要る
video_types: [embed, talk]
url: https://github.com/dai-shi/excalidraw-animate
author: Daishi Kato（excalidraw-animate）、Excalidraw チーム、tldraw, Inc.
published: excalidraw-animate v0.7.2（npm、2026-04-24）／Excalidraw v0.18.1（2026-04-21）／tldraw v5.6.0（2026-10-28）
retrieved: 2026-11-09
sources:
  - https://github.com/dai-shi/excalidraw-animate/blob/main/README.md
  - https://github.com/dai-shi/excalidraw-animate/blob/main/src/animate.ts
  - https://github.com/dai-shi/excalidraw-animate/blob/main/src/export.ts
  - https://github.com/dai-shi/excalidraw-animate/blob/main/src/Toolbar.tsx
  - https://github.com/excalidraw/excalidraw/blob/master/packages/excalidraw/CHANGELOG.md
  - https://github.com/excalidraw/excalidraw/pull/8530
  - https://github.com/excalidraw/excalidraw-mcp/blob/main/README.md
  - https://github.com/tldraw/tldraw/blob/main/LICENSE.md
  - https://tldraw.dev/community/license
  - https://tldraw.dev/sdk-features/license-key
  - https://tldraw.dev/sdk-features/animation
  - https://tldraw.dev/sdk-features/image-export
  - https://developer.mozilla.org/en-US/docs/Web/API/SVGSVGElement/setCurrentTime
---

# 手描き風の図を順に描く: Excalidraw ＋ excalidraw-animate、tldraw

## 何の文献か

- excalidraw-animate: Daishi Kato（個人）の OSS。README とソース（`src/animate.ts`・`src/export.ts`・`src/Toolbar.tsx`）を読んだ。MIT、GitHub の star 約 2,100（2026-11-09 の API 値）、2020-05 作成、最終 push 2026-10-22。npm の最新は 0.7.2（2026-04-24）で、依存は `@excalidraw/excalidraw` 0.18.1
- Excalidraw: 公式 repo の CHANGELOG と PR #8530。MIT。最新リリース v0.18.1（2026-04-21）、star 約 13.5 万
- tldraw: tldraw, Inc. の SDK。LICENSE.md と tldraw.dev の docs（License・License key・Animation・Ticks・Image export）を読んだ。最新 v5.6.0（2026-10-28）、star 約 5.1 万。ライセンスは OSS ではない（下）
- いずれも作り手の一次資料。動画の書き出しを試した記録・速度の数字は無い

## 書いてあること

### excalidraw-animate（Excalidraw の図を描き順アニメにする）

- 「Excalidraw の図をアニメーションにする外部の道具」。Web 版（dai-shi.github.io/excalidraw-animate）に `.excalidraw` ファイル・ライブラリ・共有リンクを読ませる（README）
- **仕組み（ソースから）**: Excalidraw が書き出した SVG の各要素に SMIL の `<animate>`（`attributeName` は `d`・`opacity`）と `<animateMotion>` を足し、`begin`・`dur` をミリ秒で書く（`animate.ts`）。線は path の `d` を少しずつ伸ばし、描く前は `opacity` 0 で隠す（`hideBeforeAnimation`）
- **既定の時間**: 先頭に 1 秒の余白、個々の要素は 500ms、グループは合計 5 秒をメンバーで割る、最後に 1 秒の余白（`animateSvg` の `startMs ?? 1000`・`individualDur = 500`・`groupDur = 5000`・`finishedMs = current + 1000`）。README も「個々の要素は既定 500ms、グループは合計 5 秒」と書く
- **順番と長さの指定**: 明示の順番が無い要素は Order=0 で作った順（README）。ソースでは順番・長さを**要素の id に埋めた文字列** `animateOrder:N`・`animateDuration:N` から読む（`extractNumberFromElement` が `element.id` を正規表現で読む）。Web 版の UI で Order/Duration を入れられる
- **書き出し**: SVG と WebM。SVG は `svg.setCurrentTime(0)` にしてから文字列にする（`exportToSvgFile`）ので、**書き出した SVG は SMIL のアニメを持ったまま**。WebM は `navigator.mediaDevices.getDisplayMedia`（画面共有）を `MediaRecorder` で実時間に録る（`prepareWebmData`）。README の Known issues は「WebM の書き出しは完全ではない。うまくいかなければ画面収録を使って」
- 一時停止・コマ送りは `svg.pauseAnimations()`／`svg.setCurrentTime(秒)` で実装している（`Toolbar.tsx`）。「Step through animations」は各要素の `begin` の一覧（`getBeginTimeList`）の次の時刻へ飛ぶ
- npm パッケージとして `animateSvg(svg, elements, options)`・`getBeginTimeList` などを出している（`src/library.ts`）

### SMIL の時刻を外から決める（MDN）

- `SVGSVGElement.setCurrentTime(time)`: 「この SVG 文書片の時計を合わせ、新しい現在時刻を決める」。引数は秒の浮動小数
- `pauseAnimations()`: 「この SVG 文書片の中で動いているアニメーションをすべて止め、時計を止める」

### Excalidraw 本体

- v0.18.0（2025-03-11）の Highlights に「Font for Chinese, Japanese and Korean (#8530)」「Font subsetting for SVG export」。PR #8530 は手書き風の Excalifont の fallback として `Xiaolai-Regular` を入れ、CJK 以外の字形を除き、ハングルの字間を詰めたなどと書く
- CHANGELOG の Unreleased（2026-10-18、#12347）に**破壊的変更**: `exportToCanvas`・`exportToBlob`・`exportToSvg` は `exportScene({ type, data, config })` 一つに置き換わる。0.18.1 では旧 API のまま
- Excalidraw MCP（excalidraw/excalidraw-mcp、v0.3.2 2026-02-09）は「手描きの Excalidraw の図を、視点のカメラ操作付きでストリームする」MCP Apps のサーバ。チャットの中で描く道具で、動画の書き出しは README に無い。GitHub の API ではライセンスが判定できなかった（未確認）

### tldraw

- **ライセンス**: 既定の条件では「開発でのみ使ってよい」。本番（Production Environment）には trial（100 日、無料、1 社 1 回）・commercial（有償、見積もり）・hobby（非商用、審査制、「made with tldraw」の透かしを出す）のどれかのライセンスキーが要る（tldraw.dev/community/license）。LICENSE.md は Production Environment を「サーバ・クラウド・Web アプリなどの本番配備、またはエンドユーザー・顧客・公衆に機能を提供する使い方」、Development Environment を「組織内の開発・試験・ステージング用で、エンドユーザー等がアクセスできないもの」と定める
- **開発か本番かの判定**: 「HTTPS でない、ホスト名が localhost かループバック、または `NODE_ENV` が production でない、のどれかなら開発」。本番でキーが無いと「5 秒後に描画を止める」（License key のページ）
- **アニメーション**: `editor.animateShape` やカメラの `animation` オプションは「エディタの tick」で進み、tick は「毎フレーム、前フレームからの経過ミリ秒」を渡す（Animation・Ticks のページ）。時刻を外から与える API の記述は無い
- **書き出し**: SVG・PNG・JPEG・WebP。SVG はフォントを data URL で埋め込み、「見る側に何が入っていても同じに描ける」（Image export のページ）

## この wiki への含意

- **西尾の方式に載る**: excalidraw-animate の SVG は SMIL なので、headless Chrome で開き `pauseAnimations()` → `setCurrentTime(f / fps)` → スクリーンショット、でフレーム番号から 1 枚が決まる（MDN の API と excalidraw-animate 自身のコマ送りの実装からの推測。未検証）。付属の WebM 書き出しは画面共有の実時間録画で、決定的でない。[[exp-html-capture-pipeline]] の `renderFrame(f)` は自分で描く純関数だが、ここでは「SVG の時計を合わせる」が `renderFrame` の代わりになる
- [[web-timesnap-timecut-hyperframes-webcodecs]] の HyperFrames のアダプター一覧（GSAP・CSS・Lottie・Three.js・Anime.js・WAAPI）に SMIL は無い。SMIL は自前で時計を合わせる（推測）
- **embed（流しっぱなし、30〜60 秒で一概念）に合う理由**: 描き順そのものが説明の順になる。既定値だと 10 要素で約 7 秒（1 秒＋10×0.5 秒＋1 秒）。話し手が止められないので、要素の多い図は `animateDuration` を延ばすか、描く順の区切りで間を置く必要がある（担当の計算と推測）
- 経験との照合: [[exp-llm-wiki-explainer-series]] の「図形と文字だけで描けば（private な画面の）映り込みは起きない」と同じ側の手段。[[exp-qualia-video]] の「動かすなら説明中の図・語・数値・工程 node を直接 highlight する」とも合う。ただし手描き風の線のゆらぎが「真面目な解説」に合うかは試していない
- tldraw は「localhost で開く」なら開発扱いでキーが無くても動く（docs の判定の記述から）。ただし自分の機械で描いて**動画を公開する**ことがライセンスの「本番」に当たるかは条文から読み切れない（下の Open Questions）。手描き風の段階描画が目的なら、MIT の Excalidraw ＋ excalidraw-animate のほうが条件の確認が少ない

## 着手の仕方（未検証。galleria で確かめる）

- **増える表現**: 手描き風の図が線ごとに描かれていく 30〜60 秒の mp4（embed 向き。talk の中の図解にも）
- **機械**: 描くのはどこでも（ブラウザ。Mac でも可）。撮るのは galleria（WSL か Windows。[[exp-polis-magi-op]] は Windows 側の Chrome に合わせた）
- **入れるもの**: Node（galleria にある）、`puppeteer-core`（既存の capture.mjs と同じ）、Chrome。図を描くのは excalidraw.com（ブラウザ、アカウント不要）と excalidraw-animate の Web 版（アカウント不要）。費用 0。ライセンスは両方 MIT。Xiaolai フォントのライセンスは PR に書かれておらず未確認
- **成熟度**: excalidraw-animate は個人の道具で、npm の最終版 2026-04、repo の最終 push 2026-10。Excalidraw 本体は活発だが、次の版で書き出し API が変わる（0.18.1 に固定する）
- **最小の手順**
  1. excalidraw.com で図を描き、`.excalidraw` を保存（文字は日本語で書き、Excalifont のまま）
  2. dai-shi.github.io/excalidraw-animate で読み込み、Animate モードで順番・長さを調整し、**SVG を書き出す**（`anim.svg`）
  3. galleria の WSL: `mkdir -p ~/video-tools-trial/exa && cd ~/video-tools-trial/exa`、`anim.svg` を置き、`index.html` に `<body style="margin:0;background:#fff">` と SVG を**インラインで**入れる（`<img>` で読むと `pauseAnimations` を呼べない。推測）
  4. `python3 -m http.server 8000` で配信（[[exp-html-capture-pipeline]] の「file:// で開かない」に合わせる）
  5. capture.mjs を次の形に変える（推測で書いた骨格）:
     ```js
     const svgSel = 'svg';
     await page.goto('http://localhost:8000/');
     await page.evaluate(() => document.fonts.ready);
     const dur = await page.evaluate(s => {          // 最後の begin+dur を総尺に
       let end = 0; document.querySelectorAll(`${s} animate, ${s} animateMotion`).forEach(a => {
         end = Math.max(end, parseFloat(a.getAttribute('begin')) + parseFloat(a.getAttribute('dur'))); });
       return end / 1000 + 1; }, svgSel);
     for (let f = 0; f < Math.ceil(dur * FPS); f++) {
       await page.evaluate((s, t) => { const v = document.querySelector(s); v.pauseAnimations(); v.setCurrentTime(t);
         return new Promise(r => requestAnimationFrame(() => r())); }, svgSel, f / FPS);
       ffmpeg.stdin.write(await page.screenshot({ type: 'png' }));
     }
     ```
     ffmpeg 側は既存と同じ `-f image2pipe -framerate 30 -i - -c:v libx264 -pix_fmt yuv420p out.mp4`
- **動いたと言える確かめ方**: (1) `ffprobe out.mp4` の duration が上で計算した総尺と一致、(2) 同じ f を 2 回撮った PNG の `sha256sum` が一致（決定的であることの確認）、(3) f=0・中央・最後の 3 枚の静止画で、線が途中まで描かれた状態が出ている、(4) 日本語が豆腐（□）になっていない
- **所要の見込み（推測）**: 図を描く 30 分、撮影の骨格の改造 1 時間、10 秒の図で撮影は数十秒

## Open Questions

- `setCurrentTime` の直後に 1 回の `requestAnimationFrame` で描画が SVG の新しい時刻を反映するか（反映が 1 コマ遅れないか）は未確認。2 回待つ必要があるかもしれない
- Excalidraw の書き出し SVG にフォントが埋め込まれるか（0.18 の「SVG 書き出しのフォントのサブセット化」）、それとも CDN から読むかで、機械による差が変わる。excalidraw-animate の Web 版が書き出す SVG にフォントが入っているかは未確認
- Xiaolai は CJK 用の fallback と PR に書かれているが、漢字の字形が日本語として自然か（中国語の字形にならないか）、ライセンスは何か、は未確認
- tldraw を localhost で動かして描いた動画を公開することは、LICENSE.md の「Production Environment（エンドユーザー・公衆に機能を提供する使い方）」に当たるか。動画は SDK の機能を提供していないとも読めるが、条文は動画の出力について書いていない。使うなら tldraw に確かめるのは西尾が決めること
- 手描き風（線のゆらぎ）は、Tufte の data-ink の考え（[[web-layout-tufte-data-ink-chartjunk]]）から見ると「データでないインク」に当たるか、Bateman の「データを描く飾り」（[[web-layout-bateman-2010-useful-junk]]）に近いか。どちらとも言えず、効果は測られていない
