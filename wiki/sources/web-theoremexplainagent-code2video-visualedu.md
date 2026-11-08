---
type: source
summary: LLM のエージェントに Manim のコードを書かせて解説動画を作る研究 3 本（TheoremExplainAgent・ACL 2025、Code2Video・2025-10、VisualEDU・EMNLP 2025 Findings）。失敗の型は存在しない API の呼び出し、LaTeX のエラー、要素の重なり・位置ずれ・大きさの不揃い。対策はエラーを読んで直す再試行、6×6 の格子に配置させる、描いた動画を VLM に見せて配置を直させること。人間は VLM より短い重なりに敏感だと報告している。末尾に道具の比較表
video_types: [talk, embed]
url: https://arxiv.org/abs/2502.19400
author: Max Ku ほか（Waterloo / Votee AI / Vector Institute）、Yanzhe Chen・Kevin Qinghong Lin・Mike Zheng Shou（NUS Show Lab）、Hao Chen ほか（South China Normal Univ. ほか）
published: 2025-05-25（TheoremExplainAgent v2）／2025-10-01（Code2Video v1）／2025-11（VisualEDU, EMNLP 2025 Findings）
retrieved: 2026-11-09
sources:
  - https://arxiv.org/abs/2502.19400 （TheoremExplainAgent: Towards Video-based Multimodal Explanations for LLM Theorem Understanding, v2, ACL 2025 main）
  - https://arxiv.org/abs/2510.01174 （Code2Video: A Code-centric Paradigm for Educational Video Generation, v1）
  - https://aclanthology.org/2025.findings-emnlp.889 （VisualEDU: A Benchmark for Assessing Coding and Visual Comprehension through Educational Problem-Solving Video Generation）
  - https://www.remotion.dev/docs/ai/generate.md
  - https://github.com/remotion-dev/remotion/tree/main/packages/skills/skills
  - https://github.com/heygen-com/hyperframes/blob/main/README.md
---

# LLM のエージェントに解説動画のコードを書かせる研究（TheoremExplainAgent・Code2Video・VisualEDU）

## 何の文献か

3 本とも Manim Community Edition（[[web-manim]]）のコードを LLM に書かせて教育用の動画を作る研究。本文（PDF）を読んだ。

- **TheoremExplainAgent**（TEA）: arXiv 2502.19400 v2（2025-05-25）、ACL 2025 main。Waterloo 大の Wenhu Chen らのグループ。査読あり。
- **Code2Video**: arXiv 2510.01174 v1（2025-10-01）。NUS Show Lab。GitHub の README は NeurIPS 2025 の DL4C ワークショップ採択と書く（論文本体では未確認）。
- **VisualEDU**: EMNLP 2025 Findings（ACL Anthology 2025.findings-emnlp.889）。査読あり。

使ったモデルが古い（TEA は GPT-4o・Claude 3.5 Sonnet v1・Gemini 2.0 Flash・o3-mini、Code2Video は GPT-5・GPT-4.1・Claude Opus 4.1・Gemini 2.5 Pro、VisualEDU は Claude 3.7 Sonnet・GPT-4o など 9 個）。成功率の数字は今のモデルには当てはまらない可能性が高い。失敗の型と対策の構造のほうが持ち越せる。

## 書いてあること

### TheoremExplainAgent（ACL 2025）

