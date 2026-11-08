---
type: source
summary: three.js の場面を render(t) の時刻の純関数として描き、headless Chrome で 1 コマずつ撮るための一次資料。WebGL の描画バッファは合成のあと消えるので「撮る直前に描く」か preserveDrawingBuffer を使う（WebGL 仕様・three.js manual）。headless の Chromium は GPU を切ることが多く、Remotion は --gl=angle を勧める。SwiftShader（CPU）への自動の逃げ道は廃止方向で --enable-unsafe-swiftshader が要る。WSL の GPU は WSLg の vGPU 経由の OpenGL で、galleria では Windows 側の Chrome で撮るのが確かめやすい
video_types: [promo, talk, embed]
url: https://github.com/mrdoob/three.js/blob/dev/manual/pages/tips.html
author: three.js（mrdoob ほか、manual・WebGLRenderer のソース）、Khronos（WebGL 1.0 仕様）、Remotion AG（GPU・--gl の docs、open-browser.ts）、Chromium（swiftshader.md）、Google（Chrome headless の docs）、Microsoft（WSL の docs）、NVIDIA（CUDA on WSL User Guide）
published: unknown（各 docs は継続更新。版は本文）
retrieved: 2026-11-09
sources:
  - https://registry.npmjs.org/three （0.187.0 = r187、2026-10-30）
  - https://github.com/mrdoob/three.js/blob/dev/manual/pages/tips.html （Taking A Screenshot of the Canvas / Preventing the canvas being cleared）
  - https://github.com/mrdoob/three.js/blob/dev/src/renderers/WebGLRenderer.js （preserveDrawingBuffer の JSDoc）
  - https://github.com/KhronosGroup/WebGL/blob/main/specs/latest/1.0/index.html （2.2 The Drawing Buffer。registry.khronos.org は Cloudflare の確認画面で読めず、GitHub の原稿を読んだ）
  - https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/getContext
  - https://github.com/remotion-dev/remotion/blob/main/packages/docs/docs/gpu.mdx
  - https://github.com/remotion-dev/remotion/blob/main/packages/docs/docs/open-gl.mdx
  - https://github.com/remotion-dev/remotion/blob/main/packages/renderer/src/open-browser.ts
  - https://github.com/remotion-dev/remotion/blob/main/packages/docs/docs/three-canvas.mdx
  - https://chromium.googlesource.com/chromium/src/+/main/docs/gpu/swiftshader.md
  - https://developer.chrome.com/docs/chromium/headless （最終更新 2024-10-21）
  - https://github.com/MicrosoftDocs/WSL/blob/main/WSL/tutorials/gui-apps.md （ms.date 2025-06-08）
  - https://docs.nvidia.com/cuda/wsl-user-guide/index.html （最終更新 2026-11-02）
  - https://github.com/whaleyxbt/claude-motion （web-sims/SKILL.md。既存ページ web-opus-whaleyxbt-claude-motion で読んだもの）
---

# three.js を render(t) で描き、headless Chrome で撮る

## 何の文献か

- three.js: npm `three` の最新は **0.187.0（r187、2026-10-30）**、MIT。manual の「Tips」頁（GitHub の原稿）と `WebGLRenderer.js` の JSDoc。
- WebGL 1.0 仕様（Khronos）の「2.2 The Drawing Buffer」。公式サイトは Cloudflare の確認画面で止まったので回避せず、Khronos の GitHub にある仕様の原稿を読んだ。
- Remotion の docs（「Using the GPU」「--gl flag」）と、Remotion が `--gl` の値を Chromium の起動フラグに変換するソース `open-browser.ts`。Remotion は three.js を撮る道具を作っている当事者で、GPU の有無で困った経験から書いている。
- Chromium の `swiftshader.md`、Chrome の headless の docs。
- Microsoft の WSL の docs（GUI アプリ）、NVIDIA の CUDA on WSL User Guide。
- 効果の測定（速さ・画質）は、どの文献にも無い。

## 書いてあること

### 時刻の純関数で描く

