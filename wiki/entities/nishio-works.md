---
type: entity
summary: 事例紹介。西尾の動画作品のうち公開されているものを、一行の紹介・型（promo/talk/embed）・作り方・公開 URL・詳しい経験のページで並べたもの。公開 URL が wiki に無いものは「公開先は未確認」と書く
video_types: [promo, talk, embed]
sources:
  - exp-explainer-video-2026-11.md、exp-tsugigami-promo.md、exp-tsugigami-making.md、exp-gyazo-resumption-video.md、exp-thinklet-reading-demo-video.md、exp-qualia-video.md、exp-nishio-showreel.md、exp-democracy-river-video.md、exp-forest-misc-video-notes.md、exp-sutra-videos-overview.md、exp-sutra-hype-editions.md、exp-sutra-songs-on-music.md、exp-sutra-sync-subtitles.md、exp-sutra-voicevox-singing.md、exp-html-capture-pipeline.md、exp-timeline-2026.md
---

# 事例紹介（西尾の過去作品）

西尾の発言「nishioの過去作品も適宜事例紹介ページに載せて、そこから必要なところにリンクがあるべき」（2026-11-10、Mac の対話から）で作ったページ。

- 載せたのは、wiki の経験のページ（sources/exp-*）にあって、公開されたと記録のある作品。公開 URL は経験のページに書かれているものだけを使い、wiki に無いものは推測で補わず「公開先は未確認」と書いた
- 型は [[three-video-types]] の西尾の語（promo＝プロモーションムービー風、talk＝解説プレゼン風、embed＝プレゼンの中に埋め込んで使う特定概念を解説するもの）。経験のページの `video_types` に従う
- 作り方の手順は [[talk-video-making-2026-11]]（talk）と [[exp-html-capture-pipeline]]（canvas に描いて撮る共通の骨格）。作品の並びを時間で見るなら [[exp-timeline-2026]]
- 新しく公開したら、ここに一行足す

## talk（解説プレゼン風）

| 作品 | 一行の紹介 | 作り方 | 公開 | 詳しく |
|---|---|---|---|---|
| 動画の作り方 2026年11月（6:36、2026-11-09） | 動画は三通り（宣伝・解説・発表の中で流す）あり、通りごとのノウハウをまとめた解説 | 台本と描画のコードは Claude Opus 5.5、声は AivisSpeech（まお）、canvas に描いて headless Chrome で撮り、引用は ffmpeg で重ねる。台本の主張 15 個を原典で確かめた | https://youtu.be/IDkRFwiFXFI | [[exp-explainer-video-2026-11]] |
| 「動画の作り方」の作り方（5:51、2026-11-09） | 上の動画の作り方を、人が決めたことと AI がしたことに分けて見せるプロセス動画 | 本編と同じ作りをフォークした Claude が並行して作った。声の聞き比べ・イントネーションの直し・声の高さの計測の図 | https://youtu.be/Ezzcld2rbL8 | [[exp-explainer-video-2026-11]] |
| tsugigami の広告動画のメイキング（6:40、2026-11-09） | 26 秒の広告動画を、画面は本物・人物は生成でどう作ったかの解説 | プロセス動画の作りを写し、行の範囲と画面の表・語の時刻の測り方・引用の素材の長さを足した。書き出し四回 | https://youtu.be/aXGEaLMI7Fs | [[exp-tsugigami-making]] |
| クオリアさんの解説動画 pilot「このクオリアさんは、どう作られた？」（93 秒、2026-08） | CC BY 4.0 のキャラクター「クオリアさん」がどう作られたかの解説 | galleria の Codex が作った。Pillow の静止スライド＋TTS（SAPI）＋PyAV | https://youtu.be/bW6c9y6MkYg | [[exp-qualia-video]] |
| クオリアさんの解説動画 makingof「AI生成解説動画v2」（1:49、2026-08-11） | pilot のメイキング。Opus 5.5 以前の作り方の代表（西尾） | 同じ組み立てで、声を AivisSpeech（まお）に替えた | https://youtu.be/qntzIC2zNK8 | [[exp-qualia-video]] |
| 「デジタル民主主義の川の流れを見る」事前動画（約 34 分、2025-11-27） | Code for Japan Summit 2025 の講演の持ち時間に収まらないスライドを、同じスライドで説明し直した動画 | 作り方の記録は無い | https://www.youtube.com/watch?v=qW3uzu4uU-A | [[exp-forest-misc-video-notes]] |

