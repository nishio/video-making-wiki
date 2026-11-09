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

## [2026-11-09 01:21] ingest | 西尾の回答（embed は流しっぱなし）と chat の補足、時系列、Opus 5.5 期の外の知見 2 本

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

## [2026-11-09 07:18] schema | 目的を西尾の言葉で書いた

- 西尾: 「目的: 作るための手段を調査サーベイし、今後の表現手段を増やすこと」。CLAUDE.md のテーマと index の冒頭、llm-wiki の wikis.yaml の purpose に入れ、起点の Updates に記録
- GitHub の正本の「作成待ち」を消した（西尾が作成済み）

## [2026-11-09 07:48] ingest | origin に西尾の言葉「最終的に「動画の作り方の解説動画」を作るか」を記録（成果物の候補。未決定）

## [2026-11-09 08:00] ingest | 第 3 回サーベイ: web- 83 ページ（means 48: capture 8・diagram 8・3d 7・voice 9・sound/font 8・critic 8、check 18: flash 3・subs 4・ja 2・loudness 2・color 3・spec 4、embed 5・nonscreen 4、rights 8）

- 西尾の目的「作るための手段を調査サーベイし、今後の表現手段を増やすこと」と指示「明日からすぐ具体的に着手が可能な水準で」に沿う。CyEC2 では何も入れず動かさず、手順はすべて未検証（galleria で確かめる）
- 10 の担当（general-purpose の subagent）で並行に読み、まとめ役が index・concept・Updates を書いた

## [2026-11-09 08:05] filing-back | concepts/expression-means、concepts/checks-and-finishing、analyses/ready-to-start-2026-11-10、analyses/survey-2026-11-round3-summary

- ready-to-start: 明日から着手できること 11 項目（閃光の検査・フォントの同梱・流しっぱなしの embed・作品の promo の収録・仕上げの検査・字幕・読み辞書・批評役・ACE-Step・GSAP/three.js・確認表と C2PA）、各項目に解説動画の材料、最後に「動画の作り方の解説動画」の型・構成案・西尾が決めること（案であって決定ではない）
- Updates: concepts（embed・promo・talk・work-promotion-video・design-fundamentals・video-tools-comparison・narration-bgm-sound・after-opus55）、exp（sutra-hype-editions・html-capture-pipeline・galleria-tts-and-singing・polis-magi-op・forest-misc-video-notes・democracy-river-video）、web（promo2-vhs-shot-scraper・after-effects-lottie-rive）
- 経験の古い事実: ローカルの楽曲モデル（ACE-Step 1.5 が既にあった）、Suno の規約の版、loudnorm が 1 パス（dynamic）、gpt-4o-mini-tts の終了、包括契約の範囲の書き方

## [2026-11-09 08:10] lint | 第 3 回の後の lint。217 ページ、重複 0・孤立 0・壊れたリンク 0・未登録 0・フロントマター不備 0

## [2026-11-09 08:46] decision | 「動画の作り方の解説動画」を作る（西尾の決定）

- 西尾: 公開済みの動画の閃光の検査は今やらない。解説動画が重要。一般向け（AI を日常的に使いこなす技術力のある人、最初は未踏ジュニア）、2026-11 時点のノウハウを「三つの型」と「型ごとのノウハウ」で、声は TTS、YouTube で一般公開
- origin と ready-to-start の Updates に記録。台本の草稿は Mac の ~/video-making-explainer で作る

## [2026-11-09 09:01] filing-back | analyses/explainer-script-factcheck-2026-11: 解説動画の台本草稿の 15 の主張を原典で確かめた

- そのまま可 1（Claude は動画を直接は出せない）、言い方を直す 14、削る 0。直した文の案付き。台本（Mac の ~/video-making-explainer）は直していない
- 3 つの担当（配信先の規則・AI のモデルの docs・研究）が原典を開き、項目 15 はまとめ役が wiki の範囲で確かめた
- wiki のずれを Updates に: promo（最初の 3 秒 → 3〜5 秒）、web-digiday（YouTube のホームは音なし）、web-promo2-apple（2.3.4 はプレビュー動画だけ、2.3.14）、web-opus-hculap・howseen（hold の例外）、after-opus55（聞けないは API の条件つき）、design-fundamentals（拍の同期の研究）、web-motion-wcag（版の日付、英国の基準）、web-check-ja-speech-rate-mora（石本の要旨と本文の食い違い）、web-muller（d の中身）、web-embed-ladner（"Sometimes it is good to"）

## [2026-11-09 10:55] ingest | 動画編集を AI にさせる方法のサーベイ（web-edit-* 22 ページ）と concepts/ai-editing

