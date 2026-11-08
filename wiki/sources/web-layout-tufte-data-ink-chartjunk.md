---
type: source
summary: Edward Tufte の data-ink ratio・chartjunk・small multiples を、本人のサイト（edwardtufte.com の書籍ページと ET Notebooks の本人の回答）と、本文を頁付きで引いた二次の文献（Few 2011、Bateman ら 2010）から読めた範囲でまとめたもの。「データを描かないインクは消す」「数字が退屈なら数字が間違っている」「動くものを描くときはアニメが効く、静止画は強い競争相手」と書く。本そのものは読んでいない
video_types: [talk, embed]
url: https://www.edwardtufte.com/book/the-visual-display-of-quantitative-information/
author: Edward R. Tufte（Graphics Press）。引用の経由先は Stephen Few（Perceptual Edge）、Scott Bateman ら（University of Saskatchewan）
published: 1983（The Visual Display of Quantitative Information 初版。第 2 版 2001）／ET Notebooks の本人の回答 2002〜2015
retrieved: 2026-11-09
sources:
  - https://www.edwardtufte.com/book/the-visual-display-of-quantitative-information/
  - https://www.edwardtufte.com/notebook/chartjunk/
  - https://www.edwardtufte.com/notebook/sparkline-theory-and-practice-edward-tufte/
  - https://www.edwardtufte.com/notebook/medical-animation/
  - https://www.edwardtufte.com/notebook/recommended-background-for-projected-presentations/
  - https://www.edwardtufte.com/notebook/displays-of-movie-making-techniques/
  - https://www.edwardtufte.com/notebook/illustration-of-small-multiples-magic-knight-tours/
  - https://www.perceptualedge.com/articles/visual_business_intelligence/the_chartjunk_debate.pdf（Few 2011。Tufte の本文を頁付きで引用）
  - https://vis.csail.mit.edu/classes/6.859/readings/pdfs/Bateman-UsefulJunk.pdf（Bateman ら 2010 の関連研究の節。Tufte の定義を頁付きで引用）
---

# Tufte の data-ink・chartjunk・small multiples（読めた範囲）

## 何の文献か

- **Edward Tufte "The Visual Display of Quantitative Information"**（Graphics Press, 1983／第 2 版 2001, 197 頁）: 統計グラフの設計の古典。**本文は読んでいない**。著者のサイトの書籍ページは目次相当の説明として「small multiples」「Editing and improving graphics. The data-ink ratio.」「Detection of graphical deception」などを挙げる
- **edwardtufte.com の ET Notebooks**（旧 Ask E.T. 掲示板）: 読者の質問と Tufte 本人・読者の回答が並ぶ。ここでは **Tufte 本人が書いた回答・記事だけ**を Tufte の主張として扱い、読者のコメントは「読者が書いている」と区別する
  - "Chartjunk"（2015-01-29）は VDQI pp.106–121、Envisioning Information pp.52–65、Visual Explanations pp.88–89・146–150 の**頁の画像**を並べたページ。画像はダウンロードしない決まりなので、**本文は読んでいない**
- 本の文言は、本文を頁付きで引いている二つの文献から取った（引用の正確さは原本と照合していない）
  - Stephen Few "The Chartjunk Debate"（Visual Business Intelligence Newsletter, 2011 年 4〜6 月号）。Few は Tufte の考えにおおむね賛成の立場の実務家
  - Bateman ら "Useful Junk?"（CHI 2010）の関連研究の節（研究の中身は [[web-layout-bateman-2010-useful-junk]]）
- 第 1 回で読んだ Tufte の Wired の論説 "PowerPoint Is Evil"（2003）は [[web-powerpoint-keynote-google-slides-video-playback]] にある。ここでは重ねない

## 書いてあること

### data-ink ratio（Bateman らの要約による）

- Bateman らは Tufte の立場を、VDQI p.59 の「データの量——数の値を置くインク——を、論評を加えるため、あるいは装飾の様式に合わせるために歪めるのは誤りだ」と引き、data-ink ratio を「データを表すインク ÷ グラフ全体のインク」で、1 に近づけることを目標とし、データを表さないインクは消すべきだと Tufte が論じた、と要約している（Bateman ら 2010, Related Work）
- 同じ節で Bateman らは、Gillan & Richman の実験が data-ink を増やすと速く正確になることを示しつつ、**足したインクの位置と働きで結果が変わった**（背景の絵は読みを難しくし、x・y 軸の線は反応を速めた）と紹介し、data-ink の最大化は「ほどほどに（within reason）」支持された、と書いている。グリッド線や枠の有無だけを変えた研究では差が出なかったとも書く

