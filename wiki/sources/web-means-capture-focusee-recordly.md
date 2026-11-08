---
type: source
summary: Windows でも動く自動ズーム・カーソル強調の画面収録アプリ 2 つの一次資料。FocuSee（iMobie、商用、Windows 10 以降・macOS）は「クリックと入力の区間を追って自動でズーム」、試用は 1 本だけ 4K で書き出せ、年 $49.99〜（2026-11-09 の表示価格）、AI 機能はクレジット消費。Recordly（AGPLv3、v1.4.0 2026-09-08）は OpenScreen から分かれた OSS で、Windows は Windows Graphics Capture で録り、カーソルの動きからズームを「提案」する。どちらも GUI で、CLI は書かれていない
video_types: [promo, talk, embed]
url: https://focusee.imobie.com/
author: iMobie（FocuSee の販売元、公式サイト）／webadderall ほか（Recordly の README）
published: unknown（FocuSee のサイト）／Recordly v1.4.0 は 2026-09-08
retrieved: 2026-11-09
sources:
  - https://focusee.imobie.com/（トップと FAQ）
  - https://focusee.ai/pricing.htm?os=others（store.php からの転送先。料金表と FAQ）
  - https://focusee.ai/specs.htm（動作環境）
  - https://github.com/webadderallorg/Recordly/blob/main/README.md
---

# FocuSee と Recordly — Windows で使える自動ズームの収録アプリ

## 何の文献か

- **FocuSee**: 中国のソフト会社 iMobie の販売サイト。販売ページなので、効果の主張は宣伝として読む。価格は割引表示（元値に取り消し線）で、時期で変わりうる
- **Recordly**: OSS の README（star 約 36,000、AGPL-3.0）。「Recordly originally started as a fork of OpenScreen. Over 80% of code has diverged since」と書く（[[web-means-capture-openscreen]]）
- どちらも測定の数字は無い

## 書いてあること

### FocuSee（公式サイト、料金表、動作環境）

- 「FocuSee is an AI-powered screen recorder with auto zoom effects. After you record your screen, FocuSee automatically adds zoom on clicks, mouse movement tracking, cursor highlighting, silence removal, AI audio enhancement, and dynamic camera」
- 「Auto zoom follows clicks and typing sections to emphasize key actions ... no manual keyframing needed」。カーソルに合わせた 3D の傾き（3D Motion）。既存の動画を読み込んで効果を付けることもできる。iOS・Android を USB で繋いで録れる
- 「Is FocuSee available on Mac and Windows? Yes」。動作環境は Windows 10 以降、macOS 10.15 以降（12.3 以上で最適）、RAM 8GB 以上
- **試用**: 「FocuSee offers a free trial that allows you to explore standard features and export one high-quality video in up to 4K resolution for free. Some advanced AI-powered features require a subscription and credits to use」
- **料金（2026-11-09 の表示）**: Standard 年 $49.99（元値表示 $179.99）、月 $19.99。Advanced 年 $79.99（年 3,600 クレジット）、月 $24.99（月 300 クレジット）、買い切り $199.99（2.x の永続利用、1,000 クレジットは 1 年有効、最大 5 台）。どの版も 4K・60fps、透かしの除去あり。AI の字幕・無音除去・声の補正・アバターはクレジットを消費
- 買い切りは「use the current version (e.g. Version 2) forever, but upgrading to the next major version (e.g. Version 3) comes at an additional upgrade cost」。返金は年・買い切り 60 日、月 7 日（使った AI クレジットの分は引く）
- 有効化は「sign up and log into your account using the email you entered when purchasing」

### Recordly（README）

