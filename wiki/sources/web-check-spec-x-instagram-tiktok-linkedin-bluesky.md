---
type: source
summary: 2026-11-09 時点で読めた X・Instagram・TikTok・LinkedIn・Bluesky の動画の公式仕様。X はヘルプ（2026-10-12 更新）でウェブからのアップロードを 1920×1200・40fps・25 Mbps まで、無料は 140 秒・512MB、60 秒以下はループと書き、開発者文書は 60fps まで・既定で 20 分・8GB と書いて食い違う。Instagram と TikTok の利用者向けヘルプは JS で本文が取れず、開発者向け API の仕様（Reels 23–60fps・3 秒〜15 分・300MB、TikTok 23–60fps・最大 4GB）と広告仕様で代えた。LinkedIn は 15 分・5GB・10–60fps・1:2.4〜2.4:1（ヘルプは 2 年前の更新）。Bluesky は公式ブログで 60 秒（2024-09）、以後の引き上げは二次情報
video_types: [promo]
url: https://help.x.com/en/using-x/x-videos
author: X Corp.／Meta（Instagram Graph API、Meta 広告ガイド）／TikTok（for Developers、Ads Help）／LinkedIn（ヘルプ、Microsoft Learn の API 文書、広告ページ）／Bluesky Social
published: 下の表の各行に（多くは更新日の表示なし）
retrieved: 2026-11-09
sources:
  - https://help.x.com/en/using-x/x-videos （直接は本文が取れず、Internet Archive 2026-10-21 の版で読んだ。dateModified 2026-10-12）
  - https://docs.x.com/x-api/media/quickstart/best-practices （X API の media の Best practices）
  - https://docs.x.com/x-api/media/initialize-media-upload （media_type に text/srt・text/vtt）
  - https://developers.facebook.com/docs/instagram-platform/instagram-graph-api/reference/ig-user/media （Instagram Graph API の IG User Media。日本語版を読んだ。更新日時 2026/09/28）
  - https://www.facebook.com/business/ads-guide/update/video/instagram-reels （Meta 広告ガイド、Instagram リール）
  - https://www.facebook.com/business/ads-guide/update/video/instagram-feed （Meta 広告ガイド、Instagram フィード）
  - https://help.instagram.com/1038071743007909 （本文が取れなかった。Internet Archive の版も本文なし）
  - https://developers.tiktok.com/doc/content-posting-api-media-transfer-guide （Last updated August 4, 2026）
  - https://developers.tiktok.com/doc/content-posting-api-reference-direct-post （Last updated October 27, 2026）
  - https://ads.tiktok.com/help/article/video-ads-specifications （Last updated: June 2026）
  - https://support.tiktok.com/en/using-tiktok/creating-videos/upload-videos （本文が取れなかった）
  - https://www.linkedin.com/help/linkedin/answer/a548372 （Video sharing troubleshooting。Last updated: 2 years ago）
  - https://www.linkedin.com/help/linkedin/answer/a564109 （Media file types supported on LinkedIn。Last updated: 2 months ago）
  - https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/videos-api （Videos API。ms.date 2026-02-12）
  - https://business.linkedin.com/advertise/ads/sponsored-content/video-ads （広告の FAQ）
  - https://bsky.social/about/blog/09-11-2024-video （Bluesky 公式ブログ、2024-09-11）
  - https://docs.bsky.app/docs/about-bluesky-content/video （Bluesky 開発者文書「Uploading Video」。数値の上限は書いていない）
  - https://www.macrumors.com/2025/03/11/bluesky-extends-video-limit-latest-app-update/ （二次: v1.99 で 3 分）
  - https://opentweet.io/answers/bluesky-limits （二次: 2026-10-10 確認として 10 分・300MB・VTT 20 本）
---

# X・Instagram・TikTok・LinkedIn・Bluesky の動画の公式仕様（2026-11-09 時点）

## 何の文献か

