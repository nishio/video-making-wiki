---
type: source
summary: IBM Design Language の Animation（ブランドのアニメーション・動画向け）と Carbon Design System の Motion（UI 向け）。両方とも productive（効率・控えめ）と expressive（熱量・目立つ）の二種で動きを分け、expressive は「時々の重要な瞬間」に取っておくと書く。Animation 側は「デザインが込み入るほど動きは小さく」「24fps 未満にしない」「一度に一軸」、Carbon 側は 70〜700ms の duration トークンと cubic-bezier を出している
video_types: [any]
url: https://www.ibm.com/design/language/animation/overview/
author: IBM（IBM Design Language／Carbon Design System）
published: unknown（IBM Design Language の各ページは「Last updated 05 November 2026」と表示）
retrieved: 2026-11-09
sources:
  - https://www.ibm.com/design/language/animation/overview/
  - https://www.ibm.com/design/language/animation/classic-principles/
  - https://www.ibm.com/design/language/animation/tips-and-techniques/
  - https://carbondesignsystem.com/elements/motion/overview/
---

# IBM Design Language「Animation」と Carbon「Motion」

## 何の文献か

- IBM の公式デザインガイド。二つある:
  - **IBM Design Language の Animation**（overview・classic principles・tips and techniques の 3 ページ）。ブランドの表現としてのアニメーションの指針で、「from simple to complex, ambient loop to feature brand film」と、ループ素材からブランド映像まで対象にしている。**この wiki で読んだ UI 系の指針の中で、動画・モーショングラフィックスを直接の対象にしているのはこれだけ**
  - **Carbon Design System の Motion**（elements/motion/overview）。製品 UI の動きの指針で、easing の数値と duration のトークンを出している
- どちらも 2026-11-09 時点の公式ページによる。IBM Design Language の 3 ページは「Last updated 05 November 2026」。Carbon のページは更新日を確かめていない
- 実験や測定の報告ではなく、社内の様式の決まり。効果の根拠は示されていない

## 書いてあること

### 二つの型: productive と expressive（両方に共通）

- Animation overview: 「Productive motion leans toward efficiency and responsiveness. Expressive motion is enthusiastic and vibrant.」二つの「会話（conversation）」がはっきり見えるときアニメーションは最もよくなる、作品全体もどちらかに寄せられる、と書く。productive は「professional, confident, smart and efficient」、expressive は「more personality and emotion」の印象を作る
- Carbon: 「Reserve expressive motion for occasional, important moments, to better capture the user's attention and offer a rhythmic break to the productive experience.」productive は作業に集中すべき場面（ボタンの状態、ドロップダウン、データ表や可視化の描画）、expressive は新しいページを開く・主要な操作・**動きそのものが意味を運ぶとき**・通知、と書く

### Animation（ブランドのアニメーション）: 原則と技法

overview の四つの方針: Effective（「Motion is uniquely effective in its capacity to explain ideas sequentially and rapidly refocus on what's important」）、Concise（視聴者の時間と注意を尊重する）、Simple（「Animate only what's vital」）、Engineered。

classic principles のページは「12 basic principles of animation」をグラフィックの形に当てるための IBM の解釈を 12 項目で書いている（Lasseter の 11 項目との違いは [[web-motion-lasseter-1987-principles-of-traditional-animation]]）。主なもの:

- Squash and stretch: 加速と反応は使うが、伸び縮み・変形は控える。「precision and accuracy, not cartoonish playfulness」
- Staging: 「Lead the eye.」込み入った構図・背景を避け、順に動く要素で注意を向け、競合する動作を控える
- Slow in and slow out: 素早く加速し滑らかに減速するのが典型。「Animation curves that suggest bounce, stretch or abrupt stops aren't recommended.」
- Arc: **元の原則と逆に**、要素は一度に一軸ずつ動かし、軸の間を少し重ねる
- Timing: 「Be decisive in getting from point A to point B. Avoid long exponential eases as elements settle into place.」
- Exaggeration: 飾りで目を引くことではなく、機能と目的をはっきり見せる動かし方

