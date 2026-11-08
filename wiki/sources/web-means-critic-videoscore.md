---
type: source
summary: 生成動画を MLLM に採点させたときの人との一致を測った VideoScore（EMNLP 2024）と VideoScore2（2025-09）。プロンプトだけで頼んだ GPT-4o・Gemini 1.5 Pro の人との相関は Spearman 0.17〜0.23 と低く、人の採点で学習させた専用モデルは同じ分布の試験で 0.77。VideoScore2 では Claude Sonnet 4・Gemini 2.5 Pro・GPT-5 の 5 段階の点の完全一致は 26〜29%（1 点差まで含めて 68〜72%）。人どうしの一致も次元によって低い
video_types: [promo, any]
url: https://arxiv.org/abs/2406.15252
author: Xuan He, Dongfu Jiang, Wenhu Chen ほか（University of Waterloo / TIGER-Lab ほか）
published: 2024-06-21（VideoScore v1、v3 は 2024-10-14、EMNLP 2024）／2025-09-26（VideoScore2 v1）
retrieved: 2026-11-09
sources:
  - https://arxiv.org/abs/2406.15252 （VideoScore: Building Automatic Metrics to Simulate Fine-grained Human Feedback for Video Generation, v3）
  - https://arxiv.org/abs/2509.22799 （VideoScore2: Think before You Score in Generative Video Evaluation, v1）
  - https://huggingface.co/TIGER-Lab/VideoScore2 （モデルカード）
---

# VideoScore / VideoScore2: MLLM の動画採点と人の一致

## 何の文献か

- **VideoScore**（arXiv 2406.15252 v3、EMNLP 2024 に採択と表紙に記載。査読あり）。Waterloo 大の Wenhu Chen のグループ。生成動画の採点を人の評価に近づける専用モデルと、そのための人手の採点データ VideoFeedback（37.6K 本）を作った研究
- **VideoScore2**（arXiv 2509.22799 v1、プレプリント。本文の倫理の節は ICLR を指す）。同じグループ。3 次元・5 段階と、点の理由（思考の連鎖）を出すモデル
- どちらも PDF の本文を読んだ。対象は**テキストから生成した 1〜6 秒の短い動画**（実写風）。解説動画・モーショングラフィックスではない

## 書いてあること

### VideoScore（v1）

- 採点の 5 次元（Table 2）: Visual Quality（鮮明さ・解像度・明るさ・色）、Temporal Consistency（物体・人物の一貫性）、Dynamic Degree（動きの量）、Text-to-Video Alignment（プロンプトとの一致）、Factual Consistency（常識・事実との一致）。各 1〜4 点（4 は「実写のよう」）
- 人の採点: 20 人の専門の採点者（主に大学院生）。試行での人どうしの一致（Table 3、Krippendorff's α）は、試行 1（30 本）で 0.37〜0.54、試行 2（100 本）で **−0.11〜0.62**（Text-to-Video Alignment 0.21、Factual Consistency −0.11）。著者は「IAA は少数の試行例だけで計算したので全体を表さないかもしれない」と書く（付録 B）
- **プロンプトだけで頼んだ MLLM と人の相関**（VideoFeedback-test 760 本、Spearman ρ×100、Table 4）:

| 方法 | VQ | TC | DD | TVA | FC | 平均 |
|---|---|---|---|---|---|---|
| Gemini-1.5-Flash | 24.1 | 5.0 | 20.9 | 21.3 | 32.9 | 20.8 |
| Gemini-1.5-Pro | 35.2 | −17.2 | 18.2 | 26.7 | 21.6 | 16.9 |
| GPT-4o | 13.6 | 17.6 | 28.2 | 25.7 | 30.2 | 23.0 |
| VideoScore（学習済み） | 86.2 | 80.3 | 77.6 | 59.4 | 82.1 | 77.1 |

- 特徴量の指標（CLIP・SSIM・BRISQUE など）は平均 −20〜13。VideoScore は Mantis-Idefics2-8B（最大 128 コマ）を VideoFeedback で学習したもの。「同じ分布の試験」での数字で、別の評価（GenAI-Bench の好みの対で 78.5%、VBench の 5 側面で 72.1%）でも先行より高いと書く
- 動画は 8 fps にそろえた（高 fps と低 fps の時間の一貫性の差をならすため、§3.1）

### VideoScore2

- 3 次元（Visual Quality・Text Alignment・Physical/Common-sense Consistency）を 1〜5 点。20 以上の T2V モデルの動画 27,168 本（256×256〜1980×982、8〜30 fps、1〜6 秒）を 15 人が採点し短いコメントを付けた。人どうしの一致（試行 30 本×2、Table 3）は「1 点差以内の一致」80〜97%、α 0.78〜0.92
- 点の理由は Claude-4-Sonnet に、コマ・採点者のコメント（点は伏せる）・例を渡して書かせ、人の点と 2 点以上ずれたら作り直した（§3.3、4,951 本で 3 点以上ずれた本は 337 本）
- **プロンプトだけで頼んだ汎用モデル**（VideoScore-Bench-v2、2 fps でコマを入力、Table 5）:

| モデル | 完全一致（平均） | 1 点差まで（平均） | PLCC（平均） |
|---|---|---|---|
| Claude-Sonnet-4 | 28.93% | 71.74% | 0.229 |
| Gemini-2.5-Pro | 27.90% | 67.94% | 0.265 |
| GPT-5 | 26.24% | 69.01% | 0.180 |
| VideoScore2（Qwen2.5-VL-7B を SFT＋強化学習） | 44.35% | 90.78% | 0.604 |

