---
type: source
summary: Mac の Final Cut Pro（12.x、2026）と、日本語・韓国語の利用者が多い文字起こし編集ソフト Vrew（VoyagerX、4.8.2）の公式ページ。Final Cut Pro は文字起こしで編集する機能を持たず、AI は自動キャプション・Transcript Search・Visual Search・Auto Mask・Edit Detection・自動リフレームなどで、文字の機能（Generate Captions、Transcript Search、Visual Search）は「U.S. English only」。Vrew は字幕の自動生成、読みながらのカット編集、無音の短縮、原稿の読み込みによる字幕化を日本語のサイトで掲げ、「創作物を AI 学習に使わない」と明記する。Vrew の料金と利用規約は JS で描画され本文を読めなかった
video_types: [talk, promo]
url: https://www.apple.com/final-cut-pro/
author: Apple（製品ページ・リリースノート・Apple Creator Studio）、VoyagerX, Inc.（Vrew のサイト・データ保護のページ）
published: Final Cut Pro 12.4 は 2026-09-29、12.3 は 2026-06-30、12.0 は 2026-01-28。Vrew の最新版表示 4.8.2（2026-11-09）
retrieved: 2026-11-09
sources:
  - https://www.apple.com/final-cut-pro/
  - https://www.apple.com/jp/final-cut-pro/
  - https://support.apple.com/en-us/102825
  - https://www.apple.com/jp/apple-creator-studio/
  - https://apps.apple.com/jp/app/final-cut-pro/id424389933
  - https://vrew.ai/ja/
  - https://vrew.ai/ja/data-protection
---

# Final Cut Pro（Mac）と Vrew

## 何の文献か

- Final Cut Pro: Apple の製品ページ（英語・日本語）、Final Cut Pro のリリースノート（support.apple.com、12.4 まで）、Apple Creator Studio のページ（日本）、Mac App Store のページ（日本）
- Vrew: VoyagerX（韓国）の公式サイトの日本語ページとデータ保護のページ。料金（/ja/payment/pricepolicy）・利用規約（/ja/terms-of-service）は JS で描画され、curl では本文が取れなかった。料金は検索で出た第三者の記事の数字しかない（下に二次と明記）
- どちらも実機では試していない

## 書いてあること — Final Cut Pro

### AI 関連の機能（版ごと。リリースノート）

| 版（日付） | 機能 | 条件 |
|---|---|---|
| 11.0（2024-11） | Transcribe to Captions（タイムラインの話し声から字幕を作る）、Magnetic Mask | Apple シリコンと macOS Sequoia 以降。言語の記載はリリースノートに無い |
| 12.0（2026-01-28） | **Transcript Search**（話した語・句を完全一致か自然文で探す）、**Visual Search**（物・動作を自然文で探す）、Beat Detection | Apple シリコン。製品ページの注記で「Available only in U.S. English」 |
| 12.3（2026-06-30） | **Generate Captions**（字幕の生成と見た目の調整）、Auto Mask、Match Color、**Edit Detection**（書き出し済みの動画のショットの切れ目を見つけて分割） | Generate Captions は「available in U.S. English only」 |
| 12.4（2026-09-29） | Final Cut Camera の Cinematic mode の焦点の編集 | macOS 27 |

- 製品ページはほかに、Object Tracker、Enhance Light and Color（機械学習）、Smooth Slo-Mo、「Automatically reframe a clip」（縦横比に合わせた自動リフレーム）を挙げる。iPad 版には Montage Maker（「automatically selects the best visual highlights from your footage and cuts them to the beat of any song」）がある
- **文字起こしを編集すると映像が切れる機能、フィラー・無音の自動削除、会話で編集させるエージェントは、製品ページにもリリースノートにも無い**
- 「Some features of Apple Creator Studio require an Apple Intelligence–capable device」（製品ページの注記）

### 費用（2026-11-09、日本の公式ページ）

- 買い切り: Mac App Store で **¥50,000**（税込）
- Apple Creator Studio（Final Cut Pro・Logic Pro・Pixelmator Pro などのセット）: **月額 ¥1,780 か年間 ¥17,800**（新規は 1 か月無料）。学生・教職員は月額 ¥480 か年間 ¥4,800。米国の注記は「$12.99/month or $129/year」

## 書いてあること — Vrew

- 掲げる機能（公式サイト日本語版）: 「音声認識機能による**字幕の自動生成**」、「繰り返して再生しなくても早くて簡単なカット編集」（「言い間違えた部分はどこだっけ？」を「目で読みながら編集」）、「テキストエディタのような画面」、**「無音部分を短縮」**（「動画の合間の無音を探して、クリック一回で削除できます」）、**「原稿を読み込み」**（「テキストデータを入れると、自動認識して動画の字幕にできます」）、PDF から字幕とナレーション付きの動画、100 か国語以上の翻訳字幕、テキストから動画の自動生成、AI 音声（「5ヶ国語、約200+種」）、長い配信を短い動画に・Shorts の切り抜き
- 対応 OS: 「VrewはMac、Windows、Ubuntuでお使いになれます」。最新版 4.8.2
- 素材: 画像・ビデオ・BGM・効果音・フォントについて「商用目的の動画にも著作権を心配せずに安心してご利用になれます」と書く（素材ごとの条件は読んでいない）
- **データ保護のページ**: 「お客様のクリエイティブコンテンツをAI学習に利用することは決してありません」、「Vrewにアップロードされた動画・音声・画像などのコンテンツは ... 厳密に機密扱いし、お客様から明示的な許可をいただかない限り、ファイルにアクセスすることはありません」、ISO/IEC 27001:2022 と 27701:2019 の認証（SGS）。トップページにも「ユーザーの創作物がAIモデルの学習に使用されることは決してありません」
- 「アップロードされた」とあるので、音声分析はクラウドに送る方式と読める（推測。処理の場所を明記した記述は読めた範囲に無い）
- 料金（**二次情報**。miralab・atsoho などの第三者の記事による。2026-06〜07 時点の掲載値）: Free・Light・Standard・Business の 4 プラン、年額は Light ¥15,200・Standard ¥23,900・Business ¥43,000。2026-04-22 から「統合クレジット」方式になったとする記事がある。公式の料金ページの本文は読めていない

