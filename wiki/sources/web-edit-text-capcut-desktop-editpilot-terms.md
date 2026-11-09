---
type: source
summary: CapCut（ByteDance、運営は Bytedance Pte. Ltd.）のデスクトップ版の AI 編集機能（自動字幕からのフィラー検出と削除、文字起こしでの削除、長尺からの切り抜き、エージェントの EditPilot＝PC 版のみ・指示は英語推奨）と、利用規約（Last updated 2026-04-15）・プライバシーポリシー（同）・素材ライセンス（2026-01-22）の条文。規約は送った User Content に「非独占・無償・譲渡可能・再許諾可能・永続・全世界」のライセンスを取り、肖像を広告（sponsored content）に使う許諾まで含む。EU・英国の利用者にはこの節を適用しないが、日本の追加条項は除外していない。プライバシーポリシーは「保存や公開をするかに関わらず」作成時に事前アップロードしうると書き、機械学習モデルの学習を利用目的に挙げる
video_types: [promo, talk]
url: https://www.capcut.com/clause/terms-of-service
author: Bytedance Pte. Ltd.（CapCut の利用規約・プライバシーポリシー・素材ライセンス・製品ページ）
published: Terms of Service と Privacy Policy は Last updated 2026-04-15。Materials License Agreement は 2026-01-22
retrieved: 2026-11-09
sources:
  - https://www.capcut.com/clause/terms-of-service
  - https://www.capcut.com/clause/privacy
  - https://www.capcut.com/clause/materials-license-agreement
  - https://www.capcut.com/pricing
  - https://www.capcut.com/tools/edit-pilot
  - https://www.capcut.com/tools/filler-words
  - https://www.capcut.com/tools/long-video-to-shorts
  - https://www.capcut.com/tools/auto-caption-generator
---

# CapCut デスクトップ — AI 編集機能と、素材のライセンス条項

## 何の文献か

- ByteDance の CapCut の一次資料: 利用規約（英語版。日本語版の URL は空のページが返った）、プライバシーポリシー、素材ライセンス（CapCut Materials License Agreement）、料金ページ（日本からの取得で JPY 表示）、製品紹介ページ（tools/）
- 機能の説明は宣伝ページで、ヘルプセンターのような手順書は見つけられなかった。対応言語の一覧も公式ページで見つからなかった。規約は条文を読んだ
- [[web-genvid-seedance]] は CapCut 系の Dreamina と Seedance を扱い、「CapCut アプリ内の提供条件は読んでいない」と書いていた。このページはその穴を埋める

## 書いてあること

### AI に任せられると公式が書いていること（デスクトップ版）

- **フィラーの検出と削除**: 「Go to the Captions panel and open Auto captions. Select the language you need to generate and open the Identify filter words option. Click Generate」で文字起こしの中にフィラーが強調され、消すか手で直すかを選ぶ（tools/filler-words。原文は「filter words」と表記）。例は「um」「uh」「like」「you know」で「not a complete list」
- **文字起こしで編集**: 文字を消すと対応する映像が消える（resource/edit-video-with-text、検索結果の抜粋による）
- **長尺から切り抜き（AI Clip Maker／Long video to shorts）**: 「Let AI smart analysis identify video highlights and trim video clips automatically」、9:16 に変換、字幕を自動生成（tools/long-video-to-shorts）
- **EditPilot（エージェント）**: 「CapCut EditPilot is a video editing agent that helps you trim spoken clips, add captions, and clean up audio inside your desktop editor」。例: 間を詰める、フィラーを消す、長い発話の取りを短くする、字幕、ノイズ除去、色調整・映像のノイズ除去・高画質化・人物の補正。音楽・効果音・ステッカー・トランジション・フィルターを推薦する。**「EditPilot is part of CapCut for PC」「Write requests in English for the current experience, and work through one clear task at a time」**。結果はタイムラインで手で直せる（tools/edit-pilot）
- 自動字幕は「multiple languages」で、言語を自動判定すると書く（tools/auto-caption-generator）。日本語が対象かを明記した一覧は見つからなかった（デスクトップ版の UI に日本語があることは製品ページの言語切替から分かる）

### 料金（2026-11-09、日本から見た公式の料金ページ。「表示されている料金は参考情報です」）

