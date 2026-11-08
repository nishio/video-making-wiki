---
type: source
summary: 講演・ピッチの中で動画を流すことについて、TED と Y Combinator の側が書いたこと。TEDx の Speaker Guide（7 ページ）には動画の規則が無く、TED の Chris Anderson は HBR 2013 で「動画は 1 分以内、宣伝臭いものは避ける、サウンドトラック付きの動画は使うな」と書いた（Computerworld の要約で読んだ。HBR の原文は有料で未読）。YC の Demo Day の手引き（2016）は「かつてはここでデモを見せたが、今の Demo Day ではデモはまず機能しない」と書き、動画には触れない
video_types: [embed, talk]
url: https://tedxbend.com/tedx/manuals/tedx_speaker_guide.pdf
author: TED（TEDx Speaker Guide）／Chris Anderson（TED、HBR 2013。Melissa Shaw による Computerworld の要約）／Geoff Ralston（Y Combinator）
published: unknown（TEDx Speaker Guide）、2013-06（HBR）、2013-08-06（Computerworld）、2016-07-25（YC）
retrieved: 2026-11-09
sources:
  - https://tedxbend.com/tedx/manuals/tedx_speaker_guide.pdf （TEDx Speaker Guide。TED の manuals のパス構成のまま TEDxBend のサイトに置かれた写し。7 ページ、日付なし）
  - https://www.computerworld.com/article/1396892/how-to-avoid-multimedia-presentation-pitfalls.html （Computerworld, "How to avoid multimedia presentation pitfalls", 2013-08-06。HBR の要約）
  - https://hbr.org/2013/06/how-to-give-a-killer-presentation （Chris Anderson, "How to Give a Killer Presentation", HBR 2013-06。有料で本文は読めず、題と著者だけ確かめた）
  - https://www.ycombinator.com/blog/guide-to-demo-day-pitches/ （Geoff Ralston, "A Guide to Demo Day Presentations", 2016-07-25）
---

# TED と YC: 講演・ピッチの中の動画

## 何の文献か

- **TEDx Speaker Guide**: TED が TEDx の登壇者向けに配る 7 段の手引き（形を知る → 考えを育てる → 構成と台本 → スライド → リハーサル → 本番）。公式の配布物の写し（TEDxBend のサイト、パスは `/tedx/manuals/tedx_speaker_guide.pdf`）を読んだ。日付は無い。TED の「Create + prepare slides」のページ（ted.com/pages/create-prepare-slides）は 2026-11-09 に 404 だった
- **Chris Anderson, HBR 2013**: TED の curator の寄稿。本文は有料で読めなかった。**読んだのは Computerworld（Network World の編集者 Melissa Shaw）の要約**で、動画の項は Anderson の言葉の要約と短い引用。原典未読
- **YC の Demo Day の手引き**: Y Combinator のパートナー（当時）Geoff Ralston が、数百の Demo Day の発表を指導した経験から書いた実務の助言。2016 年の Demo Day（200 社超）の頃のもの。効果の測定ではない

## 書いてあること

### TEDx Speaker Guide（動画について）

- **動画を流すことについての規則・助言は見当たらなかった**。スライドの節は「Should I use slides?」から始まり、「they are by no means necessary」「The most important rule for slides: Keep it simple」と書く
- スライドの形式: 主催と解像度・縦横比を確かめよ、迷ったら 1920×1080・16:9。「Use the broadcast-safe zones in PowerPoint or Keynote. Don't put any information or visuals in the far corners」。42 ポイント以上、一般的なサンセリフ
- 「Images and photos ... People will understand that the images represent what you're saying, so there is no need to verbally describe the images onscreen.」
- 「No slide should support more than one point.」「if your audience is reading, they are not listening」
- 素材の権利: 「Only use images that you own or have permission to use」。Creative Commons なら出典をスライドの下に
- 本番の機材でリハーサルせよ（「with the clicker and the confidence monitor」）。尺は 18 分未満が絶対

### Anderson（HBR 2013、Computerworld の要約による）

