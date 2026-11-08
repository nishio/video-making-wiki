---
type: source
summary: 日本語の音声に「既知の台本」を合わせる、または日本語に強い書き起こしをするための公開モデル（2026-11-09 時点）。Qwen3-ForcedAligner-0.6B（Apache-2.0、2026-01-28 公開）は 11 言語・5 分までの音声に語・字の時刻を付け、Qwen の自己報告で日本語の平均ずれ 42.2ms（MFA で付けたラベルとの比較）。Montreal Forced Aligner は japanese_mfa（GMM-HMM、CC BY 4.0、v3.0.0）を conda で入れ、sudachipy で語に分ける。ReazonSpeech は 3.5 万時間の日本語で学んだ ASR と wav2vec2（Apache-2.0。コーパスは情報解析目的に限る）、kotoba-whisper は Whisper large-v3 を日本語に蒸留した ASR（Apache-2.0、6.3 倍速い）
video_types: [talk, embed, promo]
url: https://huggingface.co/Qwen/Qwen3-ForcedAligner-0.6B
author: Qwen（Alibaba）／Michael McAuliffe, Morgan Sonderegger（Montreal Forced Aligner）／Reazon Holdings（ReazonSpeech、Yuta Sasaki）／Kotoba Technologies（kotoba-whisper）
published: 2026-01-28（Qwen3-ForcedAligner-0.6B）／2024-02-08（japanese_mfa v3.0.0 の学習日）／2024-11-29（japanese-wav2vec2-large-rs35kh）／2024-10-23（kotoba-whisper の最終更新）
retrieved: 2026-11-09
sources:
  - https://huggingface.co/Qwen/Qwen3-ForcedAligner-0.6B（README。Qwen3-ASR と共通のカード）
  - https://pypi.org/project/qwen-asr/（0.0.6、2026-01-30）
  - https://mfa-models.readthedocs.io/en/latest/acoustic/Japanese/Japanese%20MFA%20acoustic%20model%20v3_0_0.html
  - https://montreal-forced-aligner.readthedocs.io/en/latest/installation.html
  - https://montreal-forced-aligner.readthedocs.io/en/latest/first_steps/alignment_example.html
  - https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner/releases.atom（最新の Version 3.4.3、2026-10-08）
  - https://research.reazon.jp/projects/ReazonSpeech/（ライセンスの表）
  - https://research.reazon.jp/projects/ReazonSpeech/howto.html
  - https://huggingface.co/reazon-research/japanese-wav2vec2-large-rs35kh
  - https://huggingface.co/kotoba-tech/kotoba-whisper-v2.2、https://huggingface.co/kotoba-tech/kotoba-whisper-v2.0、https://huggingface.co/kotoba-tech/kotoba-whisper-v2.0-faster
---

# Qwen3-ForcedAligner・Montreal Forced Aligner・ReazonSpeech・kotoba-whisper（日本語の整列と書き起こし）

## 何の文献か

- どれも公開モデル・道具の公式のカード・文書。精度の数値は**各開発元の自己報告**（独立の比較は見つけていない）
- 役割で分けると:
  - **既知の台本を音声に合わせる（強制アライメント）**: Qwen3-ForcedAligner-0.6B、Montreal Forced Aligner（MFA）、WhisperX の整列部（[[web-check-subs-whisperx-stable-ts-faster-whisper]]）、stable-ts の `align()`（同）
  - **日本語の書き起こし（ASR）**: ReazonSpeech（NeMo / k2 / ESPnet）、kotoba-whisper、Qwen3-ASR
  - **整列の部品**: ReazonSpeech の wav2vec2（CTC。WhisperX の `--align_model` に差し替えうる）

## 書いてあること

### Qwen3-ForcedAligner-0.6B（2026-01-28 公開、Apache-2.0）

