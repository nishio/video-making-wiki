---
type: source
summary: galleria の Codex が作った「クオリアさん」が解説する動画 3 本（パイロット 93 秒、メイキング 109 秒、制作ジャーニー 6 分 33 秒）。Pillow の静止スライド＋TTS＋PyAV の決定論的な組み立てで作り、人間の評価のたびに「静止が既定」「表示文と読み上げ文を分ける」「飾りより証拠を大きく」という規則へ直していった
video_types: [talk, embed]
sources:
  - galleria C:\Users\nishi\claude-win\qualia-video-pilot\README.md, script.json, render_video.py, generate_voice.ps1
  - galleria C:\Users\nishi\claude-win\qualia-video-makingof\README.md, comparison.md, AIVISSPEECH-LICENSE.md, motion-comparison\README.md, motion-comparison\WAN22_RUNNER.md
  - galleria C:\Users\nishi\claude-win\qualia-video-journey\README.md, script.json, render_video.py, generate_aivis_voice.ps1
  - 3 ディレクトリとも git 管理されていない（commit hash なし）。日付は README と galleria-wiki raw による
  - galleria-wiki raw/2026-08-12-qualia-san-explainer-video-pilot-feedback.md, -tts-feedback-followup.md, -motion-feedback-followup.md
  - galleria-wiki raw/2026-09-26-qualia-san-explainer-video-conversation-closeout.md
---

# クオリアさん解説動画（pilot / makingof / journey）

2026-08-11〜12 に、galleria（RTX 5080 16GB の Windows 機）で Codex が作った解説動画のシリーズ。題材は「クオリアさん」（CC BY 4.0 で公開されているキャラクター。出典 https://scrapbox.io/qualia-san/Qualia-san ）の画像をローカルで生成した経験そのもの。MacBook から Codex Remote で指示して作った（journey README「伝える中心」）。

フィードバックは記録上どれも「人間」の発言として書かれている（発言者の名前は記録に無い）。以下でもそのまま「人間」と書く。

## 何を作ったか

| 名前 | 尺 | 形式 | 公開 |
|---|---|---|---|
| pilot「このクオリアさんは、どう作られた？」 | 93.125 秒、8 scene / 20 音声区間 | 1920×1080、24fps、H.264＋AAC mono 22.05kHz | YouTube v1 https://youtu.be/bW6c9y6MkYg |
| makingof（v1 のメイキング） | 109.375 秒、8 scene / 17 区間 | 同、AAC mono 48kHz | YouTube v2 https://youtu.be/qntzIC2zNK8 |
| journey「クオリアさんと作る、記憶するAI工房」v4 | 393.5 秒（6 分 33 秒）、16 scene / 40 区間 | 同、9,445 frames | 未公開（README に公開 URL なし） |

（各 README。journey の初版は 538 秒・44 区間で、人間の評価を受けて削った）

## 作り方のパイプライン

共通の骨格は「台本 JSON → 区間ごとの WAV → Pillow で静止スライド → PyAV で H.264 に結合 → 機械 QA → 人間の評価」。

1. **台本** `script.json`: scene ごとに `segments` を持ち、各区間に字幕用の `caption` と音声合成用の `narration` を別々に書く。journey では `revision_policy` として「読み上げるのは役割・失敗・判断・次の行動」「画面だけに出すのは製品名・主要な接続・概数・公開 URL」「正確な version・seed・秒数・VRAM・hash は wiki だけ」と書き分けた
2. **音声**: pilot は Windows の SAPI（Microsoft Haruka Desktop、Rate 6）を PowerShell から（`generate_voice.ps1`）。makingof 以降は AivisSpeech Engine 1.2.0 の「まお／おちつき」（style ID 888753763、speedScale 1.0、intonationScale 0.9）を HTTP API で（`generate_aivis_voice.ps1`）。query・engine version・話者・各 WAV の SHA-256 を manifest に残す
3. **映像** `render_video.py`: ComfyUI portable 同梱の Python（Pillow・PyAV 入り）で実行。各区間を静止画の「変種」として描き、区間が変わるときに枠・チェック・node の色など意味のある部分だけを切り替える。画面全体の pan / zoom はしない（journey の docstring）
4. **QA**: scene ごとの preview、全区間の大型 preview シート、完成 MP4 を再 decode したコンタクトシート、`qa.json`（scene 数、区間数、stream、尺、10 分上限、音量の余裕、話者、帰属、公開 URL）。journey v4 では完成 MP4 の全 frame を decode し、40 区間を preview＋字幕と照合（最小 PSNR 37.36 dB、字幕 40 件すべて 1 行）

