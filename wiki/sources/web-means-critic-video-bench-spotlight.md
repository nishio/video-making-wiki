---
type: source
summary: MLLM を動画の評価役にしたときの人との一致と見落としを測った 4 本。Video-Bench（CVPR 2025）は GPT-4o に問いを重ねさせ例を見せると人との一致が人どうしと同程度（α 0.50 対 0.52）になるが、時間の一貫性・動きは低いまま。VBench の「人と高相関」はモデル 4 つの勝率の相関。SPOTLIGHT（2025-11）は生成動画の誤りを時刻付きで探させ、Gemini 2.5 Pro は人の半分、誤りの種類ごとに分けて聞くと小さいモデルでも並ぶ。弱い評価役を混ぜた多数決はかえって悪くなる（ICLR 2025）
video_types: [promo, talk, any]
url: https://arxiv.org/abs/2504.04907
author: Hui Han, Siyuan Li ほか（Video-Bench、上海交通大・NUS ほか）／Ziqi Huang ほか（VBench、NTU S-Lab ほか）／Aditya Chinchure ほか（SPOTLIGHT、UBC・Vector Institute）／Ming Liu, Wensheng Zhang（Iowa State）
published: 2025-04-07（Video-Bench v1、v2 は 2025-04-29）／2023-11-29（VBench、CVPR 2024）／2025-11-22（SPOTLIGHT v1）／2025-03-07（Is Your Video Language Model a Reliable Judge?、ICLR 2025）
retrieved: 2026-11-09
sources:
  - https://arxiv.org/abs/2504.04907 （Video-Bench: Human-Aligned Video Generation Benchmark, v2）
  - https://arxiv.org/abs/2311.17982 （VBench: Comprehensive Benchmark Suite for Video Generative Models）
  - https://arxiv.org/abs/2511.18102 （SPOTLIGHT: Identifying and Localizing Video Generation Errors Using VLMs, v1）
  - https://arxiv.org/abs/2503.05977 （Is Your Video Language Model a Reliable Judge?, v1）
---

# MLLM を動画の評価役にしたときの一致と見落とし（Video-Bench・VBench・SPOTLIGHT ほか）

## 何の文献か

4 本とも arXiv の PDF 本文を読んだ。

- **Video-Bench**（arXiv 2504.04907 v2）: 表紙に CVPR 2025 とある（査読あり）。生成動画の評価を GPT-4o に任せる枠組みと、人の採点との一致
- **VBench**（arXiv 2311.17982、CVPR 2024）: 生成動画の 16 次元の自動評価（MLLM ではなく、次元ごとの専用の指標）と人の好みの一致。比較のために要点だけ読んだ
- **SPOTLIGHT**（arXiv 2511.18102 v1、プレプリント）: 生成動画の中の誤りを、時刻付きで見つけて説明できるか
- **Is Your Video Language Model a Reliable Judge?**（arXiv 2503.05977、ICLR 2025）: 動画の質問応答の答えを VLM に採点させるときの信頼性。正解は人ではなく、GPT-4o を含む LLM の討論で作っている

どれも対象は実写風の生成動画か動画 QA で、解説動画・コードで描く動画ではない。

## 書いてあること

### Video-Bench（CVPR 2025）

