---
type: source
summary: Alibaba の Qwen の「Omni」系（映像・音声・テキストを一緒に入れられるモデル）の、API（Model Studio の qwen3.8-omni-flash ほか、2026-11 時点）と公開モデル（Qwen3-Omni-30B-A3B、Qwen2.5-Omni-7B/3B）。動画ファイルの音声トラックごと理解させられる。公開モデルは Qwen3-Omni が BF16 で 15 秒の動画に約 79GB と 16GB には載らず、16GB に載る公式の見込みがあるのは Qwen2.5-Omni-7B の AWQ 版（15 秒で 11.77GB）だけ
video_types: [promo, talk, embed]
url: https://www.alibabacloud.com/help/en/model-studio/qwen-omni
author: Alibaba Cloud（Model Studio ドキュメント）／Qwen チーム（Hugging Face のモデルカード）
published: 2026-10-28（Qwen-Omni の API ページの Last Updated）／2025-09-22（Qwen3-Omni のカード更新）／2025-04-30・2025-05-15（Qwen2.5-Omni と AWQ 版のカード更新）
retrieved: 2026-11-09
sources:
  - https://www.alibabacloud.com/help/en/model-studio/qwen-omni （Last Updated: Oct 28, 2026）
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing （Last Updated: Nov 07, 2026）
  - https://huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Instruct （README.md）
  - https://huggingface.co/Qwen/Qwen2.5-Omni-7B （README.md、LICENSE）
  - https://huggingface.co/Qwen/Qwen2.5-Omni-7B-AWQ （README.md）
---

# Qwen の Omni 系: 音声トラックごと動画を理解させる（API と公開モデル）

## 何の文献か

- Alibaba Cloud Model Studio（国際版）の公式ドキュメントと価格ページ。2026-11-09 に取得。「2026-11-09 時点の公式ページによる」
- Qwen チームの Hugging Face のモデルカード（README）。メモリの表は公式が「理論上の最小値」と書いているもので、実測ではない
- 読んでいないもの: Model Studio の「Billing and rate limits」（動画のトークン換算・fps）、Qwen3-Omni・Qwen2.5-Omni の技術報告の本文、Model Studio の利用規約・データの扱い

## 書いてあること

### API（Model Studio）

| モデル | 入力 | 動画の長さの上限 | 地域 | 価格（シンガポール、100 万トークン） |
|---|---|---|---|---|
| `qwen3.8-omni-flash` | テキスト・画像・音声・動画（出力はテキストのみ） | 2 時間、1 リクエスト 64 ファイル、URL で 2GB | 北京・シンガポール・香港・東京・フランクフルト・バージニア | 入力 $0.15、出力 $0.47 |
| `qwen3.5-omni-plus` / `-flash` | テキスト＋画像・音声・動画の任意の組み合わせ。音声の出力あり | 1 時間（音声は 3 時間） | 北京・シンガポール | plus: テキスト・画像・動画の入力 $1.4、音声の入力 $11 ほか |
| `qwen3-omni-flash` | テキスト＋**どれか 1 つ**のモダリティ | 150 秒 | 北京・シンガポール | 入力（画像・動画）$0.78 ほか |

- 公式の推奨: 「音声・動画の理解、議事録、字幕の生成、テキストの Q&A には **Qwen3.8-Omni-Flash** を。思考・ツール呼び出し・ウェブ検索に対応。話して返す必要があるときは Qwen3.5-Omni を」。コンテキスト 1M。音声入力は 113 の言語・方言（日本語を含む）
- 動画の渡し方は 2 通り: 「**動画ファイル（動画内の音声に対応）**」か「画像の列」。「動画ファイルの映像と音声の情報は別々に課金される」
- `qwen3.8-omni-flash` はステレオと 4 チャンネルの FOA（空間音声）を `use_multichannel` で受け、空間の情報を保つと書く
- 思考は既定で有効。思考のトークンは出力として課金
- 「音声・動画の説明の品質は Qwen3.5-Omni のほうが強く、Qwen3-Omni-Flash は相対的に弱い」と書く
- 無料枠: Qwen3.5-Omni と Qwen3-Omni はシンガポールだけで、qwen3.5-omni-plus に 100 万トークン（90 日）
- OpenAI 互換（`base_url` を地域ごとの workspace の endpoint にし、`DASHSCOPE_API_KEY`）。動画は `{"type": "video_url", "video_url": {"url": ...}}`

### 公開モデル（Hugging Face）

