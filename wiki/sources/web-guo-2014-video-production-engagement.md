---
type: source
summary: Guo・Kim・Rubin（L@S 2014）が edX の 4 講座・862 本・690 万視聴セッションのログから、動画の作り方とエンゲージメント（視聴時間と直後の問題への挑戦）の関係を調べた観察研究。短い動画、講師の顔の挿入、タブレット手描き、速めの話し方、MOOC 用に計画した収録が「長く観られた」と報告するが、学習効果は測っていない
video_types: [talk, embed]
url: https://pg.ucsd.edu/publications/edX-MOOC-video-production-and-engagement_LAS-2014.pdf
author: Philip J. Guo（MIT CSAIL / University of Rochester）, Juho Kim（MIT CSAIL）, Rob Rubin（edX）
published: 2014-03（L@S 2014, Atlanta, 2014-03-04〜05）
retrieved: 2026-11-09
sources:
  - https://pg.ucsd.edu/publications/edX-MOOC-video-production-and-engagement_LAS-2014.pdf
  - https://doi.org/10.1145/2556325.2566239
---

# Guo, Kim, Rubin (2014) How Video Production Affects Student Engagement: An Empirical Study of MOOC Videos

## 何の文献か

ACM Learning @ Scale 2014 の査読付き会議論文。**後ろ向きの観察研究で、対照実験ではない**（Limitations 節「This paper presents a retrospective study, not a controlled experiment」）。

- データ: edX の Fall 2012 の 4 講座（6.00x 入門 CS・MIT・オフィスの机で収録、PH207x 公衆衛生統計・Harvard・TV スタジオ、CS188.1x AI・Berkeley・教室、3.091x 固体化学・MIT・教室）。動画 862 本、学生 127,839 人、視聴セッション 6,902,358（表 2）。全講座が数学・理科系
- 測度は二つの代理指標（Measuring Engagement 節）
  - **engagement time**: 1 セッションで動画を観ていた時間。「cannot capture whether a watcher is actively paying attention to the video or just playing it in the background」と自ら書く
  - **problem attempt**: 動画の直後に問題がある場合（全動画の 32%）、30 分以内に問題に挑戦したか
- 5 秒未満のセッションは自動再生によるものとして除外。報告は 1 倍速の再生（全セッションの 76%）だけ
- 補足として edX の動画制作担当 4 人とプログラムマネージャー 2 人に非公式インタビュー

著者ははっきり「it is important not to draw any conclusions about student learning solely from our findings about video engagement」と書いている。エンゲージメントは学習の必要条件だが十分条件ではない、という位置づけ。

## 書いてあること

| 発見（表 1 の左列） | 数値（本文） | 推奨（表 1 の右列） |
|---|---|---|
| 短い動画ほど観られる | 長さが「by far the most significant indicator」。視聴時間の中央値は長さに関係なく最大 6 分。9 分を超える動画は半分まで観られないことが多い。0〜3 分の動画では 75% のセッションが長さの 3/4 以上を観た。直後の問題への挑戦率は長さの 5 区分で 56%・48%・43%・41%・31% | 事前の授業計画に力を入れて 6 分未満に区切る |
| 講師の顔（talking head）をスライドと交互に入れると観られる | 6.00x で顔ありの動画の後の問題挑戦 46% 対 その他 33%（χ² p << 0.001）。一時停止・再生の回数に差はなかった | 編集で適切なときに講師の顔を入れる |
| 個人的な雰囲気の収録のほうが観られるかもしれない | 机で近くから撮った 6.00x は、TV スタジオの PH207x より 6〜12 分の動画で約 2 倍、12 分超で約 3 倍長く観られた。ただし講座が 1 組しかなく講師の腕の差の可能性ありと自ら書く | 非公式な場所で、カメラに目線を合わせて撮る |
| Khan 風のタブレット手描きはスライドやコード画面より観られる（tutorial で） | 1.5〜2 倍長く観られた。問題挑戦 40% 対 31% | 手描きで撮る。スライドを使うならその上に手で書き込む |
| 良い教室講義の録画でも、MOOC 用に切り刻むと観られにくい | MOOC を想定して計画した CS188.1x の後の問題挑戦 55% 対 古い録画を切った 3.091x 41%。これも 1 組の比較 | 教室で撮るとしても MOOC 用に計画する |
| 速く・熱意をもって話す講師ほど観られる | 話す速さは 48〜254 wpm（平均 156、SD 31）。同じ長さの区分の中で、速いほど最大 2 倍観られた。6〜12 分の動画では中くらい（145〜165 wpm）が一番低かった | わざと遅く話さなくてよいと伝え、熱意を引き出す。言いよどみは編集で切る |
| lecture と tutorial で観られ方が違う | tutorial は長さに関係なく 2〜3 分しか観られず、観直し・一時停止が多い | lecture は初回視聴の体験を、tutorial は観直し・飛ばし読みの支えを |

