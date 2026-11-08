---
type: source
summary: Apple Human Interface Guidelines の Motion と Accessibility の動きの部分。「動きのための動きを足さない」「動きだけで重要な情報を伝えない」「Reduce Motion が有効なら自動・反復の動き（拡大縮小・周辺視野の動き）を減らし、x・y・z の移動をフェードに置き換える」と書き、visionOS では周辺視野の動き・世界の回転・0.2Hz 付近の持続的な揺れを避けるよう書く。動画の再生には Dim Flashing Lights（閃光を減らす設定）への対応を求める
video_types: [any]
url: https://developer.apple.com/design/human-interface-guidelines/motion
author: Apple（Human Interface Guidelines）
published: unknown（Motion の変更履歴の最新は 2025-09-09「Added guidance for Liquid Glass」、Accessibility は 2025-06-09）
retrieved: 2026-11-09
sources:
  - https://developer.apple.com/design/human-interface-guidelines/motion
  - https://developer.apple.com/design/human-interface-guidelines/accessibility
  - https://developer.apple.com/documentation/mediaaccessibility/flashing-lights
---

# Apple Human Interface Guidelines: Motion と Accessibility（動き）

## 何の文献か

- Apple の公式デザインガイド（HIG）の Motion のページと、Accessibility のページの動きに関する部分。ページは JavaScript で描かれるが、Apple の文書が使う JSON（`developer.apple.com/tutorials/data/design/human-interface-guidelines/*.json`）から本文を取り出して読んだ。2026-11-09 時点の公式ページによる
- 変更履歴: Motion は 2025-09-09（Liquid Glass の指針を追加）、2024-06-10（ゲームの例を追加）など。Accessibility は 2025-06-09（Assistive Access などを追加）、2025-03-07（全体を拡充）
- アプリ・ゲームの UI のための指針。**数値（ミリ秒）や easing の曲線は書いていない**。効果の根拠も示していない

## 書いてあること

### Motion のページ

- 「Add motion purposefully, supporting the experience without overshadowing it. Don't add motion for the sake of adding motion. Gratuitous or excessive animation can distract people and may make them feel disconnected or physically uncomfortable.」
- 「Make motion optional.」動きを重要な情報を伝える唯一の手段にしない。触覚や音で補う
- フィードバックの動きは短く正確に: 「When animated feedback is brief and precise, it tends to feel lightweight and unobtrusive, and it can often convey information more effectively than prominent animation.」
- 頻繁に起きる操作に動きを足さない。動きを取り消せるようにする（動き終わるまで待たせない。特に何度も見る動き）
- ゲームでは 30〜60fps を保つと滑らかに見える、と書く
- **visionOS**（没入型の空間）:
  - 「avoid displaying motion at the edges of a person's field of view」周辺視野の動きは、自分や周囲が動いているように感じさせ不快を生む
  - 大きな物体を動かすときは半透明にするかコントラストを下げて、動きを目立たなくする
  - 物を移すとき、移動に意味が無ければ、フェードアウト→移動→フェードインにする
  - 仮想の世界を回転させない。向きを変えるなら素早いフェードの間に一瞬で変える
  - 「Consider giving people a stationary frame of reference.」動かない領域の中に動きを収めると扱いやすい。周り全体が動くと気分が悪くなりうる
  - 「Avoid showing objects that oscillate in a sustained way. In particular, you want to avoid showing an oscillation that has a frequency of around 0.2 Hz because people can be very sensitive to this frequency.」揺らすなら振幅を小さく、半透明に

### Accessibility のページ（動きの部分）

- 「Let people control audio and video playback.」自動再生するなら開始・停止の操作を用意する
- 「Allow people to opt out of flashing lights in video playback.」Dim Flashing Lights の設定があれば、システムが動画の閃光を計算して和らげ、知らせる。動画を再生するアプリはこの設定に応じる
- 「Be cautious with fast-moving and blinking animations. When you use these effects in excess, it can be distracting, cause dizziness, and in some cases even result in epileptic episodes.」
- **Reduce Motion** が有効なら、「reducing automatic and repetitive animations, including zooming, scaling, and peripheral motion」。そのほかの減らし方:
  - spring を締めて跳ねを減らす
  - 動きを人の手の動きに直接追従させる
  - z 方向（奥行き）の変化をアニメートしない
  - **x・y・z 軸の遷移をフェードに置き換える**
  - ぼかしへの出入りをアニメートしない
