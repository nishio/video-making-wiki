---
type: source
summary: OpenAI と Anthropic（Claude）の公式 docs（2026-11-09 時点）では、どちらの汎用モデルも動画ファイルを直接は受け取らない。映像はコマを画像で渡す（OpenAI は 1 リクエスト 1,500 枚まで、Claude は 600 枚まで）。音声は OpenAI では別のモデル（gpt-audio-1.5、Chat Completions）、Claude の API には音声入力の記述が無い。OpenAI は「日本語などラテン文字以外の画面文字は最適でない」と書く
video_types: [promo, talk, embed]
url: https://developers.openai.com/api/docs/guides/images-vision
author: OpenAI（API ドキュメント）／Anthropic（Claude Platform ドキュメント）
published: unknown（どちらもページに更新日の表示なし）
retrieved: 2026-11-09
sources:
  - https://developers.openai.com/api/docs/guides/images-vision.md
  - https://developers.openai.com/api/docs/models.md
  - https://developers.openai.com/api/docs/models/gpt-6-astra.md
  - https://developers.openai.com/api/docs/models/gpt-audio-1.5.md
  - https://developers.openai.com/api/docs/guides/audio.md
  - https://developers.openai.com/api/docs/guides/audio-chat-completions.md
  - https://developers.openai.com/api/docs/llms.txt （ガイドの索引）
  - https://github.com/openai/openai-cookbook/blob/main/examples/GPT_with_vision_for_video_understanding.ipynb
  - https://platform.claude.com/docs/en/build-with-claude/vision.md
  - https://platform.claude.com/docs/en/about-claude/pricing.md
  - https://platform.claude.com/llms.txt （docs の索引）
---

# OpenAI と Claude の API: 動画は入らず、コマと音声に分けて渡す（2026-11-09 時点）

## 何の文献か

OpenAI と Anthropic の公式 API ドキュメント（ガイド・モデルページ・価格）と、OpenAI の公式 cookbook の notebook 1 本。2026-11-09 に取得（両社とも URL に `.md` を付けると Markdown を返す）。数値はすべて「2026-11-09 時点の公式ページによる」。動画を入れられないことは「書いていない」から推したのではなく、モデルページの入力モダリティの欄と、docs の索引（llms.txt）で確かめた。

## 書いてあること

### OpenAI

- モデル一覧: 「最新の OpenAI のモデルはすべてテキストと画像の入力、テキストの出力に対応」。旗艦は GPT-6 Astra（`gpt-6-astra`）、ほかに GPT-6.1 Sol・GPT-6.1 Terra・GPT-6 Luna
- `gpt-6-astra` のモデルページ: 「Input modalities: text, image」「Output modalities: text」。コンテキスト 1,050,000、最大入力 922,000。価格は入力 $10・出力 $50（100 万トークン、272K 超の入力は 2 倍）。エンドポイント表の「Videos `v1/videos`」は Not supported（これは動画生成のエンドポイント）
- 画像入力の上限（images-vision）: PNG・JPEG・WEBP・**アニメーションでない** GIF、**1 リクエスト最大 1,500 枚**、ペイロード 512MB、1 枚 30,000 パッチまで。`detail` は `low`・`high`・`original`・`auto`。小さい文字・座標が要るなら `original`
- 限界の節（Limitations）: 「**Non-English: 日本語や韓国語のようなラテン文字以外のテキストを含む画像では最適に動かないことがある**」「Small text: 画像内の文字は拡大すること」「Spatial reasoning: 正確な空間の位置づけが要る課題は苦手」「Visual elements: 色や線種（実線・破線・点線）が変わるグラフや文字の理解に苦労することがある」
- 音声: 対話は GPT-Live（Realtime 系）を推す。既存のチャットに音声入力を足すなら **Chat Completions で `gpt-audio-1.5`**（入力: テキスト・音声、出力: テキスト・音声、128K、知識の締切 2024-09-30、音声入力 $32／100 万トークン）。「Responses API の docs は今のところテキストと画像の入力・テキスト出力を説明している。この音声の使い方には Chat Completions を使う」（audio-chat-completions）
- docs の索引（llms.txt）に、動画を理解させるガイドは無い（動画の語は生成の側だけ）
- 公式 cookbook「Processing and narrating a video with GPT's visual capabilities」: 「GPT-4.1-mini は動画を直接入力として取らないが、ビジョンと 1M のコンテキストで動画全体の静止コマを一度に説明させられる」。OpenCV で全コマを JPEG にし、**25 コマに 1 枚**を `input_image` で並べて渡す例（「全コマを送らなくても何が起きているか分かる」）。cookbook のモデルは古い（GPT-4.1-mini）

### Anthropic（Claude）

- Vision の docs: 「Vision（画像）はすべてのモデルで使える」。対応は Claude Fable 5.1・Mythos 5.1・Opus 5.5・Sonnet 5.5・Haiku 5.5 ほか
- 形式: JPEG・PNG・GIF・WebP。「**アニメーションには対応しない。最初のコマだけを使う**」
- 1 リクエストの枚数: **600 枚**（200K コンテキストのモデルは 100 枚）。claude.ai は 1 ターン 20 枚。1 枚の上限は 8000×8000 px。**21 枚以上を入れると 1 枚あたりの寸法の上限が厳しくなる**（「両辺を 3,000 px 以下にするか、20 枚以下に」）。サイズは API で 1 枚 10MB（base64）
- 解像度とトークン: 28×28 px のパッチ 1 つが 1 トークン。Claude 4.7 以後は「高解像度」で長辺 2,576 px・最大 4,784 トークン、それ以前は 1,568 px・1,568 トークン。**1920×1080 の画像は高解像度の階でそのまま 2,691 トークン**
- 費用の例（docs の本文）: 「Claude Opus 5.5 の $4／100 万トークン（高解像度の階）で、1000×1000 の画像は 1,000 枚あたり約 $5.18、4K の画像は約 $19.14」
- 限界: 「低画質・回転・200 px 未満の小さい画像では誤ることがある」「数は概数になる」
- docs の索引（llms.txt）に、音声・動画の入力の項は無い（vision と座標の 2 項のみ）
- データ: 「Anthropic はアップロードされた画像をモデルの学習に使わない」（FAQ）