- 西尾の言葉「編集作業自体をAIにさせてもいいよね」「動画編集をAIにさせる方法に関するサーベイが足りてないならCyEC2にやらせといて」から。4 つの担当: text（Descript・Premiere・CapCut・Resolve・FCP/Vrew、5）、auto（auto-editor・PySceneDetect ほか・OpusClip・Vizard/Klap/Munch・切り抜きの OSS・AutoClip の観察、6）、agent（OTIO/EDL/FCPXML・MoviePy/ffmpeg・Resolve/Premiere の API・MCP サーバー・video-use などの実例・Gemini の場面選び、6）、research（文字起こしで編集する研究の系譜・LAVE/ExpressEdit・EditDuet ほか・HIVE/AVT・Timeline-Bench/MEDit-Bench、5）
- 横断: concepts/ai-editing（骨組みは「時刻付きの文字起こしを正、LLM は区間を選ぶ」。ペース・筋・ショット選びは 2026 年秋のベンチマークでも人に及ばない。日本語の文字起こし編集が公式に動くのは Premiere・Resolve Studio・Vrew）
- Updates: work-promotion-video（西尾の言葉、実物の収録が正本・編集は人でも AI でも）、expression-means、ready-to-start-2026-11-10（12〜14 の候補）、checks-and-finishing、video-tools-comparison、exp-shortmovie-draft-generator、exp-thinklet-reading-demo-video
- CyEC2 では何も入れず動かしていない。手順はすべて未検証（galleria で確かめる）。Mac の compose.py はこの機械に無く読んでいない

## [2026-11-09 10:57] lint | 241 ページ、重複・孤立・壊れたリンク・未登録・フロントマター不備すべて 0

## [2026-11-09 19:10] file back | tsugigami の広告動画のメイキング（Mac の grasp-nishio のセッションから）

- 新規 sources/exp-tsugigami-promo.md: 起点の西尾の発言、できあがりの場面表、作り（実アプリの録画＋Grok Imagine の人物動画の合成）、v1〜v6 の西尾の指摘と直し、分かったこと（自動操作の後の状態確認、場面のつなぎ、四隅の追跡、画面の向き、モデルが描いた線をインクに、冒頭 3 秒）、数字、落とし穴、YouTube の開示
- Updates: concepts/work-promotion-video（暫定の答えの形の実例）、sources/exp-galleria-local-video-generation（ホスト型 Grok Imagine の i2v の初使用）
- 公開: https://youtube.com/shorts/1qKsNrwIxCk

## [2026-11-09 19:14] filing-back | 解説動画「動画の作り方 2026年11月」とプロセス動画の制作・公開（Mac の grasp-nishio のセッションから）

- 新規 sources/exp-explainer-video-2026-11.md: 起点の西尾の発言、作り（ナレーションの長さが時刻表、引用は ffmpeg の overlay、make.sh）、三つの声の聞き比べ、AivisSpeech の核の指定で直した語、指定が効かなかったエフエフエムペグ、F0 の測定が半分の高さを拾った誤り、レビューの受け取り方（Drive・ドキュメントのコメント・db つきの非公開ページ）、プロセス動画への西尾の指摘
- Updates: sources/exp-galleria-tts-and-singing（Open Questions の「AivisSpeech と耳で比べた記録が無い」への答え、核の指定の挙動）
- 公開: 本編 https://youtu.be/IDkRFwiFXFI 。プロセス動画の URL は未記録

## [2026-11-09 19:25] file back | exp-tsugigami-promo に時系列（解説動画の材料）

- 西尾「解説動画を作る上で時系列の出来事は記録しておきたい」。会話記録の発言時刻と作業場のファイル時刻から、10:15 の引き継ぎから 18:28 の YouTube 投稿までの表を足した
- 西尾の問い「まずこのプロジェクトのソースコードを見て強みの案を出したんだっけ？」への答えも表に: ソースコードは読んでいない。README・開発 wiki・西尾の会話の raw・LOG・書き出し JSON を読んで 5 つ出した

## [2026-11-09 20:50] file back | exp-tsugigami-promo にメイキングの解説動画の公開と直し

- https://youtu.be/aXGEaLMI7Fs 。西尾の直し（読み、表示の時刻、見本の出し分け、「美人にして」を隠す）と、語の時刻の測り方を Updates に

## [2026-11-09 21:41] filing-back | ai-editing に Premiere 27 への更新と契約の確認

- Updates: 西尾の Mac の Premiere を 25.3.0 から 27.0.0 に更新（西尾が Creative Cloud で。2025 は消えた）。契約は Premiere 単体の年間・月払いで続いている見込み（2026-09-02 の更新の通知メール、解約のメールなし）。OTIO で Premiere に渡す道が Mac で試せるようになった（27 で読めるかは未検証）。OTIO の平易な説明
