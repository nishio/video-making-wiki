---
type: source
summary: EA が公開した閃光（光過敏性発作の危険）の検査ライブラリ IRIS（C++、BSD-3-Clause）と、その Python 移植 iris-pse-detection（MIT、pip で入る）。相対輝度の差 0.1・暗い側 0.8 未満・画面の 25%・飽和した赤（(R−G−B)×320 の差 20）で「遷移」を数え、1 秒に 6 遷移（3 閃光）を超えたら失敗、5 秒の窓で 4〜6 遷移が 4 秒続いたら「長く続く閃光」の失敗、とする。コードを読むと、面積は「少しでも変わった画素の割合」、明るさの差は「画面全体の平均の差」で判定していて、画面の一部だけの閃光は見逃しうる
video_types: [promo, any]
url: https://github.com/electronicarts/IRIS
author: Electronic Arts（IRIS）／tokoroten ほか「IRIS-PSE-Detection contributors」（Python 移植）
published: 2023-11-23（IRIS の最初の commit）〜2025-01-14（最新の commit）／2026-01-22（iris-pse-detection 1.0.0〜1.1.2）
retrieved: 2026-11-09
sources:
  - https://github.com/electronicarts/IRIS（README.md、LICENSE.txt、config/appsettings.json、CMakePresets.json、vcpkg.json、example/main.cpp、src/Flash.cpp・FlashDetection.cpp・TransitionTracker.cpp・RelativeLuminance.cpp・RedSaturation.cpp・VideoAnalyser.cpp を読んだ）
  - https://github.com/electronicarts/IRIS/commits/main.atom（commit の日付）
  - https://pypi.org/project/iris-pse-detection/（1.1.2、2026-01-22）
  - https://github.com/tokoroten/iris-pse-detection（README、LICENSE、src/iris_pse_detection/cli.py・configuration.py・flash.py・frame_data.py・video_analyser.py を読んだ）
---

# EA IRIS と Python 移植 iris-pse-detection（閃光の検査）

## 何の文献か

- **IRIS**: Electronic Arts が GitHub に公開した「光過敏性てんかんの危険がありうる映像を見つける」ための C++ ライブラリと、例のコンソールアプリ。種類はオープンソースの道具（README・設定・ソースコード）。研究論文ではない
  - ライセンス: **BSD-3-Clause**（LICENSE.txt、「Copyright (c) 2023 Electronic Arts Inc.」）。改変・再配布可、EA の名前を宣伝に使わない条件付き
  - 成熟度: commit は 7 本だけ。最初 2023-11-23、最新 2025-01-14（GitHub の commit の atom による）。star 241、fork 16、Releases なし（2026-11-09 時点の GitHub のページ）。**更新は 2025-01 で止まっている**
  - README の但し書き: 「IRIS is not intended to guarantee, certify or otherwise validate visual content's compliance with legal, regulatory or other requirements.」
- **iris-pse-detection**: IRIS を Python に移したもの。PyPI の 1.0.0・1.1.0・1.1.2 がすべて 2026-01-22 の同じ日に出ている。GitHub は tokoroten/iris-pse-detection（star 2、commit 18、最新 2026-01-22）。ライセンスは **MIT**（「Copyright (c) 2026 IRIS-PSE-Detection contributors」。元の BSD-3 の著作権表示は LICENSE には無く、README の Acknowledgments とソースの冒頭に「Based on IRIS by Electronic Arts Inc.」と書く）。依存は numpy・opencv-python・scipy、Python 3.10 以上
  - README: 「Due to floating-point precision differences between C++ and Python/NumPy, results may vary slightly from the original IRIS implementation.」差は閾値の境目で出る、と書く。移植の正しさを誰かが独立に確かめた記録は見つけていない

## 書いてあること

### 何を検出するか（README）

- 輝度の閃光、飽和した赤の閃光、空間の模様（縞。既定では無効）
- 判定（README の原文の要旨）:
  - 「whenever there are more than 3 flashes per second in any given second of the video, it is marked as a flash failure」
  - 「whenever there are between 2-3 flashes per second in any given 5 consecutive seconds, it is marked as an extended flash failure」
  - 模様は「harmful pattern present for half a second or more」で失敗

### 閾値（config/appsettings.json の既定値）

