---
type: source
summary: Style-Bert-VITS2（JP-Extra）の公式 README・利用規約・FAQ・エディタのサーバー実装（v2.7.0、2026-11-09 時点）。日本語特化の Bert-VITS2 改造版で、コードと事前学習の重みは AGPL-3.0、辞書モジュールは LGPL-3.0。エディタの API は単語辞書（/api/user_dict_word）とモーラごとのアクセント（moraToneList）を受け付け、2〜14 秒の音声と書き起こしで自分の声の学習ができ、学習結果は ONNX → AIVM 経由で AivisSpeech に持ち込める
video_types: [talk, embed]
url: https://github.com/litagin02/Style-Bert-VITS2
author: litagin02（Style-Bert-VITS2 の作者）。元は Fish Audio の Bert-VITS2 v2.1 と JP-Extra
published: 2023-12-27（v1.0）／2024-02-03（v2.0 JP-Extra）／2025-08-24（v2.7.0、最新リリース）
retrieved: 2026-11-09
sources:
  - https://github.com/litagin02/Style-Bert-VITS2 （README.md、master。最終 push 2025-12-07、最新リリース 2.7.0 は 2025-08-24。GitHub API で確認）
  - https://github.com/litagin02/Style-Bert-VITS2/blob/master/docs/TERMS_OF_USE.md （開発陣からのお願いとデフォルトモデルの利用規約、2024-06-14 改）
  - https://github.com/litagin02/Style-Bert-VITS2/blob/master/docs/FAQ.md 、docs/CLI.md
  - https://github.com/litagin02/Style-Bert-VITS2/blob/master/server_editor.py 、server_fastapi.py、default_config.yml、style_bert_vits2/constants.py、style_bert_vits2/nlp/japanese/user_dict/__init__.py（実装を読んだ）
  - https://huggingface.co/litagin/Style-Bert-VITS2-2.0-base-JP-Extra （モデルカード、license: agpl-3.0）
  - https://zenn.dev/litagin/articles/034819a5256ff4 （作者の解説「Style-Bert-VITS2 JP-Extra」、2024-02-05 公開・02-14 更新）
---

# Style-Bert-VITS2（JP-Extra）

## 何の文献か

- 作者自身の公式 README・規約・FAQ と、エディタ用サーバーの Python 実装。性能の主張は作者の自己申告で、第三者の評価ではない
- 作者の Zenn 記事は「機械学習や音声AIや日本語処理についてちゃんとした勉強をしたことがないので誤っている箇所が多く存在する可能性があります」と自分で断っている

## 書いてあること

### 何か

- 「入力されたテキストの内容をもとに感情豊かな音声を生成する Bert-VITS2 の v2.1 と Japanese-Extra を元に、感情や発話スタイルを強弱込みで自由に制御できるようにしたもの」（README 概要）
- JP-Extra は日本語に絞った版。Bert-VITS2 JP-Extra のリリースに「~800h single language」の日本語データとあり、作者は「日本語の発音やアクセントやイントネーション等の自然性が上がり」「日本語しか使わない場合は JP-Extra 版を使うことを強くおすすめ」と書く（Zenn 記事）。Style-Bert-VITS2 では「アクセントの制御も（ある程度は）指定できるように」した（同）
- 音声合成だけなら GPU なしの CPU で動く。学習には NVIDIA の GPU が要る（README「動作環境」）。Windows・WSL2・Ubuntu で動作確認とある

### 版と更新（2026-11-09 時点）

- 最新リリースは **2.7.0（2025-08-24）**。内容は「Aivis Project 等との連携のため、ONNX 変換の GUI 追加、また音声認識モデルとして `litagin/anime-whisper` の追加等」（README の更新履歴）。master の最終 push は 2025-12-07。**1 年以上リリースが出ていない**
- 辞書機能とエディタは ver 2.3（2024-02-26）から

### ライセンス・規約（条文から）

- リポジトリは **AGPL-3.0**（本家 Bert-VITS2 と同じ）。`text/user_dict/` モジュールは VOICEVOX Engine 由来で **LGPL-3.0**（README「LICENSE」）
- JP-Extra の事前学習モデル（HF `litagin/Style-Bert-VITS2-2.0-base-JP-Extra`）のモデルカードも `license: agpl-3.0`
- 「お願い」（強制力なしと明記）: 法律違反・政治的な目的（「本家Bert-VITS2で禁止されています」）・他者を傷つける目的・「なりすまし・ディープフェイク作成目的」に使わないでほしい。使うモデルの規約を確認してほしい（TERMS_OF_USE.md）
- 同梱の既定モデルの規約: JVNV コーパス由来の 4 話者は CC BY-SA 4.0 を継承。「小春音アミ」「あみたろ」は、あみたろの声素材工房の規約に従えば商用・非商用とも可だが、**生成音声を公開するときはクレジット必須**（例 `Style-BertVITS2モデル: あみたろ、あみたろの声素材工房 (https://amitaro.net/)`）。年齢制限のある用途、新興宗教・政治・マルチ商法に深く関わる用途、誹謗中傷、「あみたろ本人の声として扱うこと」などは禁止。他モデルとのマージは、マージ先の声の権利者が許諾している場合だけ（TERMS_OF_USE.md）
- **生成した音声そのものに AGPL がどう及ぶかは README・規約に書かれていない**（読めた範囲で記述なし）

