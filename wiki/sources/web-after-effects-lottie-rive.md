---
type: source
summary: After Effects のエクスプレッション（「プロパティが何であるか」を時刻の式で書く）と ExtendScript（「アプリに何をさせるか」を書くスクリプト）、AE から Bodymovin で JSON に書き出して Web で再生する Lottie、エディタとランタイムが分かれた Rive の一次資料。プログラム系と手作業系の分担については、Manim の作者 Grant Sanderson が「個々のクリップを作る道具。編集・ナレーション同期は普通の動画編集ソフトで」と書き、Remotion は AE の作品を Lottie で取り込む手順を公式に出している
video_types: [promo, any]
url: https://ae-scripting.docsforadobe.dev/introduction/overview/
author: Adobe（After Effects Scripting Guide、docsforadobe による公開版）、airbnb（lottie-web）、Rive、Remotion AG、Grant Sanderson（3Blue1Brown）
published: unknown（各 docs は継続更新。lottie-web 最終 push 2025-09-01）
retrieved: 2026-11-09
sources:
  - https://github.com/docsforadobe/after-effects-scripting-guide/blob/master/docs/introduction/overview.md
  - https://github.com/docsforadobe/after-effects-expression-reference/blob/master/docs/index.md
  - https://github.com/docsforadobe/after-effects-expression-reference/blob/master/docs/general/random-numbers.md
  - https://github.com/airbnb/lottie-web/blob/master/README.md
  - https://www.remotion.dev/docs/after-effects.md
  - https://www.remotion.dev/docs/rive/index.md
  - https://github.com/rive-app/rive-wasm/blob/master/README.md
  - https://www.3blue1brown.com/faq
  - https://github.com/motion-canvas/motion-canvas/blob/main/packages/docs/docs/intro.md
  - https://www.buildwithmatija.com/blog/remotion-vs-motion-canvas-code-driven-video
---

# After Effects・Lottie・Rive と、プログラム系との分担

## 何の文献か

- After Effects Scripting Guide と Expression Reference: Adobe の公式ガイドを docsforadobe（有志）が Markdown で公開・保守している版。Adobe の helpx の Expression basics ページは JavaScript で描かれていて本文を取れなかった。
- lottie-web（airbnb、MIT）の README。
- Rive の Web ランタイム（rive-wasm、MIT）の README。Rive のエディタ本体の規約は読んでいない。
- Remotion の公式ドキュメント「Import from After Effects」「@remotion/rive」。
- 分担について書いた実務家: Grant Sanderson（3Blue1Brown）の FAQ。ほかに Matija Žiberna の個人ブログ（2026-10）。モーションデザイナー側から「AE とコードをどう分けるか」を書いた一次の文章は、今回の検索では見つけられなかった（Medium の記事は 403、Lottie 関連はほとんどがベンダーの宣伝）。

## 書いてあること

### After Effects のエクスプレッションとスクリプト

- Scripting Guide の Overview: 「エクスプレッション言語と ExtendScript はどちらも JavaScript に基づくが、別物。エクスプレッションはスクリプトの情報（変数や関数）にアクセスできない。**スクリプトはアプリに何かをせよと言い、エクスプレッションはプロパティが何であるかを言う**」。
- ExtendScript は Photoshop・Illustrator・InDesign と共通の JavaScript の拡張で、ECMA-262 第 3 版に対応する。スクリプトで「レイヤーを並べ替える、テキストレイヤーの文字を一括置換する、レンダリングが終わったらメールを送る」ことができ、「スクリプトでできることのほとんどは GUI でできることの再現」と書く。プロジェクト・アイテム・コンポジション・レイヤー・レンダーキューのオブジェクトモデルを操作する。
- Expression Reference: エクスプレッションは AE の要素と標準の JavaScript で書き、ピックウィップでプロパティを挿入できる。`random()` の seed は「既定でレイヤーの一意な識別子・レイヤー内のプロパティ・現在の時刻・オフセット 0 の関数」で、`seedRandom(offset, timeless)` で変えられる。つまり同じ時刻なら同じ乱数になる。

### Lottie（AE → JSON → Web・アプリで再生）

- lottie-web README: 「Lottie は Bodymovin で JSON に書き出した After Effects のアニメを読み、モバイルでネイティブに描くライブラリ」「デザイナーが、エンジニアが手で作り直す苦労なしに、美しいアニメを作って**出荷**できる」。Web の描画は `svg`・`canvas`・`html` から選ぶ。`goToAndStop(value, isFrame)` で特定の時刻・フレームへ移動できる。
- 対応する AE の機能（README「AE Feature Support」）: プリコンポーズ・シェイプ・平面・画像・ヌル・テキスト、マスク（他のモードは「性能への打撃が大きい」）、タイムリマップ、エクスプレッション（wiki ページ参照）。**非対応: 画像連番・動画・音声**。負のレイヤー伸縮は不可。
- Remotion の「Import from After Effects」: AE に Bodymovin を入れ、「スクリプトによるファイルへの書き込みとネットワークへのアクセスを許可」を有効にし、コンポジションを JSON に書き出し、Remotion の `<Lottie animationData={...}/>` で読み込む。「Remotion のコンポジションの名前は After Effects がこの用語を作ったことから来ている」「元の AE のコンポジションと同じ大きさ・尺にすることを勧める」。

