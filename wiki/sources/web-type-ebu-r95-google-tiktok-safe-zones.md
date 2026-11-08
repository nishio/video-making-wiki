---
type: source
summary: 画面の端の「安全な範囲」の資料 3 つ。放送の EBU R 95（2017）は 16:9 の動きのセーフを各辺 3.5%、グラフィックス（文字）のセーフを各辺 5% とし、縦長の SNS 広告では Google（YouTube の縦長広告）と TikTok（TopView）が UI に覆われない範囲を数値でなく参照画像・テンプレートで示し、TikTok は「説明文が長いほど安全な範囲は狭い」と書いている
video_types: [promo, any]
url: https://tech.ebu.ch/docs/r/r095.pdf
author: EBU（European Broadcasting Union）／ Google（Google Ads Help）／ TikTok（TikTok Ads Help Center）
published: 2017-06
retrieved: 2026-11-09
sources:
  - https://tech.ebu.ch/docs/r/r095.pdf （EBU R 95 "Safe areas for 16:9 television production" Version 1.1, June 2017）
  - https://support.google.com/google-ads/answer/9128498?hl=en （Google Ads Help "Use square and vertical video to engage mobile customers" の "Safe zones for vertical video ads on YouTube"）
  - https://ads.tiktok.com/help/article/tiktok-reservation-topview （TikTok Ads Help Center "TopView ad specifications" の "Safe zone specifications"）
---

# セーフエリア: EBU R 95 と、縦長 SNS の UI が覆う範囲（Google・TikTok）

## 何の文献か

- **EBU R 95**: 欧州放送連合の勧告（公式の技術文書、10 ページ）。初版 1999、改訂 2000・2008・2015・2016、2017-06 の Version 1.1 が最新（文書の表紙による）。16:9 で作った番組を 16:9 で出す前提の safe area を、SD・HD・UHD の画素と行の数で定める
- **Google Ads Help**: Google の広告主向けヘルプ。YouTube の縦長動画広告の safe zone を参照画像で示す。2026-11-09 時点の公式ページによる（ページの最終更新日は表示されていない）
- **TikTok Ads Help Center**: TikTok の広告商品 TopView（アプリを開いたとき最初に出る広告）の仕様。safe zone は zip のテンプレートで配っている。2026-11-09 時点の公式ページによる
- Meta の Reels の「下 35%」は第 1 回のサーベイで扱った（[[web-meta-video-ads-best-practices]]）ので、ここでは繰り返さない
- 種類: すべて公式ドキュメント（仕様・推奨）。効果を測った報告ではない
- SMPTE の safe area の規格（ST 2046-1 など）は有料で読めなかった

## 書いてあること

### EBU R 95（放送）

- 「Two safe areas are needed in television production; all essential action should be protected inside an Action Safe Area, and all graphics inside a Graphics Safe Area.」
- 数値（Notes 5）: 「The action safe area is 3.5% and the graphics safe area is 5%, at the top, bottom and lateral parts of the image.」
- 1080p の画素での値は図（画像）にあり、本文のテキストには 3.5% = 67 画素（16:9 の横）という訂正の注だけがある。5% から計算すると、1920×1080 のグラフィックス・セーフは左右 96 画素・上下 54 行を除いた 1728×972、アクション・セーフは左右 67 画素・上下 38 行を除いた範囲（計算。図の値とは 1 画素ずれる可能性がある）
- 画像の中心はすべての工程で動かさない（創作上の理由がある場合を除く）
- 以前の版にあった、16:9 の番組を 4:3・14:9 で出すための保護の範囲は、この版では扱っていない
- **なぜ要るか**は R 95 自身はほとんど書いていない。BBC の字幕ガイドは、Teletext の描画範囲が画面の高さの約 90% だったのは「a safe area which accommodates overscan」（テレビが画面の端を切って映す）のためだった、と書いている（[[web-type-bbc-subtitle-guidelines]] §9.2.1）

### Google（YouTube の縦長広告）

