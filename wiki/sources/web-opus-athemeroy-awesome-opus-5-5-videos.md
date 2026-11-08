---
type: source
summary: Opus 5.5 公開後に X に流れた動画を集めて分類した GitHub の公開データセット（athemeroy, 2026-09-25〜10-11）。"brief contagion" の語の出どころ（9/26 版 README の 1 行の注釈で、翌日の「主張を締める」commit で消えた）と、「one-shot」の申告を人の指示・内部の見直し・受け入れまでの時間に分けて記録せよという整理、長い指示書どうしの 5-gram 一致 87.0%
video_types: [promo, talk, embed]
url: https://github.com/athemeroy/awesome-claude-5-5-videos
author: athemeroy（GitHub 表示名 Oddly Useful）
published: 2026-09-25（初版。最終 commit 2026-10-11）
retrieved: 2026-11-09
sources:
  - https://github.com/athemeroy/awesome-claude-5-5-videos （旧名 awesome-opus-5-5-videos。旧 URL は新しい名前へ転送される。README.md、docs/workflow-analysis.md、docs/snapshot-analysis.md、data/prompt-overlap.json、data/visible-prompt-lengths.json、data/corpus-snapshot.json。HEAD = 87e5cbf, 2026-10-11）
  - 同 repo の commit e5a0072（2026-09-26 22:56 +0800）の README.md（"brief contagion" の唯一の出現箇所）と commit 10bc706（2026-09-27 16:39 +0800, "Make Opus video evidence browsable and tighten source claims"、この行を削除）
  - https://x.com/donaldjewkes/status/2102801469976248500 と https://x.com/anjmaxx/status/2103174007319413155 （5-gram 一致の検算に使った本文。api.fxtwitter.com 経由で取得）
---

# athemeroy「Awesome Claude 5.5 Videos」— "brief contagion" の出どころと「one-shot」の数え方

## 何の文献か

- GitHub の公開 repo（ライセンス: 文章と図は CC BY 4.0）。Opus 5.5 公開（2026-09-22）の 3 日後、2026-09-25 に初版。X の検索で集めた投稿を、動画の中身・見た目・作り方の経路で分類し、作者の申告と自分たちが確かめたことを分けて書いている。star 973・fork 76（2026-11-09 に GitHub API で取得）
- 誰がどう測ったか（docs/snapshot-analysis.md）: 2026-09-26 21:05（中国標準時）までの X 検索 56 件（成功 55）で候補投稿 1,511、mp4 付き 1,419、添付 1,449。Hypit 0.2.3 で全添付から 9 コマを抜き、SHA-256 で別ファイル 1,401。**Gemini 3.8 Flash（視覚モデル）が 9 コマと投稿文から「Opus が関わったか」を yes 980 / likely 139 / no 282 と判定**し、その 1,119 本を分母に分野と様式を数えた。別に 168 件を作り方の経路で選んで読んだ（無作為抽出ではない）
- repo 自身が繰り返し書いている限界: 9 コマでは動き・音・内容の正しさ・裏のモデル呼び出しは分からない。判定は分類器のもので作者の確認ではない。いいね数は見え方の指標で、作者性や質の証拠ではない
- 宣伝目的は見当たらない（独立のプロジェクトで Anthropic・X とは無関係、と初版 README に書いている）。ただし作り手のコミュニティの中の資料で、査読は無い

## 書いてあること

### "brief contagion" の出どころ

- この語が repo に出てくるのは、**2026-09-26 版（commit e5a0072）の README の表の 1 行だけ**。「9/26 の更新で入った新しい事例」の表で、@stephanlivera の 15 秒ショーリール（[[web-opus-stephanlivera-showreel-prompt]]）に付けた注釈: "Viral resume-style motion design reel (14k+ likes) demonstrating the brief contagion behind identical 15-second showreels."
- 定義も測定も無い。翌日の commit 10bc706（"tighten source claims"）でこの行ごと消え、以後の版（HEAD まで）には出てこない（2026-11-09 に repo の全履歴を `git log -S` で確かめた）
- Movez の記事（2026-09-27、[[web-movez-opus-motion-design-course]]）が「athemeroy のデータセットは "brief contagion" と呼んでいる。同じ一行から何百本も、互いに韻を踏むような reel が出た」と紹介し、そこから hculap の skill（[[web-opus-hculap-skill-motion-graphic]]）や seeco の X 長文（2026-10-02）に広がった。**データセットが測った現象ではなく、データセットの作者が一度書いて取り下げた注釈が、二次の記事で名前として定着した**、という経緯になる

### 「one-shot」を一つの量として扱わない（docs/workflow-analysis.md）

