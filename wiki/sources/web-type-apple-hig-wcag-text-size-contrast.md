---
type: source
summary: 画面の文字の大きさとコントラストの公式の基準。Apple HIG は iPhone の文字を既定 17pt・最小 11pt とし細い字は大きく、WCAG 2.2 の 1.4.3 は文字と背景のコントラストを 4.5:1（大きい文字は 3:1）以上とする。ただし動画の中の文字に 1.4.3 が当たるかは W3C の作業部会の 2017 年の議論でも割れていて、焼き込み字幕に当てると黒い帯で映像を隠すことになる、という反論がある
video_types: [any]
url: https://developer.apple.com/design/human-interface-guidelines/typography
author: Apple（Human Interface Guidelines）／ W3C（WCAG 2.2 Understanding、WAI GL 作業部会のメーリングリスト）
published: 2025-12-16
retrieved: 2026-11-09
sources:
  - https://developer.apple.com/design/human-interface-guidelines/typography （Apple HIG "Typography"。変更履歴の最新 2025-12-16。本文は developer.apple.com の JSON 版から読んだ）
  - https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html （Understanding SC 1.4.3 Contrast (Minimum)）
  - https://lists.w3.org/Archives/Public/w3c-wai-gl/2017JanMar/0644.html （W3C WAI GL のスレッド "does anyone currently fail colour contrast for text in timed media"、2017-02。0692・0704・0712・0715 も読んだ）
---

# 画面の文字の大きさとコントラスト: Apple HIG と WCAG 1.4.3

## 何の文献か

- **Apple Human Interface Guidelines「Typography」**: Apple のアプリ設計の公式指針。アプリの UI の文字の話で、動画の文字の話ではない。2026-11-09 時点の公式ページによる（変更履歴の最新は 2025-12-16）
- **WCAG 2.2 Understanding 1.4.3「Contrast (Minimum)」**: W3C のウェブアクセシビリティ基準の解説文書。達成基準そのものと、その根拠の説明
- **W3C WAI GL 作業部会のメーリングリスト（2017-02）**: 「動画の中の文字のコントラストで不合格にしている人はいるか」というスレッド。作業部会の参加者の意見で、W3C の公式の解釈ではない
- 動画の焼き込みの文字の最小サイズを書いた一次資料（プラットフォーム・放送）は、BBC の字幕ガイド（[[web-type-bbc-subtitle-guidelines]]）以外に今回見つけられなかった。そこで UI の文字の基準を、動画に換算する材料として読む

## 書いてあること

### Apple HIG（Ensuring legibility）

- 「Follow the recommended default and minimum text sizes for each platform — for both custom and system fonts — to ensure your text is legible on all devices.」
- 表:

| プラットフォーム | 既定 | 最小 |
|---|---|---|
| iOS, iPadOS | 17 pt | 11 pt |
| macOS | 13 pt | 10 pt |
| tvOS | 29 pt | 23 pt |
| visionOS | 17 pt | 12 pt |
| watchOS | 16 pt | 12 pt |

- 「Keep in mind that font weight can also impact how easy text is to read. If you use a custom font with a thin weight, aim for larger than the recommended sizes to increase legibility.」
- 読みにくければ、大きくする、文字や背景の色でコントラストを上げる、読みやすさを考えた書体（システムフォント）を使う。「Increasing text size and adding visible background shapes can help make text easier to read.」（ゲームの文字の例）
- visionOS の節: 背景の無い文字は太字にする。影でコントラストを足すのは避ける（背景の面が無いため）
- 立体の文字より 2D の文字を。「The more visual depth text characters have, the more difficult they can be to read.」

### WCAG 2.2 SC 1.4.3

- 「The visual presentation of text and images of text has a contrast ratio of at least 4.5:1」。大きい文字（18pt 以上、太字なら 14pt 以上）は 3:1。飾りの文字・写真に偶然写った文字・ロゴは除く
- 4.5:1 の根拠: 3:1 は ISO 9241-3・ANSI の通常の視力向けの最小。視力 20/40（80 歳前後の典型と書く）で生じるコントラスト感度の低下（約 1.5 倍）を補って 3 × 1.5 = 4.5
- 大きい文字の定義には「or font size that would yield equivalent size for Chinese, Japanese and Korean (CJK) fonts」とあり、CJK は各言語の大活字の基準に相当する大きさ、と書く（具体の pt は書いていない）
- 細い書体はアンチエイリアスで実際より薄く描かれ、数値上は通っても実際のコントラストが低くなることがある。線の太い書体を選ぶか、余裕のある色の組み合わせを、と勧める（規範ではない）
- 文字の縁取り: 細い縁は文字の一部、文字の内側まで埋めるような太い縁は「halo」で背景の一部として計算する
- 失敗例 F83: 「using background images that do not provide sufficient contrast with foreground text」
- Understanding の本文は、動画（時間で変わる背景）の中の文字には触れていない

### W3C の作業部会の議論（2017-02、意見の対立）

