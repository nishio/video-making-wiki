---
type: source
summary: テキストから図を作る D2 の公式ドキュメント・README・リリースノート・ソース。steps（前の段を引き継ぐ段）で図を段階的に組み、--animate-interval で段を一定間隔で切り替える SVG/GIF を、PPTX・PDF・段ごとの SVG も出せる。v0.9.0（2026-09-07）で TALA レイアウトが OSS 化・同梱され、PNG/GIF/PDF/PPTX はブラウザ無しの内蔵描画になった。段の切り替えはクロスフェードでなく 1ms の切り替えのループ
video_types: [embed, talk]
url: https://d2lang.com/tour/composition-formats
author: D2 チーム（d2lang。旧 Terrastruct、Hack Club の fiscal sponsorship）
published: v0.9.0（2026-09-07）
retrieved: 2026-11-09
sources:
  - https://github.com/d2lang/d2/blob/master/README.md
  - https://github.com/d2lang/d2/blob/master/ci/release/changelogs/v0.9.0.md
  - https://github.com/d2lang/d2/blob/master/docs/INSTALL.md
  - https://github.com/d2lang/d2/blob/master/d2renderers/d2animate/d2animate.go
  - https://github.com/d2lang/d2-docs/blob/master/docs/tour/composition-formats.md
  - https://github.com/d2lang/d2-docs/blob/master/docs/tour/steps.md
  - https://github.com/d2lang/d2-docs/blob/master/docs/tour/exports.md
  - https://github.com/d2lang/d2-docs/blob/master/docs/tour/fonts.md
  - https://github.com/d2lang/d2-docs/blob/master/docs/tour/man.md
  - https://github.com/d2lang/d2-docs/blob/master/docs/tour/tala.md
  - https://github.com/d2lang/d2/issues/517
---

# D2: steps で段階的に組む図と、その書き出し

## 何の文献か

D2（MPL-2.0）の README、v0.9.0 のリリースノート、INSTALL.md、段の切り替えを作るソース（`d2animate.go`）、公式 docs の元の Markdown（d2-docs repo の composition-formats・steps・exports・fonts・man・tala）、日本語・中国語のフォントに関する issue #517。repo は terrastruct/d2 から d2lang/d2 に移り、サイトの末尾に「Hack Club が fiscal sponsor の独立した OSS」とある。GitHub の最新リリースは v0.9.0（2026-09-07）。一次資料のみ。

## 書いてあること

### 段階表示の材料: boards（layers・scenarios・steps）

- 「Step は一連の出来事の一段を表す。各 Step は前の Step を引き継ぐ。最初の Step は親（Scenario か Layer）を引き継ぐ」。docs の例では Step 3 に書いていない「Approach road」が Step 2 から引き継がれて出る（steps.md）
- 複数の board からなる図の書き出し（composition-formats.md）:
  - **複数の SVG**（既定）: 「ファイルシステム上にディレクトリとファイル名で整理して」出す
  - **アニメする 1 枚の SVG**: `--animate-interval=1200` で「各 board に 1200ms とどまる」アニメになる。「少ない Steps や Scenarios の切り替えには良いが、board が多すぎると見る人が混乱したりループを待ったりする」
  - **アニメする GIF**: 同じものを SVG が描けない場所向けに
  - **PDF**（board ごとに 1 ページ）と **PowerPoint**（`.pptx`、Google Slides でも開ける）
- man: `--animate-interval` は「SVG と GIF の書き出しにだけ使える。GIF は指定しなければ 1000ms」。`--target` で描く board を選べる（`--target='layers.x.*'` で layer x とその子を全部）
- exports.md: GIF は「数秒でループする、見る人がめくらなくても消化できる短い composition 向け」

### 切り替えの実装（ソース）

- `d2animate.go` は各 board を `<g style="animation: d2Transition-… <board 数×間隔>ms infinite">` で包み、`@keyframes` で opacity を 0→1→0 にする。遷移の長さは `transitionDurationMS = 1`（1ms）。つまり**段の切り替えは瞬間で、無限ループの CSS animation**

### v0.9.0（2026-09-07）の変更

- 「TALA は OSS になり D2 に同梱。`--layout=tala` で選ぶ。別のプラグインの導入もライセンスキーも要らない」「PNG・GIF・PDF・PPTX を内蔵の描画器で出す」（リリースノート）。exports.md も「PNG の書き出しは外部依存が無い。Mermaid のように Chromium で描いてスクリーンショットを撮るのではない」と書く
- SVG の描画は「E2E の題材で約 10 倍速く」、Markdown のラベルを `foreignObject` でなく SVG で描くようになった（同）
- README: 同梱のレイアウトは Dagro（既定。Dagre の Go 移植）・elk-go・TALA。手描き風（`--sketch`）は Rough.js 4.6.6 の Go 移植、LaTeX は MathJax 3.2.2 の Go 移植
- TALA の短所として docs は「乱数を持つ。ラベルの小さな変更が全く違う配置に波及しうる」（tala.md）。TALA の README（d2talalayout）は「seed を指定した試行を決定的に選ぶ」と書く

### 日本語フォント

- D2 の既定は Source Sans Pro。issue #517（2022-12）は「Source Sans Pro は漢字を含まない」とし、2023-04 に「フォントを指定できるようになったので不要」として閉じた
- `--font-regular`・`--font-bold`・`--font-italic`・`--font-semibold` に `.ttf` を渡す。「全部渡すか何も渡さないか」を勧め、一部だけなら残りは Source Sans Pro に戻る。`--sketch` のときに渡したフォントは手描き風のフォントを置き換える（fonts.md）

### 入れ方

