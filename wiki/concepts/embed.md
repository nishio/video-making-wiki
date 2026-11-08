---
type: concept
summary: 西尾の語「プレゼンの中に埋め込んで使う特定概念を解説するもの」の型（embed）について、経験が無いところを文献で埋めたページ。根拠のある実例はループではなく「話し手が時間を握る」形（先に見方を言い、始める時を告げて流し、動いている最中に意味を語る）で、アニメーションは中身の変化を見せる時だけ効き、抽象的・記号的な表現のアニメは効果が見られなかった
video_types: [embed]
sources:
  - web-roslingifier-data-presentations.md
  - web-powerpoint-keynote-google-slides-video-playback.md
  - web-motion-canvas-presentation-mode.md
  - web-victor-explorable-explanations.md
  - web-nicky-case-explorable-explanations.md
  - web-hohman-2020-communicating-with-interactive-articles.md
  - web-3blue1brown-explainer-advice.md
  - web-berney-betrancourt-2016-animation-meta-analysis.md
  - web-tversky-2002-animation-can-it-facilitate.md
  - web-mayer-multimedia-principles.md
  - web-common-craft-script-writing-guide.md
  - exp-*.md（本文に個別の出典）
---

# プレゼンの中に埋め込んで使う特定概念を解説するもの（embed）

西尾の語のまま（[[origin-2026-11-09]]）。三つの型の比較は [[three-video-types]]。**この型の直接の制作経験は wiki にまだ無い**（[[three-video-types]]）。以下は文献が中心で、経験への当てはめは推測として書く。

## 「ループさせるか、止めて話すか」（[[three-video-types]] の Open Question）への文献の答え

- **根拠のある実例は「話し手が時間を握る」形**。Roslingifier（Shin ら、IEEE TVCG / VIS 2022。読んだのは投稿版）は、話し手が動くグラフを語る発表 11 本（うち Hans Rosling 6 本）を分析し、再生の操作を「止める・遅くする・速くする・巻き戻す・全体をもう一度流す」の 5 種に分けた。止めるのは理由を説明するとき、もう一度流すのは消化する時間を与えるときに使われていた、と報告している（[[web-roslingifier-data-presentations]]）
- Garr Reynolds が要約した Rosling の「バブルを見せる五つのヒント」は、**先に軸と色の意味を言う → 注目する点を示す → 始める時を告げてから動かす → 動いている最中に意味を語る**（同）
- **道具の既定も「止めて話す」寄り**。PowerPoint・Keynote・Google Slides の三つとも、既定は話し手が送る操作で再生が始まる。ループは Keynote が公式に書いている（Repeat → Loop、「次へ進むまで繰り返す」）。発表中の一時停止は Keynote が K、Google Slides が k（[[web-powerpoint-keynote-google-slides-video-playback]]）
- Motion Canvas の presentation mode は `beginSlide()` で止まってスペースを待つ設計で、要望段階で出た「クリックまでループ」案は採られなかった（[[web-motion-canvas-presentation-mode]]）
- **ただし、どれも観察と比較条件の無い評価・道具の仕様**。ループとの比較実験は見つかっていない

## 一つの概念を短いアニメーションで渡すこと

