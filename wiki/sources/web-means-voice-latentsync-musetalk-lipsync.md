---
type: source
summary: 口の動きを音声に合わせる公開モデルの公式 README・モデルカード（2026-11-09 時点）。既存の動画の口だけを直す LatentSync（1.5 は推論 8GB、1.6 は 18GB。コード Apache-2.0、1.6 の重みは OpenRAIL++）・MuseTalk 1.5（MIT、重みも商用可、4GB の GPU で 8 秒に約 5 分）・Wav2Lip（商用禁止）と、画像と音声から話す人物の動画を作る InfiniteTalk（Apache-2.0）・daVinci-MagiHuman（Apache-2.0、15B）・LongCat-Video-Avatar 1.5（MIT、アニメ調も対象）を並べた
video_types: [promo, talk, embed]
url: https://github.com/bytedance/LatentSync
author: ByteDance（LatentSync）、Tencent Music Lyra Lab（MuseTalk）、Rudrabha Mukhopadhyay ほか（Wav2Lip）、MeiGen-AI（InfiniteTalk）、GAIR・Sand.ai（daVinci-MagiHuman）、Meituan LongCat（LongCat-Video-Avatar）
published: 2025-03-14（LatentSync 1.5）／2025-06-11（LatentSync 1.6）／2025-03-28（MuseTalk 1.5）／2020（Wav2Lip）／2025-08-18（InfiniteTalk の重み）／2026-03-21（daVinci-MagiHuman）／2026-05-21（LongCat-Video-Avatar 1.5）
retrieved: 2026-11-09
sources:
  - https://github.com/bytedance/LatentSync （README、inference.sh。最終 push 2025-06-20）、https://huggingface.co/ByteDance/LatentSync-1.6 （license: openrail++）、https://huggingface.co/ByteDance/LatentSync-1.5 （openrail++）、docs/changelog_v1.5.md・changelog_v1.6.md
  - https://github.com/TMElyralab/MuseTalk （README の「Disclaimer/License」。最終 push 2025-09-26）
  - https://github.com/Rudrabha/Wav2Lip （README。GitHub API で license は null）
  - https://huggingface.co/MeiGen-AI/InfiniteTalk （モデルカード、license: apache-2.0）
  - https://huggingface.co/GAIR/daVinci-MagiHuman （モデルカード、apache-2.0）、https://github.com/GAIR-NLP/daVinci-MagiHuman （README）
  - https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.5 （モデルカード、mit）
  - 探索の手がかり: Web 検索（sync.so・pixazo などの比較記事。主張は上の一次資料で確かめ、二次記事の数値は使っていない）
---

# 口の動きの同期: LatentSync・MuseTalk・Wav2Lip と、音声から人物を動かす新しいモデル

## 何の文献か

- 各開発元の README・モデルカード（一次資料）。品質の比較は開発元の自己評価だけ。VRAM の数値は開発元の記述で、galleria で測った値ではない

## 書いてあること

### 既存の動画の口だけを音声に合わせる（ダビング型）

| モデル | 何をする | 推論の VRAM | ライセンス | 出典 |
|---|---|---|---|---|
| **LatentSync 1.5** | 動画の口元を音声に合わせる。Whisper の音声埋め込みを U-Net に cross-attention で入れる潜在拡散 | 「**8 GB** with LatentSync 1.5」 | コード Apache-2.0 | README |
| **LatentSync 1.6** | 512×512 で学習し「mitigate the blurriness problem」 | 「**18 GB** with LatentSync 1.6」 | 重みは HF で `openrail++` | README、HF |
| **MuseTalk 1.5** | 「modifies an unseen face according to the input audio, with a size of face region of 256 x 256」。V100 で 30fps 以上の実時間 | 最小構成として「RTX 3050 Ti Laptop GPU with 4GB VRAM. In fp16 mode, generating an 8-second video takes approximately 5 minutes」 | 「code: MIT … no limitation for both academic and commercial usage」「model: … available for any purpose, even commercially」。ただし whisper・ft-mse-vae・dwpose・S3FD などはそれぞれのライセンスに従う。テストデータは非商用研究のみ | README |
| **Wav2Lip** | 同上（2020 年の手法） | — | 「As the models are trained on the LRS2 dataset, **any form of commercial use is strictly prohibited**」。README の先頭は商用版（sync.）の案内 | README |

