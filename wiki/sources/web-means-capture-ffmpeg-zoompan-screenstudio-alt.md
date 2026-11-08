---
type: source
summary: 自動ズームを後処理で作る方法の一次資料。ffmpeg の公式文書（zoompan は z・x・y を式で与え、入力の時刻 it を使える。crop の幅・高さはフレームごとに変えられない。scale は eval=frame で時刻 t を使える）、zoompan が揺れる不具合の Trac #4298（2015 年に報告、2026-11 時点で open、回避は前に scale を挟む）、screenstudio-alt（MIT、macOS 専用の Claude Code skill）の設計文書（クリックの位置は画素からは取れないので録画中にログを取る、元の高解像度のコマから LANCZOS で切り出して cosine で寄る、crop した完成品より約 1.3 倍鮮明と書く）
video_types: [promo, embed]
url: https://ffmpeg.org/ffmpeg-filters.html#zoompan
author: FFmpeg プロジェクト（文書・Trac）／Conner K. Ward（screenstudio-alt）
published: ffmpeg-filters は 2026-11-09 取得の git master 版。Trac #4298 は 2015 報告・最終更新は約 5 か月前。screenstudio-alt の最終 push は 2026-06-23
retrieved: 2026-11-09
sources:
  - https://ffmpeg.org/ffmpeg-filters.html（11.298 zoompan、11.47 crop、11.223 scale）
  - https://ffmpeg.org/ffmpeg.html（オプションの値をファイルから読む `-/` の記法）
  - https://trac.ffmpeg.org/ticket/4298（「zoompan filter creates shaky image」）
  - https://github.com/connerkward/screenstudio-alt-skill（README.md、docs/ARCHITECTURE.md）
---

# 自動ズームを後処理で作る（ffmpeg の zoompan・crop と screenstudio-alt）

## 何の文献か

- **ffmpeg の公式文書**（ffmpeg-filters、ffmpeg）。2026-11-09 に ffmpeg.org から取った版（最新のリリースは 9.0.2）。仕様の説明で、画質の評価は無い
- **FFmpeg Trac #4298**: 利用者（slhck）の不具合報告と開発者のコメント（2015〜）。状態は open、「Reproduced by developer: yes」
- **screenstudio-alt**: 個人の OSS（MIT、star 11）。Screen Studio の効果を CLI で再現する Claude Code の skill。README は Screen Studio との比較表を載せるが、比較の測定は自分の道具の側だけ。「macOS-only, end to end」と自分で書いている

## 書いてあること

### ffmpeg の zoompan（11.298）

- 「Apply Zoom & Pan effect」。`zoom`（1〜10）、`x`・`y`（切り出す左上の位置）、`d`（1 枚の入力から何フレーム出すか。既定 90）、`s`（出力の大きさ。**既定 hd720**）、`fps`（出力の fps。**既定 25**）
- 式の中で使えるもの: `iw`・`ih`、`in`・`on`（入出力のフレーム番号）、**`in_time`／`it`（入力の時刻、秒）**、`out_time`、直前の `zoom`・`x`・`y`、`pzoom` など
- 文書の例: 「Zoom in 2x into center of picture only for the first second of the input video: `zoompan=z='if(between(in_time,0,1),2,1)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'`」。動画に使うときは `d=1`（1 入力 1 出力）

### crop と scale（11.47、11.223）

- crop の `w`・`h` は「evaluated during the filter configuration, when the 'w' or 'out_w' command is sent, or when the input frame size changes」。`x`・`y` は「evaluated per-frame」で、`t`（秒）と `n` を使える。**一定の大きさで動かす（パン）は crop だけでできるが、寄る・引く（大きさを変える）は crop だけではできない**
- scale は `eval=frame` で「Evaluate expressions for each incoming frame」、そのとき `t`・`n` を使える
- 式をコマンドラインに書くと引用符と区切りが入り組む。ffmpeg は「add a forward slash '/' immediately before the option name」でオプションの値をファイルから読める: `ffmpeg -i INPUT -/filter:v filter.script OUTPUT`（ffmpeg.html）

### zoompan が揺れる不具合（Trac #4298）