| プラン | 月額 | 年額 | AI クレジット／月 |
|---|---|---|---|
| 無料版 | ¥0 | ¥0 | — |
| Pro | ¥2,700 | ¥21,800 | 800 |
| Ultra | ¥12,600 | （未確認） | 13,821 |
| Teams | ¥1,295／シート（2 シート〜） | — | 800／シート |

- Pro に Seedance 2.5（1 秒 $0.12 から、初月）・Seedance 2.0 Mini の生成が付く。Pro は 7 日の無料体験（クレジットカード不要）
- フィラー削除が無料で使えるかは公式の中で食い違う: tools/filler-words は「You can remove filler words ... for free with CapCut's trial」と書く（試用で無料という意味に読める）

### 利用規約（Terms of Service、Last updated 2026-04-15）の素材の条項

運営は Bytedance Pte. Ltd.（シンガポール）。対象に「CapCut Desktop version」を明記している。

- **User Content の定義**: 「content through the Services, including ... videos, sound recordings ... (including videos that incorporate locally stored sound recordings from your personal music library and ambient noise) uploaded to, or otherwise made available through, the Services」
- **秘密にならない**: 「All User Content will be considered non-confidential. You must not upload or make available any User Content ... that you consider to be confidential or proprietary to any other person」
- **ライセンス**: 「We don't own your User Content ... By submitting User Content via the Services, you grant to the Company and its affiliates a non-exclusive, royalty-free, transferable, sub-licensable, perpetual and worldwide license to use your User Content. This license ... allows us to modify, adapt, reproduce, make derivative works of, display, publish, transmit, distribute and/or store your User Content for the purposes of operating, developing and providing the Services, subject to your Platform settings」
- **名前・肖像**: 「You further grant us and our affiliates, agents, services providers, partners and other connected third parties a royalty-free fully transferable (including sub-licensable), worldwide license to use your username, image and likeness to identify you as the source of any of your User Content, including for use in sponsored content」
- 音源の録音・楽曲の複製と公衆送信を含む無償の許諾で、作曲者が PRO（JASRAC のような団体）に属するなら、この無償許諾を団体に知らせる義務を負う、と書く
- **権利の放棄**: 「you waive any rights to prior inspection or approval of any marketing, advertising or promotional materials related to such User Content」、パブリシティ権と人格権を（法の許す範囲で）放棄する
- 「We, or authorised third parties, reserve the right to cut, crop, edit or refuse to upload your content」
- **地域の例外**: EU・英国の追加条項は「The paragraphs under "User-Generated Content" of Section 10 shall not apply」とする。**日本の追加条項（変更の通知・クラウド容量・責任制限・準拠法は日本法と東京地裁）は、この節を除外していない**。ブラジルは別の短い許諾に置き換えている
- **外部の AI**: 一部の機能は Runway・Stable Diffusion・Google・YouTube・FLUX・Luma などの技術と API を使い、その提供者の条件にも従う
- **CapCut の素材（Company Content）**: テンプレート・映像・画像・ステッカー・フォント・効果音・エフェクトなど。商用に使えるかは素材ライセンスによる。素材ライセンス（2026-01-22）は、多くは「personal and non-commercial use」に限られ、「commercial use」の印が付いた Dual Use Materials だけが限られた商用利用を許すと書く。録音物・楽曲は規約か素材ライセンスが明示しない限り許諾しない
- Feedback には無制限のライセンス

### プライバシーポリシー（Last Updated 2026-04-15）

- User Content は「the content you create, import, upload, or generate through the Services」で、AI に送ったプロンプト・ファイルと AI の応答を含む
- **「We may collect User Content through pre-uploading at the time of creation, import, or upload, regardless of whether you choose to save or publish that User Content, for example, to recommend audio options, generate captions」**
- 映像・音声から物体・風景・顔と体の位置・音の性質・話された言葉の文字（自動字幕を使った場合）を取得しうる。顔と体の情報で本人を識別はせず、エフェクトの適用後に消す
- 利用目的に「train, test, and improve technology, such as machine learning models and algorithms」がある。opt-out の手続きの記述は見つけられなかった

## この wiki への含意

