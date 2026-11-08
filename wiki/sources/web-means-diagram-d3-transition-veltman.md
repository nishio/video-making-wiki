---
type: source
summary: D3 の transition と timer の公式ドキュメントと、Noah Veltman の「データのアニメを GIF・動画に書き出す方法」の比較（GitHub README）。d3-transition は開始時の DOM の値から補間し d3-timer（requestAnimationFrame・performance.now）で進むので、フレーム番号の純関数にならない。Veltman は手法を 9 通り比べ、フレーム単位で書く方法は transition のような宣言的なアニメに使えず、時間関数を偽る方法は「後片付け」のため一方向にしか進めないと書く。d3 の補間・イージング・スケールを transition 抜きで使えば純関数で書ける
video_types: [embed, talk, promo]
url: https://github.com/veltman/gifs
author: Mike Bostock ほか（D3）、Noah Veltman（gifs）
published: D3 v7.9.2（2026-11-03）／Veltman gifs は日付不明（例が d3 3.5.10＝2015-11-30 公開を読み込むので 2015-12 以降）
retrieved: 2026-11-09
sources:
  - https://d3js.org/d3-transition
  - https://d3js.org/d3-transition/modifying
  - https://d3js.org/d3-timer
  - https://github.com/d3/d3/blob/main/docs/d3-transition.md
  - https://github.com/d3/d3/blob/main/docs/d3-timer.md
  - https://github.com/d3/d3/blob/main/docs/d3-transition/modifying.md
  - https://github.com/veltman/gifs/blob/master/README.md
  - https://github.com/veltman/d3-unconf
  - https://github.com/tungs/timesnap/blob/master/README.md
---

# D3 の transition と、データのアニメを動画に書き出す方法（Veltman）

## 何の文献か

- D3（ISC、star 約 11.4 万、v7.9.2 が 2026-11-03）の公式ドキュメント（d3js.org の元の Markdown、d3/d3 repo の docs/）。d3-transition・d3-timer の章を読んだ
- Noah Veltman（所属は README に書かれていない）の GitHub repo `veltman/gifs` の README「Animation Tests」。データのアニメを GIF・動画にする手法を比べた実務の覚え書き。実験の数値は「Web Worker＋canvas で 1 秒のアニメに 5〜10 秒」くらい。日付は repo から取れず、例が d3 3.5.10（npm 公開 2015-11-30）を読み込むので 2015-12 以降の文書
- timesnap の README（[[web-timesnap-timecut-hyperframes-webcodecs]] で既に読んだもの）は「Noah Veltman の講演（d3-unconf）に着想を得た」と書く

## 書いてあること

### d3-transition と d3-timer（公式）

- transition は「DOM の変化を即座に適用せず、今の状態から目標の状態へ、指定した時間で滑らかに補間する」。色・数・transform・数を含む文字列（path など）の補間を自動で選ぶ（d3-transition）
- `transition.attr` の補間の始点は「transition が**始まったとき**の属性の値」（modifying）。つまり前の状態に依存する
- `attrTween` の項: 「有用な技法は data interpolation。`interpolateObject` で 2 つのデータ値を補間し、その結果を（shape などで）属性の値に計算する」（modifying）
- d3-timer: 「内部で requestAnimationFrame を使い、24ms より長い遅延では setTimeout に切り替える」。`d3.now()` は `performance.now`（無ければ `Date.now`）。「ページがバックグラウンドで requestAnimationFrame が止まると、見かけの時間は凍る」。`timerFlush()` は「条件を満たす timer の callback を即座に呼ぶ」（d3-timer）

### Veltman の比較（gifs の README）

- 動機: 「インタラクティブな可視化は良いが、GIF や動画のほうが話をよく伝えることもある」「GIF にする現在の定石は画面収録で、簡単だが再現も設定もしにくい」
- 9 つの手法と長所・短所（要旨）:

| 手法 | Veltman の評価の要点 |
|---|---|
| QuickTime＋FFmpeg／＋Photoshop／LICEcap | 画面収録。どんなアニメも撮れるが、変えるたびに撮り直し、範囲と開始・終了を正確に合わせにくい |
| Node＋canvas | 全部コードで自動化でき、大きさ・開始終了・fps を細かく決められる。ただし「1 コマずつ最初から描くコードでしか使えない。`d3.transition` や CSS アニメのような宣言的なものは不可」。canvas だけ、CSS・SVG 不可 |
| Web Worker＋canvas／＋SVG | ブラウザ内で 1 コマずつ描いて gif.js でまとめる。「アニメ 1 秒に描画 5〜10 秒」、SVG はさらに遅い。宣言的なアニメには使えない |
| PhantomJS（＋Web Worker） | ふつうに書いた transition のページを headless ブラウザで数ミリ秒ごとに撮る |
| d3 transition をハックする（d3-record.js） | transition が内部に持つイージングと tween を取り出し、任意の進み具合 t を同期で適用する「ghost transition」。「だいたい動く試作」。「d3 の軸のように transition に特有の振る舞いを持つものでは動かない」 |
| 時間を止める | `Date.now` と `requestAnimationFrame` を上書きして「今は t＋◯ミリ秒だ」と嘘をつく。どの宣言的ライブラリにも効くが、「後片付けの問題（アニメが要所の時刻を過ぎると裏で自分を片付ける）は解けないので、複雑なアニメは一方向にしか進められない」。「グローバルな時間関数の上書きは勧めるのが不正行為に感じる。気をつけて」 |

