---
type: source
summary: Gemini API の動画理解（2026-11-09 時点の公式 docs）。動画ファイルを映像と音声のまま入れられ、既定は 1 秒 1 コマ（fps は指定可）・音声は 1 チャンネルに落とす。1M コンテキストで既定 3 時間・高解像度 1 時間まで。2026-09 から「agentic」処理（文字起こしを先に見て必要なコマだけ読む）が加わった。docs 内でトークン数・音声のビットレートの記述が食い違っている。無料枠に入れたものは Google が学習に使い人が読むことがある
video_types: [promo, talk, embed]
url: https://ai.google.dev/gemini-api/docs/video-understanding
author: Google（Gemini API ドキュメント）
published: unknown（ページに更新日の表示なし。changelog の最新は 2026-11-06）
retrieved: 2026-11-09
sources:
  - https://ai.google.dev/gemini-api/docs/video-understanding
  - https://ai.google.dev/gemini-api/docs/audio
  - https://ai.google.dev/gemini-api/docs/media-resolution
  - https://ai.google.dev/gemini-api/docs/tokens
  - https://ai.google.dev/gemini-api/docs/models
  - https://ai.google.dev/gemini-api/docs/pricing
  - https://ai.google.dev/gemini-api/docs/changelog
  - https://ai.google.dev/gemini-api/terms （Effective March 23, 2026）
---

# Gemini API の動画理解（2026-11-09 時点）

## 何の文献か

Google の公式ドキュメント（製品ドキュメント・モデル一覧・価格・changelog・追加利用規約）。2026-11-09 に curl で取得した（ai.google.dev はこの時点で Markdown をそのまま返す）。数値はすべて「2026-11-09 時点の公式ページによる」。動画生成の側（Gemini Omni Flash・Veo）は [[web-genvid-gemini-omni-veo]] にある。このページは**動画を入力して理解させる側**だけを書く。

## 書いてあること

### 入れ方と上限（video-understanding）

| 入れ方 | 上限 | 公式の推奨 |
|---|---|---|
| File API | 20GB（有料）／2GB（無料） | 100MB 超、10 分超、何度も使うファイル |
| Cloud Storage の登録 | 1 ファイル 2GB | 同上 |
| inline | 100MB 未満（本文の別の箇所は「リクエスト全体で 20MB 未満」と書く） | 1 分未満の単発 |
| YouTube URL | 公開動画のみ（限定公開・非公開は不可）。無料枠は 1 日 8 時間まで | ― |

- 形式: mp4・mpeg・mov・avi・x-flv・mpg・webm・wmv・3gpp
- 長さ: 「1M コンテキストのモデルは、既定（低いメディア解像度）で 3 時間まで、高いメディア解像度で 1 時間まで」
- 1 リクエストの動画は Gemini 2.5 以後で最大 10 本（YouTube の節の記述）
- 時刻は `MM:SS` で指せる。テキストと動画 1 本なら、テキストを動画の**後**に置くよう書いている

### 映像と音声をどう取り込むか

- 「Gemini は**音声と映像の両方**のストリームを処理する」と書く（Extract detailed insights の節）
- **static（既定）**: 「1 FPS でコマを取り出してコンテキストに入れる。音声は 1Kbps（単一チャンネル）で処理。毎秒タイムスタンプを入れる」。注意書きとして「速いアクションは 1 FPS の抽出で細部を失うことがある」「動きの速い動画や素早い場面転換では細部を見落とすことがある」
- fps は `processing: {type: "static", fps: 0.5}` のように指定できる（例は 0.5 = 2 秒に 1 コマ）。`start_offset`・`end_offset` で切り出しもできる。どちらも static のときだけ
- **agentic**（opt-in）: 「モデルが動画のタイムラインを動的にたどり、プロンプトに応じて**文字起こしを先に見て**、必要な区間だけコマを読み、fps と解像度をその場で変える」。対応は Gemini 4 Argon・3.8 Flash・3.6 Flash・3.5 Flash Lite。長尺（5〜10 分超）向けで、公式は「長尺でトークンを最大 88% 減らし、品質は約 7% 上がる」と書く。5 分未満の短いクリップや全体の要約では static のほうがよい（推論とツール往復の分が増える）とも書く。リリースは 2026-09-01（changelog）
- `media_resolution`（Gemini 3 以後）: 1 コマに割くトークンの上限。動画は low と medium が同じ扱いで、**画面の細かい文字を読むなら high** と書く（media-resolution の推奨表: 「Video (Text-heavy): high、280 tokens/frame。密な文字（OCR）や小さな細部を読むときだけ」）

### 音声だけを入れる場合（audio）

