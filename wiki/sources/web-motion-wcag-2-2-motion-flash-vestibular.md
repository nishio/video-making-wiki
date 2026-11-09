---
type: source
summary: WCAG 2.2 の動きに関する 3 つの達成基準（2.2.2 Pause, Stop, Hide、2.3.1 Three Flashes or Below Threshold、2.3.3 Animation from Interactions）の Understanding 文書と、前庭障害と画面の動きについての Val Head の記事（A List Apart, 2015）。閃光は「1 秒に 3 回まで、または面積・明るさが閾値未満」、自動で動くものは 5 秒を超えるなら止められるように、操作で起きる飾りの動きは切れるように、と書く。前庭障害の引き金になりやすいのは「画面に対して大きな動き」「向きや速さの食い違い（視差）」「大きな距離を素早く移る動き」で、不透明度・色・ぼかしだけの変化は問題になりにくい、と書く
video_types: [any]
url: https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html
author: W3C Accessibility Guidelines Working Group／Val Head（A List Apart）
published: 2023-10-05（WCAG 2.2 の勧告。Understanding 文書は随時更新）／2015-09-08（Val Head、2020-04-30 更新）
retrieved: 2026-11-09
sources:
  - https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html
  - https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html
  - https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html
  - https://alistapart.com/article/designing-safer-web-animation-for-motion-sensitivity/
---

# WCAG 2.2 の動きの達成基準と、前庭障害と画面の動き（Val Head 2015）

## 何の文献か

- **WCAG 2.2**（Web Content Accessibility Guidelines）は W3C の勧告。読んだのは達成基準ごとの **Understanding 文書**（「Informative explanations, not required to meet WCAG」と書かれた解説で、規範の本文そのものではないが、達成基準の文言を含む）。2026-11-09 時点の公開版
- **Val Head "Designing Safer Web Animation For Motion Sensitivity"**（A List Apart, 2015-09-08、2020-04-30 更新）。Web のアニメーションの実務家が、前庭障害のある 2 人（Greg Tarnoff、Craig Grannell）への聞き取りをもとに書いた実務記事。**研究ではなく、2 人の経験からの整理**。WCAG 2.3.3 の Understanding が関連資料として挙げている
- どちらも Web ページ向け。動画については「Web ページに置かれた動画」として触れる範囲

## 書いてあること

### 2.3.1 Three Flashes or Below Threshold（レベル A）

- 達成基準: 「Web pages do not contain anything that flashes more than three times in any one second period, or the flash is below the general flash and red flash thresholds.」
- 閃光（flash）の定義: 「a pair of opposing changes in relative luminance」。明→暗→明の**往復で 1 回**
- 閾値（general flash and red flash thresholds）。次のどちらかなら合格:
  - 1 秒間の general flash が 3 回以下、かつ／または red flash が 3 回以下
  - 同時に光る面積の合計が、典型的な視距離での 10 度の視野の中で 0.006 ステラジアン（10 度の視野の 25%）以下
- general flash: 相対輝度の最大値（1.0）の **10% 以上**の往復の変化で、暗い側の相対輝度が 0.80 未満のもの
- red flash: 飽和した赤を含む往復の遷移。WCAG 2.2 で新しい作業定義: 一方の状態の R/(R+G+B) ≥ 0.8 で、CIE 1976 UCS 色度図で両状態の差が 0.2 を超えるもの
- 例外: 細かく釣り合った模様（ホワイトノイズや、1 辺 0.1 度未満の市松模様）は閾値違反にしない
- 10 度の視野の目安: 1024×768 で表示したときの 341×256 ピクセルの矩形。CSS ピクセルに直すと 87,296 CSS px の面積
- 動画について: 「with a video that may play in an area of a web page and also at full screen, the video should be analyzed for risks at full screen.」「For short clips that might be looped (such as GIF animations), the content should be analyzed while looping.」HDR などで検証する場合は ITU-R BT.1702 の定義（暗い側が 160 cd/m² 未満なら 20 cd/m² 以上の変化）を使う
- 元は英国のテレビ放送の基準をコンピュータの画面に合わせたもの、と書く（放送の基準は [[web-motion-itu-r-bt1702-ofcom-nhk-minpo-flash-guidelines]]）
- 「Blinking」（気を散らす点滅。短時間なら許される）と「Flashing」（発作を起こしうる。1 秒も許されない。止める操作を用意しても足りない。発作は止める前に起きうるから）を分けている
- 1 秒に 3 回以下なら道具で測る必要はなく自動的に合格、と書く。道具の例として Harding FPA と Trace Center の PEAT を関連資料に挙げる（どちらも開いていない）

### 2.2.2 Pause, Stop, Hide（レベル A）

- 達成基準: 自動で始まり、**5 秒を超えて続き**、他の内容と並んで表示される動く・点滅する・スクロールする情報には、止める・停止する・隠す仕組みを用意する（その動きが不可欠な活動の一部である場合を除く）
- 「Moving, blinking and scrolling」の例に「motion pictures, synchronized media presentations, animations」を含める
- 5 秒の理由: 注意を引くには十分長く、待てないほど長くはない
- 注意欠陥のある人などには、連続した動きが他の部分を読む妨げになる

### 2.3.3 Animation from Interactions（レベル AAA）

