---
type: source
summary: ffmpeg のフィルタの公式文書のうち閃光の検査に使えるもの（signalstats の YAVG、photosensitivity、metadata）と、それを使って ITU-R BT.1702 / WCAG の閃光の基準を「画素ごと・領域ごと」に近似して数える自前の手順。photosensitivity は閃光を「減らす」フィルタで、検査の道具ではない。近似の手順は本ページで組んだもので、どの規格の正式な測定手順でもない
video_types: [promo, any]
url: https://ffmpeg.org/ffmpeg-filters.html
author: FFmpeg 開発者（公式文書）／近似の手順は本ページ（第 3 回サーベイ）で組んだもの
published: unknown（ffmpeg.org の filters 文書は開発版に追従して更新される）
retrieved: 2026-11-09
sources:
  - https://ffmpeg.org/ffmpeg-filters.html（§11.197 photosensitivity、§11.239 signalstats、§20.13 metadata、§20.17 select）
  - https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html（閾値。本文は [[web-motion-wcag-2-2-motion-flash-vestibular]]）
  - https://www.itu.int/rec/R-REC-BT.1702/en（閾値。本文は [[web-motion-itu-r-bt1702-ofcom-nhk-minpo-flash-guidelines]]）
---

# ffmpeg で閃光を近似して数える（signalstats・photosensitivity と自前の画素ごとの計数）

## 何の文献か

- **ffmpeg-filters の公式文書**（ffmpeg.org、2026-11-09 時点。ページは開発版の文書で、galleria の ffmpeg 9.0.1（Gyan の full build。[[exp-galleria-ffmpeg-measurement-and-delivery]]）と細部が違いうる。手元では `ffmpeg -h filter=<名前>` で確かめる）
- 閃光の検査そのものを行うフィルタは ffmpeg に**無い**。近いのは次の 2 つ:
  - **signalstats**: 「Evaluate various visual metrics that assist in determining issues associated with the digitization of analog video media.」フレームごとに `YAVG`（Y の平均、0〜255）などをメタデータに出す
  - **photosensitivity**: 「Reduce various flashes in video, so to help users with epilepsy.」閃光を**減らす（書き換える）**フィルタ。オプションは `frames`（既定 30）、`threshold`（既定 1、小さいほど厳しい）、`skip`、`bypass`、`blend`（閾値を超えたフレームを、0 なら直前の採用フレームの複製、1 なら閾値までの混合に）。文書には判定の基準（どの規格か）も、検出結果の数値の出し方も書いていない
- 下の「画素ごとの近似」は、ITU-R BT.1702 と WCAG 2.x の定義（相対輝度の差 0.1、暗い側 0.8 未満、画面の 25% ／ 10 度の視野の 25%、1 秒に 3 回を超える閃光）を、本ページで numpy の手順に直したもの。**規格の正式な測定手順でも、IRIS・Harding FPA の再現でもない**

## 書いてあること（文書と定義から）

- `signalstats` の `YAVG` は Y'（ガンマのかかった符号値）の平均で、規格が使う**相対輝度（線形の光）ではない**。また画面全体の 1 つの値なので、画面の一部だけの閃光は薄まる。IRIS が画面全体の平均で判定するのと同じ限界（[[web-check-flash-ea-iris]]）
- WCAG・ITU の定義が要るのは、(1) sRGB を線形にした相対輝度、(2) 光っている**領域の中**の明暗の往復、(3) 同時に光る面積（ITU は画面の 25%、WCAG は 1024×768 での 341×256 の矩形の 25%＝全画面の動画なら画面の約 1/9 の窓の 1/4）（[[web-check-flash-peat-harding-fpa]] に比較の表）
- 赤: WCAG 2.0 の作業定義は R/(R+G+B) ≥ 0.8 の状態を含み、(R−G−B)×320 の変化が 20 を超える往復（PEAT のガイドの原文。[[web-check-flash-peat-harding-fpa]]）

## この wiki への含意

- IRIS は「画面全体の平均」で明るさを見るので、**アゲアゲ版の叩きつけ（字と周りが青く光る）のような部分的な閃光**を見逃しうる（[[web-check-flash-ea-iris]]）。画素ごとに往復を数えて、光った画素が「画面の 25%」「どこか 1/9 の窓の 25%」を超えるかを見る近似を、IRIS と**並べて**読むと、どちらの基準でどこが危ないかが分かる
- [[exp-html-capture-pipeline]] のように自分で 1 フレームずつ描く作りなら、書き出し前の PNG 連番でも同じ計算ができる（第 2 回で「機械でできる、実装はしていない」とした部分）
- photosensitivity フィルタで「安全な版」を自動で作るのは、演出（拍に合わせた光）そのものを書き換えるので、西尾の promo には向かない（推測）。検査で引っかかった区間を、作り手が明るさの差・面積・回数で直す方が筋がよい
- 型: promo が主。embed のループは 2 周つないで測る

