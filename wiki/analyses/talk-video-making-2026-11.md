---
type: analysis
summary: 解説動画（talk）を、台本 → 事実確認 → 声 → 時刻表 → 描画 → 引用の重ね → 検査 → レビューの受け取り → 公開の順に作る手順。2026-11-09 に同じ作りで作った 3 本（本編「動画の作り方 2026年11月」、プロセス動画、tsugigami のメイキング）の作業場のファイルから書いた。各手順に、どの動画のどのファイルで確かめたかと、何本で確かめたかを付ける。各段に、wiki の経験のページから集めた「踏んだ失敗と直し方」（起きた・気づいた・次は・出典）を寄せ、直したらその場で一行足す。skill video-making から最初に読まれるページ
video_types: [talk]
sources:
  - Mac の ~/video-making-explainer、~/video-making-process、~/tsugigami-promo/making のテキストの写し（CyEC2 の ~/handoffs-from-mac/2026-11-09-talk-materials/。音・映像・画像・out/ は写していない）
  - 同 gitlog/（video-making-explainer 25 commit、video-making-process 9 commit の git log --stat、tsugigami-promo/making のファイル時刻）
  - exp-explainer-video-2026-11.md、exp-tsugigami-making.md、exp-tsugigami-promo.md、exp-html-capture-pipeline.md、exp-galleria-tts-and-singing.md
  - explainer-script-factcheck-2026-11.md
  - 踏んだ失敗と直し方: exp-galleria-ffmpeg-measurement-and-delivery.md、exp-qualia-video.md、exp-gyazo-resumption-video.md、exp-democracy-river-video.md、exp-sutra-sync-subtitles.md、talk-three-videos-2026-11.md、experience-lessons-2026-11.md
---

# 解説動画（talk）の作り方 — 3 本で使った手順（2026-11）

西尾の問い「このWikiってビデオを作るHowについてはどれくらい書いてある？」への答えが「型ごとのページは文献と経験の並べで、この順で作るという一本の手順が無い」だったので、2026-11-09 に作った解説動画 3 本の作業場のファイルから手順を書いた（Mac の Claude からの依頼、2026-11-09）。

| 略 | 動画 | 作業場（Mac） | 経験のページ |
|---|---|---|---|
| 本編 | 「動画の作り方 2026年11月」6:36 https://youtu.be/IDkRFwiFXFI | ~/video-making-explainer | [[exp-explainer-video-2026-11]] |
| プロセス | 「「動画の作り方」の作り方」5:51 https://youtu.be/Ezzcld2rbL8 | ~/video-making-process | [[exp-explainer-video-2026-11]] の「プロセス動画」 |
| メイキング | tsugigami の広告動画のメイキング 6:40 https://youtu.be/aXGEaLMI7Fs | ~/tsugigami-promo/making | [[exp-tsugigami-making]] |

3 本の比較（使い回せたもの、毎回直しが入った所）は [[talk-three-videos-2026-11]]。

## 読み方

- **このページは、Mac で作る skill「video-making」から最初に読まれるページになる**（西尾の決定、2026-11-10）。動画を作り始める前に、これから作る段の **踏んだ失敗と直し方** を読む
- **決まり: 失敗に気づいて直したら、その場で該当の段の「踏んだ失敗と直し方」に一行足す。** 形は「起きた: 何が起きたか。気づいた: どう気づいたか。次は: 次はどうするか（出典ページ）」。出典は経験のページ（sources/exp-*）か作業場のファイル・commit。気づき方の記録が無ければそう書く。talk 以外の型（promo・embed）で踏んだ失敗でも、段が同じならここに足す
- 共通のコードベースは持たない（西尾の決定、2026-11-10: 動画ごとにやりたいことが違い、保守の手間が大きい）。動画どうしで共有するのは「失敗に気づいて直した知見」で、コードは前の作業場から写してその動画に合わせて変える
- 各手順の **確かめた** は、作業場のファイル・commit・README にその記録があること。〔3 本〕〔2 本〕〔1 本〕は、その手順を何本で使ったか。〔1 本〕のものは一般化していない
- **意図** は、ファイルのコメントや台本に書いてある設計の意図で、効果を測ったものではない
- **文献** は、この wiki の web- ページの主張で、この 3 本で検証したものではない
- パスは Mac の作業場からの相対。手順とコマンドは写しの実物から書いた。写しに無いことは書いていない
- 3 本とも Claude Opus 5.5（Claude Code）が書いて回した。人（西尾）がしたのは、決めること・見て直しを言うこと・YouTube Studio での投稿

## 全体の形

```
script-draft.md      台本（> の行がナレーション）
tts/lines.json       行ごとに id・caption（画面の字幕）・narration（読ませる文）
tts/synth.py         AivisSpeech「まお」で 1 行 1 wav → tts/wav/<id>.wav
src/build_timeline.py wav の実際の長さから時刻表 → src/timeline.js・out/overlays.json・out/concat.txt
src/explainer.html   1920×1080・30fps の canvas に renderFrame(f) で描く（字幕も）
src/capture.mjs      headless Chrome で 1 コマずつ撮る → out/video_noaudio.mp4
compose.py <版>      引用の映像を枠に重ね、ナレーションを -14 LUFS で載せる → out/<名前>_draft<版>.mp4
youtube/UPLOAD.md    投稿の設定・タイトル・説明欄
```

描いて撮る骨格は 2026-09 の [[exp-html-capture-pipeline]] と同じ。違うのは、BGM でなくナレーションの長さが時刻表を決めることと、引用の映像を canvas でなく ffmpeg で重ねること。

