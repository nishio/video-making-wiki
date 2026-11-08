---
type: concept
summary: 西尾の語「Opus 5.5 が出たあとのもの」（2026-09-22 以後）について、LLM がコードで描く動画の流行を、ハーネス・skill・house rules・批評ループ、型ごとの使われ方、道具の側の変化で整理したページ。流行の中心は promo だったが talk（ナレーション付きの 1〜12 分の解説）も多数作られ、ナレーションを時計にする作り方が広がった。流しっぱなしの embed として作った例は見つからなかった
video_types: [promo, talk, embed]
sources:
  - web-movez-opus-motion-design-course.md
  - web-taelin-bend-nge-feedback.md
  - web-opus-*.md（8 ページ）
  - web-opus2-*.md（7 ページ）
  - exp-timeline-2026.md
---

# Opus 5.5 が出たあとのもの（2026-09-22 以後）

西尾の指示「特にOpus5.5が出たあとのもの」から。経験の側の時系列は [[exp-timeline-2026]]（9/25 以後、西尾の制作も canvas に描く方式・promo に寄った）。

**資料の性格**: ほぼすべて作り手本人の X 投稿・repo・ブログで、効果を測った資料ではない。人気の数字（star・表示回数）は取得日 2026-11-09 のもので、根拠にはしない。X の本文は fxtwitter の API と Internet Archive で取得し、取れなかったものは各ページに書いてある。

## 一行プロンプトと長い指示書

- 一行プロンプト「履歴書用の 15 秒ショーリール」の元の投稿は Stephan Livera（2026-09-25）。効くのはジャンルの文法をモデルが知っていて、間違えようのある中身が無いから（Movez）。中身を足すと事実確認の手間に置き換わる（[[web-opus-stephanlivera-showreel-prompt]]、[[web-movez-opus-motion-design-course]]）。西尾の 15 秒版はこの一行に題材を足した形だった（[[exp-nishio-showreel]]）
- whaleyxbt の作例は一行に記事の全文を足し、15 秒では読めず 22 秒に延ばした。この修正は人が出したもので、review-loop からは出なかった（[[web-opus-whaleyxbt-claude-motion]]）
- Donald Jewkes の約 9,600 字の依頼文は、素材・工程・宛先（「SF の tech Twitter で banger に」）に字数を使い、尺・fps・禁止リストは書いていない。Claude Code チームの Thariq の言葉は「投稿は one-shot、プロンプトは 1 万字で、良い見立てと skill・例・API キー付き」（[[web-opus-donaldjewkes-claude-pop-brief]]）
- 後から出た skill の house rules は、描画の約束・禁止する見た目・採点の形を書く（下）。PDoom は中間で、人の指示は短く、決まりごと（ANIMATION_GUIDE）はモデルが自分で書いてサブエージェントに渡した（[[web-opus-pdoomvideo]]）
- **"brief contagion"（似た動画が大量に出る）は測られた現象ではない**。athemeroy の repo の 9/26 版 README の注釈 1 行に出て翌日消えた語で、Movez が紹介して広がった。似通いの実測として出せるのは「長い依頼文どうしの 5 語連続の一致 87.0%」のほう（[[web-opus-athemeroy-awesome-opus-5-5-videos]]）
- 「one-shot」の申告は、人の指示の回数・内部の見直しの回数・受け入れまでの時間の 3 つに分けて記録せよ、と athemeroy は書く。howseen は「反復したなら one shot と書かない」を最優先の決まりにしている（同、[[web-opus-howseen-claude-motion-design]]）

## house rules と批評ループ

