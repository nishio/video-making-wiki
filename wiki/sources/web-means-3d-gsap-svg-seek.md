---
type: source
summary: GSAP（GreenSock）の 2024-10 の Webflow による買収と 2025-04-30 の全面無償化、現行の「Standard No Charge License」の条文、paused timeline を seek / progress で外から 1 コマずつ動かす方法と、Remotion・HyperFrames が GSAP を撮るときに課している決まり。SVG の SMIL と CSS/WAAPI を時刻指定で止める標準 API も並べた
video_types: [promo, talk, embed]
url: https://gsap.com/standard-license/
author: Webflow（GSAP Standard License・公式ブログ）、GreenSock/Webflow（GSAP docs）、Remotion AG（@remotion/gsap docs）、HeyGen（HyperFrames docs）、MDN
published: 2025-04-30（ライセンスの発効日。最終更新 2025-05-30）
retrieved: 2026-11-09
sources:
  - https://gsap.com/standard-license/
  - https://gsap.com/pricing/
  - https://webflow.com/blog/webflow-acquires-gsap
  - https://webflow.com/updates/gsap-becomes-free
  - https://registry.npmjs.org/gsap （版と日付）
  - https://github.com/greensock/GSAP/blob/master/README.md
  - https://gsap.com/docs/v3/GSAP/Timeline/seek()
  - https://gsap.com/docs/v3/GSAP/Timeline/progress()
  - https://gsap.com/docs/v3/GSAP/gsap.globalTimeline
  - https://gsap.com/docs/v3/GSAP/gsap.exportRoot()
  - https://gsap.com/docs/v3/GSAP/gsap.ticker
  - https://github.com/remotion-dev/remotion/blob/main/packages/docs/docs/gsap/index.mdx
  - https://github.com/remotion-dev/remotion/blob/main/packages/docs/docs/gsap/use-gsap-timeline.mdx
  - https://github.com/heygen-com/hyperframes/blob/main/docs/guides/gsap-animation.mdx
  - https://developer.mozilla.org/en-US/docs/Web/API/SVGSVGElement/setCurrentTime
  - https://developer.mozilla.org/en-US/docs/Web/API/Document/getAnimations
  - https://developer.mozilla.org/en-US/docs/Web/API/Animation/currentTime
---

# GSAP（と SVG）を時刻指定で止めて撮る

## 何の文献か

- **ライセンスと経緯**: GSAP の公式サイトの「Standard "No Charge" GSAP License」（条文と FAQ。発効 2025-04-30、最終更新 2025-05-30、Copyright 2025 Webflow）、Webflow の公式ブログ（買収 2024-10-15、無償化の告知）。いずれも当事者の文章。
- **API**: GSAP の公式 docs（v3）の Timeline・globalTimeline・exportRoot・ticker の頁。
- **撮る側の決まり**: Remotion の `@remotion/gsap`（v4.0.517、npm の公開 2026-08-25）の docs と、HyperFrames の「Animate with GSAP」ガイド。どちらも道具の作り手の docs で、効果の測定ではない。
- **SVG・CSS の標準 API**: MDN（mdn/content の原稿）。
- 版は 2026-11-09 時点の npm による: `gsap` latest **3.15.1（2026-11-04）**、beta タグに **4.0.0-beta.3（2026-11-05）**。3.13.0 が 2025-04-30（無償化の日）。GitHub の greensock/GSAP は star 30,325・最終 push 2026-11-04（GitHub API）。GitHub の Releases は使われていない。v4 beta の中身は読んでいない。

## 書いてあること

### 買収と無償化（Webflow の文章）

- 2024-10-15 の Webflow ブログ: Webflow が「GSAP の背後の会社 GreenSock の事業を買収した」。「数か月かけて GSAP をプラットフォームに統合する」「**GSAP は広い Web で誰でも使えるよう公開され続ける**。Webflow と GSAP のチームは保守と発展を約束する」と書いている。
- 無償化の告知（Webflow updates）: 「GSAP は Webflow の顧客かどうかにかかわらず、すべての利用者に 100% 無料」「以前は有料だった Club のプラグインを含め、GSAP の全道具を無料で」「**standard license を商用利用まで広げる**」。同時に SplitText を書き直した（ファイルサイズ 50% 減、スクリーンリーダー対応、マスク）と書く。
- GitHub の README も「SplitText・MorphSVG など Club GSAP 会員だけのボーナスプラグインを含め 100% 無料、商用でも」と書く。npm の `license` 欄は「Standard 'no charge' license: https://gsap.com/standard-license」（3.15.1）、「See https://gsap.com/standard-license」（4.0.0-beta.3）。**OSI のオープンソースライセンスではない**（MIT 等ではなく独自の利用許諾）。

