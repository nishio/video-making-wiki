---
type: concept
summary: プログラムで動画を作る道具（Remotion、Motion Canvas、Revideo、Manim、timesnap/timecut、HyperFrames、WebCodecs）と After Effects 系を、西尾の経験の 2 方式（HTML を描いて撮る、Pillow の静止スライド）と同じ観点で並べ、LLM のエージェントに作らせるときの失敗の型と対策を文献と経験で突き合わせたページ
video_types: [any]
sources:
  - web-remotion.md
  - web-motion-canvas.md
  - web-motion-canvas-presentation-mode.md
  - web-revideo.md
  - web-manim.md
  - web-timesnap-timecut-hyperframes-webcodecs.md
  - web-after-effects-lottie-rive.md
  - web-theoremexplainagent-code2video-visualedu.md
  - exp-html-capture-pipeline.md
  - exp-qualia-video.md
  - exp-polis-magi-op.md
---

# 動画を作る道具の比較

道具ごとの詳細な比較表は [[web-theoremexplainagent-code2video-visualedu]] の末尾と [[web-timesnap-timecut-hyperframes-webcodecs]] にある。ここは判断に効く点だけを経験と並べる。

## 経験の方式（[[exp-html-capture-pipeline]]、[[exp-qualia-video]]）

- HTML 方式: canvas に `renderFrame(f)` をフレーム番号の純関数で描き、puppeteer-core の headless Chrome 1 タブで `toDataURL` → ffmpeg の image2pipe。BGM は numpy で合成して後から重ねる。粒子系で 1 分に約 10 分、文字だけで 47 秒 60fps を約 38 秒（実測）
- Pillow 方式: 音声区間ごとの静止スライドを Pillow で作り、PyAV で結合

## 道具と経験の差（文献の記述から）

| 道具 | 経験との一番大きな差 | 出典 |
|---|---|---|
| Remotion | 同じく「フレーム番号の純関数・seed 固定の乱数」を要求する。理由は複数タブでの並列レンダリングで、`--concurrency=1` で合うのは「たまたま」と自ら書く。西尾の方式は純関数であることを並列化に使っていない。**4 人以上の営利組織では Company License が要る**（人数は会社全体で数える）。会社の発信物として作るなら該当しうる | [[web-remotion]] |
| Motion Canvas | generator で上から時間を書き、ナレーションの合図を `waitUntil` の時刻イベントとしてエディタ上でドラッグして合わせる。西尾は 120BPM の格子と TTS の区間長から時刻を自動で決め、合わせる作業そのものを無くしている。書き出しはエディタのボタン、音声は 1 本。正式リリースは 2024-12 の v3.17.2 から止まっている。MIT。presentation mode は embed に効く | [[web-motion-canvas]]、[[web-motion-canvas-presentation-mode]] |
| Revideo | Motion Canvas の fork。書き出しが UI からだけ・音声の制約・Remotion のライセンスを避けたい、が fork の理由（作者のブログ、2024-04）。今は開発の主体が別会社に移った | [[web-revideo]] |
| Manim | `play()` ごとの部分動画とキャッシュ。数式は LaTeX、文字は Pango（日本語可）。作者の Sanderson は「manim は個々のクリップを作る道具。ナレーションとの同期は普通の動画編集ソフトで」と書く | [[web-manim]] |
| timesnap / timecut | ページの時間関数を仮想時間に差し替えて撮る。既存の rAF ベースのアニメを撮るときに効く。CSS アニメは撮れない。自前の純関数なら不要 | [[web-timesnap-timecut-hyperframes-webcodecs]] |
| HyperFrames | HeyGen の OSS（Apache-2.0、2026-03 作成）。整数フレームで全アニメ（CSS・GSAP・Lottie など）をシークして撮る。Docker でフォントと Chrome の版を固定する。CLI が非対話・lint・コマを見る、をエージェント向けに持つ | 同 |
| WebCodecs＋Mediabunny | canvas から直接エンコードし、PNG の符号化と標準入力の転送を省ける | 同 |
| After Effects / Lottie / Rive | 手でキーフレームを打つ系。Lottie は音声・動画・画像連番に非対応 | [[web-after-effects-lottie-rive]] |

## LLM のエージェントに作らせるとき

