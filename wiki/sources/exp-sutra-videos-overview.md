---
type: source
summary: 経文・真言・偈・行者問答を動画にする制作（~/sutra-videos、2026-07〜11）の全体像。制作の系統、作品ごとの尺・比率・公開先、正本の置き方、レンダリングの道具、Mac と galleria の分担、公開まわりの決まり
video_types: [promo, talk, embed]
sources:
  - ~/sutra-videos/CLAUDE.md
  - ~/sutra-videos/wiki/index.md
  - sutra-videos wiki/analyses/同期解説動画の制作パターン.md
  - sutra-videos wiki/analyses/般若心経漢字版の制作.md
  - sutra-videos wiki/analyses/般若心経のカノンの制作.md
  - sutra-videos wiki/analyses/真言言えるかなの設計と校訂.md
  - sutra-videos wiki/log.md（2026-10-06 init）
  - ~/sutra-videos/zankoku-hannya/HANDOFF.md
  - commit 402251a（repo の切り出し）、2d43337（公開素材）
---

# 経文・真言の動画制作の全体像（sutra-videos）

## 何を作ったか

2026-07 から 11 月にかけて、西尾の Mac（一部 galleria）で、経文・真言・漢文偈・行者問答を動画にした。もとは修験道の wiki（mountain）の中で作っていたが、2026-10-06 に制作だけを `~/sutra-videos`（GitHub `nishio/sutra-videos`、private）へ履歴ごと切り出した（commit `402251a`、sutra-videos wiki/log.md 2026-10-06）。経文の意味・出典は mountain 側に残り、sutra-videos は「作り方」だけを持つ。

制作は大きく四つの系統に分かれる。版の名前は西尾の呼び方のまま。

| 系統 | 作品 | 尺・比率 | 公開 |
|---|---|---|---|
| 同期解説（学習用） | 火界咒、蔵王権現・役行者・不動慈救呪、開経偈・懺悔文・本覚讃・五大尊名号、般若心経の解説版、三條錫杖（試作） | 真言は約45秒・3回反復、16:9（1920×1080）と 9:16 Shorts。般若心経は1回版107秒 | 般若心経の解説版は YouTube に出ている（カノンの概要欄から案内、sutra-videos wiki 般若心経のカノンの制作 2026-09-27）。真言・偈は公開パッケージ一式まで作ったが、公開の記録は wiki に無い |
| テンポで上げる別エディション | 般若心経 漢字版（210BPM）、アゲアゲ版（128→176BPM、約3分）、真言言えるかな（19尊・128BPM・約2分26秒） | 16:9、30fps | アゲアゲ版は読経版とメロディ版の2本を YouTube（2026-09-27）。真言言えるかなは X（2026-09-26）→ YouTube（09-27）。漢字版は横版レビュー止まり |
| 曲に載せる | 般若心経のカノン（パッフェルベルの通奏低音に3声、2分58秒）、残酷な般若心経のテーゼ（替え歌、約114秒、制作中）、第九「歓喜の歌」の一節（24秒、9:16） | 16:9／9:16、30fps | カノン v1 を YouTube（2026-09-27、Heart Sutra Canon）。残テは権利の確認前で未公開 |
| 行者問答 | 学習動画（全編13分25秒を作って不採用→問一だけの26秒）、アゲアゲ行者問答（28秒・19.6秒・14.5秒の試作） | 16:9 | 未公開。本人評価は「だるい」「いまいち面白くない」 |

系統ごとの詳細: 同期解説と行者問答の学習動画は [[exp-sutra-sync-subtitles]]、テンポで上げる版とアゲアゲ行者問答は [[exp-sutra-hype-editions]]、曲に載せる版は [[exp-sutra-songs-on-music]]、声の合成は全系統共通で [[exp-sutra-voicevox-singing]]。

この wiki の三つの型との対応は、同期解説が embed（一つの真言・偈を音と意味で渡す短尺）と talk（般若心経の解説版のような長め）の間、テンポで上げる版と曲に載せる版が promo 寄り（SNS で「何これ」と思わせる）。ただし sutra-videos 側に型の区別は無く、これはこの wiki での当てはめ。

## 正本の置き方（全系統に共通）

sutra-videos/CLAUDE.md の「動画の制作」節と[[exp-sutra-sync-subtitles]]に詳しい。骨格だけ:

