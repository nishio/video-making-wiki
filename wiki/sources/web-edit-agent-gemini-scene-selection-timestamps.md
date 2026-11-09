---
type: source
summary: 編集のために「素材のどこを使うか」を、動画を入力できるモデルに時刻付きで選ばせるときの公式の記述。Gemini API は既定で 1 秒 1 コマ・「毎秒タイムスタンプを入れる」・時刻の指定は MM:SS で、細かさは秒の単位。長尺（5〜10 分超）で特定の場面を探すなら agentic（文字起こしを先に見て必要な区間だけコマを読む）を公式が推す。Qwen3-VL は各コマの前に「<3.0 seconds>」の文字の時刻を置く方式。どれも時刻の精度（何 ms ずれるか）は公表していないので、切る位置は文字起こしの単語の時刻に吸着させるのが、エージェント向けの編集の道具の共通のやり方
video_types: [promo, talk]
url: https://ai.google.dev/gemini-api/docs/video-understanding
author: Google（Gemini API ドキュメント）／Qwen Team（Qwen3-VL Technical Report、arXiv 2511.21631）／Browser Use（video-use）
published: Gemini の docs は更新日の表示なし（agentic は 2026-09-01）。Qwen3-VL の報告は 2025-11-26（v2）
retrieved: 2026-11-09
sources:
  - https://ai.google.dev/gemini-api/docs/video-understanding（第 3 回で取得した本文を再読。「Refer to timestamps」「Agentic video understanding」「Set clipping intervals」「Set a custom frame rate」「Best practices」の節）
  - https://arxiv.org/abs/2511.21631（Qwen3-VL Technical Report、§2.3 Video Timestamp）
  - https://github.com/browser-use/video-use（README の「How it works」）
  - https://extremraym.com/cloud/resolve-scripting-doc/（Resolve の DetectSceneCuts・TranscribeAudio）
  - https://helpx.adobe.com/premiere-pro/kb/fixed-issues.html（Premiere 26.5 の Paper Edit）
---

# 動画を入力できるモデルに、編集のための場面と時刻を選ばせる

## 何の文献か

- Gemini API の公式 docs（video-understanding）。第 3 回で批評役として読んだページ（[[web-means-critic-gemini-video-understanding]]）を、**編集のための場面選び**の側から読み直した。入れ方・上限・トークン・価格・規約はそのページにあるので書き直さない
- Qwen3-VL の技術報告（arXiv 2511.21631 v2、2025-11-26）の §2.3。モデルカードの主張（「秒単位で索引できる」）の元の設計の記述。ローカルで動かす話は [[web-means-critic-qwen3-vl-open-vlms]]
- 比べるため: 動画モデルを使わない video-use（[[web-edit-agent-video-use-and-claude-code-editing-examples]]）の README、Resolve の scripting README、Premiere の release notes
- 種類: 公式ドキュメント・技術報告。**場面選びの時刻の精度を測った数字はどれにも無い**

## 書いてあること

### Gemini API（場面選びに効く記述だけ）

- できること: 「describe, segment, and extract information from videos ... refer to specific timestamps within a video」（冒頭）
- **時刻の細かさ**: static（既定）は「Extracts frames at a fixed rate (1 FPS) ... Timestamps are added every second」。プロンプトで時刻を指すときは「use the `MM:SS` format (e.g., `01:15` for 1 minute and 15 seconds)」。つまり公式の書き方の単位は**秒**で、コマ単位の時刻を返すとは書いていない
- 公式の例のプロンプト: 「Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.」（「目立つ場面に時刻を付けよ」はそのまま場面選びの形）
- 1 FPS の注意: 「it may miss details in videos with rapid motion or quick scene changes」。fps は `processing: {type: "static", fps: ...}` で変えられる（例は 0.5）
- 区間だけ見せる: `start_offset`・`end_offset`（「"1200s" or "10.5s"」）。長い素材の一部だけを見せて選ばせるのに使える
- **agentic の使い分け**（2026-09-01 から。Gemini 4 Argon・3.8 Flash・3.6 Flash・3.5 Flash Lite）:
  - 「Static (default): Best for short clips (under 5 minutes) ... or **frame-level precision across the entire clip**」
  - 「Agentic: Best for long-form videos (over 5–10 minutes), needle-in-a-haystack retrieval, or **queries targeting specific moments or topics**. The model inspects transcripts first and loads only relevant visual segments on demand, reducing video input token usage by up to 88%」
  - 有効にするのは video の part に `"processing": "agentic"`。長いと時間がかかるので `background` での非同期を例にしている
  - 応答の `steps` に `processing_call`（「the model requested a video segment or audio transcript, identified by `id`」）と `processing_result` が入る。例では区間の時刻は出ておらず `id` と `signature` だけ（どの区間を読んだかを編集に使えるかは不明）
