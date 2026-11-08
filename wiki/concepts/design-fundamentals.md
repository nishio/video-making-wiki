---
type: concept
summary: 西尾の語「普遍的なデザイン知識」について、モーション（原則・イージング・UI の指針・閃光と前庭障害の基準）、動画の文字（字幕の速さと大きさ・セーフエリア・動く文字）、構図・色・情報デザイン、編集の文法、物語の構造、表現としての音を、文献と西尾の経験で並べたページ。動画にそのまま当てはまる数値は閃光の基準と字幕の規則くらいで、UI の duration や Tufte の原則は前提（UI の遷移、印刷物の読者）を確かめて移す必要がある
video_types: [any]
sources:
  - web-motion-*.md（7 ページ）
  - web-type-*.md（7 ページ）
  - web-layout-*.md（8 ページ）
  - web-mayer-multimedia-principles.md
  - web-tversky-2002-animation-can-it-facilitate.md
  - experience-lessons-2026-11.md
---

# 普遍的なデザイン知識

西尾の指示「普遍的なデザイン知識」から。型ごとの話は [[promo]]・[[talk]]・[[embed]]、音の量（ラウドネス・ダッキング）は [[narration-bgm-sound]]。

**読み方の注意**: この領域の古典の多くは本で、本文を読めていない（Thomas & Johnston、Tufte、Murch、Chion、Duarte）。読めたのが原典の論文・著者の講演やインタビュー・抜粋・書評のどれかは各ページに書いてある。

## モーション

- Lasseter（SIGGRAPH '87、原典）の要点は Timing（「足りるだけ、それ以上でなく」）と Staging（一度に一つ。静かな場面では動くものに、忙しい場面では止まったものに目が行く）（[[web-motion-lasseter-1987-principles-of-traditional-animation]]）
- Penner（2002）は動きを「時刻から位置を返す関数」として扱い、等速は機械的に見え、4 乗以上の曲線は「この世のものでない」感じになると書く。「開始点から走らせずに任意の時刻へ飛べる」は、経験の `renderFrame(f)` と同じ考え方（[[web-motion-penner-easing-css-easing]]、[[exp-html-capture-pipeline]]）
- UI の指針の duration（Carbon 70〜700ms、M3 50〜1000ms）は UI の状態遷移の値で、動画の場面の長さの根拠にはならない。移せるのは「距離・面積が大きいほど長く」「入るときは減速、出るときは加速」「色・不透明度は行き過ぎさせない」という向きだけ（担当の推測）（[[web-motion-material-3-easing-duration]]、[[web-motion-ibm-design-language-carbon-motion]]）
- IBM は productive と expressive を分け、「デザインが込み入るほど動きは小さく、簡素なほど大きく」と書く（IBM の経験則で根拠は示していない）。経験の「動きの評価が promo と talk で逆」（[[three-video-types]]）に一つの説明を与える
- **全画面の拡大・パン・揺れは避ける側、フェードは比較的安全側**で、Apple の HIG（Reduce Motion で移動をフェードに置き換える）、WCAG 2.3.3、Val Head（前庭障害の引き金は画面に対する動きの大きさ・視差・移る距離）が一致する（[[web-motion-apple-hig-motion]]、[[web-motion-wcag-2-2-motion-flash-vestibular]]）。[[exp-qualia-video]] の「全画面の drift は気持ち悪い」と同じ向き

### 閃光の基準（動画にそのまま当てはまる）

- ITU-R BT.1702-3（2023）: 画面の 25% を超える面積で、1 秒に 3 回を超える閃光（明暗の往復で 1 回）を続けない。閃光の先端の間隔が 360ms（50Hz 圏）／334ms（60Hz 圏）以上なら可。速いカットも閃光を生むなら同じ扱い。基準内でも 5 秒を超える連続は危険かもしれない（[[web-motion-itu-r-bt1702-ofcom-nhk-minpo-flash-guidelines]]）
- NHK・民放連のガイドライン（2006 改訂）は、輝度変化が 20% を超える場面転換を原則 1 秒 3 回までとしていて、速いカットについて ITU より厳しく読める（同）
- **経験への当てはめ（要確認）**: 般若心経アゲアゲ版の R3（176BPM、1 拍 ≒ 341ms、30fps）は、拍ごとに光るなら 50Hz 圏の目安を満たさず、コマに丸めると 60Hz 圏の目安も下回りうる。否定区間の叩きつけ（画面が青く光る）は約 256ms 間隔の箇所がある。レビューは R1（128BPM）だけで回していて、R3 で閃光を確かめた記録は無い。青は相対輝度が低いので閾値に届かない可能性もある。**実フレームで測る必要がある**（同、[[exp-sutra-hype-editions]]）。Polis の OP 様式は 1 拍 1 カット（128BPM）ならどの基準でも収まるが、8 分音符で刻むと NHK・民放連の場面転換の基準を超える（[[exp-polis-magi-op]]）

