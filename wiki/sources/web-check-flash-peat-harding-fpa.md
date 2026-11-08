---
type: source
summary: 閃光の検査の道具のうち IRIS 以外。Trace Center の PEAT（無償、Windows、v1.6＝2017-02-15 版、AVI・1024×768・25/30fps の録画が前提、テレビ・映画・ゲームの商用作品への使用は禁止、更新は止まり後継の OSS は開発中）と、Cambridge Research Systems の Harding FPA（商用。Desktop は買い切り＋年間保守か年額、価格は非公開。オンラインの hardingtest.com は 1 本 £30 から、Ofcom / NAB / ITU-R BT.1702-3 で判定）。PEAT の解説は WCAG 2.0 の閾値（相対輝度 10%、暗い側 0.80 未満、341×256 の矩形の 1/4）を原文で載せていて、面積は ITU の「画面の 25%」より約 9 分の 1 小さい
video_types: [promo, any]
url: https://trace.umd.edu/peat/
author: Trace R&D Center（University of Maryland。PEAT の解析エンジンは Cambridge Research Systems）／Cambridge Research Systems Ltd（Harding FPA）
published: 2017-02-15（PEAT v1.6 の zip）／unknown（Harding FPA の各ページ）
retrieved: 2026-11-09
sources:
  - https://trace.umd.edu/peat/
  - https://trace.umd.edu/photosensitive-epilepsy-analysis-tool-peat-user-guide/
  - https://trace.umd.edu/open-source-photosensitive-epilepsy-analysis-tool/（TRACE の D2 プロジェクト）
  - https://www.hardingfpa.com/support/how-to-get-a-hardingfpa-system/
  - https://www.hardingfpa.com/hardingfpa-for-broadcast/broadcast-industry/harding-fpa-desktop
  - https://www.hardingfpa.com/
  - https://www.hardingtest.com/
  - https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html（定義の照合。本文は [[web-motion-wcag-2-2-motion-flash-vestibular]] で読んだもの）
---

# PEAT と Harding FPA（閃光の検査の道具、IRIS 以外）

## 何の文献か

- **PEAT**（Photosensitive Epilepsy Analysis Tool）: Trace R&D Center（もと Wisconsin 大学、今は Maryland 大学）が Web 制作者向けに無償で配る Windows のアプリの公式ページと利用者ガイド。解析エンジン（PSEe）は Cambridge Research Systems の著作物で、Harding 博士と組んで作った、と書く
- **Harding FPA**（Flash and Pattern Analyser）: Cambridge Research Systems（英国）の商用製品の公式ページと、オンライン検査サービス hardingtest.com のページ。製品の宣伝ページで、性能の主張（「No false failures」など）は売り手の主張
- **TRACE の D2**: PEAT の後継として、オープンソースの検査道具を作っている、という研究室のプロジェクト紹介
- その他、検索で見つかった OSS（読んだのは一覧の記述だけ）: epi-lens（ブラウザ拡張、JavaScript、PEAT の代替を名乗る）、lissy93/pax（閃光を消す、MIT）、EzraMarks/strobe-blocker（閃光を消す）、KaliPhobos/EpiScan（明るさの変化を見る）。どれも本体は読んでいない

## 書いてあること

### PEAT（2026-11-09 時点の公式ページ）

- 版: 「Free download: Version 1.6 release」、ファイルは `peat_2017-02-15.zip`。展開して `PEAT.exe` を起動する
- 動く OS: 「Windows Vista, Windows 7, Windows 10 (Firefox only), Windows XP (with some restrictions)」。Mac は Boot Camp で Windows を起動して、と書く。Windows 11 の記載は無い
- ページ自身の注意: 「This version is old in the tooth with regard to video formats.」。画面の録画機能は動かないことがあるので別の道具で撮る、新しい形式は読めないので **AVI に変換する**、と書く
- 録画の条件（利用者ガイド §9 Video Requirements）: 全画面で **1024×768**、**AVI**（非圧縮か、入っているコーデック）、**2GB 未満**、**25 か 30fps（30 推奨）**
- **使用の制限**（原文）: 「Use of PEAT to assess material commercially produced for television broadcast, film, home entertainment, or gaming industries is prohibited.」これらには Harding FPA を使え、と書く。また「It is NOT designed to analyze commercial videos or games」
- 判定（利用者ガイドの「How Seizure Risk is Determined」。WCAG 2.0 の文言をそのまま載せる）:
  - 合格: 1 秒に general flash 3 回以下かつ red flash 3 回以下、または「The combined area of flashes occurring concurrently occupies no more than a total of one quarter of any 341 x 256 pixel rectangle anywhere on the displayed screen area when the content is viewed at 1024 by 768 pixels」
  - general flash: 「a pair of opposing changes in relative luminance of 10% or more of the maximum relative luminance where the relative luminance of the darker image is below 0.80」
  - red flash の作業定義: 「for either or both states involved in each transition, R/(R+ G + B) >= 0.8, and the change in the value of (R-G-B)x320 is > 20 (negative values of (R-G-B)x320 are set to zero) for both transitions」
  - **Extended Flash Warning**（WCAG には無い）: 「any 5-second sequence of images that contain red or luminance flashing of at least one third of that required for ITC/Ofcom failure in at least 80% of the images」
