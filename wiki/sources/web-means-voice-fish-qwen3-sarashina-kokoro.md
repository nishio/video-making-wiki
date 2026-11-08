---
type: source
summary: 2026-11-09 時点で日本語を読める公開 TTS モデルの公式 README・モデルカード・ライセンス本文の比較。Fish Audio Drama 3（48GB 以上）と S2-Pro（24GB 以上、研究用ライセンス）は galleria の 16GB に入らず、Fish のコミュニティライセンスは年商 50 万ドル未満だけ商用可。Qwen3-TTS（Apache-2.0、日本語含む 10 言語）、Sarashina2.2-TTS（日本語特化、非商用）、MioTTS（基盤モデルごとにライセンスが違う）、Kokoro の日本語（自己評価 C+ 以下）
video_types: [any]
url: https://github.com/QwenLM/Qwen3-TTS
author: Fish Audio（39 AI, Inc.）、Alibaba Qwen、SB Intuitions、Aratako、hexgrad
published: 2026-01-22（Qwen3-TTS）／2026-03（Fish S2）／2026-10-13（Fish Audio Community License 1.0、Drama 3）／2026-07-01（Sarashina2.2-TTS のモデルカード更新）
retrieved: 2026-11-09
sources:
  - https://github.com/fishaudio/fish-speech （README、LICENSE「FISH AUDIO COMMUNITY LICENSE AGREEMENT Version 1.0 — Last Updated: October 13, 2026」。最新リリース v3.0.0-beta 2026-10-13）
  - https://speech.fish.audio/install/ （GPU memory の表）
  - https://huggingface.co/fishaudio/drama-3 （license: other、最終更新 2026-10-29）、https://huggingface.co/fishaudio/s2-pro （license_name: fish-audio-research-license、2026-03-11）
  - https://github.com/QwenLM/Qwen3-TTS （README）、https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base （license: apache-2.0、2026-01-23）
  - https://huggingface.co/sbintuitions/sarashina2.2-tts （モデルカード、2026-07-01 更新。論文 arXiv 2606.25369 は未読）
  - https://huggingface.co/Aratako/MioTTS-2.6B （モデルカードの系列表、2026-02-10）
  - https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md （Kokoro の声の一覧と自己評価）
  - https://huggingface.co/Aratako/Irodori-TTS-500M-v3 （license: mit、2026-05-12。HF API で確認のみ）
  - https://github.com/FunAudioLLM/CosyVoice （GitHub API: QwenAudio/CosyVoice に移動、Apache-2.0、最終 push 2026-05-25）
  - 探索の手がかり: Web 検索（Gigazine の Qwen3-TTS 記事 https://gigazine.net/gsc_news/en/20260123-qwen3-tts-family-opensource ほか）。主張は上の一次資料で確かめた
---

# 日本語を読める公開 TTS（2026-11 時点）: Fish Audio・Qwen3-TTS・Sarashina2.2-TTS・MioTTS・Kokoro

## 何の文献か

- 各開発元の README・モデルカード・ライセンス本文（一次資料）。ベンチマークの数値はすべて開発元の自己申告。**日本語の品質を同じ条件で比べた第三者の評価は見つからなかった**（Web 検索でも、三者を直接比べた日本語の評価は無いと返った）
- 西尾が既に使った Irodori-TTS・AivisSpeech・VOICEVOX と、別ページの Style-Bert-VITS2（[[web-means-voice-style-bert-vits2]]）・GPT-SoVITS（[[web-means-voice-gpt-sovits]]）は除く

## 書いてあること

### 一覧（条文・モデルカードから）

| モデル | 日本語 | 大きさ・必要な GPU | ライセンス（商用） | 出典 |
|---|---|---|---|---|
| Fish Audio **Drama 3** | 多言語（HF の language に `ja`） | 35B-A3B。「at least 48 GB (FP8)」、NVIDIA のみ | Fish Audio Community License 1.0（下記） | README、install |
| Fish Audio **S2-Pro** | 約 100 言語 | 4B。「at least 24 GB」 | **Fish Audio Research License**（README「The S2-Pro weights remain under the Fish Audio Research License」） | 同 |
| **Qwen3-TTS** | 10 言語に日本語。既定の声に `Ono_Anna`（「Playful Japanese female voice」） | 0.6B / 1.7B。VRAM の数値は README に無い。FlashAttention 2 を「to reduce GPU memory usage」で推奨 | **Apache-2.0** | README、HF |
| **Sarashina2.2-TTS** | 日本語中心（＋英語） | 0.5B の LLM（sarashina2.2-0.5b-instruct）が土台 | **Sarashina Model NonCommercial License**。商用は問い合わせ。サンプル音声も研究目的のみ | HF |
| **MioTTS** | 日本語・英語 | 0.1B〜2.6B の 6 種 | **基盤モデルで違う**: 0.6B・1.7B は Apache-2.0（Qwen3 由来）、0.4B・1.2B・2.6B は LFM Open License v1.0、0.1B は Falcon-LLM License | HF の系列表 |
| **Kokoro-82M** | 日本語 5 声（女 4・男 1） | 82M | Apache-2.0。一部の声は学習データの CC BY 表記あり | VOICES.md |
| （参考）Irodori-TTS-500M-v3 | 日本語のみ | 500M | MIT | HF API |