- 対応: macOS 14.0 以降、Windows 10 Build 19041 以降、Linux。「Windows uses a native Windows Graphics Capture (WGC) helper on supported builds, with native WASAPI audio support」。Linux は「Cursor hiding is not supported on Linux today」
- 「Recordly can automatically emphasize activity with zoom suggestions, smooth cursor movement, add motion effects」。タイムラインには「Use automatic zoom suggestions based on cursor activity」
- カーソル: 描画したカーソルの表示・非表示、大きさ、平滑化、モーションブラー、クリックの跳ね、揺れ、「Cursor loop mode for cleaner looping exports」
- 書き出しは MP4・GIF。プロジェクトは `.recordly`（素材のパスと編集の状態）
- 仕組み: 収録は Electron が取りまとめ、合成は PixiJS、「The same scene logic used in preview is rendered into exported MP4 or GIF output」
- 拡張（Marketplace）で、クリック音・端末の枠・ブラウザの枠などを足せる
- CLI・自動化の記述は README に無い。ライセンスは GNU AGPLv3

## この wiki への含意

- **Windows の GUI で手早く寄りを付けるなら、どちらも候補**。ただし西尾の制作は Claude Code が台本とコードで回す形で（[[exp-html-capture-pipeline]]）、GUI での手作業は THINKLET の Premiere の 1 件だけ（[[exp-thinklet-reading-demo-video]]）。CLI で回せない FocuSee・Recordly は、人（西尾）が手で操作して撮る場面に限られる。台本で回すなら OpenScreen（CLI あり）か、自分で寄りを描く（[[web-means-capture-ffmpeg-zoompan-screenstudio-alt]]）
- **FocuSee の「入力の区間でも寄る」**は、クリックしかしない Screen Studio（[[web-means-capture-screen-studio]]）との違いとして書かれている。文字を打つ場面の多いデモ（検索・プロンプト入力）では効きうる（未確認）
- **FocuSee の AI 機能はクレジット課金で、どこで処理されるかは読んだページに無い**。作品の画面に未公開の内容や個人情報があるなら、送られる先を確かめる前に AI 機能を使わない
- **Recordly の「ループ用のカーソル」**は Screen Studio と同じく embed（流しっぱなしのループ）に効く
- どちらも出力は普通の MP4 なので、最後の仕上げ（文字の重ね、ラウドネス）は西尾の方式で後から足せる

## 着手の仕方（未検証。galleria で確かめる）

- **表現できるようになること**: 手で操作した Windows の画面収録に、クリック・入力に合わせた自動ズーム、カーソルの平滑化、背景と枠、カメラの重ねを GUI で付ける。効く型: promo、talk、embed
- **機械**: galleria Windows（どちらも）
- **入れるもの・費用・アカウント**:
  - FocuSee: 公式サイトのインストーラ（版はサイトに明記なし、2.x）。**試用は 1 本だけ書き出せる。続けるなら要: 費用（年 $49.99〜）とアカウント**。利用規約は読んでいない
  - Recordly: GitHub Releases の v1.4.0 の Windows 版。費用 0。AGPLv3（使って撮るだけなら動画には及ばない、と読むのが普通だが条文は読んでいない）
- **成熟度**: FocuSee は商用で 2.x。Recordly は 2026-09 の v1.4.0 が最新の正式版で、その後は beta が無い（最終 push は 2026-11-08）
- **最小の手順**: どちらも GUI。ウィンドウを選んで録画 → 30 秒、クリックと文字入力を数回 → 停止 → エディタで自動ズーム（FocuSee は自動で付く、Recordly は「zoom suggestions」を採用）→ MP4・1080p・30fps で書き出す
- **動いたと言える確かめ方**: 書き出した MP4 を `ffmpeg -i out.mp4 -vf fps=2,scale=480:-1,tile=6x5 sheet.png` で 1 枚のコンタクトシートにし、クリックと入力の場面で寄っているかを見る。FocuSee の試用版の書き出しに透かしが出るかも記録する
- **所要の見込み（推測）**: 導入 10 分、1 本 20 分

## Open Questions

- FocuSee の試用の 1 本に透かしが入るか（料金表に「Remove Watermark」の行があり、試用で付くかの記述は無い）
- FocuSee の AI 機能の処理場所（端末かクラウドか）とデータの扱い
- Recordly の「zoom suggestions」の根拠がクリックかカーソルの動きか（README は「based on cursor activity」とだけ書く）
- 両者とも、Playwright で CDP から動かした操作に自動ズームが付くか（OS の入力が起きないので付かないはず。推測）
