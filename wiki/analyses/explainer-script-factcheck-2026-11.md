---
type: analysis
summary: 「動画の作り方の解説動画」の台本草稿（Mac の ~/video-making-explainer が正本、2026-11-09）で言い切っている 15 の主張を、wiki のページではなく原典（公式ページ・規格・論文）を開いて確かめた結果。そのまま可は 1 件（Claude は動画を直接は出せない）、ほかは言い方を直す。各社が「そろって 3 秒」（Google は 5 秒）、X は「音なしで流れる前提」とは書いていない、App Store の制限はプレビュー動画だけ、Netflix の 4 字は目安でなく上限、「Claude は音を聞けない」はアプリの voice mode と食い違って聞こえる、など。直した文の案付き
video_types: [promo, talk, embed]
sources:
  - 原典の URL は各項目に（取得日 2026-11-09）
  - web-meta-video-ads-best-practices.md、web-tiktok-creative-best-practices.md、web-x-video-ads-best-practices.md、web-google-youtube-abcds.md、web-digiday-2016-85-percent-sound-off.md
  - web-promo2-apple-app-previews-google-play-video.md、web-type-netflix-timed-text-style-guide.md、web-check-spec-powerpoint-keynote-google-slides-formats.md
  - web-genvid-gemini-omni-veo.md、web-genvid-seedance.md、web-genvid-sora-kling-runway.md、web-means-critic-openai-claude-vision-docs.md
  - web-opus-hculap-skill-motion-graphic.md、web-opus-howseen-claude-motion-design.md
  - web-motion-wcag-2-2-motion-flash-vestibular.md、web-motion-itu-r-bt1702-ofcom-nhk-minpo-flash-guidelines.md、web-check-ja-speech-rate-mora.md、web-3blue1brown-exposition-advice.md、web-muller-2008-misconceptions.md、web-mayer-multimedia-principles.md、web-embed-ladner-sigaccess-chi-video-in-talks.md、web-embed-siggraph-ieeevis-chi-fast-forward.md
---

# 解説動画の台本のファクトチェック（2026-11）

西尾の決定（[[origin-2026-11-09]] の Updates）で、「動画の作り方の解説動画」を一般向けに YouTube で公開する。台本の草稿（Mac の `~/video-making-explainer` が正本。この wiki には置かない）で言い切っている主張を、一つずつ原典で確かめた。

**確かめ方**:
- wiki のページは、どの原典を引いているかを知るためだけに使った。原典（公式ページ・規格・論文）を開いて、該当の文言を引いた。
- 項目 1〜14 は 3 つの担当（配信先の規則、AI のモデルの docs、研究）が読み、まとめ役が判定を揃えた。項目 15 は、まとめ役が wiki の経験と文献で確かめた。
- 開けなかった原典は、各項目に書いた。Internet Archive の版で読んだものは、版の日付を書いた。
- 台本そのもの（script-draft.md）は直していない（Mac 側で直す）。

## 判定の一覧

| # | 台本の主張（節） | 判定 | 一番の理由 |
|---|---|---|---|
| 1 | 画面の文字や数字を正確に出すことは、どの会社も保証していない（2） | 言い方を直す | Google は Omni について「正しく読める形で描く」と明言（英語以外は未評価） |
| 2 | Claude Opus 5.5 のようなモデルは、動画を直接は出せない（2） | **そのまま可**（任意で直す） | 公式は "Text and images → text"。「のような」は Gemini Omni（動画を出す）と紛れうる |
| 3 | 各社の広告の資料は、そろって「最初の 3 秒」（3） | 言い方を直す | Google は 5 秒、TikTok は 3 秒と 6 秒、X はブランドを 4 秒 |
| 4 | X のタイムラインは音なしの前提、YouTube・TikTok は音ありの前提（3） | 言い方を直す | X は「音なしへの備え」を勧めるだけ（縦長全画面は音あり既定）。YouTube のホームは音なし・字幕つきで再生 |
| 5 | 数秒ごとに新しいことを起こし、拍に揃えると、まとまって見える（3） | 言い方を直す | 作り手の手順書の決まりで、効果は測っていない（意図した hold は例外）。「まとまって」の原典は無し。拍と揃えると心地よい、の実験はある |
| 6 | App Store はアプリ自身の画面の収録だけを認めている（3） | 言い方を直す | 2.3.4 はプレビュー動画の決まり。2.3.14 の creative assets がある |
| 7 | 画面の大きな部分が 1 秒に 3 回を超えて光らないように（3） | 言い方を直す | WCAG の面積は 10 度の視野の 25%（画面の約 1 割）。「大きな部分」は ITU 寄りで甘い。赤の閃光は別扱い |
| 8 | 日本語なら 1 秒に 6〜7 モーラ（4） | 言い方を直す（軽く） | 値は合うが、発話の中の速さで、文と文の間を含まない |
| 9 | 最初の 30 秒で見る理由を渡す／誤解を先に言って崩すのも効く（4） | 1 文目そのまま可、2 文目を直す | 30 秒は 2021 年の審査の指針（現行は "early on"）。Muller は物理の動画の実験 1 つで、事前知識の高い組では差なし |
| 10 | 動きは指すためだけに／飾りの動きは理解を助けない（4） | 言い方を直す | 2 文目は Höffler & Leutner 2007（g=−0.05, k=17）で支えられる。1 文目は狭い（変化を見せる動き g=0.40 が抜ける） |
| 11 | Claude は音を聞けない（4） | 言い方を直す | API に音声の入力は無いが、アプリには voice mode がある。「作った音声ファイルを聞いて確かめられない」に絞る |
| 12 | 日本語の字幕の目安は 1 秒 4 文字（5） | 言い方を直す | Netflix は「目安」でなく「上限（up to）」。出典を言う |
| 13 | 流す前に一言／動画の声と話し手の声は重ねない（5） | 言い方を直す（軽く） | どれも実験でなく助言と規則。原典に近いのは「声はどちらか一つ」 |
| 14 | H.264 の mp4 ならどの発表ソフトでも通る（5） | 言い方を直す（軽く） | 三つとも H.264 可。音は AAC が前提、確かめたのは三つだけ |
| 15 | 正解は逆になる／宣伝では止めない、解説では飾りを動かさない（6） | 言い方を直す | 経験は一人の評価で、逆向きの記述もある。冒頭の「ことがあります」と揃える |

