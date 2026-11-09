---
type: source
summary: LLM に切り貼りのプログラムを書かせるときの 2 つの下回り。MoviePy（v2.2.1、2025-05-21、MIT）は v2.0 で import・メソッド名・エフェクトが総入れ替えになり、LLM が v1 の書き方（moviepy.editor、set_、subclip）を書くと動かない。ffmpeg に比べて遅いと README 自身が書き、メンテナを募集している。ffmpeg（9.0.2、2026-09-18）の concat demuxer の inpoint/outpoint はキーフレームの間では正確に切れないと公式が書く。エージェント向けの道具は「区間ごとに書き出して -c copy でつなぐ」と「1 つの filter graph で trim してつなぐ」で割れている
video_types: [any]
url: https://zulko.github.io/moviepy/getting_started/updating_to_v2.html
author: MoviePy（Zulko ほか）／FFmpeg（ffmpeg-formats の docs）／browser-use（video-use の SKILL.md）／Frank Heijdenrijk（video-editing-skill、dev.to）
published: MoviePy v2.2.1 は 2025-05-21（最後の commit は 2026-08-17 の docs の修正）。FFmpeg 9.0.2 は 2026-09-18。dev.to の記事は 2026-10-30
retrieved: 2026-11-09
sources:
  - https://zulko.github.io/moviepy/getting_started/updating_to_v2.html
  - https://zulko.github.io/moviepy/getting_started/install.html
  - https://github.com/Zulko/moviepy（README、release v2.2.1、commits）
  - https://pypi.org/project/moviepy/（2.2.1、2025-05-21）
  - https://ffmpeg.org/ffmpeg-formats.html#concat-1（3.6 concat）
  - https://ffmpeg.org/download.html（9.0.2「Lei」2026-09-18、8.1.3 2026-09-21）
  - https://github.com/browser-use/video-use/blob/main/SKILL.md（Hard Rules）
  - https://dev.to/fheijdenrijk/video-editing-skill-for-claude-code-an-agent-that-plans-every-cut-then-renders-with-ffmpeg-518a（2026-10-30）
---

# MoviePy と ffmpeg の concat／trim（LLM に切り貼りを書かせる下回り）

## 何の文献か

- MoviePy の公式 docs（v1 → v2 の移行ガイド、インストール）と GitHub の README・リリース・commit 履歴
- FFmpeg の公式 docs（ffmpeg-formats の concat demuxer の節）と download ページ
- エージェント向けの編集の道具 2 つが書く「切り貼りの正しいやり方」: browser-use の video-use の SKILL.md（Hard Rules）と、video-editing-skill の作者の dev.to 記事（作者は WoopSocial の関係者で、記事の末尾に開示がある。宣伝の性格がある）。2 つの全体は [[web-edit-agent-video-use-and-claude-code-editing-examples]]
- 種類: 公式ドキュメント・README・実務ブログ。どれも速度や精度を比べて測った表は出していない

## 書いてあること

### MoviePy v2

- 最新は **v2.2.1（2025-05-21、PyPI・GitHub）**。それ以後のリリースは無い。commit は 2025-09 と 2026-07〜08 の docs の修正だけ（GitHub API、2026-11-09）
- README: 「MoviePy recently upgraded to v2.0, introducing major breaking changes ... v1 is no longer maintained」。「**Maintainers wanted!** this library has only been kept afloat by the involvement of its maintainers, and there are times where none of us have enough bandwidth」
- 仕組み（README）: 「MoviePy imports media ... and converts them into Python objects (numpy arrays) so that every pixel becomes accessible ... This makes MoviePy very flexible and approachable, **albeit slower than using ffmpeg directly**」
- ffmpeg との関係（install の docs）: 読み書きは ffmpeg に頼る。既定（`FFMPEG_BINARY` が `ffmpeg-imageio`）では imageio が**初回に ffmpeg のバイナリを自動でダウンロード**して使う。`"auto-detect"` にすると手元の ffmpeg を使う。プレビューには ffplay が要る
- v1 → v2 の破壊的変更（移行ガイドから）:
  - `moviepy.editor` が無くなった。`from moviepy import VideoFileClip` のように直接 import する
  - `.set_*` はすべて `.with_*` に（元を変えずに写しを返す）。`clip.resize` → `resized`、`crop` → `cropped`、`rotate` → `rotated`。README の例では `subclip` → `subclipped`、音量は `with_volume_scaled`
  - エフェクトは関数からクラスに。`clip.fx(...)` は無くなり `with_effects([...])`
  - ImageMagick・PyGame・OpenCV・scipy などへの依存をやめ、画像は Pillow に。`TextClip` は**フォントファイルのパスが必須**になった
  - 消えた機能: `moviepy.video.tools.tracking`・`segmenting`・`io.sliders`
  - 「there is a high likelihood that your pre-v2.0 programs will not run without some changes」

