---
type: source
summary: Whisper 系で日本語の音声に語・字単位の時刻を付ける公開の道具 3 つ。faster-whisper（MIT、1.2.1＝2025-10-31）は word_timestamps を出す土台。WhisperX（BSD-2-Clause、3.8.6＝2026-05-25）は書き起こしの後に wav2vec2 の音素モデルで強制アライメントし、日本語は既定で jonatasgrosman/wav2vec2-large-xlsr-53-japanese を使う（字単位、空白なし言語として扱う）。stable-ts（MIT、2.19.1＝2025-08-16）は「既知の台本」を音声に合わせる align() と、SRT / VTT / ASS の書き出しを持つ。台本があるなら stable-ts の align か WhisperX の align に台本を渡すのが筋で、書き起こしの文字は使わない
video_types: [talk, embed, promo]
url: https://github.com/m-bain/whisperX
author: Max Bain ほか（WhisperX）／jianfch（stable-ts）／SYSTRAN（faster-whisper）
published: 2026-05-25（whisperx 3.8.6）／2025-08-16（stable-ts 2.19.1）／2025-10-31（faster-whisper 1.2.1）
retrieved: 2026-11-09
sources:
  - https://github.com/m-bain/whisperX（README.md、LICENSE、whisperx/alignment.py を読んだ）
  - https://pypi.org/project/whisperx/（版と日付）
  - https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-japanese（ライセンス）
  - https://github.com/jianfch/stable-ts（README.md の Alignment・Output・regroup の節）
  - https://pypi.org/project/stable-ts/
  - https://github.com/SYSTRAN/faster-whisper（README.md）
  - https://pypi.org/project/faster-whisper/
---

# WhisperX・stable-ts・faster-whisper（日本語の語・字の時刻）

## 何の文献か

- 3 つとも GitHub の公開ソフトの README とソース（公式ドキュメント）。版・日付は 2026-11-09 時点の PyPI による
- WhisperX は論文（Bain ら、INTERSPEECH 2023）があるが、本ページは README とコードを読んだ範囲。精度の数値は README・論文の主張で、日本語では測られていない

| | 版（PyPI） | ライセンス | Python | 何をするか |
|---|---|---|---|---|
| faster-whisper | 1.2.1（2025-10-31） | MIT | ≥3.9 | Whisper を CTranslate2 で速く回す。`word_timestamps=True` で語の時刻 |
| WhisperX | 3.8.6（2026-05-25。3.8.7rc1 が 2026-06-26） | BSD-2-Clause | 3.10〜3.13 | faster-whisper で書き起こし → VAD → wav2vec2 で強制アライメント → 任意で話者分離 |
| stable-ts | 2.19.1（2025-08-16） | MIT | ≥3.8 | Whisper の時刻を安定させる、既知の文を音声に合わせる `align()`、SRT/VTT/ASS/TSV/JSON の書き出し |

## 書いてあること

### faster-whisper

- 「up to 4 times faster than openai/whisper for the same accuracy while using less memory」。large-v2 を GPU（RTX 3070 Ti 8GB、CUDA 12.4）で int8・beam 5 なら VRAM 2,926MB、`batch_size=8` で 4,500MB（README の表）
- GPU には CUDA 12 用の cuBLAS と **cuDNN 9** が要る。「The latest versions of ctranslate2 only support CUDA 12 and cuDNN 9」。pip で `nvidia-cublas-cu12 nvidia-cudnn-cu12==9.*` を入れて `LD_LIBRARY_PATH` を通す方法を書く
- モデルは `large-v3`、`turbo`、distil-large-v3 などを名前で指定。kotoba-whisper の faster-whisper 用の重み（`kotoba-tech/kotoba-whisper-v2.0-faster`）も使える（[[web-check-subs-qwen3-forcedaligner-mfa-reazonspeech]]）

### WhisperX

