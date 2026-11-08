---
type: source
summary: Opus 5.5 期の一行プロンプト「履歴書用の 15 秒ショーリール」の元の投稿（Stephan Livera, 2026-09-25, X）と、それに続いた批評（Rexan Wong「自分の一行は mid だった」→ 参照・素材・絵コンテを先に、2026-09-26）・反論（「2 文で one-shot、ただし motion.so のハーネスで」）。一行が効く理由は「ジャンルの文法をモデルが知っていて、中身を間違えようがない」こと、と Movez が書いている
video_types: [promo]
url: https://x.com/stephanlivera/status/2103315922098470926
author: Stephan Livera（@stephanlivera）ほか（下の sources）
published: 2026-09-25
retrieved: 2026-11-09
sources:
  - https://x.com/stephanlivera/status/2103315922098470926 （2026-09-25 02:49 UTC。本文・いいね・表示回数は api.fxtwitter.com 経由で 2026-11-09 に取得）
  - https://x.com/rexan_wong/status/2103707054108299437 （2026-09-26 04:43 UTC。同上）
  - https://x.com/_adishj/status/2102881137484087308 （2026-09-23 22:01 UTC。同上）
  - https://movez.substack.com/p/how-to-build-motion-design-studio （Movez の記事の Substack 版、2026-10-04 掲載。X の長文 2026-09-27 と同じ本文と見られる。「03. One-liner」節を本文で読んだ）
  - https://x.com/seeconvm/status/2106096193235259564 （seeco の X 長文「Opus 5.5 Motion Design: What the Viral 'One-Prompt' Videos Are Hiding」2026-10-02。api.fxtwitter.com 経由で本文を取得）
---

# 一行プロンプト「履歴書用の 15 秒ショーリール」とその批評

## 何の文献か

- 元の投稿は X の短い投稿 1 件（動画付き）。批評・反論も X の投稿。どれも作り手の自己申告で、動画そのものはこの wiki では見ていない（動画は取得しない決まり）
- 理由づけの部分は Movez の記事（[[web-movez-opus-motion-design-course]]）と seeco の長文による。この 2 本は構成も例もほぼ同じで（9 本の投稿 → 12 段階／8 段階）、seeco は Movez の 5 日後に出ている。どちらも実務家の解説で、検証はしていない

## 書いてあること

### 元の投稿（Stephan Livera, 2026-09-25 02:49 UTC）

- 本文はこれだけ: "Opus 5.5 on Max effort - "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.""
- いいね 17,241・表示 2,318,641（2026-11-09 取得）。effort を Max にしたことだけが書かれ、道具（Claude Code か、どのハーネスか）・回数・時間は書かれていない
- Movez によると、同じ文を xhigh で回した Rob Hallam が「one-shot だった、音も込みで」と書いた（Movez の記事に引用された投稿。この wiki では元投稿を開いていない）。athemeroy のデータセットの 9/25 の更新でも、同じ形の依頼文の変種が同じ検索の窓に多数出たと書いている（[[web-opus-athemeroy-awesome-opus-5-5-videos]]）

### 一行が効く理由（Movez の記事「03. One-liner」）

Movez は「9 本のうち 4 本が同じ文を使った」として、効く理由を 4 つ挙げている:

- 「showreel for a résumé」がジャンルを決める。ジャンルの規則（速いカット、1 ショットごとに違う技法、いちばんいい作品を先に）をモデルが既に知っている
- 「what an incredible motion designer you are」でモデル自身が題材になる。製品を説明しないので、**間違えようのある中身が無い**
- 「15 秒」は 1 回で作り切れる短さで、6〜8 ショットが入る長さ
- 「go all out」は xhigh・max の上にかかる effort の倍率として働く

弱点として「同じ文を何百人も送り、互いに韻を踏むような reel が出た」（"brief contagion"）を挙げ、**「設定の試験に使ったら先へ進め」**と書く。seeco も同じ趣旨で「一行はエンジンを試すが、アイデアは試さない。アイデアを含んでいないから」と書いている。"brief contagion" の語の出どころは [[web-opus-athemeroy-awesome-opus-5-5-videos]]。

Movez が挙げる「出荷された変種」: 60 秒・16:9 で「S-tier の音、汎用のシンセパッド禁止、オリジナルのピアノ曲に全カットを合わせる」、10 秒で「隅に枠や文字を置くな（AI 製の動画の目印）」、技法でなく物語（「[題材] の歴史を [始まり] から今日まで。絵コンテで驚かせて」）、架空のスタジオの人格（「スタートアップ創業者向けのブランディングスタジオとして」）。

### 批評: 「自分の一行は mid だった」（Rexan Wong, 2026-09-26）