- 報告（2015）: 「When using the zoompan filter and setting any x or y (or both) value, the effect is shaky and jerky」。動画を入力にしても「the output is shaky and lots of frames are dropped」
- 開発者（comment 2）の回避: 「Workaround is to insert the scale filter」（zoompan の前に scale を入れる）
- 後のコメント: 「Scaling beforehand consumes a lot of memory for 4k+ resolutions」（2018 頃）。「Even with the trick of upscaling, zooming, and downscaling, the jitter is still noticeable when looking closely」（約 2 年前）。開発者 Gyan は「Using the other swscale algorithms made no difference to the jitter in the output. What's needed is anti-aliasing」と書いた。直っていない

### screenstudio-alt の設計（README、ARCHITECTURE.md）

- 「Screen Studio's signature effects need to know where you clicked and what you typed — pixels alone can't tell you that」。録画中に Swift の `events-log` がカーソル位置（60 Hz）・クリック・キー入力を JSONL に書く（パスワード入力中はキーを捨てる）。README: 「auto-zoom needs this — it can't be recovered from pixels」
- 描画（`render.py`）: 「a non-destructive, single-pass camera renderer ... a virtual camera that zooms/pans over the original high-res frames, sampled with LANCZOS, exported to a smaller target — so a zoom still reads ≥1:1 source pixels and stays crisp (measured ~1.3× sharper than cropping a finished video, more with native-retina capture)」。寄りは「cosine ease-in/out per region」、60fps で書き出し、9:16 では切り出し窓が動きを追う。測り方（何をもって 1.3 倍か）は書かれていない
- 寄る区間は `regions.json` = `[{"t0","t1","z","cx","cy"}]`。古い ffmpeg のフィルタの経路（`polish.py`）は「not a substitute for `render.py`: every Studio export and high-quality zoom/pan goes through `render.py`」
- 何も動かない区間を速める（`--speedup`）は「no input AND frozen pixels — a playing animation is never compressed」で、こちらはログ無しでも画素だけで動く
- 自分のデモ動画は Playwright の recordVideo を使わず、1 コマずつシークしてスクリーンショットを撮った（理由は可変フレームレート。[[web-means-capture-playwright-screencast]]）

## この wiki への含意

- **寄る位置は台本から渡せば、ログ取りの道具は要らない**。screenstudio-alt・Screen Studio・Cap・OpenScreen はみな「録画中の OS の入力をログにする」が、Playwright の台本で動かすなら、クリックの時刻と座標は台本が知っている（[[web-means-capture-playwright-screencast]] の clicks.json）。そこから zoompan の式か、OpenScreen の zoomRegions（[[web-means-capture-openscreen]]）を作る
- **西尾の方式の延長で書ける**。西尾の canvas の方式は「時刻表（TL）から 1 コマを描く純関数」だった（[[exp-html-capture-pipeline]]）。寄りの区間の表 `[{t0,t1,z,cx,cy}]` は同じ形の時刻表で、screenstudio-alt の `render.py` がやっていること（元のコマからの切り出し＋cosine）は、西尾の capture.mjs の側に「収録した動画を canvas に drawImage して寄る」として書ける（推測。動画の 1 コマを正確な時刻で canvas に出す手間がある）
- **ffmpeg だけで済ませる経路は、揺れの不具合が残っている**。zoompan は 10 年以上 open の揺れがあり、前に拡大を入れる回避でも「近くで見ると分かる」とコメントされている。promo で大きく映す寄りには、元のコマから補間付きで切り出す方式（screenstudio-alt の render.py、OpenScreen の描画）を優先し、ffmpeg は下書き・確認用にとどめる（推測。揺れの程度は galleria で測る）
- **寄りの道具ごとの効き方は「1 つの動きの体系」の決まりに関わる**。cap-demo は「Never stack 2D zoom segments on 3D shots」、howseen は「カメラのズームは対数空間で補間し、ズームインとアウトを続けない」と書く（[[web-means-capture-cap]]、[[web-opus-howseen-claude-motion-design]]）。寄りは区間を分け、続けて寄り引きしない

## 着手の仕方（未検証。galleria で確かめる）

