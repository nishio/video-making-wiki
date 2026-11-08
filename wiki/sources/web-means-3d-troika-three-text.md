---
type: source
summary: three.js の場面に日本語の文字を置く 2 つの方法の一次資料。troika-three-text（MIT、0.53.1）はフォントファイルを直接読んで SDF で平面の文字を描き、無いグリフは Noto のフォールバックを CDN から取る（自前で置くと約 300MB）。処理は非同期なので撮る前に sync の完了を待つ。厚みのある立体の文字は three.js の TextGeometry（typeface.json か TTFLoader）で作るが、TTFLoader は opentype.js を CDN から読み込む
video_types: [promo, talk, embed]
url: https://github.com/protectwise/troika/blob/main/packages/troika-three-text/README.md
author: protectwise/troika（Jason Johnston ほか）、three.js（TextGeometry・FontLoader・TTFLoader のソース）
published: unknown（README は継続更新。npm 0.53.1 は 2026-11-02）
retrieved: 2026-11-09
sources:
  - https://github.com/protectwise/troika/blob/main/packages/troika-three-text/README.md
  - https://registry.npmjs.org/troika-three-text
  - https://github.com/mrdoob/three.js/blob/dev/examples/jsm/geometries/TextGeometry.js
  - https://github.com/mrdoob/three.js/blob/dev/examples/jsm/loaders/FontLoader.js
  - https://github.com/mrdoob/three.js/blob/dev/examples/jsm/loaders/TTFLoader.js
---

# three.js で日本語の文字を出す（troika-three-text と TextGeometry）

## 何の文献か

- `troika-three-text` の README（作者の説明）。npm の最新 **0.53.1（2026-11-02）**、MIT。
- three.js の `TextGeometry`・`FontLoader`・`TTFLoader` のソース（dev ブランチ、JSDoc）。three は r187（[[web-means-3d-threejs-headless-webgl]]）。
- どちらも日本語を名指しした記述は無い。日本語に当てはめた所は推測として書く。

## 書いてあること

### troika-three-text（平面の文字、SDF）

- 「three.js の場面で質の高い文字を描く。**符号付き距離場（SDF）**を使い、標準の微分でアンチエイリアスをかける」。
- 「事前に作った SDF のテクスチャに頼らず、**フォントファイル（.ttf・.otf・.woff）を直接解析**し（Typr）、使うグリフの SDF のアトラスをその場で作る。カーニング、合字、右から左・双方向、アラビア文字のような連結する文字を扱い、**Unicode を全部覆うためにフォールバックのフォントを自動で読む**。フォントの解析・SDF の生成・配置はすべて Web Worker で行う」。
- 形式: `.ttf`・`.otf`・`.woff`。**`.woff2` は非対応**。既定のフォントは Google Fonts の CDN から読む Roboto。
- 配置したジオメトリを組み立て、**任意の three.js の Material を「パッチ」して** SDF のシェーダを足すので、**three.js の組み込みの Material の光・PBR・影・霧が使える**。
- Unicode のフォールバック: 「設定した `font` に無い文字は、unicode-font-resolver で適切なフォールバックを探す。**Google の Noto Fonts が覆う全 Unicode の範囲**がこの方法で覆われる」「既定ではデータの索引とフォントファイルを **jsDelivr の CDN** から読む。自前で置けるが、**全データとフォントで約 300MB**」。`unicodeFontsURL` で置き場を変える。
- 非同期: 「文字の処理は Web Worker で行うので、定義上非同期。文字がすぐに見えたり、ジオメトリが完全だったりすることを当てにできない」。`sync(callback)` か `synccomplete` イベントで完了を待つ。
- 先読み: `preloadFont({font, characters, sdfGlyphSize}, callback)` で「最初の表示の長い間を避けるため、フォントを先に読み、**指定した文字の SDF を前もって作る**」。合字があるなら合字の並びも指定する。
- その他の性質: `anchorX`・`anchorY`（`'top-baseline'` など）、`maxWidth`・`whiteSpace`、`clipRect`、**`curveRadius`（文字の平面を円柱に沿って曲げる）**、`strokeWidth`・`outlineWidth`（縁取り）、`fillOpacity`、`sdfGlyphSize`（2 のべき乗。大きいほど角が鋭く細い線が消えにくいが、メモリと生成時間が増える）、`gpuAccelerateSDF`（WebGL で SDF を作る。「まだやや実験的」）、範囲ごとの色・フォント・大きさ。
- CSP の厳しい環境では Worker を作れないので、メインスレッドで（非同期のまま）動かす設定がある。

### three.js の TextGeometry（厚みのある立体の文字）

