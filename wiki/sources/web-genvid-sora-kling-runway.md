---
type: source
summary: OpenAI（Sora）、Kuaishou（Kling）、Runway の 2026-11-09 時点の公式ページ。Sora はアプリが 2026-04-26、API が 2026-09-24 に終了し後継なし。Kling 4.0 は 1 回 30 秒・参照 15 個・キーフレーム 10 枚だが、無料会員は商用不可・Kling の表示が義務。Runway は自社モデル（Gen-4.5・Aleph 2.0）より他社モデルの窓口になっており、API は「入力に重ねた文字」「文字の生成を明示した指示」を失敗の主な原因に挙げる。最後に 5 社を同じ 4 項目で並べた表
video_types: [promo, any]
url: https://docs.dev.runwayml.com/guides/pricing/
author: OpenAI / Kuaishou（Kling AI）/ Runway
published: 2026（各節に記載）
retrieved: 2026-11-09
sources:
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/guides/video-generation
  - https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation（Internet Archive 2026-11-03 の写し）
  - https://bernama.com/en/press/news.php?id=2622471（Kuaishou のプレスリリース、2026-10-19）
  - https://app.klingai.com/global/docs/user-policy
  - https://app.klingai.com/global/docs/payment-policy
  - https://app.klingai.com/global/docs/ai-content-detection
  - https://docs.dev.runwayml.com/guides/pricing/
  - https://docs.dev.runwayml.com/guides/models/
  - https://docs.dev.runwayml.com/_llms-txt/core-api.txt
  - https://runwayml.com/research/introducing-runway-gen-4.5
  - https://runwayml.com/terms-of-use
  - https://runwayml.com/changelog
---

# Sora・Kling・Runway（2026-11-09 時点）と 5 社の並べ表

## 何の文献か

三社の公式ページ（API ドキュメント・廃止の告知・ヘルプ記事・プレスリリース・利用規約・changelog）。2026-11-09 に curl で取得し本文を読んだ。数値は以下すべて「2026-11-09 時点の公式ページによる」。

- OpenAI のヘルプ記事は直接は 403 で取れず、Internet Archive の 2026-11-03 の写しで読んだ
- **Kling の製品・API のページ（release notes、開発者ドキュメント、価格）は JavaScript で描く作りで、本文を取り出せなかった**。Kling 4.0 の仕様は Kuaishou のプレスリリース（Bernama 掲載）と、Kling 4.0 を売っている Runway Dev のページで読んだ。Kling の直販 API の価格は確かめられていない。規約のページ（Terms of Service・Paid Service・AI Content Detection）は本文が取れた

## 書いてあること

### OpenAI: Sora は終了した

- 廃止のページ（"2026-03-24: Sora 2 video generation models and Videos API"）:「2026-03-24 に、Videos API と Sora 2 の別名・スナップショットを **2026-09-24 に API から削除**すると通知した」。対象は Videos API、`sora-2`、`sora-2-pro` と各スナップショット。**推奨の置き換え先は「—」（なし）**
- 動画生成のガイド冒頭:「Sora 2 モデルと Videos API は 2026-09-24 に停止し、もう使えない。1 対 1 の代わりの API は無い。このガイドは記録として残す」
- ヘルプ記事 "What to know about the Sora discontinuation"（Internet Archive 2026-11-03 の写し）:「Sora の web とアプリは 2026-04-26 に、Sora API は 2026-09-24 に終了した」。sora.chatgpt.com/sunset から書き出せる。終了と書き出し期間の後、データは完全に削除する
- ChatGPT の中で動画を生成できるかについて、読んだページに記述は無い（公式の記述なし）

記録として残るガイドの内容（停止前の仕様。今は使えない）: `sora-2` と `sora-2-pro`、16 秒・20 秒まで、`input_reference` は最初のフレームを条件づける画像、人間でない「character」を短い動画から登録して使い回せた。ガードレールとして「実在の人物（公人を含む）は生成できない」「人の姿を含む character のアップロードは既定でブロック」「著作権のあるキャラクター・音楽は拒否」。

### Kuaishou: Kling 4.0

プレスリリース（2026-10-19、Kuaishou 名義、Bernama 掲載）:「Kling 4.0 は 10 月 15 日に正式公開」。改善点として「激しい動きと複雑なカメラワークで安定」「**1 回で最長 30 秒**」「Omni Reference: **参照素材 15 個まで、キーフレーム 10 枚まで**の組み合わせ」を挙げる。解像度・音声・文字については、このリリースに記述が無い。

