---
type: source
summary: 商用 TTS 4 社（Google Cloud TTS・Gemini TTS、Azure AI Speech、OpenAI、ElevenLabs）の 2026-11-09 時点の公式ドキュメント・価格表から、日本語の対応、読みの直し方（Google の yomigana とアクセント記号、Azure の sapi カナと PLS 辞書、ElevenLabs の alias 辞書、OpenAI と Gemini は指示文だけ）、価格、開示の義務を並べたもの。OpenAI の gpt-4o-mini-tts は 2027-01-06 に終了と告知されている
video_types: [any]
url: https://cloud.google.com/text-to-speech/docs/ssml
author: Google Cloud、Microsoft（Azure AI Speech）、OpenAI、ElevenLabs（各公式ドキュメント）
published: 各ページの最終更新: Google SSML・Chirp 3 HD 2026-10-26、Gemini-TTS 2026-10-30、Azure 発音 2026-02-25・音素セット 2026-03-25、ElevenLabs 禁止用途ポリシー 2026-10-09
retrieved: 2026-11-09
sources:
  - https://cloud.google.com/text-to-speech/docs/ssml （<sub>・<phoneme>、Last updated 2026-10-26）
  - https://cloud.google.com/text-to-speech/docs/phonemes （「Japanese Yomigana」節）
  - https://cloud.google.com/text-to-speech/docs/chirp3-hd （対応 SSML、custom pronunciations、pause の markup。2026-10-26）
  - https://cloud.google.com/text-to-speech/docs/gemini-tts （2026-10-30。言語表で ja-JP が GA）
  - https://cloud.google.com/text-to-speech/pricing （Gemini-TTS のトークン単価、Chirp 3 HD・Neural2・WaveNet・Standard・Studio の文字単価）
  - https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup-pronunciation （2026-02-25）
  - https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-ssml-phonetic-sets （ja-JP 節、2026-03-25）
  - https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts （ja-JP の声と custom lexicon 対応）
  - https://azure.microsoft.com/en-us/pricing/details/cognitive-services/speech-services/ （価格の数値は JavaScript で描画され、取得できたのは「Neural 0.5 million characters free per month」だけ）
  - https://developers.openai.com/api/docs/guides/text-to-speech （非推奨と終了日、開示の義務、対応言語）
  - https://developers.openai.com/api/docs/pricing （Realtime と音声生成モデルの単価）
  - https://elevenlabs.io/docs/best-practices/prompting/controls （発音: IPA・phoneme・alias・発音辞書）
  - https://elevenlabs.io/docs/models 、https://elevenlabs.io/pricing （プランと credit）
  - https://elevenlabs.io/use-policy （Last Updated: 09 October 2026）
---

# 商用 TTS の日本語と読みの直し方: Google・Azure・OpenAI・ElevenLabs

## 何の文献か

- 4 社の公式ドキュメントと価格表（一次資料）。価格・仕様は日付が大事なので、すべて「2026-11-09 時点の公式ページによる」。音質の比較は無い（ここでは何も呼んでいない。API キーも取っていない）

## 書いてあること

### Google Cloud Text-to-Speech と Gemini-TTS

**読みの直し方（SSML）**

- `<sub alias="にっぽんばし">日本橋</sub>` が公式の日本語の例（SSML ページ「`<sub>`」）
- `<phoneme>` の alphabet は通常 `ipa` か `x-sampa` だが「The only exceptions are Japanese, which must be specified as `yomigana`」（SSML ページ）
- **yomigana の書き方**（phonemes ページ「Japanese Yomigana」）: `<phoneme alphabet="yomigana" ph="ちゅう">中</phoneme>`。ピッチアクセントも書ける: 句の始まりを `^`、下がる位置を `!`。例 `^はし`（端）、`^は!し`（箸）、`^はし!`（橋）。長音は自動、複合語可、カタカナ・ひらがなどちらでも
- custom pronunciations（リクエストに辞書を付けると `<phoneme>` に自動変換）: 例は IPA・X-SAMPA だけで、yomigana を辞書形式で渡せるかは書かれていない
- **Chirp 3: HD** の声は同期リクエストで `<phoneme>` `<sub>` `<say-as>` `<break>` `<prosody>` ほかに対応、ストリーミングでは SSML 非対応（Chirp 3 HD ページ）。速さは `speaking_rate` 0.25〜2.0、間は `markup` 欄に `[pause short]` `[pause long]` `[pause]`
- 「Japanese with Kanji characters is not supported by the `<lang>` tag」（SSML ページ。英文の中に日本語を混ぜる用途の注意）