本編だけは一続きの make.sh がある〔1 本〕:

```sh
./make.sh 2   # galleria の wav を scp で持ち帰る → build_timeline.py → capture.mjs video → compose.py 2 → スマホ用
```

（[[exp-explainer-video-2026-11]] によると、古い wav のまま書き出した事故（二回目）のあとに作った。プロセス・メイキングの作業場には無い）

---

## 1. 台本

事例: Gyazo の 47 秒（作業報告をやめて主役を決めた）、クオリアさんの解説動画（細かい数値を読み上げない）（[[nishio-works]]）

**やること**
- script-draft.md の冒頭に、西尾が決めたこと（型・見る人・声・出す先）を原文で書き、節ごとに **画面**（映すものの案）と **ナレーション**（`> ` の行）を書く。本編は各主張の後ろに `[ ]` で出典の wiki ページを書いた
- 末尾に「西尾に決めてほしいこと」を番号で並べ、決まったら打ち消し線と西尾の原文を書く（本編・プロセスの script-draft.md）
- 尺は字数から見積もる

**確かめた**
- 〔3 本〕script-draft.md の形（本編 2ac02f1、プロセス 32015d2、メイキング script-draft1.md）。メイキングは画面の案を【画面】の行にした
- 〔2 本〕尺の見積もりと結果: 本編は「約 6 分（ナレーション 1,666 字。1 字を 1.3〜1.5 モーラ ÷ 6.5 モーラ／秒）」→ 公開版 6:36。メイキングは「43 行、5〜6 分の見込み（1 秒に約 6.5 字）」→ 6:40。どちらも見込みより長く出た。行間（0.45 秒）・節の間（1.2 秒）・頭と終わりの無音を見込みに入れていない
- 〔1 本〕本編の一回目のナレーションは 33 行・発話 297 秒（cb02e9a）

**文献**
- 尺は 6〜7 モーラ／秒で見積もれる（[[web-check-ja-speech-rate-mora]]）。台本の骨格（なぜ → どうやって、最初の 30 秒で見る理由）は [[talk]]

**踏んだ失敗と直し方**

- 起きた: wiki の語「時計」（ナレーションが時計）を台本の中心に置いた。気づいた: 西尾「「時計は」という表現は不自然なのでダメ」。次は: wiki や作業の中の語・比喩を台本の中心語にしない。平易な言い方に開く（[[exp-explainer-video-2026-11]]）
- 起きた: 「編集は人がしても、AI にさせても構いません」と一般論で書いた。気づいた: 西尾「情報がない」。次は: この動画自身の具体例で言う（[[exp-explainer-video-2026-11]]）
- 起きた: プロセス動画に経過時間、「AI が間違えたこと」の節、機械の製品名を入れた。気づいた: 西尾「8時間の大部分は人間が寝てたから紹介すべきではない」「無益なのでこのセクション削れる？」「MacBookはMacBookである必然性がなければ「普段使いのラップトップ」とかで」。次は: 内輪の事情は出さない。失敗は失敗談でなく手順として書く。機械は役割で書く（[[exp-explainer-video-2026-11]]）
- 起きた: 作業の順に数字を並べて作業報告になった。気づいた: 西尾のフィードバック。次は: 主役（モデル名と実測）を決めて、そこに尺を割く（[[exp-gyazo-resumption-video]]、[[experience-lessons-2026-11]]）
- 起きた: 細かい数値（version・seed・hash・codec）を読み上げた。気づいた: 人の評価「細かい数値を耳で聞くのが辛い」。次は: 細かい数値は資料に移して読まない。最初の 1 分で目的と関心を作る（[[exp-qualia-video]]）
- 起きた: 尺の見込みが 2 本とも公開の長さより約 40 秒短かった。気づいた: 公開の長さと比べて。次は: 字数からの見込みに、行間 0.45 秒・節の間 1.2 秒・頭と終わりの無音を足す（[[talk-three-videos-2026-11]]）

## 2. 事実確認

事例: 動画の作り方 2026年11月（主張 15 個を原典で）、デジタル民主主義の川 60 秒版（講演の数字を一次ソースで）（[[nishio-works]]）

**やること**
- 台本の言い切っている主張を選び、wiki のページでなく原典（公式ページ・規格・論文）を開いて確かめ、言い方を直した案の文を作る

**確かめた**
- 〔1 本〕本編: 15 の主張を CyEC2 が原典で確かめ、そのまま使えたのは 1 個（[[explainer-script-factcheck-2026-11]]、本編 b2bff79「事実確認の案の文を反映」）。説明欄の「出典」に原典の URL を節ごとに並べた（本編 youtube/UPLOAD.md）
- 〔1 本〕プロセス: 中身は自分の制作の話なので、各節の後ろの `[ ]` に一次の記録（commit・LOG・wiki のページ）を書いた（プロセス script-draft.md）。原典を開いての確認とは別
- メイキングの写しには、事実確認の記録が無い。材料は [[exp-tsugigami-promo]] の時系列（会話記録の時刻とファイル時刻）

**踏んだ失敗と直し方**

