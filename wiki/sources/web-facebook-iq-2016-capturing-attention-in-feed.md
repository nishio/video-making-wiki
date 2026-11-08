---
type: source
summary: Facebook IQ（2016-04）が、実際に出稿された動画広告を一般の評価者に「最初の 10 秒を無音で」見せて採点させ、その点数で Nielsen の ad recall を回帰した社内研究。商品を見せる・ブランドを結びつける・情報量を絞ると recall が高かったと報告し、「ブランドを前に、音なしでも分かるように」と勧める
video_types: [promo]
url: https://www.facebook.com/iq/articles/capturing-attention-feed-video-creative
author: Facebook IQ（Facebook。著者名の記載なし）
published: 2016-04-20
retrieved: 2026-11-09
sources:
  - https://www.facebook.com/business/news/insights/capturing-attention-feed-video-creative（Internet Archive 2019-01-16 の版で本文を読んだ）
  - https://www.facebook.com/iq/articles/capturing-attention-feed-video-creative（同じ記事の旧 URL）
  - https://www.socialmediatoday.com/news/facebook-releases-new-guide-to-help-advertisers-maximize-video-ad-performan/450818（Andrew Hutchinson、2016-04-21。図の数字の二次情報）
---

# Facebook IQ (2016) Capturing Attention in Feed: The Science Behind Effective Video Creative

## 何の文献か

- Facebook の調査部門 Facebook IQ の記事。**広告を売る側の社内研究**で、査読はない。公開日は検索結果とSocial Media Today の記事（2016-04-21）から 2016-04-20 とした
- 現行の facebook.com では本文が出ず（エラー）、Internet Archive の 2019-01-16 の保存版で読んだ
- 結果の数字の多くは**図（画像）の中にあり、本文に書かれていない**。画像は取得していない。図の数字のうち 2 つは Social Media Today の記事の記述による（原典未読）

### 測り方（Methodology 節、原文から）

- 対象: 「over 850 English-language-only video ads that were in market in the US and in Europe between Q4 2014 and Q4 2015」。末尾の Source 欄では「2,183 Video Ad ratings corresponding to 965 video ads in market in the US and EMEA」（本文の 850 本と数が合わない）
- 評価者: 「people who did not have a creative or advertising background」（人数は書いていない）
- 手順: 各広告を 2 回、19 問（4 次元: first impressions, branding, messaging, video features）で評価。「To mimic the mobile News Feed experience, the raters first watched the first 10 seconds of the video ad with sound turned off. Next … watched the first 30 seconds of the video with sound turned on.」
- 効果の測度: 出稿中に行われた **Nielsen Brand Effect の Ad Recall**。「We were able to match over 600 video ads to over 200 Nielsen Brand Effect studies」。キャンペーンの特性を統制した線形回帰で、評価者の点数から Ad Recall を説明し、「able to account for 82% of the variation in Ad Recall scores (r2=0.82)」
- つまり**観察データの回帰**で、要素を操作した実験ではない。r² = 0.82 は「キャンペーンの特性」も含めたモデル全体の説明力で、クリエイティブの要素だけの寄与ではない（本文はこの区別を書いていない）

## 書いてあること

- 前提として、Fors Marsh Group のテストで「it takes only 0.25 seconds of exposure for people to recall mobile feed content at a statistically significant rate」、フィードの 1 投稿あたりの滞在が「1.7 seconds with a piece of content on mobile compared to 2.5 seconds on desktop」と書いている
- 「Consumption is fast, frequent and sound-free. For these reasons, video ads on News Feed need to bring the brand to the front to capture people's attention quickly and be understandable regardless of sound by using captions or other visual techniques.」
- 回帰の結果として: 「the strongest Ad Recall scores occurred when video ad creative showcased the products or services, included conversations and brand links and got the message across succinctly with the right amount of information」
- 図の数字（Social Media Today による。原典の図は未読）: 調べた広告のうち「only 46% of them were seen to have had easily identifiable brand links present within the first 10 seconds」「only 23% of the ads had a clear brand message within that first segment」。つまり当時の広告の多くは、無音の最初の 10 秒でブランドを伝えていなかった、という現状の記述
- マーケターへの助言: 「Design with the screen in mind」「Think holistically about creative」「Test, learn, iterate」

## この wiki への含意

- **promo の「最初の数秒・無音」の根拠としてよく引かれる研究の、実際の測り方**がこれ。評価者が「無音で最初の 10 秒」を見たのは「フィードを真似る」ための実験の設定で、**「フィードでは無音で見られている」ことを測ったものではない**。無音の割合の数字は別の出所（[[web-digiday-2016-85-percent-sound-off]]、[[web-meta-video-ads-best-practices]]）
- 測度は ad recall（ブランドを覚えているか）で、「最後まで見られたか」ではない。西尾の依頼は「誰もが最後まで見てしまうような動画」（[[exp-democracy-river-video]]、[[exp-words-as-public-goods-video]]）で、目的の指標がずれている
- 「商品を見せる」「情報量を絞る」は、西尾の動画では「主役の技術を見せる」に当たりそう。Gyazo の動画で西尾が「Visual Jev の話も超重要、これが一番大事」と主役を前に出させたのは（[[exp-gyazo-resumption-video]]）、この研究の「showcased the products」と同じ向き。ただし同じものを測ったわけではない
- 「brand links を早く」は、問いを先に置いて答え（名前・結論）を最後に回収する西尾の構成（[[exp-democracy-river-video]]、[[exp-words-as-public-goods-video]]）とは向きが違う。広告の recall を上げる設計と、最後まで見させる設計が同じかは、この研究からは言えない

## Open Questions

- 本文の「over 850」と Source 欄の「965 video ads」が合わない（評価の重複や除外があったのかは書いていない）
- 19 問の中身と、どの要素がどれだけ recall に効いたかの係数は図の中で、読めていない
- 評価者の人数・募集方法、評価者間の一致は書いていない
- 2014〜2015 年の英語の広告で、フィードが無音既定だった時期のデータ。Meta 自身がその後に音ありへ動いている（[[web-meta-video-ads-best-practices]]）ので、今のフィードや Reels に当てはまるかは分からない