- 批評の側で見たとおり、agentic は「文字起こしを先に見る」ので、**話している内容で場面を探す**（講演から「○○を説明している所」）には向き、**話さない映像の場面**（実機が動く瞬間、画面が切り替わる瞬間）を探すには static で fps を上げる方が筋（公式の使い分けの記述からの推論）

### Qwen3-VL の時刻の入れ方（技術報告 §2.3）

- Qwen2.5-VL は時刻を位置埋め込み（MRoPE）で入れていたが、長い動画で位置の番号が大きく疎になる、学習にいろいろな fps の一様なデータが要る、という問題があった、と書く
- Qwen3-VL は「each video temporal patch is prefixed with a timestamp expressed as a formatted text string—e.g., <3.0 seconds>」。学習では秒と時:分:秒の両方の書き方を作った。「it enables the model to perceive temporal information more effectively and precisely, thereby facilitating time-aware video tasks such as video grounding and dense captioning」
- 時刻の単位はコマの組（temporal patch）ごとで、どの細かさの時刻を返せるかは fps の設定次第（報告からの推論。精度の数字は §2.3 には無い）

### 動画モデルを使わない場面選び（比べるため）

- video-use: 「The LLM never watches the video. It **reads** it」。単語ごとの時刻付きの文字起こし（約 12KB）を常に読み、迷う所だけフィルムストリップ＋波形の PNG を作って見る。「30,000 frames × 1,500 tokens = 45M tokens of noise」に対し「12KB text + a handful of PNGs」
- Resolve の API: `Timeline.DetectSceneCuts()`（場面の切れ目を検出してカットを入れる）、`MediaPoolItem.TranscribeAudio(useSpeakerDetection)`。21.1 で「retrieve Media Pool transcriptions with speaker and timing data」が足された（業界誌による。[[web-edit-agent-davinci-resolve-premiere-scripting]]）
- Premiere 26.5: 「Create sequences from transcripts with **Paper Edit**」（文字起こしの行を選ぶと sequence になる。人が選ぶ機能）
- 画面の変わり目の検出は ffmpeg の `select='gt(scene,...)'` でもできる（[[web-check-spec-ffmpeg-contact-sheet-select-tile-drawtext]]）

## 何を AI に任せられるか

- **公式が書いていること**: Gemini は動画から「salient moments」を時刻付きで挙げられる、長尺で特定の場面・話題を探すのは agentic が向く。Qwen3-VL は時刻付きの出来事の位置づけ（video grounding）を狙って設計した
- **実例で確かめられたこと**: このページの文献には、モデルが選んだ時刻でそのまま切った結果を評価したものが無い。第 3 回の SPOTLIGHT（[[web-means-critic-video-bench-spotlight]]）は「AI 生成動画の誤りを時刻付きで見つける」課題で、Gemini 2.5 Pro でも人の半分程度だった（場面選びではなく誤り探し）
- 秒の単位の時刻は「どのあたりを使うか」を決めるのには足りるが、**切る位置**（言葉の途中で切らない）には粗い。エージェント向けの編集の道具は、どれも切る位置を文字起こしの単語の時刻に吸着させ、30〜250 ms の余白を足している（[[web-edit-agent-moviepy-ffmpeg-concat]]）

## 何が人の判断として残るか

- 文献は場面選びの判断の良し悪しについて書いていない
- Resolve の第三者の MCP の作者は「Performance is most of what makes a take right, and none of it is measurable from a waveform or a transcript」と書く（[[web-edit-agent-video-editing-mcp-servers]]）。文字起こしを先に見る agentic も同じ限界を持つはず（推測）
- 第 3 回の批評役の文献はどれも、動画の評価で人との一致は低〜中程度と報告している（[[web-means-critic-videoscore]]）

## 日本語の対応

- Gemini の docs に日本語の音声・画面の文字での場面選びの精度の記述は無い（第 3 回と同じ）。agentic が先に見る「transcripts」が日本語でどう作られるかも書いていない
- Qwen3-VL の報告は多言語の OCR を強調するが、日本語の音声には触れていない（Qwen3-VL は音声を入力しない。音声も入れるなら Qwen-Omni、[[web-means-critic-qwen-omni]]）

## 費用・アカウント・利用条件

- Gemini: [[web-means-critic-gemini-video-understanding]] のとおり（要: API キー。無料枠の入力は人が読むことがある。未公開の素材・第三者の写る素材は有料枠のみ）。10 分の講演を static の既定で入れると約 6 万トークン（docs の「~100 tokens/秒」から）、3.8 Flash で入力は約 $0.045
- Qwen3-VL: Apache-2.0、ローカル（galleria の GPU）。素材は外に出ない

## この wiki への含意

