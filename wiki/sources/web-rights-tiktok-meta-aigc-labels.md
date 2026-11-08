---
type: source
summary: TikTok のコミュニティガイドライン「Edited Media and AI-Generated Content」（2026-09-24 施行）と Meta（Instagram・Facebook・Threads）の「AI info」の公式ヘルプ。TikTok はリアルな人・場面にラベルを求め「実在の人と分からない汎用の TTS ナレーション」「アニメなどの画風」は不要と明記。Meta は写実的な動画とリアルな音声に開示を求め、「リアルな AI の声で語るリール」を要ラベルの例に挙げる
video_types: [promo, talk]
url: https://www.tiktok.com/community-guidelines/en/integrity-authenticity
author: TikTok（ByteDance）／Meta Platforms
published: 2026-08-25（TikTok のガイドライン公表、2026-09-24 施行）／Meta のヘルプは「24 週間前に更新」（2026-11-09 時点、2026-05 頃）
retrieved: 2026-11-09
sources:
  - https://www.tiktok.com/community-guidelines/en/integrity-authenticity （Integrity and Authenticity、Released 2026-08-25、Effective 2026-09-24。折りたたみの「More information」は HTML 内のデータから読んだ）
  - https://www.tiktok.com/transparency/en/supporting-responsible-transparent-ai-generated-content （TikTok の透明性のページ）
  - https://support.tiktok.com/en/using-tiktok/creating-videos/ai-generated-content （AIGC ラベルのヘルプ。JavaScript で描画され本文を取れず、未読）
  - https://www.meta.com/en-gb/help/artificial-intelligence/1783222608822690/ （How to identify AI content on Meta products。JavaScript 描画のため WebFetch で該当箇所の原文を引用させて読んだ）
  - https://about.fb.com/news/2024/02/labeling-ai-generated-images-on-facebook-instagram-and-threads/ （Meta 2024-02-06）
  - https://about.fb.com/news/2024/04/metas-approach-to-labeling-ai-generated-content-and-manipulated-media/ （Meta 2024-04-05、2024-07-01 更新）
---

# TikTok の AIGC ラベルと Meta の AI info

## 何の文献か

- TikTok: コミュニティガイドラインの「Integrity and Authenticity」の節（公表 2026-08-25、施行 2026-09-24）と、透明性センターの説明ページ。ラベルの付け方のヘルプ（support.tiktok.com）は JavaScript で描画され、curl でも WebFetch でも本文が取れなかった（リダイレクト先も同じ）。読めていない
- Meta: ヘルプセンター「How to identify AI content on Meta products」（2026-11-09 時点で「24 週間前に更新」）。JavaScript 描画で curl では本文が取れず、WebFetch に該当箇所の原文の引用を頼んで読んだ（要約経由なので、原文と一字一句の照合はしていない）。背景として Meta の 2024 年の公式発表 2 本を読んだ

## 書いてあること

### TikTok（Edited Media and AI-Generated Content）

- 「**リアルに見える場面や人を示す、AI 生成または大きく編集したコンテンツ**にラベルを求める」。ラベルの無いものは、害の大きさに応じて削除・制限・運営によるラベル付与がありうる
- 定義（More information）:
  - AIGC =「AI が作った・変えた画像・動画・音声すべて。リアルな場面も、アニメ・カートゥーン・絵画のような画風も含む」
  - Significantly Edited Content = 誰かが言っていない・していないことをしたように見せる、または見分けがつかないほど外見を変えるもの（意味を変える切り取り、クリップの並べ替え・結合、速度の変更、音声・映像の追加削除を含む）
  - Likeness = 顔・体・**声**・身振りを含む、認識できる人の表象
- 開示が要る例: 顔を他人に置き換える、言っていないことを言ったように見せる、背景・物・人を誤解させる形で足す・消す、**実在の人の声をまねた AI の音声**
- 開示が要らない例（原文）: 色補正・リフレーム・切り抜きの小さな編集、「**Using artistic styles, like anime**」、「**Using generic text-to-speech (TTS) narration, when the TTS isn't a recognizable voice of a known individual**」
- 開示の方法:「AIGC ラベル、または分かりやすいキャプション・ステッカー・透かし」。自分で付けた表示でもよい、と書いている
- 禁止: 同意の無い私人の likeness、公共の重要事項について誤解させる AIGC（本物の報道に見せる、災害・紛争、公人の政治的立場や商品の推奨をでっち上げる など）
- 自動ラベル（透明性のページ）: TikTok の AI エフェクトで作ったものに自動で付け、「**一部の他のプラットフォームの AIGC には Content Credentials（C2PA）を読んで**ラベルを付ける」。TikTok 側でも C2PA を付ける作業を進めており、ダウンロードや他所での共有でも残る、と書いている。C2PA の一般会員で、Content Authenticity Initiative にも参加