## 動画の文字

| 項目 | 文献の数字 | 出典 |
|---|---|---|
| 日本語の字幕 | 1 行 13 字、2 行まで、1 秒 4 字、最短 0.5 秒・最長 7 秒（Netflix。日本語版の最終更新 2025-12-19）。SDH は 1 行 16 字・1 秒 7 字 | [[web-type-netflix-timed-text-style-guide]] |
| 英語の字幕 | 160〜180 WPM、16:9 で 2 行・9:16 で 3 行まで、行の高さは 16:9 で画面の 7〜8%・9:16 で 3.9〜4.5%（BBC v1.2.5） | [[web-type-bbc-subtitle-guidelines]] |
| 字幕付きの TV CM（日本） | 1 枚 2 秒以上、冒頭と終わりの 1 秒は出さない、1 画面 2 行 30 字、15 秒 CM で 6 枚が限界（日本広告業協会の資料、2014） | [[web-type-jaaa-captioned-tv-cm-guidelines]] |
| 字幕の速さと理解 | 割れている。Szarkowska ら 2018（74 人、12・16・20 字/秒）では理解は変わらず、Kruger ら 2022（12・20・28 字/秒、抄録のみ）では速いほど下がった。上限の目安はどちらも 20 字/秒あたり。日本語の研究は見つからず | [[web-type-szarkowska-2018-kruger-2022-subtitle-speed]] |
| セーフエリア | EBU R 95: 動きは各辺 3.5%、文字は各辺 5%。SNS の safe zone は UI に覆われる範囲で、下と右に偏り、公式は画像・テンプレートで示す | [[web-type-ebu-r95-google-tiktok-safe-zones]] |
| 大きさとコントラスト | Apple は iOS の文字の最小 11pt。16:9 の 1080p をスマホの縦持ちで見ると 54px 未満の文字は 11pt より小さく見える（担当の計算）。WCAG 1.4.3 は 4.5:1（大きい文字 3:1）。動画に焼き込んだ文字に当たるかは W3C で割れたまま | [[web-type-apple-hig-wcag-text-size-contrast]] |
| 動く文字 | Lee ら 2002: 大きさ＝声量、震え＝高い覚醒。「注意を奪いすぎる」「文の意味は上書きできない」 | [[web-type-lee-forlizzi-hudson-kinetic-typography]] |

- 経験への当てはめ: Gyazo の 0.5 秒ごとの叩き込みは Netflix の最短表示と同じ長さで、山の文字「43分24秒」を 0.5 秒だけ出したなら 8 字/秒（日本語字幕の上限の 2 倍）。各文字が何秒残ったかは記録に無い（[[exp-gyazo-resumption-video]]）。Polis の 1 拍 1 カット（約 0.47 秒）は最短 0.5 秒を下回る。経験の多くは文字の px 値と叩き込み 1 回の字数が記録に無く、範囲に収まったかはほとんど確かめられなかった
- TikTok の「毎秒 5〜10 語」（[[web-tiktok-creative-best-practices]]）は、1 語 5 字の換算で 25〜50 字/秒になり、Kruger らが速すぎるとした 28 字/秒以上に当たる（担当の換算）

## 構図・色・情報デザイン

- 飾りが効くか害になるかは「その絵がデータを描いているか」で分かれる。Bateman ら 2010（CHI、20 人）の Holmes の絵や、Haroz ら 2015 の ISOTYPE の絵記号は損が無いか、2〜3 週間後の想起を上げた。無関係な背景の絵は記憶と読みの両方を妨げた。ただし Bateman は見る時間を制限していない（[[web-layout-bateman-2010-useful-junk]]、[[web-layout-tufte-data-ink-chartjunk]]）。第 1 回の coherence（[[web-mayer-multimedia-principles]]）・装飾的アニメ ≈0（[[web-berney-betrancourt-2016-animation-meta-analysis]]）と同じ線で、「データを描く飾り」は別扱い
- 色だけで情報を区別しない（CUD の 3+1 原則、WCAG 1.4.1）。形・線種・直接のラベルを重ね、明るさの差を取る。よく引かれる色覚バリアフリーの配色のうち、橙・空色・黄は白地で 3:1 に届かず、黒地では青だけが文字の 4.5:1 に届かない（4.05。担当の計算、RGB は二次の文献の値）（[[web-layout-okabe-ito-cud-wcag-contrast]]）
- 三分割は Reynolds 自身が「規則でなく指針」と書き、Amirshahi ら 2014 の実測でも高評価の写真や絵画でほとんど目立たなかった。Duarte の glance test は 3 秒（[[web-layout-presentation-zen-rule-of-thirds]]）

