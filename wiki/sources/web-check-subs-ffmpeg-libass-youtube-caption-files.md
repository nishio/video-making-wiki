---
type: source
summary: 字幕を「焼き込む」ffmpeg の subtitles / ass フィルタ（libass。fontsdir・force_style・original_size・wrap_unicode・shaping）と、ASS の折り返しの指定（WrapStyle / \q の 0〜3）、「別ファイルで出す」ときの YouTube の対応形式（SRT・SBV は書式なし・UTF-8、WebVTT は位置のみ、SCC が推奨の放送形式、時刻なしの台本を自動で合わせる Auto-sync）。日本語は libass の自動折り返しに任せず、文節で切って \N を自分で入れ、WrapStyle=2 にする
video_types: [any]
url: https://ffmpeg.org/ffmpeg-filters.html#subtitles-1
author: FFmpeg 開発者／Aegisub（ASS のタグの文書）／Google（YouTube ヘルプ）
published: unknown（ffmpeg.org の文書は開発版に追従）／unknown（YouTube ヘルプ）
retrieved: 2026-11-09
sources:
  - https://ffmpeg.org/ffmpeg-filters.html（§11.5 ass、§11.250 subtitles）
  - https://aegisub.org/docs/latest/ass_tags/（\q、\N、\n）
  - https://support.google.com/youtube/answer/2734698（Supported subtitle and closed caption files）
  - https://support.google.com/youtube/answer/2734796（Add subtitles and captions。Upload file の With / Without timing、Auto-sync）
---

# 字幕の焼き込み（ffmpeg・libass）と字幕ファイルの書き出し（YouTube の対応形式）

## 何の文献か

- **ffmpeg-filters の公式文書**の ass / subtitles フィルタの節（2026-11-09 時点の ffmpeg.org。開発版の文書なので、galleria の ffmpeg 9.0.1 では `ffmpeg -h filter=subtitles` で手元の版のオプションを確かめる）
- **Aegisub の ASS タグの文書**（ASS 形式の上書きタグの解説。ASS の仕様書そのものではない）
- **YouTube ヘルプ**の 2 ページ（2026-11-09 時点）。配信先ごとの仕様の表は別の担当（check-spec）。ここは形式と手順だけ

## 書いてあること

### ffmpeg の subtitles / ass フィルタ

- subtitles: 「Draw subtitles on top of input video using the libass library.」`--enable-libass` でビルドされている必要がある。SRT などを ASS に変換してから描く
- ass: 「Same as the subtitles filter, except that it doesn't require libavcodec and libavformat to work. On the other hand, it is limited to ASS」
- 主なオプション（文書の原文の要旨）:
  - `filename, f`: 字幕ファイル。`subtitles=sub.srt` で可
  - `original_size`: 「Due to a misdesign in ASS aspect ratio arithmetic, this is necessary to correctly scale the fonts if the aspect ratio has been changed.」
  - `fontsdir`: 「Set a directory path containing fonts that can be used by the filter. These fonts will be used in addition to whatever the font provider uses.」
  - `charenc`: UTF-8 でないときだけ（subtitles のみ）
  - `force_style`: 「Override default style or script info parameters of the subtitles」。例: `subtitles=sub.srt:force_style='Fontname=DejaVu Serif,PrimaryColour=&HCCFF0000'`
  - `wrap_unicode`: 「Break lines according to the Unicode Line Breaking Algorithm.」libass 0.17.0 以上かつ libunibreak 付きのビルドが要る。「enabled by default except for native ASS」
  - `shaping`: `auto` / `simple` / `complex`（HarfBuzz。アラビア語などに必要）
- 文書の例: `subtitles=video.mkv:si=1`（動画に入っている 2 本目の字幕を描く）

### ASS の折り返し（Aegisub の \q の説明。スタイルの WrapStyle と同じ値）

- 0: 「Smart wrapping, make each line approximately equally long, but top line wider when equal width is impossible. Only `\N` forces line breaks.」
- 1: 行末まで詰めて折り返す。`\N` だけが強制改行
- 2: 「No word wrapping, wide lines will extend beyound the edges of the screen. Both `\n` and `\N` force line breaks.」
- 3: 0 と同じだが下の行を広く
- `\N` は強制改行。`\n`（小文字）は WrapStyle 2 のときだけ改行、他では空白になる

