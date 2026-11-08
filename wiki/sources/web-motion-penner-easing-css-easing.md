---
type: source
summary: Robert Penner の easing equations の原典の章（Programming Macromedia Flash MX, 2002, 第 7 章）と W3C の CSS Easing Functions（Level 1・Level 2）。Penner は「動きを時刻から位置を返す関数」として定義し、等速は機械的に見え、ease-in-out が最も自然、4 乗以上は「この世のものでない」感じになると書く。CSS は easing を純関数と定め、ease 系の cubic-bezier の数値と steps()・linear() を規定している
video_types: [any]
url: http://robertpenner.com/easing/penner_chapter7_tweening.pdf
author: Robert Penner／W3C CSS Working Group（Brian Birtles, Dean Jackson, Matt Rakow ほか編）
published: 2002（Penner）／2023-02-13（CSS Easing Level 1, Candidate Recommendation Draft）／2024-08-29（Level 2, First Public Working Draft）
retrieved: 2026-11-09
sources:
  - http://robertpenner.com/easing/penner_chapter7_tweening.pdf
  - https://robertpenner.com/easing/penner_easing_as1.txt（Easing Equations v1.5 の変更履歴）
  - https://www.w3.org/TR/css-easing-1/
  - https://www.w3.org/TR/css-easing-2/
---

# Penner の easing equations（2002）と CSS Easing Functions

## 何の文献か

- **Penner**: Robert Penner "Robert Penner's Programming Macromedia Flash MX"（McGraw-Hill/Osborne, 2002）の第 7 章「Motion, Tweening, and Easing」。著者のサイトで章の PDF（51 ページ）が公開されている。ActionScript の本の一章で、実務家（著者は哲学の訓練を背景に持つと書く）の解説。広く使われている「easeInQuad」などの関数名の出どころ
- **CSS Easing Functions Level 1**: W3C の CSS Working Group の仕様。読んだのは 2023-02-13 の Candidate Recommendation Draft。**Level 2** は 2024-08-29 の First Public Working Draft（linear() 関数を加える）
- 両方とも「動きの曲線をどう定義するか」の文献で、**どの曲線が見る人に良いかを測った研究ではない**

## 書いてあること

### Penner: 動きと tween の定義

- 動きを「a numerical change in position over time」と定義し、要素を position・time・beginning position の三つに分ける。tween はそれに duration と final position を加えたもの
- tween 関数の目的は「to deliver a position for a specific time」。引数は (t, b, c, d) = 時刻・開始位置・変化量・長さ
- 前のフレームの値から次を作る「standard exponential slide」（毎フレーム残りの一定割合だけ進む）と比べ、自分の方式は長さを正確に決められ、「can jump to any point in time without running the tween from the starting point」と書く

### Penner: easing の美学

- 等速（linear）の tween は機械的に見える。工場のロボットアームやベルトコンベアの動き。「For most other things, though, linear motion can look downright ugly.」
- 理論として: 「the mind is constantly interpreting an object's motion in order to infer the forces acting on it」。速度が急に変わると、見えない鎖に引かれた・見えない壁に当たったように感じる（著者の仮説として書いている。検証はしていない）
- 「Easing is acceleration, a change in speed.」ease-in（遅く始まって速くなる）・ease-out（速く始まって止まる）・ease-in-out（前半 ease-in、後半 ease-out）
- 「I use in-out easing pervasively because it produces the most natural-looking motion.」エレベーターを例にする
- **名前の注意**: Flash の ease-in/out は他の多くのアニメソフトと逆で、3D ソフトでは ease-in は「終わりで遅くなる」意味だった、と書く

### Penner: 曲線の種類

| 種類 | 式（ease-in） | Penner の書き方 |
|---|---|---|
| Quadratic | t² | Flash のタイムラインの easing。「normal」easing |
| Cubic | t³ | quadratic より少し曲がる。まだ自然 |
| Quartic | t⁴ | 「It's at the quartic level that the motion starts to feel a bit "other-worldly," as the acceleration becomes more exaggerated.」 |
| Quintic | t⁵ | かなり強い曲線。exponential に近い |
| Sinusoidal | sin(t·π/2) | quadratic よりさらに穏やか。ほぼ 45 度の直線 |
| Exponential | 2^(10(t−1)) | 曲がりが大きい。t=0 で傾きが 0 にならないので近似 |
| Circular | 1 − √(1 − t²) | 加速は劇的で、他より「突然」起きる感じ |

