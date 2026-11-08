---
type: source
summary: Opus 5.5 公開（2026-09-22）後の 2 週間に X に投稿された、ナレーション付きの解説動画（1〜12 分）の作者本人の投稿 17 本と、Hacker News の議論 2 本。描画は Manim・Remotion・HyperFrames・名前のない JS/Canvas に分かれ、声は edge-tts・Azure・クローン音声。作者たちは「モデルは音を聞けない・通しで見られない」ことを自分で書き、HN では「スライドに動きを付けただけ」という批判も出た
video_types: [talk, promo]
url: https://x.com/LinearUncle/status/2103128559174971663
author: X の各投稿者（下の表）、Hacker News の投稿者、BeatAPI（Eric Kang）
published: 2026-09-23〜2026-10-10
retrieved: 2026-11-09
sources:
  - https://x.com/LinearUncle/status/2103128559174971663
  - https://x.com/Tz_2022/status/2102838830285898214
  - https://x.com/imShiWen/status/2102954743442399395
  - https://x.com/dotey/status/2103683057689522564
  - https://x.com/ng169onX/status/2103183904563998809
  - https://x.com/kimmonismus/status/2102844654169575547
  - https://x.com/akokoi1/status/2102606609574941028
  - https://x.com/0xpai_eth/status/2103166575071330778
  - https://x.com/0x0funky/status/2102736587708854585
  - https://x.com/jisaku_net/status/2103095131536764940
  - https://x.com/addyosmani/status/2103009037164110327
  - https://x.com/joaoli13/status/2102805381542220038
  - https://x.com/kenyondigital/status/2106108583570034984
  - https://x.com/HenrygSing/status/2106206696146382891
  - https://x.com/xRog3r/status/2105863471434981768
  - https://x.com/Acai_murmur/status/2105869306625982594
  - https://x.com/agito20211021/status/2108852733792891379
  - https://news.ycombinator.com/item?id=49836374
  - https://news.ycombinator.com/item?id=49875112
  - https://huggingface.co/blog/karmen-beatapi/how-to-make-videos-with-claude-opus-5-5
---

# Opus 5.5 で作ったナレーション付き解説動画（X の作者本人の投稿と HN の議論）

## 何の文献か

- **X の投稿 17 本**（作者本人の投稿・返信）。本文は api.fxtwitter.com（X の公開投稿を JSON で返す第三者の API）経由で取得した。動画の長さはその API が返す値。動画そのものは見ていない。題材の正しさ・音声の質は確かめていない
- 投稿の選び方: [[web-opus2-awesome-claude-5-5-videos]] が「教育の解説」に分類した 27 件と 10-03 の追加分から、ナレーションがあり作者が作り方を書いているものを選んだ。抽出は偏っている（拡散した投稿が中心）
- **Hacker News のスレッド 2 本**（algolia の API で全コメントを取得）: 「Opus 5.5 is good at explainer videos」（2026-09-24、433 点、リンク先は launchvideo.io）と、2026-09-28 の Ask 形式の投稿
- **BeatAPI の解説記事**（Hugging Face のコミュニティ記事、2026-09-27、Eric Kang）。BeatAPI は Opus 5.5 を安く再販する API 業者で、記事は自社の宣伝を含む

## 書いてあること

### 作者たちの投稿（talk に当たるもの）