- 達成基準: 「Motion animation triggered by interaction can be disabled, unless the animation is essential to the functionality or the information being conveyed.」
- 前庭（内耳）障害の反応は、めまい・吐き気・頭痛。「potentially needing bed rest to recover」まである、と書く
- スクロールに合わせて要素が動く、視差スクロール（背景と前景が違う速さで動く）を、不要になりがちな例に挙げる
- motion animation の定義: 「addition of steps between conditions to create the illusion of movement」。**色・不透明度の変化は含まない**（ぼかしは正誤表で除外から外された）
- 対処: 不要な動きを避ける、切る操作を用意する、OS や UA の Reduce Motion（CSS の `prefers-reduced-motion`）を使う

### Val Head（2015）: 前庭障害の引き金になる動き

- 引き金になりやすい要因を三つ挙げる:
  - **相対的な大きさ**: 画面の大きさそのものより、画面に対する動きの大きさ。「a small button with a 3D rotation probably won't cause trouble, but a full-screen wipe transition covering the entire screen likely would」「Animation that involves only non-moving properties, like opacity, color, and blurs, are unlikely to be problematic.」
  - **向きと速さの食い違い**: 誇張した視差、スクロールと違う向き・速さで動くもの
  - **移る距離**: 仮想の空間で大きな距離を素早く移るもの（iOS 7 の 3D ズームの遷移）
- 聞き取った 2 人とも、アニメーションを全部なくしたいとは言っていない、と書く
- 安全にするには: 目的のある動きにする、どんな動きが起きるかを前もって知らせる、動きを減らす・切る操作を用意する
- 有病の規模として vestibular.org の数字（米国の成人で約 800 万人が慢性のバランスの問題、さらに 240 万人が慢性のめまい）を引いている（原典は確かめていない）

## この wiki への含意

### 指針が書いている範囲と、動画へ移せる範囲（推測）

- **2.3.1 の閃光の基準は、動画にそのまま当てはまる**。Understanding 自身が「動画は全画面で評価せよ」「ループする短い動画はループさせて評価せよ」と書いている。放送の基準（ITU-R BT.1702）が元なので、映像全般の基準として扱ってよい
- **2.2.2 と 2.3.3 は Web ページの操作の話**で、動画の中身の作り方を縛るものではない。ただし、動画を Web ページやスライドに**自動再生・ループで埋め込む**と、2.2.2 の「5 秒を超えて自動で動くものは止められるように」に当たる（推測）
- **前庭障害の三要因は、動画の画面全体の動き（パン・ズーム・ワイプ・画面の揺れ）にも当てはまりそう**。Val Head の記事はスクロールと UI の遷移の話だが、要因は「画面に対する動きの大きさ」なので、平面の動画でも効くと考えるのが自然（推測。動画で測った文献は読んでいない）

### 経験との照合

- **[[exp-qualia-video]] の「全画面の drift は気持ち悪い」と同じ向き**。pilot の全 scene 1.8% 拡大＋sin 波の低速パンは、Val Head の言う「画面全体の動き」に当たる。0.42 秒のクロスフェードは「不透明度だけの変化」で問題になりにくい側。人間の評価で否定されたのが drift の方だったのと、Val Head の整理は一致する
- **promo の画面の揺れ**: Gyazo の `HITS` の「フラッシュと画面の揺れ」（[[exp-gyazo-resumption-video]]）、アゲアゲ版の叩きつけ（約 1.9 倍→戻る、画面が青く光る）（[[exp-sutra-hype-editions]]）は、全画面の拡大・揺れ・閃光を組み合わせている。前庭障害の観点では引き金になりやすい側。閃光の回数と面積は 2.3.1 と放送の基準で確かめる必要がある（[[web-motion-itu-r-bt1702-ofcom-nhk-minpo-flash-guidelines]] に計算）
- **embed をループで流す場合**: Understanding は「ループする短い動画はループさせて評価」と書く。ループの継ぎ目で明暗が反転すると、1 回だけの再生では出ない閃光が出る（推測）
- 型ごと: 閃光の基準は promo（速いカット・閃光を使う）で一番効く。talk は静止が既定なので当たりにくい。embed は会場の大画面で流すと視野に占める割合が大きく、2.3.1 の注記「画面に近い人は、規範上合格する閃光でも影響を受ける」が当たる（推測）

## Open Questions

- 2.3.1 の面積の基準（10 度の視野の 25%）は「典型的な視距離」の前提。会場のスクリーン、スマホを顔に近づけて見る縦長動画では、視野に占める割合が違う。WCAG 自身が「視距離は考慮できない」と注記している
- 前庭障害の三要因は 2 人への聞き取りからの整理で、数値の閾値（何 % の画面の動きから、何度/秒から）は無い
- Harding FPA・PEAT の判定手順は読んでいない。経験の動画（Polis の OP 様式、アゲアゲ版）を実際に測ったことはない
- 2.3.2 Three Flashes（AAA、面積の例外なしに 1 秒 3 回まで）の Understanding は読んでいない

## Updates

### 2026-11-09 台本のファクトチェックから（[[explainer-script-factcheck-2026-11]]）

- published の 2023-10-05 は WCAG 2.2 の初版の日付。現行は W3C Recommendation 2024-12-12、Understanding 2.3.1 は 2025-09-17 更新
- 閃光の基準の元: Understanding 2.3.1 の原文は "based on existing specifications in use in the UK and by others for television broadcast"（英国の放送の基準）。このページの含意の節の「放送の基準（ITU-R BT.1702）が元」は言い方が違う
- Understanding は "the video should be analyzed for risks at full screen" と書く
