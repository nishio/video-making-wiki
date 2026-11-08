---
type: source
summary: ffmpeg だけで動画のコンタクトシート（コマの一覧画像）を作るための公式文書の記述。select（式で間引く、scene は 0〜1 で「0.3〜0.5 と比べるのがまず妥当」）、tile（格子に並べる。連続出力では -fps_mode passthrough が要る）、drawtext（%{pts:hms} と %{n} で時刻とフレーム番号を焼く）、thumbnail（n コマごとに代表を選ぶ）、scdet（場面転換の点数を metadata に出す）。経験では動きの多い素材で scene が効かず、1 秒ごとのサムネイル列を人に見せる方が一発で決まった
video_types: [any]
url: https://ffmpeg.org/ffmpeg-filters.html
author: FFmpeg project
published: unknown（git master から生成。2026-11-09 取得。最新安定版は 9.0.2、2026-09-18）
retrieved: 2026-11-09
sources:
  - https://ffmpeg.org/ffmpeg-filters.html （20.17 select・aselect、11.259 tile、11.76 drawtext、11.258 thumbnail、11.227 scdet の節を読んだ）
---

# ffmpeg でコンタクトシートを作る（select・tile・drawtext・thumbnail・scdet）

## 何の文献か

- ffmpeg の公式文書（フィルタの説明と例）。コンタクトシートという機能があるわけではなく、フィルタを組み合わせる。下の「着手の仕方」のコマンドは文書の例を組み合わせたもので、組み合わせた形は未検証
- 経験側には既に「1 秒ごとのサムネイル列を HTML にして人に見せると一発で決まる」（[[exp-galleria-ffmpeg-measurement-and-delivery]]）と、HTML の作り方での「全場面のコンタクトシート（sheet.png）」（[[exp-html-capture-pipeline]]）がある。このページはそれを ffmpeg だけで作る形

## 書いてあること

### select（20.17）

- 式が 0 でないコマを通す。使える定数: `n`（入力のコマ番号、0 から）、`selected_n`、`t`（秒）、`prev_selected_t`、`pict_type`、`scene`
- `scene`: 「value between 0 and 1 to indicate a new scene; a low value reflects a low probability for the current frame to introduce a new scene」
- 文書の例: `select='not(mod(n\,100))'`（100 コマに 1 枚）、`select='isnan(prev_selected_t)+gte(t-prev_selected_t\,10)'`（最低 10 秒おき）、`select='eq(pict_type\,I)'`（I フレームだけ）
- 「Create a mosaic of the first scenes: `ffmpeg -i video.avi -vf select='gt(scene\,0.4)',scale=160:120,tile -frames:v 1 preview.png`」「Comparing scene against a value between 0.3 and 0.5 is generally a sane choice」

### tile（11.259）

- 「Tile several successive frames together」。`layout`（列x行、既定 6x5）、`nb_frames`、`margin`、`padding`、`color`（空きの色、既定 black）、`overlap`、`init_padding`
- 例: `ffmpeg -skip_frame nokey -i file.avi -vf 'scale=128:72,tile=8x8' -an -fps_mode passthrough keyframes%03d.png` と、「The -fps_mode passthrough is necessary to prevent `ffmpeg` from duplicating each output frame to accommodate the originally detected frame rate」

### drawtext（11.76）

- `text` の中の `%{...}` を展開する（expansion=normal が既定）。`%{pts}` は「The timestamp of the current frame」で、第 1 引数 `hms` で「[-]HH:MM:SS.mmm」、第 2 引数で時刻にずらしを足せる。`%{n}`（`frame_num`）は「The frame number, starting from 0」。`%{pict_type}`、`%{metadata:key}` も使える
- エスケープは「up to four levels of escaping」になりうるので、`textfile` を使えば避けられる、と書く
- `box=1`・`boxcolor`・`boxborderw` で文字の下に箱。`fontfile` は fontconfig が無いビルドでは必須

### thumbnail（11.258）と scdet（11.227）

- thumbnail: 「Select the most representative frame in a given sequence of consecutive frames」。`n`（既定 100）コマごとに 1 枚。大きな n はメモリを食う
- scdet: コマごとに `lavfi.scd.mafd`・`lavfi.scd.score` を、閾値を超えたコマに `lavfi.scd.time` を付ける。`threshold`（既定 10、「Good values are in the [8.0, 14.0] range」、最大変化に対する百分率）、`sc_pass=1` で転換のコマだけ次へ流す

## この wiki への含意