| 投稿（UTC） | 長さ | 描画 | 声 | 作者が書いていること |
|---|---|---|---|---|
| LinearUncle 09-24 | 457 秒 | Manim | edge-tts | 導関数の授業。プロンプトは「请用Manim给我制作一个导数概念学习的视频，要求通俗易懂，并且有例子，引人思考。配音使用edge-tts」の一文。「opus 5.5 は Manim を使うのがとてもうまい」 |
| Tz_2022 09-23 | 249 秒 | 記載なし（「按帧确定性渲染」） | edge-tts（云希） | password と passkey の違い。「数十分、余計な質問を一つもせずに 4 分 10 秒の解説動画を作った」。モデルの申告として「**配音は自分の耳で試聴できない。音量が正常で削波が無いことだけ確かめた。時間軸と字幕は同じデータなので理論上は同期している。まず通して聞いてほしい。bank.example のような英単語の読みは硬いかもしれない**」「BGM は入れていない」「縦長版も同じ素材から作り直せる」を引用 |
| imShiWen 09-24 | 375 秒 | 記載なし | 無料の TTS | 同じ題材（password と passkey）。「6 分・12 章・字幕付き。対話的な Web ページも付けてきた。私は 1 コマも編集していない」 |
| dotey 09-26 | 732 秒 | JS | 記載なし | 「什么是 Transformer」。プロンプトは「js で動画を。高校生にも分かるように、high level だけでなく細部も、注意機構や数学の概念も。どんな道具を入れてもよい、ネットで調べてよい。驚かせて」 |
| ng169onX 09-24 | 335 秒 | Manim | Qwen3-TTS（MLX）でクローンした人の声 | VAE の解説。「3Blue1Brown に似た様式」「MNIST で実際にモデルを学習させたので、出てくる数字は本物」「BGM も作った」。一つの短いプロンプトから、と書く |
| kimmonismus 09-23 | 180 秒 | Remotion（React/TypeScript 約 7,400 行）、絵は SVG と Canvas | オープンソースの TTS | AI の歴史。「ストック映像も画像生成も無し」「曲は Python で合成」「約 1 時間、週の利用枠の 7%」 |
| akokoi1 09-23 | 288 秒 | 記載なし（線画） | 中国の TTS 業者の API | 高校地理「大気循環」。「26 分」。手順として TTS 業者の文書を TTS.md に貼り、API キーは .env に置き、`.claude/settings.json` に `"deny": ["Read(./.env)"]` を書いて Claude に鍵を読ませない、と書く |
| 0xpai_eth 09-24 | 264 秒 | 記載なし（線画） | 作者自身の声（既存の素材） | 経済の解説。「一番驚いたのは、まず私の PC のプロジェクトを調べ、私の声・私の決めた字幕の規範と署名を見つけ、以前の解説シリーズにつなげたこと」 |
| 0x0funky 09-23 | 394 秒 | （返信によると Remotion、React/SVG）| （返信によると CosyVoice） | 英文法の授業。「教育機関向けに作ってきた私の教材の workflow と Skills を打ち負かした」「6 分の動画を週の枠の 1% 未満、one-shot で」。道具と約 45 分は返信によると [[web-opus2-awesome-claude-5-5-videos]] の記録（返信は未読） |
| jisaku_net 09-24 | 77 秒 | コードで描いたアニメ | Azure Speech | 日本語。「電気は発電所からどうやってコンセントまで来るのか」。「写真も画像生成もなし」 |
| addyosmani 09-24 | 40 秒 | JS（各コマ） | 記載なし | 「how browsers work を 40 秒で」 |
| joaoli13 09-23 | 101 秒 | JS | 無し | LLM のコンテキストウィンドウの説明。プロンプト 1 で JS のアニメ、プロンプト 2 で「MP4 にして」と 2 段 |
| kenyondigital 10-02 | 363 秒 | 黒板の様式（第三者の skill「anidoodle」） | クローンした作者の声 | 「for ループ」の授業。「台本を書いて試し、私の声で読み、**チョークの一画一画を私の言葉に合わせ**、4K で描いた」 |
| HenrygSing 10-03 | 180 秒 | Remotion＋React | Microsoft の TTS | 研修の紹介動画。「原稿と要件だけ渡した。絵コンテ、**場面ごとのスクリーンショットの確認、レイアウトの修正**、最後の描画まで自分でやった」 |
| xRog3r 10-02 | 540 秒 | ブラウザで t の関数、headless Chrome 8 プロセスで並列に撮る | VoxCPM2 で自分の声をクローン（火山引擎の声は不満で替えた） | 「LLM で動画を作る」チュートリアル。下に詳しく |
| Acai_murmur 10-02 | 249 秒 | Python（約 2,000 行、場面関数 30 個、6 プロセス並列） | システムの音声 | AI ニュースの 4 分 9 秒・51 ショット。下に詳しく |
| agito20211021 10-10 | 61 秒 | HyperFrames（Opus が進行・台本・設計、Sonnet 5.5 が 9 体でコマを並列に） | Gemini 3.8 Flash TTS で声の複製、Whisper で時刻合わせ | 日本語。記事から 1 分。「演出の指示まで読み上げた件、84 秒から 61 秒への短縮、書き出し後のフェードアウト。これも全部 AI が内部で修正」 |