### Fish Audio

- 機能（README）: Drama 3 は複数話者の場面、長尺、「Multi-turn director revision」（前のテイクに「もっと優しく、少し悲しく」と指示して作り直す）、「Infilling and precise editing」（一語だけ差し替えて前後の声色をつなぐ）、`[whisper]` `[angry]` `[laughing]` のようなインラインのタグ。S2-Pro は 10〜30 秒の参照で声を複製
- **GPU**（install のページ）: Drama 3 は「at least 48 GB (FP8)」「NVIDIA GPU only: no CPU, Apple MPS or AMD ROCm」。S2-Pro は「at least 24 GB」。System: Linux, WSL
- **Fish Audio Community License 1.0**（2026-10-13）の要点（条文から）:
  - 研究・非商用は無償（II）
  - 商用は「**Annual Revenue is less than USD 500,000**」の間だけ（III(a)）。Annual Revenue は「You and Your Affiliates」の全収入の合計。超えたら 30 日以内に通知、90 日の移行期間の後は別契約（III(b)）
  - 自分で作った音声ファイルだけを顧客に納める（代理店・スタジオとして）のは第三者の売上の条件にかからない（III(a)）
  - 「Hosted Service」（他人が自分の文・音声・声サンプルから音声を作れる API・サイト）は別契約。自分のコンテンツのナレーションを作るのは Hosted Service ではない（III(c)(1)）
  - 配布するときは「Built with Fish Audio」を関連するサイト・UI・ブログ・about・文書に「prominently display」（IV(a)）
  - 禁止（IV(b)）: 識別できる実在の人の声を**その人の事前の同意なしに**まねる、なりすまし、透かし・来歴の信号の除去、**出力で他の音声生成モデルを学習・蒸留・改良すること**
- 2026-03 の S2 の README は Seed-TTS Eval（中国語・英語）の WER などで他モデルより良いと書く。日本語の数値は載っていない

### Qwen3-TTS（README）

- 2026-01-22 公開。0.6B / 1.7B。種類: `CustomVoice`（9 つの既定の声＋指示文で話し方を変える）、`VoiceDesign`（1.7B、自然文で声を設計）、`Base`（「3-second rapid voice clone」、微調整の元）
- 「We recommend using each speaker's native language for the best quality」。日本語なら `Ono_Anna`
- 導入: `pip install -U qwen-tts`（Python 3.12 の新しい環境を推奨）、FlashAttention 2 は任意。複製は `ref_audio` と `ref_text` を渡す。`x_vector_only_mode=True` なら書き起こし不要だが質が落ちうる

### Sarashina2.2-TTS（モデルカード）

- 「Japanese-centric text-to-speech system built on a large language model」。特徴に「High Accuracy: Delivers strong pronunciation accuracy on Japanese text」、英語混じりの文（コードスイッチ）、数秒の参照でのゼロショット
- 学習データ: 「legitimately purchased audio sources, public speech archives, and data gathered in compliance with applicable domestic laws」「robots.txt directives and terms of service」に従ったと書く
- 論文の題は「Tackling **Kanji Polyphony** in Japanese Speech Generation via Data Scaling and Targeted Data Synthesis」（arXiv 2606.25369、未読）。漢字の多音（「空」をから／そら）を正面から扱っている
- 非商用ライセンス

### Kokoro（VOICES.md）

- 日本語は `lang_code='j'`（`misaki[ja]`）。5 声の「Overall Grade」は jf_alpha が C+、他は C〜C-。学習時間は「H hours」「MM minutes」「M minutes」と伏せ字。「Support for non-English languages may be absent or thin due to weak G2P and/or lack of training data」

### CosyVoice

- リポジトリは QwenAudio/CosyVoice に移った（Apache-2.0、最終 push 2026-05-25。GitHub API）。README は読んでいない

## この wiki への含意

