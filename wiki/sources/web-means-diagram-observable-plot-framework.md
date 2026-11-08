---
type: source
summary: Observable Plot と Observable Framework の公式ドキュメント・README。Plot は「アニメーションの宣言的な指定は将来の版で計画中」で、部分的な再描画も遷移も持たず「古いプロットを捨てて新しいのに置き換えればよい」と書く。だから時刻ごとにデータを作って Plot を描き直す形がそのままフレーム番号の純関数になる。Node でも JSDOM で SVG を出せるが、公式は「フォントの描画をよくするなら Puppeteer」と書く。Framework はデータアプリ用の静的サイト生成器で、動画の書き出しは持たない
video_types: [embed, talk]
url: https://observablehq.com/plot/features/interactions
author: Observable, Inc.
published: Plot v0.6.19（2026-11-05）／Framework v1.13.4（2026-03-02）
retrieved: 2026-11-09
sources:
  - https://github.com/observablehq/plot/blob/main/docs/features/interactions.md
  - https://github.com/observablehq/plot/blob/main/docs/getting-started.md
  - https://github.com/observablehq/plot/blob/main/docs/features/plots.md
  - https://github.com/observablehq/plot/blob/main/docs/why-plot.md
  - https://github.com/observablehq/plot/blob/main/CHANGELOG.md
  - https://github.com/observablehq/framework/blob/main/README.md
---

# Observable Plot と Framework: 描き直しで動かすグラフ

## 何の文献か

Observable, Inc. の OSS。Plot（ISC、star 約 5,400、v0.6.19 が 2026-11-05）は docs の元の Markdown（features/interactions・getting-started・features/plots・why-plot）と CHANGELOG を、Framework（ISC、star 約 3,700、最新 v1.13.4 が 2026-03-02、repo の最終 push 2026-05-15）は README を読んだ。observablehq.com のページは Vercel のセキュリティ確認で止められ、取得していない（回避していない）。一次資料のみ。

## 書いてあること

### Plot のアニメーションの扱い（features/interactions「Animation」「Custom reactivity」）

- 「宣言的なアニメーションのサポートは将来の版で計画している。関心があれば #166 に投票を。**time** チャンネルの初期の作業は #995」
- 「render transform（pointer の実装）を除き、Plot は今のところ、描いたプロットの部分的な再描画（incremental re-rendering）も、表示の間のアニメーション遷移も提供しない」
- 「それでも、古いプロットを捨てて新しいのに置き換えればよい。これでストリームで変わるデータや、スライダーなど外の入力から導いたデータを描ける」
- 「低レベルの API に慣れていれば Plot が作った SVG を操作してもよい」として Mike Freeman と Philippe Rivière の Observable のノートブック（plot-animation、plot-animate-a-bar-chart）を挙げる（ノートブックは読んでいない）
- why-plot: 「広いアニメーションやインタラクションを持つ特注の可視化（…）は D3 の低レベル API のほうが向く」

### Plot をブラウザの外で描く（getting-started「Plot in Node.js」、features/plots）

- 「Node で SVG や PNG をサーバ側描画できる。DOM の実装に JSDOM を **document** オプションで渡し、`outerHTML` で文字列にする」。PNG にするには canvg＋node-canvas、または sharp。「**フォントの描画をよくするなら Puppeteer を検討して**」
- **document** オプションは「プロットの要素を作る document。既定は window.document」
- React での SSR は「単純なプロットと小さなデータでだけ実用的」（getting-started）

### Framework（README）

- 「データアプリ・ダッシュボード・レポートのための、無料の OSS の静的サイト生成器」。前面は JavaScript、裏は任意の言語で、「ビルド時にデータの静的なスナップショットを前もって計算するデータローダー」を持つ
- 動画・アニメの書き出しの記述は無い

## この wiki への含意

