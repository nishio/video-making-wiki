---
type: source
summary: 作品のデモ動画が実際の動きと違って見えた 2 つの例の一次資料。Google の「Hands-on with Gemini」（2023-12-06、6 分 22 秒。説明欄に「遅延を短縮し出力を短くした」、同日の開発者ブログは静止画と文字のプロンプトで作ったと書く）と、SEC の訴状が述べる Nikola の「In Motion」動画（2018、自走できない試作トラックを坂で転がして撮り、2〜3 倍に速めて「in motion」と投稿）
video_types: [promo]
url: https://developers.googleblog.com/en/how-its-made-interacting-with-gemini-through-multimodal-prompting
author: Google（Alexander Chen, Creative Director。YouTube の Google チャンネル）／U.S. Securities and Exchange Commission
published: 2023-12-06（Google の動画と開発者ブログ）／2021-07-29（SEC の訴状）／2021-12-21（SEC の Nikola との和解の発表）
retrieved: 2026-11-09
sources:
  - https://developers.googleblog.com/en/how-its-made-interacting-with-gemini-through-multimodal-prompting（「How it's Made: Interacting with Gemini through multimodal prompting」2023-12-06）
  - https://www.youtube.com/watch?v=UIZAiXYceBI（「Hands-on with Gemini: Interacting with multimodal AI」。直接の取得は bot 判定で止められ、Internet Archive の 2023-12-06 15:36 UTC の版の説明欄を読んだ）
  - https://www.sec.gov/litigation/complaints/2021/comp-pr2021-141.pdf（SEC v. Trevor R. Milton, Case 1:21-cv-06445, filed 07/29/21。Internet Archive の 2023-04-04 の版）
  - https://www.sec.gov/news/press-release/2021-267（「Nikola Corporation to Pay $125 Million to Resolve Fraud Charges」2021-12-21。Internet Archive の版）
---

# 演出されたデモ動画の 2 例: Gemini の Hands-on と Nikola の「In Motion」

## 何の文献か

- **Google の 2 つの一次資料**: 動画の説明欄（作った側の注記）と、同じ日に出た開発者ブログの制作の説明。作った側の書いたもので、第三者の検証ではない
- **SEC の訴状**: 米国証券取引委員会が Nikola の創業者 Trevor Milton を訴えた民事訴訟の訴状。**訴状は SEC の主張であり、裁判所の認定ではない**。会社の Nikola は 2021-12-21 に「without admitting or denying」で 1 億 2,500 万ドルの和解に応じた（SEC の発表）。Milton 個人の裁判の結末やその後の経過は、このページでは確かめていない
- どちらも作品紹介の動画の「誤解させる見せ方」の例として選んだ。どの資料も、動画の作り方の指針ではない
- 自動判定に止められた取得（YouTube の bot 判定、SEC の自動アクセスの制限）は回避せず、Internet Archive の版を読んだ。動画そのものは見ていない

## 書いてあること

### Google「Hands-on with Gemini」（2023-12-06、382 秒）

- 説明欄（公開直後の版）: 「This video highlights some of our favorite interactions with Gemini」「Explore our prompting approaches here: https://goo.gle/how-its-made-gemini」、そして「**For the purposes of this demo, latency has been reduced and Gemini outputs have been shortened for brevity.**」
- チャプターは Multimodal Dialogue、Multilinguality、Game Creation、Visual Puzzles など 10 区切り
- 同日の開発者ブログ「How it's Made」は、「In this post, we'll explore some of the prompting approaches we used in our Hands on with Gemini demo video」と書き、手の写真（静止画）を 1 枚ずつ見せて文字で問う例を並べる: 3 枚の手の画像に「What do you think I'm doing? Hint: it's a game.」と聞くと「You're playing rock, paper, scissors.」と答える、など
- つまり作った側の説明では、動画は「画像と文字のプロンプトでの好きなやり取り」を選び、遅延を縮め出力を短くして編集したもの。一方、動画は人とモデルが映像と声でその場でやり取りしているように見え、実際の作り方と違う、という批判が当時報じられた。**この批判の部分は書き手（Opus 5.5）の記憶によるもので、報道の原文はこのページでは読んでいない。動画も見ていない**

### SEC の訴状が述べる Nikola One「In Motion」動画（段落 59〜65）

