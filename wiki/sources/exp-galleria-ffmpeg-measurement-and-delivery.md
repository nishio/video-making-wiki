---
type: source
summary: galleria で動画を扱ったときの ffmpeg・計測・受け渡しの落とし穴。秒は pts でしか取れない、カットは色ヒストグラムで、周期は scene score の自己相関で出す、作り直した動画を同じファイル名で上書きすると相手は古いものを見続ける、Unity は batchmode で PNG 連番にして ffmpeg で MP4 にする
video_types: [any]
sources:
  - galleria-wiki wiki/video-timing-measurement.md（raw 2026-09-09-video-timing-measurement.md）
  - galleria-wiki wiki/replace-in-place-serves-the-old-file.md（raw 2026-09-21-lifepose-unity-headless-render.md）
  - galleria-wiki wiki/unity-headless-batchmode.md、wiki/lifeposesystem.md
  - galleria-wiki wiki/video-loop-period-detection.md、wiki/first-last-frame-video-interpolation.md（「補間器は仕事で選ぶ」節。raw 2026-09-15-sprite-gen-repo.md）
---

# galleria での ffmpeg・計測・受け渡しの落とし穴（2026-09）

## 手元の動画から時刻を測る（2026-09-09、実際に踏んだ）

参考素材を切り出す前に、尺・カット・繰り返しの周期・フェードの開始点を出したときの記録。

- **秒は pts でしか取れない。** opencv の `CAP_PROP_FPS` は平均か公称を返し、フレーム番号 ÷ fps は時刻ではない。画面録画は VFR（可変フレームレート）になりやすい。68.65 秒のファイルを opencv だけで測って 70.08 秒と出し、その上に付けた秒のラベルが全部ずれた。
  ```
  ffprobe -v error -show_entries format=duration -show_entries stream=r_frame_rate,nb_frames -of default=noprint_wrappers=1 IN
  ```
  `r_frame_rate` と `nb_frames / duration` が食い違ったら VFR を疑う。opencv のフレーム番号は信用してよく、秒は信用できない。サムネイル一覧にはフレーム番号を併記しておくと救える。
