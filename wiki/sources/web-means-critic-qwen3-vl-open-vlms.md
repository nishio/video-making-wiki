---
type: source
summary: galleria（RTX 5080 16GB）で動かせる公開の映像理解モデルのモデルカード（2026-11-09 時点）。Qwen3-VL-8B は GGUF の Q8_0（8.71GB）＋ビジョン部（1.16GB）で llama.cpp から画像（コマ・コンタクトシート）を読ませられる。動画をそのまま入れるなら transformers / vLLM で FP8 版（10.6GB）。新しい Qwen3.8-27B・Qwen3.6 は画像と動画を受けるが 16GB には量子化なしで載らない。InternVL3.5・VideoLLaMA3 も Apache-2.0。どれも音声は入らない
video_types: [promo, talk, embed]
url: https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct
author: Qwen チーム（Alibaba）／OpenGVLab（Shanghai AI Lab）／DAMO-NLP-SG（Alibaba DAMO）
published: 2025-10-15（Qwen3-VL-8B のカード更新）／2026-11-07（Qwen3.8-27B・Qwen3.6 のカード更新）／2025-09-28（InternVL3.5 Flash 版のカード更新）／2025-01（VideoLLaMA3、arXiv 2501.13106。カードのニュース欄は「2024.01.22 公開」と書くが論文番号と合わない）
retrieved: 2026-11-09
sources:
  - https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct （README.md）
  - https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct-GGUF （README.md、ファイル一覧）
  - https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct-FP8 （ファイル一覧）
  - https://huggingface.co/Qwen/Qwen3.8-27B （README.md）
  - https://huggingface.co/Qwen/Qwen3.6-35B-A3B （README.md）
  - https://huggingface.co/OpenGVLab/InternVL3_5-8B （README.md）
  - https://huggingface.co/DAMO-NLP-SG/VideoLLaMA3-7B （README.md）
  - https://huggingface.co/Qwen/Qwen2-Audio-7B-Instruct （README.md）
  - https://github.com/ggml-org/llama.cpp/releases （最新 b12110、2026-11-04）
  - https://arxiv.org/abs/2511.18102 （SPOTLIGHT、Qwen3-VL と Gemini 2.5 Pro の比較の数字だけ）
---

# galleria で動かせる公開の映像理解モデル（Qwen3-VL ほか）

## 何の文献か

Hugging Face のモデルカード（README）とファイル一覧、llama.cpp のリリースページ。2026-11-09 に取得。性能の数字はモデルの作り手の自己申告で、批評役としての精度を測ったものではない。批評に近い課題で第三者が測った数字は SPOTLIGHT（[[web-means-critic-video-bench-spotlight]]）から 1 つだけ引く。**どのモデルもダウンロード・実行していない**（CyEC2 では動かさない決まり）。

## 書いてあること

### Qwen3-VL（2025-10、Apache-2.0）

- 2B・4B・8B・32B・30B-A3B・235B-A22B、それぞれ Instruct と Thinking、FP8 版と GGUF 版がある（GGUF は 2025-11-01、FP8 の一部は 2025-11-26 更新）
- カードの主張: 「ネイティブ 256K コンテキスト（1M まで拡張）。本や何時間もの動画を全部覚えて秒単位で索引できる」「Text–Timestamp Alignment: タイムスタンプに基づく出来事の位置づけ」「画像・動画から Draw.io / HTML / CSS / JS を生成」
- 使い方: transformers は「最新をソースから入れよ（4.57.0 は未リリース）」と書く（カードの書かれた 2025-10 時点の注記）。マルチ画像・動画では flash_attention_2 を推す
- **GGUF（llama.cpp・Ollama 向け）**: 8B の LLM 部は F16 16.39GB・Q8_0 8.71GB・Q4_K_M 5.03GB、ビジョン部（`mmproj`）は F16 1.16GB・Q8_0 0.75GB。CLI は `llama-mtmd-cli -m ...Q8_0.gguf --mmproj ...F16.gguf --image test.jpeg`、サーバーは `llama-server`（`/v1/chat/completions`）。カードの例は**画像**だけ
- FP8 版（Qwen3-VL-8B-Instruct-FP8）のファイル合計は 10.61GB

### 新しい Qwen（2026-11-07 にカード更新）

- **Qwen3.8-27B**（dense 27B、Apache-2.0）: 「画像と動画を理解するネイティブの視覚言語モデル」「STEM の図・文書から 1 時間規模の動画まで」。動画は vLLM で既定 `fps=2`（`mm_processor_kwargs` で変更可、vLLM のみ）。長い動画では `video_preprocessor_config.json` の `longest_edge` を上げるよう書く（既定は保守的）
- **Qwen3.6-35B-A3B / 27B**（Apache-2.0）: 「Qwen3.6 の最初の公開版」。カードの主眼はコーディング
- **Qwen3.8-Flash-Next**（125B・活性 6B）: ライセンスは `qwen-community-1.0`（Apache ではない。条文は未読）
- 27B の重みは BF16 で約 54GB（パラメータ数からの計算）。16GB に入れるには 4 bit 以下が要る

### その他

- **InternVL3.5**（OpenGVLab、Flash 版のカード更新 2025-09-28、Apache-2.0）: 1B〜241B と「Flash」版。カードの動画の例は decord で**一様に 32 区間**のコマを取って渡す（`num_segments=32`）
- **VideoLLaMA3-7B**（DAMO-NLP-SG、Apache-2.0、Qwen2.5-7B ベース）: 動画専用の系統。カードに VRAM の記述なし
- **Qwen2-Audio-7B-Instruct**（Apache-2.0）: 音声のみ。「音声の分析: 音声とテキストの指示を与えて分析」。動画は入らない。音声の判定の実測は [[web-means-critic-omni-judge-audiojudge]]
- **llama.cpp**: 最新 b12110（2026-11-04）。Windows 用のビルド済みバイナリが releases にある（asset の名前は今回確かめていない）

