---
type: source
summary: 長尺から縦型のショートを自動で切り出す商用サービス OpusClip の、2026-11-09 時点の公式の価格・ヘルプ・利用規約・プライバシーポリシー。切り抜きの選び方は Virality Score（0〜99）で、公式は Hook・Flow・Value・Trend の 4 観点で AI が評価すると書くが重みや式は出していない。日本語は「BETA」扱い。無料は 60 credits/月（1 credit＝処理 1 分）・透かし・3 日で書き出せなくなる。個人ユーザーのデータは AI の改善に「使うことがある」とヘルプが書く
video_types: [promo, talk]
url: https://www.opus.pro/pricing
author: OpusClip（Opus Pro）
published: 価格ページは取得日の版（「OpusClip 4.0」の告知あり）。利用規約・プライバシーポリシーは 2025-11-17 発効。ヘルプ記事は日付の表示なし
retrieved: 2026-11-09
sources:
  - https://www.opus.pro/pricing
  - https://help.opus.pro/docs/article/virality-score.md
  - https://help.opus.pro/docs/article/9947095-clip-anything.md
  - https://help.opus.pro/docs/article/clipanything-qa-2 、clipanything-qa-10
  - https://help.opus.pro/docs/article/video-languages-supported.md
  - https://help.opus.pro/docs/article/upload-own-srt.md
  - https://help.opus.pro/docs/article/video-length.md
  - https://help.opus.pro/docs/article/how-many-clips.md
  - https://help.opus.pro/docs/article/speech-cleanup.md
  - https://help.opus.pro/docs/article/import-to-adobe-premiere.md
  - https://help.opus.pro/docs/article/opusclip-data-training.md
  - https://help.opus.pro/docs/article/opusclip-data-security-standards.md
  - https://www.opus.pro/terms-of-service（Effective date: November 17, 2025）
  - https://www.opus.pro/privacy-policy（Effective as of November 17th, 2025）
---

# OpusClip — Virality Score で長尺から切り抜きを選ぶ商用サービス

## 何の文献か

- 商用サービスの公式の価格ページ、ヘルプセンター（Mintlify、`.md` で本文を取得）、利用規約、プライバシーポリシー。自社の宣伝の文書で、切り抜きの選択の精度・Virality Score の当たり方の測定は公開されていない
- 価格ページの「Create & Grow Faster Calculator」は、ページの JavaScript に `avgIncreaseInWatchTimeByOpus = 1.41`、「on average they spend 40 minutes on a short video」（「We talked with hundreds of creators」）などの固定の係数を持つ計算で、測定値ではない

## 書いてあること

### 切り抜きの選び方（Virality Score、ClipAnything）

- Virality Score は 0〜99、「higher scores suggesting a greater chance of engagement and shares on social media」。結果は既定でスコアの高い順に並ぶ。Starter と Pro だけが見られ、無料では見えない（virality-score）
- 公式の説明する観点（原文の見出し）:
  - **Hook**:「Does the introduction grab attention and directly relate to the main topic of the video?」
  - **Flow**:「Does the video flow logically from one part to the next, with a satisfying conclusion?」
  - **Value**:「Does the video offer value, resonate emotionally, and create a personal connection with the audience?」
  - **Trend**:「Is the video aligned with current trends and audience interests?」
  - 加えて ClipAnything ではプロンプトへの合致も見る。**重み・式・検証の数字は書いていない**
- モデルは 2 つ（clipanything-qa-2）: **ClipBasic** は「Can only clip talking-head videos well」「Relies solely on the transcript」、プロンプトは動画で話された語だけ。**ClipAnything** は映像（物・色・動作・画面の文字）・音（話者の特定、笑い・歓声などの音）・感情を見て、「narrative library in collaboration with award-winning producers」を当てる、と書く。ClipAnything は「currently in beta」で、音のない動画・動きの少ない静的な場面では結果を返さないことがある（clipanything-qa-10）
- 何本出るか（how-many-clips）: 0–3 分で 1–2 本、10–30 分で 5–21 本、60–120 分で 32–42 本、120 分超で 42–55 本
- 入力: ローカルの動画は 1 本 10GB まで（価格表）、長さは 10 時間まで（video-length）。切り抜く時間帯・長さ（0–1m、1–3m、3–5m、5–10m、10–15m）を指定できる（価格表）

### 編集で任せられること（公式の機能の記述）

