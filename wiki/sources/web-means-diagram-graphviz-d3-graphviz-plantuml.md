---
type: source
summary: Graphviz（DOT）・d3-graphviz・PlantUML の公式資料。Graphviz と PlantUML は静止図（SVG/PNG/PDF など）を出すだけでアニメは持たない。段階表示は「全部の要素を置いたまま後の要素を style=invis にする」形で位置を保てる（推測を含む）。d3-graphviz は DOT から DOT への変化を d3 の transition で動かし（形・辺の補間、出入りのフェード）、キーで同じノードを対応させるが、時間は d3 の timer が持つ
video_types: [embed, talk]
url: https://github.com/magjac/d3-graphviz
author: Graphviz プロジェクト、Magnus Jacobsson（d3-graphviz）、PlantUML プロジェクト
published: Graphviz 16.1.1（2026-11-08）／d3-graphviz 5.6.0（2024-08-18）／PlantUML v1.2026.9（2026-10-17）
retrieved: 2026-11-09
sources:
  - https://graphviz.org/license/
  - https://graphviz.org/download/
  - https://graphviz.org/docs/outputs/
  - https://graphviz.org/docs/attr-types/style/
  - https://gitlab.com/graphviz/graphviz/-/releases
  - https://github.com/magjac/d3-graphviz/blob/master/README.md
  - https://github.com/plantuml/plantuml/blob/master/README.md
  - https://plantuml.com/en/command-line
---

# Graphviz・d3-graphviz・PlantUML: 配置を保ったまま図を変化させる

## 何の文献か

- Graphviz: 公式サイトの License・Download・Output Formats・style 属性のページ、GitLab のリリース一覧。最新 16.1.1（2026-11-08）、その前 16.1.0（2026-09-04）。EPL-2.0
- d3-graphviz: Magnus Jacobsson の OSS の README。BSD-3-Clause、star 約 1,800、npm の最新 5.6.0（2024-08-18）、repo の最終 push 2025-02。Graphviz の WebAssembly 版（@hpcc-js/wasm。graphviz 部分の npm パッケージは Apache-2.0、1.30.0 が 2026-10-21）でレイアウトする
- PlantUML: GitHub の README と公式サイトの command-line のページ。最新 v1.2026.9（2026-10-17）、star 約 1.3 万
- いずれも作り手の一次資料

## 書いてあること

### Graphviz

- ライセンス: 「現在の Graphviz は Eclipse Public License のもとでだけオープンソースとして提供される」（EPL-2.0 の全文を掲載。「お金が絡むなら知財の弁護士に相談を」とも書く）
- 出力形式: SVG・PNG・PDF・GIF・JSON・xdot ほか 30 種以上（Output Formats）。アニメの形式は無い
- Ubuntu は `sudo apt install graphviz`、Windows はインストーラ（16.1.0 の exe・zip）（Download）
- style 属性に `invis` がある（style のページ）。見えないが配置には参加する（Graphviz の一般的な挙動。このページは invis の意味を詳しく書いていないので、ここは担当の知識による）

### d3-graphviz

- 「DOT の図を SVG に描き、図と図の間をアニメーションで遷移させる」。機能: DOT からの SVG 描画、ある図から別の図へのアニメ遷移、辺の path の補間、ノードの形の補間、出入りするノード・辺のフェード、入ってくる辺が伸びるアニメ、パン・ズーム（README Features）
- 仕組み: @hpcc-js/wasm でレイアウトして SVG の文字列を作り、それを解析してデータにし、D3 でデータを DOM に結び、図から図への遷移を D3 で動かす（Principles of Operation）
- 遷移は `d3.transition().duration(750).ease(d3.easeLinear)` を作って `graphviz.transition(t)` で付ける。同じノードを対応させるキーは既定で SVG の `title`（ノード ID、辺は「a -> b」）（Creating Transitions・Object Constancy）
- イベント: `layoutStart`・`layoutEnd`・`transitionStart`・`transitionEnd`・`end` などを `graphviz.on()` で受けられる
- 性能: 形・辺の補間は「かなり計算が重い」。「遷移を滑らかにするため、重い計算は遷移の前に済ませる」（Performance）

### PlantUML

- UML（シーケンス・クラス・アクティビティなど）と、マインドマップ・ガント・ワイヤーフレームなどを文字から描く（README）
- ライセンスは GPL・LGPL・Apache・EPL・MIT から選べる（README の License）
- CLI: `--png`（既定）・`--svg`・`--format pdf` など（command-line のページ）。アニメの機能は README・CLI に無い
- 新しく `@plantuml/mcp-js`（「Java もサーバも要らない、純粋な Node の MCP サーバ」）と、TeaVM でブラウザだけで動く JavaScript 版がある（README）

## この wiki への含意

