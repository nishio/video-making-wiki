---
type: source
summary: Mac 専用の画面収録アプリ Screen Studio の公式サイトとガイド（2026-11-09 取得、changelog の先頭は 4.1）。カーソルを映さずに画面を録り、マウスの動きのデータを別に記録して後から合成するので、カーソルの平滑化・大きさの変更・クリック位置への自動ズームを録った後に直せる、と説明している。料金は月 $29（年払いなら月 $9）、書き出しは MP4 で 4K・60fps まで。Windows 版の予定は無い
video_types: [promo, talk, embed]
url: https://screen.studio/
author: Adam Pietrasiak（Screen Studio の開発者、公式サイト）
published: unknown（公式サイトとガイド。changelog の先頭は Screen Studio 4.1、日付は取れなかった）
retrieved: 2026-11-09
sources:
  - https://screen.studio/（トップ。料金・FAQ を含む）
  - https://screen.studio/guide/auto-zoom
  - https://screen.studio/guide/cursor
  - https://screen.studio/guide/system-requirements
  - https://screen.studio/guide/explanation-of-export-settings
  - https://screen.studio/guide/extracting-raw-recording-files
  - https://screen.studio/changelog
---

# Screen Studio（Mac）— カーソルを別に記録して後から合成する収録アプリ

## 何の文献か

- 開発者自身の公式サイト・ガイド・changelog。販売ページなので、効果（見る人が引き込まれる等）は宣伝の主張として読む。比較・測定の数字は無い
- 「自動ズーム・カーソル強調」の収録アプリの元祖として扱われ、OSS の代替が「Screen Studio alternative」と名乗っている（[[web-means-capture-openscreen]]、[[web-means-capture-focusee-recordly]]、[[web-means-capture-ffmpeg-zoompan-screenstudio-alt]]）。仕組みの説明を一次資料で押さえるために読んだ

## 書いてあること

### 仕組み（トップの FAQ）

- 「It records your screen, ignoring the mouse cursor, and then adds the cursor back in the final video. This is possible because Screen Studio records precise mouse movement data and synchronizes it with the recorded video」
- 「Thanks to this, it can apply many effects after the video is recorded, such as making mouse movement smooth, changing cursor size and shape, etc. Most screen recording apps record your screen with the mouse cursor, making it impossible to apply cursor effects after the recording is done」
- 収録は「ScreenCaptureKit, the system's own capture」、書き出しは「your Mac's media engine」で行う、と書く

### 自動ズーム（ガイド「Auto Zoom」、トップ）

- 「The Auto zoom option focuses on the areas where clicks occurred during your recording. It automatically detects the click positions and zooms in on those areas」
- 「if you add auto-zoom where no mouse click occurs, it will not zoom to any area. In this situation, you'll need to choose manual zoom」。ズームは Auto と Manual を 1 つずつ選べる
- トップでは「Screen Studio looks at what you did while recording, like where you clicked, and zooms in on the moments that matter」「Zooms are balanced so your webcam never covers the cursor」。ズームの種類は Classic と Loupe。縦横比を変えると「Zooms re-aim」

### カーソル（ガイド「Cursor」）

- 後から変えられる設定: 隠す、大きさ、種類（macOS／Touch）、常にシステムの標準カーソル、**動いていないときに隠す**、**ループ用に終わりで初めの位置に戻す**（「You can use this option to create a perfect loop」）
- Advanced: 動きに合わせて傾ける、終わりの前にカーソルの動きを止める（「avoiding unwanted captures like stopping the recording」）、手ぶれの除去、カーソルの種類の頻繁な切り替えを抑える
- トップ: 「Optics-based motion blur」

### 書き出し（ガイド「Explanation of export settings」、トップ）

- MP4 で 720p・1080p・4K、最大 60fps。GIF は 1080p まで、「We do not recommend creating GIFs that are longer than 1 minute」
- 「a 4K resolution export will take four times longer than exporting the same project in HD」。圧縮率は書き出しの時間に影響しない、と書く
- 生の素材（画面・カメラ・マイク）は Export → 「Extract raw recording files…」で取り出せる

### 料金・条件（トップ、2026-11-09 時点）

