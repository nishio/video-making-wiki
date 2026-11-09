---
type: source
summary: 切り抜きの OSS AutoClip の作者たちが、公開の短尺 158 本を同じアカウントの中で比べた観察の報告（2026-10-09、査読なし）。「何が・誰が映っているか」と「どこから始まるか」が、カットの速さ・ズーム・装飾字幕・効果音・色・テンプレートより再生数をよく分けた、と書く。冒頭はおよそ 1.5 秒以内に顔か見える出来事、単独で意味が通る一文、既定は 90 秒以下。自分たちのアカウントのデータはまだなく、道具の作り手が書いている
video_types: [promo]
url: https://github.com/zhouxiaoka/autoclip/blob/main/docs/research/2026-10-what-drives-views/article-en.md
author: AutoClip team（Charlie Zhou ほか）
published: 2026-10-09
retrieved: 2026-11-09
sources:
  - https://github.com/zhouxiaoka/autoclip/blob/main/docs/research/2026-10-what-drives-views/article-en.md（AutoClip Research Note #1）
---

# 「Pick the moment, not the effect」— 158 本の切り抜きの観察（AutoClip、2026-10）

## 何の文献か

- 切り抜きの OSS（[[web-edit-auto-openshorts-ai-youtube-shorts-generator-supoclip-autoclip]] の AutoClip）の作者たちが repo に置いた調査のノート。**査読なし、道具の作り手が書いた**。本人たちも「We build the tool we're writing about. Read our implications with that in mind」と限界の節に書く
- 標本: 公開の短尺 **158 本**、6 つの群（インタビュー・ポッドキャスト 57、ニュース＋ドキュメンタリー 22、バラエティ・映画 26、ゲーム・配信 25、Vlog・雑誌 28）。X と YouTube Shorts。指標は **2026-10-09 の一時点の公開の数字**（X の impressions / views、YouTube の views）
- 方法の決まり: 比べるのは**同じアカウントの中だけ**（同じ動画・同じ文面でもアカウントで 141,835 対 386 の impressions、約 367 倍になった例を挙げる）、投稿から 12 時間以上、いいね率の低すぎる投稿は外す、「上位がやっていること」は慣行で、上位と下位で違うときだけ効果と呼ぶ。根拠の強さに High（3 アカウント以上で一致）・Medium・Low の札を付ける
- 測り方: 尺とカット数は ffprobe / ffmpeg の場面検出、音量は ebur128、間は silencedetect（-45 dB、0.25 秒）。ズームはコマで確かめたものだけ
- 統計の検定はない。比べた組は少数（アカウントあたり 2〜4 本）

## 書いてあること

- **TL;DR（原文）**:「One pattern held across groups: **who or what is in the clip, and where the clip starts,** predicted views far better than how it was edited.」「Cut rate, zooms, stylised captions (花字), stickers, sound effects, grading and templates showed up in hits and flops alike.」「We have **no data from our own account yet**」
- **Finding 1（High）同じ型で結果が大きく違う**: GQ の同じセットの「10 Essentials」で 2,823,259 回と 6,261 回（330〜450 倍）。違いはゲストの知名度と話題。HasanAbi の同じテンプレートで 8〜12 倍
- **Finding 2（Medium）始まり: 約 1.5 秒以内に顔か見える出来事**: Veritasium は 0 コマ目に実演・動作で始まる短尺が 25.8K〜200K 回、話す顔・記録映像で始まるものが 3.3K〜6.3K 回。後者は文の切れ目でズーム（1.27 倍）していたが救わなかった（交絡: 後者の 2 本は抽象的な話題の連作）。バラエティでは上位 8 本中 7 本が 1.6 秒以内に表情のある顔、下位は 6 本中 2 本。「The first 1.5 seconds are mostly decided **when the in-point is chosen**, not in the edit. An editor can't add a reaction that isn't in the footage.」
- **Finding 3（Low–Medium）題は「人＋具体的な行為か数字」**: スローガン型の題より、人の名前と何をしたかの題が伸びた例が複数。再生の少ない切り抜きの方がいいね率が高いことが多く、「ファンの外に出なかった」と読む
- **Finding 4（Low–Medium）単独で意味が通る一文**: 上位は前提なしで通じる一行（数字・対比・一文の答え）を持つ。「One of the first experiments that was done…」のように前提の要る始まりは下位。「This is a **selection-layer** signal. You can't add it in the edit.」
- **Finding 5（Medium）既定は短く、例外あり**: AJ+ は 80 秒以下の中央値 31,664、81〜135 秒 17,169、135 秒超 8,254。例外は「continuous argument or continuous laughter」で 60〜180 秒が効く。既定は 90 秒以下
- **Finding 6（「一貫した効果なし」について High）包装は技芸で、当たりにも外れにもある**: カット率は上位で 0〜51 回/分。インタビュー 44 本で 10 万 impressions 以上の群の中央値 3.8 回/分、1,000 未満の群 4.5。ズーム・装飾字幕・効果音の密度・音量（配信の切り抜きで -8.4〜-31.2 LUFS、上下どちらが勝つかは組で逆）・色・テンプレート（タイトル帯＋16:9＋ブランド帯の「サンドイッチ」型も当たり外れ両方）。包装が効くのは「アカウントがどう見えるか」と、保存・いいね（と考えられる）
- **作り手の結論**:「for a clipping tool, the highest-leverage decisions come **before the edit**: which video, which moment, which first second, which title」。包装は「a reliable floor」（音量、顔に被らない重ね、音と映像の同期、1080p の素材、終わりのカードは短くか無し）として自動で検査する。題と投稿文は「Every claim must be traceable to the speaker's words」「with a mandatory human read. Drafts only; nothing is auto-posted」
- これから自分たちのアカウントで A/B を取る仮説（H10〜H18、各 8 組以上）を並べている。例: H14「payoff の一行を 1.5 秒で先に出し、それから文脈」、H18「同じ区間を 45 秒以下と 60〜90 秒で」。**どれも未検証**
- 限界（原文の要約）: 英語に偏る。抖音・微博・小紅書は取得を拒まれて取っていない（回避しなかったと書く）。同じアカウントでも話題・ゲスト・時刻・投稿の年齢の交絡は残る。一時点の数字

