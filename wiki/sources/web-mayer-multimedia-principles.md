---
type: source
summary: Mayer のマルチメディア学習の 15 原則（Mayer 2024 の表 6、Mayer 2021 から。自分の研究室の実験の効果量）と、それを他のメタ分析 29 本で検証し直した Noetel ら 2022 のメタメタ分析。独立のメタ分析では効果量がおおむね Mayer の値の半分前後になり、redundancy は向きが逆に出た。設計の原則は「システムがペースを決める（講演のような）教材」と「複雑な教材」でより効くと報告している
video_types: [talk, embed]
url: https://doi.org/10.1007/s10648-023-09842-1
author: Richard E. Mayer（UC Santa Barbara）／ Michael Noetel, Shantell Griffith, Oscar Delaney, Nicola Rose Harris, Taren Sanders, Philip Parker, Borja del Pozo Cruz, Chris Lonsdale
published: 2024-01-17（Mayer）／ 2021-10 オンライン、2022-06 号（Noetel ら）
retrieved: 2026-11-09
sources:
  - https://link.springer.com/content/pdf/10.1007/s10648-023-09842-1.pdf （Mayer, R. E. (2024). The Past, Present, and Future of the Cognitive Theory of Multimedia Learning. Educational Psychology Review 36:8。オープンアクセス、全文を読んだ）
  - https://doi.org/10.3102/00346543211052329 （Noetel et al. (2022). Multimedia Design for Learning: An Overview of Reviews With Meta-Meta-Analysis. Review of Educational Research 92(3), 413–454。出版社のページは取れず、https://files.constantcontact.com/1145f86e901/7bc63268-3738-46ae-9ee0-fbdafb58537f.pdf にある出版版の写しで全文を読んだ）
---

# マルチメディア学習の原則（Mayer 2024 の 15 原則と Noetel ら 2022 のメタメタ分析）

## 何の文献か

- **Mayer (2024)**: Educational Psychology Review の招待エッセイ（査読誌）。cognitive theory of multimedia learning（CTML）の 40 年の変遷をまとめ、表 6 に「15 principles of multimedia instructional design (from Mayer, 2021)」として、原則ごとの効果量と検定数（Tests）を載せている。数値は Mayer の研究室と共同研究者の実験から（本文「15 evidence-based principles based on more than 200 experiments conducted by my colleagues and me」）。版ごとの実験比較数は 2001 年版 45、2009 年版 93、2021 年版 201（表 3）
- **Noetel et al. (2022)**: Review of Educational Research（査読誌）の overview of reviews。マルチメディア設計の効果を扱った系統的レビュー 29 本（一次研究 1,189 本、参加者 78,177 人と抄録、本文では 79,415 人）を集め、23 本から 674 の効果量を二重抽出し、多層ランダム効果モデルでメタメタ分析した。原則ごとに一番包括的なレビューを選んで一次研究の重複を避けた（Results 節）

この二つを一ページにしたのは、Noetel らが Mayer の数値の出し方を名指しで批判し、同じ原則を独立のメタ分析で測り直しているため。片方だけ読むと効果量の大きさを取り違える。

## 書いてあること

### CTML の前提（Mayer 2024）

核の三つは変わっていないと書いている: dual channels（視覚と聴覚・言語で別の処理経路）、limited capacity（処理容量は厳しく限られる）、active processing（選ぶ・まとめる・既有知識と統合する）。原則は三つの目標に分けられる: 余計な処理（extraneous）を減らす／本質的な処理（essential）を管理する／生成的な処理（generative）を促す。「Each principle is subject to boundary conditions including for whom the principle applies, for which kind of lesson the principle applies, and under what circumstances」と書くが、境界条件の中身は Mayer (2021) の本に回していて、このエッセイには載っていない。

### 原則ごとの効果量: Mayer の研究室の値と、独立のメタ分析の値

左は Mayer 2024 表 6（効果量 d と検定数）。右は Noetel ら 2022 が採ったメタ分析の値（g、k は効果量の数）。Noetel らは Mayer (2008) の値を「Mayer calculated the unweighted median effect size from a group of studies he and his colleagues had conducted」と説明しており、表 6 の値も同じ作り方と思われるが、表 6 自体には "Effect size" とだけあり中央値とは書いていない。

