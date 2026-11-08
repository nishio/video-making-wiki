---
type: source
summary: 重みが公開されている動画生成モデル 4 系統（Alibaba Wan、Lightricks LTX-2.x、Tencent HunyuanVideo 1.5、MiniMax H3）の 2026-11-09 時点の公式 README・モデルカード・ライセンス本文・価格表から、尺・解像度・音声・必要な VRAM・API の秒単価・ライセンス（商用の条件・地域・出力の権利・開示）を並べたもの。作品の promo を作る手段の比較に要る範囲だけ
video_types: [promo, any]
url: https://huggingface.co/MiniMaxAI/MiniMax-H3
author: MiniMax、Alibaba（Wan チーム）、Lightricks、Tencent Hunyuan（各公式）、Comfy Org（H3 のローカル実行の記事）
published: 2025-07-28（Wan2.2）／2025-11-20（HunyuanVideo 1.5）／2026-07-23（LTX-2.5 の HF リポジトリ作成）／2026-08-02（H3 のライセンス日）
retrieved: 2026-11-09
sources:
  - https://huggingface.co/MiniMaxAI/MiniMax-H3 （README、最終更新 2026-08-13）
  - https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/LICENSE （MiniMax H3 Community License Agreement、2026-08-02）
  - https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/docs/QA-about-License.md
  - https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/docs/VIDEO_PROMPT_WRITING_GUIDE_base_en.md
  - https://platform.minimax.io/docs/guides/pricing
  - https://blog.comfy.org/p/minimax-h3-day-0-support-in-comfyui （2026-08-03）
  - https://github.com/Wan-Video/Wan2.2 （README と LICENSE.txt、最終 commit 2026-09-21）
  - https://huggingface.co/Wan-AI （2026-07〜08 の Wan2.2-Animate-2、Wan-Dancer）
  - https://www.alibabacloud.com/help/en/model-studio/wan2-7-t2v （最終更新 2026-10-11）
  - https://github.com/Lightricks/LTX-2 （README、LICENSE-2、LICENSE-2_x）
  - https://huggingface.co/Lightricks/LTX-2.3 、https://huggingface.co/Lightricks/LTX-2.5 （モデルカード）
  - https://docs.ltx.io/pricing.md 、https://docs.ltx.io/models/ltx-2-5.md 、https://docs.ltx.io/open-source-model/getting-started/system-requirements.md
  - https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5 （README と LICENSE）
---

# 重みが公開されている動画生成モデル 4 系統の仕様とライセンス（2026-11-09 時点）

## 何の文献か

各社の公式の一次資料（GitHub の README、Hugging Face のモデルカード、ライセンス本文、公式の価格表）。すべて **2026-11-09 時点の公式ページによる**。ライセンスの条文は原文を読んだが、法律の解釈はしていない。宣伝の文（「品質の低下なし」など）は各社の主張で、この wiki で確かめたものではない。

ByteDance・Google・OpenAI・Kuaishou・Runway は別の担当が書くので、ここでは扱わない。

## 書いてあること

### 一覧（公式ページに書いてあること）