```powershell
Start-Process 'C:\Users\nishi\AI\apps\AivisSpeech-Engine-1.2.0\run.exe' -WindowStyle Hidden
Set-Location C:\Users\nishi\claude-win\qualia-video-journey
.\generate_aivis_voice.ps1
& 'C:\Users\nishi\AI\apps\ComfyUI_windows_portable\python_embeded\python.exe' .\render_video.py --validate-only
& 'C:\Users\nishi\AI\apps\ComfyUI_windows_portable\python_embeded\python.exe' .\render_video.py
```
（journey README「再生成手順」より、引数は一部省略）

画像は ComfyUI 0.31.0 + FLUX.2 Klein 4B distilled FP8（text encoder Qwen 3 4B）、1024×1024、Euler、4 steps、CFG 1.0。参照画像は `LoadImage → VAEEncode → ReferenceLatent → positive conditioning` で効かせる。同じ構成の固定条件の単発試験で 6.2 秒、peak 14,666 MiB（pilot README、journey README「実機で確認済みの値」）。日本語の文字は生成させず、空の吹き出し・空 panel を生成してから Pillow で後から合成する。

## 人間の評価と、それで何を変えたか

### pilot → makingof

- 「音声合成に改善の余地がありまくり」「解説動画でゆっくり動くの気持ち悪いなw」（pilot-feedback raw）。pilot は静止画らしさを隠すため全 scene に 1.8% の拡大と sin 波の低速パン、0.42 秒のクロスフェードをかけていた
- 音声の追補（言い換え・要約）: 速度そのものは主な問題ではない。「空の吹き出し」の「空」を「から」と読まなかった、「ホモ・サピエンス」が中黒で切れた、SAPI の声が古臭い、VOICEVOX 等も比べたい（tts-feedback raw）
- motion の追補: 「Pillowの静止スライド＋SAPI＋PyAV なのは割と良かったと思うよ、Wan2.2とも小さい単位で比較実験したいね」（motion-feedback raw）。否定されたのは方式全体でなく全画面の drift だった、と解釈した
- 変えたこと:
  - **表示文と読み上げ文を分ける**（画面「空の吹き出し」／読み「からの吹き出し」、画面「ホモ・サピエンス」／読み「ホモサピエンス」、製品名はカタカナ読みに開く）
  - **TTS は全編の前に 15〜30 秒の共通原稿で比べる**。AivisSpeech（まお・コハク）、VOICEVOX（夜語トバリ、ナースロボ＿タイプＴ）、VOICEVOX Nemo、旧 SAPI を同じ読み上げ専用原稿で作り、試聴用コピーだけ発話中 RMS を -22 dBFS に揃えて音量差に引っ張られないようにした。人間の評価で AivisSpeech に決め、engine・speaker・style・query を一組で固定（makingof `comparison.md`）
  - **静止を既定にする**（次の A/B/C 比較で決めた）

### motion の A/B/C 比較（同じ 4.0417 秒・97 frames・同じ音声）

- A: Pillow の完全静止 → 人間「よい」。**既定に採用**
- B: 人物 card に focus ring（frame 40–63 だけ）→ 変化は分かったが「解説上無意味」。不採用。動かすなら説明中の図・語・数値・工程 node を直接 highlight する
- C: Wan2.2 TI2V-5B でキャラクター部分（640×640）だけ I2V して固定スライドに合成 → 「どこが変わったのかわからん」。不採用
- C の条件: seed 22022026、20 steps、CFG 5、uni_pc / simple、shift 8。runner 全工程 70.074 秒、VRAM used 1,901 → 15,675 MiB（makingof `motion-comparison/README.md`, `WAN22_RUNNER.md`）
- 設計の工夫: Wan に文字・図・背景を通さない（文字の変形と画面の漂いが比較を汚すため）。ROI の外の画素はスライドと完全一致することを検査。Wan の出力は動画 node を使わず PNG で受けて、A/B と同じ PyAV 設定でエンコード

### journey 初版 → v2 → v3 → v4

- 初版（8 分 58 秒）への評価: 「細かい数値を耳で聞くのが辛い」「人間が理解できる台本へ」「最初の1分で目的と関心を作る」「図解が多すぎる」（journey README「人間理解を優先した改稿」）
  - → version・seed・hash・codec は wiki と再現用ファイルへ移して読み上げない。冒頭 52.9 秒で成果物・道具・v1 の失敗・比較・最後の 7 ステップのチェックリストを予告する。図を減らし、ローカル生成のクオリアさん場面絵 12 枚を使う
- v2 の通し視聴で、音の聞こえ方（「こえつき」が「こわつき」、「こえしつ」が「せいしつ」に聞こえる）と、その瞬間の画面が説明を助けているかを scene ごとに見直した（v3）
- v3 への評価: 「意味のない飾り画像の面積が多すぎる」。場面絵が画面の 36% を占めていた
  - → v4 は **evidence-first**: 装飾の場面絵を 0% にし、実際の生成画像の比較、工程、machine QA と人間評価の差、採用した規則に面積を配る。box は実画像の境界か具体的な工程 node を示すときだけ使う
