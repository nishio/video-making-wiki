---
type: analysis
summary: MacBook と galleria での動画制作の経験（2026-08〜10、24 ページ）から、制作を横断して効きそうな教訓を工程ごとに並べたもの。各項目は経験 1〜数件からの抽出で、一般則として検証したものではない
video_types: [any]
sources:
  - exp-*.md（2026-11-09 の抽出。各項目に出典）
---

# 制作経験から横断して効きそうな教訓（2026-11 時点）

2026-11-09 に 5 つの担当が `sources/exp-*` を書いたときの横断の教訓を、重なりをまとめて工程ごとに並べた。
**どれも 1〜数件の経験から出たもので、一般則として確かめてはいない。** 文献と照らすのはサーベイ（`sources/web-*`）の仕事。型ごとの違いは [[three-video-types]]。

## 企画・宛先

- 宛先を先に決め、そこから「出さない語」と「必ず答える問い」を導く。作った側の用語（「268群」など）は見る人には分からない（talk/any。[[exp-llm-wiki-explainer-series]]、[[exp-gyazo-resumption-video]]）
- 二言語を併記すると宛先も二つになる。誰向けの論証かを先に決める（promo。[[exp-words-as-public-goods-video]]）
- 台本を書く前に、同じ宛先に向けて前に作った説明を読む。1 分解説の台本案は、売り文句が西尾の LT の結論と逆だった（talk。[[exp-llm-wiki-explainer-series]]）
- 作業の順に数字を並べると作業報告になる。主役（モデル名と実測）を決めて、そこに尺を割く（promo。[[exp-gyazo-resumption-plan-galleria]]、[[exp-gyazo-resumption-video]]）
- 題材の構造をそのまま演出と曲の構造に当てる。注釈より構造で推察させる（promo/embed。[[exp-sutra-hype-editions]]）

## 台本と音

- 画面に出す文と読み上げる文を分ける（「空→から」など）。読みは通し視聴で耳で拾う（any。[[exp-qualia-video]]、[[exp-galleria-tts-and-singing]]）
- 合成音声に台本を読ませて尺を測る。字幕用の 60 秒の台本にナレーションを付けたら約 107 秒になった（talk/any。[[exp-lt-20260909]]、[[exp-democracy-river-video]]）
- 時間の調整は可変長の部分に集め、削る順を先に決めておく。前半の話を終盤で回収し、終盤に新しい要素を入れない（talk。[[exp-lt-20260909]]）
- 低域だけの太鼓はスマホのスピーカーで聞こえない。声の埋もれは声あり／なしの帯域差で測る（any。[[exp-sutra-hype-editions]]、[[exp-sutra-voicevox-singing]]）
- 声の license が台本の言い回しを縛ることがある（ACML 1.0 の声に他製品の批判を読ませない）（any。[[exp-qualia-video]]）

## 画面

- 映像と音で同じ時刻表を使う。場面の切り替えを 120BPM の小節頭に置くと、合わせる作業がほぼ要らない（any。[[exp-html-capture-pipeline]]）
- 描画はフレーム番号（時刻）だけの純関数にする。好きな秒の静止画やコンタクトシートで確かめてから全編を書き出せる（any。[[exp-html-capture-pipeline]]、[[exp-polis-magi-op]]）
- 描画が軽いほど作り直せる回数が増える（粒子の描画は 1 分に約 10 分、文字だけの描画は 47 秒を約 38 秒）（any。[[exp-html-capture-pipeline]]）
- 図形と文字だけで描けば、権利の確認も private な画面の映り込みも要らない。写真を使うと手間が一気に増える（promo/any。[[exp-nishio-showreel]]、[[exp-words-as-public-goods-video]]）
- 生成モデルに文字を描かせず、字幕・ロゴは後から合成する（any。[[exp-local-scene-studio]]、[[exp-qualia-video]]）
- 飾りの絵より、実画像・工程・比較といった証拠に画面の面積を配る（talk。[[exp-qualia-video]]）
- 様式を借りるときは、文章の記述でなく実物を見て、カットの密度を測って合わせる（4.5 秒 → 1.07 秒）（promo。[[exp-polis-magi-op]]）
- フォントの欠字は fontTools の cmap で全字照合する（any。[[exp-sutra-hype-editions]]）

