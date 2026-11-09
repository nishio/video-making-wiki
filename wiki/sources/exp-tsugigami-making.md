---
type: source
summary: tsugigami の広告動画のメイキングの解説動画（6 分 40 秒、2026-11-09）を、プロセス動画の作り（まおの声、声の長さから時刻表、canvas の図と字幕、引用は ffmpeg で枠に重ねる）を写して作った経験。解説動画の 3 本目。行の範囲と画面の対応を表（VIS）にし、行の中の語の時刻を「語の手前までを別に合成した長さ」で測り、引用の素材ごとに使う長さを決めた。書き出しは四回
video_types: [talk]
sources:
  - Mac の ~/tsugigami-promo/making/（README.md、script-draft1.md、tts/build_lines.py・synth.py・cues.py・cues.json・word_overrides.json、src/build_timeline.py・explainer.html・capture.mjs、compose.py、assets.py、youtube/UPLOAD.md）。CyEC2 の ~/handoffs-from-mac/2026-11-09-talk-materials/tsugigami-promo/making/ の写しで読んだ（音・映像・画像・out/ は写していない）
  - 同 gitlog/tsugigami-promo-making-mtimes.txt（making/ に commit は無く、ファイルの更新時刻の一覧）
  - exp-tsugigami-promo.md（広告動画そのもの。メイキングの材料の時系列）
  - exp-explainer-video-2026-11.md（写した元のプロセス動画）
---

# tsugigami の広告動画のメイキングの解説動画（2026-11-09）

公開: https://youtu.be/aXGEaLMI7Fs （6 分 40 秒、西尾が YouTube Studio から投稿）

題材の広告動画は [[exp-tsugigami-promo]]（26 秒、YouTube ショート）。このページはそのメイキングの解説動画で、型は talk（[[talk]]）。同じ日に作った解説動画 3 本の 3 本目で、手順にまとめたものは [[talk-video-making-2026-11]]、3 本の比較は [[talk-three-videos-2026-11]]。

これまで [[exp-tsugigami-promo]] の Updates に 4 行で書いていた。プロセス動画の作りを写した所と、写した上で足した所（画面の表、行の中の語の時刻、引用の素材の長さ）が 3 本の比較の材料になるので、独立したページにした（2026-11-09）。

## 起点と時刻

- 西尾「解説動画を作る上で時系列の出来事は記録しておきたい」（log.md 2026-11-09 19:25）。広告動画の会話記録とファイル時刻から [[exp-tsugigami-promo]] の「時系列」を作り、それを材料にした（README.md「材料の時系列は video-making-wiki sources/exp-tsugigami-promo.md の「時系列」」）
- making/ に commit は無い。ファイルの最終更新の時刻は 19:35（tts/synth.py）〜 20:38（README.md・youtube/UPLOAD.md）。この wiki への公開の file back は 20:50（log.md）。更新の時刻なので、作り始めの時刻は分からない
- 書き出しは四回（README.md の draft1〜draft4）

## 作り（README.md の表のまま）

フォーク A の ~/video-making-process の作りを写して使う（README.md「読むだけで、あちらは触らない」）。

```
tts/build_lines.py    script-draft1.md の〔mN_NN〕の行 → tts/lines.json（読みは READ でかなに開く）
tts/synth.py          AivisSpeech「まお」（galleria の Engine。Mac から ssh -L 10101 で）→ tts/wav/
src/build_timeline.py 声の長さから時刻表。行の範囲ごとの画面（VIS）→ src/timeline.js, out/overlays.json, out/concat.txt
src/explainer.html    1920x1080 の canvas。見出し・枠の名札・図・字幕
src/capture.mjs       stills <秒...> | video → out/video_noaudio.mp4
compose.py            引用を枠に重ね（短い素材は繰り返す）、ナレーションを -14 LUFS で載せる。stills <秒...> は確認用
assets.py（..）       素材: 昔の版のコマ・切り抜き、四隅を追う枠の動画、インクの前後、12 本の一覧、版の並び → assets/
```

- tts/synth.py はプロセス動画のものと同じファイル（diff で差が無い）。word_overrides.json（語ごとのイントネーションの指定）は、本編で西尾が選んだ指定に「グロックイマジン…」を一つのアクセント句にする 5 行を足したもの
- 原稿は Google ドキュメントに置いた（README.md の ID）。原稿の行頭の〔m0_01〕を、build_lines.py が正規表現 `^〔(m\d_\d+)〕 (.+)$` でそのまま読む。直し用の原稿の書式と、合成の入力の書式が同じ
- 原稿には【画面】の行（映すものの案、読まない）が節ごとにある（script-draft1.md）

## 3 本目で足したもの

プロセス動画の写しから変えた所（ファイルの差から）。

### 行の範囲と画面の表（VIS）

