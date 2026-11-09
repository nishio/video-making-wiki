---
type: source
summary: 編集ソフトを外のプログラム（エージェント）から動かす口。DaVinci Resolve の scripting API（README v21.0.4）は Python/Lua で timeline の作成・区間を指定した追加・マーカー・書き出しまでできるが、外部のプロセスからの接続は Studio（$236）だけ。21.1（2026-09-08）で Studio に Claude Code などとつなぐ組み込みの MCP サーバーが入り、外部からの scripting は Studio の機能と明記された（業界誌の記事による。Blackmagic の一次資料は未読）。Premiere は UXP（JavaScript、Premiere の中で動くプラグイン）が正式になり、CEP は 2027-12 に新規受付停止・2028-12 に既定で無効・2029-12 に同梱終了と Adobe が公表した。ExtendScript はこの移行の対象外で終了日は無い
video_types: [any]
url: https://extremraym.com/cloud/resolve-scripting-doc/
author: Blackmagic Design（Resolve の scripting README。X-Raym による写し）／Adobe（Premiere UXP の docs・Developer Blog・Developer Forums・release notes）
published: Resolve README は「Last Updated: 24 Jul 2026 - v21.0.4」。Adobe の CEP 移行の blog は 2026-09-24。フォーラムの回答は 2026-08-28
retrieved: 2026-11-09
sources:
  - https://extremraym.com/cloud/resolve-scripting-doc/（README.txt の整形版。X-Raym は 21.1 以後の更新をしないと書く）
  - https://www.blackmagicdesign.com/products/davinciresolve（DaVinci Resolve 21、Studio $236）
  - https://github.com/samuelgursky/davinci-resolve-mcp（README の「Free edition」の節、v4.19.3 2026-11-06）
  - https://dev.to/depsir/unlock-the-secrets-of-automating-davinci-resolve-with-python-free-version-edition-1fkn
  - https://digitalproduction.com/2026/09/08/resolve-21-1-adds-mcp-and-finally-gets-presets/（2026-09-08）
  - https://ymcinema.com/2026/09/17/davinci-resolve-21-1-mcp-ai-assistants-control-edit/（2026-09-17）
  - https://developer.adobe.com/premiere-pro/uxp/ ・ https://developer.adobe.com/premiere-pro/uxp/introduction/
  - https://blog.developer.adobe.com/en/publish/2026/09/investing-in-the-future-of-creative-cloud-extensibility-uxp-comes-to-our-flagship-applications（2026-09-24）
  - https://forums.creativeclouddeveloper.com/t/cep-to-uxp-what-developers-need-to-know/12189（2026-09-25）
  - https://forums.creativeclouddeveloper.com/t/uxp-api-parity-for-mogrt-parameter-control-current-extendscript-support-status/12131（2026-08-28）
  - https://helpx.adobe.com/premiere-pro/kb/fixed-issues.html（release notes、26.0〜26.5.2）
---

# DaVinci Resolve の scripting API と Premiere の UXP／ExtendScript

## 何の文献か

- **Resolve**: Blackmagic がアプリに同梱する `Developer/Scripting/README.txt`。Web に公式の掲載が無いので、X-Raym（Resolve のスクリプトの作者）が整形して公開している写し（v21.0.4、2026-07-24 更新）を読んだ。X-Raym は「v21.1 で原文の書式が変わり、自分のコードが追従しないので更新の予定はない」と書いている。無料版と Studio の差は、README に書かれていない部分を DaVinci Resolve MCP の README と、無料版で使う人のブログで補った。Blackmagic のフォーラム（社員の発言があるとされるスレッド）は 403 で読めず、Internet Archive にも無かった
- **Premiere**: Adobe の開発者向け docs（UXP）、Adobe Developer Blog（2026-09-24、CEP の移行の日程）、Adobe の開発者フォーラムでの Adobe 側の回答（2026-08-28）、Premiere の release notes
- 種類: 公式ドキュメント（README・docs・release notes・blog）、フォーラムでの社員の回答、第三者の README とブログ

## 書いてあること

### DaVinci Resolve の scripting API（README v21.0.4）

