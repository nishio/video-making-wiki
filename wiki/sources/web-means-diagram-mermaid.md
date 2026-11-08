---
type: source
summary: テキストから図を作る Mermaid と mermaid-cli（mmdc）の公式ドキュメント・リリース・ソース。書き出しは SVG/PNG/PDF で、動きは辺の破線アニメ（CSS）と、v12.3.0（2026-11-03）で入った「辺に step 番号を付けると点が順に辺をたどる」機能（SVG の SMIL）だけ。どちらも時刻を外から合わせて撮れる形だが、ノードを順に出す機能は無い
video_types: [embed, talk]
url: https://mermaid.js.org/syntax/flowchart.html
author: Mermaid チーム（mermaid-js）
published: mermaid 12.3.0（2026-11-03）／mermaid-cli 12.2.0（2026-11-02）
retrieved: 2026-11-09
sources:
  - https://github.com/mermaid-js/mermaid/blob/develop/packages/mermaid/src/docs/syntax/flowchart.md
  - https://github.com/mermaid-js/mermaid/releases/tag/mermaid%4012.3.0
  - https://github.com/mermaid-js/mermaid/commit/692d22a3ec9cf235cecf17013160f14dafb42999
  - https://github.com/mermaid-js/mermaid-cli/blob/master/README.md
  - https://github.com/mermaid-js/mermaid-cli/blob/master/package.json
  - https://github.com/mermaid-js/mermaid-cli/blob/master/docs/linux-sandbox-issue.md
  - https://developer.mozilla.org/en-US/docs/Web/API/Document/getAnimations
  - https://developer.mozilla.org/en-US/docs/Web/API/Animation/currentTime
  - https://developer.mozilla.org/en-US/docs/Web/API/SVGSVGElement/setCurrentTime
---

# Mermaid と mermaid-cli: テキストの図に「順に流れる」動きを付ける

## 何の文献か

Mermaid（MIT、star 約 9.1 万）の公式ドキュメント（flowchart の構文ページ、develop ブランチの md）、GitHub のリリースノート、step アニメの実装コミット（692d22a、2026-10-18）、mermaid-cli（MIT、star 約 5,200）の README・package.json・既知の問題のページ。いずれも作り手の一次資料。npm の最新は mermaid 12.3.0（2026-11-03）、mermaid-cli 12.2.0（2026-11-02）。

## 書いてあること

### mermaid-cli（mmdc）

- 「mermaid の定義ファイルを入力に SVG/PNG/PDF を出す CLI」。`npm install -g @mermaid-js/mermaid-cli`、`mmdc -i input.mmd -o output.svg`、背景透過は `-b transparent`、PNG の大きさは `--size`（README）
- `--cssFile` で CSS を差し込める（Mermaid の `themeCSS` に渡る）。README に「カスタム CSS で SVG をアニメにする」例がある
- Docker イメージ（`minlag/mermaid-cli`）と Node API（`run()`、semver の対象外）もある
- package.json: 依存 `mermaid ^12.2.0`、peer に `puppeteer ^25.0.0`、`engines.node >=22.13.0`。つまり内部で headless Chrome を使って描く
- Linux で root のまま動かすと Chrome が sandbox で起動しない。`{"args": ["--no-sandbox"]}` を書いた設定ファイルを `mmdc -p puppeteer-config.json` で渡す（docs/linux-sandbox-issue.md。ただし「まず root で動かさないこと」と書く）

### 辺のアニメーション（flowchart）

- 辺に ID を付ける: `A e1@--> B`。`e1@{ animate: true }` で辺が動く。速さは `animation: fast | slow`（構文ページ「Turning an Animation On」）
- classDef で CSS アニメを直接書ける: `classDef animate stroke-dasharray: 9,5,stroke-dashoffset: 900,animation: dash 25s linear infinite;`（同）。つまり破線が流れる **CSS animation**
- **step 番号（v12.3.0+）**: 「辺に `step` 番号を付けると、その step になったとき点が辺を走る。step 1、2…の順に回り、最後の step の後また始まる。同じ番号の辺は同時に動く」。1 step の既定は 1 秒、`flowchart.stepDuration`（秒）で変える。走っている辺は太く強調（クラス `edge-step-highlight`）。`flowchart.stepNumbers: true` で辺に番号の札を出し、「アニメを見なくても、印刷でも、動きを減らす設定でも順番が読める」。`prefers-reduced-motion: reduce` のときは点と強調を隠して静止図になる
- **実装（コミット 692d22a）**: 点は `<circle class="edge-step-dot">` に SMIL の `<animateMotion>`（`path`・`dur`・`begin="${begin}s;${id}.end+${gap}s"`）と `<animateTransform>` を付ける。つまり **SVG の SMIL** で、ループは `begin` の連鎖で作っている

## この wiki への含意

