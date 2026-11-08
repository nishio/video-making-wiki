---
type: source
summary: Blender の Grease Pencil（3D 空間に手描きの線を置く 2D アニメの道具）の、4.3（2024-11）の全面書き直しから 5.2 LTS までの変化の一次資料。4.3 でデータ構造と Python API が別物になり（GPENCIL → GREASEPENCIL、frame.strokes → frame.drawing と属性）、5.0 で旧 API の名前が Annotation に移り、5.1 で塗りの扱いが fill_id に変わり、5.2.4 からフレームの長さの機能が無効になる。SVG の読み込み・書き出し、3D の場面から線画を作る Line Art がある
video_types: [promo, talk, embed]
url: https://developer.blender.org/docs/release_notes/4.3/grease_pencil/
author: Blender Foundation（Developer docs の release notes、Blender Manual、Python API docs）
published: 2024-11-19（4.3）〜 2026-07-14（5.2 LTS）。各 notes は継続更新
retrieved: 2026-11-09
sources:
  - https://developer.blender.org/docs/release_notes/4.3/grease_pencil/
  - https://developer.blender.org/docs/release_notes/4.3/grease_pencil_migration/
  - https://developer.blender.org/docs/release_notes/5.0/grease_pencil/
  - https://developer.blender.org/docs/release_notes/5.0/python_api/ （Annotations & Grease Pencil）
  - https://developer.blender.org/docs/release_notes/5.1/grease_pencil/
  - https://developer.blender.org/docs/release_notes/5.2/grease_pencil/
  - https://docs.blender.org/manual/en/latest/grease_pencil/introduction.html
  - https://docs.blender.org/manual/en/latest/grease_pencil/modifiers/generate/line_art.html
  - https://docs.blender.org/api/current/bpy.types.GreasePencilDrawing.html
  - https://docs.blender.org/api/current/bpy.ops.wm.html （grease_pencil_import_svg / export_svg）
---

# Blender の Grease Pencil（4.3 の書き直しから 5.2 まで）

Blender 全体の版・コマンドラインの描画・ライセンスは [[web-means-3d-blender-bpy-cli]]。ここは Grease Pencil に固有のことだけ。

## 何の文献か

- Blender の開発者サイトの release notes（4.3 の Grease Pencil と移行の手引き、5.0・5.1・5.2 の Grease Pencil、5.0 の Python API）、Manual（導入、Line Art）、Python API docs。すべて作り手の文書。使った人の評価や、手描きのアニメの実務の記録は読んでいない。

## 書いてあること

### 何をする道具か（Manual）

- 「Grease Pencil は Blender の物体。マウスか筆圧のあるペンからの描画を受け取り、**3D 空間に点の集まり（ストローク）として置く**」「伝統的な 2D アニメ、切り絵アニメ、モーショングラフィックス、絵コンテの道具などに使える」。
- 始め方: Object Mode で Add ‣ Grease Pencil ‣ Blank → キーフレームを作るか Auto Key → Draw Mode で描く。既存の場面に足すか、「2D Animation」のテンプレートで始める。描いた線に材質・モディファイア・光・効果を足せる。
- **Line Art モディファイア**: 「場面・コレクション・物体から様式化した線画を作る」。アクティブなカメラが要り、カメラから見える部分にだけ線ができる。モディファイアごとに遮蔽の計算を全部やり直す（共有のキャッシュが無い）。

### 4.3（2024-11-19）: 書き直し

- 「深い制約を取り除き全体の性能を上げるため、Grease Pencil を書き直した」。新機能: レイヤーのグループ、ブラシのアセット、描画ツールの変更（半径の単位を View か Scene に、`Spacing`、能動的な平滑化を曲線の当てはめで書き直し、簡略化をピクセル単位に）、線を「切る」消しゴム、**Geometry Nodes で Grease Pencil を扱える**、塗りのグラデーションの道具。マルチスレッド化、ファイルは 2.5〜3.4 倍小さく（例示の 2 ファイル）。
- 互換: 「4.3 以後、Grease Pencil の物体は読み込み時に新しい構造へ自動変換する。**前方互換は無い。4.3 以上で作った・保存したファイルは 4.2 以下で正しく読めない**」。
- 廃止: Screen Space の線の太さ（常に World Space）、補間ツールの選択順、描画のガイド、曲線の編集モード（ストロークの `Curve Type` に置き換え）。
- **Python API（移行の手引き）**: 「4.3 より前の Grease Pencil の Python API で書いたアドオンは、この版で壊れると見込まれる」。
  - 物体の型 `GPENCIL` → **`GREASEPENCIL`**、RNA の型 `bpy.types.GreasePencil` → `bpy.types.GreasePencilv3`、モード `PAINT_GPENCIL` → `PAINT_GREASE_PENCIL`、`EDIT_GPENCIL` → `EDIT` など。
  - `layer.info` → `layer.name`、`layer.active_frame` → `layer.current_frame()`、`layer.location` → `layer.translation` など。
  - **ストロークと点**: 4.2 の `frame.strokes`・`strokes.points` は、4.3 では `frame.drawing` が全データを持ち、**属性（`drawing.attributes`、CURVE と POINT の領域）**として入る。旧来に近い互換の API `drawing.strokes` があるが、「RNA の型ではなく補助のクラス。ストロークや点の参照を持ったまま描画を変えて再び触ると**未定義の動作**」「性能は 4.2 より悪いと見込まれる。性能が要るなら `drawing.attributes` を使え」。フレームの移動は `frames.move(old, new)`。
