---
type: source
summary: 公開の楽曲生成モデル（ACE-Step 1.5、YuE2、DiffRhythm／DiffRhythm 2、Stable Audio Open、MusicGen）の README・モデルカード・ライセンス条文を 2026-11-09 に読み、生成物の商用利用・VRAM・尺を並べたページ。ACE-Step 1.5 と DiffRhythm は重みが MIT／Apache 2.0、YuE2 は個人の作り手に限って収益化を許す CC BY-NC 4.0、Stable Audio Open は年商 100 万ドル未満なら登録して商用可、MusicGen は重みが CC BY-NC 4.0
video_types: [promo, talk, embed]
url: https://github.com/ace-step/ACE-Step-1.5
author: ACE Studio・StepFun（ACE-Step）、M-A-P（YuE2）、ASLP-lab・Xiaomi（DiffRhythm）、Stability AI（Stable Audio Open）、Meta（AudioCraft／MusicGen）
published: 2026（各 README の更新日は本文）
retrieved: 2026-11-09
sources:
  - https://github.com/ace-step/ACE-Step-1.5
  - https://huggingface.co/ACE-Step/Ace-Step1.5
  - https://github.com/ace-step/ACE-Step-1.5/blob/main/docs/en/GPU_COMPATIBILITY.md
  - https://github.com/ace-step/ACE-Step-1.5/blob/main/docs/en/CLI.md
  - https://github.com/multimodal-art-projection/YuE
  - https://github.com/multimodal-art-projection/YuE/blob/main/MODEL_LICENSE
  - https://github.com/multimodal-art-projection/YuE/blob/main/docs/hardware.md
  - https://github.com/ASLP-lab/DiffRhythm
  - https://github.com/ASLP-lab/DiffRhythm2
  - https://huggingface.co/stabilityai/stable-audio-open-1.0
  - https://huggingface.co/stabilityai/stable-audio-open-small
  - https://stability.ai/community-license-agreement
  - https://github.com/facebookresearch/audiocraft
  - https://github.com/facebookresearch/audiocraft/blob/main/model_cards/MUSICGEN_MODEL_CARD.md
---

# 公開の楽曲生成モデル: ACE-Step 1.5・YuE2・DiffRhythm ほか（2026-11 時点）

## 何の文献か

各プロジェクトの公式 README（GitHub）、Hugging Face のモデルカード、ライセンス本文。いずれも作り手自身の記述で、品質の比較（「Suno v4.5 と v5 の間」「Suno v5/v6 と競る」）は作り手の自己評価。第三者の聴取試験ではない。2026-11-09 時点の main ブランチ・モデルカードを読んだ。GitHub API は回数制限で使えず、リリース日はリリースページの HTML から取った。

## 書いてあること

### 一覧（2026-11-09 時点の公式の記述）

| モデル | 重みのライセンス | 生成物の商用 | 尺 | VRAM（公式） | 歌 | 最新 |
|---|---|---|---|---|---|---|
| ACE-Step 1.5（2B DiT＋LM） | MIT（モデルカード `license: mit`） | 「strictly use the generated music for commercial purposes」とモデルカードが書く | 10 秒〜10 分 | 4GB 未満で動く。16GB 帯は 2B＋LM 1.7B 推奨 | 歌詞付き、50 以上の言語 | リリース v0.1.8（2026-05-18）。XL（4B DiT）は 2026-04-02。commit は 1,410 |
| YuE2（3B） | CC BY-NC 4.0 ＋「individual creator permission」（2026-09-16） | 個人として使う作り手は収益化可。会社の商用は別契約 | 長さの上限は「測定中」 | 24GB（BF16）が標準。8GB で `low_vram` の報告あり | 歌詞付きの歌、インストも可 | v0.1.6。技術報告 2026-09-26、arXiv 2026-09-29 |
| DiffRhythm v1.2 | Apache 2.0（コードと DiT の重み） | ライセンス上は可 | base 1分35秒、full 4分45秒 | base は `--chunked` で最低 8GB | 歌詞付きの歌、インストも可 | v1.2 は 2025-05-09 |
| DiffRhythm 2 | Apache 2.0（コードと重み） | ライセンス上は可 | 未確認 | 未確認 | 歌 | 2025-10-30 公開 |
| Stable Audio Open 1.0 / Small | Stability AI Community License | 年商 100 万ドル未満なら登録して可 | 1.0 は最大 47 秒、Small は 11 秒 | 未記載（1.0 は 1B パラメータ、Small は 0.5B） | 「realistic vocals は作れない」 | — |
| MusicGen（AudioCraft） | コード MIT、重み CC BY-NC 4.0 | 不可（NC） | 学習は 30 秒の断片（モデルカード） | 未確認 | 無し | GitHub にリリース無し |

