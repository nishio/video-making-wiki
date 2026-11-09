---
type: concept
summary: 動画の検査と仕上げ（閃光・字幕・音量・色とコントラスト・コンタクトシート・出す場所の仕様）の道具と手順を、第 3 回サーベイ（2026-11-09）の文献と西尾の経験で並べたページ。閃光は IRIS と自前の画素ごとの近似を並べて読む、字幕は台本を正にして整列の道具には時刻だけ出させる、loudnorm は 2 パスでも条件を満たさないと線形にならない、出す場所の仕様は公式のヘルプと API で食い違う
video_types: [any]
sources:
  - web-check-flash-*.md（3）
  - web-check-subs-*.md（4）
  - web-check-ja-*.md（2）
  - web-check-loudness-*.md（2）
  - web-check-color-*.md（3）
  - web-check-spec-*.md（4）
  - web-means-critic-*.md
  - exp-html-capture-pipeline.md、exp-sutra-hype-editions.md、exp-galleria-ffmpeg-measurement-and-delivery.md
---

# 検査と仕上げ

表現手段の一覧は [[expression-means]]、明日からやることは [[ready-to-start-2026-11-10]]。

**読み方**: 手順はどれも各ページの「着手の仕方」の要約で、**未検証（galleria で確かめる）**。CyEC2 では何も入れず、何も動かしていない。

## 一覧

| 検査 | 道具 | 何が分かるか | 限界 | 出典 |
|---|---|---|---|---|
| 閃光 | EA の IRIS（C++、BSD-3）、Python 移植の iris-pse-detection 1.1.2（MIT） | 秒ごとの閃光の回数と、赤の閃光の合否（CSV で出る） | 明るさを画面全体の平均の差で見るので、画面の一部だけの閃光を見逃しうる（担当がソースを読んだ解釈。動かしてはいない）。拠り所の規格は書かれておらず、値は WCAG 2.0 の式、面積は ITU 側の書き方 | [[web-check-flash-ea-iris]] |
| 閃光 | 自前の近似（ffmpeg で縮小した rawvideo を numpy で画素ごとに数える） | ITU と WCAG の両方の面積の基準で、危ない秒を出す | 規格の道具ではない | [[web-check-flash-ffmpeg-signalstats-photosensitivity]] |
| 閃光 | PEAT v1.6（2017、Windows）、Harding FPA（商用。hardingtest.com は 1 本 £30 から） | 公的に使われてきた判定 | PEAT は AVI の録画が前提で、テレビ・映画・ゲームの商用作品には使用禁止。Harding は動画を外部に上げる | [[web-check-flash-peat-harding-fpa]] |
| 字幕の時刻 | stable-ts の `align()`、Qwen3-ForcedAligner-0.6B、WhisperX、MFA | 台本の文字のまま音声に時刻を付ける | Qwen の日本語の平均ずれ 42.2ms は Qwen の自己報告 | [[web-check-subs-whisperx-stable-ts-faster-whisper]]、[[web-check-subs-qwen3-forcedaligner-mfa-reazonspeech]] |
| 字幕の改行 | BudouX 0.10.3、CSS の `word-break: auto-phrase` | 文節で改行する | — | [[web-check-subs-budoux]] |
| 字幕の焼き込み・配信 | ffmpeg の subtitles／ass フィルタ（fontsdir、WrapStyle 2）、YouTube の字幕ファイル | 日本語フォントを指定して焼き込む。同じ正本から SRT・VTT も出す | libass の自動の折り返しに日本語を任せない | [[web-check-subs-ffmpeg-libass-youtube-caption-files]] |
| 音量 | ffmpeg の ebur128、loudnorm の 2 パス、ffmpeg-normalize 1.43.0（MIT） | 全体の LUFS と True Peak。ステムを別々に測れば声と BGM の差も | 2 パスでも、入力の LRA と TP が条件を満たさないと、警告なしで dynamic に戻る | [[web-check-loudness-ffmpeg-loudnorm-ebur128]]、[[web-check-loudness-ffmpeg-normalize]] |
| コントラスト | WCAG 2.2 の相対輝度の式で、描画の指定色かコマの画素から計算する | 文字と背景のコントラスト比 | canvas の文字は Lighthouse・DevTools で測れない（推論） | [[web-check-color-wcag-contrast-on-frames]] |
| 色覚 | DaltonLens（Brettel・Viénot・Machado）、Puppeteer の `emulateVisionDeficiency` | 色だけで区別していないか | Chrome は Machado の行列を使うが、2 色覚には Brettel・Viénot の方が当事者の評価が良かった（DaltonLens の 2021 の追記）。Puppeteer の模擬は `page.screenshot` にだけ乗り、`toDataURL` には乗らない（推論） | [[web-check-color-cvd-simulation-daltonlens-machado-chrome]] |
| 色域・札 | ffprobe の color_space、signalstats の BRNG、limiter | BT.709 の札、範囲外の画素 | ネット動画で効くのは範囲より札（YouTube は札が無ければ BT.709 とみなす） | [[web-check-color-ffmpeg-signalstats-limiter-ebu-r103]] |
| 見渡す | ffmpeg の select・fps・tile・drawtext（`%{pts\:hms}`、`%{n}`） | 全編を数枚で見る（人にも批評役のモデルにも渡せる） | 場面転換の閾値は動きの多い素材で効かない（[[exp-galleria-ffmpeg-measurement-and-delivery]]）。等間隔を主にする | [[web-check-spec-ffmpeg-contact-sheet-select-tile-drawtext]] |
| 止まり | ffmpeg の freezedetect | 2 秒以上止まった所 | — | [[web-nonscreen-cell-iop-nejm-video-abstract-guides]] の「2 秒以上止めない」に使う（担当の案） |
| 中身が伝わるか | 批評役のモデル（Gemini の動画入力、ローカルの Qwen3-VL） | ナレーションの事実の誤り、分かりにくい時刻 | 点数は人と合わない。同期・停止・閃光は拾えない | [[expression-means]] の批評役の節 |