### 読みとアクセントを直す仕組み（実装を読んだ）

- エディタ用サーバー `server_editor.py`（既定ポート 8000、`--port` で変更）の API（`/api` 配下）:
  - `GET /api/user_dict`、`POST /api/user_dict_word`、`PUT /api/user_dict_word/{uuid}`、`DELETE /api/user_dict_word/{uuid}`。本文は JSON で `surface`・`pronunciation`・`accent_type`（コメント「アクセント核位置（存在しない場合は0、1文字目は1）」）・`priority`（既定 5）。VOICEVOX と違い **query ではなく JSON 本文**で渡す
  - `POST /api/g2p` に文を渡すと `[{mora, tone}]`（カタカナのモーラと 0/1 の高低）が返る。`POST /api/synthesis` は `text` と一緒に **`moraToneList`** を受け取り、それを `given_tone` として合成に使う。つまり**モーラごとの高低を台本の側に持たせて渡せる**
- 辞書の実体は `dict_data/` の `default.csv`（既定）＋`user_dict.json`（ユーザー）を pyopenjtalk 用の `user.dic` にコンパイルしたもの（`user_dict/__init__.py`、`constants.py` の `DEFAULT_USER_DICT_DIR`）
- 外部連携用の `server_fastapi.py`（`config.yml` の `server.port` 既定 5000）は `GET/POST /voice?text=…` で合成。**入力は既定で 100 文字まで**（`server.limit`、-1 で無制限。README・FAQ）

### 自分の声の学習

- 「学習には2-14秒程度の音声ファイルが複数と、それらの書き起こしデータが必要」。長さを問わない音声ファイルだけからスライスと自動書き起こしでデータセットを作る道具が同梱（README「学習」）
- どのくらいのデータが要るかは「分かりません。試行錯誤してください」。参考として「数分程度でも学習はできるらしく」、RVC では「多くても45分くらいで十分説」。ステップ数は「最初の2k-3kで声音はかなり似始めて、5k-10k-15kステップほどで感情含めてよい感じになりやすく」（FAQ）
- 学習の VRAM の数値は README・FAQ・CLI.md に**無い**。FAQ は「バッチサイズが大き過ぎてメモリがVRAMから溢れると非常に遅くなる」とだけ書き、CLI の既定バッチは 2
- ステップの選別の目安に SpeechMOS のスクリプト（`python speech_mos.py -m <model_name>`）があるが、作者は「アクセントや感情表現や抑揚を全く考えない基準での評価」「実際に読み上げさせて選別するのが一番」と書く
- 学習したモデルは「ONNX変換」タブで ONNX にし、Aivis Project の AIVM Generator で AivisSpeech 用の AIVM / AIVMX にできる（README「ONNX変換」）。AivisSpeech Engine が読むのは Style-Bert-VITS2 と Style-Bert-VITS2 (JP-Extra) の AIVMX（[[web-means-voice-voicevox-aivisspeech-user-dictionary]]）

## この wiki への含意

- [[exp-galleria-tts-and-singing]]・[[exp-qualia-video]] で使った **AivisSpeech の声（まお）は、中身が Style-Bert-VITS2 系のモデル**（AivisSpeech Engine が対応するアーキテクチャが SBV2 / SBV2 JP-Extra だけ）。Style-Bert-VITS2 を直接使うことは「別のエンジンに替える」より「AivisSpeech の下の層を触る」ことに近い。増えるのは主に (1) モーラごとの高低を台本で指定する、(2) 自分の声・許諾を得た声の学習、の二つ
- **モーラ単位の高低（moraToneList）は、[[exp-sutra-sync-subtitles]] の「表示ルビ／音声への入力（speech）」の分離と相性がよい**。speech 欄にカタカナと高低を持たせれば、TTS の推定読みを表示に戻す失敗（行者問答）と逆向きに、人が決めた読みだけを TTS に渡せる。ただし `g2p` が返す読みは推定なので、それを正本にしない点は経験と同じ
- ライセンスの面: [[exp-galleria-tts-and-singing]] は「license で在庫が二分される」「配布物に載せるなら license が閉じている順」と書いた。SBV2 は**コードと事前学習の重みが AGPL-3.0**で、合成したナレーション入り動画を出すだけなら配布物にコードは入らないが、合成をサービスとして公開する・改造したコードを配る場合は AGPL の条件がかかる。MIT の Irodori-TTS-v4.1-Small より条件は重い
- 型: 解説のナレーション（talk）と、流しっぱなしの embed のナレーション。promo の声にも使えるが、感情の強いスタイルは学習データ次第

