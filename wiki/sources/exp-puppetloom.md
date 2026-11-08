---
type: source
summary: クオリアさんの 1 枚絵から PuppetLoom（レイヤー PSD から 2D パペットを作る OSS）で動くキャラクター動画を作ろうとした 2026-09-08 の試み。前段の See-Through（1 枚絵のレイヤー分解）がオンラインのデモにしか無く、接続拒否とログイン要求で止まり、リギングと録画には進まなかった
video_types: [talk, any]
sources:
  - galleria C:\Users\nishi\claude-win\PuppetLoom\README.ja.md（上流 github.com/CheshireMew/PuppetLoom の clone、最終 commit f545608 2026-08-28）
  - galleria C:\Users\nishi\claude-win\PuppetLoom\docs\VIDEO_REFERENCE_FINDINGS.md
  - galleria C:\Users\nishi\claude-win\PuppetLoom\work\layering-review\（git 管理外。2026-09-08 の request.json / result.json）
  - galleria-wiki raw/2026-09-09-qualia-puppetloom-see-through-experiment.md
---

# PuppetLoom でクオリアさんを動かす試み

## 何をしようとしたか

既存のクオリアさん画像と音声から、レイヤー分けした 2D キャラクターの動画を作れるかを試した（galleria-wiki raw 2026-09-09）。PuppetLoom は上流の OSS をそのまま clone したもので、西尾側の変更は無い（`git status` で未追跡の `work/` だけ）。

PuppetLoom がすること（README.ja.md の要約）:

- レイヤー分けしたキャラクター PSD から、呼吸・視線が先行する頭の回転・髪や衣装の遅れなどを持つ 2D パペットを作る（Windows、Node.js 24、WebGL2）
- 中立姿勢と 12 の動作姿勢を検証し、調整を revision として残す。外部のエージェントには CLI（`inspect` / `create` / `verify` / `play` / `record`）と同梱の Skill を使わせる設計
- パペットのウィンドウは透明・単色背景で 24/30/60 FPS の WebM 録画ができる。マウス追従・顔トラッキング・マイク口パクも入力にできる
- 素材に無い閉じ目や口の形をパラメータで偽造しない。プロの Live2D の代わりではない、と README 自身が書いている

## やったこと

- PuppetLoom の Skill と手順を読み、「1 枚絵 → See-Through で分層 PSD → PuppetLoom の inspect / create / verify / record」の経路を選んだ
- 512×512 の参照画像を不透明な白背景の PNG にし、比較用に 1024px 正方へ正規化した（`work/layering-review/<run>/request.json`）
- 1 回目: See-Through のオンラインデモへの接続が Windows のソケット権限エラー（WinError 10013）で失敗（`result.json`）
- 2 回目: アップロードまでは進んだが、ModelScope Studio がログイン・登録（携帯電話番号など）を求め、そこで止めた（galleria-wiki raw）

## 分かったこと・落とし穴

- PuppetLoom は 1 枚の PNG をそのままキャラクターとして扱う道具ではなく、**分層済みの PSD が前提**の制作・検証基盤だった（galleria-wiki raw の結論）
- 1 枚絵の分層を外部のオンラインサービスに頼ると、アカウント登録と画像の外部送信が要る。避けるなら分層 PSD を別の経路で用意するか、PuppetLoom を使わない簡易な経路に切り替える
- 上流の `docs/VIDEO_REFERENCE_FINDINGS.md` は、別の動画プロジェクトの画面から読み取れる機能（意味点・姿勢テンプレート・自動巡検・作用レイヤーの確認）を参考にした記録で、ソースの無いものから「中で何を使っているか」を断言しない書き方をしている

## Open Questions

- 分層 PSD をローカルで作れれば、解説動画の話し手キャラクターとして使えるか（口パク・瞬きのある話し手は、qualia の「静止が既定」の規則と両立するか）は未検証。[[exp-qualia-video]] の C 案（Wan2.2 の微小な動き）は不採用だった
- 同じ時期のクオリアさんの 3D / VRM 経路の試み（galleria-wiki raw 2026-09-06, 09-08）はこのページでは扱っていない
