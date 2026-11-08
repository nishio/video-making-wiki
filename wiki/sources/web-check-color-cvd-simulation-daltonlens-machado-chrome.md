---
type: source
summary: 色覚の多様性の見え方を機械で模擬する手段の原典。DaltonLens の作者による公開実装の総説（2021）は、P 型・D 型には Viénot 1999・Brettel 1997・Machado 2009 が使え、T 型は Brettel 1997 だけが妥当、Coblis v1（ColorMatrix）は使うな、sRGB の復号を省いた実装が多いと書く。Machado らは強さ 0〜1 の 3×3 行列を公開し、Chrome はその行列で DevTools と Puppeteer の emulateVisionDeficiency を実装している。ffmpeg の colorchannelmixer は 3×3 の行列をかけられるが、線形化しないので近似
video_types: [any]
url: https://daltonlens.org/opensource-cvd-simulation/
author: Nicolas Burrus（DaltonLens）／Gustavo M. Machado, Manuel M. Oliveira, Leandro A. F. Fernandes（UFRGS）／Mathias Bynens（Google Chrome）／Puppeteer・Chrome DevTools Protocol／FFmpeg
published: 2021-10-19（DaltonLens の総説。2021-11 に追記）／2009（Machado ら、IEEE TVCG 15(6)）／Chrome の記事は Last updated 2025-07-04
retrieved: 2026-11-09
sources:
  - https://daltonlens.org/opensource-cvd-simulation/ （「Review of Open Source Color Blindness Simulations」2021-10-19。全文を読んだ）
  - https://github.com/DaltonLens/DaltonLens-Python （README と LICENSE（MIT）。PyPI の daltonlens 0.1.5 は 2021-11-22）
  - https://github.com/DaltonLens/libDaltonLens （README。C の単一ファイル、public domain）
  - https://www.inf.ufrgs.br/~oliveira/pubs_files/CVD_Simulation/CVD_Simulation.html （Machado らの論文の補助ページ。Tutorial と Table 1 の行列を読んだ。論文本文は未読）
  - https://developer.chrome.com/blog/cvd （Mathias Bynens「Simulating color vision deficiencies in the Blink Renderer」）
  - https://pptr.dev/api/puppeteer.page.emulatevisiondeficiency （Puppeteer の API 文書）
  - https://raw.githubusercontent.com/ChromeDevTools/devtools-protocol/master/json/browser_protocol.json （Emulation.setEmulatedVisionDeficiency の型の一覧）
  - https://ffmpeg.org/ffmpeg-filters.html （11.31 colorchannelmixer）
---

# 色覚の模擬: DaltonLens の総説、Machado 2009 の行列、Chrome／Puppeteer、ffmpeg

## 何の文献か

- **DaltonLens の総説**（2021-10-19）: 色覚補助アプリ DaltonLens の作者（本人が軽い P 型と書く）が、公開されている模擬の実装を原論文に当たって比べた技術ブログ。査読論文ではない。各手法の妥当性の判断は、引用している検証研究（Simon-Liedtke & Farup 2016、Lillo ら 2014）と、2021-11 の追記で reddit の r/colorblind で集めた当事者の反応による
- **Machado ら 2009**: 生理学に基づく模擬のモデル（IEEE TVCG）。補助ページに強さ 0.0〜1.0（0.1 刻み）の 3×3 行列を公開。論文本文は読んでいない
- **Chrome の記事**（Google の DevTools 担当、Last updated 2025-07-04）と **Puppeteer の API 文書**: ブラウザに組み込まれた模擬の実装の説明
- 「模擬は 2 色覚の型を真似たもので全員がそう見えるわけではない、当事者に見てもらえ」という CUD の注意は [[web-layout-okabe-ito-cud-wcag-contrast]] にある

## 書いてあること

### DaltonLens の総説

