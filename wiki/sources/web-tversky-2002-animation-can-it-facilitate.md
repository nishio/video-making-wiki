---
type: source
summary: Tversky・Morrison・Bétrancourt（2002, IJHCS）の文献レビュー。アニメーションが静止図より良いとされた研究の多くは、アニメ側に情報が多い・操作や予測の手続きがある、という比べ方の不備によるもので、同じ情報の静止図と比べると利点はほとんど見つからないと書く。良い図の条件として Congruence（中身の構造と図の構造を合わせる）と Apprehension（正確に知覚・理解できる）の二原則を挙げ、アニメは速すぎ・複雑すぎて後者に反しやすいとする
video_types: [embed, talk]
url: https://hci.stanford.edu/courses/cs448b/papers/Tversky_AnimationFacilitate_IJHCS02.pdf
author: Barbara Tversky, Julie Bauer Morrison（Stanford University）, Mireille Bétrancourt（INRIA Rhône-Alpes）
published: 2002（International Journal of Human-Computer Studies 57(4), 247–262）
retrieved: 2026-11-09
sources:
  - https://hci.stanford.edu/courses/cs448b/papers/Tversky_AnimationFacilitate_IJHCS02.pdf
  - https://doi.org/10.1006/ijhc.2002.1017
---

# Tversky, Morrison, Bétrancourt (2002) Animation: can it facilitate?

## 何の文献か

International Journal of Human-Computer Studies の査読論文。種類は**選択的な文献レビュー**で、メタ分析ではない（「We will selectively review research on animation」）。対象は複雑な系（機械・生物・物理・操作・計算）を教えるアニメーションで、結論もその範囲に限ると自ら書く（3.4 Caveats）。効果量は出していない。

## 書いてあること

### 前提: 図が効く条件

- 図の研究は「慎重に設計された適切な図だけが、複雑な系を伝えるのに役立つ」と示してきた、と書く（抄録）
- **Congruence Principle**: 「the structure and content of the external representation should correspond to the desired structure and content of the internal representation」。たとえば道順は「曲がり角の列」として理解されるので、良い道順の図は曲がり角を中心に作る
- この原則からは、時間の変化を表すアニメは「時間の変化」を伝えるのに自然に合うはず、と期待される（1.5 節）

### アニメが勝ったとされた研究の多くは比べ方が悪かった（2 節）

- **情報が同じでない**: Baek & Layne (1988) の速さの問題、Large ら (1996) の心臓（アニメにだけ血流の経路）、Rieber の運動の法則（静止図に慣性の情報がない）、Park & Gittelman (1992) の回路、Thompson & Riding (1990) のピタゴラスの定理（連続アニメだけが細かい手順を見せた）。どれもアニメ側に**細かい途中の動き（microsteps）**が多く、それは静止図でも描けた情報だった
- **手続きが同じでない**: アニメ側だけ操作（interactivity）や予測（prediction）がある。操作も予測も、それだけで学習を助けると知られている（Hegarty ら 1999 → 後の研究ではアニメそのものの利点なし、Hegarty ら 2002）。Kieras (1992) はテスト中も図を見られたので、理解でなく図を読む課題になっていた
- 比べ方が適切な研究では、利点がないものが多い: Morrison & Tversky (2001)、Rieber (1989)、ChanLin (1998)、Byrne ら (1999、予測つきの静止図と同等)、コンピューターの操作を教えるアニメ（Payne ら 1992 など）。Palmiter らでは、アニメで学んだ人は訓練は速かったがテストでは遅く、1 週間後には成績が下がった
- アニメは時間がかかり、いつも好まれるわけでもなく、天気図のアニメを見た初心者は目立つ所にだけ注意を向けて因果を読み取れなかった（Lowe 1999）

### なぜ失敗するか: Apprehension Principle（3 節）

