---
type: source
summary: galleria（RTX 5080 16GB）でのローカル動画生成モデルの実測。Wan2.2 TI2V-5B は瞬き程度しか動かず、Wan2.2 I2V-A14B fp8 は 832x480・49 frames を 30〜35 秒、peak 15.8GB で回せた。両端固定（FLF2V）は終点を正確に再現するので、動画の良し悪しは keyframe 対の質に移る
video_types: [any]
sources:
  - galleria-wiki wiki/local-video-generation-on-rtx-5080-16gb.md
  - galleria-wiki wiki/first-last-frame-video-interpolation.md
  - galleria-wiki wiki/comfyui-flux2-character-keyframe-pair.md
  - galleria-wiki wiki/qualia-san-explainer-video-pilot.md（「4秒motion micro比較の結果」節）
  - galleria-wiki wiki/local-scene-studio.md（「期待値はkeyframeまで」「上位の役割は静止画探索へ移す」節）
  - galleria-wiki wiki/hosted-video-generation-apis.md、wiki/text-encoder-residency.md、wiki/pose-sheet-driven-video.md
  - galleria-wiki の raw（ページ内の出典表記）: 2026-08-12-qualia-san-motion-micro-comparison.md、2026-08-31-wan22-i2v-a14b-adoption.md、2026-08-31-wan22-i2v-a14b-first-smoke-test.md、2026-08-31-wan22-flf2v-first-run.md、2026-08-31-wan-first-last-frame-node-inspection.md、2026-08-31-first-last-frame-video-practice-survey.md、2026-09-04-ai-video-generation-survey.md、2026-09-23-disk-free-1p5gb-cleanup.md、2026-09-26-qualia-wan22-dance-loop-closeout.md
---

# galleria でのローカル動画生成（2026-08〜10）

機械: galleria（Windows、RTX 5080 16GB、物理 16,303 MiB）。ComfyUI portable から使う。動画は「静止画で keeper を選んでから、動きが要るものだけ動画化する」下流の工程として扱うようになった（下の「判断の変遷」）。

## 実測の一覧

| モデル | 条件 | 時間 | peak VRAM | 動きの所見 |
|---|---|---|---|---|
| Wan2.2 TI2V-5B | 640 x 640、97 frames、24fps、20 steps、CFG 5、I2V（人物部分だけ、瞬きを要求）、2026-08-12 | runner 全体 70.074 秒 | 15,675 MiB（baseline 1,901） | 瞬きより、顔の位置・scale・輪郭・視線のゆっくりした描き直し。人間の通常再生で「どこが変わったのか分からない」 |
| Wan2.2 TI2V-5B | 640 x 640、49 frames、24fps、20 steps、CFG 5、`uni_pc`/`simple`、shift 8、単体人物のダンス、2026-08-12 | queue 38.2 秒、runner 39.315 秒 | 15,493 MiB（直前の画像モデルが載ったまま。差分は比較に使わない） | 腕の上げ下げと表情の維持を AI の目視確認で報告。人間の評価・採否は記録なし |
| Wan2.2 I2V-A14B fp8_scaled | 832 x 480、49 frames、batch 1、lightx2v 4 steps（high 2＋low 2）、CFG 1.0、euler/simple、shift 8.0、2026-08-31 | cold 34.8 秒（server 実行時間）、warm 30.2 秒 | **15,807 / 16,303 MiB（96.96%）** | 頭が持ち上がり、上体が起き、前肢が机から離れ、カメラが寄る。被写体の同一性と背景の位置関係は保たれた。出力は 16fps・3.06 秒・h264 |
| 同上で FLF2V（両端固定） | 同条件、`WanFirstLastFrameToVideo` | wall 33.1〜36.2 秒 | 15,699 MiB | 終点は指定どおりに再現（下） |

A14B と 5B の比較は統制された A/B ではない（開始画像も prompt も別）。A14B の数字は lightx2v 4 steps のもので、LoRA なし・full steps、720p、81 frames は未測定。

### A14B を 16GB に収めている仕組み

fp8 の本体は 14.3GB x 2（high noise と low noise）だが、同時には載せず片方ずつ載せ替える。切替で約 5〜7 秒かかり、VRAM が 15.5GB → 11.9GB → 15.7GB と谷を作る。**余裕は約 500 MiB しかなく、他の GPU 利用と同時には走らせられない**。GGUF Q5 への退避は不要だった。取得物は `Comfy-Org/Wan_2.2_ComfyUI_Repackaged` の 5 file、計 29.15 GiB（text encoder `umt5_xxl_fp8_e4m3fn_scaled` 6.27 GiB は共用で別）。

## 両端固定（FLF2V）で分かったこと