Runway Dev のモデル一覧（Kling 4.0 を売っている側の公式の記述）:

- `kling_4`: 「720p か 1080p、3〜30 秒。文字・フレーム・画像や動画の参照から、または元の動画の編集」。Runway Dev への追加は 2026-10-23。「Kling 4.0 は音声を含み、音声を切る設定は無い」
- `kling_4_flash`: 「720p、3〜20 秒。文字・最初のフレーム・画像と動画の参照、元の動画の編集」。追加は 2026-11-05

Kling の文字の描画・実在人物の扱いについて、読めたページに記述は無い（公式の記述なし。Kling の製品ページ自体が読めていない）。

**規約**（Kling AI Terms of Service、"Last Updated Date: 2026/04/21"）:

- 4.4「利用者は入力・出力の知的財産権を持つ（または法に従った正当な権利者に属する）。我々はコンテンツの所有権を主張しない」
- 4.5「書面の許可なく生成物を使用・配布するときは、出力に Kling AI のブランドとロゴを表示しなければならない。表示が付かない場合は、生成物を使う場面（タイトルなど目立つ所）で "Kling AI" による生成だと明示する」
- 4.6「書面の許可なく、出力を商用目的で使用・複製・配布・改変してはならない」
- 4.7 Kling AI は、入力と出力を宣伝・機能改善・研究などに使う非独占・無償のライセンスを持つ

**有料サービスの規約**（Terms of Paid Service、会員特典の節）:「KLING AI の会員は出力の商用利用を制限されない（Kling AI と競合する製品・サービスの開発・提供を除く）」。会員特典に「透かしの除去」。7.2「非会員は、書面の許可がない限り、生成したすべてのコンテンツに Kling のブランドとロゴを付ける」。

**AI Content Detection** のページ:「生成した画像と動画に見えない透かしとメタデータを埋め込み、圧縮・編集・再共有を経ても追跡できる」「C2PA などの開かれた来歴の標準に沿う」。kling.ai/detection で誰でも判定できる。

### Runway: 自社モデルと、他社モデルの窓口

Runway Dev（API）のモデル一覧には 64 モデルがあり、自社の動画モデルは Gen-4.5・Aleph 2.0・Gen-4 Turbo（ほか Act-Two）。残りは Kling・Seedance・Gemini Omni・Veo・MiniMax・Wan・Grok Imagine などの他社モデル。changelog（runwayml.com/changelog）の 2026-08〜10 の項目も、他社モデルの追加・Adobe と DaVinci Resolve のプラグイン・MCP・広告の自動生成（Runway Ads、2026-10-27）が中心で、Gen-4.5 の後の自社の生成モデルの発表は見当たらない。

- **Gen-4.5**（`gen4.5`）: 発表 2025-12-01（研究ページ）、Runway Dev へ 2026-02-10。text-to-video と image-to-video、**2〜10 秒**。text-to-video は 1280:720 と 720:1280 だけ、image-to-video は 7 種の比。2026-08-20 から HDR・ProRes・PNG 連番・OpenEXR を直接出せる。音声生成について Runway の読んだページに記述は無い
- Gen-4.5 の研究ページの "Limitations":「因果の推論（原因より先に結果が起きる。取っ手を押す前に扉が開く）」「物体の永続性（隠れた後にカップが消える）」「成功への偏り（狙いの悪いキックでもゴールが決まる）」
- **Aleph 2.0**（`aleph2`）: 2026-06-02。**既存の動画を文章と、時刻に置いたキーフレーム画像（5 枚まで）で編集する** video-to-video。入力は 2〜30 秒・30 FPS 以下、解像度は入力のまま（1080p まで）。$0.28/秒（28 credits、最低 56 credits）
- **API の失敗の原因**（core-api の "INTERNAL.BAD_OUTPUT failures" 節）: よくある原因として「**入力の素材に入ったロゴ・透かし・重ねた文字**」「**文字の生成をはっきり求めるプロンプト**」「プロンプトを書いてくれという依頼」を挙げる。この失敗は直して再試行すれば通ることがある、と書く