- カードの説明: 「supports timestamp prediction for arbitrary units within up to 5 minutes of speech in 11 languages. Evaluations show its timestamp accuracy surpasses E2E based forced-alignment models.」対応言語に **Japanese** を含む。方式は NAR（非自己回帰）、音声の種類は「Speech」（歌は ASR 側だけが対応）
- 使い方（カードの例）: `pip install -U qwen-asr`（0.0.6、2026-01-30）→ `Qwen3ForcedAligner.from_pretrained("Qwen/Qwen3-ForcedAligner-0.6B", dtype=torch.bfloat16, device_map="cuda:0")` → `model.align(audio=..., text=..., language="Chinese")`。結果は単位ごとの `text, start_time, end_time`。「can align text–speech pairs and return word or character level timestamps」
- Qwen3-ASR（0.6B・1.7B）に `forced_aligner="Qwen/Qwen3-ForcedAligner-0.6B"` を渡すと、書き起こしに時刻が付く。ASR は 30 言語（日本語を含む）、「Speech, Singing Voice, Songs with BGM」
- 精度（カードの「Forced Alignment Benchmarks (AAS ms ↓)」。AAS は平均の時刻のずれ、と読める。基準のラベルは MFA で付けたもの）:

| 条件 | 言語 | NFA | WhisperX | Qwen3-ForcedAligner |
|---|---|---|---|---|
| MFA-Labeled Raw | Japanese | — | — | **42.2** |
| 同 | English | 107.5 | 92.1 | 37.5 |
| 同 | 平均 | 129.8 | 133.2 | 42.9 |
| MFA-Labeled Concat-300s（5 分につないだ音声） | Japanese | — | — | **81.3** |
| 同 | 平均 | 246.7 | 2708.4 | 52.9 |

  - 日本語は他の道具の数値が無く（「—」）、比べられていない。正解が MFA の出力なので、「MFA にどれだけ近いか」の数値でもある。人手のラベルの表（Human-Labeled）もあるが、日本語の行は読み取れなかった
- 推論の道具: transformers と vLLM の両方。flash-attn は任意。`Qwen/Qwen3-ForcedAligner-0.6B-hf`（transformers 本体に入る版）もある

### Montreal Forced Aligner（MFA）の日本語

- `japanese_mfa` 音響モデル v3.0.0: GMM-HMM（MFCC）、学習日 2024-02-08、**CC BY 4.0**、学習は 5 つのコーパス計 150 時間超（カードの表の合計。読み上げ音声が中心）。「it was trained on read speech in low-noise environments」
- カード自身の注意: 「MFA does not use state-of-the-art ASR models for forced alignment.」
- 入れ方: **conda が前提**（「conda create -n aligner -c conda-forge montreal-forced-aligner -y」）。日本語は追加で「conda install -c conda-forge spacy sudachipy sudachidict-core」。モデルは `mfa model download acoustic japanese_mfa`、`mfa model download dictionary japanese_mfa`
- 実行: `mfa align <コーパスのディレクトリ> japanese_mfa japanese_mfa <出力> --clean`。コーパスは音声と同名の文字起こし（.lab/.txt）を並べる形。出力は TextGrid（語と音素の区間）と `alignment_analysis.csv`（`phone_duration_deviation` の大きい順に怪しい発話）
- 日本語の落とし穴（チュートリアルの例）: 「税、その他全て込みだと、１泊いくらですか。」を sudachipy が分けたとき、「１泊」が辞書に無く、前後の語が誤った区間に伸びた。直し方は辞書に読みを足すか「一泊」に書き換える。辞書に無い語は sudachipy のカタカナを G2P に渡して実行時に発音を作れる
- 最新のリリースは Version 3.4.3（GitHub のリリースノート、2026-10-08）

### ReazonSpeech（Reazon Holdings）

