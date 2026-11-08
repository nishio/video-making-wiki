---
type: source
summary: Motion Canvas の Presentation Mode の公式ドキュメントと関連 issue・リリースノート。アニメーションのコードに beginSlide() で区切りを置くと、そこで再生が止まってスペースキーを待つ。エディタの左のパネルでスライドを移動でき、全画面ではキーボードだけで送る（v3.15.0 から PowerPoint 系のキーにも対応）。発表はブラウザでのリアルタイム描画なので、重い場面ではコマ落ちしうる（issue #752）。区切りで「止まって待つ」作りで、待つ間にループさせる機能はドキュメントに無い
video_types: [embed]
url: https://motion-canvas.io/docs/presentation
author: motion-canvas（OSS プロジェクト。主な作者 aarthificial）
published: 2023-03-07（v3.1.0 で Presentation Mode 追加。ドキュメントの最終更新 commit 4ca346b は 2024-04-06）
retrieved: 2026-11-09
sources:
  - https://motion-canvas.io/docs/presentation
  - https://github.com/motion-canvas/motion-canvas/blob/main/packages/docs/docs/getting-started/presentation.mdx
  - https://github.com/motion-canvas/motion-canvas/blob/main/packages/core/src/utils/beginSlide.ts
  - https://github.com/motion-canvas/motion-canvas/issues/213（Interactive live presentation support）
  - https://github.com/motion-canvas/motion-canvas/issues/441（Feature Request: Presentation mode）
  - https://github.com/motion-canvas/motion-canvas/issues/752（pre-render presentation）
  - packages/docs/blog/2023-03-07-version-3.1.0.mdx, 2023-04-06-version-3.5.0.mdx, 2024-03-21-version-3.15.0.mdx
---

# Motion Canvas の Presentation Mode

## 何の文献か

- Motion Canvas は TypeScript でベクターのアニメーションを書く OSS の道具（MIT）。道具全体の説明は別担当のページ web-motion-canvas がある。ここは**発表の中で送る機能**だけを扱う
- 読んだもの: 公式ドキュメントの "Presentation" のページ（GitHub の `presentation.mdx` と、公開サイト motion-canvas.io/docs/presentation の両方で本文を読んだ）、`beginSlide` の実装、この機能を求めた issue 2 件とその後の issue 1 件、リリースノート 3 件（いずれも gh api で取得）
- **公式サイトのドメインは motion-canvas.io（ハイフンあり）**。GitHub のリポジトリの homepage もこちら。2026-11-09 に **motioncanvas.io**（ハイフンなし）の `/docs/presentation-mode` と `/docs/` を取得したところ、シンガポールの金融系マーケティング会社のサイトが返り、Motion Canvas のドキュメントではなかった
- 最新リリースは v3.17.2（2024-12-14）。リポジトリへの push は 2026-07 にもある（gh api で確認）

## 書いてあること

### 公式ドキュメント（presentation.mdx）

- 「アニメーションを書き出すだけでなく、Motion Canvas を使って**リアルタイムで発表**できる。アニメーションの中にスライドを定義し、Presentation Mode でその間を移動するだけ」と書く
- **`beginSlide(name)`**: スライドの始まりの印。これを yield すると「**再生が一時停止し、SPACE を押すのを待つ**」。例は、一つの場面（scene）の中でテキストを書き換えて `beginSlide('first slide')`、`'second slide'`、`'last slide'` と三つ区切るもの
- **Presentation Mode に入る**: Video Settings タブで RENDER ボタン横のドロップダウンから PRESENT を選ぶ。以後そのボタンで Presentation Mode に入る（同じドロップダウンで書き出しに戻せる）。オンラインエディタでも試せる
- 左のパネルで全スライドの間を素早く移動できる。下の再生操作でスライド間を移動でき、ボタンに重ねると割り当てられたキーが出る。**全画面にすると操作ボタンは消えるが、キーボードで移動できる**

### 実装（beginSlide.ts）

- `beginSlide` は、場面の `slides` に名前と時刻を登録し、`slides.shouldWait(name)` が真の間、毎コマ yield し続ける（時間を進めない）。つまり区切りの位置で**止まって待つ**作り。待っている間に何かを繰り返し動かす仕組みは、この関数には無い（他のスレッドが待機中にどう扱われるかまでは読んでいない）

### この機能ができた経緯（issue）