- `TextGeometry` は `ExtrudeGeometry` を継承し、文字の輪郭を押し出して立体にする（`size`・`depth`・`curveSegments`・ベベル）。フォントは「**typeface.json**（facetype.js で生成）を使う」。
- `FontLoader.generateShapes(text, size, direction)` の `direction` は `'ltr'`・`'rtl'`・**`'tb'`（上から下）**。
- `TTFLoader` は「TTF を読み、typeface JSON に変換して `Font` を作る」。r187 のソースは `import opentype from 'https://cdn.jsdelivr.net/npm/opentype.js@1.3.4/+esm'` で、**opentype.js を CDN から読み込む**。

## この wiki への含意

- **西尾の文字は Hiragino 頼みだった**（[[exp-html-capture-pipeline]]: 「文字は Mac のシステムフォント。別の機械で撮ると変わる」）。troika も TextGeometry も**フォントファイルを明示して読む**ので、galleria でも Mac でも同じ字形になる。一方で、troika の既定のフォールバックは CDN の Noto なので、フォントを明示しないと「撮った日の CDN の版」に依存する。日本語用のフォント（例: Noto Sans JP、SIL OFL）を作業場に置いて `font` に指定し、`preloadFont` で全文字を先に作るのが、決定論の撮影に合う（推測）。
- **撮影の待ち**: 西尾の方式の `window.ready`（フォントの読み込みと下準備が済むまで撮らない）に、troika の `sync` の完了を足す必要がある。足さないと最初の数コマで文字が欠ける（README の「すぐに見えると当てにできない」から推測）。
- **平面の文字で足りることが多い**: 説明動画の 3D 空間のラベル（talk・embed）は troika の平面の文字で足り、光と影も効く。厚みのある立体の文字（promo のタイトル）は TextGeometry で、日本語なら使う文字だけを typeface.json にする（全字を入れた日本語フォントの JSON は大きくなる。推測、測っていない）。
- 縦書きは troika の README に記述が無い。TextGeometry の `direction: 'tb'` は字を上から並べるだけで、句読点の位置や回転などの縦組みの規則を扱うとは書いていない。

## 着手の仕方（未検証。galleria で確かめる）

- **何が表現できるようになるか / 効く型**: 3D の場面の中の日本語ラベル・見出し（光と影を受ける、円柱に沿って曲がる、縁取り）、立体のタイトル文字。promo（立体のタイトル）、talk・embed（3D の図のラベル）
- **機械**: [[web-means-3d-threejs-headless-webgl]] と同じ（galleria Windows で GPU。WSL は未確認）。入れるもの: `troika-three-text@0.53.1`、`three@0.187.0`、日本語フォントのファイル（.ttf / .otf。.woff2 不可）。費用 0、アカウント不要。ライブラリは MIT。フォントの利用条件は別に確かめる（means-sound-font の担当の範囲）
- **成熟度**: 0.53.1（2026-11-02）、0.x のまま更新が続く
- **最小の手順（Windows。推測を含む）**:
  ```powershell
  cd $HOME\video-tools-trial\three
  npm i troika-three-text@0.53.1
  # fonts\NotoSansJP-Bold.ttf を置く（西尾が入手。CyEC2 ではダウンロードしない）
  # scene.html に足す（推測）:
  #   import { Text, preloadFont } from 'troika-three-text';   // import map で node_modules を指す
  #   const LINES = ['合意はどこにあるか', '意見の地図'];
  #   window.ready = new Promise(r => preloadFont({ font: './fonts/NotoSansJP-Bold.ttf', characters: LINES.join('') }, r))
  #     .then(() => { label.text = LINES[0]; label.font = './fonts/NotoSansJP-Bold.ttf'; return new Promise(r => label.sync(r)); });
  #   renderFrame(f) の中では label.text を変えない（変えると再び非同期の sync が走る。推測）
  node capture.mjs stills 0 2
  ```
- **動いたと言える確かめ方**: (1) f=0 の静止画で日本語が欠けず豆腐（□）も無い、(2) 撮影中の request ログに `cdn.jsdelivr.net` が出ない（フォールバックが走っていない）、(3) 同じ f を 2 回撮って `cmp` が一致、(4) カメラを 45 度回したコマで文字の縁がにじまない（`sdfGlyphSize` を 64 → 128 で見比べる）
- **所要の見込み（推測）**: three.js の最小例が動いた後なら 2〜3 時間

## Open Questions

- troika は文字の内容を変えるたびに非同期の sync が走る。字幕のように毎コマ文字が変わる使い方で、決定論の撮影をどう保つか（全文字を先に用意し、表示だけ切り替える？）は文献に無い
- 日本語フォントのグリフ数で SDF のアトラスがどれだけメモリを使うか、`gpuAccelerateSDF` が headless で動くかは書かれていない
- TTFLoader の opentype.js の CDN 読み込みは、オフラインの機械では失敗する。three の npm パッケージの中で import の先を差し替える方法は読んでいない
- 縦書きの日本語を 3D で出す方法は見つけていない
