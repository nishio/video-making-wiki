---
type: source
summary: SIGGRAPH・IEEE VIS・CHI の「Fast Forward／Madness」（論文 1 本を 10〜30 秒で予告する全体会）の決まり。止められない動画を流しっぱなしにし、著者がその上で生で話す形で、VIS 2015 は「録音したナレーションを入れるな（発表は生で）」、SIGGRAPH 2026 は「動画が終わるとマイクを切る」と書いている。流しっぱなしの embed と話し手の声の分担について、この wiki で見つかった一番はっきりした規則
video_types: [embed, promo]
url: https://s2026.siggraph.org/papers-fast-forward-author-instructions/
author: ACM SIGGRAPH 2026 組織委員会／IEEE VIS 2015・2024 組織委員会／ACM CHI 2008・2012 Madness chairs
published: 2008〜2026（各年の公式ページ。下の sources に年を書く）
retrieved: 2026-11-09
sources:
  - https://s2026.siggraph.org/papers-fast-forward-author-instructions/ （SIGGRAPH 2026 Papers Fast Forward Author Instructions。会期 2026-07-19）
  - https://ieeevis.org/year/2015/info/presenter-information/fast-forwards （IEEE VIS 2015 Fast Forwards）
  - https://aa.ieeevis.org/year/2024/info/presenter-information/fast-forward-and-video-previews と https://aa.ieeevis.org/year/2024/info/presenter-information/talk-guide （IEEE VIS 2024 Video Previews・Talk Guide）
  - https://chi2012.acm.org/cfp-madness-guide.shtml （CHI 2012 CHI Madness Authors' Guide）
  - https://chi2008.acm.org/madness.html （CHI 2008 CHI Madness）
---

# SIGGRAPH・IEEE VIS・CHI の Fast Forward／Madness

## 何の文献か

- 大きな学会が、その日の（またはその会期の）全論文を 1 本 10〜30 秒で次々に予告する全体会（SIGGRAPH・VIS は「Fast Forward」、CHI は「CHI Madness」）の、著者向けの公式の決まり。**会場の大画面で動画を流しっぱなしにし、著者が舞台で生で話す**、という形を規則として書いた一次資料
- 効果の測定ではない。決まり（must）と助言が混ざる。年ごとに形が変わっている（VIS は 2015 の生の Fast Forward から、2024 には YouTube 用の Video Preview に移った）ので、年を明記して書く
- 2026-11-09 時点で読めた各年の公式ページによる

## 書いてあること

### SIGGRAPH 2026（Papers Fast Forward、2026-07-19）

- 提出した動画が **20 秒**なら「you must have at least one author on the stage to narrate your video while it is playing」。**10 秒**なら著者は舞台に上がらない（動画だけ）
- 二つの舞台で交互に進める。前の動画が反対側の舞台で流れている間に位置につき、「when your video starts to play you can begin your presentation」
- 「Please be prepared to speak only for the duration of your video (20 seconds). **Your microphone will be cut off when your video ends.**」
- 動画そのものの音声の扱い（ナレーションを入れてよいか）はこのページには書かれていない（提出側の決まりは読めていない）

### IEEE VIS 2015（Fast Forwards）

- 各論文は「preview their work live in 25 seconds」が必須。そのために「A 25-second Fast Forward video (**without** pre-recorded voice-over)」を出す
- チェックリスト: 25 秒、20MB 以下、1280×720・24〜30fps、H.264 の MPEG-4、VLC 2.2.1 で追加のソフトなしに再生できること。**音声は「allowed, but」**——音量は普通の範囲（小さすぎず大きすぎず）、「**no pre-recorded voice-over** (presentation must be done live)」
- 中身は「communicates the topic and the message of your work (like an elevator pitch)」。題・著者・セッションは冒頭に主催が足すので入れない
- 「All the videos presented at a Fast Forward session will then be assembled into one single video, which will be played while the speakers get on stage ... This single video for the session **cannot** be stopped or paused at any point. So all the Fast Forward presentations have to be **strictly 25 seconds**」
- 「Practice your Fast Forward **at least 5 times** in advance!」。25 秒が終わると次の人の動画が自動で始まるので、舞台を降りる
- 「What you do during your 25-second preview presentation is completely up to you ... You can for instance perform a short sketch」。YouTube 用の Video Preview（ナレーション入り）を流用してよいが、冒頭の題・著者を切り、**録音したナレーションは消せ**、と書く
- 作り方は動画編集ソフト（Windows Movie Maker・iMovie）か、PowerPoint・Keynote の動画書き出し、変換は FFmpeg など、と挙げる