- visionOS: 周辺視野の動きの速さと強さを下げる。「Be gentle with camera and video motion, and avoid situations where someone may feel like the world around them is moving without their control.」

### Dim Flashing Lights（開発者文書 MediaAccessibility）

- 設定が有効になったら、独自のタイムライン表示に閃光の強さを示す、閃光の無い別版があればそれを再生して知らせる、プログラムで制御できる閃光のアニメーションは調整する、と書く
- システムがどの基準で閃光を判定するかは、この文書には書いていない

## この wiki への含意

### 指針が書いている範囲と、動画へ移せる範囲（推測）

- **書いている範囲**: アプリ・ゲームの UI。visionOS の記述は頭に着けて視野全体を覆う没入型の画面の話で、平面の画面で見る動画とは視野に占める割合が違う
- **動画へ移せそうなこと**: (1) 動きのための動きを足さない、(2) 全画面の移動・拡大縮小・周辺の動きが不快の主な原因で、フェード（不透明度）は比較的安全、(3) 動かない枠（参照の枠）を残す、(4) 持続的な揺れを避ける。これらは視聴者が操作できない動画（特にシステムペースの embed）にこそ効くはず（推測）。ただし動画の側には Reduce Motion の設定を受け取る仕組みが無い（Web に埋め込む場合を除く）ので、**作る段階で最初から減らしておく**しかない

### 経験との照合

- **[[exp-qualia-video]] の「解説動画でゆっくり動くの気持ち悪いなw」と一致する向き**。pilot は全 scene に 1.8% の拡大と sin 波の低速パンをかけていた。Apple は Reduce Motion で減らすべきものとして zooming・scaling・peripheral motion を挙げ、visionOS では「周り全体が動くと気分が悪くなる」「持続的な揺れ（特に 0.2Hz 付近）を避ける」と書く。pilot の sin 波パンの周期は経験ページに書かれていないので、0.2Hz（5 秒周期）に近かったかは分からない（未確認）
- **A/B/C 比較の結論とも同じ向き**: 静止（A）を既定にし、動かすなら説明中の要素を直接強調する（[[exp-qualia-video]]）は、Apple の「動きを重要な情報の唯一の手段にしない」「動きのための動きを足さない」と合う
- **promo の経験とは向きが違う**: アゲアゲ版・叩き込み文字・OP 様式（[[exp-sutra-hype-editions]]、[[exp-gyazo-resumption-video]]、[[exp-polis-magi-op]]）は、画面の揺れ（`HITS` のフラッシュと画面の揺れ）・拡大縮小・速い切り替えを意図的に使っている。Apple の言う「fast-moving and blinking animations を過剰に使うと、めまいや、場合によっててんかん発作」に当たりうる。閃光の数値の基準は [[web-motion-itu-r-bt1702-ofcom-nhk-minpo-flash-guidelines]] と [[web-motion-wcag-2-2-motion-flash-vestibular]] で確かめる
- **ナレーション無しの動画で動きを唯一の手段にしない**: 無音で自動再生される promo（[[exp-words-as-public-goods-video]]）は文字で伝える作りで、動きだけに頼っていない

## Open Questions

- 0.2Hz の揺れへの敏感さについて、Apple は根拠の文献を示していない。平面の画面の動画でも同じかは分からない
- Dim Flashing Lights がどの基準（ITU-R BT.1702 か、独自か）で閃光を判定するかは書いていない。YouTube や X の再生に効くかも分からない
- 「x・y・z の遷移をフェードに置き換える」は、promo の勢い（[[exp-sutra-hype-editions]] の「変化が止まると下がる」）とぶつかる。fade だけで勢いが保てるかは試していない