### Rive（エディタ ＋ ランタイム）

- rive-wasm README: Rive は「ゲーム・アプリ・対話的な UI のための agent-native な 2D・3D エンジン」。Rive CLI でコーディングエージェントから作るか、Rive Editor で描き・リグを組み・手でアニメを付ける。「両方が同じファイルを扱う」。`.riv` を Web・モバイル・ゲームエンジンなどで再生。ランタイムは OSS（MIT）で、「ロイヤリティもランタイム料金も無い」。状態機械（state machine）を持つ。
- Remotion は `@remotion/rive` で Rive のファイルを動画に組み込める（Remotion License が適用）。

### 分担について実務家が書いたこと

- **Grant Sanderson（3Blue1Brown FAQ）**: 「Blender や After Effects のようなプロのアニメ道具もプログラムで動かせる。数学以外のアニメも多く要るなら、先にそちらを調べる価値がある」「"ナレーションを manim の中でどう同期させるか" と聞かれると心配になる。これは個々のクリップを作って後で編集でつなぐための道具にすぎない。できるだけ普通の動画編集ソフトを使うべき」。正確さ・繰り返し・抽象化が効く絵ならコード、GUI が欲しいなら他の道具、という目安も書く（詳しくは [[web-manim]]）。
- **Motion Canvas の docs**: 「従来の動画編集ソフトの代わりではない」（[[web-motion-canvas]]）。
- **Žiberna のブログ（2026-10）**: 「キャラクターアニメ、物理の重いベクターのシミュレーション、複雑なパスのモーフィングが要るなら Remotion を使うな。DOM は文書のレイアウトには優れるが、幾何の動きには非効率」。コード系の中での分担の話で、AE との分担には触れない。

## この wiki への含意

- **AE のエクスプレッションも「時刻の関数」**: 「エクスプレッションはプロパティが何であるかを言う」「乱数の seed は時刻とレイヤーの関数」は、[[exp-html-capture-pipeline]] の `renderFrame(f)` の純関数・seed 固定の乱数と同じ考え方。違いは、AE ではキーフレームを手で置いた上に式を部分的に足すことで、コード系では全部を式で書くこと。
- **手作業系とコード系の分け方の候補**（文献から読める範囲で）:
  - 手で形と動きを詰めたい部品（キャラクター、ロゴのアニメ、複雑なイージング）は AE / Rive で作り、Lottie・`.riv` で書き出して、コード側（[[web-remotion]]・[[web-timesnap-timecut-hyperframes-webcodecs]] の HyperFrames は Lottie をシークできる）で時刻表に並べる。
  - 文字・数値・図・データが中身で、作り直しが多いものはコードで書く（[[exp-gyazo-resumption-video]]・[[exp-words-as-public-goods-video]] のような字幕・図形中心の動画）。
  - ナレーションとの同期・カットの並べ替えは、Grant は動画編集ソフトで、西尾は時刻表とコードで行っている。
- **西尾の制作との違い**: 西尾の機械には AE が無く（記録に出てこない）、全部コードで AI（Claude Code・Codex）が書いて回した。手作業系の道具はエージェントが直接操作しにくい（ExtendScript で AE を外から動かす経路はあるが、試した記録は無い）。Rive が「agent-native」「Rive CLI でエージェントから」と書き始めているのは、この境目を道具側が動かそうとしている例。
- **promo 型への効き方**: [[exp-polis-magi-op]] が「腰を据えないとできない」で止まったように、promo の作り込み（カット密度・質感・メロディ）はコードだけでは時間がかかった。手で詰める部品を AE/Rive に分ける選択肢は、この wiki の経験にはまだ無い。

## Open Questions

- モーションデザイナーが「AE とコードをどう分けているか」を書いた一次の文章を見つけられていない（Lottie の handoff の記事はベンダーのものが多い）。探し直す価値がある。
- Lottie は音声・動画・画像連番に非対応で、AE の効果の多くも落ちる。どの程度の作り込みまで Lottie で持ち出せるかは、実際に書き出して確かめていない。
- Rive のエディタの利用規約・価格（ランタイムは MIT だが、エディタは商用サービス）は読んでいない。
- After Effects の CLI レンダリング（aerender）や ExtendScript をエージェントから回す実務の記録は読んでいない。
