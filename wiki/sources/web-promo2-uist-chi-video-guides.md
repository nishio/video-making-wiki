---
type: source
summary: HCI の学会 UIST 2026 と CHI 2026 の動画の指針。研究の 30 秒の video preview（論文の「elevator pitch」、YouTube と ACM DL で公開）と査読用の video figure を分け、字幕ファイルを必須にし、実際のシステムの画面収録と撮影の作法（何が起きるかを先に言う、見る場所を指す、マウスを無駄に動かさない、クリック音を足す）を書いている
video_types: [promo, talk]
url: https://uist.acm.org/2026/video-guide
author: ACM UIST 2026 の組織委員会／ACM CHI 2026 の組織委員会
published: 2026（UIST 2026 の Video Guide、CHI 2026 の「Guide to a Successful Video Submission」。ページに日付なし）
retrieved: 2026-11-09
sources:
  - https://uist.acm.org/2026/video-guide
  - https://chi2026.acm.org/?p=834（Guide to a Successful Video Submission / Guide to an Accessible Video Submission）
  - https://chi2020.acm.org/technical-requirements-and-guidelines-for-videos-at-chi/（video figure の長さ「usually up to 5 minutes」、容量の数字。2020 年のもの）
---

# UIST・CHI の video preview と video figure の指針

## 何の文献か

- ACM の HCI の学会（UIST: User Interface Software and Technology、CHI: Human Factors in Computing Systems）が、論文の著者に向けて出している動画の作り方と提出の決まり。研究の作品（システム・インタラクション）を紹介する動画の、学会側の規範
- 効果の測定ではない。決まり（must）と助言（hints）が混ざるので分けて書く
- 2026-11-09 時点の公式ページによる。UIST 2026 は 30 秒・mp4 などを書くが、video figure の長さと容量は「see CFP」とし、このページには数字がない。CHI 2026 のページにも長さの数字はない。長さの数字は CHI 2020 のページのもの（古い）

## 書いてあること

### 二つの種類

- **Video preview（30 秒）**: 「a video abstract of a paper ... an "elevator pitch" that communicates the contributions of the work in a visual, concise way」（UIST 2026）。目的は「promote their work to a wider audience and to attract more readers」。会議の前・中・後に ACM SIGCHI の YouTube と ACM Digital Library（論文の要旨の隣）、会議アプリに載り、選ばれたものは会議のティーザー動画に入る。UIST 2026 は Papers の著者に必須
- **Video figure**: 投稿の補足資料で、査読者に送られる。「illustrate the key aspects of the work」。論文は単独で成り立つことが前提で、動画は補助（UIST 2026）。CHI 2020 は「They usually last up to 5 minutes」、容量 100MB（論文と合わせ 120MB）、preview は 20MB と書いていた

### 決まり（must）

- 形式: MPEG-4/H.264（.mp4）、正方画素（UIST 2026）
- **冒頭 3〜5 秒にタイトル**（論文名・著者・所属・連絡先）。匿名査読では初回提出から識別情報を除く（UIST 2026）
- **字幕**: UIST 2026 は「For ALL videos closed captions (CC) / subtitles of spoken text are mandatory」で、焼き込まず .srt か .sbv の別ファイルで出す。CHI 2026 も「Closed-captioning is mandatory for all video content at CHI」。CHI 2026 は「If you use automatic speech recognition or other AI-based captioning tools (e.g., otter.ai), it is essential to review your closed captions and correct any error」と書く
- 解像度: 1080p か 4K、16:9（UIST 2026 の Equipment の項）
- 素材の権利は著者の責任。音楽・映像・画像・識別できる人物の写真・他社の中身。提出時に同意を確認する（UIST 2026）。CHI 2026 も音楽の権利を「very important」と書く

### 作り方の助言（UIST 2026 の Creation Advice、CHI 2026 の同種の項）