- 構成: planner エージェントが場面の計画とナレーションを作り（vision・storyboard・技術的実装・アニメとナレーションの計画）、coding エージェントが Manim のスクリプトを書く。声は TTS。「生成したコードがエラーになったら、coding エージェントがエラーを読んで直した版を作る。最大 N＝5 回。超えたら失敗」（§3）。Manim のドキュメントを使う agentic RAG を足した版もある。
- ベンチマーク TheoremExplainBench: 数学・物理・化学・CS の 240 定理（易・中・難 各 80、OpenStax と LibreTexts から）。
- 結果: 「エージェント無し（agentless）では 20 秒より長い動画を作れなかった」が、エージェント方式で最長 10 分の動画を作れた。完全な動画を作れた割合は o3-mini（medium）が 93.8%、GPT-4o 55.0%、Gemini 2.0 Flash 14.6%、Claude 3.5 Sonnet v1 2.1%（Table 1）。再試行の効果（o3-mini、Table 3）: N＝0 では易 7%・中 0%・難 3%、N＝5 で 93%・91%・96%。
- RAG は「結果がまちまち」: 取ってきた例が一般的すぎたり無関係だったりして、誤った関数呼び出しを招いた。o3-mini は RAG 付きのほうが成功率が低い（82.1%）（§4、Table 1）。
- **失敗の型**（§4.3 Error Analysis、失敗した実行のログの分析）: (1) 最多は「Manim コードの幻覚」: 存在しない関数・モジュール・属性・画像ファイル、引数の型・数の誤り、(2) LaTeX のレンダリングエラー（数式の構文の誤り、特殊文字の扱い）、(3) 一般的なコードの誤り（import 漏れ、未定義の変数、NumPy の計算ミス）。
- **見た目の失敗**: 「生成したアニメはしばしば小さな配置の不正確さを示した。文字の位置ずれ、図形の重なり、物体の大きさの不揃い。目立たないことも多いが、中・難の問題ほど目立ち、気を散らしうる」（§1、§4.4）。化学（フラスコや原子）は単純な図形で表すので分かりにくくなる。
- 評価: Element Layout（要素がよく配置され、適切な大きさで、意図しない重なりが無いか）など 5 次元を、キーフレームを GPT-4o に見せて自動採点。人間の評価（12 人の STEM 学生、40 本）との相関は Element Layout で Spearman ρ＝0.42（p＝0.03）、Visual Relevance 0.72、Accuracy and Depth 0.14、Logical Flow 0.16、Visual Consistency 0.17（Table 4）。人手で作った Manim 動画 10 本の Element Layout は 0.73、エージェントは 0.57〜0.65（Table 2）。
- 注意点: 生成ループの中で直すのは**実行エラー**（エラーメッセージ）で、描いた絵を見て直す工程は無い。コード生成のプロンプトで「安全領域の余白と最小間隔の制約に照らして配置を検証し、違反しそうならコメントを残して人手の確認に回す」と指示しているだけ（付録 D.3）。
- 費用（Table 5、1 本あたり平均）: o3-mini で $1.16・1,680 秒、Claude 3.5 Sonnet v1＋RAG で $4.67・2,380 秒。実験全体で API に約 1,500 ドル。「この種のアニメのローカルレンダリングに GPU は要らない」（付録 D.4）。

### Code2Video（2025-10）

- 構成: Planner（アウトライン → storyboard、参照画像・アイコンを外部 DB に集めてキャッシュ）、Coder（節ごとに並列にコード生成、ScopeRefine で直す）、Critic（描いた動画を VLM に見せて配置を直す）（§4）。
- **ScopeRefine**: エラーの行 ±1 行だけを直す（最大 K1 回）→ 直らなければ講義の 1 行分のブロック（K2 回）→ 最後に節全体を作り直す。全コードとエラーログを毎回渡す方式は時間とトークンがかかる、と書く。並列化と合わせて、1 本あたり 15.4 分（並列も ScopeRefine も無しだと 149.8 分）（Table 3）。「生成・デバッグ・レンダリングを含めると 1 本の Manim 動画は 2 時間を超えうる」（§4.2）。
- **Visual Anchor Prompt**: 「LLM や VLM は空間の把握が弱く、"猫のアイコンの位置がおかしい" とは言えても、どちらへどれだけ動かすかを言えない」ので、画面を **6×6 の格子のアンカー点**に区切り、各セルを Manim の固定座標に対応させる。小さい要素は 1 点、大きい要素は複数のアンカーにまたがる領域に置かせる。「連続の配置問題を離散のアンカー割り当て問題に変える」（§4.3）。
- **Critic**: 描いた動画と節のコードを VLM（Gemini 2.5 Pro）に見せる。どの要素がどのアンカーを使い、どのコード行に対応するかの占有表を持ち、(1) セル内での要素の重なり、(2) 講義の文字がアニメに隠れる、(3) 使われていない大きな領域で偏る、の 3 種を見つけて直す（§4.3）。
- ベンチマーク MMMC: 3Blue1Brown の 117 本（平均 16.9 分）と、それを区切った 339 本（平均 3.35 分）、計 456 単位、13 分野。
- 評価 TeachQuiz: VLM に対象の概念を「unlearning」させてから動画を見せ、クイズの正答の回復を測る。**学習者は人間でなく VLM**。
- 結果（Table 1、VLM 採点）: Claude Opus 4.1 で、コードを直接書かせるだけの場合の平均 aesthetics 37.8・TeachQuiz 40.0 が、Code2Video では 87.9・86.0。3B1B の人手の動画は 99.7・97.1。動画生成モデル（Veo3 など）は 9.0 以下・2.5 以下。部品を外すと（Table 2、GPT-4.1）: Planner 無しで TeachQuiz −41.5、Visual Anchor 無しで −26.8、Critic 無しで −21.3。
- 人間の評価（Table 4）: 5 群、各群に中学生 6 人と大学生 2 人、20 の学習トピックで各 5 問。Code2Video（Claude Opus 4.1、平均 2.0 分）の Quiz は 80.3、3B1B（16.9 分）は 78.8 で、論文は「エージェントが作った動画がプロの手による教材を上回ることもある」と書く。ただし尺が 8 倍違い、各群 8 人の比較。完走意欲は 3B1B 36.2、Code2Video 64.0。
- **人間は重なりに敏感**: 「参加者は Code2Video の動画の配置（EL）に低い点を付けた。人間はごく短い遮蔽にもとても敏感で、VideoLLM はそうしたコマ単位の問題を見逃しやすい」（§5、Human Study）。人手の評価では Code2Video（Claude）の EL は 60.2 で、VLM 採点の 90.6 より大きく低い。

