---
type: source
summary: 放送のラウドネス規格 3 本の原文。EBU R 128（2023 版）は番組全体の統合ラウドネスを −23.0 LUFS、True Peak を −1 dBTP 以下に揃えよと書き、測り方は ITU-R BS.1770-5（K 特性＋400 ms ブロックの二段ゲート）に従う。米国の ATSC A/85:2013 は台詞を基準に −24 LKFS・−2 dBTP 未満を勧める
video_types: [any]
url: https://tech.ebu.ch/docs/r/r128.pdf
author: EBU（European Broadcasting Union）技術委員会 PLOUD／ITU-R（国際電気通信連合 無線通信部門）／ATSC（Advanced Television Systems Committee）
published: 2023-11（R 128 V5、BS.1770-5、Tech 3343 V4）／2020-08（R 128 s1 V3）／2013-03-12（A/85:2013、2021-02 の正誤表つき）
retrieved: 2026-11-09
sources:
  - https://tech.ebu.ch/docs/r/r128.pdf （EBU R 128-2023「Loudness normalisation and permitted maximum level of audio signals」。全文を読んだ）
  - https://tech.ebu.ch/docs/r/r128s1.pdf （EBU R 128 s1-2020「Loudness Parameters for Short-form Content (Adverts; Promos etc.)」。全文を読んだ）
  - https://tech.ebu.ch/docs/tech/tech3341.pdf （EBU Tech 3341「Loudness Metering: 'EBU Mode' metering」。時間窓の節を読んだ）
  - https://tech.ebu.ch/docs/tech/tech3343.pdf （EBU Tech 3343-2023「Guidelines for Production of Programmes in accordance with R 128」。46 ページのうち前景音・レベル設定の節を読んだ）
  - https://www.itu.int/dms_pubrec/itu-r/rec/bs/R-REC-BS.1770-5-202311-I!!PDF-E.pdf （ITU-R BS.1770-5 (11/2023)「Algorithms to measure audio programme loudness and true-peak audio level」。Annex 1 の算法の節を読んだ）
  - https://www.atsc.org/wp-content/uploads/2025/06/A85-2013-with-Corrigendum-No-1.pdf （ATSC A/85:2013「Techniques for Establishing and Maintaining Audio Loudness for Digital Television」。目標値・アンカーの節を読んだ）
  - https://www.sportsvideo.org/2026/07/16/atsc-releases-first-major-revision-to-a-85-audio-loudness-recommended-practice-since-2013/ （A/85 の 2026 年改訂の報道。改訂版本文は未読）
---

# EBU R 128・ITU-R BS.1770・ATSC A/85（放送のラウドネス規格）

## 何の文献か

- **EBU R 128**: 欧州放送連合の勧告（Recommendation）。2010 年初版、2023-11 の V5 を読んだ。放送局の技術者・機器メーカー・研究者の作業部会 PLOUD が書いた。補遺に s1（短尺: CM・番組宣伝）、s2（ストリーミング。[[web-aes-td1004-streaming-loudness]] で扱う）、s3（ラジオ）、s4（映画）がある。制作の実務指針が Tech 3343、メーターの仕様が Tech 3341
- **ITU-R BS.1770-5**: 国際電気通信連合の勧告。ラウドネスと True Peak の**測り方**（算法）だけを定める。R 128 も A/85 も Apple や Spotify も、測り方はこれを参照している
- **ATSC A/85:2013**: 米国のデジタルテレビの推奨実務（Recommended Practice）。FCC が CALM Act の規則に取り込んだ（2014 年の Federal Register による、と検索結果は書いている。規則本文は未読）。2026-07 に初の大改訂（A/85:2026）が出て、ストリーミング向けの付属書が加わったと Sports Video Group が報じている。**改訂版の数値は読んでいない**

いずれも放送（テレビ・ラジオ）の規格で、ネット動画にそのまま課されるものではない。

## 書いてあること

### 測り方（ITU-R BS.1770-5 Annex 1）

- 算法は 4 段だと書いている: 「"K" frequency weighting」→ チャンネルごとの二乗平均 → チャンネルの重み付き和（LFE は除く）→「gating of 400 ms blocks (overlapping by 75%)」。ゲートは 2 段で、「the first at −70 LKFS」「the second at −10 dB relative to the level measured after application of the first threshold」
- K 特性は 2 段のフィルタ（第 1 段が頭の音響効果を剛体球で近似したシェルビング、第 2 段がハイパス）
- 単位は LKFS（ITU）＝ LUFS（EBU）で同じもの（R 128 脚注 1）。1 LU は 1 dB の差
- True Peak は標本の間に立つ山を見るための測り方（BS.1770 の Annex 2。AES TD1004 は「at least 4x」のオーバーサンプリングと書いている）

### メーターの時間窓（EBU Tech 3341）

- Momentary（M）は 0.4 秒、Short-term（S）は 3 秒のスライド窓。Integrated（I）は上のゲート付きで番組全体

### EBU R 128（2023）の勧告

