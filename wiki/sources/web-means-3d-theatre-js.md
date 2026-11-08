---
type: source
summary: Theatre.js（ブラウザのモーションデザインの編集画面とアニメのライブラリ）の一次資料。three.js などの値をシーケンスエディタ・グラフエディタでキーフレームとして手で詰め、状態を JSON で書き出して @theatre/core で再生する。再生位置は sheet.sequence.position に秒で代入できるので 1 コマずつ撮れる。core は Apache-2.0、studio は AGPL-3.0。公開の最新は 0.7.2（2024-05-19）で、README は「1.0 のため開発を一時的に非公開の repo へ移した」と書いたまま 2026-11 時点で 1.0 は出ていない
video_types: [promo, talk, embed]
url: https://github.com/theatre-js/theatre
author: Theatre.js Oy（Aria Minaei ほか、ヘルシンキ）
published: unknown（README の 1.0 告知の commit は 2024-04-11、最新の公開版 0.7.2 は 2024-05-19）
retrieved: 2026-11-09
sources:
  - https://github.com/theatre-js/theatre/blob/main/README.md
  - https://registry.npmjs.org/@theatre/core
  - https://registry.npmjs.org/@theatre/studio
  - https://registry.npmjs.org/@theatre/r3f
  - https://www.theatrejs.com/
  - https://www.theatrejs.com/docs/latest/api/core （#sequence.position）
  - https://www.theatrejs.com/docs/latest/manual/projects
  - https://www.theatrejs.com/docs/latest/manual/sequences
  - https://www.theatrejs.com/docs/latest/getting-started/with-three-js
---

# Theatre.js — 手で詰めるシーケンスエディタ付きのアニメ

## 何の文献か

- 作り手（Theatre.js Oy）の GitHub の README、公式サイト、公式 docs（manual・API・three.js との始め方）。宣伝を含む作り手の説明で、使った人の評価や測定ではない。
- 状態は GitHub API と npm で確かめた（2026-11-09）: repo は star 12,947、**最終 push 2024-08-14**、main の最新 commit は 2024-04-11「Add the 1.0 notice」、0.7.x ブランチの最新は 2024-05-19「Public API for changing length/fps of a sequence」。npm の最新は **@theatre/core・@theatre/studio・@theatre/r3f とも 0.7.2（2024-05-19）**。公式ブログの最新の記事は 2022 年のもの。docs の repo（theatre-docs）の最終 push は 2022-09-29（今の docs は公式サイト側にある）。

## 書いてあること

- README: 「高精細なモーショングラフィックスのためのアニメのライブラリ。細かなアニメを表現し、入り組んだ動きを作り、ニュアンスを伝える」「**プログラムからも視覚的にも使える**」。用途に「THREE.js などの 3D の物体」「React などを通じた HTML/SVG」「マイクロインタラクション」「生成的な対話的アート」「その他の任意の JS の変数」。
- README の告知: 「**Theatre.js 1.0 が近い。速く回すため、開発を一時的に非公開の repo に移した。作業は近くこの公開 repo に戻す。条件とライセンスはこれまでどおり OSS**」（2024-04-11 の commit）。2026-11-09 時点で npm の版は 0.7.2 のまま。
- 公式サイト: シーケンスエディタ（「数秒で場面を組む。プリセットで味付けし、準備ができたらグラフエディタで全コマを詰める」）、ドープシート、グラフエディタ、イージングのプリセット、アウトライン、プロパティエディタ、拡張。「**コードか、ではなく、コードと絵（Code vs plus Art）**。コードで作り、ブラウザで仕上げる」。
- ライセンス（README）: 「core（`@theatre/core`）は Apache License。リポジトリの大半のパッケージも同じ」「**studio（`@theatre/studio`）は AGPL 3.0**。アニメの編集・場面の設定に使うパッケージ。**studio は設計・開発の間だけ使う。最終のバンドルには `@theatre/core` だけが入るので、Apache License だけが適用される**」。
- 状態の保存（manual「Projects」）: 「作ったつまみやアニメは全部プロジェクトの state。`@theatre/core` は state を使ってアニメを動かし、`@theatre/studio` は state の編集画面。studio を開いている間は state は **`localStorage` に JSON で保存され、JSON ファイルに書き出せる**」。書き出しはアウトラインのプロジェクト名 →「Export」。読み込みは `getProject('My Project', { state: projectState })`。studio を使っている間は読み込みが非同期で、`project.ready` を待つ。
- 再生位置（API「#sequence.position」）: 「再生ヘッドの現在位置。時間ベースのシーケンスでは**秒**」。例: `sheet.sequence.position = 1`（1 秒の位置に置く）。ほかに `play`（位置・繰り返し・方向）、`pause`、`pointer`（`onChange` で値の変化を見る）、`attachAudio`（音をシーケンスに付けて同期させる）。0.7.x の最後の commit で「シーケンスの長さ・fps を変える公開 API」が足された。
- three.js との始め方: Vite の雛形を clone → `npm install --save @theatre/core @theatre/studio` → `studio.initialize()` → `getProject` → `project.sheet(...)` → `sheet.object('Torus Knot', {rotation: types.compound({...})})` で three.js の物体のつまみを作り、`onValuesChange` で `mesh.rotation` に写す、という流れ。React Three Fiber 用には `@theatre/r3f` がある。