- **表現できるようになること**: 台本で撮った画面収録に、クリックの時刻に合わせて滑らかに寄って戻るカメラを、アプリを使わずに付ける。効く型: promo、embed
- **機械**: galleria WSL（ffmpeg と python3 があり、追加は無し）
- **入れるもの・費用**: 無し（既にある ffmpeg・python3）。費用 0
- **成熟度**: ffmpeg の zoompan は古くからあるが、揺れの不具合が open
- **最小の手順（WSL）**: 入力は CFR に直した 1920×1080・30fps の `take.mp4` と、`clicks.json`（`[{"t":秒,"x":px,"y":px}]`、1920×1080 の座標）。区間の決め方（クリックの 0.4 秒前から寄り始め 1.6 秒後まで、0.5 秒で寄る、1.8 倍）は推測で置いた値
  `zoomexpr.py`（推測で書いたもの。未実行）:
  ```python
  import json, sys
  S = 2            # Trac #4298 の回避: 先に 2 倍に拡大してから zoompan
  Z, PRE, POST, R = 1.8, 0.4, 1.6, 0.5
  W, H, FPS = 1920, 1080, 30
  clicks = json.load(open(sys.argv[1]))
  regs = []
  for c in sorted(clicks, key=lambda c: c["t"]):
      t0, t1 = max(0, c["t"] - PRE), c["t"] + POST
      if regs and t0 < regs[-1][1]:      # 重なる区間はつなげる（中心は後のクリック）
          regs[-1] = (regs[-1][0], t1, c["x"], c["y"])
      else:
          regs.append((t0, t1, c["x"], c["y"]))
  def ease(t0, t1):
      return (f"if(lt(it,{t0+R:.3f}),0.5-0.5*cos(PI*(it-{t0:.3f})/{R}),"
              f"if(gt(it,{t1-R:.3f}),0.5+0.5*cos(PI*(it-{t1-R:.3f})/{R}),1))")
  def piece(vals, default):
      e = default
      for (t0, t1, *_), v in reversed(list(zip(regs, vals))):
          e = f"if(between(it,{t0:.3f},{t1:.3f}),{v},{e})"
      return e
  z  = f"1+{Z-1}*({piece([ease(r[0], r[1]) for r in regs], '0')})"
  cx = piece([f"{r[2]*S:.1f}" for r in regs], "iw/2")
  cy = piece([f"{r[3]*S:.1f}" for r in regs], "ih/2")
  x = f"max(0,min(iw-iw/zoom,{cx}-iw/zoom/2))"
  y = f"max(0,min(ih-ih/zoom,{cy}-ih/zoom/2))"
  print(f"scale={W*S}:{H*S}:flags=lanczos,"
        f"zoompan=z='{z}':x='{x}':y='{y}':d=1:s={W}x{H}:fps={FPS}")
  ```
  ```sh
  cd ~/video-tools-trial/pw-capture/out
  python3 zoomexpr.py clicks.json > zoom.txt
  ffmpeg -i take.mp4 -/filter:v zoom.txt -c:v libx264 -crf 18 -pix_fmt yuv420p -an zoomed.mp4
  ```
- **動いたと言える確かめ方**: `zoomed.mp4` の長さと fps が `take.mp4` と同じ（ffprobe の duration・nb_frames。zoompan で落ちたフレームが無いか）。各クリックの t で 1 コマ切り出して、クリックの印が画面の中央寄りに大きく映っている。揺れは、寄りの保持中（区間の中央）を 0.5 秒分 PNG にして並べ、画面の縁の文字が 1px 単位で動いていないかを見る（動いていれば #4298 が出ている）
- **所要の見込み（推測）**: 1〜2 時間（式の誤りの修正込み）。揺れが目立つ場合は、Python で元のコマを切り出す方式（screenstudio-alt の render.py の考え方、numpy と Pillow が要る）に切り替えて半日

## Open Questions

- zoompan を `d=1` で動画に使ったとき、2026 年の ffmpeg（galleria の 9.0.1）で、Trac #4298 の「frames are dropped」が起きるか
- 拡大の倍率 S を 2 にしたときと 3 にしたときの揺れと速さの差
- screenstudio-alt の「crop した完成品より約 1.3 倍鮮明」の測り方
- クリック以外（文字入力・スクロール）で寄るべきかは、FocuSee（入力の区間でも寄る、[[web-means-capture-focusee-recordly]]）と screenstudio-alt（入力の塊で寄る）が「寄る」側。根拠の研究は見ていない
