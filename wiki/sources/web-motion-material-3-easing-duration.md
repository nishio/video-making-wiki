---
type: source
summary: Google の Material Design 3 の motion のトークン。easing は emphasized（M3 の標準）と standard（実用的な動き）を、画面内で完結・入る・出るの 3 つに分け、duration は 50ms〜1000ms の 16 段階。「面積・移動距離が大きいほど長く」。M3 Expressive の spring（減衰比と剛性）を、小さい部品・部分的・全画面の 3 速度 × 空間・効果の 2 種で出している
video_types: [any]
url: https://m3.material.io/styles/motion/easing-and-duration/tokens-specs
author: Google（Material Design）
published: unknown（読んだトークンのファイルの最終 commit は 2026-04-06、Android の Motion 文書は 2025-01-07）
retrieved: 2026-11-09
sources:
  - https://m3.material.io/styles/motion/easing-and-duration/tokens-specs（JavaScript で描くページで、本文を取得できなかった）
  - https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-sys-motion.scss（最終 commit 763a973, 2026-04-06）
  - https://github.com/material-components/material-components-android/blob/master/docs/theming/Motion.md（最終 commit 2025-01-07）
---

# Material Design 3 の motion: easing・duration・spring のトークン

## 何の文献か

- Google の Material Design 3（M3）のデザインシステムの motion の指針。**指針の本文がある m3.material.io は JavaScript で描くページで、curl でも WebFetch でも本文が取れなかった**（Internet Archive の旧 M2 の「speed」ページも同じく取れなかった）
- 代わりに読んだのは Google 自身が公開している二つ:
  - Material Web（`material-components/material-web`）の motion のトークン値のファイル `_md-sys-motion.scss`（2026-04-06 の commit）
  - Material Components for Android の文書 `docs/theming/Motion.md`（2025-01-07 の commit）。トークンごとの用途の説明がある
- したがって**数値は 2026-11-09 時点の公式の実装・文書による**。「どの場面にどの長さを使うか」という M3 サイト本体の推奨（applying easing and duration）は読めていない
- UI の部品の動き（ボタン・シート・画面遷移）のための値で、効果を測った報告ではない

## 書いてあること

### easing（Android の Motion.md の表と Material Web のトークンから）

| トークン | 値 | 用途（Android 文書の説明の要約） |
|---|---|---|
| emphasized | path（2 つの cubic をつないだ曲線: `M 0,0 C 0.05, 0, 0.133333, 0.06, 0.166666, 0.4 C 0.208333, 0.82, 0.25, 1, 1, 1`） | M3 らしい普通の動きで、画面内で始まり終わるもの |
| emphasized-decelerate | cubic-bezier(0.05, 0.7, 0.1, 1) | M3 らしい動きで画面に入るもの |
| emphasized-accelerate | cubic-bezier(0.3, 0, 0.8, 0.15) | M3 らしい動きで画面から出るもの |
| standard | cubic-bezier(0.2, 0, 0, 1) | 実用的な（utility focused）動きで画面内で完結するもの |
| standard-decelerate | cubic-bezier(0, 0, 0, 1) | 実用的な動きで入るもの |
| standard-accelerate | cubic-bezier(0.3, 0, 1, 1) | 実用的な動きで出るもの |
| linear | cubic-bezier(0, 0, 1, 1) | 「simple, non-stylized motion」 |

- Material Web のトークンでは、emphasized は 1 本の cubic-bezier で書けないため `$easing-emphasized: $easing-standard;` と standard で代用している（CSS の cubic-bezier は制御点 2 つの 1 区間しか表せない。[[web-motion-penner-easing-css-easing]]）
- 旧（M2 の）曲線も `legacy` として残っている: cubic-bezier(0.4, 0, 0.2, 1)、accelerate (0.4, 0, 1, 1)、decelerate (0, 0, 0.2, 1)

### duration（16 段階）

| 群 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| short | 50ms | 100ms | 150ms | 200ms |
| medium | 250ms | 300ms | 350ms | 400ms |
| long | 450ms | 500ms | 550ms | 600ms |
| extra-long | 700ms | 800ms | 900ms | 1000ms |