## embed（プレゼンの中に埋め込んで使う）

| 作品 | 一行の紹介 | 作り方 | 公開 | 詳しく |
|---|---|---|---|---|
| THINKLET を使った AI 読書支援のデモ（52 秒、2026-08-27） | 首から下げるカメラ付き端末で本の見開きを AI が読んで答えるデモ。約 30 秒の処理待ちを、処理の流れの説明に変えた | 西尾が Premiere Pro で手で編集（この wiki で唯一）。iPhone の実機映像、画面写し、ずんだもんの読み上げ 3 本 | https://youtu.be/-heTyY0l3qc | [[exp-thinklet-reading-demo-video]] |

（経験のページの型は embed と talk。LT に組み込む候補になった）

## promo（プロモーションムービー風）

| 作品 | 一行の紹介 | 作り方 | 公開 | 詳しく |
|---|---|---|---|---|
| tsugigami の広告動画（26 秒、YouTube ショート、2026-11-09） | 手書きノート Web アプリ tsugigami の広告 | 実アプリの録画（ペン入力はプログラムから）と Grok Imagine の人物動画を、画面の四隅の追跡ではめ込んで合成。v1〜v6 | https://youtube.com/shorts/1qKsNrwIxCk | [[exp-tsugigami-promo]] |
| Visual Jev 4BでGyazoを仕分ける — 1万枚をGPUで44分（47 秒、2026-09-29） | 約 13 万枚の画像の配信再開の前に、ローカルのモデルで仕分けた作業を伝える | canvas に描いて撮り、BGM は numpy で合成。2分52秒 → 1分55秒 → 47 秒のハイテンポ版へ作り直した。西尾の評価は「Jevの凄さのアピール重視で技術の詳細を伝えるには適切ではない」 | https://youtu.be/3YlYrPGbluA | [[exp-gyazo-resumption-video]] |
| 西尾の自己紹介のショーリール 15 秒（日本語・英語・縦長ショート、2026-09-27） | 1 つの点が形を変えて経歴をたどるモーショングラフィックス。写真なし | canvas に描いて撮る型を最初に作った作品。粒子 2400 個、BGM は numpy で合成 | 日本語 https://youtu.be/l7P2YNQQEnU 、英語 https://youtu.be/xSXn2iGzys0 、縦長ショート https://youtube.com/shorts/8Ao3mrbEVMU | [[exp-nishio-showreel]] |
| 西尾泰和 — 1分でわかる 研究・執筆・育成・ブロードリスニング（ショーリール 1 分版、60 秒、2026-09 制作） | 15 秒版と同じ事実の集まりを、書影・登壇などの写真で 7 章に分けて見せる | 15 秒版の型に写真を足した。素材は 1 点ずつ出典・権利者・確信度を MANIFEST.md に書いてから使い、画像を描くので HTTP サーバーを立てて撮った。画面に出す事実は一次ソースと突き合わせた | https://youtu.be/N82ljzZCFs4 | [[exp-nishio-showreel]] |
| デジタル民主主義の川の流れを見る — 60 秒版（2026-09-29） | 34 分の講演を、X の無音の自動再生でも字幕だけで通じる 60 秒の動画に | 上の型を流用。字幕と合成 BGM だけ、写真なし。X 用は最初のコマにサムネイル | 日本語 https://www.youtube.com/watch?v=QElvtdsQgdQ （X にも投稿） | [[exp-democracy-river-video]] |

## 経文・真言の動画（sutra-videos）

声は VOICEVOX の歌唱 API（[[exp-sutra-voicevox-singing]]）、画は Python と Pillow で 1 コマずつ描く（[[exp-sutra-videos-overview]]）。型はこの wiki での当てはめで、テンポで上げる版と曲に載せる版は promo 寄り、同期解説は embed と talk の間。公開 URL は Mac の ~/sutra-videos の記録から、YouTube の oembed で西尾のチャンネルと確かめた 6 本（2026-11-10）。

