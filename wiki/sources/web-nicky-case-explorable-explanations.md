---
type: source
summary: Nicky Case の explorable explanation 論。"How I Make Explorable Explanations"（2017）は「問いから始め、具体から抽象へ一段ずつ上り（BUT/THEREFORE でつなぐ）、読者自身の問いで終える（最後に砂場）」を型として書き、"4 More Design Patterns"（2018）は Puzzle・Place Your Bets・Role Play・Sandbox の四つを挙げ、砂場は深すぎると溺れると書く。Nutshell（2022）は「その場で展開できる、埋め込める説明」の道具。いずれも作り手の経験則で、効果は測っていない
video_types: [embed]
url: https://blog.ncase.me/how-i-make-an-explorable-explanation/
author: Nicky Case
published: 2017-09-20（How I Make Explorable Explanations）／ 2018-06-20（Explorable Explanations: 4 More Design Patterns）／ 2022（Nutshell）
retrieved: 2026-11-09
sources:
  - https://blog.ncase.me/how-i-make-an-explorable-explanation/
  - https://blog.ncase.me/explorable-explanations-4-more-design-patterns/
  - https://ncase.me/nutshell/
  - https://explorabl.es/
---

# Nicky Case の explorable explanation 論

## 何の文献か

- 著者は Nicky Case（"Parable of the Polygons"（Vi Hart と共作）、"The Evolution of Trust" などの対話的な解説の作者）。自分のブログと道具のページ。**実務者の経験則**で、学習効果を測った記述は無い
- 読んだもの（curl で取得し本文を読んだ）
  - "How I Make Explorable Explanations"（2017-09-20）: 自分の作り方の型
  - "Explorable Explanations: 4 More Design Patterns"（2018-06-20）: 最初の Explorable Explanations meetup から 4 年、「100 以上の Explorables」を経ての型の一覧
  - Nutshell（ncase.me/nutshell、ページ内で「2022 年」と書く）: 説明を文中に展開・埋め込みする道具
  - explorabl.es: Case が中心の「まとまりのない『運動』」のハブ。「遊びと学びを再び結びつけたい」と書く

## 書いてあること

### How I Make Explorable Explanations（2017）

三段の型として書いている。

1. **問いから始める**: Steven Strogatz の「（従来の教え方が）効かないのは、生徒がまだたずねていない問いに答えるからだ。……問いを好きにさせなければならない」を引く。問いは露骨に出さなくてよく、"The Evolution of Trust" では物語（第一次大戦の塹壕でなぜ休戦が生まれたか）、"Parable of the Polygons" ではゲームの形で出した
2. **抽象の梯子を上る**: 「地面から始めて、一段ずつ、ゆっくり上る」。講演者の多くは聴衆が地面にいるのに雲の上で専門語を話す、と書く。「アイデアを dumb down するのでなく、人を smart up する」。最初に**具体的な体験**（図形を直接ドラッグする、相手と実際に対戦する）を置き、それが後のすべての土台になるものを選ぶ。段のつなぎは South Park の Matt Stone と Trey Parker の「and then ではなく THEREFORE と BUT でつなげ」を借りる。"The Evolution of Trust" では BUT を連ねて「数分ごとに直観に反する新しい考えを見せられる」と書く。Bret Victor の Ladder of Abstraction が「自分の仕事の 90% に影響した」と注記する（[[web-victor-explorable-explanations]]）
3. **問いで終える**: 多くの作品の最後に「Sandbox Mode」を置く理由を「最初は**私の**問いを渡し、最後は読者が**自分の**問いを探る」ためと書く

### 4 More Design Patterns（2018）

- 前提として「学ぶには**考える**ことが要る」。高校の化学実験は手を動かした（手に火もついた）が考えなかったので何も覚えていない、と書く
- 四つの型と、それぞれ何に向くか（Case の判断）
  - **Puzzle It Out**（例: SineRider）: 答えが無数にあるパズルで考えさせる。教えることと評価することが一つになる。シミュレーションにしやすい題材（数学・プログラミング・科学）向き
  - **Place Your Bets!**（例: New York Times の The Upshot "You Draw It"）: 答えを見せる前に、読者に予想を描かせる。予想と現実のずれが大きな驚きになる。正誤のはっきりした題材向き
  - **Role Play**（例: BBC "A Syrian Journey"）: 正解の無い題材（哲学・政治・倫理）向き
  - **Sandbox Mode**（例: Earth: A Primer）: 最も深い知識に届くが、「溺れる」こともある。TensorFlow の Neural Network Playground は機械学習を少し知る友人には役立ったが、自分には情報過多だった、と書く。対策は、とても単純なシミュレーションにする（「子ども用プールの深い所」）か、砂場を**最後**に置いてそこまでに部品を一つずつ紹介すること
