---
type: source
summary: 効果音を生成する手段（ElevenLabs Sound Effects、Stable Audio Open、TangoFlux、AudioLDM 2、映像から音を付ける MMAudio・HunyuanVideo-Foley）の公式ドキュメントとライセンスを 2026-11-09 に読んだページ。ElevenLabs は 30 秒まで・有料プランで商用、公開モデルは重みが非商用（CC BY-NC・研究のみ）か地域制限付きのものが多く、商用で手元で回せるのは条件付きの Stable Audio Open くらい
video_types: [promo, talk, embed]
url: https://elevenlabs.io/docs/overview/capabilities/sound-effects
author: ElevenLabs、Stability AI、declare-lab（TangoFlux）、Haohe Liu ら（AudioLDM 2）、Ho Kei Cheng ら（MMAudio）、Tencent Hunyuan（HunyuanVideo-Foley）
published: 2026（ElevenLabs docs）、2025（MMAudio・HunyuanVideo-Foley）
retrieved: 2026-11-09
sources:
  - https://elevenlabs.io/docs/overview/capabilities/sound-effects
  - https://elevenlabs.io/terms-of-use
  - https://huggingface.co/stabilityai/stable-audio-open-1.0
  - https://github.com/declare-lab/TangoFlux
  - https://github.com/haoheliu/AudioLDM2
  - https://huggingface.co/cvssp/audioldm2
  - https://github.com/hkchengrex/MMAudio
  - https://github.com/Tencent-Hunyuan/HunyuanVideo-Foley
  - https://github.com/Tencent-Hunyuan/HunyuanVideo-Foley/blob/main/LICENSE
---

# 効果音の生成: ElevenLabs Sound Effects・公開モデル・映像から音（2026-11 時点）

## 何の文献か

公式ドキュメント・README・モデルカード・ライセンス本文。性能は作り手の記述で、第三者の比較ではない。

## 書いてあること

| 手段 | 入力 | 尺 | ライセンス（生成物の商用） | VRAM（公式） | 最新 |
|---|---|---|---|---|---|
| ElevenLabs Sound Effects（API・Web） | 文 | 0.1〜30 秒、ループ可 | 有料プランは商用可、Free は非商用（ToS 2026-10-09） | — | `eleven_text_to_sound_v3`（v2 は 2027-03-01 に廃止予定） |
| Stable Audio Open 1.0 / Small | 文 | 47 秒／11 秒 | Community License（年商 100 万ドル未満は登録で商用可） | 未記載 | — |
| TangoFlux | 文 | 1〜30 秒 | 「non-commercial, research-only」、Stability AI Community License 等にも従う | 未記載 | ICLR 2026 採択（2026-01-28） |
| AudioLDM 2 | 文 | 指定 | 重み CC BY-NC-SA 4.0（HF モデルカード） | 未記載（mps で約 20GB の RAM） | — |
| MMAudio | 映像＋文 | 既定 8 秒（学習も 8 秒） | コード MIT、重み CC BY-NC 4.0 | 約 6GB（16-bit） | CVPR 2025、更新は 2025-03 |
| HunyuanVideo-Foley | 映像＋文 | 未確認 | Tencent Hunyuan Community License（EU・英国・韓国では適用されない。月間 1 億ユーザー超は別契約） | XXL 20GB（offload で 12GB）、XL 16GB（offload で 8GB） | XL は 2025-09-29 |

### ElevenLabs Sound Effects（docs、2026-11-09 時点）

- 「Duration: Range: 0.1 to 30 seconds」「Cost: 40 credits per second when duration is specified」
- 「Looping: Enable seamless looping for sound effects longer than 30 seconds」。ループ用の効果音は「no audible start or end point」
- 出力: 「MP3 for all effects; WAV at 48 kHz for non-looping effects」
- SFX v3 は「follows prompts that contain several instructions more closely ... less likely to clip on high-frequency sounds such as chimes and whistles」と書く。「Results vary by prompt, so compare both models on your own prompts」
- ドラムループ・ベースライン・旋律の素材も作れるが、曲は Music API を使えと書く
- 料金（pricing ページ）: Free 月 1 万 credits、Starter $5/月で 3 万 credits と「Commercial License」。30 秒の効果音は 1,200 credits（尺を指定した場合）なので、Starter で月約 25 本（担当の計算）

### 公開モデル

- Stable Audio Open のモデルカードは「better at generating sound effects and field recordings than music」と書く。学習データは CC0・CC BY・CC Sampling+ の Freesound と FMA（詳細は [[web-means-sound-ace-step-yue2-diffrhythm]]）
- TangoFlux の README: 「created for non-commercial, research-only purposes under the UK data copyright exemption」
- MMAudio: 映像を入れて同期した音を付ける。「inference only takes around 6GB of GPU memory (in 16-bit mode)」「The default output (and training) duration is 8 seconds. ... a large deviation from the training duration may result in a lower quality」。`python demo.py --duration=8 --video=<path> --prompt "..."`。学習データに AudioSet・VGGSound など（権利の整理されていない YouTube 由来を含む）。重みは CC BY-NC 4.0
- HunyuanVideo-Foley: 映像から効果音。ライセンス冒頭「THIS LICENSE AGREEMENT DOES NOT APPLY IN THE EUROPEAN UNION, UNITED KINGDOM AND SOUTH KOREA」。日本は Territory に含まれる。出力を他のモデルの学習に使うことは「Model Derivatives」に当たる条項がある