削る項目は無い。

## 1. 「（動画生成モデルは）雰囲気のある映像は得意ですが、画面の文字や数字を正確に出すことは、どの会社も保証していません。」

- **判定: 言い方を直す**
- **原典**（2026-11-09）:
  - Google Gemini Omni: https://ai.google.dev/gemini-api/docs/omni （"Text in videos" と "Technical details" の節）
  - Google Veo 3.1（Vertex）: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate （最終更新 2026-11-07。画面の文字の記述は見つからず）
  - ByteDance Seedance 2.5: https://docs.byteplus.com/en/docs/modelark/seedance-2-5-prompt-guide （UpdatedTime 2026-11-07。JavaScript で描くページで、HTML に埋め込まれた本文データから読んだ）
  - Runway: https://docs.dev.runwayml.com/_llms-txt/core-api.txt
  - OpenAI: https://developers.openai.com/api/docs/deprecations
  - Kling: app.klingai.com は JavaScript で描くページで、本文が読めなかった
- **該当の文言**:
  - Google: "You can prompt to include text in your video and Gemini Omni will render in a way that is correct and readable." / "English (EN) is fully supported, but other languages have not been evaluated, so they may work but results can vary."
  - ByteDance: "Text in the video may be misspelled. Letters in English words may be substituted, added, or omitted…"
  - Runway（INTERNAL.BAD_OUTPUT の原因）: "Prompt including explicit text generation requests"
  - OpenAI: "The Sora 2 models and Videos API were shut down on September 24, 2026"
- **理由**:
  - docs は保証書ではないので、字面だけなら外れていない。
  - しかし Google は Omni について「正しく読める形で描く」と明言している。「どの会社も」と言うと、Google の docs を見た視聴者には誤りに聞こえる。
  - Google は自分で測った数字を出しておらず、英語以外は評価していない。日本語の視聴者に一番効くのはこの条件。
  - 文字の失敗を自分で認めているのは ByteDance と Runway。Sora は提供が終わっている。Kling は確認できない。
- **直した文の案**:
  - 案 A: 「雰囲気のある映像は得意ですが、画面の文字や数字は当てにできません。綴りを誤ると自分で書いている会社があり、正しく描けると書く Google も、英語以外は評価していないとしています。」
  - 案 B（短い）: 「雰囲気のある映像は得意ですが、画面の文字や数字が正確に出るかは、まだ当てにできません。綴りを誤ることがあると、自分で書いている会社もあります。」
- **wiki との食い違い**:
  - [[web-genvid-gemini-omni-veo]]、[[web-genvid-seedance]]、[[web-genvid-sora-kling-runway]] は原典と合っていた。
  - 台本の出典メモの「sora-kling-runway（文字は保証しない）」は不正確。Sora は終了していて文字の記述が無く、Kling は確認できない。

## 2. 「Claude Opus 5.5 のようなモデルは、動画を直接は出せません。」

- **判定: そのまま可**（任意で直す）
- **原典**（2026-11-09）:
  - https://platform.claude.com/docs/en/models/opus-5-5/overview.md
  - https://platform.claude.com/docs/en/models/overview.md
  - https://platform.claude.com/docs/en/api/messages/create.md
- **該当の文言**:
  - "Input → output | Text and images → text"（Opus 5.5 のページ）
  - "All current models support text and image input, text output, multilingual capabilities, vision, and tool use."（モデル一覧）
- **理由**:
  - 公式は、出力をテキストとしている。
  - コード実行ツールでファイルを作る道はあるが、それは「直接は」で除かれる。
  - ただし Google の Gemini Omni Flash は「Gemini」の名前で、出力に動画を持つ（https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash の "Output Video with native Audio, Text"）。「のような」を「言語モデル一般」と受け取られると、ずれる。
- **直した文の案（任意）**: 「Claude Opus 5.5 が出せるのは文字だけで、動画を直接は出せません。」
- **wiki との食い違い**: なし

## 3. 「宣伝の動画は、最初の数秒がすべてです。各社の広告の資料は、そろって『最初の 3 秒』と書いています。」

