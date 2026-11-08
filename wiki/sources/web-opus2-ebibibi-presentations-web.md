---
type: source
summary: 解説動画（YouTube）と対になるスライドを、コーディングエージェントが Remotion のコンポーネントとして書き、ブラウザの Remotion Player で動くスライドにして、話し手がそれを送りながら録画する個人のプラットフォーム（ebibibi/presentations-web、2026-06〜）。Opus 5.5 公開後もこの形で解説を出し続けている。動画を丸ごと AI が描くのでなく「動くスライドは AI、語りと時間は人」の分担
video_types: [talk]
url: https://github.com/ebibibi/presentations-web
author: ebibibi（Ebisuda。個人の GitHub リポジトリ、公開。ライセンス表記なし）
published: 2026-06-21（repo 作成）〜2026-11-07（最終 push）
retrieved: 2026-11-09
sources:
  - https://github.com/ebibibi/presentations-web/blob/main/README.md
  - https://github.com/ebibibi/presentations-web/blob/main/AGENTS.md
  - https://github.com/ebibibi/presentations-web/pull/227
  - https://github.com/ebibibi/presentations-web/blob/main/content/decks/opus-5-5-prompting-guide/deck.yaml
---

# presentations-web（動くスライドを AI に書かせ、人が語って録る）

## 何の文献か

- 個人の公開リポジトリ。README と、エージェント向けの指示書 `AGENTS.md`、PR を読んだ。README の説明は「YouTube に紐づいた、リッチなスライドデッキを公開する個人の Web プレゼンテーション基盤」
- 作者の YouTube の解説動画と、同じ内容のスライド（Web で読める）を対にして公開している。デッキは 38 個（2026-11-09 の `content/decks`）。コミットの共著者表記は「Claude Opus 5.5」13 件、「Claude Opus 5」1 件（直近 100 コミットのメッセージ）
- 動画そのもの・視聴の数字は見ていない。下の「視聴維持が約 2 倍」は作者の自己申告で、根拠は「私的なメモにある」と書かれている

## 書いてあること

### 仕組み（README）

- Vite＋React＋TypeScript の静的サイト。スライドの描画は `@remotion/player` と `remotion` で「ブラウザの中でタイムラインに沿ったリッチなスライド」を出す
- デッキは `content/decks/<slug>/deck.yaml`（題・要約・公開状態・YouTube の ID・スライドの並び）と `slides.tsx`（各スライドの React コンポーネント）。両者は id で対応させ、並び順は deck.yaml だけが持つ
- 目標に「スタジオでの録画と、聴衆が読むことの両方を支える」「デッキの作成をコード生成エージェントに向いた形に保つ」を挙げる
- **録画面**: 1920×1080 のうち、左 1280×1080 がスライド、右 640×1080 は空けてある。「全画面撮影」ボタンはこの録画面だけを全画面にする。録画は所有者だけ（ログインで制御）
- スライドの文字は、開発サーバー上でクリックして直接書き換えられる（ソースの該当範囲だけを書き戻す）。誤字直しのためにエージェントを呼ばなくてよいように、と書く

### 一つのデッキの形（opus-5-5-prompting-guide、2026-09-26）

- 各スライドに `durationInFrames`（240〜300 など）と `notes` を持つ。notes は話し言葉の文（例: 「Anthropicが Opus 5.5 専用のプロンプトガイドを出しました。結論から言うと、…」）で、語りの原稿として読める
- PR #227（2026-09-26）は「スライドに対応する YouTube 動画を紐付ける」。「動画の概要欄にはこのURLを既に入れてあります。動画を公開する前にこのPRをマージしてください」とある。動画の公開と同じ日にスライドを公開している

### エージェントへの指示（AGENTS.md「AI Deck Creation Flow」）

- 「最初の版は絞る。文字の多いスライドをたくさん並べるより、強いスライド 5〜12 枚」
- 「**Remotion は、タイミングやアニメーションが発表を良くするところでだけ使う**」
- 「大雑把な題から頼まれたら、細部をいちいち聞かずに完成した初稿を作る。公開の承認までは `status: draft`」
- YouTube の動画を支えるデッキの並べ方: 「網羅でなく視聴維持のために並べる。この並べ方で、視聴者がチャンネルの普段の約 2 倍の割合で残った」として、(1) 題の答え（何が起きて、なぜ大事か）を最初の 1〜2 枚に書く。節の見出しではなく具体的な答えを書く、(2) 個人の利害があればそのスライド（「以前は逆を勧めていた」）、(3) 中核は時系列で語り、各スライドが「次に何が起きた？」を生むように、(4) 一般論は短く、最後は「今日確かめること」の短い一覧
- 公開物として扱い、私的・顧客・家族・雇用主に関わる情報を入れない、とも書く

## この wiki への含意

- **talk のもう一つの分担**: Opus 5.5 の流行の多くは「動画の全部（絵・声・音楽）を AI が描く」形だった（[[web-opus2-opus-5-5-explainer-posts-on-x]]）。このプラットフォームは「動くスライドを AI が Remotion で書き、語りと時間は人が持つ」形で、talk（解説プレゼン風）にそのまま当たる。西尾の LT（[[exp-lt-20260909]]）や 1 分解説シリーズ（[[exp-llm-wiki-explainer-series]]）の作り方の候補になる
- **notes が台本を兼ねる**: スライドごとの話し言葉の notes は、[[exp-qualia-video]] の `script.json`（区間ごとに字幕用の caption と読み上げ用の narration）と同じ位置にある。違いは読み手が人であること。TTS の読み違いの問題（[[exp-galleria-tts-and-singing]]）は起きない代わりに、録音の手間が人に残る
- **「最初に答え」**: 作者の自己申告の視聴維持の改善は、[[talk]] の「冒頭で目的を示す」や [[exp-qualia-video]] の「冒頭 1 分で目的・失敗・見終わったらできること」と同じ向き。数字の根拠は公開されていない
- **embed には当たらない**: スライドは話し手が送る前提で、流しっぱなしの動画ではない（[[embed]] の Updates の「流しっぱなしの前提」とは別）。ただし各スライドの中の Remotion のアニメ（`durationInFrames` を持つ）は、スライドの中で流しっぱなしになる数秒の部品で、embed を「スライドの中の短い動く部品」として作る一つの形と読める（推測）

## Open Questions

- 右側 640×1080 の空き領域に何を置くか（顔の映像か）は README に書かれていない
- 「視聴維持が普段の約 2 倍」の測り方（どの動画の、どの指標か）は非公開
- notes を読み上げるのは人だけか、TTS で読ませる経路もあるか（README の「将来の作業」に「生成した動画素材のための Remotion の描画パイプライン（任意）」がある）