- **galleria（RTX 5080 16GB）で動く候補は Qwen3-TTS・MioTTS・Kokoro・Irodori（既使用）**。Fish の Drama 3（48GB）と S2-Pro（24GB）は公式の数値で 16GB に入らない
- **商用とライセンス**: 西尾の発信を会社の業務として出すなら、Fish の「Annual Revenue … You and Your Affiliates」は会社の売上で判定されうる（条文からの推論。どの名義で使うかは西尾が決める）。Sarashina は非商用。条件が閉じているのは Qwen3-TTS（Apache-2.0）、MioTTS の 0.6B・1.7B（Apache-2.0）、Kokoro（Apache-2.0）、Irodori-TTS-500M-v3（MIT）。[[exp-galleria-tts-and-singing]] の「license で在庫が二分される」に、**売上の閾値**という三つ目の軸が加わった
- **読みの正しさ**: [[exp-qualia-video]]・[[exp-sutra-sync-subtitles]] の失敗は読み違い。Sarashina2.2-TTS は漢字の多音を主題にした唯一のモデルだが非商用。LLM 系の TTS（Qwen3-TTS・MioTTS・Fish）は**ユーザー辞書を持たない**（README に記述なし）ので、読みは台本の `narration` 欄で直すしかない。辞書で直せる VOICEVOX・AivisSpeech・Style-Bert-VITS2 とは運用が違う（[[web-means-voice-voicevox-aivisspeech-user-dictionary]]）
- **Fish Drama 3 の「一語だけ差し替え」**は、[[exp-qualia-h3-live2d-galleria]] の「正しいテイクが得られない短い区間だけ局所的に再生成する」を音声で行う機能。ただし 48GB 要で galleria では動かず、API（fish.audio）を使うなら有料（未調査）
- **出力を学習に回す禁止**: Fish（IV(b)）は出力で他の音声生成モデルを学習することを禁じる。[[exp-galleria-tts-and-singing]] の「自分の出力から参照を作る」（Irodori の出力を Irodori の参照に）は Irodori（MIT）なら問題ないが、Fish の出力を Irodori の参照の束に入れる運用は条文に触れうる
- 型: どれも talk・embed のナレーション。promo の演技（笑い・ささやき）には Fish のタグや Qwen3-TTS の指示文が効くと開発元は書く（未検証）

## 着手の仕方（未検証。galleria で確かめる）

- **何が表現できるようになるか**: 自然文の指示で話し方を変える日本語ナレーション（Qwen3-TTS CustomVoice）、3 秒参照の声の複製（Qwen3-TTS Base）。型は talk・embed、promo の語り
- **機械**: galleria WSL。入れるもの: `qwen-tts`（PyPI）と `Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice` の重み。費用 0、アカウント不要、Apache-2.0。GPU 要・VRAM の見込み: 0.6B なら数 GB（推測。公式の数値なし）
- **成熟度**: 2026-01-22 公開、HF の更新は 2026-01-23 が最後。リポジトリの更新状況は GitHub API の制限で確かめられなかった
- **最小の手順**（WSL。README のコマンドを元に、仮想環境は uv で推測。関数名・引数は README の例から）:
  ```bash
  mkdir -p ~/video-tools-trial/qwen3tts && cd ~/video-tools-trial/qwen3tts
  uv venv --python 3.12 && . .venv/bin/activate
  uv pip install -U qwen-tts
  uv pip install soundfile
  python - <<'EOF'
  # README の generate_custom_voice の例（中国語）を日本語に置き換えた。attn_implementation は省略（FlashAttention 2 を入れない場合。推測）
  import torch, soundfile as sf
  from qwen_tts import Qwen3TTSModel
  m = Qwen3TTSModel.from_pretrained("Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice", device_map="cuda:0", dtype=torch.bfloat16)
  print(m.get_supported_speakers(), m.get_supported_languages())
  wavs, sr = m.generate_custom_voice(text="空の吹き出しに、あとから文字を入れます。", language="Japanese", speaker="Ono_Anna")
  sf.write("ja_test.wav", wavs[0], sr)
  EOF
  ```
  （`language="Japanese"` の綴りは README の例 `"Chinese"` `"English"` からの推測。`get_supported_languages()` の出力で確かめる）。続けて [[exp-qualia-video]] の比較用原稿を同じ要領で焼く
- **動いたと言える確かめ方**: (1) `get_supported_languages()` に日本語が含まれる。(2) WAV が出る。(3) 比較用原稿の問題語（「空の吹き出し」「ホモ・サピエンス」「93.12秒」「H.264」）を正しく読むかを人が聴いて表にする。(4) AivisSpeech（まお）と RMS を揃えて聴き比べる
- **所要の見込み（推測）**: 1〜2 時間

## Open Questions

- 日本語の品質を同じ原稿で比べた第三者の評価が無い。手元で比べるしかない
- Qwen3-TTS・MioTTS の 16GB での実際の VRAM と速度
- Fish の「Built with Fish Audio」の表示義務が、出力の音声を入れた動画を公開するだけの場合にかかるか（IV(a) は「distribute or make available the Fish Audio Materials or a Derivative Work, or a product or service that uses any portion of them」。動画がこれに当たるかは条文から決まらない）
- Sarashina2.2-TTS の論文（漢字の多音の扱い）は未読
- MioTTS・Kokoro の日本語の読み（G2P）がどの辞書に基づくか、直せるか
