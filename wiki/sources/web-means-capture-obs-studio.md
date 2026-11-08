---
type: source
summary: OBS Studio（v33.0.1、2026-10-29、GPL-2.0）の公式ナレッジベースと obs-websocket 5.x のプロトコル文書。録画の形式は Hybrid MP4（30.2〜。落ちても壊れにくく、章マーカーを入れられる）、NVENC などのハードウェア符号化、起動オプション（--profile・--scene・--startrecording 等）、内蔵の WebSocket（28〜、既定ポート 4455）で StartRecord／StopRecord／CreateRecordChapter を外から呼べる。galleria の Windows で、台本を動かす側と別に「画面全体・実機のカメラを撮る係」に置ける
video_types: [promo, talk, embed]
url: https://obsproject.com/kb/standard-recording-output-guide
author: OBS Project（ナレッジベース・GitHub）／obs-websocket-community-projects（obs-websocket-js）／Microsoft（WSL の docs）／BlankSourceCode（obs-zoom-to-mouse）
published: OBS 33.0.0 は 2026-10-23、33.0.1 は 2026-10-29。KB の各記事は 2021-05-30〜2024-06-06
retrieved: 2026-11-09
sources:
  - https://github.com/obsproject/obs-studio/releases（33.0.0 のリリースノート本文）
  - https://obsproject.com/kb/launch-parameters（2021-05-30）
  - https://obsproject.com/kb/standard-recording-output-guide（2023-05-26）
  - https://obsproject.com/kb/hybrid-mp4（2024-06-06）
  - https://obsproject.com/kb/remote-control-guide（2023-04-18）
  - https://obsproject.com/kb/hardware-encoding（2022-01-11）
  - https://obsproject.com/kb/window-capture-sources
  - https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md
  - https://github.com/obs-websocket-community-projects/obs-websocket-js（README、v5.0.8 2026-03-14）
  - https://github.com/MicrosoftDocs/wsl/blob/main/WSL/networking.md（ms.date 07/16/2024）
  - https://github.com/BlankSourceCode/obs-zoom-to-mouse（README）
---

# OBS Studio を台本から操作して録画する

## 何の文献か

- OBS Studio の公式ナレッジベース（KB）とリリースノート。OBS は配信・録画の OSS（GPL-2.0、star 約 79,000）。最新は **33.0.1（2026-10-29）**。33.0 は browser source の CEF を 127 → 150 に上げ、プラグインの読み込みを作り直した（既存の第三者プラグインは 34.0 まで旧い場所からも読む）
- obs-websocket のプロトコル文書（自動生成、5.x）。OBS 28 以降に内蔵
- obs-websocket-js（MIT、v5.0.8）の README。Node から呼ぶ側の公式ではない（コミュニティ）ライブラリ
- WSL のネットワークの Microsoft の docs（WSL から Windows 側のサーバーに繋ぐ方法）
- どれも機能の説明で、画質・負荷の測定は無い

## 書いてあること

### 録画の設定（KB「Standard Recording Output Guide」「Hybrid MP4」「Hardware Encoding」）

- 設定は Settings → Output。Recording Format について、古い記事（2023）は「MKV is recommended in case of unforeseen issues arising, since MKV will not corrupt the whole file if there is no graceful stoppage of recording」と書き、MP4 が要るなら File → Remux Recordings か「Automatically remux to mp4」を使えとする
- **Hybrid MP4**（30.2 で導入、Hybrid MOV は 32.0）: 「It remains recoverable even if writing the file is aborted, e.g. due to system crashes or power outages, while still maintaining wide compatibility」。書きながらは fragmented で、終わりに「soft-remux」で通常の MP4 に見せる。H.264・HEVC・AV1 と AAC・Opus 等に対応（ProRes は Hybrid MOV）
- **章マーカー**: Hybrid MP4 では、ホットキー・WebSocket の `CreateRecordChapter`・フロントエンド API で章を入れられ、「supported by most video players and editing suites such as DaVinci Resolve」。ただし「Chapters are written during the finalisation process, i.e. they are not recoverable in the event of a crash」
- **ハードウェア符号化**: 「Hardware encoders ... are generally recommended for best performance as they take the workload off the CPU」。NVENC は Windows と Linux で、「For best results, use a GPU with 6th generation NVENC (Turing)」以降
- **Window Capture の Capture Cursor** は既定で On（KB の表）

