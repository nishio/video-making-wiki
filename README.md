# video-making-wiki

動画を作るための知識を整理する LLM Wiki。目的は「作るための手段を調査サーベイし、今後の表現手段を増やすこと」（西尾、2026-11-09）。動画の型ごとの作り方、MacBook と GPU 機（galleria）での制作経験から得た手法と落とし穴、ネット上の知見のサーベイを、Claude（Claude Code）が書いて保っている。

## この wiki から作った動画

**動画の作り方 2026年11月**（6 分 36 秒）— 動画は少なくとも三通り（宣伝・解説・発表の中で流す）あり、通りごとに作り方の正解が逆になることがある。2026 年 11 月の時点のノウハウを、三通りそれぞれについてまとめた解説。

[![動画の作り方 2026年11月](https://img.youtube.com/vi/IDkRFwiFXFI/hqdefault.jpg)](https://youtu.be/IDkRFwiFXFI)

**「動画の作り方」の作り方**（5 分 51 秒）— 上の動画をどう作ったかを、人が決めたことと AI がしたことに分けて見せるプロセス動画。

[![「動画の作り方」の作り方](https://img.youtube.com/vi/Ezzcld2rbL8/hqdefault.jpg)](https://youtu.be/Ezzcld2rbL8)

上の 2 本を作った経験は [wiki/sources/exp-explainer-video-2026-11.md](wiki/sources/exp-explainer-video-2026-11.md)。

**広告動画を AI と作った ― 画面は本物、人物は生成**（6 分 40 秒）— 手書きノートの Web アプリ tsugigami の 26 秒の広告動画（[YouTube ショート](https://youtube.com/shorts/1qKsNrwIxCk)）を、アプリの画面は本物の録画、人物は生成でどう作ったかを見せるメイキング。上のプロセス動画の作りを写して作った 3 本目。

[![広告動画を AI と作った ― 画面は本物、人物は生成](https://img.youtube.com/vi/aXGEaLMI7Fs/hqdefault.jpg)](https://youtu.be/aXGEaLMI7Fs)

作った経験は [wiki/sources/exp-tsugigami-making.md](wiki/sources/exp-tsugigami-making.md)、広告動画そのものは [wiki/sources/exp-tsugigami-promo.md](wiki/sources/exp-tsugigami-promo.md)。

3 本とも、台本と映像を描くコードは Claude Opus 5.5（人が確認・修正）、声は AivisSpeech（まお）。広告動画の人物の映像は Grok Imagine で生成した。

## 入口

| 読みたいこと | ページ |
|---|---|
| 解説動画をこの順で作る手順と、各段で踏んだ失敗と直し方 | [wiki/analyses/talk-video-making-2026-11.md](wiki/analyses/talk-video-making-2026-11.md) |
| 動画の三つの型の違い | [wiki/concepts/three-video-types.md](wiki/concepts/three-video-types.md) |
| 型ごとのページ | [promo（プロモーションムービー風）](wiki/concepts/promo.md)・[talk（解説プレゼン風）](wiki/concepts/talk.md)・[embed（プレゼンの中に埋め込んで使う特定概念を解説するもの）](wiki/concepts/embed.md) |
| 西尾の過去作品の事例紹介 | [wiki/entities/nishio-works.md](wiki/entities/nishio-works.md) |
| 解説動画 3 本の比較 | [wiki/analyses/talk-three-videos-2026-11.md](wiki/analyses/talk-three-videos-2026-11.md) |
| 全ページの一覧 | [wiki/index.md](wiki/index.md) |
| 作業の記録 | [wiki/log.md](wiki/log.md) |

## 構造と運用

```
wiki/concepts/   概念・型のページ
wiki/sources/    ソースの要約（exp-* は西尾の制作経験、web-* はネット上の知見）
wiki/analyses/   問いから生まれた考察・手順
wiki/entities/   作品などの一覧
scripts/lint_wiki.py  リンク切れ・孤立・未登録などの検査
```

ページの書き方と操作（ingest・query・lint）は [CLAUDE.md](CLAUDE.md)。文献の主張は「〜と書いている」と書き、確かめたこととは分けている。