### YouTube の字幕ファイル（Supported subtitle and closed caption files）

| 区分 | 形式 | YouTube の記述（要旨） |
|---|---|---|
| 基本 | SubRip `.srt` | 「Only basic versions of these files are supported. No style info (markup) is recognized. The file must be in plain UTF-8.」 |
| 基本 | SubViewer `.sbv` / `.sub` | 同上 |
| 基本 | MPsub `.mpsub`、LRC `.lrc` | LRC は enhanced format に対応 |
| 基本 | Videotron Lambda `.cap` | 「primarily used for Japanese subtitles」 |
| 高度 | WebVTT `.vtt` | 「Positioning is supported, but styling is limited to <b>, <i>, <u>」 |
| 高度 | SAMI、RealText、TTML、DFXP | 書式は一部、TTML は「partial implementation」 |
| 放送 | SCC、EBU-STL など | 「Scenarist Closed Caption (.scc file extension) files are our preferred file format.」（CEA-608 に基づく字幕の場合） |

- ASS は一覧に無い。**ASS で作った見た目（字の大きさ・色・縁取り）は YouTube の字幕ファイルには持っていけない**
- 追加の方法（Add subtitles and captions）: Upload file で **With timing / Without timing** を選べる。**Auto-sync**: 「Transcript text is automatically synchronized to your video. The transcript must be in a language supported by our speech recognition technology. The transcript must also be in the same language that's spoken in the video. Transcripts are not recommended for videos that are over an hour long or have poor audio quality.」

## この wiki への含意

