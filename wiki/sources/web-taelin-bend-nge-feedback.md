---
type: source
summary: Victor Taelin が Bend の宣伝動画をエヴァンゲリオン OP の様式で Opus 5.5 のエージェントに作らせたときの、人間側の指示とフィードバックだけを並べた gist（2026-09-28）。3 体を並走させて部品ごとに人が勝者を選び、「アイデアは共有、コードは共有しない」
video_types: [promo]
sources:
  - Victor Taelin（@VictorTaelin）gist https://gist.github.com/VictorTaelin/b788de1da66ddfc270a35e94293cae19（作成 2026-09-28、最終更新 09-29）
  - tweet-memo sources/taelin-bend-nge-video-feedback.md（この wiki ではその要約から書いた）
---

# Taelin「Bend をエヴァ OP 様式で」— 人間側のフィードバックログ（2026-09-28）

- 著者: Victor Taelin（Bend / HigherOrderCO）。gist 1 ファイル・約 600 行、**人間側の発言だけ**が 18 ブロック。エージェントの出力と完成動画は入っていない
- **読み方の注意**: この wiki では gist を開いていない。tweet-memo の要約（`sources/taelin-bend-nge-video-feedback.md`）から書いた

## 流れ（tweet-memo の要約）

1. 「Bend を紹介するワクワクする動画を」→ 映像は綺麗だが、友人 5 人（うち開発者 2 人）に見せて誰もついてこられなかった
2. エヴァ OP の様式に切り替えた（原曲の OP を参照に指定）。冒頭は図形がゆっくり組み上がるだけ、説明は後から部分的に、点と点は見る人につながせる
3. 逆の失敗: 文字が少なすぎて何も伝わらない。ここで配置の原則が出る — "you must throw these high impact slides with big white titles around the animations that are relevant to them, to help the reader connect the dots." アニメーションが心象を作り、短いタイトルが「何の話か」の手がかりになる
4. Opus 5.5 のエージェント A・B・C を並走させ、Taelin が批評役になって、導入は B、盤面は A、ロゴは C のように**部品ごとに勝者を選んだ**
5. B が C のコードを持ち込んで見た目が崩れたとき、"the IDEAS are shared. NEVER to copy the other agent's code verbatim." と決めた。理由は visual identity を失うから
6. 最後は B を採用し、拍ごとに証明の戦術を 1 つずつ見せる、赤から青の空への遷移を滑らかにする、などを詰めた

フィードバックの粒度の例: タイトルは全部大文字（NGE がそうだから）、「PROOF.」の句点は不可、字形は細く、関連の薄い専門用語も関連スライドの近くに置けば効く、「動画関係のものを repo に足すな。頼んでいない bureaucracy に時間を使うな」

## この wiki の経験との突合

- **同じ週に同じ様式**: 西尾も 9/29〜30 に、エヴァ OP に重ねて Polis・Plurality を伝える動画を作った（[[exp-polis-magi-op]]）
- **収束のさせ方が違う**: 西尾の側は 1 体で v1 → v4 を直列に直した。Taelin は 3 体を並走させ、人間が部品単位で選んだ。並走させるなら「アイデアは共有、コードは共有しない」が要る、とこのログから読める（tweet-memo）
- **文字量の往復はどちらも通った**: 多すぎ → 少なすぎ。抜け出す鍵は量でなく配置（タイトルを関連するアニメのそばに置く）だった（tweet-memo）
- 人間の目視は 18 ブロック分要った。[[web-movez-opus-motion-design-course]] の「一回目は mid → 参照と自己批評で直る」の、批評を人間がやった大きい版

## Open Questions

- 部品ごとに選んだものを 1 体に統合させるとき、アイデアだけを移すと劣化しうる（B のタイトルが「より磨かれたが悪くなった」）。どう防ぐか（tweet-memo）