- 2016 年 12 月の発表会の後、Nikola One の試作車には手が入らず、自走できなかった、と訴状は書く
- 2018 年初め、取引先の部品会社の広告撮影で、試作車をトレーラーで運び、「It was towed to the top of an inclined stretch of road and then filmed rolling down the incline」。これを 3 回繰り返した
- Milton は撮影に立ち会い、生の映像を社内のデジタルメディア担当に渡して短いクリップを作らせ、編集を指示した。最終版は「had been sped up two- to-three times. This had the effect of making the Nikola One appear to move faster than it was」
- 2018-01-25 に Twitter・Facebook・YouTube に投稿。「The video does not have any narration or text」。投稿文は「Behold, the Nikola One in motion. Pre-production units to hit fleets in 2019 for testing ...」
- 訴状の主張: 動画と投稿文は、トラックが自力でなく重力で坂を下っていたことを省き、「left viewers with the false impression that the Nikola One was capable of moving under its own power」。動画は 2020 年 9 月まで会社の SNS とサイトに残り、SEC の調査の開始後に消された
- 会社の和解の発表（2021-12-21）は、Milton の発言が製品と技術の到達点について投資家に誤った印象を与えた、と SEC の命令が認定した、と書く（動画には直接触れていない）

## この wiki への含意

- **嘘の文字は一つもなくても誤解させられる**: Nikola の動画にはナレーションも文字もなかった。訴状が問題にしたのは、映像（坂を転がす・速める）と投稿文（「in motion」）の組み合わせが、言っていないことを信じさせた点。Gemini の動画も、説明欄には注記があったが、画面の上の見え方が注記より強く伝わった、という形の批判を受けた。**作品の中身を正確に見せるには、画面に映る出来事の時間（速さ・待ち）と因果（何が動かしたか）を、画面の上で誤解させないことが要る**
- **速さを変えるときは画面で言う**: 西尾の作品紹介でも、LLM・画像判定・TTS の待ちは長い。[[exp-thinklet-reading-demo-video]] は約 30 秒の待ちを削らずナレーションで「今何が起きているか」を語った。これは速さを偽らない作りで、Gemini の「遅延を短縮」の逆。早送りやカットを選ぶなら、Google のように説明欄に書くだけでは足りず、画面に「×4」「待ち 30 秒を省略」と出すほうが、この 2 例からの教訓に合う（文献の主張ではなく、このページの見立て）
- **数字は条件ごと**: [[exp-gyazo-resumption-video]] で、部品の比較（約 5 倍）や低解像度の実験の値を本番の条件で測り直し、説明文に条件を添えたのは、同じ問題への対処。西尾が「この比較の仕方はちょっとおかしくて」と指摘したのは、映像の見え方が実際の性能と食い違うことへの指摘だった
- **描いた図は「イメージ」と明記**: 47 秒版の「JSON 生成と確率値の比較図」は中身をイメージと明記した（[[exp-gyazo-resumption-video]]）。コードで描く方式や生成映像の方式で作品の挙動を見せるとき、描いた・生成したものであることを画面で言うのは、Kickstarter の「完成品と見間違えるレンダリングは不可」（[[web-promo2-kickstarter-producthunt-launch-video]]）とも同じ線
- **promo の圧は誤解の側に働く**: どちらの例も、宣伝の場（新モデルの発表、投資家向けの SNS）で起きた。Derek Lieu の「ゲームにない機能はトレーラーで作れない（倫理的に）」（[[web-promo2-derek-lieu-game-trailers]]）と並べると、作品紹介の promo で「アピール重視」にするほど、この線に近づく。西尾が 47 秒版を「アピール重視で技術の詳細を伝えるには適切ではない」と評した（[[origin-2026-11-09]] の Updates）のは誤解の問題ではないが、promo の形が中身の正確さと引っ張り合う、という同じ構図の中にある

## Open Questions

- Gemini の動画への批判の報道（どの媒体が何を指摘したか）は原文を読んでいない。Google 側の追加の説明（X の投稿など）も読めていない
- Milton 個人の訴訟・刑事事件の結末は確かめていない。訴状の事実関係は SEC の主張として扱う
- 「早送りを画面で明示する」が、見る人の受け取り方を実際に変えるかを測った資料は探していない
