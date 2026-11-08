---
type: source
summary: BBC の字幕の公式ガイド（Subtitle Guidelines v1.2.5、2026-03）。読む速さ 160〜180 WPM（1 語約 0.3 秒）、16:9 は 2 行・9:16 は 3 行まで、文字の大きさは 16:9 で行の高さが画面の高さの 7〜8%、9:16 で 3.9〜4.5%、言葉の切れ目で改行、カットをまたがない、白・黄・シアン・緑を黒地に、と書いている
video_types: [any]
url: https://www.bbc.co.uk/accessibility/forproducts/guides/subtitles/
author: BBC（Subtitle Guidelines。Ofcom と BBC の旧文書をまとめたもの）
published: 2026-03
retrieved: 2026-11-09
sources:
  - https://www.bbc.co.uk/accessibility/forproducts/guides/subtitles/
---

# BBC Subtitle Guidelines

## 何の文献か

- BBC の字幕の公式ガイド。「Version .1.2.5 / March 2026」（2026-11-09 時点の公式ページによる）。初版は 2016-09（同ページの改訂履歴）
- 冒頭で「This document brings together documents previously published by Ofcom and the BBC」と書き、BBC の放送・オンライン、自社制作・外注のすべての字幕の基準にする、としている
- 種類: 公式ドキュメント（作法のガイド）。実験の報告ではない。数値は「推奨」で、本文自身が「it is not possible (or advisable) to provide a set of hard rules」と書いている
- 対象は **closed の字幕**（視聴者が消せる字幕ファイル）。「not 'burnt in' to the image」と明記している。西尾の動画の字幕はすべて焼き込み（open）なので、そのまま当てはまるのではなく、作法の参考として読む

## 書いてあること

### 読む速さと表示時間（§4「Timing」）

- 「The recommended subtitle speed is 160-180 words-per-minute (WPM) or 0.33 to 0.375 second per word」。ただし視聴者は逐語の字幕を好むので、番組のテンポに合わせて上げてよい、と書く
- 最短の目安: 「a minimum period of around 0.3 seconds per word (e.g. 1.2 seconds for a 4-word subtitle)」。ただし「think about much more than the number of words on the screen; this would be an unacceptably crude approach」
- 改訂履歴に、生字幕の語の速さを「130-150wpm から 160-180wpm へ」上げたとある
- 時間を多めに取る場面: 画面で多くのことが起きているとき（サッカーの試合や地図）は「enough time both to read the subtitle and to take in the visuals」、長い数字（例 12,353）には時間を多く（§4.3.4、§4.3.6）
- 字幕の間の空白は「a minimum of one second, preferably a second and a half」。それより短いと「a very jerky effect」（§4.3）
- 話者が映っているとき、字幕は発話より 1.5 秒以上先に出ない・1.5 秒以上残らない。遅れても 2 秒以内（§5）
- 子ども向け（11 歳未満、ITC の推奨）は別の節。語を「変える」より「省く」で短くする（§20）

### 行・改行（§3）

- 行数: 「For landscape or square (16:9, 4:3 or 1:1) video, a maximum subtitle length of two lines is recommended. For vertical (9:16) video, a maximum subtitle length of three lines is recommended.」
- 1 行の長さ: 放送（Teletext）は 37 字。オンラインは幅で決め、16:9 で動画の幅の 68%、4:3・1:1・9:16 で 90%。「the equivalent to 37 characters in a 75% width region of a 16:9 (landscape) video is 25 characters in a 90% width region of a 9:16 (vertical) video」
- 改行は句読点で。やむを得ず文の途中で切るときも、冠詞と名詞、前置詞と続く句、代名詞と動詞などを分けない。「Line breaks within a word are especially disruptive to the reading process」。言語上の切れ目を幾何（行の長さの揃い）より優先する
- 1 行の長いものと 2 行の短いものなら、「‘long and thin’ subtitles are less disruptive of picture content than are ‘short and fat’ subtitles」（ただし常にではない）

### カットとの関係（§6）

- 「It is likely to be less tiring for the viewer if shot changes and subtitle changes occur at the same time」
- カットをまたぐ字幕（前のショットの途中で出て、次のショットの途中で消える）は避ける
- 積み上げ字幕（cumulative。前半を先に出し、後半を足して同時に消す）は、劇的な間や歌のリズムなど理由があるときだけ。2 行目が出るのをカットに重ねると「may cause the viewer to reread the first line」（§19）
- 歌の字幕は「reflect as closely as possible the rhythm and pace of a performance」で、通常の時間より「much faster or slower」になりうる

### 文字の大きさ（§9.2）

- 作るときの大きさ: 「Font size should be set to fit within a line height in the range 7% to 8% of the active video height for 16:9, 4:3 and 1:1」。9:16 は「3.9% to 4.5% of the active video height」
- 8% の由来は Teletext の倍高の行。テレビが小さかった頃に読みやすさのため倍高を使った（BBC R&D White Paper 287 を参照、と書く。WHP287 は未読）
- 再生側は大きさを**下げてよいが上げてはいけない**。画面別の推奨倍率の表があり、4〜4.7 型のスマホは ×1（作った大きさのまま）、5.5 型のスマホ ×0.67、タブレット ×0.67〜0.8、PC ×0.6、テレビ ×0.67。「the physical height of the video when displayed on the device's screen is the most direct determinant of font size」
- 幅の広い書体（Reith Sans、Verdana、Tiresias）で作ると、再生側が細い書体（Arial など）で出しても行が折り返さない
- 絵文字の音符（🎵）は黒地で見えにくいので使わず ♫ を使う。放送では使える文字が限られる（§9.3）

