# Log

## [2026-11-09 01:10] ingest | 起点と、MacBook・galleria の制作経験 24 ページ

- 西尾の依頼（未踏ジュニアの文脈で安川さんと話し、解説動画の知識は有用そうとなった）で wiki を作った。起点は sources/origin-2026-11-09.md、CLAUDE.md に動画の型（promo/talk/embed）と「置かないもの」を足した
- MacBook の Claude（grasp-nishio のセッション）が 5 つの担当に分けて抽出: Mac の HTML capture 系 5 ページ、sutra-videos 5、解説・LT・切り抜き・森の散在記録 4、galleria-wiki（Mac の複製）5、galleria の制作ディレクトリ（ssh で読むだけ）4。qualia の重複 2 ページは外し、そちらにだけあった点を exp-qualia-video に統合
- 横断の整理: concepts/three-video-types.md（経験の範囲では型を分けたのは流す場所。embed の経験は無い）、analyses/experience-lessons-2026-11.md
- 除外: 私生活・宗教実践の場所、galleria の私的領域と成人向けの実験、第三者の名前と権利者、接続先、版権曲の中身
- 次: CyEC2 の Claude Code でネット上の知見をサーベイ（sources/web-*）

## [2026-11-09 02:10] ingest | ネット上の知見のサーベイ（web- 37 ページ）と横断の concept 5 ページ

- 起点の問い 6 つを 6 つの担当（学習研究・解説の実務・embed と概念アニメ・道具と LLM・SNS の promo・音）に分けて並行で読んだ。各担当は原典の本文を curl/pdftotext で読み、数値と条件は原文で確かめた。読めなかった原典は各ページに明記
- 新規 sources: web- 37 ページ（研究 6、実務 6、embed 7、道具 7、promo 6、音 5）
- 新規 concepts: promo、talk、embed（西尾の語の型ごと）、video-tools-comparison、narration-bgm-sound。three-video-types に Updates（軸ごとの表、「誰が時間を握るか」の軸）
- 担当同士のファイル名の衝突で web-3blue1brown-exposition-advice が一時消えたので、担当の作業記録から復元し、web-3blue1brown-explainer-advice と相互に Updates で繋いだ
- web-motion-canvas の url を motion-canvas.io（ハイフンあり）に直した。ハイフンなしは別会社のサイト
- 経験ページの古い事実を見つけた: exp-html-capture-pipeline の「縦長 60 秒以内ならショート」は 2024-10 以降 3 分以内。exp- 側への反映はまだ

## [2026-11-09 02:15] filing-back | サーベイのまとめ

- analyses/survey-2026-11-summary.md: 何が分かったか 10 項目、三つの型の違いの暫定の答え（視聴の場・誰が時間を握るか・音が主か・測るもの）、経験と文献の食い違い 10 件、次に調べること

## [2026-11-09 02:20] lint | 機械的 lint のみ: 69 ページ、孤立 0・壊れたリンク 0・index 未登録 0（サーベイのまとめの孤立を three-video-types から繋いで解消）。意味的 lint は未実施
