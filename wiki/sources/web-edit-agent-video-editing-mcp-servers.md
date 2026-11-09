---
type: source
summary: 動画編集を LLM のエージェントに触らせる MCP サーバーの README を 2026-11-09 に読み比べたページ。編集ソフトを操作するもの（DaVinci Resolve 4 本、Premiere 2 本、Final Cut Pro の FCPXML 1 本）、ffmpeg を道具として出すもの（ffmpeg-skill、clipwright ほか）、クラウドの編集サービスにつなぐもの（ChatCut、Kapwing、Video Jungle）に分かれる。Resolve 系は Studio 前提か「Resolve の中で動く橋」で無料版を回避、Premiere 系は CEP の橋が本命で UXP は試験的、ffmpeg 系は素材を外に出さない。どれも個人の OSS で、匿名のテレメトリが既定で有効なものがある
video_types: [any]
url: https://github.com/samuelgursky/davinci-resolve-mcp
author: 各 repo の作者（samuelgursky、emircbngl、flamexnreal、hetpatel-11、leancoderkavy、DareDev256、kajisho5、satoh-y-0323、misbahsy、ChatCut-Inc、burningion）／Kapwing
published: 各 repo の最終 push・リリースは本文の表（2026-11-09 に GitHub API で取得）
retrieved: 2026-11-09
sources:
  - https://github.com/samuelgursky/davinci-resolve-mcp（v4.19.3 2026-11-06）
  - https://github.com/emircbngl/davinci-resolve-mcp-free
  - https://github.com/flamexnreal/davinci-resolve-ai-bridge-mcp（v1.14.3 2026-11-07）
  - https://github.com/hetpatel-11/Adobe_Premiere_Pro_MCP（v1.2.11 2026-10-24）
  - https://github.com/leancoderkavy/premiere-pro-mcp（v1.30.0 2026-11-08）
  - https://github.com/DareDev256/fcp-mcp-server（v0.30.0 2026-11-02）
  - https://github.com/kajisho5/ffmpeg-skill（v3.2.3 2026-11-07）
  - https://github.com/satoh-y-0323/clipwright（v0.41.0 2026-08-12）
  - https://github.com/misbahsy/video-audio-mcp（2025-05-24 以後更新なし）
  - https://github.com/ChatCut-Inc/agent-plugin（v1.11.1 2026-11-05）
  - https://github.com/burningion/video-editing-mcp（最終 push 2025-10-09）
  - https://www.kapwing.com/resources/how-to-edit-videos-with-claude-code-free-ai-video-editing-skill/（2026-11-04、Kapwing MCP の節）
---

# 動画編集の MCP サーバー（2026-11-09 時点）

## 何の文献か

GitHub の検索（「davinci resolve mcp」「premiere mcp」「ffmpeg mcp」「video editing mcp」「fcpxml mcp」「otio mcp」、star 順）で出た repo の README と、GitHub API の数字（star・作成日・最終 push・最新リリース・ライセンス）。star 数は参考程度。**どれもインストール・実行していない**（CyEC2 では動かさない決まり）。README の「できる」「実測した」は作者の申告で、このページでは確かめていない。Resolve 21.1 の組み込みの MCP（Blackmagic 製）は [[web-edit-agent-davinci-resolve-premiere-scripting]] に書いた。

## 書いてあること

### 一覧

| repo | 何を操作するか | star | 作成 → 最終 push | 最新リリース | ライセンス |
|---|---|---|---|---|---|
| samuelgursky/davinci-resolve-mcp | Resolve（公式の scripting API） | 4,001 | 2025-03 → 2026-11-06 | v4.19.3（2026-11-06） | MIT |
| emircbngl/davinci-resolve-mcp-free | Resolve 無料版（Lua の橋・FCPXML・macOS の UI 操作） | 17 | 2026-05 → 2026-10-15 | なし | MIT |
| flamexnreal/davinci-resolve-ai-bridge-mcp | Resolve 無料版・Studio（Lua の橋） | 47 | 2026-07 → 2026-11-07 | v1.14.3（2026-11-07） | MIT |
| hetpatel-11/Adobe_Premiere_Pro_MCP | Premiere（CEP の橋。UXP は試験的） | 835 | 2025-07 → 2026-11-02 | v1.2.11（2026-10-24） | MIT |
| leancoderkavy/premiere-pro-mcp | Premiere（UXP と CEP/ExtendScript） | 499 | 2026-02 → 2026-11-08 | v1.30.0（2026-11-08） | MIT |
| DareDev256/fcp-mcp-server | Final Cut Pro の FCPXML（ファイル）と起動中の FCP | 140 | 2026-01 → 2026-11-02 | v0.30.0（2026-11-02） | MIT |
| kajisho5/ffmpeg-skill | ffmpeg（42 の道具、skill と MCP の両方） | 4,826 | 2026-09-03 → 2026-11-07 | v3.2.3（2026-11-07） | MIT |
| satoh-y-0323/clipwright | ffmpeg と OTIO、whisper.cpp | 3 | 2026-06 → 2026-08-12 | v0.41.0（2026-08-12） | MIT |
| misbahsy/video-audio-mcp | ffmpeg | 89 | 2025-05-24 のみ | なし | MIT |
| ChatCut-Inc/agent-plugin | ChatCut（クラウド＋デスクトップの編集アプリ） | 1,018 | 2026-06 → 2026-11-06 | v1.11.1（2026-11-05） | Apache-2.0 |
| burningion/video-editing-mcp | Video Jungle（クラウド） | 296 | 2024-12 → 2025-10-09 | なし | なし |
| Kapwing MCP（`https://www.kapwing.com/mcp`） | Kapwing（クラウド） | ― | ― | ― | サービス |