- 「Whisper ... the corresponding timestamps are at the utterance-level, not per word, and can be inaccurate by several seconds.」それを、音素を認識する wav2vec2 の CTC モデルで強制アライメントして語の時刻にする（README）
- faster-whisper を裏に使い「requires <8GB gpu memory for large-v2 with beam_size=5」。GPU で使うなら「install the CUDA toolkit 12.8 before WhisperX」
- 日本語: `alignment.py` の `DEFAULT_ALIGN_MODELS_HF` で `"ja": "jonatasgrosman/wav2vec2-large-xlsr-53-japanese"`（Apache-2.0）。`LANGUAGES_WITHOUT_SPACES = ["ja", "zh"]` で、空白で語に分けず**字の単位**で合わせる。モデルの語彙に無い字（数字・記号・別の文字体系）はワイルドカードとして扱う（コードのコメント「unknown char (digit, symbol, foreign script) — use wildcard」）
- README の限界: 「Transcript words which do not contain characters in the alignment models dictionary e.g. "2014." or "£13.60" cannot be aligned and therefore are not given a timing.」（コードでは今はワイルドカードで扱う版がある。README とコードで食い違う）
- `--align_model` で別のモデルに差し替えられる。日本語なら ReazonSpeech の wav2vec2（`reazon-research/japanese-wav2vec2-large-rs35kh`）が候補（CER の比較は [[web-check-subs-qwen3-forcedaligner-mfa-reazonspeech]]）
- **既知の台本で合わせる**: Python の `whisperx.align(transcript, model, metadata, audio, device)` の `transcript` は `{"text","start","end"}` の区間の並び（docstring「Align phoneme recognition predictions to known transcription」）。書き起こしを使わず、台本の文と大まかな区間を渡せる（区間をどう作るかは使う側の仕事）
- 話者分離は pyannote の `speaker-diarization-community-1`（CC-BY-4.0、Hugging Face のトークンと利用条件への同意が要る）。字幕だけなら使わない
- 出力: `--highlight_words True` で SRT に語の強調。CLI の出力形式の一覧は README には無い（`whisperx --help` で確かめる）
- 2026 年の新機能: 「Context-Aware Batching」（前の文脈を渡して句読点・固有名詞を改善）。arXiv 2608.31170 は読んでいない

### stable-ts

- **Alignment**（README 原文）: 「Audio can be aligned/synced with plain text on word-level.」`model.align('audio.mp3', text, language='en')`。CLI は `stable-ts audio.mp3 --align text.txt --language en`
- `align()` の主な引数: `original_split`（「Whether to preserve the original segment groupings. Segments are split by line breaks if text is plain-text」＝**台本の改行を字幕の区切りとして保つ**）、`failure_threshold`（長さ 0 の語の割合がこれを超えたら中止）、`nonspeech_skip`（既定 5 秒以上の無音を飛ばす）、`vad`（Silero VAD）、`fast_mode`
- `align_words()`: 既存の区間の中だけで語の時刻を合わせる速い版
- 書き出し: `result.to_srt_vtt('audio.srt')`、`.vtt`、`result.to_ass('audio.ass')`。`segment_level` と `word_level` を両方 True にすると、語ごとに強調する字幕（カラオケ風）になる
- 区切り直し（regroup）: 既定の規則は `sp=.* /。/?/？` で句点「。」でも切る。日本語の句点・疑問符を扱う規則が既定に入っている
- `load_faster_whisper()`、`load_hf_whisper()`（Hugging Face の Whisper。kotoba-whisper を名前で読める、推測）でも同じ機能。「Any ASR」の例で、他の音声認識の結果にも後処理を掛けられる

## この wiki への含意

- **西尾の動画の多くは TTS（VOICEVOX・AivisSpeech）でナレーションを作るので、時刻は合成器が持っている**。VOICEVOX は 93.75fps のフレームで音素の長さを返し、同期解説はそれで光る位置を決めた（[[exp-sutra-sync-subtitles]]）。強制アライメントが要るのは、(1) 講演の録画や自分の声の録音、(2) 時刻を返さない外部の TTS・歌声（MiniMax、SoulX-Singer の一部）、(3) 公開後に YouTube 用の字幕ファイルを作る、とき
- **台本がある場合は書き起こしの文字を使わない**: 読経の音声認識は反復崩壊・幻覚を起こした（[[exp-sutra-voicevox-singing]]）、講演の自動字幕は年号・単位・固有名詞を間違えた（[[exp-democracy-river-video]]、[[exp-forest-misc-video-notes]]）。stable-ts の `align()` に台本を渡せば、文字は台本のまま時刻だけ付く。shortmovie-draft-generator の「タイムスタンプは字幕データを正とし、LLM には触らせない」（[[exp-shortmovie-draft-generator]]）の逆向きで、「文字は台本を正とし、ASR には時刻だけ出させる」
- stable-ts の `original_split=True` は、台本の 1 行＝字幕 1 枚という作りに合う。改行は BudouX で文節の切れ目に置いてから渡す（[[web-check-subs-budoux]]）
- 型: talk（ナレーション付きの解説）、embed（流しっぱなしで字幕に頼る）。promo の歌の字幕（Polis の英語の歌、[[exp-polis-magi-op]]）は、歌声に Whisper 系の時刻が合うかは未知（歌は話し声より崩れやすい、推測）

## 着手の仕方（未検証。galleria で確かめる）