- できること: 要約・質問への回答、文字起こしと翻訳、話者の分離、**音声と音楽の感情の検出**、タイムスタンプ付きの区間の分析
- 「非音声（鳥の声、サイレンなど）も理解する」。1 プロンプト 9.5 時間まで。「16 Kbps にダウンサンプル」「多チャンネルは 1 チャンネルに合成」
- 形式: WAV・MP3・AIFF・AAC・OGG・FLAC・M4A・Opus・WebM ほか

### トークンと費用

docs の中で値が揃っていない（下の Open Questions）。

- video-understanding: static で 1 コマ 66 トークン（low）／258（それ以外）、音声 32 トークン/秒、「既定で約 100 トークン/秒、高解像度で約 300 トークン/秒」
- media-resolution（Gemini 4・3）: 動画 1 コマ 70（low・medium）／280（high）、音声 25 トークン/秒
- tokens: 冒頭の一覧は「Video: 263 tokens per second」、下の表は「~100（既定）/ ~300（高）、60 秒で ~6,000 / ~18,000」
- 価格（Paid tier、100 万トークンあたり。入力はテキスト・画像・動画・音声で共通の行）:
  - `gemini-3.8-flash`: 入力 $0.75、出力（思考を含む）$3.75（2026-12-31 まで。2027-01-01 から $1.50 / $7.50）。2026-09-02 GA
  - `gemini-4-argon`: 入力 $2.00、出力 $10.00（2026-11-30 まで。2026-12-01 から $4.00 / $20.00）。**無料枠なし**。2026-10-13 GA
  - 3.8 Flash・3.6 Flash は無料枠あり（Free of charge）
- 例（このページでの試算）: 60 秒の動画を 3.8 Flash の高解像度（約 18,000 トークン）で入れると、入力は約 $0.014。出力 2,000 トークンで約 $0.0075

### 利用規約（無料枠と有料の違い）

- 無料枠（AI Studio・API の unpaid quota）: 「Google は送られた内容と生成された応答を、Google の製品・サービス・機械学習技術の提供・改善・開発に使う」「品質向上のため**人のレビュアーが入力と出力を読み、注釈し、処理することがある**」「**機密・個人情報を無料のサービスに送らないこと**」（Unpaid Services の節）
- 有料（請求先アカウントのある Cloud プロジェクト経由）: 「プロンプト（画像・動画などのファイルを含む）と応答を製品の改善に使わない」。違反の検出のため限られた期間ログを残す（Paid Services の節）
- EEA・スイス・英国では無料でも有料の扱い

## この wiki への含意

- **「モデルは聞けない・通しで見られない」への一番直接の手当て**: round 2 で作り手が書いた制約（[[web-opus2-opus-5-5-explainer-posts-on-x]]）は、Claude で作る側の話。Gemini は完成した mp4 を映像と音声のまま受け取り、時刻付きで答える、と公式が書いている。ただし既定は **1 秒 1 コマ**。西尾の promo（[[exp-polis-magi-op]]、[[exp-sutra-hype-editions]]）のように拍に合わせて 0.2〜0.5 秒で切り替わるものは、既定のままだと間のコマを見ない。fps を上げて渡す必要がある（上げたときの精度は公式に数字が無い）
- **閃光・1 コマだけの崩れは拾えない前提で使う**: 1 fps（指定しても数 fps）では 1 コマの閃光や「ポップ」は見えない。これは howseen のコマ間差分の検査（[[web-opus-howseen-claude-motion-design]]）や ffmpeg の機械検査の仕事のまま
- **音声は 1 チャンネル・低ビットレートに落とされる**: 「音量の釣り合い」「ステレオの定位」「BGM の音質」は見られない前提。読み・言い間違い・何を言っているかの確認向き。[[exp-galleria-tts-and-singing]] の「読みは最後は耳」を置き換えるものではなく、通し視聴の前のふるいとして使える可能性（未検証）
- **talk の画面の文字を読ませるなら `high`**: 西尾の talk（[[exp-qualia-video]]、[[exp-llm-wiki-explainer-series]]）は字幕・ラベルが多い。公式は文字の多い動画は high と書く
- **agentic は短い作品の批評には向かない**: 公式自身が 5 分未満は static を推す。さらに agentic は「文字起こしを先に見る」ので、映像だけで伝わるか（howseen の「音を消して要旨を言えるか」）を試す目的とは逆向き。批評に使うなら static で、音の有無を入れ替えて別々に聞くのが筋（下の手順）
- **未公開の作品を無料枠に入れない**: 規約上、無料枠の入力は人が読むことがある。発表前の動画・第三者の写る素材は有料枠でのみ（西尾が決めること）