### DaVinci Resolve 系

- **samuelgursky/davinci-resolve-mcp**: 「lets AI assistants control DaVinci Resolve Studio through the official Scripting API」。既定は 37 の tool（関連操作を束ねる）、`--full` で 390（API の関数 1 つに 1 tool）。「API Coverage 100%」「Live Tested 93.6%」のバッジ。Resolve 18.5 以上、Python 3.10 以上。`npx davinci-resolve-mcp setup` が Claude Code などの設定まで書く
  - 無料版: 「Blackmagic gates *external* scripting to Studio」。21.0.x までは Scripts のメニューから起動する橋（loopback、HMAC 署名）で回避できたが「Resolve 21.1 moved Python scripting to Studio」。「This is the documented in-app path, not a licence circumvention, but Blackmagic could close it」
  - 素材の扱い: 「This project treats camera originals and source media as immutable」。分析（ffprobe・ffmpeg・Whisper）の結果は脇のファイルに書く
  - テイク選び: 「Performance is most of what makes a take right, and none of it is measurable from a waveform or a transcript. `rank_takes` ranks *fluency* — fillers, restarts, script coverage — and says so in every response」
  - Resolve を起動しないで `.drp`/`.drt` を読み書きする別の Node のサーバー（advanced、18 tool）も同梱
- **emircbngl/davinci-resolve-mcp-free**: Resolve の中で動く Lua の橋・FCPXML の書き出し・macOS のアクセシビリティ API での UI 操作で無料版を回す。「verified on 20.3; written for 21.1's restricted Lua, not yet tried on a 21.1 install」。README は Studio を「~$295」と書く（製品ページは 2026-11-09 時点で $236）
- **flamexnreal/davinci-resolve-ai-bridge-mcp**: 「Lua editing is verified on macOS Free 21.1.2.10」。「Windows, Linux and other builds still need live verification」。複製した timeline で試してから元に触る、を売りにする

### Premiere 系

- **hetpatel-11/Adobe_Premiere_Pro_MCP**: 283 の tool を `search_tools`／`invoke_tool` の裏に置く（常に見えるのは一部）。「**CEP is the supported production bridge; UXP remains experimental**」。`premiere-pro-mcp --install-cep` が「enables the required Adobe CEP debug setting」。Premiere 2020 以上、Node 20 以上、同じ機械で動かす
  - 「**Anonymous usage telemetry is on by default**」。送るのは install id・OS・版・失敗した tool 名など、「Project names, media paths, arguments, and results are not sent」。`PREMIERE_MCP_TELEMETRY=0` で止める
- **leancoderkavy/premiere-pro-mcp**: 「447 core tools across 68 modules ... A connected UXP host adds 98 capability-gated tools」。UXP の経路は Premiere 25.6 以上で「Live loopback WebSocket」。Premiere の AI 機能（Generative Extend・Object Mask・文字起こしなど）を「direct, observable-only, artifact-import, external-provider, user-assisted, unavailable, or planned」に分けた表を返す tool がある。Opus 5.5 の節は「Model selection belongs to the client; this server does not run an Anthropic model ... Keep Premiere mutations serialized and preview before apply」

### Final Cut Pro

- **DareDev256/fcp-mcp-server**: FCP から書き出した FCPXML を Claude が読み書きし、起動中の FCP に送り込む。「15 grouped tools, 102 operations: trims, splits, silence removal, markers from transcripts and beats, rough cuts ... cross-NLE export」。「Every write is journaled with its sha256 and can be undone. `deliver` refuses an unreviewed cut」。FCP 10.4〜12.x。Mac 専用（FCP が Mac のみ）