**Gemini-TTS**

- 「Gemini 3.8 Flash TTS and Gemini 3.8 Flash-Lite TTS are Generally Available (GA) through the Agent Platform API and Agent Studio (with voice design and voice replication in Preview). They aren't available through the Cloud Text-to-Speech API」（Gemini-TTS ページ）。言語表で ja-JP は GA
- 読み・話し方は自然文の指示とタグ（例 `[laughs]` `[extremely fast]`）で制御。SSML の記述はページに無い。特徴として「Enhanced pace and pronunciation control: Controlling delivery speed helps to ensure more accuracy in pronunciation including specific words」

**価格**（pricing ページ）

| 種類 | 無料枠／月 | 単価 |
|---|---|---|
| Gemini 3.8 Flash TTS（Preview の表記）2026-12-31 まで | なし | 入力 $0.50 / 100 万テキストトークン、出力 $9.00 / 100 万音声トークン |
| 同 2027-01-01 から | なし | 入力 $1.00、出力 $18.00 |
| Gemini 3.8 Flash-Lite TTS 2026 年中 | なし | 入力 $0.50、出力 $6.00 |
| Chirp 3: HD | 100 万文字 | $30 / 100 万文字 |
| Instant custom voice | なし | $60 / 100 万文字 |
| Neural2 | 100 万文字 | $16 / 100 万文字 |
| WaveNet・Standard | 400 万文字 | $4 / 100 万文字 |
| Studio | 100 万文字 | $160 / 100 万文字 |

- 「Audio tokens correspond to 25 tokens per second of audio」。Gemini 3.8 Flash TTS の 2026 年の単価なら 1 分の音声の出力は 1,500 トークンで約 $0.0135（担当の計算）
- [[exp-galleria-tts-and-singing]] によれば Gemini 3.8 Flash TTS の全クリップに SynthID が入る

### Azure AI Speech

- ja-JP の声: Neural HD の `ja-JP-Nanami:DragonHDLatestNeural`（女）・`ja-JP-Masaru:DragonHDLatestNeural`（男）、標準の `ja-JP-NanamiNeural`（スタイル `chat`・`cheerful`・`customerservice`）・`KeitaNeural`・`AoiNeural`・`DaichiNeural` ほか（language-support の表）
- **`<phoneme>`**: alphabet は `ipa`・`sapi`・`ups`・`x-sampa`。`sapi` を使えるロケールに ja-JP が入る。「The Speech service phone set for `ja-JP` is based on the native phone Kana set」（音素セットのページ）。例の表に `合成 | ゴ'ウセ | goˈwɯseji` があり、`'` がアクセント記号に当たると読めるが、ページの例は崩れて見える（`所有者 | ショュ'ウ?ャ`）ので、書き方は実際に送って確かめる必要がある。認識できない音素なら HTTP 400
- **カスタム辞書（custom lexicon）**: PLS 形式の XML（`.xml` / `.pls`）を公開 URL（Blob Storage の SAS も可）に置き、SSML で `<lexicon uri="…"/>` と参照する。制限: 100 KB まで、同じ URI は 15 分間キャッシュされ「the custom lexicon change needs to wait 15 minutes at the most to take effect」、1 つの辞書は 1 ロケール、`alphabet` は `ipa` か `x-microsoft-sapi`、大文字小文字を区別、Long Audio API では使えない（発音のページ）。ja-JP は「TTS custom lexicon phoneme target」が Yes（language-support の表）
- 価格: ページの数値は JavaScript で描画されて取れず、取れたのは「Neural: 0.5 million characters free per month」（Free F0）だけ。Personal Voice（本人の声）は「limited access feature」

### OpenAI

