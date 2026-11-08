---
type: source
summary: スライドに動画を入れて流すときの形式と持ち方の公式記述（2026-11-09 時点）。PowerPoint は H.264＋AAC の .mp4 を推奨し、既定で埋め込み（リンクも可、ウェブ版は 256 MB まで）、動画に埋め込まれた字幕を表示でき、2505 以降で古い形式の対応を縮める。Keynote は QuickTime が扱える形式で、HEVC・ProRes を H.264 に変換する設定を持ち、ループと自動開始ができ、macOS 26.4 以降で字幕を表示できる。Google Slides は動画を YouTube か Drive から参照し（ファイルを抱え込まない）、Drive の再生は 1920×1080 まで、ループの記述は無い
video_types: [embed]
url: https://support.microsoft.com/en-us/office/video-and-audio-file-formats-supported-in-powerpoint-d8b12450-26db-4c7b-a5c1-593d3418fb59
author: Microsoft（PowerPoint サポート）／Apple（Keynote User Guide for Mac）／Google（Docs Editors Help、Google Drive Help）
published: unknown（どのヘルプも更新日の表示なし。2026-11-09 取得）
retrieved: 2026-11-09
sources:
  - https://support.microsoft.com/en-us/office/video-and-audio-file-formats-supported-in-powerpoint-d8b12450-26db-4c7b-a5c1-593d3418fb59 （Video and audio file formats supported in PowerPoint）
  - https://support.microsoft.com/en-us/office/insert-and-play-a-video-file-from-your-computer-f3fcbd3e-5f86-4320-8aea-31bff480ed02 （Insert and play a video file from your computer）
  - https://support.apple.com/guide/keynote/add-video-and-audio-tan63d61519a/mac （Add video and audio in Keynote on Mac）
  - https://support.apple.com/guide/keynote/tan12af068f9/mac （Set movie and image formats for Keynote presentations on Mac）
  - https://support.google.com/docs/answer/97447?hl=en&co=GENIE.Platform%3DDesktop （Insert or delete images & videos）
  - https://support.google.com/drive/answer/2423694 （Store & play video in Google Drive）
---

# スライドに入れる動画の形式と持ち方（PowerPoint・Keynote・Google Slides）

## 何の文献か

- 3 社の公式ヘルプ。再生の始まり方・発表中のキーは第 1 回の [[web-powerpoint-keynote-google-slides-video-playback]] に既にある。ここは**形式・埋め込みかリンクか・字幕・ループ**を足す
- どのページにも更新日の表示が無い。Keynote のページは macOS 26.4 に触れているので 2026 年の版

## 書いてあること

### PowerPoint

- 推奨: 「.mp4 files encoded with H.264 video and AAC audio」。Windows の対応: .mp4/.m4v（H.264＋AAC）、.mov、.webm（Vorbis の WebM は Web Media Extensions が要る）
- 「Support for Windows Media Video (.wmv, .asf), … MPEG-2 …, (.avi), … (.aiff …) and … 3GPP is limited and deprecated in PowerPoint version 2505 and」later（文の末尾は取得したテキストで切れていた）
- Mac 版は .mp4・.m4v・.mov・.mpg・.ts など（.wmv は不可）
- 埋め込みかリンクか: 「you can insert an embedded video (the default behavior) or link to a video file」。埋め込みはファイルが大きくなる。リンクは同じフォルダにコピーしてから、と書く（切れるのを防ぐため）。File > Info の「Optimize Media Compatibility」で埋め込みかリンクかが分かる
- 「PowerPoint for the web supports insertion of video files up to 256 MB」
- 字幕: 「PowerPoint also supports closed captions and subtitles that are embedded in video files」（新しい版）
- 始まり方の既定は In Click Sequence（[[web-powerpoint-keynote-google-slides-video-playback]]）。動画のループ（Loop until Stopped）は今回読んだ現行ページにも記述が無い

### Keynote（Mac）

- 「Video and audio files must be in a format that QuickTime supports on your Mac」。だめなら iMovie・QuickTime Player・Compressor で .mov に
- 既定ではクリックで再生。「You can set video or audio looping, or set the start time to make the media files play automatically when the slide appears」
- YouTube と Vimeo のリンクを「web video」としてスライド内で再生できる（ネット接続が前提、推論）
- 「On macOS 26.4 or later, you can add subtitles to videos」（スライドショーで Closed Captions のボタン）
- 形式の設定（Keynote > Settings > General の Adding Media）: 既定は元の形式のまま。「Optimize media for older devices」で HEVC・HEIC・ProRes を H.264・JPEG・PNG に変換、「Optimize media for iPhone, iPad, and Apple Vision Pro」で ProRes などを変換。元の形式のままだと「may not display on all devices」

### Google Slides

