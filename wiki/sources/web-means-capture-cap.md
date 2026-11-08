---
type: source
summary: OSS の画面収録アプリ Cap（CapSoftware/Cap、v0.6.2 2026-10-28、macOS・Windows・Linux）の README・docs・CLI の README・同梱の skill。Studio Mode で録ると、カーソルとクリックのデータからクリック位置のズームを生成できる。CLI（`cap record start/stop`、`cap export`）が JSON で話し、AI エージェントから操作する前提で作られている。コードは AGPLv3（一部 MIT）だが、配布されるアプリは「商用目的には商用ライセンスが要る」（年 $29 か買い切り $58）。雇い主の製品の宣伝・デモの制作は商用目的に含む、と書いている
video_types: [promo, talk, embed]
url: https://github.com/CapSoftware/Cap
author: Cap Software, Inc.（README・docs・CLI README・skill）
published: v0.6.2 は 2026-10-28（最終 push 2026-11-08）
retrieved: 2026-11-09
sources:
  - https://github.com/CapSoftware/Cap/blob/main/README.md
  - https://github.com/CapSoftware/Cap/blob/main/LICENSE
  - https://github.com/CapSoftware/Cap/blob/main/apps/cli/README.md
  - https://github.com/CapSoftware/Cap/blob/main/apps/cli/skill/cap/SKILL.md
  - https://github.com/CapSoftware/Cap/blob/main/apps/cli/skill/cap-demo/SKILL.md
  - https://cap.so/docs/recording/studio-mode
  - https://cap.so/docs/installation
  - https://cap.so/docs/commercial-license
  - https://cap.so/pricing
---

# Cap — CLI で操作できる OSS の画面収録アプリ

## 何の文献か

- 会社 Cap Software が作る OSS の画面収録アプリの一次資料（README、docs、CLI の README、同梱の Claude Code 等向けの skill 2 つ）。star 約 24,700。宣伝を兼ねる文書で、効果の測定は無い
- 自称「Open source alternative to Loom」。共有リンク・コメントなど Loom 型の機能と、Screen Studio 型の編集（Studio Mode）の両方を持つ

## 書いてあること

### 2 つの録画モード（README、docs「Studio Mode」）

- Instant Mode は録りながらアップロードして停止と同時に共有リンク。Studio Mode は「Record locally, edit with Cap's full timeline and canvas tools」。「Nothing is uploaded just because you record or edit in Studio Mode」
- **自動ズーム**: 「For Studio recordings that contain Cap's recorded cursor and click data, select Click to generate zoom segments to create zooms around recorded clicks」。「Automatic generation is not available when the project does not contain the required cursor metadata. Imported MP4s, for example, do not gain click data during import」
- 手動ズームは 1x〜4.5x、焦点を指定。クリップごとに 0.25x〜8x の速度、クロスフェード。カメラがあるときは Scene トラック（Camera Only・Hide Camera・Split Screen・Floating）。マスク（Sensitive はぼかし・モザイク、Highlight は外を暗く）は「do not automatically follow a moving window」。テキストのトラック
- 対応: Apple Silicon と Intel の Mac、64-bit Windows、64-bit Linux（.deb）（docs「Installation」）

### CLI（apps/cli/README.md）

- 「The `cap` binary is built for automation and AI coding agents (Claude Code, Codex, OpenCode, Cursor): every command speaks JSON, errors are machine-readable, and recordings have an explicit start/stop lifecycle」
- 入れ方: デスクトップアプリの Settings → Command Line → Install CLI、または Windows の PowerShell で `irm https://cap.so/install-cli.ps1 | iex`（デスクトップアプリが無ければ先に入れる）。「The desktop app and the CLI share the same binary」
- 典型の流れ:
  ```sh
  cap doctor --json
  cap targets --json
  cap record start --screen <id> --json --detach
  cap record stop --id <recordingId> --json   # {"type":"stopped","path",...,"recordingMetaExists":true}
  cap project validate <path.cap> --json
  cap export <path.cap> --output out.mp4 --json
  ```
- skill（SKILL.md）は「A stopped recording is complete only when `recordingMetaExists` is `true`」と書き、アップロード・課金・削除などの変更の前に利用者の確認を取れ、と決めている
- `cap project config get|set` で .cap プロジェクトを編集できる、とあるが、ズームの区間を CLI から足す方法は README には書かれていない

### cap-demo skill（macOS のみ）

