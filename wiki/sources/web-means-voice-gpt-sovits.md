---
type: source
summary: GPT-SoVITS の公式 README（日本語版・英語版）・変更履歴・API（api_v2.py）・推論の実装（2026-11-09 時点）。MIT。参照音声 3〜10 秒でのゼロショット、1 分程度の学習データでの微調整、日本語の入出力、V5（2026-10-05 公開）。日本語の読みは pyopenjtalk で、ユーザー辞書は MeCab 形式の CSV。自分の声をローカルで複製する経路の一つ
video_types: [talk, embed, promo]
url: https://github.com/RVC-Boss/GPT-SoVITS
author: RVC-Boss（GPT-SoVITS の開発者）ほかコントリビューター
published: 2024（初版）／2026-10-05（V5）
retrieved: 2026-11-09
sources:
  - https://github.com/RVC-Boss/GPT-SoVITS/blob/main/docs/ja/README.md （日本語 README）
  - https://github.com/RVC-Boss/GPT-SoVITS/blob/main/README.md （英語 README の V2Pro・V5 Release Notes）
  - https://github.com/RVC-Boss/GPT-SoVITS/blob/main/docs/en/Changelog_EN.md （202610 まで）
  - https://github.com/RVC-Boss/GPT-SoVITS/blob/main/api_v2.py （API の引数）
  - https://github.com/RVC-Boss/GPT-SoVITS/blob/main/GPT_SoVITS/TTS_infer_pack/TTS.py （参照音声の長さの検査）
  - https://github.com/RVC-Boss/GPT-SoVITS/blob/main/GPT_SoVITS/text/japanese.py （日本語のユーザー辞書）
  - https://huggingface.co/lj1995/GPT-SoVITS （事前学習の重み、license: mit、最終更新 2026-10-06。gsv-v5-pretrained/s2Gv5dev.pth・s2Gv5turbo.pth 各約 766 MB、vocoder.pth 約 58 MB）
  - GitHub API: star 約 64,500、最終 push 2026-10-31、タグ付きリリースの最新は 20250606v2pro（参考）
---

# GPT-SoVITS

## 何の文献か

- 開発者の公式 README・変更履歴・ソース。性能の図（SeedTTS Eval の中国語テストセットでの声質類似度）は作り手の自己評価で、日本語の評価ではない

## 書いてあること

### 機能（日本語 README「機能」）

1. 「**Zero-Shot TTS:** たった 5 秒間の音声サンプルで、即座にテキストからその音声に変換できます」
2. 「**Few-Shot TTS:** わずか 1 分間のトレーニングデータでモデルを微調整し、音声のクオリティを向上」
3. 多言語: 英語・日本語・韓国語・広東語・中国語（学習データと違う言語でも推論できる、と英語 README）
4. WebUI に、伴奏の分離、学習セットの自動分割、ASR、書き起こしの校正の道具が入る。日本語・英語の ASR には Faster Whisper Large V3 を `tools/asr/models` に置く（英語 README）

- 実装上の制約: 推論の参照音声は **3〜10 秒**でないとエラー（`TTS.py`: 16 kHz で 48,000 サンプル未満か 160,000 超なら「参考音频在3~10秒范围外，请更换！」）

### 版

| 版 | 主な変化（README の Release Notes） |
|---|---|
| V2 | 声質の類似度が上がり、微調整なしでも近づく |
| V3 / V4（2025-02 / 04） | V4 は V3 の金属的なノイズを直し、48 kHz をネイティブ出力 |
| V2Pro（2025-06） | 「Slightly higher VRAM usage than v2, surpassing v4's performance, with v2's hardware cost and speed」。平均的な音質の学習セットなら v1/v2/v2Pro は良い結果、v3/v4 は出ない。v3/v4 は学習セット全体より参照音声の音色に寄る |
| **V5（2026-10-05）** | 「Significantly improved voice similarity without SoVITS fine-tuning」、ボコーダーの更新で高域の折り返しノイズを減らす、`cuda_graph` と `flash_attention` で推論を速く。README は `cuda_graph_accel_v5` ブランチからの導入を指示（変更履歴は 2026-10-05「Release the new V5 version」） |