### Standard "No Charge" License の条文（要点を原文から）

- 許諾（II）: Webflow は「GSAP Products を **Permitted Uses に限って**使用・複製・表示・実装する、非独占・全世界のライセンス」を与える。
- **Permitted Uses**: 「任意の Web サイト、Web アプリケーション、**またはデジタルインターフェース**での GSAP Products の実装・使用（明確化のため、他の事業分野で Webflow と競合する会社のものを含む）」。
- **Prohibited Uses**: 「**コードなしで視覚的なアニメを作れるツール**での使用のうち、Webflow の視覚的アニメ作成機能と競合する解決策を作ることを奨励・誘引・実質的に助けるもの」。Competitive Products は「Webflow に似た視覚的インターフェースやビルダーでアニメを作成・編集・管理できるソフト・道具・サービス」。
- 制限（III）: 書面の同意なく Prohibited Uses に使わない、競合製品を作る目的でリバースエンジニアリングしない、**所有権表示やブランディングを除去・改変しない**。
- 所有（IV）は Webflow、終了（V）は「条件に違反したら Webflow の裁量で終了でき、全コピーを破棄」。条文は Webflow の Terms of Service に組み込まれ、抵触時は GSAP License が優先（VI-1）。
- 改定（VI-2）: Webflow はいつでも改定できる。改定に同意しないなら、**改定の発効日以後に出た版は使えないが、それ以前の版は以前の条件で使い続けられる**（「セキュリティ・完全性・機能を実質的に劣化させる改定はしない」と但し書き）。
- FAQ: 「ChatGPT・Cursor・Lovable などの AI ツールが GSAP のコードを生成するのは問題ない? → もちろん。**AI が生成したコードは Prohibited Use ではない**」「商用プロジェクトで本当に無料? → はい。SplitText・MorphSVG など旧会員限定のプラグインも商用で無料」。

### 外から時刻を決める API（GSAP docs）

- `timeline.seek(position, suppressEvents)`: 「再生中か停止中か・逆再生かに影響せず、特定の時刻（またはラベル）へ跳ぶ」。数値は先頭からの秒、文字列ならラベルや `"-=2"` などの相対。**`suppressEvents` の既定は `true`**で、跳ぶ間のコールバックは発火しない（「レコードの針を持ち上げて別の位置に置く」）。
- `timeline.progress(value, suppressEvents)`: 0〜1 の再生位置（repeat を除く。repeat を含むのは `totalProgress`）。**こちらの `suppressEvents` の既定は `false`**。seek と既定が逆である点に注意（両 docs の記述から）。
- `gsap.globalTimeline`: 「GSAP の全てを動かすルートの Timeline」。`pause()` で全アニメが止まり、`delayedCall` も影響を受ける。`gsap.exportRoot()` はその時点のルートのトゥイーン・タイムラインを新しいタイムラインに移す（完了済みのものは GC のため含まれない、と warning）。
- `gsap.ticker`: `requestAnimationFrame` ごとに globalTimeline を更新する「心臓」。タブが隠れると rAF とともに間引かれる。`lagSmoothing` は既定で有効（500ms を超える遅れは 33ms とみなす）で、「CPU が詰まると時間がゆっくり進んだように見える」。`lagSmoothing(0)` で無効化。→ **実時間で再生して録画すると、重いコマで時刻がずれうる**。seek で撮るならこの問題は起きない（推測。docs は撮影について書いていない）。

### Remotion の `@remotion/gsap`（v4.0.517〜）

- 「GSAP は普通、壁時計で動く自前の ticker でアニメを進める。Remotion は全コマが `useCurrentFrame()` の純関数であることを要求する。このパッケージは paused の GSAP timeline を作り、現在のコマへ seek する」。ライセンスはパッケージ自体は MIT（Remotion 本体の Remotion License は別、[[web-remotion]]）。
- builder に課す決まり（違反すると build 時にエラー）:
  - 再生・seek を書かない（`play()`・`seek()`・`progress()`・`tweenTo()` などは hook が持つ）
  - **コールバック禁止**（`onStart`・`onUpdate`・`onComplete`・`timeline.call()` など）。「描画はコマを任意の順で訪れ、複数のブラウザに分けるので、コールバックは意味のある順に発火しない」
  - 同期の builder だけ（Promise を返さない）
  - **対象は DOM か SVG の要素だけ**。「素のオブジェクトをトゥイーンすると Player では動くが、静止画と描画では止まる。seek の後に誰もそのオブジェクトを読み直さないから」
  - **seed の無い乱数禁止**: `"random(...)"`、`stagger: {from: 'random'}`、`repeatRefresh: true` は GSAP が `Math.random()` で解決するので描画プロセスごとに変わる
  - 迷子のアニメ禁止（builder の外の `gsap.to()`・`gsap.delayedCall()` は壁時計で進む）。長さ 0 の `gsap.set()` は可