- whaleyxbt の web-sims skill: 群れ・粒子・3D は Remotion でなく 1 枚の HTML（three.js）で `render(t)` を時刻の純関数にし、**状態のあるシミュレーションは読み込み時に一度だけ回す**（[[web-opus-whaleyxbt-claude-motion]]）。
- Remotion の `<ThreeCanvas>`（`@remotion/three`、React Three Fiber の Canvas の包み）: 「React Three Fiber の `useFrame` でなく、Remotion の `useCurrentFrame` で宣言的にアニメを書かなければならない（must）。そうすればタイムラインを前後にスクラブでき、止められる」。**描画中は `frameloop` を `'never'` に上書きし、場面は `advance()` で必要なときだけ描き直す**。テクスチャを非同期に更新するなら `invalidate()` でなく `advance(performance.now())` で同期的に描き直してからコマを撮れ、と書く。
- OpenFilm も `frame(t)` の中で three.js・WebGL を使ってよいとする（[[web-opus2-remotion-openfilm-manim-after-2026-09-22]]）。

### WebGL の描画バッファは消える（仕様と manual）

- WebGL 仕様 2.2: 「既定では、合成（compositing）の後、描画バッファの内容は既定値に消去される。この既定の振る舞いは `preserveDrawingBuffer` 属性で変えられる。true なら、作者が消すか上書きするまで内容は保たれる。**false なら、描画の関数が戻った後にこの文脈を画像の元として使う操作（`readPixels`・`toDataURL`・別の文脈の `texImage2D`・`drawImage`・ImageBitmap の作成）は未定義の動作になりうる**」。
- three.js manual「Taking A Screenshot of the Canvas」: ボタンを押して `canvas.toBlob` で撮ると「真っ黒な画像」になる。「性能と互換性の理由で、ブラウザは WebGL の canvas の描画バッファを描いた後に消すから」。**解決は「撮る直前に描画のコードを呼ぶ」**。そのために `render()` を rAF のループから切り出し、時刻を `state.time` に置く例を示す。
- 別の解として「`preserveDrawingBuffer: true` を `WebGLRenderer` に渡す。これでブラウザは canvas を消さない。three.js にも消さないよう `renderer.autoClearColor = false` を伝える」（こちらはユーザーが動く物で絵を描くような、前のコマを残したい場合の例）。
- `WebGLRenderer` の JSDoc: `preserveDrawingBuffer`（既定 false）「手で消すか上書きするまでバッファを保つか」。`powerPreference`（`'default' | 'low-power' | 'high-performance'`）は「どの GPU 構成が適するかのヒント」。

### headless の Chromium と GPU（Remotion・Chromium）

- Remotion「Using the GPU」: 「多くの場合、headless では GPU が無効で、描画がかなり遅くなる」。GPU が効くもの: **WebGL（Three.js・Skia・P5.js・Mapbox）**、動画のデコード、`box-shadow`・`text-shadow`・グラデーション、`filter: blur()`・`drop-shadow()`、`transform`、多くの Canvas 2D の操作。
- Remotion「--gl flag」: 選べる描画の裏側は `null`（Chrome に任せる、Remotion 4 の既定）、`angle`（Remotion 5 の既定）、`egl`、`swiftshader`、`vulkan`、`angle-egl`、`swangle`（Lambda・Cloud Run の既定）。推奨は「WebGL・WebGPU・Three.js を使うなら、**デスクトップでは `angle`**、GPU 付きのクラウドでは `angle-egl`、GPU の無い機械では `swangle`（遅い）」。「⚠ `angle` ではメモリリークが既知の問題。**長い描画は複数に分けよ**」。
- Remotion の `open-browser.ts` が Chromium に渡すフラグ: `swangle` → `--use-gl=angle --use-angle=swiftshader`、`angle-egl` → `--use-gl=angle --use-angle=gl-egl`、`vulkan` → `--use-angle=vulkan --use-vulkan=native ... --enable-gpu` など、それ以外 → `--use-gl=<値>`。Remotion 5 の `angle` は `--use-gl=angle --enable-unsafe-swiftshader`。共通に `--ignore-gpu-blocklist`、`--headless=new`（または old）。
- Chromium の swiftshader.md: SwiftShader は「CPU だけで動く Vulkan と OpenGL ES の実装」。「**SwiftShader への自動の WebGL の逃げ道は廃止予定で、WebGL の文脈の作成は SwiftShader に逃げずに失敗するようになる**」。理由は GPU プロセスで JIT のコードが走るセキュリティの危険と、利用者の体験。headless や GPU の無い機械での試験には **`--enable-unsafe-swiftshader`** で明示的に許可する（「信頼できない内容には使うな」）。
- Chrome の headless の docs（2024-10-21 更新）: Chrome の headless は headful と同じコードに統合された。**Chrome 132.0.6793.0 以後、古い headless は単独のバイナリ `chrome-headless-shell` だけにある**。Puppeteer は `headless: true`（新）、`headless: 'shell'`（古い方）を選べる。

