---
type: source
summary: 学会発表の中で動画を流すときの、ACM の側の作法（Ladner 2015「Making Your Conference Talk Accessible」、SIGACCESS の Accessible Presentation Guide、CHI 2018 の発表の手引き）。ナレーションだけで字幕の無い動画、音楽だけでナレーションの無い動画をどちらも「届かない例」に挙げ、流す前に何が映るかを一言で言う、字幕と音声解説を付ける、を勧めている。会場の音は「ノート PC の 3.5mm 音声入力から会場のスピーカーへ」が CHI 2018 の標準設備
video_types: [embed, talk]
url: https://homes.cs.washington.edu/~ladner/MakingYourTalkAccessible.pdf
author: Richard E. Ladner（University of Washington）／ACM SIGACCESS／ACM CHI 2018 組織委員会
published: 2015-10-18（Ladner）、unknown（SIGACCESS のページ）、2017〜2018（CHI 2018）
retrieved: 2026-11-09
sources:
  - https://homes.cs.washington.edu/~ladner/MakingYourTalkAccessible.pdf （Ladner, "Making Your Conference Talk Accessible", 2015-10-18、4 ページ）
  - https://www.sigaccess.org/welcome-to-sigaccess/resources/accessible-presentation-guide/ （SIGACCESS Accessible Presentation Guide。9 項目）
  - https://chi2018.acm.org/guide-to-a-successful-presentation/ （CHI 2018 Guide to a Successful Presentation）
---

# 学会発表の中で動画を流す作法（Ladner 2015・SIGACCESS・CHI 2018）

## 何の文献か

- **Ladner 2015**: アクセシビリティ研究者 Richard E. Ladner（University of Washington）の 4 ページの手引き。学会の発表を、目の見えない人・耳の聞こえない人を含む全員に届くようにするための実務の助言。著者の観察（「何百の学会、何千の発表を見てきた」）に基づく助言で、実験ではない
- **SIGACCESS Accessible Presentation Guide**: ACM のアクセシビリティの分科会のページ。Ladner の文書を引き、9 項目の指針を並べる
- **CHI 2018 Guide to a Successful Presentation**: CHI 2018 の発表者向けの公式の手引き。会場の設備と、DON'T/DO の表
- 三つとも、動画を発表の中で流す前提の記述を含む。2026-11-09 時点で読めた版による

## 書いてあること

### 届かない例（Ladner 2015 の冒頭）

Ladner は「話し手の言ったこと」と「なぜ届かないか」を並べる。動画に関わるのは次の三つ:

- 「Video 1: "Let me show you a video demonstrating process Y." The video is narrated but has no captions」——耳の聞こえない人にはナレーションが分からない
- 「Video 2: "Let me show you a video showing Z in action." The video has no narration, but just some background music」——目の見えない人には Z の動きが分からない
- 「Animation: "Watch how our algorithm manipulates the data." There is no narration to help blind or low-vision audience members understand the algorithm」
- 続けて「These examples are not meant to imply that images, videos, graphs, pointing, allusion, and animation should never be used. Instead they point out the perils」と書く

### 助言（Ladner 2015 の「Some Additional Practical Suggestions」ほか）

- 「Make sure that videos are captioned and audio described. **Sometimes it is good to give a brief description of what is in the video before it is played.** This will help blind audience members to establish context for what they will hear.」
- 「Control the speed of animations so they can be described fully.」
- スライドが出たら数秒黙って読ませてから話す。スライドの文は声に出して読む
- 手話通訳・リアルタイム字幕を使う人は「can only focus on one thing at a time: the interpreter, the speaker, or the slides」。通訳・字幕には遅れがあるので、スライドの情報を指すときは少し間を置け
- 「A great talk is not about the slides, but about the speaker. The focus of the audience should be on the speaker, not on the slides.」

### SIGACCESS の 9 項目のうち動きに関わるもの

- 「6. Avoid using animations — Unless with a detailed audio description」
- 「7. Audio describe and caption videos」
- ほかは色の対比、色だけで情報を伝えない、文字を少なく、ポインタを避ける、はっきり話す、スライドを前日か 1 週間前に配る

### CHI 2018 の手引き

- 会場の標準設備: 1920×1080・16:9 のプロジェクタ、HDMI と VGA（変換アダプタは自分で持参）、「**1/8″ audio input to room speakers**」、演台のマイク
- 「DON'T subject your audience to an "ordeal by bulleted list."」「DO present a series of "exhibits": images, videos, system demos, diagrams, graphs, or tables. **You can explain and elaborate on these exhibits while people are looking at them.**」
- 「DO arrive 20 minutes before your session to test the compatibility of your laptop with the projector」。他人の PC で流すなら、可搬性を最大にして早めに試せ（足りないフォントなど）
- マイクは聴衆が少なくても使え。部屋が満員なら外のスクリーンに中継され、マイクが唯一の音の経路になる

## この wiki への含意

- **流しっぱなしの embed の声の分担に、二つの失敗の型が名指しされている**: (1) ナレーションだけで字幕が無い（聞こえない人に届かない）、(2) 音楽だけでナレーションが無い（見えない人に届かない）。西尾の embed で考えると、
  - ナレーション入り（THINKLET のデモ、[[exp-thinklet-reading-demo-video]]）なら字幕を付ける
  - ナレーション無し（般若心経の同期解説、[[exp-sutra-sync-subtitles]]。ただし唱える音そのものがある）なら、流す前に話し手が「何が映るか」を一言で言う
- **流す前の一言**: Ladner の「流す前に短く説明する」は、Rosling 型の「先に見方を言う」（[[embed]]、[[web-roslingifier-data-presentations]]）と同じ動作だが、Rosling 型と違って**流し始めたら止めなくてよい**。流しっぱなしの前提と両立する、話し手の側の作法として一番使いやすい
- **動いている最中に話し手が説明するか**: CHI 2018 は「見ている間に説明・敷衍せよ」と書く（exhibit の一般論で、動画に限らない）。Ladner の注意（通訳・字幕を使う人は一度に一つしか見られない）からは、**動画の間に話し手が話すと、字幕・通訳を頼る人は動画と話のどちらかを捨てる**ことになる。流す前に言い、流している間は黙る（または最小限）が、両方に届く順序（推論）
- **会場の音**: CHI 2018 の標準設備は「3.5mm の音声入力から会場のスピーカーへ」。動画の音を出すなら、ノート PC の音声出力を会場の卓につなぐ前提。HDMI で音も送れる会場もあるが、この手引きには書かれていない。音のある embed は、リハーサルで会場の音量を確かめる手順が要る（CHI 2018 の「20 分前に試せ」の延長、推論）
- **アニメーションの速さ**: 「説明しきれる速さに」（Ladner）は、流しっぱなしで動画が時間を握る embed では、作る側が見積もるしかない。動画の秒ごとに話し手が言う量を台本にしておく（推論）

## Open Questions

- 「流す前に一言」と「流している間に語る」のどちらが伝わるかを比べた資料は無い。Ladner の助言は経験からのもの
- 字幕を焼き込んだ embed（西尾の作り方）と、会場のリアルタイム字幕（話し手の声の字幕）が同時に出ると、画面の文字が二重になる。どう分けるかは読んだ資料に無い
- CHI 2018 の設備は 2018 年のもの。現在の学会（2026）の標準設備は確かめていない