### 起動オプション（KB「Launch Parameters」）

- `--startrecording`、`--profile "name"`、`--collection "name"`、`--scene "name"`、`--minimize-to-tray`、`--portable`、`--disable-updater` など
- Windows では「To launch OBS Studio via scheduled tasks or other automated means, make sure to also set a working directory ("Start in...") which must point to the folder where obs64.exe is located」
- `--safe-mode` は第三者プラグイン・スクリプト・WebSocket を止める（33.0 で Safe Mode では WebSocket サーバーを起動しないよう変更）

### WebSocket（KB「Remote Control Guide」、protocol.md）

- 「WebSocket integration is now included by default with OBS Studio 28 and above」。Tools → obs-websocket Settings で有効化。パスワードは「highly recommended」。コマンドラインで `--websocket_port`・`--websocket_password` を上書きできる
- 録画の要求: `StartRecord`、`StopRecord`（応答に `outputPath`）、`PauseRecord`／`ResumeRecord`、`SplitRecordFile`（5.5.0〜）、`CreateRecordChapter`（5.5.0〜、「As of OBS 30.2.0, the only file format supporting this feature is Hybrid MP4」）。イベント `RecordStateChanged` は停止時に `outputPath` を返す。シーン切り替えは `SetCurrentProgramScene`、ソースの表示は `SetSceneItemEnabled`
- ホットキーを WebSocket から押す要求もあるが「In 9/10 usages of hotkey requests, there exists a better, more reliable method via other requests」
- obs-websocket-js の既定の接続先は `ws://127.0.0.1:4455`。`await obs.connect(url, password)` → `await obs.call('StartRecord')`

### WSL から Windows の OBS に繋ぐ（WSL docs）

- 既定の NAT モードでは、WSL から Windows 側のサーバーには `localhost` でなく **ホストの IP** で繋ぐ: `ip route show | grep -i default | awk '{ print $3}'`
- Windows 11 22H2 以降で `.wslconfig` に `networkingMode=mirrored` を書くと、「the Windows host and WSL2 VM can connect to each other using localhost (127.0.0.1)」
- WSL 2.0.9 以降では Hyper-V firewall が既定で有効（Windows 側のファイアウォールが効く）

### 自動ズームは OBS 本体に無い（obs-zoom-to-mouse）

- 第三者の Lua スクリプト obs-zoom-to-mouse（star 約 1,200）は「zoom a display-capture source to focus on the mouse」。「Built with OBS v29.1.3」、Windows・Linux・Mac 対応と書く。最終 push は 2024-06-07、リポジトリに license の表示が無い。収録中にホットキーでズームする方式で、後から直せない

## この wiki への含意