- 起きた: 「各社の広告の資料は、そろって最初の 3 秒」など、wiki のページから書いた台本の主張が原典と食い違っていた（15 個のうちそのまま使えたのは 1 個）。気づいた: CyEC2 が原典を開いて確かめた。次は: 台本の言い切りは wiki のページでなく原典で確かめ、言い方を直した案の文まで作る（[[explainer-script-factcheck-2026-11]]）
- 起きた: 自動字幕が年号・単位・固有名詞を間違えた。次は: TTS や ASR の推定を画面の字や数字の根拠にしない。画面に出す数字と役割語は一次ソースで確かめる（[[experience-lessons-2026-11]]、[[exp-sutra-sync-subtitles]]、[[exp-democracy-river-video]]）
- 起きた: タイトルで「AI」とぼかして「全部は AI に見せなかった」と書いたが、実際は 1 万枚をモデルに見せていて論理が崩れた。気づいた: 西尾の指摘。次は: 「AI」と書かずモデル名を出す（[[exp-gyazo-resumption-video]]、[[exp-html-capture-pipeline]]）

## 3. 声

事例: クオリアさん pilot（SAPI）→ makingof（AivisSpeech）、動画の作り方（三つの声の聞き比べ）、THINKLET のデモ（ずんだもん）（[[nishio-works]]）

### 3a. 声を選ぶ

**やること**
- 前に選んだ声があればそれから始める。迷うときは、台本の全行を候補の声で焼き、音量をそろえて、同じ行を声ごとに続けて聞けるようにする

```sh
python tts/compare_http.py aivis       # AivisSpeech まお → tts/compare/aivis/
python tts/compare_http.py zundamon    # VOICEVOX ずんだもん（:50021、speaker 3）
python tts/compare_build.py            # -16 LUFS にそろえ、6 行を まお→ずんだもん→Irodori の順に → out/compare/lines.m4a、全文 full_<声>.m4a
```

**確かめた**
- 〔1 本〕本編: 西尾「Aivis と VOICEVOX(ずんだもん) と Irodori とで比較したい」→ 3 つで全 33 行を焼いた（df5edd1）。西尾「まおがいいな」。Irodori の焼き方のスクリプトは写していない。比べたページ（Artifact に db）は [[exp-explainer-video-2026-11]]
- 〔3 本〕声は AivisSpeech「まお／おちつき」（speaker 888753763、speedScale 1.0・pitchScale 0.0・intonationScale 0.9）。2026-08 の比較で西尾が選んでいた声（本編 script-draft.md、[[exp-galleria-tts-and-singing]]）。プロセスとメイキングは聞き比べをせずにまおにした

### 3b. 読みを確かめる

**やること**
- lines.json は行ごとに `caption`（字幕）と `narration`（読ませる文）を分ける。誤読は narration 側の表記を変えて直す（英字・数字・一字の漢語を、かなに開く）
- 機械で二つ確かめる。合成エンジンが返す読み（拍の列）と、合成した声の文字起こし

```sh
python3 tts/kana.py     # audio_query の accent_phrases の moras をつないで「／」で句を区切る → tts/kana.json
python3 tts/asr.py      # faster-whisper large-v3（CPU、int8）で各行の wav を文字に起こす → tts/asr.json
```

- プロセス・メイキングは、台本から lines.json を作る build_lines.py に読みの表 `READ = [(表記, 読み), ...]` を持たせた

```sh
python3 tts/build_lines.py   # プロセス: script-draft.md の「> 」と「>> 」（見本の音）から。メイキング: 〔mN_NN〕の行から
```

**確かめた**
- 〔3 本〕caption と narration を分ける（3 本の lines.json）
- 〔3 本〕kana の確かめ（本編・プロセスの kana.py、メイキングは README「全行のカナは audio_query で確かめた」）。audio_query の `kana` の欄は入力をそのまま返すので使えず、moras の text をつなぐ（[[exp-explainer-video-2026-11]]）
- 〔2 本〕文字起こしの照合（本編・プロセスの asr.py・asr.json）
- 機械で見つけた誤読: 本編 H.264・2026 年・ある時刻（4f850cf・b2bff79）、メイキング 公開中・紙を継ぐ・Image 2.0（README）
- 人が聞いて見つけた誤読: プロセス 「元」をゲン → モト（198adda）、メイキング 開けば・四つの辺（README）。3 本とも、機械の確かめのあとに人が聞いて直した読みがある

**意図**
- 本編の台本の文「Claude は、作った音声ファイルを聞いて確かめることができません。そこで、合成した声を文字起こしして台本と照合し…最後は人が聞きます」（本編 review/round1-original.md の s4_05）

### 3c. イントネーションを直す（AivisSpeech）

**やること**
1. 全行のアクセント句を取り出し、高低の線をつけた札にして並べ、人に気になる札へ印をつけてもらう
2. 印のついた語ごとに、核の位置を全部変えた候補を、短い文脈の文で丸ごと焼く（句だけを切り出すと 500 になる）
3. 人が選んだ指定を書いておき、合成の前に当てる

```sh
python tts/accent.py dump                # 行ごとの audio_query → accent_queries.json
python tts/accent.py clips2 clips2.json  # {"name","text","target": 拍の文字列,"segs": [[拍数, 核], ...]} → variants/<name>.wav
python tts/accent.py show "少なくとも三通りあって、"   # 句ごとの拍と核を表示
```

- 指定の書き方は二通り。本編は行ごと（`tts/overrides.json`: `{"s0_03": [{"target": "サントオリ", "segs": [[5, 5]]}]}`、核を拍数と同じ位置に置くと平ら）。プロセス・メイキングは語ごとに全行へ当てる（`tts/word_overrides.json`: `[["サントオリ", [[5, 5]]], ...]`）。synth.py は当てた行と語を `applied` で出す

