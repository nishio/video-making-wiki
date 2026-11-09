---
type: source
summary: DaVinci Resolve（Blackmagic Design）の AI 編集機能を、公式の製品ページ（Resolve 21、2026-11-09 時点）と New Features Guide（20＝2025-04、21＝2026-04）で読んだもの。文字起こしとテキストベース編集、台本（.txt・Final Draft）と文字起こしを照合して荒つなぎを作る IntelliScript、無音の削除（IntelliCut）、話者に合わせたマルチカムの自動切替（SmartSwitch）、Smart Reframe、21 の IntelliSearch と「既存の字幕・文字起こしを取り込んで時刻を検出」。AI 機能の多くは有料の Studio（$236、表示は 20% 引き）だけで、日本語の文字起こしは Studio の拡張言語パック。端末で動き、アップロードしない作り
video_types: [talk, promo, embed]
url: https://www.blackmagicdesign.com/products/davinciresolve/whatsnew
author: Blackmagic Design（製品ページ、DaVinci Resolve 20／21 New Features Guide）
published: Resolve 20 New Features Guide 2025-04-22、Resolve 21 New Features Guide 2026-04-10（PDF の作成日）。製品ページは 21.1 の表示
retrieved: 2026-11-09
sources:
  - https://www.blackmagicdesign.com/products/davinciresolve
  - https://www.blackmagicdesign.com/products/davinciresolve/whatsnew
  - https://www.blackmagicdesign.com/products/davinciresolve/studio
  - https://documents.blackmagicdesign.com/SupportNotes/DaVinci_Resolve_20_New_Features_Guide.pdf
  - https://documents.blackmagicdesign.com/SupportNotes/DaVinci_Resolve_21_New_Features_Guide.pdf
---

# DaVinci Resolve（Studio）— IntelliScript、テキストベース編集、無音の削除

## 何の文献か

- Blackmagic Design の一次資料。製品ページ（Resolve 21、「What's New in 21.1」の表示）と、版ごとの New Features Guide（PDF。20 は 3,953 行、21 は 6,132 行を pdftotext で読み、該当の節を読んだ）。21 の Guide は「will be included in the DaVinci Resolve reference manual after the public beta」と書く（公開ベータ時の文書）
- Reference Manual（数千ページ）全体は読んでいない。Resolve 19 以前の導入時期は Guide に無い機能について確かめていない
- scripting API（Python／Lua）は別の担当のページで扱うので、ここでは触れる程度

## 書いてあること

### 無料版と Studio の差（製品ページ）

- 無料版: 「works with virtually all 8-bit video formats at up to 60fps in resolutions as high as Ultra HD 3840 x 2160」、マルチユーザー共同作業・HDR グレーディングを含む
- Studio: 「Includes everything in the free version plus the DaVinci AI Neural Engine, dozens of additional Resolve FX, temporal and AI spatial noise reduction, **text based editing**, magic mask ...」。10-bit・120fps・4K 超
- Studio のページ: Neural Engine の機能として「facial recognition ... Super Scale ... speed warp ... magic mask ... **smart reframe**, object removal, scene cut detection」を挙げ、「found exclusively in DaVinci Resolve Studio」と書く
- 価格: 「Davinci Resolve Studio Buy Online Now **$236**」「Save 20%」（2026-11-09 の表示。通常価格は表示されていない。20% 引きなら $295 と計算できるが、通常価格の公式の記述は読んでいない）。無料版は「Free」。Mac・Windows・Linux
- Neural Engine は「fully supported in Apple M series and Snapdragon X Elite」、GPU で動く（whatsnew）

### Resolve 20（2025）で入った AI 編集機能（New Features Guide 20）

- **AI IntelliScript（Studio Version Only）**: 「uses the Transcription Engine to match and generate a timeline using an original script」。手順は、台本を .txt で用意 → Media Pool でクリップを選び右クリック **AI Tools > Audio Transcription > Transcribe** → 文字起こしの後、再び選んで **AI Tools > Create New Timeline Using IntelliScript** → 台本ファイルを開く。結果は「track one ... the best clips in order based on the dialog in the script file. Any alternative takes are automatically placed on additionally created tracks that are disabled by default」。アドリブで台本と少し違う言い回しでも見つける、と書く
  - 「NOTE: IntelliScript chooses the "best" take by matching the spoken dialog only. It does not use any good take metadata or make any judgments based on anything other than dialog matching」