- 最近の変更履歴: 2026-08-18「New ASR models」、2026-08-28 単一 GPU の学習で DDP を飛ばして速く、2026-10-05 V5（Changelog_EN.md）

### 導入（README）

- テスト済み: Python 3.10〜3.12、PyTorch 2.5.1〜2.8、CUDA 11.8〜12.8、Apple silicon、CPU
- Windows: 統合パッケージ（`GPT-SoVITS-v3lora-20250228.7z`）を解凍して `go-webui.bat`。**統合パッケージは 2025-02 の版**のままで、V5 は含まない
- Linux（WSL を含むと推測）: `conda create -n GPTSoVits python=3.10` → `bash install.sh --device <CU126|CU128|ROCM|CPU> --source <HF|HF-Mirror|ModelScope> [--download-uvr5]`
- macOS: 「Mac で GPU を使用して訓練されたモデルは、他のデバイスで訓練されたモデルと比較して著しく品質が低下するため、当面は CPU を使用して訓練することを強く推奨」
- Docker イメージ `xxxxrt666/gpt-sovits` もある（「Docker イメージのリリースは比較的遅い」）
- 学習データの書式: `vocal_path|speaker_name|language|text`（日本語は `ja`）
- 微調整の流れ: 音声のパス → 分割 → ノイズ除去（任意） → ASR → 書き起こしの校正 → 学習
- API: `python api_v2.py -a 127.0.0.1 -p 9880 -c GPT_SoVITS/configs/tts_infer.yaml`、`/tts` に `text`・`text_lang`・`ref_audio_path`・`prompt_text`・`prompt_lang` ほか。`seed` で再現（既定 -1）、`speed_factor`、`text_split_method`（cut0〜cut5）

### VRAM

- README に推論・学習の VRAM の具体的な数値は**無い**。`is_half`（fp16）で「reduce memory usage」、V2Pro は「v2 よりやや多い」とだけ

### 日本語の読み

- `japanese.py` は pyopenjtalk で読みを作る。`GPT_SoVITS/text/ja_userdic/userdict.csv` があれば、hash が変わったときに `pyopenjtalk.mecab_dict_index` で `user.dict` に作り直し、`update_global_jtalk_with_user_dict` で読み込む。**辞書は MeCab 形式の CSV**（VOICEVOX の HTTP API とは違う。[[web-means-voice-voicevox-aivisspeech-user-dictionary]]）

### ライセンス

- コードは MIT。HF の事前学習の重み `lj1995/GPT-SoVITS` も `license: mit`
- README・LICENSE に**利用の禁止事項や同意の要件は無い**（MIT の条文だけ）。他人の声を参照にする行為を縛るのはライセンスではなく法と各国の規則

## この wiki への含意

- **自分の声をローカルで複製する経路として、Irodori-TTS の参照（[[exp-galleria-tts-and-singing]]）と同じ「参照音声で話者を決める」型に、微調整（1 分〜）を足せるもの**。経験の「話者を固定するのは参照音声だけ」「参照は 30 秒の束が目安」に対し、GPT-SoVITS の推論の参照は 1 本 3〜10 秒に制限され、補助参照（`aux_ref_audio_paths`）で混ぜる設計。束の作り方の経験はそのままは移らない
- 経験の「F0 の統計も Whisper の一致も良し悪しの判定にならなかった」（[[exp-galleria-tts-and-singing]]）は GPT-SoVITS でも同じはずで、採否は耳。`seed` を記録して同じ声を取り出せるようにするのは経験の Irodori の運用と同じ
- [[exp-galleria-tts-and-singing]] の CosyVoice と Seed-VC は 2026-09-15 に退役している（galleria-wiki raw の題名から）。中国発の多言語ゼロショット TTS を日本語のナレーションに使って満足しなかった前例があるので、GPT-SoVITS も**まず 15〜30 秒の共通原稿で AivisSpeech と比べる**（[[exp-qualia-video]] の手順）のが順当
- ライセンスが MIT で閉じているので、[[exp-galleria-tts-and-singing]] の「license が閉じている順」では在庫の上位に入る。ただし声の権利（本人の同意、他人の声に似ていないか）は license の外で、[[web-means-voice-elevenlabs-google-openai-voice-clone-consent]] にまとめた
- 型: talk・embed で「西尾本人の声のナレーション」を作る手段。promo で本人の声を使う場合も同じ。voice principle の研究（[[web-mayer-2003-voice-principle-tts]]）に本人の声の複製と TTS を比べたものは無い

