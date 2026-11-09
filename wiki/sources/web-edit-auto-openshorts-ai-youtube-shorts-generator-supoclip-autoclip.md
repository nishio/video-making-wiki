---
type: source
summary: 書き起こし＋LLM で長尺からハイライトを選んで縦型にする OSS の 5 つ（2026-11-09 時点の README とコード）。OpenShorts（MIT、Docker、Gemini かローカル LLM）は LLM が出した区間を語の時刻に吸着させ、「LLM はミリ秒の計算が苦手、語の時刻が正」とコードに書く。プロンプトの主基準は「2 秒テスト」。AI-Youtube-Shorts-Generator（MIT）は LLM の出した秒数を尺で切り詰めるだけ。SupoClip は AGPL で AssemblyAI のキーが要る。AutoClip（MIT、v1.5.8）は中国語圏向けのデスクトップ版で日本語の README がある。ClipsAI は 2024-01 で止まっている
video_types: [promo, talk]
url: https://github.com/mutonby/openshorts
author: mutonby（OpenShorts）／SamurAIGPT・Anil-matcha（AI-Youtube-Shorts-Generator）／FujiwaraChoki（SupoClip）／zhouxiaoka（AutoClip）／ClipsAI
published: いずれも取得日の main。OpenShorts の最終 commit 2026-11-08、AutoClip v1.5.8 は 2026-11-02、AI-Youtube-Shorts-Generator のコードの最終変更 2026-06-20、ClipsAI の最終 push 2024-01-17
retrieved: 2026-11-09
sources:
  - https://github.com/mutonby/openshorts（README.md、clip_selection.py、gemini_worker.py）
  - https://github.com/SamurAIGPT/AI-Youtube-Shorts-Generator（README.md、shorts_generator/highlights.py）
  - https://github.com/FujiwaraChoki/supoclip（README.md）
  - https://github.com/zhouxiaoka/autoclip（README.md、README-JA.md）
  - https://github.com/ClipsAI/clipsai（README.md）
---

# 切り抜きの OSS — OpenShorts・AI-Youtube-Shorts-Generator・SupoClip・AutoClip・ClipsAI

## 何の文献か

- 5 つの OSS の README と、選択の部分のコード（OpenShorts と AI-Youtube-Shorts-Generator は読んだ。他は README だけ）。どれも作者の文書で、選択の精度の測定はない。AutoClip の作者たちの観察の報告は [[web-edit-auto-autoclip-what-drives-views-2026]] に分けた
- 数字は GitHub API（2026-11-09）

| repo | star | ライセンス | 最新 | 書き起こし | 選ぶ LLM | 動く形 |
|---|---|---|---|---|---|---|
| mutonby/openshorts | 約 7,600 | MIT | 最終 commit 2026-11-08（リリースなし） | faster-whisper（語の時刻）、任意で Parakeet | Gemini 3.1 Flash-Lite（既定）か、OpenAI 互換のローカル LLM | Docker Compose ＋ Web 画面、REST API、MCP |
| SamurAIGPT/AI-Youtube-Shorts-Generator | 約 5,800 | MIT | コードの最終変更 2026-06-20（その後は README の動画リンクの差し替え） | MuAPI の whisper-1 か、ローカルの faster-whisper | MuAPI の gpt-5-mini か、OpenAI（gpt-4o-mini）・Gemini（2.5 Flash） | Python の CLI とライブラリ |
| FujiwaraChoki/supoclip | 約 2,700 | **AGPL-3.0** | 最終 push 2026-11-08 | **AssemblyAI（要キー）** | Gemini・GPT・Claude・Ollama | Docker Compose、MCP、iOS アプリ（ホスト版） |
| zhouxiaoka/autoclip | 約 10,100 | MIT | v1.5.8（2026-11-02） | 作者の字幕、ローカル Whisper・SenseVoice、クラウド | 選べる（Ollama・LM Studio も） | Windows・macOS（Apple Silicon）のデスクトップ版、CLI、MCP |
| ClipsAI/clipsai | 約 560 | MIT | 最終 push **2024-01-17** | WhisperX | （LLM ではなく書き起こしの分割） | Python ライブラリ |

## 書いてあること

### OpenShorts