## この wiki への含意

- **作り手（Claude Code）の側では「通しで見る」は API の上でもできない**: round 2 で作り手が書いた「モデルは聞けない・通しで見られない」（[[web-opus2-opus-5-5-explainer-posts-on-x]]）は、2026-11 の公式 docs でもそのまま正しい。Claude に見せられるのはコマ（静止画）だけで、GIF も最初の 1 コマしか見ない。音は渡せない
- **だから西尾の今のやり方（静止画・コンタクトシート）が Claude で取れる最大の形**: [[exp-html-capture-pipeline]] の `capture.mjs stills` と `sheet.png` は、docs の上限の内側でやっていたことになる。1920×1080 のシート 1 枚は約 2,700 トークン、Opus 5.5 で約 1 セント。20 枚までなら寸法の厳しい上限にかからない
- **コマを何枚・どう並べるかが批評の質を決める**: 1 秒 1 コマの 60 秒＝60 枚を個別に渡すと、Claude では 21 枚以上の制約にかかる。シートに並べる（1 枚に 30 コマ）と制約は避けられるが、1 コマが小さくなり字幕が読めなくなる（OpenAI も「小さい文字は拡大せよ」と書く）。talk は「字幕が読める大きさのコマを少なく」、promo は「小さくてよいので密に」と分けるのが筋（このページの推論、未検証）
- **日本語の画面文字は OpenAI 自身が弱いと書いている**: 西尾の動画は日本語の字幕・ラベルが多い（[[exp-qualia-video]]、[[exp-words-as-public-goods-video]]）。OpenAI で字幕の読み取りを批評させるのは公式の注意書きに反する使い方。Claude の docs には言語の注意書きは無い（できるとも書いていない）
- **音は別の道具で**: 読み・聞き違いの確認は、OpenAI なら `gpt-audio-1.5`、または文字起こし（Whisper 系）で台本と照合する。round 2 の作り手のやり方（TTS を文字起こしして読みを照合）と同じ。声の質・BGM の釣り合いを判定できるとは、どちらの docs も書いていない（音の判定の実測は [[web-means-critic-omni-judge-audiojudge]]）

## 着手の仕方（未検証。galleria で確かめる）

- **何ができるようになるか**: いまの Claude Code の制作ループの中で、コマから批評させる段を「作る者と別のエージェント」に分ける（howseen の §9c の形、[[web-opus-howseen-claude-motion-design]]）。API キーなしで、Claude Code の中だけで始められる。型: talk・embed（静止の多い画面）に向く。promo の動きの評価には向かない
- **機械**: galleria WSL（ffmpeg で切り出し）→ Claude Code（Mac か galleria の Claude Code）が画像を読む。入れるもの: なし（ffmpeg は既にある）。費用: Claude Code の枠の中。OpenAI を使うなら **要: API キー・費用（西尾が決める）**
- **成熟度**: 画像入力は両社とも安定（Claude は「stable」と表示）。動画入力は両社とも無い
- **最小の手順**（WSL。ffmpeg のフィルタは一般的な書き方で、このページの提案）:
  ```bash
  cd ~/video-tools-trial/critic
  # talk 用: 字幕が読める大きさで 2 秒に 1 枚、20 枚以下に抑える（60 秒なら 30 枚 → 3 秒に 1 枚にする）
  mkdir -p frames && ffmpeg -i in.mp4 -vf "fps=1/3,scale=1280:-1" frames/f_%03d.png
  # promo 用: 1 秒 4 コマを 1 枚のシートに（30 秒 → 120 コマ → 12x10）
  ffmpeg -i in.mp4 -vf "fps=4,scale=240:-1,tile=12x10" -frames:v 1 sheet_promo.png
  # 音は別に: 文字起こし用に 16kHz mono
  ffmpeg -i in.mp4 -vn -ac 1 -ar 16000 voice.wav
  ```
  Claude Code に「作り手と別のサブエージェントとして、frames/ の画像だけを見て、この動画が伝えたいことを一文で言え。言えなければ不合格と言え」と頼む（howseen の §9c の問いの形）
- **動いたと言える確かめ方**: `frames/` に 20 枚前後、`sheet_promo.png` が 1 枚できる。サブエージェントの一文の要旨を、台本の狙いの一文と並べて記録する。既知の失敗作（例: Gyazo v1 のタイトル、[[exp-gyazo-resumption-video]]）のコマで「意味がわからん」相当の指摘が出るかを見る
- **所要の見込み（推測）**: 1 時間

## Open Questions

- OpenAI の「日本語の画面文字は最適でない」が GPT-6 Astra でどの程度か。注意書きは古いモデルからの持ち越しの可能性もあるが、docs からは分からない
- Claude の高解像度の階（2,576 px）で日本語字幕がどこまで読めるか。docs に言語別の記述は無い
- コマの枚数・間隔と批評の質の関係は、両社の docs に無い。動画採点の研究ではコマの fps と精度の関係が単調でない（[[web-means-critic-omni-judge-audiojudge]]）
- 「別のエージェントがコマだけから要旨を言えた」ことと、人が要旨をつかめることの一致は未検証（howseen 自身も測っていない）
