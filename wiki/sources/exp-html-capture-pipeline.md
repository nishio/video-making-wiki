---
type: source
summary: MacBook で 2026-09 に作った短い動画 4 件に共通する作り方。canvas に時刻の関数として描き、headless Chrome で 1 コマずつ撮って ffmpeg に流し、BGM は numpy で合成して最後に重ねる
video_types: [any]
sources:
  - ~/nishio-showreel/README.md, src/capture.mjs, src/audio.py, 60s/src/capture60.mjs
  - ~/democracy-river-video/README.md, src/capture.mjs, src/thumb.mjs, en/tts.py, en/timing.py, en/mix.py
  - ~/gyazo-resumption-video/README.md, src/capture.mjs, src/audio_hype2.py, out/render*.log（commit 3cd64c8）
  - ~/words-as-public-goods-video/README.md, src/capture.mjs
  - llm-wiki analyses/講演の短尺動画化では制約は配信面から来る-20260930.md
---

# HTML を描いて撮る動画の作り方（MacBook, 2026-09）

[[exp-nishio-showreel]]（2026-09-25）で作った型を、[[exp-democracy-river-video]]・[[exp-gyazo-resumption-video]]・[[exp-words-as-public-goods-video]]（いずれも 2026-09-29〜30）がそのまま流用した。動画編集ソフトは使っていない。全部コードで、AI（Claude Code）が書いて回した。

## 骨格

```
src/xxx.html   canvas に renderFrame(f) で 1 コマ描く（f はフレーム番号）
src/capture.mjs headless Chrome で renderFrame(f) → PNG → ffmpeg の標準入力へ
src/audio.py   numpy で BGM を合成 → out/audio.wav
ffmpeg         無音の映像 + audio.wav を重ねる
```

再生成の手順は各 repo の README にある。典型は次の形（`~/nishio-showreel/README.md` より）。

```sh
cd src
python3 audio.py                      # -> ../out/audio.wav
node capture.mjs stills 2.9 11.8      # 確認用の静止画（秒で指定）
node capture.mjs video                # -> ../out/video_noaudio.mp4
ffmpeg -i ../out/video_noaudio.mp4 -i ../out/audio.wav -c:v copy -c:a aac -b:a 256k -shortest ../out/xxx.mp4
```

## 描画側（HTML）の決まり

- **`renderFrame(f)` は時刻だけの純関数にする**。前のコマの状態を持たないので、どのコマからでも描ける。これで「秒を指定して静止画を撮る」確認ができる（`capture.mjs stills`）。粒子の配置などの乱数は seed 固定の自前の乱数（mulberry32 など）で作る（`~/nishio-showreel/src/reel.html`）。
- `window.ready` を Promise にして、フォントの読み込み（`document.fonts.load`）と、文字を粒子に分解する下準備が済むまで撮り始めない。
- 尺・fps は HTML 側に持たせ、`window.FPS`・`window.DUR` や `window.TOTAL_FRAMES` で撮る側に渡す（gyazo・words 版）。最初の showreel はフレーム数 900 を `capture.mjs` に直書きしていて、尺を変えるたびに直す必要があった（democracy-river では `FRAMES` 環境変数で上書き）。
- 場面の切り替えは時刻表で持つ（showreel の `TL = [[開始, 長さ, from, to, ずらし, イージング], ...]`、gyazo の `HITS = [[時刻, 強さ], ...]`）。音の側も同じ時刻を使う（下の「音」）。
- 文字は Hiragino Sans など Mac のシステムフォント。別の機械で撮ると変わる。

## 撮る側（capture.mjs）

