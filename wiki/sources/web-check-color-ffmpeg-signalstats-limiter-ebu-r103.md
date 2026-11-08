---
type: source
summary: 映像信号の範囲（放送の「broadcast safe」）と色空間の機械検査の原典。EBU R 103 v3.0（2020-05）は 8 bit で公称 16–235、許容 5–246 を超えた信号を gamut error とし、画面の 1% を超えたときだけ警告せよ、legaliser は慎重に、と書く。ffmpeg の signalstats は Y/U/V の最小・最大・分位と、範囲外の画素の割合 BRNG（Y 16–235、UV 16–240）を出し、limiter は値を切る。YouTube は SDR を BT.709 で上げることを勧め、色空間が未指定なら BT.709 とみなし、フルレンジはリミテッドに変換すると書く
video_types: [any]
url: https://tech.ebu.ch/docs/r/r103.pdf
author: EBU 技術委員会／FFmpeg project／BAVC・MediaArea（QCTools）／Google（YouTube ヘルプ）
published: 2020-05（EBU R 103 v3.0）／unknown（ffmpeg 文書は git master、2026-11-09 取得）／unknown（QCTools 文書、YouTube ヘルプ。2026-11-09 取得）
retrieved: 2026-11-09
sources:
  - https://tech.ebu.ch/docs/r/r103.pdf （EBU R 103「Video Signal Tolerance in Digital Television Systems」v3.0、2020-05。本文を読んだ）
  - https://ffmpeg.org/ffmpeg-filters.html （11.239 signalstats、11.153 limiter、11.223 scale の in/out_color_matrix・range）
  - https://raw.githubusercontent.com/FFmpeg/FFmpeg/master/libavfilter/vf_signalstats.c （BRNG の判定と値の算出を読んだ）
  - https://bavc.github.io/qctools/filter_descriptions.html （QCTools の説明。broadcast range の線の意味）
  - https://support.google.com/youtube/answer/1722171 （YouTube recommended upload encoding settings の Color Space の節）
---

# 映像信号の範囲と色空間の検査: EBU R 103、ffmpeg の signalstats・limiter、YouTube の色空間

## 何の文献か

- **EBU R 103 v3.0**（2020-05）: 欧州放送連合の勧告。放送の映像信号の許容範囲。ネット動画に課されるものではない
- **ffmpeg の文書とソース**: signalstats はアナログ映像のデジタル化の点検のために作られた計測フィルタ（文書の冒頭）。limiter は値を範囲に切るだけのフィルタ
- **QCTools の文書**（BAVC と MediaArea のオープンソースの点検ツール。signalstats の値をグラフにする）: 範囲の線の意味の説明に使った
- **YouTube のヘルプ**「YouTube recommended upload encoding settings」: ページの冒頭に「These features are only available to partners who use YouTube Studio Content Manager」と出るが、中身は一般のアップロードの推奨として書かれている（読み方は Open Questions）

## 書いてあること

### EBU R 103 v3.0

- YUV のまま処理すると、RGB に戻したとき 0〜100% を外れる「illegal」な組み合わせができる。小さなはみ出しは避けにくいので許容幅を設ける
- 勧告: 「the RGB components and the corresponding Luminance (Y) signal should not normally exceed the "Preferred Minimum/Maximum" range」
- Table 1（8 bit）: 公称 16–235、**Preferred Min./Max. 5–246**、Total Video Signal Range 1–254。10 bit は 64–940 / 20–984 / 4–1019
- 範囲外は「gamut error」。計測は横に 1/16・2/16・3/16・4/16・3/16・2/16・1/16、縦に 1/4・1/2・1/4 のフィルタを通してから
- 「measuring equipment should indicate an "Out-of-Gamut" occurrence only after the error exceeds 1% of the image」
- 「colour gamut "legalisers" should be used with caution as they may create artefacts in the picture that are more disturbing than the gamut errors」「not "legalise" video signals before all signal processing has been carried out」

### ffmpeg の signalstats（11.239）

- 既定でコマごとに YMIN・YLOW（10 パーセンタイル）・YAVG・YHIGH（90）・YMAX、U・V も同じ、SATMIN〜SATMAX、HUEMED・HUEAVG、YDIF（前のコマとの差の平均）などをメタデータに出す（8 bit で 0–255）
- `stat=brng` で「pixels that fall outside of legal broadcast range」を数える。ソースでは Y < 16 or > 235、U・V < 16 or > 240 を範囲外とし、メタデータ `lavfi.signalstats.BRNG` は**範囲外の画素の割合**（範囲外の数 ÷ 画素数）
- `out=brng:color=red` で範囲外の画素を赤く塗った映像を出せる
- 文書の例: `ffprobe -f lavfi movie=example.mov,signalstats -show_entries frame_tags=lavfi.signalstats.YMAX,lavfi.signalstats.YMIN`

### ffmpeg の limiter（11.153）と scale

- limiter: 「Limits the pixel components values to the specified range [min, max]」。`min=auto`/`max=auto` は「use the minimum/maximum signal level for the input colorspace (only affects TV-range YUV signals)」
- scale: `in_color_matrix`/`out_color_matrix`（bt709・bt601 など）、`in_range`/`out_range`（full=0–255、limited=16–235）を上書き・指定できる。「If not specified, the color space type depends on the pixel format」と書くだけで、RGB の PNG を yuv420p にするときの既定の行列は文書に明記が無い

### QCTools の説明

- 8 bit の Y の 235 は「broadcast white」、16 は「broadcast black」。235–255 は同じ白に、0–16 は同じ黒に切られて表示される。「these lines are only applicable to content that is decoded as broadcast range. Content marked as full range may appropriately exceed these limits」