- 年払い **月 $9**（「Save 69%」）、月払い **月 $29**。どちらも全機能、「Export up to 4K at 60 fps」、共有リンク、クラウドの文字起こし。学生・教員は 40% 引き。以前の買い切りは新規販売していない
- 無料の試用の有無・透かしの有無は、取得したページの本文には書かれていなかった（第三者の screenstudio-alt の README は「paywalled on export」と書く。未確認）
- 「Is the Windows version ready? No, and there are no near-future plans to add Windows support」
- 動作環境: macOS Ventura 13.1 以降、Apple M1 以降を推奨（Intel は MacBook Pro 2018 以降など）、RAM 8GB 以上
- プライバシー: 「Screen Studio never sends data about your recordings to servers」。文字起こしなどの AI 機能は「done locally on your computer」と書く（ただし料金表には「Cloud transcript」もある。どちらがどの機能かは本文からは分からない）

## この wiki への含意

- **「カーソルを録らずにデータで持つ」が、この種のアプリの核**。Playwright の showActions（[[web-means-capture-playwright-screencast]]）が録画の中にカーソルを描き込むのとは逆で、録った後に直せる。OSS の代替（OpenScreen の `--cursor editable-overlay`、screenstudio-alt の events-log）も同じ設計を取っている
- **自動ズームの根拠はクリックだけ**。Screen Studio 自身が「クリックの無い所では寄らない」と書く。Playwright で CDP から操作すると OS のクリックが起きないので（推測）、Screen Studio の自動ズームは効かない。台本で動かすなら、寄る位置は台本の側から渡すしかない（[[web-means-capture-ffmpeg-zoompan-screenstudio-alt]]）
- **「ループ用にカーソルを初めの位置に戻す」「止まっているカーソルを隠す」は embed（流しっぱなし）に効く**。会場で繰り返し流す 10〜20 秒のループを、継ぎ目でカーソルが飛ばずに作れる。howseen の「ループの継ぎ目を位置と速度の両方で確かめる」（[[web-opus-howseen-claude-motion-design]]）と同じ問題への、アプリ側の答え
- **西尾の機械では Mac でしか使えない**。galleria（Windows）での自動ズームは OpenScreen・Recordly・FocuSee・Cap（[[web-means-capture-cap]]）から選ぶ
- 手で操作して撮る方式なので、台本どおりの再現性はない。撮り直すと毎回カーソルの道筋が変わる。「作品が変わったら撮り直す」promo には、操作を台本にする Playwright・VHS のほうが向く（[[web-promo2-vhs-shot-scraper-demos-as-code]]）。Screen Studio が向くのは、手で触って見せたい一回きりのデモ（デスクトップアプリ、iPhone のミラーリング）

## 着手の仕方（未検証。Mac で確かめる）

- **表現できるようになること**: 手で操作した画面収録に、クリック位置への滑らかなズーム、平滑化したカーソル、背景と枠、カメラの重ねを、録った後の編集で付ける。効く型: promo（作品の実画面）、embed（ループ）、talk（話し手のカメラ付き）
- **機械**: Mac（Apple Silicon の MacBook）。galleria では使えない
- **入れるもの・費用**: Screen Studio の現行版（サイトの Download for Mac）。**要: 費用（月 $29 か年 $108）とアカウント（購入のメール）**。西尾が決める。利用規約（Terms of Service）は読んでいない。撮った動画の商用利用の制限の記述は、読んだページには無かった
- **成熟度**: changelog の先頭が 4.1（3.0.0 → 4.1）。開発は続いている
- **最小の手順**: 公式ガイドの順（GUI）: 権限（画面収録・アクセシビリティ）を許可 → New Recording でウィンドウを選ぶ → 操作 → 停止 → タイムラインの Zoom を Auto のまま確認 → Export で MP4・1080p・30fps（X に出すなら 30fps。[[web-x-video-ads-best-practices]]）
- **動いたと言える確かめ方**: 書き出した MP4 で、クリックした場面ごとに寄りが入っている。`ffprobe` で 1920×1080・30fps。Extract raw recording files で取り出した素の画面録画にカーソルが映っていなければ、FAQ の「カーソルを録らない」が確かめられる
- **所要の見込み（推測）**: 30 秒のデモで、撮影 10 分、編集 15 分

## Open Questions

- 無料の試用と、試用中の書き出しの制限（透かし・回数）の公式の記述
- 「Cloud transcript」と「AI 機能はローカル」の関係
- 自動ズームの寄り方（倍率・速度・カメラの減衰）の数値は公開されていない。OSS（screenstudio-alt の cosine ease など）と見比べるには実物を見るしかない