## 着手の仕方（未検証。galleria で確かめる）

- **何ができるようになるか**: 書き出した動画（または PNG 連番）から、フレームごとに「1 秒に 3 回を超えて往復した画素の割合（画面全体／最悪の 1/9 窓）」を CSV で出し、ITU 基準と WCAG 基準の両方で危ない秒を一覧にする。効く型: promo、embed（ループ）
- **機械**: galleria WSL（ffmpeg と python3 は入っている。numpy は uv の venv に入れる）。Mac でも同じ
- **入れるもの**: numpy だけ（PyPI の最新版）。GPU・費用・アカウント不要
- **成熟度**: 自前の近似。正しさは陽性対照（合成動画）と IRIS との突き合わせで確かめるしかない

### 手順 0: 画面全体の明るさの往復をざっと見る（ffmpeg だけ）

```bash
cd ~/video-tools-trial/flash
ffmpeg -v error -i hype.mp4 -vf "fps=30,signalstats,metadata=print:key=lavfi.signalstats.YAVG:file=yavg.txt" -f null -
grep -c YAVG yavg.txt   # フレーム数と一致すれば成功
```

`YAVG` が 1 秒の中で大きく上下する箇所（目安: 25 以上の往復が 1 秒に 4 回以上。数値は推測）を拾う。IRIS と同じく部分的な閃光は見えない

### 手順 1: 画素ごとの近似（ffmpeg → numpy）

スクリプトは素材と別のディレクトリに置き、`python3 -I` で回す。

```bash
mkdir -p ~/video-tools-trial/flash/bin && cd ~/video-tools-trial/flash
uv venv && . .venv/bin/activate && uv pip install numpy
cat > bin/flashcount.py <<'EOF'
# 近似: ITU-R BT.1702 / WCAG 2.x の閃光の定義を画素ごとに数える。規格の正式な手順ではない
import sys, argparse, numpy as np
p = argparse.ArgumentParser()
p.add_argument("--w", type=int, default=192); p.add_argument("--h", type=int, default=108)
p.add_argument("--fps", type=int, default=30); p.add_argument("--out", default="flash.csv")
a = p.parse_args(); W, H, F = a.w, a.h, a.fps
c = np.arange(256) / 255.0
lut = np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4).astype(np.float32)

class Tracker:  # 画素ごとに「前の折り返しから T 以上動いたら遷移 1 回」と数える
    def __init__(s, T, D):
        s.T, s.D, s.lo = T, D, None
        s.ring = np.zeros((F, H, W), np.bool_); s.i = 0
    def step(s, v):
        if s.lo is None:
            s.lo, s.hi, s.dir = v.copy(), v.copy(), np.zeros(v.shape, np.int8)
        s.lo = np.minimum(s.lo, v); s.hi = np.maximum(s.hi, v)
        up = (s.dir != 1) & (v - s.lo >= s.T) & (s.lo < s.D)    # 暗い側（lo）が D 未満
        dn = (s.dir != -1) & (s.hi - v >= s.T) & (v < s.D)      # 暗い側（v）が D 未満
        t = up | dn
        s.dir[up] = 1; s.dir[dn] = -1; s.lo[t] = v[t]; s.hi[t] = v[t]
        s.ring[s.i % F] = t; s.i += 1
        return s.ring.sum(axis=0)   # 直近 1 秒の遷移の数（2 遷移＝閃光 1 回）

def worst_window(m):  # 画面の 1/3×1/3 の窓（WCAG の 341×256 相当）の中の最大の割合
    k, l = max(1, W // 3), max(1, H // 3)
    s = np.pad(m.astype(np.int32).cumsum(0).cumsum(1), ((1, 0), (1, 0)))
    return (s[l:, k:] - s[:-l, k:] - s[l:, :-k] + s[:-l, :-k]).max() / (k * l)

lum, red = Tracker(0.1, 0.8), Tracker(20.0, 1e9)
n = W * H * 3; f = 0
with open(a.out, "w") as out:
    out.write("frame,t,lum_itu,lum_wcag,red_itu,red_wcag,lum_2to3_itu\n")
    while True:
        b = sys.stdin.buffer.read(n)
        if len(b) < n: break
        rgb = lut[np.frombuffer(b, np.uint8).reshape(H, W, 3)]
        R, G, B = rgb[..., 0], rgb[..., 1], rgb[..., 2]
        L = 0.2126 * R + 0.7152 * G + 0.0722 * B
        S = R + G + B
        rv = np.where(R >= 0.8 * np.maximum(S, 1e-6), np.maximum(R - G - B, 0) * 320, 0).astype(np.float32)
        cl, cr = lum.step(L), red.step(rv)
        fl, fr, mid = cl > 6, cr > 6, (cl >= 4) & (cl <= 6)
        out.write(f"{f},{f/F:.3f},{fl.mean():.3f},{worst_window(fl):.3f},{fr.mean():.3f},{worst_window(fr):.3f},{mid.mean():.3f}\n")
        f += 1
EOF
ffmpeg -v error -i hype.mp4 -vf "fps=30,scale=192:108:flags=area,format=rgb24" -f rawvideo - \
  | python3 -I bin/flashcount.py --out hype_flash.csv
# 危ない秒の一覧（ITU: 画面の 25% 超、WCAG: どこかの 1/9 窓の 25% 超）
python3 -I -c "
import csv
for r in csv.DictReader(open('hype_flash.csv')):
    li, lw, ri, rw = (float(r[k]) for k in ('lum_itu','lum_wcag','red_itu','red_wcag'))
    if li > .25 or lw > .25 or ri > .25 or rw > .25:
        print(r['t'], 'ITU' if li > .25 else '', 'WCAG' if lw > .25 else '', 'RED' if max(ri, rw) > .25 else '')
" | awk '{s=int($1); if (s!=last) print; last=s}'
```