### 第三者の数字（SPOTLIGHT、arXiv 2511.18102、§6・Table 2）

AI 生成動画 600 本（Veo 3・Seedance・LTX-2）の誤り 1,604 個を、時刻付きで見つけさせた課題。Qwen3-VL-8B-Instruct（2 fps、動画を丸ごと）の S+P は 0.148、Gemini 2.5 Pro は 0.250、人は 0.508。**誤りの種類ごとに 6 回別々に聞く**と Qwen3-VL-8B で 0.254（Gemini 2.5 Pro の zero-shot と同程度）、2 秒ずつに切って 4 fps で見せると 0.189。

## この wiki への含意

- **galleria で今日すぐ使える形は「コマを画像で見せる」**: llama.cpp ＋ Qwen3-VL-8B の Q8_0（約 10GB）は 16GB に収まり、Windows のビルド済みバイナリで動く見込み。これは Claude にコンタクトシートを見せるのと同じ形（[[web-means-critic-openai-claude-vision-docs]]）を、外に出さずにローカルでやるもの。未公開の作品・第三者の写る素材を API に出せないときの逃げ道になる
- **動画として入れる（時間の情報も使う）のは transformers / vLLM の道**: FP8 版 10.6GB は載る見込みだが、動画のトークンでさらに増える（量は未確認）。WSL の CUDA と RTX 50 系での vLLM の対応は、今回確かめていない
- **ローカルの小さいモデルは「聞き方」で補う**: SPOTLIGHT では、誤りの種類ごとに分けて聞くだけで 8B が Gemini 2.5 Pro の zero-shot に並んだ。西尾の批評でいえば「要旨を一文で」「字幕と読み上げの食い違い」「画面の文字の読みにくさ」「1 秒を超えて止まる所」を 1 回ずつ別に聞く形になる（このページの応用案、未検証）。それでも人の半分
- **音は入らない**: どのモデルも映像だけ。読み・声・BGM は別に（文字起こしで台本と照合、[[exp-galleria-tts-and-singing]] の運用）
- 型: talk（[[exp-qualia-video]] のような静止の多い画面）はコマの画像で十分に近い。promo（[[exp-polis-magi-op]]）の動きの良し悪しは、コマの画像ではほぼ見えない

## 着手の仕方（未検証。galleria で確かめる）

- **何ができるようになるか**: 外部に出さずに、ローカルの視覚モデルにコマ（またはコンタクトシート）から要旨・分かりにくさ・字幕の読みにくさを指摘させる。型: talk・embed（静止の多い画面）
- **機械**: galleria Windows（llama.cpp のビルド済み CUDA 版）。**GPU 要・VRAM の見込み 10〜12GB（根拠: 公式の GGUF のファイルサイズ 8.71＋1.16GB に、コンテキストの分を足した推測）**
- 入れるもの: llama.cpp b12110 以後の Windows 用 CUDA 版、`Qwen3VL-8B-Instruct-Q8_0.gguf` と `mmproj-Qwen3VL-8B-Instruct-F16.gguf`（約 10GB のダウンロード）。費用なし、アカウント不要（Hugging Face からの取得はアカウントなしで可能な見込み）。ライセンス Apache-2.0
- **成熟度**: Qwen3-VL は 2025-10 公開・2026-04 に関連モデル（Embedding・Reranker）の追加あり。llama.cpp は数日おきにリリース
- **最小の手順**（Windows の PowerShell。llama.cpp のコマンドは GGUF のカードのとおり、問いの文とシートの作り方は提案）:
  ```powershell
  cd $HOME\video-tools-trial\vlm
  # コマを作る（Windows 側の ffmpeg）。talk は 3 秒に 1 枚を 1280 幅で、字幕が読める大きさに
  ffmpeg -i in.mp4 -vf "fps=1/3,scale=1280:-1,tile=3x3" -frames:v 1 sheet_01.png
  .\llama-mtmd-cli.exe -m Qwen3VL-8B-Instruct-Q8_0.gguf --mmproj mmproj-Qwen3VL-8B-Instruct-F16.gguf `
    --image sheet_01.png -ngl 99 `
    -p "これは解説動画のコマを時間順に左上から並べたものです。この動画が伝えたいことを日本語の一文で言ってください。字幕が読みにくいコマがあれば番号で挙げてください。"
  ```
  （`-ngl 99` は全層を GPU に置く llama.cpp の一般的な指定。カードの例には無い）
- **動いたと言える確かめ方**: 日本語の一文が返る。`nvidia-smi` で VRAM が 16GB 未満。同じシートを Claude にも見せ、要旨の一文を並べて記録する（一致・不一致の数）。字幕の文字を正しく読み返せるかを 1 枚で確かめる（日本語 OCR の力の確認）
- **所要（推測）**: ダウンロード込みで 1〜2 時間

## Open Questions

- Qwen3-VL-8B の日本語の画面文字の読み取りの精度は、カードに数字が無い
- llama.cpp の Qwen3-VL で動画（コマの列ではなく時間付きの入力）を扱えるかは確かめていない
- Qwen3.8-27B を 16GB に載せる量子化版（公式・コミュニティ）があるかは調べていない
- SPOTLIGHT の数字は AI 生成の実写風の短い動画での誤り探しで、西尾のコードで描く解説動画の批評とは課題が違う