- **静止図の道具は「段ごとの画像」にしてから動かす**: Graphviz・PlantUML はアニメを持たないので、段ごとの SVG を作り、[[exp-html-capture-pipeline]] の `renderFrame(f)` で重ねて出す。Graphviz なら**全要素を一つの DOT に書き、まだ出さない要素を `style=invis` にした版を段の数だけ作る**と、配置が段の間で変わらない（担当の知識による推測。galleria で差分画像で確かめる）。Mermaid・D2（[[web-means-diagram-mermaid]]、[[web-means-diagram-d2]]）で段ごとに別の図を描くと配置が変わりうる問題への、一番単純な答え
- **d3-graphviz は「図が図に変わる」を自動で補間する**: 段の間でノードが動く・形が変わる・辺が伸びる、を作り手が書かずに得られる。Tversky の Congruence（変化の構造と表現の構造を合わせる、[[web-tversky-2002-animation-can-it-facilitate]]）で言えば、「関係が増える・組み替わる」概念にはこの補間が合う（推測）
- **ただし時刻は d3 の timer が持つ**: d3-graphviz の遷移は d3-transition で動き、d3-transition は d3-timer（requestAnimationFrame と performance.now）で進む（[[web-means-diagram-d3-transition-veltman]]）。フレーム番号の純関数にはならない。撮るなら (a) timesnap のように時間関数を差し替える（[[web-timesnap-timecut-hyperframes-webcodecs]]）、(b) 遷移を使わず、2 つの段の SVG の座標を自前で補間する、のどちらか。(a) が手早く、(b) が決定的（推測）
- d3-graphviz は 2024-08 から版が出ていない。動くかは galleria で確かめる
- PlantUML はシーケンス図が得意で、embed の「誰が誰に何を送るか」の順を見せる図に向く。段階表示はシーケンス図を段ごとに切った別ファイルにする（推測）

## 着手の仕方（未検証。galleria で確かめる）

- **増える表現**: ネットワーク・依存関係・木の図が、配置を保ったまま段ごとに現れる embed。d3-graphviz なら図が別の図へ形を変えて移る embed
- **機械**: galleria WSL（Graphviz は apt）。Windows のインストーラでも可。Mac でも可
- **入れるもの**: Graphviz（apt の版。最新は 16.1.1）。d3-graphviz を使うなら npm の `d3-graphviz@5.6.0`・`d3@7`。費用 0、アカウント不要。EPL-2.0（Graphviz）・BSD-3（d3-graphviz）
- **成熟度**: Graphviz は 2026-11 にもリリース、活発。d3-graphviz は 2024-08 で止まり気味
- **最小の手順 A（Graphviz の invis で段階表示、WSL）**
  1. `sudo apt install graphviz fonts-noto-cjk`（galleria で）、`dot -V`
  2. `mkdir -p ~/video-tools-trial/gv && cd $_`。`full.dot` に全ノード・全辺を書き、`fontname="Noto Sans CJK JP"` を graph/node/edge に付ける
  3. 段 k で出す要素の一覧を持つ小さな Python で、段 k より後の要素に `style=invis` を足した `step1.dot`…`stepN.dot` を作る（推測で書く手順）
  4. `for i in 1 2 3 4; do dot -Tsvg step$i.dot -o step$i.svg; dot -Tpng -Gdpi=192 step$i.dot -o step$i.png; done`
  5. PNG を ffmpeg の `xfade` でつなぐか、SVG を重ねた HTML を既存の capture.mjs で撮る
- **最小の手順 B（d3-graphviz を timecut で撮る）**: README の例（`d3.select("#graph").graphviz().transition(t).renderDot(dot1)` の後に `dot2`）で HTML を作り、[[web-timesnap-timecut-hyperframes-webcodecs]] の timecut で撮る。timecut は 2022-04 の 0.3.3 が最後で、今の Chrome で動くかは未確認
- **動いたと言える確かめ方**: A は (1) `step1.png` と `stepN.png` の差分画像で、段 1 にある箱の位置が変わっていない（差分が新しい要素の所だけ）、(2) 日本語が出ている。B は (1) 同じ設定で 2 回撮った mp4 の各フレームの md5（`ffmpeg -i out.mp4 -f framemd5 -`）が一致
- **所要の見込み（推測）**: A は 1〜2 時間、B は timecut が動けば 1 時間、動かなければ半日

## Open Questions

- `style=invis` の要素が配置に参加することを、Graphviz の公式ページの文で確かめていない（style のページは値の一覧だけ）
- d3-graphviz の遷移を timesnap の仮想時間で撮ると、レイアウトを Web Worker で計算する設定（`useWorker`）のとき、Worker 側の時間は差し替わらない。レイアウト完了を待ってから時間を進める必要がある（推測）
- PlantUML の日本語フォントの指定（`skinparam defaultFontName`）と、JavaScript 版・MCP 版で同じ絵が出るかは見ていない