| 原則（Mayer の言い方） | Mayer 2024 表 6 | 独立のメタ分析（Noetel ら 2022 による） | 効く条件・注記 |
|---|---|---|---|
| Coherence（余計なものを除く） | 0.86（19） | 誘惑的な細部を除く g = 0.33, 95% CI [0.18, 0.48], k = 68（Sundararajan & Adesope 2020） | 細部が画面に**出しっぱなし**のとき g = 0.43（k = 47）、一時的なら g = 0.12（CI が 0 をまたぐ, k = 18）。既有知識のない学習者で g = 0.52（Noetel 表 1） |
| Signaling（構成を強調する手がかり） | 0.69（16） | g = 0.43, [0.35, 0.50], k = 209（S. Schneider et al. 2018） | 低既有知識で効く: d = 0.47（Alpizar 2020）、r = 0.19 対 高既有知識 r = −0.08（Richter 2016）。動く手がかりで d = 0.43（Alpizar）。Schneider 2018 は既有知識の高低・システム／学習者ペースのどちらでも効いたと報告。文字の強調のほうが図の強調より効いた（Noetel 表 1） |
| Redundancy（図＋ナレーションに同じ文字を足さない） | 0.10（12）。原則の文は「when the lesson is fast-paced」付き | **逆向き**: 言語の冗長は学習を少し上げた g = 0.15, [0.08, 0.22], k = 57。音声に文字を足すと g = 0.29（k = 34）、文字に音声を足すと g = −0.04（k = 23）（Adesope & Nesbit 2012） | Adesope & Nesbit の正の効果は学習者ペース／システムペース、教室／実験室を通じて一貫（Noetel 表 1）。L2 動画の字幕は g = 0.99, k = 15（Montero Perez 2013） |
| Spatial contiguity（対応する語と絵を近くに） | 0.82（9） | g = 0.63, [0.55, 0.71], k = 58（Schroeder & Cenkci 2018） | Ginns 2006 では空間 d = 0.72、時間 d = 0.78、全体 g = 0.74（k = 46） |
| Temporal contiguity（対応する語と絵を同時に） | 1.31（8） | g = 0.78, [0.64, 0.92], k = 13（Ginns 2006） | Noetel らは例に「話し手が触れる箇条書きを一つずつ出す」を挙げる |
| Segmenting（学習者がペースを決める区切り） | 0.67（7） | g = 0.34, [0.30, 0.38], k = 123（Rey et al. 2019） | 教える側が区切ると g = 0.41（k = 32）、学習者に区切らせると g = 0.20（k = 32）。区切った教材は学習時間が長くなった（g = 0.92） |
| Pre-training（主要概念の名前と特徴を先に） | 0.78（10） | Noetel の結果節には独立の推定が見当たらなかった | — |
| Modality（図＋画面の文字より、図＋ナレーション） | 1.00（19） | g = 0.38, [0.33, 0.43], k = 86（Reinwein 2012）。出版バイアスを補正すると g = 0.20 | Ginns 2005 ではシステムペースの提示でだけ効いた（d = 0.93）。Reinwein 2012 では学習者が自分のペースで進めると効果が消え、短い文・動的な視覚化で大きい（Noetel 表 1） |
| Multimedia（語だけより語＋絵） | 1.35（13） | — | — |
| Personalization（会話調） | 1.00（15） | g = 0.33, [0.23, 0.44], k = 55（Ginns et al. 2013） | 出版バイアスの兆候あり（Noetel 表 1） |
| Voice（機械の声より親しみのある人の声） | 0.74（7） | — | — |
| Image（話し手の姿を足しても必ずしも良くならない） | 0.20（7） | 教育エージェント g = 0.19（k = 43）。エージェントが要所を指し示す（signaling の働き）と g = 0.28（k = 7）。3D のエージェントは g = 0.11（効果なし）、2D は g = 0.38 | — |
| Embodiment（画面の講師の身振りが豊か） | 0.58（17） | — | — |
| Immersion（3D VR が 2D より良いとは限らない） | −0.10（9） | — | — |
| Generative activity（学習中の要約・説明などを促す） | 0.71（44） | — | — |
| （Mayer の 15 にない）Animation | — | 静止図よりアニメ g = 0.23（Berney & Bétrancourt 2016）。表現的なアニメ g = 0.40、装飾的なアニメ g = −0.05（Höffler & Leutner 2007） | [[web-berney-betrancourt-2016-animation-meta-analysis]] |