- 番組は**ピークではなくラウドネスで揃える**。理由として、ピーク正規化が番組間・チャンネル間の大きなラウドネス差を生み、それが「the most viewer/listener complaints」の原因だと書いている（considering a, b）
- 目標値: 「normalised to a Target Level of −23.0 LUFS」。生放送など実際に無理な場合のみ ±1.0 LU、QC の測定誤差として ±0.2 LU（h, i）
- 測るのは**番組の全体**で、「without emphasis on specific foreground elements such as speech, music or sound effects」（l）。つまり R 128 は台詞を基準にしない（A/85 と違う点）
- True Peak は制作時に「shall not exceed −1 dBTP」、配信系や低ビットレートの符号化ではさらに低い値がありうる（m）
- Loudness Range（LRA）は番組の大小の幅を見る補助の量。ただし「For programmes shorter than 1 minute, the use of the measure Loudness Range is not recommended」（脚注 2）

### 短尺（R 128 s1-2020。CM・番宣・ジングル）

- 「Short-form content」は「up to approximately 2 minutes, typically shorter than 30 seconds」と定義
- 統合ラウドネス −23.0 LUFS、**Short-term の最大 −18.0 LUFS（目標の +5 LU）**、True Peak −1 dBTP。LRA は「not applicable」（点が少なすぎるため）
- Short-term の上限を設けた理由は「overly dynamic short-form programmes, which would lead to audience complaints」を避けるため、と書いている

### 制作の実務（EBU Tech 3343-2023）

- レベル合わせの最初は、ナレーターの声のような「foreground signals」を Short-term（3 秒窓）で見るとよい。3 秒窓が語と語の間を埋めて読みやすい、と放送局の経験として書いている
- 前景音は −23 LUFS より「a bit lower」に置けと勧める。背景音が足されて統合値は上がるから。途中で上げるほうが下げるより楽だとも書く
- 「The most important elements of a mix for a uniform subjective loudness impression are so-called 'foreground sounds' — such as voice, title music or key sound effects」。ただし要素ごとの音量の釣り合いは「an artistic decision」で、ラウドネス計は聞こえ方を目で確かめる助けだ、という書き方。**声と BGM を何 LU 離せという数値は Tech 3343 の読んだ範囲には無い**（ダッキングの数値は [[web-torcoli-2019-background-ducking]]）
- 番組の大半が台詞で、統合ラウドネスと台詞のラウドネスの差が大きい（>5 LU）ときは、台詞などを「anchor signal」にした正規化を選べる、と書いている（§4.1）

### ATSC A/85:2013（米国）

- 番組の「Anchor Element」（多くは台詞）のラウドネスを「Dialog Level」として測る。台詞を分離できないときは全体を測る
- メタデータの取り決めが無いときの目標は「the Target Loudness value should be –24 LKFS」、True Peak は「below -2 dB TP」（§6・Annex の Key Idea）
- R 128 との違い: R 128 は全体を −23 LUFS、A/85 は台詞を基準に −24 LKFS、True Peak の上限も −1 と −2 で違う

## この wiki への含意

- **西尾の経験の値はどれも放送規格ではない**。[[exp-html-capture-pipeline]]・[[exp-democracy-river-video]] の英語版は最後に `loudnorm=I=-16:TP=-1.5:LRA=11` をかけている。−16 LUFS は R 128 の −23 より 7 LU、A/85 の −24 より 8 LU 大きい。どの配信向け推奨に当たるかは [[web-aes-td1004-streaming-loudness]] にまとめた
- True Peak −1.5 dBTP は R 128（−1 dBTP）より厳しく、A/85（−2 dBTP 未満）より緩い
- `LRA=11` について: R 128 は 1 分未満の番組で LRA を使うなと書き、s1 は短尺で LRA を「not applicable」としている。87 秒の英語版は「1 分以上・約 2 分以下」の境目にあり、LRA の目標値に意味があるかは微妙（ffmpeg の loudnorm での LRA の効き方は [[web-torcoli-2019-background-ducking]] の ffmpeg の節）
- **promo（短尺）の参考になるのは s1 の「Short-term 最大 +5 LU」**。統合値だけ揃えても、一瞬だけ大きい短尺は苦情になる、という放送側の経験が書かれている。[[exp-sutra-hype-editions]] のドロップ（無音＋暗転の直後に閃光と全楽器）は Short-term が跳ねる作りで、s1 の考え方で測るなら Short-term の最大と統合値の差を見ることになる
- **聞き比べで音量を揃えるとき**: [[exp-qualia-video]] は TTS の候補を「発話中 RMS を −22 dBFS に揃えて」聞き比べた。R 128 の前提（ピークで揃えると大きさの印象がずれる）と同じ向きの判断で、規格に沿うなら BS.1770 の統合ラウドネス（K 特性＋ゲート）で揃える方法もある。どちらが TTS の比較に向くかは確かめていない
- **型ごと**: talk（YouTube の解説）と promo（X・YouTube）はどれも配信先がネットで、放送規格の数値を直接使う場面は少ない。embed（講演の中で流す動画）は、会場の PA で声の大きさと並べて鳴るので、「番組ごとの大きさを揃える」という R 128 の考え方が一番近い（推論。会場で測った例は無い）

## Open Questions

- A/85:2026（2026-07 承認）のストリーミング向け付属書がどの目標値を書いているか。未読
- 1〜2 分の動画で LRA を見ること・loudnorm に LRA を指定することに意味があるか（R 128 は 1 分未満で非推奨、s1 は短尺で不適用）
- embed 用の動画を講演の会場で流すとき、どの統合値に揃えると話し手の声と釣り合うか。規格も経験も無い
- R 128 は台詞を基準にしない（全体を測る）、A/85 は台詞を基準にする。ナレーション主体の talk でどちらの考え方で揃えるべきか
