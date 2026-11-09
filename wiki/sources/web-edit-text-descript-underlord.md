---
type: source
summary: Descript の公式ヘルプ・料金・利用規約（2026-11-09 時点）。文字起こしを消すと映像が切れる編集に、フィラー削除・間の短縮・Edit for Clarity・切り抜き（Create clips）・話者中心の自動リフレーム、さらにエージェントの Underlord（モデルを選べる。Claude Opus 5.5 も並ぶ）と API・MCP を載せている。ただし文字起こしはラテン文字の 26 言語だけで「日本語は未対応」と公式に書いており、フィラー検出と台本の取り込みも英語だけ。規約は素材に永続・取消不能のライセンスを取り、モデル学習は opt-out 制
video_types: [talk, promo]
url: https://help.descript.com/
author: Descript, Inc.（ヘルプセンター・料金ページ・Terms of Service）
published: ヘルプ各ページは随時更新（言語のページの lastModified 2026-08-20、ヘルプ全体の索引 2026-11-06）。Terms は Last Updated 2025-02-25
retrieved: 2026-11-09
sources:
  - https://www.descript.com/pricing
  - https://help.descript.com/script-editing/supported-transcription-languages
  - https://help.descript.com/getting-started/underlord-beta-your-ai-co-editor-in-descript.md
  - https://help.descript.com/script-editing/edit-for-clarity.md
  - https://help.descript.com/script-editing/filler-words.md
  - https://help.descript.com/script-editing/shorten-word-gaps.md
  - https://help.descript.com/script-editing/import-transcript.md
  - https://help.descript.com/repurpose/create-clips-from-your-content.md
  - https://help.descript.com/visuals/center-active-speaker.md
  - https://help.descript.com/api-and-mcp/api.md
  - https://help.descript.com/api-and-mcp/mcp.md
  - https://help.descript.com/api-and-mcp/claude-motion.md
  - https://help.descript.com/account-and-app-settings/data-privacy.md
  - https://www.descript.com/terms
---

# Descript — 文字起こしで編集し、Underlord に編集させる

## 何の文献か

- Descript 社の一次資料: ヘルプセンター（Mintlify の docs。`/llms.txt` で索引が取れ、各ページの `.md` を直接読めた）、料金ページ、利用規約（Terms of Service、Last Updated 2025-02-25）。宣伝を兼ねる文書で、機能の効果を測った数字は無い
- 2026-11-09 に curl で本文を取得して読んだ。実機では試していない

## 書いてあること

### 文字起こしで編集する（Descript の土台）

- ヘルプの見出しどおり「Edit your recording by editing the transcript. Delete a word, or every um, and the footage goes with it」（ヘルプのトップ）。料金表の Enterprise の項も「Text-based editing: Edit video by editing a doc」と書く
- 消し方は 2 通り: 文字と音を消す「Delete」と、打ち消し線で残して音だけ消す「Ignore」（フィラーのページ）

### AI に任せられるとヘルプが書いていること（AI Tools パネル）

| 機能 | 公式の記述（要点） | 言語の条件 |
|---|---|---|
| Remove filler words | 「um」「uh」「you know」を検出し、Delete／Delete and replace with gap／Ignore／Remove from transcript を 1 件ずつ選べる。「Avoid harsh cuts」を入れると、前後の語を切らずに消せないものは飛ばす | 「This feature currently detects filler words in **English** transcripts only」 |
| Shorten word gaps | 「more than／between」で間の長さの条件を決め、目標の長さ（例 200ms）に詰める。1 件ずつ「Shorten」か「Shorten all」 | 記載なし |
| Edit for Clarity | 「cleans up pacing, tighten delivery, and remove unnecessary or off-topic content」。強さは Low／Medium／Heavy。消した語は Ignore として残り、戻せる。「Reword for flow」を入れると AI 音声で言い換えを生成（青で表示） | 記載なし |
| Remove retakes | 「Cut all but your best takes」（料金表の説明） | 記載なし |
| Create clips | 長尺から 1〜20 本、10 秒〜5 分の切り抜きを作る。縦・正方形のレイアウトと、選ぶ観点（topic, goal, criteria）を指定できる。「the most engaging moments it identifies」を選ぶと書く。1 分未満の素材では作れないことがある | 記載なし |
| Center active speaker（Beta） | 広角で複数人が 1 本の映像に映る素材で、話している人を中心に自動でリフレーム。マルチトラックでは不可 | — |
| Automatic Multicam・Quick Design・Generate image/video・Eye Contact・Studio Sound など | 料金表に列挙（Quick Design は「scenes, layouts and B-roll」を自動で整える） | — |

