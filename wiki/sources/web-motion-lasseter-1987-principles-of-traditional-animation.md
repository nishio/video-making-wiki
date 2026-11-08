---
type: source
summary: Lasseter（Pixar, SIGGRAPH 1987）が Disney の手描きアニメの原則を 3D キーフレームのアニメに移して説明した論文。Timing（速さが意味を決める。準備・動作・反応に「足りるだけ、それ以上でなく」時間を割く）と Staging（一度に一つの考えだけを見せる。静かな場面では動くものに、忙しい場面では止まったものに目が行く）は媒体によらず同じ、と書く
video_types: [any]
url: https://www.ics.uci.edu/~fowlkes/class/ics162/exercises/lasseter.pdf
author: John Lasseter（Pixar）
published: 1987-07
retrieved: 2026-11-09
sources:
  - https://www.ics.uci.edu/~fowlkes/class/ics162/exercises/lasseter.pdf（Computer Graphics, Vol. 21, No. 4, July 1987, pp. 35–44 のスキャン。大学の授業ページに置かれた写し）
  - Thomas, F. & Johnston, O. "Disney Animation: The Illusion of Life", Abbeville Press, 1981（本文は未読。Lasseter の引用 [26] を通してだけ）
---

# Lasseter 1987「Principles of Traditional Animation Applied to 3D Computer Animation」

## 何の文献か

- John Lasseter（当時 Pixar）が SIGGRAPH '87 で発表した論文。Computer Graphics, Vol. 21, No. 4（1987-07）pp. 35–44。種類は査読会議の論文だが、中身は実験ではなく**実務家による原則の解説**（自作の Luxo Jr.・The Adventures of André and Wally B. を例にする）
- 読んだのは大学の授業ページに置かれたスキャン PDF（OCR で本文を抽出。図は見ていない）。ACM の正本は開いていない
- 「Disney の 12 原則」の出どころとされる Thomas & Johnston "The Illusion of Life"（1981）は**読めていない**。この論文は原則の定義の多くをこの本（文献 [26]）から引いている。以下で「Disney の原則」と書くのは、Lasseter が [26] を引いて書いた範囲

## 書いてあること

### 原則の一覧（2 節）

Lasseter は Disney で 1930 年代に名前の付いた原則として、次の **11 項目**を挙げている（番号は論文のまま）。

1. Squash and Stretch — 動きの最中に形を歪めて、物の硬さと質量を示す
2. Timing — 動作の間隔で物の重さ・大きさと、キャラクターの人格を示す
3. Anticipation — 動作の準備
4. Staging — 考えを紛れなく明らかに見せる
5. Follow Through and Overlapping Action — 動作の終わり方と、次の動作との関係
6. Straight Ahead Action and Pose-To-Pose Action — 動きを作る二つの対照的なやり方
7. Slow In and Out — 中割りの間隔で、タイミングと動きの細やかさを出す
8. Arcs — 自然な動きの経路
9. Exaggeration — デザインと動作で考えの本質を強める
10. Secondary Action — 別の動作から生じる動作
11. Appeal — 観客が見て楽しいデザインや動作

一般に「12 原則」と呼ばれるものとの違い: この論文には **Solid Drawing が無く**、Straight Ahead と Pose-to-Pose を 1 項目にしている（IBM の解説は 12 項目で Solid drawing を含む。[[web-motion-ibm-design-language-carbon-motion]]）。どちらが本の並びに忠実かは、本を読めていないので確かめていない。

Lasseter は、**Timing・Anticipation・Staging・Follow through・Overlap・Exaggeration・Secondary action は 2D と 3D で同じように効き**、Squash and stretch・Slow in and out・Arcs・Appeal・Straight ahead・Pose-to-pose は意味は同じだが媒体の違いで当て方が変わる、と書いている。

### Timing（2.2 節）

- 「the speed of an action defines how well the idea behind the action will read to an audience」。速さは重さ・大きさを表し、感情の意味まで運ぶ、と書く
- 「It is important to spend enough time (but no more) preparing the audience for: the anticipation of an action; the action itself; and the reaction to the action. If too much time is spent on any of these, the audience's attention will wander. If too little time is spent, the movement may be finished before the audience notices it, thus wasting the idea.」（Whitaker & Halas "Timing for Animation" [30] を引く）
- 速い動きほど、観客が追えることを確かめる必要がある。読めないほど速くしてはいけない
- 中割りの枚数ごとに印象が変わる表を載せている（中割り 2 枚: 神経質なひきつり、3 枚: レンガをよける、4 枚: 「急げ！」と鋭く命じる、5 枚: もっと友好的に「こっちだ」、… 10 枚: 凝った筋を伸ばす）。何コマ撮り・何 fps の前提かは本文に書いていない
- 同じ大きさ・形の物でも、タイミングだけで重さが全く違って見える。重い物は動き出し・止まりに時間とかかる力を見せる

### Anticipation（2.3 節）

- 動作は準備・動作そのもの・終わりの三つに分かれる。予備動作は**観客の目を画面の正しい場所に正しい瞬間に向ける**ための仕掛けでもある、と書く
- 「If the audience expects something to happen, then it can be much faster without losing them.」準備が足りなければ、予備動作を大きくするか動作を遅くする。Wally B. が飛び去る動作は 3〜4 コマだが、予備動作を長く取って何が起きるか分かるようにした