- 結果の画面: 輝度の閃光（白の点線）と赤の閃光（赤の点線）の高さは「the brightness of the flash and the area of the screen that is flashing」で決まる。線が「fail」の領域に入ったら不合格。青の実線が extended flash warning
- 後継: 「We are working on a new fully-open-source version ... It will also be free to use. No ETA for it as yet.」（今の版は「open-source except for a proprietary analysis engine」）。D2 のページは、J. Bern Jordan 博士が作っていて「TRACE already has a PEAT tool but it's breaking in slow motion」と書く。公開の時期は書いていない

### Harding FPA（2026-11-09 時点の公式ページ）

- 「compliance with international guidelines on Flashing and Spatial Patterns in Broadcast Video, including Ofcom, ITU, NAB-J and ISO」（NAB-J は日本民間放送連盟と読める）。2001 年から放送局・ポストプロダクション・規制当局が使っている、と書く
- 手に入れ方（How to get a HardingFPA system）: 買う（sales@hardingfpa.com、電話）、**借りる**（HD-SDI のシステム、最短 1 週間）、**オンライン検査**（onlineflashtest.com / hardingtest.com、要登録）、QC の製品に組み込んだ提携先（Telestream Aurora、Venera）
- HardingFPA Desktop: 「Full perpetual licence with one time payment, and annual maintenance」か「Annual licence」。4K・8K・HDR は追加。「Current product version HardingFPA Desktop v6, containing Algorithm FPA v.3.5」「Available for 64-bit Windows and macOS」。**価格はページに無い**（問い合わせ）
- 宣伝の主張: 「Physiologically defined analysis engine detects only genuine violations」、失敗箇所を色の「heat map」とフレームごとの表で示す、無料のビューアで結果を共有できる。英国 DPP（納品の技術規格）の認定機器、と書く
- **hardingtest.com**（オンライン）: 「Online Test £30 Starting from」（自分でアップロード、平均 5 分）、「Manual Test £45 Starting from」（登録不要、落ちたら再検査無料、平均 10 分）。どちらも「Test using Ofcom / NAB / ITU-R BT.1702-3 Standards」。Netflix・BBC などのロゴを「Trusted By」に並べる（宣伝）

### 基準ごとの面積の違い（WCAG の Understanding と ITU-R BT.1702 を並べた計算）

| | 面積の条件 | 1920×1080 の全画面の動画に直すと（計算） |
|---|---|---|
| ITU-R BT.1702-3・Ofcom | 同時に光る面積が「表示画面の 25%」を超える | 約 518,400 画素 |
| WCAG 2.x・PEAT | 「10 度の視野」＝1024×768 のときの 341×256 の矩形の 25% | 341×256 は画面の約 1/9。その 1/4 は画面の約 2.8%。1920×1080 で約 57,600 画素（640×360 の 1/4） |
| IRIS の既定 | 画面の 25% の画素が「変わった」（[[web-check-flash-ea-iris]]） | 約 518,400 画素（ただし明るさは画面全体の平均で判定） |

WCAG の Understanding は「動画は全画面で評価せよ」と書く（[[web-motion-wcag-2-2-motion-flash-vestibular]]）。全画面の動画では、**WCAG の面積の条件は ITU より約 9 倍厳しい**（どこか 1/9 の窓の中の 25% で引っかかる）。これは机のモニタを近くで見る前提（10 度の視野）の違いから来ている、と読める（推測）。

## この wiki への含意

- **西尾の公開動画（YouTube・X）は「Web の動画」**なので、PEAT の使用の制限（テレビ・映画・ゲームの商用作品は禁止）には当たらないと読めるが、PEAT は 2017 年版で AVI・1024×768 しか読めず、Windows 11 の記載もない。galleria の Windows で動くかは分からない。**主の道具は IRIS（Python 版）、PEAT は使わない**のが現実的（推測）
- **Harding の判定が欲しいとき**は、hardingtest.com に 1 本 £30 からで出せる。ただし**動画を外部のサービスにアップロードする**ことになり、アカウント登録と支払いが要る（西尾が決めること）。放送・広告の納品の水準で「合格」と言いたい場合だけの手段
- 面積の基準が ITU と WCAG で 9 倍違うので、「どの基準で合格と言うか」を先に決める必要がある。アゲアゲ版のように全画面で光る演出は ITU でも引っかかりうるが、画面の一部（字の周り）だけが光る演出は、**ITU なら合格、WCAG なら不合格**、がありうる
- PEAT の extended flash warning（5 秒の窓の 80% で、失敗の 1/3 以上の強さの閃光）は、アゲアゲ版のように「拍に合わせた光が 3 分続く」動画に効く観点。IRIS にも extended failure がある（数え方は違う）
- promo で一番効く。embed（会場の大画面）は視野に占める割合が大きいので、WCAG の 10 度の考え方の方が近い（推測）

## Open Questions

- PEAT v1.6 が Windows 11 で動くか、MP4 を AVI に直せば読めるか（未検証。上の理由で優先度は低い）
- Harding FPA の判定の中身（窓・重み・面積の数え方）は公開されていない。IRIS や自前の近似との一致は、hardingtest.com に出さないと分からない
- TRACE の新しい OSS（D2）が公開されたか。2026-11-09 時点のページには時期が書かれていない
- epi-lens などの OSS の判定の中身・ライセンスは読んでいない
- WCAG の「10 度の視野」と ITU の「画面の 25%」のどちらを西尾の動画の基準にするか（スマホの縦長全画面、会場の大画面で答えが変わる）