- API docs（current）: `GreasePencilDrawing.add_strokes(sizes)`（各ストロークの点の数を渡して末尾に足す）、`remove_strokes`、`resize_strokes`、`set_types` など。

### 5.0（2025-11-18）

- 編集: 「Curve Data」パネル、**Pen ツール**（旧来の曲線物体のペンツールに似る）、補間ツールが Bézier と Catmull-Rom に対応、`Join Strokes`。
- 描画: **モーションブラーに対応**（描画の設定で有効にし、Grease Pencil の「Motion Blur Steps」を上げる。制限: メッシュの背後などに合成されるときは現在のコマだけで合成し、遮られる所の縁が硬くなりうる。ビューポートには出ない）。角の種類に Sharp・Flat を追加。
- 書き出し: Bézier・Catmull-Rom・NURBS の曲線を **SVG に書き出せる**（今は幅が一様なストロークだけ）。
- Python API: Annotation（注記）に関わる型の名前を変えた。`bpy.types.GPencilStroke` → `AnnotationStroke`、`bpy.types.GreasePencil` → `bpy.types.Annotation`、`Scene.grease_pencil` → `Scene.annotation` など。

### 5.1（2026-03-17）

- **新しい塗りの流れ**: 材質で塗りを入り切りする代わりに、描画ツールの「Stroke / Fill / Both」と専用の操作で塗る。**塗りに穴を開けられる**。`Join Fills`・`Separate Fills`・`Select Fill` など。Trace Image と **SVG の読み込みも穴を作れる**。PDF・SVG の書き出しは穴のある塗りを出せる。
- 互換: 新しい属性 `hide_stroke`（ストロークを隠す）と **`fill_id`（0 なら塗らない。既定が 0 なので「曲線は既定で塗られない」）**。Geometry Nodes の `Set Material` で塗っていた構成は手直しが要る。notes の例は「**文字列を Grease Pencil の塗りに変える**構成」で、5.0 では穴のために字を分割する小技が要ったが、5.1 は `fill_id` を与えれば足りる。
- Python: `LayerGroup.children`・`GreasePencil.root_nodes`（レイヤーの木を下から上の順で辿る）。

### 5.2 LTS（2026-07-14）

- **警告**: 「技術的な理由で、**5.2.4 から frame duration（フレームの長さ）の対応を完全に無効にする**」。既存の「終わりのフレーム」は読み込み時に空の描画のフレームに変換される。（2026-11-09 の配布は 5.2.3。）
- 描画ツールで作る曲線の型（Bézier・Catmull-Rom・NURBS）を選べる。塗りツールに新しい **Delaunay** の解法（境界のストロークから正確な形を作る、隙間の自動検出、ズームに依らない、多くの場合速い）が既定に。点・四角の材質の配置（数・密度・半径）と乱数化。オンラインの「essentials」のテクスチャ付きブラシ（使うには「Allow Online Access」が要る）。

## この wiki への含意