- 評価役は GPT-4o（gpt-4o-2024-08-06）にコマを入れ、GPT-4o-mini をテキストの補助に使う（§5.3）。工夫は 2 つ: **chain-of-query**（プロンプトとの一致を、問いを生成 → 答える → 最終点、と何度も問い直す。先に全体の描写を作り直させる）と **few-shot scoring**（点の各段の例を動画で見せる）（§4）
- 人の採点: 10 人、1 本に 4 人、計 35,196 件（§5.2）
- 人との相関（Spearman、Table 2）: Imaging Quality 0.733、Aesthetic 0.702、**Temporal Consistency 0.402、Motion Effects 0.514**、Video-text 0.732、Object-class 0.735、Color 0.750、Action 0.718、Scene 0.733。専用指標（MUSIQ 0.363、CLIP 0.260、RAFT 0.329 など）より高い
- 人どうしとの比較（Krippendorff's α、Table 3）: 人–人の平均 0.52、人–Video-Bench 0.50、**人–工夫なしの GPT 0.41**（Scene は 0.11）。時間の一貫性・動きは人–Video-Bench でも 0.48
- 工夫の効果（Table 4）: few-shot で品質系の平均 0.561 → 0.620、chain-of-query で一致系の平均 0.679 → 0.734
- 安定性: 同じ設定で 3 回回して、同じ点になった動画は 67%、α 0.867（§6.4）
- 著者は「食い違うときは、こちらの評価のほうが客観的で正確な洞察を出す」と書くが、これは著者の解釈
- Table 3 の注に「grid-view」（コマを格子に並べる）を工夫の 1 つとして挙げている（本文に説明は無い）

### VBench（CVPR 2024）

- 人の好みとの一致は、2 本の動画のどちらがよいかを人に選ばせ、**モデルごとの勝率**を VBench の勝率と比べて Spearman を出す（§4.2、Figure 5）。図の点は LaVie・ModelScope・VideoCrafter・CogVideo のモデルごと。値は例えば Motion Smoothness 0.998、Dynamic Degree 0.821、Color 0.607
- つまり**1 本の動画の採点が人と合うかではなく、モデルの順位が合うか**の数字

### SPOTLIGHT（2025-11）

- Veo 3・Seedance・LTX-2 で 200 のプロンプトから 600 本を作り、誤り 1,604 個を 6 種類（物理の違反、見た目の不整合、プロンプトの順守、出現と消失、体の姿勢 など。分類表 Table 1 の全項目は書き写していない）で時刻付きで注釈。人の検証で理由の 93%・区間の 99% を妥当と判定（§3）
- 結果（Table 2、閾値 0.7、S+P は類似度と精度を合わせた指標）: Qwen3-VL-8B-Instruct 0.148、Qwen3-VL-30B-A3B 0.137、**Gemini 2.5 Pro 0.250**、**人 0.508**。どのモデルも 2 fps で動画全体を入力
- 推論の工夫: 2 秒ずつに切り 4 fps で見る（sliding window）と Qwen3-VL-8B が 0.189、「理由を先に挙げてから位置を探す」2 段は 0.189、**誤りの種類ごとに 6 回別々に聞く（multi-agent）と 0.254**（精度 49.8%）で Gemini 2.5 Pro の zero-shot に並ぶ（§6.2、§7）
- 観察: プロンプトの順守と物理の誤りは長い区間に、出現・消失と体の姿勢の誤りは短い区間に出る（§4）

### Is Your Video Language Model a Reliable Judge?（ICLR 2025）

- 5 つの VLM（Video-LLaVA、LLaMA-VID、GPT-4o mini、InternVL2、GPT-4o）に、他の VLM の答えを採点させ、LLM の討論の結果と照らした
- 結論（§1）: 「弱い VLM に強いモデルを採点させると信頼できない」「**信頼できる評価役と信頼できない評価役を混ぜて集約しても、最終の評価の精度は必ずしも上がらない。信頼性の低い評価役はノイズを入れる**」「弱い評価役（Video-LLaVA）を微調整して理解力を上げるだけでは、評価役として信頼できるようにはならない」

## この wiki への含意

