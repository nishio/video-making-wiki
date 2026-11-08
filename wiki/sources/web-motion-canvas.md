---
type: source
summary: Motion Canvas の公式ドキュメント。TypeScript の generator で「yield ＝ このコマは描けた」として時間を書き、エディタでリアルタイムにプレビューし、ナレーションの合図を waitUntil の時刻イベントとしてエディタ上でドラッグして合わせる、説明用ベクターアニメの道具（MIT）。動画編集ソフトの代わりではないと自ら書く
video_types: [talk, embed]
url: https://motion-canvas.io/docs/（ハイフンあり。ハイフンなしの motioncanvas.io は別の会社のサイト。本文は GitHub の docs ソースで読んだ）
author: motion-canvas（OSS プロジェクト。docs は GitHub motion-canvas/motion-canvas の packages/docs）
published: unknown（docs は継続更新。最新リリース v3.17.2 は 2024-12-14、v3.18.0-alpha.0 は 2025-02-16）
retrieved: 2026-11-09
sources:
  - https://github.com/motion-canvas/motion-canvas/blob/main/packages/docs/docs/intro.md
  - https://github.com/motion-canvas/motion-canvas/blob/main/packages/docs/docs/getting-started/flow.mdx
  - https://github.com/motion-canvas/motion-canvas/blob/main/packages/docs/docs/getting-started/time-events.mdx
  - https://github.com/motion-canvas/motion-canvas/blob/main/packages/docs/docs/getting-started/media.mdx
  - https://github.com/motion-canvas/motion-canvas/blob/main/packages/docs/docs/getting-started/rendering/index.mdx
  - https://github.com/motion-canvas/motion-canvas/blob/main/packages/docs/docs/getting-started/rendering/video.mdx
  - https://github.com/motion-canvas/motion-canvas/blob/main/packages/docs/docs/getting-started/rendering/image-sequence.mdx
  - https://github.com/motion-canvas/motion-canvas/blob/main/packages/docs/docs/advanced/random.mdx
  - https://github.com/motion-canvas/motion-canvas/blob/main/packages/docs/docs/components/latex.mdx
  - https://github.com/motion-canvas/motion-canvas/blob/main/packages/docs/docs/getting-started/presentation.mdx
  - https://github.com/motion-canvas/motion-canvas/blob/main/LICENSE
  - https://www.buildwithmatija.com/blog/remotion-vs-motion-canvas-code-driven-video （実務ブログ、2026-10-02）
---

# Motion Canvas（generator で時間を書く説明アニメ）

## 何の文献か

Motion Canvas の公式ドキュメント（GitHub の `packages/docs/docs/*.mdx` を原文で読んだ）と LICENSE（MIT、Copyright (c) 2022 motion-canvas）。比較の観点として、Matija Žiberna の実務ブログ「Remotion vs Motion Canvas: The Two Mental Models of Code-Driven Video」（2026-10-02 公開、10-06 更新）も使った。後者はフロントマターに `llm-purpose` 欄を持つ、LLM に読ませることも意識した個人ブログで、検証データは無い。

GitHub のスター数は約 2.0 万、最新の正式リリースは v3.17.2（2024-12-14）、その後は v3.18.0-alpha.0（2025-02-16）で、最後の push は 2026-07-02（API 値）。リリースの間隔が空いている。

## 書いてあること

### 位置づけ

- 「TypeScript のライブラリ（generator でアニメをプログラムする）と、それをリアルタイムにプレビューするエディタの 2 つから成る」「説明的なベクターアニメを作り、ナレーションと同期させるための専門の道具。従来の動画編集ソフトの代わりではない」と書いている（`intro.md`）。

### 1 コマの描き方と時間（generator）

- 「`yield` は "このコマは描けた。画面に出して、後で戻ってきて" という意味」と書く（`flow.mdx`）。シーンは `makeScene2D(function* (view) {...})` で、`yield*` で別の generator（tween）に任せる。`yield* circle().fill('#e6a700', 1)` は 1 秒かけて色を変える tween。`all`・`any`・`chain`・`delay` などの flow generator で組み合わせる。
- 描画は HTML の canvas（DOM・CSS は使わない）。JSX を使うが React ではなく、独自の JSX runtime で canvas のシーングラフを作る（Žiberna のブログ。公式 docs の hierarchy の章は未読）。
- 乱数: `useRandom()` はシーンごとの乱数生成器で「`Math.random()` と違い完全に再現可能。再生のたびに同じ値になる。seed は各シーンの meta ファイルに保存される」と書く（`random.mdx`）。
- フレームレートを変えても「ほとんどのアニメは影響を受けない」（rendering の Frame rate の項）。プレビューと書き出しで Scale・Frame rate を別に設定できる。