- build_timeline.py に `VIS = [(最初の行, 最後の行, [素材...], 図), ...]` の表を置き、行の範囲ごとに、重ねる素材（映像・画像）と canvas で描く図（`two`・`three`・`list`・`machines`・`memo`・`settings`・`quote`）を決める。本編・プロセス動画は引用ごとに `by["s5_01"]["start"]` のように時刻を書いていた
- 素材は `AREA`（`one`・`L`・`R`・`wide` など 9 つの枠）に、ffprobe で取った縦横比のまま収める（`fit`）
- 30 行の VIS のうち 10 行が、昔の版と完成版（直す前と後）を左右（`L`・`R`、`Ltxt`・`Rtxt`）に並べる（v1 と完成版、v4 と v6 など）。最終のファイルでの数で、一回目からそうだったかは写しからは分からない
- 画面は行の頭の 0.2 秒前に切り替わる（`by[a]["start"] - 0.2`）

### 行の中の語の時刻（cues.py）

- 西尾の直しで「3 つの表示の時刻のずれ」を直すために作った（README.md 二回目）。一行の中で 3 つの項目を順に出す場面（「人が決めたことと、AI がしたこと」「実写は撮らない。iPad の画面に…」「普段使いのラップトップ、…」など 10 か所）
- 測り方: 行の頭からその語の手前までを別に合成した長さ × （行の実際の長さ ÷ 行全体を別に合成した長さ）。末尾の無音のぶん 0.1 秒を引く（cues.py のコメントとコード）
- 理由: AivisSpeech の audio_query はモーラの長さを返さない（0）（README.md）。合成は毎回少し違うので、比で直している
- 結果は tts/cues.json（例 `"three2": {"id": "m1_06", "at": 4.072}`）。build_timeline.py が行の頭の時刻に足して `window.CUE` に書く
- 合っているかの確かめは西尾の目で、測った記録は写しに無い

### 引用の素材の長さ（compose.py）

- 一回目は、行が長いと引用の動画が素材の先（別の場面やロゴ）まで流れた（README.md）
- 素材ごとに使う長さ `dur` を決め、それを超える行では繰り返す（`-stream_loop -1`）。締めの完成版は最後のコマで止める（`hold`、`tpad=stop_mode=clone`）
- 引用は先に区間を切り出して枠の大きさの mp4 にしてから重ねる（`seg`）。本編・プロセス動画は重ねるときに `-ss` と `trim` で切っていた
- `python3 compose.py stills <秒...>` で、canvas の静止画に引用の素材のそのコマを重ねた確認用の静止画を作る。本編・プロセス動画の stills は canvas だけで、引用の枠は空だった

## 声と読み

- 声は本編・プロセス動画と同じ AivisSpeech「まお」（speaker 888753763）。聞き比べはしていない
- 読みの直し（README.md）: 公開中（コオカイナカ → こうかいちゅう）、紙を継ぐ（シオツグ → かみを）、Image 2.0（ツウポイントゼロ → ニーテンゼロ）。全行のカナを audio_query で確かめた
- 西尾の直し（README.md 二回目・四回目）: 開けば → ひらけば、Grok Imagine を一塊に（word_overrides で一つのアクセント句に。句の区切りの読点も一拍として数える）、四つの辺（あたり → へん）
- build_lines.py の READ（表記 → 読み）は 24 組。プロセス動画の READ（22 組）と同じ表記は AI・YouTube・GPU の 3 組だけで、残りはこの動画の語

## 西尾の直し（四回の書き出し）

| 版 | 長さ | 直したこと（README.md） |
|---|---|---|
| draft1 | — | 引用の動画が場面を越えて流れていた → 素材ごとの長さと繰り返し、締めは最後のコマで止める |
| draft2 | 6:43 | スマホ用（720p・crf 33、7.0MB）を Drive へ |
| draft3 | 6:40 | 開けば → ひらけば、3 つの表示の時刻のずれ（cues.py）、Grok Imagine を一塊に、文字の解説の見本を行ごとに出し分け、「美人にして」の指示は隠す |
| draft4 | 6:40 | 四つの辺（あたり → へん）。西尾「OK、それでリリースしましょう」 |

- 「美人にして」の指示を隠した理由は西尾「ムッとする人がいそう」（[[exp-tsugigami-promo]] の Updates）。引用を「最後の人、静止画は微妙」「動画がいいな」に変えた。Google ドキュメントの原稿は元のまま（README.md）

## 公開（youtube/UPLOAD.md）

- -14 LUFS に合わせた写しを出した（-13.9 LUFS・ピーク -2.3 dBFS）。compose.py の書き出しは -15.1 LUFS だった（README.md draft2）。写しの作り方は写しに無い
- サムネイルは 5 節の「四隅を追う赤い枠／はめ込んだ結果」の画面を、字幕を描かずに撮ったもの（capture.mjs の `NOSUB`）
- チャプター 9 個、どれも 10 秒以上（いちばん短いのは「結び」18 秒）
- AI の使用: はい。広告動画の、生成 AI で作った写真のようにリアルな女性の映像を引用している
- 説明欄の「使ったもの」に Claude Opus 5.5、Grok Imagine Image 2.0・Video 1.5、FLUX.2 Klein、Yomogi、AivisSpeech（まお）

## Open Questions

- cues.py の比で直した時刻が、実際の声の語の頭とどれだけずれるかは測っていない（西尾が見て直しを止めた、まで）
- 書き出しが -15.1 LUFS になる理由（compose.py はナレーションだけを一回の loudnorm で -14 にしている）と、写しを -14 に合わせた方法は写しに無い

## Updates
