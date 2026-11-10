---
type: source
summary: VOICEVOX Engine と AivisSpeech Engine の公式 README・API 実装から、読みとアクセントを直す 3 つの手段（ユーザー辞書 /user_dict_word と /import_user_dict、AquesTalk 風記法で accent_phrases を差し替える、AivisSpeech の kana 欄）と、AivisSpeech で無視される欄（Mora の pitch・長さ、pitchScale は劣化しうる）を並べ、台本に読みを持たせる運用に落としたもの
video_types: [talk, embed]
url: https://github.com/VOICEVOX/voicevox_engine
author: VOICEVOX（ヒホ ほか）、Aivis Project（AivisSpeech Engine）。比較のため Style-Bert-VITS2・GPT-SoVITS の実装も参照
published: VOICEVOX Engine 0.26.1（2026-10-31）／AivisSpeech Engine 1.2.0（2026-04-30）
retrieved: 2026-11-09
sources:
  - https://github.com/VOICEVOX/voicevox_engine （README.md「ユーザー辞書機能について」「読み方を AquesTalk 風記法で取得・修正」「英単語の読み方を変える」「データを変更する API を無効化する」。最新リリース 0.26.1 2026-10-31、0.27.0-dev 2026-10-24。GitHub API で確認）
  - https://github.com/VOICEVOX/voicevox_engine/blob/master/voicevox_engine/app/routers/user_dict.py （引数の説明文を読んだ）
  - https://github.com/Aivis-Project/AivisSpeech-Engine （README.md「VOICEVOX API との互換性について」「よくある質問」「ライセンス」。最新リリース 1.2.0 2026-04-30、1.3.0-dev 2026-05-07、最終 push 2026-10-31）
  - https://github.com/Aivis-Project/AivisSpeech-Engine/blob/master/voicevox_engine/app/routers/tts_pipeline.py （accent_phrases の引数）
  - https://voicevox.hiroshiba.jp/term/ （VOICEVOX ソフトウェア利用規約）
  - https://github.com/litagin02/Style-Bert-VITS2/blob/master/server_editor.py 、https://github.com/RVC-Boss/GPT-SoVITS/blob/main/GPT_SoVITS/text/japanese.py （比較のため）
---

# VOICEVOX・AivisSpeech の読み辞書と、台本に読みを持たせる方法

## 何の文献か

- 公式 README と API の実装（一次資料）。辞書が「どこまで効くか」の実測は無い。効き方の限界は AivisSpeech の README の FAQ に作り手自身の記述がある

## 書いてあること

### VOICEVOX Engine（既定 `127.0.0.1:50021`）

**1. ユーザー辞書（API）**（README「ユーザー辞書機能について」、`user_dict.py`）

| 操作 | エンドポイント | 要る値 |
|---|---|---|
| 一覧 | `GET /user_dict` | なし。返り値は UUID → 単語の JSON（これがそのままエクスポート形式） |
| 追加 | `POST /user_dict_word` | **URL パラメータ**で `surface`（表層形）、`pronunciation`（カタカナ）、`accent_type`（「アクセント型（音が下がる場所を指す）」整数）。任意で `word_type`（`PROPER_NOUN`・`COMMON_NOUN`・`VERB`・`ADJECTIVE`・`SUFFIX`）、`priority`（0〜10、「1から9までの値を指定することを推奨」）。返り値は UUID |
| 修正 | `PUT /user_dict_word/{word_uuid}` | 同上。成功で 204 |
| 削除 | `DELETE /user_dict_word/{word_uuid}` | 成功で 204 |
| 取り込み | `POST /import_user_dict?override=true/false` | 本文に辞書 JSON（`GET /user_dict` の形）。`override` は「重複したエントリがあった場合、上書きするかどうか」 |

- `accent_type` の考え方として README は tdmelodic の説明（https://tdmelodic.readthedocs.io/ja/latest/pages/introduction.html ）を挙げ、「〇型となっている数字の部分がアクセント核位置になります」と書く
- 設定ページ `http://127.0.0.1:50021/setting` でも辞書のエクスポート／インポートができる
- `--disable_mutable_api`（または `VV_DISABLE_MUTABLE_API=1`）で「辞書登録や設定変更など、エンジンの静的なデータを変更するAPIを無効化」できる