| | MiniMax H3 | Wan（Alibaba） | LTX-2.x（Lightricks） | HunyuanVideo 1.5（Tencent） |
|---|---|---|---|---|
| 重みの公開 | 2026-08 公開（FL2VA と Ref2VA の 2 checkpoint）。前処理の H3-Context-IR と 2K 化の H3-Regenerate-2K は**非公開で API のみ** | **重みは Wan2.2（2025-07-28）まで**。2026-07〜08 に Wan2.2 系の派生（Animate-2-14B、Wan-Dancer-14B）が Apache-2.0 で出た。Wan2.7 は Alibaba Cloud Model Studio の API で提供 | LTX-2.3、LTX-2.5（2026-07 以降。HF は同意が要る gated） | 2025-11-20 公開。2026 年の新しい版は公式の org に見当たらない |
| 尺 | 4〜15 秒（README） | Wan2.2 は短尺（README は TI2V-5B について「5 秒の 720P を単一の消費者向け GPU で 9 分未満」と書く） | API の LTX-2.5 fast は 6〜20 秒（720p/1080p、24/25fps）、pro は 6〜10 秒。LTX-2.5 はプロンプトから尺を決める機能がある | 既定 121 frames（README の引数表。fps の記載は確かめていない）。README は「10 秒の 720p」の速度にも触れる |
| 解像度 | 既定は短辺 768。2K は非公開の H3-Regenerate-2K（API）で | Wan2.2 は 480P/720P。Wan2.7 の API は 720P/1080P | API で 720p〜4K（3840x2160） | 480p/720p を生成し、超解像で 1080p |
| 音声 | **映像と同時に生成**（32kHz ステレオ、台詞は 11 言語を「安定」と書く。日本語を含む） | Wan2.2 本体は無音。音声から動かす S2V-14B が別にある | **映像と同時に生成**（音声 VAE を持つ） | 同時生成の記載なし（README の機能一覧に無い） |
| 画面の文字 | プロンプトガイドに「画面に見える文字は英語の二重引用符に入れ、原文のまま」と書く（4.5 On-Screen Text） | 記載なし | LTX-2.5 は新しいデコーダで「画面の文字」が鮮明になったと書く | 記載なし |
| 参照入力 | Ref2VA: 画像 ≤9、動画 ≤3 本（合計 ≤15 秒）、音声 ≤3 本。FL2VA: 先頭・末尾フレーム | I2V、両端固定（ComfyUI の `WanFirstLastFrameToVideo`） | 画像を任意のフレーム位置に、音声から動画、末尾フレーム | I2V |
| VRAM（公式） | README の配備例は SGLang で **GPU 4 枚**。Comfy Org は「量子化で総メモリ 123.6GB → 42.5GB、動的オフロードで RTX 3060 級でも動く」と書く（2026-08-03） | README: T2V/I2V-A14B は「80GB 以上の GPU で動く」、TI2V-5B は「24GB 以上（RTX 4090 など）」 | 公式の最低要件: **VRAM 32GB 以上**、RAM 32GB、空き 100GB。推奨 A100 80GB / H100 | README: **最低 14GB（オフロード有効時）**。README が紹介する外部の Wan2GP は「6GB から」と書く |
| API の秒単価（出力 1 秒） | H3（2K）$0.13、H3（768P）$0.08、Highspeed 768P $0.06、Lite 480P $0.025（MiniMax 公式価格表） | wan2.7 の Singapore 地域で 720P $0.10、1080P $0.15（Model Studio、2026-10-11 更新） | ltx-2-3-fast 720p $0.03〜4K $0.24、ltx-2-5-pro 720p $0.12〜4K $0.39（LTX 公式 docs） | 公式 API の価格は見つけていない |

### ライセンス（原文の要点）

- **Wan2.2**: Apache 2.0。README は「生成した内容についての権利を主張しない」と書き、違法・有害な内容の共有を禁じる文を添える。
- **LTX-2.x Community License**（LTX-2.5 に適用。License date 2026-08-11、2026-10-29 改定）: 誰でも使えるが、**年間売上 1,000 万ドル以上の事業体（"Commercial Entities"）は、非商用の試験・研究を除き有料の Commercial Use Agreement が要る**（2.1 節）。売上は子会社・関連会社を含めて数えるとモデルカードに書く。出力について「Licensor は出力に権利を主張しない」（5 節）。ファインチューンした重みを他社に渡すときに有料の許諾が要る場合がある。LTX-2.3 は別文書の LTX-2 Community License（本文は未読、モデルカードの表記による）。
- **MiniMax H3 Community License**（2026-08-02）:
  - 適用地域は「全世界から EU・英国・韓国・**米国**を除く」。除外地域では重みも**出力**も使えない（V.4、Exhibit A（Acceptable Use Policy）の 1）。除外地域の組織は申請で個別に許諾を受けられる（License Q&A）。API は全世界で使える（Q&A）
  - 年間売上 2,000 万ドル超の商用製品・サービスは事前の書面許可が要る（IV.1）。H3 を使う商用製品の UI に「MiniMax H3」を目立つように表示する（IV.2）
  - **公開の場に出す内容は「機械生成であることを明確かつ目立つように開示せずに」流してはならない**（Exhibit A（Acceptable Use Policy）の 12）
  - 出力の権利: 「MiniMax は出力に権利を主張しない。出力とその後の利用の責任は利用者にある」（VI.4）。出力を他の AI モデルの改良に使うことは禁止（V.3）
- **Tencent Hunyuan Community License**（HunyuanVideo 1.5、2025-11-21）: 適用地域は EU・英国・韓国を除く全世界。リリース日の前月の月間利用者が 1 億人を超える事業者は別途許諾が要る。出力に権利を主張しない。出力を他の AI モデルの改良に使うことは禁止。

