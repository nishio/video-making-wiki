---
type: source
summary: 既存の [[web-after-effects-lottie-rive]] への差分。2026-11-09 時点の版とライセンス（lottie-web 5.13.0 は 2025-05 から止まり、LottieFiles の dotlottie-web 0.82.1 が更新中。Rive ランタイム 2.49.4 は MIT、エディタの無料プランは .riv にスプラッシュ画面が付く）と、ブラウザで 1 コマずつ止めて撮る API の差（lottie-web の goToAndStop、dotlottie-web の setFrame、Rive の scrub は線形アニメだけで状態機械は advance しかない）
video_types: [promo, talk, embed]
url: https://github.com/LottieFiles/dotlottie-web/blob/main/packages/web/README.md
author: airbnb（lottie-web）、LottieFiles（dotlottie-web）、Rive（rive-wasm・料金表）、Remotion AG（@remotion/lottie・@remotion/rive）
published: unknown（各 README・ソースは継続更新。版は本文）
retrieved: 2026-11-09
sources:
  - https://registry.npmjs.org/lottie-web
  - https://registry.npmjs.org/@lottiefiles/dotlottie-web
  - https://registry.npmjs.org/@rive-app/canvas
  - https://github.com/LottieFiles/dotlottie-web/blob/main/packages/web/README.md
  - https://github.com/LottieFiles/dotlottie-web/blob/main/packages/web/src/dotlottie.ts
  - https://github.com/remotion-dev/remotion/blob/main/packages/lottie/src/Lottie.tsx
  - https://github.com/rive-app/rive-wasm/blob/master/js/src/rive.ts
  - https://github.com/remotion-dev/remotion/blob/main/packages/docs/docs/rive/remotionrivecanvas.mdx
  - https://rive.app/pricing
---

# Lottie・Rive を止めて撮る（既存ページへの差分）

AE のエクスプレッション、Lottie の対応機能、Rive の概要、手作業系とコード系の分担は [[web-after-effects-lottie-rive]] にある。ここは版・ライセンス・「ブラウザで時刻を指定して 1 コマ撮る」手順の差分だけ。

## 何の文献か

- npm レジストリの版・日付・license 欄（2026-11-09 取得）、GitHub API の最終 push。
- dotlottie-web の README とソース（`dotlottie.ts` の JSDoc）、rive-wasm の `rive.ts`（JSDoc）。作り手のコードの注釈で、動作は確かめていない。
- Remotion の `@remotion/lottie` のソース（`Lottie.tsx`）と `@remotion/rive` の docs。他人の道具が実際にどう seek しているかの実例として読んだ。
- Rive の料金表のページ（rive.app/pricing）。HTML から機能の行は読めたが、**どのプランに丸が付くかは HTML のテキストから読み取れなかった**（アイコンで描かれている）。

## 書いてあること

### 版とライセンス（2026-11-09 時点の npm）

| パッケージ | 最新版（日付） | license | 動き |
|---|---|---|---|
| `lottie-web`（airbnb） | 5.13.0（2025-05-21） | MIT | GitHub の最終 push 2025-09-01。star 32,380、open issue 862 |
| `@lottiefiles/dotlottie-web`（LottieFiles） | 0.82.1（2026-11-02） | MIT | 0.x のまま頻繁に更新 |
| `@rive-app/canvas`・`@rive-app/webgl2`（Rive） | 2.49.4（2026-11-05） | MIT | 頻繁に更新 |
| `@remotion/lottie`・`@remotion/rive` | 4.0.541（2026-11-05） | Remotion License（「SEE LICENSE IN LICENSE.md」） | — |

### Lottie を止める

- **lottie-web**: `loadAnimation({autoplay: false, renderer: 'svg' | 'canvas', ...})` で読み、`goToAndStop(frame, true)`（第 2 引数 `true` でフレーム番号として解釈）。Remotion の `Lottie.tsx` は読み込み完了時に「**Lottie の初期化のバグを避けるため 2 回 seek する**」（`goToAndStop(frame - 1)` の直後に `goToAndStop(frame)`）とコメント付きで書いている。既定の描画は `svg`。
- **dotlottie-web**（`.lottie` ＝ ZIP にまとめた Lottie と素材、および `.json`）: `setFrame(frame)` は「指定のフレームへ seek して描く。自前のスクラブや正確なフレーム位置に有用」。`setUseFrameInterpolation(false)` で「補間せず、フレームごとの正確な絵」。`totalFrames` を持つ。Node.js 18 以上でも動く isomorphic なライブラリと書く。
- **dotlottie-web の落とし穴**: 「プレイヤーの WASM エンジン（圧縮で約 500KB）は最初のプレイヤーを作るときに **CDN から取得する**」。CDN の URL は版に固定されている。オフラインや決定論が要るなら `setWasmUrl()` で自前の場所を指す（README）。

### Rive を止める

- rive-wasm の高水準 API の `scrub(animationNames, value)` は「名前付きのアニメの時刻を設定する。value は再生位置を跳ばす先の浮動小数」。対象は **線形のアニメ（timeline）**。
- **状態機械（state machine）は `advance(time)`（「与えた時間だけ進める」）しかなく、任意の時刻へ跳ぶ API は見当たらない**。状態機械を決定論的に撮るなら、`reset()` してから固定の刻みで最初から進める必要がある（推測。rive.ts のメソッド一覧から）。
- さらに、`animations` 引数（名前付きアニメの再生）と複数の状態機械の同時再生には **@deprecated**:「状態機械を再生するには `stateMachine` を使え。名前付きアニメでの再生開始は**将来のメジャー版で削除**される」。scrub しやすい側（線形アニメ）が縮小方向にある。
- Remotion の `<RemotionRiveCanvas>` は `animation`（名前か番号）を受け取り、Remotion の時刻に同期させる。状態機械を指定する prop は docs に無い。