- `puppeteer-core` で Mac にある Google Chrome を headless で起動し、`--force-device-scale-factor=1` で画面の倍率を 1 に固定。viewport を動画の解像度（1920×1080、縦長なら 1080×1920 や 1080×1350）にする。
- 1 コマごとに `page.evaluate` の中で `renderFrame(f)` を呼び、`canvas.toDataURL('image/png')` を受け取って ffmpeg の標準入力へ書く。ffmpeg は `-f image2pipe -framerate 60 -i - -c:v libx264 -preset slow -crf 16 -pix_fmt yuv420p`。書き込みが詰まったら `drain` を待つ（これがないとメモリが膨らむ）。
- **画像ファイルを描く場合は `file://` で開かない**。canvas が tainted になり `toDataURL` が失敗する。1 分版 showreel では `capture60.mjs` の中に小さな HTTP サーバーを立て、`http://localhost:<port>/` から開いた（`~/nishio-showreel/60s/README.md`）。words 版もこの形を流用した。
- `node_modules`（puppeteer-core）は後の 3 件では `~/nishio-showreel/src/node_modules` へのシンボリックリンクで済ませた。

### 撮る時間（実測）

- 粒子 2400 個＋ぼかしの重ね描きの showreel 系: 1 分版で「約10分」、60 秒の democracy-river も「約10分」（各 README）。
- 文字と図形だけの gyazo ハイテンポ版（47 秒・60fps）: エンコードのログでは 2,820 コマを約 38 秒、毎秒約 74 コマ（`out/render_hype.log`）。
- 描画の重さで 10 倍以上違う。作り直しの回数が多い制作ほど、軽い描画のほうが回せる。

## 確認のしかた

- 静止画: `node capture.mjs stills <秒...>` で `stills/` に PNG（各 README で「確認用の静止画」）。全編を撮る前に、山場の秒だけ撮って見る。
- 全場面のコンタクトシート（`sheet.png`）を作って一覧で見る（words・showreel）。
- 西尾には「finder で開いて」と言われて、完成した mp4 を Finder で開いて渡すことが多かった（各 session の西尾の発言、2026-09-25〜30）。

## 出力の版

| 用途 | 作り方 | 例 |
|---|---|---|
| マスター | 1080p60、crf 16〜17 | showreel 15 秒で約 47MB |
| 送付・軽量 | `_web`、30MB 未満 | showreel |
| X 投稿 | `-crf 23 -r 30 -c:a aac -b:a 160k -movflags +faststart` | democracy-river 60 秒で 17MB |
| 縦長ショート | HTML の canvas と W/H だけ変えた別ファイル（`reel_v.html`） | showreel |

## 音（numpy で合成）

- 48kHz ステレオの配列に、関数で作った音を時刻を指定して足していく（`add(sig, start, gain, pan)`）。音色は kick・clap・hat（ノイズを高域通過）・impact（下降するサイン波＋ノイズ）・whoosh・riser・pad（デチューンしたのこぎり波）・pluck など。フィルタは FFT で周波数領域に掛ける簡易版（`~/nishio-showreel/src/audio.py`）。
- 仕上げ: 減衰するノイズとの畳み込みで簡易リバーブ、`tanh` で軽く歪ませて正規化、頭と尻にフェード。
- **120BPM（1 拍 0.5 秒、1 小節 2 秒）に固定し、場面の切り替えを小節の頭に置く**。映像の時刻表と音の時刻表が同じ格子に乗るので、合わせる作業がほぼ要らない。4 件とも 120BPM。
- 2 版目の作り方（gyazo `src/audio_hype2.py`）: 楽器ごとの bus に分け、スーパーソウ（7 声のデチューン）のコードとリード、キックに合わせたサイドチェイン、ビルド（スネアロール＋フィルタ上昇＋ライザー）→ ドロップを、映像の山の秒に合わせる。
- 落とし穴: Homebrew の Python 3.13/3.14 の numpy が壊れていて、words 版では `/opt/homebrew/bin/python3.11` で回した（`~/words-as-public-goods-video/README.md`）。
- YouTube の説明文には「音楽: オリジナル（プログラムで合成）」と書いた。権利の申告対象がない。

## 声を入れる場合（democracy-river 英語版）

