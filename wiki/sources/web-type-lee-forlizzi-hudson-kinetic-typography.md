---
type: source
summary: キネティック・タイポグラフィ（動く文字）の研究。Lee・Forlizzi・Hudson 2002（UIST）は、動く文字が声の調子・登場人物・注意の誘導を伝えられると整理し、大きさ＝声量、震え＝高い覚醒などの技法と「注意を奪いすぎる」危険を書いたシステム論文で、効果は測っていない。感情の伝わり方を測った研究（Lee ら 2006、Xie ら 2023）は、作り込んだ動きなら感情がある程度一致して読み取られたと報告しているが、文脈が無いと読み取りは割れた
video_types: [promo, any]
url: http://www.cs.cmu.edu/~johnny/kt/dist/files/Kinetic_Typography.pdf
author: Johnny C. Lee, Jodi Forlizzi, Scott E. Hudson（Carnegie Mellon University）ほか
published: 2002
retrieved: 2026-11-09
sources:
  - http://www.cs.cmu.edu/~johnny/kt/dist/files/Kinetic_Typography.pdf （Lee, Forlizzi & Hudson 2002 "The Kinetic Typography Engine: An Extensible System for Animating Expressive Text", UIST '02, pp. 81–90。本文を読んだ）
  - http://www.cs.cmu.edu/~johnny/kt/ （CMU の Kinetic Typography のプロジェクトページ）
  - https://www.sciweavers.org/node/107675 （Lee, Jun, Forlizzi & Hudson 2006 "Using kinetic typography to convey emotion in text-based interpersonal communication", DIS '06, pp. 41–49 の抄録。本文未読）
  - https://arxiv.org/pdf/2306.07560 （Xie ら 2023 "Creating Emordle: Animating Word Cloud for Emotion Expression", IEEE TVCG。本文を読んだ）
---

# キネティック・タイポグラフィ: Lee・Forlizzi・Hudson 2002 と、感情の伝達を測った研究

## 何の文献か

- **Lee, Forlizzi & Hudson 2002**: 査読付きの国際会議 UIST の論文。動く文字を作るためのエンジン（Java、約 2700 行）の設計を書いたシステム論文で、**ユーザー実験は無い**。評価は「既存の作例約 30 本のコーパスの効果を再現できた」こと。前半に、動く文字が何を伝えるかの整理（先行の Ford ら 1997・Ishizaki 1998 などのまとめ）がある
- **Lee, Jun, Forlizzi & Hudson 2006**: 査読付きの国際会議 DIS の論文。チャットの文に動きを付けて感情を伝える研究。**抄録だけ読んだ**（sciweavers に載った抄録）
- **Xie ら 2023（Emordle）**: IEEE TVCG の論文（arXiv 版を読んだ）。ワードクラウドに動きを付けて感情を伝える研究で、クラウドソーシングの実験 2 本。動画の字幕ではなく、文字の集まりのアニメーション
- 読みやすさ（読む速さ・理解）への動く文字の効果を測った研究は、今回は原典に当たれなかった（Rashid ら 2008「Dancing with Words: Using Animated Text for Captioning」、IJHCI 24(5) は抄録も取れず未読）

## 書いてあること

### Lee, Forlizzi & Hudson 2002

**動く文字が伝えられるもの**（先行研究の整理として）

- 「Expression of affective (emotional) content」「Creation of characters」「Capture or direction of attention」の三つ
- 起源の一つは映画のタイトル（Saul Bass の『北北西に進路を取れ』1959、『サイコ』1960）で、情報を伝えるより雰囲気を作るために使われた。今はテレビ広告で多く使われ、「its ability to convey emotive content and direct the user's attention is generally a good match to the goals of advertising」
- もう一つの起源は読みの心理学の RSVP（1 語ずつ同じ位置に出す）。目の移動が要らないので訓練なしで速く読める、と書き、小さい画面で大きな文字を見せるために「trading time for space」できる、と書く（RSVP の研究そのものは引用のみ）

**声の調子を文字で写す技法**

- 声の高さ: 大きな上下の動き
- 声の大きさ: 文字の大きさ・太さ、ときにコントラストや色。大声には震える動き。震えと合わせて、言い終えた後も文字を残すと残響に見える
- 速さ・テンポ・リズム: 出す時刻・長さ・間で直接写す。1 語を引き伸ばすなら文字の幅を横に伸ばす
- 「analogous motion」（人の動作に似た動き）: 小さな震え＝期待・興奮・怒りなど覚醒の高い感情。縮む動き（肩を落とす）＝落胆。ゆっくりした呼吸のような動き＝共感
- 図の例: 同じ語でも、速いリズムの動き・大きさの変化・回転で「はしゃぎ」、地味な書体・減速・細くなる・縮むで「落胆」

**限界と危険**