### WSL の GPU（Microsoft・NVIDIA）

- WSL の GUI アプリの docs: 「GUI アプリを動かすには、まず系に合う vGPU 用のドライバ（Intel・AMD・**NVIDIA**）を入れる。これで仮想 GPU を使い、**ハードウェアで加速した OpenGL の描画**の恩恵を受けられる」。WSL に Linux 版の Google Chrome を入れる手順（`.deb` を apt で入れる）も載っている。
- NVIDIA の CUDA on WSL: 「Windows の NVIDIA ドライバだけを入れる。**WSL の中に Linux 用の NVIDIA ドライバを入れてはいけない**」（WSL の中では `libcuda.so` として見える）。未対応の機能に「**OpenGL と CUDA の相互運用は未対応。OpenGL に頼るアプリは動かない**」。
- WSL の中の Chrome で WebGL が GPU（vGPU 経由）で動くか、SwiftShader に落ちるかを書いた一次資料は見つからなかった。

## この wiki への含意

- **西尾の方式はほぼそのまま使える**: [[exp-html-capture-pipeline]] は `page.evaluate` の中で `renderFrame(f)` を呼んで、同じ評価の中で `canvas.toDataURL` している。three.js の manual の「撮る直前に描く」と同じ形なので、`preserveDrawingBuffer` 無しでも撮れる可能性が高い（推測。仕様は「描画の関数が戻った後」を未定義としている）。迷ったら `preserveDrawingBuffer: true` を付ける（性能の代価は測っていない）。
- **違うのは GPU**: 西尾の 2D canvas は CPU でも回ったが、three.js の場面は headless で GPU が切れていると極端に遅いか、WebGL 自体が作れない（SwiftShader の自動の逃げ道の廃止）。撮影の最初に「どの GPU で描いているか」をログに出すのが要る。
- **galleria では Windows 側で撮るのが近道**: [[exp-polis-magi-op]] で `capture.mjs` を Windows の Chrome に合わせた前例がある（commit 6b587ad）。[[exp-puppetloom]] も Windows・Node.js 24・WebGL2 で動く設計だった。WSL の中の Chrome は vGPU 経由の OpenGL になるはずだが、確かめた記録が無い。
- **増える表現**: 3D の場面（カメラの移動、光と影、多数の粒子を GPU で）。粒子 2400 個で 1 分に約 10 分かかった showreel（[[exp-html-capture-pipeline]]）の重い描画を、GPU の点群（`THREE.Points`）で書き直せば速くなる可能性がある（推測、測っていない）。
- **型ごと**: promo（立体のロゴ、空間を飛ぶカメラ）、talk・embed（立体の構造の説明: 分子・建物・ネットワークを回して見せる）。流しっぱなしの embed では回転の速さが見る時間を決める（[[embed]]）。
- 流行の作品 168 件で Three.js / WebGL の名前が出たのは 10 件、教育の解説 27 件では 0 件（[[web-opus2-awesome-claude-5-5-videos]]）。3D は promo 側で使われている。