- David MacDonald: 動画の文字を 1.4.3 で不合格にしてこなかった理由として、Understanding は「pixels」と静止画像に限っていて動画や映画の文字に触れていない、1.4.3 を作ったときに動画の文字のコントラストの議論をした覚えがない、と書く（0644）
- Detlev Fischer: 字幕は明らかに文字で、画面の切り出しで不合格を示せる。監査では「white caption text on transparent grey background」をよく見るが、背景の映像が明るいとコントラストは 4.5:1 を大きく下回る、と書く（0692）
- Gregg Vanderheiden: 焼き込み（open）の字幕にコントラストを義務づけると、背景を制御する方法が他に無いので、字幕の後ろに色の塊を置いて映像を隠す字幕しか許されなくなる。それは多くの人が好む字幕ではない。closed の字幕は再生側が描くので作り手の管理の外、と書く（0704）。「How do you control the color of the captions when the background image is changing frame by frame?」（0712）
- スレッドの中で結論は出ていない（読んだ範囲）

## この wiki への含意

型に依らない（any）。スマホで見る promo と、会場で流す embed の両方に効く。

### 文字の大きさ（Apple の最小をスマホで見る動画に換算する。このページの計算）

前提: iPhone の画面幅を 393pt（iPhone 15・16 の標準サイズの縦持ち）とし、動画が画面の幅いっぱいに表示されるとする。X のタイムラインは左右に余白があるので、実際はこれより小さく表示される。

| 動画 | 縦持ちで幅いっぱい | 11pt（最小）に当たる文字の大きさ | 17pt（既定） |
|---|---|---|---|
| 1920×1080（16:9）を横のまま縦持ちで見る | 1920px → 393pt（約 4.9px/pt） | 約 54px | 約 83px |
| 1080×1350（4:5） | 1080px → 393pt（約 2.75px/pt） | 約 30px | 約 47px |
| 1080×1920（9:16） | 1080px → 393pt（約 2.75px/pt） | 約 30px | 約 47px |

- 16:9 の動画をスマホの縦持ちのフィードで見ると、文字は動画の中で大きく作る必要がある。1080p の 16:9 で 54px 未満の文字は、Apple が UI の最小とする 11pt より小さく見える（計算）。BBC の字幕の大きさ（16:9 で行の高さが画面の高さの 7〜8% = 76〜86px、[[web-type-bbc-subtitle-guidelines]]）は、この換算で Apple の既定 17pt に近い
- 講演 → X 用 60 秒（[[exp-democracy-river-video]]、1920×1080）は X のタイムラインに 16:9 で出した。字幕の px の値は exp ページに無いので、最小を満たしたかは確かめられない
- Polis の v4 で自己採点の「スマホ可読性 4 点」を受けて字幕を拡大し、計画には「360px 幅のスマホ試験」があった（[[exp-polis-magi-op]]）。360px 幅（CSS px、≈ pt）で 1920 幅の動画を見るなら 1pt ≈ 5.3px で、11pt ≈ 59px（計算）
- Words（[[exp-words-as-public-goods-video]]）は「日本語を大きく、英語を小さく併記」。小さい英語が 4:5 で 30px を下回るなら、Apple の最小より小さい（px の値は記録に無い）

### 書体の太さ

- Apple は「細い字は推奨より大きく」、WCAG の解説は「細い字はアンチエイリアスで薄くなる」と書く。Polis の明朝の白字幕（[[exp-polis-magi-op]]）は線の細い書体で、スマホで小さく見ると読みにくくなる側（推測）。経文のアゲアゲ版はヒラギノ角ゴ W9 で、欠字を W6 で補うと「一部がフォント違い」になった（[[exp-sutra-hype-editions]]）。太さを揃えることは見た目の統一でもある

### コントラスト

- 白い文字を黒地に置けば 21:1 で、1.4.3 の 4.5:1 を大きく超える。BBC が字幕を黒地にするのも同じ理由（[[web-type-bbc-subtitle-guidelines]]）。西尾の canvas の動画の多くは暗い背景に図形と文字を描いていて、背景を作り手が決められる。このとき 1.4.3 は計算できる（Vanderheiden の反論の前提「背景を制御できない」が当てはまらない）
- **閃光の下の白い文字**: アゲアゲ版で、ドロップの白飛びの減衰を 0.35 秒にしたら約 1 秒字が読めなかった（[[exp-sutra-hype-editions]]）。白い背景の上の白い文字はコントラスト 1:1 に近づく。減衰を 0.16 秒にしたのは、コントラストが下がる時間を縮めたことになる（解釈）。Gyazo の山の「フラッシュと揺れ」（[[exp-gyazo-resumption-video]]）も同じ種類
- **映像の上の焼き込み字幕**: クオリアさん journey は字幕を y=890 以降、主な内容を y=860 以内に分けていて（[[exp-qualia-video]]）、字幕の背景を絵と分ける作りになっている。写真や動く映像の上に字幕を重ねる場合、背景がコマごとに変わるので、半透明の灰色の帯では明るい場面で不足する（Fischer の監査の観察）。縁取りは WCAG の解説では細ければ文字の一部、太ければ背景として扱われる

## Open Questions

- 動画の焼き込みの文字の最小サイズを書いた、スマホ向けのプラットフォームの一次資料は今回見つけられなかった（BBC の字幕の 9:16 の値が一番近い）
- 393pt で幅いっぱいという前提はおおまかで、X・YouTube・TikTok の実際の表示幅は測っていない
- WCAG 1.4.3 が動画の中の文字に当たるかは、2017 年の議論では決着していない。その後の W3C の公式の解釈は確かめていない
- 日本語（CJK）の「大きい文字」の具体の大きさは WCAG に書いていない