### ナレーションと絵の時間の合わせ方（作者の記述）

- **xRog3r**: 「配音が時計。各ショットの長さは実際の配音で決まり、ショットの中の動作はどれもナレーションのある句に掛けてある。配音を替えれば画面は自動で伸び縮みする」「配楽と効果音は numpy で合成し、効果音は動作のコマに掛ける」「同じ源から何度描いても各コマは画素単位で一致する」。公開済みの教程と OSS の skills を先に Claude に学ばせて pipeline に整えた、とも書く（リポジトリのリンクは返信欄にあると書くが、このページでは確かめていない）
- **Acai_murmur**: 「旁白はシステムの音声で 1 文ずつ合成し、各文の実際の長さで画面の切れ目を決める」
- **kenyondigital**: チョークの線を作者の言葉に合わせた（上の表）
- **agito20211021**: Whisper で時刻を測ってから組み立てた（工程 5「時刻を測る」）

### 「モデルは聞けない・通しで見られない」

- Tz_2022 が引くモデルの申告（上の表）
- xRog3r: 「モデルは音を聞けないし、連続再生も見られない。だから出す前に毎回自動の品質検査を回す: 空白のコマ、静止した区間、プロセスをまたいだ再描画が画素単位で一致するか、音と画の同期、ラウドネス、背景音が配音を覆っていないか、物理の検算。全部通ってから私に見せる」
- Acai_murmur: 「Claude は動画を再生できない。ffmpeg で数秒ごとに 1 コマ抜いてコンタクトシートにし、それを見て判断する」。完成後に同じ方法で「ランキングと字幕の重なり、分割画面の半分が 3 秒近く黒い、判子が画面の外」を見つけ、問題の区間だけ描き直した。納品のときにモデルが挙げた盲点として「声を聞けない（発音・効果音の耳障りさはラウドネスの数値しかない）」「連続再生を見ていない（テンポは抜いたコマからの推測）」「システムの音声は商用不可なのでこれは試写版」を引く。画像の中の原文が読めず台詞を作ったとき、画面に「DRAMATIZATION — NOT A REAL QUOTE」と出した、とも書く

### Hacker News の反応（2026-09-24〜28）

- 「Opus 5.5 is good at explainer videos」（433 点）への批判: 「既存のプレゼンスライドの skill から動画を作っただけ。概念を説明する絵やアニメは無い」（lern_too_spel）、「OP のはコピーの下手な単純なスライドで、1 年前のモデルでもできた」（ricardobeat、別の投稿者の作品と比べて）
- 前のモデルでも作れたという声: 「1 か月ほど前に Sol 5.6 にテスト用アカウントを作らせ、スクリーンショットを撮り、台本を書き、ElevenLabs の TTS と Remotion で作らせた」（dalemhurley）。「去年 Opus 4.5 を試したときは "まあまあ" だった。今は Opus 5.5 が動画制作の全工程を回している。5 分の解説を MacBook Air M4 で約 5 分、Gemini TTS と MiniMax H3 Max の B ロールで」（AISnakeOil）
- モデルの側の変化と見る声: 「JS の絵とアート・ディレクションは予想外の能力の跳躍に見える。モデルは自分がどの道具に強いかを知っているとは限らないので、既定の道具でないなら手に持たせる必要がある」（NiloCK）。「Opus 5.5 の視覚的な仕事の段差には驚いた」（XenophileJKO、09-28 のスレッド）。逆に「音楽動画などは魔法の多くが ElevenLabs や Suno の API にある」（prodigycorp、同）
- 自分のための解説: 「Claude と作っている複雑な機能の解説を one-shot で作らせた。客に見せるには、Claude が作った内部の語彙を直す必要がある。でも**自分には驚くほど役に立った**。Claude が使っていた内部の語彙がやっと分かった」（hughw）

