---
type: source
summary: 2026-11-09 時点の YouTube 公式ヘルプが書く、アップロードの仕様（MP4・H.264 High・AAC か Opus・48 kHz・BT.709、1080p は 30fps 級で 8 Mbps・60fps 級で 12 Mbps を推奨）、上限（256 GB か 12 時間。未確認の口座は 15 分まで）、Shorts（2024-10-15 以降は正方形か縦長で 3 分以内が自動で Shorts、上げられるのは 1080p まで）、字幕ファイル（SRT・SBV・VTT・TTML・SCC など）、サムネイル（動画 3840×2160・Shorts 2160×3840 を推奨、Shorts の自作サムネイルは PC の Studio で確認済み口座のみ）
video_types: [promo, talk]
url: https://support.google.com/youtube/answer/1722171
author: Google（YouTube ヘルプ）
published: unknown（ヘルプに更新日の表示なし。2026-11-09 取得）
retrieved: 2026-11-09
sources:
  - https://support.google.com/youtube/answer/1722171 （YouTube recommended upload encoding settings）
  - https://support.google.com/youtube/answer/6375112 （Video resolution & aspect ratios）
  - https://support.google.com/youtube/answer/71673 （Upload videos longer than 15 minutes。上限）
  - https://support.google.com/youtube/answer/2734698 （Supported subtitle and closed caption files）
  - https://support.google.com/youtube/answer/72431 （Add custom thumbnails on YouTube）
  - https://support.google.com/youtube/answer/15424877 （Understand three-minute YouTube Shorts）
  - https://support.google.com/youtube/answer/10059070 （Get started creating YouTube Shorts）
---

# YouTube の公式仕様（通常の動画・Shorts）

## 何の文献か

- YouTube の公式ヘルプ（Google）。すべて 2026-11-09 に curl で取得した英語版。**どのページにも最終更新日の表示が無い**
- 「recommended upload encoding settings」の冒頭には「These features are only available to partners who use YouTube Studio Content Manager」という一文が出る。中身は一般向けの推奨の書き方なので、ここでは推奨として扱う（[[web-check-color-ffmpeg-signalstats-limiter-ebu-r103]] の Open Question と同じ）
- 目標ラウドネスの数値は YouTube の公式ヘルプに無い（[[web-aes-td1004-streaming-loudness]]）

## 書いてあること

### 符号化の推奨（1722171）

- 容器 MP4、Edit List なし、moov atom を先頭に（Fast Start）
- 音声 AAC-LC か Opus（か Eclipsa Audio）、ステレオ（か ＋5.1）、**48 kHz**
- 映像 H.264、プログレッシブ、High Profile、連続 B フレーム 2、Closed GOP で GOP はフレームレートの半分、CABAC、可変ビットレート（上限なし）、4:2:0
- フレームレート: 「Content should be encoded and uploaded in the same frame rate it was recorded」。24・25・30・48・50・60 が一般的、他も可
- 推奨ビットレート（SDR）: 1080p は 8 Mbps（24/25/30）・12 Mbps（48/50/60）、1440p 16/24、2160p 35–45/53–68、720p 5/7.5。音声はステレオ 384 kbps
- 色空間: SDR は BT.709。未指定なら BT.709 とみなし、フルレンジはリミテッドに変換

### 解像度・縦横比（6375112）

- 標準は 16:9。それ以外はプレイヤーが合わせる。「avoid adding padding or black bars directly to your video」
- 16:9 の推奨解像度は 7680×4320 〜 426×240 の 8 段（1080p は 1920×1080）

### 上限（71673）

- 既定で 15 分まで。確認済み（電話で認証）の口座はそれ以上
- 「The maximum file size you can upload is 256 GB or 12 hours, whichever is less」

### Shorts（15424877、10059070）

- 「Videos uploaded after October 15, 2024: Any videos uploaded on or after this date with a square or vertical aspect ratio up to three minutes in length will be categorized as Shorts」。Shorts にしたくなければ 16:9 などの横長で
- 1 分を超える Shorts に Content ID の申し立てがあると全世界でブロック
- 「You can upload Short videos with a maximum resolution of 1080p」
- 2025-03-31 から Shorts の再生回数は「the number of times a Short starts to play or replay」（繰り返しも数える）。従来の数え方は「Engaged views」