### ACE-Step 1.5

- README の abstract は「under 2 seconds per full song on an A100 and under 10 seconds on an RTX 3090」「runs locally with less than 4GB of VRAM」と書いている。品質は「between Suno v4.5 and Suno v5」と自己評価（README Features）
- 機能: 参照音声、カバー生成、Repaint（区間の作り直し）、トラック分離、Vocal2BGM（歌から伴奏）、BPM・調・拍子の指定、LRC（歌詞の時刻）の生成、LoRA 学習（「8 songs, 1 hour on 3090 (12GB VRAM)」）（README Features の表）
- 学習データ: モデルカードは「Licensed Data」「Royalty-Free / No-Copyright Data」「Synthetic Data（MIDI-to-Audio）」と書く。内訳の数や第三者の監査は書かれていない
- GPU の段（GPU_COMPATIBILITY.md）: 12〜16GB は Tier 5（LM 1.7B 推奨、最大の長さは LM あり 8 分／無し 10 分、XL は「marginal」）、16〜20GB は Tier 6a（XL は CPU offload で可）。XL の重みは約 9GB、2B は約 4.7GB
- 免責（README の License & Disclaimer）: 様式の近さによる意図しない侵害の恐れを挙げ、生成物の独自性の確認、AI の関与の開示、保護された様式を借りる時の許諾を勧めている
- 入口: Gradio UI（`uv run acestep`、http://localhost:7860）、REST API（`uv run acestep-api`、8001）、対話式 CLI（`python cli.py`、設定を `.toml` に保存して `--config` で再実行）、Python API、VST3 プラグイン。Windows 用の portable package もある

### YuE2

- 2026-09 に YuE（v1）から YuE2 に置き換わった（v1 は `YuE-v1` ブランチに保存）。歌詞とスタイルから「melody-and-chord plan」（ABC 記法の楽譜）を先に書き、それを音にする。楽譜を人や agent が編集して作り直せる（README「White-box music generation」）
- ライセンス（README の License 表と MODEL_LICENSE）: 「Personal users, content creators, and musicians | Free to use YuE2 and monetize generated outputs, with no fees or royalties」。条件は「acting in an individual capacity」。「The individual creator permission does not authorize commercial use of the model weights by companies」。クレジットは任意（#YuE2 を勧める）
- ハード（docs/hardware.md）: 標準は「Linux · Python 3.12 · NVIDIA GPU with BF16 support and 24 GB VRAM」。`--low-vram --budget 8` の低メモリ動作は opt-in で、報告は「Windows, RTX 5060 Laptop 8 GB」で 2 曲が完走、など。「Stable length limits on 6/8/12 GB devices remain to be measured」
- 出力は 48 kHz ステレオの flac。出力フォルダに楽譜・トークン・設定・モデル名が残る（README Quick start）
- WildSongBench（作り手が作った 192 プロンプトの自動評価、2026-09-12）で最高と書いている

### DiffRhythm / DiffRhythm 2