- 近似の主な割り切り（推測で決めた所）: 192×108 に縮める（細かい模様の往復は平均で消える。気になる区間だけ 384×216 で測り直す）、縮小はガンマのかかった値の平均（線形の平均ではない）、YUV→RGB の行列は ffmpeg の既定（色の情報が付いていない mp4 では BT.601 で変換されうる）、赤の暗い側の条件は省いた、「同時に光る」は「直近 1 秒に 3 回を超えて往復した画素」で代用
- 「長く続く閃光」の目安: `lum_2to3_itu`（直近 1 秒に 2〜3 回往復した画素の割合）が 0.25 を超える状態が 5 秒のうち 4 秒以上続く区間を探す（IRIS の extended failure に寄せた。PEAT の定義とは違う）

### 動いたと言える確かめ方

- **陽性対照**: [[web-check-flash-ea-iris]] の合成動画 3 本（全画面 5Hz・全画面 2Hz・左 20% だけ 5Hz）を同じコマンドに通す。期待: 全画面 5Hz は開始 1 秒後から `lum_itu`≒1.0・`lum_wcag`≒1.0、全画面 2Hz は両方 0（1 秒に 2 往復＝4 遷移で 6 を超えない）、左 20% の 5Hz は `lum_itu`≒0.2（ITU なら合格）で `lum_wcag`≒1.0（WCAG なら不合格）
- `hype_flash.csv` の行数が `ffprobe` の `nb_frames`（30fps に直した後）と一致する
- IRIS の秒ごとの表（[[web-check-flash-ea-iris]]）と並べ、全画面の閃光では両方が同じ秒を指すこと。食い違う秒（近似だけが指す＝部分的な閃光）は、その秒の前後 1 秒を PNG 連番に書き出して目で見る（`ffmpeg -ss <秒-1> -t 2 -i hype.mp4 -vf fps=30 r3_%03d.png`）

### 所要の見込み（推測）

- 3 分・30fps（約 5,500 フレーム）を 192×108 で数えるのは CPU で数分。陽性対照と IRIS との突き合わせを含めて 1〜2 時間

## Open Questions

- 縮小の大きさ（192×108）で、字の周りだけ光る演出の面積がどれだけ正しく出るか
- 画素ごとの往復の数え方（前の折り返しからの差）が、Harding FPA・IRIS の数え方とどれだけ違うか。Harding の手順は非公開
- NHK・民放連の「輝度変化 20% 超の場面転換を 1 秒 3 回まで」をこの近似でどう測るか（場面転換は往復ではなく 1 回の変化で数えると読める。[[web-motion-itu-r-bt1702-ofcom-nhk-minpo-flash-guidelines]]）。画面全体の平均相対輝度の 1 フレームの差が 0.2 を超えた回数を 1 秒の窓で数える列を足すのが一案（推測）
- photosensitivity フィルタの判定の中身（どの規格の数値か）は文書に無く、ソースは読んでいない
