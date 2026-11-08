---
type: source
summary: 動画のコマに焼いた文字のコントラスト比を機械で測るための原典。WCAG 2.2（W3C 勧告 2024-12-12）の相対輝度の式（sRGB を線形化、閾値は 2021-05 以降 0.04045）と、Understanding 1.4.3 の測り方の注（アンチエイリアスでなく指定色で測る、細い縁取りは文字・太い縁取りは背景、背景画像の上の文字は不足すると失敗例 F83）。動画のコマでは指定色が手に入らないので、コマの画素から文字と背景の色を推定して式に入れる手順（このページの推測）を書く
video_types: [any]
url: https://www.w3.org/TR/WCAG22/#dfn-relative-luminance
author: W3C（Accessibility Guidelines Working Group）
published: 2024-12-12（WCAG 2.2 W3C Recommendation）／Understanding 1.4.3 は継続更新（2026-11-09 取得）
retrieved: 2026-11-09
sources:
  - https://www.w3.org/TR/WCAG22/ （用語「relative luminance」「contrast ratio」の定義と注 1〜5 を読んだ）
  - https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html （Understanding SC 1.4.3。アンチエイリアス・縁取り・背景の注を読んだ）
  - https://developer.chrome.com/blog/cvd （Chrome DevTools のコントラスト検査の道具の列挙。Last updated 2025-07-04）
---

# 動画のコマで文字のコントラスト比を測る（WCAG 2.2 の式と測り方の注）

## 何の文献か

- **WCAG 2.2**: W3C の勧告（2024-12-12）。ウェブの内容のアクセシビリティの基準。動画に焼いた文字は WCAG の語で「images of text」にあたる。放送や SNS の動画に課される規則ではない
- **Understanding SC 1.4.3**: 同じ W3C の解説文書。基準の意図と測り方の注
- 4.5:1・3:1 の基準値とその根拠（視力 20/40 の感度低下）は既に [[web-layout-okabe-ito-cud-wcag-contrast]] にある。ここは**式の細部と、コマの画素で測るための注**だけを足す
- 動画のコマに対してコントラスト比を測る、定まった公開の道具は今回見つからなかった（探した範囲: Chrome DevTools・Lighthouse の説明。どちらも DOM の文字が対象）

## 書いてあること

### 相対輝度とコントラスト比（WCAG 2.2 の定義）

- sRGB の相対輝度: `L = 0.2126 R + 0.7152 G + 0.0722 B`。各成分は 8 bit 値を 255 で割り（RsRGB）、`RsRGB <= 0.04045` なら `RsRGB/12.92`、それ以外は `((RsRGB+0.055)/1.055)^2.4`
- 注 2: 「Before May 2021 the value of 0.04045 in the definition was different (0.03928). … It has no practical effect on the calculations」
- 注 3: 他の色空間と分かっていない限り sRGB で評価せよ
- 注 4: 配信後のディザは元の色で、作り手がディザした色は R・G・B それぞれの平均で
- コントラスト比 `(L1 + 0.05) / (L2 + 0.05)`（L1 が明るい方）。1〜21

### 測り方の注（Understanding 1.4.3）

- 「when evaluating this Success Criterion, refer to the foreground and background colors obtained from the user agent, or the underlying markup and stylesheets, rather than the text as presented on screen」— 画面に描かれた文字（アンチエイリアスで薄まった色）ではなく、指定した色で測れ
- ただし細い字や変わった書体は、アンチエイリアスで実際にはかなり薄く描かれ、名目上は合格でも実際のコントラストが低いことがある。その場合は余裕を持たせよ、と勧める（規範ではない）
- 「When there is a border around the letter, the border can add contrast and would be used in calculating the contrast between the letter and its background. A narrow border around the letter would be used as the letter. A wide border … acts as a halo and would be considered background」
- 背景の画像の上の文字でコントラストが足りないのは失敗例 F83

### Chrome DevTools（参考）

- Inspect の tooltip・色の picker・CSS Overview・Lighthouse がコントラスト不足の**文字要素**を出す、と書く（[[web-check-color-cvd-simulation-daltonlens-machado-chrome]] と同じ記事）。どれも DOM の文字が対象

## この wiki への含意