- これらの多くは「AI Credits」を使う（各ページの Usage note）

### Underlord（エージェント。Beta）

- プロジェクトの右サイドバーのアイコンから会話で指示する。例として、字幕の様式指定、「5 本の 1 分以内の切り抜きに分けて」「60〜90 秒の SNS 用の切り抜きを探して縦にして」、「強調の瞬間にズーム」「3〜6 秒ごとにズームカット」、字幕の日本語への翻訳、スライドと文書から 1 分の動画、Web 検索による事実確認を挙げる
- **モデルを選べる**: Auto のほか GPT 6 Luna、GPT 6.1 Sol、Claude Sonnet 5.5、Claude Opus 5.5、Gemini 4 Argon など（2026-11-09 時点の一覧。上位モデルは有料プラン）。同じ指示でもクレジット消費が回ごとに違う（「non-deterministic」）と書く
- 限界の記述が具体的: 「Underlord might overpromise, make incorrect assumptions, or follow you into workflows it's not equipped to complete」。「works best when treated like a fast, talented collaborator who still needs clear instructions, context, and regular check-ins」。URL を渡しても**そのページ自体は読めない**（検索結果を見るだけ）ので、本文を貼れと書く
- 繰り返す指示は skill として保存できる（旧 prompt templates は skill に移行中）

### API・MCP（外から編集させる）

- **API**: トークンは Drive ごと。メディアの取り込み（URL かローカルのアップロード。取り込むと自動で文字起こし）、Underlord の編集の実行、プロジェクトの検索、Web リンクへの公開、文字起こしの書き出し（text・Markdown・HTML・RTF・DOCX・SRT）、ジョブの追跡。CLI もある。メディア時間・クレジットが尽きると 402
- **MCP**: Claude・ChatGPT・Cursor、または「Claude Code and other MCP-compatible assistants take the server URL」。Descript のログインで認証し、Drive を 1 つ選ぶ
- **共通の制限**: 「No rendered file download without publishing」。書き出した mp4 を手元に落とすには Web リンクに公開して署名付き URL を取るか、アプリで書き出す。YouTube の URL は取り込めない。ジョブの履歴は 30 日
- Claude Motion のアニメを Claude の Share → Export → Send to Descript で送れる。届くのは平たい動画で、文字・色・タイミングは Descript では直せない（Claude で直して送り直す）

### 日本語の対応

- **文字起こしは日本語に未対応**: 「Currently, supported transcription languages are limited to those using the Latin alphabet. Languages such as Chinese, Japanese, or Russian are not yet supported」（Supported transcription languages、lastModified 2026-08-20）。対応は 26 言語（英語・欧州語のほか Hindi・Greek は Beta）。料金表の「25 languages」の列挙とも数が少し違う
- 自分の文字起こしを取り込む「Import transcript」も「**English only**」
- 日本語が出てくるのは出力側だけ: 字幕の翻訳（61 言語に Japanese）、吹き替え（30 言語に Japanese）、AI 話者（14 言語に Japanese）

### 料金（2026-11-09 の公式の料金ページ、1 人あたり月額。年払い／月払い）