- **Speech Cleanup**（speech-cleanup）:「detects 90%+ of fillers and pauses — you see exactly what gets removed before anything is deleted. You're in control, not the AI.」。フィラー（um・uh・you know・どもり）、間（既定 0.5 秒、スライダーで変更）、**言い直し（Remove Bad Takes:「retakes, restarts, self-corrections, and phrase repetitions」）**を検出し、文字起こしの上で示して、人が選んでから消す。「Nothing gets cut without your approval」。90% の根拠は書かれていない
- リフレーム（9:16・1:1・16:9、被写体の追跡）、アニメーション字幕、AI B-roll、Viral Hook、モーショングラフィックス、吹き替え、音声の強調（価格表の機能一覧）
- **自分の SRT を上げられる**（upload-own-srt）:「your SRT file will be used for us to generate captions instead of the transcript we normally create」。標準の SRT の書式の検査（番号の連番、`HH:MM:SS,MS`）がある
- **Premiere への書き出し（Pro）**（import-to-adobe-premiere）: 元の動画、`.xml`（字幕・リフレーム・B-roll 入り）、`.srt` の 3 つ。OpusClip の字幕は「exported as overlays and cannot be edited in Premiere Pro」なので、Premiere で字幕を直すなら `.srt` を読む。前後を延ばせる余白は、各区間で前後 30 秒（中の区間は 10 秒）。複数の切り抜きの一括書き出しはできない
- API・MCP もある（Business は API、Pro は「Limited API Access」、価格表）

### 日本語の対応

- 「We support over 25 languages」の表に **Japanese (ja) があり、「\*」付き = BETA**。「\* means the language is still in BETA version. You may encounter some inaccurate emojis or highlighted keywords」（video-languages-supported）。BETA が文字起こし・切り抜きの選択にどう効くかは書かれていない。価格表は「AI animated captions in 20+ languages」

### 費用（2026-11-09 時点の価格ページ）

| プラン | 価格 | credit | 主な違い |
|---|---|---|---|
| Free | $0 | 60/月 | 1080p まで、透かしあり、編集なし、「After 3 days, the clips will no longer be exportable」、Virality Score は見えない |
| Starter | $15/月（月払いのみ） | 150/月 | Virality Score、透かしなし、フィラー・無音の除去 |
| Pro | $29/月（年払いは $14.5/月＝$174/年、3,600 credits/12 か月） | — | 2 席、Premiere・Resolve への書き出し、AI B-roll、複数の縦横比、限定 API。未使用の credit は 2 か月繰り越し |
| Business | 個別 | — | API、MSA、専用ストレージ |

- 「1 credit = 1 minute of video processing」（価格表のツールチップ）。Pro の年払いは「1 credit per minute of video processing. AI features vary.」
- 無料・試用は「No credit card required」

### 素材の扱い・AI 学習・権利（条文）

- 利用規約（2025-11-17 発効）「Rights You Grant」: すべての投稿について「translate, modify (for technical purposes ...) and reproduce」のライセンスを OpusClip に与える。「This is a license only – your ownership in User Submissions is not affected」。自分だけが見られる投稿（Personal User Submission）は、自分に見せ、サービスを提供する目的に限る。**公開した投稿（Public User Submission）は「OpusClip' marketing and promotional purposes」にも使える**。ライセンスは「royalty-free, perpetual, sublicensable, irrevocable, and worldwide」
- 投稿してはいけないもの: 第三者の著作権・肖像権（Publicity Rights）・プライバシーを侵すもの、など
- 禁止: 「Uses output from the Services to develop models that compete with OpusClip」
- **AI 学習**（opusclip-data-training）:「For individual (non-enterprise) users, we **may** use your data to improve our AI models ... any data used for training is carefully selected and stripped of personally identifiable information」。「For enterprise customers, we **do not** use your data to train AI models」
- SOC 2 Type II（opusclip-data-security-standards）

## この wiki への含意