- **ffmpeg の filter 引数に Windows のパスを書かない。** `-vf` / `-af` の中では `\` がエスケープ、`:` が区切り。カレントを移して相対名で渡す（`-i` と出力の側は絶対パスでよい）。パスや `\` を含むスクリプトは heredoc でなくファイル書き込みで置く。
- **カットは `select='gt(scene,N)'` だけでは出ない。** 動きの多い素材では 0.15 でほぼ全フレームが通る。HSV の 2D ヒストグラム（24 x 24）の相関で `1 - correl > 0.3` をカット候補にすると素直に立つ。**構図が変わらず中身だけ切り替わる境目は数値に出ないので、1 秒ごとのサムネイル列を HTML にして人に見せる。一発で決まる。**
- **周期は scene score の自己相関で出る。** `ffmpeg -copyts -ss 2 -to 22 -i IN -an -vf "scale=160:90,select='gte(scene,0)',metadata=print:file=loop.txt" -f null NUL`。`-copyts` が無いと pts が 0 起点に戻る。160 x 90 に落としても結果はほとんど変わらず段違いに速い。VFR なので自己相関の前に等間隔へ補間する（`np.interp`）。出た周期が作画の更新の刻み（例: 1/12 秒）と一致したら、動きでなく再描画の刻みを拾っている疑い。相関 0.5 前後は「だいたい周期的」で確定ではない。
- **フェードは `signalstats` の `YAVG` で出る。** 前半の中央値に対して 80% を割った時刻がフェード開始。
- **切り出しは CFR に直して渡す。** `ffmpeg -ss 57.5 -t 10.233 -i IN -an -vf "fps=60" -c:v libx264 -crf 14 -preset slow -pix_fmt yuv420p OUT.mp4`。`-ss` を `-i` の前に置くと高速シークで、尺は `-t` で切る（`-to` と混ぜない）。見せる版は別に作る（`scale=1280:-2`、`-crf 20`、`-movflags +faststart`）。コマ単位で調べる区間はフル解像度の PNG 連番にする。
- galleria にはもともと ffmpeg が無かった。`winget install --id Gyan.FFmpeg --scope user` で 9.0.1 full build が入る（管理者権限不要）。動画モデルを取る前に ffmpeg を入れる、と local-video-generation のページにも書かれている。

## 作り直した動画を同じ名前で上書きすると、相手には古いまま出る（2026-09-21、実際に踏んだ）

LifePose の待機モーション動画を 3 回作り直し、毎回 `Vita_Idle_LifePose.mp4` に上書きして同じ URL を案内した。所有者からは 3 回とも「まだ直っていない」と返ってきた。1 回目は本当に直っていなかったが、2 回目は生成物の方は直っていた。galleria の配信スクリプト `serve_sites.py` が HTML 以外に `private, max-age=3600` を付けていて、Mac / iPhone 側がキャッシュを使っていた。こちらの確認は `Invoke-WebRequest` の 200 とバイト数だけで、それは「サーバが新しいものを持っている」ことしか示さない。

- **差し替えるならファイル名を変える**（`lifepose_v3_standing.mp4` → `lifepose_v4_life100.mp4` のように版を名前に入れる）。
- **古い名前は消す。** 消せば 404 になり、古いものを見ていたことが相手の側でも分かる。
- `?v=4` のようなクエリは HTML 内の参照には効くが、URL を直接開かれると効かない。

## Unity の映像を headless で MP4 にする

- batchmode で描画するときは `-nographics` を**付けない**（付けると `GfxDevice: Null` で `cam.Render()` が効かない）。カメラを `RenderTexture` に描き、`ReadPixels` → `EncodeToPNG` で連番を書き、ffmpeg で MP4 にする。720 x 1280 を 300 枚で数十秒。Unity Recorder は要らない（Recorder の GameView 入力は batchmode では使えない）。
- `-executeMethod` に `-quit` を組み合わせるとメソッドの戻りで即終了する。後続の処理を待つなら `-quit` を外して自分で `EditorApplication.Exit(0)` を呼ぶ。
- Unity Hub の CLI は成功しても exit 255 を返す。失敗と誤認しない。
- 購入アセット（LifePoseSystem）の規約は「購入者本人のみ、再配布不可。完成した動画・画像は商用可」と記録されている。（lifeposesystem.md）

## 生成 clip からループを切り出す（他 repo の主張、galleria では未実行）

sprite-gen という repo の記録を読んだもの。galleria-wiki も「本機では未実行、リポジトリの主張」としている。

- 「一番似ている後続フレームで切る」は歩行で壊れ、脚が入れ替わった半周期ずれの姿に着地する（side walk で周期 28 のところ 39、run で 17 のところ 25 を選んだ）。**先に周期を測り、その周期に対して継ぎ目の良い開始点を選ぶ。** 周期プロファイル `P[L] = mean_j |f[j] − f[j+L]|` の、最深の谷の 15% 以内にある最小の極小を取る（半周期の谷は全周期の 55〜70% の深さしかない）。
- 環境動画のループ化では、位置の距離に速度の差の項を足す（`β ≈ 5`）。ちらつく clip で位置は合うが速度が跳ぶ切り口を避けられた（継ぎ目の平均絶対差 1.65 → 0.87）。
- 補間器は「何を保存したいか」で選ぶ。RIFE はキャラクターの中割りではぼやけたクロスフェードになって退役したが、環境動画のループの継ぎ目を橋渡しするのには正解だった。ピンポン（半分が逆再生）、クロスフェード、単一フレーム一致は棄却されている。
- Grok Imagine の i2v は `aspect_ratio` を無視する（3:4 を頼んで 960 x 960 が返った）。出力のフレーミングは入力画像のフレーミングで決まるので、「ジャンプで髪が切れる」は prompt でなく静止画に余白を足して直した。

## Open Questions

- 計測の手順（pts、HSV ヒストグラム、自己相関）は参考素材の切り出しのためだった。何の素材で何に使ったかは galleria-wiki に書かれていない。