- 「人の 1 回の指示」の裏に多数の見直しがある例を並べている: F1 の作者は「Opus が途中の成果を何度も却下した」と返信で書いている。Taxtello は第 5 版で批評役のエージェントつき。ゲームの作者は購入した素材と 2 日で約 20 回の指示
- 処方として「**人の指示の回数、道具・内部の見直しの回数、受け入れた結果までの時間**の 3 つを別々に記録せよ。投稿はこの 3 つを一貫して開示していないので、"one-shot" は制作の手間の共通の単位にならない」と書いている
- 費用も同じ扱い: 作者の申告するタスク全体の費用（例: 同じ場面で Haiku $2.19 / Opus $3.04、F1 の Haiku 実行役が全体 $96.27 の 64.2%）を並べるが、成果物・素材・effort の設定・受け入れ基準が違うのでモデルの順位にしない、としている
- 「もっともらしいアニメは検証済みの説明ではない」節: Sonnet の塔の作者自身が「施工順は創作、幾何は簡略、構造計算なし」と書いている例。数学・科学の説明をレンダリングしても、その主張の正しさは示されない

### 指示書の長さと、長い指示書どうしの一致（docs/snapshot-analysis.md）

- 公開された 5 本の依頼文の見える文字数は 172〜17,664 字（data/visible-prompt-lengths.json）。5 本は分布を表さない、と注記
- 後発の MV の依頼文（@anjmaxx, 2026-09-24, 5,594 字）は、先行の依頼文（@donaldjewkes, 2026-09-23, 9,554 字、[[web-opus-donaldjewkes-claude-pop-brief]]）と、**ユニークな 5 語連続の 87.0%、12 語連続の 78.6% を共有**している（data/prompt-overlap.json）。repo は「文面の一致だけでは誰が何を読んで写したか、どの手順が実行されたかは言えない」と限界を書いている
- 検算: 2 本の本文を取り直し、repo の方法（小文字の英数字とアポストロフィを語にし、連続 n-gram の集合を比べる）で数えると、5-gram 1,745 / 1,008 / 共有 877（0.870）、12-gram 共有 789（0.786）で、repo の値と一致した（2026-11-09）
- 似通いは一行プロンプトだけの話ではない、ということになる。長い指示書も写されて広がった

### 何が作られたか

分野・様式・尺の集計（広告・ローンチの 71.6% がモーショングラフィックス／UI、教育の解説の尺の中央値 102.28 秒など）は同じ repo を読んだ [[web-opus2-awesome-claude-5-5-videos]] にある。このページでは扱わない。

## この wiki への含意

- **"brief contagion" は測られた現象として引かない**。この wiki の [[web-movez-opus-motion-design-course]] は「athemeroy のデータセットが "brief contagion" と呼んでいる」と書いているが、原典では 1 日だけあった注釈の語だった。似た動画が大量に出たこと自体は、同じ一行プロンプトが多数投稿されたこと（[[web-opus-stephanlivera-showreel-prompt]]）からは確かだが、出力の似通いを測った人はこの repo を含めて見つからなかった
- **西尾の showreel 15 秒版の記録の書き方**: [[exp-nishio-showreel]] は一行プロンプトの形だが、実際には 15 秒版のあとに日英・縦長・1 分版を作り、静止画で確かめている（[[exp-html-capture-pipeline]]）。athemeroy の言う 3 つ（人の指示の回数・内部の見直し・受け入れまでの時間）で記録すると、他の作例と比べられる。西尾の側の記録には「内部の見直しの回数」が残っていない
- **talk・embed への含意**: 「もっともらしいアニメは検証済みの説明ではない」は、解説（talk）と概念の埋め込み（embed）にそのまま効く。[[exp-polis-magi-op]] の「事実の言い切りの境界」や [[exp-html-capture-pipeline]] の「画面の主張 → 一次ソース」の表は、この指摘への西尾の側の対応にあたる
- promo の側では、広告・ローンチの大半がモーショングラフィックス／UI に寄ったこと（71.6%）が、西尾の 9/25 以後の制作が promo に寄ったこと（[[exp-timeline-2026]]）と同じ向きを向いている。ただし分類器の判定で、作者の確認ではない

## Open Questions

- 一行プロンプトの出力がどれだけ似ていたかを測った資料はあるか（同じ依頼文の出力どうしの画像の類似度など）。この repo の色の測定は分野・様式ごとで、同じ依頼文ごとではない
- athemeroy が "brief contagion" の行を消した理由は commit メッセージ（"tighten source claims"）以上には書かれていない
- 87.0% の一致は文面の一致で、後発の作者が先行の依頼文を下敷きにしたのか、同じテンプレートを両方が使ったのかは分からない（repo もそう書いている）