- 文献の失敗の型は 3 つ: 存在しない API・引数の誤り（最多）、LaTeX のエラー、重なり・位置ずれ・はみ出し（TheoremExplainAgent 2025）。エラーを読んで再試行するだけで成功率は N=0 の数 % から N=5 で約 9 割（[[web-theoremexplainagent-code2video-visualedu]]）
- 対策として、Code2Video は 6×6 の格子のアンカーに配置させ、VisualEDU・Code2Video は描いた動画を VLM に見せる。それでも「人間は短い遮蔽に敏感で VideoLLM は見逃す」。配置の点は VLM 採点で 90.6、人間採点で 60.2（同）
- 経験との対応: 西尾の方式は API が小さい自前の canvas 描画で、存在しない API の失敗の記録が無い。配置は [[exp-qualia-video]] が字幕と内容の帯を座標で分けた。確認は `capture.mjs stills` とコンタクトシートで西尾が見た（[[exp-html-capture-pipeline]]）。「機械 QA が全部通っても視聴品質は保証されない」（[[exp-qualia-video]]）は文献の VLM と人間の差と同じ向き

## 経験と文献の食い違い

- Sanderson は「同期・編集は動画編集ソフトで」と書く。西尾は全部コード（時刻表・TTS 区間・ffmpeg）で合わせている。エージェントに全工程を回させる前提の違いとして両方残す
- Code2Video は人の評価で「3B1B を上回る」と書くが、尺は 2.0 分と 16.9 分、各群 8 人、主指標 TeachQuiz の学習者は VLM（[[web-theoremexplainagent-code2video-visualedu]]）

## Open Questions

- 粒子系の 1 分に約 10 分のうち、描画と PNG の受け渡しのどちらが支配的か測っていない。描画が支配的なら WebCodecs に変えても速くならない
- Mac の Hiragino 依存（[[exp-html-capture-pipeline]]）は、HyperFrames の「Docker でフォントを固定」で解決できるか。CyEC2（Linux）で同じ絵が出るか試していない
- Remotion のライセンスが西尾の発信物（個人か会社か）にどう当たるかは、条文と所属で決まる。判断していない
- embed を Motion Canvas の presentation mode で作る（スライドとして送る）方式と、mp4 をスライドに貼る方式を比べていない（[[embed]]）

## Updates

### 2026-11-09 第 2 回サーベイから

- 道具の側の Opus 5.5 以後の変化: HyperFrames は skill を 21 から 7 に減らし、Remotion は「プレビューを先に開く」「静止画で確かめる」「人が後で直せるタイムライン」を skill に足した。新しい OSS の OpenFilm は `frame(t)` 一つで描き、2 通りの順で描いて一致を確かめる。Manim CE・Motion Canvas には LLM 向けの動きが無い（[[web-opus2-hyperframes-after-2026-09-22]]、[[web-opus2-remotion-openfilm-manim-after-2026-09-22]]）
- 流行の作品で名前が出た道具は、素の JS/Canvas 55、Remotion 10、HyperFrames 8、Manim 2（[[web-opus2-awesome-claude-5-5-videos]] から担当が数えた）。西尾の方式は多数派の側
- 実物を台本で動かして撮る道具（Charm の VHS、shot-scraper）は、作品の promo に効く別の系統（[[web-promo2-vhs-shot-scraper-demos-as-code]]、[[work-promotion-video]]）
- 丸ごと生成のモデルとの組み合わせ方は [[work-promotion-video]]

### 2026-11-09 第 3 回サーベイから

- 道具の範囲を、収録・図・2D/3D・声・音・文字・批評役に広げた一覧は [[expression-means]]。検査と仕上げの道具は [[checks-and-finishing]]
- 西尾の方式（canvas の `toDataURL`）に載るかの要点: SVG・DOM の道具（Mermaid、D2、Excalidraw、GSAP、lottie-web の svg 描画）は `page.screenshot` が要る。時刻の止め方は、SMIL なら `setCurrentTime`、CSS なら `getAnimations`、GSAP なら paused timeline の seek（[[web-means-diagram-mermaid]]、[[web-means-3d-gsap-svg-seek]]）
- WebGL は headless で GPU が切られやすい。`--use-gl=angle` で起動し、`UNMASKED_RENDERER_WEBGL` で確かめる（[[web-means-3d-threejs-headless-webgl]]）
- Open Questions の「Mac の Hiragino 依存」への答えの候補: フォントのファイルを作品に同梱して `@font-face` で指す。Ubuntu の `fonts-noto-cjk` に Black は無い（[[web-means-font-fontconfig-noto-cjk-linux]]）