- **動画を「校正」せよ（usability test）**: 台本を同僚に読ませ、絵コンテを見せ、ラフカットを見せる。「Is the demo clear? Is the pace too fast or too slow?」（UIST）
- 研究をしていない人に、撮る前にデモをして見せよ（UIST）
- 「Usually the most realistic and convincing advocate of an idea is the person responsible for the research」。話す顔の場面は最小限に（UIST）
- **テンポ（「Really Important!」）**: 「Too slow a pace is as common as too fast. A recording of a live demo often will appear too slow」（UIST）
- **説明の仕方**: 「Always explain (briefly perhaps) what is about to happen or what is most interesting」「Tell the viewer where to look and what to look for」。要点は一度、繰り返さない（UIST）。CHI 2026 も同じ文言で、矢印・注記・字幕で視線を導け、字幕が下端に重なるので重要なものを下に置くな、と書く
- 最初に全体を見せるショット（establishing shot）を置き、ときどき戻る。顔・画面・手・スライドを切り替える（UIST）
- CHI 2026: 物理世界での動き（身振りや人とのやり取り）が操作の一部なら、システム上の効果だけでなく、その動きを見せよ
- **画面の収録**: 「Avoid visual distractions, such as idly moving the mouse」（UIST・CHI）。画面収録のソフトは十分な fps で、アプリの性能を落とさないこと。収録範囲は関心のある所に絞る。「screen capture only captures the screen」なので、操作する人を撮った広いショットを足し、クリックしたときのクリック音を足すことを考えよ（UIST・CHI）
- CHI 2026: 最終の画は手元のモニタほど鮮明にならないので「zoom in closer than might seem necessary」、重要なものを画面の端に置かない
- CHI 2026: ナレーションを先に録り、場面の切り替えに合わせて間を空け、映像をそれに合わせる、という作り方を「common and often effective」と書く。台本を書いておくと字幕も作りやすい
- CHI 2026 の accessibility の項: 見えない人もいるので「presentation should be understandable from the script alone」。重要な視覚は声で説明せよ。点滅や動きに敏感な人もいる
- 30 秒の preview の例として、UIST 2026 は「冒頭で貢献を見せる」「問題 → 解決 → 評価」「使用例を並べる」「ナレーションなしで、良い図と短い注記で自明にする」を挙げる（例の動画は見ていない）

### AI について

- 生成映像についての決まりは、どちらのページにもない。CHI 2026 の AI への言及は、自動字幕を必ず見直せ、という所だけ

## この wiki への含意

- **研究の作品の promo には、学会が二つの型を用意している**: 30 秒の preview（広める・読ませる＝promo）と、査読者に見せる video figure（理解させる＝talk 寄り）。西尾の Gyazo の動画で「promo の形にしたら技術の詳細が伝わらなくなった」（[[origin-2026-11-09]] の Updates、[[exp-gyazo-resumption-video]]）のは、学会の言葉で言えば preview と figure を一本で兼ねようとした形になる。学会は最初から別の動画にしている
- **30 秒でも中身は「貢献」**: preview は「elevator pitch」で、冒頭で貢献を見せる例を挙げる。ブランドより先に貢献、という点は Derek Lieu の「作品を早く」（[[web-promo2-derek-lieu-game-trailers]]）と揃う
- **実物の画面と撮影が前提**: 「the most realistic and convincing advocate」「screen capture」「クリック音」は、実際のシステムを動かして撮ることを前提にした助言。コードで描くモーショングラフィックスや生成映像は想定されていない。[[exp-thinklet-reading-demo-video]]（実機の撮影＋画面＋ナレーション）は、ほぼこの指針どおりの作り
- **字幕**: CHI・UIST は字幕ファイルを必須にする。西尾の promo は字幕を焼き込む作り（[[exp-democracy-river-video]]、[[exp-words-as-public-goods-video]]）で、学会の「焼き込まず別ファイル」とは違う。学会に出すなら別に .srt を書き出す必要がある
- **「ライブデモの録画は遅く見える」**: [[exp-thinklet-reading-demo-video]] の実機 1 ターンは約 33〜50 秒かかった。西尾は待ちを削らずナレーションで埋めた。UIST の助言（遅すぎるテンポは速すぎるのと同じくらい多い）からは、待ちを早送りする選択もありうるが、その場合は早送りを明示しないと「実際の速さ」を誤解させる（[[web-promo2-gemini-nikola-staged-demos]] の論点）
- **「何が起きるかを先に言い、見る場所を指す」** は [[web-mayer-multimedia-principles]] の signaling と同じ向きで、talk の文献とも揃う

## Open Questions

- UIST 2026・CHI 2026 の video figure の長さと容量の上限は、このページからは確かめられなかった（CFP 側にある、と書かれている）。「5 分まで」は CHI 2020 の記述
- 早送り・合成・事前に用意した出力を video figure で使うときの開示の決まりは、両ページに書かれていない。SIGGRAPH の決まりは今回読めなかった
- 30 秒の preview の視聴数や論文の読まれ方への効果を測った資料は見つけていない