**価格**（Runway Dev の価格ページ、1 credit = $0.01）: Gen-4.5 12 credits/秒（$0.12/秒）、Gen-4 Turbo 5、Aleph 2.0 28。他社モデルの Runway 経由の価格: Kling 4.0 は定価 720p 15.7・1080p 23.5 credits/秒（2026-11-30 まで 20% 引き。動画を入れると入力の秒数にも課金）、Kling 4.0 Flash 720p 9.4、Seedance 2.5 720p 30（＋入力・参照の動画 15/秒、最低 80）、Veo 3.1 音声あり 40・音声なし 20、Gemini Omni 1.2 Flash 720p 7（＋参照画像 1 枚 1 credit）。

**規約**（Runway Terms of Use、"Last updated October 23, 2026"）4.4:「入力と出力の所有権を主張しない。規約を守る限り、出力の商用利用を制限しない」。ただし「入力と出力は Runway の AI モデルの学習・改善に使われうる」として、Runway に非独占・取消不能・永久・無償・再許諾可能なライセンスを与える。C2PA・透かしについて、読んだ Runway のページに記述は無い（公式の記述なし）。

## 5 社を同じ項目で並べる（2026-11-09 時点の公式ページによる）

価格は API の 720p・音声あり・動画入力なしの秒単価。Google と ByteDance の詳細は [[web-genvid-gemini-omni-veo]]、[[web-genvid-seedance]]。

| | Google: Gemini Omni 1.2 Flash | Google: Veo 3.1（Vertex） | ByteDance: Seedance 2.5（ModelArk） | Kuaishou: Kling 4.0 | Runway: Gen-4.5 / Aleph 2.0 | OpenAI: Sora 2 |
|---|---|---|---|---|---|---|
| 提供 | GA（2026-11-05） | GA（2025-11-17）、従量課金なし | 提供中 | 公開（2026-10-15） | 提供中 | **終了**（API 2026-09-24） |
| 1 回の最長 / 延長 | 15 秒 / 延長で 30 秒 | 8 秒 / 延長あり（上限は読んだページに記述なし） | 30 秒 / 2 回延長（Seed のページ） | 30 秒 | Gen-4.5 は 10 秒 / Aleph は入力 30 秒まで | — |
| 解像度 | 360p〜4K（1080p 以上は upscale） | 720p・1080p・4K | 480p〜1080p | 720p・1080p（Runway Dev の記述） | 720p 級（Gen-4.5） | — |
| 音声の同時生成 | あり | あり | あり（日本語を含む 11 言語） | あり（切れない。Runway Dev の記述） | 記述なし | — |
| **(1) 画面の文字** | 「正しく読める形で描く」と主張（測定なし、英語以外は未評価） | 記述なし | 綴りを誤ると公式が明記。正しい文字を画像で渡すよう勧める。字幕を禁じても出る | 記述なし | 入力の重ねた文字・文字の生成の指示が失敗の主な原因（API） | — |
| **(2) 実在の素材を入れる** | 参照画像 6、参照動画 3（各 3 秒）、両端、自分の動画の編集 15 秒まで（EEA・英・スイス除く） | 両端、参照画像、動画入力なし | 参照 50（画像 30・動画 10・音声 10）、両端、動画の編集・延長 | 参照 15、キーフレーム 10、動画の編集（Runway Dev） | Aleph 2.0 で既存動画を編集（キーフレーム 5） | — |
| 実在の人（顔） | 認識できる人物の画像は不可 | 記述を読んでいない | 直接は不可。本人確認・許諾済みの資産登録で可 | 記述なし | 記述なし | 生成不可だった |
| **(3) 価格**（720p 音声あり） | 約 $0.07/秒 | $0.40/秒（Fast $0.10、Lite $0.05） | 約 $0.23/秒（480p Draft 約 $0.10） | 直販は未確認。Runway 経由 $0.157/秒（定価） | Gen-4.5 $0.12/秒（音声の記述なし）、Aleph $0.28/秒 | — |
| **(4) 生成物の権利** | 所有権を主張しない | （Google Cloud の規約は未読） | API の規約は未読。Dreamina は「一般に非商用」、出力は利用者のものだが他の利用者にもライセンス | 権利は利用者。**非会員は商用不可・Kling の表示義務**、会員は商用可 | 所有権を主張しない、商用を制限しない、学習に使われうる | — |
| 開示・透かし | SynthID を必ず入れる | C2PA 対応 | API は見える透かしを任意（既定オフ）。Dreamina は見える透かし＋見えない透かし＋来歴メタデータ | 見えない透かし＋メタデータ（C2PA に沿う）、非会員は見える透かし | 記述なし | — |