- 拡散で全曲を一度に作る。v1.2（2025-05-09）、full 版は 4分45秒、base は 1分35秒（README のモデル表）
- 「DiffRhythm-base requires a minimum of 8G of VRAM. To meet the 8G VRAM requirement, use the `--chunked` argument」（README）
- 免責は「users must implement verification mechanisms to confirm musical originality, disclose AI involvement」と書く（README）
- DiffRhythm 2 は 2025-10-30 にコードと重みを Apache 2.0 で公開（DiffRhythm2 README）。以後の更新は README に無い

### Stable Audio Open

- 1.0 は「variable-length (up to 47s) stereo audio at 44.1kHz」、Small は「up to 11s」（モデルカード）。1.0 は HF でゲート付き（取得にログインと同意が要る。CyEC2 から raw は取れず、HTML のモデルカードを読んだ）
- 学習データは Freesound 472,618 件と FMA 13,874 件、CC0・CC BY・CC Sampling+ のみ。Audible Magic で著作権のある音楽を除いた、と書く（モデルカード Training dataset）。Small の DiT は Freesound だけで学習
- 限界: 「not able to generate realistic vocals」「better at generating sound effects and field recordings than music」（モデルカード Limitations）
- Community License（stability.ai）: 研究・非商用は無料。商用は「You must register with Stability AI」、本人と関連会社の年商が 100 万ドルを超えたらライセンスは終了し、Enterprise を申請。配布する時は「Powered by Stability AI」の表示。「You own any outputs generated from the Models」（IV.c.iii）。出力を基盤モデルの学習・改良に使うことは禁止（IV.b）

### MusicGen（AudioCraft）

- モデルカード: 「Code is released under MIT, model weights are released under CC-BY-NC 4.0」。学習データは Meta Music Initiative Sound Collection・Shutterstock・Pond5 のライセンス済み音源
- GitHub の audiocraft にはリリースが無い（2026-11-09、リリースページ「There aren't any releases here」）

## この wiki への含意

- **galleria の 2026-09-04 の整理「楽曲は実用的なローカルモデルが無く外部 platform に頼る」**（[[exp-galleria-tts-and-singing]] の楽曲の節）は、少なくとも条件の面では古い。ACE-Step 1.5（技術報告 arXiv 2602.00744 で 2026-02、MIT、商用可と明記、16GB で LM 1.7B 推奨の段）は 2026-09 の時点で既にあった。2026-09 の整理が品質で外したのか、見落としたのかは経験ページから分からない。YuE2 は 2026-09 の公開（README の GitHub Trending 1 位の日付が 2026-09-14、creator permission が 2026-09-16）で、整理とほぼ同時かその後
- **「台詞は local、楽曲は hosted」の非対称**（同）は、ACE-Step 1.5 で崩せる可能性がある。素材台帳の管理（規約の版、生成の設定）は手元で閉じる
- **numpy で合成する BGM**（[[exp-html-capture-pipeline]]、[[exp-polis-magi-op]]）との違い: numpy 合成は拍と場面の時刻表を同じ格子に乗せられ、権利の申告対象が無い。生成モデルは音色と曲らしさで勝つが、拍の位置は出来上がった音から測り直す必要がある（ACE-Step は BPM・拍子を指定でき、LRC で歌詞の時刻を出す。拍の格子に正確に乗るかは未検証）
- 型ごと: promo は曲が主導するので ACE-Step／YuE2 の歌付きが効く候補。talk・embed は Moreno & Mayer の向き（[[web-moreno-mayer-2000-coherence-sounds]]）から、歌の無いインストを声より 10 LU 以上下げる（[[web-torcoli-2019-background-ducking]]）のが無難。embed は流しっぱなしなので、ループできる短いインストか、尺ぴったりの曲が要る
- 既存曲の替え歌（[[exp-sutra-songs-on-music]] の残テ）の伴奏を「カバー生成」で作るのは、元の楽曲の権利（作曲）を消さない。ACE-Step・YuE2 のカバー機能は権利の問題を解決しない（README の免責も許諾を求めている）
- Stable Audio Open は歌も曲らしさも弱く、効果音・環境音の側（[[web-means-sound-elevenlabs-sfx-mmaudio-foley]]）