## 着手の仕方（未検証。galleria で確かめる）

- **何が表現できるようになるか**: (a) 読み違いをアクセントごと台本で固定したナレーション、(b) 自分の声（または許諾を得た声）のローカル TTS。効く型は talk・embed（流しっぱなしのナレーション）
- **機械**: galleria Windows（README の zip＋bat が Windows 前提）。WSL2 も動作確認ありとされる。入れるもの: Style-Bert-VITS2 2.7.0（`sbv2.zip`）、内部で Python・torch（README の手順では `torch<2.4` の cu118）。費用 0、アカウント不要（初回に HF から既定モデルを落とす）。利用条件: AGPL-3.0、既定モデルごとの規約（あみたろはクレジット必須）
- **成熟度**: 最新リリース 2.7.0（2025-08-24）、以後リリースなし。star 約 1,400（参考）。**RTX 5080（Blackwell）で README の `torch<2.4` cu118 が動くかは不明**（推測では Blackwell は新しい CUDA の torch を要するので、合成だけ CPU 版で始めるのが安全）
- **最小の手順**（Windows。README の手順そのまま、引数は推測なし）:
  1. `sbv2.zip`（https://github.com/litagin02/Style-Bert-VITS2/releases/latest/download/sbv2.zip ）を日本語・空白を含まないパス（例 `<アプリの置き場>\sbv2`）に展開
  2. まず `Install-Style-Bert-VITS2-CPU.bat`（合成とマージだけ。学習はできない）をダブルクリック。エディタが自動で開けばインストール成功
  3. エディタで既定モデル（JVNV など）を選び、[[exp-qualia-video]] の 15〜30 秒の比較用原稿（`qualia-video-makingof/` の読み上げ専用原稿）を読ませる。読み違う語を辞書タブで登録
  4. API で辞書を入れる場合（推測で補ったコマンド。エンドポイントと引数名は `server_editor.py` から）:
     ```powershell
     python server_editor.py --inbrowser --device cpu   # 既定ポート 8000
     Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/api/user_dict_word -ContentType 'application/json' -Body '{"surface":"空","pronunciation":"カラ","accent_type":2,"priority":7}'
     Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/api/g2p -ContentType 'application/json' -Body '{"text":"空の吹き出し"}'
     ```
     （「空」を常に「から」と読ませる登録は他の文脈を壊すので、実際には「空の吹き出し」のような複合で登録する方がよい、と推測）
  5. 自分の声の学習は GPU 版（`Install-Style-Bert-VITS2.bat`）が要る。録音は西尾が決める（[[web-means-voice-elevenlabs-google-openai-voice-clone-consent]]）
- **動いたと言える確かめ方**: (1) エディタが開き既定モデルで WAV が出る。(2) `/api/g2p` の返り値で「空の吹き出し」の最初の 2 モーラが `カ`・`ラ` になる（辞書が効いた）。(3) 同じ原稿を AivisSpeech（まお）と並べ、[[exp-qualia-video]] と同じく発話中 RMS を -22 dBFS に揃えた試聴用コピーで人が聴く。採否は耳で決める（[[exp-galleria-tts-and-singing]]）
- **所要の見込み（推測）**: CPU 版の導入と既定モデルでの試聴 1〜2 時間。自分の声の学習はデータ作りを含めて半日〜1 日（Blackwell と torch の版が合わなければそれ以上）

## Open Questions

- 生成音声の扱いに AGPL-3.0 がどう及ぶかの公式の説明は見つからなかった
- RTX 5080 で学習を回せる torch の版（README の `torch<2.4` cu118 のままか）。2.7.0 以後リリースが無いので、Blackwell 対応は利用者側の作業になる可能性がある
- AivisSpeech（同じ系統のモデル）と比べて、直接 SBV2 を使うと音が変わるか（AIVMX は ONNX 版。推論の違いがあるか未確認）
- moraToneList で高低を与えたとき、BERT 側の文脈による抑揚とどう両立するか（作者は「ある程度は」と書くだけ）