### chartjunk（Few が引く本文）

Few は VDQI と Envisioning Information から次を頁付きで引く（Few 2011, p.1–2）:

- 「グラフの内装の飾りは、見る人に何も新しいことを伝えないインクを大量に生む……原因が何であれ、それはすべて非データインクか冗長なデータインクで、しばしば chartjunk である」（VDQI p.107）
- 「幸い、chartjunk の大半は芸術上の判断とは関係ない。それは単に、通りかかるすべての図に決まって足される慣習的な道具立て——込みすぎたグリッド線と余計な目盛り、最も単純なデータの冗長な表現、作図ソフトの残骸——である」（同 p.107）
- 「chartjunk は決して薄いデータを救えない。最良の設計は……ときに物語の力で、ときに膨大な細部で、ときに単純だが面白いデータの優雅な提示で、見る人をデータの驚きへ引き込む」（同 p.121）
- Envisioning Information（1990, pp.34–35）で Nigel Holmes のダイヤモンド価格のグラフを例に「chartjunk の背後には、情報と聴衆の両方への軽蔑がある」「数字が退屈なら、数字が間違っている」「読者は忙しいかもしれないが、愚かではない」と書いた（Few はこの一節が Tufte と Holmes の論争の発端になったと書く）

Few 自身は「Tufte の chartjunk の定義はやや緩すぎた。メッセージを意味ある形で支えるものは junk ではない」と書いている（Few 2011, 結論）。

### small multiples

- 書籍ページの説明に「small multiples」が挙がる。定義の本文は読めていない
- ET Notebooks では読者が「VDQI p.170 ほか」を引いて、140 通りの Magic Knight's Tour を一枚に並べた図を small multiples の例として投稿している（2003-08-18、読者の投稿）。別の読者は Muybridge の馬の連続写真を「時間の中の動きを見せる small multiple」として挙げる
- Tufte 本人は "Displays of movie-making techniques"（2010-07-12）で、Wally Wood の漫画のコマ割りの手引き「22 FRAMES THAT ALWAYS WORK」を「古典的な small multiple」と呼び、それを動画に作り直した例や、Beautiful Evidence p.92 で作った絵コンテ（15 世紀の本の挿絵と Hitchcock の『北北西に進路を取れ』の絵コンテの比較）を並べている

### アニメーションと静止画（本人の回答）

"Medical animation"（質問 2003-03-13、Tufte の回答 2003-05-25）。医療の解説アニメの制作者に「アニメが静止画より良いのはいつか」と聞かれて:

- 「アニメは、**実際に動くもの**を描くときにうまく働くことが多い。心臓病学の推論にはアニメと音が明らかに役立つ。タイポグラフィの推論にはおそらく役立たない」
- 「静止画の世界（still-land）はアニメの強い競争相手だ。静止画の Muybridge は、アニメにした Muybridge に勝つ。両方見るべきではあるが」
- 「表示の次元の数は、内容の次元の数と、内容を理解するのに要る次元の数で決まる」
- 1997 年までの科学可視化の文献は「計算機の練習が多すぎて科学が少なすぎ」、定量性を失った図が多かったと書く
- 同じスレッドで読者（karen medina）が「アニメのためのアニメは学習を妨げうる」「受け身の視聴者になる」と書き、文献を並べている。これは読者の意見

### スパークラインと「データは最大、設計は最小」

"Sparkline theory and practice"（2004-05-27 の記事、その後追記）で Tufte は:

- 「スパークラインは小さく、密で、単純な、語の大きさのグラフで、活字の解像度を持つ」「データのグラフは活字の解像度を持つべきだ」
- Apple Watch の表示に「良いが、もっと細部、データの肌理を見せるべき。**設計の最小化であってデータの最小化ではない**」、Twitter analytics に「一般原則 = max[data], min[design]」
- スポーツや金融の報道が、ランダムなデータにも連続や勢いを読み込む「物語の行き過ぎ」をすると書き、実データの横に同じ条件で乱数化した 10 本を並べて見比べさせる試みを示す