| 項目 | 値 | 意味（README・コードから） |
|---|---|---|
| `RelativeLuminanceFlashThreshold` | 0.1 | 相対輝度の累積の変化が ±0.1 以上で「遷移」1 回 |
| `RelativeDarkLuminanceThreshold` | 0.8 | 暗い側の（平均の）相対輝度が 0.8 未満のときだけ遷移と数える |
| `RedSaturation.FlashThreshold` | 20 | 赤の値（(R−G−B)×320、R/(R+G+B)≥0.8 の画素）の累積の変化が ±20 以上で遷移 |
| `FlashDetection.AreaProportion` | 0.25 | 画面の 25% 以上の画素が変わったときだけ数える |
| `TransitionTracker.MaxTransitions` | 6 | 1 秒の窓で 6 遷移（＝3 閃光）を**超えたら**失敗 |
| `MinTransitions` / `ExtendedFailWindow` / `ExtendedFailSeconds` | 4 / 5 / 4 | 4〜6 遷移の状態が 5 秒の窓の中で 4 秒ぶんのフレーム以上続くと「extended failure」 |
| `WarningTransitions` | 4 | 1 秒に 4 遷移以上で警告（README: 「transitions have surpassed the 2 flashes, 4 transitions, per second threshold」） |
| `PatternDetection` | MinStripes 6、TimeThreshold 0.5 秒、面積 0.25、既定で無効 | |

相対輝度は sRGB の 8bit 値を線形化して `0.2126R + 0.7152G + 0.0722B`（`RelativeLuminance.cpp`、`appsettings.json` の sRGB 表）。

### 判定の根拠は何か（読んだ範囲）

- README は「publicly available guidelines」に基づく既定値、とだけ書き、どの規格かを名指ししていない
- 数値の出どころを照らすと（照合は本ページの作業）:
  - 相対輝度 10%・暗い側 0.80 未満・赤の (R−G−B)×320 > 20 と R/(R+G+B) ≥ 0.8 は、**WCAG 2.0 の general flash / red flash の定義と同じ**（Trace Center の PEAT の解説が同じ式を載せる。[[web-check-flash-peat-harding-fpa]]）。WCAG 2.2 の新しい red flash の作業定義（CIE 1976 UCS で差 0.2）は使っていない（[[web-motion-wcag-2-2-motion-flash-vestibular]]）
  - 面積を「画面全体の 25%」で見るのは **ITU-R BT.1702・Ofcom 側**の書き方。WCAG は「10 度の視野（1024×768 で 341×256 の矩形）の 25%」で、全画面の動画ならずっと小さい面積で引っかかる（[[web-check-flash-peat-harding-fpa]] に比較）
  - BT.1702 の cd/m² による定義（暗い側 160 cd/m² 未満なら差 20 cd/m²）は使っていない（[[web-motion-itu-r-bt1702-ofcom-nhk-minpo-flash-guidelines]]）
  - 「extended failure」（5 秒）は、PEAT の「Extended Flash Warning」や BT.1702・Ofcom の「5 秒を超える閃光の連続は危険かもしれない」に当たる。ただし数え方は同じではない
  - Python 移植の README は「based on guidelines from W3C WCAG and ISO 9241-391」と書く（ISO 9241-391 の本文は読んでいない）
- **Harding FPA の判定と一致するかは書かれていない**。比べた報告も見つけていない

### 面積と明るさの差の数え方（ソースコードを読んだ解釈。動かしてはいない）

- `Flash::CheckSafeArea`: 前のフレームとの差の画像で `cv::countNonZero`（0 でない画素の数）を数え、それが画面の 25% 以上なら、**画面全体の平均の相対輝度の差**（今のフレームの平均 − 前のフレームの平均）を返す。25% 未満なら 0
- `Flash::IsFlashTransition`: 平均の差を同じ向きの間は足し込み、その累積が ±0.1 を超えたら遷移 1 回。暗い側のフレームの平均が 0.8 未満のときだけ
- ここから言えそうなこと（推測）:
  - 差の画像に閾値をかけていないので、**圧縮のノイズでほぼ全画素が「変わった」ことになり、面積の条件はほとんど常に満たされる**
  - 明るさの条件は画面全体の平均で見るので、**画面の一部だけの閃光は薄められる**。たとえば画面の 30% が黒→白（相対輝度 1.0）に光れば平均の差は約 0.3 で数えられるが、画面の 10% だけが黒→白なら平均の差は約 0.1 で境目、25% が 0.3 だけ明るくなるなら約 0.075 で数えられない。ITU・WCAG は「光っている領域の中の明暗の差」で見るので、ここは基準と食い違う
  - 逆に、画面全体が少しずつ明るくなる・暗くなるだけの往復（大きな面のフェード）は累積で数えられる