- **経験の設計は「場面選びを文字だけでやる」側**: [[exp-shortmovie-draft-generator]] は Whisper／YouTube の字幕の時刻付きの文を LLM に渡して切り抜きを選ばせた。agentic の Gemini も「文字起こしを先に見る」ので、話の切り抜きなら経験の方式と同じ情報で選ぶことになる。動画モデルが効くのは**話さない映像の場面**（画面収録で操作がうまくいった瞬間、実機が反応した瞬間）を探すとき
- **THINKLET のデモ（[[exp-thinklet-reading-demo-video]]）のような素材は動画モデルの出番**: iPhone で撮った実機の映像は、声の質問と端末の反応（回答の再生）が音で取れるが、「本の見開きが写った瞬間」「画面が切り替わった瞬間」は映像にしかない。static で fps を 2〜4 に上げ、「端末が回答を話し始めた時刻」「本の見開きがはっきり写っている区間」を MM:SS で挙げさせ、切る位置は人か音の検出で詰める、という分担が筋（このページの提案、未検証）
- **promo の拍に合わせた素材選びには粗い**: 1 秒の単位では、拍（0.2〜0.5 秒）に合わせて切る西尾の promo（[[exp-sutra-hype-editions]]）の素材選びには足りない。候補の区間を選ばせるまでにとどめる

## 着手の仕方（未検証。galleria で確かめる）

- **何ができるようになるか**: 撮った素材（講演の録画・画面収録・実機の映像）から「使う区間の候補」を時刻付きの JSON で出させ、そのまま ffmpeg で切って並べた下書きを作る。効く型: promo（実物の収録から見せ場を選ぶ）、talk（講演から要点の区間を選ぶ）
- **機械**: どこでも（API）。galleria WSL で `uv run --with google-genai`。**要: API キー・費用（西尾が決める）**。手順の骨格は [[web-means-critic-gemini-video-understanding]] の `critic_gemini.py` と同じで、問いと出力の形だけ変える
- **成熟度**: 動画入力は Gemini 1.5 以来。agentic は 2026-09-01
- **最小の手順**（WSL。公式の upload と processing の書き方を元にし、問いと JSON の形はこのページの提案）:
  ```bash
  cd ~/video-tools-trial/select && export GEMINI_API_KEY=...   # 西尾が用意
  uv run --with google-genai python select_gemini.py demo.mp4 static 2 > cands.json
  uv run --with google-genai python select_gemini.py lecture.mp4 agentic > cands_long.json
  ```
  `select_gemini.py`（推測で書いた最小形。upload → ACTIVE を待つ所は critic_gemini.py と同じ）:
  ```python
  import sys, time, json
  from google import genai
  client = genai.Client(); path, mode = sys.argv[1], sys.argv[2]
  f = client.files.upload(file=path)
  while not f.state or f.state.name != "ACTIVE":
      time.sleep(5); f = client.files.get(name=f.name)
  part = {"type": "video", "uri": f.uri, "mime_type": f.mime_type}
  part["processing"] = {"type": "static", "fps": float(sys.argv[3])} if mode == "static" else "agentic"
  Q = ("この素材から、作品の動きが一番よく分かる区間を最大 5 つ選んでください。"
       "JSON の配列だけを返す: [{\"start\":\"MM:SS\",\"end\":\"MM:SS\",\"what\":\"映っていること\",\"why\":\"選んだ理由\"}]")
  r = client.interactions.create(model="gemini-3.8-flash", input=[part, {"type": "text", "text": Q}])
  print(r.output_text)
  ```
  候補を切るときは、`start` を 0.5 秒前に、`end` を 0.5 秒後ろにずらしてから、文字起こしの単語の境界（[[web-check-subs-whisperx-stable-ts-faster-whisper]]）か無音（`silencedetect`）に吸着させる（推測。秒の単位の時刻をそのまま切ると言葉の途中になりうるため）
- **動いたと言える確かめ方**: (1) JSON として読める（`python -c "import json;json.load(open('cands.json'))"`）。(2) 各候補の `start` の時刻の前後 2 秒のコマをコンタクトシートで見て、`what` に書かれたことが写っているかを人が ○×（5 候補で 4 つ以上 ○ なら使える、を仮の基準に）。(3) 同じ素材を static の fps 1 と 4 で 2 回聞き、候補の時刻が何秒ずれるかを表にする。(4) 長尺（10 分以上）で agentic と static の `usage` のトークン数と候補の一致を比べる
- **所要の見込み（推測）**: キーがあれば 1 時間。○× の採点を入れて 2 時間

## Open Questions

- Gemini が返す時刻の精度（実際の出来事から何秒ずれるか）。公式に数字が無い。fps を上げると時刻の精度が上がるか
- agentic の `processing_call` から「モデルがどの区間を読んだか」を取り出せるか（docs の例では `id` だけ）。取れれば、それ自体が場面選びの手がかりになる
- 文字起こしを先に見る agentic は、話さない映像（実機の反応・画面の変化）の場面を見落とすか
- 日本語の講演で、Gemini の場面選びと、文字起こしだけを LLM に読ませる方式（経験・video-use）の選ぶ区間がどのくらい重なるか