### 投影の背景（本人の回答）

"Recommended Background for Projected Presentations"（質問 2002-03-12、回答 2002-03-19）:

- 紙の比喩で白地に黒字にするとビデオのぎらつきが出ることがあり、暗い地に光る字の方が疲れにくいこともある。「テレビの調整室や操縦席は、一般に暗い背景に光るデータを表示する」
- 「投影では、図と地のコントラストは室内の光に打ち勝つだけ必要だ」「事前に部屋と投影機を確かめ、照明とカーテンの操作を知り、**実際の条件で設計案を見よ**。このような言葉の議論で決めるな」

## この wiki への含意

- **「飾りより証拠に面積を」は Tufte の「max[data], min[design]」と同じ向き**: クオリアさんの動画の v3 は場面絵が画面の 36% を占め「意味のない飾り画像の面積が多すぎる」と評価され、v4 で装飾を 0% にして実画像の比較・工程・評価に面積を配った（[[exp-qualia-video]]、[[experience-lessons-2026-11]]）。Tufte の chartjunk 批判は統計グラフについてだが、talk の画面にもそのまま当てはまる。ただし Tufte の chartjunk は「装飾の絵」より先に「慣習的な道具立て（グリッド線・枠・作図ソフトの残骸）」を指している点は区別しておく
- **「図形と文字だけで描く」は data-ink の発想に近い**が、西尾の経験での理由は権利確認と private な画面の映り込みを避けることだった（[[exp-nishio-showreel]]、[[exp-words-as-public-goods-video]]）。理由が違うので、Tufte を根拠に書き換えない
- **embed に効くのは「実際に動くものを描くときにアニメが効く」**。第 1 回の Tversky ら・Berney & Bétrancourt の結論（中身の変化を見せる動きだけ効く）と同じ向き（[[web-tversky-2002-animation-can-it-facilitate]]、[[web-berney-betrancourt-2016-animation-meta-analysis]]）。Tufte は根拠を例で示していて、比較実験ではない
- **「静止画の Muybridge が勝つ」は「全部を常時表示し、光る位置だけ動かす」と合う**: 般若心経の同期解説は意味ブロックごとに切り替える案をやめ、全体を固定して現在位置の色だけを変えた（[[exp-sutra-sync-subtitles]]）。並べて見比べられる形を残している点が small multiples・「横に並べる」と同じ。ただし同期解説は音（唱え）に合わせて時間で光らせるので、静止画にはできない
- **promo とはぶつかる**: Tufte の立場は読み手が時間をかけて読む印刷物が前提。般若心経のアゲアゲ版では「変化が止まるとテンションが下がる」「出しっぱなしで光らせ続けるとインパクトが減る」が原則になった（[[exp-sutra-hype-editions]]）。promo では「データの最大化」より「変化の連続」が評価軸になっていて、Tufte の基準をそのまま当てると型を取り違える
- **投影の背景は「実際の条件で見よ」**: embed は会場で流すので、Tufte の「部屋と投影機で確かめよ」がそのまま効く。この wiki に会場で流して見え方を確かめた記録はまだない
- **スパークラインの「物語の行き過ぎ」への注意**は、talk で数字の変化に物語を付けるときの戒めになる（ランダムでも連続は出る）。Rosling 型の発表（[[web-roslingifier-data-presentations]]）が動きに意味を語るときも同じ注意が要る（推測）

## Open Questions

- VDQI・Envisioning Information の本文（とくに data-ink ratio の定義の頁、small multiples の章）は読めていない。ここの本文の文言は Few と Bateman らの引用を経由している
- Tufte の基準は印刷物・静止画の統計グラフについて書かれた。動画の 1 コマ（数秒しか見えない）に data-ink ratio をどう当てるかは、Tufte の読めた範囲には書いていない
- 「暗い地に光る字」と「白地に黒字」のどちらが動画・投影で読みやすいかは、Tufte も「証拠があるはず」と書くだけで示していない。読みやすさの研究は [[web-layout-okabe-ito-cud-wcag-contrast]] の WCAG の根拠の節を参照
- chartjunk の効果を測った研究は [[web-layout-bateman-2010-useful-junk]]。Tufte の主張と実験の結果は一致しない部分がある