### 字幕ファイル（2734698）

- 基本: SubRip（.srt）・SubViewer（.sbv/.sub）は「Only basic versions … No style info (markup) is recognized. The file must be in plain UTF-8」。MPsub、LRC、Videotron Lambda（.cap、「primarily used for Japanese subtitles」）
- 上級: SAMI、RealText、WebVTT（.vtt、「Positioning is supported, but styling is limited to <b>, <i>, <u>」）、TTML（.ttml、iTT を含む）、DFXP
- 放送用: SCC（「our preferred file format」）、EBU-STL など

### サムネイル（72431）

- 推奨解像度: 動画 3840×2160、Shorts 2160×3840。最小は動画が幅 640、Shorts が高さ 640。JPG か PNG。上限は携帯から 2 MB、PC から 50 MB
- 「Custom thumbnails for Shorts are currently only available to add in YouTube Studio on a computer. Your account must be verified」
- 「Vertical videos with 16:9 custom thumbnails will be replaced by an auto-generated 4:5 thumbnail on the home, explore, and subscription pages」
- 自作でなければ自動の候補から選ぶ（「Get suggestions」）

## この wiki への含意

- **経験の書き出しとの照合**:
  - マスターの 1080p60・crf 16（[[exp-html-capture-pipeline]]）は、YouTube の「録ったフレームレートのまま」に合う。crf 指定は可変ビットレートで、推奨の 12 Mbps（1080p60）を下回るか上回るかはファイルによる。`ffprobe` の bit_rate で確かめられる
  - 音声の AAC 256k・48 kHz は推奨（ステレオ 384 kbps）より少し低い
  - `-movflags +faststart` は「moov atom at the front」に当たる（経験では X 用の版にだけ付けていた）
  - 縦長 4:5（1080×1350）や 9:16 で 3 分以内なら Shorts に分類される。[[exp-html-capture-pipeline]] の「60 秒以内」は古い（同ページの Updates に既記）
- **promo**: Shorts の再生回数がループを数えるようになったので、ループする終わり方（[[exp-words-as-public-goods-video]]）は数字の上でも効きうる（数え方の変更で、視聴の質の話ではない）。Shorts のサムネイルを自作するには PC の Studio と確認済み口座が要る
- **talk**: 字幕は SRT で足りる（スタイルは無視される）。位置を指定したいなら VTT。内容と時間を正本で分けていた経験（[[exp-sutra-sync-subtitles]]）からは、正本→SRT/VTT の書き出しを一つ持てばよい
- **embed**: YouTube は embed の配信先ではないが、Google Slides に動画を入れるとき YouTube から入れる経路がある（[[web-check-spec-powerpoint-keynote-google-slides-formats]]）

## 着手の仕方（未検証。galleria で確かめる）

- **何が表現できるようになるか / 効く型**: 上げる前に仕様との食い違いを機械で見つける（promo・talk）
- **機械**: galleria WSL の ffprobe。費用・アカウントなし（アップロードそのものは西尾が決めること）
- **最小の手順**:
  ```sh
  ffprobe -v error -show_entries format=duration,bit_rate:stream=codec_name,profile,width,height,r_frame_rate,avg_frame_rate,pix_fmt,color_space,sample_rate,channels,bit_rate -of default=nw=1 out.mp4
  # moov が先頭か（faststart）: 最初の数十バイトに moov が mdat より先に現れるか
  python3 -I -c "import sys;b=open(sys.argv[1],'rb').read(1<<20);print('moov' ,b.find(b'moov'),'mdat',b.find(b'mdat'))" out.mp4
  ```
- **動いたと言える確かめ方**: codec_name=h264・profile=High・pix_fmt=yuv420p・音声 aac で sample_rate=48000。r_frame_rate と avg_frame_rate が一致（CFR）。縦横比と尺から「Shorts になるか」を判定できる。moov の位置が mdat より小さい
- **所要の見込み**（推測）: 15 分

## Open Questions

- Shorts の上限 1080p はアプリからの記述（10059070）。Studio から 4K の縦長を上げた場合の扱いは書かれていない
- ヘルプに更新日が無いので、いつの仕様かは取得日でしか言えない
- 字幕の Videotron Lambda（.cap）を日本語向けと書くが、SRT で日本語に困ることがあるかは書かれていない（UTF-8 必須）
