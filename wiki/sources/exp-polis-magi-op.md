---
type: source
summary: アニメ OP の様式（明朝の白字幕と映像の高速交互、拍ごとのカット）を借りて Polis・デジタル民主主義・Plurality を伝える 55 秒動画。HTML Canvas＋headless Chrome で描き、音は Python で合成した。v1 は「しょぼい」と言われ、実物の OP のカット密度に合わせて直したが、メロディの未検証と英語の歌声の品質不足で 2026-09-30 から止まっている
video_types: [promo]
sources:
  - galleria C:\Users\nishi\claude-win\polis-magi-op\README.md（commit b5f73bc 時点の記述）
  - galleria C:\Users\nishi\claude-win\polis-magi-op\HANDOFF.md（commit f993146 まで）
  - polis-magi-op の git log（2c82db0 2026-09-30 〜 f993146 2026-10-06、計 10 commit）
  - polis-magi-op src/capture.mjs, src/score.py, src/op.html, sing/*.py
  - grasp-nishio LOG.md 2026-09-30 の項、grasp-nishio wiki/entities/polis-magi-op-on-galleria.md
---

# エヴァ OP 様式の Polis / Plurality 動画（polis-magi-op）

## 何を作ったか

- 『新世紀エヴァンゲリオン』TV 版 OP の様式（明朝の白字幕と映像の高速交互、青い点の冒頭、生命の樹、十二枚の翼、青空で終わる）を参照して、Polis・デジタル民主主義・Plurality を伝える短い動画。起点は西尾の「Polis は MAGI にインスパイアされている。エヴァOPの音声に重ねて Polis・デジタル民主主義・Plurality を伝える動画を作れないか」（grasp-nishio LOG 2026-09-30）
- 55 秒、1920×1080、30fps（`src/op.html` の `W, H, FPS`）。128BPM の構成で、イントロ 0–12.7 秒／リフ 13.1–20.6 秒／サビ 20.6–45 秒／アウトロ 45–55 秒（README「構成」）
- 状態: 2026-09-30 に西尾の指示で制作停止。最新のレンダリングは v3。v4 の修正はソースにだけ入っていて未レンダリング（README 冒頭）。**公開はしていない**
- 同日、西尾の判断で Mac から galleria へ移管。理由は「腰を据えてかからないとできない」（HANDOFF、grasp-nishio LOG 2026-09-30）

## 作り方のパイプライン

道具は Mac の `~/nishio-showreel` と同じ系統（README: node_modules は showreel のものへのシンボリックリンクだった）。

1. **音**: `src/score.py`（numpy だけ）が打ち込みのインスト短縮版を合成して `out/audio.wav` と `timeline.json`（区間の区切り時刻）を書く。メロディは「音名オクターブ:長さ(8分音符単位)」の文字列、和音は 1 小節ごとの記号で持つ
2. **映像**: `src/op.html` が 1 枚の canvas に `renderFrame(f)` でフレーム番号から絵を決定論的に描く。ショットは `sh(開始秒, 終了秒, 描画関数, カメラ, ラベル)` の表で、区切り時刻 `S` を `timeline.json` と一致させる。動きは閉形式のばね（`spring(t, k, d)`）で入れる
3. **書き出し**: `src/capture.mjs`（puppeteer-core）が headless Chrome でページを開き、`document.fonts.ready` を待ってから 1 フレームずつ `renderFrame` → `canvas.toDataURL` → ffmpeg の image2pipe へ流す（libx264, CRF 17, yuv420p）。`stills` モードで指定秒の静止画だけ出せる
4. **結合**: `ffmpeg -i video_noaudio.mp4 -i audio.wav -c:v copy -c:a aac -b:a 256k -shortest`

```sh
cd src
python3 score.py                 # -> ../out/audio.wav, timeline.json
node capture.mjs stills 22.5 40  # 静止画確認
node capture.mjs video           # -> ../out/video_noaudio.mp4
ffmpeg -y -i ../out/video_noaudio.mp4 -i ../out/audio.wav -c:v copy -c:a aac -b:a 256k -shortest ../out/polis_magi_op.mp4
```
（README「再レンダリング」より）

## 版の経過と西尾のフィードバック

| 版 | 内容 | 反応・気づき |
|---|---|---|
| v1 | 約 12 場面（平均 4.5 秒） | 西尾「しょぼい」。実物の OP は 90 秒・84 カット（平均 1.07 秒）で、テンポが 4 倍以上遅かった |
| v2 | 約 50 カット、1 拍 1 カット。青い点の冒頭・白字幕の交互挿入・鉛筆スケッチ・十二枚の翼・青空。音をロック寄りに厚く | 参照は Wikipedia の OP 構成の記述（動画そのものは見ていない） |
| v3 | 生命の樹を MAGI（上の 3）＋ 6-Pack of Care（中央の 6）＋ ⿻ Plurality（最下）に対応させた | 西尾の提案「6pack of care を絡めるといいかも」 |
| v4（未レンダリング） | 自己採点（フック 3／スマホ可読性 4／動き 5／変化 6）でワースト 3 を直す。ばね、冒頭の光、アウトロを回想フラッシュ→青空の ⿻→クレジットへ、四隅の HUD を撤去、字幕を拡大 | アウトロ 10 秒の静止クレジットが「死んだ拍」だった（AI の自己評価） |

（README「版の経過」、HANDOFF「現在の状態」）

- **参照は文章でなく実物を見る**: v1〜v3 は「実物の動画は取得しない、参照は文章の構成記述で代替する」としていたが、2026-10-01 に西尾の指示で改めた。以後は西尾の手元にある実物の OP 動画（私的な置き場。repo へコピー・commit しない）から、音声で拍と区切りを解析して画面の切り替えを合わせ、映像からショット長・字幕の出し方・配色・質感を取る方針（README「参照」、commit b5f73bc）
- 先行例として、Taelin が同じ OP を参照して Bend で作った動画の gist があり、エージェントが拍に合わせていた（README「参照」。tweet-memo に source あり、grasp-nishio LOG 2026-09-30）

## 腰を据えるための進め方（HANDOFF に書かれた計画）

西尾が「参考」として貼った Movez の記事（Opus 5.5 でモーション動画を作る手順）から取った計画。**実施されたのは自己採点まで**で、以下の docs はまだ無い。

- 最初に `docs/style_guide.md`（参照の文法: ショット長、字幕の出し方、配色、質感）と `docs/shotlist.md`（拍単位のショット表）を書いて西尾に見せる
- レンダリングの前に 1 拍 1 枚のコンタクトシートと 360px 幅のスマホ試験を見て、フック・可読性・動き・変化・構図・音の同期を 10 点満点で辛口に採点し、ワースト 3 を直す。全項目 8 点以上まで回す
- 「最初の 2 秒のフック」はエヴァ OP の静かな冒頭とぶつかる。参照の文法で上書きしてよい軸は西尾と決める（未決）
- 閉形式ばね、サブフレーム合成のモーションブラー、音量 -14 LUFS は未導入（ばねは v4 で一部）
- 本物と同じ 90 秒（A メロ・B メロ込み）に伸ばすかは未決

経過そのものは記事の「一回目は mid → 参照と自己批評で直る」をなぞった（HANDOFF、grasp-nishio LOG 2026-09-30）。

## 英語の歌声の試み（2026-10-03〜06、終了）

- SoulX-Singer（歌声合成、galleria のローカル GPU）で、VOICEVOX 波音リツを参照の声にして英語の替え歌を歌わせた。伴奏は別プロジェクト zankoku-hannya の伴奏、尺は実物の OP と同じ構成（西尾が案 2 を選択）。西尾の初回評価は「使えそうではある」（HANDOFF、commit 7de02b2）
- 西尾の指示: **歌っている英語は字幕に出す**。歌だけでは聞き取りに頼れない。字幕の時刻は生成時の行・音節ごとの開始・終了秒（`sing/out_*/lines.json`）から取る（HANDOFF）
- 伴奏の時刻を実物の OP の時刻に合わせた: `sing/align_op.py` で音声を突き合わせて OP の構成（イントロ・間奏・A・A'・B・サビ 1 回、91.4 秒）を確かめ、`make_backing.py` で伴奏のサビ 1 を飛ばし頭を 2.4 秒詰めた。`check_backing.py` で ±0.2 秒。こうすると映像のショット時刻を実物からそのまま写せる（HANDOFF）
- 流れ: 歌詞の下書き（20 行 218 音節）→ `build_full.py` → `takes.py out_X 6`（行ごとに最大 6 回生成し、Whisper の書き起こしが歌詞に一番合う版を採る）→ `check_lines.py`（伴奏と合成、行ごとの書き起こし）→ `review_page.py`（試聴ページ）
- **落とし穴**: SoulX-Singer の `auto_shift` は行ごとに参照の声の音域へ整数半音で移調するので、伴奏と調がずれる。out_full3 は 20 行の多くが ±2〜7 半音ずれ、西尾の評価は「音程がメチャクチャで聞くに耐えない」。Whisper の一致は音程を見ないので、**渡す前に `pitch_check.py`（librosa の pyin で音節ごとの音高を楽譜と比較）を通す**ことにした。auto_shift を外し版の選択に音程の減点を加えた out_full4 で、音節の 96% が楽譜から 0.5 半音以内になった（HANDOFF、commit 9416d91）
- **終了**: 2026-10-06、西尾「soulx-singerは英語の歌を歌わせられないかと少し試行錯誤してみたが満足いくクオリティにならなかったので終了」。モデルごと削除したので `sing/` のスクリプトはもう動かない（HANDOFF、commit f993146）。詳細は galleria-wiki の `wiki/soulx-singer-english-singing.md`

## 詰まったこと・落とし穴

- **AI が記憶から打ち込んだメロディは未検証**。サビ 1 行目以外はずれている可能性が高い、と AI 自身が書いている。公開前のブロッカーで、実物の音声と突き合わせたうえで西尾の耳で確かめる手順になっていた（HANDOFF「公開前の必須事項」）。ここが止まりどころになった
- 事実の言い切りの境界: 「Polis は MAGI にインスパイアされた」は会場ツイート 3 件の引用しか根拠がなく、本人の発言の一次記録が未確認だったので、画面では MAGI→Polis の対比に留めた（README「確認した事実」）。人物・組織の事実は確認済みの範囲だけ載せ、役割語を補完で作らない
- 音の権利: 出力に載せる音は合成のカバーで、原盤の録音は使わない。YouTube 公開は作曲の権利の包括契約の範囲を前提にした（README「音源」）
- 機械の移し替え: Mac→galleria で、Chrome のパス（capture.mjs）、node_modules（シンボリックリンクだった）、WSL の numpy 不在、Windows 側にしか node が無い、C: の空き約 3GB（レンダリング 1 回で約 250MB）などが差分になった（HANDOFF「galleria で動かすための差分」）。capture.mjs は commit 6b587ad で Windows の Chrome に合わせた

## 再利用できる部品

- `src/capture.mjs`: canvas の `renderFrame(f)` を 1 フレームずつ PNG にして ffmpeg へパイプする書き出し器。静止画モードでコンタクトシート用のフレームを取れる
- `src/score.py`: 文字列で書いたメロディ・和音から numpy で音を合成し、区間の区切り時刻を JSON に出す（映像側のショット表と時刻を共有する作り）
- `sing/pitch_check.py`: 生成した歌声の音程を音節ごとに楽譜と比べる検査
- `sing/takes.py`: 行ごとに複数回生成し、書き起こしの一致で版を選ぶ（＋音程の減点）

## Open Questions

- 拍に当てた高速カットの promo は、参照の文法（静かな冒頭）とスマホ視聴のフック（最初の 2 秒）がぶつかる。どちらを優先するかは決まっていない
- メロディの検証を AI だけでどこまで進められるか（実物の音声からの採譜）は試されていない

## Updates

### 2026-11-09 第 2 回サーベイ: 閃光の基準とカットの密度

- 1 拍 1 カット（128BPM）ならどの閃光の基準にも収まるが、8 分音符で刻むと NHK・民放連の「輝度変化 20% 超の場面転換は原則 1 秒 3 回まで」を超える。v4 で予定の「回想フラッシュ」は局所の密度が問題になる場所。参照の平均 1.07 秒/カットは平均で、局所の密度は分からない（[[web-motion-itu-r-bt1702-ofcom-nhk-minpo-flash-guidelines]]）
- 参照の平均 1.07 秒は現代ハリウッド映画の平均ショット長（4 秒未満、Cutting ら）よりはるかに短い。v1 の 4.5 秒は映画の平均程度だった（[[web-layout-smith-2012-cutting-2011-film-attention]]）
- 1 拍 1 カット（約 0.47 秒）は字幕の最短表示（0.5 秒、Netflix）を下回る（[[web-type-netflix-timed-text-style-guide]]）

