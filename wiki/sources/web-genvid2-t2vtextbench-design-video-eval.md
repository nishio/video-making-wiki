---
type: source
summary: 動画生成モデルが画面の文字とデザインのレイアウトをどこまで守れるかを測った 2 本。T2VTextBench（2025-05）は 10 モデルの画面文字を人が採点し、最高でも平均 0.37（0〜1）、アプリ・Web の UI の再現も最高 0.50。Evaluating Design Video Generation（ICML 2026 workshop）は Sora-2 と Veo-3.1 にデザインのレイアウトを動かさせ、要素が複数ある画面では文字の完全一致が最高 67% に落ち、指定外の要素まで動かすと報告している
video_types: [promo, talk, embed]
url: https://arxiv.org/abs/2505.04946
author: Xuyang Guo ほか 6 名（Guilin Univ. of Electronic Technology、Arizona、Wisconsin-Madison、UC Berkeley ほか）／Adrienne Deganutti・Dingning Cao・Jaejung Seol・Elad Hirsch・Purvanshi Mehta（Lica World）
published: 2025-05-08（T2VTextBench v1）／2026-05-15（Design Video Generation v1、v2 は 2026-06-08）
retrieved: 2026-11-09
sources:
  - https://arxiv.org/abs/2505.04946 （T2VTextBench: A Human Evaluation Benchmark for Textual Control in Video Generation Models, v1）
  - https://arxiv.org/abs/2605.16223 （Evaluating Design Video Generation: Metrics for Compositional Fidelity, v2, ICML 2026 Workshop on Human-AI Co-Creativity）
  - https://github.com/purvanshi/lica-bench
---

# 動画生成モデルの画面文字とレイアウトの忠実さ（T2VTextBench／Evaluating Design Video Generation）

## 何の文献か

2 本とも arXiv の論文で、本文（PDF）を読んだ。

- **T2VTextBench**（arXiv 2505.04946 v1、2025-05-08）: 査読の記載なし（プレプリント）。動画生成の「画面の文字」に絞った、人の採点によるベンチマーク。
- **Evaluating Design Video Generation: Metrics for Compositional Fidelity**（arXiv 2605.16223 v2、2026-06-08）: ICML 2026 の Human-AI Co-Creativity ワークショップ採択（arXiv のコメント欄による）。著者はデザインのデータセット LICA を作った会社 Lica World の所属。自社のデータセットとツールで測っている。

**測ったモデルが古い点に注意**。T2VTextBench は 2023〜2025 年初めのモデル（Sora 初代、Kling、Hailuo、Wan 2.1、LTX Video 2B など）。2 本目は Sora-2 と Veo-3.1 だけ。2026-11 時点の H3・LTX-2.5・Veo の新版などは測られていない。

## 書いてあること

### T2VTextBench（画面の文字）

- **条件**: 10 モデル、各モデルの最低の解像度（多くは 720p）、16:9、約 4 秒（3.1 節）。プロンプトは 6 分類 × 8 本＋追加の検証で計 73 本（3.2 節）。分類は「段階・記号の可視化」「アプリ・Web の UI の模擬」「日常のデジタルな場面」「映画・プレゼンの場面」「数学」「多言語（中国語）」
- **採点**: AI に一般的な知識のある学部・大学院の学生 3 名が独立に、0（Poor）／0.25（Fair、正しいのは 50% 未満）／0.5（Good、50〜80%）／1（Excellent、ほぼ正しい）の 4 段で採点し、平均した（3.3 節）
- **結果**（Table 2）: 平均の最高は Sora の **0.37**、次いで Pika 0.36、Hailuo 0.35、Wan 2.1 と SD Video 0.33、LTX Video 0.20、Kling 0.01。「すべてのモデルが平均 0.4 未満で、一貫して失敗している」と書いている（Observation 4.1）
- **アプリ・Web の UI の模擬**の列: Sora 0.50、Hailuo 0.47、Wan 2.1 0.44、LTX Video 0.19、Kling 0.00。例のプロンプトは「GPS の画面に "Turn right onto Oak Avenue in 200 m."」「QR を読むと "Open https://example.com/welcome"」「チャットの吹き出し」など
- 同じモデルでも分類によって大きく変わる（Sora は UI 0.50 だが映画の場面 0.28、Hailuo は映画 0.50 だが数学 0.25）。モデル間・分類間のばらつきが大きく「不安定」と書く（Observation 4.2）
- 文字を動かす指示（スライド、回転、色の変化、旗のように揺らす）では、最良の Pika 2.2 でも 0.38／0.42／0.58、ほとんどが 0.2〜0.45（4.2 節）
- 質的な観察: Kling は文字にならない記号だけ、Qingying は字形が重なる、Wan 2.1 は数字が歪む、SD Video は指定と違う式を描いた（4.1 節）

### Evaluating Design Video Generation（デザインのレイアウトを動かす）

