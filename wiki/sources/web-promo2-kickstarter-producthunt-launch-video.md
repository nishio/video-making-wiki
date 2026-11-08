---
type: source
summary: 製品の立ち上げの場の動画の決まりと数字。Kickstarter の規約（試作品のデモは現状を映し、存在しない機能を CGI や特殊効果で見せない。2012 年からは写実的なレンダリングと模擬映像を禁止。AI の使い方は開示）、Mollick 2014 の分析（Kickstarter 48,526 件、動画の有無はロジスティック回帰でオッズ比 4.3 と成功に結びつく）、Product Hunt の公式ガイド（Product of the Day の約 53% に動画、Loom で手早いデモでよい）
video_types: [promo]
url: https://www.kickstarter.com/rules
author: Kickstarter（Rules、Creator Handbook、公式ブログ）／Ethan Mollick（Journal of Business Venturing）／Product Hunt（Launch Guide）
published: 2012-09-20（Kickstarter Is Not a Store）／2023-08-01（AI Policy）／2014（Mollick）／Rules と Product Hunt は unknown
retrieved: 2026-11-09
sources:
  - https://www.kickstarter.com/rules（直接は JS のチャレンジで取れず、Internet Archive の 2026-10-01 の版 http://web.archive.org/web/20261001025242/https://www.kickstarter.com/rules を読んだ）
  - https://www.kickstarter.com/help/handbook/your_story（同上、2026-10-20 の版）
  - https://www.kickstarter.com/blog/kickstarter-is-not-a-store（2012-09-20。Internet Archive の 2026-09-08 の版）
  - https://updates.kickstarter.com/introducing-our-new-ai-policy/（2023-08-01）
  - Mollick, E. (2014). The dynamics of crowdfunding: An exploratory study. Journal of Business Venturing, 29(1), 1–16.（PDF: https://leeds-faculty.colorado.edu/bhagat/Dynamics-of-Crowdfunding.pdf）
  - https://www.producthunt.com/launch/preparing-for-launch（直接は 403、Internet Archive の 2026-10-20 の版）
---

# Kickstarter と Product Hunt の立ち上げの動画

## 何の文献か

- **Kickstarter の規約・ハンドブック・公式ブログ**: クラウドファンディングの場の公式文書。規約は守らなければ掲載されない・中止される。ハンドブックは助言
- **Mollick 2014**: 査読のある経営学の論文。Kickstarter の 2009 年の開始から 2012 年 7 月までの全プロジェクトから、極端な目標額と米国外を除いた 48,526 件（成功 23,719 件、48.1%）を集めた観察研究。動画の効果は目標 5,000 ドル以上のプロジェクトでロジスティック回帰を当てたもの（観測 22,651 件）。**動画は「準備の度合い＝質の信号」の指標として使われ、動画の中身や出来は測っていない**。因果は言えない
- **Product Hunt の Launch Guide**: 製品の立ち上げの場の公式ガイド。数字は自社の集計（方法は書かれていない）
- Kickstarter と Product Hunt のページは、直接の取得が自動判定（JS のチャレンジ／403）で止められたので回避せず、Internet Archive の版を読んだ。2026-11-09 時点の最新とは限らない

## 書いてあること

### Kickstarter の規約（Rules、2026-10-01 の版）

- 「Information must be honest and clearly presented ... Projects can't mislead people or misrepresent facts」
- **Design & Technology**: 「**Prototype demonstration** should reflect a product's current state and should not include any CGI or special effects to demonstrate functionality that does not yet exist. If a project requires software and hardware integration, creators are required to show that functionality and any dependency clearly, or disclose that it has not yet been developed」
- **App Projects**: アプリ・ソフトウェアも「a **prototype must be demonstrated**」
- 素材の権利: 「Projects must solely contain materials that the creator has rights to using」
- **AI Use**: 「Creators must be transparent about how AI is used」。人の考えや関与がほとんどない「Excessive AI use」は禁止。規約の冒頭の項にも「As long as there is human creativity and human involvement, the use of AI is permitted」

### 「Kickstarter Is Not a Store」（2012-09-20）

- Hardware と Product Design の分類で、「Product simulations are prohibited. Projects cannot simulate events to demonstrate what a product might do in the future. Products can only be shown performing actions that they're able to perform in their current state of development」
- 「Product renderings are prohibited. Product images must be photos of the prototype as it currently exists」
- 9/24 の追記: 禁じたのは「photorealistic renderings of a product concept」。技術図面・CAD・スケッチなど設計の過程は引き続き可。「renderings that could be mistaken for finished products are prohibited」
- 見分け方: 「We may not know」。審査は短く、明らかなものは公開させず、公開後に見つかれば中止。「Everyone should continue to use their best judgment」
- 同じ日のコメント欄で Kickstarter の職員が、この決まりは Product Design と Hardware だけで、Games などには及ばない、と答えている
- 2026 年の規約の「CGI や特殊効果で存在しない機能を見せない」は、この 2012 年の決まりの後継と読める（つながりはこのページの見立て）