### Rive のエディタの料金（2026-11-09 の料金表）

- Free（$0）: Rive Editor、「**.riv をスプラッシュ画面付きで書き出し**」、共同編集ファイル 3、CLI は月 50 回の publish/push。「無料の書き出しは Rive のスプラッシュ画面を再生する。外すにはアップグレード」。**Rive CLI はアカウント無しで入れられる**（build・preview・スクリーンショットは「無制限・アカウント不要」）。
- Cadet（$9/seat/月、最大 3 seat）: スプラッシュ無しの書き出し。Voyager（$32/seat/月）、Enterprise（$120/seat/月、年商 1,000 万ドル以上向け）。
- 機能表に「書き出し: RIV・REV・**MP4・GIF・PNG 連番・WebM**」の行がある。プランごとの可否は読み取れなかった。

## この wiki への含意

- **西尾の canvas 方式に入れるなら dotlottie-web か Rive の canvas 版**: どちらも canvas に描くので、[[exp-html-capture-pipeline]] の `canvas.toDataURL` の撮り方がそのまま使える（推測。dotlottie-web は自前の canvas、lottie-web は `renderer: 'canvas'` を選べば canvas）。lottie-web の既定の `svg` は DOM なので、撮るには `page.screenshot` が要る（[[web-means-3d-gsap-svg-seek]]）。
- **素材の入手経路が増える**: Lottie は LottieFiles の素材集、Rive は Rive Editor・CLI。どちらも AE を持たない西尾にとって「手で詰めた動きの部品」を持ち込む入口（[[web-after-effects-lottie-rive]] の「手作業系とコード系の分け方」）。素材集の利用条件は読んでいない（means-sound-font・rights の担当の範囲）。
- **embed（流しっぱなし）との相性**: Rive の強みの状態機械（クリックやホバーで分岐）は、流しっぱなしの動画には使い道が薄く、しかも止めて撮りにくい。動画に使うなら線形アニメだけで作る。
- 費用: Rive の無料プランで書き出した .riv はスプラッシュ画面が出る、と料金表が書く。動画の頭にスプラッシュが入るかは試していない。

## 着手の仕方（未検証。galleria で確かめる）

- **何が表現できるようになるか / 効く型**: 既成の Lottie 素材（アイコンの動き、イラストの動き）や Rive の線形アニメを、自前の canvas 動画の部品として時刻どおりに置く。promo（ロゴ・アイコンの作り込み）、talk・embed（図の中の小さな動き）
- **機械**: galleria WSL（GPU 不要。dotlottie-web は Canvas 2D と WASM）。Mac でも同じ。入れるもの: `@lottiefiles/dotlottie-web@0.82.1` か `lottie-web@5.13.0`、Rive なら `@rive-app/canvas@2.49.4`。費用 0（Rive のスプラッシュ無しは Cadet $9/seat/月）。アカウント: Lottie の素材を LottieFiles から取るなら要（推測）、Rive Editor は要、Rive CLI は不要
- **成熟度**: dotlottie-web と Rive ランタイムは 2026-11 にも更新。lottie-web は 2025-05 から版が出ていない
- **最小の手順（WSL）**:
  ```sh
  mkdir -p ~/video-tools-trial/lottie && cd ~/video-tools-trial/lottie
  npm init -y && npm i @lottiefiles/dotlottie-web@0.82.1 puppeteer
  cp node_modules/@lottiefiles/dotlottie-web/dist/dotlottie-player.wasm .   # 推測: dist の中の名前は README の CDN URL から
  # index.html（推測）:
  #   const dl = new DotLottie({ canvas, src: 'anim.lottie', autoplay: false, loop: false });
  #   DotLottie.setWasmUrl('./dotlottie-player.wasm')  // README: 構築より前に呼ぶ
  #   dl.setUseFrameInterpolation(false);
  #   window.ready = new Promise(r => dl.addEventListener('load', r));   // 推測: イベント名は docs で確かめる
  #   window.renderFrame = f => dl.setFrame(f * dl.totalFrames / window.TOTAL_FRAMES);
  # 既存の capture.mjs（canvas.toDataURL 版）で撮る
  ```
  `anim.lottie` は手元で作るか、利用条件を確かめた素材を西尾が選ぶ（素材のダウンロードは CyEC2 ではしない）
- **動いたと言える確かめ方**: (1) 撮影中にネットワークを切っても（または DevTools の request ログに jsdelivr が出ない）最後まで撮れる、(2) `stills` で同じ f を 2 回撮って `cmp` が一致、(3) 最初のコマが空白でない（Remotion が書く初期化のバグの有無の確認。f=0 と f=1 を撮って見比べる）
- **所要の見込み（推測）**: 素材があれば半日

## Open Questions

- Rive の MP4・WebM の書き出しがどのプランで使えるか、書き出した動画にスプラッシュが入るかは料金表の HTML から読めなかった。エディタの利用規約も未読
- dotlottie-web の `setFrame` のフレーム番号は 0 始まりか、端数を渡したときに補間するか（`setUseFrameInterpolation(false)` の時）。ソースの注釈だけでは分からない
- 状態機械を `advance` で先頭から進める撮り方は、長い動画で毎コマ O(f) になる。Remotion の GSAP と同じ代価（[[web-means-3d-gsap-svg-seek]]）
- LottieFiles・Rive の素材集の利用条件（商用・改変・クレジット）は読んでいない
