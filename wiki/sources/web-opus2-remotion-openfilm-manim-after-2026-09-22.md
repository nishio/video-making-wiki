---
type: source
summary: 2026-09-22 以後の、HyperFrames 以外の描画の道具の公式の動き。Remotion は 15 リリースで、agent skill を「プレビューを先に開く」「静止画で確かめる」「人が後で直せるタイムライン」に寄せ、UI を高解像度で録る Canvas Capture と字幕の部品を足した。新しい OSS の OpenFilm（10-04 作成）は「フレームワーク無し、`frame(t)` 一つ」を掲げ、確認（2 通りの順で描いて一致を見る）に力を置く。Manim CE と Motion Canvas には LLM 向けの公式の変化は見当たらない
video_types: [any]
url: https://github.com/remotion-dev/remotion/releases
author: Remotion AG（release notes・PR・skills）、OpenFilm（README）、Manim Community（release notes）、motion-canvas（commit 履歴）
published: 2026-09-22〜2026-11-08
retrieved: 2026-11-09
sources:
  - https://github.com/remotion-dev/remotion/releases （v4.0.527 2026-09-22 〜 v4.0.541 2026-11-05）
  - https://github.com/remotion-dev/remotion/pull/11498 （Skills: visual checks、2026-09-22）
  - https://github.com/remotion-dev/remotion/pull/11788 （Skills: editable timeline、2026-09-29）
  - https://github.com/remotion-dev/remotion/pull/11837 （Skills: Studio を先に開く、2026-09-30）
  - https://www.remotion.dev/docs/canvas-capture.md
  - https://www.remotion.dev/docs/canvas-capture/how-to-use.md
  - https://github.com/remotion-dev/remotion/tree/main/packages/skills/skills （remotion-license・remotion-captions の SKILL.md、version 4.0.541）
  - https://github.com/openfilm/openfilm/blob/main/README.md
  - https://github.com/ManimCommunity/manim/releases/tag/v0.22.0
  - https://github.com/motion-canvas/motion-canvas/commits/main
---

# Remotion・OpenFilm・Manim・Motion Canvas の 2026-09-22 以後

Remotion の基本・ライセンス・Agent Skills（v4.0.541 の時点の本文）は [[web-remotion]]、Manim は [[web-manim]]、Motion Canvas は [[web-motion-canvas]]、HyperFrames は [[web-opus2-hyperframes-after-2026-09-22]]。ここは Opus 5.5 の公開以後の変化だけ。

## 何の文献か

- 各プロジェクトの公式の release notes・PR・README・commit 履歴（GitHub の API で取得）。作り手自身の説明で、効果の測定は無い
- Remotion のブログは 2025-09 の記事が最新で、2026 年の投稿は無かった（2026-11-09 に remotion.dev/blog を見た）。変化は release notes と PR から読んだ

## 書いてあること

### Remotion（v4.0.527 2026-09-22 〜 v4.0.541 2026-11-05、15 リリース）

**agent skill の変更（日付は PR のマージ日かリリース日）**

- 09-22（#11498）「visual checks を書き直す」: `remotion-markup` に「見た目の確認が要るときは Remotion Studio を開いて対話的にプレビューする。描画（render）で 1 コマか複数のコマを画像にして見てもよい」、`remotion-render` に `npx remotion render <id> out/frames --frames=0,30,90 --image-format=png` を足した
- 09-29（#11788）「タイムラインをもっと編集しやすく」: 「独立に編集できるタイムラインの要素は、別々の JSX のソースノードが要る」。クリップ・複数場面の作り方を、ソースの持ち主の指針に沿わせる
- 09-30（#11837）「動画を作る前に Studio のプレビューを開く」: 「プロジェクトが動くようになったらすぐ、コンポジションを作る前に Studio を起動してプレビューを開く。作業中ずっと開いておき、ユーザーが変化を見て舵を取れるようにする」（この文言は [[web-remotion]] が v4.0.541 の skill として引いたもの。入ったのがこの日）
- 10-07（v4.0.534）「Canvas Capture の取り込み」、10-19（v4.0.537）「アラビア語と右から左の文字の指針」、11-02（v4.0.540）「`/remotion-license` skill」（ライセンス・FAQ・規約の Markdown 版と購入先を示すだけ）、「グローバルの Claude の skill がプロジェクトの Remotion の skill を隠すときに警告」「AI エージェントと Studio を起動する手順」

**道具の追加**

- **Canvas Capture**（実験的、Chrome 拡張）: 「マイクロインタラクションのための高精細な画面録画」「画面のネイティブ解像度より高い解像度で録れる」「UI の寄りを見せる製品デモに最適」。録った動画を Studio にドラッグすると、映像とカーソルが別々にキーフレームを打てる層になる（`/docs/canvas-capture`）。9 月末〜10 月に取り込み・名前付け・プライバシーの告知が続いた
- **字幕**: Elements（部品の集まり）に基本の字幕（09-09）、角丸の字幕（09-24）、Studio での字幕の様式の選択（10-12、10-19）、Karaoke Captions を製品の資料に（11-05）。`remotion-captions` skill は「字幕はすべて JSON の `Caption` 型（`text`・`startMs`・`endMs`・`timestampMs`・`confidence`）で扱う」と書く
- **HTML-in-canvas**（Chrome 157 の実装に合わせる、ネストがサーバー側の描画で動く、09-30〜10-07）と、Studio のモーションブラー・HTML-in-canvas の操作（09-29）
- Studio に「ChatGPT で注記する」「ChatGPT に送る」（10-07、#11993）: エラーの表示や効果の設定から、ChatGPT にソースと選択の情報を渡す