- 時刻: `FrameData` の時刻は `1000 × フレーム番号 ÷ fps`。fps は C++ 版が ffprobe 相当の `avg_frame_rate` を四捨五入、Python 版は `int(cv2.CAP_PROP_FPS)`（29.97fps は 29 になる）。**VFR の動画は時刻がずれる**（[[exp-galleria-ffmpeg-measurement-and-delivery]] の「秒は pts でしか取れない」と同じ問題）

### 入力と出力

- 入力: OpenCV（vcpkg の `opencv[ffmpeg,contrib]`）が開ける動画。C++ 版は `TestVideos/` のファイルを全部、または `-v <path>` の 1 本
- C++ 版の引数（example/main.cpp）: `-v` 動画、`-j true` で JSON も、`-p true/false` 模様の検出、`-r true/false` 縮小、`-a <割合>` 面積の割合の上書き
- Python 版の CLI（cli.py）: `iris video.mp4 [-c 設定のあるディレクトリ] [-j] [-o 出力先] [--pattern-detection] [--resize 0.5]`。`appsettings.json` が無ければ既定値。終了コード 0＝PASS、1＝Fail、2＝PassWithWarning、3＝エラー
- 出力: `Results/<動画名>/framedata.csv`（1 行 1 フレーム）。`-j` で `result.json`（`OverallResult` と `Results` の一覧）と `frameData.json`（PASS 以外のフレーム）
- CSV の列（Python 版の `FrameData.csv_columns()`）: `Frame, TimeStamp, AverageLuminance, FlashAreaLuminance, AverageLuminanceDiff, AverageLuminanceDiffAcc, AverageRed, FlashAreaRed, AverageRedDiff, AverageRedDiffAcc, LuminanceTransitions, RedTransitions, LuminanceExtendedFailCount, RedExtendedFailCount, LuminanceFrameResult, RedFrameResult, PatternArea, PatternDetectedLines, PatternFrameResult`
- 読み方（README）: `LuminanceTransitions` は「この時点から 1 秒前までの遷移の数」。`*FrameResult` は 0 pass、1 警告（4 遷移以上）、2 extended failure、3 flash failure

### ビルド（C++ 版。README）

- CMake ＋ Ninja ＋ vcpkg。`VCPKG_ROOT` を環境変数で渡す。プリセットは `linux-debug` / `linux-release`（説明に「Target the Windows Subsystem for Linux (WSL)」）、`windows-release`（cl.exe）、`macos-release`
- `cmake --preset linux-release` → `cmake --build --preset linux-release`。オプション `BUILD_EXAMPLE_APP` でコンソールアプリ
- vcpkg が OpenCV（ffmpeg・contrib 付き）を源から作るので、初回は長くかかる（推測）

## この wiki への含意

- **西尾の動画の閃光を「数字で出す」最初の道具になる**。第 2 回の結論「アゲアゲ版 R3 は計算では基準の境目。実フレームで測っていない」（[[web-motion-itu-r-bt1702-ofcom-nhk-minpo-flash-guidelines]]、[[exp-sutra-hype-editions]]）に、1 フレームごとの遷移の数で答えられる
- ただし上のとおり、IRIS は**画面全体の平均**で明るさを見る。アゲアゲ版の否定区間の「画面が青く光る」叩きつけや、ドロップの白飛びは、画面のどれだけが光るかで結果が変わる。**IRIS で PASS でも「部分的な閃光は見ていない」**ので、ffmpeg と numpy で領域ごとに数える近似（[[web-check-flash-ffmpeg-signalstats-photosensitivity]]）と並べて読む
- 青の閃光: 純青の相対輝度は 0.0722 なので、暗い背景の上で青く光らせても平均の差は 0.1 に届きにくい。第 2 回の「青は閾値に届かない可能性」は、IRIS でもそう出るはず（推測）。ただし赤の判定は R/(R+G+B) で、青には掛からない
- promo（速いカット・拍に合わせた光）で一番効く。talk はほぼ当たらない。embed をループで流すなら、ループの継ぎ目を含めるために **2 周つないだ動画**を検査する（WCAG の「ループさせて評価」。[[web-motion-wcag-2-2-motion-flash-vestibular]]）
- Polis の OP 様式の「回想フラッシュ」（[[exp-polis-magi-op]]）も、レンダリングしたらすぐこれに掛けられる

