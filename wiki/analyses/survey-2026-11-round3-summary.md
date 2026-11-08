---
type: analysis
summary: 第 3 回のネット上の知見のサーベイ（2026-11-09、web- 83 ページ）のまとめ。西尾の目的「作るための手段を調査サーベイし、今後の表現手段を増やすこと」と指示「明日からすぐ具体的に着手が可能な水準で」に沿って、第 1・2 回で薄かった「どの手段で、どの機械で、何を入れて、どう始めるか」を埋めた。足りない領域の判断、分かったこと、経験と文献の食い違い、読めなかったもの。主な出力は ready-to-start-2026-11-10
video_types: [promo, talk, embed]
sources:
  - web-means-*.md（48 ページ）
  - web-check-*.md（18 ページ）
  - web-embed-*.md、web-nonscreen-*.md（9 ページ）
  - web-rights-*.md（8 ページ）
  - exp-*.md
---

# 第 3 回サーベイのまとめ（2026-11-09）

西尾の目的: 「作るための手段を調査サーベイし、今後の表現手段を増やすこと」。指示: 「それを踏まえてサーベイの足りない領域にしっかりサーベイをかけて。明日からすぐ具体的に着手が可能な水準で。」途中で追加の言葉「最終的に「動画の作り方の解説動画」を作るか」（[[origin-2026-11-09]]。成果物の候補で、未決定）。

- 10 の担当で 83 ページ: 手段 48、検査 18、embed と画面の無い作品 9、権利と開示 8。
- 横断の整理は [[expression-means]]（表現手段）と [[checks-and-finishing]]（検査と仕上げ）。
- **主な出力は [[ready-to-start-2026-11-10]]**（明日から着手できること 11 項目と、解説動画の案）。
- 第 1 回は [[survey-2026-11-summary]]、第 2 回は [[survey-2026-11-round2-summary]]。

**決まり**: CyEC2 では何も入れず、何も動かしていない（西尾の決定）。手順はすべて**未検証（galleria で確かめる）**で、確かめ方を添えた。アカウント・課金・API キーの取得はしていない。

## 着手前の「既にあるもの／足りないもの」

wiki を読んで作った表（Mac 側の候補を元に直したもの）。

| 候補 | 既にあるもの | 足りないもの | 担当 |
|---|---|---|---|
| a 実物の収録 | VHS・shot-scraper（web-promo2-vhs-shot-scraper-demos-as-code）、howseen の Playwright 撮影の注意、THINKLET の Premiere 手編集 | Playwright の録画 API、OBS（galleria Windows）、自動ズームの画面収録アプリ、実機・カメラ撮影の最小構成 | means-capture |
| a 図・データ | Tufte・Bateman（原則のみ） | Excalidraw・tldraw・Mermaid・D2 の段階描画、D3・Observable・Flourish のアニメーション | means-diagram |
| a 2D/3D | AE/Lottie/Rive（web-after-effects-lottie-rive）、three.js は流行の作品の道具として名前だけ | GSAP のライセンス（2025 の無償化）、SVG、three.js を render(t) で撮る手順、Blender Python・Grease Pencil、Theatre.js | means-3d |
| a 人物・声 | 経験: SAPI・AivisSpeech・VOICEVOX・Irodori-TTS・MiniMax H3・Live2D・PuppetLoom。voice principle の研究 | Style-Bert-VITS2 ほか公開 TTS と商用日本語 TTS の比較、自分の声の複製、口の同期の公開モデル、アバター。読み辞書の運用 | means-voice |
| a 音・文字 | ラウドネス規格、Moreno & Mayer。経験: numpy 合成 BGM、Suno 等は外部頼みという galleria の 2026-09 調査 | BGM・効果音の生成モデル（公開・商用）と素材集の利用条件、日本語フォントの利用条件 | means-sound-font |
| a 批評役のモデル | round 2「モデルは聞けない・通しで見られない」、howseen の新しいエージェントにコマを見せる、TheoremExplainAgent の VLM と人間の差 | 動画・音声を入力できるモデル（API・公開）と、評価の一致の実測 | means-critic |
| b 閃光 | ITU-R BT.1702・NHK 基準・WCAG（PEAT・Harding は名前だけ、未読） | IRIS・PEAT などの入手と使い方、判定の根拠、R3 を回す手順 | check-flash-subs |
| b 字幕 | Netflix ja・BBC の規則、経験: 内容と時間の正本の分離、Whisper API（OpenAI） | 日本語の強制アライメント（WhisperX 等、ローカル）、BudouX、SRT/ASS の焼き込み、配信先の字幕ファイル | check-flash-subs |
| b ラウドネス・色・コンタクトシート・仕様表 | loudnorm の注意（1 パスだと dynamic）、X 40fps、Shorts 3 分、Apple 30fps | loudnorm 2 パスの手順、色・コントラストの機械検査、コンタクトシートのコマンド、出す場所ごとの仕様の 1 表（スライド埋め込みを含む） | check-spec |
| c embed | 外に例が無い（round 2）、THINKLET、Claude Motion の用途例 | 話し手が黙って流す映像の作法（基調講演の製品映像、展示・美術館のループ、学会発表の中の動画） | embed-nonscreen |
| c 画面の無い作品の promo | 本のトレーラー（Schafer）、UIST・CHI の video preview | video abstract（論文の動画要約）の研究と実例、考え方の紹介の実例 | embed-nonscreen |
| c 日本語固有 | Netflix ja 4 字/秒、日本語の字幕の速さの研究は見つからず | 日本語ナレーションの速さ（モーラ／秒）、字幕の速さの研究（再探索）、TTS の読み辞書の運用 | check-flash-subs（速さ）・means-voice（辞書） |
| d 権利と開示 | Apple 2.3.4、Seedance・Veo の透かし・C2PA の記述、JASRAC は作曲だけで原盤は別（経験） | 各配信先の AI 生成の開示規則、C2PA の付け方、既存曲・PD 曲と録音、様式を借りること、素材の利用条件の確かめ方 | rights |

