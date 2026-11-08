---
type: analysis
summary: 2026-11-09 のネット上の知見のサーベイ（sources/web-* 37 ページ）のまとめ。何が分かったか、三つの型の違いについての暫定の答え（視聴の場・測るもの・誰が時間を握るか・音が主か）、経験と文献の食い違い、次に調べること
video_types: [promo, talk, embed]
sources:
  - web-*.md（37 ページ。各項目に出典）
  - exp-*.md
---

# ネット上の知見のサーベイのまとめ（2026-11-09）

起点の問い（[[origin-2026-11-09]]）の 6 つ（三つの型の違い、解説動画の構成、短いアニメで一概念、SNS の短い promo、道具と LLM、音）を、6 つの担当に分けて読んだ。37 ページ。横断の整理は [[three-video-types]]（Updates）、[[promo]]、[[talk]]、[[embed]]、[[video-tools-comparison]]、[[narration-bgm-sound]]。

**根拠の強さについて**: promo の文献はほぼすべてプラットフォームの広告販売の資料と自社顧客データの業界調査で、査読のある研究は見つからなかった。talk・embed の研究は学習（保持・転移）を測っていて、多くは学生の実験。どれも「〜と書いている」以上には扱っていない。原典を読めずに抄録や二次の要約で書いたものは各ページに明記した（下の「読めなかったもの」）。

## 何が分かったか

1. **Mayer の原則の効果量は、独立したメタ分析のおよそ 1.5〜3 倍**（modality 1.00 対 g=0.38、補正後 0.20 など）。原則は向きとしては支えられるが、大きさは小さめに読む（[[web-mayer-multimedia-principles]]）
2. **設計原則は、システムがペースを決める教材と複雑な教材でよく効く**（g=0.41 対 0.27、0.70 対 0.20）（同）
3. **アニメは中身の変化を見せるときだけ効く**（表現的 d=0.40、装飾的 ≈0）。抽象的・記号的な表現のアニメは効果が見られず（g=0.006）、文字を添えないアニメ（g=0.89）とナレーションと組むアニメ（g=0.32）で効いた（[[web-berney-betrancourt-2016-animation-meta-analysis]]）
4. **誤概念を先に述べて否定する解説は、簡潔な講義形式より伸びが大きかった**（物理の学生 364 人、0.79〜0.83）（[[web-muller-2008-misconceptions]]）
5. **「6 分」も「85% 無音」も、言われ方より弱い**。6 分は MOOC の視聴の中央値の観察で学習ではない（[[web-guo-2014-video-production-engagement]]）。85% は 2016 年に 3 社が記者に語った自社の数字（[[web-digiday-2016-85-percent-sound-off]]）
6. **音あり前提か無音前提かは面ごとに違う**。X のタイムラインは無音への備え、YouTube・TikTok・Reels は音あり前提。どの面も字幕と「最初の 3 秒」は勧める（[[promo]]）
7. **embed の答えはループでなく「話し手が時間を握る」形**（Rosling 型: 先に見方を言う → 始める時を告げて流す → 動いている最中に意味を語る）。スライドソフト 3 つと Motion Canvas の presentation mode の既定もこの向き。ただしループとの比較実験は無い（[[embed]]）
8. **道具の多くは西尾の方式と同じ「フレーム番号の純関数」を要求する**（Remotion は並列化のため）。Remotion は 4 人以上の営利組織で Company License が要る（[[video-tools-comparison]]）
9. **LLM のエージェントの失敗の型は「存在しない API」「LaTeX」「重なり」**。VLM に描いた絵を見せると改善するが、人間の方が重なりに敏感（VLM 採点 90.6 対 人間 60.2）（[[web-theoremexplainagent-code2video-visualedu]]）
10. **ラウドネスは配信で −20〜−16 LUFS、声に対して音楽は少なくとも 10 LU 下げる**。BGM が学習を妨げるかは研究が割れている（[[narration-bgm-sound]]）

## 三つの型の違いについての暫定の答え

西尾の見立て「それぞれ別だよな感」は、文献からも支えられる。ただし分けている軸は一つではない。

| | promo | talk | embed |
|---|---|---|---|
| 視聴の場 | 流れてくる | 見に来る | 話し手が会場で流す |
| 誰が時間を握るか | 視聴者（スクロールで離脱） | 視聴者（止められる） | 話し手（聴衆は止められない） |
| 音が主か | 面による。字幕で通じることが前提 | ナレーションが主 | 話し手の声が主。動画は無音か小さく |
| 文献が測るもの | 広告の想起 | 視聴維持・学習 | 学習 |
| 構成の型 | 最初の 3 秒 | Why → How、誤概念を先に | 見方を先に言う → 流す → 語る |

- 経験のページで立てた仮説「型を分ける軸は視聴の場」（[[three-video-types]]）は、実務家の分け方（目的と置き場所。Wistia・Yum Yum）と同じ向き
- 文献から足せる軸は **「誰が時間を握るか」**。研究の「システムペース／学習者ペース」がそのまま当たり、embed と talk を分ける。embed の作り方（ナレーションを入れない、止める位置を作る）もこの軸から出てくる
- **「何を測るか」** の違いで、経験の「動きの評価が promo と talk で逆」が説明できる。promo の動きを学習で測った文献も、talk の静止を注意で測った文献も無いので、どちらも「逆の評価になる理由の候補」で止まる
- 一本の動画が複数の型にまたがりうる、という経験の見立て（[[exp-llm-wiki-explainer-series]]）は、文献では扱われていない