（Mayer の列は Mayer 2024 表 6。右の 2 列は Noetel ら 2022 の「Synthesis of Review Findings」節と表 1）

### 全体の大きさと、効く条件（Noetel ら 2022）

- 規模の大きい 11 本のレビュー（808 効果量、66,553 人）で、設計原則の平均効果は g = 0.38, 95% CI [0.27, 0.49]。保持テスト（g = 0.42）と転移テスト（g = 0.43）でほとんど同じ（Results 節）
- 大きいのは L2 動画の字幕、時間・空間の近接、signaling、modality。弱いが正なのは言語の冗長と教育エージェント
- **ペース**: 設計原則は「システムがペースを決める（講演のような）」教材で g = 0.41、「学習者がペースを決める（ウェブサイトのような）」教材で g = 0.27。調整効果は有意（R² = 0.34, p = 0.02）
- **複雑さ（element interactivity）**: 複雑な教材で g = 0.70、単純な教材で g = 0.20
- **既有知識**: 全体としては調整効果が有意でなかった（p = 0.14）。ただし signaling や coherence の個別のレビューは低既有知識で大きいと報告（上の表）。expertise reversal（既有知識が高いと良い設計の利点が減る）は非系統的レビューの支持にとどまる、と限界の節に書いている
- 認知負荷の管理への効果は小さい（g = 0.22）

### Noetel らが書いている限界

- 含めたレビューの質が低い: 二重スクリーニングを明記したのは 29 本中 2 本、一次研究の質を評価したのは 1 本だけ。出版バイアスの評価法も誤りやすいものが多い
- 学習と認知負荷だけを見て、満足度・動機づけ・エンゲージメントだけを測ったレビューは外した
- レビューのないもの（例: 対話形式の教材）は推定できない

## この wiki への含意

### 「画面に出す文と読み上げる文を分ける」と redundancy

- [[exp-qualia-video]] は台本の各区間に字幕用 `caption` と TTS 用 `narration` を別に書き、journey で「読み上げるのは役割・失敗・判断・次の行動」「画面だけに出すのは製品名・主要な接続・概数・公開 URL」「正確な version・seed・hash は wiki だけ」と書き分けた。これは redundancy 原則の「同じ文を二重に出すな」とは違い、**語の表記の分離**（「空の吹き出し」／「からの吹き出し」）と**チャンネルへの情報の割り振り**が中心で、画面には字幕も残っている（40 件すべて 1 行）
- 研究との照らし合わせ: Mayer の redundancy は 0.10（12 検定）と小さく、しかも「速いペースの教材」という条件付き。独立のメタ分析（Adesope & Nesbit 2012）は逆に、音声に文字を足すと g = 0.29 と報告している。Noetel らは理由の一つに「音声は読み返せない。聞き逃したら文字で直せる」を挙げる。TTS の読み違い（「こえつき」が「こわつき」に聞こえた件）があった [[exp-qualia-video]] では、字幕は聞き違いを直す役に立ちうる。文献の側からは、字幕を消す根拠は弱い
- ただし Noetel らは「death by PowerPoint」のように、話と文字を結びつける手間が大きすぎる場合は冗長が害になりうるとも書いている。「字幕は 1 行・要点だけ・話と同時に出す」は temporal contiguity（Ginns 2006 で g = 0.78）と両立する

### 「完全静止を既定」と coherence・signaling