- 画面上の主張に色付きのラベルを付けて種類を混ぜない: `実機確認`（cyan）／`人間評価`（pink）／`推奨`（gold）／`制作時設定`（blue）／`当時の状態`（purple）。v1 の時点で未導入だった Wan2.2 を v1 で使ったように見せない（journey README「情報ラベル」）

## 詰まったこと・落とし穴

- **「目標尺に入った」は音声の合格条件ではない**。pilot は SAPI の Rate を 1→5→6 と上げて尺に押し込んだ（発話 148.7 秒→85.8 秒）が、評価された問題は速度でなく読みと声質だった（pilot-feedback raw）
- **機械 QA が全部通っても視聴品質は保証されない**。codec・尺・字幕・stream・hash が正しくても、読み・声質・視線誘導・理解しやすさは人間が見ないと分からない（closeout raw の規則 6）
- sandbox 内では SAPI のファイル出力がアクセス拒否になり、許可された sandbox 外で生成した（pilot-feedback raw）
- **アーカイブはそのまま再実行できない**: 2026-09-26 の監査で、`render_video.py --validate-only` が移行前の旧パスの画像を参照して失敗した。`script.json` の status と visual policy も v3 のままで v4 の方針と食い違っていた（closeout raw）。完成 MP4 と当時の QA は有効
- 製作途中で台本の記述と renderer の実装がずれる（上の script.json の件）。方針を変えたら台本側のポリシー欄も同時に直す必要がある

## 権利・表示

- クオリアさん素材は CC BY 4.0。出典・ライセンス・変更内容（AI 画像生成、構図調整、字幕、音声、動画編集）を README と動画内に出す
- AivisSpeech Engine は LGPL-3.0、「まお」「コハク」は ACML 1.0。ACML 1.0 は実在の人物・団体・商品への批判を目的とする用途、政治・宗教的主張、なりすまし、虚偽を禁じるので、技術比較は条件と用途への適合を中立的に書く。義務でなくても音声モデル名と「本人・公式の音声ではない」旨を表示した（makingof README、comparison.md）
- VOICEVOX Nemo は公開時にクレジット必須、VOICEVOX は音声ライブラリごとに規約確認が要る（comparison.md）

## 再利用できる部品

- `qualia-video-journey/render_video.py`: 静止スライドの変種＋字幕＋進捗バーを PyAV で結合し、preview・コンタクトシート・QA JSON まで出す renderer
- `qualia-video-journey/generate_aivis_voice.ps1`: AivisSpeech の HTTP API から区間ごとの WAV と query・manifest を作る
- `qualia-video-makingof/generate_http_tts_sample.ps1`: AivisSpeech / VOICEVOX / VOICEVOX Nemo の話者一覧と比較用 WAV（`-ListSpeakers`、`-StyleId`）
- `qualia-video-makingof/motion-comparison/`: 同じ 4 秒 cut で静止／局所 motion／Wan2.2 を比べる一式（`run_wan_micro.py --validate-only` `--preflight-only` で推論前に検査できる）

## galleria-wiki 側の記録にだけあること（2026-11-09 統合）

元 repo でなく galleria-wiki（`qualia-san-explainer-video-pilot.md`、`parts-animation-backends.md` ほか）から読んだ別の担当の抽出のうち、上と重ならない点。

- メイキング本編から Wan2.2 と A/B/C 比較は外した（「v1 はどう作られたか」に焦点を保つ人間の編集判断）。画面の章番号は `06 / HUMAN FEEDBACK` の次を `08 / THE NEW RULES` とし、外した 07 を飛ばした。A/B/C の説明は続編に回した
- AivisSpeech の声（ACML 1.0）は実在の製品への批判・攻撃目的の利用を禁じるので、「他の製品が古臭い」という批判をその声に読ませず、「今回の用途で求める声質と合わなかった」という実験結果として書いた。声の license が台本の言い回しを縛る例
- journey 版のレイアウト: 字幕は y=890 以降、主な内容は y=860 以内に収め、説明対象と字幕を重ねない。字幕 40 件はすべて 1 行
- 台本と音声を固定したまま画面だけを改稿できた（v3 → v4）。音声 segment 単位の timeline があったから
- 同じ時期の旧デモ `PSDMaker-A/scripts/qualia_talk.py` の口パクは、音声の RMS（30fps で平滑化）を口の開きにする方式で、音素・母音には同期していない
- 2026-09-26 の締めの時点で、`render_video.py --validate-only` に移行前の asset path が残り、`script.json` も v3 の方針のままで、そのまま再生成できる状態ではないと galleria-wiki は書いている

## Open Questions

- journey v4 は公開されたか、見た人にどう受けたかは記録が無い
- 「静止が既定」は解説（talk）での結論。promo 型でも同じかは試していない
- Wan2.2 の C 案は「idle の微小な動き」だった。説明対象そのものを動かす I2V（指差し等）は比べていない