### H3 の公式の作例が文字をモデルに描かせていること

Comfy Org の記事（2026-08-03）の作例プロンプトには、製品広告として「"STAY" then "HYDRATED"」と巨大な文字を拍に合わせてモデルに描かせ、最後に「"STAY COMFY"」を水面に映すものや、マウスの「Editorial tech product film」がある。**ベンダーは製品の広告と画面の文字をモデルの中で作る使い方を見せている**。出来は確かめていない（動画は取得しない決まり）。

## この wiki への含意

- **promo（作品の紹介）**: 西尾の作品（ソフトウェア・研究・本）を紹介する promo で、丸ごと生成を使うなら費用は小さい。秒単価から計算すると、15 秒の H3 768P は API で $1.2、LTX-2.3 fast 720p の 10 秒は $0.3（選び直しの回数を掛ける。下の [[web-genvid2-niq-system1-ai-generated-ads]] の Coca-Cola は 7 万 clip から組んだと報じられている）。費用より、[[web-genvid2-t2vtextbench-design-video-eval]] の「画面の文字・レイアウトを守れない」が先に効く。作品の実画面（UI・図・数値）は生成でなく実際の画面の収録かコードで描くことになる
- **ローカルで回せるか（galleria の RTX 5080 16GB）**: 公式の数字で 16GB に収まると言えるのは HunyuanVideo 1.5（14GB、オフロード込み）だけ。Wan2.2 A14B の公式は 80GB だが、[[exp-galleria-local-video-generation]] では fp8・lightx2v 4 steps で 832x480・49 frames を peak 15,807 MiB で回した。**公式の最低要件と、量子化・蒸留したコミュニティ版での実測は 5 倍ほど違う**。LTX-2.5 の公式最低 32GB も同じ関係かもしれない（未測定）
- **H3 は galleria で一体生成した記録がある**（[[exp-qualia-h3-live2d-galleria]]、component 39.55 GiB）。公式 README の配備例（GPU 4 枚）とは違い、Comfy Org の量子化・オフロード版で動かしたと読める（どの版かは exp に書かれていない）
- **H3 で公開する動画は「機械生成」の開示が要る**（ライセンスの Exhibit A の 12）。[[exp-qualia-h3-live2d-galleria]] の「公開制作に使うなら、品質評価より前に現行の公式規約を一次情報で確かめる（第 0 の関門）」の答えの一部はこれ。日本は H3 と Hunyuan の除外地域に入っていない。一方、米国が H3 の重みの除外地域に入っているので、米国の視聴者に向けた配信が「除外地域での表示」に当たるかは条文から読み切れない
- grasp-nishio の「動画ではモデル名を明示する」は、H3 の UI 表示義務（商用製品の場合）・開示義務と向きが同じ
- **Wan は 2.2 が実質最後の公開世代**という [[exp-galleria-local-video-generation]] の整理は、2026-11-09 時点でも公式の org と一致する（2.2 系の派生が 2026-07〜08 に出たことが追加）。Wan2.7 を Apache-2.0 とする記事は公式で確かめられない
- 文字: H3 のプロンプトガイドと Comfy の作例は「文字をモデルに描かせる」方向で、[[exp-qualia-video]]・[[exp-local-scene-studio]] の「生成モデルに文字を描かせず後で合成する」と逆。日本語の文字をどこまで正しく描くかを測った資料は見つけていない

## Open Questions

- LTX-2.x の年間売上 1,000 万ドルの線と、H3 の 2,000 万ドルの線に、西尾の所属先での制作が当たるか。個人の制作と組織の制作のどちらとして扱うかで変わる（この wiki には所属先の情報を書かないので、使う前に本人が確かめる）
- H3 の「機械生成の開示」は、動画内の表示か、投稿文での表示で足りるか。条文は「明確かつ目立つように」としか書いていない
- 16GB で LTX-2.5（公式最低 32GB）が回るか。[[exp-galleria-local-video-generation]] の記録では LTX-2.3 は「Windows local 最低線が VRAM 16GB」とされていたが、出典は二次情報
- H3 の日本語の画面文字・日本語の台詞の正確さ。[[exp-qualia-h3-live2d-galleria]] では日本語の台詞の一部が壊れた
- HunyuanVideo 1.5 の公式 API の価格（Tencent Cloud）は確かめていない