**2. AquesTalk 風記法で読みとアクセントを直接与える**（README「読み方を AquesTalk 風記法で取得・修正」）

- `/audio_query` の返り値の `kana` 欄に、エンジンが判断した読みが AquesTalk 風記法で入る。規則: カタカナのみ／アクセント句は `/` か `、` で区切る（`、` なら無音を挿入）／`_` で次のカナを無声化／`'` でアクセント位置（各アクセント句に一つ必須）／句末の全角 `？` で疑問
- 直す手順: 直した記法を `POST /accent_phrases?speaker=1&is_kana=true` に渡して accent_phrases を得て、`audio_query` の `accent_phrases` を差し替えて `/synthesis` に渡す。README の例: `ディ'イプ/ラ'アニングワ/バンノオヤクデワアリマセ'ン` → `ディイプラ'アニングワ/バンノ'オヤクデワ/アリマセ'ン`
- 辞書に無い英単語は既定でカタカナ読みする（「ボイス シンセシス」）。`enable_katakana_english=false` で無効（README「英単語の読み方を変える」）
- 出力は 24000 Hz（README）

**利用規約**（https://voicevox.hiroshiba.jp/term/ ）: 商用・非商用とも可。作成した音声は各音声ライブラリ（キャラクター）の規約に従う。「ご利用の際は VOICEVOX を利用したことがわかるクレジット表記が必要です」。エンジンのコードは LGPL v3 と別ライセンスのデュアル（README）

### AivisSpeech Engine（既定 `127.0.0.1:10101`）

- 「概ね VOICEVOX ENGINE の HTTP API と互換性があります」。URL を差し替えるだけで動くはず、ただし「根本的に異なるモデルアーキテクチャの音声合成システムを強引に同一の API 仕様に収めている関係で…互換性のない API があるかもしれません」（README「VOICEVOX API との互換性について」）
- 対応モデルは Style-Bert-VITS2 と Style-Bert-VITS2 (JP-Extra) の **AIVMX** だけ。日本語のみ（README）
- **辞書**: 内蔵辞書に加え「東京式アクセント・品詞・優先度まで詳細に調整したユーザー辞書」を API で追加できる。設定画面 `http://127.0.0.1:10101/setting` でインポート／エクスポート（README）
- **辞書の効く範囲の限界**（FAQ「読み方やアクセントが想定と異なります」）: 内蔵辞書に無い固有名詞・人名は正しく読まれないことが多く、辞書登録で直す。ただし「**複合語や英単語に関しては、単語の優先度にかかわらず、辞書への登録内容が反映されないことがあります。これは現時点での仕様になります**」
- **VOICEVOX と意味が違う・無視される欄**（README「AudioQuery 型の仕様変更」「Mora 型の仕様変更」）:
  - `kana`: VOICEVOX では読み取り専用の AquesTalk 風記法だが、AivisSpeech では「**通常の読み上げテキストを指定するフィールド**」。空なら accent_phrases から自動生成したひらがなを読むが「不自然なイントネーションになる可能性があります」
  - Mora の `consonant` / `vowel` は読み取り専用で「音声合成時のテキストの読みには、常に `text` フィールドの値が利用されます」。`consonant_length` / `vowel_length` / `pitch` は**常に無視**（ダミー値 0.0）
  - `intonationScale` は「全体の抑揚」ではなく「話者スタイルの感情表現の強さ」（0.0〜2.0）。`pitchScale` は 0.0 から動かすと「音質が劣化する可能性があります」。`pauseLength` / `pauseLengthScale` は無視。`tempoDynamicsScale`（話す速さの緩急）が独自に追加
  - `enable_katakana_english` は無視（`tts_pipeline.py` の引数説明「常に無視されます」）。`enable_interrogative_upspeak` も無視で、「？」「…」などの記号に応じた抑揚になる
  - 歌声合成系と `/synthesis_morphing` は使えない（501 / 400）
