---
type: source
summary: Flourish（Canva の一部）の料金ページ・利用規約・stories の製品ページ（2026-11-09 時点）。無料版は公開して埋め込むだけで、書き出し（画像・HTML）は無く、動画の書き出しは Enterprise だけ。stories は複数の段のグラフを自動再生・ループでき、無料版の埋め込みには Flourish のクレジットが必須。Flourish の内容を含む画像・動画・GIF を作ったら「Created with flourish.studio」の表示（Web・SNS ではリンクも）が必須
video_types: [embed, talk]
url: https://flourish.studio/pricing/
author: Flourish（Canva）
published: 利用規約の最終更新 2026-06-15／料金ページは日付なし
retrieved: 2026-11-09
sources:
  - https://flourish.studio/pricing/
  - https://flourish.studio/terms/
  - https://flourish.studio/product/data-storytelling/
---

# Flourish: ノーコードのデータの物語と、その書き出しの条件

## 何の文献か

Flourish（データ可視化の SaaS。料金ページの FAQ は「Flourish は Canva の一部」と書く）の公式ページ 3 つ: 料金（プランと機能の比較表、FAQ）、利用規約（「Last updated: 15 June 2026」）、stories の製品ページ。いずれも 2026-11-09 に取得。ヘルプセンター（helpcenter.flourish.studio）は 403 で読めなかった。AI 製品の規約（/terms/ai-product-terms/）は取得したが本文が JavaScript で描かれていて読めなかった。料金・規約は宣伝を含む事業者の一次資料。

## 書いてあること

### プランと書き出し（料金ページの比較表）

| プラン | 入手 | 書き出し（Export options） | クレジット |
|---|---|---|---|
| Free | 登録して無料 | **無し** | 公開・埋め込みは「attribution 付き」 |
| Presenter | Canva Business／Enterprise に含まれる | Image（PNG・JPEG・SVG） | Canva と PowerPoint の中では表示しない |
| Publisher | 見積もり（talk to us） | Image、HTML | 外さない |
| Enterprise | 見積もり | Image、HTML、**Video** | 外さない |

- 比較表の行の説明は「Download as PNG, JPEG, SVG, or HTML to host or share anywhere」で、Video は Enterprise の列にだけある
- Free の内容: 「プロジェクト無制限（stories を含む）」「テンプレート全部」「公開前のプロジェクトとデータは非公開」「公開と埋め込みは attribution 付き」
- PowerPoint への埋め込みは Presenter から。Scrollytelling は Publisher から
- AI の機能（Flourish Assistant、MCP の Flourish Connector）は全プランにあり、量の上限がプランで違う

### stories（製品ページ）

- 「グラフとキャプションで複数の段の解説を作る」。グラフから始め「別の見え方を見せたり複数の可視化を組み合わせたり」して物語にする
- 「Autoplay and loop mode — 物語を自動で進める。埋め込みやプレゼンでループする映像に向く」
- 段の間に画像・文字・動画のスライドを入れられる

### 利用規約（2026-06-15）

- 7c「公開・ダウンロード・埋め込みのときの Flourish のクレジット」: 公開すると公開 URL ができ、「Flourish と他の利用者がどんな理由でも改変・利用できる」公開ページに埋め込まれる。プランが公開の制御を含むならその設定が効く
- 埋め込みには、埋め込みコードが入れる Flourish のクレジットとリンクを含め、「取り除いたり隠したり、小さく・目立たなく装飾し直したりしてはならない」（Flourish Business Customers の同じ組織内の埋め込みを除く）
- 「プランが別に定めない限り、または Flourish Business Customer でない限り、**Flourish で作った内容を含む画像・動画・GIF を作ったら、Flourish のクレジットが厳格に必要**。必ず見える文字（"Created with flourish.studio" か同等）を含め、Web や SNS で共有するときは https://flourish.studio へのリンクも含める」
- 利用者の内容について、Flourish に「サービスの提供のため」と「他者と共有したプロジェクト・テンプレートに含まれる範囲で」表示・保存などの非独占・取消不能の許諾を与える
- Free User は「アクティブなアカウントがある間」サービスを使える。ダウンロードしたプロジェクトは、アカウントが無くなっても「改変しない形で」公開してよい

