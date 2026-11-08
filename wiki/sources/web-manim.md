---
type: source
summary: Manim の 2 系統（3b1b の ManimGL と Manim Community Edition）の README・FAQ・内部解説と 3Blue1Brown の FAQ。Python で数式・図形のアニメを書き、play() ごとに部分動画を作って最後に連結する。数式は LaTeX、それ以外の文字は Pango（日本語可）。作者自身は「ナレーションを manim の中で同期させるものではない、個々のクリップを作る道具で、編集は普通の動画編集ソフトで」と書く
video_types: [talk, embed]
url: https://docs.manim.community/en/stable/faq/installation.html
author: The Manim Community Developers（ManimCE）／Grant Sanderson（3b1b/manim、3Blue1Brown FAQ）
published: unknown（docs は継続更新。ManimCE v0.22.1 は 2026-10-27、ManimGL v1.7.2 は 2024-12-13）
retrieved: 2026-11-09
sources:
  - https://github.com/3b1b/manim/blob/master/README.md
  - https://github.com/ManimCommunity/manim/blob/main/README.md
  - https://docs.manim.community/en/stable/faq/installation.html （"Why are there different versions of Manim?" ほか）
  - https://docs.manim.community/en/stable/guides/deep_dive.html
  - https://docs.manim.community/en/stable/guides/using_text.html
  - https://github.com/ManimCommunity/manim-voiceover/blob/main/README.md
  - https://www.3blue1brown.com/faq
---

# Manim（ManimGL と Manim Community Edition）

## 何の文献か

- 2 つの repo の README（3b1b/manim＝ManimGL、ManimCommunity/manim＝ManimCE）、ManimCE の公式ドキュメント（インストール FAQ、内部の「deep dive」、文字の扱い）、manim-voiceover の README。いずれも一次資料。
- Grant Sanderson（3Blue1Brown、Manim の原作者）のサイトの FAQ（manim の節）。作者本人の実務上の意見。
- どちらも MIT。GitHub のスターは 3b1b/manim 約 9.6 万、ManimCE 約 4.2 万（2026-11-09 の API 値）。

## 書いてあること

### 2 つの版の違い

- ManimCE の FAQ: Manim は Grant Sanderson が個人の道具・3Blue1Brown のために作った。2019 年末に Grant が OpenGL で速く描く `shaders` ブランチを始め、2020 年中ごろに有志が fork して Community Edition に、2021 年初めに Grant が `shaders` を master に入れたのが今の `manimgl`。それ以前の版は `ManimCairo` と呼ばれ、「Grant の古い動画を手元で再レンダリングする」ためだけに役立つ、と書く。
  - ManimCE: PyPI 名 `manim`。`from manim import *`。
  - ManimGL: PyPI 名 `manimgl`。`from manimlib import *`。「実験的な機能が多く、版の間の破壊的変更は文書化されない」。
  - 「初心者には特に community 版を勧める。安定し、テストされ、文書化されている」「文書や安定性を気にせず、Grant と同じ版を使いたいなら ManimGL」。
- 3b1b/manim の README も「2 つの版がある」「インストール手順を混ぜると問題が起きる。先にどちらを使うか決める」と警告する。
- Grant の FAQ: 「自分が使い続けている版は、動画を作りながら新しいものを素早く試すテスト場と見るのがよい」「始めるなら Community Edition から」。

### 1 コマの描き方・時間・レンダリング

- Python でシーン（`Scene.construct()`）を書き、`self.play(Animation, run_time=...)` を順に呼ぶ手続き的な書き方（ManimCE deep dive）。
- deep dive によると、`Scene.play()` の呼び出しごとに「アニメを準備 → 時間軸を進めながら 1 コマずつ描く render loop → 短い動画片（partial movie file）のエンコードを閉じる」。`construct()` が終わったら部分動画をつないで 1 本の動画にする。
- レンダラーは Cairo（CPU のベクター描画、ライブプレビュー不可）と OpenGL（ライブプレビュー可）の 2 つ（ManimCE deep dive）。ManimGL は OpenGL が既定で、`manimgl file.py Scene` で窓が開いて再生される。`-w` でファイルに書く、`-s` で最後のコマだけ、`-n <番号>` で n 番目のアニメまで飛ばす（3b1b README）。
- キャッシュ: 「play の呼び出しごとにハッシュを作り、次に描くとき同じなら前の出力を使い、違えば描き直す」（ManimCE deep dive）。手続きを上から実行する作りなので、ある秒の絵だけを独立に描く仕組みではなく、`play()` の単位で描き直しを省く。
- 必要なもの（3b1b README）: FFmpeg、OpenGL、LaTeX（数式を使うなら）、Linux では Pango の開発ヘッダ。