- **長文**: 「音声合成1回につき 500 文字以内が望ましい」。句読点・段落・会話文で区切ると、区切りごとに感情表現と抑揚がリセットされて自然になる傾向がある（FAQ）
- **利用条件**: Engine は VOICEVOX のデュアルライセンスのうち LGPL-3.0 だけを継承。「少なくともソフトウェア本体はクレジット表記不要で、個人・法人・商用・非商用を問わず」。ACML / ACML-NC / CC0 のモデルならクレジット義務なし（FAQ）

### 比較: 他のローカル TTS の辞書

| エンジン | 辞書の入れ方 | アクセント | 出典 |
|---|---|---|---|
| VOICEVOX | `POST /user_dict_word`（URL パラメータ）、`/import_user_dict` | `accent_type`＋AquesTalk 風記法で句ごとに直接 | 上 |
| AivisSpeech | 同じ API。複合語・英単語は効かないことがある | Mora の pitch は無視 | 上 |
| Style-Bert-VITS2 エディタ | `POST /api/user_dict_word`（**JSON 本文**、`surface`・`pronunciation`・`accent_type`・`priority`） | `/api/synthesis` に `moraToneList`（モーラごとの 0/1）を渡せる | [[web-means-voice-style-bert-vits2]] |
| GPT-SoVITS | `GPT_SoVITS/text/ja_userdic/userdict.csv`（MeCab 形式の CSV）。起動時に hash を見て `pyopenjtalk.mecab_dict_index` で `user.dict` にコンパイル | 辞書の CSV の項目次第（未確認） | `japanese.py` の実装、[[web-means-voice-gpt-sovits]] |
| Irodori-TTS | 辞書なし（文字列をそのまま読む）。読みはテキストを書き換えて直す | — | [[exp-galleria-tts-and-singing]] |

## この wiki への含意

### 台本に読みを持たせる運用（文献と経験からの整理。設計で、未実測）

[[exp-qualia-video]] は表示文と読み上げ文を台本の別フィールド（`caption` / `narration`）に分け、[[exp-sutra-sync-subtitles]] は一語を surface／ruby／speech／status の 4 欄に分けた。辞書は「エンジンの状態」で、台本の外にある。そこで次の三層にするのが文献の仕様から自然（推測）:

1. **台本の `narration`（speech）欄**: まず書き換えで直す（かなに開く、中黒を取る）。どのエンジンにも効き、AivisSpeech の「複合語・英単語は辞書が効かないことがある」にも左右されない
2. **repo に置く辞書 JSON**（`GET /user_dict` の形）: 頻出の固有名詞・製品名だけ。合成スクリプトの最初に `POST /import_user_dict?override=true` を呼ぶ。辞書は台本と同じ commit に入るので、[[exp-qualia-video]] の manifest（engine version・話者・query・WAV の SHA-256）に**辞書ファイルの hash**を足せば再現できる
3. **区間ごとの accent_phrases の上書き**（VOICEVOX のみ）: どうしても直らないアクセントだけ、台本に AquesTalk 風記法を書いて `/accent_phrases?is_kana=true` で差し替える。AivisSpeech では Mora の pitch が無視されるので**この層は使えない**（README の記述からの推論）。AivisSpeech でアクセントまで台本で決めたいなら、同じモデル系統の Style-Bert-VITS2 エディタの `moraToneList` が代わりになりうる

- 辞書を変えると同じ台本でも音が変わる。[[exp-sutra-sync-subtitles]] の「音声を作り直すときはキャッシュしない」と同じく、辞書の hash が変わったら全区間を作り直す
- 経験との一致: [[exp-sutra-sync-subtitles]] の失敗は `audio_query` の推定読みを表示ルビへ戻したこと。辞書を整えても `audio_query` の読みは**推定の出力**であり、正本は台本の側に置く、という向きは変わらない
- 経験との差: [[exp-galleria-tts-and-singing]] の「VOICEVOX の C API（core 0.16.2、配布版 0.25.2）」は HTTP サーバーを使わない経路で、ユーザー辞書の HTTP API は使えない。core 側の辞書 API（`voicevox_user_dict_*`）があるかはこの調査で読んでいない
- 規約: VOICEVOX は**クレジット必須**（ソフトウェア規約）、AivisSpeech は本体のクレジット不要。[[exp-qualia-video]] の「VOICEVOX Nemo は公開時にクレジット必須」と合わせ、エンジンを替えると概要欄の文言も替わる