| 作品 | 型 | 一行の紹介 | 作り方 | 公開 | 詳しく |
|---|---|---|---|---|---|
| アゲアゲ般若心経【メロディ版】（3:09、2026-09-27） | promo | 128→176BPM へテンポを上げながら般若心経を唱える。経の構造（否定・列挙・咒）をそのまま演出と曲の構造にした | R1 だけ書き出してレビューを回し、全編は最後。読経も「単音の歌」として合成し、旋律は本人の違和感で止めるまで広げた | https://youtu.be/y-geMFLAoRc | [[exp-sutra-hype-editions]] |
| 読経できるかな？ 般若心経【読経版】（2026-09-27） | promo | 上のアゲアゲ版の読経版（v3.9、詠唱は単音）。メロディ版とはサムネイルの言葉・配色・帯で区別した | 同上 | https://youtu.be/0LLjDnq16uk （題名の【読経版】で対応をつけた） | [[exp-sutra-hype-editions]] |
| 真言言えるかな？【中ボス慈救咒・ラスボス火界咒】（約 2:26、2026-09-27） | promo | 19 尊の名を出し、間をおいて真言を唱える。真言の短い順に並べ、長さを難易度にした | 呼びかけ → 間 → 答えの繰り返し。リズムは西尾が rhythm.txt を直接書き換えた | https://youtu.be/KLWEdhb-Ajk | [[exp-sutra-hype-editions]] |
| 般若心経のカノン｜Heart Sutra Canon（3:22、2026-11-08） | promo | パッフェルベルのカノンの通奏低音の上で、3 声が 2 小節ずつ遅れて同じ旋律で唱える（v2） | 1 声ずつ聴くページで本人の耳でレビュー。声がそろう所を増やし、画面は唱え始める拍の位置に字を置いてそろいを縦の列で見せる | https://www.youtube.com/watch?v=zLO-0EyS_CM | [[exp-sutra-songs-on-music]] |
| 般若心経のカノン(Heart Sutra Canon) | promo | カノンのもう 1 本。wiki の記録では v1（2:58）を 2026-09-27 に公開していて、これがそれと思われるが、長さ・公開日は確かめていない | 同上 | https://youtu.be/KjvsBlcZVtk （v1 との対応は未確認） | [[exp-sutra-songs-on-music]] |
| 残酷な般若心経のテーゼ（1:55、2026-10-01） | promo | 「残酷な天使のテーゼ」のボーカル旋律に般若心経 266 字を載せた替え歌。歌は波音リツ 1 声。西尾は「般若心経の構造解説という意味ではこっちの方が頑張ってる」とも評した | 原曲の歌詞 1 行に経文を割り付け、全行をつなぐと経文と一字も違わないことを毎回検査。歌声の割り付けと映像を二つの機械で並行し、演出は 20 秒×3 案で一回で決めた | https://youtu.be/i0mZXxlrxzY | [[exp-sutra-songs-on-music]] |
| 般若心経 | 未確認 | どの版か、wiki の記録だけでは決められない。wiki で YouTube に出ていると記録があるのは、カノンの概要欄から案内した般若心経の解説版（同期解説、1 回版 107 秒）だが、この URL との対応は確かめていない | — | https://www.youtube.com/watch?v=Y9366zKpRRI （どの版かは未確認） | [[exp-sutra-videos-overview]] |

## 手順書の段から見る事例

[[talk-video-making-2026-11]] の段ごとに、参考になる作品。