- 手法の系譜: Brettel, Viénot & Mollon 1997（JOSA A）→ Viénot, Brettel & Mollon 1999（P 型・D 型向けに簡略化、ディスプレイ向け）→ Machado ら 2009（異常 3 色覚も扱う）。古い Coblis v1 の「ColorMatrix」は、作者自身が「一晩のハック」と言った 3 色だけ合わせた行列で、sRGB の非線形も無視している
- 推奨（原文の要旨）:
  - T 型には「the Brettel 1997 approach is still the most solid and basically only valid choice」
  - P 型・D 型には Viénot 1999・Brettel 1997・Machado 2009 のどれも「solid choices」で、極端な値で Viénot がやや良い。異常 3 色覚（強さ < 1）なら Machado の方が理屈が通る
  - 「Coblis V1 (ColorMatrix) should never be used」
- **2021-11 の追記**: 当事者の反応を集めると Brettel 1997 と Viénot 1999（sRGB に合わせたもの）が勝ち、「Machado 2009 consistently ranks lower」。原因として sRGB の復号の扱いを疑い、2 色覚には勧めない、と書き直している
- よくある誤り: Fidaner らの daltonize（2005）の流れのコードは**ガンマの復号をせずに**行列を生の RGB にかけるものが多く、「This makes a whole range of colors look way too dark」
- 「All these models are based on _average_ observers」（Brettel 1997 でも D 型 4 人のうち 2 人と 2 人で錐体の感度の山が違った）
- 自作の実装: **libDaltonLens**（C の単一ファイル、public domain、Brettel 1997 と Viénot 1999）、**DaltonLens-Python**（3 手法を単体テスト付きで）、SVG フィルタ版

### DaltonLens-Python（README）

- CLI: `daltonlens-python [--model vienot|brettel|machado|auto] [--filter simulate|daltonize] [--deficiency protan|deutan|tritan] [--severity 0..1] input_image output_image`
- ライセンス MIT（Copyright (c) 2021 DaltonLens）。PyPI の最新は **0.1.5（2021-11-22）**。以後の版は出ていない

### Machado ら 2009（補助ページ）

- 模擬は 1 回の 3×3 行列の積（Eq. 1）。強さ 1.0（2 色覚に当たる）の行列（Table 1、行は出力の R, G, B）:
  - Protan: `0.152286 1.052583 -0.204868 / 0.114503 0.786281 0.099216 / -0.003882 -0.048116 1.051998`
  - Deutan: `0.367322 0.860646 -0.227968 / 0.280085 0.672501 0.047413 / -0.011820 0.042940 0.968881`
  - Tritan: `1.255528 -0.076749 -0.178779 / -0.078411 0.930809 0.147602 / 0.004733 0.691367 0.303900`
- 中間の強さは近い 2 行列を線形補間してよい、と書く。行列を線形 RGB にかけるかガンマのままかは、補助ページの Tutorial には書かれていない（DaltonLens の追記の論点）

### Chrome DevTools と Puppeteer

- DevTools の Rendering タブに模擬がある。値は「based on a physiologically accurate color vision deficiency simulation model by Machado, Oliveira, and Fernandes」で、SVG の `feColorMatrix` に Machado の D 型の行列（0.367 0.861 −0.228 …）を入れる例を示す。ページの DOM を変えずに描画の段で掛ける実装だと書く
- Puppeteer: `page.emulateVisionDeficiency(type)`。例は `achromatopsia`・`deuteranopia`・`blurredVision`・`reducedContrast` を順に掛けて `page.screenshot` を撮る
- Chrome DevTools Protocol の型: `none, blurredVision, reducedContrast, achromatopsia, deuteranopia, protanopia, tritanopia`。説明は「best-effort emulations come first, followed by any physiologically accurate emulations for medically recognized color vision deficiencies」

### ffmpeg の colorchannelmixer（11.31）

- 出力の各チャンネルを入力の R・G・B・A の線形結合で作る（`red=red*rr + blue*rb + green*rg + alpha*ra`）。係数は −2.0〜2.0。例はグレースケールとセピア
- 文書には線形化の記述は無く、符号化された値（ガンマのかかった値）にそのまま掛かる（推論。DaltonLens が「too dark」と書く誤りと同じ形になる）

## この wiki への含意