Android 文書: 「In general, duration should increase as the area/traversal of an animation increases. Maintaining this rule when customizing duration attributes will ensure your transitions have a consistent sense of speed.」easing と duration は組にして使う（推奨の組み合わせは M3 サイトの「Easing and duration guidance」を見よ、と書いている。そのページは読めなかった）。

### spring（M3 Expressive の物理ベースの動き）

| 速度 | 空間（spatial: 位置・大きさ） | 効果（effects: 色・不透明度） | 用途 |
|---|---|---|---|
| fast | 減衰比 0.9、剛性 1400 | 減衰比 1、剛性 3800 | スイッチ・ボタンなど小さい部品 |
| default | 減衰比 0.9、剛性 700 | 減衰比 1、剛性 1600 | 画面の一部を覆う（ボトムシート、ナビゲーションドロワー） |
| slow | 減衰比 0.9、剛性 300 | 減衰比 1、剛性 800 | 全画面のアニメーション・遷移 |

- 「A speed is chosen based on the size of the component being animated or the distance covered.」
- 空間の spring は減衰比 0.9 で少し行き過ぎてよい。効果の spring は減衰比 1（行き過ぎない）。「a background's alpha shouldn't bounce or oscillate above 100%」と、色や不透明度は行き過ぎてはいけないものとして分けている

## この wiki への含意

### 指針が書いている範囲と、動画へ移せる範囲（推測）

- **書いている範囲**: 利用者の操作に応じた UI の部品の動き。最長でも 1000ms。「全画面」と言っても画面遷移のこと
- **動画の場面転換にそのまま当てはまらない**: 数十秒の動画の場面の長さ（[[exp-polis-magi-op]] の 1 カット平均 1.07 秒、[[exp-words-as-public-goods-video]] の 2〜6 秒）は、M3 の duration の対象外。M3 の数値が使えるのは、場面の**中で**要素が出入りする動き（文字が飛び込む、枠が広がる）の長さの目安まで（推測）
- **移せそうな原則**: 「面積・移動距離が大きいほど長く」「入るときは減速、出るときは加速」「位置や大きさは少し行き過ぎてよいが、色・不透明度は行き過ぎない」。最後のものは、動画で白い閃光や透明度を spring で動かすと 100% を超えて「ちらつく」ことを防ぐ注意として、そのまま使えそう（推測）

### 経験との照合

- Gyazo の叩き込み文字は 0.14 秒（140ms）で 1.8 倍→1 倍に縮んで着地し行き過ぎる（[[exp-gyazo-resumption-video]]）。M3 の表では short3〜short4 の範囲で、小さい部品の fast spring（減衰比 0.9、行き過ぎあり）の動きに近い。文字が画面の大部分を占めるなら、M3 の「面積が大きいほど長く」とは逆の選択になっている（推測。promo の誇張として意図的）
- クオリアさん pilot の 0.42 秒のクロスフェード（[[exp-qualia-video]]）は M3 の long1 付近。クロスフェードは不透明度の変化なので、M3 の分け方では効果（effects）側の動き。否定されたのはクロスフェードではなく全画面の pan / zoom の drift だった
- Polis v4 の「ばね」（[[exp-polis-magi-op]]）を入れるなら、M3 の spring の値（減衰比 0.9、剛性 300〜1400）は出発点になる。ただし M3 の spring は物理シミュレーションの値で、[[exp-html-capture-pipeline]] のように時刻の純関数で描くには、閉形式（減衰振動の式）に直す必要がある（Polis の HANDOFF にも「閉形式ばね」とある）

## Open Questions

- M3 サイト本体の「applying easing and duration」（どの場面にどの組を使うか、全画面の遷移の推奨値）は読めていない。JavaScript を実行できる取得手段が要る
- emphasized と standard の使い分け（「M3 らしい」と「実用的」）は Android 文書の短い説明だけで、M3 の側の理由は読めていない
- spring の剛性・減衰比が、何 px の移動で何 ms 程度に落ち着くかは計算していない。動画の時刻表に入れるなら秒に直す必要がある