## 着手の仕方（未検証。galleria で確かめる）

- **何が表現できるようになるか / 効く型**: 立体の場面・カメラワーク・GPU の粒子。promo・talk・embed
- **機械**: **galleria Windows**（GPU 要。VRAM の見込みは簡単な場面なら 1GB 未満〈推測〉。RTX 5080 16GB を他のローカルモデルと取り合うなら、先に `nvidia-smi` で空きを確かめる〈[[exp-local-scene-studio]] の運用〉）。WSL でも試せるが GPU の経路が未確認。入れるもの: `three@0.187.0`、`puppeteer-core`（既存）＋ Windows の Chrome、または `puppeteer`（Chrome for Testing）。費用 0、アカウント不要。MIT
- **成熟度**: r187（2026-10-30）。毎月版が出ている
- **最小の手順（Windows の PowerShell。推測を含む）**:
  ```powershell
  mkdir $HOME\video-tools-trial\three; cd $HOME\video-tools-trial\three
  npm init -y; npm i three@0.187.0 puppeteer-core
  # scene.html（推測）:
  #   import * as THREE from './node_modules/three/build/three.module.js';
  #   const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, preserveDrawingBuffer: true, powerPreference: 'high-performance' });
  #   const FPS = 30, DUR = 4; window.TOTAL_FRAMES = FPS * DUR;
  #   window.renderFrame = f => { const t = f / FPS; cube.rotation.set(t, t * 0.7, 0); renderer.render(scene, camera); };
  #   const gl = renderer.getContext(); const ext = gl.getExtension('WEBGL_debug_renderer_info');
  #   window.GPU_NAME = ext ? gl.getParameter(ext.UNMASKED_RENDERER_WEBGL) : gl.getParameter(gl.RENDERER);
  # capture.mjs: puppeteer.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe',
  #   headless: true, args: ['--use-gl=angle', '--use-angle=d3d11', '--ignore-gpu-blocklist', '--force-device-scale-factor=1'] })
  #   ※ --use-angle=d3d11 は推測（Remotion の docs は Windows の値を書いていない。外して既定でも試す）
  #   最初に console.log(await page.evaluate('window.GPU_NAME'))
  node capture.mjs stills 0 1 2
  node capture.mjs video
  ```
  対照として、同じものを WSL で `args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader']` で撮り、CPU の速さを測る
- **動いたと言える確かめ方**: (1) ログの `GPU_NAME` に **"NVIDIA" / "RTX 5080" を含む**（"SwiftShader" や "llvmpipe" なら CPU に落ちている）、(2) PNG が真っ黒でない（`ffprobe` でなく、PNG を開くか平均輝度を python で出す）、(3) 120 コマの mp4 ができ、`ffprobe` で 4.0 秒、(4) 毎秒何コマ撮れたか（GPU と SwiftShader で比べる）
- **所要の見込み（推測）**: GPU が一発で効けば半日。効かなければフラグの組み合わせで 1 日

## Open Questions

- WSL の中の Linux 版 Chrome で、WebGL が vGPU（NVIDIA）で動くか。WSL の docs は「ハードウェアで加速した OpenGL」と書くが、Chrome の GPU プロセスがそれを使うかは書いていない
- Windows の headless Chrome で `--use-angle=d3d11` を付けるべきか、既定のままで GPU が使われるか。Remotion の docs は「デスクトップでは angle」とだけ書く
- `preserveDrawingBuffer: true` の性能の代価、`toDataURL` と `readPixels` のどちらが速いかは測っていない。WebCodecs で canvas から直接エンコードする経路（[[web-timesnap-timecut-hyperframes-webcodecs]]）との比較も無い
- Remotion の「angle でメモリリーク、長い描画は分けよ」は Remotion の撮り方での話。西尾の 1 タブで全コマを撮る方式で同じことが起きるかは分からない
- 物理・群れのシミュレーションを「読み込み時に一度回して状態を表に持つ」と、メモリは尺に比例する。どこまでの尺・粒子数で持つかの目安は文献に無い