- **判定: 言い方を直す**
- **原典**（取得日はすべて 2026-11-09）:
  - TikTok の creative best practices: https://ads.tiktok.com/help/article/creative-best-practices?lang=en （Last updated: June 2025）
  - X の video advertising best practices: https://business.twitter.com/en/blog/video-advertising-best-practices.html （直接は開けず、Internet Archive の 2024-02-26 の版で読んだ）
  - X の Vertical Video Ads: https://business.x.com/en/products/vertical-video-ads （Internet Archive の 2026-09-06 の版）
  - Google の ABCD reference guide: https://services.google.com/fh/files/misc/youtube_google_abcd_reference_guide_en.pdf （日付なし）
  - Meta（Reels）: https://www.facebook.com/government-nonprofits/resources/reels （Internet Archive の 2024-11-02 の版）
  - Meta の 2016 年の発表: https://www.facebook.com/business/news/updated-features-for-video-ads （Internet Archive の 2026-10-26 の版）
- **該当の文言**:
  - TikTok: "Introduce your content proposition in the first 3 seconds" / "Prioritize your hook in the first 6 seconds"
  - X: "include your product/service within the first three seconds" / "brand name and logo should appear ... within the first four seconds"
  - Google: "Introduce your product or brand in the first five seconds" / "Have more than two frames in the first five seconds"
  - Meta: "How will you hook your audience in the first 3 seconds?"（Reels）
  - Meta の 2016 年の発表: "up to 47% of the value in a video campaign was delivered in the first three seconds"（Nielsen との調査の数字で、推奨ではない）
- **理由**:
  - 4 社とも「最初の数秒が大事」という向きは同じ。
  - ただし数字は揃っていない。Google は 5 秒、TikTok は「3 秒で提案、6 秒以内にフック」、X はブランドを 4 秒以内。
  - 「すべてです」も、原典より強い言い方。
  - Meta の現行の動画広告のページ（business/ads/video-ad-format、Internet Archive の 2026-10-07 の版）には、冒頭の秒数の記述が無い。
- **直した文の案**: 「宣伝の動画は、最初の数秒が勝負です。各社の広告の資料は、そろって、最初の 3 秒から 5 秒にいちばん大事なものを置くよう勧めています。」
- **wiki との食い違い**:
  - sources の 4 ページの数値は、原典と合っていた。
  - [[promo]] の「経験と並べる」の「各社の『最初の 3 秒』と同じ向き」は、同じページの表（Google は 5 秒）と食い違う。台本の誤りの元はここの可能性がある。→ [[promo]] の Updates に直しを足した。

## 4. 「X のタイムラインは音なしで流れる前提、YouTube や TikTok は音ありが前提です。」

- **判定: 言い方を直す**
- **原典**（2026-11-09）:
  - X の動画広告の記事（項目 3 と同じ。Internet Archive の 2024-02-26 の版）
  - X の Vertical Video Ads（Internet Archive の 2026-09-06 の版）
  - X のヘルプ: https://help.x.com/en/using-x/x-videos （Internet Archive の 2026-10-21 の版）
  - Google: https://www.thinkwithgoogle.com/future-of-marketing/creativity/youtube-video-ad-creative/ （2022）
  - YouTube のヘルプ: https://support.google.com/youtube/answer/7640367 （Use the inline player）
  - TikTok: https://ads.tiktok.com/business/en-US/blog/9-creative-tips-to-drive-auction-ad-performance （2020-10-21）と、項目 3 の TikTok のヘルプ
- **該当の文言**:
  - X の動画広告: "A sound-off strategy — subtitles ensure accessibility for all and can help capture on-the-go mobile viewers"
  - X の Vertical Video Ads: "Vertical Video Ads are sound-on by default"
  - Google（広告主向け）: "YouTube is almost entirely a sound-on experience"
  - YouTube のヘルプ（ホームと検索結果での再生）: "videos will begin to play on mute with captions auto-enabled"
  - TikTok: "The second you open TikTok, it's a sound-on experience."
- **理由**:
  - X の公式は、タイムラインが音なしで流れるとは書いていない。書いているのは、広告に「音なしへの備え（字幕）」を勧めることだけ。X の縦長全画面は、音ありが既定。
  - YouTube の「音あり前提」は Google の広告資料の言い方。YouTube 自身のヘルプでは、ホームと検索結果で音なし・字幕つきで再生される。
  - TikTok は原文どおり。
- **直した文の案**: 「音が出るかは場所で違います。X は動画広告に、音なしでも伝わる工夫を勧めています。YouTube や TikTok の広告の資料は、音ありを前提にしています。ただ、YouTube もホーム画面では音なしで流れます。」
  - 続く「だから、字幕だけで通じるように作るか…」はそのまま使える。
- **wiki との食い違い**: [[web-digiday-2016-85-percent-sound-off]] の表は YouTube を「音あり前提」とだけ書いていて、ホームと検索結果の音なし再生が抜けている。→ そのページの Updates に足した。
- 補足（項目 6 の原典から）: App Store のプレビュー動画も、既定は音なし（"By default, app previews play with the sound muted"）。

## 5. 「動きは止めない。数秒ごとに新しいことを起こし、場面の切り替えを音楽の拍にそろえると、まとまって見えます。」

