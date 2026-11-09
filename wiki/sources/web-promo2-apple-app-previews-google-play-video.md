---
type: source
summary: Apple の App Store の App Previews（審査ガイドライン 2.3.4「アプリ自身の画面収録だけ」、15〜30 秒、無音で自動再生）と Google Play のプレビュー動画の指針（最初の 10 秒で実際の体験、8 割以上を実際の体験に、指で触る撮影は避ける、行動喚起の文言を禁じる）。どちらも「作品の実際の画面で、誤解させない」を決まりにしている
video_types: [promo]
url: https://developer.apple.com/app-store/review/guidelines/
author: Apple（App Review Guidelines、App Previews ページ、App Store Connect Help）／Google（Play Console Help）
published: 2026-10-16（App Review Guidelines の Last Updated）／他は unknown
retrieved: 2026-11-09
sources:
  - https://developer.apple.com/app-store/review/guidelines/（2.3 Accurate Metadata。Last Updated: October 16, 2026）
  - https://developer.apple.com/app-store/app-previews/（「Show more with app previews」）
  - https://developer.apple.com/help/app-store-connect/reference/app-information/app-preview-specifications
  - https://support.google.com/googleplay/android-developer/answer/9866151?hl=en（「Add preview assets to showcase your app」）
---

# App Store の App Previews と Google Play のプレビュー動画

## 何の文献か

- アプリストアを運営する 2 社の公式ドキュメント。どちらも **規約（守らないと審査で落ちる・掲載から外される）** と **推奨（守ると露出が増えるかもしれない）** が混ざっているので、以下では分けて書く
- 効果の測定は載っていない。どの決まりも「こうすると売れた」という実測ではなく、ストアの方針として書かれている
- すべて 2026-11-09 時点の公式ページによる。Apple の審査ガイドラインは「Last Updated: October 16, 2026」。他のページは更新日が書かれていない

## 書いてあること

### Apple（App Store）

**規約（App Review Guidelines 2.3 Accurate Metadata）**

- 2.3 の冒頭: メタデータ（説明・スクリーンショット・プレビュー）は「accurately reflect the app's core experience」であれ、と書いている
- **2.3.4**: 「previews may only use video screen captures of the app itself」。そのうえで「You can add narration and video or textual overlays to help explain anything that isn't clear from the video alone」。つまり、画面はアプリ自身の収録に限り、説明はナレーションと重ねる文字で足す、という形
- 2.3.1(a): 実際には提供しない中身や機能を宣伝するなど「marketing your app in a misleading way」は、ストア外での宣伝も含めて削除・アカウント停止の理由になる、と書いている
- 2.3.2: アプリ内課金が要る機能は、プレビューでもそれが分かるようにする
- 2.3.9: 素材の権利は開発者の責任。「display fictional account information instead of data from a real person」——実在の人のデータでなく架空のアカウント情報を見せよ
- 2.3.7: プレビューに価格や関係ない文言を入れない

**作り方の推奨（App Previews ページ）**

- 「footage captured on device」。1 言語につき最大 3 本、各 30 秒まで。製品ページと検索結果で自動再生され、Apple Ads にも使われる
- 「Stay within the app」: 「Don't film people interacting with a device, such as an over-the-shoulder angle or fingers tapping the screen」。肩越しの撮影や画面を叩く指を映さない
- 「Show more gameplay than cutscenes so you don't mislead your audience」
- 操作を示すためのタッチ位置などの図形は足してよい。「We recommend capturing the native UI resolution rather than zooming in on the view」。場面のつなぎは「don't imply functionality that your app doesn't include」、ディゾルブやフェードのような素直なものを、と書く
- 「By default, app previews play with the sound muted」なので、文字で文脈を足せ。文字は読める大きさで、読めるだけの時間出す。「new for spring」や日付のような古びる言及、価格は入れない
- 音は一本の曲で通すこと、UI やゲームの効果音を入れることを勧め、声を入れるなら良い機材で、プロの声優も考えよ、と書く
- 自動再生を切った人にはポスターフレーム（静止画）が出るので、アプリの本質が伝わるコマを選ぶ
- 撮り方: Mac に端末をつなぎ QuickTime Player で収録、iMovie か Final Cut Pro で編集

**仕様（App Store Connect Help）**

- 長さ 15〜30 秒、500MB まで、ポスターフレームの既定は 5 秒の位置
- 最大 30fps（H.264 は 10〜12 Mbps、ProRes 422 HQ も可）。音はステレオ、AAC 256kbps、44.1kHz か 48kHz
- 画面収録が前提なので、端末の解像度でなく「accepted resolution」の決まった組で受け付ける、と書く
- 処理に最大 24 時間

### Google Play

**規約（Requirements）**

- プレビュー動画は YouTube の URL で 1 本。収益化（広告）を切る、公開か限定公開、年齢制限なし、埋め込み可
- 文字を重ねるときも含め、Google Play の順位・受賞・利用者の声・価格や販促（「Best」「#1」「Top」「New」「Discount」「Million Downloads」など）を出さない。「Download now」「Install now」のような行動喚起の文言を使わない（この 2 点は動画の項では「Highly recommended」の下にあるが、短い説明文の項ではアイコンと同じく Metadata policy に結びつけている）