## この wiki への含意

- **無料で mp4 は作れない（公式の経路では）**: 書き出しは Free に無く、Video は Enterprise だけ。無料で動画にする道は、公開した story を自動再生にして画面収録することだが、(1) 公開すると「Flourish と他の利用者が改変・利用できる」公開ページになる（データも公開の前提で考える）、(2) 動画にクレジットの文字が要り、X・YouTube に出すならリンクも要る、(3) 画面収録は実時間でフレーム単位の決定性が無い。西尾の方式（[[exp-html-capture-pipeline]]）には載らない
- **embed への当てはまり**: stories の「自動再生とループ」は、流しっぱなしの embed（[[web-powerpoint-keynote-google-slides-video-playback]] の Keynote のループと同じ使い方）に機能としては合う。Presenter（Canva Business）なら PowerPoint に**動くまま埋め込める**ので、mp4 を経由しない embed になる。ただし発表の会場のネット接続に依存するか（埋め込みが Web 読み込みか）は確かめていない
- **権利の面**: 西尾の経験は「図形と文字だけで描けば権利の確認が要らない」（[[experience-lessons-2026-11]]、[[exp-llm-wiki-explainer-series]]）。Flourish で作ると、クレジットの表示義務と公開の条件が加わる。発信物の説明文に「Created with flourish.studio」とリンクを書く運用になる
- 他のこのページ群の道具（Plot・Vega-Lite・D3、[[web-means-diagram-observable-plot-framework]]、[[web-means-diagram-vega-lite-vl-convert]]、[[web-means-diagram-d3-transition-veltman]]）は OSS で、クレジットの義務も公開の条件も無い。Flourish の利点は「コードを書かずにテンプレートで作れる」「bar chart race などの完成した型がある」ことだが、Claude Code がコードを書く前提ならこの利点は小さい（推測）

## 着手の仕方（未検証。西尾が決めることが先）

- **増える表現**: テンプレートの完成度の高いデータの物語（地図・bar chart race・段ごとに見え方が変わるグラフ）を、コードを書かずに作る
- **機械**: どこでも（ブラウザ）。画面収録するなら galleria Windows の OBS（means-capture の担当範囲）か Mac
- **入れるもの・費用・アカウント**: **要: アカウント**（Flourish の登録。Google か Canva のアカウントでも可）。無料版は書き出し不可。画像・SVG の書き出しは Canva Business（**要: 費用**）、動画の書き出しは Enterprise（**要: 費用、見積もり**）。どれも西尾が決めること
- **利用条件の要点**: 無料版の公開は誰でも見られ再利用されうる。Flourish の内容を含む動画には「Created with flourish.studio」の見える文字（Web・SNS ではリンク）が必須。AI 製品の規約は読めていない
- **成熟度**: 商用 SaaS（Canva の一部）。仕様・料金は告知なく変わりうる
- **最小の手順**（アカウントを作ると西尾が決めた場合）
  1. app.flourish.studio で登録 → テンプレートからグラフ → 「Create story」で段を作る
  2. 公開してよいデータだけで作る（公開の条件のため）
  3. story を Autoplay・Loop にして公開し、公開ページをブラウザで全画面にして画面収録（実時間）
  4. 動画の最後かどこかに「Created with flourish.studio」を入れ、投稿文に https://flourish.studio のリンク
- **動いたと言える確かめ方**: (1) 公開 URL で段が自動で進む、(2) 収録した mp4 に段の切り替えが全部入っている、(3) 動画内にクレジットの文字がある
- **所要の見込み（推測）**: テンプレートに慣れるまで 1〜2 時間

## Open Questions

- Enterprise の動画書き出しの形式・fps・解像度、どのテンプレートで使えるかは、ヘルプセンターが 403 で読めず未確認
- Presenter（Canva Business）で PowerPoint に埋めた Flourish が、オフラインの会場で動くか
- AI 製品の規約（/terms/ai-product-terms/）で、入れたデータが学習に使われるかは読めていない
- 「Flourish で作った内容を含む動画」にクレジットを入れる位置（冒頭・末尾・常時）の決まりは規約に無い。どこに入れれば足りるかは Flourish に確かめる必要がある