- **Plot は「描き直し」が公式の答えなので、西尾の方式とぶつからない**: `renderFrame(f)` の中で時刻 `f/FPS` からデータ（補間した値や、年 `≤ year(f)` で絞った行）を作り、`Plot.plot({...})` を毎フレーム作り直して置き換えれば、フレーム番号だけで絵が決まる（公式の「置き換えればよい」からの推測。未検証）。Plot が遷移を持たないことが、撮る側にとってはむしろ扱いやすい
- **補間は自分で書く**: Plot は遷移しないので、棒が「伸びる」には中間の値を自分で作る。[[web-means-diagram-d3-transition-veltman]] の d3-interpolate・d3-ease と組む。軸の目盛り（domain）が毎フレーム変わると目盛りが跳ねるので、domain は固定する（推測）
- **SVG なので canvas の `toDataURL` では撮れない**: [[exp-html-capture-pipeline]] は canvas の `toDataURL` を ffmpeg に流す。Plot の SVG は `page.screenshot` で撮るか、SVG を `Image` に読んで canvas に描いてから `toDataURL`（Veltman の「Web Worker＋SVG」と同じ技、[[web-means-diagram-d3-transition-veltman]]）。前者が簡単
- **Node＋JSDOM の経路は日本語に弱そう**: 公式自身が「フォントの描画をよくするなら Puppeteer」と書く。日本語の字幅の計測が要るラベルでは headless Chrome で描くほうが安全（推測）
- **Framework は embed の道具ではない**: 静的サイトのダッシュボードを作る道具で、動画とは別。talk で「ページを見せる」なら使えるが、この wiki の問いからは外れる
- Plot の簡潔さは、Claude Code に「このデータでこの図を」と書かせるときに効く（D3 で一から書くより短い。推測）。[[web-layout-tufte-data-ink-chartjunk]] の「データでないインクを減らす」に既定の見た目が近い（担当の印象）

## 着手の仕方（未検証。galleria で確かめる）

- **増える表現**: 年ごとに点が動く散布図、累積していく折れ線、並びが変わる棒グラフなどの 30〜60 秒の embed。Plot の既定の見た目のまま使える
- **機械**: galleria WSL か Windows（既存の capture.mjs が動く側）。Mac でも可
- **入れるもの**: `@observablehq/plot@0.6.19`・`d3@7`（ISC）、既存の puppeteer-core・ffmpeg。日本語は Noto Sans JP の web フォントをページで読む。費用 0、アカウント不要
- **成熟度**: Plot は 0.x だが毎月のようにリリース。アニメの機能は「計画中」のまま
- **最小の手順**（WSL）
  1. `mkdir -p ~/video-tools-trial/plot && cd $_ && npm i @observablehq/plot@0.6.19 d3@7 puppeteer-core`
  2. `index.html` で `node_modules/d3/dist/d3.min.js` と `node_modules/@observablehq/plot/dist/plot.umd.min.js` を `<script>` で読む（UMD の配布物の名前は推測。`ls node_modules/@observablehq/plot/dist` で確かめる）
  3. `renderFrame(f)` で `const year = 2000 + Math.floor(f / (FPS*2))` のように時刻から絞り込み、`const svg = Plot.plot({width:1920, height:1080, x:{domain:[...]}, y:{domain:[...]}, style:{fontFamily:'Noto Sans JP', fontSize:'28px'}, marks:[Plot.dot(rows.filter(r => r.year === year), {x:'a', y:'b'})]}); document.body.replaceChildren(svg);`
  4. capture.mjs の `toDataURL` の行を `page.screenshot({type:'png', clip:{x:0,y:0,width:1920,height:1080}})` に替える
- **動いたと言える確かめ方**: (1) 同じ f の PNG の sha256 が 2 回で一致、(2) 軸の目盛りがコマ間で動かない（f と f+1 の差分画像で軸の領域が 0）、(3) 日本語のタイトル・ラベルが出ている
- **所要の見込み（推測）**: 2〜3 時間

## Open Questions

- Plot の `time` チャンネル（#995）がいつ入るか、入ったときに時刻を外から与えられる形になるか
- 毎フレーム SVG を作り直すときの撮影速度。DOM の作り直しが canvas より重いかは測っていない（[[exp-html-capture-pipeline]] の「描画の重さで 10 倍以上違う」の実測は canvas の場合）
- 毎フレーム作り直すと、行の並びが変わるときの「同じものが動いた」感（object constancy）は出ない。点の位置を補間するなら、前後の年の同じ行をキーで対応させる処理を自分で書く必要がある（推測）
