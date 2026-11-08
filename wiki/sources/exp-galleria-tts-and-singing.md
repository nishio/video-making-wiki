---
type: source
summary: galleria で試したナレーション用 TTS（SAPI、AivisSpeech、VOICEVOX の C API、Irodori-TTS v4.1-Small と v4-Large）と歌声合成（SoulX-Singer、終了）の実測と判断。話者を固定するのは参照音声だけ、license で在庫が二分される、機械の数値は耳の判定の代わりにならない
video_types: [any]
sources:
  - galleria-wiki wiki/qualia-san-explainer-video-pilot.md（音声の節）
  - galleria-wiki wiki/local-expressive-audio-synthesis.md
  - galleria-wiki wiki/voice-reference-conditioning.md
  - galleria-wiki wiki/irodori-tts-runtime-api.md
  - galleria-wiki wiki/irodori-tts-v4-large.md
  - galleria-wiki wiki/voicevox-offline-c-api.md
  - galleria-wiki wiki/soulx-singer-english-singing.md
  - galleria-wiki wiki/gemini-3-8-flash-tts.md、wiki/ai-voice-rights.md、wiki/ai-music-generation-rights.md
  - galleria-wiki の raw（ページ内の出典表記）: 2026-08-12-qualia-san-explainer-video-tts-feedback-followup.md、2026-08-12-aivisspeech-license-review.md、2026-09-08-irodori-speaker-reference.md、2026-09-15-easy-irodori-tts-colab-notebook.md、2026-09-15-cosyvoice-and-seed-vc-retired.md、2026-09-26-voicevox-offline-c-api.md、2026-09-30-irodori-tts-v4-large-local-run.md、2026-10-06-soulx-singer-english-singing-ended.md
---

# galleria での TTS と歌声合成（2026-08〜10）

## ナレーションに使ったもの（完成動画まで行ったもの）

| エンジン | 使った所 | 結果 |
|---|---|---|
| Microsoft Haruka Desktop（SAPI COM → WAV） | 解説動画の第一作（2026-08-12）。Rate 6 | 人間の評価で「音声合成に改善の余地がありまくり」。読み違い（「空」を「から」と読めない）、中黒での区切り、声の古さ |
| AivisSpeech Engine 1.2.0、「まお 1.2.0／おちつき」（style ID `888753763`、`speedScale 1.0`・`pitchScale 0.0`・`intonationScale 0.9`） | メイキング（109 秒）と第三作（6 分 33 秒） | VOICEVOX・AivisSpeech・SAPI を同じ 15〜30 秒の sample で比べ、人間の評価で決定。第三作の通し視聴でも `こえつき`／`こえしつ` の読みを直す必要があった |

制作の全体は [[exp-qualia-video]]。

### 読みを直す方法（実際にやったこと）

- 画面に出す文字と TTS に渡す文字を台本の別フィールドにする（`caption` / `narration`）。例: 表示 `空の吹き出し` / 読み `からの吹き出し`、表示 `ホモ・サピエンス` / 読み `ホモサピエンス`、`93.12秒`・`H.264`・`1.8%` は読み上げ用の表記へ。
- 比較用の短い sample には、問題になった語と、これから頻出する技術語（ComfyUI、FLUX.2、ReferenceLatent、英数字）を入れる。
- それでも通し視聴で聞き違える読みが残った。最後は耳。

### 権利の確認（AivisSpeech）

Engine は LGPL-3.0、「まお」「コハク」は ACML 1.0。禁止事項に当たらない動画の公開・収益化・商用利用ができ、credit は任意。ローカルの AIVMX の SHA-256 が AivisHub の掲載値と一致することも確かめた。ACML は実在の製品への批判・攻撃目的、なりすまし、政治・宗教への賛否の呼びかけなどを禁じる。

## VOICEVOX をサーバーなしで呼ぶ（2026-09-26）