- [[exp-qualia-video]] の A/B/C 比較で採ったのは「全画面は動かさず、説明中の図・語・数値・工程 node だけを highlight する」。前半は coherence（余計なものを除く。独立のメタ分析で g = 0.33）、後半は signaling（g = 0.43）にあたる。B 案の「人物 card の focus ring」は説明対象を指していない手がかりで、「解説上無意味」という評価は signaling の定義（本質的な内容の構成を強調する）と合う
- journey v3 →v4 で装飾の場面絵（画面の 36%）を 0% にした件は、Sundararajan & Adesope の「誘惑的な細部が出しっぱなしのとき害が大きい（g = 0.43 対 一時的 0.12）」と同じ向き
- ただし [[exp-qualia-video]] の評価は人間 1 人の好み（「気持ち悪い」「わからん」）で、学習テストではない。研究が支えるのは「装飾の動きは学習を上げない」までで、「静止のほうが学習が上がる」ではない

### 「無音で字幕だけで通じる promo」と modality

- modality 原則（Mayer 1.00、独立のメタ分析 g = 0.38、補正後 0.20）は「図＋画面の文字」と「図＋ナレーション」の比較で、聞こえることが前提。無音で自動再生される X では、そもそもナレーションという選択肢がない（[[exp-democracy-river-video]]、[[exp-words-as-public-goods-video]]）。だから「字幕だけの promo」は modality 原則に反しているのではなく、原則の前提の外にある
- それでも原則から引けること（推論、未検証）: 文字が視覚の経路を絵と取り合うので、字幕は短く、絵の近くに、絵が変わる瞬間に出す（spatial/temporal contiguity）。また Reinwein 2012 は modality の効果を「短い文で大きい」とする。promo の測度はふつう学習でなく注意や再生完了なので、そもそもこれらの効果量はそのまま移せない
- talk は音声が前提なので modality が効く側にいる。[[three-video-types]] の「promo は無音前提、talk は音声前提」という分け方は、研究の前提条件の違いとして説明できる

### ペースと embed

- 設計原則は「システムがペースを決める」教材でより効く（g = 0.41 対 0.27）。講演の中で流す embed は、聴衆が止められないのでシステムペースの典型。talk の YouTube 動画も一時停止はできるが、多くの視聴者は流して観る。つまり embed では coherence・signaling・contiguity をより丁寧にやる意味がある
- 話し手が横にいる embed では、動画を止めて話すことが segmenting（教える側が区切ると g = 0.41）の代わりになりうる。また話し手が流す前に概念の名前を言っておくことは pre-training（Mayer 0.78、独立の推定は見つからず）にあたる。どちらも未検証
- Mayer の voice 原則（機械より人の声、0.74、7 検定）は TTS を使う [[exp-qualia-video]]・[[exp-galleria-tts-and-singing]] に関係するが、比べた「機械の声」がいつの合成音声かはこのエッセイからは分からない（原典未読）

## Open Questions

- **効果量の大きさの食い違い**: Mayer の研究室の値は独立のメタ分析のおよそ 1.5〜3 倍（coherence 0.86 対 0.33、modality 1.00 対 0.38、personalization 1.00 対 0.33）。Noetel らは Mayer の値を「研究室内の重みなし中央値で、系統的でない」と批判している。この wiki で原則の強さを引くときは、独立のメタ分析の値を主に使うべきか
- **redundancy の向き**: Mayer は「足すな（速いペースの教材で）」、Adesope & Nesbit は「音声に文字を足すと少し良い」。Adesope & Nesbit の比較に図があったかどうか（Mayer の条件は図＋ナレーション＋文字）は Noetel の要約からは分からない。Noetel らは「図がないときは文字を足せ、図があるときは声で」と読んでいる。字幕つきの解説動画（図＋声＋字幕）がどちらの条件に入るかは未決
- Mayer の境界条件（どの学習者・どの教材・どの状況で）の中身は Mayer (2021) と Mayer (2017) "Using multimedia for e-learning"（J Computer Assisted Learning 33(5)）に書かれているはずだが、どちらも本文を取得できなかった（Wiley は 403）。Mayer (2008, American Psychologist) も本文未読
- Mayer 2024 の本文は原則を「5・4・6」に分けると書くが、表 6 の区切りは 5・3・7 で、三つ目の見出しが二つ目と同じ「managing essential processing」になっている。誤植と思われる
- 日本語の TTS と字幕で、redundancy・modality・voice の研究（主に英語、主に人の声または古い合成音声）がどこまで移るか
- promo の目的（止めてもらう・興味を持たせる）を測った研究は、この二つの文献の範囲外