- **判定: 言い方を直す**
- **原典**（2026-11-09）:
  - hculap/skill-motion-graphic: https://github.com/hculap/skill-motion-graphic （SKILL.md、assets/template/STUDIO.md、references/critique.md）
  - howseen-ai/claude-motion-design: https://github.com/howseen-ai/claude-motion-design （skill/motion-design/SKILL.md）
  - 研究: Lin, Yeh & Shams (2022) Neuroscience Letters 779:136623, doi:10.1016/j.neulet.2022.136623 。PubMed 35398533 の要旨だけ読んだ（本文の PDF は 403）。
  - 研究: Lipscomb (1995) の UCLA 博士論文の要旨（本人が 1998 年に投稿したもの）: https://auditory.org/postings/1998/35.html
  - 西尾の経験: [[exp-sutra-hype-editions]]（「変化が止まるとテンションが下がる」は西尾のレビューから）、[[exp-polis-magi-op]]（「死んだ拍」は AI の自己採点）、[[exp-html-capture-pipeline]]（120BPM の小節頭は、合わせる手間を減らすための作り方で、見る人への効果の話ではない）
- **該当の文言**:
  - hculap: "Something new happens on screen every 2–4 seconds." / "Cuts on downbeats, state changes on beats" / "no frames where everything is static unless it is a deliberate hold on a beat"
  - howseen: "Nothing still for > 1 s." / "no frozen frame anywhere except the final hold"
  - Lin ら: "Despite the subliminal nature of this manipulation, a higher perceptual pleasure was found for temporal congruency"
- **理由**:
  - 「2〜4 秒ごと」「1 秒を超えて止めない」「カットは小節の頭」は、作り手の手順書の決まりで、効果を測ったものではない。
  - どちらの手順書も、意図して止める間（拍の上の hold、最後の hold）を例外として認めている。「止めない」と言い切るのは、原典より強い。
  - 「まとまって見える」を言っている原典は見つからなかった。
  - 研究が示しているのは次の二つ。
    - Lin らでは、カットと拍が揃うと心地よさの評定が上がった。
    - Lipscomb では、単純なアニメで揃えたものが高く評価された。実際の映画の抜粋では、揃えたものと少しずらしたものに差が出なかった。
  - 「数秒ごとに新しいこと」を支える研究は、短く探した範囲では見つからなかった。
- **直した文の案**:
  - 案 A: 「動きは長く止めない。数秒ごとに新しいことを起こし、場面の切り替えは音楽の拍にそろえる。AI で動画を作る人たちの手順書にもそう書かれていて、カットと拍がそろうほうが心地よく感じる、という実験もあります。」
  - 案 B（短い）: 「動きは長く止めず、数秒ごとに新しいことを起こし、場面の切り替えを音楽の拍にそろえます。カットと拍がそろうと心地よく感じる、という実験もあります。」
- **wiki との食い違い**: [[web-opus-hculap-skill-motion-graphic]]、[[web-opus-howseen-claude-motion-design]]、[[after-opus55]] は、原典の例外（"deliberate hold on a beat"、"except the final hold"）を落としている。→ それぞれの Updates に足した。拍と映像の同期の研究（Lin ら 2022、Lipscomb 1995）も、[[design-fundamentals]] の Updates に足した（要旨のみ）。

## 6. 「App Store はアプリ自身の画面の収録だけを認めています。」

- **判定: 言い方を直す**
- **原典**（2026-11-09）:
  - App Review Guidelines: https://developer.apple.com/app-store/review/guidelines/ （Last Updated: October 16, 2026）
  - App Previews: https://developer.apple.com/app-store/app-previews/
  - Asset best practices: https://developer.apple.com/app-store/asset-best-practices/
- **該当の文言**:
  - 2.3.4: "previews may only use video screen captures of the app itself. ... You can add narration and video or textual overlays"
  - App Previews: "App previews must show only content within the app itself. Don't film people interacting with a device"
  - 2.3.14: "Creative assets allow you to highlight the value of your app in new ways compared to app-in-use screenshots and preview videos"
- **理由**:
  - 2.3.4 の制限は**プレビュー動画（App Previews）**が対象で、App Store 全体の決まりではない。
  - 現行版には 2.3.14 の creative assets があり、ブランドや季節の企画を見せる画像・動画を置ける（iOS 27 以降）。
  - プレビュー動画にも、ナレーションと文字は重ねてよい。
- **直した文の案**: 「作品を紹介するなら、実物を誤解させないこと。App Store のプレビュー動画は、アプリ自身の画面を収録したものだけと決められています。」
- **wiki との食い違い**: [[web-promo2-apple-app-previews-google-play-video]] の 2.3.4 の引用は合っていたが、2.3.14 に触れていない。→ そのページの Updates に足した。

## 7. 「速く点滅させるときは、画面の大きな部分が 1 秒に 3 回を超えて光らないようにします。光に敏感な人のための基準です。」

- **判定: 言い方を直す**
- **原典**:
  - ITU-R BT.1702-3（2023-11、In force）: https://www.itu.int/dms_pubrec/itu-r/rec/bt/R-REC-BT.1702-3-202311-I!!PDF-E.pdf 。itu.int は取得を拒否したので、Internet Archive で読んだ（PDF は 2026-10-21 の版、勧告のページは 2026-09-03 の版）。
  - WCAG 2.2（W3C Recommendation 2024-12-12）: https://www.w3.org/TR/WCAG22/ （取得 2026-11-09）
  - Understanding 2.3.1（Updated 2025-09-17）: https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html （取得 2026-11-09）
- **該当の文言**:
  - ITU: "the combined area of flashes occurring concurrently occupies more than 25% of the displayed screen area; and there are more than three flashes ... within any one-second period" / "Irrespective of luminance, a transition to or from a saturated red is also potentially harmful."
  - WCAG 2.3.1: "Web pages do not contain anything that flashes more than three times in any one second period, or the flash is below the general flash and red flash thresholds."
  - WCAG の面積: "25% of any 10 degree visual field"、目安は "a 341 x 256 pixel rectangle ... at 1024 x 768"
  - Understanding: "the video should be analyzed for risks at full screen"