### Staging（2.4 節）

- 「only one idea be seen by the audience at a time」。多くの動きが同時に起きると目の行き先が分からず、主な考えが見落とされる
- 「In a still scene, the eye will be attracted to movement. In a very busy scene, the eye will be attracted to something that is still.」（[26] を引く）
- 「Look at this, now look at this, and now look at this.」と、一つずつ最も強く簡単に見せてから次へ進む
- Luxo Jr. では、重要な動作をするのは常に親子のどちらか一方にし、もう一方の動きを抑えた。シルエットで読める向き（横向き）に動作を置いた

### Slow In and Out・Arcs（2.7・2.8 節）

- Slow in and out は「中割りの間隔」の話で、数学的には 2 次・3 次の連続性のこと、と書く
- スプラインの補間では、短いコマ数で値が大きく変わるときに**行き過ぎ（overshoot）**が出る。Luxo Jr. の台座が跳ぶ前後に床へめり込んだので、止まっている値と同じキーを前後に足してスプラインを固定した
- 経路（arc）とタイミング（間隔）を同じスプラインで制御すると、速い動作ほど弧が平らになる。経路のスプラインとタイミングのスプラインは分けるべき、と書く

### 結び（3・4 節）

- 人格（personality）は原則の一つではなく、全原則を知的に当てた結果。動作はキャラクターの思考の結果であるべき
- 「the first goal of the animator is to entertain」。道具（ハード・ソフト）だけでは足りず、原則も道具だ、と結ぶ

## この wiki への含意

この論文はキャラクターアニメの論文で、**図形と文字だけの解説動画・モーショングラフィックスについては何も書いていない**。以下はどこまで移せるかの推測。

- **Staging の「一度に一つ」は talk・embed の「説明中の要素だけを動かす」と同じ向き**。[[exp-qualia-video]] の A/B/C 比較で、完全静止（A）を既定にし、動かすなら説明中の図・語・数値を直接強調する、と決めたのは、「静かな場面では動くものに目が行く」をそのまま使った形に読める（推測）。人物カードの focus ring（B）が「解説上無意味」だったのは、目を引いた先に説明すべきものが無かったから、と読める
- **逆向きの経験**: [[exp-sutra-hype-editions]] では、不生不滅を「静止」で表したら「単にバグに見える、テンションも下がる」と言われた。Lasseter の「忙しい場面では止まったものに目が行く」は**一部が止まる**話で、[[exp-sutra-hype-editions]] は**画面全体の変化が止まった**話なので、食い違いではなく条件が違う（推測）。promo の速い場面で「止まったものに目を向ける」演出が効くかは試していない
- **Timing の「足りるだけ、それ以上でなく」**: [[exp-polis-magi-op]] の v1（平均 4.5 秒/場面）が「しょぼい」と言われ、実物の平均 1.07 秒に寄せたのは「時間をかけすぎると注意がさまよう」側の失敗に当たる。逆に [[exp-sutra-hype-editions]] の「閃光の減衰 0.35 秒で約 1 秒字が読めなかった」は、動きが読みを邪魔した例
- **Anticipation は「目を正しい場所に向ける」装置**: 120BPM の小節頭で切り替える [[exp-html-capture-pipeline]] の作りは、拍が予備動作の代わりになって「次に変わる」を予告している、と読める（推測。拍の効果を測ってはいない）。[[exp-sutra-hype-editions]] のビルド→ドロップ（ドロップ直前 1 拍は無音＋暗転）は、音で予備動作をしている
- **スプラインの行き過ぎ**: 時刻表の補間でイージングに back 系（行き過ぎるもの）を使うと（[[exp-nishio-showreel]] は expo・cubic・back を場面ごとに変えた）、意図しない向きに一瞬動くことがある。Lasseter は「予備動作に見えて良いこともあるが、多くは望ましくない」と書く
- 型ごと: Timing・Staging・Anticipation は型によらない（any）。Squash and stretch・Exaggeration・Appeal は promo のキャラクター・ロゴの動きに効きそうだが、talk の図解に当てると飾りになりやすい（[[web-tversky-2002-animation-can-it-facilitate]] の Apprehension 原則、[[web-berney-betrancourt-2016-animation-meta-analysis]] とつながる。推測）

## Open Questions

- Thomas & Johnston の本文（12 項目の並び、Solid Drawing の扱い、各原則の元の説明）は未読。Lasseter の要約がどこまで本に忠実かは確かめていない
- 中割りの枚数表は何 fps・何コマ撮りを前提にしているか書いていない。秒に直せない
- Lasseter の原則は「観客を楽しませる」キャラクターアニメのための経験則で、理解（学習）を測った研究ではない。解説動画で効くかは、学習研究（[[web-berney-betrancourt-2016-animation-meta-analysis]]）と別に確かめる必要がある
- 「静かな場面では動くもの、忙しい場面では止まったものに目が行く」は、promo の速い場面で一要素だけ止める演出として使えるか。[[exp-sutra-hype-editions]] の「止めたらバグに見えた」とどう両立するか
- Willenskomer "UX in Motion" の 12 principles（UI への移し替え）は、Medium の本文が取得できず読めていない
