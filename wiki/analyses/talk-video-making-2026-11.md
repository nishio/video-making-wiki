---
type: analysis
summary: 解説動画（talk）を、台本 → 事実確認 → 声 → 時刻表 → 描画 → 引用の重ね → 検査 → レビューの受け取り → 公開の順に作る手順。2026-11-09 に同じ作りで作った 3 本（本編「動画の作り方 2026年11月」、プロセス動画、tsugigami のメイキング）の作業場のファイルから書いた。各手順に、どの動画のどのファイルで確かめたかと、何本で確かめたかを付ける
video_types: [talk]
sources:
  - Mac の ~/video-making-explainer、~/video-making-process、~/tsugigami-promo/making のテキストの写し（CyEC2 の ~/handoffs-from-mac/2026-11-09-talk-materials/。音・映像・画像・out/ は写していない）
  - 同 gitlog/（video-making-explainer 25 commit、video-making-process 9 commit の git log --stat、tsugigami-promo/making のファイル時刻）
  - exp-explainer-video-2026-11.md、exp-tsugigami-making.md、exp-tsugigami-promo.md、exp-html-capture-pipeline.md、exp-galleria-tts-and-singing.md
  - explainer-script-factcheck-2026-11.md
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

## 2. 事実確認

**やること**
- 台本の言い切っている主張を選び、wiki のページでなく原典（公式ページ・規格・論文）を開いて確かめ、言い方を直した案の文を作る

**確かめた**
- 〔1 本〕本編: 15 の主張を CyEC2 が原典で確かめ、そのまま使えたのは 1 個（[[explainer-script-factcheck-2026-11]]、本編 b2bff79「事実確認の案の文を反映」）。説明欄の「出典」に原典の URL を節ごとに並べた（本編 youtube/UPLOAD.md）
- 〔1 本〕プロセス: 中身は自分の制作の話なので、各節の後ろの `[ ]` に一次の記録（commit・LOG・wiki のページ）を書いた（プロセス script-draft.md）。原典を開いての確認とは別
- メイキングの写しには、事実確認の記録が無い。材料は [[exp-tsugigami-promo]] の時系列（会話記録の時刻とファイル時刻）

## 3. 声

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

## 4. 時刻表

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

## 5. 描画

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

## 6. 引用の重ね

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

## 8. レビューの受け取り

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

## 9. 公開

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