- **焼き込みか、別ファイルか**: 西尾の動画は字幕を絵として描いて焼き込む作りが多い（HTML Canvas で描く。[[exp-html-capture-pipeline]]、[[exp-democracy-river-video]]）。X は無音で自動再生されるので焼き込みが前提（同）。一方、学会（UIST・CHI）は字幕を**別ファイル（.srt / .sbv）で必須**にする（[[web-promo2-uist-chi-video-guides]]）。YouTube も別ファイルを出せば、視聴者が消せる・大きさを変えられる・自動翻訳が効く（BBC の closed 字幕の前提。[[web-type-bbc-subtitle-guidelines]]）。**同じ時間正本から、焼き込み用（ASS か HTML）と配信用（SRT / VTT）の両方を出す**のが筋（[[exp-sutra-sync-subtitles]] の Open Question「YouTube の字幕ファイルを同じ正本から作る範囲は未決」への答えの候補）
- **YouTube の Auto-sync** は「台本（時刻なし）を上げると YouTube が音声に合わせる」機能。公開後に字幕ファイルを足すだけなら、ローカルで整列（[[web-check-subs-whisperx-stable-ts-faster-whisper]]）をしなくても済む。ただし合わせた結果は YouTube の中にあり、焼き込みには使えない。日本語が対象か、精度はどうかは書いていない
- **日本語の改行は libass に任せない**: `wrap_unicode` の Unicode 改行規則では日本語はほぼどの字の間でも切れる（推測。UAX #14 の CJK の扱い）。BudouX で文節に分けて `\N` を入れ（[[web-check-subs-budoux]]）、ASS の `WrapStyle: 2`（自動で折り返さない）にする
- **galleria の Windows パスの落とし穴**: filter の引数の中では `\` と `:` が特別な意味を持つ（[[exp-galleria-ffmpeg-measurement-and-delivery]]）。`subtitles=` と `fontsdir=` にはカレントからの相対名を渡す
- 型: any。embed（会場で音を出さずに流すことがある）は焼き込みが前提。talk は焼き込み＋YouTube 用の別ファイル。promo（X）は焼き込み

## 着手の仕方（未検証。galleria で確かめる）

- **何ができるようになるか**: 時刻付きの字幕データ（整列の結果や時間正本）から、(1) 日本語フォントを指定した ASS を作って ffmpeg で焼き込む、(2) 同じデータから YouTube・学会用の SRT / VTT を出す。効く型: any
- **機械**: galleria WSL（ffmpeg は入っている）か Windows の ffmpeg 9.0.1（Gyan の full build。libass を含むはず、推測）
- **入れるもの**: 日本語フォント（例: Noto Sans JP。SIL Open Font License。フォントの利用条件は使う前に条文を読む）。費用 0、アカウント不要
- **成熟度**: ffmpeg・libass とも安定

### 最小の手順

```bash
# galleria WSL
mkdir -p ~/video-tools-trial/subs/fonts && cd ~/video-tools-trial/subs
ffmpeg -hide_banner -filters | grep -E " (ass|subtitles) "     # 2 行出れば libass 入り
ffmpeg -hide_banner -h filter=subtitles | grep -E "fontsdir|wrap_unicode|force_style"
# fonts/ に日本語フォント（例: NotoSansJP の .ttf/.otf）を置く
cat > sub.ass <<'EOF'
[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Noto Sans JP,64,&H00FFFFFF,&H000000FF,&H00000000,&H80000000,0,0,0,0,100,100,0,0,1,4,0,2,80,80,60,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.50,0:00:03.00,Default,,0,0,0,,字幕の改行は\N文節で切る
Dialogue: 0,0:00:03.20,0:00:05.50,Default,,0,0,0,,二枚目の字幕
EOF
ffmpeg -y -f lavfi -i "color=0x202020:s=1920x1080:r=30:d=6" -vf "ass=sub.ass:fontsdir=fonts" -c:v libx264 -pix_fmt yuv420p burn_test.mp4
ffmpeg -y -ss 1 -i burn_test.mp4 -frames:v 1 burn_test.png
# 配信用の別ファイル（ASS → SRT / VTT。書式は落ちる）
ffmpeg -y -i sub.ass sub.srt && ffmpeg -y -i sub.srt sub.vtt
```

- `Fontsize` 64 は 1080p で行の高さ約 6%（BBC の 16:9 の目安 7〜8% より少し小さい。[[web-type-bbc-subtitle-guidelines]]）。値は素材に合わせて決める
- `Fontname` はフォントファイルの中の名前（ファミリー名）と一致させる。`fc-scan fonts/*.otf | grep family`（WSL に fontconfig があれば）で確かめる
- SRT を直接焼くなら: `-vf "subtitles=sub.srt:fontsdir=fonts:force_style='FontName=Noto Sans JP,Fontsize=24,Outline=2'"`。SRT から変換した ASS は既定の解像度の座標で描かれるので、`Fontsize` の数値は ASS を直接書くときと意味が違う（ffmpeg の既定の値は文書に無い。推測）

### 動いたと言える確かめ方

- `burn_test.png` に日本語が豆腐（□）でなく出て、1 枚目が「字幕の改行は」「文節で切る」の 2 行になっている
- ffmpeg のログに `fontselect: (Noto Sans JP, ...) -> ...NotoSansJP...` のような行が出て、指定したフォントが選ばれている（別のフォントに置き換わったら名前が違う）
- `sub.srt` が UTF-8 で、YouTube Studio の Upload file（With timing）で読み込めて時刻が合う（アップロードは西尾が決める）
- 欠字の機械検査: 字幕に使う字を全部、フォントの cmap で照合する（fontTools。西尾の「目視では低頻度の字の豆腐を見落とす」。[[exp-sutra-sync-subtitles]]、[[exp-sutra-hype-editions]]）

### 所要の見込み（推測）

- 30〜60 分（フォント名の一致で詰まることが多い）

## Open Questions

- galleria の Windows 版 ffmpeg 9.0.1 の libass が `wrap_unicode`（libunibreak）付きか、fontconfig がどのフォントを見るか
- YouTube の Auto-sync が日本語で使えるか、精度はどうか（ヘルプは「speech recognition が対応する言語」としか書かない）
- 焼き込み字幕と YouTube の字幕ファイルを両方出すと、字幕を有効にした視聴者には二重に出る。焼き込みのある版で別ファイルを出すべきか（学会の必須要件は満たす必要がある）
- WebVTT の位置指定を使って、焼き込みのテロップと重ならない位置に配信用の字幕を出せるか