- **経験との一致と注意**: 文書は scene に 0.3〜0.5 を勧めるが、経験は「動きの多い素材では 0.15 でほぼ全コマが通る」「構図が変わらず中身だけ変わる境目は数値に出ない」と書く（[[exp-galleria-ffmpeg-measurement-and-delivery]]）。**主は等間隔（fps=1 など）のシート、scene・scdet のシートは補助**、が経験と文献の両方に合う
- **時刻の焼き込みは pts で**: 経験は「秒は pts でしか取れない（opencv の fps × 番号は VFR でずれる）」と書く。drawtext の `%{pts\:hms}` は pts そのものなので、この教訓に沿う。番号も `%{n}` で併記すれば「サムネイル一覧にフレーム番号を併記しておくと救える」と同じことになる
- **drawtext の置き場所**: `select` や `fps` の**前**に drawtext を置くと、`%{n}` は元の動画のコマ番号になる（後ろに置くと間引いた後の通し番号になる）。前に置くと全コマに描くので遅い（文書の定義からの推論）
- **型ごと**: promo（短尺・カットが多い）は 0.5 秒ごと、talk（長い）は 5〜10 秒ごと、embed（流しっぱなしの 30〜60 秒）は 1 秒ごとのシートが一覧しやすい（推測）。どれも「批評役のモデルにコマを見せる」用途（[[after-opus55]] の「モデルは通しで見られない」）の入力にもなる
- 閃光の候補（短時間に明暗が反転する場面）は、等間隔のシートでは見落とす。閃光の検査は別の道具で（閃光の担当のページ）

## 着手の仕方（未検証。galleria で確かめる）

- **何が表現できるようになるか / 効く型**: 書き出した動画の全体を 1〜数枚の画像で見渡す。人にもモデルにも渡せる（any）
- **機械・入れるもの**: galleria WSL の ffmpeg。日本語を焼かないなら英数字のフォント 1 つ（WSL の distro が未確認なので、パスは `fc-list | head` で探す。下の DejaVu のパスは推測）。費用・アカウントなし
- **成熟度**: どのフィルタも ffmpeg に長く入っている。`-fps_mode` は 5.1 以降の名前（古い版は `-vsync 0`）
- **最小の手順**（WSL、`~/video-tools-trial/sheet`）:
  ```sh
  FONT=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf   # fc-list で確かめる
  # A. 1 秒ごと、時刻とコマ番号入り、6x5 を何枚でも（sheet_01.png, sheet_02.png, …）
  ffmpeg -hide_banner -i in.mp4 -an -vf "drawtext=fontfile=$FONT:text='%{pts\:hms} #%{n}':x=10:y=10:fontsize=36:fontcolor=white:box=1:boxcolor=black@0.6:boxborderw=6,fps=1,scale=384:-2,tile=6x5:padding=4:margin=4" -fps_mode passthrough sheet_%02d.png
  # B. 場面転換だけ（補助）。閾値は 0.3〜0.5 から
  ffmpeg -hide_banner -i in.mp4 -an -vf "drawtext=fontfile=$FONT:text='%{pts\:hms} #%{n}':x=10:y=10:fontsize=36:fontcolor=white:box=1:boxcolor=black@0.6,select='gt(scene\,0.4)',scale=384:-2,tile=6x5:padding=4" -fps_mode passthrough scenes_%02d.png
  # C. 転換の時刻の一覧だけ欲しいとき
  ffmpeg -hide_banner -i in.mp4 -an -vf "scdet=t=10,metadata=print:key=lavfi.scd.time:file=scd.txt" -f null -
  ```
  A の drawtext は fps の前なので、`#` の後は元のコマ番号（推論）。最後の 1 枚は空きのマスが黒で埋まる
- **動いたと言える確かめ方**: `sheet_01.png` が 6 列 5 行で、左上のマスが `00:00:00.000 #0`、次のマスが `00:00:01.000` 前後。60 fps の動画なら 2 マス目の番号が `#60` 前後。60 秒の動画で A は 2 枚（30 マス×2）。C の `scd.txt` に `lavfi.scd.time=` の行が転換の数だけ並ぶ
- **所要の見込み**（推測）: 30 分。エスケープ（`\:`・`\,`）で詰まったら、文字列を `textfile=` に逃がす（文書の勧め）

## Open Questions

- `fps=1` の後に選ばれるコマが各秒のどのコマか（丸め方）は文書のこの節では確かめていない。秒ちょうどのコマが要るなら `select='isnan(prev_selected_t)+gte(t-prev_selected_t\,1)'` に替える
- 画面録画など VFR の素材で、`fps` フィルタの埋め方が見た目を変えないか（[[exp-galleria-ffmpeg-measurement-and-delivery]] の VFR の教訓）
- Windows 側の ffmpeg で同じコマンドを使う場合のフォントのパスのエスケープ（経験は WSL に逃げる方針）
