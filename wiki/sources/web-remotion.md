---
type: source
summary: Remotion の公式ドキュメント・LICENSE・Agent Skills。React コンポーネントを useCurrentFrame() の関数として書き、headless Chrome の複数タブで各フレームを撮って FFmpeg で動画にする。従業員 4 人以上の営利組織は有料の Company License が要り、コーディングエージェント向けに skills・Markdown 版ドキュメント・prompt to video のテンプレートを出している
video_types: [any]
url: https://www.remotion.dev/docs/
author: Remotion AG（公式ドキュメント）
published: 2026-11-08（ドキュメントの最終更新日。LICENSE.md は Copyright 2026）
retrieved: 2026-11-09
sources:
  - https://www.remotion.dev/docs/idea.md
  - https://www.remotion.dev/docs/flickering.md
  - https://www.remotion.dev/docs/terminology/concurrency.md
  - https://www.remotion.dev/docs/lambda.md
  - https://www.remotion.dev/docs/lambda/how-lambda-works.md
  - https://www.remotion.dev/docs/client-side-rendering/index.md
  - https://www.remotion.dev/docs/client-side-rendering/how-it-works.md
  - https://www.remotion.dev/docs/webcodecs/index.md
  - https://github.com/remotion-dev/remotion/blob/main/LICENSE.md
  - https://www.remotion.dev/docs/license/faq.md
  - https://github.com/remotion-dev/remotion/pull/3750
  - https://www.remotion.dev/docs/ai/index.md （HTML 版 https://www.remotion.dev/docs/ai）
  - https://www.remotion.dev/docs/ai/coding-agents.md
  - https://www.remotion.dev/docs/ai/skills.md
  - https://www.remotion.dev/docs/ai/generate.md
  - https://github.com/remotion-dev/remotion/tree/main/packages/skills/skills （remotion-best-practices / remotion-markup / remotion-render の SKILL.md, version 4.0.541）
  - https://www.remotion.dev/system-prompt.txt
  - https://www.remotion.dev/templates/prompt-to-video
  - https://www.remotion.dev/llms.txt
---

# Remotion（React で動画を書く）

## 何の文献か

Remotion AG（スイスの会社）が出している公式ドキュメント、GitHub の `LICENSE.md`、License FAQ、コーディングエージェント向けの Agent Skills（`packages/skills`）。いずれも一次資料だが、製品の作り手自身の説明なので、速さ・使いやすさの記述は宣伝を含みうる。GitHub のスター数は約 7.2 万（2026-11-09 の API 値）。ドキュメントは `.md` を付けると Markdown で取れる（下の「AI 向けのドキュメント」）。

## 書いてあること

### 1 コマの描き方と時間

- 「Remotion の考え方は、フレーム番号と白紙のキャンバスを渡し、そこに React で好きなものを描かせること」「動画は時間に沿った画像の関数である」と書いている（`/docs/idea`）。コンポーネントは `useCurrentFrame()` で現在のフレーム番号を受け取る。動画の性質は `width`・`height`・`durationInFrames`・`fps` の 4 つで、最初のコマは 0、最後は `durationInFrames - 1`。
- `<Composition>` に React コンポーネントと尺・fps・解像度を登録する。同じコンポーネントを 1920×1080 と 1080×1920 で別の Composition として登録する例がある（`/docs/idea`）。

### 決定論であることの要求（flickering のページ）

- レンダリングは「高速化のために複数のタブを開く。タブは状態を共有しないので、`useCurrentFrame()` に依らずに動くアニメは壊れる」と書いている（`/docs/flickering`）。
- コンポーネントが満たすべき条件として 4 つを挙げる: 何度呼んでも同じ絵を出す／フレームが順番に描かれることに依存しない／一時停止中に動かない／乱数に依存しない（例外は Remotion の `random()`）。
- `--concurrency=1` で順番に描けばちらつきが消えることが多いが、「遅く、タイミングの正しさも保証されない」「Lambda でのレンダリングができなくなる」と書く。理由として「たまたまレンダリング速度がアニメの速度と同じくらいだったから良く見えるだけで、本当の時刻の同期はなく、機械ごとに結果が違う」。
- アセットの読み込み待ち: `<Img>`・`<Video>`・`<Audio>` などの専用要素を使う、データ読み込みは `delayRender()` で止める、フォントの読み込みを待つ、CSS の `background-image`・`mask-image` を避ける（`/docs/flickering`）。
- Agent Skill `remotion-markup` は「CSS の `transition` や `animation` は正しくレンダリングされないので書き直す。Tailwind の animation クラスも同じ」と書く。`system-prompt.txt` は「Remotion は React のコードがすべて決定論的であることを要求する。だから `Math.random()` は禁止」と書く。

### レンダリング方式と速さ

