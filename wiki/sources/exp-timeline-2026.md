---
type: source
summary: 西尾の機械での動画制作を時系列に並べたもの（2026-07〜10）。2026-09-22 の Opus 5.5 の公開を境に、galleria の Codex と Pillow・TTS・ローカル動画モデルの組み立てから、Claude（Opus 5.5）が canvas に描くモーショングラフィックスへ移り、9/25〜9/30 の 6 日に 10 本前後が出た
video_types: [any]
sources:
  - 西尾との対話（2026-11-09）「クオリアさんの解説動画は8月のもので、その後にOpus5.5がすごいとなって自己紹介動画を作ったんだよね？」
  - exp-*.md（各行の出典）
  - tweet-memo sources/movez-opus-motion-design-course.md（Opus 5.5 の公開日 2026-09-22）
---

# 制作の時系列（2026-07〜10）

西尾の言葉（2026-11-09）: 「クオリアさんの解説動画は8月のもので、その後にOpus5.5がすごいとなって自己紹介動画を作ったんだよね？」

この wiki の `exp-*` は制作ごとに書かれていて、どの順に何が起きたかが見えなかった。ここに並べる。

## 時系列

| 時期 | 制作 | 誰が・どの道具で | 出典 |
|---|---|---|---|
| 2026-07〜 | 経文・真言の同期解説（約 45 秒・3 回反復） | Mac（一部 galleria）。制作パターンの記録は 2026-08-12 | [[exp-sutra-videos-overview]]、[[exp-sutra-sync-subtitles]] |
| 2026-08-11〜12 | クオリアさん解説 pilot（93 秒）・メイキング（109 秒） | galleria で Codex（journey の記録では GPT-5.6 Sol Ultra）が、Pillow のスライド＋SAPI／AivisSpeech＋PyAV。動きの候補に Wan2.2 | [[exp-qualia-video]] |
| 2026-08〜09 | クオリアさん journey（6 分 33 秒）、H3・Live2D の版 | galleria。FLUX.2・Wan2.2・VOICEVOX | [[exp-qualia-video]]、[[exp-qualia-h3-live2d-galleria]] |
| 2026-08-27 | THINKLET の読書支援のデモ（52 秒） | 西尾が Premiere Pro で手作業。ずんだもんのナレーション 3 本 | [[exp-thinklet-reading-demo-video]] |
| 2026-09-09 前 | LT の準備（8 分） | 台本をずんだもんに読ませて尺を測った | [[exp-lt-20260909]] |
| **2026-09-22** | **Opus 5.5 の公開** | 公開直後に「コードで描くモーション動画」が流行した（tweet-memo の Movez の記事） | [[web-movez-opus-motion-design-course]] |
| 2026-09-25 | showreel 15 秒（日・英）、1 分版 | Mac の Claude（Opus 5.5）。canvas の `renderFrame(f)` を headless Chrome で 1 コマずつ撮り ffmpeg、BGM は numpy で合成。依頼の 15 秒版は流行の一行プロンプトの形（下） | [[exp-nishio-showreel]]、[[exp-html-capture-pipeline]] |
| 2026-09-26〜27 | 真言言えるかな、般若心経のアゲアゲ版・漢字版・カノン v1 | Mac。YouTube・X に公開 | [[exp-sutra-hype-editions]]、[[exp-sutra-songs-on-music]] |
| 2026-09-29〜30 | 講演 34 分 → X 用 60 秒（日・英） | 同じ方式 | [[exp-democracy-river-video]] |
| 2026-09-30 | Gyazo 配信再開（v1 2 分 52 秒 → v3 47 秒）、Words as Public Goods（50 秒・4:5）、Polis のエヴァ OP 様式（55 秒、停止して galleria へ） | 同じ方式 | [[exp-gyazo-resumption-video]]、[[exp-words-as-public-goods-video]]、[[exp-polis-magi-op]] |
| 2026-10-06 | LLM Wiki 1 分解説シリーズの構想と台本案（動画はまだない） | — | [[exp-llm-wiki-explainer-series]] |
| 2026-10〜11 | 般若心経のカノン v2 の公開準備など | Mac | [[exp-sutra-songs-on-music]] |

公開日・制作日は各 exp ページの記録による。月単位で書いたものは、記録に日が無いもの。

## Opus 5.5 の公開で何が変わったか

- **15 秒版の依頼文は、流行していた一行プロンプトそのものだった**: 「make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.」に「Thema: 西尾泰和(NISHIO Hirokazu)の活動・功績」を足したもの（[[exp-nishio-showreel]]）。Movez の記事は、この「履歴書用のショーリール」の一行が効くのは、ジャンルの文法をモデルが既に知っていて中身を間違えようがないからで、「エンジンの試験にはなるが、アイデアの試験にはならない」と書いている（[[web-movez-opus-motion-design-course]]）
- **作る主体と道具が変わった**: 8 月の解説動画は、galleria の Codex がスライド画像（Pillow）と音声を並べ、ローカルの画像・動画モデルで絵を足す組み立てだった。9/25 以後は、Mac の Claude が 1 枚の HTML の canvas に時刻の純関数として全部を描き、音も同じ時間軸で合成する方式になった。この方式は 9/25 の showreel で作り、その後の 4 本が流用した（[[exp-html-capture-pipeline]]）。Movez の記事が挙げる流行の作り方（`seek(t)`、headless ブラウザ、ffmpeg）と独立に一致していた
- **作る速さ**: 9/25〜9/30 の 6 日で、showreel 4 版、経文の 4〜5 本、川 2 版、Gyazo 3 版、Words、Polis が出た（上の表）。8 月のクオリアさんは 3 本に数週間かかっている。ただし題材も尺も目的も違うので、道具の差だけとは言えない
- **型が promo に寄った**: 9/25 以後の制作は、ほとんどが X・YouTube に流す短いもの（promo）だった。8 月のクオリアさんは talk だった。この偏りが道具の向き不向きから来たのか、ちょうど発信したい題材が溜まっていたからかは記録から分からない
- **変わらなかったこと**: 人間の評価が要ること。一回目は「しょぼい」（Polis）、「展開が遅くてだるい」（Gyazo）で、直したのは参照の文法と、自分のフレームを見る批評のループだった（[[exp-polis-magi-op]]、[[exp-gyazo-resumption-video]]、[[web-movez-opus-motion-design-course]]）

## Open Questions

- 8 月の galleria の方式（Codex＋Pillow＋TTS）で、9 月の canvas の方式のような promo を作ろうとしたことはあるか。無いなら、方式の差と題材の差を分けられない
- 9 月の方式で talk（ナレーションが主の解説）を作ったらどうなるか。democracy-river の英語版（87 秒、TTS のナレーション付き）が一番近い（[[exp-democracy-river-video]]）