- **custom node は要らず、コストは I2V と同じ。** 組込みの `WanFirstLastFrameToVideo` は `WanImageToVideo` に `end_image` が増えただけなので、API graph の 1 node 差し替えで済む。
- **終点はそのまま再現される。** 最終 frame と end image の差（grayscale 平均絶対差、0-255）は 4.28〜4.79 で、VAE 往復と h264 の床（先頭 frame と start image の差 3.91〜4.38）とほぼ同じ。
- だから**失敗の位置が上流へ移る**: 5B は動かない、14B I2V はどこへ動くかをモデルが発明する、14B FLF2V は指定した終点へ正確に行くので、動画の良し悪しは keyframe 対の質そのものになる。実測では、FLUX.2 で作った終了画像の被写体が小さく引いた構図だったため、832 x 480 への center crop で構図がずれ、**最終 frame で耳の上端が見切れた**。
- 開始・終了画像の対は galleria-wiki の comfyui-flux2-character-keyframe-pair.md の方法で作る。FLUX.2 Klein の `ReferenceLatent` には strength 入力が無く、開始画像を参照にすると終了画像での変更まで消えるので、参照あり／なしの予測を重み付きで混ぜて調整した（`s = 0.75` の 1 点のみ）。

### MiniMax H3（FL2VA）で動きの量を測った（2026-09-18）

| keyframe 対の作り方 | 2 枚の距離 | 生成 clip の動き（中央値） | 起きたこと |
|---|---:|---:|---|
| A と B を別々に生成 | 21.3 | 0.76 | 静止 → 中央の frame で切り替わり → 静止 |
| B を A からの i2i で生成 | 8.03 | 1.81 | 切り替わりが消え、連続して動く |
| 同じ 2 枚で frame 数 124 | 8.03 | 0.55 | 同じ移動が薄く伸びるだけ |
| 同じ 2 枚で frame 数 22 | 8.03 | 0.38 | 短いと動かない |

- 出るのは A から B への 1 回の移動だけで、1 frame あたりの動きは「2 枚の距離 ÷ frame 数」。**別々に生成した 2 枚は同じ場面の 2 瞬間ではなく違う 2 枚の絵**になり、モデルは補間せず中央で切り替える。
- 手当ては B を A からの i2i で作ること。ただし i2i は B を A に引き戻すので、**寄せると動かない、離すと cut になる**。frame 数は動きのつまみではない。
- **平均は嘘をつく。** 「静止＋1 回の切り替わり」は frame 間の平均では動いて見える（別々生成の全画面平均 2.139 は、連続して動く参照 clip の 1.930 より大きい）。中央値は 0.59。cut の有無は中央値と最大値で見る。
- H3 の `length` は 24fps で `17k+5` の grid に載るが、学習レンジは約 124〜362 frames。grid に載ることとレンジに入ることは別条件。

## 判断の変遷

1. 2026-08-11 の調査時点の順位は Wan2.2 TI2V-5B → HunyuanVideo 1.5 → LTX-2.3。
2. 2026-08-12 の解説動画では、情報スライド全体に I2V をかけず、人物部分だけを生成して固定のスライドに後合成する方法が成功した（人物部分の外の画素は全 frame で固定）。ただし動き自体は採用されず、完全静止が既定になった（[[exp-qualia-video]]）。
3. 2026-08-31: 5B では具体的な開始画像と具体的な pose・接触・camera の prompt を与えても二身体の行為が出ず、時間変化は瞬き程度だった（人間の報告）。「prompt、planner、workflow の改良で回復させようとしない」と決め、14B（A14B fp8）へ移った。抽象的な指示を 27B の planner で構造化して動画まで直列に作る Scene Studio も、価値は静止画 keyframe までとした。
4. 2026-09-08 以降: 動画モデルは題材探しの入口ではない。rough な場面・テーマから静止画候補を広く作り、人間が keeper を選び、動きに明確な役割があるものだけを小さな A/B で動画化する（所有者の制作評価による方向転換）。
5. 2026-09-23: ディスク枯渇時の所有者判断で 5B（本体・`wan2.2_vae`・LoRA、11.2GB）を削除。A14B は `wan_2.1_vae` を使うので影響なし。

## galleria-wiki が推奨する workflow（設計）

1. 静止画候補を batch で作る。2. 人間が keeper を選び、局所修正する。静止画で完成する作品はそこで終わり。3. 動きに役割がある keeper だけ、行為に合うモデルを小さな A/B で選ぶ。4. 走らせる前に LLM と画像モデルをアンロードし、480p の短尺で動き・同一性・破綻・時間・peak VRAM を比べる。5. 通過した cut だけを高解像度化し、補間・upscale・音声・ffmpeg encode へ進める。長い動画を一度に狙わず、短い shot を編集でつなぐ。

## 詰まったこと・落とし穴