## この wiki への含意

- **何を AI に任せられるか / 何が人に残るか（この報告の主張）**: 伸びを決めるのは編集の前の「どの動画・どの瞬間・どの最初の 1 秒・どの題」で、そこは自動の選択（AI）が担うべき所と作り手は位置づける。ただし題と投稿文は人が必ず読む下書きで、自動投稿しない。**選ぶのは AI に下書きさせ、出すかどうかは人**、という分担
- **[[exp-shortmovie-draft-generator]] と照らす**:
  - **一致**: 西尾の回した道具のプロンプトの「冒頭 2 秒でインパクト」「冒頭 2 秒は YouTube のサムネイルにあたる」は、Finding 2（約 1.5 秒以内に顔か見える出来事）と同じ向き。しかもこの報告は「始まりは編集でなく、どこから切るか（in-point）で決まる」と書く。西尾の道具が `first_impact`（最初の 2 秒のフレーズ）を**企画の欄として選ばせた**のは、編集でなく選択の段で冒頭を決める作りで、報告の結論と合う
  - **一致**: 尺 90 秒以内・理想 60 秒は Finding 5 の既定（90 秒以下）と合う
  - **食い違い（重みの置き方）**: 西尾の道具のプロンプトは「アルゴリズムの 7 割が視聴時間」「5〜10 秒で話を切り替えたりカットを変えたり」と、**編集のテンポで離脱を防ぐ**ことも求めた。この報告は、カット率は当たりと外れで違わなかった（Finding 6）と書く。どちらも検証された数字ではない（プロンプトの 7 割・9 割は出典なし、報告は一時点の観察）。両方を残す
  - **報告にあって西尾の道具にない観点**: 誰が・何が映っているか（Finding 1）、単独で意味が通る一文（Finding 4）。後者は OpenShorts の STANDS ALONE の規則と同じ
  - **西尾の道具の Open Question「黒帯の縦か、話者に寄せた縦か」**: この報告は「サンドイッチ型」（16:9 を縦の中央に置く。黒帯に近い）が当たりにも外れにもあったと書く。直接の比較ではないが、レイアウトより中身、という向き
- **talk の型には当てはまらない部分がある**: 標本は SNS で広める切り抜き（promo）。解説の講演から「理解させる」短尺の基準ではない。Veritasium の「抽象的な話題の talking head は伸びない」は、解説の切り抜きには不利な事実として読める
- [[exp-forest-misc-video-notes]] の「解説形式より一緒に唱える形式が残った」は、編集より中身（何をしているか）が効く、という点で Finding 1 と同じ向き（別の場・別の測り方なので並べるだけ）

## Open Questions

- 統計の検定がなく、アカウントあたり 2〜4 本の極端な組の比較。報告自身が「overstates the typical spread」と書く。一般化できるかは、作り手が予告した A/B（H10〜H18）の結果待ち
- 日本語の短尺は 有吉の壁 の 1 例ほど。日本語の講演・解説の切り抜きに当てはまるかは分からない
- 「始まりは in-point で決まる」を自動でやる部分（表情・動作の山のコマで始まりを選ぶ）は「not built yet」と書く。書き起こしだけで選ぶ道具（西尾の道具、OpenShorts の一次の採点）は、映像の山を見ていない
- 西尾の「3 秒延長」と、報告の「終わりの反応を 1.0〜2.5 秒保つ」（§5 の 1 番、フレームから推した実装の提案で測定ではない）は同じ向きか。量は近い
