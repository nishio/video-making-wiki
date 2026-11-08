---
type: source
summary: 「一つのプロンプトで作った、話したのは 5 分、Claude は 12 時間働いた」の MV（Donald Jewkes, 2026-09-23）の公開された依頼文（約 9,600 字）と、それへの Claude Code チームの Thariq の一言「投稿は one-shot、プロンプトは 1 万字で、良い見立てと skill・例・API キー付き」、および「one-shot ではない」と内訳を出した作り手（163 回のモデル呼び出し・約 6¾ 時間）
video_types: [promo]
url: https://x.com/donaldjewkes/status/2102801469976248500
author: Donald Jewkes（@donaldjewkes）、Thariq（@trq212, Claude Code チーム）、Mables Joseph（@mablesjoseph）
published: 2026-09-23
retrieved: 2026-11-09
sources:
  - https://x.com/donaldjewkes/status/2102801274173587569 （完成動画の投稿、2026-09-23 16:44 UTC）
  - https://x.com/donaldjewkes/status/2102801469976248500 （依頼文の全文、2026-09-23 16:45 UTC）
  - https://x.com/trq212/status/2102870353781641416 （Thariq、2026-09-23 21:18 UTC）
  - https://x.com/mablesjoseph/status/2103465246014746943 （2026-09-25 12:42 UTC）
  - 以上の本文・いいね・表示回数は api.fxtwitter.com 経由で 2026-11-09 に取得
  - https://github.com/JohnHeibel/PDoomVideo （依頼文が「元の動画のソース」として渡した repo。[[web-opus-pdoomvideo]]）
---

# Donald Jewkes の「Claude Pop」の依頼文と、Thariq の「one-shot、1 万字」

## 何の文献か

- X の投稿 4 件（作り手 2 人の自己申告と、Anthropic の Claude Code チームの Thariq の一言）。依頼文は作り手が公開した本文そのもの。実際に何が呼ばれ何が実行されたかは、依頼文からは分からない（athemeroy のデータセットも「依頼文は入力を示すが、隠れた呼び出しは示さない」と書いている、[[web-opus-athemeroy-awesome-opus-5-5-videos]]）
- Thariq の投稿は Anthropic の公式の発表ではなく社員個人の投稿。この領域で Claude Code チームの人が出した発信として、この wiki で見つけたのはこの一言だけ（Anthropic の製品としての発信は [[web-opus-anthropic-claude-motion]]）

## 書いてあること

### 完成動画の投稿（2026-09-23）

- "I made this with one prompt using Opus 5.5 / I spoke to my computer for 5mins, claude worked for 12 hours, and I woke up to this / full prompt:"（いいね 11,310・表示 4,056,723、2026-11-09 取得）
- 元にしたのは別の作者の動画（@other__reality の「Claude Pop」）の作り直し

### 依頼文（約 9,600 字、音声入力の書き起こし）

字数は数え方で違う: 取得した本文で 9,608 字、athemeroy の数えで 9,554 字（[[web-opus-athemeroy-awesome-opus-5-5-videos]]）、Movez は「約 9,500 字」。

本文から、何を渡し何を求めたかを拾う（引用は原文の語）:

- **入力**: 元の mp4 と曲、元の JS アニメの repo（PDoomVideo）、自分の過去作のフォルダ、skill 2 つ（参照の集成を引く skill と「video scoring」の skill）、ElevenLabs の API キーと文書、画像・動画生成の API キー（本文では "foul API" と書かれている。音声入力の書き起こしで fal を指すと読める（推測））と約 2,000 ドル分のクレジット、Seedance 2.5 の文書
- **自由度**: "You do not need to anchor to the current style, you can do truly anything"。参照は K-pop の MV を挙げつつ「寄せすぎるな」、Pixar は "kind of slop"、"I don't want you to produce something that is GPT slop"
- **工程の指定**: キャラクターシートとスタイルシートを先に作る → Seedance 2.5 で土台の映像を作り、歌のタイミングを合わせるための "verification loops" を組む → その上に JavaScript のアニメで全編を描き直し、土台は見せない（"that animation technique where you shoot first in traditional film and then draw over top of it"）
- **画面の文字**: 歌詞のモーショングラフィックスを入れ、背景を空けて大きく出す所と字幕のように出す所を分ける。冒頭のフックでは文字を大きく
- **自己批評**: "You're going to want to watch the entire video multiple times, take screenshots at individual parts, and think about if something is really up to the bar of quality that we need here." と、構図とタイミングの計画を厳密に、戻ってやり直すことに開いていろ、と書いている
- **宛先と目標**: "a San Francisco tech Twitter audience"、"The goal for this is to make a banger for Twitter"。Max プランの使用量を全部使え。最後の一文は "make no mistakes."

