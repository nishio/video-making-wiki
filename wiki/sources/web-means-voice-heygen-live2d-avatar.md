---
type: source
summary: アバターの要点だけ（2026-11-09 時点の公式ページ）。HeyGen は月 $29 の Creator から本人の映像と声の「Custom Video Avatar」、無料は月 3 本で透かし入り。本人の映像の分身（digital twin）は同意の録画が必須で、写真や文から作る分身には同意の確認が無い（HeyGen 自身が「許可ではない」と書く）。Live2D の使用許諾は、直近の売上 1,000 万円以上の事業者の出版に出版許諾契約を求め、企業の活動は非営利と認めない
video_types: [promo, talk, embed]
url: https://developers.heygen.com/docs/avatar-consent
author: HeyGen（公式の価格表・開発者ドキュメント・ヘルプ）、Live2D Inc.（使用許諾契約書）
published: unknown（HeyGen のページに日付なし。ヘルプは「Updated over a week ago」）
retrieved: 2026-11-09
sources:
  - https://www.heygen.com/pricing （Free・Creator・Pro のプラン）
  - https://developers.heygen.com/docs/avatar-consent.md （Avatar Consent。3 段階のアクセス）
  - https://help.heygen.com/en/articles/12092609-recording-your-consent-video （同意の録画の要件）
  - https://www.live2d.com/eula/live2d-proprietary-software-license-agreement_jp.html （Live2D Proprietary Software 使用許諾契約書）
  - 探索の手がかり: Web 検索（HeyGen の同意の要件。ヘルプ記事と開発者ドキュメントを一次資料として読んだ。30 秒か 35 秒かは記事で食い違うと検索結果が指摘）
---

# アバター: HeyGen の分身と同意、Live2D の使用許諾（要点だけ）

## 何の文献か

- HeyGen の価格表・開発者ドキュメント・ヘルプ記事と、Live2D の使用許諾契約書（一次資料）。深追いしていない。VTuber 用の道具（VTube Studio・VSeeFace・Warudo など）の規約は読んでいない

## 書いてあること

### HeyGen

**プラン**（pricing ページ、月払い）

| プラン | 月額 | 要点 |
|---|---|---|
| Free | $0 | 「3 videos a month, watermarked」、Avatar IV と Video Agent、「One Custom Video Avatar, plus 500+ ready-made presenters」 |
| Creator | $29 | Avatar III・IV、Avatar V（制限つき）、600 credits、1080p、「Custom Video Avatar with your own voice and likeness」 |
| Pro | $49 | 1,000 credits、4K、Cinematic Avatars、Avatar V、1 本 30 分まで |

**同意**（開発者ドキュメント「Avatar Consent」）

- 本人の映像から作る分身（digital twin）で動画を作る前に「HeyGen needs proof that the person depicted agreed to be cloned」
- 3 段階: (1) ウェブカメラで本人が同意文を読む（全顧客）、(2) 録画済みの同意動画をアップロード（Enterprise のみ）、(3) 補償契約を結んだ Enterprise は同意の手続きを省ける
- **写真や文（prompt）から作る分身には同意の API の手順が無い**。ただし「A photo avatar is still built from a real person's image. Having no API step to complete is not permission to use someone's likeness. HeyGen runs no consent check and keeps no consent record for a photo avatar」— 同意を得て記録を残すのは利用者の責任
- ヘルプ記事: 同意の文は「read it exactly as written」、「Keep the video under 30 seconds」、同意の動画はアバターの映像と「at the same time」に録って出す。本人が離れていれば QR コードから本人のスマホで録れる
- HeyGen は OSS の HyperFrames の開発元で、その docs は HeyGen の声とクローンへの導線を含む（[[web-opus2-hyperframes-after-2026-09-22]]）

### Live2D（Live2D Proprietary Software 使用許諾契約書）

- 「出版」は派生作品を「個人的、内部的、営利、非営利またはその他のいかなる形であれ」公開・共有することで、該当するかは Live2D 社の裁量（1 条）
- 「非営利」の定義: 「企業による活動、およびその依頼による、または、その利益のためにする活動は、たとえ活動の主体が個人や団体であっても非営利とは認められません」
- 派生作品の出版には原則「Live2D 出版許諾契約書」が要る（2.1）。**一般ユーザーと小規模事業者（直近売上高 1,000 万円未満）と適格教育機関は免除されうる**（2.2）。中規模（1,000 万〜1 億円）・大規模（1 億円以上）は事業規模で契約料が決まる。実質的に運営している企業がある場合はその企業の売上で判定（1.25）
- 中規模以上の「特定のプロモーションを目的とした一時的な出版」には「Live2D 著作物シンプルライセンスプラン」が適用される場合がある（事前申請と承認が要る。2.4）
- 「拡張性アプリケーション」（例: アバター、配信アプリ、動画生成ツール）は別の条件で、免除の対象外