VOICEVOX Engine 配布版 0.25.2 CPU に入っている core 0.16.2 の DLL を Python の ctypes から直接呼び、HTTP サーバーなしで 9 区間・合計約 79 秒の音声を作った。呼ぶ順は `voicevox_onnxruntime_load_once` → `voicevox_open_jtalk_rc_new` → `voicevox_synthesizer_new` → `voicevox_voice_model_file_open` / `voicevox_synthesizer_load_voice_model` → `voicevox_synthesizer_create_audio_query` → JSON を調整 → `voicevox_synthesizer_synthesis`。

- 設定例: 速度 0.83、抑揚 0.65、音量 1、24 kHz mono、前後の無音 0.18 / 0.25 秒。最初の 12.725 秒の clip を約 1.39 秒（CPU 4 threads）。
- 四国めたん（ささやき）はこの版の `model/5.vvm` で style ID 36。ID やファイル構成は配布版ごとに確かめ直す。
- 48 kHz に変換して約 135 秒に結合できた。左右同じ stereo は dual mono でありバイノーラルではない。**聴感の評価はしていない**。

## Irodori-TTS（v4.1-Small、MIT）の実測（2026-09-08）

- **話者を固定するのは参照音声だけ。** 中立の日本語 3 文 × seed 0–15 = 48 本を参照なし（`--no-ref`）で焼くと、同じ seed・同じ caption でも文を変えると別人になった。caption に「20代後半の女性」と書いても声は決まらない。caption が動かすのは演技。
- 参照が無くても自分の出力から作れる: ① `--no-ref` で候補を大量に焼く（48 本で 95 秒、約 2 秒/本）② **人間が 1 本選ぶ** ③ その 1 本を `--ref-wav` にして焼き直す ④ 飽和していない本を集めて `--ref-wavs` の束にする。束は合計 30 秒が目安（README によれば 30 秒あたりで話者類似度の伸びがほぼ飽和）。1 本を参照にした 16 本は全部同じ話者になった。
- 条件の強さは `cfg_scale_text` / `cfg_scale_caption` / `cfg_scale_speaker` = 3.0 / 3.0 / 5.0 で回した。
- **F0（声の高さ）の統計は話者が揃っているかの代わりにならなかった。** 同じ文を読んだ他の seed と比べる正規化で seed の順位は出たが、耳は「揃っていない」と判定した。採用も棄却も耳で決める。機械が確実に効くのはピーク飽和のような欠陥だけ。
- 落とし穴: 中立の平文でも 16 本中 5 本が peak ≥ 0.98。参照は −16 dB に正規化されるので、飽和した本を束に入れると毒になる。SilentCipher の透かしは常に入り、無効化の flag が無い。
- 長さは既定でモデルが予測する（`seconds=None`）。`duration_scale` 0.5〜1.5 で伸縮、秒数を手で与えることもできる。尺を timeline に合わせたいときに効く（galleria ではこの挙動を意識せずに 66 本を焼いていた）。
- プログラムから回すなら `irodori_tts.inference_runtime` でモデルを常駐させ、`num_candidates` で 1 リクエストから複数本を焼ける。seed は呼び出し側で振って記録する（後で同じ声を取り出すため）。これは第三者の Colab ノートブックを読んだ記録で、galleria では未実行。

### v4-Large（3.29B）は動いたが音は未聴（2026-09-30）

- RTX 5080 の bf16 で 1 文（3.96 秒の音声）を生成。重みの読み込み込みで 23.7 秒、読み込み後 4.08 秒（長さ予測 0.94、生成 2.68、変換 0.16、透かし 0.27）。
- 上流の `InferenceRuntime.from_key` は fp32 のまま GPU に移してから bf16 にするので 16GB で OOM になる。先に CPU 上で bf16 にしてから移すよう作業用コピーを直した（上流には出していない）。
- license が MIT から **Gemma Terms of Use** に変わった。配布物には Small が残る。2026-10-01 に容量確保のため重みを削除した。

## license で在庫が二分される

