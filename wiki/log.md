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

## [2026-11-09 02:35] ingest | 取りこぼしの経験 1 ページ: THINKLET の読書支援のデモ動画

- 西尾の指摘「Thinkletの読書支援ツールの解説の動画を作った話は？」で最初の抽出の取りこぼしが分かり、Mac の Claude が書いた sources/exp-thinklet-reading-demo-video.md をそのまま置いた（~/handoffs-from-mac/2026-11-09-video-making-wiki/ から）
- concepts/three-video-types.md の「経験の内訳」の embed の行に追記（LT に組み込む候補、実際に流したかは未確認）
- concepts/embed.md に Updates: ナレーション入りの動画を発表で流すときの衝突、待ち時間を説明に変えた形、「ライブのデモを録画で置き換える」用途

## [2026-11-09 13:30] ingest | 西尾の回答（embed は流しっぱなし）と chat の補足、時系列、Opus 5.5 期の外の知見 2 本

- Mac の Claude が書いた（CyEC2 のセッションの待機中に Mac の clone で編集して push）
- 西尾の回答: embed は「流しっぱなしの前提」、THINKLET の動画も「流しっぱなし」→ embed・three-video-types・survey summary の Updates。サーベイの「話し手が時間を握る（Rosling 型）」は西尾の embed の前提ではない
- 西尾の chat の補足（YouTube 5 本）を origin の Updates に原文で。残テは 2026-10-01 に公開済みで、exp-sutra-songs-on-music の「未公開」は古かった。Gyazo 47 秒版は本人評価「Jevの凄さのアピール重視で技術の詳細を伝えるには適切ではない」
- 新規: exp-timeline-2026（Opus 5.5 公開 9/22 前後の時系列）、web-movez-opus-motion-design-course・web-taelin-bend-nge-feedback（tweet-memo の要約から。元投稿は未読）


## [2026-11-09 04:30] ingest | 第 2 回サーベイ（web- 53 ページ）と横断の concept 3 ページ

- 西尾の指示「特にOpus5.5が出たあとのもの、bytedanceなどで動画を丸ごと生成する系のもの、普遍的なデザイン知識、の3領域」で、8 つの担当に分けて並行で読んだ。途中で B の問いが「作品のプロモーション的な動画を作る上での最良の方法」に直され、丸ごと生成の 2 担当の範囲を絞り、作品紹介の作法の担当を足した
- A（Opus 5.5 以後）: web-opus-* 8、web-opus2-* 7。B（作品の promo）: web-promo2-* 8、web-genvid-* 3、web-genvid2-* 5。C（デザイン）: web-motion-* 7、web-type-* 7、web-layout-* 8
- 新規 concepts: after-opus55、work-promotion-video、design-fundamentals。Updates: promo、talk、embed、video-tools-comparison、narration-bgm-sound、three-video-types
- 経験ページへの Updates: exp-sutra-hype-editions と exp-polis-magi-op（閃光の基準。R3 は要確認）、exp-galleria-local-video-generation（価格・VRAM の二次情報が古い）、exp-html-capture-pipeline（Shorts 3 分、X の 40fps）
- 訂正: web-movez-opus-motion-design-course（Thariq の言葉の範囲、brief contagion の出どころ、Substack 版で本文が読める）、web-opus2-awesome-claude-5-5-videos

## [2026-11-09 04:35] filing-back | 第 2 回サーベイのまとめ

- analyses/survey-2026-11-round2-summary.md: 3 領域で分かったこと、三つの型（embed は流しっぱなし）への含意、食い違い 11 件、次にすること（閃光の検査が最優先）、読めなかったもの

## [2026-11-09 04:40] lint | 機械的 lint のみ: 130 ページ、重複 0・孤立 0・壊れたリンク 0・index 未登録 0・フロントマター不備 0。意味的 lint は未実施

## [2026-11-09 14:40] schema | 目的を西尾の言葉で書いた

- 西尾: 「目的: 作るための手段を調査サーベイし、今後の表現手段を増やすこと」。CLAUDE.md のテーマと index の冒頭、llm-wiki の wikis.yaml の purpose に入れ、起点の Updates に記録
- GitHub の正本の「作成待ち」を消した（西尾が作成済み）