| 段 | 事例 |
|---|---|
| 1. 台本 | Gyazo の 47 秒（作業報告をやめて主役を決めた）、クオリアさん（細かい数値を読み上げない） |
| 2. 事実確認 | 動画の作り方 2026年11月（主張 15 個を原典で）、デジタル民主主義の川 60 秒版（講演の数字を一次ソースで） |
| 3. 声 | クオリアさん pilot（SAPI）→ makingof（AivisSpeech）、動画の作り方（三つの声の聞き比べとイントネーション）、THINKLET（ずんだもん）、経文・真言の動画（VOICEVOX の歌唱 API で読経を単音の歌として合成） |
| 4〜6. 時刻表・描画・引用 | ショーリール 15 秒（型の最初）、Gyazo の 47 秒（軽い描画で作り直しを回す）、動画の作り方（引用 3 本を ffmpeg で重ねる）、tsugigami の広告動画（実アプリの録画と生成動画の合成） |
| 8. レビュー | 動画の作り方（出先でスマホ、Google ドキュメントのコメント）、tsugigami のメイキング（原稿の書式をそのまま合成の入力に） |
| 9. 公開 | デジタル民主主義の川 60 秒版（X は最初のコマがサムネイル）、tsugigami の広告動画（生成の人物で AI の使用「はい」）、アゲアゲ般若心経（同じ題材の別版をサムネイルで区別）、ショーリール 1 分版（写真の出典・権利者を 1 点ずつ記録） |

## Open Questions

- （答えが出た）公開先が未確認だった 3 件の URL → 2026-11-10 の Updates
- （答えが出た）このページの置き場所と名前 → 2026-11-11 の Updates
- このページに載せていない作品と理由は、2026-11-10 の log.md の項に書いた
- （答えが出た）残酷な般若心経のテーゼを載せるか → 2026-11-13 の Updates

## Updates

### 2026-11-10 公開先が未確認だった 3 件の URL

- Mac の作業場から（~/nishio-showreel/README.md の「公開（YouTube, 2026-09-27）」の表、~/democracy-river-video/youtube/UPLOAD.md・UPLOAD_en.md）。表の「公開」の列を「公開先は未確認」から URL に直した
  - ショーリール 15 秒: 日本語 https://youtu.be/l7P2YNQQEnU 、英語 https://youtu.be/xSXn2iGzys0 、縦長ショート https://youtube.com/shorts/8Ao3mrbEVMU
  - デジタル民主主義の川 60 秒版（日本語）: https://www.youtube.com/watch?v=QElvtdsQgdQ
  - 「デジタル民主主義の川の流れを見る」34 分の事前動画: https://www.youtube.com/watch?v=qW3uzu4uU-A
- ショーリール 1 分版は README に URL があるが、写真の大半が第三者の撮影なので、載せないままにした

### 2026-11-10 ショーリール 1 分版と経文・真言の動画を載せた（西尾の答え）

- ショーリール 1 分版: 西尾「載せてよい（第三者の撮影の写真があっても可）」。前の項で「第三者の撮影の写真」を理由に載せなかったのを改めた。URL は Mac から
- 経文・真言の動画（sutra-videos）: 西尾「なんで？のせていいよ」。Mac の ~/sutra-videos の記録にあり、YouTube の oembed で西尾のチャンネルと確かめた 6 本を「経文・真言の動画」の節に載せた。exp ページとの対応は題名で付けた。カノンの KjvsBlcZVtk（v1 と思われる）と「般若心経」の Y9366zKpRRI（どの版か）は対応を確かめていない
- 修行や行事の場所、他人のチャンネルの動画は書かない（Mac の Claude の依頼）

### 2026-11-11 置き場所と名前は今のまま（西尾の答え）

- このページの置き場所（entities/）と名前（nishio-works）は今のままでよい
- 2026-11-10 の Updates の「修行や行事の場所、他人のチャンネルの動画は書かない」の出どころを「西尾の指示」から「Mac の Claude の依頼」に直した（西尾の発言ではなかった）


### 2026-11-13 残酷な般若心経のテーゼを載せた（西尾の答え）

- 西尾「載せていいよ」（Mac の対話、2026-11-13）。「経文・真言の動画」の節に一行足した。URL は [[exp-sutra-songs-on-music]] の Updates の i0mZXxlrxzY で、YouTube の oembed で西尾のチャンネルと確かめた（2026-11-13）
- 替え歌の権利の確認がどう決着したかは、この wiki では確かめていないまま