- LatentSync の推論（`inference.sh`）: `python -m scripts.inference --unet_config_path configs/unet/stage2_512.yaml --inference_ckpt_path checkpoints/latentsync_unet.pt --inference_steps 20 --guidance_scale 1.5 --enable_deepcache --video_path … --audio_path … --video_out_path video_out.mp4`。`inference_steps` 20〜50（高いほど画質、遅い）、`guidance_scale` 1.0〜3.0（高いほど口が合うが「may cause the video distortion or jitter」）。導入は `source setup_env.sh`、Gradio は `python gradio_app.py`
- LatentSync の README のデモには「anime videos are from VASA-1」とあり、アニメ調の顔の例も載っている
- MuseTalk は入力動画を 25fps にすることを勧める（「the same fps used during model training」）。顔の領域が 256×256 で「has not yet reached the theoretical resolution bound」（限界の節）

### 画像（と文）と音声から、話す人物の動画を作る（音声駆動の生成）

| モデル | 要点 | 必要な GPU | ライセンス | 出典 |
|---|---|---|---|---|
| **InfiniteTalk** | 長さの制限なく音声駆動で動画をダビング・生成（名前と README の説明から）。base は Wan2.1-I2V-14B-480P（[[exp-qualia-h3-live2d-galleria]]） | 公式の数値は読んでいない。galleria-wiki は Wan2.2 の実測から 16GB に入る見込みとしたが未検証 | Apache-2.0。「We claim no rights over the your generated contents」 | HF |
| **daVinci-MagiHuman** | 15B。音声と映像を一緒に生成。対応言語に**日本語**を含む 6 言語。「5-second 256p video in 2 seconds and a 5-second 1080p video in 38 seconds on a single H100」。DMD-2 蒸留で 8 ステップ | H100 での数値のみ。消費者向け GPU の数値は README に無い | Apache-2.0（基盤・蒸留・超解像・推論コードすべて） | HF、GitHub |
| **LongCat-Video-Avatar 1.5** | LongCat-Video の上の音声駆動の人物動画。音声エンコーダを Whisper-Large に。「Robustly generalizes to **anime**, animals, and complex real-world conditions」。8 ステップの蒸留。`--use_int8` で VRAM を減らせる | README の例は `torchrun --nproc_per_node=2`（2 GPU）。単一 16GB での可否は書かれていない | MIT（重み） | HF |

- LongCat の評価: 6 場面（ニュース、知識教育、日常、娯楽、歌、商品宣伝）× 中国語・英語 × 写実・アニメ、508 組、770 人の評価者が 1〜5 の人らしさで 13,240 判定（モデルカード。開発元による評価）

## この wiki への含意

- **[[exp-qualia-h3-live2d-galleria]] の教訓が先に立つ**: 版 3（口だけを重ねて補正）は「同期は改善したが、顔の動きとは別の表現の層になった」。galleria-wiki は「LatentSync（既存動画の口だけを音声に合わせる）も版 3 と同じ所に戻る」と注意している。**ダビング型（LatentSync・MuseTalk）は、演技を作る道具ではなく、合っていない口を直す道具**。H3 で作った魅力的なテイクの音声を VOICEVOX に差し替えたあと、口だけを合わせる用途なら当てはまるが、生命感は戻らない可能性が高い（経験からの推論）
- **音声駆動の生成（InfiniteTalk・MagiHuman・LongCat）は H3 と同じ側**（声と顔の協調を一度に作る）。経験の「H3 を母体に残す」方針の代わりになりうるのは、音声を外から与えられるこちら側。台詞を VOICEVOX・AivisSpeech で決定論的に作り、その音声で人物を動かせば、版 2 の「台詞は正しいが口が合わない」を避けつつ顔の協調を生成に任せられる（設計の推論で未検証）
- **アニメ調**: クオリアさんはアニメ調。LongCat-Video-Avatar 1.5 はアニメへの汎化を明記し、LatentSync のデモにもアニメの顔がある。MuseTalk・Wav2Lip は写実の顔の検出（S3FD・dwpose）が前提で、アニメ調で顔が取れるかは不明
- **ライセンス**: 商用で使えるのは MuseTalk（MIT＋重みも商用可）、LatentSync（コード Apache-2.0、1.6 の重みは OpenRAIL++ の利用制限つき）、InfiniteTalk・MagiHuman（Apache-2.0）、LongCat（MIT）。**Wav2Lip は商用禁止**。H3 のライセンスの地域・開示の条件は [[web-genvid2-wan-ltx-hunyuanvideo-minimax-h3]]
- **galleria の 16GB に入る見込み**: LatentSync 1.5（8GB）と MuseTalk（4GB で動いた記述）は入る。LatentSync 1.6（18GB）は公式の数値で入らない。MagiHuman・LongCat は公式に単一の消費者 GPU の数値が無い
- 型: promo（キャラクターや人物が語る数秒の見せ場）、talk（話し手のいる解説）、embed（講演に埋め込む、話し手の顔が話す短い映像）。[[exp-qualia-video]] の「解説動画は静止が既定」の結論からは、talk で常に口を動かす必要は無い