## この wiki への含意

- 経験の効果音は numpy の関数（kick・clap・impact・whoosh・riser など、[[exp-html-capture-pipeline]]）。抽象的な動きの音はこれで足り、権利も軽い。生成モデル・サービスが効くのは**実在の物音**（紙をめくる、キーボード、雨、ドア、群衆）で、numpy では作りにくい音
- Moreno & Mayer（2000）の「出来事と一対一で一度だけ鳴らした効果音は害にならなかった」（[[web-moreno-mayer-2000-coherence-sounds]]）からは、talk・embed で効果音を足す時は「画面の出来事 1 つに音 1 つ」が無難。Chion の synchresis（[[web-layout-chion-audio-vision-murch-sound]]）は、同期した音が映像の出来事に「くっつく」ことを言う。MMAudio・Foley 系は映像から同期を作るが、重みが非商用か地域条件付き
- **商用で手元で回せる効果音の生成モデルは少ない**。2026-11 時点で条件が一番軽いのは Stable Audio Open（登録・年商条件・「Powered by Stability AI」の表示）。それ以外は ElevenLabs の有料プランか、素材集（[[web-means-sound-soundeffect-lab-maoudamashii-opentracks]]、[[web-means-sound-pixabay-youtube-audio-library-freesound]]）
- embed（流しっぱなし）は会場の PA で鳴る。環境音のループ（ElevenLabs の looping、30 秒×ループ）は embed の背景に合う候補

## 着手の仕方（未検証。galleria で確かめる）

- **何が表現できるようになるか**: 画面の出来事に合わせた実在の物音（1〜10 秒）と、継ぎ目の無い環境音のループ。効く型: talk・embed（控えめな SE）、promo（impact・whoosh の質感）
- **機械と入れるもの**:
  - 案 A（手元、商用は条件付き）: galleria WSL に Stable Audio Open 1.0（diffusers の `StableAudioPipeline`）。GPU 要・VRAM の見込み 8GB 前後（推測。1B パラメータを fp16 で、公式の記述は無い）。要: Hugging Face アカウントとモデルのゲートへの同意（西尾が決める）。商用なら Stability AI への登録
  - 案 B（API）: ElevenLabs Sound Effects。要: アカウント・API キー・費用（Starter $5/月以上で商用）
- **成熟度**: Stable Audio Open 1.0 は 2024 公開で更新は少ないが diffusers に取り込み済み。ElevenLabs は v3 が現行
- **最小の手順（案 A、WSL、モデルカードの diffusers の例より）**:
  ```bash
  mkdir -p ~/video-tools-trial/sao && cd ~/video-tools-trial/sao
  uv venv && source .venv/bin/activate
  uv pip install torch diffusers transformers accelerate soundfile torchsde   # 版はその時の最新（推測で列挙。torchsde は sampler 用で要否未確認）
  huggingface-cli login            # ゲート付きモデルのため（西尾がトークンを用意）
  python - <<'EOF'
  import torch, soundfile as sf
  from diffusers import StableAudioPipeline
  pipe = StableAudioPipeline.from_pretrained("stabilityai/stable-audio-open-1.0", torch_dtype=torch.float16).to("cuda")
  g = torch.Generator("cuda").manual_seed(0)
  a = pipe("The sound of a hammer hitting a wooden surface.", negative_prompt="Low quality.",
           num_inference_steps=200, audio_end_in_s=10.0, num_waveforms_per_prompt=3, generator=g).audios
  for i, x in enumerate(a):
      sf.write(f"hammer_{i}.wav", x.T.float().cpu().numpy(), pipe.vae.sampling_rate)
  EOF
  ```
- **動いたと言える確かめ方**: `hammer_0.wav`〜`hammer_2.wav` ができ、`ffprobe` で 44.1kHz・2ch・約 10 秒。`ffmpeg -i hammer_0.wav -af astats -f null -` で無音でない。音の良し悪しは耳で（機械では判定しない）
- **所要の見込み（推測）**: ゲートの同意後、環境作りとモデル取得で 1 時間。1 本の生成は数十秒

## Open Questions

- Stable Audio Open の VRAM の実測は公式に無い。galleria で `nvidia-smi` の最大値を記録する
- MMAudio・HunyuanVideo-Foley の「映像から音」は embed の作り方（無音の画面収録に後から音）に合うが、MMAudio は非商用、Hunyuan は地域とユーザー数の条件。業務の発信物に使えるかは西尾が決める
- ElevenLabs の効果音が Content ID に当たる事故（他人が同じ生成物を登録する）は、生成物が非独占かどうかに依る。ElevenLabs が出力を他の利用者に重ねて出すかは書かれていない
- 2026 年に入って出た公開の効果音モデル（商用可のもの）は、この調査では見つけていない（探索は README を読んだ 6 件のみ）