## この wiki への含意

- **Final Cut Pro は「AI に編集させる」道具としては弱い**（2026-11 時点の公式の機能一覧による）。文字で切る編集が無く、文字の AI 機能は米国英語だけ。西尾の Mac で日本語の素材を AI に切らせる目的なら、Premiere（[[web-edit-text-adobe-premiere-text-based-editing-ai-assistant]]）か DaVinci Resolve Studio（[[web-edit-text-davinci-resolve-intelliscript-studio]]）の方が公式の記述に合う
- Edit Detection（書き出し済みの動画をショットごとに分ける）は、既存の動画を素材に戻す用途に効く。ffmpeg の scene 検出（[[web-check-spec-ffmpeg-contact-sheet-select-tile-drawtext]]）を GUI でやる位置
- **Vrew は日本語の素材でそのまま試せる文字起こし編集の候補**。日本語サイトが一次資料で、「原稿を読み込み」は台本を正にした字幕づくり（[[exp-sutra-sync-subtitles]]、[[web-check-subs-qwen3-forcedaligner-mfa-reazonspeech]]）と同じ向きの機能。ただし規約・料金を読めていないので、商用・業務の素材に使えるかは未確認
- Vrew の「無音部分を短縮」は、[[exp-thinklet-reading-demo-video]] の判断（待ちを削らず説明に変える）とは逆向きの操作。デモの待ちを自動で詰めると、[[web-promo2-gemini-nikola-staged-demos]] の「時間と因果を偽らない」に触れうる。どこを詰めるかは人が決める

## 何を AI に任せられるか／何が人に残るか

- **Final Cut Pro に任せられる（公式）**: 字幕の生成（米国英語）、話した語と映像の検索（米国英語）、ショットの切れ目の検出、物体のマスク・追跡、色の一致、縦横比の自動リフレーム、（iPad）曲に合わせたハイライトの自動選択
- **Vrew に任せられる（公式サイト）**: 日本語の字幕の自動生成、原稿からの字幕化、無音の検出と一括削除、翻訳字幕、AI 音声、テキスト・PDF からの動画生成
- **人に残る**: Vrew のサイトの利用者の声は「誤字脱字などはあります」「内容にそぐわない素材が使われていることがある」と書く（Vrew が載せた利用者の声で、測定ではない）。どこを切るかの判断（「読みながら編集」）は人がする設計

## 着手の仕方（未検証）

- **何が表現できるようになるか**: Vrew で日本語の話の収録から字幕付きの短縮版を作る。Final Cut Pro では英語の素材の字幕と、既存の動画のショット分割。効く型: talk（字幕付きの短縮版）、promo（切り抜き）
- **機械**: Vrew は galleria Windows か Mac（Ubuntu 版もあるが WSL の GUI では未確認）。Final Cut Pro は **Mac のみ**（Apple シリコン）
- **入れるもの・費用・アカウント**: Vrew は無料版から（**要: アカウントの可能性が高い。推測**）。料金・規約は公式ページを人がブラウザで読んで確かめる。Final Cut Pro は ¥50,000 の買い切りか Creator Studio（1 か月無料）。**どちらも費用・登録は西尾が決める**
- **成熟度**: Final Cut Pro は 2026 に 12.0→12.4 と 4 回更新。Vrew は 4.8.2
- **最小の手順（Vrew、GUI。サイトの機能名から。メニューの細部は推測）**:
  1. vrew.ai/ja から入れて起動 → 新規で動画ファイル（日本語、2〜3 分、公開してよい素材）を開き、音声分析の言語を日本語にする
  2. 字幕の文の一覧で、言い間違いの文を選んで削除（映像も切れることを確かめる）
  3. 「無音部分を短縮」を実行
  4. 字幕付きで動画を書き出し、字幕も SRT で書き出す（SRT の書き出しはサイトの利用者の声に出てくる。正確なメニュー名は未確認）
- **最小の手順（Final Cut Pro、Mac、GUI）**: 英語の素材をタイムラインに置き、Generate Captions（12.3）で字幕を作る／書き出し済みの動画を取り込み Edit Detection で分割する（メニューの位置はリリースノートに無く未確認）
- **動いたと言える確かめ方**: Vrew の手順 1 で日本語の字幕が文単位で並ぶ。手順 2・3 の後、書き出しの duration が短くなる（ffprobe）。SRT の時刻が書き出し動画の音声と合う（5 か所を目視）。字幕の誤りを 1 分あたりで数える。Final Cut Pro は Edit Detection の後のクリップ数が、ffmpeg の scene 検出の切れ目の数とおおむね一致するか
- **所要の見込み（推測）**: Vrew 30〜60 分、Final Cut Pro の試し 30 分

## Open Questions

- Vrew の利用規約の素材のライセンスと、生成物（AI 音声・テキストから動画）の権利の条文。ブラウザで読む必要がある
- Vrew の料金の公式の数字（2026-04 の統合クレジットへの変更の後）
- Vrew の音声分析がクラウドか端末か
- Final Cut Pro の Transcribe to Captions（11.0）が日本語で動くか。リリースノートは言語を書かず、12.3 の Generate Captions は米国英語だけと書く
- Apple が macOS 27 世代で Final Cut Pro に文字で編集する機能を足すか（2026-11 時点で発表は見つからなかった）
