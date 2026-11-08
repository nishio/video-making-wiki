---
type: source
summary: 実機・手元を iPhone で撮るときの最小の設定を Apple の公式ガイド（iPhone ユーザガイドの iOS 27 版と Apple Support の HEVC の記事、2026-11-09 取得）で押さえたページ。形式は「互換性優先」で H.264、「高効率」で HEVC。対応機種は既定で HDR（Dolby Vision）で撮る。暗い所では Auto FPS が 24fps に落とす。カメラの自動切り替え・ホワイトバランスは録画中に固定できる。編集に渡す前に HDR・Auto FPS・形式を決めておく
video_types: [promo, talk, embed]
url: https://support.apple.com/guide/iphone/change-video-recording-settings-iphc1827d32f/ios
author: Apple（iPhone ユーザガイド、Apple Support）
published: unknown（iOS 27 版のユーザガイド。ページに日付の表示なし）
retrieved: 2026-11-09
sources:
  - https://support.apple.com/guide/iphone/change-video-recording-settings-iphc1827d32f/ios
  - https://support.apple.com/guide/iphone/record-a-video-iph61f49e4bb/ios
  - https://support.apple.com/guide/iphone/adjust-hdr-camera-settings-iph2cafe2ebc/ios
  - https://support.apple.com/en-us/116944（「Using HEIF or HEVC media on Apple devices」）
---

# 実機・手元を iPhone で撮るときの設定（Apple の公式ガイド）

## 何の文献か

- Apple の公式のユーザガイド（iOS 27 版）とサポート記事。機能の説明で、どの設定が編集に向くかの推奨は書いていない（HEVC の記事だけは互換性について書く）
- 西尾が THINKLET のデモで実機を iPhone で撮った経験（[[exp-thinklet-reading-demo-video]]）に、設定の側の一次資料を足すために読んだ。深追いはしていない（担当の割り振りで「深追いしなくてよい」とされた項目）

## 書いてあること

### 解像度・fps（「Record a video」）

- 「Depending on your iPhone model, you can record video in high-quality formats, like HD, 4K, HD (PAL), and 4K (PAL). Also depending on your model, you can change the fps rates to 24, 25, 30, 60, or 120」。設定 → カメラ → ビデオ撮影で既定を選ぶ。撮影画面の右上で切り替えもできる
- 「Faster frame rates and higher resolutions result in larger video files」
- Action mode は「improved stabilization」で、明るい所で最もよく効く

### 撮影中に変わってしまうもの（「Change video recording settings」）

- **Auto FPS**: 「iPhone can improve the video quality in low-light situations by automatically reducing the frame rate to 24 fps」。30fps だけ・30 と 60 の両方・オフを選べる（機種による）
- **HDR**: 「iPhone records video in HDR and shares HDR videos with devices using iOS 13.4, iPadOS 13.4, macOS 10.15.4, or later; other devices receive an SDR version of the same video」。HDR のガイドでは「iPhone records video in Dolby Vision HDR」。オフは設定 → カメラ → ビデオ撮影 → HDR ビデオ
- **カメラのロック**: 「the Lock Camera setting prevents switching between cameras while recording video. Lock Camera is off by default」
- **手ぶれ補正（強化）**: 「zooms in slightly to provide improved stabilization ... Enhanced Stabilization is on by default」
- **ホワイトバランスのロック**: 録画中のホワイトバランスを固定できる
- 音: iPhone 16 以降は既定で空間オーディオ。ステレオ・モノラルを選べる

### 形式（Apple Support「Using HEIF or HEVC media」）

- 設定 → カメラ → フォーマットで「互換性優先（Most Compatible）」にすると「All new photos and videos will now use JPEG or H.264 format」。「高効率（High Efficiency）」は HEIF・HEVC
- 「On some older devices, support for HEVC is affected by the resolution and frame rate (fps) of the video. Resolutions of 1080p or lower and frame rates of 60 fps or lower are more broadly compatible」
- USB で PC に取り込むと「the media might be converted to JPEG or H.264」。変換させないなら設定 → アプリ → 写真 →「元のフォーマットのまま」（Keep Originals）

## この wiki への含意