### BeatAPI の記事の「限界」（業者の解説）

「コードだけの場面はモーショングラフィックスで、実写や自然な口の動きは作らない」「見た目の質はばらつく。**場面がアニメ付きのスライドに見えることがある**」「事実の誤りはありうる。解説には検証済みの brief を渡し、描かれた主張を見直す」「長い実行は壊れうる。サブエージェントの章がきれいにつながらないことがあり、モデルが場面にタイマーを紛れ込ませることがある。まず短い範囲を描く」と書く。描き方は `window.seek(t)` を持つ 1 枚の HTML を Playwright で 1 コマずつ撮る（[[web-movez-opus-motion-design-course]] と同じ）

## この wiki への含意

- **talk（技術の詳細をナレーションで伝える解説）は、9 月の方式で実際に多く作られていた**。[[exp-timeline-2026]] の Open Question「9 月の方式で talk を作ったらどうなるか」に対して、外では 3〜12 分のナレーション付きの解説が公開直後の 2 週間に何本も出ている。ただし題材の正しさ・分かりやすさを第三者が測った記録は無く、HN では「スライドに動きを付けただけ」という評も出た
- **ナレーションが時計になる作り方**（xRog3r、Acai_murmur、agito20211021）は、[[exp-democracy-river-video]] の英語版で西尾の側がやったこと（場面ごとの TTS の長さ＋0.6 秒で各場面の実時間を決め、`warp()` で 60 秒版の時間に写す）と同じ発想。違いは、西尾は字幕版の時間を先に作ってからナレーションに合わせて伸ばしたのに対し、彼らは最初から声の長さで切れ目を決めている点。talk を作るなら後者が素直と読める（試していない）
- **「モデルは聞けない」への対処は、作者ごとに機械検査（ラウドネス・同期・空白）＋人の通し視聴**で、[[exp-qualia-video]] の「機械 QA が通っても視聴品質は保証されない」、[[exp-galleria-tts-and-singing]] の「最後は耳」と一致する。edge-tts の英単語の読み（Tz_2022）は、西尾の「表示文と読み上げ文を分ける」（[[exp-qualia-video]]）で対処する種類の問題
- **既存の声・字幕規範・過去のシリーズを置いたワークスペースが効く**（0xpai_eth）。西尾の側では、Gyazo・Words・Polis が showreel の capture.mjs と音源関数を流用した（[[exp-html-capture-pipeline]]）のと同じ向き
- **並列に撮る**: xRog3r は headless Chrome 8 プロセス、Acai_murmur は 6 プロセスで並列に描いた。西尾の方式は 1 タブで順に撮り、粒子系で 1 分に約 10 分（[[exp-html-capture-pipeline]]）。時刻の純関数なので並列にできる、は [[web-remotion]] と同じ理屈
- **hughw の「自分のための解説」**は、三つの型のどれにも入らない用途（作り手自身の理解）で、embed の「話し手の理解を聴衆に渡す」の手前にある

## Open Questions

- 長い解説（4〜12 分）の題材の正しさを、作者以外が確かめた記録は見つからなかった。導関数・VAE・Transformer のような数式を含む解説で、どこに誤りが出やすいか（[[web-theoremexplainagent-code2video-visualedu]] の LaTeX・配置の失敗が今の世代でも出るか）は分からない
- 「モデルが Manim をうまく使う」（LinearUncle）、「workflow と Skills を打ち負かした」（0x0funky）はモデル側の変化を示す本人の感想で、同じ課題で前のモデルと比べた記録は無い。HN には Sol 5.6・Opus 4.5 でも作れたという反対の証言がある
- xRog3r が公開したという pipeline（make-video skill、20 の落とし穴）は、リンク先を確かめていない
- 0x0funky・rainwishyt の道具の開示は、[[web-opus2-awesome-claude-5-5-videos]] の記録によるもので、返信そのものは読めていない（rainwishyt の投稿は fxtwitter で取得できなかった）