| プラン | 年払い | 月払い | メディア時間／月 | AI クレジット／月 | 書き出し |
|---|---|---|---|---|---|
| Free | $0 | $0 | 60 分 | 100（一度だけ） | 720p |
| Hobbyist | $16 | $24 | 10 時間 | 400 | 1080p、透かしなし |
| Creator | $24 | $35 | 30 時間 | 800 | 4K |
| Business | $50 | $65 | 40 時間 | 1,500 | 4K |
| Enterprise | 要相談 | — | 相談 | 相談 | 「opt-out of training, custom retention」 |

Free では Underlord・フィラー削除などは「Limited」。

### 利用条件（Terms of Service、Last Updated 2025-02-25 の条文）

- 5.1: 利用の許諾は「for your own personal or internal business use」
- **8.2（素材のライセンス）**: 「We claim no ownership rights in your User Content」としたうえで、「a perpetual, irrevocable, nonexclusive, royalty-free, sublicensable, fully paid, worldwide license to create derivative works from, access, reproduce, distribute, process, publish, display, perform, adapt, modify, analyze, and otherwise use the User Content ... to provide, maintain, and improve the Descript Service」。ただし Project の利用は 9 条の制限と守秘義務に従う
- **8.4（生成物）**: Input も Output も User Content で、「as between you and Descript, you own all right, title, and interest in and to any Input and Output, to the extent protectable under applicable law」。生成物は他の利用者と同じになりうる、著作権の状態は不明でありうる、と書く
- **8.4(e)（学習）**: Descript は Input・Output を「to train, improve, and develop its models and technologies (unless you have opted out of such use)」に使える。外部の AI 提供者（Third-Party Providers）には学習に使わせない契約がある
- 9.2: Project とその中の音声・動画・文書を「Confidential Information」として扱う
- ヘルプ「Account data and privacy」: 「Current AI models in production use no Descript user data」、研究開発のモデルは**データ共有に opt-in した人のデータだけ**。設定 → Profile → Share data with Descript で切れる。Enterprise は既定で無効。規約の「opt-out しない限り使える」と、ヘルプの「opt-in の人だけ」は書き方が違う（Open Questions）

## この wiki への含意

- **日本語の講演・画面収録には、2026-11 時点では土台の文字起こしが使えない**。西尾の素材（日本語の講演・デモ）で Descript の「消すと切れる」編集・フィラー削除・Edit for Clarity・Create clips を使う根拠は無い。英語の素材か、英語の字幕翻訳・吹き替えを作るときに限られる
- 切り抜きの選択（Create clips）は、[[exp-shortmovie-draft-generator]] が LLM に企画 5 案を作らせ人が選んだのと同じ仕事を製品の中でやる。ただし Descript の基準は「most engaging moments」で、shortmovie-draft-generator が持っていた「冒頭 2 秒」「肯定的な内容に」「タイムスタンプは字幕データを正に」のような決まりを外から渡せるのは自由記述の観点の欄だけ
- **Edit for Clarity の「Reword for flow」は話者の声を AI 音声で言い換える**。発信物で話者の発言を合成で書き換えることになり、grasp-nishio の「設計意図を検証済みの効果として書かない」以前に、本人の発言の改変の問題がある（推測。公式は「AI-generated edits appear in blue」と見分けられるようにしている）
- MCP で Claude Code から編集させられる設計は、この wiki の「AI が台本とコードで回す」方式（[[exp-html-capture-pipeline]]）と相性がよい。ただし書き出しの mp4 は公開しないと手元に来ないので、ffprobe などの検査（[[web-check-loudness-ffmpeg-loudnorm-ebur128]]）に回す前に公開の手順が挟まる
- Claude Motion → Descript の連携は、コードで描いたアニメ（[[web-opus-anthropic-claude-motion]]）に声・画面収録・字幕を足す仕上げ場として使える、と Descript は書いている。届くのは平たい動画なので、文字の誤りは Claude 側で直す

## 何を AI に任せられるか／何が人に残るか