Mac 側の候補からの直し:
- VHS・shot-scraper・Lottie/Rive・AE は、既にページがある。新しいページは書かず、差分（版・手順）を既存ページの Updates に入れた。
- 「日本語の字幕の速さ」は、第 2 回で研究が見つかっていなかったので、再探索は短くし、ナレーションのモーラ／秒を主にした。結果として研究が 1 本見つかった。
- 出す場所の仕様の 1 表は量が多いので、検査と別の担当にした。

## 分かったこと

### 表現手段（[[expression-means]]）

1. **台本どおりに実物を撮る道具が揃った**。Playwright の screencast が、カーソル・クリック点・章見出しを組み込みで描くようになった（2026）。ブラウザの外は、OBS を WebSocket で操作して撮る。自動ズームのアプリは OS の入力で寄る位置を決めるので、台本で撮るなら寄る位置は台本の側から渡す（[[web-means-capture-playwright-screencast]]、[[web-means-capture-obs-studio]]）。
2. **西尾の方式（canvas の `toDataURL`）に載るかは、時刻の持ち方と描画の層で決まる**。
   - SVG・DOM の道具（Mermaid、D2、Excalidraw、GSAP）は `page.screenshot` が要る。
   - 遷移を持たない道具（Plot、Vega-Lite）、d3 の interpolate、GSAP の paused timeline は、フレーム番号の純関数にできる（[[web-means-diagram-mermaid]]、[[web-means-3d-gsap-svg-seek]]）。
3. **手元で商用に使える楽曲の生成モデルがある**（ACE-Step 1.5、MIT）。商用サービスは、無料プランを動画に使えない（[[web-means-sound-ace-step-yue2-diffrhythm]]、[[web-means-sound-suno-udio-elevenlabs-music-terms]]）。
4. **利用条件は名義と売上で変わる**。どの名義で出すかが、多くの道具の可否を決める。
   - Fish は年商 50 万ドルまで商用可。
   - Live2D は売上 1,000 万円が境。
   - ElevenLabs の Free〜Pro は個人の利用に限る。
   - Cap は、雇い主の製品のデモも「商用」に入る。
   - mojimo は本人のチャンネルだけ。
5. **読みの直し方はエンジンで違う**。台本にアクセントまで書けるのは Google の yomigana だけ。AivisSpeech はモーラの pitch と長さを無視する（[[web-means-voice-voicevox-aivisspeech-user-dictionary]]）。
6. **通しで見て聞ける批評役は、Gemini と Qwen-Omni の API だけ**。ただし、点数の批評は人と合わない（点の完全一致 26〜29%）。同期・停止・動きは拾えない。効くのは「1 回に 1 種類の誤りを時刻付きで」聞くこと（[[web-means-critic-videoscore]]、[[web-means-critic-video-bench-spotlight]]、[[web-means-critic-omni-judge-audiojudge]]）。

