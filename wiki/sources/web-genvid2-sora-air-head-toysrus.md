---
type: source
summary: 2024 年に初期の Sora で作られた 2 本の制作記録。shy kids の短編「Air Head」（fxguide の取材）は 300:1 の素材から人が編集し、480p 生成 → 外部で拡大、色の補正・ロト・顔の消去・速度の補正を After Effects 等で行った。Toys"R"Us のブランド映像（Native Foreign、公式発表）は「数百のショットを二十数個に絞り」、修正の VFX と人の作曲を足した。丸ごと生成の映像も、選別と後処理と人の音で仕上げていたという記録
video_types: [promo]
url: https://www.fxguide.com/fxfeatured/actually-using-sora/
author: Mike Seymour（fxguide。shy kids の Patrick Cederberg への取材）／WHP Global（Toys"R"Us の所有者）のプレスリリース
published: 2024-04-14（fxguide）／2024-06（Toys"R"Us、Cannes Lions 2024 で初公開）
retrieved: 2026-11-09
sources:
  - https://www.fxguide.com/fxfeatured/actually-using-sora/ （"Actually using SORA", 2024-04-14）
  - https://www.whp-global.com/blogs/brand-news/toysrus-studios-and-native-foreign-use-openais-sora-to-narrate-the-origin-story-of-beloved-toyrus-brand （プレスリリース）
---

# 初期の Sora で作った 2 本の制作記録（Air Head／Toys"R"Us の origin film）

## 何の文献か

- **fxguide「Actually using SORA」**（2024-04-14、Mike Seymour）: VFX の業界誌による、shy kids（カナダの制作会社）の Patrick Cederberg への取材記事。短編「Air Head」（風船の頭の男）は OpenAI が 2024 年春に作家に試させた初期の Sora で作られた。制作者本人の言葉を引いた一次に近い資料。
- **WHP Global のプレスリリース**（Toys"R"Us Studios と Native Foreign の共同制作、監督 Nik Kleverov）: Cannes Lions 2024 で初公開した Toys"R"Us の創業者の物語の「ブランド映像」についての公式発表。宣伝の文書で、制作の細部は少ない。

どちらも 2024 年前半の Sora（一般公開前）の記録で、2026 年のモデルとは機能が大きく違う（参照画像・先頭フレームの入力が無かった）。持ち越せるのは工程の形。

## 書いてあること

### Air Head（fxguide）

- **ショット間の一貫性が出せない**: 当時の Sora は文字のプロンプトだけで、別のショットを前のショットに合わせる手段が無かった。黄色い風船を頼んでも黄色でないことがあり、顔が埋め込まれたり描かれたりし、風船から連想して紐がシャツの前に垂れた。対策は「衣装や風船の種類を極めて詳しく書く」ことだけだった
- **後処理**: 「Air Head は Sora の生成映像だけを使っている」が、多くは色の補正・処理・手ぶれ補正をし、**すべてを拡大した**。480p で生成し（速度のため）、外部のツール（Topaz）で拡大した。風船を切り出して色を塗り直すロトスコープ、マーカーで描いたような顔の消去を After Effects で行った。35mm フィルムの語で一貫性を出し、最後に自前の粒子とちらつきを足して全体をなじませた
- **時間の制御はスロットマシン**: プロンプトは自動で拡張され、タイムライン上の「keyframe」で調整できたが、「どこで何が起きるかの時間の制御は少しあるが正確ではない……スロットマシンのよう」と言う
- **カメラの動きが出ないとき**: ジーンズから頭へのパンアップを Sora は出さなかった（主題の頭を常に画面に入れたがる）ので、縦長で生成し、後で切り抜いてパンを作った
- **速度**: 多くの clip が頼んでいないのにスローモーション（50〜75% の速さ）で出たので、実時間に見えるよう速度を直した
- **300:1**: 最終の約 1 分半に対し「10〜20 秒の生成を数百本」、素材と完成の比は「たぶん 300:1」。台本はあったが、ドキュメンタリーのように大量の素材から語り（VO）に合わせて編む方法をとった。1 本の生成は 10〜20 分
- **音は人**: 音楽は shy kids の既存の曲、声は Patrick 本人。間が足りないときは台詞を書き足して録り、それに合う clip を生成した
- 作り手は 3 人、約 1.5〜2 週間
- 「Aronofsky type shot」「Hitchcock Zoom」のような監督名・技法名を含むプロンプトは著作権の理由で拒否された

### Toys"R"Us の origin film（公式発表）

- Native Foreign の CCO が Sora の alpha 版の利用権を持っていた。「Sora によって数週間でコンセプトを形にし、**数百の反復したショットを二十数個に絞った**」
- 「ほぼ全体を Sora で作り、**修正の VFX** と、Copeland の Aaron Marsh が作曲した**オリジナルの音楽**を加えた」
- どのショットに何の修正をしたかは書いていない

## この wiki への含意

- **promo**: 2 本とも「丸ごと生成」と呼ばれるが、実際は**大量に生成 → 人が選ぶ → 人が直す（色・ロト・速度・拡大）→ 人の音**の工程だった。[[web-genvid2-niq-system1-ai-generated-ads]] の NIQ の「見抜かれなかった唯一の広告は専門家の大きな編集」、Coca-Cola の 7 万 clip（報道）と同じ形。生成の費用（[[web-genvid2-wan-ltx-hunyuanvideo-minimax-h3]] の秒単価）より、選別と後処理の人手が支配的になる
- **経験と一致（keeper を選ぶ）**: 300:1 で選ぶ作り方は、[[exp-galleria-local-video-generation]] の「rough な場面から候補を広く作り、人間が keeper を選び、動きに役割があるものだけを小さな A/B で動画化する」と同じ向き。ただし Air Head は**動画を大量に作ってから選んだ**のに対し、galleria は**静止画で選んでから動画にする**ことで生成の時間を節約した。2024 年の Sora には先頭フレームの入力が無かったので、静止画で選ぶ方法がとれなかった
- **経験と一致（一貫性は上流で決める）**: Air Head の「ショット間で風船が揃わない」は、[[exp-galleria-local-video-generation]] の「別々に生成した 2 枚は中央で切り替わるだけ」「質は keyframe 対で決まる」と同じ問題の、参照入力が無い時代の版。今のモデルは参照画像・両端固定でここを上流（静止画）に移せる
- **音は人が持つ**: どちらも音楽と声は人。[[exp-qualia-h3-live2d-galleria]] では H3 の一体生成の声と映像の協調が一番魅力的だった。音を同時生成するモデル（H3、LTX-2.x）が出た 2026 年に、この分担がどう変わるかは 2024 年の記録からは言えない
- **作品の紹介には不向きな点**: どちらも作り話・想像の場面（風船の男、創業者の夢）で、実在の製品の画面を正確に見せる必要が無かった。作品の画面や数値を見せる promo では、[[web-genvid2-t2vtextbench-design-video-eval]] の問題が加わる

## Open Questions

- Toys"R"Us の「修正の VFX」の中身（どのショットの何を直したか）は公式発表に無い。監督の取材で書いたものは見つけていない
- 両作品の受け手の評価（ネット上の反応は賛否が割れたと報じられたが、測った資料は読んでいない）
- 2026 年の参照画像つきのモデルで、選別の比（300:1）がどこまで下がるか