- **内容正本**（何を見せるか）と**時間正本**（いつ発声するか）を別ファイルにする。内容は JSON（`content/mantras/<slug>.json` など）、時間は人が手で直せる一行テキスト（`<slug>-rhythm.txt`。空白＝区切り、`ー`＝1拍延長、`・`＝1拍休止）
- **同じ題材の別エディションは正本を複製しない**。テンポ・音程は描画時のパラメータ（`--beat-ms` / `--transpose`）で上書きし、出力先だけ `output/<slug>-<edition>/` に分ける。本文を直せば全エディションに効く（般若心経漢字版の制作）
- 版ごとに必要な追加情報だけを派生ファイルに持つ。アゲアゲ版の「見せる単位」＝`hannya-shingyo-hype-phrases.txt`、カノンの編曲リズムと旋律正本。編曲リズムは「元の正本との差が `ー`・`・` の置き方だけ」であることをスクリプトが毎回検証する
- 人がレビューする画面文言は `output/<slug>/screen-text.md`。直しは生成物でなく正本へ戻して再生成する
- 公開時に見るもの（動画・サムネイル・概要欄・screen-text・preview）だけ `output/<slug>/` 直下、音声・フレーム・QA 画像は `build/`（gitignore）。2026-10-05 に「用途別フォルダに散らばって一題材の編集にフォルダ横断が要った」ので題材単位に寄せた（同期解説動画の制作パターン 2026-10-05）

## 作り方のパイプライン（道具）

- **音声**: VOICEVOX Engine の歌唱 API（`sing_frame_audio_query` → `frame_synthesis`）。読経も「単音の歌」として合成する。詳しくは[[exp-sutra-voicevox-singing]]
- **画**: Python + Pillow で1フレームずつ（または状態ごとに1枚）描く。ビート同期で揺れ・閃光がある版（アゲアゲ版・真言言えるかな）は `multiprocessing.Pool` で並列に描き、raw RGB を ffmpeg の標準入力へ流す（`scripts/make_sutra_hype.py`。9並列で5512フレーム約5分）
- **状態が切り替わるだけの版**（同期解説）は、状態ごとの静止画を ffconcat で継続時間つきに並べて ffmpeg で H.264/AAC にする（`scripts/make_sutra_package.py`、`make_mantra_package.py`）
- **伴奏**: MIDI を fluidsynth + GeneralUser GS で鳴らす（残テ・第九）。打楽器・鐘・EDM の伴奏は numpy で合成（`make_sutra_percussion.py`、`make_sutra_hype.py`）
- **長い動画の部分書き出し**: カノンは画が音声に依存しない作りなので、区間ごとに音声なしで書き出して `-c copy` で連結し、最後に音声を重ねる（`scripts/canon_render_segment.py`）
- **サムネイル**: 背景だけ画像生成（文字なし）、正確な題名は Pillow で後組み（`make_kakaiju_thumbnail.py`、`make_verse_thumbnails.py`、`make_sutra_publication.py`）
- **環境の罠**: scipy は Homebrew の python3 に無く pyenv の 3.12 で動いた。第九は `/opt/homebrew/bin/python3.11` 指定。http.server を立てる前に `lsof -i :<port>` で空きを確かめる（般若心経のカノンの制作 2026-10-07）

## Mac と galleria の分担

- 正本は GitHub、Mac `~/sutra-videos` と galleria `claude-win\sutra-videos` の両方で pull/push する。「commit したか」でなく「push したか」を見る（sutra-videos/CLAUDE.md）
- 2026-10-01 の残テは、割り付け（歌声）を Mac、映像を galleria で並行した。galleria 側は Codex が担当し、全編01〜04、分類名追加版、十二因縁の位置調整…と一日で十数版を重ねた（zankoku-hannya/HANDOFF.md）
- 二拠点に分けたことで起きたこと（実際にあった）:
  - galleria にはアゲアゲ版の知識（効いた原則）が無く、それを知らないまま「かっこよさ」の改善案を作り始めていた。後から refs/ にコピーして渡した（残酷な般若心経のテーゼの制作 2026-10-01）
  - 同じ「是大神呪」の音声を両拠点で別々に直していた。「二拠点で同じ素材を触るときは、どちらの版を正とするかを本人から両方の session に伝える必要がある」（残酷な般若心経のテーゼの割り付け 2026-10-01）
  - 描画中に別 session が `notes.json` と音声を作り直し、字のタイミングが古く音声が新しい動画ができかけた
  - galleria の Windows git と WSL git の改行ノイズは `.gitattributes` で LF 固定にして止めた（commit `064b726`）