## 着手の仕方（未検証。galleria で確かめる）

- **何が表現できるようになるか**: 読みとアクセントを台本と一緒に版管理したナレーション。効く型は talk・embed（流しっぱなしで読み違いを話し手が補えない embed で特に効く）
- **機械**: galleria Windows。入れるもの: **なし**（AivisSpeech Engine 1.2.0 は galleria に既に入っている。[[exp-qualia-video]]）。VOICEVOX でも試すなら Engine 0.26.1 の配布版（費用 0、クレジット必須）。アカウント不要
- **成熟度**: VOICEVOX Engine は 2026-10-31 に 0.26.1、更新が続いている。AivisSpeech Engine は 1.2.0（2026-04-30）以後リリースは dev のみ、push は 2026-10-31
- **最小の手順**（PowerShell。エンドポイントは README から、PowerShell の書き方は推測）:
  ```powershell
  Start-Process '<AivisSpeech Engine 1.2.0 の置き場>\run.exe' -WindowStyle Hidden
  $B='http://127.0.0.1:10101'
  # 1) 辞書前の読みを記録
  $t=[uri]::EscapeDataString('声質と声付きを比べる')
  $q0=Invoke-RestMethod -Method Post "$B/audio_query?speaker=888753763&text=$t"
  ($q0.accent_phrases | % { $_.moras | % { $_.text } }) -join ''
  # 2) 登録（例: 声付き → コエツキ、核は 0 型。値は仮）
  Invoke-RestMethod -Method Post "$B/user_dict_word?surface=$([uri]::EscapeDataString('声付き'))&pronunciation=$([uri]::EscapeDataString('コエツキ'))&accent_type=0&word_type=COMMON_NOUN&priority=7"
  # 3) 登録後の読み
  $q1=Invoke-RestMethod -Method Post "$B/audio_query?speaker=888753763&text=$t"
  ($q1.accent_phrases | % { $_.moras | % { $_.text } }) -join ''
  # 4) 辞書を repo に書き出す
  Invoke-RestMethod "$B/user_dict" | ConvertTo-Json -Depth 5 | Out-File -Encoding utf8 user_dict.json
  ```
  （style ID `888753763` は [[exp-galleria-tts-and-singing]] の「まお／おちつき」。ID は `/speakers` で確かめ直す）
- **動いたと言える確かめ方**: (1) 手順 3 で連結したモーラ列が登録した読み（`コエツキ`）を含み、手順 1 と違う。(2) `user_dict.json` に登録語の UUID が入る。(3) Engine を再起動しても `GET /user_dict` に残る。(4) 合成した WAV を [[exp-qualia-video]] で「こわつき」「せいしつ」と聞こえた所だけ人が聴いて、聞こえ方が直ったか判定する（モーラ列が正しくても耳で違うことがありうる）
- **所要の見込み（推測）**: 30 分〜1 時間。既存の `generate_aivis_voice.ps1` に `import_user_dict` の 1 行を足すのは 30 分程度

## Open Questions

- AivisSpeech で `accent_phrases` の `accent`（アクセント核の位置）を書き換えたら効くのか。README は Mora の pitch を無視すると書くが、AccentPhrase の `accent` については書いていない
- AivisSpeech の「複合語や英単語は辞書が効かないことがある」がどの程度の頻度か（実測なし）
- VOICEVOX core（C API）の辞書の扱い（[[exp-galleria-tts-and-singing]] の経路で辞書が使えるか）
- `accent_type` の値をどう決めるか。辞書（NHK アクセント辞典など）を引くのか、耳で決めるのか。tdmelodic の説明は読んでいない