- いいね 6,895・表示 649,875（2026-11-09 取得）。冒頭: "everyone says they created it with "one prompt", but my one prompt video looked mid" — そこで流行の動画の作り方を調べた、として 6 段階を挙げる
  1. 参照の動画を選ぶ（whatships.com）。「スタイルは説明するより名前で言うほうがずっと効く」。参照が無いと Opus は既定の見た目（中央の文字、グラデーション背景、全部フェードイン）に戻る。**"that's why so many of these videos look the same"**
  2. HyperFrames か Remotion を入れる（無いと「粗い HTML を画面録画することになる」と書いている。ただし Movez と seeco は、Opus は頼まれなければ自分で HTML＋Playwright＋ffmpeg の経路を選ぶ、と書いていて食い違う）
  3. 21st.dev の UI 部品を入れる。Opus がその場で描く UI は「間隔が違う、仮置きの箱、偽物っぽいボタン」で安っぽく見える
  4. ブランド（ロゴ・色・フォント）、本物の製品の画面、参照動画、頭の中の構想を全部渡し、**絵コンテを 3 案**出させる
  5. 選んだ案で、**動かす前に場面ごとの静止画を 1 枚ずつ**。「絵コンテを直すほうがレンダリングを直すよりずっと安い」
  6. 走らせたら、監督のように注文する（「ズームを全部 0.7 倍に」「ここはハードカット」）。最初のレンダリングは 8 割の出来で、残り 2 割は注文で決まる。「もっと良くして」のような曖昧な注文はランダムな変更を招く
- 締め: "everyone has the same model. the context you give it is what makes it look pro"

### 反論: 「2 文で one-shot、ただしハーネス込み」（Adish Jain, 2026-09-23）

- Claude Code チームの Thariq の「投稿は one-shot、プロンプトは 1 万字」（[[web-opus-donaldjewkes-claude-pop-brief]]）への引用で、"except this actually was one-shotted with a 2-sentence prompt, no references, examples or API keys.. claude opus 5.5 with the @motion_so harness"（いいね 36）
- 依頼文は 2 文でも、ハーネス（製品）の側に決まりごとが入っている、という形。Movez の「プロンプトは 10%、残り 90% はハーネス」と矛盾しない

## この wiki への含意

- **西尾の showreel 15 秒版は、この投稿と同じ日の依頼だった**: 西尾の依頼（2026-09-25）は Livera の文に「Thema: 西尾泰和(NISHIO Hirokazu)の活動・功績」を足したもの（[[exp-nishio-showreel]]、[[exp-timeline-2026]]）。Movez の理由づけでいうと、**題材を足したことで「間違えようのある中身」が入った**。西尾の側は 15 秒版でも経歴の形（球 → 地図 → 島 → 流れ → 意見の地図 → 名前）を描き、1 分版で書影・写真と「画面の主張 → 一次ソース」の表が要った（[[exp-html-capture-pipeline]]）。一行の手軽さは、中身を足すと事実確認の手間に置き換わる
- **Rexan Wong の 5（動かす前に場面ごとの静止画）は、西尾の `capture.mjs stills` と同じ位置**にある（[[exp-html-capture-pipeline]]）。ただし Rexan Wong は人が絵コンテを選ぶ段（4・5）を置く。西尾の 9 月の制作には静止画・コンタクトシートで確かめる手順はあるが、絵コンテの複数案から人が選んだ記録は無い
- **一回目の評価は割れた**: 西尾の 15 秒版は、西尾の最初の反応が「great, 英語版も作って。」で、直しは肩書きの訳だけだった（[[exp-nishio-showreel]]）。Rexan Wong の一行は「mid」、西尾の Polis の v1 は「しょぼい」（[[exp-polis-magi-op]]）。一行で通ったのはジャンルの文法がそのまま効く「自分のショーリール」で、借りる様式（エヴァ OP）が決まっている題材では一回目が通らなかった。Movez の「一行はジャンルを知っているから効く」と同じ向きの観察だが、件数は少ない
- **6 の「監督の語で注文する」**は、[[exp-gyazo-resumption-video]] の西尾のフィードバック（「展開が遅くてだるい、ドーパミンアゲアゲ動画にして」「この比較の仕方はちょっとおかしくて…」）と照らすと、西尾の注文はカメラの語より**中身と論理の語**が多かった。promo でも、題材が技術の主張なら注文は中身に向かう
- 一行プロンプトの作品群は promo の型にしか向かない。「間違えようのある中身が無い」ことが効く理由なので、talk・embed（中身を正しく渡すのが目的）にはそのまま使えない。whaleyxbt は同じ一行に記事の全文を先に渡して解説を作り、15 秒では文字が読めず 22 秒に延ばした（[[web-opus-whaleyxbt-claude-motion]]）

## Open Questions

- 「一行の出力は似る」を、同じ依頼文の出力どうしで測った資料は見つからなかった。Rexan Wong の「だから似る」は観察の言明
- Rexan Wong の「HyperFrames か Remotion が要る」と、Movez・seeco の「Opus は頼まれなければ素の HTML＋Playwright を選ぶ」は食い違う。西尾の方式は後者だった（[[exp-html-capture-pipeline]]）
- Livera の投稿の制作条件（Claude Code か claude.ai か、回数、時間）は投稿からは分からない