| skill / repo | 決まりの例 | 批評ループ |
|---|---|---|
| hculap/skill-motion-graphic（[[web-opus-hculap-skill-motion-graphic]]） | 依頼の長さ L1〜L4 で段取りを変える。既定は 15 秒・9:16・60fps・120BPM。禁止リスト | 7 軸 10 点、全項目 8 点以上まで、最低 3 回、止める条件つき。納品物に「正直な回数」 |
| whaleyxbt/claude-motion（[[web-opus-whaleyxbt-claude-motion]]） | 読む時間を数値で決める（短い句で 1 秒以上、3 語を超えたら 1 語 0.25 秒足す） | 点数を付けず、チェックリストで何も見つからなくなったら止める |
| howseen-ai/claude-motion-design（[[web-opus-howseen-claude-motion-design]]） | 画面で捏造しない、キャプションを正直に（facts.md、「Example data」の表示） | 作る者と裁く者を分け、読み取り専用のエージェントが「既定は却下」。新しいエージェントにコマだけから要旨を言い直させる。人に音を消して見せ一文で要約できるか試す |
| PDoom（[[web-opus-pdoomvideo]]） | 「自分の章のファイルだけ編集、共有ファイルは直さず報告」 | シートを開いて見る |

- 経験との一致: 「2〜4 秒ごとに新しいこと」「1 秒を超えて止めない」は西尾の promo の経験（死んだ拍。[[exp-polis-magi-op]]、[[exp-sutra-hype-editions]]）と一致する
- 経験との食い違い: 同じ決まりは talk の経験（完全静止を既定、drift は気持ち悪い。[[exp-qualia-video]]）と逆。skill 群は解説も対象に挙げるが、解説用に決まりを変える記述は無い
- 合格条件の違い: skill は AI の自己採点、西尾の制作は人の一言が合格条件だった。Gyazo の 12 行の指摘（[[exp-gyazo-resumption-video]]）は「中身が伝わるか」への指摘で、howseen の「コマだけから要旨を言い直させる」が一番近い試み。効くかは誰も測っていない

## 型ごとに何が作られたか

- **promo が中心**: athemeroy のデータセット（X で集めた約 1,400 本）の機械のラベルでは、ゲーム・広告・AI の話題が 57.7%、教育・科学は 1 割強（[[web-opus2-awesome-claude-5-5-videos]]）
- **talk も多数作られた**: 公開後 2 週間で 1〜12 分のナレーション付き解説（導関数、VAE、Transformer、パスキー、大気循環など）が作者本人の投稿で 17 本読めた。長い解説では Manim と Remotion が名指しされている。手で選んだ 168 件のうち教育の解説は 27 件で、尺の中央値 102 秒（他の経路は 25〜52 秒）（[[web-opus2-opus-5-5-explainer-posts-on-x]]、[[web-opus2-awesome-claude-5-5-videos]]）
- 日本語の talk の例: 研修動画 2〜3 分を Opus 5.5 と GPT-6 Astra に作らせ、差は見た目でなく説明の順序に出た、と著者は書く。Opus 5.5 は TTS の読みの誤りを文字起こしで自分で確かめていた（[[web-opus2-tatebayashi-opus-5-5-vs-gpt-6-astra-training-video]]）。各ショットに「次のショットへのつながり」を書かせて「スライドを 9 枚切り替えるだけ」を避けた例（[[web-opus2-zenn-acntechjp-opus-5-5-jev-explainer]]）
- **ナレーションを時計にする**: 声の実際の長さで各ショットの切れ目を決め、動作を句に掛ける。HyperFrames の解説ガイドは「~60 秒」と書き、尺はナレーションが決めるとする（[[web-opus2-opus-5-5-explainer-posts-on-x]]、[[web-opus2-hyperframes-after-2026-09-22]]）。西尾の democracy-river 英語版は字幕版の時間を先に作ってナレーションに合わせて伸ばす順で、逆だった（[[exp-democracy-river-video]]）
- **作り手自身が「モデルは聞けない・通しで見られない」と書く**。対処はラウドネス・同期・空白コマの機械検査、コンタクトシート、TTS を文字起こしして読みを照合すること。最後は人が聞く（同）。[[exp-galleria-tts-and-singing]] の「最後は耳」と一致
- **embed（流しっぱなしで発表に埋め込む）として作った例は見つからなかった**。HyperFrames の公式ガイドは「誰も話さず最初から最後まで流すならデッキでなく動画」と分けている（[[web-opus2-hyperframes-after-2026-09-22]]）。話し手が送る動くスライド（Remotion Player）は ebibibi の例がある（[[web-opus2-ebibibi-presentations-web]]）が、これは西尾の embed の前提（流しっぱなし）ではない
- Anthropic の公式の Claude Motion（2026-10-08、Team・Enterprise のベータ）は、動画生成モデルを使わずコードで描き、例は「全社集会の 30 秒の解説」「取締役会の資料のグラフに動き」「顧客向けの手順」。talk・embed 寄りで、助言は「誰が見るか、どこで流すか、だいたいの長さ」を言うこと（[[web-opus-anthropic-claude-motion]]）。西尾の「型を決めたのは流す場所」と同じ軸