- 性能: 「決定論のため、毎コマ timeline を時刻 0 から前へ描き直す。普通は気づかないが、数百のトゥイーンがあるとコマごとにその代価を払う」。プラグインは「まだ非対応」（ScrollTrigger・Draggable は動画では意味がない）。

### HyperFrames の GSAP ガイド

- 「GSAP は HyperFrames の主なアニメ実行系。動きはあなたが書き、再生位置は HyperFrames が持つ」。最小の契約: `gsap.timeline({ paused: true })` を作り、`window.__timelines[<composition-id>]` に登録する。
- 決まり: 重要なトゥイーンには明示の位置を与える／**両端が大事なら `fromTo()` を使う（後ろ向き・ランダムな seek の後も信頼できる）**／動きは transform と opacity で（`top`・`width` などレイアウトの属性を繰り返し動かさない）／クリップの表示とメディアの再生は HyperFrames に任せる（timeline から `video.play()` しない）。
- **文字の幅を測るならフォントを先に読む**: 「`document.fonts.ready` は既に要求されたフォントを待つだけで、使われていない書体は要求しない」。`document.fonts.load('700 64px "LocalFace"', text)` で文字を渡して読み込む。非同期の build が終わる前に空の timeline を登録しない。

### SVG・CSS の標準 API（MDN）

- SVG の SMIL アニメ（`<animate>` など）: `svg.pauseAnimations()` で「その SVG 断片の時計を止め」、`svg.setCurrentTime(秒)` で「時計を新しい現在時刻に合わせる」。
- CSS Animations・Transitions・Web Animations: `document.getAnimations()` が全 `Animation` を返す。`Animation.currentTime`（ミリ秒）は「再生中でも停止中でも」読み書きできる。ただし「タイミング攻撃と指紋採取への対策として、ブラウザの設定によって精度が落とされることがある」と書く。

## この wiki への含意

- **西尾の方式との関係**: [[exp-html-capture-pipeline]] は canvas に `renderFrame(f)` を描いて `canvas.toDataURL` で撮る。GSAP・SVG は DOM を動かすので、**canvas の toDataURL では撮れない**。撮るには (1) ページ全体を `page.screenshot` で撮る自前の撮影、(2) HyperFrames（GSAP が主な実行系、Apache-2.0、[[web-timesnap-timecut-hyperframes-webcodecs]]）、(3) Remotion の `@remotion/gsap`（4 人以上の営利組織は Company License、[[web-remotion]]）のどれか。`renderFrame(f)` の中身を `tl.seek(f / FPS)` にすれば「時刻だけの純関数」という西尾の決まりはそのまま守れる。
- **増える表現**: 文字と SVG のパスを使うモーショングラフィックス（SplitText で文字ごとに出す、MorphSVG で形を変える、DrawSVG で線を描く、MotionPath で経路に沿って動かす）。これらは無償化前は有料の Club プラグインだった。西尾の canvas 方式で手で書いていた「文字を粒子に分解して組み直す」（[[exp-nishio-showreel]]）とは別の、ベクターの形のままの変形が手に入る。
- **型ごと**: promo（ロゴ・文字の作り込み）、talk（図の線を順に引く、ラベルを出す）、embed（流しっぱなしの概念図。SVG なので解像度に依らない）。どれにも効く。
- **LLM に書かせるとき**: Remotion の禁止事項の一覧（コールバック・素のオブジェクト・seed の無い乱数・壁時計）は、エージェントが書きがちな GSAP の典型をそのまま列挙したものと読める。自前で撮るなら、同じ一覧を AGENTS.md / CLAUDE.md に写すのが安い対策（推測）。
- 流行の作品 168 件で GSAP の名前が出たのは 1 件（[[web-opus2-awesome-claude-5-5-videos]]）。一方、HyperFrames は GSAP を主な実行系に置いている。名前が出ないだけで HyperFrames 経由の利用はもっと多い可能性がある（推測）。