- 2026-10-06 に置き場を一本化してからは bundle の受け渡しも refs/ も不要になった

## 公開まわりで決まったこと

同期解説動画の制作パターン 2026-09-27、般若心経漢字版の制作 2026-09-27 より。

- **同じ題材の別版を並べるときは、サムネイルで一覧から区別できるようにする**。冒頭の言葉・配色・帯の3つを変えた（読経版／♪メロディ版）。帯の言葉は作る側の説明（「単音版」）でなく見る側の価値（「読経版」＝一緒に唱えやすい）にする
- **サムネイルと動画冒頭の画を合わせる**（言葉も配色も。再生直後に色が変わらない）。アゲアゲ版は冒頭の画をそのままサムネイルにした（`--thumbnail`、`--question`、`--intro-palette`）
- **YouTube のチャプターは1つ10秒以上必要**。チャプター時刻はレンダラの区切りから計算して出す（目で拾わない）
- **実地で録音したこと自体を公開物に書かない**（本人の方針）。寺名も概要欄に出さず「いくつかの寺・宗派の資料を見比べた」と書く。公開文を作ったら該当語を grep してから渡す
- **メイキング記事は制作した AI の視点で書く**。本人の体験・感情を想像で書くとハルシネーションになる。Claude が何を考え、どこを間違え、指摘から何を学んだかを書き、本人の発言は実際の言葉だけを引用し、案と指摘の主を区別する（`output/hannya-shingyo-hype/blog/making.md`）
- 解説版と音楽作品では断り書きの量が違う。カノンの公開前に西尾は読みの注記・実践の指示・本文の参照を削った（般若心経のカノンの制作 2026-09-27。理由は記録上「と読める」止まり）
- 概要欄に公式性の否定（「公式音源ではありません」）や視聴者への実践指示を入れない。`This is an educational aid.` と留保だけ（同期解説動画の制作パターン 2026-08-12）
- **版の番号は対外の呼び方に一本化する**。公開前の版を v1 と数えていたせいで内部 v3＝対外 v2 になり、西尾「とても紛らわしい」でファイル名まで付け替えた（般若心経のカノンの制作 2026-10-07）
- 100MB を超える本編動画・原曲 MIDI・伴奏 wav は git に入れない（commit `2d43337`）

## 進め方で効いたこと（系統をまたいで）

- **短い試作を複数案ぶん作って見比べる**。漢字版のレイアウトは静止画6枚で選べず、20秒の音声つき動画3本で即決。残テの演出も20秒×3案で一回で決まった
- **レビューは一部分だけ書き出して回す**。アゲアゲ版は R1（約64秒）だけで判断し、全編（5分の描画）は最後
- **人が直せる面を先に作る**。表示文言の screen-text.md、リズムの一行テキスト、試聴ページのコメント欄
- **本人の試聴・視聴の反応を正とする**（sutra-videos/CLAUDE.md の運用方針）。機械検査（解像度・尺・欠字・全フレーム復号）は通っても、読み・面白さ・歌いやすさは本人の耳と目でしか決まらなかった

## 再利用できる部品

- `scripts/make_mantra_package.py` — 真言の JSON から横版・Shorts・サムネイル・概要欄を一括生成
- `scripts/make_sutra_package.py` — 長文経典のページ送り型同期動画
- `scripts/make_sutra_hype.py` — ビート同期のフレーム描画、EDM 伴奏、ビルド／ドロップ（1802行）
- `scripts/kakaiju_synth.py` — VOICEVOX 歌唱 API の呼び出し（他のスクリプトが共通で呼ぶ）
- `scripts/sutra_rhythm.py` / `validate_sutra_rhythm.py` — 人が書くリズム正本の読み取りと、本文のかなとの照合
- `scripts/canon_render_segment.py` — 区間の音声なし書き出しと連結

## Open Questions

- 同期解説の真言・偈の動画は公開パッケージまで作ってあるが、公開したか・どう受けたかの記録が sutra-videos に無い
- 公開した4本（カノン、アゲアゲ2本、真言言えるかな）の視聴者の反応は記録されていない
- 同期解説を embed（プレゼンに埋め込む概念解説）として使えるかは試していない。45秒・3回反復・ナレーションなしという形は、講演の中で流すには向いていそうだが未検証
