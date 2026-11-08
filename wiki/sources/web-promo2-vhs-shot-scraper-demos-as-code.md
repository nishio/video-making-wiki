---
type: source
summary: 開発者向けツールのデモの画を「コードで書いて、実物を動かして撮る」道具の一次資料 2 つ。Charm の VHS（端末の操作を .tape に書き、実際のコマンドを実行して GIF/動画にする。CI で作り直し、テキスト出力を golden file にして結合テストにも使う）と Simon Willison の shot-scraper（文書のスクリーンショットが実物からずれるのを、YAML と GitHub Actions で撮り直して防ぐ）。GitHub に動画を置くときの容量の上限も添える
video_types: [promo, embed]
url: https://github.com/charmbracelet/vhs
author: Charm（charmbracelet/vhs の README）／Simon Willison（個人ブログ）／GitHub Docs
published: 2022-10-14（Simon Willison の記事）／VHS の README は unknown（2026-11-09 に main を取得）
retrieved: 2026-11-09
sources:
  - https://github.com/charmbracelet/vhs（README.md、raw を取得）
  - https://simonwillison.net/2022/Oct/14/automating-screenshots/（「Automating screenshots for the Datasette documentation using shot-scraper」2022-10-14）
  - https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/attaching-files（GitHub Docs「Attaching files」）
---

# VHS と shot-scraper: デモの画をコードで書き、実物を動かして撮る

## 何の文献か

- **VHS**: 端末アプリの会社 Charm が出している OSS の README。道具の作者による説明なので、効果の測定はない
- **shot-scraper**: Datasette の作者 Simon Willison の個人ブログ。自分の作った道具を自分の文書に使った手順の記録
- **GitHub Docs**: GitHub の公式ドキュメント。2026-11-09 時点の公式ページによる（更新日の表示なし）

## 書いてあること

### VHS（charmbracelet/vhs README）

- 一行目: 「Write terminal GIFs as code for integration testing and demoing your CLI tools」
- `.tape` ファイルに命令を並べる: `Output demo.gif`、`Set FontSize 46`、`Set Width 1200`、`Type "echo 'Welcome to VHS!'"`、`Sleep 500ms`、`Enter`、`Sleep 5s`。VHS は仮想の端末でこれを実行して撮る
- `Wait /regex/`: 画面（または行）に正規表現が現れるまで待つ。既定は `/>$/`、時間切れは 15 秒。処理の長さが変わっても、終わってから次へ進める
- `Hide` / `Show`: 撮らずに実行する区間。「performing any setup and cleanup required to record a GIF, such as building the latest version of a binary and removing the binary once the demo is recorded」
- **CI**: 「You can hook up VHS to your CI pipeline to keep your GIFs up-to-date with the official VHS GitHub Action」
- **結合テスト**: 「Use the `.txt` or `.ascii` output to generate golden files. Store these files in a git repository to ensure there are no diffs between runs of the tape file」。同じ `.tape` がデモの画とテストの期待値の両方になる

### shot-scraper（Simon Willison、2022-10-14）

- 問題: 「It's very easy for feature screenshots in documentation for a web application to drift out-of-date with the latest design of the software itself」
- 撮る対象を YAML（`shots.yml`）に URL・幅・高さ・出力名で並べ、`shot-scraper multi shots.yml` で一度に撮る。CSS セレクタで一部だけ切り出し、余白を足せる
- 撮る前にページで JavaScript を実行できる。記事では表の行を先頭 2 行だけ残して撮った——見せたい所だけに絞るための加工を、実物のページの上で行う
- 例には実在の公開データ（英国の議員の利益登録簿の検索結果）を使った
- GitHub Actions で、`shots.yml` を commit すると撮り直して同じ repo に書き戻す。高解像度版と通常版を撮り、`oxipng` で圧縮する。「simply committing a change to the `shots.yml` file is enough to generate and store the new screenshots」

### GitHub に置くときの上限（GitHub Docs「Attaching files」）

- 画像と GIF は 10MB、動画は無料プランの repo で 10MB、有料プランで 100MB
- 動画は `.mp4` `.mov` `.webm`。「Video codec compatibility is browser specific ... we recommend using H.264」
- このページは Issue・PR・コメントへの添付の説明で、README に動画を埋める方法は直接は書いていない（README での扱いはこのページでは確かめていない）

### AI について

- どの資料にも、AI 生成の映像についての記述はない

## この wiki への含意

- **コードで描くのとは別の「コードで撮る」**: この wiki の経験の方式（[[exp-html-capture-pipeline]]）は、HTML と canvas で画を描き、それを撮る。VHS と shot-scraper は、画を描かず **作品そのものを台本どおりに動かして撮る**。作品の中身を正確に見せる、という西尾の条件には、描く方式より直接に応える。台本（`.tape`、`shots.yml`）が git に入り、作品が変われば撮り直せる点は、西尾の方式の「台本と描画が git にあり何度でも書き出せる」と同じ利点を持つ
- **デモがテストになる**: VHS の golden file は、デモの画と作品の挙動を同じ台本で縛る。偽のデモ（[[web-promo2-gemini-nikola-staged-demos]]）の逆で、画に映るものが実際に動いた結果であることを、作る側で確かめ続けられる
- **見せたい所に絞る加工は、作品の上でやる**: shot-scraper は撮る前に JavaScript で余計な行を消す。これは Apple の「ズームでなく元の解像度で」（[[web-promo2-apple-app-previews-google-play-video]]）や、Derek Lieu の「情報を詰め込むな」（[[web-promo2-derek-lieu-game-trailers]]）と同じ方向の加工だが、描き直しではなく実物を絞る
- **embed への効き**: 数秒〜数十秒の端末の操作や画面の変化は、講演に埋め込んで流しっぱなしにする部品（[[embed]] の Updates で西尾の embed は流しっぱなしの前提）として作りやすい。`Sleep` と `Wait` で間を台本に書けるので、話し手が止めずに語れる長さに合わせられる（推測。経験はない）
- **[[exp-thinklet-reading-demo-video]] との違い**: THINKLET は実機と声と本が要るので、端末の中だけで閉じる VHS の方式は使えない。実機の撮影は人が撮り、編集ソフトで組むしかなかった。作品の種類（端末の中で完結するか、物理世界に出るか）で、取れる方式が分かれる

## Open Questions

- VHS の GIF は README の上で自動再生・ループされるが、音はない。音や声が要る promo にそのまま使えるかは別の問題
- 実物を撮る方式で、待ち時間（LLM の応答など）をどう扱うか。`Hide` で隠すと実際の速さを誤解させうる。隠したことを画面に出す慣行は、この資料には書かれていない
- GitHub の README に動画を直接埋めたときの上限・挙動は、公式ドキュメントで確かめていない

## Updates

### 2026-11-09 第 3 回サーベイから

- VHS の最新は v0.12.1（2026-09-24）。v0.12.0 で Windows のコマンドコンソールが止まる問題が直った。Windows は `winget install charmbracelet.vhs` で入り、`ttyd` と `ffmpeg` が PATH に要る（means-capture 担当の確認）
- shot-scraper 1.10（2026-06-30）で `shot-scraper video storyboard.yml` が入った。YAML の台本で click・type・scroll・pause・wait_for を並べ、`cursor: true` でカーソルの点とクリックの輪を出す。1.12（2026-09-13）で WebP に対応（[[web-means-capture-playwright-screencast]]）