- **会社の素材・未公開の作品の画面・第三者が映る講演は、CapCut に入れない方がよい**、という根拠が条文にある。規約は User Content を「non-confidential」とし、秘密のものを上げるなと書き、永続・譲渡可能・再許諾可能のライセンスと肖像の広告利用を取る。プライバシーポリシーは保存・公開しなくても作成時に事前アップロードしうると書き、機械学習の学習を目的に挙げる。この wiki の「置かないもの」（会社の内部情報、第三者の個人的な情報）と CyEC2 の決まりに照らすと、少なくとも業務の素材には使えない（担当の判断。西尾が決めること）
- デスクトップ版で「端末内だけで処理される」と書いた箇所は見つからなかった。ローカルの編集でもどこまでが送られるかは、規約とポリシーからは区別できない
- 機能の面では、フィラー検出・切り抜き・EditPilot は [[exp-shortmovie-draft-generator]] の「長尺 → 切り抜きの下書き」を製品の中でやる。ただし EditPilot は英語の指示が前提で、選択の基準を外から渡す仕組み（shortmovie-draft-generator のプロンプトのような）は見当たらない
- CapCut の素材（テンプレ・BGM・ステッカー）は既定で非商用。発信物に使うなら「commercial use」の印を 1 つずつ確かめる。音楽の扱いは [[web-rights-jasrac-nextone-ugc-music]] と合わせて見る

## 何を AI に任せられるか／何が人に残るか

- **任せられる（公式の製品ページ）**: 自動字幕、フィラーの検出と削除、文字起こしでの削除、長尺からのハイライトの選択と縦化、ノイズ除去、EditPilot による一連の編集（英語の指示）、BGM・効果音・トランジションの推薦
- **人に残る（公式）**: フィラーを消すか直すかの判断（「choose whether to delete or manually adjust」）、EditPilot の結果の再生と確認（「Check each cut to make sure the speaker's meaning stays intact」「check the final cut before you export it yourself」）。規約の上では、入力の権利の確保と出力が他者の権利を侵さないことの確認は利用者の責任
- 実例で確かめたものはこの wiki に無い。日本語の自動字幕・フィラー検出の精度は公式ページに無い

## 着手の仕方（未検証。galleria で確かめる）

- **何が表現できるようになるか**: 自分で撮った公開してよい素材（私物の画面収録・自分だけが映る話）から、自動字幕と切り抜きの縦動画を短時間で作る。効く型: promo（SNS の縦の切り抜き）
- **機械**: galleria Windows か Mac（デスクトップ版。EditPilot は「CapCut for PC」とあり、Mac 版で使えるかは書かれていない）
- **入れるもの・費用・アカウント**: CapCut デスクトップ（capcut.com からダウンロード）。**要: アカウント（AI 機能・書き出しにログインが要る可能性が高い。推測）**。Pro ¥2,700／月（7 日の無料体験あり）。**規約の素材ライセンスに同意することになるので、使うか自体を西尾が決める**
- **成熟度**: 規約・ポリシーは 2026-04 に改定。EditPilot の公開日は書かれていない
- **最小の手順（GUI。製品ページの手順から）**:
  1. 公開済みか公開してよい自分の素材（1〜3 分、日本語の話）だけを使う
  2. 「+」で取り込み → タイムラインに置く
  3. Captions パネル → Auto captions → 言語を選ぶ → 「Identify filter words」を入れる → Generate
  4. 強調されたフィラーを確認し、消す
  5. （英語の指示で）EditPilot に「remove filler words and shorten long pauses」と頼む
  6. Export
- **動いたと言える確かめ方**: 手順 3 で日本語の字幕トラックができ、フィラーが強調される（強調が 0 件なら、日本語のフィラー検出が効いていない可能性を記録）。手順 4〜5 の後、書き出しの duration が元より短い（ffprobe）。字幕の誤認識の数を 1 分あたりで数えて記録
- **所要の見込み（推測）**: 導入 15 分、1 本 30 分

## Open Questions

- 日本語の利用者に対する規約の日本語版（`/ja-jp/clause/terms-of-service` は空のページだった）が、英語版の User-Generated Content の節と同じ内容か
- デスクトップ版のローカル編集で、どの処理（自動字幕・フィラー検出・EditPilot）がサーバーに送られるか。プライバシーポリシーの「pre-uploading ... regardless of whether you choose to save or publish」がデスクトップ版のどの操作に当たるか
- 規約のライセンスは「subject to your Platform settings」と書くが、どの設定が範囲を狭めるのかは書かれていない
- 機械学習の学習への利用を断る設定（opt-out）があるか
- 自動字幕の対応言語の公式な一覧と、日本語のフィラー検出の対象語