### Thariq の一言（2026-09-23 21:18 UTC、上の依頼文の引用）

- "the post: "Claude one-shot this" / the prompt: 10k characters with good takes plus skills, examples and API keys"（いいね 2,260・表示 266,638）
- Movez の記事はこれを「投稿は one-shot、プロンプトは skill・例・キー付きの 1 万字」と引き、「9,500 字の指示書、skill のフォルダ、API キー 2 つ、12 時間の自律実行」と並べている（[[web-movez-opus-motion-design-course]]）。**9,500 字・12 時間は Donald Jewkes の側の数字で、Thariq が言ったのは「1 万字」と「良い見立て・skill・例・API キー」まで**

### 内訳を出した作り手（Mables Joseph, 2026-09-25）

- 45 秒の水彩風の短編。"Does Opus 5.5 absolutely cook in one shot, not really ? It's good but still needs a good supporting project."
- 申告した数字: 62.7M トークン（96% がキャッシュ読み）、モデル呼び出し 163 回、API の定価で約 34 ドル、開始から完成まで約 6¾ 時間（うち手を動かしたのは約 1½ 時間）、ラップトップでのレンダリング 12 分（いいね 173・表示 12,334）
- Movez・seeco・hculap の skill は、この例を「批評ループが本体」の根拠に引いている（[[web-opus-hculap-skill-motion-graphic]]）

## この wiki への含意

- **長い指示書の中身は「決まりごと」より「素材と道具と目標」だった**: Donald Jewkes の約 9,600 字は、見た目の禁止リストや尺・fps の指定より、渡す素材（元動画・曲・repo・過去作・skill・API）と工程（キャラ → 土台の映像 → 描き直し）と宛先（SF の tech Twitter）に字数を使っている。尺も fps も書いていない。後から出た skill（[[web-opus-hculap-skill-motion-graphic]]、[[web-opus-howseen-claude-motion-design]]）の house rules とは書いている物が違う
- **「宛先」を書いている点は西尾の経験と同じ向き**: 西尾の経験では型を決めたのは流す場所だった（[[exp-gyazo-resumption-video]] の「X に流す」「ドーパミンアゲアゲ」、[[exp-democracy-river-video]]）。Jewkes も「Twitter で banger に」を目標に据え、冒頭のフックと文字の大きさをそこから導いている
- **自己批評の指示はあるが採点の形は無い**: 「全体を何度も見て、スクリーンショットを撮り、水準に達しているか考えよ」。Movez 以後の skill の「1 拍 1 枚のコンタクトシート、7 軸 10 点、ワースト 3」はこの後に形式化されたもの。西尾の Polis（9/30）は Movez の形式で採点した（[[exp-polis-magi-op]]）
- **「one-shot」と人の手間**: Mables Joseph の「約 6¾ 時間のうち手を動かしたのは約 1½ 時間」は、西尾の Gyazo の 47 秒版が v3 から v3e の 5 版を約 1 時間 15 分で出したこと（[[exp-gyazo-resumption-video]]）と桁が同じ。ただし西尾の側は西尾のフィードバック 1 行ごとに版を出す形で、自律実行の時間ではない
- 土台を動画モデルで作り、上をコードで描き直す（generate-then-trace）は、西尾の Polis が galleria の歌声合成を別に用意した形（[[exp-polis-magi-op]]）とは違う分担。西尾はコードで描く部分と生成モデルの部分（音）を分け、映像を生成モデルに頼まなかった

## Open Questions

- 12 時間の自律実行の中で、自己批評が何回回り、どの段で何が直ったかは公開されていない。依頼文の「verification loops」が実際に組まれたかも分からない
- Thariq の「1 万字」は Donald Jewkes の例を指すが、「流行の作品の多くがそうだった」とは言っていない。Movez・seeco の「最良のものは 9,500 字の指示書から」は彼らの一般化
- Mables Joseph の数字は自己申告で、請求書やログは公開されていない