- Lua 5.1 と Python（3.6 以上 64bit、2.7 64bit）。「DaVinci Resolve needs to be running for a script to be invoked」
- 呼び方: Fusion ページの Console、コマンドライン、Workspace > Scripts のメニュー。「This permission can be changed in Resolve Preferences, to be only from Console, or to be invoked from the local network. Please be aware of the security implications」
- 外から呼ぶには `RESOLVE_SCRIPT_API`・`RESOLVE_SCRIPT_LIB`（Windows は `C:\Program Files\Blackmagic Design\DaVinci Resolve\fusionscript.dll`）・`PYTHONPATH` を設定し、`import DaVinciResolveScript as dvr_script; resolve = dvr_script.scriptapp("Resolve")`
- **headless**: 「DaVinci Resolve can be launched in a headless mode without the user interface using the -nogui command line option ... the various scripting APIs will continue to work as expected」
- 編集に効く関数（README の表から）:
  - `MediaPool.AppendToTimeline([{clipInfo}])`: `mediaPoolItem`・`startFrame`・`endFrame`・`mediaType`（1 映像のみ／2 音声のみ）・`trackIndex` を指定して区間を追加
  - `MediaPool.CreateTimelineFromClips(name, [{clipInfo}])`: 区間の一覧から timeline を作る（`recordFrame` も指定可）
  - `MediaPool.ImportTimelineFromFile(filePath, {importOptions})`: 「AAF/EDL/XML/FCPXML/DRT/ADL/OTIO」
  - `Timeline.Export(...)`: `EXPORT_OTIO`・`EXPORT_EDL`・`EXPORT_FCPXML_1_8`〜`1_10` ほか
  - `Timeline.DeleteClips([items], ripple)`、`AddMarker(frameId, color, name, note, duration, customData)`、`SetCurrentTimecode`
  - `Timeline.DetectSceneCuts()`（場面の切れ目を検出してカットを入れる）、`Timeline.CreateSubtitlesFromAudio({autoCaptionSettings})`、`MediaPoolItem.TranscribeAudio(useSpeakerDetection)`
- **無料版と Studio**（README の「Studio and AI Scripting APIs」）: 「The DaVinci Resolve scripting APIs cover a common superset of functions for both the Free and Studio versions」。Studio の機能を無料版で呼ぶと False が返る。IntelliSearch・Slate ID・音声生成などは Extras のダウンロードが要る
- **README（v21.0.4）には「外部からのスクリプトは Studio のみ」とは書いていない**（写しを通読して見当たらなかった）。21.1 で Blackmagic がそう明記したと業界誌が書く（下の節）。それ以前の挙動を書いているのは次の第三者:
  - DaVinci Resolve MCP の README: 「Blackmagic gates *external* scripting to Studio: on the free edition `scriptapp("Resolve")` refuses a foreign process, whatever the preference says」。21.0.x までは Workspace > Scripts のメニューから起動したスクリプトには `resolve` が渡される（無料版 21.0.3.7 で実測と書く）ので、Resolve の中で動く小さなスクリプトがローカルの listener を立てて橋渡しする。「**Resolve 21.1 moved Python scripting to Studio.** On free 21.1 the Scripts menu no longer lists `.py` files at all」（Fedora の利用者の報告、issue #203。Lua は出る）
  - 無料版のブログ（dev.to、Francesco）: 「The free version does not allow standalone python scripts to interact with DaVinci Resolve」。Scripts のメニューに置けば `resolve`・`fusion`・`bmd` が使える
  - X-Raym: 「Without any mention in the v19.1 changelog, Blackmagic just removed UIManager for the free version」
### Resolve 21.1（2026-09-08）: Studio に組み込みの MCP サーバー、Python の外部操作は Studio に

Blackmagic の一次資料（21.1 の release notes・Reference Manual）は今回取れなかった（製品ページ・media ページに記述が見つからず、manual は 4,300 ページ超の PDF）。以下は業界誌の記事による（どちらも manual と Blackmagic の発表を引いている）。