tips and techniques の主な記述:

- **複雑さの反比例**: 「every movement of an element increases the density of information presented to a viewer」。だから「minimally populated compositions lend themselves to more expressive and expansive animation, while dense and complex designs benefit from smaller, more textural motion.」（「Detailed visuals call for subtle animations. Simple designs allow for dynamic animation.」）
- Focus: 注目点を一つ保ち、次の対象へ継ぎ目なく移す。「With the brief and dense nature of most animation, be cognizant of how you capture and shift a viewer's focus to minimize confusion and fatigue.」
- Camera: 一軸の移動は意図的で目立たず、つながれていない動的なカメラは混沌と不確かさを与える。動的なカメラが必要なら制御し、焦点をはっきりさせる
- Detail: 透明な形が重なるときの乱れを避けるため、不透明度でなく色の間でアニメートする。線は crossfade せず太さを 0 から上げる
- Consistency: 要素が画面に出入りする向き、crossfade、文字のふるまいを揃える。一貫性が「基準」になり、そこからの急な変化が目立つ
- Rhythm: 「rarely does everything happen at once」。ずらし（stagger）、因果の瞬間、動いてから休む、で「viewer a mental pause」を作る
- Fluidity: 「motion requires animating at or above 24 frames per second (FPS)」「Don't use a frame rate lower than 24 frames per second.」
- Mass and momentum: 衝突・摩擦・滑りで魅力を出せるが、「avoid cartoonish overshoots and bounces」
- Structure: アニメは sequential（始点と終点のある A→B の物語）か looped。「Loops continue in a usually seamless cycle and often only convey a singular idea or message.」「Use simple loops to convey individual concepts.」入れ子のループはずらして注意を領域から領域へ導く
- Type: 読む自然なリズム（左→右、上→下）で出す。**一度に一軸**。読めて理解できるだけ画面に残す。中央揃えの段落と多軸の同時の出現を避ける（文字の動きの詳細は文字・字幕の担当のページに譲る）

### Carbon（UI）: easing と duration の数値

easing（Carbon の表から）:

| | productive | expressive |
|---|---|---|
| standard（最初から最後まで見えている要素） | cubic-bezier(0.2, 0, 0.38, 0.9) | cubic-bezier(0.4, 0.14, 0.3, 1) |
| entrance | cubic-bezier(0, 0, 0.38, 0.9) | cubic-bezier(0, 0, 0.3, 1) |
| exit（画面から去る。去るときは加速） | cubic-bezier(0.2, 0, 1, 0.9) | cubic-bezier(0.4, 0.14, 1, 1) |

- 「Strictly linear movement appears unnatural to the human eye.」要素は素早く加速し滑らかに減速する、と書く
- exit の例外: 画面から出ても近くに留まって呼び戻せる要素（サイドパネル）は standard easing（減速しながら出る）を使う

duration（「Duration is calculated based on the style and size of the motion」。productive は expressive よりかなり速い。距離・拡大が大きいほど長く。非線形の尺度で、Motion Generator で個別に計算する。静的トークンは 6 個）:

| トークン | 用途（原文の要約） | 値 |
|---|---|---|
| duration-fast-01 | ボタン・トグルなどの微小な操作 | 70ms |
| duration-fast-02 | フェードなどの微小な操作 | 110ms |
| duration-moderate-01 | 小さな展開、短い距離の移動 | 150ms |
| duration-moderate-02 | 展開、システムの通知、toast | 240ms |
| duration-slow-01 | 大きな展開、重要な通知 | 400ms |
| duration-slow-02 | 背景の暗転 | 700ms |

評価のチェックリスト: 微小な操作は 90〜120ms の固定に収まるか。大きな・全画面の遷移では、案内する「連続した要素」があるか。「The best interface motion may go unnoticed」平均的な利用者がしばしば気づく動きなら、外すか減らす。Adaptive interface motion: 動きを知覚・処理しにくい利用者がいるので、状態の遷移には常に代替を用意し、同じことを静的にも伝えられるようにする。

## この wiki への含意

### 指針が書いている範囲と、動画へ移せる範囲（推測）