- ローカルのレンダリングでの concurrency は「並列に開くブラウザのタブの数。各タブがウェブの内容を描いてスクリーンショットを撮る」（`/docs/terminology/concurrency`）。上げすぎると機械が過負荷で落ちる、とも書く。
- 出力は動画のほか、静止画（`npx remotion still`）、画像連番（`--sequence`）、GIF、透過動画（`/docs/render`）。Agent Skill `remotion-render` は複数コマを 1 回で画像に書き出す `npx remotion render <id> out/frames --frames=0,30,90 --image-format=png` を挙げる。
- **Lambda**: 1 つの Lambda 関数が Serve URL を headless ブラウザで開き、尺と concurrency から動画をチャンクに分け、チャンクごとに別の Lambda 関数を起動して描かせ、最後に連結して S3 に置く（`/docs/lambda/how-lambda-works`）。「Remotion の動画を描く最速でもっともスケールする方法」と書く（`/docs/lambda`）。使ってよい目安は「Full HD で 80 分未満（AWS の 15 分のタイムアウトに当たるまで）」、1 リージョンの同時実行は既定で 1000、出力は約 5GB（Full HD で約 2 時間）まで、Lambda では AV1 不可。「多くの利用者は数分の動画を数セントで描いている」と書くが、実測の条件は書いていない。
- **ブラウザ内レンダリング**（`@remotion/web-renderer`、v4.0.491 から stable）: WebCodecs と Mediabunny でエンコードし、FFmpeg を使わない。ただし「ブラウザの viewport はキャプチャできない」ので、DOM の各要素の位置を `getBoundingClientRect()` で計算して canvas に描き直す方式で、対応する HTML 要素と CSS は一部だけ（`/docs/client-side-rendering/how-it-works`）。Chrome 94+、Firefox 130+、Safari 26+。
- `@remotion/webcodecs` は「Mediabunny へ移行するので段階的に廃止」と警告が出ている（`/docs/webcodecs`）。動画の変換・フレーム抽出用で、canvas の録画用ではない。

### 音

- `<Audio>`・`<Video>` を置くと、その音がレンダリング結果に混ざる。ブラウザ内レンダリングでも `<Audio>`・`<Video>` の音を拾って混ぜる（`/docs/client-side-rendering/how-it-works`）。音量などをフレームの関数として書ける（Skill `remotion-markup` は「フレームに依存する音量・タイトル・オーバーレイは小さいコンポーネントへ切り出す」と書く）。

### ライセンス（原文）

`LICENSE.md`（2026-11-09 取得）の該当部分:

> You are eligible to use Remotion for free if you are:
> - an individual
> - a for-profit organization with up to 3 employees
> - a non-profit or not-for-profit organization
> - evaluating whether Remotion is a good fit, and are not yet using it in a commercial way

> You are required to obtain a Company License to use Remotion if you are not within the group of entities eligible for a Free License.

> It is not allowed to copy or modify Remotion code for the purpose of selling, renting, licensing, relicensing, or sublicensing your own derivate of Remotion.

- 冒頭に「In Remotion 5.0, the license will slightly change」とあり、PR #3750（2024-04-22 作成、未マージ）は実質的な変更として「契約者（contractors）も人数に数える」「Company License を新しい利用規約に結びつける」の 2 点を挙げる。
- License FAQ（`/docs/license/faq`）の言い方は LICENSE.md と少し違い、「an organization or team of individuals with up to 3 people」。人数は会社全体の人数で数える: 「社員 20 人で Remotion を使うのは 1 人だけでも Company License が要る」。
- Company License は 2 種類: **Remotion for Creators**（自動化を組まずに動画を作る組織。Remotion のコードを自分で、または agentic coding tools で書く 1 人につき月 $25）と **Remotion for Automators**（1 render $0.01、月の最低 $100）。「自動化」は `renderMedia()`・`renderStill()`・`npx remotion render`・`<Player>` などをプログラムから呼ぶコードを持つこと、と定義する。Studio・Player のプレビューは render に数えない。
- 無料と有料で機能の差はない（FAQ）。Lambda のページは「ライセンスが必要な会社がクラウドでレンダリングするなら Remotion for Automators が要る」と書く。ブラウザ内レンダリングはライセンスキーの有無にかかわらず毎回テレメトリを送る（`/docs/client-side-rendering`）。

### LLM・エージェント向けに出しているもの