- **西尾の HTML の作り方では、文字は canvas に描かれる**（[[exp-html-capture-pipeline]]）。DOM の文字を見る道具（Lighthouse、DevTools の tooltip）は canvas の中の文字を測れない（推論）。測るなら (a) 描画コードの中の指定色で計算する（Understanding の言う「指定色」に当たる）か、(b) 撮ったコマの画素から推定する
- **(a) が正攻法**: `renderFrame` が使う文字色と背景色（単色の背景なら）を時刻表から抜き出して式に入れる。背景がグラデーション・粒子・動画のときは指定色が一つに決まらず、(b) が要る
- **(b) の注意**: コマは yuv420p に符号化された後のもの。色差が 1/4 に間引かれ、文字の縁で色が滲む（推論）。画素からの推定は「実際に見える」側の値で、Understanding の言う指定色とは違う。合否の判定ではなく、危ない場面を探す道具として使う
- **型ごと**: promo は文字が背景の映像に重なる（粒子・写真の上の字）ことが多く、(b) の対象。talk の字幕帯（[[exp-qualia-video]] の字幕）は帯の色が決まっていれば (a) で済む。embed は会場のプロジェクタで黒が浮き、コントラストが下がる（推測。測った例は wiki に無い）ので、基準より余裕を持たせる側
- 縁取り（stroke）・影で文字を立たせる作りは、Understanding の規則で「細い縁取りは文字の色として測る」。粒子の上の白文字に黒の細い縁を付けたなら、縁の黒と背景で測る

## 着手の仕方（未検証。galleria で確かめる）

- **何が表現できるようになるか / 効く型**: 背景が動く上の文字（promo）や字幕帯（talk）の読みやすさを、数字で場面ごとに洗い出す（any）
- **機械・入れるもの**: galleria WSL。ffmpeg と Python（`uv run --with pillow --with numpy` で一時環境。Pillow は MIT-CMU 系、numpy は BSD。費用・アカウントなし）。道具を新しく入れずに書ける規模
- **成熟度**: 式は WCAG 2.0（2008）から同じ（閾値の表記だけ 2021-05 に修正）
- **最小の手順**:
  1. 確かめたい秒のコマを PNG で抜く（HTML の作り方なら `node capture.mjs stills <秒>` の PNG がそのまま使える。符号化前の画素なので (a) に近い）:
     ```sh
     ffmpeg -hide_banner -ss 12.5 -i in.mp4 -frames:v 1 f_12_5.png
     ```
  2. 文字のある矩形（x, y, w, h）を決め、その中の輝度の上位と下位から文字色と背景色を推定してコントラスト比を出す（推測の手順。`contrast.py` として置く）:
     ```python
     # usage: uv run --with pillow --with numpy python3 -I contrast.py f.png x y w h
     import sys, numpy as np
     from PIL import Image
     f, x, y, w, h = sys.argv[1], *map(int, sys.argv[2:6])
     a = np.asarray(Image.open(f).convert('RGB'), dtype=np.float64)[y:y+h, x:x+w] / 255.0
     lin = np.where(a <= 0.04045, a / 12.92, ((a + 0.055) / 1.055) ** 2.4)
     L = lin @ np.array([0.2126, 0.7152, 0.0722])
     lo, hi = np.percentile(L, 5), np.percentile(L, 95)   # 暗い側・明るい側の代表
     print(f"L_lo={lo:.4f} L_hi={hi:.4f} ratio={(hi + 0.05) / (lo + 0.05):.2f}")
     ```
     背景が一様でないときは、矩形を文字の行より少し広く取り、暗い側（または明るい側）の 5 パーセンタイルではなく背景側の**最悪値**（文字色に一番近い背景の値）を取る版も作る（推測）
  3. 全編を走査するなら、1 秒ごとのコマ（`ffmpeg -i in.mp4 -vf fps=1 f_%04d.png`）に同じ矩形で回し、比が 4.5 を割る秒を一覧にする。字幕の位置が場面で変わるなら矩形も時刻表から取る
- **動いたと言える確かめ方**: 白地に黒（#000 on #fff）の PNG で ratio=21.00、#777 on #fff で 4.48 前後（WebAIM などの計算器と同じ値になる。計算器の値は手元で確かめる）。動画のコマで、目で読みにくいと感じた場面が上位に並ぶ
- **所要の見込み**（推測）: 1〜2 時間（矩形の決め方が手間の大半）

## Open Questions

- 動画のコマに WCAG の数値（4.5:1）をそのまま当てはめてよいかは、WCAG 自身は答えていない。字幕の規則（[[web-type-bbc-subtitle-guidelines]]、[[web-type-netflix-timed-text-style-guide]]）は箱・縁取りで対処する書き方で、比の数値は無い
- yuv420p への符号化と配信側の再符号化で、細い色付き文字のコントラストがどれだけ落ちるか。符号化前の PNG と配信後のコマを同じ手順で測れば分かる
- WCAG 3 の候補とされる別の見え方の指標（APCA など）は今回読んでいない
- プロジェクタ・スマホの屋外での見え方は sRGB の計算の外