- **時刻を外から合わせられる**: 辺の破線は CSS animation なので `document.getAnimations()` で取れ、各 `Animation` の `currentTime`（ミリ秒）を書けばその時刻にシークできる（MDN: getAnimations は「CSS Animations・CSS Transitions・Web Animations を含む」、currentTime は「再生中でも停止中でも設定できる」。Chrome は丸めない）。step の点は SMIL なので `svg.pauseAnimations(); svg.setCurrentTime(秒)`。どちらもフレーム番号から 1 枚が決まり、[[exp-html-capture-pipeline]] の「フレーム番号の純関数を headless Chrome で撮る」に載る（MDN と実装からの推測。未検証）
- **できないこと**: Mermaid 自身にノードを順に出す（段階表示）機能は無い。step は「辺の上を点が走る」で、全体の図は最初から全部見えている。段階表示が要るなら (a) 全体を一度描き、後の要素を CSS の opacity で隠して `renderFrame(f)` から出す（レイアウトが動かない）、(b) 段ごとに別の `.mmd` を描いて切り替える（dagre が段ごとに配置し直すので位置が跳ぶ。推測）。embed には (a) が合う（推測）
- **embed（流しっぱなし）に向く使い方**: step の点で「リクエストがどう流れるか」「処理がどの順か」を一周見せる形は、30〜60 秒で一つの流れを見せる embed にそのまま当たる。ただしループするので、流しっぱなしの動画にするなら「何周撮るか」を決めて切る。`stepNumbers` を付ければ動きを見落としても順番が読める（Mayer の signaling、[[web-mayer-multimedia-principles]] の担当の当てはめ）
- 経験との照合: [[exp-gyazo-resumption-video]] で西尾は「今の棒グラフいまいち」として「JSON を 1 字ずつ打つ側と、確率が一度に揃う側の比較図」に変えさせた。**処理の順・流れを見せる図**のほうが通じた例で、Mermaid の step はその種類の図を少ない手間で作れる（推測）
- [[web-timesnap-timecut-hyperframes-webcodecs]] の timesnap は「CSS の transition・animation は意図どおり描けない」と書く。Mermaid の破線は CSS animation なので timesnap では撮れず、WAAPI のシークか HyperFrames の CSS アダプターになる

## 着手の仕方（未検証。galleria で確かめる）

- **増える表現**: システムや手順の流れ図で、点が順に辺を走り、走っている辺が太くなる 30〜60 秒の mp4（embed 向き）。テキスト 10 行ほどで図が変わるので、Claude Code に図ごと書かせやすい
- **機械**: galleria WSL（Node は ~/.local/bin）。Windows 側でも可。Mac でも可
- **入れるもの**: `@mermaid-js/mermaid-cli`（12.2.0。依存の範囲 `^12.2.0` から、新しく入れれば mermaid 12.3.0 が入るはず＝推測。`npm ls mermaid` で確かめる）、puppeteer が持ってくる Chrome。費用 0、アカウント不要、MIT
- **成熟度**: リリースが頻繁（mermaid 12.3.0 が 2026-11-03、mermaid-cli 12.2.0 が 2026-11-02）。step 機能は出て 1 週間で、仕様が変わりうる
- **最小の手順**（WSL）
  1. `mkdir -p ~/video-tools-trial/mermaid && cd $_ && npm init -y && npm i @mermaid-js/mermaid-cli puppeteer`
  2. `flow.mmd` に構文ページの例を書く（`Client e1@--> API` … `e1@{ step: 1 }` …、先頭の `config:` に `flowchart: { stepDuration: 1, stepNumbers: true }`）。ラベルは日本語で
  3. `npx mmdc -i flow.mmd -o flow.svg -b white`（root なら `-p puppeteer-config.json`）
  4. `grep -c animateMotion flow.svg` で step の数が出ることを確かめる
  5. `flow.svg` を HTML にインラインで入れ、`python3 -m http.server 8000`
  6. 撮影は [[web-means-diagram-excalidraw-animate-tldraw]] の骨格と同じ。各フレームで `svg.pauseAnimations(); svg.setCurrentTime(f/FPS)` と、破線を使う場合は `document.getAnimations().forEach(a => { a.pause(); a.currentTime = f/FPS*1000; })` を呼んでからスクリーンショット
- **日本語**: mmdc は Chrome で描くので、WSL に日本語フォントが無いと豆腐になる（推測）。`fc-list :lang=ja` で確かめ、無ければ `sudo apt install fonts-noto-cjk`（galleria で。CyEC2 ではしない）か、`--cssFile` で `@font-face` を指定
- **動いたと言える確かめ方**: (1) `flow.svg` に `edge-step-dot` と `animateMotion` がある、(2) 撮った mp4 の 1 秒目と 2 秒目で点が別の辺にいる（stepDuration=1 のとき）、(3) 同じ f の PNG の sha256 が 2 回で一致、(4) `ffprobe` の duration が「step 数 × stepDuration × 周回数」と合い、f と f＋（step 数 × stepDuration × FPS）の PNG が同じ（1 周で元に戻る）
- **所要の見込み（推測）**: 入れて SVG が出るまで 15 分、撮影まで 1〜2 時間

## Open Questions

- 1 周の長さ: コミットの `getEdgeStepTiming` は step k の辺に `begin=(k-1)×d`・`dur=d`・`gap=(n-1)×d`（d は stepDuration、n は step 数）を与え、`begin` に「前回の end＋gap」を連ねる。つまり各辺は n×d ごとに走り、1 周は n×d 秒（ソースの読みから。描かれた SVG で確かめる）。ただしこれは最初のコミットで、12.3.0 の出荷版で同じかは確かめていない
- mmdc の出力 SVG を `<img>` で読むと SMIL は動くが `pauseAnimations` を呼べない。インラインにしたとき Mermaid の ID・スタイルが他とぶつからないか
- `prefers-reduced-motion` を headless Chrome の既定がどう返すか（reduce なら点が消える）。撮るときは `page.emulateMediaFeatures([{name:'prefers-reduced-motion', value:'no-preference'}])` で固定するのが安全（推測）
- ノードを順に出す機能は Mermaid に無い。要望・計画があるかは調べていない