- **動くのが中身の変化なら効き、飾りの動きは効かない**。Höffler & Leutner 2007 で表現的なアニメ d=0.40、装飾的なアニメ ≈0。Berney & Bétrancourt 2016 のメタ分析では全体 g=0.23、ばらつきは大きい（I²=78%）（[[web-berney-betrancourt-2016-animation-meta-analysis]]。Höffler & Leutner は抄録と二次の要約から）
- **embed に一番効く知見**: Berney & Bétrancourt で、抽象的・記号的な表現のアニメは効果が見られなかった（g=0.006, k=26）。アニメが効いた条件は、学習者がペースを操作できないとき（g=0.31）、文字を添えないとき（g=0.89, k=14）、ナレーションと組むとき（g=0.32）。画面の文字と組んだときは有意でなかった（0.105）（同）
- Tversky ら 2002 は、アニメが勝ったとされた研究の多くは比べ方が悪かった（アニメの側だけ情報が多い等）と指摘し、Congruence（変化の構造と表現の構造を合わせる）と Apprehension（見て取れる速さ・単純さ）の二原則を挙げる（[[web-tversky-2002-animation-can-it-facilitate]]）
- 3Blue1Brown の Sanderson は「動きには一つずつ目的を。ナレーションと同じ点を伝え、注意を奪い合わない」「具体から先、定義から始めない」と書く（[[web-3blue1brown-explainer-advice]]）
- Distill の Hohman ら 2020 は、アニメーションの効果には議論があると認め、4 用途（状態の遷移・不確かさ・因果・物語）を挙げる。引用先は実験・知覚研究・アニメーターの本が混ざっていて強さが揃っていない（[[web-hohman-2020-communicating-with-interactive-articles]]）
- **予想を先に立てさせる型**には実験がある。Kim ら 2017（MTurk 378 人）で予想と自己説明をさせると想起の誤差が 1 点あたり 4.08 ポイント減った。ただし文で見せた場合は効果が出ず、よく知っている題材では再現しなかった（同）。発表の場で口頭で問う条件とは違う
- Bret Victor の Explorable Explanations は「操作しなくても普通に読める」「作者が会話の自分の側を担う（砂場は説明ではない）」（[[web-victor-explorable-explanations]]）。Nicky Case の型は「問い → 具体から一段ずつ上る → 最後に砂場」（[[web-nicky-case-explorable-explanations]]）。embed に移すと「話し手がただ流しても通じ、止めたり戻したりすれば深くなる」になる（推測）

## 研究のペースの条件から

- 講演の中で流す embed は、聴衆が止められないのでシステムペースの典型。設計原則はシステムペースでより効く（g=0.41 対 0.27）ので、coherence・signaling・contiguity を丁寧にやる意味が大きい（[[web-mayer-multimedia-principles]] の担当の推論）
- 話し手が流す前に概念の名前と見方を言うことは pre-training、動画を止めて話すことは segmenting に当たる（同、推論。未検証）

## 経験への当てはめ（推測、試していない）

- 般若心経の同期解説（[[exp-sutra-sync-subtitles]]: 45 秒・ナレーションなし・3 回反復）は、反復を動画の中に焼き込んでいる。発表で使うなら「1 回目は話し手が先に見方を話してから流し、2 回目以降は黙って音を聞かせる」が Rosling 型に近い。ただし唱える音そのものが中身なので、「動いている最中に語る」とはぶつかる（[[web-roslingifier-data-presentations]] の含意）
- 同期解説の「全部を常時表示し、光る位置だけ動かす」は、Kim 2014 の「消えた画面に戻る」観察、Tversky の「静止図は見比べ・見直しができる」と同じ向き（[[web-kim-2014-in-video-dropouts]]、[[web-tversky-2002-animation-can-it-facilitate]]）
- クオリアさんの 4 秒の A/B/C 比較（[[exp-qualia-video]]）を発表で見せるなら、「先に何を見るかを告げてから流す」がそのまま使える
- 動画の側に録音した語り（TTS）があると、話し手が告げて語る形とぶつかる。Rosling 型に寄せるなら、embed の動画はナレーションを入れず、無音か小さい音にして話し手の声で語る作りになる。三つのスライドソフトの機能だけでできる一番単純な形もこれ
- Common Craft の「約 3 分・1 概念・授業の中で導入として流す」使い方は、embed に一番近い実務の型（[[web-common-craft-script-writing-guide]] の担当の見立て。未検証）

## Open Questions

- **抽象的・記号的なアニメは効果が見られなかった（g=0.006）** と、3Blue1Brown が数学の抽象概念をアニメで見せて支持されていることの関係。メタ分析の「抽象」が何を指すか（記号の動き、か、抽象概念の具体化、か）を原典で確かめる
- 「文字を添えないアニメが効く（g=0.89）」は、字幕を焼き込む西尾の作り方と逆向き。embed で話し手が話すなら字幕は要らない、と読めるが未検証
- ループと「話し手が時間を握る」の比較実験は見つかっていない。どちらが伝わるかは分からない
- embed の尺は発表が決める。文献に数値は無い
- embed を作る道具として、Motion Canvas の presentation mode（スライドとして送る）と、mp4 をスライドに貼る方式のどちらが良いかは試していない。[[video-tools-comparison]] を参照