- Digital Production（2026-09-08）: 「the native MCP server in DaVinci Resolve Studio」「Resolve Studio 21.1 can connect to Claude, Claude Code and ChatGPT Codex, with setup handled through File > Setup AI Assistants」。Blackmagic の例は「take a long video from the Media Pool, turn it into a three-minute highlight edit, remove edits shorter than one second and render the result as H.265 for review」。記者は「What Blackmagic does not explain in its primer is ... permissions, safeguards around destructive operations, logging」と書く
- 同記事の scripting の変更: 「Blackmagic labels Advanced Scripting as a Studio feature, but the scripting API remains available from the console in the free edition. Workflow Integrations, the native UIManager and **external scripting access require Resolve Studio**」。理由として Blackmagic は「the Python API had been used to unlock Studio functionality from the free edition」と説明した、と書く。21.1 で scripting API が 20 増え、「retrieve Media Pool transcriptions with speaker and timing data」「create and flatten multicams」などができる。Python 2 は廃止
- YMCinema（2026-09-17）: manual の 4,318 ページに「Using DaVinci Resolve with AI Assistants」の節。設定画面のスクリーンショットに Claude Desktop・Claude Code・Codex in ChatGPT・Google Antigravity・Grok が並ぶ。manual の例は「render the current timeline as ProRes 422 HQ, H.265 4K, and a 1080p H.264 proxy」「rename every clip on V1 sequentially」「reframing a timeline to 9:16 vertical」など。記者は「The creative decisions remain with the person operating the system」と書く（記者の意見）
- 21.2 が 2026-11 上旬に出た（CineD の見出し。本文は読んでいない。MCP・scripting に変更があるかは未確認）
- 上の README（v21.0.4）は 21.1 より前の版。21.1 以後の README は今回読めていない

- 価格（製品ページ、2026-11-09）: 無料版あり。**Studio $236**（買い切り）。Studio は「DaVinci AI Neural Engine ... text based editing, magic mask ...」を加える。無料版は「8-bit video formats at up to 60fps in resolutions as high as Ultra HD 3840 x 2160」

### Premiere の UXP／CEP／ExtendScript

- UXP: 「a JavaScript-based extensibility platform (ES6/ECMAScript 2015 compliant)」「UXP is not a Browser」。Premiere の DOM API で「sequences, tracks, clips, markers, project items」を扱い、UXP の JS API に「File system, networking, shell execution」がある（docs のトップ）。UXP は「Premiere (version 25.6)」から（introduction）。Adobe の社員はフォーラムで「UXP API support, in 25.4 (MAX 2025)」と書いており、版の書き方が揃っていない
- **UXP はプラグインとして Premiere の中で動く**。外のプログラムから直接呼ぶ口（Resolve の `scriptapp` に当たるもの）は docs のトップに無い。エージェントから動かすには、プラグインが WebSocket などで外と話す橋を作る（Premiere の MCP がそうしている。[[web-edit-agent-video-editing-mcp-servers]]）
- **CEP の終了の日程**（Adobe Developer Blog、2026-09-24）:
  - 「CEP no longer works reliably, and we will retire it at the end of 2029」
  - 「Premiere stops accepting new CEP submissions in December 2027 ... move to CEP-disabled-by-default in December 2028」。無効化されても「users can easily turn it back on」
  - 「Starting December 2029, CEP will no longer be included in these apps」
  - 「**ExtendScripts are not affected by this transition**」
- ExtendScript の状況（フォーラム、Adobe の社員 bbb_999 の回答、2026-08-28）: 「no removal of CEP or ExtendScript from Premiere has been planned or scheduled」「Is ExtendScript expected to continue working after September 2026? Yes.」「Will existing ExtendScript functionality remain supported until equivalent UXP APIs are available? That is our plan, yes.」。以前に言われた「2026-09 の終了」はこの時点で否定されている（9 月 24 日の blog で CEP は 2029 まで、と日程が出た）
- UXP にまだ無いもの（フォーラムの開発者の報告）: 配置済みの MOGRT のパラメータの読み書き（Adobe は「coming soon」「MAX 2026」と回答）、シーケンスの再生・停止（2026-10-12 の投稿。QE の ExtendScript でしかできない）
- release notes の関連（Premiere）:
  - 26.0（2026-01）: OTIO の読み込みと書き出し。fixed issues に「UXP did not have the equivalent of ExtendScript's ability to get the frame rate of a sequence」
  - 26.2（2026-04）: 「Export sequences to FCP XML and OTIO formats, and access a new scripting API for the Preset Object. Also includes support for the UXP Hybrid Plugin workflow」
  - 26.5（2026-09）: 「Create sequences from transcripts with **Paper Edit**. Select multiple lines of transcript in the Text panel and use them to quickly construct sequences」。音声認識に新しい Voice Activity Detection のモデル

## 何を AI に任せられるか