- **Carbon の数値（70〜700ms）は UI の状態遷移についての値**で、利用者の操作に応答する数百ミリ秒の話。数十秒〜数分の動画の場面転換の長さを決める根拠にはならない。移せそうなのは「距離・面積が大きいほど長く」「入るときは減速、出るときは加速」「去って戻らないものは加速して出す」という**向き**だけ（推測）
- **IBM Design Language の Animation はブランド映像まで対象**なので、動画への距離は Carbon より近い。ただしこれも IBM のブランドの様式（落ち着いた・漫画的でない）を守るための決まりで、「漫画的な行き過ぎ・跳ねを避ける」は IBM の声の選択であって、普遍則として書かれてはいない

### 経験との照合

- **「複雑なデザインほど動きは小さく、簡素なデザインほど動きは大きく」は、[[three-video-types]] の「動きの評価が promo と talk で逆向き」に一つの説明を与える**。talk のクオリアさん解説は図・語・数値の詰まったスライドで、全画面の drift を「気持ち悪い」と言われ完全静止を既定にした（[[exp-qualia-video]]）。promo の叩き込み文字（[[exp-gyazo-resumption-video]]）・アゲアゲ版（[[exp-sutra-hype-editions]]）は 1 画面の要素が少なく、大きく動かして「変化が止まると下がる」と言われた。IBM の言い方では、型の違いより**画面の情報の密度**が動きの量を決めている、とも読める（推測。IBM はこの関係の根拠を示していない）
- **productive / expressive の「会話」と「expressive は時々」**: [[exp-sutra-hype-editions]] の「否定区間で光らせ続けたらインパクトが減った。打つたびに叩きつけ、間は 4 割に沈める」「同じものを 3 回繰り返すと 2 回目で慣れる」は、expressive を連続させると効かなくなるという Carbon の書き方と同じ向き。Polis の OP 様式（[[exp-polis-magi-op]]）の v4 で「アウトロ 10 秒の静止クレジットが死んだ拍」とされたのは、逆に productive すぎる区間の問題
- **Rhythm（ずらし・動いてから休む）**: 120BPM の小節頭で切り替え、時刻表に「ずらし（stagger）」を持たせた作り（[[exp-html-capture-pipeline]]、[[exp-nishio-showreel]] の粒子ごとの遅れ）は、IBM の Rhythm の技法と同じ
- **24fps 以上**: 経験の動画は 30fps または 60fps で、条件を満たしている（[[exp-html-capture-pipeline]]、[[exp-polis-magi-op]]）
- **ループは一つの概念を運ぶ**: embed（プレゼンに埋め込む特定概念の解説）にそのまま当たりそうな記述。ただし西尾の embed は「流しっぱなしの前提」（[[embed]] の Updates）で、ループとは限らない。IBM の言う sequential（A→B の物語）の方が流しっぱなしの embed に近いかもしれない（推測）
- **カメラの一軸移動**: [[exp-qualia-video]] で否定された「全 scene に 1.8% の拡大と sin 波の低速パン」は、IBM の言う「意図の見えないカメラの動き」に当たりそう（推測）。IBM は「一軸で制御された移動は目立たない」と書くので、低速パンそのものより、目的が無いことが問題だった可能性がある

## Open Questions

- 「複雑さと動きの反比例」は IBM の経験則で、根拠（測定）は示されていない。talk の静止の既定が、情報密度のせいなのか、ナレーションが主導する型のせいなのかは、経験からは分けられない
- Carbon の Motion Generator（距離から duration を出す非線形の式）の中身は読んでいない
- IBM Design Language の Animation の各ページにある例の動画は見ていない（文字だけ読んだ）
- 「漫画的な行き過ぎと跳ねを避ける」（IBM）と、Gyazo の叩き込み文字の「1.8 倍 → 1 倍に縮んで着地しオーバーシュート」（[[exp-gyazo-resumption-video]]）・Polis v4 の「ばね」（[[exp-polis-magi-op]]）は向きが逆。IBM の様式の選択か、promo では跳ねが効くのかは分からない
