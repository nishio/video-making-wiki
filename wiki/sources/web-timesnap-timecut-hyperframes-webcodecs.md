---
type: source
summary: Web ページを動画にする道具の README・公式ドキュメント。timesnap/timecut はページの時間関数（Date・performance.now・requestAnimationFrame・setTimeout）を仮想時間に差し替えて 1 コマずつ撮る。HyperFrames（HeyGen、Apache-2.0）は HTML＋シーク可能なアニメを 1 コマずつシークして撮る決定論的な描画をエージェント向けに出している。puppeteer の screencast/record は実時間の録画。WebCodecs（VideoEncoder、Mediabunny）は canvas をブラウザ内で直接エンコードできるが、mux は別ライブラリが要る
video_types: [any]
url: https://github.com/tungs/timesnap
author: Steve Tung（timesnap/timecut）、HeyGen（HyperFrames）、Puppeteer チーム、MDN、Vanilagy（Mediabunny）
published: timesnap 最終 push 2024-01-17／timecut 2023-07-18／HyperFrames v0.9.23 2026-11-08（repo 作成 2026-03-10）
retrieved: 2026-11-09
sources:
  - https://github.com/tungs/timesnap/blob/master/README.md
  - https://github.com/tungs/timecut/blob/master/README.md
  - https://github.com/heygen-com/hyperframes/blob/main/README.md
  - https://github.com/heygen-com/hyperframes/blob/main/docs/concepts/determinism.mdx
  - https://github.com/heygen-com/hyperframes/blob/main/docs/concepts/frame-adapters.mdx
  - https://github.com/heygen-com/hyperframes/blob/main/docs/guides/rendering.mdx
  - https://github.com/puppeteer/puppeteer/blob/main/docs/api/puppeteer.page.screencast.md
  - https://github.com/puppeteer/puppeteer/blob/main/docs/api/puppeteer.page.record.md
  - https://github.com/mdn/content/blob/main/files/en-us/web/api/videoencoder/index.md
  - https://github.com/mdn/content/blob/main/files/en-us/web/api/webcodecs_api/index.md
  - https://github.com/Vanilagy/mediabunny/blob/main/docs/guide/media-sources.md
  - https://www.remotion.dev/docs/client-side-rendering/how-it-works.md
---

# HTML を撮って動画にする: timesnap / timecut・HyperFrames・puppeteer の録画・WebCodecs

## 何の文献か

いずれも作り手の README・公式ドキュメント（一次資料）。速度の比較の数字はどれにも無い（または条件が書かれていない）。HyperFrames は HeyGen（AI 動画の会社）の OSS で、Pro プランの宣伝を含む。GitHub のスターは timesnap 約 240、timecut 約 650、HyperFrames 約 8.1 万（2026-11-09 の API 値。repo 作成は 2026-03-10）。

## 書いてあること

### timesnap / timecut（仮想時間で撮る）

- timesnap は「JavaScript のアニメを使う Web ページのスクリーンショットを撮る Node.js のプログラム。timeweb と puppeteer でページを開き、時間を扱う関数を上書きして、仮想の時刻でスナップショットを撮る。ページによっては実時間より遅く撮っても、動画にしたとき滑らかで一定に見える」と書く。timecut は同じ仕組みで撮ったコマを ffmpeg に渡して動画にする。
- 仕組み（timesnap README「How it works」）: puppeteer の `page.evaluateOnNewDocument` で、ページの `new Date()`、`Date.now`、`performance.now`、`requestAnimationFrame`、`setTimeout`、`setInterval`、`cancelAnimationFrame` などを仮想タイムラインを使うものに差し替え、「JavaScript の計算が終わってからスクリーンショットを撮る」。Noah Veltman の d3 の発表（`Date.now` と `performance.now` を仮想時刻にし、puppeteer で時刻を進めて撮る）に着想を得たと書く。
- 制限: 「JavaScript の関数と動画の再生しか上書きしないので、CSS の transition や animation で変化するページは意図どおりに描けないだろう」（両 README の Limitations）。
- 撮り方は 2 つ: スクリーンショットモード（既定。div・svg・canvas をページに描かれたとおり撮れる。切り抜き可。遅い）と、canvas capture モード（実験的。canvas のデータを直接コピー。「スクリーンショットより速いことが多い」）。
- 例: `--fps=60 --duration=10 --output-stdout | ffmpeg -framerate 60 -i pipe:0 ... video.mp4`（ディスクに保存せず ffmpeg にパイプ）。timecut は既定で一度ディスクに保存し、パイプモードは実験的。
- ライセンス BSD-3-Clause。最終更新は 2023〜2024 年。