- 縦長の広告は、Performance Max・App・Demand Gen では in-stream・in-feed・Shorts に、モバイル・PC・テレビで出うる
- 「Overlays, call-to-actions, and buttons may appear in different places depending on the format, campaign type, and screen.」
- 「Use this image as a reference to ensure important elements like your logo, product, supers, and others are within the red safe area to avoid risk of elements being covered within certain inventory.」（supers ＝ 画面に重ねる文字）
- **範囲は参照画像（赤い枠）でしか示しておらず、本文に数値は無い**。画像は取得していない（この wiki の決まりで画像はダウンロードしない）。第三者のツールのサイトが「Google の画像から」として画素の値（左 48・右 192・上 288 など）を載せているが、サイトによって値が違い、確かめていない
- YouTube アプリのプレイヤーは動画の比率に合わせて変わり、9:16 の動画は画面の 75% を覆い、全画面にすると 100%、と書く

### TikTok（TopView）

- TopView は「最初の 3 秒の全画面」と「その後のフィード」の二段で、safe zone もそれぞれ別。左から右の言語と右から左の言語でも別のテンプレート
- 「The safe zone size is determined by the ad caption length and any Interactive Add-on usage; the longer the caption, the smaller the safe zone will be.」
- 「The safe zone may not cover all devices」。機種ごとのプレビューで確かめよ、と書く
- 最初の 3 秒で TikTok のロゴ・スキップボタン・上スワイプの表示に文字やロゴを重ねてはいけない。フィードの段では、ボタン・ユーザー名・説明文が出る場所に文字・ロゴ・主な内容を置かない
- 第 1 回の [[web-tiktok-creative-best-practices]] は「UI safe zone の中に」とだけ書いていて、比率は無かった。この TopView の仕様も数値でなくテンプレートで、比率は本文に無い

## この wiki への含意

- **放送のセーフと SNS のセーフは理由が違う**: 放送はテレビが端を切ること（overscan）への備えで、四辺に均等（3.5%・5%）。SNS は UI（ボタン・説明文・ユーザー名・進捗バー）が覆う範囲で、下と右に偏り、面・広告の種類・説明文の長さで変わる。西尾の動画はウェブと SNS に出すので、overscan の心配は小さく、SNS の UI のほうが効く（推測）
- **クオリアさん journey の字幕（y=890 以降）**（[[exp-qualia-video]]、1920×1080）: EBU のグラフィックス・セーフの下端は y=1026。字幕の下端がそこを超えたかは exp ページに無い。YouTube の横長の再生では下端にプレイヤーの操作バーが重なりうる（BBC は操作の重ね表示から字幕を避けよと書く。[[web-type-bbc-subtitle-guidelines]]）
- **下端の進捗バー**（[[exp-words-as-public-goods-video]]、[[exp-democracy-river-video]]）: EBU の 3.5% の内側には入っていないと思われる（下端に置いたと書かれているだけで位置の値は無い）。X のタイムラインでは問題になったという記録は無い。Shorts・TikTok に縦長で出すなら、下端は UI の範囲で、TikTok は説明文が長いほど覆う範囲が広がる。Reels の下 35% は [[web-meta-video-ads-best-practices]]
- **縦長ショート**（[[exp-nishio-showreel]] の縦長版、YouTube ショート向け）: Google の参照画像に照らしたかは記録が無い。重要な文字・ロゴは「赤い枠の中」に、と Google は書く
- **promo の 4:5**（[[exp-words-as-public-goods-video]]、1080×1350）: Google・TikTok の safe zone の資料は 9:16 が前提で、4:5 が Shorts や TikTok でどう枠に収まり、どこが覆われるかはこれらの資料には書いていない
- **embed**: スライドに貼って会場で流すなら、SNS の UI は無い。プロジェクタの映り方（端の欠け）は放送の overscan に近い問題で、EBU のグラフィックス・セーフ 5% は目安になりうる（推測。試していない）

## Open Questions

- Google の縦長広告の safe zone の数値（画像の赤い枠）を確かめていない。広告でない通常の Shorts の投稿に同じ範囲が当てはまるかも書いていない
- TikTok の通常の投稿（広告でない）の safe zone を書いた公式資料は今回見つけていない
- SMPTE（ST 2046-1）の値は読んでいない。広く引かれる「アクション 93%・タイトル 90%」は二次情報でしか見ていない
- X のタイムラインの動画で、UI が覆う範囲を書いた公式資料は見つけていない
