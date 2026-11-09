---
type: source
summary: OpusClip 以外の切り抜きの商用サービス 3 つの、2026-11-09 時点の公式の価格・ヘルプ・規約。Klap は切り抜き 1 本単位の課金（年払い $14.50/月で 100 本〜）で、書き起こしは WhisperX、選択は OpenRouter・OpenAI の LLM に書き起こしを渡して行う、とプライバシーポリシーに書く。Vizard は日本語の書き起こしに対応と明記し、顧客のデータで学習しないと書くが、価格の数字はページが JavaScript で描くため取れなかった。Munch は「Munch Studio」に変わり、動画の再利用は SNS 運用の一機能になった。日本語向けの国産の切り抜き専用サービスは、公式ページで確かめられるものが見つからなかった
video_types: [promo, talk]
url: https://klap.app/pricing
author: ZIGG SAS（Klap）／Vizard, Corp.（Vizard）／Munch Studio
published: Klap の価格は「last updated on November 4, 2026」、Klap のプライバシーポリシー 2026-10-01、利用規約 2024-07-25。Vizard のヘルプ記事は 2024-02〜2026-02、利用規約 2022-10-31。Munch は取得日の版
retrieved: 2026-11-09
sources:
  - https://klap.app/pricing
  - https://klap.app/terms-of-services（Last updated: 25/07/2024）
  - https://klap.app/privacy-policy（Last updated: 01/10/2026）
  - https://vizard.ai/pricing
  - https://help.vizard.ai/en/articles/8768631-how-does-vizard-work
  - https://help.vizard.ai/en/articles/8767561-what-languages-are-supported（2026-02-04）
  - https://help.vizard.ai/en/articles/8767564-what-types-of-video-content-work-best-with-vizard
  - https://help.vizard.ai/en/articles/9629134-vizard-and-data-safety（2024-09-07）
  - https://help.vizard.ai/en/articles/9905409-what-is-spark-1-0（2025-08-15）
  - https://vizard.ai/user-service.html（Last updated: Oct 31, 2022）
  - https://www.getmunch.com/pricing
---

# Vizard・Klap・Munch — OpusClip 以外の切り抜きサービス

## 何の文献か

- 3 社の公式の価格ページ・ヘルプ・規約。どれも宣伝の文書で、切り抜きの選択の精度の測定はない
- OpusClip は [[web-edit-auto-opusclip]] に分けた

## 書いてあること

### Klap（ZIGG SAS。利用規約の準拠法はフランス法）

- **課金は切り抜き 1 本単位**:「Only pay for clips you generate」。Basic 100 本/月・Pro 300 本・Pro+ 1,000 本。月払い $29・$79・$189、年払い $174・$474・$1,134（月 $14.50・$39.50・$94.50）。「The length of your source video doesn't use up your plan, and a video can run up to 3 hours」。価格は「last updated on November 4, 2026」（pricing の FAQ）
- 無料: 「try Klap free on 1 video」、プレビューと編集まで。「Downloading and posting clips needs a paid plan」
- 全プランに「AI clipping, with a virality score, active-speaker reframing and animated captions」「99+ languages」（pricing の FAQ）。日本語を名指しした記述は価格ページにない
- API は別料金: 「$0.44 per input video, $0.32 per short and $0.48 per export」。MCP サーバーもある
- **中で何を使っているか**（プライバシーポリシー 2026-10-01、第 10 節、原文）:「RunPod hosts the open-source models we use to transcribe your videos (WhisperX) and to follow the people in them; OpenRouter, the model providers it routes to, and OpenAI receive your transcripts and clipping instructions to find the best moments, score them and write titles, emojis and translations; Google (Gemini) receives the video when it has no speech to transcribe.」。**書き起こし → LLM が書き起こしから選んで点を付ける**、話のない動画だけ Gemini が映像を見る
- 同じ節:「contractors who help us improve Klap, for example by reviewing samples of video frames to improve our reframing」。動画のコマが外部の委託先に見られうる
- 第 14 節:「Currently, while users are informed about AI processing, explicit consent before data sharing with third-party AI models is not obtained」（同意の仕組みは準備中と書く）
- 保持: 「Content Data: until you delete it or your account, plus up to 30 days in our backups」
- 利用規約（2024-07-25）の User Content は「You are responsible for ensuring that you have the necessary rights for any content you submit」の 1 文だけで、Klap に与えるライセンスの条文は見当たらなかった。準拠法はフランス法

### Vizard（Vizard, Corp.）

