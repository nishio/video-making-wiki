---
type: concept
summary: 西尾の見立て「プロモーションムービー風・解説プレゼン風・プレゼンに埋め込む特定概念の解説は別」を、制作経験から何が言えるかで埋めていくページ。経験の範囲では、型を分けているのは中身より「どこで流すか」に見える。embed の経験はまだない
video_types: [promo, talk, embed]
sources:
  - origin-2026-11-09.md
  - exp-*.md（2026-11-09 の抽出。個々の出典は本文）
---

# 動画の三つの型

起点は西尾の見立て（[[origin-2026-11-09]]）:

> プロモーションムービー風のやつと、解説プレゼン風のやつと、プレゼンの中に埋め込んで使う特定概念を解説するものとはそれぞれ別だよな感はある

ここに書くのは、2026-11-09 に MacBook と galleria の制作経験（`sources/exp-*`）から抽出した範囲で言えること。文献の側はサーベイ（`sources/web-*`）で足す。型に依らない教訓は [[experience-lessons-2026-11]]。

## 経験の内訳

| 型 | 経験 | 主な出典 |
|---|---|---|
| promo（プロモーションムービー風） | 多い。showreel（15 秒・60 秒・縦長）、講演 → X 用 60 秒、Gyazo 配信再開 47 秒、Words as Public Goods 50 秒、Polis の OP 様式 55 秒、般若心経のアゲアゲ版・漢字版、切り抜きショートの下書き生成 | [[exp-nishio-showreel]]、[[exp-democracy-river-video]]、[[exp-gyazo-resumption-video]]、[[exp-words-as-public-goods-video]]、[[exp-polis-magi-op]]、[[exp-sutra-hype-editions]]、[[exp-shortmovie-draft-generator]] |
| talk（解説プレゼン風） | クオリアさん解説 3 本（93 秒・109 秒・6 分 33 秒）、8 分の LT の準備、LLM Wiki 1 分解説シリーズ（構想と台本案で止まっている） | [[exp-qualia-video]]、[[exp-lt-20260909]]、[[exp-llm-wiki-explainer-series]] |
| embed（プレゼンに埋め込む特定概念の解説） | 直接の経験は見つからなかった。近いのは般若心経の同期解説（45 秒・ナレーションなし・3 回反復。講演に埋め込んだ実績はない）、H3 の数秒の台詞 shot、4 秒の動きの A/B/C 比較 | [[exp-sutra-sync-subtitles]]、[[exp-qualia-h3-live2d-galleria]]、[[exp-qualia-video]] |

## 経験から言えそうなこと

### 型を決めたのは流す場所だった

- Gyazo 配信再開の動画は、中身は作業の経緯の解説（talk 寄り）だったが、X に流すことと西尾の「ドーパミンアゲアゲ動画にして」で、47 秒・120BPM の叩き込み文字（promo の形）に作り直した（[[exp-gyazo-resumption-video]]）
- 講演 34 分 → 60 秒でも、作りを決めた制約の多くは講演の中身ではなく配信面（無音自動再生、最初のコマがサムネイル、チャプターの長さ）から来た（[[exp-democracy-river-video]]。llm-wiki の考察「講演の短尺動画化では制約は配信面から来る」と同じ見方）
- 1 本 1 概念の 1 分シリーズは、talk でも embed でもあり、X に出せば promo の制約も受ける。一本の動画が複数の型にまたがりうる（[[exp-llm-wiki-explainer-series]] の抽出者の見立て）

ここから、三つの型を分ける軸は「視聴の場」——流れてくる場（SNS）／見に来た場（YouTube の解説・講演そのもの）／講演の中で話し手が流す場——ではないか、という仮説が立つ。検証はしていない。

### 何が主導するかが違った

| | promo | talk |
|---|---|---|
| 主導するもの | 音楽と拍。120BPM の小節頭で場面を切り替える（[[exp-html-capture-pipeline]]） | ナレーション。耳で分かる量まで台本を削る（[[exp-qualia-video]]） |
| 動き | 変化が止まるとテンションが下がる。静止・出しっぱなしは下げた（[[exp-sutra-hype-editions]]、[[exp-polis-magi-op]] の「死んだ拍」） | 完全静止を既定にし、説明中の語・数値だけを強調する。画面全体の drift は「気持ち悪い」と評価された（[[exp-qualia-video]]） |
| 音 | 無音で自動再生される前提で、字幕だけで通じるようにする（[[exp-words-as-public-goods-video]]、[[exp-democracy-river-video]]） | 音声が前提。画面に出す文と読み上げる文を分ける（[[exp-qualia-video]]、[[exp-galleria-tts-and-singing]]） |
| 冒頭 | 最初の 1〜2 秒と最初のコマ（サムネイル）が勝負（[[exp-shortmovie-draft-generator]]、[[exp-democracy-river-video]]） | 冒頭 1 分で目的・失敗・見終わったらできることを示す（[[exp-qualia-video]]） |
| 数値 | 尖った一点（モデル名と実測）だけ。正確さの条件は概要欄へ（[[exp-gyazo-resumption-video]]） | 耳で数値を覚えさせない。細かい数値は読み上げず wiki や概要欄へ（[[exp-qualia-video]]） |