### 検査と仕上げ（[[checks-and-finishing]]）

1. **閃光は、IRIS と自前の画素ごとの近似を並べて読む**。IRIS は画面全体の平均で判定するので、画面の一部の閃光を見逃しうる（ソースを読んだ解釈）。全画面の動画では、WCAG の面積の基準が ITU より約 9 倍厳しい（[[web-check-flash-ea-iris]]、[[web-check-flash-peat-harding-fpa]]）。
2. **字幕は、台本を正にして、整列の道具には時刻だけ出させる**（stable-ts の align、Qwen3-ForcedAligner）。改行は BudouX、焼き込みは ASS の WrapStyle 2（[[web-check-subs-whisperx-stable-ts-faster-whisper]]、[[web-check-subs-budoux]]）。
3. **日本語の字幕の速さの研究が見つかった**: 1 秒 6 字まで視線の負荷が変わらず、8 字で増えた（豊倉・山田 2017、視線 5 人）。話す速さの目安は 5〜8 モーラ／秒（[[web-check-ja-toyokura-yamada-2017-subtitle-4-chars]]、[[web-check-ja-speech-rate-mora]]）。
4. **loudnorm は 2 パスにしても、条件を満たさないと線形にならない**。経験の設定は 1 パスで、dynamic で動いている（[[web-check-loudness-ffmpeg-loudnorm-ebur128]]）。
5. **出す場所の仕様は、公式のヘルプと API で食い違う**（X の 40fps と 60fps）。Instagram・TikTok の利用者向けヘルプは本文が取れなかった（[[checks-and-finishing]] の表）。

### 型ごとの穴

1. **embed（流しっぱなし）の外の実例は、学会の Fast Forward**。話し手が上に乗る版は録音したナレーションを禁止し、単独で流れる版はナレーションを必須にしている。声の分担は「流す前に、何が映るかを一言」（[[web-embed-siggraph-ieeevis-chi-fast-forward]]、[[web-embed-ladner-sigaccess-chi-video-in-talks]]）。
2. 展示の映像は、上映時間の半分未満しか見られない。どこから見ても分かる作りが要る（[[web-embed-serrell-smithsonian-museum-video]]）。
3. **画面の無い作品の promo（video abstract）**: 閲覧には少し効くが、引用への効果は割れている。理解を上げたのは主に台本の平易さ（[[web-nonscreen-zong-bonnevie-bredbenner-video-abstract-studies]]）。一番近い型は Cell の Figure360（[[web-nonscreen-cell-iop-nejm-video-abstract-guides]]）。

### 権利と開示

1. **AI の声（TTS）の扱いは、配信先で逆**。TikTok は汎用の TTS を開示不要と明記し、Meta はリアルな AI の声のリールを要ラベルの例に挙げる。コードで描くモーションを名指しした規則は無い（[[web-rights-tiktok-meta-aigc-labels]]、[[web-rights-youtube-genai-disclosure]]）。
2. YouTube は C2PA を含む動画に、作り手が外せない AI ラベルを付ける（[[web-rights-c2pa-c2patool-content-credentials]]）。
3. 包括契約は作詞・作曲の利用だけ。原盤・替え歌・広告目的は外。X は UGC の一覧に無い（[[web-rights-jasrac-nextone-ugc-music]]）。
4. 作風はアイデアで保護されないが、特定の作品の創作的表現が直接感じ取れれば侵害になりうる（文化庁 2024、[[web-rights-bunkacho-ai-copyright-style]]）。
5. 着手前に西尾が決めることの一覧は、[[ready-to-start-2026-11-10]] の「権利と開示」。

## 経験と文献の食い違い