- 仕組み（how-does-vizard-work、2024-02-05）:「Vizard automatically detects the most important moments in your longer video, turns them into engaging short clips, adds trendy captions」。テキストで編集する画面で人が選び直せる
- 向く素材（2024-02-19）:「Vizard works best with speech-based videos as we use text to attract highlights from videos」。ポッドキャスト・ウェビナー・教育・インタビュー・講演。「We recommend uploading videos longer than 15 minutes」。BGM・不明瞭な発話・訛り・音質の悪さは書き起こしの質に響く
- **日本語**: 書き起こしの対応言語 40 の中に「Japanese (日本語)」（what-languages-are-supported、2026-02-04）。BETA の注記はない
- Spark 1.0（2025-08-15）: 「next-gen video understanding large language model」。映像・音・感情を見て、会話の少ない動画も切れる、プロンプトで指定できる、と書く。β で、1 プロジェクトにプロンプト 10 回まで、再プロンプトは credit を使わない
- 価格（pricing）: 無料は 60 credits/月、720p、3 日の保存。「1 credit = 1 minute of video」「Every minute of video you upload will cost 1 credit」。Creator（透かしなし、4K、100GB）と Business（共有ワークスペース、ブランドキット）は**金額がページの JavaScript で描かれ、取得した HTML では「$0」の置き場所だけだった**。OpenShorts の README は「Vizard $14.50/mo billed yearly ($29 monthly)」（2026-10 確認）と書くが、競合の作った比較表
- **データと学習**（vizard-and-data-safety、2024-09-07）: 「We have not used, nor do we plan to use, customer data to train our models」。顔認識・音声認識・画面共有の分割のモデルは「trained exclusively on publicly available data from YouTube, which is copyright-free」と書く（YouTube の公開データが著作権フリーだという主張は、この会社の言い分）。「we also utilize ChatGPT」。保存は AWS カリフォルニア、無料ユーザーの動画はアップロードから 7 日で自動削除（価格ページの「3-day storage」と日数が食い違う）
- 利用規約（2022-10-31）「User content」: 「nonexclusive, perpetual, irrevocable, royalty-free, worldwide, transferable, sub-licensable license to access, use, host, cache, reproduce, transmit, and display ... solely for the operation and maintenance of the Website」（条文中で "content" が "explain" と誤記されている）

### Munch（Munch Studio）

- 価格ページは「Munch Studio」で、SNS の運用一式（台本・生成動画・ストレージ）の中に「Video Repurposing」が分単位で入っている。Essential は年払い $38/月（$456/年、月払い $68）で「500 min Video Repurposing / mo」、Premium は年払い $60/月（$720/年、月払い $85）で 1,000 分。7 日の無料試用
- 切り抜きの選び方・日本語・規約の条文は今回読んでいない。切り抜き専用のサービスから方向を変えたと読める（推測）

### 日本語向けのサービス

- 「国産」「日本語特化」の切り抜き専用サービスを検索したが、公式ページで日本語の切り抜きの選択を明記したものは見つからなかった（2026-11-09）。用語解説サイト AI PICKS は「字幕生成や話者検出の精度は英語に比べて日本語コンテンツでまだ粗さが残り」と書く（二次の記述、出典の測定なし）

## この wiki への含意

- **何を AI に任せられるか**: 3 社とも「長尺から候補を選ぶ・縦にする・字幕を付ける」までを公式が掲げる。Klap は規約で、**選択は書き起こしを LLM に渡してやっている**と明かしている。これは [[exp-shortmovie-draft-generator]] の 2（Whisper の書き起こし → ChatGPT に 1 回投げて 5 案）と同じ骨格で、商用サービスの中身も「書き起こし＋LLM」だと確かめられた例
- **何が人の判断として残るか**: Vizard は「manually choose your video highlights by using our text-based video editor」と、人が選び直す画面を持つ。Klap は無料ではダウンロードもできず、選んで投稿するのは人。どれを公開するかの判断を自動にすると公式が書いているサービスはなかった
- **日本語**: Vizard は書き起こしの対応に日本語を明記、Klap は「99+ languages」、OpusClip は BETA。日本語で切り抜きの選択（どこが面白いか）がうまくいくかは、どこも測定を出していない
- **素材の扱いの違いが大きい**: Klap は外部の LLM と委託先にコマ・書き起こしが渡ると明記、Vizard は学習に使わないと明記、OpusClip は個人プランで学習に使いうる。講演の録画に他人（共演者・聴衆）が映るなら、渡し先の多さが問題になる（推測）
- 課金の単位が違う: OpusClip・Vizard は素材の分数、Klap は出した本数。長い講演から少数を選ぶなら Klap、短い素材から多く出すなら分課金、が安い（計算からの推測）

## 着手の仕方（未検証。galleria で確かめる）

- **表現できるようになること**: OpusClip と同じ（長尺からの縦型の切り抜き候補）。3 社の見立てを並べられる
- **機械**: どこでも（ブラウザ）
- **費用・アカウント**: **要: アカウント**（西尾が決める）。試すだけなら Vizard の無料（60 分/月、720p）が一番軽い。Klap は 1 本だけ無料で、ダウンロードには有料
- **最小の手順**: OpusClip と同じ録画を Vizard の無料に上げ、出た切り抜きの開始・終了の時刻を [[web-edit-auto-opusclip]] の比較表に足す
- **動いたと言える確かめ方**: 同じ録画から各サービスが選んだ区間の重なり（何本が同じ所を選んだか）。日本語の字幕の誤りの数
- **所要の見込み（推測）**: 1 社 30 分

## Open Questions

- Vizard の Creator・Business の金額（JavaScript の描画で取れなかった）
- Vizard の無料の保存期間: 価格ページは 3 日、データ安全の記事（2024-09）は 7 日で自動削除
- Klap の「99+ languages」に日本語の切り抜きの選択が含まれるか（書き起こしは WhisperX なので日本語は通るはず。推測）
- Munch Studio の規約（素材の扱い・学習）は未読