## 着手の仕方（未検証。galleria で確かめる）

- **何ができるようになるか**: 書き出した mp4 を丸ごと見せて「何の動画か一文で」「どこで分からなくなるか（時刻付き）」「画面の文字と読み上げが食い違う所」を聞く批評役。型: talk（字幕・図の多い解説）が一番効く見込み。promo は fps を上げる前提。embed（流しっぱなし）は音を消した版で試す
- **機械**: どこでも（API）。galleria WSL で Python（uv）から呼ぶ想定。入れるもの: `google-genai`（interactions API を持つ版。版番号は未確認）
- **要: API キー・費用（西尾が決める）**。Google AI Studio のアカウント、未公開作品を入れるなら請求先付きの有料枠。費用の見込みは 1 分の動画 1 回で 1〜3 セント程度（上の試算、3.8 Flash）
- **成熟度**: 動画入力自体は Gemini 1.5 以来。agentic は 2026-09-01、3.8 Flash は 2026-09-02 GA、Gemini 4 Argon は 2026-10-13 GA。API の形が `generateContent` から `interactions` に移りつつある（docs の例はすべて `client.interactions.create`）
- **最小の手順**（WSL。公式の例を元にし、3 本に分ける所と問いの文はこのページの提案）:
  ```bash
  cd ~/video-tools-trial/critic && export GEMINI_API_KEY=...   # 西尾が用意
  # 音あり・音なし・音だけ の 3 本を作る（ffmpeg は WSL に既にある）
  ffmpeg -i in.mp4 -c copy full.mp4
  ffmpeg -i in.mp4 -an -c:v copy muted.mp4
  ffmpeg -i in.mp4 -vn -ac 1 -ar 16000 voice.wav
  uv run --with google-genai python critic_gemini.py muted.mp4 full.mp4 voice.wav
  ```
  `critic_gemini.py` の中身（公式の upload → ACTIVE を待つ → `interactions.create` の例そのまま。`processing` と `resolution` は公式の fps・media_resolution の節から。両方を同じ動画に付けられると公式は書くが、組み合わせの書き方は推測）:
  ```python
  from google import genai; import sys, time
  client = genai.Client()
  Q = "この動画が伝えたいことを日本語の一文で言ってください。次に、分かりにくい箇所を MM:SS 付きで最大 5 つ挙げてください。"
  for path in sys.argv[1:]:
      f = client.files.upload(file=path)
      while not f.state or f.state.name != "ACTIVE":
          time.sleep(5); f = client.files.get(name=f.name)
      part = {"type": "video" if path.endswith(".mp4") else "audio", "uri": f.uri, "mime_type": f.mime_type}
      if part["type"] == "video":
          part["processing"] = {"type": "static", "fps": 2}   # promo なら 4〜5 も試す
          part["resolution"] = "high"                          # 字幕・ラベルを読ませる
      r = client.interactions.create(model="gemini-3.8-flash", input=[part, {"type": "text", "text": Q}])
      print("==", path, "\n", r.output_text)
  ```
- **動いたと言える確かめ方**: 3 本それぞれについて一文の要旨と時刻付きの指摘が返る。`muted.mp4` の要旨が台本の狙いの一文と合うか、合わないなら `full.mp4` で合うか、を表にする。さらに、既知の誤りを 1 つ仕込んだ版（例: 字幕と読み上げの数字を変える）で、その時刻を指摘できるかを見る。`interaction.usage` のトークン数が上の目安（1 分で数千〜2 万）に収まるか
- **所要の見込み（推測）**: キーがあれば 30 分〜1 時間。既存の作品 3〜5 本で人の評価（西尾の一言）と並べるのに半日

## Open Questions

- docs 内の食い違い: 1 コマのトークン（66/258 と 70/280）、音声のトークン（32/秒と 25/秒）、1 秒あたり（263 と ~100/~300）、音声のビットレート（動画の節は 1Kbps、音声の節は 16Kbps）。どれが今の 3.8 Flash に当てはまるかは `usage` を見るしかない
- fps を上げたときの精度の変化は公式に数字が無い。Omni-Judge（[[web-means-critic-omni-judge-audiojudge]]）は fps と精度が単調でないと報告している
- 「Gemini が要旨を言えた」ことと「人が要旨をつかめた」ことの一致は、この docs からは分からない。動画の採点での人との一致は [[web-means-critic-videoscore]]・[[web-means-critic-video-bench-spotlight]]・[[web-means-critic-edupanel-paper2video]] を参照（どれも低〜中程度）
- 日本語の画面文字・日本語の音声での精度は docs に記述が無い