| 経験 | 文献 | 扱い |
|---|---|---|
| 般若心経アゲアゲ版のレビューを R1 だけで回した（[[exp-sutra-hype-editions]]） | 閃光は BPM で決まる（[[web-check-flash-ea-iris]]） | R3 を測る（[[ready-to-start-2026-11-10]] の 1） |
| `loudnorm=I=-16:TP=-1.5:LRA=11`（[[exp-html-capture-pipeline]]） | 作者のブログの 1 パスの例と同じで、dynamic で動く | 2 パスに置き換える（同 5） |
| 「楽曲は実用的なローカルモデルが無い」（[[exp-galleria-tts-and-singing]]、2026-09-04） | ACE-Step 1.5（2026-02、MIT） | 経験の側が古い。exp 側に Updates |
| 「Suno は有料でも自らを author と称する」（同） | 2026-09-03 版の規約に当たる条文が無い | 古い版を読んだ可能性。両方残す |
| 「包括契約は作曲の権利だけ」（[[exp-forest-misc-video-notes]]、[[exp-polis-magi-op]]） | 公式は「作詞・作曲」 | 書き方の違い。原盤は別、は一致 |
| マティス-EB を使った（[[exp-polis-magi-op]]） | mojimo は個人契約・本人のチャンネルだけ | 会社の発信物に使えない。OFL の 900 の明朝で置き換えられる |
| 英語版の `gpt-4o-mini-tts`（[[exp-democracy-river-video]]） | 2027-01-06 に終了 | 作り直すときは API から変わる |
| THINKLET はナレーション入りで流しっぱなし（[[exp-thinklet-reading-demo-video]]） | VIS 2015: 話し手が上に乗るなら録音ナレーションは禁止 | 話し手が黙っていたなら矛盾しない（未確認） |
| talk は完全静止を既定（[[exp-qualia-video]]） | Figure360「2 秒以上画面が変わらない間を作らない」 | 単独の動画と、話し手が隣にいる動画の違い。両方残す |
| 「1 分 300 字」（[[exp-lt-20260909]]） | 一次資料は見つからず。研究はモーラ／秒 | 換算は漢字の割合で変わる |
| 収録アプリの「読み込みを詰めろ」（cap-demo） | THINKLET は待ちを説明に変えた | 待ちを偽ることと紙一重。両方残す |
| 機械の QA は視聴品質を保証しない（[[exp-qualia-video]]） | 批評役の研究（VideoScore・Omni-Judge・Paper2Video） | 一致 |

## 次に調べること・すること

1. [[ready-to-start-2026-11-10]] の 1〜11 を galleria で回し、各ページの「着手の仕方」に実測を Updates で足す。手順が通らなければ、そこを直す。
2. 解説動画（候補）の型・相手・尺・出す場所・声を、西尾が決める。
3. 日本語の画面文字・日本語の音声での、批評役の精度（研究が見つからなかった）。
4. NHK のアナウンサーの話す速さの一次資料。
5. 会場での上映（embed）での音楽の利用の扱い（UGC の包括契約とは別の利用。読んでいない）。

## 読めなかったもの

- **JavaScript の描画・ボット対策で止まったもの**（回避していない）:
  - Instagram・TikTok・LinkedIn の利用者向けヘルプ
  - Flourish のヘルプ、observablehq.com
  - stableaudio.com の規約
  - COEIROINK の API の仕様
  - Azure の単価
  - TikTok の AIGC ラベルの手順
  - Pixabay・Unsplash の規約
  - ニコニコの規約の本体
  - Adobe Premiere の C2PA のヘルプ
- **Internet Archive の版で読んだもの**: X のヘルプ、Pixabay の規約、Cell のガイド、Spicer の PDF、判決 2 件。
- **ログインが要るもの**: YouTube オーディオライブラリの外部利用の条文、Suno のダウンロード数。
- **有料・未公開のもの**:
  - 有料の本文: Anderson の HBR 2013、Zong・Copiello・Bonnevie、Machado 2009。
  - 非公開: Harding FPA の判定手順。
  - 未読の規格: ISO 9241-391。
- **見つからなかったもの**: NHK の話す速さの一次資料、日本語での批評役の精度の研究、見本市のループ映像の一次資料。
- **GitHub API の上限**: 一部のリリース日は、HTML のリリースページ・PyPI・commit の atom から取った。

## Open Questions

- 名義（個人か会社か）が決まらないと、多くの道具の可否が決まらない。西尾の発信物の名義を、作品ごとに決めるのか、一律にするのか。
- 「動画の作り方の解説動画」を作るなら、その動画が自分の説明する手段で作られている（自己言及の）並べ方が、「主役を決めて尺を割く」（[[exp-gyazo-resumption-video]]）とどう両立するか。案は [[ready-to-start-2026-11-10]] の最後の節。