- 「while kinetic typography can set the emotional tone of ambiguous text, it cannot normally replace or override strong emotive content intrinsic to the meaning of the text」。悲しい話を楽しい話にはできない。強めるか和らげるかだけ
- 登場人物を区別するには、位置・動きの型・書体・太さ・声の調子の表現を**一貫して**使う
- 注意: 突然現れるものは注意を奪う（attentional capture）。動くものは目を引き、経路に沿った動きは終点へ目を連れていく
- 「an important potential pitfall of kinetic typography techniques can be that they demand too much attention from the user」。注意を奪いたくないときは突然の出現を避ける
- 伝統的なアニメーションの技法（slow-in slow-out、squash and stretch、弧の動き、予備動作、follow-through）は動く文字にもそのまま使える
- 文字の拡大は幾何の拡大でなく活字の拡大（大きさに応じた字形・字間）で扱うべき、と書く（図 4）

### Lee, Jun, Forlizzi & Hudson 2006（抄録）

- 「three designers prepared 24 kinetic examples expressing four different emotions. We found that the examples were rated quite consistently by 66 participants.」
- 少数のデザイナーが作った既製の動きを、使う人が選んで感情を伝えられる見込みを示した「preliminary indication」と書く

### Xie ら 2023（Emordle）

- 4 つの感情（幸福・悲しみ・怒り・恐れ）にそれぞれ動き（DANCE・FADE・EXPLOSION・SHIVER）を作り、Prolific で実験
- 研究 I（100 人を募集し 30 人を品質検査で除外、1 問あたり平均 52.5 回答）: 語の意味を伏せた（lorem）ときは読み取りが割れ、DANCE・FADE・SHIVER は 40% 以上が意図した感情を選んだが、EXPLOSION は幸福 25.5%・怒り 21.6%・恐れ 17.6% に割れた。語の意味を見せると、幸福—DANCE 57.7%、悲しみ—FADE 82.7%、怒り—EXPLOSION 50.0%、恐れ—SHIVER 57.7% になった（偶然は 25%）
- 設計上の注意として「Maintaining readability」を挙げ、動きを誇張するほど感情は伝わるが文字の情報は読み取りにくくなる、と書く。最大の速さは読みやすさを、最小は効果を見て著者が経験的に決めた（測っていない）

## この wiki への含意

- **promo の「叩き込み文字」は、この整理の「声の大きさ」と「注意の誘導」にあたる**: Gyazo の `slam()`（0.14 秒で 1.8 倍 → 1 倍に縮んで着地しオーバーシュート）と山の揺れ（[[exp-gyazo-resumption-video]]）は、大きさ＝声量、震え＝高い覚醒、突然の出現＝注意の捕獲の組み合わせ。西尾の「ドーパミンアゲアゲ」の依頼と、Lee らの「広告の目的によく合う」は同じ向き。ただし Lee らの「注意を奪いすぎる」危険は、西尾が後に「技術の詳細を伝えるには適切ではない」と評価したことと噛み合う（解釈）
- **動く文字は意味を上書きできない**: Lee らの「強い感情の文を逆の感情にはできない」と、Emordle の「意味を伏せると読み取りが割れ、意味を見せると揃う」は、動きは文の意味の上に乗るだけ、と読める。アゲアゲ行者問答が「遅さを直しても面白くはならなかった」（[[exp-sutra-hype-editions]]）のは、テンポ（動き）では中身の面白さを作れない、という同じ向きの経験（推測）
- **速すぎる動きは見えない**: 「色」を 0.08 秒で枠へ滑らせても分からなかった（[[exp-sutra-hype-editions]]）。Lee らの「経路に沿った動きは終点へ目を連れていく」は、動きが見えるだけの時間があって成り立つ。最初から最終位置に置いた西尾の直し方は、注意の誘導をあきらめて読みを取った選択（解釈）
- **一貫した表現で人物を区別する**: Words の「日本語を大きく、英語を小さく」（[[exp-words-as-public-goods-video]]）は、二つの言語を位置と大きさで一貫して分けた形。Lee らの「一貫した視覚の属性で人物を区別」と同じ手法で、西尾の指摘「宛先が混ざっている」は表現の問題でなく中身の問題だった
- **経文の同期解説の「光る位置だけ動かす」**（[[exp-sutra-sync-subtitles]]）は、Lee らの言う RSVP の逆（文字は全部置いたまま、注意の位置だけ時間で動かす）。読み返しができる作り
- **talk ではほぼ使わない側**: クオリアさんは画面全体の drift を「気持ち悪い」と言われ、静止を既定にした（[[exp-qualia-video]]）。動く文字の文献は感情・注意の伝達を扱い、理解を助けるという報告は今回読んだ範囲には無い
- **embed（流しっぱなし）**: 話し手が横で話す場で、動く文字は「注意を奪いすぎる」危険が大きい（推測）

## Open Questions

- 動く文字が字幕の読みやすさ・理解をどう変えるかの実験（Rashid ら 2008 など）は原典を読めていない。読む速さの研究（[[web-type-szarkowska-2018-kruger-2022-subtitle-speed]]）は静止した字幕の話
- RSVP（1 語ずつ同じ位置に出す）が理解を下げるかには、後の研究で異論がある（Benedetto ら 2015 の Spritz の研究など。検索結果の要約しか読んでいない）。Gyazo の叩き込みは RSVP に近い形なので、確かめる価値がある
- Lee ら 2006 の 66 人の評定の詳細（どの感情がどれだけ一致したか）は抄録に無い
- 日本語の文字の動き（縦書き・漢字の一字の叩き込み）を扱った研究は今回見つけていない