- 「the structure and content of the external representation should be readily and accurately perceived and comprehended」
- **知覚しにくい**: 馬の脚のように、速く複雑な動きは正確に見えない。単純な軌跡でさえ、知覚は物理でなく Gestalt 的な傾向に引っ張られる
- **連続でも離散的に理解される**: 人は滑らかな動きを段階の列として理解することが多い。それなら段階ごとの静止図のほうが自然で、しかも静止図の並びは**比べたり見直したりできる**。アニメは「fleeting, they disappear」
- **操作で補える**: 止める・戻す・拡大する・速さを変えられれば、知覚の問題は和らぐかもしれない（ただし静止図も拡大はできるので、適切な実験はまだ、と書く）

### 結論（4 節）

- アニメが静止図より効くかもしれないのは、**連続的な変化の「様子（manner）」や、部品どうしの細かいタイミング（microsteps）**。しかしそれも「clever schematization of static diagrams may be just as effective」。矢印は順序と動きの向きを示すのに効く（Tversky ら 2000）
- Apprehension を満たすには、アニメは「slow and clear enough」でなければならず、「lean toward the schematic and away from the realistic」。矢印や強調で重要な変化に注意を向けること
- アニメの見込みのある使い道は、複雑な系の説明よりも、**時間と空間の中の実時間の変化や向きの変え方**（ウォークスルー、ダウンロードの進捗バーなど）
- 「Like all good things, animation must be used with care.」

## この wiki への含意

- **embed（一つの概念を短い動画で渡す）に直結する警告**: 「動かせば分かりやすい」は既定では成り立たない。動かすことに意味があるのは、伝えたい中身そのものが時間の変化（過程・順序・因果の流れ）で、しかもその変化が見て追える速さと単純さのときだけ（Congruence ＋ Apprehension）
- **[[exp-qualia-video]] の「完全静止が既定」と一致**: 全画面の drift と Wan2.2 の idle の微小な動きは、伝える中身と無関係な動き（Congruence に反する）で、評価は「気持ち悪い」「どこが変わったのかわからん」。Tversky らの枠組みでは、どちらも採る理由がない動き。[[exp-qualia-video]] の Open Questions にある「説明対象そのものを動かす I2V（指差し等）は比べていない」は、まさに Congruence を満たしうる側の比較で、まだやっていない
- **[[exp-sutra-sync-subtitles]] の「全部を常時表示し、変わるのは現在位置の色だけ」**: 意味ブロックごとに画面を切り替える案をやめ、全体を出したまま強調だけを動かした。Tversky らの「静止図の並びは比べたり見直したりできる、アニメは消える」と同じ判断で、しかも唱える音の時間の流れ（Congruence）に合わせて色だけが動く。動く部分が最小なので Apprehension も満たしやすい
- **連続より段階**: 「人は連続した動きを段階として理解する」なら、embed で過程を見せるときは、なめらかなモーフィングより、段階ごとに止まる見せ方（各段階で話し手が説明できる）が合うかもしれない。講演の中で話し手が止めて説明できる embed の場に向いている（推論、未検証）
- **promo との違い**: [[three-video-types]] の promo では「動きが止まるとテンションが下がる」（[[exp-sutra-hype-editions]]、[[exp-polis-magi-op]]）。Tversky らの議論は学習（理解）の話で、注意を引く・気分を上げることは対象外。promo の動きを否定する根拠にはならない

## Open Questions

- 2002 年のレビューで、対象は 1980〜2000 年ごろの研究。その後のメタ分析（[[web-berney-betrancourt-2016-animation-meta-analysis]]）は、アニメに小さな正の効果（g = 0.23）を見つけている。Tversky らの「比べ方の不備を除けば利点はほぼない」と、後のメタ分析の「小さいが正」をどう両立させるか（後者は情報が同じ比較に限っているのか）
- 「操作できるアニメなら補える」という見込みに対して、Berney & Bétrancourt は逆に「学習者がペースを操作できないとき（システムペース）だけ」効果が出たと報告している
- 抽象的な概念（矢印や図式で表すもの）を動かすことの効果は、このレビューの範囲（具体的な系の説明）の外