- 「The `tts-1`, `tts-1-hd`, and `gpt-4o-mini-tts` models are deprecated and will shut down on **January 6, 2027**. Migrate to `gpt-realtime-2.1-mini` using the Realtime API. This is a change of API workflow: `gpt-realtime-2.1-mini` isn't a supported model for `/v1/audio/speech`」（TTS ガイド、告知は 2026-10-01）
- 「Voices are currently optimized for English」。対応言語は Whisper に準じ、日本語を含む。読みの指定（SSML・辞書）の記述は無く、`instructions`（話し方の指示文）だけ
- 「Our usage policies require you to provide a clear disclosure to end users that the TTS voice they are hearing is AI-generated and not a human voice」
- 単価（pricing）: `gpt-realtime-2.1-mini` の音声出力 $20.00 / 100 万トークン（入力 $10.00）、`gpt-realtime-2.1` は出力 $64.00
- 録音からの custom voice は「limited to eligible customers」（custom voices ガイド）。[[web-means-voice-elevenlabs-google-openai-voice-clone-consent]]

### ElevenLabs

- モデル: `eleven_v4`（90+ 言語）、`eleven_v3`（70+ 言語）、`eleven_multilingual_v2`、`eleven_flash_v2_5`（models ページ）
- **発音**（controls ページ）: Eleven v4 は `/IPA/` をテキスト中に書くと IPA として扱う。SSML の `<phoneme>` は「only compatible with the `eleven_flash_v2` model」（英語用）。それ以外は **alias**（語を別の綴りに置き換える）。発音辞書は TXT か PLS をプロジェクトや API に付け、「Currently we only support pronunciation dictionaries that specify replacements using phoneme or alias tags」「checked from start to end and only the very first replacement is used」、大文字小文字を区別
- v4・v3 は SSML の break に対応しない（controls ページ）
- **プランと価格**（pricing ページ）: Free $0（10k credits/月）、Starter $6/月（初月 $1、30k credits、「Commercial License」「Instant Voice Cloning」）、Creator $22/月（121k、Professional Voice Cloning）、Pro $99/月（600k、API で 44.1kHz PCM）、Scale $299、Business $990。「For V2 Multilingual models, 1 text character equals 1 credit」、Flash/Turbo は 0.5〜1 credit/文字。**Free には Commercial License が含まれない**（Starter 以上の項目に「Commercial License」）
- 禁止用途ポリシー（2026-10-09）: 開示が法で求められる場合は AI であることを明示、透かし・来歴の信号の除去の禁止、同意の無い声の複製の禁止

### 4 社の読みの直し方（まとめ）

| | 漢字の読み | アクセント | 辞書（台本の外に置く） |
|---|---|---|---|
| Google Cloud TTS（Chirp 3 HD ほか） | `<sub alias>`、`<phoneme alphabet="yomigana">` | yomigana の `^` と `!` | custom pronunciations（日本語での可否は未記載） |
| Gemini-TTS | 指示文 | 指示文 | なし（記載なし） |
| Azure | `<sub>`、`<phoneme alphabet="sapi">`（カナ） | sapi の `'`（例の表から。要確認） | PLS の custom lexicon（ja-JP 対応、URL に置く、15 分キャッシュ） |
| OpenAI | 指示文 | 指示文 | なし |
| ElevenLabs | alias（辞書でも可） | v4 の IPA（日本語での効き方は未記載） | 発音辞書（PLS / TXT） |

## この wiki への含意