## 経験と文献の食い違い

| 経験 | 文献 | 扱い |
|---|---|---|
| 画面に出す文と読み上げる文を分ける（[[exp-qualia-video]]） | redundancy は割れている。独立のメタ分析は音声に文字を足すと g=0.29（[[web-mayer-multimedia-principles]]） | 経験は字幕を残しているので直接の矛盾ではない。字幕を消す根拠は文献から弱い |
| 字幕を焼き込む | アニメは文字を添えない方が効いた（g=0.89）（[[web-berney-betrancourt-2016-animation-meta-analysis]]） | embed で話し手が話すなら字幕は要らない、と読める。未検証 |
| 冒頭に問い、答えと名前を最後に回収（[[exp-words-as-public-goods-video]]） | 「ブランドは早く」（各社） | 目的（最後まで見させる）と測度（想起）が違う |
| 全部コードで同期（時刻表・TTS 区間） | Sanderson「同期は動画編集ソフトで」（[[web-manim]]） | エージェントに回させる前提の違い |
| 声と BGM を sidechaincompress で分ける | 少なくとも 10 LU（[[web-torcoli-2019-background-ducking]]） | 経験の差の実測が無い。既定の ratio 2 では足りない可能性 |
| −16 LUFS で書き出し、LRA=11 | 話し言葉は −18 寄り。短尺では LRA は不適用（[[web-ebu-r128-itu-bs1770]]） | 誤りではないが大きめの側。LRA の指定は効いていない可能性 |
| 縦長 60 秒以内ならショート（[[exp-html-capture-pipeline]]） | 2024-10-15 以降は 3 分以内（[[web-google-youtube-abcds]]） | 経験ページの事実が古い |
| 60fps で X に出した（[[exp-gyazo-resumption-video]]） | X のウェブからのアップロードは 40fps まで（[[web-x-video-ads-best-practices]]） | 実際の挙動は未確認 |
| 1 分解説の台本案「放り込むだけ」（[[exp-llm-wiki-explainer-series]]） | 誤概念を先に述べて否定する型（[[web-muller-2008-misconceptions]]） | 西尾の LT の結論と逆だった台本案は、Refutation 型で書き直せる。未検証 |
| AI の台本・TTS の声で解説を作っている | SoME は AI の台本・ナレーション・AI の声を不可にしている（[[web-3blue1brown-exposition-advice]]） | 規範の違い。発信先ごとに開示の扱いを決める |

## 読めなかったもの・弱い根拠

- Mayer 2008・2017・2021 の本、Mayer, Fiorella & Stull 2020 "Five ways…"、Höffler & Leutner 2007 の本文、Muller の JCAL・Sci Ed の本文、Torcoli 2019 の本文、voice principle の追試の多く（abstract のみ）
- Noetel ら 2022 は第三者が置いた出版版の写しで読んだ
- Meta・X の公式ページは本文が取れず Internet Archive の保存版で読んだ。Verizon Media・Publicis 2019 の報告書の本体は未読
- YouTube の文字起こし（Sanderson・Veritasium・Kurzgesagt の動画）は取れなかった
- 日本語の解説動画の制作者が書いた一次資料は見つけられなかった

## 次に調べること

1. **西尾に確かめる**: 「プレゼンの中に埋め込んで使う」動画は、話し手が操作する前提か、流しっぱなしの前提か。これで embed の作り方（ナレーションの有無、止める位置）が決まる
2. **embed を一本作ってみる**: 経験が無い型なので、Rosling 型（ナレーションなし、止める位置あり）で一概念を作り、発表で流して比べる。Motion Canvas の presentation mode と mp4 をスライドに貼る方式の比較も兼ねる
3. 抽象的・記号的なアニメが効かなかった（g=0.006）ことと 3Blue1Brown の関係を、Berney & Bétrancourt の原典の分類で確かめる
4. 経験の方式の計測: 粒子系 1 分約 10 分の内訳（描画か PNG 受け渡しか）、声と BGM の LU 差、YouTube の参照レベル（Stats for nerds）
5. 日本語の TTS（VOICEVOX・AivisSpeech など）で voice principle を測った研究、日本語の解説動画の制作論
6. 経験ページの古い事実（Shorts の長さ）を exp- 側に Updates で反映する

## Open Questions

- 三つの型を分ける軸のうち、「視聴の場」と「誰が時間を握るか」と「測るもの」のどれが独立でどれが従属か
- promo の文献がほぼすべて広告販売の資料であることを、この wiki ではどこまで参考にするか

## Updates

- 2026-11-09: 取りこぼしの経験 [[exp-thinklet-reading-demo-video]]（52 秒、ナレーション入り、LT に組み込む候補）が入った。「次に調べること」の 1 は、まずこの動画を 9/9 か 10/2 の LT で流したか、流したならナレーションをどうしたかを西尾に確かめるのが早い。embed への当てはめは [[embed]] の Updates

- 2026-11-09: 「次に調べること」の 1 に西尾が答えた: embed は**流しっぱなしの前提**。THINKLET の動画も流しっぱなしで流した。上の表の embed の「誰が時間を握るか: 話し手」と「構成の型: 見方を先に言う → 流す → 語る」は、西尾の embed には当たらない（[[embed]] の Updates）
- 2026-11-09: 経験側に [[exp-timeline-2026]]（Opus 5.5 の公開前後の時系列）、文献側に [[web-movez-opus-motion-design-course]]・[[web-taelin-bend-nge-feedback]]（tweet-memo から。当時の流行の作り方と人間側のフィードバック）を足した