**確かめた**
- 〔1 本〕手順 1〜3 は本編で（ebf2d74・a0fb526・c69b942、494 句・18 か所・9 語・57 候補は [[exp-explainer-video-2026-11]]）
- 〔2 本〕本編で選んだ指定を、プロセスは語ごとの表にしてそのまま当てた（3d1a02c「本線の指定を同じ語に当てる」）。メイキングはその表に「グロックイマジン…」を一つの句にする 5 行を足した（読点も一拍として数える）
- 〔1 本〕効かない語がある: エフエフエムペグは三回試して指定どおりにならず、そのままにした（f26ad48、西尾「諦めよう。breakはなしで」）
- 〔1 本〕効いたかを測るときは F0 を見る。声の高さの探索範囲を声に合わせ、スペクトログラムの倍音で検算する（プロセス analysis/f0_figure_lib.py・mora_f0.py・spec_vs_measured.py。半分の高さを拾った誤りは [[exp-explainer-video-2026-11]]）

**踏んだ失敗と直し方**

- 起きた（数字・英字）: H.264 を「エイチ、ニイ、ロクジュウヨン」、2026 年、Image 2.0 を「ツウポイントゼロ」と読んだ。気づいた: kana の列と faster-whisper の文字起こし。次は: 英字・数字・小数点を含む語は、台本を書いた時点で narration 側をかなに開き、READ に入れる（[[exp-explainer-video-2026-11]]、[[exp-tsugigami-making]]）
- 起きた（漢字一字・読みの割れる語）: 「元」をゲン、「開けば」、「四つの辺」をあたり、「空」をそら。気づいた: 機械の確かめを通ったあと、人が聞いて。次は: 一字の漢字と読みの割れる語は narration でかなに開く。kana の列を人も目で読む（[[talk-three-videos-2026-11]]、[[exp-tsugigami-making]]、[[exp-galleria-tts-and-singing]]）
- 起きた: 「ホモ・サピエンス」が中黒で切れた。「Grok Imagine」が途中で区切れた。気づいた: 人が聞いて。次は: narration から中黒を除く。一塊で読ませたい語は word_overrides で一つのアクセント句にする（読点も一拍として数える）（[[exp-galleria-tts-and-singing]]、[[exp-tsugigami-making]]）
- 起きた: エフエフエムペグは核の位置を変えた候補を三回作っても指定どおりに下がらなかった。気づいた: 西尾「どれも違う」「音声あってる？」と、拍ごとの F0。次は: 候補を並べる前に、その語に指定が音へ反映されるかを短い文 1 本の F0 で確かめる。効かなければ書き方を変えるか諦める（[[exp-explainer-video-2026-11]]）
- 起きた: 声の高さの自己相関の探索上限を 360〜400Hz にして、400〜480Hz のまおの声の半分の高さを拾い「4 候補はほぼ同じ」と報告し、西尾がその言葉で台本を直した。気づいた: 測り直しで、スペクトログラムの倍音が約 450Hz と約 900Hz にあった。次は: 探索範囲をその声に合わせ、倍音で検算してから報告する（[[exp-explainer-video-2026-11]]）
- 起きた: 同じ入力でも波形が毎回少し違い、波形の差では指定が効いたかを判定できなかった。次は: F0 で見る（[[exp-explainer-video-2026-11]]）
- 起きた: アクセント句だけを切り出した query が 500 になった。次は: 短い文脈の文を丸ごと合成し、対象の句を拍の文字列で探して書き換える（`accent.py clips2`）（[[exp-explainer-video-2026-11]]）
- 起きた: Whisper の語の時刻が英字の語でずれた（「M」〜「グ」が実際は「エフエムペ」あたり）。次は: 拍の区切りはスペクトログラムと音量から読む（[[exp-explainer-video-2026-11]]）
- 起きた: 尺に入れるために SAPI の読む速さを上げた（発話 148.7 秒 → 85.8 秒）が、評価された問題は速さでなく読みと声質だった。気づいた: 人の評価。次は: 速さで押し込まない。声は全編の前に短い共通原稿で聞き比べる（[[exp-qualia-video]]）

## 4. 時刻表

事例: 動画の作り方・tsugigami のメイキング（声の長さから時刻表）（[[nishio-works]]）

**やること**
- 合成した wav の実際の長さを並べて、行ごとの開始・終了の秒を出す。音の連結リストと、描画用の時刻表と、引用を重ねる区間を同時に書き出す

```sh
python3 src/build_timeline.py   # → src/timeline.js（window.TL・DUR・CLIPS）、out/overlays.json、out/concat.txt
```

- 定数は 3 本とも `LEAD, GAP, SECGAP = 1.0, 0.45, 1.2`（頭の無音・行間・節の間、秒）。終わりの無音 `OUTRO` は本編・プロセス 6.0、メイキング 4.0。節は id の頭（`s3_01` の `s3`）で判定
- 引用・画面の切り替えは行の id で書く（`by["s5_01"]["start"]`）。台本の行を足しても秒を手で直さない
- 一行の中で項目を順に出すときは、行の頭からその語の手前までを別に合成した長さで測る

```sh
python3 tts/cues.py   # メイキング: 語の手前までの合成の長さ × (行の実際の長さ / 行全体の合成の長さ) − 0.1 → tts/cues.json
```