## この wiki への含意

- **西尾の方式にない「手で詰める」層**: 西尾は時刻表（showreel の `TL` の表: 開始・長さ・イージングの行の並び）とイージングの関数をコードで書き、AI に書かせた（[[exp-html-capture-pipeline]]）。Theatre.js は同じ値をグラフエディタで手で詰め、結果を JSON にする。**AI がコードで骨組みを作り、人がブラウザで動きの曲線だけ直し、その JSON を AI のコードが読む**という分担ができる（推測）。[[web-after-effects-lottie-rive]] の「手作業系とコード系の分け方」の、ブラウザの中で閉じる版。
- **撮影との相性はよい**: 状態は JSON、再生位置は `sequence.position = 秒` の代入なので、`renderFrame(f)` の中で `sheet.sequence.position = f / FPS` → three.js を描く、で純関数の契約を守れる（推測）。撮影時は studio を読み込まず core だけ使えば、編集画面は映らず、ライセンスも Apache-2.0 の側だけになる（README の説明から）。
- **Remotion・HyperFrames・OpenFilm も「人が後から直せる編集画面」を足した**（[[web-opus2-remotion-openfilm-manim-after-2026-09-22]]）。Theatre.js はその考えを 2021 年ごろから持っていた道具だが、2024 年から公開の開発が止まっている。
- **リスク**: 0.7.2 から 2 年半、版が出ていない。1.0 の告知は 2024-04。three.js の新しい版（r187）との組み合わせで壊れていないかは分からない。新しく覚える道具としては、止まっている前提で扱う。

## 着手の仕方（未検証。galleria で確かめる）

- **何が表現できるようになるか / 効く型**: three.js（または DOM・SVG・任意の JS の値）の動きを、グラフエディタでキーフレームとイージング曲線を手で詰める。カメラワーク・物体の入りの細かな間合い。promo（作り込み）に一番効く。talk・embed では「AI の書いた動きの間合いを人が直す」用途
- **機械**: 編集は画面が要るので **galleria Windows のブラウザ**か **Mac**。撮影は [[web-means-3d-threejs-headless-webgl]] と同じ（galleria Windows、GPU）。入れるもの: `@theatre/core@0.7.2`・`@theatre/studio@0.7.2`（`@theatre/r3f@0.7.2` は React Three Fiber のとき）、`three`、Vite。費用 0、アカウント不要。ライセンス: core は Apache-2.0、studio は AGPL-3.0（編集時だけ使う）
- **成熟度**: 公開の最新 0.7.2（2024-05-19）。公開の開発は止まっている（README の 1.0 告知のまま）
- **最小の手順（Windows の PowerShell。公式の始め方に沿う）**:
  ```powershell
  cd $HOME\video-tools-trial
  git clone https://github.com/fulopkovacs/vanilla-threejs-project theatre-trial; cd theatre-trial
  npm install
  npm install --save @theatre/core@0.7.2 @theatre/studio@0.7.2
  # main.ts に studio.initialize()、getProject('Trial')、sheet.object(...) を足す（公式の始め方の手順）
  npm run dev   # ブラウザで開き、シーケンスエディタでキーフレームを 2 つ打ち、Export で state.json を保存
  # 撮影用のページ（推測）: studio を import せず、getProject('Trial', { state }) → await project.ready
  #   window.renderFrame = f => { sheet.sequence.position = f / FPS; renderer.render(scene, camera); };
  ```
- **動いたと言える確かめ方**: (1) Export した `state.json` に打ったキーフレームの値が入っている、(2) 撮影用ページで f=0 と最後のコマの静止画が、エディタで見た最初と最後の姿勢と一致、(3) 撮った画面に studio の UI が映っていない、(4) 同じ f を 2 回撮って `cmp` が一致
- **所要の見込み（推測）**: three.js の最小例が動いた後なら半日。r187 との相性で詰まればそれ以上

## Open Questions

- 0.7.2 と three.js r187 の組み合わせで動くか（Theatre.js は three.js を直接は依存に持たない作りに見えるが、`@theatre/r3f` は React Three Fiber の版に依存する。確かめていない）
- 1.0 がいつ公開されるか、ライセンスが「これまでどおり OSS」のままか。2024-04 の告知のみ
- AGPL の studio を編集時だけ使って作った動画を外に出すことは、README の説明では問題にならないと読めるが、条文の解釈はしていない
- 手で詰めた JSON を、AI が後で書き換えるとき（キーフレームの時刻をナレーションに合わせて動かすなど）に、人の詰めが壊れないか。分担の境目は試していない