- **理由**:
  - 「1 秒に 3 回まで」は、両方の原典と合っている。
  - 「大きな部分」がずれる。ITU は画面の 25% 超だが、WCAG は 10 度の視野の 25%（1024×768 の画面の約 11%）。YouTube を全画面で見ると、画面の 1 割ほどの閃光でも WCAG の基準を超えうる。
  - どちらも、赤の閃光を別扱いにしている。
  - 面積の条件は口で正確に言えない。条件を落として「1 秒に 3 回まで」とだけ言う方が、厳しい側に寄るので安全。WCAG 2.3.2（AAA）は面積の例外なしで「3 回まで」としている。
- **直した文の案**: 「注意が一つ。速く点滅させるときは、1 秒に 3 回までにします。赤い点滅は特に避けます。光で発作を起こしやすい人のための、放送とウェブの基準です。」
- **wiki との食い違い**: 数値（25%、20 cd/m²、10%、341×256、0.006 sr）は原典と合っている。[[web-motion-wcag-2-2-motion-flash-vestibular]] について 2 点。→ そのページの Updates に足した。
  - published の 2023-10-05 は初版の日付で、現行は 2024-12-12、Understanding は 2025-09-17 更新。
  - 「放送の基準（ITU-R BT.1702）が元」は、Understanding の原文では "based on existing specifications in use in the UK and by others for television broadcast"（英国の基準）。

## 8. 「日本語なら 1 秒に 6〜7 モーラくらいで見積もれます。」

- **判定: 言い方を直す（軽く）**
- **原典**（取得 2026-11-09）:
  - 吉村・幡手・浅井「日本語能力試験・聴解の発話速度分析と発話速度評価サービスの開発」（JSiSE 2023）: https://www.jsise.org/taikai/2023/program/contents/pdf/D4-3.pdf
  - 石本「日本語日常会話コーパスにおける会話場面と発話速度の関係」（言語資源ワークショップ 2024）: https://clrd.ninjal.ac.jp/lrw/lrw2024/i3_A2-paper.pdf
- **該当の文言**:
  - 吉村ら: 「N1 は 7.07 モーラ/秒，N2 は 6.76 モーラ/秒，N3 は 6.15」。公式問題集の聴解・課題理解の音声 273 発話。「1 人の話者が話し始めてから話し終えるまでを 1 発話」と数えている。
  - 石本: 「モーラ長は全話者での平均が 0.151 秒、最も速い話者 … 0.124 秒、最も遅い話者 … 0.198」（換算で約 6.6、範囲は 5.1〜8.1 モーラ／秒。協力者 18 人）。「括弧書きの時間で間が記されている発話は除外」と書いている。
- **理由**:
  - 6〜7 は、「自然な速さ」の値として二つの原典が支える。JLPT の N1・N2 は台本を読んだ試験の音声で、読み上げに一番近い。
  - ただし、どちらも一つの発話の中の速さで、文と文の間は入っていない。台本のモーラ数を 6.5 で割るだけだと、実際の尺より短く出る。
  - 一般の視聴者には「モーラ」の言い換えが要る。
- **直した文の案**: 「日本語の自然な速さは、1 秒に 6〜7 モーラ、かなにしてだいたい 6〜7 文字です。これに文と文の間を足して、尺を見積もります。」
  - 拗音の小さい「ゃ」などは 1 モーラにならないので、「だいたい」で受ける。
- **wiki との食い違い**:
  - [[web-check-ja-speech-rate-mora]] は、石本 2024 を「子どもに向けた発話は遅く、父母に向けた発話は速い」と書く。これは原典の要旨のとおりだが、本文（3.2 節）は逆で、「子どもに対する発話では発話速度が速くなる傾向」と書く。原典の中で要旨と本文が食い違っている。→ そのページの Updates に足した。
  - 台本の頭の尺の見込み（6.5 モーラ／秒で割る）も、間の分だけ短く出る。

## 9. 「最初の 30 秒で、見る理由を渡します。よくある誤解を先に言って、それを崩すのも効きます。」

- **判定: 1 文目はそのまま可、2 文目は言い方を直す**
- **原典**:
  - SoME1 の告知（2021-07-16）: https://www.3blue1brown.com/blog/some1 （取得 2026-11-09）
  - SoME の現行ルール（日付なし）: https://some.3b1b.co/rules （取得 2026-11-09）
  - Muller の博士論文 "Designing effective multimedia for physics education"（University of Sydney, 2008）の 9 章: https://www.sydney.edu.au/science/physics/pdfs/research/super/PhD(Muller).pdf 。大学のサイトから取れず、Internet Archive の 2022-01-22 の版で読んだ。JCAL の論文本文は開いていない。
- **該当の文言**:
  - SoME1: "Motivation: It should be clear to the reader/viewer within the first 30 seconds why they should care."
  - 現行ルール: "It should be clear early on in the explainer why the topic matters"
  - Muller: "The effect size for these differences in comparison to the Exposition was d = .83 for the Dialogue and d = .79 for the Refutation."（表 9.2 の n は 92+86+95+91=364）