- まとめ: 「1 コマずつ画像の束を作る仕組みはどれも ffmpeg に通せば動画になる。After Effects を覚えなくてもデータ駆動のアニメを動画にできる」

## この wiki への含意

- **西尾の方式は Veltman の「Node＋canvas」をブラウザで回したもの**: [[exp-html-capture-pipeline]] の `renderFrame(f)` は「1 コマずつ最初から描く」型で、Veltman が書く長所（自動化・大きさと fps の制御）と短所（宣言的な transition が使えない）をそのまま持つ。headless Chrome を使うので canvas に限られない点が Veltman の Node＋canvas より有利
- **D3 は transition を使わずに使う**: `d3.scaleLinear`・`d3.interpolate`・`d3.easeCubicInOut`・`d3.line` は時間を持たない純関数。`renderFrame(f)` の中で `t = ease(clamp((f/FPS - 開始)/長さ))` を作り、`interpolateObject(前のデータ, 次のデータ)(t)` を描けば、公式が勧める data interpolation を時刻の純関数として書ける（公式の記述の組み合わせ。未検証）
- **既にある transition のコードを撮るなら** timesnap の仮想時間（[[web-timesnap-timecut-hyperframes-webcodecs]]）。Veltman の言う「一方向にしか進めない」制約は timesnap でも同じはずで、`stills` で途中の秒だけ撮る確認（[[exp-html-capture-pipeline]]）は頭から流し直しになる（推測）
- **embed（流しっぱなし）で何を動かすか**: [[web-berney-betrancourt-2016-animation-meta-analysis]] は表現的なアニメに効果、装飾的なアニメは ≈0 とする。データのアニメは「値の変化そのもの」が中身なので表現的な側。ただし Roslingifier（[[web-roslingifier-data-presentations]]）の分析した発表は話し手が止めて語る形で、西尾の embed（流しっぱなし）とは違う。流しっぱなしなら「先に軸と色の意味を画面に出す → 注目点を示す → 動かす」を動画の側の文字・強調で代わりにやる（推測）
- 経験との照合: [[exp-gyazo-resumption-video]] で西尾は棒グラフを「いまいち」とし、処理の違いが見える比較図に変えさせた。データを動かすときも「どの値の変化を見せたいか」を一つに絞る必要がある（推測）

## 着手の仕方（未検証。galleria で確かめる）

- **増える表現**: 棒が伸びる・線が描かれる・点が移る（散布図の年ごとの移動）などの、データが動く 30〜60 秒の embed。既存の HTML/canvas の型のまま、D3 の計算部品だけ足す
- **機械**: galleria WSL か Windows（既存の capture.mjs が動く側）。Mac でも可
- **入れるもの**: `d3@7.9.2`（ISC）を npm かローカルのファイルで。既存の puppeteer-core と ffmpeg。費用 0、アカウント不要
- **成熟度**: D3 v7 は長く安定（7.9.2 は 2026-11-03）。transition 抜きで使う部品は API が変わりにくい
- **最小の手順**（WSL。既存の型の流用）
  1. `mkdir -p ~/video-tools-trial/d3bar && cd $_ && npm i d3@7.9.2 puppeteer-core`、capture.mjs を既存の repo から写す
  2. `index.html` で `<script src="node_modules/d3/dist/d3.min.js"></script>`（全体を `d3` として読む）を読み、次の形の `renderFrame(f)` を書く（推測で書いた骨格）:
     ```js
     const FPS = 30, DUR = 30; window.FPS = FPS; window.TOTAL_FRAMES = FPS * DUR;
     const A = [{k:'2020',v:12},{k:'2021',v:30}], B = [{k:'2020',v:40},{k:'2021',v:18}];
     const x = d3.scaleBand(A.map(d=>d.k), [200, 1700]).padding(0.3), y = d3.scaleLinear([0, 50], [900, 150]);
     window.renderFrame = f => {
       const s = f / FPS, t = d3.easeCubicInOut(Math.min(1, Math.max(0, (s - 3) / 1.5)));
       const data = A.map((d, i) => ({k: d.k, v: d3.interpolateNumber(d.v, B[i].v)(t)}));
       // canvas に x(d.k), y(d.v) で棒を描く（前のコマの状態を持たない）
     };
     window.ready = document.fonts.load('48px "Noto Sans JP"');
     ```
  3. `node capture.mjs stills 2 4 6` で静止画を見て、`node capture.mjs video`
- **動いたと言える確かめ方**: (1) 3 秒の静止画で棒が A の高さ、4.5 秒以降で B の高さ（ピクセルで棒の上端を測る）、(2) `stills 3.75` を 2 回撮って sha256 が一致、(3) `ffprobe` の duration が 30.0 秒
- **所要の見込み（推測）**: 既存の型があるので 1〜2 時間

## Open Questions

- Veltman の README は 2015〜2016 年頃の道具（PhantomJS・gif.js）を前提にしている。「時間を止める」の後片付けの問題が、今の d3-transition（v3）と timesnap で同じに起きるかは確かめていない
- d3-transition の `transition.end()` や `interrupt` を使うコードを timesnap で撮ると、どこで「一方向にしか進めない」が効くか
- データのアニメを流しっぱなしで見せたときに、Roslingifier 型（話し手が止めて語る）と比べてどれだけ伝わるかの研究は見つかっていない（[[web-roslingifier-data-presentations]] の Open Questions と同じ）