**推奨（Highly recommended）**

- 「Show the actual in-app or in-game experience, focusing on the core features and content as early as possible within the first 10 seconds of the video」
- 「Aim for at least 80% of the video to be representative of the user experience」。タイトル画面・ロゴ・カットシーン・事前レンダリングの映像は控え、使うなら実際の体験の補助にとどめる
- 自動再生は最初の 30 秒だけ（端末・設定・回線による、音は消して）。だから短く
- 指で端末を触る人を映さない（中心の使い方が端末の外にある場合を除く）
- 「Your video does not need to be professionally made」。ただしテンポ・効果・音・つなぎ・文字が滑らかに噛み合っていること
- 縦でも横でもよい。アプリの体験に合う向きで、縦長の動画の両脇に黒帯を残さない
- 無音で自動再生されるときのために文字で文脈を足す。文字は読める大きさと時間で
- UI・キャッチコピー・音声を各言語に合わせる

### AI 生成の映像について

- Apple・Google Play とも、2026-11-09 時点の上のページに「AI で生成した映像」を名指しした決まりは見つからなかった
- ただし Apple の 2.3.4「アプリ自身の画面収録だけ」と、Google の「8 割以上を実際の体験に」「事前レンダリングは補助に」は、作品の画面ではない生成映像を主にすることを、名指しせずに締め出している（読み方はこのページの見立て）

## この wiki への含意

- **promo の中で「作品の紹介」は、ストアでは別の決まりで縛られている**。SNS 広告の文献（[[web-meta-video-ads-best-practices]]、[[web-google-youtube-abcds]]）は「注意を引け、ブランドを早く」だったが、アプリストアの決まりは「作品の実際の画面を、誤解させずに」が先に来る。西尾の作品紹介で、中身（画面・実機・数値）を正確に見せる必要がある、という条件にはこちらが近い
- **「実際の画面 + 重ねる文字 + ナレーション」が両社の基本形**。描いたものに置き換えるのでなく、収録した画面に説明を重ねる。[[exp-thinklet-reading-demo-video]]（実機の撮影・画面のスクリーンショット・ずんだもんの読み上げを Premiere Pro で組んだ）は、この形にほぼ当たる。ただし実機を撮った縦長の映像には端末と本が映っていて、Apple の「端末を操作する人を映すな」とは違う。THINKLET は首から下げる端末で、Google の例外「中心の使い方が端末の外にある場合」に当たる
- **[[exp-gyazo-resumption-video]] との照合**: 47 秒版は画面の画像をすべて図形で描いた架空のもので、実画像を使っていない（README）。アプリストアの決まりで言えば、これは「アプリの画面」ではなく説明図にあたる。Gyazo の作業は公開するアプリではないので規約の対象ではないが、「作品の中身を正確に見せる」という問いには、描いた図だけの promo は画面の証拠にならない、という読みになる。他方で比較の数字に条件を添えた（UPLOAD.md）のは、Apple の「誤解させない」と同じ向き
- **無音・最初の数秒・ポスターフレーム**は、SNS の文献（[[promo]]）とも経験（冒頭 2 秒をサムネイルに焼き込んだ [[exp-gyazo-resumption-video]]、[[exp-democracy-river-video]]）とも揃う。Apple のポスターフレームの既定は 5 秒の位置で、最初のコマではない
- **fps の上限**: Apple のプレビューは最大 30fps。西尾の canvas の方式の promo は 60fps で出すことが多い（[[exp-nishio-showreel]]、[[exp-gyazo-resumption-video]]）。ストアに出すなら書き出し直しが要る
- **「架空のアカウント情報を見せよ」（2.3.9）**は、「実データを使え」という逆向きの助言と食い違って見える。Apple の決まりは実在の他人の個人情報を出さないためのもので、作品の挙動まで作り物にせよという意味ではない、と読める

## Open Questions

- 両社とも、プレビュー動画の有無や中身で何が変わったか（インストール率など）を、このページでは数字で出していない。効果は確かめられない
- Google の行動喚起の禁止は、動画の項では「Highly recommended」の下にある。動画の文字にも Metadata policy の規約として効くのかは、ページからは読み切れなかった
- 生成映像を「補助」として一部に使うことが、Apple の 2.3.4 で許されるのか（画面収録に重ねる「video overlays」に入るのか）は書かれていない

## Updates

### 2026-11-09 台本のファクトチェックから（[[explainer-script-factcheck-2026-11]]）

- 2.3.4 の「アプリ自身の画面収録だけ」は**プレビュー動画（App Previews）**の決まりで、App Store 全体の決まりではない。現行の Guidelines（Last Updated: October 16, 2026）には 2.3.14 の creative assets（"Creative assets allow you to highlight the value of your app in new ways compared to app-in-use screenshots and preview videos"）があり、ブランドや季節の企画を見せる画像・動画を置ける（iOS 27 以降。https://developer.apple.com/app-store/asset-best-practices/）
- プレビュー動画は既定で音なし、ナレーションと文字の重ねは可（2.3.4 "You can add narration and video or textual overlays"）