- 「Give it a URL, get back a short, cinematic product-demo video」。頁を headless で下見し、**headed のブラウザを「virtual input only (CDP mouse/keyboard — the user's real cursor is never touched)」で動かし**、Cap の CLI で録り、3D のカメラ・ブランド色の背景・**後から合成したカーソル**・音楽を付けて MP4 にする
- 「macOS only (for now)」（ウィンドウの撮り方と Playwright の Chromium の置き場所が macOS 依存）
- 決まり（Hard editorial rules）: 全体 12 秒まで、「A camera cut MUST be a content cut」、「Cut on action, trim dead time」（読み込み中のコマを残さない）、「One motion system ... Never stack 2D zoom segments on 3D shots」、「The on-screen cursor is synthesized post-hoc from the logged glide path」
- 落とし穴として、「`cap record --detach` can engage late and the window capture stalls timestamps on static pixels, so the true rate is often ~58, not 60」。ffprobe で実際の fps を測り、60 か 58 かを確かめてから書き出しの fps を決めろ、と書く
- 決定論的なモードは「~70% quality」、エージェントがコマを見て直すモードは「~95% quality」と書く（測り方の記述は無い。宣伝的な自己評価）

### ライセンスと料金

- LICENSE: `cap-camera*` と `scap-*` の crate は MIT、それ以外は **AGPLv3**
- docs「Commercial License」: 「Cap Desktop is free to use, but requires a commercial license to be used for commercial purposes」。「This license does not apply to versions of the app you build yourself from our source code, only to binaries that we distribute」
- 商用目的の定義: 「any use of Cap Desktop for recording or editing content that will be used as part of revenue-generating activities. This includes but is not limited to: **Producing content for promotion or demonstration of your employer's product or service**; Producing content for communication between team members of a company」
- 料金（2026-11-09 の pricing）: 個人利用は無料（「no time limit on local recordings」）。Desktop License は **年 $29**（または買い切り **$58**）で商用利用権・Studio Mode・月 25 本の共有リンク。Cap Pro は 1 人月 $12（年払いで月 $8.16）でクラウド・AI の文字起こし等
- README の「Get Started」の 2 番目は「Sign in or create an account」、docs の「Verify the installation」の 1 番目も「Sign in to Cap Desktop」

## この wiki への含意

- **galleria（Windows）で使える自動ズームの候補**で、CLI があるので Claude Code から回せる。ただし自動ズームの根拠は「録ったカーソルとクリックのデータ」で、Playwright の CDP 入力では OS のクリックが起きない（cap-demo 自身が virtual input では本物のカーソルは動かないと書き、カーソルを後から合成している）。**台本で動かす撮影に自動ズームは期待できず、寄りは台本側から渡す**（[[web-means-capture-ffmpeg-zoompan-screenstudio-alt]]）
- **cap-demo の決まりは、西尾の promo の経験と同じ向き**。「読み込み中のコマを残すな」「死んだ時間を詰めろ」は西尾の「死んだ拍」（[[exp-polis-magi-op]]）、「カメラの切り替えは中身の切り替えに合わせる」「動きの体系は 1 つ」は howseen の「一度に動くのは 1 つ」（[[web-opus-howseen-claude-motion-design]]）と同じ。ただし「読み込みを詰める」は待ち時間を隠すことでもあり、THINKLET のデモが待ちを説明に変えたのとは逆（[[exp-thinklet-reading-demo-video]]、[[web-promo2-gemini-nikola-staged-demos]]）
- **58 fps 問題は経験と一致**: 画面録画は VFR になりやすい（[[exp-galleria-ffmpeg-measurement-and-delivery]]）。どの収録手段でも、書き出しの前に ffprobe で実際の fps を測る、が共通の手順
- **商用ライセンスは西尾が決めること**。西尾の作品の promo が「雇い主の製品・サービスの宣伝・デモ」に当たるかで要否が変わる。迷うなら、自分でソースからビルドした版は対象外（docs の記述）、または MIT の OpenScreen（[[web-means-capture-openscreen]]）を使う

## 着手の仕方（未検証。galleria で確かめる）

- **表現できるようになること**: Windows の画面を CLI から録り、GUI でクリック位置のズーム・カメラの配置・マスク・文字を付けて書き出す。効く型: promo、talk（話し手のカメラ）、embed
- **機械**: galleria Windows（CLI は PowerShell）。WSL からは Windows の実行ファイルを呼ぶ形になる（推測。`cap.exe` を WSL から直接呼べるかは未確認）
- **入れるもの・費用・アカウント**: Cap Desktop（v0.6.2、cap.so/download の Windows .exe）＋ CLI（同じバイナリ）。**要: アカウント（サインインの手順が公式の流れに入っている）。商用目的なら要: 費用（年 $29 か $58）**。AGPLv3 は自分でビルドする場合の条件
- **成熟度**: 0.x 版（v0.5.7 2026-07 → v0.6.2 2026-10、ほぼ毎月）。デスクトップアプリは Rust と GPUI に書き直された（README の Repository Map）
- **最小の手順（PowerShell）**:
  ```powershell
  # 1. cap.so/download から Windows 版を入れ、起動してサインイン（GUI）
  # 2. Settings → Command Line → Install CLI
  cap doctor --json
  cap targets --json                         # displays の id を見る
  cap record start --screen <id> --detach --json
  # ここで操作（手で、または Playwright を headed で）
  cap record stop --id <recordingId> --json
  cap project validate <path.cap> --json
  cap export <path.cap> --output $HOME\video-tools-trial\cap\take.mp4 --json
  ```
  自動ズームは Cap Desktop で .cap を開き、Zoom トラックの「Click to generate zoom segments」（GUI）
- **動いたと言える確かめ方**: `record stop` の JSON に `"recordingMetaExists":true`、`project validate` が成功、`take.mp4` を ffprobe して r_frame_rate と avg_frame_rate を記録（cap-demo の言う 58 vs 60 を確かめる）。手でクリックした録画で「Click to generate zoom segments」が区間を作れば、クリックのデータが取れている
- **所要の見込み（推測）**: 導入とサインイン 20 分、1 本 30 分

## Open Questions

- Windows でクリック・カーソルのデータが録れるか（docs の自動ズームの記述は OS を限定していない。cap-demo は macOS のみ）
- CLI から .cap にズーム区間を書く方法（`cap project config set` のキー）。`cap guide --json` を galleria で読むと分かるはず
- サインインなしで Studio Mode のローカル録画・書き出しができるか
- 個人の発信（西尾の作品の紹介）が「revenue-generating activities」に当たるか。Cap に問い合わせるか、OpenScreen を使うかは西尾が決める