- **OpenAI の `gpt-4o-mini-tts` の終了（2027-01-06）は経験に直接効く**: [[exp-democracy-river-video]] の英語版は `en/tts.py` で `gpt-4o-mini-tts`（voice onyx）を呼んでいる。2027-01-06 以後はそのままでは再生成できず、Realtime API の `gpt-realtime-2.1-mini` へは「change of API workflow」。英語版を作り直す予定があるなら、それまでに音声を固定（WAV と SHA-256 を残す）しておくのが安全
- **日本語の読みを台本で決めたいなら Google の yomigana が最も表現力がある**（読みとアクセント核を 1 つの記法で、語ごとにインラインで）。[[web-means-voice-voicevox-aivisspeech-user-dictionary]] の AquesTalk 風記法（VOICEVOX）と同じ発想で、台本の speech 欄に `<phoneme>` を書けば [[exp-sutra-sync-subtitles]] の「音声への入力（speech）」欄をそのまま SSML にできる（推測）
- Gemini-TTS と OpenAI は指示文だけで、読みを決定論的に固定する手段が書かれていない。[[exp-qualia-h3-live2d-galleria]] の「生成モデルは語・発音・数値のような離散的な記号を誤る」の向きで、記号の正しさが要る talk・embed のナレーションでは**台本の書き換え（かなに開く）＋耳の検査**が要る
- **開示**: OpenAI は利用ポリシーで「AI-generated and not a human voice」の明示を求める（TTS ガイド）。[[exp-qualia-video]] が義務でなくても「本人・公式の音声ではない」と書いたのと同じ向き
- 価格の桁: 10 分のナレーション（日本語で約 3,000 文字と仮定、担当の推測）は Chirp 3 HD で約 $0.09、Gemini 3.8 Flash TTS（2026 年）で約 $0.14（出力のみ）。ローカルの AivisSpeech は 0。費用は選定の決め手にならず、決め手は読みの直しやすさ・声・規約
- 型: すべて any。商用 TTS は galleria を使わずどこからでも呼べる（API キーは西尾が決める）

## 着手の仕方（未検証。galleria で確かめる）

- **何が表現できるようになるか**: アクセントまで台本で指定した日本語ナレーション（Google の yomigana）。型は talk・embed
- **機械**: どこでも（HTTP API）。入れるもの: なし（curl）。**要: Google Cloud のアカウント・課金の有効化・API キーかサービスアカウント**（西尾が決める）。費用: Chirp 3 HD は月 100 万文字まで無料枠（pricing ページ）。利用条件: Google Cloud の規約（未読）
- **成熟度**: Chirp 3 HD・SSML のページは 2026-10-26 更新
- **最小の手順**（REST の形は Chirp 3 HD ページの例から。日本語の声の名前は推測で、`voices:list` で確かめる）:
  ```bash
  curl -s "https://texttospeech.googleapis.com/v1/voices?languageCode=ja-JP" -H "Authorization: Bearer $(gcloud auth print-access-token)" | jq -r '.voices[].name' | grep -i chirp3
  cat > req.json <<'EOF'
  {"input":{"ssml":"<speak><phoneme alphabet=\"yomigana\" ph=\"^から\">空</phoneme>の吹き出し。<phoneme alphabet=\"yomigana\" ph=\"^は!し\">箸</phoneme>と<phoneme alphabet=\"yomigana\" ph=\"^はし!\">橋</phoneme>。</speak>"},
   "voice":{"languageCode":"ja-JP","name":"<上で見つけた Chirp3-HD の声>"},
   "audioConfig":{"audioEncoding":"LINEAR16","sampleRateHertz":48000}}
  EOF
  curl -s -X POST "https://texttospeech.googleapis.com/v1/text:synthesize" -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json" -d @req.json | jq -r .audioContent | base64 -d > yomigana.wav
  ```
- **動いたと言える確かめ方**: (1) `yomigana.wav` が出る（HTTP 400 なら yomigana の書式が通らない）。(2) 人が聴いて「空」が「から」、「箸」と「橋」のアクセントが違って聞こえる。(3) 同じ文を `<phoneme>` なしでも焼き、違いがあることを確かめる
- **所要の見込み（推測）**: アカウントの準備を除いて 30 分〜1 時間

## Open Questions

- Azure の ja-JP の `sapi` カナ記法でのアクセント記号の正確な書き方（公式の例の表が崩れている）
- Google の custom pronunciations に yomigana を辞書として渡せるか（ドキュメントの例は IPA・X-SAMPA だけ）
- Gemini-TTS に読みを固定する手段（SSML や辞書）が今後入るか
- ElevenLabs の日本語で alias 辞書がどこまで効くか、Eleven v4 の IPA が日本語にどう効くか
- Azure の現在の単価（JavaScript の価格表を取れなかった）
- 4 社の日本語の声の質を同じ原稿で聴き比べた記録は無い