- **理由**:
  - 「30 秒」は 2021 年のコンテストの審査の指針の文言で、効果を測った値ではない。現行ルールでは "early on" に変わっている。ただ、台本は出典名を言わない助言なので、1 文目はそのままでよい。
  - Muller の条件:
    - シドニー大学の 1 年の物理の学生に、ニュートンの法則の約 9.5 分の動画を見せた。
    - 誤概念は冒頭だけでなく、全体を通して取り上げて否定している。
    - d は伸び（事後 − 事前）の差で、7 分の簡潔な説明の版と比べた値。同じ長さの版と比べても有意だった。
    - 事前知識の高い組では、有意な差がなかった。
  - 測ったのは理解の伸びで、掴みではない。「効きます」と一般化するより、「実験が一つある」と言う方が正確。
- **直した文の案**: 「最初の 30 秒で、見る理由を渡します。よくある誤解をわざと言ってから崩すと、正しい説明だけの動画より理解が伸びた、という物理の授業動画の実験もあります。」
- **wiki との食い違い**: [[web-muller-2008-misconceptions]] は「効果量が何の差の d かは未確認」と書くが、論文で「伸びの差、Exposition と比べた値」と確かめられた。→ Updates に足した。0.79・0.83・364 は合っている。論文の中の ANOVA の自由度 F(3, 461) は n=364 と合わない（論文の誤記と思われる）。

## 10. 「動きは、いま説明しているものを指すためだけに使います。飾りの動きは、理解を助けません。」

- **判定: 言い方を直す**
- **原典**:
  - Noetel ら 2022, Review of Educational Research 92(3)。出版社のページではなく写し（https://files.constantcontact.com/1145f86e901/7bc63268-3738-46ae-9ee0-fbdafb58537f.pdf 、取得 2026-11-09）で読んだ。
  - Höffler & Leutner 2007 の抄録: https://www.leibniz-ipn.de/en/research/publications/instructional-animation-versus-static-pictures-a-meta-analysis 。本文は 403 で開けなかった。
  - Sundararajan & Adesope 2020 は、Springer のボット確認で開けなかった（回避していない）。
- **該当の文言**:
  - Noetel: "Decorational animations had no learning benefits (g = −0.05, 95% CI [−0.17, 0.07], k = 17; Höffler & Leutner, 2007)"
  - Noetel: "Animations were only helpful when the animations communicated something meaningful, like how gears work (g = 0.40 ...)"
  - Noetel: signaling は "g = 0.43, 95% CI [0.35, 0.50], k = 209"
- **理由**:
  - 「飾りの動きは理解を助けない」は、装飾的なアニメを直接測った値と合っている。Höffler & Leutner 2007 の下位分析で、k=17、1973〜2003 年の研究、静止図と比べて差なし。
  - 言っているのは「益がない」で、「害がある」ではない。この言い方なら言い切りの範囲内。
  - 誘惑的な細部（seductive details）の値は、関係のない面白い話や絵を除く効果で、「動き」を測ったものではない。動きの根拠には使えない。
  - 1 文目の「指すためだけに」は狭すぎる。研究が一番はっきり支えるのは、変化や仕組みそのものを見せる動き（表現的なアニメ、g=0.40）。指す動き（signaling、g=0.43）と並べるべき。
- **直した文の案**: 「動きは、いま話しているものを指すか、ものが変わる様子そのものを見せるために使います。飾りのための動きは、理解の助けにならない、と報告されています。」
- **wiki との食い違い**: なし。[[web-mayer-multimedia-principles]] と [[talk]] の値は Noetel と一致した。[[web-berney-betrancourt-2016-animation-meta-analysis]] の「Noetel の表と本文で符号が違う（d=0.05／g=−0.05）」も原典どおり。

## 11. 「Claude は音を聞けないので、合成した声を文字起こしして台本と照合し、読みは辞書で直して、最後は人が聞きます。」

- **判定: 言い方を直す**
- **原典**（2026-11-09）:
  - API: https://platform.claude.com/docs/en/models/opus-5-5/overview.md 、https://platform.claude.com/docs/en/api/messages/create.md
  - アプリの voice mode: https://support.claude.com/en/articles/11101966-use-voice-mode 、https://academy.claude.com/tutorials/how-to-choose-between-voice-mode-and-dictation
- **該当の文言**:
  - API: "Input → output | Text and images → text"。Messages API の create.md には "audio" が一度も出てこない。
  - アプリ: "Allowing you to speak to Claude and hear Claude's voice responses." / "In hands-free mode, Claude listens continuously…"
- **理由**:
  - API に音声を入れる口が無いのは、公式どおり。
  - しかしアプリには voice mode があり、公式も "Claude listens" と書いている。一般の視聴者には、「Claude は音を聞けない」が自分の体験と食い違って聞こえる。
  - voice mode が内部で音声を文字に直してから渡すのかは、開いた公式ページに書かれていなかった（確かめられていない）。
  - 台本で言いたいのは、「作った音声ファイルを Claude に聞かせて確かめることはできない」の一点。
- **直した文の案**: 「Claude は、作った音声ファイルを聞いて確かめることができません。そこで、合成した声を文字起こしして台本と照合し、読みは辞書で直して、最後は人が聞きます。」
- **wiki との食い違い**: [[after-opus55]] の「Claude については 2026-11 の docs でもそのまま正しい」は、API については合っている。ただしアプリの voice mode に触れていない。→ Updates に「API の条件つき」と足した。