- 各社の公式ページ。利用者向けヘルプ、開発者向け API 文書、広告仕様の 3 種類があり、**同じ会社でも数値が食い違う**（API は API 経由の投稿の上限、広告は広告枠の仕様）。下では種類を分けて書く
- **読めなかったもの**: Instagram の利用者向けヘルプ（help.instagram.com は JS で本文が空。WebFetch と Internet Archive でも本文なし）、TikTok の利用者向けヘルプ（support.tiktok.com、同じく本文なし）、X の Creative best practices（第 1 回の [[web-x-video-ads-best-practices]] でも読めていない）、LinkedIn の字幕のヘルプ（a1338046、本文なし）、Bluesky の lexicon（GitHub・jsDelivr から取れなかった）
- 第 1 回の [[web-x-video-ads-best-practices]] が X の広告仕様（29.97/30fps 推奨・60fps まで、2:20 まで、サムネイルの欄、60 秒未満でループ）とヘルプ（2026-05 の版）を既に書いている。ここは 2026-10 の版の確認と、他の 4 社を足す

## 書いてあること

### X

- **ヘルプ**（Internet Archive 2026-10-21 の版、JSON-LD の dateModified 2026-10-12）:
  - Premium と X Subscription の Plus 以上: 4 時間未満を 1080p で 16GB まで。2〜4 時間は 720p
  - それ以外: 「up to 140 seconds long with a maximum file size of 512MB」
  - ウェブからのアップロード: 最小 32×32、最大「1920 x 1200 (and 1200 x 1900)」、縦横比「1:2.39 - 2.39:1 range (inclusive)」、「Maximum frame rate: 40 fps」、「Maximum bitrate: 25 Mbps」
  - 「All videos posted to X that are 60 seconds or shorter will automatically loop」
  - 自動再生は既定でオン（設定で切れる）。字幕は端末の音を切ると見える、iOS・Android はタイムラインで自動表示（字幕ファイルの付いた動画の話）
  - 通常の投稿でカバー（サムネイル）を選ぶ方法は書かれていない
- **API の Best practices**（docs.x.com）:
  - 既定の口座: Post の動画は「0.5 seconds–20 minutes」「8 GB」。Premium／認証済み: 125 分・16 GB。「Post-video caps match the X app」と書く
  - 推奨: H.264 High、30 か 60 FPS、1280×720（横）・720×1280（縦）・720×720、映像 5,000 kbps 以上、AAC LC 128 kbps 以上。「Subscribed users can upload a 1080p video and get 1080p playback. Unsubscribed users can upload a 720p video and get a 720p playback」
  - 必須: 60 FPS 以下、32×32〜1280×1024、縦横比 1:3〜3:1、画素比 1:1、**YUV 4:2:0 のみ**、AAC-LC（HE-AAC 不可）、モノかステレオ、open GOP 不可、プログレッシブ
  - 字幕: media_category に `subtitles`、media_type に `text/srt` と `text/vtt`（API で字幕ファイルを付ける経路）

### Instagram（Meta）

- **利用者向けヘルプは読めなかった**
- **Instagram Graph API**（IG User Media、日本語版の更新日時 2026/09/28）の「リールの仕様」: MOV か MP4（エディットリストなし、moov 先頭）、AAC 48 kHz まで・モノかステレオ・128 kbps、HEVC か H.264（プログレッシブ、closed GOP、4:2:0）、**23–60 FPS**、横の画素は最大 1920、縦横比 0.01:1〜10:1 だが 9:16 を推奨、映像 VBR 最大 25 Mbps、**3 秒〜15 分**、**300 MB まで**
  - カバー: `cover_url`（JPEG、8MB まで、9:16 推奨。9:16 でなければ中央の 9:16 が使われ、フィードに出すと中央の 1:1）か `thumb_offset`（ミリ秒。既定 0 ＝最初のコマ。両方あれば cover_url）
  - ストーリーズの動画: 3〜60 秒、100 MB