- **公式（README）が書いていること**: Resolve の API で、区間を指定して timeline を組む（`AppendToTimeline` の clipInfo）、マーカーを打つ、場面の切れ目を検出する、文字起こし・字幕を作る、OTIO/EDL/FCPXML で書き出す、headless で動かす。つまり「LLM が決めた区間の一覧を、Resolve のタイムラインにする」ところまで API でできる。Premiere は UXP の DOM API で sequence・track・clip・marker を扱える（何がどこまでできるかの表は docs の各ページ。今回は通読していない）
- Resolve Studio 21.1 の組み込み MCP について Blackmagic が挙げる例（業界誌による）は「長い動画から 3 分のハイライト、1 秒未満の編集を除き、H.265 で書き出す」「複数の形式で書き出す」「クリップの名前を揃える」「9:16 にリフレーム」。ハイライトの選択まで例に入っている
- Premiere 26.5 の Paper Edit（文字起こしの行を選んで sequence を作る）は、人が行を選ぶ機能。エージェントが行を選ぶ API があるかは確かめていない
- **実例で確かめられたこと**: このページの文献には無い。MCP の側の報告は [[web-edit-agent-video-editing-mcp-servers]]

## 何が人の判断として残るか

- 文献はどちらも API の文書で、編集の判断について書いていない
- Resolve の README は外部からのスクリプトを「security implications」として、許可を Console のみ／ローカル／ネットワークで人が選ぶ設定にしている。エージェントに編集ソフトを触らせる許可は人が決める前提

## 日本語の対応

- Resolve の `TranscribeAudio`・`CreateSubtitlesFromAudio` が日本語に対応するかは README に書かれていない（「Transcription workflows with extended language models」は Extras 要、とだけ）。Resolve の UI は日本語化されている（製品ページの jp 版がある）が、文字起こしの言語は未確認
- Premiere の文字起こしは日本語を含む多言語に対応している（Adobe のヘルプにあるはず。今回は release notes しか読んでいない。未確認）
- API の文字列（クリップ名・マーカー名）に日本語を渡せるかは、どちらも docs に記述が無い

## 費用・アカウント・利用条件

- Resolve: 無料版は手で OTIO/EDL/FCPXML を読み込めるが、エージェントから外部スクリプトで動かすには **Studio $236（買い切り。要: 購入、西尾が決める）**。21.1 からは無料版で Python のスクリプト自体が動かないという報告（MCP の README）。外部スクリプトの許可を「Local」にすると、ローカルの別プロセスから Resolve を操作できるようになる
- Premiere: Creative Cloud の契約（要: アカウント・費用）。UXP のプラグインは開発者モード（UXP Developer Tool）で読み込むか、Marketplace・社内配布。CEP の拡張は 2028-12 から既定で無効
- どちらもローカルで動き、素材を外に送らない（API 自体は）。Studio の AI 機能（IntelliSearch など）が外に送るかは README に記述なし

## この wiki への含意

- **Premiere で手編集した経験（[[exp-thinklet-reading-demo-video]]）をエージェントに渡す道は、今は Resolve の方が近い**: Resolve は Python で外から timeline を組め（Studio）、21.1 からは Claude Code をつなぐ MCP が Studio に組み込まれた。Premiere は UXP のプラグインを書いてプラグイン経由で話す形で、外からの API が無い。西尾の Premiere は 25.0（Mac）で、UXP の正式版（25.6）も OTIO（26.0）も無い版
- **ただし外からの操作でなくてもよい**: LLM が OTIO を書き、人が手で読み込む（[[web-edit-agent-opentimelineio-edl-fcpxml]]）なら、Resolve 無料版・Premiere 26 のどちらでも API は要らない。API が要るのは「エージェントが自分で読み込み・書き出し・やり直しまで回す」とき
- **headless の Resolve は galleria で回せる形**: `-nogui` で起動して Python で timeline を組み、Deliver で書き出す。ffmpeg だけの方式（[[web-edit-agent-moviepy-ffmpeg-concat]]）との違いは、出力が「編集ソフトで開ける timeline」として残ること
- **CEP 前提のものは寿命が見えている**: Premiere の MCP の多くは CEP の橋（[[web-edit-agent-video-editing-mcp-servers]]）。Premiere では 2028-12 に既定で無効、2029-12 に同梱終了

## 着手の仕方（未検証。galleria で確かめる）