## 閃光（第 2 回の次の手 1）

- 第 2 回で、般若心経アゲアゲ版 R3 が閃光の基準の境目になりうると分かった（[[design-fundamentals]]）。第 3 回で、測る道具と手順まで落とした（[[web-check-flash-ea-iris]]）。
- **R1 だけのレビューでは足りない**。[[exp-sutra-hype-editions]] は「R2・R3 は R1 で判断できる」としてレビューを R1 だけで回したが、閃光は BPM で決まる。
  - R3 は 176BPM で、1 モーラ（16 分音符）は約 85ms。
- 面積の基準は、ITU（画面の 25%）と WCAG（341×256 の窓の 1/4）で、全画面の動画では WCAG の方が約 9 倍厳しい（[[web-check-flash-peat-harding-fpa]]）。どちらで合否を言うかは西尾が決める。
- 道具を信じる前に、合成した試験の動画で確かめる。全画面 5Hz・全画面 2Hz・画面の左 20% だけ 5Hz の 3 本を、IRIS と自前の近似の両方に通す（手順は [[ready-to-start-2026-11-10]]）。
- ループで流す embed は、2 周つないでから検査する（継ぎ目の閃光を拾うため。担当の案）。

## 字幕と日本語の速さ

- 台本がある西尾の作りでは、**字幕の文字は台本を正にし、整列の道具には時刻だけ出させる**。これは [[exp-sutra-sync-subtitles]] の「内容と時間の正本を分ける」と同じ向き。
- 日本語の字幕の速さの研究が見つかった。豊倉・山田 2017 は「1 秒 6 字までは視線の負荷が変わらず、8 字で増えた」と報告している（[[web-check-ja-toyokura-yamada-2017-subtitle-4-chars]]）。
  - ただし、視線を測ったのは 5 人だけで、全員が英語の上級者。
  - 理解度は測っていない。
  - Netflix の「1 秒 4 字」（[[design-fundamentals]]）より緩い側の結果。
- 話す速さの目安は、約 5〜8 モーラ／秒（[[web-check-ja-speech-rate-mora]]）。
  - JLPT の聴解の音声で、N5 は 5.05、N1 は 7.07 モーラ／秒。
  - 日常会話の平均は約 6.6 モーラ／秒。
  - アゲアゲ版 R3 は約 11.7 モーラ／秒で、「速さ自体が見せ物」の領域にある。
  - [[exp-lt-20260909]] の「1 分 300 字」には、一次資料が見つからなかった。

## 音量

- [[exp-html-capture-pipeline]] の `loudnorm=I=-16:TP=-1.5:LRA=11` は、loudnorm の作者のブログにある 1 パスの例と一字一句同じ。1 パスなので dynamic で動いていて、`-ar` が無ければ 192 kHz で出ている可能性がある（[[web-check-loudness-ffmpeg-loudnorm-ebur128]]）。
- 2 パスにしても、線形になるには条件がある。
  - measured_* の 4 つを全部渡す。
  - 入力の LRA が目標以下。
  - 入力の True Peak ＋上げ幅が、目標の TP 以下。
- ffmpeg-normalize の `--keep-loudness-range-target --auto-lower-loudness-target` で、黙って dynamic に戻るのを避けられる、と作者は書いている。`-p` を付けると、実際に使われた normalization_type を確かめられる（[[web-check-loudness-ffmpeg-normalize]]）。
- 声と BGM の差（Torcoli の 10 LU。[[narration-bgm-sound]]）は、ステムを別々に ebur128 で測って出す。ステムの統合値の差で近似するのは推測。
- 比べて選ぶときは、先にラウドネスを揃える。大きい音を良いと判定する偏りは、評価役のモデルにある（[[web-means-critic-omni-judge-audiojudge]]）。