### Kickstarter の AI 方針（2023-08-01 公表、08-29 施行）

- AI を禁じない。AI で画像・文章などを生成するプロジェクトは、ページで何に AI を使い、何が自分の作で何が AI の出力かを開示する。生成に使った作品の持ち主の同意があるかも聞く
- 公開されたプロジェクトには「Use of AI」の欄が出る。開示しなければ停止されうる
- 動画（プロジェクト動画）を AI で生成したときの特別な決まりは、この告知には書かれていない

### Creator Handbook「Telling your story」（2026-10-20 の版）

- 「Make a compelling video. It's the best way to introduce yourself, and to give people a closer look at what you're working on. It doesn't have to be super slick; some of our favorite videos have a very DIY feel」
- 字幕・翻訳を付けることを勧める

### Mollick 2014 の数字

- Kickstarter 自身の 2011 年の助言「Rule #1 for Kickstarter videos: make one!」を引き、動画の有無を「at least minimum preparation」の信号として扱った
- 標本の 86% に動画があった
- 表 3（目標 5,000 ドル以上、ロジスティック回帰、指数化した係数＝オッズ比）: Video 4.30（Model 3）、4.26（Model 6）、p<0.01。分類・目標額・期間・特集の有無などを統制
- 本文: 「not including a video decreases chances by 26%」（Model 6、他の変数を平均に置いた平均的なプロジェクトで）。同じ書き方で、綴りの誤りは成功の見込みを 13% 下げ、開始 3 日以内の更新がないと 13% 強下げる
- 「%」が率の差（ポイント）か相対の減少かは、本文の書き方からは確かめきれない

### Product Hunt の Launch Guide（2026-10-20 の版）

- 「**Video** (optional) - About 53% of products that reached Product of the Day since 2021 include a video, so videos can help depending on what your product is, but aren't always necessary」
- 「If you don't have a budget for a high end video, consider doing a quick demo with a video tool (e.g. Loom)」。動画は YouTube のリンクだけ
- 動画とは別に「Interactive Demo」（Arcade など）を勧め、「The most successful launches tell a compelling story of the product, including showing what the user interface looks and feels like」
- 2021 年の Golden Kitty Awards に「Best Video」の賞があった

## この wiki への含意

- **「実際に動くものを見せる」が規約になっている場がある**: Kickstarter は作品紹介の動画に「現状を映せ、存在しない機能を CGI や特殊効果で見せるな、ソフトとハードの連携は見せるか、未開発だと開示せよ」を課している。これは西尾の問いの「作品の中身を正確に見せる」をそのまま規約にしたもの。**丸ごと生成した映像で作品の機能を見せる方式は、この線に正面から当たる**。コードで描くモーショングラフィックス（[[exp-html-capture-pipeline]]）も、作品の画面の代わりに描いた図で機能を見せれば「模擬（simulation）」に近づく。2012 年の追記の「技術図面・CAD・スケッチは可、完成品と見間違えるレンダリングは不可」は、描いた図が許される線の一つの例
- **[[exp-thinklet-reading-demo-video]]** は「ソフトとハードの連携を実機で見せ、動画に入らなかった段階 3 は文字で補った」。Kickstarter の「見せるか、未開発と開示せよ」の形に近い
- **[[exp-gyazo-resumption-video]]** の「中身はイメージと明記」（JSON 生成と確率値の比較図）は、描いた図であることを開示する作法として、Kickstarter の線と同じ向き
- **動画の有無と成功の相関は強いが、動画の出来の効果ではない**: Mollick の数字は「動画を作るほど準備した人のプロジェクトは成功しやすい」で、どんな動画が効くかは分からない。Kickstarter・Product Hunt とも「凝らなくてよい（DIY、Loom）」と書く。作る手間を抑えて実物を見せることを、場の側が勧めている
- **AI の開示**: Kickstarter は AI の使い方の開示を求める。grasp-nishio の「動画ではモデル名を明示する」（CLAUDE.md）と同じ向きで、生成に使ったモデルを書く習慣はこの場の決まりにも合う

## Open Questions

- Mollick の「26%」が絶対の差か相対の減少か。表の係数（オッズ比 4.26）からの計算は、このページではしていない
- 2012 年の「模擬映像の禁止」と 2026 年の規約の「CGI・特殊効果の禁止」の間の改訂の経過は追っていない
- Product Hunt の「53%」は Product of the Day に届いた製品の割合で、届かなかった製品の割合が書かれていないので、動画の有無と結果の関係は分からない
- Kickstarter の AI 方針が、プロジェクト動画を生成映像で作った場合をどう扱うか（「Use of AI」に書けば足りるか、規約の「CGI・特殊効果」に当たるか）は書かれていない