## 着手の仕方（未検証。galleria で確かめる）

- **何ができるようになるか**: 書き出した動画を 1 本渡すと、PASS / 警告 / 失敗と、失敗したフレームの時刻が出る。公開前の機械の足切り（[[experience-lessons-2026-11]] の「機械の QA は足切り」）。効く型: promo（主）、embed（ループ）
- **機械**: galleria WSL（Python 版）。C++ 版は galleria WSL か Windows（Visual Studio）。Mac でも Python 版は動くはず（推測）
- **入れるもの**: `iris-pse-detection` 1.1.2（PyPI、2026-01-22）＋ numpy・opencv-python・scipy。GPU 不要。費用 0、アカウント不要。MIT（元の IRIS は BSD-3）
- **成熟度**: 元の IRIS は 2025-01 から更新なし。Python 版は 2026-01 に一日で出た個人の移植で、使用例・検証の記録は見つけていない
- **素材**: 公開した動画をダウンロードしない。**書き出し元の mp4** を使う。アゲアゲ版は sutra-videos の `output/` 配下（Mac の `~/sutra-videos`。ファイル名は未確認。`output/<slug>-<edition>/` の決まり（[[exp-sutra-videos-overview]]）から `output/hannya-shingyo-hype*/` の中と推測）。galleria の `claude-win\sutra-videos` には生成物が無いかもしれない（`build/` は gitignore）。無ければ Mac から scp で渡す。galleria で作り直す（`make_sutra_hype.py`）のは、ヒラギノ W9（macOS のフォント）を使うので避ける

### 最小の手順（般若心経アゲアゲ版の R3 を測る）

```bash
# galleria WSL
mkdir -p ~/video-tools-trial/iris && cd ~/video-tools-trial/iris
uv venv && . .venv/bin/activate
uv pip install iris-pse-detection==1.1.2
# 書き出し元の mp4 を置く（Mac から。ファイル名は手元で確かめる）
#   Mac: scp ~/sutra-videos/output/<アゲアゲ版のディレクトリ>/<動画>.mp4 galleria:~/video-tools-trial/iris/hype.mp4
ffprobe -v error -show_entries stream=r_frame_rate,avg_frame_rate,nb_frames -show_entries format=duration -of default=nw=1 hype.mp4
iris hype.mp4 -j -o results/ ; echo "exit=$?"
```

- `ffprobe` で `r_frame_rate` と `avg_frame_rate` が両方 30/1 なら CFR。食い違えば先に `ffmpeg -i hype.mp4 -vf fps=30 -c:v libx264 -crf 12 -an hype_cfr.mp4` で CFR にしてから測る（[[exp-galleria-ffmpeg-measurement-and-delivery]]）
- 秒ごとにまとめる（R3 の区間を見るため。スクリプトは別ディレクトリに置き `python3 -I` で回す）:

```bash
cat > ~/video-tools-trial/iris/summarize.py <<'EOF'
import csv, sys, collections
rows = list(csv.DictReader(open(sys.argv[1])))
per_sec = collections.defaultdict(lambda: [0, 0, 0, 0])  # max lumTrans, max redTrans, max lumResult, max redResult
for r in rows:
    h, m, s = r["TimeStamp"].split(":")
    sec = int(int(h) * 3600 + int(m) * 60 + float(s))
    v = per_sec[sec]
    v[0] = max(v[0], int(r["LuminanceTransitions"])); v[1] = max(v[1], int(r["RedTransitions"]))
    v[2] = max(v[2], int(r["LuminanceFrameResult"])); v[3] = max(v[3], int(r["RedFrameResult"]))
for sec in sorted(per_sec):
    v = per_sec[sec]
    if v[0] >= 3 or v[2] or v[3]:
        print(f"{sec//60}:{sec%60:02d}  lumTrans={v[0]} redTrans={v[1]} lumResult={v[2]} redResult={v[3]}")
EOF
python3 -I ~/video-tools-trial/iris/summarize.py results/hype/framedata.csv
```