## 出す場所の仕様（2026-11-09 時点の公式ページ、check-spec 担当の表）

詳しい原文と食い違いは、[[web-check-spec-youtube-upload-shorts]]、[[web-check-spec-x-instagram-tiktok-linkedin-bluesky]]、[[web-check-spec-powerpoint-keynote-google-slides-formats]] にある。Instagram・TikTok は利用者向けヘルプの本文が取れず、API と広告の仕様で埋めた。Bluesky の 3 分・10 分は二次情報。

| 出す場所 | 縦横比・解像度 | fps の上限 | 長さの上限 | ファイルサイズ | コーデック | 字幕ファイル | ループ | サムネイル | 推奨ビットレート | 出典（最終更新） |
|---|---|---|---|---|---|---|---|---|---|---|
| YouTube（通常） | 16:9 が標準、他の比はプレイヤーが合わせる（黒帯を足すな）。1080p＝1920×1080〜8K | 記述なし（「録ったまま」、24〜60 が一般的） | 未確認の口座は 15 分、確認済みは 12 時間 | 256 GB | MP4（faststart、Edit List なし）、H.264 High・4:2:0・closed GOP、AAC-LC か Opus 48 kHz、SDR は BT.709 | SRT・SBV・VTT・TTML・SCC など | 記述なし | 自作（3840×2160 推奨、最小幅 640、50MB）か自動の候補 | 1080p は 8 Mbps（30fps 級）/ 12 Mbps（60fps 級）。音声ステレオ 384 kbps | support.google.com/youtube/answer/1722171・6375112・71673・2734698・72431（更新日の表示なし） |
| YouTube Shorts | 正方形か縦長で 3 分以内なら自動で Shorts（2024-10-15〜）。上げられるのは 1080p まで | 同上 | 3 分 | 同上 | 同上 | 同上 | 繰り返しも再生回数に数える（2025-03-31〜） | 自作は PC の Studio で確認済み口座のみ。縦長に 16:9 のサムネイルを付けるとホーム等では自動の 4:5 に置き換わる | 同上 | answer/15424877・10059070・72431 |
| X | ヘルプ（ウェブ）: 32×32〜1920×1200（縦 1200×1900）、1:2.39〜2.39:1。API: 推奨 1280×720 等、1280×1024 以下・1:3〜3:1 | **ヘルプ（ウェブ）40fps、API 60fps** | ヘルプ: 無料 140 秒、Premium 4 時間。API: 既定 20 分 | ヘルプ: 512MB / 16GB。API: 8GB | H.264 High、4:2:0 のみ、AAC-LC（HE-AAC 不可）、open GOP 不可 | API は SRT・VTT。ヘルプは通常投稿の方法を書いていない | 60 秒以下は自動でループ | 通常投稿は記述なし | ヘルプ上限 25 Mbps。API は映像 5,000 kbps 以上 | help.x.com/en/using-x/x-videos（2026-10-12、IA 2026-10-21 版）、docs.x.com media best-practices |
| Instagram（Reels） | API: 0.01:1〜10:1、9:16 推奨。広告: 1440×2560 | API: 23–60 | 3 秒〜15 分 | API 300MB、広告 4GB | MOV・MP4（moov 先頭）、H.264 か HEVC（closed GOP、4:2:0）、AAC 48 kHz まで | 読めた記述なし | 記述なし | API: cover_url か thumb_offset（既定は最初のコマ） | 最大 25 Mbps、音声 128 kbps | developers.facebook.com IG User Media（2026-09-28）、Meta 広告ガイド。**利用者向けヘルプは読めず** |
| Instagram（フィード） | 広告: 9:16・1080×1920 | 記述なし | 広告: 1 秒〜60 分 | 広告 4GB | MP4・MOV | 記述なし | 記述なし | 記述なし | 記述なし | Meta 広告ガイド。**利用者向けは読めず** |
| TikTok | API: 360〜4096 画素。広告: 9:16・540×960 以上 | API: 23–60 | 全員 3 分、一部 5・10 分（API は 10 分まで） | API 4GB、広告 500MB | MP4・WebM・MOV、H.264 推奨 | 読めた記述なし | 記述なし | API: video_cover_timestamp_ms（既定は最初のコマ） | 広告: 516 kbps 以上 | developers.tiktok.com（2026-08-04・2026-10-27）、ads.tiktok.com（2026-06）。**利用者向けヘルプは読めず** |
| LinkedIn | 1:2.4〜2.4:1、256×144〜4096×2304 | 10–60 | ヘルプ 15 分（最短 3 秒）、API・広告 30 分 | ヘルプ 5GB、API 500MB | MP4・MOV・WEBM・MKV など | API: SRT 1 本、英語のみ | 記述なし | API で上げられる、無ければ自動 | 192 kbps〜30 Mbps | linkedin.com/help a548372・a564109、Microsoft Learn Videos API（2026-02-12） |
| Bluesky | aspectRatio を付ける | 記述なし | 公式ブログ（2024-09）60 秒。二次情報では 3 分 → 10 分 | 二次: 300MB。公式: 1 日 25 本 / 10GB | mp4・mpeg・webm・mov | 字幕可（公式）。VTT（二次） | 記述なし（自動再生は既定でオン） | 記述なし | 記述なし | bsky.social/about/blog/09-11-2024-video。**lexicon は取得できず** |
| PowerPoint | 記述なし | 記述なし | 記述なし | ウェブ版 256MB | 推奨 H.264＋AAC の .mp4（.mov・.webm 可）。2505 以降で古い形式の対応を縮める | 動画ファイルに埋め込まれた字幕トラックを表示 | 現行ページで確かめられず | 記述なし | 記述なし | support.microsoft.com（更新日なし）。既定は**埋め込み**。開始は In Click Sequence、Automatically も可 |
| Keynote（Mac） | 記述なし | 記述なし | 記述なし | 記述なし | QuickTime が扱える形式。HEVC・ProRes を H.264 に変換する設定あり | macOS 26.4 以降で字幕を表示 | **あり**（Loop、Loop Back and Forth）、自動開始可 | ポスターフレーム | 記述なし | support.apple.com/guide/keynote（更新日なし）。**ファイルを書類に持つ** |
| Google Slides | Drive での再生は 1920×1080 まで | 記述なし | 記述なし | Drive の容量 | Drive: MP4・MOV（H.264＋AAC）、WebM | Drive のプレイヤーに CC（Slides での表示は記述なし） | 記述なし | 記述なし | 記述なし | support.google.com/docs/answer/97447。**YouTube か Drive を参照**（発表者に権限が要る）。既定 Play (on click)、automatically 可 |