- ライセンスの表（公式ページ）: 音声認識モデル（reazonspeech-nemo-v2、-k2-v2、-espnet-v2）と音声処理ライブラリは **Apache-2.0**。日本語音声コーパスは **CDLA-Sharing-1.0（ただし利用目的は著作権法 30 条の 4 に定める情報解析に限る）**
- 使い方（howto）: `git clone https://github.com/reazon-research/ReazonSpeech` → `pip install ReazonSpeech/pkg/nemo-asr` → `from reazonspeech.nemo.asr import load_model, transcribe, audio_from_path`、`load_model(device='cuda')`（実行時に 2.3GB のモデルを取得）。k2 版は 1.5GB、ESPnet 版は 1.6GB
- `japanese-wav2vec2-large-rs35kh`（2024-11、Apache-2.0、319M）: ReazonSpeech v2.0 で微調整した CTC。カードの CER は平均 16.25%（JSUT 11.00%、Common Voice 18.23%、TEDxJP 19.53%）。同じ表で WhisperX の既定の `jonatasgrosman/wav2vec2-large-xlsr-53-japanese` は平均 31.82%（TEDxJP 50.63%）、長い音声（JSUT-BOOK）で 46.20% 対 30.98%。**整列に使う音素・字の認識は ReazonSpeech の方が強い**と読める（整列の精度そのものの比較ではない）

### kotoba-whisper（Kotoba Technologies、Apache-2.0）

- Whisper large-v3 を教師に、ReazonSpeech で蒸留した日本語の ASR。「Kotoba-Whisper is 6.3x faster than large-v3, while retaining as low error rate as the large-v3」（v2.0 のカード）
- v2.2 はパイプラインに話者分離（pyannote。利用条件への同意が要る）と句読点の付与（punctuators）を足した版。出力の例は区間ごとの `timestamp: [開始, 終了]`
- `kotoba-whisper-v2.0-faster`（faster-whisper 用、カードのライセンス表記は MIT）、whisper.cpp 用の重みもある。どれも最終更新は 2024-10

## この wiki への含意

- **台本がある西尾の作りでは「整列」が主で、ASR は従**。ASR の文字は読経で崩れ（[[exp-sutra-voicevox-singing]]）、講演では固有名詞・数字を誤った（[[exp-democracy-river-video]]）。Qwen3-ForcedAligner か stable-ts の `align()` に台本を渡し、文字は台本、時刻だけ機械、にする
- Qwen3-ForcedAligner は**日本語を名指しで対応し、日本語の数値（42.2ms）を出している唯一の公開の整列モデル**（読んだ範囲）。ただし基準が MFA のラベルで、話し言葉・歌・読経での精度は分からない
- MFA は conda と sudachipy が要り、辞書に無い語（数字・英字・仏教語）で崩れやすい。真言・経文の読み（「おんばさら」など）は辞書に無いので、**読みをかなで渡す前処理**が要る（推測）。西尾の「表示の読みと発音を分ける」（[[exp-sutra-sync-subtitles]]）の speech 欄をそのまま整列の入力に使える
- ReazonSpeech のコーパスの「情報解析に限る」はコーパスの条件で、学習済みモデル（Apache-2.0）を使って字幕を作ることはこの条件の外と読める（推測。モデルのカードはコーパスの条件に触れていない）
- 型: talk・embed の字幕づくり。promo で歌の字幕を付けるなら、Qwen3-ASR が歌声に対応と書くので試す価値がある（Polis の英語の歌、[[exp-polis-magi-op]]）。ただし整列モデルの音声の種類は「Speech」だけ

## 着手の仕方（未検証。galleria で確かめる）

- **何ができるようになるか**: 日本語の録音＋台本から、語・字単位の時刻（字幕・カラオケ風の強調・同期解説の光る位置）を作る。VOICEVOX 以外の声（録音、外部 TTS）でも同期解説の形（[[exp-sutra-sync-subtitles]]）が作れる。効く型: talk、embed
- **機械**: galleria WSL（GPU）。MFA は CPU で動く
- **入れるもの**: `qwen-asr` 0.0.6（＋PyTorch の CUDA 12.8 版、推測）。MFA は Miniforge（conda）＋ `montreal-forced-aligner` 3.4.x ＋ sudachipy。費用 0、アカウント不要。モデルの重みは初回に Hugging Face から取得（0.6B なので数 GB 未満と推測）
- **VRAM の見込み**: Qwen3-ForcedAligner-0.6B を bfloat16 で 2〜4GB（推測。0.6B パラメータから）
- **成熟度**: qwen-asr は 2026-01 の 0.0.x で若い。MFA は 2026-10 まで更新