- **任せられる（公式がそう書いている）**: 英語のフィラー削除、間の短縮、冗長・脱線の削除（Edit for Clarity）、取り直しの選択（Remove retakes）、切り抜きの選択と縦化（Create clips）、話者の中心化、字幕の付与と様式、翻訳・吹き替え、会話による一連の編集（Underlord）
- **人に残る（公式がそう書いている）**: Edit for Clarity の結果の確認（Ignore として残るものを見て Remove／Discard を選ぶ）、フィラーの 1 件ずつの判断、Underlord の「regular check-ins」と出来の確認、生成物の適否・権利の確認（規約 8.4(d)「you are solely responsible for vetting」）
- 実例で確かめたものはこの wiki に無い

## 着手の仕方（未検証。galleria で確かめる）

- **何が表現できるようになるか**: 英語の収録素材（英語の講演・英語ナレーションのデモ）を、文字起こしを消す操作と Underlord への会話で荒編集し、切り抜きと字幕を作る。日本語素材の編集には使えない（公式の記述）。日本語の動画の英語字幕・英語吹き替え版を作る用途は残る。効く型: talk（英語版）、promo（切り抜き）
- **機械**: galleria Windows か Mac のデスクトップアプリ（ヘルプ「Download and install Descript」は macOS と Windows）、または Web 版。MCP は Claude Code から（どの機械でも。サーバーの URL は Descript の Settings → Descript MCP）
- **入れるもの・費用・アカウント**: **要: アカウント**。Free（60 分／月、720p、AI は Limited）で試せる。業務で使うなら Hobbyist $16〜（年払い）。**API トークン・MCP の接続は西尾が決める**。会社の素材を上げるなら、データ共有の設定（Profile → Share data with Descript）を切るかを先に決める
- **成熟度**: Underlord は「Beta」と明記。ヘルプは 2026-11-06 にも更新されている
- **最小の手順（GUI。推測で補った所あり）**:
  1. アプリでサインイン → App settings → Profile → 「Share data with Descript」を Allowed から外す
  2. 新規プロジェクトに英語の短い収録（1〜3 分）を取り込む（取り込むと自動で文字起こし。言語は English (US) を選ぶ）
  3. 右サイドバー AI Tools → Sound Good → Remove filler words → 一覧を見て Delete all（Avoid harsh cuts を入れる）
  4. 同じく Edit for Clarity → Edit intensity を Low → Submit（Reword for flow は切る）→ 打ち消し線の箇所を見て「Copy edits to a new composition」
  5. Underlord に「Find me one clip between 30 and 60 seconds and reformat it for vertical」と頼む
  6. Export で mp4 を書き出す
- **動いたと言える確かめ方**: 手順 3 の後、文字起こしに残る「um」「uh」の数が 0 になり、書き出しの尺が元より短い（ffprobe の duration で比べる）。手順 4 で新しい composition ができ、Ignore の箇所が残っている。手順 5 で 9:16 の composition ができる（書き出しを ffprobe して width < height）。日本語の素材を入れたら文字起こしが成り立たないこと（言語の選択肢に Japanese が無いこと）も一度確かめる
- **所要の見込み（推測）**: 登録と導入 20 分、1 本の試し 30〜60 分

## Open Questions

- 規約 8.4(e) は「opt-out しない限り」学習に使えると書き、ヘルプは「研究開発には opt-in した人だけ」「本番のモデルは利用者データを使っていない」と書く。既定がどちらか（初回の onboarding で聞かれるとヘルプは書く）を、アカウント作成時の画面で確かめる
- 規約の Last Updated は 2025-02-25 で、MCP・API・Underlord のモデル選択（2026）より古い。API・MCP 経由の利用に別の条件があるかは読んでいない（「Descript API」の開発者向けの条件は未読）
- 日本語の文字起こしの対応予定は「we'd like to add in the future」とあるだけで時期は書かれていない
- Edit for Clarity・Remove retakes・Create clips がどの言語で動くかはヘルプに書かれていない（文字起こしが前提なので、実質は文字起こしの 26 言語と推測）