話す速さについて、著者は「speaking rate is merely a surface feature that correlates with enthusiasm」と書き、熱意のない講師を速くしても効かないかもしれないので「無理に速く話させるな」と推奨している。速い動画でも理解に困らなかったのは「the same information was also presented visually in PowerPoint slides」だったから、とも書く。

制作担当は「pre-production（計画）が一番効く」と感じていたが、計画の効果は特定の映像上の特徴として示しにくい、とも書いている。短い動画が観られるのは短いからだけでなく、簡潔に説明するために計画が要るから、という仮説も出ているが「we do not yet have the data」。

## この wiki への含意

- **長さ**: 「6 分」は「視聴時間の中央値の上限が 6 分だった」という観察で、「6 分なら学習が最大」ではない。被験者は 2012 年の edX の初期の学習者（自ら「self-motivated learners and technology early adopters」と書く）で、全講座が理系
  - [[exp-qualia-video]] の journey は 8 分 58 秒の初版を、人間の評価（「細かい数値を耳で聞くのが辛い」「最初の 1 分で目的と関心を作る」）を受けて 6 分 33 秒に削った。Guo の観察と同じ向きだが、削った理由は長さそのものでなく台本の分かりにくさだった
  - embed は講演の中で流すので、観るのをやめるという選択肢が聴衆にほぼない。Guo の測度（途中でやめる）は embed にはそのまま当たらない
- **話す速さ**: [[exp-qualia-video]] の pilot は SAPI の Rate を上げて尺に押し込み、評価された問題は速度でなく読みと声質だった。Guo の「速さは熱意の表面にすぎない」と同じ読み方ができる。英語の wpm を日本語のモーラ毎分に換算する根拠はこの論文にない
- **講師の顔**: エンゲージメントは上がったが、学習については Mayer の image principle（話し手の姿を足しても学習は 0.20、[[web-mayer-multimedia-principles]]）があり、測度が違う。TTS とキャラクター絵で作る [[exp-qualia-video]] には顔の挿入はなく、比べられない
- **手描き**: 「動きと連続した視覚の流れを入れよ」という推奨は、[[exp-qualia-video]] の「完全静止を既定」と表面上は逆に見える。ただし Guo が勧めるのは**説明している内容そのものが描かれていく動き**で、[[exp-qualia-video]] で否定されたのは説明と無関係な全画面の drift だった。前者は signaling 寄り、後者は装飾。ここは食い違いではなく「何が動くか」の違いと読める（読みであって検証していない）
- **計画して作る**: 古い録画を切った 3.091x が観られなかったことは、[[three-video-types]] の「講演 → 短尺は配信面の制約で作りが決まる」と同じ向き。講演を切り出すときは、元の講演の流れでなく切り出し先の単位で作り直す必要がある（[[exp-democracy-river-video]]）
- **lecture と tutorial**: lecture は初回視聴の一本道、tutorial は観直しの拠点。talk 型の解説は lecture 寄り。手順を見せる動画を作るなら章立て・目印が要る

## Open Questions

- エンゲージメント（観ていた時間）と学習の関係は、この論文では測られていない。後続の研究で、6 分以下の動画で学習が上がるかを実験したものはあるか
- 長さの効果は、長い動画ほど中身が多い・計画が雑、という交絡を除けていない（著者も示唆）
- 同じデータを動画の中の秒単位で見た続編が [[web-kim-2014-in-video-dropouts]]（長さと離脱、画面の切り替わりと観直しの山）
- 2012 年の edX の理系 MOOC から、日本語の YouTube 解説・講演への埋め込みへ、どこまで一般化できるか
- 話す速さの「速いほど観られる」は英語の講師の肉声で、合成音声（[[exp-galleria-tts-and-singing]]）で同じかは分からない
- Brame (2016) はこの論文から「6 分以下なら視聴時間の中央値はほぼ 100%、9〜12 分は約 50%、12〜40 分は約 20%」と書くが、Guo の本文にこの数値はなく、図 2 からの読み取りと思われる（[[web-brame-2016-effective-educational-videos]]）