- **西尾の手元に無い「手描きの線」の表現**: 西尾の動画はすべてコードで描いた幾何の図形と文字（[[exp-html-capture-pipeline]]）。Grease Pencil は人の手の線（ペンタブレットで描く）を 3D 空間に置き、カメラを動かせる。talk・embed の「黒板に手で描いた図が動く」感じ、promo の手描きの温度。ただし手で描くのは人の仕事で、AI に任せられる部分は小さい。
- **AI に任せられる経路**（推測）: (1) **SVG を読み込んで Grease Pencil にし**（`bpy.ops.wm.grease_pencil_import_svg`、5.1 から穴も）、モディファイアで線を描き進める・揺らす。LLM は SVG を書くのが得意なので、「AI が SVG の図を書く → Blender で手描き風の線として動かす」。(2) **Line Art で 3D の場面を線画にする**（[[web-means-3d-blender-bpy-cli]] の場面を、説明図の線画の調子で描く）。(3) Python の `drawing.add_strokes` と属性で点列を直接書く。
- **LLM の知識の古さが効く所**: Grease Pencil の Python API は 4.3 で全面的に変わり、5.0 で旧名が Annotation に移った。モデルが 4.2 以前の `frame.strokes.new()` などで書くと、**5.0 以後では Annotation の API に当たってしまうか、エラーになる**（推測。名前の対応表から）。スクリプトを書かせるときは「Blender 5.2、Grease Pencil v3、`frame.drawing`」と明示する。
- **版を固定する**: 4.3 以後のファイルは 4.2 以下で読めない。5.2.4 でフレームの長さが無効になる。galleria で使う版を決めて固定する（5.2 LTS を 5.2.3 のまま使うか、5.2.4 に上げるか）。

## 着手の仕方（未検証。galleria で確かめる）

- **何が表現できるようになるか / 効く型**: 手描きの線の 2D アニメ（3D 空間に置いた線をカメラで撮る）、SVG の図を手描き風の線として描き進める、3D の場面の線画化（Line Art）。talk・embed（黒板に描くような説明図）、promo（手描きの温度）
- **機械**: **galleria Windows**（Blender 5.2.3。描くならペンタブレットがあるとよい〈有無は未確認〉。描かずに SVG・Line Art・Python で作るならマウスで足りる）。GPU: EEVEE で描くなら要（VRAM は軽い見込み、推測）。Mac でも Blender 5.2 は動く（Apple Silicon）。費用 0、アカウント不要（オンラインのブラシを使わなければネット接続も不要）。GPL、出力は作者のもの
- **成熟度**: 4.3 で書き直し、5.0〜5.2 で機能が戻り・増え続けている。5.2.4 で frame duration が無効になる予定
- **最小の手順（Windows。Python の中身は推測を含む）**:
  ```powershell
  cd $HOME\video-tools-trial\blender
  # 1) LLM に SVG を書かせる（例: 矢印と 3 つの丸の概念図 diagram.svg、幅が一様な線で）
  # 2) gp.py（推測）:
  #   import bpy, sys
  #   bpy.ops.wm.read_factory_settings(use_empty=True)
  #   bpy.ops.wm.grease_pencil_import_svg(filepath=r'...\diagram.svg', directory=r'...', files=[{'name': 'diagram.svg'}])
  #   ob = [o for o in bpy.context.scene.objects if o.type == 'GREASEPENCIL'][0]   # 4.3 以後の型名
  #   （Build モディファイアで線を描き進める。モディファイア名は 5.2 の docs で確かめる）
  #   カメラを置き、sc.render.engine = 'BLENDER_EEVEE'、出力を PNG 連番に（media_type → file_format の順）
  & $B -b --factory-startup --python-exit-code 1 -P gp.py -- out\gp_ 1 90
  ```
  手で描く場合は GUI で「2D Animation」のテンプレートから始め、.blend を保存し、`& $B -b work.blend -o //out/gp_#### -F PNG -a` で描く（引数の順は `-a` を最後に）
- **動いたと言える確かめ方**: (1) スクリプトの終了コードが 0、(2) `ob.type == 'GREASEPENCIL'` の物体ができている（ログに print）、(3) `out\gp_0001.png` で線が途中まで、`gp_0090.png` で全部描かれている、(4) 線の縁が SVG の形と一致（静止画を SVG を開いた画面と並べる）
- **所要の見込み（推測）**: SVG 経由の最小例で半日。手描きのアニメは、描く人の慣れによって日〜週

## Open Questions

- Grease Pencil の線を EEVEE で `-b` で描けるか（Windows の headless の EEVEE と同じ問い。[[web-means-3d-blender-bpy-cli]]）
- SVG の読み込みで、LLM が書いた SVG のどこまで（文字・グラデーション・クリップ）が線と塗りとして入るか。文字は輪郭にしてから入れる必要がありそう（推測）
- 手描きの説明図（talk・embed）を西尾が自分で描くか、描く人を頼むか。そもそも西尾の動画に手描きの調子が要るかは西尾が決めること
- Line Art で作った線画が、説明図として [[design-fundamentals]] の情報設計（余計な線を減らす）と合うか。Line Art は見えるエッジを全部拾うので、線を選ぶ設定が要るはず（推測、試していない）
