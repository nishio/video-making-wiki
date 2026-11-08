---
type: source
summary: Opus 5.5 公開直後に X に出た「Claude 5.5 で作った動画」を集めて分類した GitHub のデータセット（athemeroy/awesome-claude-5-5-videos、2026-09-25〜10-11）。分類器のラベルではゲーム・広告・AI の話題が 6 割近くを占め、教育・科学は少数派。手で選んだ 168 件のうち「教育の解説」は 27 件で、尺の中央値 102 秒と他の制作経路（25〜52 秒）より長い
video_types: [promo, talk, embed]
url: https://github.com/athemeroy/awesome-claude-5-5-videos
author: athemeroy（個人の GitHub リポジトリ。文章と図は CC BY 4.0）
published: 2026-09-25（repo 作成）〜2026-10-11（最終 push）
retrieved: 2026-11-09
sources:
  - https://github.com/athemeroy/awesome-claude-5-5-videos/blob/main/README.md
  - https://github.com/athemeroy/awesome-claude-5-5-videos/blob/main/docs/snapshot-analysis.md
  - https://github.com/athemeroy/awesome-claude-5-5-videos/blob/main/docs/statistics.md
  - https://github.com/athemeroy/awesome-claude-5-5-videos/blob/main/docs/collection-analysis.md
  - https://github.com/athemeroy/awesome-claude-5-5-videos/blob/main/docs/visual-effects-fit.md
  - https://github.com/athemeroy/awesome-claude-5-5-videos/blob/main/docs/workflow-analysis.md
  - https://github.com/athemeroy/awesome-claude-5-5-videos/blob/main/data/cases.csv
  - https://github.com/athemeroy/awesome-claude-5-5-videos/blob/main/data/claude55-source-review-2026-10-03.csv
---

# awesome-claude-5-5-videos（Claude 5.5 で作った動画の収集と分類）

## 何の文献か

- 個人（athemeroy）の GitHub リポジトリ。2026-09-25 作成、最終 push 2026-10-11、スター 973（2026-11-09 の API 値）。X の投稿を検索で集め、投稿本文・作者の返信・公開された repo を読み、動画は 9 コマを抜き出して見た（Hypit 0.2.3）、と書いている。動画ファイルは再配布していない
- 査読はない。集め方は X の検索（56 クエリ、2026-09-26 21:05 中国標準時まで）で、作者自身が「X 全体での割合・時間的な傾向・母集団の信頼区間は出さない」「9 コマでは連続した動き・音・事実の正しさ・隠れたツール呼び出しは確かめられない」と書いている（`docs/statistics.md`「Limits on inference」）
- 分類の多くは**機械のラベル**: 1,401 ファイルの投稿文と 9 コマを Gemini 3.8 Flash に見せて、Opus が関わったか（yes / likely / no）・主な題材・主な見た目を 1 つずつ付けさせた（`docs/snapshot-analysis.md`）。作者は「これらのラベルは作者やモデル呼び出しを確かめるものではない」と書く
- 別に、制作経路と証拠を調べるために**手で選んだ 168 件**（`data/cases.csv`）がある。無作為抽出ではない
- この repo の「brief contagion」（同じ一行プロンプトから似た動画が大量に出る）の分析は [[web-movez-opus-motion-design-course]] が紹介している。このページでは扱わず、**何の動画が作られたか**（型と制作経路）だけを読む

## 書いてあること

### 作られたものの内訳（2026-09-26 のスナップショット、機械ラベル）

- 候補の投稿 1,511、MP4 の添付 1,449、中身の違うファイル 1,401。そのうち yes か likely の 1,119 ファイルを分母にしている（`docs/snapshot-analysis.md`）
- **題材**: ゲーム・インタラクティブ 230、広告・ローンチ 215、AI についての AI 201。この 3 つで 646 ファイル（57.7%）。yes だけに絞ると 1 位が広告（191）とゲーム（187）で入れ替わる（同）
- **見た目**: モーショングラフィックス・UI 350、3D レンダー 324 で 60.2%（同）
- **題材×見た目の上位**: ゲーム×3D 161（14.4%）、広告×モーショングラフィックス 154（13.8%）、AI×モーショングラフィックス 62、AI×3D 60、**教育・科学×モーショングラフィックス 55（4.9%）**、短い物語×フラットなカートゥーン 37、…、**教育・科学×フラットなカートゥーン 25（2.2%）**（`docs/statistics.md` の上位 10 セル）
- 「教育と物語は見た目がばらける。最大の組（教育ならモーショングラフィックス）でも 37.4%」と書いている（README）。この 37.4% と 55 件から逆算すると教育・科学は約 147 ファイル（このページでの計算）で、1,119 の 1 割強
- 尺: 全 1,401 ファイルの X のプレビューの中央値 39.20 秒（四分位 21.91〜77.07 秒）（`docs/statistics.md`）

### 手で選んだ 168 件の制作経路

| 経路（repo の分類） | 件数 | 尺の中央値（秒） | 四分位（秒） |
|---|---:|---:|---|
| コードで描く 2D | 52 | 46.38 | 30.00–105.64 |
| **教育の解説（educational explainer）** | **27** | **102.28** | **60.05–256.54** |
| 3D・リアルタイム描画 | 19 | 34.18 | 23.02–64.17 |
| 既存の素材の変換（実写の描き直しなど） | 32 | 40.54 | 26.81–56.85 |
| 外部の動画生成モデルを指揮 | 10 | 24.76 | 19.33–52.82 |
| アプリ・ゲームの画面収録 | 14 | 50.30 | 32.65–116.13 |
| 混合・不明 | 14 | 51.79 | 27.53–152.91 |