- **転写の品質向上と言語の追加（Studio Version Only）**: Extras Download Manager で「Extended Transcription Language Support」を入れ、Project Settings の Subtitles and Transcription で「Enable Extended Language Support」。言語の一覧に **Japanese** がある（ほか Korean・Chinese など 57 言語）。「some of these languages are still in beta」
- 文字起こしの書き出しに話者と timecode が入る
- **AI Animated Subtitles（Studio）**: 字幕トラックに置くアニメのテンプレート。転写エンジンと合わせて語ごとに動く
- **AI Multicam SmartSwitch（Studio）**: 映像の角度と音声の両方から話している人を判断してマルチカムを自動で切り替える。「great for giving you a good first pass and letting you finesse the rest」。最短のカットの長さ、無音や話者の重なりで広角に戻す設定がある
- **AI IntelliCut（Studio）**（Fairlight ページ）:
  - **AI Remove Silence**: Range ツールで範囲を選び右クリック **Remove Silence**。Threshold（dB）・Pre Head・Post Tail・Minimum to Strip（ms）・Fade Head and Tail を設定。「non-destructive」
  - Checkerboard to New Tracks（1 本の録音から話者ごとのトラックに分ける）、Create ADR Cues
- AI Voice Convert（Studio）、AI Dialogue Matcher（Studio）、AI Music Editor（Studio）、拍の検出
- AI Audio Assistant（自動ミックス）は Resolve 20 の機能として販売店のページ・記事に出るが、New Features Guide 20 の本文では見つけられなかった（二次情報のみ）

### Resolve 21（2026）の追加（New Features Guide 21、製品ページ）

- **AI IntelliSearch**: Extras Download Manager でモデルを入れ、Faster／Better を選び、Media Pool を解析。物・人・顔・会話の語を検索（「Search Transcript Only」もある）。顔に名前を付けて検索できる
- **既存の字幕・文字起こしの語の時刻を検出**: 「DaVinci Resolve 21 now has the ability to perform word timing analysis on manually entered or imported captions」。字幕クリップは Inspector の Caption タブで **Update Word Timings**、トラック全体は右クリック **Synchronize Word Timings**。Media Pool のクリップには **AI Tools > Audio Transcription > Import and Detect Timing**
- **IntelliScript が Final Draft（.fdx）と平文の脚本の書式に対応**
- 縦・正方形の解像度の設定を足し、「Combine with Smart Reframe to quickly setup your timeline for vertical or square resolution videos」。YouTube・TikTok・Vimeo・X への直接アップロード
- AI Slate ID、AI Speech Generator（自分の声を 10 秒から）、CineFocus、顔の加工、UltraSharpen、Motion Deblur
- OGraf HTML グラフィックと Lottie（.json・.lottie）をそのまま Media Pool に入れて、透過付きのアニメのクリップとして使える
- Media Pool のリスト表示に Transcription の列

### 素材の扱い・利用条件

- Neural Engine の機能は端末の GPU で動き、製品ページ・Guide に素材をアップロードして処理するという記述は無い（IntelliSearch・拡張言語もモデルを端末にダウンロードする方式）。共同作業の Blackmagic Cloud は別の仕組み
- 生成 AI の利用条件・学習への利用に当たる条文は、この版の製品ページと Guide には無かった。ソフトの使用許諾（EULA）の本文は読んでいない

## この wiki への含意

- **台本を正本にする作り方に一番近い**。IntelliScript は「台本 → 文字起こしと照合 → 台本の順に最良のテイクを並べ、別テイクは無効のトラックに置く」で、人が後から差し替える前提の設計。[[exp-sutra-sync-subtitles]] の「内容と時間の正本を分ける」、[[exp-shortmovie-draft-generator]] の「タイムスタンプは字幕データを正に、LLM には触らせない」と同じ向き（時刻は転写エンジンが決め、LLM に作文させない）
- 21 の「Import and Detect Timing」「Synchronize Word Timings」は、台本の文字を正にして語の時刻だけを音声から取る、という [[web-check-subs-qwen3-forcedaligner-mfa-reazonspeech]] の強制整列と同じ仕事を GUI の中でやる。日本語で効くかは公式に書かれていない（言語の一覧に Japanese はあるが、時刻の検出の節は言語に触れていない）
- 「best take」の判断は台詞の一致だけで、演技・言い間違い・表情は見ない、と公式が書いている。取りの良し悪しの判断は人に残る（または映像を見るモデルに回す。[[web-means-critic-gemini-video-understanding]]）
- Lottie を直接読めるので、コードで描いたアニメ（[[web-means-3d-lottie-rive-seek]]）を実写の上に重ねる仕上げの場になる
- AI 機能はほぼすべて Studio 限定。無料版では文字起こしで編集する道具として使えない（製品ページの比較）