### VisualEDU（EMNLP 2025 Findings）

- 数学の問題（関数・平面幾何・解析幾何・立体幾何・確率・微積分、計 200 問、難易度 3 段階）を、step-by-step の解説動画として Manim で作らせるベンチマーク。メタプロンプト（問題の型に応じたテンプレート）、コードの修正、**視覚フィードバック**（描いた動画をキーフレームに切り、VLM が「重なりがあるか」「フォントの大きさが揃っているか」を判定し、`Text()`・`MathTex()` の文字量、`scale()`・`to_corner()` を直させる）を組み合わせる（§3.3、付録の prompt）。
- 結果: Claude 3.7 Sonnet と GPT-4o も難しい問題では 56% 未満。Claude 3.7 Sonnet はメタプロンプトで全体の正答率が 5%、視覚フィードバックでさらに 3% 上がった。他のモデルは両方合わせて 10〜20% 上がった（§6.4）。立体幾何のような道具を多く呼ぶ場面では最良の Claude 3.7 Sonnet でも 55%。難しい問題ほど「誤った引数、存在しないモジュールの呼び出し」が増える（§6.5）。

### 道具の側が出している対策（実務）

- [[web-remotion]]: 生成コードのコードフェンスを取り除く後処理が要る、context rot に注意、大きな system prompt より要求に応じた skill を選んで入れる（`/docs/ai/generate`）。Agent Skill は「まず Studio のプレビューを開き、人が見て舵を取れるようにする」「ユーザーの手での変更を上書きしない」。`render --frames=0,30,90` で指定コマを PNG にできる。
- HyperFrames（[[web-timesnap-timecut-hyperframes-webcodecs]]）: skill が「計画 → HTML → シーク可能なアニメ → lint → プレビュー → 描画」を教え、CLI に「コマを見る」がある。決定論の決まり（壁時計・seed 無し乱数・描画中の fetch の禁止）を道具の側で書いている。

## この wiki への含意

### 失敗の型と対策（3 本の論文と経験の対応）

| 失敗の型 | 文献の報告 | 文献の対策 | 西尾の経験 |
|---|---|---|---|
| 存在しない API・引数の誤り | TEA の最多の失敗。VisualEDU で難問ほど増える | エラーを読んで再試行（TEA: N＝0 で数%、N＝5 で 9 割）、行→ブロック→全体の順に直す（Code2Video） | Manim は使っていない。canvas の自前描画は API が小さく、この型の記録が無い（[[exp-html-capture-pipeline]]） |
| LaTeX のエラー | TEA の 2 番目の失敗 | （個別の対策は書かれていない） | 数式を使った記録が無い |
| 重なり・位置ずれ・大きさの不揃い・はみ出し | TEA「ほとんどの動画に小さな配置の問題」。VisualEDU の視覚フィードバックの対象 | 6×6 のアンカーに配置させる、描いた動画を VLM に見せる（Code2Video・VisualEDU） | [[exp-qualia-video]] は字幕を y＝890 以降、内容を y＝860 以内と領域を決めて重ねない。[[exp-html-capture-pipeline]] は静止画とコンタクトシートで見た |
| 視覚的な検証が無い | TEA の生成ループは実行エラーしか見ない | Critic（VLM）を入れると TeachQuiz −21.3 が戻る（Code2Video の ablation） | Claude Code が `capture.mjs stills` で秒を指定して撮り、西尾が見た（[[exp-html-capture-pipeline]]） |
| VLM の見逃し | 人間は短い遮蔽に敏感で VideoLLM は見逃す（Code2Video）。自動の Element Layout と人間の相関は ρ＝0.42（TEA） | ― | [[exp-qualia-video]]「機械 QA が全部通っても視聴品質は保証されない」 |

（表は 3 本の論文と exp ページからこのページでまとめたもの）