## 着手の仕方（未検証。galleria で確かめる）

- **何が表現できるようになるか**: 既にある人物・キャラクターの映像の口を、後から作った TTS の音声に合わせる。型は promo・embed の数秒の見せ場
- **機械**: galleria WSL。入れるもの: LatentSync（main、1.5 の重みを使う。`setup_env.sh` が環境と重みを入れる）。費用 0、アカウント不要（HF から取得）。利用条件: コード Apache-2.0、1.5・1.6 の重みとも HF のカードで `openrail++`（利用制限つきの責任ある AI ライセンス。条文は未読）。GPU 要・VRAM の見込み 8GB（公式の記述、1.5）
- **成熟度**: 最終 push 2025-06-20、1.6 の後は更新なし（star 約 6,300、参考）。MuseTalk も最終 push 2025-09-26
- **最小の手順**（WSL。README のコマンドを元に、1.5 への切り替えは推測）:
  ```bash
  mkdir -p ~/video-tools-trial && cd ~/video-tools-trial
  git clone https://github.com/bytedance/LatentSync.git && cd LatentSync
  source setup_env.sh            # 環境と 1.6 の重み（README）
  # 16GB では 1.6 が入らない見込みなので、HF ByteDance/LatentSync-1.5 の latentsync_unet.pt に替え、U-Net の設定の resolution を 256 にする
  # （docs/changelog_v1.6.md:「the current code is compatible with both LatentSync 1.5 and 1.6. To switch between versions, you only need to load the corresponding checkpoint and modify the `resolution` parameter in the U-Net config file」。設定ファイルを stage2.yaml にするのは推測）
  python -m scripts.inference --unet_config_path configs/unet/stage2.yaml --inference_ckpt_path checkpoints/latentsync_unet.pt \
    --inference_steps 20 --guidance_scale 1.5 --enable_deepcache \
    --video_path in.mp4 --audio_path voice.wav --video_out_path out.mp4
  ```
  入力の候補: [[exp-qualia-h3-live2d-galleria]] の版 1（H3）の映像と、版 2 で差し替えた VOICEVOX の音声（ある場合）
- **動いたと言える確かめ方**: (1) `out.mp4` ができ、`ffprobe` で尺が音声とほぼ同じ。(2) `nvidia-smi` の最大使用量が 16GB 未満で終わる。(3) README の「sync confidence score」の評価スクリプトで入力と出力を比べる（数値は足切りにしか使わない。[[exp-galleria-tts-and-singing]]）。(4) **H3 の元の版（音声も映像も H3）と通常視聴で並べ、「元より魅力的か」を人が判定する**（[[exp-qualia-h3-live2d-galleria]] の順序）
- **所要の見込み（推測）**: 導入 1〜2 時間、数秒のクリップで試すのは 30 分
- **西尾が決めること**: 口の同期を試す価値があるか（経験は「口を直す道具を演技を作る道具の代わりに置かない」と書いている）。試すなら、LatentSync（直す）と音声駆動の生成（作る）のどちらから入るか

## Open Questions

- OpenRAIL++ の利用制限の条文（未読）と、1.5 に切り替えるときの設定ファイルの正確な名前
- アニメ調のキャラクターで LatentSync・MuseTalk の顔検出が通るか
- InfiniteTalk・LongCat-Video-Avatar 1.5・MagiHuman が RTX 5080 16GB で何秒の動画を作れるか（公式の数値なし。LongCat は INT8 あり）
- MagiHuman の日本語の発話の質（音声も一緒に生成するので、H3 と同じく日本語の記号が壊れる問題が出るか）