- **何ができるようになるか**: 録音した日本語のナレーション＋台本のテキストから、台本どおりの文字で時刻の付いた SRT / ASS を自動で作る。効く型: talk、embed
- **機械**: galleria WSL（GPU）。CPU でも動く（`--device cpu --compute_type int8`）が遅い
- **入れるもの**: stable-ts 2.19.1（＋faster-whisper 1.2.1 を使うなら `stable-ts[fw]`）、または whisperx 3.8.6。PyTorch は **RTX 5080（Blackwell）では CUDA 12.8 以上のビルドが要る**（WhisperX の README が CUDA 12.8 を指定。RTX 50 系の要件は推測）。費用 0、アカウント不要（話者分離を使わない限り）。モデルは初回に Hugging Face から自動で落ちる
- **VRAM の見込み**: large-v3 / turbo の書き起こし＋wav2vec2 の整列で 4〜8GB（根拠: faster-whisper・WhisperX の README の数値から推測）。16GB で足りる
- **成熟度**: WhisperX は 2026-06 まで更新が続く。stable-ts は 2025-08 が最新。faster-whisper は 2025-10

### 最小の手順

```bash
# galleria WSL
mkdir -p ~/video-tools-trial/align && cd ~/video-tools-trial/align
uv venv --python 3.12 && . .venv/bin/activate
uv pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu128   # RTX 50 系向け（推測）
uv pip install "stable-ts[fw]==2.19.1"
python3 -c "import torch; print(torch.__version__, torch.cuda.is_available(), torch.cuda.get_device_name(0))"
# narration.wav（自分の録音か、時刻の無い TTS）と script.txt（台本。1 行＝字幕 1 枚）
stable-ts narration.wav --align script.txt --language ja --model large-v3 -o narration.srt   # README にあるのは --align・--language・-o。--model の書き方は推測（stable-ts -h で確かめる）
# Python で original_split を指定する版
python3 - <<'EOF'
import stable_whisper
m = stable_whisper.load_model("large-v3")
r = m.align("narration.wav", open("script.txt", encoding="utf-8").read(), language="ja", original_split=True)
r.to_srt_vtt("narration_lines.srt", word_level=False)
r.to_ass("narration_karaoke.ass")
EOF
```

- WhisperX で書き起こしから（台本が無いとき）: `uv pip install whisperx==3.8.6` → `whisperx narration.wav --model large-v3 --language ja --highlight_words True`。ReazonSpeech の wav2vec2 で整列するなら `--align_model reazon-research/japanese-wav2vec2-large-rs35kh`（動くかは未確認。推測）
- 試す素材: 西尾の手元の録音か、VOICEVOX で作った音声（こちらは正解の時刻を VOICEVOX の `audio_query` から取れるので、**整列の誤差を測れる**）

### 動いたと言える確かめ方

- `torch.cuda.is_available()` が True、`get_device_name` が RTX 5080
- `narration_lines.srt` の各字幕の文字が `script.txt` の各行と一字一句同じで、字幕の数が行数と同じ
- VOICEVOX の音声で、各行の開始時刻と VOICEVOX が返す音素の開始時刻の差を出し、中央値が 0.1 秒以内（目安。数値は推測）。差が大きい行（数字・英字・記号を含む行）を一覧にする
- `ffmpeg -i video.mp4 -vf subtitles=narration_lines.srt out.mp4` で焼いて目で見て、話し始めと字幕の出が合っている（[[web-check-subs-ffmpeg-libass-youtube-caption-files]]）

### 所要の見込み（推測）

- 環境作り 30〜60 分（CUDA の組み合わせで詰まると半日）。3 分の音声の整列は GPU で 1 分以内

## Open Questions

- 日本語で WhisperX の整列（jonatasgrosman の wav2vec2）と stable-ts の `align()` と Qwen3-ForcedAligner（[[web-check-subs-qwen3-forcedaligner-mfa-reazonspeech]]）のどれが正確か。公開の比較（日本語）は見つけていない。VOICEVOX の正解時刻で自分で測るのが早い
- 読経・真言のような、辞書に無い読み・反復の多い音声で整列が崩れないか（ASR の段で崩れた経験がある。[[exp-sutra-voicevox-singing]]）
- 台本に数字・英字（「Opus 5.5」「LLM」）が混ざるとき、読みに直した台本で整列して、表示は元の表記に戻す、という二重の台本が要るか（[[exp-sutra-sync-subtitles]] の「表示の読みと発音を分ける」と同じ構造）
- RTX 5080 と ctranslate2（faster-whisper）・PyTorch の組み合わせが WSL で素直に動くか