（`docs/statistics.md`。作者は「尺は制作時間・費用・品質・経路の成否を示さない」と書く）

- 教育の解説 27 件は 30 秒〜12 分 12 秒。4 分を超えるもの（英文法 6 分 34 秒〔repo のメモは 6m12s と書くが duration は 394.3 秒〕、インフレ 4 分 24 秒、パスキー 4 分 10 秒と 6 分 15 秒、大気循環 4 分 48 秒、VAE 5 分 35 秒、導関数 7 分 37 秒、Transformer 12 分 12 秒）のうち、Transformer 以外はナレーション（TTS か作者の声）付きと作者が書いている。Transformer は声について書いていない（`data/cases.csv` の creator_disclosure。個々の投稿は [[web-opus2-opus-5-5-explainer-posts-on-x]]）
- 後の追加分（10-02〜10-11）は「題材」の分類が別で、10-03 の 157 件では interactive 41、motion 20、character 18、comparison 18、**science 16**、music 12、history 9、product 9 など（`data/claude55-source-review-2026-10-03.csv`）

### どの描画方式が名指しされたか（このページで数えたもの）

168 件の作者の開示（creator_disclosure）と repo のメモ（review_note）に、道具の名前が出る件数をこのページで数えた（キーワードの一致。1 件に複数出ることがある。名前が出ないものが多い）:

| 道具 | 168 件中 | 教育の解説 27 件中 |
|---|---:|---:|
| Canvas / SVG / JavaScript / HTML（名前だけ） | 55 | 8 |
| Blender | 15 | 0 |
| Three.js / WebGL | 10 | 0 |
| Remotion | 10 | 2 |
| HyperFrames | 8 | 1 |
| headless ブラウザ・ffmpeg・Playwright | 8 | 1 |
| p5.js | 5 | 0 |
| Manim | 2 | 2 |
| GSAP | 1 | 1 |

- 教育の解説で Manim を使ったと書いたのは 2 件（導関数、VAE）だけ。残りは「JS で」「コードで描いた」とだけ書くか、道具を書いていない
- repo の判断の手引き（`docs/visual-effects-fit.md`、調査の締めは 2026-09-27）は、「工程・教育・データの解説」の描画先に「Manim / SVG / Remotion、任意で TTS と字幕」を挙げ、確認として「すべての事実の主張・式・単位・発音・音声の全編を確かめる。完成した絵は事実の検証ではない」と書く

### 作者の開示の読み方として書いていること

- 「一行のプロンプト」の裏に、スキル・素材・既存のワークスペース・内部の作り直しがある例を並べている（`docs/workflow-analysis.md`）。例: 記事から 1 分動画を作った例は Opus（計画・台本・設計）＋ Sonnet 9 体（場面）＋ HyperFrames ＋外部の画像・音楽・TTS で、「演出の指示を読み上げた」「84 秒を 61 秒に縮めた」「書き出し後のフェード」を内部で直した、と作者が報告している
- 「もっともらしいアニメは検証済みの説明ではない」: 塔の建設の例では作者自身が「手順は作り話、形は単純化、構造計算はしていない」と書いている（同）

## この wiki への含意

- **talk に当たる長い解説は、流行の中で少数派だが確かに作られていた**。分類器のラベルでは教育・科学は 1 割強で、広告・ゲーム・AI が主だった。手で選んだ件では「教育の解説」は他の経路の 2〜4 倍の尺（中央値 102 秒）で、4 分を超えるものは 1 本を除きナレーション付きと作者が書いていた。[[exp-timeline-2026]] の「9/25 以後は promo に寄った」は、西尾だけでなく流行全体の偏りと同じ向き（ただし集め方が X の検索なので、何が「流行った」かは拡散されやすさにも左右される）
- **embed（流しっぱなしで発表に埋め込む概念解説）として作った、と書いた例は、このデータセットの開示の中には見つからなかった**（このページで "slide"・"presentation"・"lecture"・"课件"・"授業" などを grep した範囲）。近いのは 10-03 の 1 件「Expressive interactive presentation」（作者が自前の harness で作った対話的な発表の裏側を見せたもの。repo は「成片と対話の分担は未審査」と書く）で、これは話し手が操作する発表で、流しっぱなしの動画ではない。教育の解説はどれも単独で見る前提（YouTube・X・bilibili）で書かれている
- **描画方式は「名前を書かない JS/Canvas」が最多で、Remotion・HyperFrames・Manim は少数**。西尾の方式（[[exp-html-capture-pipeline]] の canvas＋`renderFrame(f)`＋headless Chrome）は、この「名前のない JS」の側に入る。talk の長い解説では Manim と Remotion が名指しされた
- **確認の項目に「発音」と「音声の全編」が入っている**のは、[[exp-qualia-video]] の「機械 QA が通っても読み・声質は人間が見ないと分からない」、[[exp-galleria-tts-and-singing]] の「最後は耳」と同じ向き

## Open Questions

- 教育・科学の割合は、分類器（Gemini 3.8 Flash）のラベルと X の検索語の両方に左右される。talk 型が本当に少なかったのか、拡散されにくかっただけかは、このデータからは分からない
- 名指しされた道具の件数はこのページのキーワード数え。「JS で描いた」とだけ書いたものの中身（素の canvas か、Remotion か）は区別できない
- repo は 2026-10-11 で更新が止まっている。その後（10 月半ば〜11 月）に talk・embed の作例が増えたかは別に調べる必要がある