- **課題**: 静止したデザインのレイアウトと、要素ごとの動きの指定（フェード、スライド、拡大、回転と、向き・時間）を与えて動画にさせる。「指定した要素だけが指定どおりに動き、動かさない領域は静止し、レイアウトは保たれる」ことが要件だと書く（1 節）
- **データ**: LICA のテンプレートから、要素 1 つだけの clip 86 本と、全レイアウト 136 本（要素の評価 894 件、1 レイアウトあたり平均 7.5 の動く要素）（5.1 節）
- **評価**: 人の採点を使わず、追跡器と分類器で自動に測る。正解の描画（GT）にも同じ測り方を当てて、測り方そのものの上限を出している（5.2 節）。**測り方の上限が低い項目が多い**（全レイアウトでの動きの種類の判定は GT でも 0.690）ので、数字は「予備的な診断の信号」と位置づけている（6 節）
- **文字の再現**（Table 7、2fps で抜き出したフレームの文字を OCR または LLM で読み、目標の文字列と照合）:
  - 要素 1 つの画面: Sora-2 の完全一致（Hard AR）は OCR で 0.769、LLM で 0.846。Veo-3.1 は 0.692 と 0.615。GT は OCR 0.769、LLM 1.000
  - **全レイアウト**: GT の LLM での完全一致 0.940 に対し、**Sora-2 は 0.671、Veo-3.1 は 0.416**（OCR では 0.586 と 0.389）
  - 「単独の文字の描画より、レイアウト全体の中で文字を保てるかの方が差が出る」と書く
- **動きの失敗**: 生成モデルは指定の動きを弱くしか出さない（under-animate）ことと、**静止しているはずの要素に余計な動きを足す**ことの 2 つで正解との差が説明できると書く（5.3 節）。導入では、指示を正しい領域に結び付けられない、一つの大きな動きを画面全体にかける、違う要素を動かす、指示に無い動きを作る、という初期の観察を挙げる（1 節）
- 2 つのモデルは失敗の型が違い、全体の知覚的なスコアではそれが見えないと書く

## この wiki への含意

- **promo（作品の紹介）**: 作品紹介の promo の中身は、作品の画面（UI）・名前・数値・URL。T2VTextBench の「アプリ・Web の UI の模擬」は最高 0.50（半分前後しか正しくない）、デザインのレイアウト全体の文字の完全一致は Sora-2 で 67%、Veo-3.1 で 42%。どちらの論文の測り方でも、**作品の実画面や正確な文字を生成に任せる根拠は出ていない**。実画面は収録かコードで描き、生成は文字のない雰囲気のカット（[[web-genvid2-vidmento-chi2026]] の「確立ショット」に当たるもの）に使う、という分け方と整合する
- **経験と一致**: [[exp-qualia-video]]・[[exp-local-scene-studio]] の「生成モデルに文字を描かせず、空の吹き出し・空の panel を生成してから Pillow で合成する」「看板・UI など文字を誘発する小道具は planner の段で拒否する」は、両論文の結果と同じ向き。[[experience-lessons-2026-11]] の「生成モデルに文字を描かせず、字幕・ロゴは後から合成する」は文献からも支持される（ただし文献は 2025〜2026 年前半のモデル）
- **経験と一致（動かさない所が動く）**: 2 本目の「静止すべき要素に余計な動きを足す」は、[[exp-qualia-video]] で Wan に文字・図・背景を通さず、人物の部分だけ I2V して ROI の外の画素がスライドと完全一致することを検査した設計と同じ問題を見ている。[[exp-galleria-local-video-generation]] の「人物部分だけを生成して固定のスライドに後合成する方法が成功した」もこれに当たる
- **ベンダーの主張との食い違い**: MiniMax H3 の公式の作例と LTX-2.5 のモデルカードは、画面の文字をモデルに描かせる方向を打ち出している（[[web-genvid2-wan-ltx-hunyuanvideo-minimax-h3]]）。それらの新しいモデルを測った独立の数字は見つけていない
- **talk / embed**: 図・数式・数値を見せる解説で生成に任せられない点は同じ（数学の分類は最高 0.31）。[[web-theoremexplainagent-code2video-visualedu]] のようにコードで描く方式が、正確さの面では残る

## Open Questions

- 2026 年後半のモデル（H3、LTX-2.5、Veo・Sora・Kling の新版）で、UI の模擬と文字の正確さがどこまで上がったか。同じ T2VTextBench のプロンプトで測り直した資料は見つけていない
- 日本語の画面文字を測ったベンチマークは見つけていない（T2VTextBench の多言語は中国語だけ）
- 2 本目は測り方の上限が低い項目が多く、著者自身が「予備的」と書く。数値の比較は文字の再現（OCR／LLM）の部分が一番頼れる
- 作品の実画面を参照画像として与える I2V（先頭フレームに実画面を置く）で、文字がどれだけ保たれるかは、どちらの論文も測っていない