- **Meta 広告ガイド**（日付なし）: リール広告は 9:16・1440×2560、H.264・固定フレームレート・プログレッシブ・AAC 128 kbps 以上、0 秒〜15 分、4GB。「オーガニックなリールと同様に広告の長さは最大15分」。セーフゾーンは「上部14%、下部35%、両サイド6%」に重要な要素を置かない。フィード広告は 9:16 推奨・1080×1920、1 秒〜60 分、4GB、縦横比の許容誤差 1%

### TikTok

- **利用者向けヘルプは読めなかった**
- **Content Posting API の Media Transfer Guide**（2026-08-04 更新）: MP4（推奨）・WebM・MOV、H.264（推奨）・H.265・VP8・VP9、**23〜60 FPS**、縦横とも 360〜4096 画素、「All TikTok creators can post 3-minute videos, while some have access to post 5-minute or 10-minute videos」、API で送れるのは 10 分まで、**4GB まで**
- **Direct Post の API**（2026-10-27 更新）: `video_cover_timestamp_ms`（カバーにするコマのミリ秒。未指定なら最初のコマ）、`is_aigc`（AI 生成なら true）
- **広告仕様**（June 2026）: 縦 9:16 で 540×960 以上を推奨、最大 10 分、500MB、516 kbps 以上。セーフゾーンはテンプレートで配布（[[web-type-ebu-r95-google-tiktok-safe-zones]]）

### LinkedIn

- **ヘルプ「Video sharing troubleshooting」**（Last updated: 2 years ago）: MP4・MOV・AVI・WEBM・MKV など。最大 5 GB・最小 75 KB、**最長 15 分**、最短 3 秒（PC）・2 秒（アプリ）、256×144〜4096×2304、**1:2.4〜2.4:1**、**10〜60 fps**、192 kbps〜30 Mbps。端（上下左右）に重要な要素を置かない（安全域は画像のみ）
- **Videos API**（ms.date 2026-02-12）: 3 秒〜30 分、75 KB〜500 MB、MP4（広告を含む API の仕様）。字幕ファイル 1 本、**英語のみ**、`"format": "SRT"`。サムネイルを上げられ、上げなければ自動生成
- 広告の FAQ: 4:5・9:16・16:9・1:1、3 秒〜30 分、75KB〜500MB、「videos autoplay without sound」なので字幕を強く勧める

### Bluesky

- **公式ブログ**（2024-09-11）: 1 投稿に 1 本、「Videos can be up to 60 seconds long」、.mp4・.mpeg・.webm・.mov、自動再生は既定でオン、字幕を付けられる、1 日 25 本／10 GB
- **開発者文書**: メール確認済みの口座のみ、1 日の上限あり、aspectRatio を埋め込みに付ける。数値の上限は書いていない
- **二次情報**: MacRumors（2025-03-11）は v1.99 で 3 分に、OpenTweet（2026-10-10 確認と記す）は lexicon と公式アプリのソースを根拠に 10 分・300 MB・字幕は VTT を 20 本まで（各 20,000 バイト）と書く。**原典（lexicon）は今回取得できていない**

## この wiki への含意