- **動きと時間の評価は、工夫しても人どうしより一段低い**: Video-Bench で時間の一貫性 0.40、動き 0.51。SPOTLIGHT で人の半分。Omni-Judge でも動画の質と音の同期が最も弱い（[[web-means-critic-omni-judge-audiojudge]]）。西尾の promo の「しょぼい」「展開が遅くてだるい」（[[exp-polis-magi-op]]、[[exp-sutra-hype-editions]]）は動き・間の評価で、ここに機械の批評役は届いていない
- **一致・内容の評価は比較的よい**: プロンプトとの一致（色・物・場面）は 0.7 台。西尾の talk の「中身が伝わるか」（[[exp-gyazo-resumption-video]] の「268群って何？」）に近いのはこちら側。ただし、ここでの「一致」は書かれたプロンプトの要素が画面にあるかで、見る人が理解できるかではない
- **聞き方を分けると効く**: chain-of-query・few-shot（Video-Bench）、誤りの種類ごとの別問い（SPOTLIGHT）。howseen の「動きの批評役とデザインの批評役を別のエージェントに」（[[web-opus-howseen-claude-motion-design]] §00）は、この方向と合う。1 つの評価役に 7 軸を一度に採点させる形（[[web-opus-hculap-skill-motion-graphic]]）より、1 軸 1 回のほうが文献の側の裏付けがある
- **評価役を増やして多数決にしない**: 弱い評価役を混ぜるとノイズになる（ICLR 2025）。Gemini と小さいローカルモデルの答えを平均するより、強い方を主にし、ローカルは外に出せない素材の下見に使うのが筋（このページの推論）
- **同じ設定でも 3 回に 1 回は点が変わる**（Video-Bench の 67%）。批評役の指摘は 1 回の結果で採否を決めず、2〜3 回回して共通する指摘を拾う
- **コマの格子（grid-view）**: Video-Bench が工夫に挙げている。西尾のコンタクトシート（[[exp-html-capture-pipeline]]）と同じ形を、評価役への入力として使っている例

## 着手の仕方（未検証。galleria で確かめる）

- **何ができるようになるか**: 批評役への問いを「1 回 1 種類」に分け、例を見せ、2〜3 回回す、という聞き方の型。道具ではなく問いの設計なので、Gemini（[[web-means-critic-gemini-video-understanding]]）・Claude のコマ（[[web-means-critic-openai-claude-vision-docs]]）・ローカルの Qwen3-VL（[[web-means-critic-qwen3-vl-open-vlms]]）のどれにも使える。型: talk・promo・embed
- **機械**: どこでも。費用は使う批評役による（Gemini なら **要: API キー・費用（西尾が決める）**）
- **成熟度**: 研究の手法。西尾の作品で試した例は無い
- **最小の手順**（問いの分け方は SPOTLIGHT の 6 種類にならって、このページで西尾の制作の過去の指摘から作った案）:
  1. 過去の人の指摘から誤りの種類を 4〜6 個決める: 「意味が分からない語」（Gyazo の「268群」）、「字幕と読み上げの食い違い」、「1 秒を超えて何も起きない所」（promo）、「画面の文字が小さい・重なる」、「飾りが中身より大きい」（[[exp-qualia-video]] の v3 の指摘）
  2. 種類ごとに別の問いで、時刻付きの JSON（`[{"start": "MM:SS", "end": "MM:SS", "reason": "..."}]`）を返させる
  3. 同じ問いを 3 回回し、2 回以上出た指摘だけを残す
  4. 西尾が既に直した版と直す前の版の両方に掛け、直す前の版でだけ指摘が出るかを見る
- **動いたと言える確かめ方**: 直す前の版（例: Gyazo v1、qualia journey v3）で、記録に残る人の指摘と同じ時刻・同じ種類の指摘が出る数を数える（再現率）。直した版で出る指摘の数（誤検出）も数える
- **所要（推測）**: 問いの作成 1 時間、2 作品の前後版で半日

## Open Questions

- Video-Bench の Spearman は 1 本ずつの採点の相関で、VBench はモデルの勝率の相関。両者の数字は直接比べられない
- Video-Bench の「人どうしと同程度」は、人どうしの一致自体が 0.52 と中程度であることに支えられている
- SPOTLIGHT の動画は数秒の実写風。数分の解説動画で「時刻付きで誤りを探す」精度は分からない
- 「1 回 1 種類」に分けると、全体の流れ（順序・展開の速さ）の評価は誰がするのか。分けた問いでは拾えない種類の指摘がありうる