- **#213 "Interactive live presentation support"**（2023-02-06）: 「自分の発表のほとんどは録画でなく生なので、この道具はそこでも役立ちそう」。アニメーションの中の時刻イベントを、キーを押すことで起こせないか、そうすれば「従来の PowerPoint の発表のように使える」、という要望
- **#441 "Feature Request: Presentation mode"**（2023-02-27）: 「タイムライン上に、そこに来ると止まり、スペース・右クリック・右矢印で再開するイベントを置く。左矢印・左クリックで前のイベントに戻る」という提案。考えた別案として「**クリックを受けるまでループする JSX の関数**」を挙げていた。作者が #213 の重複として閉じた
- v3.1.0（2023-03-07）のリリースノート: 「新しい Presentation Mode で、アニメーションを生で発表できる」
- v3.5.0（2023-04-06）: 「Presentation Mode で動画が滑らかに再生される」（不具合修正）
- v3.15.0（2024-03-21）: 「Presentation Mode が PowerPoint のショートカット（Page Up、Page Down など）に対応」。プレゼン用のリモコン（クリッカー）は多くが Page Up / Page Down を送るので、それで送れるようになったと読める（推測。リリースノートはクリッカーに触れていない）

### 落とし穴の報告（issue #752, 2023-06）

- 利用者が「発表が大きくなって、発表中に**カクつく**。事前に描画しておけないか」と報告。47 秒・一つの場面で、拡大する場面が重く、エディタで 60fps 設定が 47〜48fps、重い所で約 20fps、発表に使うノート PC では 35 → 15fps に落ちた、と書く
- 作者（aarthificial）は「アニメーションの長さ自体は再生の性能に影響しないはず（シークやスライドの切り替えは遅くなりうる）」と答え、「モニタのリフレッシュレートが 60Hz と違うとアニメーションのループがコマを落とす既知の問題がある」と書いた。報告者のモニタは 144Hz。報告者は、fps 設定を 70 に上げると自分の PC では滑らかになり、ノート PC（Ubuntu）では Firefox から Edge に替えると滑らかになったと書いた
- この issue は closed。事前描画の機能が入ったかは、読んだ範囲では分からない

## この wiki への含意

### embed に効くこと

- **embed の作り方として**: Motion Canvas の Presentation Mode は、一つの概念のアニメーションを「話し手が区切りごとに送る」形で作れる。録画した動画をスライドに埋め込むのと違い、区切りの位置で**止まって待つ**ので、話し手は止まった画面の前で好きなだけ話し、準備ができたら次の動きを始められる。Rosling の五つのヒントの「始める時を聴衆に告げてから動かす」（[[web-roslingifier-data-presentations]]）と同じ形を、道具の側で既定にしている
- **ループさせるか、止めて話すか**: Motion Canvas の答えは「止めて話す」。ドキュメントは区切りで止まることだけを書き、待つ間のループは書いていない。#441 では「クリックまでループする」案も挙がったが、採られた設計は「止まって待つ」だった。ループさせたいなら、録画した動画をスライドソフトの Loop にかける（Keynote の Repeat → Loop。[[web-powerpoint-keynote-google-slides-video-playback]]）方が、少なくともドキュメント上は簡単
- **一つのスライドソフトの中に収まらない**: Presentation Mode はブラウザ上のエディタ（またはオンラインエディタ）で動く。PowerPoint や Keynote の発表の途中にこれを挟むなら、発表中にアプリを切り替えることになる。逆に、発表全体を Motion Canvas で作ることもできる（#213 の要望はそれ）。どちらが良いかはドキュメントに無い（推測）
- **会場の機械で確かめる**: 生で描画するので、発表に使う機械・ブラウザ・モニタで性能が変わる（#752）。録画した動画なら書き出した時点で尺とコマが決まり、ffprobe で確かめられる（[[exp-galleria-ffmpeg-measurement-and-delivery]]）。生で描画する embed は、その確認を会場の機械で通しでやる必要がある。この wiki の HTML を描いて撮る経験では、`renderFrame(f)` をフレーム番号だけの純関数にして、どのコマからでも描けるようにしていた（[[exp-html-capture-pipeline]]）。これは書き出し用の決まりで、生の発表のコマ落ちは扱っていない
- **音**: 読んだ範囲のドキュメントは、Presentation Mode での音の扱いを書いていない。話し手が声で語る前提なら、embed の側は無音でよい（推測）

### 経験との照合

- この wiki の経験には Motion Canvas で作ったものも、発表の中で送るアニメーションを作ったものも無い（[[three-video-types]]）。LT の準備では HTML スライドの下書きを AI が作ったが、本番は西尾が Keynote で作り直した（[[exp-lt-20260909]]）。Motion Canvas の Presentation Mode を使うなら、Keynote の発表の途中でブラウザに切り替えるか、発表全体を Motion Canvas に移すかの判断が要る

## Open Questions

- `beginSlide` の待機中に、別のスレッド（`spawn` や `loop` で動かしているもの）が動き続けるかは、実装を読み切っていないので分からない。動き続けるなら「止まって待つ間も背景はループする」ができる。試していない
- 発表中の巻き戻し（スライドを戻ったときに、そのスライドの頭から再生し直すか）は、ドキュメントでは「スライド間を移動できる」以上は書いていない
- #752 の性能の問題（60Hz 以外のモニタでのコマ落ち）がその後直ったかは確かめていない
- 他の道具（Manim など）に同じ「区切りで止めて送る」仕組みがあるかは、このページでは調べていない（道具の比較は別担当）