### HyperFrames（HTML ＋ シーク可能なアニメ、エージェント向け）

- 「HTML・CSS・メディア・シーク可能なアニメを決定論的な MP4 にする、無料の OSS フレームワーク」「Write HTML. Render video. Built for agents.」と書く（README）。Apache-2.0、Node 22+ と FFmpeg が要る。
- 書き方: `data-start`・`data-duration`・`data-track-index` などの data 属性で要素の時刻とトラックを書き、アニメは GSAP の `timeline({paused: true})` などを `window.__timelines` に登録する。GSAP・CSS・Lottie・Three.js・Anime.js・WAAPI のアニメを「フレームアダプター」でシークする（frame-adapters.mdx）。
- 決定論の仕組み（determinism.mdx）: 「描くときは動画を再生しない。1 コマずつ問い合わせ、"フレーム 90 はどう見えるか" の答えが変わる要因は 90 という数だけ」。各コマで時刻を `floor(frame) / fps` の整数計算で出し、すべてのアニメをその時刻にシークし（GSAP は一時停止してシーク、再生はしない）、Chrome の `HeadlessExperimental.beginFrame` で「一度の原子的な操作で」画素を取り、FFmpeg でエンコードして `<audio>`・`<video>` の音を混ぜる。
- 書き手への決まり: 壁時計を使わない（`Date.now()`・`requestAnimationFrame`・タイマー禁止）、seed の無い乱数を使わない、描画中に fetch しない、fps・幅・高さを最初のコマの前に固定、長さは有限。
- 機械の差: 「フォントと Chrome の版は機械ごとに違うので、ローカルの描画は機械によって 1 画素ずれうる。厳密な再現が要るなら Docker で描く（Chromium の版・フォント・FFmpeg を固定）」。
- プレビューと描画: 「プレビューは実時間で再生するので機械の性能に縛られるが、描画はシークで 1 コマずつなので、どれだけ重いコマでも落とさない。プレビューで引っかかる構成も完全に描ける」。
- エージェント向け: Claude Code のプラグイン、`npx skills add heygen-com/hyperframes`。skills は「計画 → 正しい HTML を書く → シーク可能なアニメをつなぐ → メディアを足す → lint → プレビュー → 描画」の流れを教える、と書く。CLI は「既定で非対話」。CLI の skill に「コマを見る（look at frames）」がある。`/remotion-to-hyperframes` は Remotion・Motion Canvas・Lottie などの既存コードを「1 コマずつ照合しながら」移す skill。
- Remotion との比較表（README、HyperFrames 側の主張）: 書き方は HTML か React か、ビルド工程の有無、ライブラリの時計を使うアニメは「アダプターでシーク可能」か「壁時計のパターンは注意が要る」か、ライセンスは Apache 2.0 か Remotion License か。「Remotion に着想を得た。どちらも headless Chrome と FFmpeg で描く」。
- 描画は Docker と AWS Lambda の経路もある。Lambda は「1 台に収まらない長尺・4K・大量のバッチ向けで、開発中の繰り返しにはローカルのほうが速い」（rendering.mdx）。

### puppeteer の screencast / record（実時間の録画）

- `Page.screencast()` は「このページのスクリーンキャストを撮る」。既定は WebM（VP9）・30fps、ffmpeg が要る。2026-11 時点の docs では「obsolete、`Page.record()` を使う」と表示され、`Page.record()` は Chrome DevTools Protocol の `Page.startScreenRecording` で MP4 を出す。
- 使い方は「録画開始 → 何かする → 停止」で、ページの時間を止めたり進めたりする説明は API の docs に無い。動いているページをそのまま録る道具と読める（`speed` で出力の速さを変えるオプションはある）。

### WebCodecs（canvas をブラウザ内で直接エンコード）