### ffmpeg の concat demuxer（公式 docs の 3.6 concat）

- 「All files must have the same streams (same codecs, same time base, etc.)」。タイムスタンプは各ファイルの長さでずらすので、長さが不正確だと「it can cause artifacts」
- `inpoint`: 「This directive works best with intra frame codecs, because for non-intra frame ones you will usually get extra packets before the actual In point and the decoded content will most likely contain frames before In point too」
- `outpoint`: 排他的（その時刻以降のパケットは出さない）。非イントラのコーデックでは「additional packets ... after Out point」が出ることがある
- つまり、H.264 の画面収録を `-c copy` のまま concat demuxer の inpoint/outpoint で切ると、**キーフレームの位置に引きずられて指定より前後のコマが入る**と公式が書いている。正確に切るには再エンコードが要る（docs の記述からの帰結）
- 版: 9.0.2「Lei」（2026-09-18、9 系の最新）、8.1.3（2026-09-21）、7.1.5（2026-06-20）

### エージェント向けの道具の「切り貼りの決まり」（食い違っている）

- **video-use（browser-use）の Hard Rules**:
  - 「Per-segment extract → lossless `-c copy` concat, not single-pass filtergraph. Otherwise you double-encode every segment when overlays are added.」（区間ごとに再エンコードして書き出し、つなぐときだけ `-c copy`）
  - 「30ms audio fades at every segment boundary ... Otherwise audible pops at every cut.」
  - 「Subtitles are applied LAST in the filter chain」「Overlays use `setpts=PTS-STARTPTS+T/TB`」
  - 「Never cut inside a word」「Pad every cut edge. Working window: 30–200ms. Scribe timestamps drift 50–100ms」
- **video-editing-skill（dev.to、2026-10-30）**:
  - 「Cutting hundreds of pieces as separate files and concatenating them lets audio and video drift by a few milliseconds per join, which adds up」。だから**区間の端をコマの格子に丸め、60 区間ずつ 1 つの filter graph の中で `trim`／`atrim` → `setpts=PTS-STARTPTS` → `concat=n=N:v=1:a=1`** でつなぐ
  - 区間の端の音は 4 ms の fade（「stop clicks without dipping the room tone」）。書き出し後に音と映像の長さを比べ、1 コマ以上ずれたら `manifest.json` に警告
  - 「Transcribers often put a word's end 50 to 150 ms early」。音量を 10 ms 窓で測り、Out は最大 250 ms 後ろへ、In は最大 200 ms 前へ動かす
- 両者とも「LLM は区間を決め、切り貼りは決まったスクリプトがやる」という分担は同じ。違うのは**つなぎ方**（区間ファイル＋copy か、1 グラフか）と**端の音の fade の長さ**（30 ms か 4 ms か）

## 何を AI に任せられるか