## 編集の文法

- Murch の Rule of Six（感情・物語・リズム・視線・2D の平面・3D の空間）は、本人の説明では「下から手放す」。本人の口から確かめられた数値は感情の 51% だけで、2D の値は 4% と 5% の両方が出回っている。カット点は終わりのコマを実時間で流して選び、「スクラブは音痴を生む」と言う（[[web-layout-murch-in-the-blink-of-an-eye]]）
- Smith 2012 の AToCC: 連続して見えるのは注意が連続しているからで、動き・視線・画面外の音・話者交代・リズムで注意を移してから切るとカットに気づかれにくい。match-action のカットは 3 分の 1 が見落とされた。Cutting らはハリウッド映画の平均ショット長が 1930〜40 年代の約 10 秒から 2000 年以降 4 秒未満になったと報告（[[web-layout-smith-2012-cutting-2011-film-attention]]）
- 経験との違い: 西尾の方式は場面の切り替えを 120BPM の小節頭に固定した（[[exp-html-capture-pipeline]]）。Murch の「実時間で流して選ぶ」と逆向き。Polis の参照の平均 1.07 秒/カットは現代映画の平均（4 秒未満）よりはるかに短く、v1 の 4.5 秒は映画の平均程度だった。「しょぼい」は参照した様式とのずれだった（[[exp-polis-magi-op]]）

## 物語の構造

- Duarte の sparkline: what is と what could be を往復し、主人公は聴衆、最後に「新しい至福」を描く（TEDx の書き起こし）。Story Spine（Kenn Adams 本人が起源を語った NPR 2026 の書き起こし）、ABT（And, But, Therefore。Olson、書評経由）（[[web-layout-duarte-sparkline-story-spine-abt]]）
- 経験との違い: 西尾の LT は「新概念を終盤に入れない」として、大きな絵で終える案を採らなかった（[[exp-lt-20260909]]）。冒頭の問いを最後に回収する形（[[exp-words-as-public-goods-video]]）は ABT の But → Therefore に近い（推測）

## 表現としての音

- Chion の synchresis（同時に鳴った音と映像の心の中での融合）と added value（音が作った意味を、観客は映像から来たと感じる）。Murch の「音と映像のずれを伸ばすと次元が出る、伸ばしすぎると崩れる」（NYT 2000）（[[web-layout-chion-audio-vision-murch-sound]]）
- 120BPM の小節頭で合成音を当てる作り（[[exp-html-capture-pipeline]]）と、「動きが大事な版は音つきで評価する」経験の理論上の名前になる
- 学習研究とは食い違う。Moreno & Mayer（[[web-moreno-mayer-2000-coherence-sounds]]）は学習では余計な音が損とする。劇映画の論は表現の効果、学習研究は保持・転移を見ている

## 経験の教訓（[[experience-lessons-2026-11]]）と照らす

| 教訓 | 文献 | 関係 |
|---|---|---|
| 図形と文字だけで描けば権利の確認が要らない | — | 文献はこの点を扱わない |
| 飾りより証拠に面積を | Tufte の data-ink、Bateman・Haroz の「データを描く飾りは別」 | 同じ向き。ただし「データを描く絵」は飾りではなく証拠の側 |
| 様式は実物を見てカットの密度を測る | Cutting の平均ショット長の測定 | 同じ方法。様式ごとに平均がまったく違う |
| 映像と音で同じ時刻表、小節頭で切り替え | Chion の synchresis／Murch の実時間で選ぶ | 前者とは一致、後者とは逆向き |
| 変化が止まるとテンションが下がる（promo） | Lasseter の Staging、IBM の「簡素なほど動きは大きく」、Tufte の「設計は最小」 | promo では一致、Tufte（印刷物の読者）とは前提が違う |
| 現在位置を橙だけで強調（[[exp-sutra-sync-subtitles]]） | WCAG 1.4.1、CUD の原則 2 | 色だけの強調に当たりうる。色の値が記録に無く未計算 |

## Open Questions

- 般若心経アゲアゲ版 R3 と、Polis の OP 様式で予定の「回想フラッシュ」の閃光を、実フレームで測る（1 秒の窓で、画面の 25% 超の領域の明暗の往復を数える）
- 字幕の速さの研究に日本語が無い。Netflix の 1 秒 4 字は規則で、測った値ではない
- 「跳ねを避ける」（IBM）と、Gyazo の叩き込みや Polis v4 の「ばね」が逆向き。IBM の様式の選択か、promo では跳ねが効くのか
- 流しっぱなしの embed では見る時間が動画に決められる。Bateman の「データを描く飾りは損が無い」は見る時間を制限しない条件なので、そのまま移せない