- 「The open-source OpusClip alternative」。自分で動かすなら無料・透かしなし、ホスト版は無料 20 分/月（透かし）、有料 $12/月から（README）
- 手順（README の Technical Pipeline）: 取り込み → **faster-whisper で語単位の時刻** → **PySceneDetect で場面の切れ目** → Gemini が 3〜15 の場面を選ぶ（15〜60 秒）→ ffmpeg で切る → 縦にリフレーム（TRACK＝MediaPipe＋YOLOv8 の顔追跡、GENERAL＝ぼかし背景、SPLIT＝2 人を上下に積み字幕を継ぎ目に、**SCREENCAST＝画面の上に話者**）→ 字幕・フック文字 → 投稿
- **選択のプロンプト**（gemini_worker.py、原文）:
  - 一次の採点:「THE 2-SECOND TEST is the main criterion: would the first 2 seconds of this moment force a cold viewer (no context) to keep watching? Windows that only work with prior context score low.」
  - 詳細の選択:「THE 2-SECOND RULE: the clip MUST open on its strongest moment.」「Start slightly before the hook and end slightly after the payoff when possible.」「Do not cut in the middle of a word or phrase.」「STANDS ALONE: the clip must make sense to someone who has seen nothing else. If it opens on a pronoun, a "that", a "so anyway", or an answer whose question was asked earlier, move the start back ... A brilliant moment that needs the previous five minutes is not a clip.」「DIVERSITY: never return two clips that make the same point」
  - 文字の欄は「TRANSCRIPT_LANGUAGE」で書かせ、フックは「no fake claims」
- **時刻の扱い**（clip_selection.py の `snap_clip_to_words`、原文の docstring）:「Snap Gemini-proposed clip boundaries onto real word boundaries plus a bit of the surrounding silence. **LLMs are bad at millisecond arithmetic; the word-level timestamps are ground truth**, so cuts land in pauses instead of mid-word.」。始まりは 1.5 秒以内の最も近い語の頭に吸着して、前の無音に最大 0.35 秒入る。終わりは最も近い語の終わりに吸着して、後ろの無音に最大 0.45 秒入る。採点の窓も Whisper のセグメントの境目に合わせる
- 本数の決め方のコメント（clip_selection.py）: 本番の 429 件のうち 95% が 3 本以下で、「Users who received 1-3 clips came back a second day 0.4% of the time; those who received 4-9 came back 16.1% — so the clip count, not the clip quality, is what the retention curve hangs on」（2026-08-03 の自社の測定とコメントに書いてある。条件は書かれていない）
- ローカル LLM: `LLM_BASE_URL` を Ollama などに向けると、選択も手元で済む。「The only cloud call in the clip pipeline is the moment picker: it sends the transcript (never the video) to Gemini」。「7-8B models return valid JSON reliably, 3B ones do not」。Ollama は既定の 4096 トークンで黙って切るので `OLLAMA_CONTEXT_LENGTH=16384`。映像を見る機能（レイアウトの自動選択、無音の動画）は Gemini のキーが要る
- GPU: 既定は CPU（8 分の動画で 5〜8 分）。NVIDIA なら約 1 分。「8 GB of VRAM is enough for `large-v3-turbo` fp16 plus the detection models」。Windows は Docker Desktop の WSL2 バックエンド
- Parakeet は「25 European languages」（日本語は Whisper に戻る）
- 同じ repo に、AI の俳優で広告動画を作る「AI Shorts」や公開ギャラリーも入っている（README）

### AI-Youtube-Shorts-Generator（SamurAIGPT）

- 「The open-source alternative to Opus Clip, Vidyo.ai, Klap, SubMagic ...」。既定の `--mode api` は MuAPI（有料の API、この repo の後援）に全部を投げる。`--mode local` は yt-dlp・faster-whisper・ffmpeg/OpenCV を手元で、LLM だけ OpenAI か Gemini（README）
- 選ぶ基準（highlights.py の `VIRALITY_CRITERIA`、影響順と書く）: HOOK MOMENTS、EMOTIONAL PEAKS、OPINION BOMBS、REVELATION MOMENTS、CONFLICT/TENSION、QUOTABLE ONE-LINERS、STORY PEAKS、PRACTICAL VALUE
- プロンプト:「Every highlight must open with a strong HOOK — a line that grabs attention within the first 3 seconds」「Duration sweet spot: 45-90 seconds」「Never cut mid-sentence or mid-thought」「Score 0-100 on viral potential (not general quality)」
- **時刻の扱い**（コードを読んだ。実行はしていない）: 書き起こしは `[123.4s] 本文` の形で各セグメントの**始まりの時刻だけ**を付けて LLM に渡し、LLM が `start_time`・`end_time` を float で返す。後処理は 0 未満・逆順を捨て、動画の尺で切り詰め、重なり 50% 超を点の高い方に寄せるだけで、**セグメントや語の境目への吸着はない**
- 30 分を超える動画は 20 分の窓（重なり 60 秒）に分けて選ぶ

### SupoClip