- 動画の入れ方は「Search YouTube」「By URL」「Google Drive」から選ぶ（Vids の動画も Drive に書き出してから）。**ファイルをプレゼンに抱え込む経路は書かれていない**（参照の形）
- 再生: Play (on click) が既定、Play (automatically)、Play (manual)（[[web-powerpoint-keynote-google-slides-video-playback]]）。ループの記述は無い
- 音声は Drive の .mp3 と .wav
- Drive の動画: 対応は WebM（VP8＋Vorbis）、MPEG4・3GPP・MOV（H.264・MPEG4＋AAC）、AVI、MPEGPS、WMV、FLV など。「The maximum playback resolution is 1920 x 1080」。Drive のプレイヤーには字幕（CC）の表示がある

## この wiki への含意

- **embed の書き出しは「H.264＋AAC の .mp4、1080p、30 か 60fps」で 3 つとも通る**（PowerPoint の推奨、Keynote は QuickTime が扱える、Drive は H.264＋AAC の MP4 を挙げ再生は 1080p まで）。経験の出力（ffprobe で 1920×1080・H.264/AAC を確かめていた。[[exp-sutra-sync-subtitles]]）はそのまま当てはまる
- **4K や HEVC で書き出すと Google Slides（Drive）では 1080p で再生され、Keynote は変換の設定次第**。embed 用は 1080p の H.264 にしておくのが安全（推論）
- **流しっぱなしの前提（[[embed]] の Updates）と再生の設定**: 流しっぱなしなら、PowerPoint は「Automatically」、Keynote は自動開始（start time）、Google Slides は「Play (automatically)」にする。ループさせたいなら Keynote が公式にループを持つ。PowerPoint と Google Slides は今回の公式ページでループを確かめられなかったので、**動画の中で必要な回数を繰り返して書き出す**方が依存が少ない（推論。[[exp-sutra-sync-subtitles]] は 3 回繰り返しを中に持っていた）
- **会場で確実に流す**: PowerPoint は既定で埋め込み、Keynote はファイルを持つ、Google Slides は YouTube か Drive を参照するのでネットと権限に依存する（[[web-powerpoint-keynote-google-slides-video-playback]] の推測と同じ向き）
- **字幕**: PowerPoint は動画に埋め込まれた字幕トラック、Keynote は macOS 26.4 以降で字幕。流しっぱなしの embed では、トラックの字幕を会場で表示させる操作に頼らず、焼き込みが確実（推論）
- **音**: 3 つとも音量を下げる・消すことはできる（第 1 回のページ）。音量を揃えるのは書き出し時に（[[web-check-loudness-ffmpeg-loudnorm-ebur128]]）

## 着手の仕方（未検証。Mac と galleria で確かめる）

- **何が表現できるようになるか / 効く型**: embed の動画を 3 つのソフトで確実に流れる形で渡す（embed）
- **機械**: 書き出しは galleria WSL の ffmpeg。再生の確認は Mac（Keynote、PowerPoint for Mac）と、ブラウザ（Google Slides。要: Google アカウント、西尾が決めること）。galleria の Windows に PowerPoint があるかは未確認
- **最小の手順**:
  ```sh
  # embed 用の書き出し（1080p、H.264 High、AAC 48k、faststart、BT.709 の札。推測で組んだ設定）
  ffmpeg -i master.mp4 -vf "scale=1920:1080:flags=lanczos,format=yuv420p" -colorspace bt709 -color_primaries bt709 -color_trc bt709 -c:v libx264 -profile:v high -crf 18 -c:a aac -b:a 192k -ar 48000 -movflags +faststart embed_1080.mp4
  ffprobe -v error -show_entries stream=codec_name,profile,width,height,r_frame_rate,pix_fmt -of default=nw=1 embed_1080.mp4
  ```
  Keynote: 新しい書類に入れ、Movie の設定で自動開始とループを付けて再生。PowerPoint: Insert > Video > This Device、Playback の Start を Automatically。Google Slides: Drive に上げて Insert > Video > Google Drive
- **動いたと言える確かめ方**: 3 つのソフトで、スライドに入った瞬間に再生が始まり、最後まで止まらない。Keynote で 2 周目に入る。PowerPoint の File > Info で「埋め込み」と出る。ffprobe で h264・High・1920×1080・yuv420p
- **所要の見込み**（推測）: 1 時間（Google の権限まわりを除く）

## Open Questions

- PowerPoint（現行版）の動画のループ・Rewind after Playing の公式記述を見つけられなかった（第 1 回と同じ）
- Google Slides でループや開始・終了位置を設定できるか（現行ヘルプに記述なし）
- Keynote の「web video」はオフラインの会場で再生できない、は推論
- PowerPoint の 2505 以降で非推奨になった形式の文の続きが取れていない