### 最小の手順

```bash
# galleria WSL: Qwen3-ForcedAligner
mkdir -p ~/video-tools-trial/qwen-align && cd ~/video-tools-trial/qwen-align
uv venv --python 3.12 && . .venv/bin/activate
uv pip install torch --index-url https://download.pytorch.org/whl/cu128   # RTX 50 系向け（推測）
uv pip install -U qwen-asr==0.0.6
cat > align_ja.py <<'EOF'
import sys, json, torch
from qwen_asr import Qwen3ForcedAligner
m = Qwen3ForcedAligner.from_pretrained("Qwen/Qwen3-ForcedAligner-0.6B", dtype=torch.bfloat16, device_map="cuda:0")
text = open(sys.argv[2], encoding="utf-8").read().replace("\n", "")
res = m.align(audio=sys.argv[1], text=text, language="Japanese")
out = [{"text": u.text, "start": u.start_time, "end": u.end_time} for u in res[0]]
json.dump(out, open(sys.argv[3], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(out), out[:5])
EOF
python3 align_ja.py narration.wav script.txt units.json
```

- `language="Japanese"` の綴りはカードの例（`"Chinese"`、`"English"`）からの推測。5 分を超える音声は区切って渡す
- 台本の行（字幕 1 枚）への戻し方: `units.json` の字を台本の行の字と先頭から照合し、各行の最初の字の `start` と最後の字の `end` を取る（同期解説の「モーラ列と意味区分の照合」と同じ手。[[exp-sutra-sync-subtitles]]）。そこから SRT を書く（[[web-check-subs-ffmpeg-libass-youtube-caption-files]]）

```bash
# MFA（比較用。CPU）
# Miniforge を入れてから（要: conda。入れるかは西尾が決める）
conda create -n aligner -c conda-forge montreal-forced-aligner -y && conda activate aligner
conda install -c conda-forge spacy sudachipy sudachidict-core -y
mfa model download acoustic japanese_mfa && mfa model download dictionary japanese_mfa
mkdir -p corpus && cp narration.wav corpus/n1.wav && cp script.txt corpus/n1.lab
mfa align corpus japanese_mfa japanese_mfa aligned --clean
```

### 動いたと言える確かめ方

- `units.json` の `text` をつなぐと台本と同じ文字列（空白・句読点を除いて）になり、`start` が単調に増え、最後の `end` が音声の長さ以内
- **正解のある素材で誤差を測る**: VOICEVOX で台本を読ませた音声は、`audio_query` の各モーラの長さから正解の時刻が出る。Qwen3-ForcedAligner・stable-ts・WhisperX・MFA の 4 つで、行の開始時刻の誤差の中央値と最大値を並べる（どれが西尾の素材で一番合うかが分かる）
- MFA は `aligned/n1.TextGrid` ができ、`alignment_analysis.csv` に `spn`（不明な語）が出ていないこと

### 所要の見込み（推測）

- Qwen3-ForcedAligner: 環境づくり 30〜60 分、1 本数秒。4 つの比較を含めて半日
- MFA: conda の導入から 1〜2 時間

## Open Questions

- Qwen3-ForcedAligner の日本語の精度（42.2ms）は MFA のラベルとの比較で、読み上げ音声か話し言葉かも書いていない。歌・読経・早口（アゲアゲ版は 1 モーラ約 85ms。[[web-check-ja-speech-rate-mora]]）で使えるか
- 漢字の台本と、かなの台本のどちらを渡す方が合うか（読みの曖昧な漢字で崩れるか）
- ReazonSpeech の wav2vec2 を WhisperX の `--align_model` に差し替えて動くか（語彙の作りが WhisperX の前提と合うか）
- qwen-asr の 0.0.x の API が今後変わるか