- README の副題は OpusClip への悪態。自分で動かすなら「AGPL-3.0, unlimited usage on your own hardware」。ホスト版と iOS アプリもある
- 書き起こしに **AssemblyAI の API キーが必須**、加えて LLM のキー（Google・OpenAI・Anthropic）か Ollama。選ぶのは「3–7 most clip-worthy segments」、各切り抜きに「hook, engagement, value, and shareability scores」
- 「Performance loop — views, likes, comments and shares flow back from each platform and steer future clip selection toward what works for your audience」（投稿の反応を次の選択に戻す、と書く。効果の測定は書かれていない）

### AutoClip（zhouxiaoka）

- 中国語の README に加えて**日本語の README（README-JA.md）**がある。「カット・構図・書き出しはローカル。分析モデルを選び、作者字幕、ローカル Whisper / SenseVoice、設定済みクラウド文字起こしを利用できます」
- 対象は抖音・小紅書・TikTok・Reels・YouTube Shorts・Bilibili・YouTube。「主に検証しているのは対談・ポッドキャスト・講義・トーク」
- 作者の実測の例（2026-10-01、同じ Apple Silicon Mac）: 1h43m の英語の講演（作者字幕あり）→ 7.5 分で 10 本、文字モデルの費用 ¥0.09（人民元）。2h52m の中国語の対談（字幕なし、Whisper base）→ 29.5 分で 10 本、¥0.20（qwen-plus の当時の単価での見積もり）
- インストーラに Python と FFmpeg が入っている。Windows 10/11 x64 の `-setup.exe`。アプリは無料・MIT、クラウドの分析・書き起こしは自分のキーと料金

### ClipsAI

- 「designed for audio-centric, narrative-based videos such as podcasts, interviews, speeches, and sermons」。`ClipFinder().find_clips(transcription)` で書き起こしから区間を出し、`resize()` で話者に合わせて 9:16。話者の分離に pyannote（Hugging Face のトークンが要る）
- 最終 push 2024-01-17。LLM を使う前の世代の作り。いま選ぶ理由は薄い

## この wiki への含意

- **何を AI に任せられるか**（各 README の主張）: 書き起こし、候補の区間の選択と点数付け、縦へのリフレーム（顔追跡・2 人の積み・画面＋話者）、字幕の焼き込み、フック文字・タイトル、投稿。**どれも中身は「書き起こし → LLM が区間を選ぶ」で、[[exp-shortmovie-draft-generator]] と同じ骨格**
- **何が人の判断として残るか**: どの README も「確認してから投稿」の手順を書く（AutoClip:「字幕・構図・内容の完全性を確認し」）。選んだ切り抜きを公開するかは人。研究としての根拠はどこにもなく、残るものは作り手の手順書から読んだもの
- **[[exp-shortmovie-draft-generator]] と照らす**:
  - **時刻を字幕データから取る分担は、OpenShorts のコードとそのまま一致する**。西尾の回した道具 1 は「元の chunk のタイムスタンプは絶対に変更しない」を LLM への指示で守らせた。OpenShorts は LLM に自由に秒数を出させてから、**コードで語の時刻に吸着させる**。同じ問題（LLM が時刻を作文するとずれる）への、指示でなく後処理での対処。AI-Youtube-Shorts-Generator は吸着しないので、同じ問題を抱えたまま（コードからの読み）
  - **冒頭 2 秒は一致**: 西尾の道具のプロンプトの「冒頭 2 秒でインパクト」は、OpenShorts の「THE 2-SECOND TEST/RULE」とほぼ同じ言い方。AI-Youtube-Shorts-Generator は 3 秒
  - **「単独で意味が通る」は西尾の道具には明示がない**: OpenShorts の STANDS ALONE（代名詞・「それで」・前の質問への答えで始まるなら始まりを前に戻す）は、[[exp-democracy-river-video]] と [[web-opus2-tatebayashi-opus-5-5-vs-gpt-6-astra-training-video]] の「切り抜きだけでは説明にならない」と同じ問題を、選択の規則で避けている
  - **終わりの延長**: 西尾は全カットの終わりを 3 秒延ばした（理由の記録なし）。OpenShorts は「payoff の少し後で終える」をプロンプトで、語の後ろの無音へ最大 0.45 秒をコードで足す。延ばす向きは同じで、量は一桁違う
  - **尺**: 西尾の道具は 90 秒以内・理想 60 秒、OpenShorts は 15〜60 秒、AI-Youtube-Shorts-Generator は 45〜90 秒
  - **縦動画**: 西尾の道具は「縮めて黒帯」。OpenShorts は話者に寄せる（TRACK）・2 人を積む（SPLIT）・画面＋話者（SCREENCAST）を場面ごとに選ぶ。スライドの講演には SCREENCAST が近い（推測）
  - 西尾の道具 2 の「話している内容に肯定的に」に近いのは、OpenShorts のフックの「no fake claims」だけ。話者に不利な切り抜きを避ける規則はどれにもない
