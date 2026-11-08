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

## Updates

### 2026-11-09 経験の材料: THINKLET の読書支援のデモ動画

最初の抽出の取りこぼしとして [[exp-thinklet-reading-demo-video]] が入った（52 秒、西尾が Premiere Pro で編集、2026-09-09 の LT の語り順に「デモ動画あり」と入った候補。実際に流したかは未確認）。embed の経験の候補として、上の文献と照らす。

- **ナレーション入りの動画である点**: 動画には VOICEVOX（ずんだもん）のナレーション 3 本（約 28 秒）が入っている。Rosling 型（話し手が告げて語る）に寄せるなら、発表で流すときにこのナレーションとぶつかる。流したなら、ナレーションを消したか、流したまま話し手が黙ったかが、このページの Open Question「ループさせるか、止めて話すか」の最初の実例になる（未確認）
- **待ち時間を説明に変えた**: 実機の約 30 秒の処理待ちを「今何が起きているか」の説明にした。これは Rosling の「動いている最中に意味を語る」と同じ形を、動画の側のナレーションでやったもの（推測）。話し手がいる場なら、同じ語りを話し手がやれる
- **ライブのデモの代わり**: 10/2 の THINKLET 開発者イベントの LT は「事前録画した映像で行い、ライブ解説はしない」と決めた（[[exp-thinklet-reading-demo-video]]）。embed には「概念を見せる」だけでなく「ライブのデモが危ういときに録画で置き換える」用途がある。文献（Roslingifier・スライドソフトの資料）はこの用途を扱っていない
- この動画は手作業の編集で、[[video-tools-comparison]] のどの道具でもない。embed を作る道具の選択肢に「人が編集ソフトで組む」も残る

### 2026-11-09 西尾の回答: 流しっぱなしの前提

[[survey-2026-11-summary]] の「次に調べること」の 1 に、西尾が答えた（[[origin-2026-11-09]] の Updates）:

- 「プレゼンの中に埋め込んで使う」動画は、話し手が操作する前提か、流しっぱなしの前提か → **「流しっぱなしの前提」**
- THINKLET の動画を LT で流したとき → **「流しっぱなし」**（[[exp-thinklet-reading-demo-video]]。どの LT かは言っていない）

これで、このページの上の「根拠のある実例は話し手が時間を握る形（Rosling 型）」は、西尾の embed の前提ではないことが分かった。

- 流しっぱなしなら、embed の動画は**自分で時間を持つ**。止める位置・告げてから流す、という Rosling 型の作法は使えない。研究の語ではシステムペース（[[web-mayer-multimedia-principles]]）で、設計原則が効きやすい側
- 流しっぱなしなら、動画の側にナレーションがあってよい。THINKLET の動画はずんだもんのナレーション入りで流しっぱなしにした。このとき話し手がナレーションの間に話したか黙ったかは聞いていない
- 上の「経験への当てはめ」の「embed の動画はナレーションを入れず、無音か小さい音にして話し手の声で語る」は Rosling 型を前提にした推測なので、流しっぱなしの前提では成り立たない。流しっぱなしで話し手と動画の声がどう分担するかが、次の問い
- ループの比較実験が無いことは変わらない。ただ、流しっぱなし（1 回流して終わる）とループ（次へ進むまで繰り返す）も、また別

### 2026-11-09 第 2 回サーベイから（流しっぱなしの前提で読む）

- 流しっぱなしの embed を、LLM がコードで描く方式で作った例は外に見つからなかった。HyperFrames の公式ガイドは「誰も話さず最初から最後まで流すならデッキでなく動画」と分けている（[[web-opus2-hyperframes-after-2026-09-22]]、[[after-opus55]]）
- Anthropic の Claude Motion の用途の例（全社集会の 30 秒の解説、資料のグラフに動き）は embed に近い（[[web-opus-anthropic-claude-motion]]）。日本語の「動く図解」の制作記（KAKERU デザイン、2026-09-24）も提案書・研修への埋め込みを用途に挙げる（opus の担当の報告。ページにはしていない）
- 流しっぱなしでは見る時間を動画が決める。字幕・文字の表示時間の規則（日本語 1 秒 4 字、最短 0.5 秒・最長 7 秒）と、「データを描く飾りは損が無い」（見る時間を制限しない条件）の違いに注意（[[design-fundamentals]]）

### 2026-11-09 第 3 回サーベイから

- **流しっぱなしの外の実例が見つかった**: 学会の Fast Forward（10〜30 秒、止まらない）。話し手が上に乗る版は録音したナレーションを禁止し（VIS 2015）、単独で流れる版はナレーションを必須にしている（VIS 2024）（[[web-embed-siggraph-ieeevis-chi-fast-forward]]）
- **動画の声と話し手の分担**への最初の答え: 流す前に、何が映るかを一言で言う（Ladner、[[web-embed-ladner-sigaccess-chi-video-in-talks]]）。字幕や手話通訳を頼る人は一度に一つしか見られないので、動画の間に話すと、どちらかを捨てさせることになる
- 講演の中に埋める動画に、サウンドトラックや宣伝臭いものは使うな（Anderson、要約のみ。[[web-embed-ted-anderson-yc-demo-day]]）。ただし Apple の基調講演は CM を流していた（[[web-embed-evangelist-2006-apple-keynote]]）
- 展示の映像で実際に見られるのは、上映時間の半分未満（上映 2 分で 53 秒）。ナレーション無しのループが一番人を止めた。どこから見ても分かる作りが要る（[[web-embed-serrell-smithsonian-museum-video]]）
- 一番近い外の型は Cell の Figure360（図 1 枚・2 分・「図にある要素だけ」・「2 秒以上画面が変わらない間を作らない」）（[[web-nonscreen-cell-iop-nejm-video-abstract-guides]]）
- 3 つの発表ソフトに共通して通る形は H.264＋AAC の .mp4・1080p。ループを公式に書いているのは Keynote だけ（[[checks-and-finishing]]）
- 一本作る手順は [[ready-to-start-2026-11-10]] の 3。段階表示の図の道具（Mermaid の step、D2 の steps、excalidraw-animate）は [[expression-means]]
- 流しっぱなしでは読み違いを話し手がその場で補えないので、読み辞書の版管理が効く（[[web-means-voice-voicevox-aivisspeech-user-dictionary]]）
- THINKLET の動画（ずんだもんのナレーション入り）は、VIS 2015 の規則なら、話し手が上に乗るときは不可。話し手が黙っていたなら矛盾しない（未確認のまま）