- **OBS は「撮る係」、台本は別に持つ**。OBS は画面・ウィンドウ・カメラ・音を合成して録る係で、何をどう操作するかは持たない。台本は Playwright（[[web-means-capture-playwright-screencast]]）や手の操作で持ち、OBS は WebSocket で始め・止め・章を打つ。章マーカーを台本の拍ごとに打てば、編集で拍の位置を探さずに済む（推測）
- **Playwright の録画と比べた使いどころ**: ブラウザの中だけなら Playwright の録画で足りる（OBS は要らない）。OBS が要るのは、(1) ブラウザ以外（デスクトップアプリ、Unity、ComfyUI の UI、端末と複数ウィンドウ）、(2) 実機のカメラ（USB のカメラやキャプチャーボード）と画面を同時に録る、(3) Windows のフォント・GPU の描画のまま撮りたい、とき
- **Playwright で動かした操作を OBS で撮るとき、OS のカーソルは動かない**（推測。Cap の cap-demo skill が「virtual input only (CDP mouse/keyboard — the user's real cursor is never touched)」と書くのと同じ仕組み。[[web-means-capture-cap]]）。OBS の Capture Cursor はオフにし、Playwright の `showActions` のカーソルを画面に描かせる
- THINKLET のデモは iPhone で撮った縦の映像と画面のスクリーンショットを Premiere で並べた（[[exp-thinklet-reading-demo-video]]）。OBS なら「カメラ（実機）＋画面」を 1 つのシーンにして同時に録れる。撮った後に並べる手間が減るが、配置は撮る前に決めることになる
- 画面録画は VFR になりやすい（[[exp-galleria-ffmpeg-measurement-and-delivery]]）。OBS の録画は設定した FPS の CFR で出るはず（推測。KB には明記が無い）。ffprobe で確かめる

## 着手の仕方（未検証。galleria で確かめる）

- **表現できるようになること**: Windows の画面・アプリ・実機のカメラを、台本のスクリプトから録画の開始・停止・章打ちをして撮る。効く型: promo（作品の実画面）、talk（画面＋話し手のカメラ）、embed（操作の流れ）
- **機械**: galleria Windows（OBS）。台本のスクリプトは Windows 側の node か、WSL から（ホスト IP か mirrored モード）
- **入れるもの**: OBS Studio 33.0.1（obsproject.com のインストーラ。winget の ID は未確認）、Node のライブラリ `obs-websocket-js@5.0.8`（Windows 側の作業フォルダに npm で）。費用 0、アカウント不要。GPL-2.0（使って撮るだけなら条件は撮った動画に及ばない、と読むのが普通だが、条文の該当箇所は読んでいない）。NVENC を使う（RTX 5080。GPU の負荷は小さいはず、VRAM の見込みは公式の記述なし）
- **成熟度**: 33.0 が 2026-10、毎月の点リリース。WebSocket の 5.x は 2022 から同じ形
- **最小の手順**:
  1. OBS を起動し、Settings → Output を Advanced、Recording の Format を **Hybrid MP4**、Encoder を NVIDIA NVENC H.264、Settings → Video を 1920×1080・60（または 30）fps。Profile 名 `demo`、Scene Collection 名 `demo`、シーン `screen`（Display Capture か Window Capture）を作る（GUI。一度だけ）
  2. Tools → obs-websocket Settings で Enable、パスワードを設定（パスワードは repo に書かない。環境変数 `OBS_PW` で渡す）
  3. Windows の PowerShell で:
     ```powershell
     mkdir $HOME\video-tools-trial\obs-ctl; cd $HOME\video-tools-trial\obs-ctl
     npm init -y; npm i obs-websocket-js@5.0.8
     ```
     `rec.mjs`（obs-websocket-js の README と protocol.md の要求名から組んだもの）:
     ```js
     import { OBSWebSocket } from 'obs-websocket-js';
     const obs = new OBSWebSocket();
     await obs.connect('ws://127.0.0.1:4455', process.env.OBS_PW);
     await obs.call('SetCurrentProgramScene', { sceneName: 'screen' });
     await obs.call('StartRecord');
     const wait = ms => new Promise(r => setTimeout(r, ms));
     await wait(2000); await obs.call('CreateRecordChapter', { chapterName: 'beat1' });
     await wait(3000); await obs.call('CreateRecordChapter', { chapterName: 'beat2' });
     await wait(2000);
     const { outputPath } = await obs.call('StopRecord');
     console.log('OUTPUT', outputPath);
     await obs.disconnect();
     ```
     `node rec.mjs`
  4. WSL から呼ぶ場合: `HOST=$(ip route show | grep -i default | awk '{print $3}')` で `ws://$HOST:4455` に繋ぐ（Windows のファイアウォールで 4455 を通す要あり。推測）
- **動いたと言える確かめ方**: `OUTPUT C:\...\2026-11-10 ...mp4` が表示され、`ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate,avg_frame_rate -show_chapters <file>` で h264・1920×1080・r と avg が一致（CFR）し、章が 2 つ（beat1・beat2）出る
- **所要の見込み（推測）**: OBS の設定 30 分、スクリプト 30 分

## Open Questions

- OBS の録画が本当に CFR か（Hybrid MP4・NVENC の組み合わせで avg_frame_rate を測る）
- 章マーカーは Premiere・DaVinci Resolve で読めると KB は書くが、ffprobe・Python から読む手順（`-show_chapters`）で取れるかは未確認
- obs-zoom-to-mouse（2024-06 が最後、OBS 29 で作成）が OBS 33 の新しいプラグイン読み込みの下で動くか。license の表示が無いので、配布物に含めない
- 起動オプション `--startrecording` と WebSocket の `StartRecord` のどちらで始めるのが、録画の頭の空白を短くできるか