- **Qwen3-Omni-30B-A3B**（Instruct・Thinking・Captioner、カード更新 2025-09-22）: MoE（総 30B・活性 3B）。「36 の音声・動画ベンチマークのうち 22 で SOTA」と書く。音声入力 19 言語（日本語を含む）。**Captioner**は「任意の音声に、詳しく幻覚の少ないキャプションを付ける」音声専用の派生
  - 「最小 GPU メモリ」（transformers・BF16・FlashAttention 2、理論値）: Instruct は **15 秒の動画で 78.85GB、30 秒 88.52GB、60 秒 107.74GB、120 秒 144.81GB**。Thinking（talker なし）は 15 秒 68.74GB。「`model.disable_talker()` で音声出力を止めると約 10GB 節約」
  - vLLM を推す（当時はフォーク・ソースからのビルド）。`vllm serve` は thinker のみで「`use_audio_in_video` は使えない。映像と音声を別々に渡して処理すること」
  - ライセンス: カードのメタデータは `license: other`, `license_name: apache-2.0`（LICENSE ファイルは取得できなかった）
- **Qwen2.5-Omni-7B / 3B**（カード更新 2025-04-30）: ライセンス Apache-2.0（LICENSE ファイルを確認）
  - 「最小 GPU メモリ」（理論値。「実際は少なくとも 1.2 倍」と書く）: 7B BF16 で 15 秒 31.11GB・30 秒 41.85GB・60 秒 60.19GB、3B BF16 で 15 秒 18.38GB
  - **AWQ 版**（Qwen2.5-Omni-7B-AWQ、2025-05-15）: thinker の重みを 4 bit にし、モジュールごとに読み込んで終わったら CPU に退避する。「RTX 3080・4080・5070 など GPU メモリの少ない機械向け」。**15 秒 11.77GB、30 秒 17.84GB、60 秒 30.31GB**。VideoMME 72.4 → 72.0、LibriSpeech test-other WER 3.4 → 3.91。「量子化と CPU 退避のため推論は少し遅い」
  - 動画の音声を使うかは `use_audio_in_video=True`。補助の `qwen-omni-utils[decord]`（Linux 以外は decord が入らないことがあり torchvision に落ちる）と ffmpeg が要る

## この wiki への含意

- **「映像と音を一緒に見せる」ができる、Gemini 以外の選択肢**: API の `qwen3.8-omni-flash` は動画ファイルを音声トラックごと受け、日本語の音声にも対応すると書く。Gemini（[[web-means-critic-gemini-video-understanding]]）との違いは、公式が「議事録・字幕の生成」を推す音声寄りの設計であること、地域に東京があること。批評に使った場合の精度は誰も測っていない（Omni-Judge は公開版の Qwen3-Omni で測った。[[web-means-critic-omni-judge-audiojudge]]）
- **galleria の 16GB では「丸ごと」はほぼ無理**: Qwen3-Omni は 15 秒でも 70GB 台。16GB に載る公式の見込みがあるのは Qwen2.5-Omni-7B-AWQ の **15 秒（11.77GB）だけ**で、30 秒（17.84GB）は超える。公式は「実際は 1.2 倍以上」とも書くので 15 秒でも際どい。西尾の promo（15 秒のショーリール、[[exp-nishio-showreel]]）なら 1 本、talk（1〜6 分、[[exp-qualia-video]]）は 15 秒ずつに切って見せることになる。切ると「通しで見る」の意味が薄れる
- **音だけの批評役として Captioner**: Qwen3-Omni-30B-A3B-Captioner は音声専用の詳しいキャプション。BGM の雰囲気・効果音の有無・声の調子を言葉にさせる用途が考えられる。ただし 30B-A3B で、16GB に載る記述は無い。[[exp-galleria-tts-and-singing]] の「機械の数値は耳の代わりにならない」は、キャプションでも同じだと思っておくべき
- 声の権利（[[exp-galleria-tts-and-singing]]）: Omni 系は音声を出力もできるが、ここでは批評（入力して文章を返す）だけに使う

## 着手の仕方（未検証。galleria で確かめる）

### A. API（qwen3.8-omni-flash）

