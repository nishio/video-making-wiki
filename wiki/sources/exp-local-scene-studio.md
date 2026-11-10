---
type: source
summary: 抽象的な日本語の指示を、ローカルの LLM で観察できる視覚要素の plan JSON に分解してから、FLUX.2 Klein で keyframe、Wan2.2 TI2V-5B で 3.4 秒の短い動画にする galleria の道具。16GB GPU でモデルを一つずつ載せ替える運用の作法が詰まっている。作品として使った記録は無い
video_types: [embed, any]
sources:
  - galleria の作業場の local-scene-studio の README.md
  - galleria の作業場の local-scene-studio の scene_studio.py（先頭の docstring と定数）
  - local-scene-studio は git 管理されていない（commit hash なし）
---

# Local Scene Studio（抽象指示 → 画像・短い動画）

## 何を作ったか

動画作品ではなく道具。「境界を越えた瞬間だけ、都市の重力が反転する」のような抽象度の高い日本語の brief を、クラウドを使わずローカルモデルだけで画像か短い動画にする「シーンコンパイラ」（README 冒頭）。出力は 1 shot あたり 832×480・81 frames・24fps・音声なし（3.375 秒）。長い尺は shot を作って編集でつなぐ前提（README「固定profile」）。

作品に使った記録・西尾の評価は、このディレクトリには無い。以下は設計と README に書かれた手順。

## 作り方のパイプライン

```text
抽象的な日本語 brief
  -> Ollama / Qwen（ローカル 27B）: 意味、視覚比喩、空間、motion、採否条件へ分解
  -> 検証済み scene plan JSON（schema 1.2）
  -> FLUX.2 Klein 4B distilled FP8: 1280x720 keyframe（4 steps、Euler、CFG 1.0）
  -> Wan2.2 TI2V-5B: 832x480 / 81 frames / 24fps（20 steps、CFG 5）
  -> PNG、H.264 MP4（PyAV / libx264、CRF 19）、prompt、SHA-256 付き manifest、contact sheet
```
（README の図と「固定profile」の表）

- `scene.cmd plan` で plan だけ作り、`interpretation`・`distributed_cues`・`image_prompt_en`・`motion_prompt_en`・`success_criteria` を人が読んでから `scene.cmd render <plan.json>` する、という 2 段の使い方ができる
- `--shots 1`〜`8`。画像を全 shot 作ってから画像モデルを降ろし、次に動画を全 shot 作る（モデルの切り替えを最小にする）
- `scene.cmd validate`（サービスを起動せずに plan と workflow を検査）、`scene.cmd doctor`（GPU・Ollama・ComfyUI・モデル・ノード・PyAV を検査）、`verify-video`（81 frames・832×480・24fps・H.264・音声なしを独立 decode で検査し 9 コマの contact sheet）

## 抽象語を絵にするときの考え方（README「抽象指示を扱う仕組み」）

- 画像・動画モデルへ抽象語をそのまま渡すと「孤独 = 一人の人物」のような単一の記号に縮む。前段の LLM に、次の観察できる要素へ翻訳させる
  - 前景・中景・背景に散らした最低 3 つの具体的な環境の変化
  - 主体と環境、視線の誘導、画面内の優先順位
  - 構図、レンズ感、光、色、材質
  - 開始画像を壊さない短い動きとその終点
  - 失敗条件（形の崩れ、ちらつき、不要なカメラの動き）
  - 人が採否を判断できる success criteria
- 看板・広告・UI・ホログラムなど文字を誘発する小道具は planner の検証で拒否する。**正確な文字・字幕・ロゴは生成後に合成する**

## 16GB GPU での運用の作法（落とし穴の裏返し）

- RTX 5080 16GB では、LLM を降ろしてから画像モデル、それを降ろしてから Wan、の逐次実行に固定した
- 他のセッションが Ollama のモデルを載せている間は勝手に止めずに停止する。止めてよいときだけ `--unload-ollama`
- Ollama の `/api/ps` が空になっただけでは解放完了としない。`nvidia-smi` で必要量の VRAM が戻ったのを 2 回確かめてから ComfyUI へ移る
- ComfyUI の `/free` は非同期に受け付けるだけなので、HTTP 200 一回を解放完了と扱わない。小さな barrier を 2 件通して処理されたことを確かめる
- 制作用には手動操作用の ComfyUI とは別のポート・別の state / input / output / temp / log を持つ専用 ComfyUI を起動し、処理の成否にかかわらず終了する
- 既存の成果物は既定で上書きしない。`--overwrite` 時も候補を作って完全 decode で合格してから一組で置き換える
- `--reference`（参照画像）は停止中。入力画像の内容をローカルで検証する仕組みがまだ無いため

## 再利用できる部品

- `scene_studio.py`: brief → plan → keyframe → I2V の一式（Ollama と ComfyUI の loopback API だけを使う）
- `examples/abstract-brief.txt`, `examples/example-plan.json`: plan の schema と手編集の例（実行ログの写しではない）

## Open Questions

- プレゼンに埋め込む概念解説（embed）の「動く挿絵」として使えるかは、作例と評価が無いので分からない。qualia の A/B/C 比較では、意味の無い微小な動きは「どこが変わったのかわからん」と評価された（[[exp-qualia-video]]）
- 1 shot の所要時間はこの README に書かれていない（manifest には記録される設計）
- FLUX / Wan の重みは Apache-2.0 だが、text encoder・VAE・生成物の条件は部品ごとに確認が要る、と README は書いている