- 次元別では、汎用モデルは**物理・常識の次元**が最も低い（完全一致 20〜24%）
- 分布の外の 4 つの評価（好みの対 2、点 2）の平均は VideoScore2 が 50.37 で最高だが、「各評価で常に一番ではない」と書く。旧版 VideoScore-v1.1 は分布の外の好みの対の評価で 16.79 まで落ちる（Table 6）。つまり**学習した分布の外では専用モデルも崩れうる**
- 推論は 2 fps が既定（4・8 fps の比較は付録）。点の理由（CoT）を付けて学習すると分布の内では上がり、分布の外では評価によって上下する（Table 7）
- モデル: Hugging Face `TIGER-Lab/VideoScore2`（Apache-2.0、Qwen2.5-VL-7B-Instruct ベース）。カードの推論例は `torch==2.6.0`・`transformers==4.53.2`・`qwen-vl-utils`、`fps=2.0`、`max_tokens=1024`

## この wiki への含意

- **「汎用の大きなモデルに採点させれば人に近い」は、動画では支持されない**: 2024 の GPT-4o・Gemini 1.5 で ρ 0.17〜0.23、2025 の GPT-5・Gemini 2.5 Pro・Claude Sonnet 4 で完全一致 3 割弱。点数を付けさせて「全項目 8 点以上まで回す」hculap の批評ループ（[[web-opus-hculap-skill-motion-graphic]]）や movez 型の 7 軸 10 点（[[web-opus-howseen-claude-motion-design]] §8）の点は、人の評価の代わりとしての裏付けが無い、と読むべき
- **点より「どこが・なぜ」**: 専用モデルでも分布の外で崩れる。西尾の作品（canvas で描く解説・ショーリール）は、これらの学習データ（実写風の T2V 1〜6 秒）の外にある。VideoScore2 を西尾の作品の採点に使っても、数字の意味は保証されない
- **人どうしも割れる**: VideoScore v1 の試行 2 では「プロンプトとの一致」「事実との一致」で α が 0.2 以下〜負。西尾の制作で評価が「西尾の一言」だった（[[exp-gyazo-resumption-video]]、[[exp-polis-magi-op]]）ことは、複数の人の平均より一人の判断者の基準に合わせる運用だった、と言える。機械の採点を合わせる相手も「西尾の一言」にするのが筋（このページの推論）
- **promo の生成素材の足切りには使える可能性**: [[exp-galleria-local-video-generation]] のように動画生成モデルの出力を複数本から選ぶ場面は、VideoScore2 の学習分布に近い（短い実写風）。Best-of-N の選別（論文 §4.5 は n=5 で使った）として試す価値はある

## 着手の仕方（未検証。galleria で確かめる）

- **何ができるようになるか**: 動画生成モデル（Wan・LTX など、[[exp-galleria-local-video-generation]]）で作った数秒の候補を、画質・プロンプトとの一致・物理の破綻の 3 つで採点し、理由の文つきで並べる。型: promo（生成素材を使う場合）。解説の画面（canvas・スライド）には学習分布の外なので使わない
- **機械**: galleria WSL。**GPU 要・VRAM の見込み 16〜20GB（根拠: Qwen2.5-VL-7B の BF16 の重み約 15GB に動画のコマの分を足した推測。16GB では足りない可能性があり、その場合は fps を下げるか 8 bit 読み込みを試す）**
- 入れるもの: カードのとおり `torch==2.6.0 torchvision==0.21.0`、`transformers==4.53.2`、`qwen-vl-utils`、`accelerate`、`opencv-python-headless`、`numpy==2.2.6`。**RTX 5080（Blackwell）は torch 2.6 の配布版の対象外の可能性がある（推測）**ので、torch は 2.7 以後の CUDA 12.8 版に替えて試すことになる。費用なし。モデル・データとも Apache-2.0（データ VideoFeedback の元プロンプトは VidProM で CC BY-NC 4.0 と v1 の付録 C）
- **成熟度**: VideoScore2 は 2025-09 公開。その後の更新は確かめていない（GitHub API が制限で読めなかった）
- **最小の手順**（WSL。カードの推論コードをそのまま `vs2_infer.py` として保存して使う。torch の差し替えは推測）:
  ```bash
  cd ~/video-tools-trial && uv venv vs2 && source vs2/bin/activate
  uv pip install torch torchvision --index-url https://download.pytorch.org/whl/cu128   # カードの 2.6.0 の代わり（推測）
  uv pip install transformers==4.53.2 qwen-vl-utils accelerate scipy opencv-python-headless numpy==2.2.6
  # カードの Python の例を vs2_infer.py に写し、video_path と prompt を自分の候補に替える
  python vs2_infer.py --video cand_01.mp4 --prompt "（生成に使ったプロンプト）"
  ```
- **動いたと言える確かめ方**: 3 次元の点（1〜5）と理由の文が出る。同じプロンプトの候補 5 本で、西尾が選ぶ 1 本と VideoScore2 の 1 位が一致するかを記録する（一致率をメモ）
- **所要（推測）**: 環境づくりで半日、比較で 1〜2 時間

## Open Questions

- VideoScore2 の汎用モデルの数字は「2 fps のコマ」を入れた条件。Gemini に動画ファイルを音声つきで丸ごと入れた場合の一致は測られていない
- 人どうしの一致: VideoScore v1 は低く、VideoScore2 は高い。採点者の訓練と「1 点差以内」という緩い指標の違いが大きい。どちらが西尾の判断に近いかは分からない
- 解説・モーショングラフィックス・字幕の多い画面で、同じ種類の人との一致を測った研究はこの 2 本には無い（教育動画は [[web-means-critic-edupanel-paper2video]]）