- 結びで、Carl Wieman が講義を「教授法における瀉血」にたとえたことを引く

### Nutshell（2022）

- 「expandable, embeddable explanations」を作る道具。文中のリンクを開くと、その場に別の説明（他のページの一節、対話的な部品、YouTube 動画、Wikipedia の記事も）が展開される。読者は「必要なものを、必要な時に、文脈の中で」学べる、と書く
- リンクとの違いとして、ページ全体ではなく**必要な一節だけ**を持ち込めること、新しいタブに飛ばず読みの流れが切れないこと、文の途中で展開しても閉じた後に文を要約し直すことを挙げる
- 書き方の助言: 「**見せてから言う**（具体例と絵が先、抽象的な定義は後）」「初稿の語数を数えて 10% 削る」「Wikipedia のような中立語でなく自分の声で」「入れ子は楽しいが自制する。本質的なものだけ埋め込む」
- 着想の元は Ted Nelson の StretchText（1967 の設計文書）と書く

## この wiki への含意

### embed に効くこと

- **embed は「別の説明の中に埋め込まれる一節」**: Nutshell は文章の中に説明を埋め込む道具で、西尾の embed（プレゼンの中に埋め込んで使う特定概念の解説）と同じ構造を文章の側で作っている。Case が書く条件——ページ全体でなく必要な一節だけ、流れを切らない、閉じた後に元の文脈へ戻す——は、発表の途中で概念の動画を流すときの条件にそのまま読み替えられる（読み替えは推測。Case は発表について書いていない）
- **「見せてから言う」**: 具体例が先、定義は後。3Blue1Brown の「定義から始めるな」（[[web-3blue1brown-explainer-advice]]）と一致する。般若心経の同期解説で「専門語は名前だけ出しても解説にならない」「その場で要る最小の構造を一般語で添える」とした経験（[[exp-sutra-sync-subtitles]]）とも同じ向き
- **Place Your Bets は発表でも使える**: 予想を先に立てさせてから答えを見せる型は、聴衆に手を挙げさせる・心の中で予想させる形で生の発表に持ち込める。この型の効果には実験の裏付けがある（Kim, Reinecke, Hullman 2017。[[web-hohman-2020-communicating-with-interactive-articles]] で原典の数値を確かめた）。ただしその実験は画面上で自分の予想を描く条件で、口頭で予想させる発表の場とは条件が違う
- **砂場は embed に向かない**: Case 自身、砂場は溺れうるので最後に置くと書く。発表の中の数十秒〜数分の embed で聴衆に砂場を渡すことはできないので、embed は Case の型でいう「問い → 具体 → 一段上る」の部分だけを担い、砂場（自分の問い）は発表の後に URL で渡す、という分担になる（推測）

### talk への含意

- 「BUT / THEREFORE でつなぐ」は talk の台本の型として使える。LT 準備での円環構造（前半のエピソードを終盤で回収する）は別の型だが、どちらも「次々に話を並べない」ことを狙っている（[[exp-lt-20260909]]）

## Open Questions

- Case の型はどれも作り手の経験則で、測られていない。2018 の記事も「何をしているか分かっていなかった。今も分かっていない」と書いている。効果の根拠として引くときは、Place Your Bets（予想を先に描かせる）のように別の実験で確かめられたものと、そうでないものを分ける
- Case の explorable は読者が自分で操作する前提。発表の中では操作するのは話し手で、聴衆は見るだけになる。「学ぶには考えることが要る」という Case の前提に従うなら、見るだけの embed で考えさせるには何が要るか（予想を聞く、止めて問う、など）は文献からは決まらない
- Nutshell は「閉じた後に文を要約し直す」ことで文脈を保つ。発表で embed を流した後、話し手が何を言って本筋に戻るべきかについて、文献は見つかっていない
