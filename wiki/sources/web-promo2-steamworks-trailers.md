---
type: source
summary: Valve の Steamworks ドキュメントのトレーラーの項（最初のトレーラーはゲームプレイを、HUD を見せる、10 秒未満・無音で見られる前提、マイクロトレーラーは最初の動画から自動で 6 秒）と、生成 AI の開示（Content Survey。プレイヤーが消費する中身が対象、ゲームは宣伝素材と一致すると約束する）
video_types: [promo]
url: https://partner.steamgames.com/doc/store/trailer
author: Valve（Steamworks Documentation）
published: unknown（ページに日付なし）
retrieved: 2026-11-09
sources:
  - https://partner.steamgames.com/doc/store/trailer（Store Presence > Trailers）
  - https://partner.steamgames.com/doc/gettingstarted/contentsurvey（Content Survey、3) Generative Artificial Intelligence Content）
  - https://partner.steamgames.com/doc/store/assets/rules（Graphical Asset Rules、2022-09-01 施行）
---

# Steamworks のトレーラーの作法と生成 AI の開示

## 何の文献か

- Steam を運営する Valve の、開発者向けの公式ドキュメント（Steamworks Documentation）。トレーラーの項は推奨と仕様、Content Survey は申告の決まり
- 「We have found that most Steam users are looking for gameplay」とあるが、何をどう測ったかは書かれていない。Valve の自社の観察として読む
- 2026-11-09 時点の公式ページによる。どのページにも更新日はない

## 書いてあること

### トレーラー（Store Presence > Trailers）

- 発売にはトレーラーのアップロードが要る。ストアページの最上部に出る
- 見られる文脈を考えよ、と書く: 「you may have less than 10 seconds to make an impression」（Discovery Queue を回している客）、「the customer may be watching your trailer without any audio」。音なしで分かるかを考えよ
- **Gameplay Trailers First**: 最初に並べるトレーラーは主にゲームプレイで、「from the perspective that they will be interacting with your game」。「It is also often beneficial to have the in-game HUD elements visible」
- トレーラーに分類を付ける: General/Cinematic（事前レンダリング・ロゴ・タイトル・受賞などの混合）、Teaser（ゲームをあまり見せない）、Gameplay（大半がゲームプレイ）、Interview/Dev Diary。分類はプレイヤーに表示される
- 最初の 2 本の有効なトレーラーはスクリーンショットより前に出る
- **マイクロトレーラー**: 「6-second looping videos」で、Steam が「the first video visible in its Store Page」から 1 秒の切り抜きを 6 つつないで自動で作る。「It is not possible to customize microtrailers」
- 仕様: 1920×1080 まで、30/29.97 か 60/59.94fps、5,000Kbps 以上、H.264 と AAC が望ましい、16:9 が望ましい（4:3 も可）。音はステレオに落とされる
- サムネイル・ポスターを自分で上げるなら「It must be a frame from the video itself」。文字は避けよ
- 詳しくは Steam Dev Days 2016 の講演を見よ、とリンクしている（動画なのでこのページでは見ていない）

### 生成 AI の開示（Content Survey の 3）

- 開発の効率化のための AI 道具は対象外。対象は「the use of AI in creating content that ships with your game, and is consumed by players」（絵・音・物語・翻訳など）
- **Pre-Generated**: 開発中に AI の助けで作り、ゲームと一緒に出る中身。「Under the Steam Distribution Agreement, you promise Valve that your game will not include illegal or infringing content, and that your game will be consistent with your marketing materials」。発売前の審査で AI の中身も他と同じに評価し、この約束を確かめる、と書く
- **Live-Generated**: 実行中に AI が作る中身。違法な中身を出さないためのガードレールを申告する
- トレーラーそのもの（宣伝素材）を AI で作ったときの開示は、このページには書かれていない。書かれているのは「ゲームは宣伝素材と一致する」という約束の側

### ストアの画像の決まり（参考）

- 2022-09-01 から、ストアのカプセル画像にはゲームの絵・名前・公式の副題だけ。評価点・受賞・割引・行動喚起（「Wishlist now」など）を入れない（Graphical Asset Rules）。トレーラーの決まりではないが、ストアが「宣伝の文言」をどう扱うかの例

## この wiki への含意

- **「作品の中身を、作品の視点で」**: Valve は最初のトレーラーをゲームプレイにし、HUD も見せよ、と書く。ソフトウェアに置き換えれば、最初の動画は実際の画面を実際の操作の視点で、になる。Apple・Google の決まり（[[web-promo2-apple-app-previews-google-play-video]]）と同じ向き
- **最初の動画が自動で切り刻まれる**: マイクロトレーラーはどの 1 秒が切り出されても作品に見える動画を求める。西尾の promo の「最初の 1〜2 秒と最初のコマが勝負」（[[exp-shortmovie-draft-generator]]、[[exp-democracy-river-video]]）より厳しく、全体のどのコマも作品の中身であることを求める形になる。文字だけを叩き込む作り（[[exp-gyazo-resumption-video]] の 47 秒版）は、ここでは不利と読める（検証はしていない）
- **10 秒未満・無音** は SNS の文献（[[promo]]）と同じ。Steam は「音なしで学べるか」を考えよ、と書くだけで、無音前提にせよとは書いていない
- **分類を表示する**のは、見る側に「これはゲームプレイか、演出か」を知らせる仕組み。西尾の Gyazo の動画で、技術の詳細を伝える版と promo の版を分けるべきだったという本人の評価（[[origin-2026-11-09]] の Updates）と重なる: 一本で両方を兼ねず、種類を分けて名前を付ける
- **生成 AI**: Steam の開示は作品（ゲーム）の中身が対象で、宣伝素材の生成は名指ししない。ただし「ゲームは宣伝素材と一致する」と約束させているので、生成した映像で作品にない場面を見せれば、この約束に触れる

## Open Questions

- 「most Steam users are looking for gameplay」の根拠のデータは公開されていない
- マイクロトレーラーは最初の動画のどこから切るのか（等間隔か、選び方があるのか）は書かれていない
- トレーラー自体に生成映像を使うことへの決まりは、このページの範囲では見つからなかった