## 12. 「日本語の字幕の目安は、1 秒に 4 文字です。」

- **判定: 言い方を直す**
- **原典**: Netflix の Japanese Timed Text Style Guide。https://partnerhelp.netflixstudios.com/hc/en-us/articles/215767517-Japanese-Timed-Text-Style-Guide （取得 2026-11-09、変更履歴の最新は 2025-12-19）
- **該当の文言**:
  - "I.19. Reading Speed Limits — Up to 4 characters per second"
  - 変更履歴（2022-12-22）: "sections edited to mention 'reading speed limits' and 'up to'"
  - 聴覚障害者向けの字幕: "II.18 ... Up to 7 characters per second"
- **理由**:
  - 4 文字は「目安」ではなく「上限」。Netflix は 2022 年に、わざわざ "limits" と "up to" に書き換えている。
  - 対象は Netflix に納める日本語の字幕で、聴覚障害者向けの字幕は 7 文字まで。
  - 出典を言わずに一般の規則のように言うと、条件が落ちる。
  - 研究の側では、豊倉・山田 2017 が「1 秒 6 字までは視線の負荷が変わらない」と報告している（人数は少ない。[[web-check-ja-toyokura-yamada-2017-subtitle-4-chars]]）。4 字は保守的な側。
- **直した文の案**: 「文字は、読み終わるまで出しておく。Netflix は日本語の字幕を、1 秒に 4 文字までと決めています。」
- **wiki との食い違い**: なし（[[web-type-netflix-timed-text-style-guide]] は原典と合っていた）。

## 13. 「流す前に、話し手が『いまから何が映るか』を一言だけ言う。動画の声と話し手の声は重ねません。」

- **判定: 言い方を直す（軽く）**
- **原典**（取得 2026-11-09）:
  - Ladner "Making Your Conference Talk Accessible"（2015-10-18）: https://homes.cs.washington.edu/~ladner/MakingYourTalkAccessible.pdf
  - SIGACCESS Accessible Presentation Guide: https://www.sigaccess.org/welcome-to-sigaccess/resources/accessible-presentation-guide/
  - IEEE VIS 2015 Fast Forwards: https://ieeevis.org/year/2015/info/presenter-information/fast-forwards
  - SIGGRAPH 2026 Fast Forward: https://s2026.siggraph.org/papers-fast-forward-author-instructions/
- **該当の文言**:
  - Ladner: "Make sure that videos are captioned and audio described. Sometimes it is good to give a brief description of what is in the video before it is played. This will help blind audience members to establish context for what they will hear."
  - VIS 2015: "Audio: allowed, but ... no pre-recorded voice-over (presentation must be done live)"
  - SIGGRAPH 2026: "you must have at least one author on the stage to narrate your video while it is playing"
- **根拠の強さ**: どれも実験ではない。
  - Ladner は経験からの助言で、"Sometimes it is good" と控えめ。目的は、目の見えない聴衆に文脈を渡すこと。
  - VIS 2015 は特定の形式（25 秒の Fast Forward、話し手が生で語る）の規則で、禁じる理由は書かれていない。
  - 「声を重ねない」を一般的な主張として書いた原典は見つからなかった。
- **理由**:
  - 1 文目は Ladner と合っている。「だけ」は原典に無い制限だが、害はない。
  - 2 文目は、どちらの声を残すかが聞き手に分からない。原典に近い形は「声はどちらか一つにする」（VIS・SIGGRAPH は「話し手が語るなら、動画に録音したナレーションを入れない」）。
- **直した文の案**: 「流す前に、話し手が『いまから何が映るか』を一言言います。声はどちらか一つにします。話し手が語るなら動画に声を入れず、動画が語るなら話し手は黙ります。」
- **wiki との食い違い**: ほぼなし。[[web-embed-ladner-sigaccess-chi-video-in-talks]] の summary の「勧めている」は、原文の "Sometimes it is good to" より強い。→ Updates に足した。

## 14. 「書き出しは、どの発表ソフトでも通る H.264 の mp4 にしておくと安全です。」

- **判定: 言い方を直す（軽く）**
- **原典**（2026-11-09）:
  - PowerPoint: https://support.microsoft.com/en-us/office/video-and-audio-file-formats-supported-in-powerpoint-d8b12450-26db-4c7b-a5c1-593d3418fb59
  - Keynote: https://support.apple.com/guide/keynote/add-video-and-audio-tan63d61519a/mac 、https://support.apple.com/guide/keynote/tan12af068f9/mac
  - Google Drive: https://support.google.com/drive/answer/2423694
  - Google スライド: https://support.google.com/docs/answer/97447
- **該当の文言**:
  - PowerPoint: "Recommended formats — Video: .mp4 files encoded with H.264 video and AAC audio"
  - Keynote: "Movies in H.264 format play on all devices and versions of macOS, iOS, iPadOS, and visionOS"
  - Drive: "MPEG4, 3GPP, and MOV files (h264 and MPEG4 video codecs; AAC audio codec)" / "The maximum playback resolution is 1920 x 1080"
- **理由**:
  - 三つとも、H.264 の mp4 を扱える。
  - ただし音は AAC が前提（PowerPoint の推奨、Drive の対応形式）。
  - 「どの発表ソフトでも」は、三つしか確かめていない。
  - Google スライドは Drive か YouTube から入れるので、再生は 1080p まで。