### ffmpeg 系（素材を外に出さない）

- **kajisho5/ffmpeg-skill**: 「Give your coding agent a video editor ... No cloud · No API keys · Python standard library」。42 の道具（切る・つなぐ・無音の削除・尺と縦横比の合わせ・字幕とカラオケ・重ね・ラウドネス・納品の検査など）。MCP の `tools/list` は既定で 12 に絞る。CI で ffmpeg 6.1・7.1・8・9 を試験。作者は「It does not decide what to cut, whether a deliverable is approvable, what makes a highlight interesting, or what a caption should say ... those are a *brain*'s job」と書き、判断は別の repo に分けている
- **satoh-y-0323/clipwright**: 「MCP server group wrapping FFmpeg/OTIO」。文字起こしは whisper.cpp（`whisper-cli` と ggml のモデルを別に用意）。手ぶれの検出は libvidstab 入りの ffmpeg が要る。日本語の README がある。star 3、最終 push 2026-08-12
- **misbahsy/video-audio-mcp**: ffmpeg の切る・つなぐ・重ね・字幕の焼き込み・無音の削除。2025-05-24 の 1 日だけで更新が止まっている

### クラウドの編集サービス

- **ChatCut**: 「an MCP server and plugin that lets Codex, ChatGPT, Claude Code ... edit your own footage, add captions and subtitles, remove silences and filler words」。デスクトップ版（ローカルの MCP）か Web 版（OAuth）。「Generation uses ChatCut credits, and the agent asks before spending them」。要: ChatCut のアカウント
- **Kapwing MCP**（Kapwing の自社記事、2026-11-04）: `claude mcp add --transport http kapwing https://www.kapwing.com/mcp`。素材を Kapwing のワークスペースに上げ、字幕・翻訳・吹き替え・書き出し。「editing and AI generation are subject to the limits and credits of your Kapwing plan」。結果は Kapwing のタイムラインで人が直せる
- **Video Jungle**（burningion）: 要: アカウントと API キー。2025-10 以後更新なし

## 何を AI に任せられるか

- **作者が書いていること**: 編集ソフトの操作（取り込み・timeline の組み立て・マーカー・書き出し・名前の整理・色の適用）、ffmpeg の作業（無音の削除・切り貼り・字幕・ラウドネス）、クラウドでの字幕・翻訳・吹き替え
- **実例で確かめられたこと**: samuelgursky は「Live Tested 93.6%」（API の関数を実機で呼んだ割合。編集の出来ではない）。DareDev256 は FCP を起動したまま 10 クリップにマーカーと役割を付ける録画を出している。どれも「LLM が良い編集をした」ことの評価ではない
- ffmpeg-skill の作者は道具（手）と判断（頭）を分け、この repo は判断しないと明言している

## 何が人の判断として残るか

- samuelgursky の README: テイクの良し悪しの大半は「演技」で、波形や文字起こしからは測れない。`rank_takes` は流暢さ（言いよどみ・言い直し・台本の網羅）だけを順位付けし、そう毎回言う
- DareDev256: 人が見ていないカットは `deliver` が拒む。leancoderkavy: 変更は 1 つずつ、適用の前にプレビュー
- Kapwing: 「Neither approach guarantees a publication-ready result ... Both still require you to review the final video for pacing, accuracy, and visual quality」（自社記事。宣伝の性格がある）

## 日本語の対応

- MCP の README で日本語の文字起こし・日本語の切り抜きを試したと書くものは見つからなかった。hetpatel-11・leancoderkavy・clipwright は README の日本語訳を置いている（UI の言葉の話で、日本語の素材の処理の話ではない）
- 文字起こしは各サーバーが外の道具（Whisper、whisper.cpp、Resolve・Premiere の内蔵）に任せるので、日本語の精度はその道具次第

## 費用・アカウント・利用条件

- OSS の MCP 自体は MIT（Video Jungle の MCP は LICENSE なし）。無料
- 動かす先の費用: Resolve Studio $236（Resolve 系の多く）、Premiere は Creative Cloud、FCP は Mac の有料アプリ、ChatCut・Kapwing・Video Jungle はアカウントとクレジット（**要: アカウント・費用、西尾が決める**）。クラウドの 3 つは素材を先方に上げる。規約（素材の扱い・AI 学習への利用）は**今回読んでいない**
- テレメトリ: hetpatel-11 の Premiere MCP は既定で匿名の利用統計を送る（止め方あり）。会社の機械で使うかは西尾が決めること（[[web-means-3d-blender-bpy-cli]] の blender-mcp と同じ論点）
- 「CEP の debug setting を有効にする」（hetpatel-11）は Premiere の署名のない拡張を読む設定。Premiere の CEP は 2028-12 に既定で無効になる（[[web-edit-agent-davinci-resolve-premiere-scripting]]）