**確かめた**
- 〔3 本〕wav の長さからの時刻表と定数（3 本の build_timeline.py）
- 〔1 本〕行の範囲 → 画面の表 `VIS` と、行の中の語の時刻 cues.py（メイキング。西尾の直し「3 つの表示の時刻のずれ」から。[[exp-tsugigami-making]]）。AivisSpeech の audio_query はモーラの長さを返さない（0）ので、合成した長さで測った（メイキング README.md）

**意図**
- ファイル冒頭のコメント「ナレーションの実際の長さから時刻表を作る（声が時計）」。この比喩は台本では使わない（西尾「「時計は」という表現は不自然なのでダメ」、[[exp-explainer-video-2026-11]]）

**文献**
- ナレーションの実際の長さで切れ目を決める作り方は Opus 5.5 期に広く使われている（[[after-opus55]]）。Kurzgesagt は「ナレーションがアニメーションのタイミングを決める」と書く（[[web-kurzgesagt-video-process]]）

**踏んだ失敗と直し方**

- 起きた: 古い wav のまま書き出した（本編の二回目）。どう気づいたかは記録に無い。次は: 合成した wav の持ち帰り → 時刻表 → 描画 → 重ねを一続きのスクリプト（make.sh）で回す（[[exp-explainer-video-2026-11]]）
- 起きた: 一行の中で順に出す 3 つの項目が、声とずれて出た。気づいた: 西尾。次は: 語の手前までを別に合成した長さで時刻を測る（cues.py）。audio_query はモーラの長さを返さない（0）（[[exp-tsugigami-making]]）
- 起きた: 効果音の時刻を `O + 8.3` のような式で書き、正規表現で読んで空振りし、例外を握りつぶして 0 件になり、v1〜v3 で効果音が鳴っていなかった。どう気づいたかは記録に無い。次は: 時刻は値として評価して読む（node で評価する）。読めなかったら止める（[[exp-tsugigami-promo]]）
- 起きた: 字幕を読む速さで書いた 60 秒の台本（英語版）が、合成音声では約 107 秒になった。次は: 時刻表は台本の字数でなく、合成した声の長さから作る（[[exp-democracy-river-video]]、[[experience-lessons-2026-11]]）

## 5. 描画

事例: ショーリール 15 秒（canvas に描いて撮る型の最初）、Gyazo の 47 秒（軽い描画で作り直しを回す）（[[nishio-works]]）

**やること**
- src/explainer.html: 1920×1080 の canvas、`window.FPS = 30`、`window.TOTAL_FRAMES = Math.ceil(window.DUR * FPS)`。timeline.js を `<script>` で読む。`renderFrame(f)` は時刻だけの純関数（ファイル冒頭のコメント）
- 画面の切り替えは行の頭の 0.2 秒前（`isNow`・`cur` の `- 0.2`）
- 字幕は行の caption を「。」で文に分け、行の長さを文の字数の比で割って、いま読んでいるはずの文を出す（`subtitle(t)`）。42px（メイキング 40px）、幅 1560px で「、。・」の後を優先して折り返し、下に半透明の帯
- 字幕なしのコマを撮れるようにする（`window.NOSUB`、サムネイル用）
- 撮る

```sh
cd src
node capture.mjs stills 12.5 40   # 指定の秒のコマ → ../stills/
node capture.mjs video            # 全コマ → ../out/video_noaudio.mp4（libx264 crf 18）
NOSUB=1 node capture.mjs stills 3 # 字幕なし（プロセス・メイキング）
```

- 画面写しが要るときは別に撮る（プロセス src/shot.mjs `<url> <out> <w> <h> [scroll]`）。図は matplotlib で PNG にする（プロセス analysis/spec_vs_measured.py）

**確かめた**
- 〔3 本〕renderFrame・30fps・字幕の出し方・capture.mjs（3 本の explainer.html・capture.mjs。capture.mjs は 3 本でほぼ同じで、違いは NOSUB・ffmpeg のパス・静止画のファイル名）
- 〔2 本〕NOSUB でサムネイル（プロセス・メイキングの UPLOAD.md）。本編のサムネイルも「字幕を消したもの」だが、本編の capture.mjs に NOSUB は無く、作り方は写しに無い
- 本編の一回目は 11,326 コマ（プロセス script-draft.md の撮影ログ「10800/11326」）。撮る時間の記録は写しに無い

**注意**
- 字体は Hiragino Sans（Mac のシステムフォント）。別の機械で撮ると変わる
- capture.mjs は `file://` で開き `--allow-file-access-from-files` を付けている。[[exp-html-capture-pipeline]] は「画像を描くなら file:// で開かない（tainted canvas）」と書くが、この 3 本は引用の画像・映像を canvas に描かず ffmpeg で重ねたので、その問題に当たっていない
- 字幕の文ごとの時刻は字数の比での推定で、声と合わせて測ってはいない

**踏んだ失敗と直し方**

- 起きた: 再生倍率 0（止める）が `speed || 1` で 1 になった。次は: 0 があり得る値の既定は `??` で与える（[[exp-tsugigami-promo]]）
- 起きた: 画像を描く canvas を `file://` で開いて tainted になり、`toDataURL` が失敗した。次は: 画像を canvas に描くなら小さな HTTP サーバーから開く。描かないなら ffmpeg で重ねる（[[exp-html-capture-pipeline]]）
- 起きた: 計測の場面に、説明のページの画面写しを出した。気づいた: 西尾「この説明の通りであることを示す画面であるべき、今の画面には情報がない」。次は: 主張そのもの（指定した形と計測した形）を同じ軸の図にする（[[exp-explainer-video-2026-11]]）
- 起きた: 音の聞き比べが、何が始まるのか分からないまま鳴った。気づいた: 西尾「音の聴き比べの前には聴き比べが始まるというひとことがひつよう」。次は: 始まる前の一言と、鳴っている音の名札を出す（[[exp-explainer-video-2026-11]]）
- 起きた: 飾りの場面絵が画面の 36% を占めた。気づいた: 人の評価「意味のない飾り画像の面積が多すぎる」。次は: 実画像・工程・比較といった証拠に面積を配る（[[exp-qualia-video]]）
- 起きた: Homebrew の Python 3.13/3.14 の numpy が壊れていた。次は: 動く版（3.11）で回し、README に書く（[[exp-html-capture-pipeline]]）