- **X の 40fps と 60fps の食い違い**: ヘルプ（ウェブから）は 40fps まで、API は 60fps まで。Gyazo の 47 秒版（60fps、[[exp-gyazo-resumption-video]]）をウェブから上げると制限にかかりうる。X 用は 30fps で書き出す経験の版（[[exp-html-capture-pipeline]]）が両方に収まる
- **X の解像度**: API の必須は「1280×1024 以下」なのに推奨で「Subscribed users can upload a 1080p video」と書く、ヘルプは 1920×1200 まで。経験の 1080p30・4:5（1080×1350）はヘルプの縦の最大 1900 には収まる。無料口座の再生が 720p になるかは API の記述だけで、ヘルプには無い
- **X の長さ**: ヘルプの無料 140 秒と API の既定 20 分が食い違う（API は「match the X app」と書く）。西尾の X 用（47〜87 秒）はどちらでも収まる
- **最初のコマがカバーになる**: Instagram（thumb_offset の既定 0）と TikTok（未指定なら最初のコマ）は API でそう書く。X は通常投稿のカバーの記述が無い。経験の「最初のコマにサムネイルを焼き込む」（[[exp-html-capture-pipeline]]）は TikTok・Instagram の API 経由でも同じ考え方が効き、API ならカバーのコマを指定し直せる
- **セーフゾーン**: Meta のリール広告は下 35%・上 14%・左右 6%（[[promo]] の表の「下 35%」と同じ出典の系列）。西尾の下端の進捗バーは、この範囲に入る
- **字幕ファイル**: X（API）は SRT/VTT、LinkedIn（API）は SRT・英語のみ、Bluesky は VTT（二次）、YouTube は SRT/VTT など（[[web-check-spec-youtube-upload-shorts]]）。日本語の字幕ファイルを付けられることが公式に読めたのは X の API と YouTube だけ。無音で見られる面では焼き込み字幕が確実（[[promo]]）
- **縦横比**: 4:5 は X（ヘルプの範囲内）、LinkedIn（1:2.4〜）、Instagram（API の範囲内、推奨は 9:16）、YouTube（Shorts に分類）で通る。TikTok は API の範囲（画素数の制限のみ）で通るが、推奨は 9:16

## 着手の仕方（未検証。galleria で確かめる）

- **何が表現できるようになるか / 効く型**: 1 本のマスターから、出す場所ごとの版を機械で作り分け、仕様の表と照合する（promo）
- **機械**: galleria WSL の ffmpeg・ffprobe。アップロードは西尾が決めること（要: 各社のアカウント）
- **最小の手順**（推測で組んだ版の作り分け。値は下の表の厳しい側に合わせる）:
  ```sh
  # X 用（ヘルプの 40fps・25 Mbps を下回る。無料口座の 140 秒・512MB 以内）
  ffmpeg -i master.mp4 -vf "fps=30,format=yuv420p" -c:v libx264 -profile:v high -crf 23 -maxrate 20M -bufsize 40M -g 15 -c:a aac -b:a 160k -ar 48000 -movflags +faststart x.mp4
  # Reels／TikTok 用（9:16 の別マスターから。23–60fps、Reels API の 25 Mbps 以下）
  ffmpeg -i master_9x16.mp4 -vf "fps=30,format=yuv420p" -c:v libx264 -profile:v high -crf 20 -maxrate 20M -bufsize 40M -c:a aac -b:a 128k -ar 48000 -movflags +faststart reels.mp4
  ffprobe -v error -show_entries format=duration,size,bit_rate:stream=codec_name,profile,width,height,r_frame_rate,pix_fmt -of default=nw=1 x.mp4
  ```
- **動いたと言える確かめ方**: ffprobe で fps が 30、pix_fmt が yuv420p、profile が High、size と duration が表の上限内。上げた後にどの解像度で再生されるかは各サービスで見る（西尾が決めること）
- **所要の見込み**（推測）: 版の作り分けのスクリプト化で 1 時間

## Open Questions

- Instagram・TikTok の利用者向けヘルプが読めず、アプリから上げるときの上限（長さ・サイズ）は API・広告の仕様からの推定にとどまる
- X のヘルプ（無料 140 秒・40fps）と API（既定 20 分・60fps）のどちらが実際の UI の制限か。上げて確かめるしかない
- Bluesky の現行の上限（3 分か 10 分か、100MB か 300MB か）は原典未確認
- 各社が再生時に音量を正規化するか、色空間の札をどう扱うかは公式の記述を見つけていない
- LinkedIn のヘルプは「2 years ago」の更新で、API（30 分・500MB）とも違う