- **道具の作り手が書いていること**: LLM に任せるのは「どの区間を残すか（理由付き）」。切り貼り・fade・字幕の時刻の付け替えは決まったスクリプト（video-use の `render.py`、video-editing-skill の `edit_video.py`）。どちらも LLM に ffmpeg のコマンドを毎回一から書かせる形ではない
- **実例で確かめられたこと**: video-editing-skill の作者は、NASA の公開インタビュー 6:39 → 5:57（12 カット）の例を repo に置いている（作者の報告。手元では見ていない）
- MoviePy に LLM がコードを書く場合、学習データに多い v1 の書き方（`moviepy.editor`、`set_duration`、`subclip`、`clip.fx`）を書くと v2.2.1 では動かない（移行ガイドの記述からの推論。LLM が実際にどれだけ間違えるかを測った文献は見つからなかった）

## 何が人の判断として残るか

- video-editing-skill は「Possible retakes」（同じ書き出しの 2 文）を**自動では切らず**、エージェントと人が 1 つずつ決めると書く。「like」「so」のような口癖も既定では切らない（opt-in）
- video-use は「Strategy confirmation before execution. Never touch the cut until the user has approved the plain-English plan」を Hard Rule に入れている
- 下回り（MoviePy・ffmpeg）の文献は判断について何も書いていない

## 日本語の対応

- ffmpeg・MoviePy は言語に依らない。字幕を焼くときのフォントは別の問題（MoviePy v2 の `TextClip` はフォントファイルのパスが必須。日本語は Noto CJK などのパスを渡す。[[web-means-font-fontconfig-noto-cjk-linux]]）
- 「単語の境界で切る」「単語の前後に 30〜200 ms」の規則は、単語ごとの時刻を返す文字起こしが前提。日本語の単語の時刻は文字起こしの道具次第（[[web-check-subs-whisperx-stable-ts-faster-whisper]]、[[web-check-subs-qwen3-forcedaligner-mfa-reazonspeech]]）。日本語で 30 ms の余白が足りるかを測った文献は見つからなかった

## 費用・アカウント・利用条件

- MoviePy: MIT。ffmpeg: LGPL/GPL（ビルドによる）。どちらも無料・アカウント不要。素材は外に出ない
- MoviePy の既定は初回に ffmpeg を自動ダウンロードする。galleria WSL では既にある ffmpeg を使うため `FFMPEG_BINARY=auto-detect` にする（install の docs の設定）

## この wiki への含意

- **経験と一致**: [[exp-shortmovie-draft-generator]] の 1 は、LLM がカット区間を作り、切り出し・縦動画化・concat・字幕の焼き込み・BGM を決まった ffmpeg のコード（`video_processing.py`）がやる分担だった。2026-10 の 2 つの道具も同じ分担。違いは、経験の道具には**区間の端の fade と単語境界への吸着が無い**こと（コードから読める範囲。音の「プツッ」が出たかの記録は無い）
- **「3 秒延長」との対応**: 西尾が入れた「全カットの end に 3 秒足す」（[[exp-shortmovie-draft-generator]]）は、文献の「文字起こしは単語の終わりを 50〜150 ms 早く置く」「Out を最大 250 ms 後ろへ」と同じ向きの補正。ただし 3 秒は桁が 1 つ大きく、YouTube の字幕の chunk の終わりの粗さか、切り抜きの余韻のためか（Open Question のまま）
- **Mac の解説動画の合成**: Mac 側で解説動画のために、ffmpeg の overlay で THINKLET のデモと Gyazo の動画を枠に重ねた（`~/video-making-explainer` の `compose.py`）。**この機械（CyEC2）には無いので読めない**。video-use の Hard Rule 4（overlay は `setpts=PTS-STARTPTS+T/TB` で開始時刻に合わせる）と Rule 1（字幕は最後）が、その合成で効いていたか・ずれが出たかは Mac 側で compose.py を読んで突き合わせる
- 計測の側は既存の [[exp-galleria-ffmpeg-measurement-and-delivery]]（galleria での ffmpeg の測り方）と [[web-check-loudness-ffmpeg-loudnorm-ebur128]] がそのまま使える。video-use も最後に `ebur128` で測れ（「You cannot listen: say so, and report the numbers」）と書く