## 何を AI に任せられるか／何が人に残るか

- **任せられる（公式）**: 文字起こし（日本語は Studio の拡張パック、一部 beta）、台本からの荒つなぎとテイクの整理（IntelliScript）、無音の削除（閾値で）、話者に合わせたマルチカムの切替の初版、縦・正方形への Smart Reframe、語の時刻に合わせた字幕アニメ、取り込んだ字幕への語の時刻の付与、物・顔・会話の検索、スレートの読み取り
- **人に残る（公式）**: IntelliScript の別テイクの選び直し（「preview alternative takes ... enabling and disabling them as needed」）、SmartSwitch の結果の手直し（「letting you finesse the rest」）、無音削除の閾値の調整（「some of the remaining audio sounds "chopped up"」と Guide が注意）。会話による編集のエージェントは、この 2 冊の Guide には無い

## 着手の仕方（未検証。galleria で確かめる）

- **何が表現できるようになるか**: 台本どおりに話した収録（講演の練習・解説のナレーション付き画面収録）を、台本から自動で荒つなぎし、無音を詰め、台本の文字を正にした字幕を語の時刻付きで焼く。効く型: talk（台本のある解説）、embed（流しっぱなしの短い解説）、promo（縦の切り抜き）
- **機械**: **galleria Windows**（RTX 5080。Neural Engine は GPU）。Mac（Apple Silicon）も可。Linux 版もあるが WSL での GPU 利用は未確認なので Windows 側を推す（推測）
- **入れるもの・費用・アカウント**: DaVinci Resolve 21（無料）と **Studio（$236 の表示、要: 購入。西尾が決める）**。AI 編集機能の試しには Studio が要る。拡張の文字起こし言語と IntelliSearch のモデルは Extras Download Manager から
- **成熟度**: 21.1 が製品ページの表示。20（2025）→ 21（2026）と年 1 回の大きな版
- **最小の手順（GUI。Guide のメニュー名から）**:
  1. Resolve Studio を入れる → DaVinci Resolve > Extras Download Manager → Extended Transcription Language Support をダウンロード → Project Settings > Subtitles and Transcription で「Enable Extended Language Support」、言語を Japanese
  2. 台本（.txt、日本語）を用意し、同じ台本を 2 回読んだ収録を 2 クリップ取り込む
  3. 2 クリップを選び右クリック AI Tools > Audio Transcription > Transcribe
  4. 再び選び AI Tools > Create New Timeline Using IntelliScript → 台本 .txt を開く
  5. Fairlight ページで Range ツールで範囲を選び右クリック Remove Silence（Threshold と Minimum to Strip を設定）
  6. （21）台本から作った字幕を Media Pool のクリップに AI Tools > Audio Transcription > Import and Detect Timing、または字幕トラックを右クリック Synchronize Word Timings
  7. Deliver ページで書き出し
- **動いたと言える確かめ方**: 手順 3 で Media Pool の Transcription の列に日本語が出る。手順 4 で新しいタイムラインができ、track 1 に台本の順でクリップが並び、無効のトラックに別テイクがある（台本の文の数と track 1 のクリップの区切りを数えて比べる）。手順 5 で赤い縞の区間が出て、尺が短くなる。手順 6 で字幕の語ごとのハイライトが音声と合う（目視で 5 か所、ずれを ±何フレームで記録）。書き出しを ffprobe
- **所要の見込み（推測）**: 導入と言語パック 30 分、試し 1〜2 時間

## Open Questions

- 日本語で IntelliScript の照合（アドリブの許容）と語の時刻の検出がどれだけ合うか。公式は日本語での精度を書いていない
- Studio の通常価格と、表示の 20% 引きの期間
- 拡張言語パックの日本語が beta に入るか（「some of these languages are still in beta」とだけ書き、どれかは書いていない）
- Resolve 20 の「AI Audio Assistant」の一次資料（Reference Manual の該当章）
- EULA に AI 機能・生成物（AI Speech Generator の声）の条件があるか