この章が扱うのは linear と上の 7 種（「eight flavors」）。back・elastic・bounce は**この章には無い**。Penner のサイトで配っている ActionScript 1.0 版のライブラリ（Easing Equations v1.5, 2003-05-01）の変更履歴には「1.4 - added elastic and back easing」「1.5 - added bounce easing」とあり、章に無い曲線を Penner 自身がライブラリに足した（v1.4 の日付は書いていない。back は「overshooting cubic easing: (s+1)*t^3 - s*t^2」）。物理のアニメは次の第 8 章と書いている（第 8 章は読んでいない）。

### CSS Easing Level 1

- 「An easing function takes an input progress value and produces an output progress value.」「An easing function must be a pure function meaning that for a given set of inputs, it always produces the same output progress value.」
- 序論: 速さを徐々に上げると「a sense of weight as it appears to gather momentum」が出る、と書く。段階的に進めたい場合（区切りのある車輪）もある
- キーワードの定義（2.2 節）:
  - ease = cubic-bezier(0.25, 0.1, 0.25, 1)
  - ease-in = cubic-bezier(0.42, 0, 1, 1)
  - ease-out = cubic-bezier(0, 0, 0.58, 1)
  - ease-in-out = cubic-bezier(0.42, 0, 0.58, 1)
- cubic-bezier(x1, y1, x2, y2) は P0=(0,0)・P3=(1,1) 固定、x は [0,1] に制限、y は制限なし（だから行き過ぎる曲線も書ける）
- steps(n, jump-start | jump-end | jump-none | jump-both) で段階的な変化
- **長さ（duration）は規定していない**。曲線だけの仕様

### CSS Easing Level 2

- linear() 関数: 点の列の間を直線で補間する。点を細かく取れば任意の曲線（例として「bounce」）を近似できる、と例を載せている

## この wiki への含意

- **「時刻から位置を返す関数」はそのまま経験の作り方**。[[exp-html-capture-pipeline]] の `renderFrame(f)` を時刻だけの純関数にする決まり、Movez の `seek(t)`（[[web-movez-opus-motion-design-course]]）は、Penner の「開始点から走らせずに任意の時刻へ飛べる」を描画全体に広げたもの。前フレームの状態を持つ「exponential slide」型の書き方をすると、好きな秒の静止画を撮る確認ができなくなる。CSS もイージングを純関数と定めている
- **曲線の名前と数値**: showreel の時刻表 `TL` は expo・cubic・back を場面ごとに変えている（[[exp-nishio-showreel]]）。Penner の表で言えば expo は「曲がりが大きい」、cubic は「まだ自然」。back は章の後に Penner がライブラリに足した「行き過ぎる cubic」
- **「4 乗以上は他界的」**: promo の叩き込み（[[exp-gyazo-resumption-video]] の 0.14 秒で 1.8 倍→1 倍）のように誇張したい場面と、talk の説明中の要素の強調とで、曲線の強さを分ける根拠に使える（推測。Penner の印象の記述で、測定ではない）
- **UI の数値は動画の数値ではない**: CSS の ease は、ブラウザの UI 遷移の既定値として決められた曲線。動画の場面転換の曲線として良いかは何も言っていない。ただ曲線は長さに依らない（入力は 0〜1 の進み具合）ので、数秒の動きにもそのまま当てはめられる。当てはめて「自然に見えるか」は別の問題（推測）
- **拍との関係**: [[exp-html-capture-pipeline]] は 120BPM の小節頭で切り替える。切り替えの瞬間を拍に合わせるとき、ease-out（速く始まって止まる）なら動きの頭が拍に当たり、ease-in（遅く始まって速くなる）なら動きの終わりが拍に当たる。どちらを拍に合わせるかは文献に無い（推測）

## Open Questions

- Penner の「力を推し量る」理論や「quartic から他界的」は著者の印象で、知覚の実験で確かめたものではない。easing の好みを測った研究は、この担当では探していない
- Penner の第 8 章（物理のアニメ、ばね・跳ね）は読んでいない
- back・elastic・bounce は Penner のライブラリ v1.4・v1.5（2003）で足された。見た目の性質について Penner が書いた文章は読んでいない（ライブラリのコメントだけ）
- イージングの曲線を拍に合わせる作法（動きの頭を拍に置くか、着地を拍に置くか）について書いた文献は見つけていない