## 着手の仕方（未検証。galleria で確かめる）

- **何が表現できるようになるか**: 西尾本人の声（または許諾を得た声）の日本語ナレーションをローカルで。型は talk・embed（流しっぱなしの embed のナレーションを本人の声にする）、promo の語り
- **機械**: galleria WSL（`install.sh` が Linux 向け）。入れるもの: GPT-SoVITS main（V5 は `cuda_graph_accel_v5` ブランチ、README 指示）、conda の Python 3.10、`--device CU128`（RTX 5080 は CUDA 12.8 系が要ると推測）、事前学習の重み（V5 で約 1.6 GB＋共通部分）、日本語 ASR 用の Faster Whisper Large V3。費用 0、アカウント不要（HF から取得）。利用条件: MIT。GPU 要・VRAM の見込み: 推論は数 GB 程度（推測。公式の数値なし）、学習は不明
- **成熟度**: star 約 64,500、最終 push 2026-10-31、V5 は 2026-10-05。更新は続いているが、タグ付きリリースは 2025-06 で止まっていて、Windows 統合パッケージも 2025-02 の版
- **最小の手順**（WSL。README のコマンドを元に、ブランチ指定とディレクトリは推測）:
  ```bash
  mkdir -p ~/video-tools-trial && cd ~/video-tools-trial
  git clone -b cuda_graph_accel_v5 https://github.com/RVC-Boss/GPT-SoVITS.git && cd GPT-SoVITS
  conda create -n GPTSoVits python=3.10 -y && conda activate GPTSoVits
  bash install.sh --device CU128 --source HF
  # V5 の重みを GPT_SoVITS/pretrained_models/gsv-v5-pretrained/ に置く（README の指示）
  python api_v2.py -a 127.0.0.1 -p 9880 -c GPT_SoVITS/configs/tts_infer.yaml
  # 別の端末で（ref.wav は西尾が録った 3〜10 秒、ref.txt はその書き起こし）
  curl -sG http://127.0.0.1:9880/tts --data-urlencode "text=これは試験用の文です。" --data-urlencode text_lang=ja \
    --data-urlencode ref_audio_path=$PWD/ref.wav --data-urlencode "prompt_text=$(cat ref.txt)" --data-urlencode prompt_lang=ja \
    --data-urlencode seed=1 -o out.wav
  ```
  （conda が WSL に入っているかは未確認。無ければ README の「手動インストール」の pip 手順を uv の venv で行う、と推測）
- **動いたと言える確かめ方**: (1) `out.wav` ができ、`ffprobe` で尺が 1 秒以上、サンプリングレートが出る。(2) 3 秒未満か 10 秒超の参照を渡すと「参考音频在3~10秒范围外」のエラーになる（参照の検査が効いている）。(3) 同じ `seed` で 2 回焼いて同じ WAV（SHA-256 一致）になるか記録する。(4) [[exp-qualia-video]] の比較用原稿を AivisSpeech（まお）と並べ、本人と第三者が聴いて「本人に聞こえるか」「読みが正しいか」を判定
- **所要の見込み（推測）**: 導入 1〜3 時間（Blackwell 向けの torch の版合わせ次第）、ゼロショットの試聴 30 分。微調整は録音とデータ作りを含めて半日

## Open Questions

- RTX 5080 16GB での推論・学習の VRAM（公式に数値なし）
- V5 が main に統合されたか（README は別ブランチを指すが、main の `api_v2.py` は `v5turbo`・`v5dev` に言及している）
- 日本語の品質の第三者評価（README の図は中国語のテストセット）
- `userdict.csv` の列の書き方（アクセント型をどう書くか）は MeCab / pyopenjtalk の辞書形式を読んでいない