## 6. 引用の重ね

事例: 動画の作り方（引用 3 本を ffmpeg で重ねる）、tsugigami の広告動画（実アプリの録画と生成動画の合成）（[[nishio-works]]）

**やること**
- 引用の映像・画像は canvas に枠と名札だけ描き、中身は compose.py が ffmpeg の overlay で重ねる。区間は out/overlays.json（`src`・`from`・`start`・`end`・`box`・`label`）
- 同じ compose.py でナレーションを連結し、loudnorm（`I=-14:TP=-1.5:LRA=11`）をかけて載せる

```sh
python3 compose.py 8          # → out/explainer_draft8.mp4
python3 compose.py stills 40  # メイキング: 静止画に引用のそのコマを重ねた確認用
```

**確かめた**
- 〔3 本〕overlay の形（`setpts=PTS-STARTPTS+<start>/TB` で開始をずらし `enable='between(t,start,end)'`）
- 〔2 本〕静止画の引用（プロセス: `image` なら `-loop 1`。メイキング: 先に枠の大きさの PNG にする）
- 〔1 本〕メイキング: 素材ごとに使う長さ `dur` を決めて繰り返し（`-stream_loop -1`）、締めは最後のコマで止める（`hold`）。行が長いと引用が素材の先（別の場面やロゴ）まで流れた一回目の直し（README.md）
- 〔2 本〕直す前と直した後を同じ場面の同じ位置で左右に並べる（プロセス build_timeline.py の CLIPS 5・6、メイキングの VIS の 10 行）
- 引用元の秒は build_timeline.py のコメントに書く（本編「assets/tsugigami-cut.mp4 = v6 の 17.6–26.0」、プロセス「一回目 208.0 秒、公開版 221.407 秒が解説の節の最初の行の頭」）

**踏んだ失敗と直し方**