- R3 の区間（176BPM）は、題名＋R1（約 64 秒）＋R2 の後ろ。正確な開始・終了秒は `make_sutra_hype.py` のタイムラインから取る（推測。R1 の 64 秒を 128/156・128/176 倍すると R2 約 52 秒・R3 約 47 秒）
- **ループの検査**（embed で流すなら）: `ffmpeg -stream_loop 1 -i clip.mp4 -c copy clip_x2.mp4` で 2 周にして同じように測る

### 動いたと言える確かめ方

- `iris` が `Overall Result: PASS|PassWithWarning|Fail` を表示し、終了コードが 0/1/2 のどれか（3 はエラー）。`results/hype/framedata.csv` の行数が `ffprobe` の `nb_frames` と ±1 で一致する
- **道具が閃光を拾えることを先に確かめる**（陽性対照）。黒と白を 1 秒に 5 回（6 フレームごと）切り替える 5 秒の合成動画を作り、Fail（`LuminanceFrameResult=3`）が出ること、1 秒に 2 回の版で PASS が出ることを見る:

```bash
# 白黒 5Hz（30fps で 3 フレームずつ交互＝1 秒に 5 往復）→ Fail になるはず
ffmpeg -f lavfi -i "color=black:s=1280x720:r=30:d=5" -vf "geq=lum='if(mod(floor(N/3),2),235,16)':cb=128:cr=128" -c:v libx264 -pix_fmt yuv420p -crf 10 pos5hz.mp4
# 白黒 2Hz（7〜8 フレームずつ交互）→ PASS か警告のはず
ffmpeg -f lavfi -i "color=black:s=1280x720:r=30:d=5" -vf "geq=lum='if(mod(floor(N/7.5),2),235,16)':cb=128:cr=128" -c:v libx264 -pix_fmt yuv420p -crf 10 neg2hz.mp4
iris pos5hz.mp4 -o results/; iris neg2hz.mp4 -o results/
# 画面の 20% だけ 5Hz で光らせる版（ITU なら 25% 未満で合格、WCAG の 341×256 基準なら不合格になりうる）→ IRIS の面積の扱いを見る
ffmpeg -f lavfi -i "color=black:s=1280x720:r=30:d=5" -vf "geq=lum='if(lt(X,256)*mod(floor(N/3),2),235,16)':cb=128:cr=128" -c:v libx264 -pix_fmt yuv420p -crf 10 part20.mp4
iris part20.mp4 -o results/
```

  （`geq` の式は推測で組んだ。ffmpeg のバージョンで式の書き方が通らなければ直す）
- アゲアゲ版の結果は、秒ごとの表で「R3 の区間に `lumTrans` が 7 以上（＝3 閃光超）の秒があるか」「`lumResult=2`（5 秒の連続）があるか」で読む

### 所要の見込み（推測）

- Python 版の導入 5 分、3 分の 1080p 動画の解析は CPU で数分〜十数分（Python で 1 フレームずつ処理するので遅め。`--resize 0.5` で速くなるが結果が変わりうる）。合成動画での陽性対照を含めて 30〜60 分
- C++ 版のビルドは vcpkg で OpenCV を作るので 30 分〜数時間

## Open Questions

- IRIS が「画面全体の平均」で判定していることが、規格の「光っている領域」の判定とどれだけずれるか。合成動画（画面の一部だけ光る）で確かめる
- Python 移植と C++ 版の結果が一致するか（移植の README は境目で違うと書く）。C++ 版のビルドが WSL で通るか
- IRIS の判定と Harding FPA の判定がどれだけ一致するか（EA は書いていない）
- 30fps で 176BPM の拍（341ms）がコマに丸められたとき、IRIS の 1 秒の窓（30 フレーム）で数える遷移の数が拍の位相でどう揺れるか
- NHK・民放連の「輝度変化 20% 超の場面転換を 1 秒 3 回まで」は、IRIS の閾値（相対輝度 0.1、往復で数える）とは別の数え方。IRIS が PASS でも民放連の基準を超えることがある（[[web-motion-itu-r-bt1702-ofcom-nhk-minpo-flash-guidelines]]）