## 生成モデル（galleria の RTX 5080 16GB での実測）

- 動画モデルは静止画で keeper を選んだ後の下流工程に置き、prompt の改良で動きを取り戻そうとしない（any。[[exp-galleria-local-video-generation]]）
- 両端固定（FLF2V）では質は keyframe 対で決まる。別々に生成した 2 枚は中央で切り替わるだけになる（any。同）
- 口だけ直す道具を、演技を作る道具の代わりにしない。検査できる正しさを上げた版より、最初の一体生成の版の方が魅力があった（embed?。[[exp-qualia-h3-live2d-galleria]]）
- 外部のオンラインサービス頼みの工程は、登録や画像の送信で止まる。ローカルで完結する経路を先に確かめる（any。[[exp-puppetloom]]）

## 検証とレビュー

- 全編を作る前に、一節・一問の短尺（15〜30 秒、動きなら 4 秒の A/B/C）を本人に見せて選んでもらう。自動化は誤りを全編に複製する。動きが大事な版は静止画では評価できない（any。[[exp-sutra-sync-subtitles]]、[[exp-sutra-hype-editions]]、[[exp-qualia-video]]）
- 機械の QA（Whisper の一致、音程の %）は足切りにしか使えない。Whisper の一致は音程を見ない。人の評価を別の合格条件にする（any。[[exp-polis-magi-op]]、[[exp-galleria-tts-and-singing]]、[[exp-qualia-video]]）
- AI が記憶から作ったもの（メロディ）は未検証として公開前の止め札にする（any。[[exp-polis-magi-op]]）
- TTS や ASR の推定を表示ルビや本文の根拠にしない。自動字幕は年号・単位・固有名詞を間違える。画面に出す数字と役割語は一次ソースで確かめる（any。[[exp-sutra-sync-subtitles]]、[[exp-democracy-river-video]]、[[exp-forest-misc-video-notes]]、[[exp-nishio-showreel]]）
- 画面に出す比較は、実務で置き換えた相手と同じ条件で測る（any。[[exp-gyazo-resumption-video]]）
- レビューの道具を「1 行聞く → ここが変と言う」の流れに合わせる。人に直してもらう初稿は作り込まず、AI が補った所を末尾に並べる（any。[[exp-sutra-songs-on-music]]、[[exp-sutra-voicevox-singing]]、[[exp-lt-20260909]]）

## 配信

- 配信面の操作は助言で渡さず成果物に焼き込む。X では最初のコマがサムネイルになるので動画の頭に焼き込む（promo。[[exp-democracy-river-video]]、[[exp-forest-misc-video-notes]]）
- 無音自動再生の場では字幕だけで話が通じるようにする（promo。[[exp-words-as-public-goods-video]]、[[exp-democracy-river-video]]）
- 作り直した版はファイル名を変えて渡す。同じ名前で上書きすると相手のキャッシュで古い版が出る。秒は pts から取り、VFR の素材は CFR に直す（any。[[exp-galleria-ffmpeg-measurement-and-delivery]]）
- 「AI」とぼかさずモデル名と実測を出す（promo。[[exp-gyazo-resumption-video]]。grasp-nishio の決まり name-the-model-not-ai）
- 別版はサムネイルの言葉・配色・帯で区別する（promo。[[exp-sutra-videos-overview]]）

## 実測の反応（数が少ないので参考）

- YouTube で、解説形式（v1 4 視聴・v2 23 視聴）より「一緒に唱える」形式が残った（[[exp-forest-misc-video-notes]]）。題材に固有かもしれない

## Open Questions

- ここに並べた教訓のうち、文献（マルチメディア学習の原則、SNS 動画の実務の知見）と食い違うものはどれか
- embed の経験が無いので、embed に固有の教訓はまだ出ていない