- **何を AI に任せられるか**（公式がそう書いているもの）: 長尺から候補の区間を選び、スコアで並べる。縦へのリフレーム、字幕、フィラー・間・言い直しの検出。**検出の精度（90%+）と Virality Score の当たり方は公式の主張で、測定は公開されていない**
- **何が人の判断として残るか**（公式）: Speech Cleanup は「Nothing gets cut without your approval」と、消す前に人が選ぶ作り。Premiere 書き出しは「Precise Editing」「Trim & Extend」を人がする前提で前後に余白を付ける。候補を選んで投稿するのも人
- **[[exp-shortmovie-draft-generator]] と照らす**:
  - **一致**: 西尾が回した道具のプロンプトは「冒頭 2 秒」と「最後の結論（オチ）」を別の欄で書かせた。OpusClip の Hook（冒頭が注意を掴み、主題とつながるか）と Flow（満足のいく結末）はその 2 つにほぼ当たる
  - **一致**: 道具 1 は「タイムスタンプは字幕データを正」とした。OpusClip は自分の SRT を上げると文字起こしの代わりに使う。字幕を人が正せる入口がある点は同じ向き（切る時刻にも SRT を使うかは書かれていない）
  - **食い違い**: 西尾の道具は 5 案を人が選ぶ下書き。OpusClip は数十本を出してスコアで並べる。尺は西尾の道具が 90 秒以内・理想 60 秒、OpusClip は 0–1 分から 10–15 分まで選べる
  - **食い違い（考え方）**: OpusClip は Trend（流行との合致）を観点に入れる。西尾の道具のプロンプトにはない
  - 西尾の道具 2 の「話している内容に肯定的に」に当たる指定は、OpusClip の公式文書には見当たらなかった。他人の講演を切り抜くときに文脈を変えない注意（[[web-rights-x-linkedin-niconico-eu-ai-act]] の X の「字幕の変更で意味を変える」）は人に残る
- **[[exp-thinklet-reading-demo-video]] と照らす**: 西尾は Premiere で手で編集した。OpusClip の Pro は Premiere の XML を出すので、「切り抜きの候補とリフレームは OpusClip、仕上げは Premiere」の分担は公式の想定どおり。ただし OpusClip の字幕はオーバーレイで Premiere では直せない
- **日本語は BETA**。日本語の講演では、自分で台本を正にした SRT（[[web-check-subs-whisperx-stable-ts-faster-whisper]]）を上げる使い方が、公式の機能の範囲で一番確かそう（推測）
- **会社・第三者の素材を上げる前に**: 個人プランでは学習に「使うことがある」。公開の切り抜きは宣伝に使われうる。上げてよい素材かは西尾が決めること

## 着手の仕方（未検証。galleria で確かめる）

- **表現できるようになること**: 1 本の講演・LT の録画から、縦型の切り抜きの候補を数十本、スコア順で得る。どこが切り抜きに向くかの、自分以外の見立て。効く型: promo（SNS の短尺）、talk の告知
- **機械**: どこでも（ブラウザ）。galleria Windows のブラウザで、galleria の録画を上げる
- **費用・アカウント**: **要: アカウント**（西尾が決める）。無料は 60 分/月、透かし、3 日。Virality Score を見るには Starter（$15/月）以上。Premiere の XML は Pro（$29/月）
- **利用条件の要点**: 個人プランは AI の改善に使われうる。公開した投稿は宣伝に使われうる。第三者の権利を侵す素材は不可
- **最小の手順**: (1) 権利のある自分の録画（どれを使うかは西尾が決める）を 1 本選ぶ → (2) 無料で上げ、ClipBasic と ClipAnything の両方で回す（無料で選べるかは未確認）→ (3) 同じ録画を shortmovie-draft-generator2 にも通し、5 案の時刻と OpusClip の上位 5 本の時刻を表に並べる
- **動いたと言える確かめ方**: 切り抜きが数本以上出て、各切り抜きの開始・終了の時刻が分かる。日本語の字幕の誤りの数（1 本 60 秒あたり何か所）を数える。西尾の道具の 5 案と、区間が重なる本数を数える（重なりが多ければ選ぶ基準が近い）
- **所要の見込み（推測）**: アカウント作成と 1 本の処理で 30 分、比べる表で 30 分

## Open Questions

- Virality Score が実際の再生数とどれだけ相関するか。公式は測定を出していない。[[web-edit-auto-autoclip-what-drives-views-2026]] は、公開の 158 本の観察から「何が映っているか」と「どこから始まるか」が編集より効くと書く。Trend の観点がそれと合うかは分からない
- 日本語の BETA が、字幕の誤り以外（どこを選ぶか）にどう効くか
- 自分の SRT を上げたとき、切る時刻もその SRT に合わせるか（字幕にだけ使うのか）
- 無料プランで ClipAnything を選べるか。価格表からは読み取れなかった
- Speech Cleanup の「90%+」は英語での数字か。日本語のフィラー（えー、あのー）を検出するか