## この wiki への含意

問い:「作品（ソフトウェア・研究・本・動画）の promo を作る最良の方法は何か」の中で、丸ごと生成がどこまで使えるか。

- **Sora は選択肢から外れた**。ネットの比較記事・2025 年の事例（Sora を使った作例など）を読むときは、2026-11 時点で使えないことを前提にする
- **Kling は規約が promo に効く**。無料会員のまま作った出力を作品の宣伝に使うのは「商用」に当たりうるので、会員になるか書面の許可が要る。非会員は Kling の表示も義務。他社は表示を利用者に義務づける文言が無い（Google は SynthID、ByteDance の API は透かしが任意）
- **Runway は「生成モデル」より「作業場」**になっている。自社の Gen-4.5 は 10 秒・720p 級で、他社の新しいモデル（Kling 4.0・Seedance 2.5・Omni）より短い。一方で Aleph 2.0 は**既存の動画を編集する**モデルで、作品の画面録画や実機の撮影を入れて加工するという、promo で一番要る入れ口を持つ。ただし Runway の API は「入力に重ねた文字」を失敗の原因に挙げているので、文字の多い画面録画を入れると失敗しやすいと読める（未検証）
- **画面の文字について、5 社の公式の書き方が揃っていない**: Google は「正しく描ける」、ByteDance は「誤る、正しい文字は画像で渡せ」、Runway は「文字を入れると失敗しやすい」、Kling は記述なし。どの社も測定値を出していない。西尾の経験の規則「生成モデルに文字を描かせず、字幕・ロゴは後から合成する」（[[experience-lessons-2026-11]]、[[exp-local-scene-studio]]）は、ByteDance と Runway の公式の記述とは合い、Google の主張とは食い違う
- **作品の中身（画面・数値・UI）を見せる部分は、生成に任せない方が公式の記述とも合う**。西尾の promo の経験は、canvas に描いて headless Chrome で撮る決定論的な組み立て（[[exp-html-capture-pipeline]]、[[exp-polis-magi-op]]）と、証拠写真を集める版（[[exp-nishio-showreel]]）で、どちらも中身の正確さを組み立ての側で持っていた。丸ごと生成を入れる余地は、中身を見せない「雰囲気のカット」（背景・つなぎ・人物の演技）か、実在の画面を最初・最後のフレームに固定する使い方で、後者は [[exp-galleria-local-video-generation]] の FLF2V の実測（終点は VAE 往復の床まで再現、間はモデルが発明する）がそのまま当てはまると考えられる（各社のホスト型では未測定）
- **費用は障壁ではない**: 15 秒を 1 案作る費用は、Omni で約 $1、Seedance 2.5 の 720p で約 $3.5、Veo 3.1 で $6。何案も作って捨てられる。障壁は規約（Kling の非会員、Dreamina の非商用）と、中身の正確さ

[[exp-galleria-local-video-generation]] の「外部の hosted モデル（Kling 3.0 約 $0.029/s、Seedance 1.5 Pro $0.0247/s〜、Veo 3.1 は 48kHz の同期音声と台詞）」は二次情報の数字で、2026-11 時点の公式の数字（上の表）とは桁が違うものがある。Kling 3.0 は Runway 経由で 720p 音声あり 13 credits = $0.13/秒（Standard）。Seedance 1.5 Pro は 2026-11-11 に退役、Veo 3.1 は Gemini API での Preview が停止した。

## Open Questions

- Kling の直販 API の価格と、Kling 4.0 の文字の描画・実在人物の扱い（公式ページが JavaScript 描画で読めなかった）
- Runway の Aleph 2.0 で画面録画を編集したとき、文字・UI がどこまで保たれるか。公式の記述は「入力の文字は失敗の原因」だけ
- Runway の Gen-4.5 が音声を出すか（読んだ Runway のページに記述なし）
- Google Cloud（Vertex）の Veo の規約、ByteDance の ModelArk の規約は未読。表の「生成物の権利」の列は消費者向け・Gemini API の規約で埋めた所がある
- どの社も「画面の文字を正確に出せるか」を測った数字を出していない。比べるなら自分で測るしかない