- install.sh（`--dry-run` で何をするか表示）、`go install github.com/d2lang/d2@latest`、GitHub Releases のビルド済み、Windows は `.msi`。INSTALL.md は「WSL でも普通の Linux と同じに動く」と書く

## この wiki への含意

- **段階表示が言語に入っている**: Mermaid（[[web-means-diagram-mermaid]]）は段階表示を持たないが、D2 は steps で「前の段に足していく」図を書ける。embed の「一つの概念を段を追って組み立てる」にそのまま当たる
- **ただし `--animate-interval` の出力は動画の材料としては粗い**: 切り替えは 1ms（実質カット）で、無限ループ。流しっぱなしの embed で使うなら、段ごとの SVG（既定の複数 SVG 出力）を受け取り、自分の `renderFrame(f)` で段を重ねて opacity をイージングで上げる（[[exp-html-capture-pipeline]] の型）か、ffmpeg の `xfade` でつなぐほうが、Lasseter の Timing・Staging（[[web-motion-lasseter-1987-principles-of-traditional-animation]]）を自分で決められる（推測）
- アニメ SVG を撮るなら CSS animation なので `document.getAnimations()` → `currentTime` でシークできる（MDN の記述からの推測。[[web-means-diagram-mermaid]] と同じ方法）
- **配置が段ごとに動くか**: 各 board を別々にレイアウトするなら、段が進むと前の段の箱の位置が変わりうる（推測。docs に記述なし）。変わると「足していく」感じが壊れる。TALA は `top`・`left` で位置を固定できる（tala.md）ので、必要なら TALA で固定する
- **PPTX の書き出し**は talk（スライドで話す）に直接効く。西尾の LT は HTML スライド（[[exp-lt-20260909]]）で、PPTX の経路は使っていない
- 内蔵描画で Chromium が要らないので、galleria・Mac のどちらでも同じ PNG が出やすい（推測。フォントを `.ttf` で渡す前提）。[[web-timesnap-timecut-hyperframes-webcodecs]] が書く「フォントと Chrome の版の差で 1 画素ずれる」問題を避けやすい

## 着手の仕方（未検証。galleria で確かめる）

- **増える表現**: 箱と矢印の図が段ごとに組み上がる embed（30〜60 秒、5〜8 段）。同じ `.d2` から talk 用の PPTX・PDF も出る
- **機械**: galleria WSL（Go のバイナリ 1 つ）。Windows の `.msi` でも可。Mac でも可
- **入れるもの**: d2 v0.9.0（2026-09-07）。日本語用に Noto Sans JP の static TTF（SIL OFL。Google Fonts から。regular/bold の 2 つ以上）。費用 0、アカウント不要、MPL-2.0
- **成熟度**: v0.9.0 で大きな変更（TALA 同梱・内蔵描画）が入ったばかり。描画器が新しいので、PNG で崩れる図があるかもしれない（推測）
- **最小の手順**（WSL）
  1. `curl -fsSL https://d2lang.com/install.sh | sh -s -- --dry-run` で中身を見てから `| sh -s --`。`d2 version` が `v0.9.0`
  2. `mkdir -p ~/video-tools-trial/d2/fonts && cd ~/video-tools-trial/d2`、`fonts/` に NotoSansJP-Regular.ttf・NotoSansJP-Bold.ttf を置く
  3. `concept.d2` に 3〜5 段の steps を書く（例: `steps: { 1: { 入力 } 2: { 入力 -> 処理 } 3: { 処理 -> 出力 } }`。構文の細部は steps のページの例に合わせる）
  4. 段ごとの書き出し: `d2 --font-regular=fonts/NotoSansJP-Regular.ttf --font-bold=fonts/NotoSansJP-Bold.ttf --font-semibold=fonts/NotoSansJP-Bold.ttf --font-italic=fonts/NotoSansJP-Regular.ttf --pad 80 concept.d2 out/concept.svg`（複数 board なので `out/` の下に段ごとの SVG が出るはず）
  5. 目で見る用: 同じ引数に `--animate-interval=1500` を付けて `concept.gif`
  6. 動画: 段ごとの SVG を `<img>` で重ねた HTML に `renderFrame(f)` を書き、各段を 0.4 秒かけてフェードインさせ、既存の capture.mjs で撮る。手早く済ませるなら PNG を段ごとに出して `ffmpeg -loop 1 -t 4 -i s1.png -loop 1 -t 4 -i s2.png -filter_complex "[0][1]xfade=transition=fade:duration=0.4:offset=3.6" …`
- **動いたと言える確かめ方**: (1) `out/` に段の数だけ SVG/PNG がある、(2) PNG に日本語が出て豆腐が無い、(3) 同じ入力で 2 回描いた PNG の sha256 が一致（決定的か）、(4) 段 2 の PNG で段 1 の箱が同じ位置にあるか（差分画像で確かめる: `ffmpeg -i s1.png -i s2.png -filter_complex blend=all_mode=difference diff.png`）
- **所要の見込み（推測）**: 入れて最初の図まで 15 分、steps の図と mp4 まで 2 時間

## Open Questions

- 段ごとにレイアウトが変わるか（位置の跳び）。dagre・ELK・TALA で違うか
- 複数 board を PNG で出すときのファイルの並び・名前（composition-formats は SVG について書く）
- 内蔵描画器（v0.9.0）の PNG で、`.ttf` の日本語フォントが正しく測られ・描かれるか。issue #513（2 バイト文字の幅の計算が合わない、閉じている）・#1556（Windows で漢字の bold が効かない、開いている）があった
- `--sketch`（手描き風）と日本語フォントを組み合わせると、手描きの線に普通の字形が乗る。Excalidraw（[[web-means-diagram-excalidraw-animate-tldraw]]）の手描きの字形とどちらが合うかは見ていない