配布物に載せるなら、選ぶ順は「音が良い順」ではなく「license が閉じている順」から始まる、と galleria-wiki は書いている。Irodori-TTS-v4.1-Small は MIT、v4-Large は Gemma 規約、VoxCPM 本体は Apache-2.0。声の権利は license とは別の層で、日本では 2026-08-07 公表の法務省の解釈指針（「肖像、声等の無断利用による民事責任の在り方に関する検討会」報告書）がある。線は「出力が本人の声に似ていないこと」で、galleria-wiki の実務上の結論は「**公開前に誰かの声に聞こえないかを人間が聴く関門を置く。似ていたら捨てる**」。参照の束で話者を固定するなら、束を作ったときに一度聴けばよい。（ai-voice-rights.md、voice-reference-conditioning.md）

## 歌声: SoulX-Singer で英語の歌（2026-10-03〜06、終了）

galleria の別 project、polis-magi-op の英語の歌声に試した（制作の側から見た記録は [[exp-polis-magi-op]]）。

- 参照の声は VOICEVOX 波音リツに旋律を「ら・る・れ…」で歌わせて作った。SoulX-Singer は日本語の音素を持たないので、参照のメタデータは英語の音素で近似した（ら → L-AA1 など）。目標は MIDI の旋律に英語の歌詞を 1 音節 1 音で割り付け、行ごとに最大 6 回生成して Whisper の書き起こしと歌詞の一致で版を選んだ。RTX 5080、CUDA・fp16 で動いた。

| 版 | やったこと | 所有者の評価 |
|---|---|---|
| サビ 2 行の試験 | 仮の歌詞 | 「使えそうではある」 |
| `out_full3`（全編） | `auto_shift` あり。行ごとに参照の声域へ半音単位で移調し、伴奏と調が ±2〜7 半音ずれた | 「音程がメチャクチャで聞くに耐えない」 |
| `out_full4`（全編） | `auto_shift` なし、版の選択に音程の減点。音節の 96% が楽譜から 0.5 半音以内 | 「全然ダメ」 |

- **`auto_shift` は伴奏の付く歌には使えない**（声域に合わせる移調が、伴奏と合わない調を作る）。
- **Whisper の一致も、楽譜に対する音程の % も、良し悪しの判定にならなかった。** 前者は音程を見ない。後者は伴奏との関係・音の揺れ・発声の質を見ない。どちらも足切りにしか使えない。
- 所有者の判断: 「soulx-singerは英語の歌を歌わせられないかと少し試行錯誤してみたが満足いくクオリティにならなかったので終了」。repo とモデル（約 7.8 GB）は 2026-10-06 に削除。polis-magi-op の `sing/` のスクリプトは削除したパスを参照していてもう動かない。

## 楽曲（BGM・主題歌）

galleria には楽曲生成の実行記録が無い。2026-09-04 の調査で、楽曲は実用的なローカルモデルが無く Suno / Udio / ElevenLabs Music など外部 platform に頼ることになり、選定の律速は音質ではなく規約と訴訟の状況だと整理した。「収益化する作品の楽曲は ElevenLabs Music を第一候補にする」「Suno/Udio は検証用の scratch に留める」（Suno は有料 plan でも自らを author と称するため）。「台詞は local、楽曲は hosted」という非対称を意識して素材台帳を分ける、とされている。（ai-music-generation-rights.md。外部情報の整理で、galleria での検証ではない）

## その他（呼んでいない・使っていない）

- Gemini 3.8 Flash TTS（2026-09-23 公開、hosted）: 単発の既定出力は 24 kHz・mono・16 bit WAV、全クリップに SynthID。公開仕様を読んだだけで API は呼んでいない。
- 出力はどれも mono。動画の音を空間に置くなら、生成の外で決定論的に空間化する（オブジェクトベース）と galleria-wiki は書いている（spatial-audio-object-vs-ambisonics.md）。実測済みのサンプリングレートは一部のモデルだけで、48kHz で納めたいなら出力レートが天井になる。

## 再利用できる部品

- VOICEVOX core を ctypes で呼ぶ手順（上の関数順）
- Irodori の参照ブートストラップ手順、`--ref-normalize-db -16`、束は peak で選ぶ

## Open Questions

- Irodori を完成動画のナレーションに使った記録はまだ無い。AivisSpeech と耳で比べた記録も無い。
- VOICEVOX C API で作った 135 秒の音声が何に使われ、聴いてどうだったか。