- **何ができるようになるか**: LLM が書いた区間の一覧から、Resolve の timeline を API で組み、OTIO と mp4 で書き出す。効く型: promo・talk（収録の組み立て）
- **機械**: galleria Windows（Resolve は Windows アプリ。WSL からは Windows の python.exe を呼ぶ形になる見込み、推測）。入れるもの: DaVinci Resolve 21（無料版で手の読み込み、Studio で API）。**要: Studio の購入 $236（西尾が決める）**。外部スクリプトの許可を Preferences > General > External scripting using = Local
- **別の道（Studio 21.1 以上）**: File > Setup AI Assistants で Claude Code を組み込みの MCP につなぎ、「cuts.json の区間で timeline を作って」と頼む（業界誌の記述による。手順は manual で確かめる）。下の Python は、MCP に頼らず再現できる形を残すための版
- **成熟度**: README は 21.0.4（2026-07-24）。21.1 で無料版の Python が外れたという報告。Studio なら API は 15 系から続く
- **最小の手順**（Windows の PowerShell。README の環境変数と例を元にし、clipInfo の組み方は README の表から。区間はコマ数）:
  ```powershell
  $env:RESOLVE_SCRIPT_API="$env:PROGRAMDATA\Blackmagic Design\DaVinci Resolve\Support\Developer\Scripting"
  $env:RESOLVE_SCRIPT_LIB="C:\Program Files\Blackmagic Design\DaVinci Resolve\fusionscript.dll"
  $env:PYTHONPATH="$env:PYTHONPATH;$env:RESOLVE_SCRIPT_API\Modules\"
  # Resolve Studio を起動しておく（または Resolve.exe -nogui）
  python cuts_to_resolve.py C:\trial\talk.mp4 C:\trial\cuts.json
  ```
  `cuts_to_resolve.py`（推測で書いた最小形）:
  ```python
  import json, sys, DaVinciResolveScript as dvr
  resolve = dvr.scriptapp("Resolve"); assert resolve, "Studio で External scripting = Local か確かめる"
  pm = resolve.GetProjectManager(); proj = pm.CreateProject("agent-draft") or pm.GetCurrentProject()
  mp = proj.GetMediaPool(); item = mp.ImportMedia([sys.argv[1]])[0]
  c = json.load(open(sys.argv[2])); fps = c["fps"]
  infos = [{"mediaPoolItem": item, "startFrame": round(s*fps), "endFrame": round(e*fps)} for s, e in c["ranges"]]
  tl = mp.CreateTimelineFromClips("draft", infos)
  print(tl.GetName(), tl.GetStartFrame(), tl.GetEndFrame(), len(tl.GetItemListInTrack("video", 1)))
  tl.Export(r"C:\trial\draft.otio", resolve.EXPORT_OTIO, resolve.EXPORT_NONE)
  ```
- **動いたと言える確かめ方**: (1) `scriptapp` が None でない（None なら無料版か許可の設定）。(2) 出力の行で、映像トラック 1 のクリップ数が `ranges` の数と同じ、`GetEndFrame - GetStartFrame` が区間の合計のコマ数と一致。(3) `draft.otio` が書かれ、[[web-edit-agent-opentimelineio-edl-fcpxml]] のスクリプトで読み戻せる。(4) 無料版 21.x で同じスクリプトを Workspace > Scripts から起動したときに動くか（21.0 と 21.1 で違うという報告の確かめ）
- **所要の見込み（推測）**: Studio があれば 1 時間。無料版での確かめだけなら 30 分

## Open Questions

- 「外部からのスクリプトは Studio のみ」「組み込みの MCP は Studio」は、21.0.4 の README に無く、業界誌（21.1 の発表と manual を引用）・第三者の README・ブログによる。Blackmagic の 21.1 の release notes と manual の該当節（4,318 ページ）を直接読んでいない
- 組み込みの MCP が何の tool を出すか（業界誌は 88 という数も挙げるが出典が不明）、破壊的な操作の確認・ログの仕組み（Digital Production が「説明が無い」と書く）
- 21.1 で無料版の Python がメニューから消えたのは Linux（Fedora）の報告。Windows の無料版でも同じか
- Premiere の UXP の正式版は 25.4 か 25.6 か（Adobe の docs と社員の発言が食い違う）
- Premiere の UXP から外のプロセスと話す正規の方法（UXP の networking で WebSocket のクライアントになる、が MCP の形）。Adobe が外部からの操作をどう位置づけているかの文書は見つからなかった
- Resolve・Premiere の文字起こしの日本語の精度

## Updates