### YouTube（Color Space の節）

- 「YouTube recommends BT.709 as the standard color space for SDR uploads」（TRC・原色・行列とも BT.709）
- TRC が未指定なら BT.709 とみなす。行列と原色が未指定なら BT.709 とみなす。BT.601 と BT.709 が混ざっていたら行列に合わせる
- 「YouTube converts full color range to limited color range」。RGB の行列での上げ方は推奨しない、sRGB の TRC は BT.709 に変換される、と書く

## この wiki への含意

- **ネット動画で効くのは「放送の範囲」より「色空間の札（タグ）」**。西尾の HTML の作り方は、canvas の PNG（sRGB・フルレンジの RGB）を ffmpeg で `-pix_fmt yuv420p` の H.264 にしている（[[exp-html-capture-pipeline]]）。このとき (1) どの行列で RGB→YUV にしたか、(2) 出力に BT.709 の札が付いているか、が配信先での色に効く。YouTube は札が無ければ BT.709 とみなすので、実際に BT.601 の行列で変換されていると色が少しずれる（推論。ffmpeg の既定の行列は文書に明記が無く、確かめていない）
- 確かめ方は `ffprobe` の `color_space`・`color_primaries`・`color_transfer`・`color_range`。明示したいなら `-vf scale=out_color_matrix=bt709:out_range=tv,format=yuv420p -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv`（推測で組んだもの。galleria で確かめる）
- **BRNG は「画面の何割が 16–235 の外か」の数字**。HTML で純白（#fff）・純黒（#000）を使うと、リミテッドレンジに変換された時点で 235・16 に収まるはずで、BRNG は出ないのが期待（推論）。出るなら変換か符号化の段ではみ出している。EBU は 1% を超えたら警告、と書く
- **limiter をかけるかどうか**: EBU は legaliser に慎重であれと書き、ネット配信では YouTube が自分でリミテッドに変換する。西尾の用途では「測って記録し、問題が出たら変換の設定を直す」で足り、limiter で切る場面は少ない（推論）
- **閃光の検査との関係**: signalstats の YAVG・YDIF はコマごとの明るさとその変化。閃光の判定（[[web-motion-itu-r-bt1702-ofcom-nhk-minpo-flash-guidelines]]）の素朴な前段に使えるが、判定の基準そのものではない（判定の道具は閃光の担当のページ）
- 型ごと: どの型にも共通（any）。embed で会場のプロジェクタに出すとき、PC の再生ソフトがリミテッドをフルとして扱うと黒が浮く・白が飛ぶ、という問題は放送の範囲の問題と同じ根（推測。会場での記録は無い）

## 着手の仕方（未検証。galleria で確かめる）

- **何が表現できるようになるか / 効く型**: 書き出した動画の色の札・範囲を毎回機械で点検し、配信先で色がずれる・黒が浮く原因を潰す（any）
- **機械・入れるもの**: galleria WSL の ffmpeg・ffprobe だけ。費用・アカウントなし
- **成熟度**: signalstats・limiter は ffmpeg に長く入っている。R 103 は 2020 年版
- **最小の手順**:
  ```sh
  # 1. 色の札
  ffprobe -v error -select_streams v:0 -show_entries stream=pix_fmt,color_range,color_space,color_primaries,color_transfer -of default=nw=1 in.mp4
  # 2. コマごとの範囲と BRNG を CSV 風に
  ffprobe -v error -f lavfi "movie=in.mp4,signalstats=stat=brng" -show_entries frame=pts_time:frame_tags=lavfi.signalstats.YMIN,lavfi.signalstats.YMAX,lavfi.signalstats.BRNG -of csv=p=0 > sig.csv
  sort -t, -k4 -g sig.csv | tail -5          # BRNG の大きいコマ（列の順は出力で確かめる）
  # 3. 範囲外を赤く塗った確認用の動画
  ffmpeg -i in.mp4 -vf "signalstats=out=brng:color=red" -an -c:v libx264 -crf 20 brng_view.mp4
  # 4. 札を付けて書き出した版と比べる（推測の設定）
  ffmpeg -i in.mp4 -vf "scale=out_color_matrix=bt709:out_range=tv,format=yuv420p" -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv -c:v libx264 -crf 16 -c:a copy in_709.mp4
  ```
  `movie=` の中のパスは WSL の相対パスにする（Windows のパスは `:` と `\` で壊れる。[[exp-galleria-ffmpeg-measurement-and-delivery]]）
- **動いたと言える確かめ方**: 1 で `color_space=bt709` などが出る（未指定なら `unknown`）。2 の `sig.csv` に全コマの行があり、BRNG が 0〜1 の数。3 で純白・純黒の場面が赤くならない。4 の後に 1 を回して bt709・tv が付いている
- **所要の見込み**（推測）: 30 分〜1 時間

## Open Questions

- ffmpeg が RGB の PNG を yuv420p にするときの既定の行列（BT.601 か BT.709 か）と札の有無。経験の書き出し（`-f image2pipe … -pix_fmt yuv420p`）で実物を ffprobe すれば分かる
- YouTube のヘルプの冒頭の「Content Manager のパートナー向け」の注が、Color Space の節まで含むのか。一般の上げ手にも同じ扱いだと読んだが、確かめていない
- X・Instagram・TikTok が色空間の札をどう扱うかの公式記述は見つけていない
- BRNG（16–235 の外）と EBU の Preferred（5–246）は基準が違う。EBU に合わせるなら YMIN < 5 か YMAX > 246 のコマを数える