- **Auto FPS は VFR の素材を作る**。暗い会場・室内で手元を撮ると、途中で 24fps に落ちうる。galleria の経験の「画面録画は VFR になりやすい、秒は pts でしか取れない」（[[exp-galleria-ffmpeg-measurement-and-delivery]]）と同じ問題が実機の側にもある。台本どおりの尺合わせ（ナレーションの区間に映像を置く、THINKLET の方式）をするなら、Auto FPS は切る
- **HDR は SDR の画面収録と混ぜると色が合わない**（推測。Apple の文書は「対応しない機器には SDR 版が渡る」とだけ書く）。画面収録（Playwright・OBS）・canvas の描画（[[exp-html-capture-pipeline]]）は SDR なので、実機の映像も SDR で撮る（HDR をオフ）のが簡単。HDR のまま撮ったら、編集の前にトーンマッピングが要る
- **カメラの自動切り替えと手ぶれ補正の「少し拡大」は、実機の画面（小さな表示・LED）の位置を変える**。端末の画面を手元で撮るなら、カメラのロックを入れ、三脚・スマホ用の固定具で撮り、強化手ぶれ補正は切る（推測）
- THINKLET では縦長 1080×1920 の映像を横長のシーケンスに置き、横に画面のスクリーンショットを並べた（[[exp-thinklet-reading-demo-video]]）。**画面とカメラの合成**は、撮りながらなら OBS のシーン（[[web-means-capture-obs-studio]]）、撮った後なら ffmpeg の overlay か西尾の canvas で並べる

## 着手の仕方（未検証。iPhone と galleria で確かめる）

- **表現できるようになること**: 実機（端末・ハードウェア・紙の本）の動きを手元から撮り、画面収録・コードの描画と色と fps の揃った素材として合成する。効く型: promo（実物）、talk（話し手）、embed（実機のデモの流しっぱなし）
- **機械**: iPhone（撮影）＋ galleria WSL（ffmpeg で確認と合成）。Mac の写真アプリからも取り出せる
- **入れるもの・費用**: 無し（iPhone の標準カメラ、既にある ffmpeg）。固定具（三脚）は推奨（推測）
- **最小の手順**:
  1. iPhone の設定 → カメラ: フォーマット「互換性優先」、ビデオ撮影 1080p・30fps、HDR ビデオ オフ、Auto FPS オフ、カメラのロック オン、強化手ぶれ補正 オフ、ホワイトバランスのロック オン
  2. 撮って取り出す（AirDrop で Mac へ、または USB）
  3. WSL で確かめる:
     ```sh
     ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate,avg_frame_rate,color_transfer,color_primaries -of default=nw=1 IMG_0001.MOV
     ```
  4. 画面収録の右下に実機を重ねる（推測で組んだ一例）:
     ```sh
     ffmpeg -i screen.mp4 -i IMG_0001.MOV -filter_complex \
       "[1:v]fps=30,scale=-2:540[c];[0:v]fps=30[s];[s][c]overlay=W-w-48:H-h-48:shortest=1" \
       -c:v libx264 -crf 18 -pix_fmt yuv420p -an composite.mp4
     ```
- **動いたと言える確かめ方**: ffprobe で `codec_name=h264`、`r_frame_rate=30/1` と `avg_frame_rate` がほぼ同じ（Auto FPS が効いていない）、`color_transfer` が `bt709` 系（HDR の `arib-std-b67` や `smpte2084` でない）。合成の `composite.mp4` で、実機の映像の色が画面収録と並べて不自然でない
- **所要の見込み（推測）**: 設定 5 分、試し撮りと確認 20 分

## Open Questions

- iPhone の画面そのもの（アプリのデモ）は、iPhone の画面収録（コントロールセンター）か、Mac の Screen Studio の iPhone 収録（[[web-means-capture-screen-studio]]）か、FocuSee の USB 収録（[[web-means-capture-focusee-recordly]]）か。比べていない
- 「互換性優先」で 4K・60fps を選べない機種がある（Apple の記事は HEVC の互換性について書く。H.264 側の上限は読んだ範囲に無い）
- 声を iPhone で録るか、別のマイクにするか（音は担当外。[[narration-bgm-sound]]）