### 色・背景（§8）

- 「Most subtitles are typed in white text on a black background to ensure optimum legibility」
- 話者の区別に使う色は優先順に白・黄（#FFFF00）・シアン（#00FFFF）・緑（#00FF00）。「All of the above colours must appear on a black background to ensure maximum legibility」
- 背景は行ごとに文字の幅に合わせ、両端に 0.5em 伸ばす。行と行の間に隙間を空けない（§9.2.4）
- ナレーターは慣例で黄

### 位置（§10）

- 通常は画面の下。ただし画面の文字（名前のテロップなど）、話者の口、重要な動きを隠さない。隠すなら上に動かす
- オンラインの 16:9 は「not be placed outside the central 90% vertically and the central 75% horizontally」。9:16 はその逆で「central 75% vertically and the central 90% horizontally」。4:3・1:1 は縦横とも中央 90%
- 「In vertical (9:16) videos, it is common to position subtitles a little higher up, though still generally in the lower third of the screen. This is because faces are generally in the top half of the screen」
- プレイヤーの操作ボタンなどの重ね表示が出ているときは、字幕を縮める・動かす・一時停止するなどで隠れないようにする

### 画面の文字と字幕

- 配信の画質で画面のグラフィックスが読めないなら、話者の名前・肩書・連絡先などは字幕にも入れる。話と関係のない画面の文字は字幕に写さない

## この wiki への含意

型に依らない（any）。ただし BBC は「音声を文字で補う closed 字幕」の作法で、西尾の動画の多くは「音のない場で字幕が主役」の焼き込み字幕（promo）なので、目的が少し違う。

- **読む速さの物差しになる**: 160〜180 WPM ＝ 1 語 0.33〜0.375 秒。日本語の字数の基準は書いていない（日本語は [[web-type-netflix-timed-text-style-guide]] の 1 秒 4 字）
- **Gyazo の 0.5 秒ごとの叩き込み**（[[exp-gyazo-resumption-video]]）: 1 回が 1 語なら BBC の「1 語 0.3 秒」を満たす側。ただし BBC の「単語数だけで決めるのは crude」と、画面で多くが起きているときは時間を足す、に照らすと、フラッシュと揺れが入る山（16 秒・30 秒・36 秒）は読む時間がより要る場面にあたる（叩き込みの 1 回が何字かは exp ページに書かれていないので、超えたかは確かめられない）
- **閃光の 0.35 秒 → 0.16 秒**（[[exp-sutra-hype-editions]]: 減衰 0.35 秒で約 1 秒字が読めなかった）: BBC が「白い文字を黒地に」とするのは、背景の明るさが変わっても文字が読めるため。白飛びの下の白文字は背景の黒地が無い状態になる
- **クオリアさん journey の字幕は y=890 以降・1 行**（[[exp-qualia-video]]、1920×1080）: BBC の 16:9 の行の高さ 7〜8% は 76〜86px。y=890 から BBC のオンラインの下限（中央 90% の下端 = y≈1026）までは 136px なので、1 行は入るが 2 行は入らない（計算。字幕の実際の文字の大きさは exp ページに書かれていない）。「字幕 40 件すべて 1 行」はこの帯の幅と合っている。「説明対象と字幕を重ねない」は BBC の「画面の文字や重要な動きを隠さない」と同じ向き
- **字幕の色**: Polis の「明朝の白字幕と映像の高速交互」（[[exp-polis-magi-op]]）は、字幕の画面を黒地に白で映像と交互に出す形なので、白を黒地に、の条件を画面ごと満たしている。ただし明朝は線が細い（線の細さは [[web-type-apple-hig-wcag-text-size-contrast]]）
- **カットと字幕を合わせる**: 「ショットの切り替えと字幕の切り替えを同時に」は、西尾の promo の「120BPM の小節頭で場面を切り替え、文字もその区間で出し入れする」（[[exp-words-as-public-goods-video]] の `win()`、[[exp-democracy-river-video]]）と同じ形
- **歌の字幕は速さの規則の外**: 経文の同期解説・アゲアゲ版（[[exp-sutra-sync-subtitles]]、[[exp-sutra-hype-editions]]）は唱える音のリズムに文字を合わせていて、BBC の「歌の字幕はリズムに合わせ、通常より速くも遅くもなる」の側に入る
- **9:16 の 3 行・やや上・中央 75%**: 縦長の版（[[exp-nishio-showreel]] の縦長ショート）や今後の縦長に使える数字。SNS の UI が覆う範囲は別の話（[[web-type-ebu-r95-google-tiktok-safe-zones]]、[[web-meta-video-ads-best-practices]]）
- **使える文字を絞る**: 放送では文字集合が限られ、絵文字の音符も使わない。経文で「埵」「罣」が豆腐になった（[[exp-sutra-hype-editions]]）のと同じ種類の問題を、BBC は文字の一覧で先に防いでいる

## Open Questions

- BBC の数値は closed 字幕（再生側が大きさを下げる前提）で、焼き込みの字幕は再生側で縮められない。焼き込みで「作った大きさ」をどう決めるべきか（スマホで ×1 の大きさにしておけば、大きい画面では大きすぎるだけ、と読めるが未検証）
- 160〜180 WPM は英語の語の速さで、日本語の字数への換算は書いていない
- 8% の根拠の BBC R&D WHP287 は読んでいない
- 「字幕が主役で音のない」promo の焼き込み字幕に、音を補う字幕の速さの基準を当ててよいか。音声の言語が分からないと字幕を見る時間が長くなった、という研究の報告は [[web-type-szarkowska-2018-kruger-2022-subtitle-speed]]