- 起きた: 行が長いと、引用の動画が素材の先（別の場面やロゴ）まで流れた。気づいた: 一回目の書き出しを見て。次は: 素材ごとに使う長さを決め、超えたら繰り返す。締めは最後のコマで止める（`dur`・`hold`）（[[exp-tsugigami-making]]）
- 起きた: 冒頭に広告動画の、女性が使う場面を切り貼りして引用した。気づいた: 西尾「よりによって失敗したシーンを引用してるな、最後のシーンでいいんじゃない」。次は: 引用の区間は、素材の中で意図が一番伝わる場面（完成版の最後など）から選ぶ（[[exp-explainer-video-2026-11]]）
- 起きた: 「情報がない」と言われて直した話を、直した後の文だけで見せた。気づいた: 西尾「「情報がない」は修正前を出さないと意味がわからない」。次は: 直す前 → 指摘 → 直した後の順に、同じ場面の同じ位置で並べる。引用は最終版を使い、直した所だけ前後を並べる（[[exp-explainer-video-2026-11]]、[[talk-three-videos-2026-11]]）
- 起きた: 生成 AI への「美人にして」の指示を、そのまま画面に引用していた。気づいた: 西尾「ムッとする人がいそう」。次は: 引用する指示文は、見る人がどう受け取るかで選ぶ（[[exp-tsugigami-promo]]、[[exp-tsugigami-making]]）
- 起きた: 録画スクリプトがメニューを開いた後につまみをもう一度押して閉じ、紙が継がれていないまま撮った（アプリの不具合と思って依頼した）。気づいた: CyEC2 の切り分け。次は: 素材を自動操作で撮るときは、操作の後に状態を確かめ、違えば止める（[[exp-tsugigami-promo]]）
- 起きた: opencv の fps を使い、フレーム番号 ÷ fps で 68.65 秒の画面録画を 70.08 秒と測った。次は: 引用元の秒は ffprobe の pts で取る。VFR を疑う（[[exp-galleria-ffmpeg-measurement-and-delivery]]）
- 起きた: ffmpeg の `-vf`・`-af` の中に Windows のパスを書いて壊れた（`\` がエスケープ、`:` が区切り）。次は: filter の引数には相対名で渡す（[[exp-galleria-ffmpeg-measurement-and-delivery]]）

## 7. 検査

**やること（写しにあるもの）**
- 静止画: `capture.mjs stills`（3 本）と `compose.py stills`（メイキング）で、山場の秒を全編の前に見る
- 読み: kana.json・asr.json（3b）、合成のたびに synth.py の `applied` で指定が当たった行を見る（プロセス・メイキング）
- 長さ: make.sh の最後の ffprobe（本編）
- 音量: 公開の写しを -14 LUFS に合わせ、ピークと一緒に UPLOAD.md に書く（プロセス -14.0 LUFS・ピーク -2.8 dBFS、メイキング -13.9 LUFS・ピーク -2.3 dBFS）
- チャプター: どれも 10 秒以上か（3 本の UPLOAD.md）

**確かめた**
- 〔2 本〕compose.py の書き出しはそのままでは -14 にならない（メイキング draft2 は -15.1 LUFS）。プロセス・メイキングは「音量を -14 LUFS に合わせた写し」を別に作って投稿した。写しの作り方は写しに無い

**写しに無いもの**
- 閃光の検査・コンタクトシート: 本編 script-draft.md の「公開前にやること」に「書き出しの検査: 閃光・音量の 2 パス・コンタクトシート」と書いてあるが、した記録は写しに無い。手順は [[checks-and-finishing]]
- 人が最後に通しで見ること自体は、次の 8 の「レビュー」で毎回している

**踏んだ失敗と直し方**

- 起きた: compose.py の書き出しが -15.1 LUFS で、-14 にならなかった。次は: 書き出しの後に最終のファイルの音量を測り、合わせた写しを作って値を UPLOAD.md に書く（[[exp-tsugigami-making]]）
- 起きた: プロセス動画で「11,326 コマを一枚ずつ撮り」と本編の一回目の数を言ったまま公開した（公開版は約 11,890 コマ）。気づいた: wiki に file back するとき。次は: 台本で言う実測の数は、最終の書き出しで測り直す（[[exp-explainer-video-2026-11]]）
- 起きた: codec・尺・字幕・hash の機械の検査が全部通っても、読み・声質・理解しやすさの問題が残った。次は: 機械の検査は足切りにだけ使い、人が通しで見る（[[exp-qualia-video]]）
- 起きた: 画像の自動判定（grok-4.3）が「画面が白いまま」を過剰に否定した（画素では線が無い動画にも線があると言った）。次は: 人の目か画素で確かめる（[[exp-tsugigami-promo]]）

## 8. レビューの受け取り

事例: 動画の作り方（出先でスマホ、Google ドキュメントのコメント）、tsugigami のメイキング（原稿の書式をそのまま合成の入力に）（[[nishio-works]]）

**やること**
- 書き出しのたびに、西尾が見られる場所へ置き、直しを受け取る。置き方は西尾のいる場所で選ぶ
  - 出先でスマホだけ: 小さくした動画を Google ドライブへ。文言は Google ドキュメントに台本を置く
  - Mac の前: ローカルのファイルを開くだけ
  - 選ぶもの（声・印・候補）: claude.ai の非公開ページに db を持たせ、選んだものを読み戻す
- Google ドキュメントの台本は、行頭に行の番号を残してもらう形にする（本編「各行の先頭の ID（s3_02 など）は残してください」、プロセス・メイキング「行頭の〔s0_01〕は行の番号なので消さないでください」）。本編は番号の後ろに一回目の動画の中の時刻（`s0_01（0:01）`）と、その行の画面の要点を付けた
- 読み戻して、元の markdown との差分を取る（本編 review/README.md「read_file_content（includeComments: true）。round1-original.md と差分を取る」）

```sh
# 本編 make.sh のスマホ用（1280 幅・24fps・crf 30・モノラル 64k）
ffmpeg -y -i out/explainer_draft$N.mp4 -c:v libx264 -crf 30 -preset slow -vf scale=1280:-2 -r 24 \
  -c:a aac -b:a 64k -ac 1 -movflags +faststart out/explainer_draft${N}_phone.mp4