- 場面ごとの台本を JSON に置き（`[id, 元の開始秒, 元の終了秒, 文]`）、OpenAI `gpt-4o-mini-tts`（voice: onyx）で場面ごとに wav を作る。既にある wav は作らない（`en/tts.py`）。
- `ffmpeg -filter:a atempo=1.12` で少し速め、各場面の実時間を「声の長さ＋0.6 秒」と「元の場面の長さ」の長いほうにする（`en/timing.py`）。
- `adelay` で各場面の頭＋0.3 秒に声を置いて `amix`、BGM は `sidechaincompress` で声の間だけ下げ、`alimiter`（`en/mix.py`）。最後に `loudnorm=I=-16:TP=-1.5:LRA=11`。

## サムネイル

- HTML 側に `renderThumb()`（または `thumb()`）を用意し、`thumb.mjs` で 1 枚撮る（`~/democracy-river-video/src/thumb.mjs`）。YouTube 用は 1280×720 の jpg に縮める。
- **X に出すものは最初のコマにサムネイルを焼き込む**（X では投稿者がサムネイルを選べないことが多く、最初のコマが使われる）。democracy-river 英語版は最初の 0.2 秒をサムネイルにして 0.7 秒までに本編へ溶かし、gyazo は最初の 2 秒をサムネイルにした。

## 説明文・投稿文（UPLOAD.md / POST.md）

各 repo の `youtube/UPLOAD.md` が同じ形をしている。

- 冒頭に、上げるファイル名・サムネイル・公開範囲・視聴者（子ども向けではない）・カテゴリ（科学と技術）・言語
- タイトル、「ここから下をそのまま貼る」説明（要旨 → チャプター → ▼ 出典（画面の主張ごとに URL）→ 画像クレジット → 音楽 → ▼ Web）、タグ
- 「メモ（貼らない）」に、数字の出典 wiki ページや、言い方の条件（「速度のみの比較」など）
- **YouTube のチャプターは 1 つでも 10 秒未満があると全部無効になる**ので、場面ではなく 10 秒以上の塊で切る（gyazo・democracy-river の UPLOAD.md）
- 縦長で 60 秒以内ならショート扱いになる。ショートの説明欄のリンクは押せないことがあるので、関連動画で長い版を指す（`~/nishio-showreel/youtube/UPLOAD_15s.md`）
- X の投稿文は、リンクを本文に入れずリプライに置く（`tweet.md`・`POST.md`）。リンク付きの投稿は表示されにくい、という前提で書いた（効果は測っていない）

## 画面に出す事実の扱い

4 件とも、README に「画面の主張 → 一次ソース」の表を置いた。役割語（主催・アドバイザー・共著など）は一次ソースで確かめたものだけ出し、確かめられないものは弱めるか出さない。講演・トークにない数字や締めの言葉を足した場合は「動画で新たに足したもの」と明記した（words 版）。発信物では「AI」と書かずモデル名を出す（[[exp-gyazo-resumption-video]] の西尾の指摘から。grasp-nishio `wiki/rules/name-the-model-not-ai.md`）。

## Open Questions

- この型は Mac の Chrome と Hiragino フォントに依存している。galleria や CyEC2（Linux）で同じ絵が出るかは試していない。
- 撮るのは 1 コマずつ PNG を経由するので遅い。粒子系で 1 分に約 10 分かかった。WebCodecs や canvas の録画など速い経路は試していない。
- 音の合成は毎回 Claude が関数を書き直している（showreel → 60s → gyazo で別ファイル）。共通の部品にまとめてはいない。

## Updates

### 2026-11-09 サーベイ: 古くなった事実

- 「縦長で 60 秒以内ならショート扱い」は、2024-10-15 以降 YouTube Shorts が「正方形か縦長で 3 分以内」になった（[[web-google-youtube-abcds]]）
- X のヘルプはウェブからのアップロードを 40fps までとしている（[[web-x-video-ads-best-practices]]）。60fps の書き出しを X に出したときの実際の挙動は未確認
- 外の Opus 5.5 期の作り手は 6〜8 プロセスで並列に撮っている。Remotion も純関数であることを並列化に使う（[[after-opus55]]、[[web-remotion]]）