- **AI 向けのドキュメント**: どのページも `.md` を付けると Markdown で取れ、`Accept: text/markdown` にも応じる。「Remotion のドキュメントのリンクを Claude Code や opencode に貼れば、自動で Markdown 版を取りにいく」と書く（`/docs/ai`）。`llms.txt` もある。
- **Agent Skills**（`npx skills add remotion-dev/skills` または `npx remotion skills add`）: `remotion-best-practices`（他の skill への案内役）、`remotion-create`、`remotion-markup`、`remotion-studio`、`remotion-render`、`remotion-maps`、`remotion-captions`、`remotion-saas`、`remotion-interactivity` など 13 個（GitHub の `packages/skills/skills`）。
  - `remotion-best-practices` は「ユーザーが動画を "作って" と言ったら、はっきり求められない限り既定ではレンダリングしない。見たいのは対話的なプレビューだ」「プロジェクトが動くようになったらすぐ Studio を起動してブラウザでプレビューを開き、作業中ずっと開いておいてユーザーが進み具合を見て舵を取れるようにする」と書く。Studio は WebMCP のツールに対応している。
  - 同じ skill は「ユーザーが会話の外でコードを直していることがある。意外な変更を見つけたら上書きせず、意図したものとみなすか確認する」とも書く。
- **コーディングエージェントで作る手順**（`/docs/ai/coding-agents`）: `npx create-video --yes --blank my-video` → skills を入れる → `npm run dev` で Studio → 別の端末で Claude Code / Codex / Kimi Code / OpenCode を起動してプロンプトで動画を作る。
- **LLM でコードを生成する例**（`/docs/ai/generate`）: Vercel AI SDK で Remotion のコンポーネントを生成する例。注意として「生の出力にはよく Markdown のコードフェンスが付くので取り除く処理が要る」「コンテキストが大きくなると出力の質と指示への従い方が落ちる（context rot）」と書き、1 つの大きな system prompt の代わりに、要求に応じて skill（charts、typography、transitions など）を選んで入れる方式を勧める。
- **テンプレート**: 「Prompt to Motion Graphics」の SaaS テンプレートと、「Prompt to Video」（OpenAI と ElevenLabs で台本・画像・ナレーションを作って短い動画にする。第三者 webmonch の寄稿）。

## この wiki への含意

- **西尾の方式と同じ原理**: [[exp-html-capture-pipeline]] の「`renderFrame(f)` は時刻だけの純関数にする」「乱数は seed 固定」は、Remotion が flickering のページで要求する 4 条件とほぼ同じ。違いは、Remotion はこれを「複数タブで並列に撮るため」の条件として書いていることで、西尾の方式は 1 タブで順に撮っているので純関数であることを「好きな秒の静止画を撮る」確認にしか使っていない。並列に撮れば、粒子系の 1 分に約 10 分（実測）は短くできる可能性がある（試していない）。
- **撮り方の違い**: 西尾の方式は canvas の `toDataURL` で 1 コマを取り出す。Remotion（サーバー側）はタブのスクリーンショットなので DOM・CSS・SVG もそのまま撮れる。逆にブラウザ内レンダリングは DOM を canvas に描き直すので CSS の対応が限られる。
- **型ごと**: promo（[[exp-nishio-showreel]] のような短尺）では利点は並列化と React の部品の再利用。talk・embed では、字幕（captions skill）・音声付き `<Audio>`・Studio のタイムライン編集が効きうる。
- **ライセンス**: 西尾の作業場は会社の機械で、会社の発信物として作るなら「4 人以上の営利組織」に当たり Company License（Creators なら書く人 1 人あたり月 $25）が要る、と読める。個人の作品として個人で作るなら無料。どちらに当たるかは使う前に決める必要がある（Open Questions）。
- **エージェントでの作り方**: Remotion の skill は「まずプレビューを開いて人に見せ続ける」方針で、[[exp-html-capture-pipeline]] の「全編を撮る前に山場の秒だけ静止画で見る」、[[exp-qualia-video]] の「機械 QA が通っても視聴品質は人間が見ないと分からない」と同じ向き。ただし skill は「人間がブラウザで見る」前提で、エージェント自身が画像を見て直す手順（[[web-theoremexplainagent-code2video-visualedu]] の VLM 検査）は skill の本文には無い。代わりに `render --frames=...` で指定コマを PNG にできるので、エージェントに画像を見せる経路は作れる。

## Open Questions

- 西尾の制作が Remotion の Free License の対象か（個人か、会社＝4 人以上の営利組織か）。会社の発信物なら Company License の費用を誰が持つか。Remotion 5.0 で contractors も人数に数えるようになる点も含めて、使う前に確かめる。
- Remotion の並列レンダリングが粒子系の重い canvas 描画でどれだけ速くなるかは、この wiki では測っていない。ドキュメントにも具体的な速度の数字は無い（Lambda の「数セント」は条件なし）。
- ブラウザ内レンダリング（WebCodecs）が日本語の文字組み（Hiragino 等）をどこまで再現するかは、limitations のページを読み込んでおらず未確認。
- 「Prompt to Video」テンプレートの出力の質についての評価は公式ページに無い。