- **talk の型の切り抜きへの注意**: どの基準も SNS の拡散（promo）向け。解説の講演から「理解させる」短尺を作る基準ではない（[[exp-shortmovie-draft-generator]] の Open Questions と同じ問い）

## 着手の仕方（未検証。galleria で確かめる）

- **表現できるようになること**: 手元の講演・LT の録画から、縦型の切り抜き候補を手元で（素材を外に出さずに）作る。西尾の道具の選択の規則と並べて比べる。効く型: promo
- **機械**: galleria。OpenShorts は Docker（galleria Windows の Docker Desktop＋WSL2。**Docker が galleria に入っているかは未確認、無ければ入れるかは西尾が決める**）。GPU は RTX 5080（VRAM の見込み: Whisper large-v3-turbo fp16 と検出のモデルで 8GB、README の記述）。ローカル LLM なら Ollama も要る（未導入。VRAM は 7〜8B モデルで数 GB、推測）
- **費用・アカウント**: OpenShorts は自分で動かせば 0。選択に Gemini を使うなら **要: Gemini の API キー**（README は「< $0.01 per 10-min video」）。ローカル LLM ならキー不要。AI-Youtube-Shorts-Generator の local は **要: OpenAI か Gemini のキー**。SupoClip は **要: AssemblyAI のキー**。AutoClip はアプリ無料、分析に LLM のキーかローカル LLM
- **成熟度**: OpenShorts は毎日 commit、ただしホスト版の課金の変更も同じ repo に入る。AI-Youtube-Shorts-Generator のコードは 2026-06 から止まり気味。ClipsAI は止まっている
- **最小の手順（OpenShorts、galleria の WSL か PowerShell。README のまま。ローカル LLM の行は README の例）**:
  ```bash
  mkdir -p ~/video-tools-trial && cd ~/video-tools-trial
  git clone https://github.com/mutonby/openshorts.git && cd openshorts
  cp .env.example .env
  # ローカル LLM で選ぶ場合（Ollama を Windows 側で動かしている前提）
  #   LLM_BASE_URL=http://host.docker.internal:11434/v1
  #   LLM_MODEL=qwen2.5:14b
  docker compose up --build
  # ブラウザで http://localhost:5175 → Clip Generator に録画を上げる
  ```
  比べる側の最小（AI-Youtube-Shorts-Generator の local、要キー）:
  ```bash
  cd ~/video-tools-trial && git clone https://github.com/SamurAIGPT/AI-Youtube-Shorts-Generator.git && cd AI-Youtube-Shorts-Generator
  uv venv && . .venv/bin/activate && uv pip install -r requirements.txt -r requirements-local.txt   # README は python3.10 -m venv と pip。uv は推測
  # .env に LLM_PROVIDER=gemini と GEMINI_API_KEY、LOCAL_WHISPER_DEVICE=cuda
  python main.py ~/video-tools-trial/talk.mp4 --mode local --language ja --num-clips 5 --output-json result.json
  ```
- **動いたと言える確かめ方**: OpenShorts は画面にクリップが 3 本以上並び、backend の記録に選んだ encoder と書き起こしの device が出る（README「The backend log on the first job reports the chosen encoder and transcription device」）。AI-Youtube-Shorts-Generator は `output/short_01.mp4` 〜 と `result.json` の `shorts[].start_time/end_time`。**時刻の吸着の差を見る**: 各切り抜きの始まりと終わりが語の途中で切れていないかを、`ffmpeg -ss <end-1> -i talk.mp4 -t 2` で聞いて数える（OpenShorts は吸着あり、SamurAIGPT はなし、という読みの確認）。同じ録画で [[exp-shortmovie-draft-generator]] の 2 の 5 案と区間の重なりを表にする
- **所要の見込み（推測）**: Docker が既にあれば 1〜2 時間（モデルのダウンロード込み）。無ければ Docker の導入から

## Open Questions

- OpenShorts の吸着は日本語でも効くか。faster-whisper の日本語の「語」は字・語のどちらの単位か（[[web-check-subs-whisperx-stable-ts-faster-whisper]] の論点と同じ）
- 日本語の講演で、ローカルの 7〜8B モデルが STANDS ALONE などの規則を守れるか
- OpenShorts の「本数が多いと翌日も戻る」は自社の利用の数字で、切り抜きの質の話ではない。視聴者の反応の数字ではない
- SupoClip の「反応を次の選択に戻す」が、少数の投稿でも効くか（[[web-edit-auto-autoclip-what-drives-views-2026]] は、同じアカウントの中でも話題と人で 8〜450 倍ばらつくと書く）
- AutoClip の日本語の README はあるが、日本語の動画での実測の例はない（中国語・英語だけ）