- 「Use video wisely」の項: 「show, don't tell」に動画は最適、と前置きしてから、落とし穴を三つ挙げる（要約の文言）
  - 「Keep clips to 1 minute or less. Any longer and you risk losing your audience's attention.」
  - 「Don't use any video that sounds like an infomercial. "People are conditioned to tune those out,"」
  - 「Don't use video with a soundtrack. Anderson calls it "dangerously off-putting."」
- ほかの項: スライドを読むな（「Information is interesting only once, and hearing and seeing the same words feels repetitive」）、「Many of the best TED speakers don't use slides at all」
- 「soundtrack」が BGM を指すのか、ナレーションを含む音声全体を指すのかは、要約からは分からない（原文で確かめる）

### YC Demo Day の手引き（Ralston 2016）

- 製品と顧客の節: 「This used to be where you would show a demo, but ironically, **demos seldom work in modern demo day presentations**. Explaining rapidly and clearly what your product does can be the most challenging, and rewarding part」
- スライド: 「an audience cannot read a slide AND listen to you simultaneously」。1 枚 1 点、言葉より絵、7 語を超えたら多すぎ、引用は大きくして読み上げよ、「Put important text at the top of the slide. People sitting in the back of an auditorium may not be able to see the lower part of a screen」
- 準備は「practice」だけが効く、と書く
- **動画を流すことについては書いていない**。デモの代わりに動画を流せ、とも書いていない

## この wiki への含意

- **TED・YC とも、話し手の場では「動画を流す」は主役でない**。TEDx の手引きは動画に触れず、YC は「デモはまず機能しない」とだけ書く。Anderson の要約の三つ（1 分以内、宣伝臭くない、サウンドトラックなし）が、講演の側から embed に向けた数少ない明示の助言
- **「1 分以内」**: round 2 の次の手「30〜60 秒で一概念」の上限と一致する。学会の Fast Forward の 20〜30 秒（[[web-embed-siggraph-ieeevis-chi-fast-forward]]）とも矛盾しない
- **「サウンドトラック付きの動画は使うな」**: 話し手が主役の場で、動画の音を足すことへの警告。西尾の embed（流しっぱなし）でも、BGM を足すかどうかに効く。BGM を入れた promo（[[exp-gyazo-resumption-video]] の 120BPM）をそのまま講演に埋めるのは、Anderson の要約に従うなら避ける側。ただし「soundtrack」の範囲（BGM か、ナレーションも含むか）は原文未読で不明
- **「宣伝臭いもの（infomercial）は避ける」**: promo を embed に転用するときの注意。VIS 2024 の「humor and trailer-like 'ads'」を避けよ（[[web-embed-siggraph-ieeevis-chi-fast-forward]]）と同じ向き
- **YC の「デモはまず機能しない」と THINKLET**: THINKLET の 10/2 の LT は「事前録画した映像で行い、ライブ解説はしない」と決めた（[[exp-thinklet-reading-demo-video]]）。YC は代わりに何をせよとは書かないが、「製品が何をするかを速く明確に説明する」ことを最重要に置く。録画のデモを流す選択は YC の文の範囲外で、西尾の判断は文献と食い違わないが、裏付けもない
- TEDx の「画像は言葉で説明しなくてよい（観客は分かる）」は、Ladner の「流す前に何が映るかを言え」（[[web-embed-ladner-sigaccess-chi-video-in-talks]]）と逆向き。TED は一般の観客の理解の速さ、Ladner は見えない人への到達を見ている。両方を残す

## Open Questions

- Anderson の HBR の原文（2013-06）は未読。「soundtrack」の意味、「1 minute or less」の根拠（経験か、TED の何かの観察か）は確かめていない。Anderson の本『TED Talks: The Official TED Guide to Public Speaking』（2016）にも動画の記述があるとされるが、本文は読めていない
- TED の本会議の Speaker Guide（TEDx でない方）に動画の規則があるかは、公開のものが見つからなかった
- 実務記事として、Apple・Google などの基調講演の「話し手が黙って製品映像を流す」型の作り方を、作った側が語った一次資料は、Evangelist 2006（[[web-embed-evangelist-2006-apple-keynote]]）のほかに見つからなかった
- デモデー・ピッチで動画を流した場合と流さない場合を比べた資料は見つけていない