```

**確かめた**
- 〔3 本〕Google ドキュメントで原稿を受け取った（本編 review/round1・round2、プロセス review/draft4、メイキング README.md）
- 〔2 本〕スマホ用を Drive に（本編 make.sh、メイキング README.md「720p・crf 33、7.0MB」）。Drive のコネクタは base64 で 10MB が上限（[[exp-explainer-video-2026-11]]）
- 〔1 本〕メイキングでは、原稿の書式（〔m0_01〕 の行）を build_lines.py がそのまま読む。直し用の原稿と合成の入力が同じ書式
- 西尾が原稿を直接書き換えた例（プロセス review/draft4-script.md → draft4-edited.txt）: 「確かめました」→「ファクトチェックをしました」、「一般向けに」→「対象視聴者は一般」、「人が選んだのは、まおです」→「今回もまおでした」、「測ると」→「計測してみると」、s7_05 の直した後の文の引用を削る

**踏んだ失敗と直し方**

- 起きた: 作り直した動画を同じファイル名で上書きして同じ URL を案内し、相手はキャッシュで古いものを見続けた。気づいた: 3 回「まだ直っていない」と返ってきて、配信スクリプトの max-age を調べた。次は: 版を名前に入れ（`_draft3`）、古い名前は消す（[[exp-galleria-ffmpeg-measurement-and-delivery]]）
- 起きた: Google ドライブのコネクタは base64 で 10MB が上限で、書き出しのままでは渡せなかった。次は: 1280×720・24fps・crf 30 前後で 10MB 未満のスマホ用を作る（[[exp-explainer-video-2026-11]]、[[exp-tsugigami-promo]]）
- 起きた: 聞き比べのページに m4a を置いたら配信されなかった。次は: 音は mp3 にする（[[exp-explainer-video-2026-11]]）
- 起きた: 西尾が Mac の前に戻った後も Drive で渡していた。気づいた: 西尾「もうMacの前にいるかGoogle Driveつかわなくていいよ」。次は: 西尾がいる場所を確かめて渡し方を選ぶ（[[exp-explainer-video-2026-11]]）
- 起きた: 動きが大事な版を静止画で見せても評価できなかった。次は: 全編の前に、短い動画（一節・数秒の A/B）を見せて選んでもらう（[[experience-lessons-2026-11]]）

## 9. 公開

事例: デジタル民主主義の川 60 秒版（X は最初のコマがサムネイル）、tsugigami の広告動画（生成の人物で AI の使用「はい」）（[[nishio-works]]）

**やること**
- youtube/UPLOAD.md に、投稿の素材と設定と説明欄を書き、西尾が YouTube Studio から投稿する。投稿後に URL を UPLOAD.md に追記して commit する（本編 9c67dc6、プロセス a725595）
- 書くこと（3 本の UPLOAD.md の共通部分）:
  - 動画のファイル（1920×1080・30fps・長さ・LUFS）、サムネイル（1280×720、字幕なしの画面）
  - 視聴者: 子ども向けではない／カテゴリ: 科学と技術／言語: 日本語／字幕: 映像に焼き込み済み
  - チャプター（どれも 10 秒以上、いちばん短いものの秒）
  - AI の使用（改変または合成されたコンテンツ）の答えと理由
  - タイトル（案を並べて西尾が選ぶ）
  - 説明欄: 冒頭 2〜3 文、チャプター、「この動画の作り方」（台本とコードは Claude Opus 5.5・人が確認、声は AivisSpeech（まお）、読みの確かめ方）、引用した動画の URL、出典、ハッシュタグ
- 見本として他の声を鳴らすなら、説明欄と最後の画面に声のクレジットを書く（プロセス 60b59fa「最後の画面に…見本の声のクレジット」、UPLOAD.md「VOICEVOX:ずんだもん」）

**確かめた**
- 〔3 本〕UPLOAD.md の形と、モデル名を説明欄に書くこと（grasp-nishio の決まり「動画ではモデル名を明示する」）
- AI の使用: 本編とメイキングは「はい」（引用した広告動画に、生成 AI で作った写真のようにリアルな人物が出る）。プロセスの UPLOAD.md は「西尾が決める」として判断の材料を並べ、どう答えたかは写しに無い
- チャプターの 10 秒の理由は本編の UPLOAD.md の記述「YouTube は 10 秒未満が一つでもあるとチャプター全体が無効」。この wiki で原典は確かめていない

**文献**
- 台本を AI が書くこと、コードで描くこと、字幕は YouTube の例示で開示不要。既製の合成音声の扱いは例示に無い（[[web-rights-youtube-genai-disclosure]]）

**踏んだ失敗と直し方**

- 起きた: プロセス動画の URL を wiki に書かないまま file back した。気づいた: file back の log に「未記録」と書き、後の commit（b189e34）で足した。次は: 投稿の直後に UPLOAD.md と exp ページの両方へ URL を書く（[[exp-explainer-video-2026-11]]）

---

## Open Questions

- 尺の見込みが 2 本とも 40 秒ほど短く出た。行間・節の間を見込みに足すと合うかは計算していない
- compose.py の書き出しが -14 LUFS にならない理由と、公開の写しの作り方（2 パスの loudnorm か）は写しに無い
- 閃光の検査は 3 本ともした記録が無い。点滅の少ない図と字幕の動画で要るかは決めていない
- 字幕の文ごとの時刻（字数の比）と、cues.py の語の時刻（合成の長さの比）は、声と突き合わせて測っていない
- この手順は「台本を AI が書き、声は合成、映像はコードで描く」解説に限る。実物を撮る解説（画面収録・実写）は 3 本に無い

## Updates

### 2026-11-10 西尾の決定（Mac の対話から）

- このページの置き場所（analyses/）と名前（talk-video-making-2026-11）は今のままでよい
- 閃光の検査: 図と字幕が中心の動画ではしなくてよい。「7. 検査」の「写しに無いもの」と Open Questions の「閃光の検査は 3 本ともした記録が無い…要るかは決めていない」への答え。点滅や速いカットのある動画（promo など）の検査は [[checks-and-finishing]] のまま

### 2026-11-10 共通のコードは持たず、失敗と直し方を各段に寄せる（西尾の決定、Mac の対話から）

- 西尾の決定: 共通のコードベースは持たない（動画ごとにやりたいことが違い、保守の手間が大きい）。共有するのは「失敗に気づいて直した知見」
- 1〜9 の各段の末尾に **踏んだ失敗と直し方** を足した（45 行）。材料は exp-explainer-video-2026-11、exp-tsugigami-making、exp-tsugigami-promo、exp-html-capture-pipeline、exp-galleria-ffmpeg-measurement-and-delivery、exp-galleria-tts-and-singing、exp-qualia-video、exp-gyazo-resumption-video、exp-democracy-river-video、talk-three-videos-2026-11、experience-lessons-2026-11、explainer-script-factcheck-2026-11。気づき方が経験のページに書かれていないものは「記録に無い」と書いた
- 「読み方」に、失敗に気づいて直したらその場で該当の段に一行足す決まりと、このページが Mac の skill video-making から最初に読まれることを書いた
- 指示の例のうち「行の頭の数字やアルファベットの誤読」は、wiki の経験のページに「行の頭」という条件の記録が見つからなかったので、数字・英字の誤読（H.264・2026 年・Image 2.0）として書いた

### 2026-11-10 事例紹介へのリンク

- 西尾「nishioの過去作品も適宜事例紹介ページに載せて、そこから必要なところにリンクがあるべき」。1〜6・8・9 の段の頭に、参考になる作品を [[nishio-works]] へのリンクで足した