### 音に合わせる（time events）

- 「コードで説明アニメを作るときの悩みの一つが音声との同期」と書き、`yield* waitFor(3.1415)` のように秒を直書きすると「ナレーションを直すたびにコード中の数字を全部直すことになる」と問題を挙げる（`time-events.mdx`）。
- 代わりに `yield* waitUntil('event')` と書くと、エディタのタイムラインに「event」の札が出て、ドラッグで時刻を動かせる。既定では 1 つを動かすと後ろのイベントも一緒にずれる（Shift で単独）。`useDuration('event')` でイベントの長さをアニメの長さに使える。
- 音声はプロジェクトに 1 本の音声ファイルを `audio` として指定する（`media.mdx`）。書き出し設定に Audio offset（秒）がある。FFmpeg の exporter に「Include audio」がある。

### レンダリング

- エディタの `RENDER` ボタンを押すと「Motion Canvas がアニメを再生し、結果を `/output` に保存する」（`rendering/index.mdx`）。既定の exporter は画像連番（PNG・JPEG・WebP。形式はブラウザの機能に依存）。`@motion-canvas/ffmpeg` を入れると MP4 を書く exporter が使え、FFmpeg は自動で入る。「まだ比較的新しく、必要な機能が無いかもしれない」と書く（`rendering/video.mdx`）。
- Range で一部のフレームだけ描ける。カメラアイコンで現在のコマのスナップショットを `/still` に保存できる。
- コマンドラインから描く方法は、読んだ範囲の公式 docs には無い（エディタのボタンから）。これが [[web-revideo]] の fork の理由の一つ。

### その他

- LaTeX: `<Latex tex="..."/>` で数式を出し、`{{...}}` で区切った部分ごとに式の変形をアニメできる。「`fill` を必ず指定しないと何も表示されない」と注意がある（`latex.mdx`）。
- presentation: `beginSlide()` で区切ると、エディタの Presentation Mode でスライドのように進められる（`presentation.mdx`。詳しくは別担当のページ）。
- ライセンス: MIT。

### 実務ブログの比較（Žiberna 2026）

- 「Remotion は React の DOM のスナップショットを並べ、Motion Canvas は canvas のベクターを手続き的に動かす」「Web の UI が中身なら Remotion、幾何が中身なら Motion Canvas」と書く。数式・アルゴリズム・グラフのノードの説明は Motion Canvas が向く、既存の React 部品や CSS を持ち込みたいなら向かない（DOM が無いので Flexbox も Tailwind も使えない）と書く。根拠は書き手の経験で、測定は無い。

## この wiki への含意

- **時間の書き方の違い**: 西尾の方式（[[exp-html-capture-pipeline]]）は「フレーム番号 → 絵」の純関数と、showreel の `TL`（開始・長さ・イージングの組の配列）のような時刻表。Motion Canvas は「順に起きることを generator で上から書く」方式で、時刻表を手で持たなくてよい。その代わり任意の秒の絵は generator を進めて得ることになる（どう実装しているかは公式 docs で未確認）。
- **音に合わせる方法が逆**: 西尾の方式は BGM を 120BPM の格子に置き、映像も同じ格子に乗せて合わせる作業を要らなくした（[[exp-html-capture-pipeline]]）。台本と声がある talk では、[[exp-qualia-video]] は音声区間（segment）単位の timeline を正にして画面だけを改稿した。Motion Canvas の time events は「声を先に録り、映像の区切りをエディタで声に合わせてドラッグする」方式で、声を作り直すたびに区切りを合わせ直す手作業が残る。TTS の区間の長さから時刻を自動で決める（[[exp-html-capture-pipeline]] の英語版 `timing.py` のやり方）なら time events は要らない。
- **型**: 自ら「説明的なベクターアニメ」と書いており、talk の中の図解や embed（特定概念を説明する短いアニメ）に向く。promo の粒子・写真・映像素材の多用は主目的ではない。
- **エージェントに書かせるとき**: 書き出しがエディタのボタンなので、エージェントが自分でレンダリングして画像を確かめる経路は公式には無い。この点は [[web-revideo]] の headless レンダリングや、[[web-remotion]] の CLI と違う。

## Open Questions

- リリースが 2024-12 の v3.17.2 から止まっている（alpha が 2025-02）。今から使い始めて保守されるかは不明。
- generator 方式でシーク（任意の秒へ飛ぶ）をどう実現しているか、書き出しが決定論的かを公式 docs で確かめていない（`useRandom` の再現性の記述だけ）。
- 音声が 1 本だけという制約が、TTS の区間ごとの WAV を並べる [[exp-qualia-video]] のような作り方とどう合うか（事前に 1 本に繋げれば済むが、区間を動かすたびに作り直しになる）。
