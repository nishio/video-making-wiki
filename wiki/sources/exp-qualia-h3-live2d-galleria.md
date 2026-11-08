---
type: source
summary: クオリアさんの数秒の台詞動画を、MiniMax H3 の音声・映像一体生成、VOICEVOX への音声差し替え、口だけの後合成、小規模な Live2D 化と段階的に作り比べた galleria の実験（2026-08-14〜17）。検査できる正しさは上がったが、人間の評価では最初の H3 版が一番なめらかだった
video_types: [promo, embed]
sources:
  - galleria-wiki wiki/qualia-san-h3-live2d-video-experiment.md
  - galleria-wiki wiki/perceptual-coherence-and-symbolic-correctness.md
  - galleria-wiki wiki/local-video-generation-on-rtx-5080-16gb.md（「H3／Live2D比較からの制作規則」節）
  - galleria-wiki wiki/audio-driven-avatar-video.md、wiki/human-avatar-motion-routes.md
  - galleria-wiki wiki/parts-animation-backends.md（「無音の揺れ」節）
  - galleria-wiki wiki/local-ai-model-catalog.md（H3 の行）
  - galleria-wiki の raw: 2026-08-17-qualia-san-h3-live2d-video-experiment-feedback.md
---

# クオリアさんの H3／Live2D 台詞動画の比較（galleria, 2026-08-14〜17）

キャラクターに数秒の台詞を喋らせる短い動画を、作り方を変えて何版も作った実験。型は西尾が分類していない。8 秒程度の「見せ場」を魅力的に作るのが目的とされているので、ここでは promo と embed の両方に仮に置く。

## 何を作ったか（版の系列）

| 版 | 作り方 | 結果（人間の評価は galleria-wiki の記録から） |
|---|---|---|
| 1 | MiniMax H3（ローカル、component 39.55 GiB）で音声と映像を一体生成 | 日本語の一部が壊れた。一方で発音・イントネーション・口・視線・頭・髪の細かなタイミングは自然。一連の版で**最もなめらか** |
| 2 | 音声を VOICEVOX に差し替え | 台詞を決定論的に管理できるようになったが、H3 映像とのリップシンクを失った |
| 3 | 口だけをオーバーレイで補正 | 同期は改善したが、顔の動きとは別の表現の層になった |
| 4 | 1 枚の画像から PSD 素材と小規模な Live2D モデルを作り、表情・瞬き・傾き・音声同期を明示的に制御 | 技術 QA（192 フレーム、音声、同期、切替位置、灰色の口、残像、継ぎ目）は通った。人間の通常視聴では**一連の版で最も微妙** |

H3 の peak VRAM と生成時間は記録されていない（local-ai-model-catalog.md）。

## 分かったこと

- **品質は一つの軸ではなかった。** H3 が同時に生成する声・視線・頬・顎・頭・髪の協調は、音声差し替え、口の重ね描き、Live2D 化のたびに分解された。各工程で検査できる正しさは上がったが、全体の魅力は単調には上がらなかった。人間が H3 版に感じていた生命感は QA の項目に入っていなかった。
- galleria-wiki はこれを「知覚的整合性」（全体として自然に見聞きできること）と「記号的正確さ」（文字・語・数値・タイミングが正しいこと）の対立として整理した。生成モデルは前者に強く、語・発音・数値のような離散的な記号を誤る。組み立て型の工程はその逆。（perceptual-coherence-and-symbolic-correctness.md）
- これは**Live2D 一般の上限を測った比較ではない**。完成した大規模生成モデルと、短期間で作った小規模の自作リグの比較で、5 母音の口形・顔の XY 回転・視線・頬・呼吸・髪の連動を備えた商用品質の Live2D ではない。
- 8 秒程度の見せ場を作るのが目的なら、Live2D に移す初期工数は重かった。Live2D の価値は、同じキャラクターの長期運用、台詞の差し替え、撮り直し、実時間制御、ゲーム・配信で大きくなる。単発のヒーローショットでは H3 の持つ動きの事前知識の方が目的に近かった。
- 「作ってからわかる」: Live2D 試作は完成映像としては最良でなくても、何を品質と感じていたかを測る装置になった。明示した不具合を順に消すことと作品全体の魅力を上げることは別の最適化で、**エージェントは長い修正ループの途中でも目的を人間と確かめ直す必要がある**、と galleria-wiki は書いている。

## それで決めた次の方針（H3 を母体に残す。設計で、まだ実行の記録は無い）

1. 台詞を短い shot に分け、表記と seed を変えて複数生成する。
2. 誤読や重大な同一性の破綻を足切りの条件にし、通過した候補から人間が生命感と魅力で選ぶ。
3. 音声と映像を対のまま編集し、「スン」のような閉口・表情転換を自然な接続点にする。
4. 正しい H3 テイクが得られない短い区間だけ、前後のフレームを含めて局所的に再生成する。
5. VOICEVOX の query と Live2D は、モーラ境界・口形・絵コンテ・表情のタイミングの正解データとして使い、最終映像の全面的な代わりにしない。

順序も変える: **まず数秒の preview を H3 の基準版と通常視聴で比べ、「元より魅力的か」を通ってから**、音声・PTS・継ぎ目などの技術 QA に進む。

## 詰まったこと・落とし穴

- 日本語の台詞を一体生成させると記号（語・発音）が壊れる。音声だけを全面差し替えて正しさを取ると、演技の結合が切れる。
- **口を直す道具を、演技を作る道具の代わりに置かない。** 後の調査で挙がった LatentSync（既存動画の口だけを音声に合わせる）も、版 3 と同じ所に戻る、と galleria-wiki は注意している。（audio-driven-avatar-video.md）
- 共有ログに H3 の生成物の利用・表示地域についての二次情報があった。公開制作に使うなら、品質評価より前に現行の公式規約を一次情報で確かめる（第 0 の関門）。

## 関連する旧デモ（PSD から OpenCV で動かす）

`C:/Users/nishi/claude-win/PSDMaker-A/scripts/qualia_animate.py` は、PSD の通常合成と意味ラベル（耳・前後髪・頭・胴体のマスク）から、240 x 240 の格子で変位場を計算し、呼吸と首の傾きを周期関数、髪を位相遅れ、耳を根元固定の小さな揺れにして `cv2.remap` で描く。10 秒・30fps・960 x 960、FFmpeg に RGB24 の raw frames を pipe して H.264・CRF18・yuv420p・faststart の無音 MP4。41 時点の変位場で Jacobian の最小値 > 0.3、ループ端点の RGB 差 ≤ 1 をコードで要求している（標本検査で、全時刻の見た目の保証ではない）。（parts-animation-backends.md）

## 以後に調べた候補（galleria では未実行）

2026-09-04 の調査で、人物を演技させる経路を「何が動きを決めるか」で 4 つに分けた: 音声駆動、駆動動画、mocap、実時間操作。H3 は音声駆動、Live2D は実時間操作に当たる。ローカルの音声駆動候補 InfiniteTalk（base が Wan2.1-I2V-14B-480P、Apache-2.0）は、Wan2.2 I2V-A14B fp8 の peak 15,807 MiB の実測から 16GB に入る見込みとされたが未検証。（human-avatar-motion-routes.md、audio-driven-avatar-video.md）

## Open Questions

- H3-first の方針で実際に作り直した記録は無い。
- 実在しない合成キャラクターでも、realistic なら AI 生成の開示義務がかかり得るという整理が galleria-wiki にある（synthetic-likeness-disclosure.md）。アニメ調のキャラクターの短尺にどこまで関わるかは未整理。