- **直した文の案**: 「書き出しは、H.264（音は AAC）の mp4 にしておくと安全です。PowerPoint・Keynote・Google スライドのどれでも流せます。」
- **wiki との食い違い**: なし（[[web-check-spec-powerpoint-keynote-google-slides-formats]] は原典と合っていた）。

## 15. 結び「三通りで、正解は逆になります。宣伝では止めない、解説では飾りを動かさない。宣伝では拍が時計、解説では声が時計、発表の中では動画そのものが時計です。」

- **判定: 言い方を直す**（まとめ役が wiki の経験と文献で確かめた。新しい原典は開いていない）
- **根拠の範囲**:
  - 宣伝の「止めない」:
    - 西尾の経験（[[exp-sutra-hype-editions]] の「変化が止まるとテンションが下がる」、[[exp-polis-magi-op]] の「死んだ拍」）。
    - 作り手の手順書（項目 5）。こちらは意図した hold を例外にしている。
    - 動きを promo の測度で測った研究は無い（[[three-video-types]]）。
  - 解説の「飾りを動かさない」:
    - 西尾の経験（[[exp-qualia-video]] の完全静止を既定、drift は「気持ち悪い」）は、一人の評価。
    - 研究が支えるのは「飾りの動きは理解の助けにならない」まで（項目 10）。
  - 逆向きの記述も wiki にある。
    - 外の解説の作法（Zenn・HyperFrames）は、解説でも連続した動きを推している。
    - Cell の Figure360（単独で流れる図の解説）は、「2 秒以上画面が変わらない間を作らない」と書く（[[design-fundamentals]] の Updates）。
    - 「飾りの」の限定が要る。
  - 「拍が時計／声が時計／動画が時計」は、経験と合っている（[[exp-html-capture-pipeline]] の 120BPM の小節頭、[[after-opus55]] の「ナレーションを時計にする」、[[embed]] の流しっぱなし）。ただし「宣伝では拍」は音楽が主の promo の話で、無音前提の X 用（[[exp-words-as-public-goods-video]]）には拍が無い。
  - 冒頭（0. の節）は「正解が逆になることがあります」で弱めてあり、そのまま可。結びだけ言い切っているので、冒頭と揃える。
- **直した文の案**: 「三通りで、正解が逆になることがあります。宣伝では動きを長く止めない。解説では、飾りのための動きはしない。そして時計が違います。宣伝では音楽の拍、解説ではナレーションの声、発表の中では動画そのものが時計です。」
- **wiki との食い違い**: なし

## 台本の頭の尺の見込みについて（項目 8 から）

草稿の「1,666 字 → 約 2,200〜2,500 モーラ ÷ 6.5 モーラ／秒 ≈ 6 分」は、文と文の間を含まない速さで割っているので、実際の尺より短く出る（推測）。TTS で一度通しで合成して、実際の長さを測る方が確か。

## 開けなかった原典（代わりに読んだもの）

- **Internet Archive の版で読んだもの**（直接の取得は 403・400・拒否）:
  - Meta の Reels（2024-11-02）、Meta の 2016 年の発表（2026-10-26）、Meta の動画広告のページ（2026-10-07）
  - X の動画広告の記事（2024-02-26。それより新しい保存版は無く、今も公開されているかは未確認）、X の Vertical Video Ads（2026-09-06）、X のヘルプ（2026-10-21）
  - ITU-R BT.1702-3 の PDF（2026-10-21）
  - Muller の博士論文（2022-01-22）
- **開けなかったもの**:
  - help.openai.com の Sora 終了の記事（403）
  - Kling の公式（JavaScript で描くページ）
  - Höffler & Leutner 2007 の本文（403。抄録のみ）
  - Sundararajan & Adesope 2020（Springer のボット確認。回避していない。値は Noetel の要約による）
  - Lin ら 2022 の本文（403。PubMed の要旨のみ）
  - Muller の JCAL の論文本文
- **公式に書かれていなかったもの**: Claude アプリの voice mode が、音声を内部で文字に直してから渡すのか。

## wiki に足した直し（各ページの Updates）

- [[promo]]: 「各社の『最初の 3 秒』」を「3〜5 秒」に（項目 3）
- [[web-digiday-2016-85-percent-sound-off]]: YouTube のホームと検索結果では、音なし・字幕つきで再生される（項目 4）
- [[web-promo2-apple-app-previews-google-play-video]]: 2.3.4 はプレビュー動画の決まりで、2.3.14 の creative assets がある（項目 6）
- [[web-opus-hculap-skill-motion-graphic]]、[[web-opus-howseen-claude-motion-design]]: 原典の例外（意図した hold、最後の hold）を足した（項目 5）
- [[after-opus55]]: 「止めない」の例外、「Claude は聞けない」は API の条件つき（項目 5、11）
- [[design-fundamentals]]: 拍と映像の同期の研究（Lin ら 2022、Lipscomb 1995。要旨のみ）（項目 5）
- [[web-motion-wcag-2-2-motion-flash-vestibular]]: 現行版の日付、閃光の基準の元は英国の放送の基準（項目 7）
- [[web-check-ja-speech-rate-mora]]: 石本 2024 の要旨と本文で、子どもへの発話の向きが逆（項目 8）
- [[web-muller-2008-misconceptions]]: d は伸びの差で、Exposition と比べた値（項目 9）
- [[web-embed-ladner-sigaccess-chi-video-in-talks]]: Ladner の原文は "Sometimes it is good to"（項目 13）