### VTuber 用の道具（名前だけ）

- galleria-wiki は人物を動かす経路を「音声駆動・駆動動画・mocap・実時間操作」に分け、Live2D を実時間操作に置いた（[[exp-qualia-h3-live2d-galleria]]）。PuppetLoom はレイヤー PSD からの 2D パペットで、マイク口パクや顔トラッキングを入力にできる（[[exp-puppetloom]]）。VTube Studio・VSeeFace などの規約・版はこの調査では読んでいない

## この wiki への含意

- **HeyGen の分身は「本人の映像と声で、話す動画を台本から作る」商用の完成品**。経験の H3（音声と映像の一体生成、[[exp-qualia-h3-live2d-galleria]]）と同じ側で、違いは本人の実写を使うこと。talk で「西尾本人が画面で話す解説」を撮影なしで作れるが、**西尾の顔と声を先方に預ける**ことになる（西尾が決めること）
- **Live2D の条文は、どの名義で出すかで結論が変わる**: 西尾個人（一般ユーザー）なら免除されうるが、会社の業務として出す動画（企業の活動）は「非営利と認められない」うえ、事業規模は会社の売上で判定される。[[exp-qualia-h3-live2d-galleria]] の Live2D 試作が「8 秒の見せ場には初期工数が重い」だったことに加え、**会社名義の発信に Live2D のモデルを使うなら出版許諾契約の確認が要る**（ただし、この契約書が Cubism Editor で作ったモデルを録画した動画に及ぶかは、この調査では決められなかった）
- [[exp-qualia-h3-live2d-galleria]] の「Live2D の価値は、同じキャラクターの長期運用、台詞の差し替え、撮り直し、実時間制御で大きくなる」は、アバターを道具として選ぶ判断基準としてそのまま使える。単発の promo には HeyGen・H3 のような生成側、シリーズの talk には Live2D・PuppetLoom のような組み立て側
- 型: promo（人物が話す見せ場）、talk（話し手が画面にいる解説）、embed（講演の中で流す、人物が話す短い映像）。[[exp-qualia-video]] の「解説動画は静止が既定」と両立するかは未検証

## 着手の仕方（未検証。galleria で確かめる）

- **何が表現できるようになるか**: 撮影なしで「本人が画面で話す」解説・紹介の短い動画。型は talk・promo
- **機械**: どこでも（ブラウザ）。**要: HeyGen のアカウント**。費用: Free（月 3 本・透かし）で試せる、透かしなしは Creator $29/月。利用条件: 本人の分身は同意の録画が必須
- **成熟度**: 価格表に Avatar V（最新、制限つき）。更新は続いている
- **最小の手順**: Free で、本人の映像（ヘルプ記事の撮影の指針に従う）と同意の録画を同時に出し、[[exp-qualia-video]] の比較用原稿の 30 秒ぶんを台本にして 1 本作る（手順は HeyGen の UI。コマンドは無い）
- **動いたと言える確かめ方**: (1) 透かし入りの MP4 が出る。(2) 人が通常視聴で、口・視線・頭の動きの自然さと、日本語の読みの正しさを記録する（[[exp-qualia-h3-live2d-galleria]] の「知覚的整合性」と「記号的正確さ」の両方）
- **所要の見込み（推測）**: 撮影と同意を含めて 1〜2 時間
- **西尾が決めること**: 自分の顔と声を外部に預けるか、どの名義で使うか

## Open Questions

- HeyGen の同意の録画の長さ（ヘルプ記事は「under 30 seconds」、検索結果によればエラーコードの記事は 35 秒と書く。後者は読んでいない）
- HeyGen の生成物の権利と、AI 生成の開示の扱い（利用規約は読んでいない）
- Live2D の使用許諾契約書（Proprietary Software）が、Cubism Editor で作ったモデルを録画して動画にする場合に「出版」としてどう扱われるか。Cubism Editor 本体の契約・FAQ は読んでいない
- VTube Studio・VSeeFace などの商用利用の条件（未読）