- **ComfyUI 同梱の workflow テンプレートは subgraph 入りの UI JSON で、`/prompt` へそのまま POST できない。** API で回すなら `/object_info/<node>` から schema を取って API graph を組む。ComfyUI 0.33.1 では `SaveWebM` が無く、`SaveVideo` の `codec` は `COMFY_DYNAMICCOMBO_V3`（`auto`/`auto` で通る）。`CLIPLoader` の `type` は `wan`。
- **LoRA はモデルの大きさを跨げない。** 5B と 14B の LoRA は互換ではない。`patches attached` が出ても意図した意味を持つとは限らない。safetensors の header で hidden dim とブロック数を読めば判別できる（5B は 3072・30 層、14B は 5120・40 層）。
- lightx2v の high 用と low 用の 2 file はバイト数が同じで SHA-256 だけ違う。容量では取り違えを検出できない。
- A14B の license（apache-2.0）は取得**後**に repository metadata で確認したもので、upstream の model card は未読。公開・商用の前に確かめ直すとされている。
- Ollama が GPU を 14GB 掴んでいると大きいモデルは載らない。Claude Code の auto mode は Claude からの `ollama stop` を「稼働中の処理への干渉」として拒否した（所有者が外した）。（irodori-tts-v4-large.md の記録だが動画でも同じ）
- 新しい prompt の 1 本目だけ遅いのは、text encoder と生成モデルが同じ GPU でスワップしている時間であることが多い。A14B fp8 の cold 37.2 秒 / warm 30.2 秒（POST から history 確定まで）はその形ではない。（text-encoder-residency.md）
- 5B の 49 frames をダンスの loop にするのに `0..48 + 47..1` の ping-pong（96 frames、4.0 秒）にした。逆再生を含むので一方向の本当の周期ではない。成果物は `C:/Users/nishi/claude-win/output/qualia-dance/`。5B を削除したので再実行には再導入が要る。

## 試していないもの（外部の情報として記録されているだけ）

- HunyuanVideo 1.5（8.3B、公式最低 VRAM は offload 込み 14GB）と LTX-2.3（映像と同期音声を一つのモデルで出す。Windows local 最低線が VRAM 16GB・RAM 32GB・空き 160GB）は、目的がはっきりしてから試すとして入れていない。
- Wan は 2.2 が実質最後の開放世代で、2.6 と 3.0 はクローズド API 専用、2.7 を「Apache-2.0 で公開」と書くブログは公式未確認、と整理した。
- 外部の hosted モデル（Kling 3.0 約 $0.029/s、Seedance 1.5 Pro $0.0247/s〜、Veo 3.1 は 48kHz の同期音声と台詞）は二次情報の秒単価で、galleria からの実行は無い。「ローカルで静止画候補を大量に出して人が選び、採用 cut だけを hosted で撮り直す」組み合わせが現実的だとされた（設計）。（hosted-video-generation-apis.md）
- 番号付き 16 ポーズの振付シート 1 枚を参照に渡し、0.5 秒ごとの割り当てを文章で書いて MiniMax H3 で 8 秒のダンスを出した外部の作例がある。シートの枠・番号・分割画面を出力に出さないよう明示的に禁止するのが要点。A14B でそのまま試せる形だが未実測。（pose-sheet-driven-video.md）

## Open Questions

- A14B で複雑な行為・複数の被写体がどこまで出るか（単体被写体の smoke test まで）。
- 720p・81 frames が 500 MiB の余裕で収まるか。
- 解説動画（talk）で、生成した動きが役に立つ場面はあるのか。2026-08-12 の比較では完全静止に負けた。

## Updates

### 2026-11-09 第 2 回サーベイ: 二次情報の数字が古い

- ホスト型の価格: Seedance 1.5 Pro は 2026-11-11 に退役、Veo 3.1 は Gemini API の Preview が 2026-10-22 に停止（後継は Gemini Omni 1.2 Flash）、Kling は公式（Runway 経由）で 720p 音声ありの Standard が $0.13/s（[[web-genvid-seedance]]、[[web-genvid-gemini-omni-veo]]、[[web-genvid-sora-kling-runway]]）
- VRAM: 「LTX-2.3 は Windows local で 16GB が最低線」は二次情報で、公式の LTX-2.5 は最低 32GB。Wan2.2 A14B の公式の要件は 80GB だが、galleria では fp8 と lightx2v 4 steps で 15.8GB に収まった（実測）。公式で 16GB に収まるのは HunyuanVideo 1.5（14GB、オフロード込み）（[[web-genvid2-wan-ltx-hunyuanvideo-minimax-h3]]）
- 「Wan は 2.2 が最後の公開世代」は 2026-11 時点でも公式と一致。2.2 系の派生（Animate-2-14B、Wan-Dancer-14B）が 2026-07〜08 に Apache-2.0 で出ている（同）


### 2026-11-09 ホスト型の Grok Imagine の image-to-video を初めて使った

- tsugigami の広告動画で、galleria から X Premium+ の枠の Grok Imagine（grok-imagine-image-2.0 で開始画像、grok-imagine-video-1.5 で i2v）を API 直叩きで 12 本。816×1104・24fps・約 6 秒で、1 本約 28 秒。人物の顔・手と、書く → 顔を上げて微笑む動きは、ローカルの 5B・A14B の実測（上）より指示に近かった（西尾が笑顔を採用。比較は統制されていない）
- 「画面は真っ白のまま」と頼んでも書く動きに合わせて薄い線を描いた。その線を Pencil の真下のインクとして使った（[[exp-tsugigami-promo]]）