- **何ができるようになるか**: 書き出した mp4 を音声つきで丸ごと見せ、要旨・分かりにくい箇所・字幕と音声の食い違いを聞く。Gemini と同じ問いを投げて答えを比べる（批評役を 2 つにする）。型: talk・embed・promo
- **機械**: どこでも（API）。galleria WSL から `openai` の Python SDK で（OpenAI 互換）
- **要: API キー・費用（西尾が決める）**。Alibaba Cloud のアカウント、地域の選択（東京あり）。データの扱いの規約は未読（入れてよい素材かは西尾が決める）
- **最小の手順**（公式の Chat Completions の例を元に。ファイルは公開 URL か base64（10MB 未満）で渡す。ローカルの mp4 を base64 で渡す書き方は推測）:
  ```bash
  cd ~/video-tools-trial/critic
  export DASHSCOPE_API_KEY=...  DASHSCOPE_BASE_URL=https://{WorkspaceId}.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1
  ffmpeg -i in.mp4 -vf scale=-2:540 -c:v libx264 -crf 30 -c:a aac -b:a 64k small.mp4   # 10MB 未満に
  uv run --with openai python - <<'EOF'
  import base64, os
  from openai import OpenAI
  c = OpenAI(api_key=os.environ["DASHSCOPE_API_KEY"], base_url=os.environ["DASHSCOPE_BASE_URL"])
  b = base64.b64encode(open("small.mp4","rb").read()).decode()
  r = c.chat.completions.create(model="qwen3.8-omni-flash", stream=True, messages=[{"role":"user","content":[
      {"type":"video_url","video_url":{"url":f"data:video/mp4;base64,{b}"}},
      {"type":"text","text":"この動画が伝えたいことを日本語の一文で。分かりにくい箇所を時刻付きで最大 5 つ。"}]}])
  for ch in r:
      if ch.choices and ch.choices[0].delta.content: print(ch.choices[0].delta.content, end="")
  EOF
  ```
- **動いたと言える確かめ方**: 一文の要旨と時刻付きの指摘が返る。最後のチャンクの `usage.prompt_tokens_details` に `audio_tokens` があれば、音声トラックも読まれている
- **所要（推測）**: キーがあれば 1 時間

### B. 公開モデル（Qwen2.5-Omni-7B-AWQ、galleria のローカル）

- **何ができるようになるか**: 未公開の素材を外に出さずに、15 秒以内のクリップを音声つきで批評させる。型: promo（15 秒）、talk は区間ごと
- **機械**: galleria WSL。**GPU 要・VRAM の見込み 12〜14GB（根拠: 公式の AWQ の表で 15 秒 11.77GB、「実際は 1.2 倍以上」の注記からの推測）**
- 入れるもの: 公式 README の手順は `transformers` の特定のブランチ（`v4.51.3-Qwen2.5-Omni-preview`）、`autoawq==0.2.9`、`accelerate`、`qwen-omni-utils[decord]`、repo の `low-VRAM-mode/low_VRAM_demo_awq.py`。RTX 50 系（Blackwell）で、この古い固定版の torch・autoawq が動くかは不明（推測: 動かない可能性がある）
- ライセンス: Apache-2.0。商用可
- **成熟度**: AWQ 版のカードは 2025-05-15 から更新なし。新しい Omni の公開は Qwen3-Omni（2025-09）以後見当たらない（2026-11-09 に Hugging Face の Qwen の一覧で確認）
- **最小の手順**（公式 README のまま。uv の venv に入れる所は推測）:
  ```bash
  cd ~/video-tools-trial && uv venv omni && source omni/bin/activate
  uv pip install git+https://github.com/huggingface/transformers@v4.51.3-Qwen2.5-Omni-preview accelerate autoawq==0.2.9 "qwen-omni-utils[decord]"
  git clone https://github.com/QwenLM/Qwen2.5-Omni.git && cd Qwen2.5-Omni/low-VRAM-mode
  CUDA_VISIBLE_DEVICES=0 python3 low_VRAM_demo_awq.py      # まずデモがそのまま動くか
  ```
  動いたら、デモの入力を自分の 15 秒の mp4 と上の問いに差し替える（`USE_AUDIO_IN_VIDEO = True`）
- **動いたと言える確かめ方**: デモが文章を返す。`nvidia-smi` のピークが 16GB 未満。自分の 15 秒の mp4 で、BGM や声に触れた文が返る（音声トラックが読まれている印）
- **所要（推測）**: 環境が合えば半日、RTX 50 系との相性で詰まれば 1 日以上

## Open Questions

- API の動画の fps・トークン換算（Billing and rate limits のページ）は未読。映像と音声の課金が別とだけ分かっている
- Model Studio のデータの扱い（学習への利用・保存期間）は未読
- Qwen3-Omni を 16GB に載せる量子化版（コミュニティ製）があるかは調べていない。公式の量子化は Qwen2.5-Omni の AWQ・GPTQ だけ
- Qwen2.5-Omni の音声入力の言語に日本語が入るかは、カードに明記が無い（Qwen3-Omni は日本語を明記）