### 文字と数式

- 文字は 2 系統（ManimCE「Rendering Text and Formulas」）: Pango で描く `Text`・`MarkupText`・`Paragraph`（「你好 や こんにちは や 안녕하세요 のような英語以外の文字も描ける」、フォントはシステムに入っていて Pango が知っている必要がある）と、LaTeX で描く `Tex`・`MathTex`。

### 音声

- 本体はシーンに音声ファイルを足す程度。manim-voiceover（ManimCE のプラグイン、MIT）は「動画編集ソフトを使わず Python の中で直接ナレーションを足す」「レンダリング中にマイクで録音する」「AI の声で開発する」「OpenAI Whisper で単語ごとの時刻を取り、特定の単語でアニメを始める」と書く。対応 TTS は Gemini（推奨）、Azure、gTTS、pyttsx3。

### 作者の意見（3Blue1Brown FAQ）

- 「適した道具かの目安は、コードで絵を作るという考えが窮屈に感じるか、解放的に感じるか。コーディングが好きで、思い描く絵が正確さ・繰り返し・抽象化の恩恵を受けるなら良い兆し。GUI が欲しい、始める手間を減らしたいなら、Desmos や GeoGebra で済まないか先に確かめる」
- 「Mathematica、matplotlib、processing、shadertoy などと比べた manim の違いは、オブジェクト指向の環境で長めのシーンを作る意図で設計され、滑らかさと整ったスタイルが既定になっていること」
- 「Blender や After Effects のようなプロのアニメ道具もプログラムで動かせる。数学以外のアニメも多く要るなら、先にそちらを調べる価値がある」
- 「"ナレーションを manim の中でどう同期させるか" と聞かれると心配になる。これは個々のクリップを作って後で編集でつなぐための道具にすぎない。できるだけ普通の動画編集ソフトを使うべき」

## この wiki への含意

- **西尾の方式との差**: [[exp-html-capture-pipeline]] は「フレーム番号の純関数」で任意の秒を描けるが、Manim は手続きを上から実行する方式で、確認は `-s`（最後のコマ）・`-n`（n 番目まで飛ばす）・`play()` 単位のキャッシュで行う。[[exp-qualia-video]] の「静止スライドの変種＋区間ごとの音声」に近い talk なら、区間＝`play()` と見て同じ組み立てができる。
- **音の扱いが正反対**: Grant は「同期は manim の外で、動画編集ソフトで」と書く。西尾の制作はどれも動画編集ソフトを使わず、時刻表・TTS の区間・ffmpeg でコードの中で合わせている（[[exp-html-capture-pipeline]]、[[exp-qualia-video]]、[[exp-sutra-sync-subtitles]]）。これはエージェントに全工程を回させる前提から来ている。manim-voiceover は、その「コードの中で同期する」側を Manim で実現する道具。
- **embed 型に近い**: 数式の変形・図形の説明を短いクリップで作り、プレゼンに埋め込む用途は、Grant の「個々のクリップを作る道具」という位置づけと合う。
- **日本語**: 字幕・説明文は `Text`（Pango）で日本語が出せるが、フォントは機械に入っているものに依存する。[[exp-html-capture-pipeline]] の「Hiragino は Mac にしかない」と同じ問題が起きる。
- **エージェントに書かせるとき**: LaTeX のエラーと API の誤り（存在しない関数・引数）が LLM の主な失敗だと研究が報告している（[[web-theoremexplainagent-code2video-visualedu]]）。ManimCE と ManimGL の API が違うことも、LLM が混ぜて書く原因になりうる（FAQ が import 文で見分けると書いているので、生成コードの import を確かめる）。

## Open Questions

- Cairo レンダラーでの描画速度（1 分あたり何分）は公式 docs に数字が無い。TheoremExplainAgent の論文は「この種のアニメのローカルレンダリングに GPU は要らない」とだけ書く。
- 日本語の数式混じりの文（LaTeX に日本語を入れる）は、TexTemplate を変える必要があるはずだが、今回の範囲では確かめていない。
- Grant の「編集は動画編集ソフトで」と、西尾の「全部コード」は、エージェントに回させるかどうかで分かれる。どちらが速いかを同じ題材で比べた記録はこの wiki に無い。