- **一致する点**: 「描いて見る」を工程に入れること。文献は VLM、経験は人間（西尾）とエージェントの静止画確認。文献でも VLM は人間ほど重なりに気づかないので、最後は人間が見る、という [[exp-qualia-video]]・[[exp-sutra-videos-overview]] の運用（本人の視聴の反応を正とする）は文献と食い違わない。
- **格子に置かせる**: Code2Video の 6×6 のアンカーは、[[exp-qualia-video]] の「字幕の帯と内容の帯を座標で分ける」をもっと細かくした形。エージェントに書かせる最初の指示に「画面の領域の割り当て」を入れる案になる。
- **型**: 3 本とも数学・理科の解説（talk・embed）。promo の見栄え（[[exp-polis-magi-op]] の「しょぼい」）を自動で評価・改善する研究は、この 3 本には無い。
- **「機械 QA が通っても」**: Code2Video の人間評価で、VLM 採点の EL 90.6 が人間では 60.2 になった。この差は [[exp-qualia-video]] の教訓と同じ方向。

### 道具の比較（このページでまとめたもの）

経験の 2 方式と、ほかのページで読んだ道具を同じ観点で並べる。速さは文献に条件付きの数字がほとんど無いので、構造だけ書く。

| 道具 | 1 コマの描き方 | 時間の扱い（決定論か） | 音 | レンダリング方式 | ライセンス |
|---|---|---|---|---|---|
| 西尾の HTML 方式（[[exp-html-capture-pipeline]]） | canvas に `renderFrame(f)` | フレーム番号の純関数＋時刻表。seed 固定の乱数 | numpy で合成、ffmpeg で後から重ねる | headless Chrome 1 タブで `toDataURL` → image2pipe。粒子系 1 分に約 10 分、文字だけ 47 秒を約 38 秒（実測） | 自前（puppeteer-core は Apache-2.0） |
| 西尾の Pillow 方式（[[exp-qualia-video]]） | Pillow で静止スライドの変種 | 音声区間ごとの静止画。決定論的 | TTS の区間 WAV | PyAV で H.264 に結合 | 自前 |
| [[web-remotion]] | React コンポーネント（DOM・CSS・SVG） | `useCurrentFrame()` の関数であることを要求 | `<Audio>`・`<Video>` を描画に混ぜる | 複数タブのスクリーンショット → FFmpeg。Lambda で分散。ブラウザ内は WebCodecs | 個人・3 人以下・非営利は無料、それ以外は Company License |
| [[web-motion-canvas]] | canvas のシーングラフ（独自 JSX） | generator で上から書く。`useRandom` は再現可能 | 1 本の音声＋エディタの time events | エディタで再生して書き出し（画像連番 or FFmpeg） | MIT |
| [[web-revideo]] | Motion Canvas と同じ | 同じ | `<Audio/>` で同期 | `renderVideo()` で headless、並列化 | MIT |
| [[web-manim]] | Python の Mobject（Cairo / OpenGL） | `play()` を上から実行、play 単位のキャッシュ | 本体は簡素。manim-voiceover で TTS と単語単位の同期 | play ごとに部分動画 → 連結 | MIT |
| HyperFrames（[[web-timesnap-timecut-hyperframes-webcodecs]]） | HTML＋CSS＋GSAP など | 整数フレーム→時刻で全アニメをシーク | `<audio>` を描画時に混ぜる | headless Chrome の beginFrame → FFmpeg。Docker・Lambda | Apache-2.0 |
| timesnap / timecut（同） | 任意の Web ページ | 時間関数を仮想時間に差し替え（CSS アニメは不可） | なし | スクリーンショット or canvas capture → ffmpeg | BSD-3-Clause |
| After Effects / Lottie / Rive（[[web-after-effects-lottie-rive]]） | 手でキーフレーム＋エクスプレッション | エクスプレッションは時刻の式、乱数は時刻の関数 | AE は可。Lottie は音声非対応 | AE のレンダラー。Lottie・`.riv` は各ランタイム | AE は商用。lottie-web・Rive ランタイムは MIT |

## Open Questions

- 3 本とも、今の世代のモデル（例えば Claude Code で使っている Opus 系）での失敗率は分からない。TEA の Claude 3.5 Sonnet v1 の 2.1% は、エージェントの実装との相性も含む数字で、モデルの能力だけの値ではない。
- Code2Video の「人手の教材を上回る」は、尺 2.0 分と 16.9 分、各群 8 人の比較。TeachQuiz の主指標は VLM が学習者で、人間の学びの測度ではない。
- VLM の配置検査は人間より甘い（Code2Video）。どこまでを VLM に任せ、どこから人が見るかの線は、文献からは引けない。
- 西尾の制作で、エージェントが静止画を「自分で見て」直した記録と、西尾が見て直させた記録の割合は、exp- ページから区別できていない。