### IEEE VIS 2024（Video Previews。生の Fast Forward ではなく、YouTube で公開する 25 秒）

- 「A 25-second video that clearly communicates the research and contribution, inviting readers to read your paper」。題・著者は主催が 5 秒の題名スライドとして前に足す
- 「Should contain audio narration. However, we discourage background music」。「We discourage humor and trailer-like 'ads' because the video will exist for a long time and can be shared widely」
- 字幕は動画に焼き込まず別ファイルで出す（主催が一貫した形で入れる）
- 同じ学会でも、**会場で話し手が上に乗る版（2015: 録音ナレーション禁止）と、単独で見られる版（2024: ナレーション必須）で、声の決まりが逆**になっている

### CHI Madness（2008・2012）

- 2008: 1 本 30 秒。素材は PowerPoint、30 秒の動画 1 本、または 1024×768 の画像。複数のスライドなら自動で送るよう設定し、30 秒で終わること。「Your slides will be visible for exactly 30 seconds; this is the time you have to get to the microphone and to present」
- 2012: Papers 25 秒、Notes 20 秒。「each author given 20-25 seconds to talk or show a video」。助言は二つ: 「try and give an overview of the work, not just a teaser」「no need to end with the implied 'come to my talk to see more' (after 150 times, the audience gets it!)」
- 2012 の技術の決まり: 長いものは自動で切られる。PowerPoint（動画の埋め込み可）か動画。埋め込むなら動画を同じフォルダに置き、別にも提出。会場は Windows の標準機で最新の PowerPoint、Mac で作ったなら Windows で再生を確かめよ。動画は WMV（予備に XVid の AVI）、合計 100MB 未満。**「We will not modify or test presentations in the morning of the Madness session」**。直せるのは事前の「office hours」の時間だけ
- 「The slide deck will be set to auto advance, and you will not have an opportunity to run longer. You can finish early though」

## この wiki への含意

- **西尾の embed（流しっぱなしの前提、[[embed]] の Updates）と同じ形の場が、学会には規則として存在する**。「動画は止まらない・話し手が上に生で話す・時間は動画が決める」。Rosling 型（話し手が止める）でも、無人のループでもない第三の形
- **声の分担の答えの一つ**: 話し手が上に乗るなら、**動画に録音したナレーションを入れない**（VIS 2015）。動画は音を持ってもよいが普通の音量で、語るのは人。逆に単独で流れる版は**ナレーション必須**（VIS 2024）。一本を両方に使い回すなら、ナレーションを別トラックにして外せるように作る、が規則から引ける作り方（推論）
- THINKLET のデモ動画（[[exp-thinklet-reading-demo-video]]）はずんだもんのナレーション入りで、LT で流しっぱなしにした。VIS 2015 の規則に当てはめると「単独で見られる版を会場で流した」形。話し手がその間黙ったか話したかは未確認のまま。もし話し手も話したなら、動画の声と人の声がぶつかる（VIS 2015 がナレーションを禁じた理由と読める。理由そのものはページに書かれていない）
- **尺**: 10・20・25・30 秒。1 概念を 1 本で予告する長さとして、学会は 20〜30 秒を選んでいる。round 2 の次の手「30〜60 秒で一概念」の短い側に当たる
- **再生の失敗を前提にした段取り**: 会場の機械で再生できる形式を指定し（VLC の版、Windows の PowerPoint）、当日の朝は直させない、事前に確かめる時間を設ける。発表の中で流す動画の作法として、そのまま使える（形式の指定は年ごとに違い、2012 の WMV は今は古い）
- **「予告だけで終わるな、概要を言え」（CHI 2012）**は、作品の promo の「中身を見せよ」（[[work-promotion-video]]、[[web-promo2-uist-chi-video-guides]]）と同じ向き
- 「最低 5 回練習せよ」（VIS 2015）。流しっぱなしの動画の上で話すなら、話す台本は動画の秒に合わせて練習で固めることになる。西尾の LT の準備で合成音声に台本を読ませて尺を測った手順（[[exp-lt-20260909]]）が、動画の秒に合わせる練習に使える（推測）

## Open Questions

- SIGGRAPH 2026 の 20 秒動画の提出の決まり（動画の側の音・ナレーションの可否）は読めていない。著者がナレーションしながら、動画にも音があったのかは分からない
- Fast Forward の形が伝わったか（聴衆がどの発表に行くかを決めるのに役立ったか）を測った資料は見つけていない
- VIS が 2015 の生の Fast Forward から Video Preview に移った理由は、読んだページには書かれていない（2020〜2021 のオンライン開催との関係は推測）
- 20 秒の間に話し手が話す量（字数）の目安は、どの年のページにも無い