## 着手の仕方（未検証。galleria で確かめる）

- **何が表現できるようになるか**: 尺と BPM を指定したオリジナルの BGM・歌付きの曲を、手元の GPU で、外部サービスの規約に縛られず作る。効く型: promo（主）、talk・embed（インスト）
- **機械**: galleria WSL（RTX 5080 16GB）。GPU 要・VRAM の見込み 4.7GB（2B DiT の重み）＋LM 1.7B（根拠: 公式の GPU_COMPATIBILITY.md の Tier 5〜6a）。費用 0、アカウント不要（モデルは Hugging Face から自動取得。ACE-Step 1.5 はゲート無しのモデルカード）
- **利用条件の要点**: MIT。モデルカードが商用可と明記。生成物の独自性の確認と AI 関与の開示を README が勧める
- **成熟度**: 1,410 commit、star 14.5k、最新リリース v0.1.8（2026-05-18）、XL は 2026-04-02。docs に日本語の INSTALL・Tutorial がある
- **最小の手順（WSL、README の Quick Start より）**:
  ```bash
  mkdir -p ~/video-tools-trial && cd ~/video-tools-trial
  git clone https://github.com/ACE-Step/ACE-Step-1.5.git
  cd ACE-Step-1.5
  uv sync                      # Python 3.11-3.12 が要る（README Requirements）
  uv run acestep               # Gradio。初回にモデルを自動取得。http://localhost:7860
  # GUI を使わない場合（推測: CLI.md の wizard を一度回して toml を作り、以後それで回す）
  uv run python cli.py --configure --config bgm60.toml
  uv run python cli.py --config bgm60.toml
  ```
  RTX 5080（Blackwell）で `uv sync` が入れる PyTorch の CUDA 版が合うかは README に書かれていない（推測で要確認。合わなければ GPU_TROUBLESHOOTING.md を読む）
- **動いたと言える確かめ方**: (1) `nvidia-smi` で生成中に GPU メモリが使われている、(2) 出力フォルダに wav/flac ができ、`ffprobe` で長さが指定（例 60 秒）と ±1 秒以内、(3) `ffmpeg -i out.wav -af ebur128 -f null -` で無音でない（Integrated が −40 LUFS より大きい）、(4) インスト指定で歌が入っていないことを耳で確かめる（機械では判定しない）
- **所要の見込み（推測）**: 入れて 1 曲出すまで 1〜2 時間（モデルの取得を含む）。1 曲の生成は RTX 3090 で 10 秒未満（公式）なので、5080 でも数十秒以内の見込み
- YuE2 を試すなら: 標準は 24GB なので 16GB では `--low-vram` が要る（公式）。「個人として」の条件は、会社の仕事の動画では満たさない可能性があり、西尾が決める

## Open Questions

- ACE-Step 1.5 の「Licensed Data」の中身と量は公開されていない。生成物が既存曲に似る確率は分からない。Content ID に誤って当たるかは試していない
- YuE2 の「individual capacity」と、会社員の西尾が業務で作る動画の関係。個人の YouTube に上げる私的な作品なら当たる、業務の発信物は当たらない、と読めるが、条文は「Companies wishing to use the model weights commercially」とだけ書く
- ACE-Step の BPM 指定で、出力の拍が 120BPM の格子（[[exp-html-capture-pipeline]] の流儀）にどれだけ正確に乗るか（拍の検出で測る。未検証）
- 日本語の歌詞の発音の質は、どのモデルも作り手の記述が無いか自己評価のみ
- Stable Audio Open の「Commercial Purpose」は「primarily intended for commercial advantage」。収益化した YouTube の動画に使うことが登録の要る商用に当たるかは条文から一意に読めない
