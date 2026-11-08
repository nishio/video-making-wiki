---
type: source
summary: Revideo（Motion Canvas の fork、MIT）の README と作者たちのブログ「なぜ fork したか」。Motion Canvas がエディタのボタンでしか書き出せず、音声の扱いも限られ、本体が単独の道具であることを方針にしていたので、関数呼び出しでのレンダリング・並列化・音声対応を入れるために fork したと書く。2026 年時点で開発の主体は商用の Midrender に移っている
video_types: [any]
url: https://github.com/redotvideo/revideo
author: Revideo（redotvideo、現 Midrender）の創業者たち
published: 2024-04-18（ブログ「We're building our company as a fork of another project - here's why」の最終更新日）／README は 2026-07 版
retrieved: 2026-11-09
sources:
  - https://github.com/redotvideo/revideo/blob/main/README.md （2026-07 時点）
  - https://github.com/redotvideo/revideo/blob/931dd43e87/README.md （2024-06 時点、"Differences between Revideo and Motion Canvas" 節）
  - https://re.video/blog/fork （Wayback Machine 2024 年の保存版で読んだ。現在は Midrender のページへ転送される）
  - https://midrender.com/revideo （"The next chapter of Revideo"）
  - https://github.com/redotvideo/revideo/blob/main/LICENSE
---

# Revideo（Motion Canvas を API 化した fork）

## 何の文献か

- Revideo の GitHub README の現行版（2026-07）と 2024-06 版（Motion Canvas との違いを書いた節がある）。
- 作者たちのブログ記事「We're building our company as a fork of another project - here's why」（re.video/blog/fork、最終更新 2024-04-18）。現在の URL は転送されるので、Wayback Machine の 2024 年の保存版を読んだ。
- いずれも当事者（fork した側）の説明。fork された Motion Canvas 側の言い分は、ブログに引用された Kai Sassnowski（Motion Canvas のメンテナー）の 2024-03-26 のツイートの冒頭だけで、全文は読んでいない。

## 書いてあること

### なぜ fork したか（ブログ、2024-04）

- 経緯: 2024 年初めに「LLM の finetuning-as-a-service」から AI を使った動画編集・制作に方向転換し、テンプレートで短尺動画を作る Web エディタを作った。最初は MoviePy で作ったが「プレビューが無く、結果を見るには書き出しを待つしかない」「Web ベースでないのでブラウザで編集できない」ので Remotion に移った。
- Remotion について: 「価格はとても公正で、払ってもよかった」が、「単一の会社が持つコードへの依存」と、自分たちの上に作る他社や、自社のアプリを顧客が自前で動かす場合にも Remotion のライセンスが及ぶことを避けたかった、と書く。MVP は Remotion で作り、代わりが見つかったら移る予定だった。
- Motion Canvas に足りなかったもの（ブログの列挙）:
  - レンダリングは Motion Canvas の UI からしか起動できない。アプリを作るには API が要る
  - video 要素の音声が書き出しに入らない
  - 音声ファイルを編集・同期できない。「できるのは、作り終えた音声ファイル 1 本をアニメに重ねることだけ」
  - 動画の中に動画を入れると書き出しがとても遅い
- 「理由 1: どうせ同じものを作ることになった」（ゼロから作れば MVP まで 6 か月以上、Motion Canvas を拡張すれば 1 か月）。「理由 2: 目的が違う」: プラグイン API では足りず、Motion Canvas のメンテナーは音声対応などを「範囲外」と繰り返し述べており、Motion Canvas を「単独の道具」として使ってほしく、npm パッケージなのは配布のためにすぎない、と読んだ。
- 反省として「最初の発表は自分たちの貢献を誇張し、Motion Canvas の功績を十分に書かなかった」と認め、表記を改めたと書く。MIT のまま続けると書く。

### Motion Canvas との違い（README 2024-06 版）

- **Headless レンダリング**: 「Motion Canvas は UI のボタンを押さないと描けない。私たちはこれを関数呼び出し（`renderVideo()`）にし、Google Cloud Run などにレンダリング API を置けるようにした」。
- **速いレンダリング**: 並列レンダリング（PR #74）と、HTML の video の `seek()` を FFmpeg ベースのフレーム抽出に置き換えた（PR #33）。
- **音声**: `<Video/>` の音声を書き出しに含め、アニメと同期できる `<Audio/>` を加えた。

### 現在（README 2026-07 版、Midrender のページ）

- 「Revideo は動画をコードで作るレンダリングエンジン。シーンを TypeScript で書くと動画ファイルにする。headless のレンダリング API と、ブラウザでプレビューする React のプレイヤーを出している」「シーンは普通の TypeScript なので、Claude や Codex がプロンプトから作れる」と書く。
- 現行の README は「Revideo は Remotion と Rive から概念を借りているが、核はゼロ依存」と書き、Motion Canvas の名を出していない。一方 LICENSE は今も「Copyright (c) 2022 motion-canvas」の MIT のまま。Midrender のページは「Motion Canvas の fork で、headless レンダリング・音声対応・ライブラリ優先の API を加えた」と書く。
- 「Revideo の開発チームは今は主に Midrender（AI でコンポジションを編集できるモーショングラフィックスの視覚エディタ。MCP に対応）に取り組んでいる。アニメーションエンジンは Midrender の一部として開発が続くが、最近の変更はまだ OSS の repo に upstream されていない」と書く。
- テレメトリ: 描いた動画の数を PostHog で匿名に数える。`DISABLE_TELEMETRY=true` で止める。
- GitHub のスター約 4,200、最新は 0.11.0（2026-07-10）。

## この wiki への含意

- **道具を選ぶ問いの立て方**: Revideo の fork の理由は「コマンド 1 つで書き出せるか」「音声を区間ごとに置けるか」「ライセンスが自分の使い方に及ぶか」で、どれも「エージェントに回させる」ときに効く条件。[[exp-html-capture-pipeline]] の `node capture.mjs video` や [[exp-qualia-video]] の `render_video.py` は最初から CLI で、人がボタンを押す工程が無い。この性質が Claude Code・Codex に作らせられた前提の一つだった。
- **音声の扱い**: Revideo が足した `<Audio/>` の同期は、西尾の方式で言えば「numpy で合成した BGM と TTS の区間 WAV を ffmpeg で後から重ねる」工程（[[exp-html-capture-pipeline]]）を描画側に取り込むもの。後から重ねる方式でも困っていないので、乗り換える理由にはなりにくい。
- **ライセンスの比較**: [[web-remotion]] は 4 人以上の営利組織で有料、Revideo・[[web-motion-canvas]] は MIT。

## Open Questions

- OSS の Revideo に最近の変更が戻っていない（Midrender 側で開発）。今から使うなら保守の見込みが問題になる。
- 並列レンダリングでどれだけ速くなるかの数字は README・ブログに無い（PR #74 は未読）。
- Motion Canvas 側が fork をどう見ているか（メンテナーのツイートの全文、Motion Canvas の Discussion #1015）は読んでいない。ブログは fork した側の要約。