## 着手の仕方（未検証。galleria で確かめる）

- **何が表現できるようになるか / 効く型**: 文字・SVG のパスのモーショングラフィックス（文字ごとの出現、線を描く、形の変形、経路に沿った移動）。promo・talk・embed（流しっぱなし）すべて。3D は無い
- **機械**: galleria WSL で足りる（GPU 不要。DOM・SVG の描画は CPU で可）。Mac でも同じ。入れるもの: `gsap@3.15.1`（npm）、`puppeteer`（Chrome for Testing を同梱で落とす）か既存の `puppeteer-core`＋Chrome。費用 0、アカウント不要。利用条件: Standard No Charge License（商用可。Webflow と競合する「コード不要の視覚的アニメ作成ツール」に組み込むのは禁止。所有権表示を消さない。Webflow が改定しうる）
- **成熟度**: 3.15.1（2026-11-04）、4.0.0-beta.3（2026-11-05）。更新は続いている。GitHub star 30,325（参考）
- **最小の手順（WSL）**:
  ```sh
  mkdir -p ~/video-tools-trial/gsap && cd ~/video-tools-trial/gsap
  npm init -y && npm i gsap@3.15.1 puppeteer
  # index.html（推測で書いた最小形）:
  #   <svg id="s" width="1920" height="1080"><circle id="c" cx="960" cy="540" r="0" fill="#e33"/></svg>
  #   <script src="node_modules/gsap/dist/gsap.min.js"></script>
  #   <script>
  #     const FPS = 30, DUR = 3;
  #     const tl = gsap.timeline({ paused: true });
  #     tl.fromTo('#c', { attr: { r: 0 } }, { attr: { r: 400 }, duration: 2, ease: 'power3.out' }, 0);
  #     window.TOTAL_FRAMES = FPS * DUR;
  #     window.renderFrame = f => tl.seek(f / FPS);   // 純関数: f だけで絵が決まる
  #     window.ready = document.fonts.ready;
  #   </script>
  # capture.mjs（推測）: http サーバーで index.html を開き、await page.evaluate('window.ready')、
  #   各 f で page.evaluate(f => renderFrame(f), f) → page.screenshot({type:'png'}) → ffmpeg の image2pipe
  ```
  HyperFrames を使う場合は公式の GSAP ガイドの最小の HTML（`window.__timelines.intro = timeline`）をそのまま置き、HyperFrames の README の描画コマンドで書き出す（コマンドは [[web-timesnap-timecut-hyperframes-webcodecs]] と公式 README を見る）
- **動いたと言える確かめ方**: (1) `ffprobe` で 90 コマ・3.0 秒の mp4、(2) `node capture.mjs stills 0 1 2` 相当で 3 枚の PNG を撮り、円の半径が 0 → 大 → 400 に単調に増える、(3) **同じ f を 2 回、順番を変えて撮って画素が一致する**（`cmp a.png b.png` が無出力。OpenFilm の検査の考え方、[[web-opus2-remotion-openfilm-manim-after-2026-09-22]]）、(4) 日本語のラベルを足したとき、豆腐（□）にならない
- **所要の見込み（推測）**: 最小例で 1〜2 時間。既存の capture.mjs を `page.screenshot` 版に直すのに半日

## Open Questions

- **動画に書き出す使い方が Permitted Uses に入るか**: 条文は「Web サイト、Web アプリ、またはデジタルインターフェースでの実装・使用」と書き、動画の書き出しには触れていない。ローカルの HTML を headless Chrome で描いて mp4 にするのは「Web ページでの使用」と読むのが自然だが、条文の解釈はしていない。Prohibited Uses は「コード不要の視覚的アニメ作成ツール」なので、西尾がコードで動画を作る使い方は当たらないと読める（解釈。確認していない）
- GSAP 4（beta）の API・ライセンスの変化は読んでいない。npm の license 欄は同じ standard-license を指している
- 西尾の DOM を撮る経路は無い。`page.screenshot` を 1 コマずつ呼ぶ速さは測っていない。HyperFrames は `HeadlessExperimental.beginFrame`（chrome-headless-shell が要る）で撮る
- Remotion の「毎コマ時刻 0 から描き直す」と GSAP の `seek` の差（seek は途中から跳ぶ）で、`from()` の初期値の扱いが変わるか。HyperFrames が `fromTo()` を勧める理由はここにあると読めるが、試していない
