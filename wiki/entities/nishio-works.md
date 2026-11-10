---
type: entity
summary: 事例紹介。西尾の動画作品のうち公開されているものを、一行の紹介・型（promo/talk/embed）・作り方・公開 URL・詳しい経験のページで並べたもの。公開 URL が wiki に無いものは「公開先は未確認」と書く
video_types: [promo, talk, embed]
sources:
  - exp-explainer-video-2026-11.md、exp-tsugigami-promo.md、exp-tsugigami-making.md、exp-gyazo-resumption-video.md、exp-thinklet-reading-demo-video.md、exp-qualia-video.md、exp-nishio-showreel.md、exp-democracy-river-video.md、exp-forest-misc-video-notes.md、exp-html-capture-pipeline.md、exp-timeline-2026.md
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
| 「デジタル民主主義の川の流れを見る」事前動画（約 34 分、2025-11-27） | Code for Japan Summit 2025 の講演の持ち時間に収まらないスライドを、同じスライドで説明し直した動画 | 作り方の記録は無い | 公開先は未確認（YouTube に公開と記録がある） | [[exp-forest-misc-video-notes]] |

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
| 西尾の自己紹介のショーリール 15 秒（日本語・英語・縦長ショート、2026-09-27） | 1 つの点が形を変えて経歴をたどるモーショングラフィックス。写真なし | canvas に描いて撮る型を最初に作った作品。粒子 2400 個、BGM は numpy で合成 | 公開先は未確認（YouTube に公開と記録がある） | [[exp-nishio-showreel]] |
| デジタル民主主義の川の流れを見る — 60 秒版（2026-09-29） | 34 分の講演を、X の無音の自動再生でも字幕だけで通じる 60 秒の動画に | 上の型を流用。字幕と合成 BGM だけ、写真なし。X 用は最初のコマにサムネイル | 公開先は未確認（X と YouTube に投稿と記録がある） | [[exp-democracy-river-video]] |

## 手順書の段から見る事例

[[talk-video-making-2026-11]] の段ごとに、参考になる作品。

| 段 | 事例 |
|---|---|
| 1. 台本 | Gyazo の 47 秒（作業報告をやめて主役を決めた）、クオリアさん（細かい数値を読み上げない） |
| 2. 事実確認 | 動画の作り方 2026年11月（主張 15 個を原典で）、デジタル民主主義の川 60 秒版（講演の数字を一次ソースで） |
| 3. 声 | クオリアさん pilot（SAPI）→ makingof（AivisSpeech）、動画の作り方（三つの声の聞き比べとイントネーション）、THINKLET（ずんだもん） |
| 4〜6. 時刻表・描画・引用 | ショーリール 15 秒（型の最初）、Gyazo の 47 秒（軽い描画で作り直しを回す）、動画の作り方（引用 3 本を ffmpeg で重ねる）、tsugigami の広告動画（実アプリの録画と生成動画の合成） |
| 8. レビュー | 動画の作り方（出先でスマホ、Google ドキュメントのコメント）、tsugigami のメイキング（原稿の書式をそのまま合成の入力に） |
| 9. 公開 | デジタル民主主義の川 60 秒版（X は最初のコマがサムネイル）、tsugigami の広告動画（生成の人物で AI の使用「はい」） |

## Open Questions

- 公開先が未確認の 3 件（ショーリール 15 秒、デジタル民主主義の川 60 秒版、34 分の事前動画）の URL。作業場の README・UPLOAD.md（~/nishio-showreel、~/democracy-river-video）か西尾のチャンネルで確かめて足す
- このページに載せていない作品と理由は、2026-11-10 の log.md の項に書いた

## Updates