## 描画方式と、Opus 5.5 以前との違い

- 道具の名前が出てくる件数（athemeroy のデータから担当が数えた）: 素の JS/Canvas 55、Remotion 10、HyperFrames 8、Manim 2（[[web-opus2-awesome-claude-5-5-videos]]）。西尾の方式（素の canvas）は多数派の側
- 道具の側の変化: HyperFrames は 9/22 以後 194 リリース、skill を 21 から 7 に減らし「強いエージェントは自分で計画し確かめる。足りないのは非公開の事実」と書いた。Remotion は skill に「プレビューを先に開く」「静止画で確かめる」「人が後で直せるタイムライン」を足した。新しい OSS の OpenFilm（10-04）は `frame(t)` 一つで描き、2 通りの順で描いて一致を確かめる。Manim CE と Motion Canvas には LLM 向けの動きが無い（[[web-opus2-hyperframes-after-2026-09-22]]、[[web-opus2-remotion-openfilm-manim-after-2026-09-22]]）
- 並列化: 外では 6〜8 プロセスで並列に撮っている。西尾の方式は 1 タブで順に撮った（[[exp-html-capture-pipeline]]）
- **モデルか道具か**: 作り手の多くはモデルの変化だと書く。HN には「Sol 5.6 や Opus 4.5 でも作れた」「アニメ付きのスライドにすぎない」という反論がある。前のモデルと同じ課題で比べた記録は見つからなかった（[[web-opus2-opus-5-5-explainer-posts-on-x]]）

## Open Questions

- house rules の「止めない」決まりを talk に使うべきか。外の解説（Zenn・HyperFrames）は連続したカメラの動きを推し、西尾の talk の経験は静止を既定にした。測った資料は無い
- 「コマだけから要旨を言い直させる」批評が、Gyazo のような「中身が伝わらない」問題を事前に拾えるか
- 流しっぱなしの embed を、この方式で作った例が外に無い。西尾が最初の例を作ることになるか
- talk の題材の正しさを第三者が確かめた記録は無い。流行の解説動画の正確さは分からない

## Updates

### 2026-11-09 第 3 回サーベイから

- 「モデルは聞けない・通しで見られない」は、Claude については 2026-11 の docs でもそのまま正しい（動画の入力が無く、API に音声の入力も無い）。Gemini と Qwen-Omni の API なら、映像と音を通しで見せられる（[[web-means-critic-gemini-video-understanding]]、[[web-means-critic-openai-claude-vision-docs]]）
- ただし、点数を付けさせる批評は人と合わない（点の完全一致 26〜29%）。同期・停止・動きの評価は、研究上まだ届いていない。hculap の「全項目 8 点以上まで回す」ループには裏付けが無い（[[web-means-critic-videoscore]]、[[web-means-critic-video-bench-spotlight]]）
- Open Questions の「コマだけから要旨を言い直させる批評が Gyazo のような問題を拾えるか」には、Paper2Video の「モデルの小テストと人の評価が逆になった」を足す（[[web-means-critic-edupanel-paper2video]]）。試す手順は [[ready-to-start-2026-11-10]] の 8