### Meta（Instagram・Facebook・Threads の AI info）

- ヘルプ:「写実的な動画やリアルな音声」を AI で作った・変えたコンテンツに、利用者がラベルを付けるよう求めることがある。**この要件は画像には適用しない**（"This requirement does not apply to images."）
- 要ラベルの例（原文）: "A video that appears realistic of a group of people walking around an outdoor market"、"An audio file of two people talking"、"A song created using AI-generated vocals"、"**A reel narrated with a realistic AI-generated voiceover**"
- 不要の例: "Video of an outdoor landscape, created in a style resembling a cartoon"、人が牛に乗る画像（画像なので不要）
- 自動: 業界標準の信号を検出したら「AI info」を付ける。AI で**編集・改変**しただけと信号が示すものは、投稿の上ではなく「…」メニューの中に表示する。Meta の AI ツールで作ったものは自動でラベル、見える透かしが入ることがある。AI 中心のアカウントは「AI creator」のプロフィール表示を付けられる
- 罰: ラベルが要るのに付けずに共有すると「ペナルティが課されることがある」（内容は書かれていない）
- 2024-02 の発表: 検出に使う信号として「C2PA と IPTC の技術標準の "AI generated" 情報」を名指しし、Google・OpenAI・Microsoft・Adobe・Midjourney・Shutterstock の画像を対象にする、と書いた。音声・動画には他社の信号がまだ無いので、利用者の開示の仕組みを作り「写実的な動画またはリアルに聞こえる音声」の投稿には使うことを求める、とした
- 2024-07-01 の更新: 「Made with AI」を「AI info」に改名。レタッチ程度の編集にもラベルが付いて、意図と合わなかったため、と書いている

## この wiki への含意

- **TTS の扱いが配信先で逆になる**。TikTok は「実在の人と分からない汎用の TTS ナレーション」を不要と明記、Meta は「リアルな AI の声で語るリール」を要ラベルの例に挙げる。YouTube は文言なし（[[web-rights-youtube-genai-disclosure]]）。西尾の talk（AivisSpeech の声で語る [[exp-qualia-video]]、[[exp-llm-wiki-explainer-series]]）を Instagram のリールに出すなら、Meta の例に当たるので AI info を付ける側になる。どこまでを「realistic」と見るかは Meta の文言からは決まらない
- **画風（アニメ）は TikTok で不要**。コードで描くモーション・図形（[[exp-html-capture-pipeline]]）は「AI が作った動画」に当たるかがまず曖昧だが、当たるとしても写実的でないので、TikTok・Meta とも開示の要件の外になる読みが自然
- **歌声合成の曲**: Meta の「AI 生成のボーカルで作った曲」は要ラベルの例。般若心経の曲（[[exp-sutra-songs-on-music]]、VOICEVOX の歌声）を Instagram・Facebook に出すなら当たる。TikTok では「実在の人の声をまねた」ものでなければ、リアルな人・場面ではないので要件の外と読める
- **promo**: 生成モデルのリアルなカットを入れた promo（[[work-promotion-video]]）は、TikTok・Meta ともラベルが要る側。生成元の C2PA が残っていれば両社とも自動で付ける可能性がある
- 開示の方法: TikTok は自分の字幕・透かしでもよいと書く。最初から画面に「声: AivisSpeech（まお）」のような表示を焼き込めば、TikTok の要件と grasp-nishio の「モデル名を明示する」を同時に満たせる（担当の推論）

## Open Questions

- TikTok の AIGC ラベルのヘルプ（付け方の手順、自動ラベルの外し方）は未読
- Meta の「realistic AI-generated voiceover」の線: 明らかに合成と分かるキャラクター声は当たるのか。例は 1 つだけで決められない
- Meta が C2PA を動画でも読むのか。2024-02 の発表は画像の話で、ヘルプは信号の名前を出していない
- 日本の利用者に別の規則（地域ごとの違い）があるかは、英語版で読んだので確かめていない（Meta は WebFetch が日本語版を返した回があり、内容は同じだった）