## 着手の仕方（未検証。galleria で確かめる）

- **何ができるようになるか**: LLM が書いた区間の JSON から、ffmpeg で「切ってつないだ下書き」を作る。2 つのつなぎ方を同じ素材で比べ、どちらで音と映像がずれるかを測る。効く型: promo・talk（収録の詰め）。embed（流しっぱなしの短い解説）は素材を切るより描く方が多い
- **機械**: galleria WSL。入れるもの: なし（ffmpeg は WSL に既にある）。MoviePy を試すなら `uv run --with moviepy==2.2.1`。費用 0、アカウント不要
- **成熟度**: ffmpeg は 9.0.2（2026-09-18）。MoviePy は 2.2.1 から 1 年半リリースなし、メンテナ募集中
- **最小の手順**（WSL。ffmpeg の docs の構文を元にし、比べ方はこのページの提案）:
  ```bash
  cd ~/video-tools-trial/cut
  # A: 区間ごとに再エンコードして書き出し、copy でつなぐ（video-use の形）
  i=0; for r in "12.40 25.10" "40.00 58.30"; do set -- $r; i=$((i+1))
    d=$(echo "$2 - $1" | bc)
    ffmpeg -y -ss $1 -i talk.mp4 -t $d -c:v libx264 -crf 18 -c:a aac \
      -af "afade=t=in:st=0:d=0.03,afade=t=out:st=$(echo "$d - 0.03" | bc):d=0.03" seg$i.mp4
    echo "file 'seg$i.mp4'" >> list.txt; done
  ffmpeg -y -f concat -safe 0 -i list.txt -c copy A.mp4
  # B: 1 つの filter graph で trim してつなぐ（video-editing-skill の形）
  ffmpeg -y -i talk.mp4 -filter_complex \
   "[0:v]trim=12.40:25.10,setpts=PTS-STARTPTS[v0];[0:a]atrim=12.40:25.10,asetpts=PTS-STARTPTS[a0];\
    [0:v]trim=40.00:58.30,setpts=PTS-STARTPTS[v1];[0:a]atrim=40.00:58.30,asetpts=PTS-STARTPTS[a1];\
    [v0][a0][v1][a1]concat=n=2:v=1:a=1[v][a]" -map "[v]" -map "[a]" B.mp4
  for f in A.mp4 B.mp4; do ffprobe -v error -show_entries stream=codec_type,duration -of csv=p=0 $f; done
  ```
- **動いたと言える確かめ方**: (1) A・B とも長さが 12.70＋18.30＝31.00 秒から 1 コマ（1/30 秒）以内。(2) 各ファイルの映像の長さと音声の長さの差が 1 コマ以内（ffprobe の `stream=duration`）。(3) 区間を 20 個に増やした版で、A と B の音と映像の長さの差が増えるかを表にする（video-editing-skill の「つなぐごとに数 ms ずれる」の確かめ）。(4) つなぎ目の ±1 秒をコンタクトシート（[[web-check-spec-ffmpeg-contact-sheet-select-tile-drawtext]]）で見て、前の区間のコマが混ざっていないか
- **所要の見込み（推測）**: 1 時間。20 区間の比較まで入れて 2 時間

## Open Questions

- 「区間ファイル＋`-c copy` でつなぐ」と「1 つの filter graph」のどちらで音と映像のずれが出るか。2 つの道具の主張が食い違っていて、どちらも測った数字は出していない
- 区間の端の音の fade は 30 ms（video-use）か 4 ms（video-editing-skill）か。部屋の音（room tone）が落ちて聞こえるかは耳で確かめるしかない
- MoviePy v2 を LLM に書かせると v1 の書き方をどのくらい混ぜるか。ffmpeg を直接書かせる方が壊れにくいか
- 経験の「3 秒延長」が何を直していたか（上の含意）

## Updates