- **HTML で描く作り方（[[exp-html-capture-pipeline]]）に一番近い道具は Puppeteer の emulateVisionDeficiency**。capture.mjs は既に puppeteer-core を使っている。ただし capture.mjs は `canvas.toDataURL` で画素を取っていて、模擬は描画の段（合成）で掛かる。**`toDataURL` の画素には模擬が乗らず、`page.screenshot` にだけ乗る**はず（推論。確かめる）。stills を screenshot で撮る版を足すのが最小の変更
- **Chrome の実装は Machado**、DaltonLens の追記では 2 色覚に Machado は低評価。Chrome の結果だけで判断せず、DaltonLens-Python の Brettel／Viénot でも同じコマを見る、が文献に沿う
- 確かめる対象は「色だけで区別しているところ」。CUD の原則（[[web-layout-okabe-ito-cud-wcag-contrast]]）は形・線種・ラベルを重ねること。模擬は、その原則を守れているかの点検に使う（模擬で区別できたから大丈夫、ではない）
- 型ごと: embed（図解・グラフの色分け）と talk（比較の色）で効く。promo の雰囲気の色は対象外になりがち
- 動画全体を流して見たいときだけ ffmpeg の colorchannelmixer に Machado の行列を入れる。線形化しないので暗く出る近似で、判定には使わない

## 着手の仕方（未検証。galleria で確かめる）

- **何が表現できるようになるか / 効く型**: 色分けの図・グラフが P 型・D 型・T 型の人にどう見えるかを、作る途中で並べて見る（embed・talk）
- **機械・入れるもの**:
  - A（静止画を正しく）: galleria WSL、`uvx --from daltonlens daltonlens-python`（0.1.5、MIT、費用なし）。依存（numpy・Pillow）は uv が入れる
  - B（HTML のまま）: Mac か galleria（node と Chrome／Chromium が要る。capture.mjs と同じ puppeteer-core）
  - C（動画全体の近似）: ffmpeg だけ
- **成熟度**: DaltonLens-Python は 2021-11 以降リリースなし（手法は 1997〜2009 の論文で固まっている）。Chrome の DevTools は継続更新
- **最小の手順**:
  - A（WSL）:
    ```sh
    for d in protan deutan tritan; do
      uvx --from daltonlens daltonlens-python -m auto -d $d -s 1.0 f_12_5.png sim_${d}.png
    done
    # 並べて 1 枚に
    ffmpeg -i f_12_5.png -i sim_protan.png -i sim_deutan.png -i sim_tritan.png -filter_complex "[0][1][2][3]xstack=inputs=4:layout=0_0|w0_0|0_h0|w0_h0" cvd_grid.png
    ```
    `-m auto` は README の既定（手法を自動で選ぶ）。T 型に Brettel が選ばれるかは手元で確かめる
  - B（capture.mjs に足す。推測で補ったコード）:
    ```js
    for (const t of ['none','protanopia','deuteranopia','tritanopia','achromatopsia']) {
      await page.emulateVisionDeficiency(t);
      await page.screenshot({ path: `stills/cvd_${t}_${sec}.png` });
    }
    ```
  - C（WSL、近似）: `ffmpeg -i in.mp4 -vf "colorchannelmixer=rr=0.367322:rg=0.860646:rb=-0.227968:gr=0.280085:gg=0.672501:gb=0.047413:br=-0.011820:bg=0.042940:bb=0.968881" -c:a copy deutan_approx.mp4`
- **動いたと言える確かめ方**: A は `sim_deutan.png` で赤と緑の区別が消え、青と黄の軸が残る。`cvd_grid.png` が 2×2 で出る。B は `cvd_none` と `cvd_deuteranopia` の PNG のハッシュが違う（模擬が screenshot に乗った）。同じ秒の `toDataURL` 版と比べて、乗らないことも確かめる。C は 1 コマ抜いて A と並べ、C の方が暗いことを確かめる（線形化の有無の差）
- **所要の見込み**（推測）: A は 30 分、B は capture.mjs の改造で 1 時間

## Open Questions

- Chrome の模擬が `toDataURL` に乗らないかは推論のまま
- DaltonLens の「Machado は 2 色覚で低評価」は当事者の reddit での反応の集計で、統制した実験ではない
- 模擬は平均的な観察者のもの。西尾の動画を当事者に見てもらった記録は wiki に無い
- DaltonLens-Python の `auto` がどの手法を選ぶかは README に明記が無い