### OpenFilm（2026-10-04 作成、MIT、14 リリース、スター 5,317）

- README: 「オープンソースの AI 動画エージェント」「One HTML file, one function, one real editor」。コーディングエージェントが映画を Web ページとして書き、ローカルの編集画面（Studio）で形になるのを見せ、人が手でもエージェントにでも直せる
- **「一つの関数」**: 各ショットは `window.film = { frame(t) { … } }` を持つ Web ページで、「t 秒の完全な絵を何でも使って描く」。three.js・WebGL・canvas・SVG・CSS・GSAP・動画などを使ってよい。「フレームワーク（Remotion や HyperFrames のような）は要らない。一つの関数で足りる」
- 「唯一の決まり: 同じ t は、前に何を描いたかにかかわらず必ず同じ絵を描く。コマは順不同・並列・コマの間（モーションブラー用）でも問われる」
- 「OpenFilm はモデルが失敗するところ、つまり映画の確認に力を使う。`look` は板の各コマを 2 通りのシャッフルした順で 2 回描き、変わったものを名指しする。ページのエラー、読み込みに失敗したフォント、無い音のファイル、画面の端で切れた文字も」
- `film.html` は `<section>` をトラック、要素をクリップとし、メディアの断片（`#t=12,18`）と `at` で時刻を書く。書き出しは動画・GIF・音・stem・字幕・静止画・**スライド**・透過動画・Final Cut / Premiere / DaVinci 用のタイムライン
- 「どう映画を作るかは道具でなく skill に置く」。共同の skill の置き場 `openfilm/skills`（10-16 作成）

### Manim Community（v0.22.0 2026-10-08、v0.22.1 2026-10-27）

- v0.22.0 の目玉は、出力の選び方を `--format`（mp4・mov・webm・gif・png・png-sequence・none）一つにまとめたこと、動画の符号化の設定（`--video-codec`・`--encoder-option`）、描画の流れをまとめる `Manager` の導入、小さい文字の描画の改善。LLM・エージェント向けの項目は release notes に無い
- 9/15 以後の commit にも LLM 向けのものは見当たらない（docs の修正など）
- エージェント向けの Manim の skill は第三者のもの: adithya-s-k/manim_skill（2026-01-22 作成、スター 1,282、最終 push 01-23）、HarleyCoops/Math-To-Manim（2025-01 作成、最終 push 2026-11-06）など。中身は読んでいない

### Motion Canvas

- main の最新の commit は 2026-07-02（「docs: ドメインの更新」）。2026-09-22 以後の commit は無い（2026-11-09 の API）。Revideo（fork）の最終 push も 2026-07-15

## この wiki への含意

- **道具の側の動きは「人が後から見て直す」に寄った**: Remotion の skill は 9/22〜30 に「先にプレビューを開いて人に見せ続ける」「静止画で確かめる」「人が編集できるタイムラインにする」を足し、HyperFrames も「描画の前に Studio を開く」（[[web-opus2-hyperframes-after-2026-09-22]]）、OpenFilm は「本物の編集画面」を最初から掲げた。モデルが一回で作れるようになったと言われた時期に、道具は人の確認と手直しの入口を増やしている。[[exp-html-capture-pipeline]] の「全編を撮る前に山場の秒だけ静止画で見る」と同じ向き
- **OpenFilm の `frame(t)` は西尾の方式とほぼ同じ契約**: [[exp-html-capture-pipeline]] の `renderFrame(f)` を時刻の純関数で書く方式、[[web-movez-opus-motion-design-course]] の `seek(t)` と同じ。違いは、OpenFilm が「2 通りの順で描いて一致を確かめる」検査と、ショットを並べるトラック（`film.html`）と編集画面を道具として持つこと。西尾の方式の Open Question「純関数であることを並列化に使っていない」（[[web-remotion]]）に対して、OpenFilm は並列・順不同を前提にしている
- **talk の道具として**: 字幕（Remotion の `Caption` 型と Elements、OpenFilm の字幕の書き出し）と文字起こしは揃いつつある。日本語の字幕の語単位の時刻合わせ（[[exp-sutra-sync-subtitles]] の同期）が Remotion の `Caption` 型でどこまで扱えるかは試していない
- **promo の道具として**: Canvas Capture は製品の UI の寄りを高解像度で録る道具で、[[exp-gyazo-resumption-video]] のような製品の紹介に効く可能性がある（試していない）
- **Manim と Motion Canvas は Opus 5.5 の波に公式には反応していない**。Manim はモデルが元々うまく使う（[[web-opus2-opus-5-5-explainer-posts-on-x]] の LinearUncle の感想）ので道具の側の変更が要らなかった、とも、単に開発の周期が違う、とも読める。Motion Canvas は 2026-07 から止まっている
- **ライセンス**: Remotion の `/remotion-license` skill は条文への案内だけで、判断はしない。会社の機械で作る西尾の場合の判断は [[web-remotion]] の Open Questions のまま

## Open Questions

- OpenFilm は作成から 1 か月でスター 5 千超え。実際の利用と品質は分からない。2 通りの順で描く検査が、どれだけの不具合を拾うかの数字は無い
- Remotion の「人が編集できるタイムライン」（別々の JSX ノード）の指針が、エージェントの書くコードの量や速さにどう効くかは書かれていない
- Manim の第三者の skill の質は読んでいない。Opus 5.5 が「Manim をうまく使う」のが skill の効果かモデルの効果かは、この資料からは分けられない