表から読めること:
- **X は、ヘルプ（ウェブ 40fps・無料 140 秒）と API（60fps・20 分）で数値が食い違う**。[[exp-gyazo-resumption-video]] の 60fps の版は、ヘルプ側の制限にかかりうる（[[promo]] の要確認と同じ）。
- **最初のコマがカバーになる**ことは、TikTok と Instagram の API の既定として公式に書かれている。X の通常投稿については記述が無い。
- YouTube の推奨は、音声 48 kHz・ステレオ 384 kbps と faststart。経験は AAC 256k で、faststart は X 用の版にしか付けていない（[[exp-html-capture-pipeline]]）。
- **スライドに埋める（embed）なら、3 つのソフトに共通して通る形は H.264＋AAC の .mp4・1080p**。
  - Google Slides は YouTube か Drive を参照する形で、発表者に閲覧の権限が要る。再生は 1080p まで。
  - ループを公式に書いているのは Keynote だけ。流しっぱなしで繰り返すなら、繰り返しを動画の中に書き出す方がソフトに依存しない（推論）。

## Open Questions

- IRIS が画面の一部の閃光を見逃すかは、ソースを読んだ解釈にすぎない。合成動画で確かめるまでは、自前の近似と並べて読む。
- 西尾の動画の色・コントラストは、描画コードの指定色から計算できるはずだが、まだしていない（[[exp-sutra-sync-subtitles]] の橙だけの強調も、[[design-fundamentals]] で未計算のまま）。
- ffmpeg が RGB の PNG を yuv420p にするときの既定の行列は、文書に書かれていない。galleria で ffprobe の color_space を見れば分かる。
- 日本語字幕の速さの研究は 1 本だけで、人数が少ない。
- 批評役のモデルと機械の検査の役割分担（どちらに何を任せるか）は、両方を回してみるまで決まらない。

## Updates

### 2026-11-09 動画編集を AI にさせる方法のサーベイから（[[ai-editing]]）

- AI に編集させた動画の検査（[[web-edit-research-timeline-bench-medit-bench]]）: Timeline-Bench は破綻の検査 6 種と、判定役に渡す 4 つの数値（1 分あたりのカット数、最長の静止、統合ラウドネス、無音の割合）を使う。エージェントは人の 0.72 倍しか切らず、静止を 1.5 倍長く持った。どれも ffmpeg で出せる（未検証）
- エージェントの自己点検は当てにならない。テストに落ちた回の 95.5% で「成功」と報告していた（同）。video-use は切れ目の ±1.5 秒の画像、`ebur128`、批評役のサブエージェントで点検する（[[web-edit-agent-video-use-and-claude-code-editing-examples]]）が、最後は人が通しで見る