## この wiki への含意

- **西尾の経験の方式（コードで描いて 1 コマずつ撮る、[[exp-html-capture-pipeline]]）では編集ソフトを使っていない**。編集ソフトの MCP が効くのは「実物を撮って編集する」側（[[work-promotion-video]] の暫定の答えの 1）と、THINKLET のように人が編集ソフトで組む場合（[[exp-thinklet-reading-demo-video]]）
- **galleria で最初に試すなら ffmpeg 系**: 素材を外に出さず、費用もアカウントも要らない。ffmpeg-skill は WSL の ffmpeg と python3 だけで動くと書く。編集ソフト系は Resolve Studio の購入か Premiere の契約が先に要る
- **shortmovie-draft-generator との対応**: [[exp-shortmovie-draft-generator]] の 1 は「エージェントがツールで企画案・カットを追加・更新・削除する」形で、MCP の形に近い（ただし自前のツールで、MCP ではない）。字幕の時刻を正にして LLM に触らせない、という経験の設計は、MCP の作者たちの「journal・sha256・プレビューしてから適用」と同じ「LLM に壊させない」側の工夫

## 着手の仕方（未検証。galleria で確かめる）

- **何ができるようになるか**: Claude Code に ffmpeg の道具を MCP で渡し、「無音を詰める」「9:16 にする」「ラウドネスを -14 LUFS に」を頼み、出力を道具自身の検査で確かめる。効く型: promo（縦の切り抜き）、talk（講演の録画の詰め）
- **機械**: galleria WSL。入れるもの: `ffmpeg-skill`（npm、v3.2.3）。ffmpeg と python3 は既にある。Node は `~/.local/bin` にある。費用 0、アカウント不要。素材は外に出ない
- **成熟度**: 2026-09-03 作成、2 か月で v3.2.3。star 4,826。更新は続いているが若い
- **最小の手順**（README の Quick start と MCP の設定例を元にした。WSL）:
  ```bash
  cd ~/video-tools-trial/mcp && cp /path/to/talk.mp4 .
  npx ffmpeg-skill            # Claude Code 用に ~/.claude/skills/ffmpeg-skill へ skill を入れる
  npx ffmpeg-skill doctor     # ffmpeg・ffprobe と各フィルタの有無。doctor --json の tools を見る
  # skill として使うならこのまま。MCP として使うなら README の設定例
  #   {"mcpServers": {"ffmpeg-skill": {"command": "python3", "args": ["~/.claude/skills/ffmpeg-skill/mcp/server.py"]}}}
  claude   # 「talk.mp4 の 0:45–3:10 と 5:00–6:30 を残して 60 秒の 9:16 にして」（README の例の形）
  ```
  README の例では、エージェントが `probe.py` → `cut.py --segments ...` → `fit.py --duration 60 --aspect 9:16 --fit crop` → `export.py --preset reels` → `check.py --platform reels` → `look.py` と回し、「final.mp4: 59.98 s, 1080×1920, 30 fps」と、見たコンタクトシートを報告する。音声から字幕を作るには faster-whisper を別に入れる（モデルを初回にダウンロード。音声は外に出ない、と書く）
- **動いたと言える確かめ方**: (1) 出力の mp4 の長さが元より短く、道具が返す JSON の「削った秒数」と ffprobe の差が 1 コマ以内。(2) `ffmpeg -i out.mp4 -af ebur128 -f null -` の Integrated が -14 LUFS ±1（[[web-check-loudness-ffmpeg-loudnorm-ebur128]]）。(3) Claude Code の会話に、道具の検査（check）の結果が出ている
- **所要の見込み（推測）**: 1 時間

## Open Questions

- Resolve 21.1 の組み込み MCP（Blackmagic 製）が出たあと、第三者の Resolve MCP（samuelgursky ほか）はどう住み分けるか。samuelgursky は 2026-11-06 にもリリースしている
- ffmpeg-skill の「無音の削除」が日本語の話し方（文末の間・言いよどみ）でどう切るか
- クラウドの 3 つ（ChatCut・Kapwing・Video Jungle）の規約で、アップロードした素材が AI の学習に使われるか（未読）
- star の多さと実際の使われ方の関係（ffmpeg-skill は 2 か月で 4,800）。宣伝で伸びた可能性は否定できない