- MDN: `VideoEncoder` は `VideoFrame` を `EncodedVideoChunk` に符号化する。secure context が要り、window と dedicated worker で使える。
- MDN WebCodecs API: 「WebCodecs は符号化と復号だけを扱う。符号化したチャンクを再生できる動画ファイルに書く仕組みは無い」。ファイルにするには mux のライブラリが要り、「Mediabunny が主な選択肢」と書く。
- Mediabunny（MPL-2.0）の `CanvasSource`: 「1 枚の canvas を描画ループで繰り返し更新し、各コマを出力ファイルに足す、というよくある形を簡単にする」。`await canvasSource.add(0.0, 0.1)` のように、各コマの時刻と長さ（秒）を呼ぶ側が渡す。リアルタイムの録画には別の `MediaStreamVideoTrackSource` がある。
- [[web-remotion]] のブラウザ内レンダリングはこの経路（WebCodecs ＋ Mediabunny）で、DOM を canvas に描き直すので対応する CSS が限られる。`@remotion/webcodecs` は Mediabunny へ移行するため段階的に廃止中。

## この wiki への含意

西尾の方式（[[exp-html-capture-pipeline]]、[[exp-polis-magi-op]]）: canvas に `renderFrame(f)` を時刻の純関数で描き、puppeteer-core の headless Chrome で 1 コマずつ `canvas.toDataURL('image/png')` を取り、ffmpeg の image2pipe へ流す。BGM は numpy で合成して最後に重ねる。

| 方式 | 時間の扱い | 1 コマの取り出し | 既存のアニメを撮れるか | 西尾の方式との差 |
|---|---|---|---|---|
| 西尾の方式 | 描く側が純関数（自前の時刻表） | `toDataURL` の PNG → image2pipe | 撮れない（`renderFrame` を書く必要） | ― |
| timesnap/timecut | ページの時間関数を仮想時間に差し替え | スクリーンショット or canvas capture | JS の時間で動くものなら撮れる。CSS アニメは不可 | 純関数で書いていれば仮想時間は要らない。既存の rAF ベースのデモを撮るときに効く |
| HyperFrames | 整数のフレーム→時刻、全アニメをシーク | `HeadlessExperimental.beginFrame` | GSAP・CSS・Lottie・WAAPI などをアダプターでシーク | CSS アニメ・GSAP も決定論的に撮れる。Docker でフォントを固定できる |
| puppeteer screencast/record | 実時間 | 録画（CDP） | 撮れるが重いコマで落ちうる | 決定論的でない。画面操作のデモの録画向き |
| WebCodecs＋Mediabunny | 呼ぶ側が各コマの時刻を渡す | canvas → VideoFrame → エンコード | 自前の描画ループ | PNG の符号化と標準入力の転送を省ける。ブラウザ内で完結 |

（表は上の各文献の記述からこのページでまとめたもの。速さの比較は実測していない）

- **西尾の Open Question「WebCodecs など速い経路は試していない」への答えの候補**: 西尾の方式は 1 コマごとに PNG を作り（圧縮）、base64 の文字列で Node へ渡し、ffmpeg が PNG を復号して再び H.264 に符号化している。WebCodecs ＋ Mediabunny の `CanvasSource` なら、canvas から直接エンコードしてファイルにできる。ただし粒子系の 1 分に約 10 分（実測）のうち、どれだけが描画でどれだけが PNG の受け渡しかは測っていない。描画が支配的なら経路を変えても速くならない。
- **「1 画素ずれ」問題**: HyperFrames が書く「フォントと Chrome の版の差で機械ごとにずれる」は、[[exp-html-capture-pipeline]] の Open Question（Mac の Hiragino 依存、galleria・CyEC2 で同じ絵が出るか未確認）と同じ問題。HyperFrames の答えは Docker で固定。[[exp-polis-magi-op]] の Mac→galleria の移し替えで Chrome のパスや node_modules が差分になった件も、同じ方向の解決ができる。
- **エージェント向け**: HyperFrames は CLI が非対話・lint・コマを見る、を最初から持つ。西尾の方式で Claude Code がやっていた「`capture.mjs stills` で秒を指定して静止画を撮る」「コンタクトシート」（[[exp-html-capture-pipeline]]）を道具側が持っている形。

## Open Questions

- 西尾の方式の 1 分に約 10 分のうち、PNG の符号化・転送の割合はどれだけか（描画が支配的か）。WebCodecs に変えて速くなるかは測らないと分からない。
- HyperFrames は 2026-03 作成で、版が 0.9 台、更新が非常に速い（1 日に複数リリース）。スター数約 8 万の急増が実利用を反映しているかは分からない。決定論の主張（同じ入力から同じ出力）は README・docs の記述で、検証はしていない。
- timesnap/timecut は 2023〜2024 年から更新が無い。最近の Chrome・puppeteer で動くかは未確認。
- puppeteer の `Page.record()` が headless でどの fps・品質で撮れるか、重いページでコマを落とすかは docs に書かれていない。