同じ「動き」の評価が promo と talk で逆向きになった点は、型を分ける根拠の一つになりそう。

### embed について経験から推せること（未検証）

- 般若心経の同期解説は「音・文字・意味を同じ瞬間に光らせる」ことを核に、ナレーションと導入を削った 45 秒だった（[[exp-sutra-sync-subtitles]]）。話し手が横にいる場で流すなら、ナレーションが無いことはむしろ合うかもしれない
- talk の LT の工夫（円環、可変長の「散弾」、削る順）は、持ち時間の決まった生の発表から来ている（[[exp-lt-20260909]]）。embed はその発表の中の部品なので、尺は発表の側が決める

## Open Questions

- 三つの型を分ける軸は「視聴の場」で足りるか。目的（興味を引く／理解させる／一つの概念を渡す）とどう重なるか
- embed の動画で、話し手のナレーションと動画の音（BGM・TTS）はどう共存させるべきか。ループさせるか、止めて話すか
- アゲアゲ版は「見て上がる」つもりが、西尾には「このテンポで唱えられるか」という挑戦として届いた（[[exp-sutra-hype-editions]]）。見る人が参加できる問いになることは promo 一般に効くのか、唱える題材に固有か

## Updates

### 2026-11-09 ネット上の知見のサーベイ（`sources/web-*` 37 ページ）から

型ごとの詳細は [[promo]]・[[talk]]・[[embed]]。道具は [[video-tools-comparison]]、音は [[narration-bgm-sound]]。サーベイ全体のまとめは [[survey-2026-11-summary]]。

#### 軸ごとの違い（文献と経験から。暫定）

| 軸 | promo | talk | embed |
|---|---|---|---|
| 視聴の場 | フィードで流れてくる。スクロールで離脱 | 見に来る（YouTube の解説）。視聴者が止められる | 会場で話し手が流す。聴衆は止められない（システムペース） |
| 尺 | 広告は 6〜15 秒の推奨（[[web-x-video-ads-best-practices]]、[[web-meta-video-ads-best-practices]]）。Wistia は 1 分未満に置く（[[web-wistia-video-length-engagement]]） | Wistia は 1〜5 分。Guo の 6 分は視聴の観察で学習でない（[[web-guo-2014-video-production-engagement]]）。Common Craft は 3 分以下 425〜525 語 | 発表が決める。文献に数値は無い |
| 音 | 面ごとに違う。X のタイムラインは無音への備え、YouTube・TikTok・Reels は音あり前提（[[web-digiday-2016-85-percent-sound-off]]） | 音声が前提（modality 原則はこの前提の上。[[web-mayer-multimedia-principles]]） | 話し手の声が主。スライドソフトの既定と Rosling 型からは、動画は無音か小さく（[[web-roslingifier-data-presentations]]、[[web-powerpoint-keynote-google-slides-video-playback]]） |
| 冒頭・構成 | 最初の 3 秒（各社）。ブランドを早く | Why → How（Common Craft）、30 秒で動機（SoME）、誤概念を先に述べて否定（[[web-muller-2008-misconceptions]]） | 先に見方を言う → 始める時を告げて流す → 動いている最中に意味を語る（Rosling 型） |
| 動き | 文献に直接の記述は少ない。経験では「変化が止まると下がる」 | 飾りを除き、説明中の要素を指し示す（coherence・signaling、Sanderson） | 中身の変化を見せる動きだけ効く。抽象的・記号的な表現のアニメは効果が見られなかった（[[web-berney-betrancourt-2016-animation-meta-analysis]]） |
| 測るもの（文献の） | 広告の想起・ブランド指標 | 視聴維持（業界）、保持・転移（研究） | 保持・転移（研究）。発表の場での測定は無い |

#### 仮説「型を分ける軸は視聴の場」への文献の反応

- 実務家も「目的と置き場所」で分けている（Wistia の目的別の長さ、Yum Yum の「置かれる場所が視聴者の意図を変える」。[[web-wistia-video-length-engagement]]、[[web-yum-yum-videos-explainer-script]]）
- Sanderson の「Know your genre」は語り手の役（学生・専門家・先生・記者）で切り、「役が違えばテンポと様式が違う」と書く（[[web-3blue1brown-exposition-advice]]）。軸は違うが「型が違えば作りが違う」という結論は同じ
- 研究の側では、「誰がペースを握るか」（システムペースか学習者ペースか）で設計原則の効き方が変わる（[[web-mayer-multimedia-principles]]）。embed（話し手が握る）と talk（視聴者が握れる）を分ける軸として、視聴の場より具体的に効きそう
- 「動き」の評価が promo と talk で逆向きになった経験は、文献からは「promo の測度（注意・想起）と talk の測度（学習）が違う」ことで説明できる。promo の動きを学習の測度で評価した文献は無い

#### Open Questions（追加）

- 三つの型を分ける軸の候補は「視聴の場」「目的（測るもの）」「誰が時間を握るか」「音が主か」。どれが独立でどれが従属か
- embed の文献の答えは「話し手が時間を握る」。西尾の言う「プレゼンの中に埋め込んで使う」動画が、話し手が操作する前提なのか、流しっぱなしの前提なのかを西尾に確かめる
