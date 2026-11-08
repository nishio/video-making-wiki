---
type: source
summary: Blender を Python（bpy）とコマンドライン（blender -b -P）で動かして描画するための一次資料。2026-11-09 時点の安定版は 5.2.3 LTS（5.2 は 2026-07-14）。引数は書いた順に実行され、-f/-a は最後に置く。Cycles の GPU は -- --cycles-device OPTIX（NVIDIA は driver 575 以上）。Linux の headless の EEVEE は EGL への逃げ道があるが Windows には無い。5.0 で EEVEE の識別子が BLENDER_EEVEE に戻り、画像形式の設定に media_type が要るなど、LLM が覚えている古い API と食い違う。pip の bpy 5.2.3 は Python 3.13 専用。GPL だが作ったものは作者のもの
video_types: [promo, talk, embed]
url: https://docs.blender.org/manual/en/latest/advanced/command_line/render.html
author: Blender Foundation（Blender Manual・Python API docs・Developer docs の release notes・blender.org）、ahujasid（blender-mcp）、athemeroy（awesome-claude-5-5-videos の data/cases.csv）
published: unknown（manual は継続更新。版は本文）
retrieved: 2026-11-09
sources:
  - https://www.blender.org/download/ （5.2.3 LTS）
  - https://developer.blender.org/docs/release_notes/ （版と日付の一覧）
  - https://docs.blender.org/manual/en/latest/advanced/command_line/render.html
  - https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html
  - https://docs.blender.org/manual/en/latest/render/cycles/gpu_rendering.html
  - https://www.blender.org/download/requirements/
  - https://www.blender.org/about/license/
  - https://pypi.org/project/bpy/ （5.2.3、requires_python ==3.13.*）
  - https://docs.blender.org/api/current/info_advanced_blender_as_bpy.html
  - https://docs.blender.org/api/current/bpy.types.ImageFormatSettings.html
  - https://developer.blender.org/docs/release_notes/5.0/python_api/
  - https://developer.blender.org/docs/release_notes/5.0/eevee/
  - https://developer.blender.org/docs/release_notes/5.1/eevee/
  - https://developer.blender.org/docs/release_notes/5.2/python_api/
  - https://lists.blender.org/pipermail/bf-blender-cvs/2022-August/176810.html （headless OpenGL on Linux の commit）
  - https://irendering.net/eevee-next-headless-dilemma-cloud-render-farm-guide/ （レンダーファームの宣伝記事。扱いは本文）
  - https://docs.blender.org/manual/en/latest/modeling/texts/introduction.html
  - https://docs.blender.org/manual/en/latest/modeling/texts/properties.html
  - https://github.com/ahujasid/blender-mcp/blob/main/README.md
  - https://github.com/athemeroy/awesome-claude-5-5-videos/blob/main/data/cases.csv
---

# Blender を bpy とコマンドラインで描く

## 何の文献か

- Blender の公式: Manual（コマンドラインの描画・引数、Cycles の GPU、文字オブジェクト）、Python API の docs、開発者サイトの release notes（4.3〜5.2）、blender.org のダウンロード・動作環境・ライセンスの頁、PyPI の `bpy`。いずれも作り手の文書。
- 2022-08 の commit の告知（bf-blender-cvs のメーリングリスト）。
- iRender（クラウドのレンダーファーム業者）のブログ記事（2026-10）。**自社のサービスを売る記事**で、主張の根拠は示されていない。参考として要点だけ書く。
- 第三者の MCP サーバー `blender-mcp`（MIT、star 33,668、最終 push 2026-11-04）の README。Blender 財団とは無関係と自ら書く。
- awesome-claude-5-5-videos の `data/cases.csv`（Opus 5.5 期の作品 168 件の作者の開示を集めたもの。[[web-opus2-awesome-claude-5-5-videos]]）から、Blender を名指しした 15 件を読んだ。数値はすべて**作者の自己申告**。

## 書いてあること

### 版（2026-11-09）

- 安定版は **Blender 5.2.3 LTS**（5.2 LTS は 2026-07-14）。5.3 は RC、5.4 は alpha。4.5 LTS（2025-07-15）は 2027-07 まで支える。5.0 は 2025-11-18、5.1 は 2026-03-17。Windows・Linux（glibc 2.28 以上）・macOS（**5.0 以後は Apple Silicon のみ**）。
- 動作環境: RAM 8GB（推奨 32GB）、GPU は **2GB VRAM で OpenGL 4.3 か Vulkan 1.3**（推奨 8GB）。NVIDIA は GeForce 900 以後。

### ライセンス（blender.org/about/license）

- Blender は GNU GPL。「**Blender で作ったものはあなただけのもの。画像・動画のファイル、.blend などのデータは自由に使える**」「商用で、スタジオで、ゲームで、研究で、教育で使える」。
- 「登録不要。Blender を入れて使う限り**インターネットに接続しない**」。一部の同梱のアドオンはネットに接続しうるが既定で無効。

### コマンドラインで描く（Manual）

- 「コマンドラインの利点は画面が要らないこと（Linux なら X サーバー不要）で、リモートのシェル（SSH）から描ける」。
- **「引数は与えた順に実行される」**。`blender -b file.blend -a -x 1 -o //render` は出力先を設定する前に描くので期待どおりにならない。**`-f` と `-a` は必ず最後に**置く。`--render-output` を `.blend` を読む前に置くと、ファイルの読み込みで上書きされる。
- 1 コマ: `blender -b file.blend -f 10`。出力: `-o /project/renders/frame_#####`（# は桁数）、`//` で始めると .blend からの相対。形式の上書き: `-F PNG`（`OPEN_EXR`・`FFMPEG` などはビルドによる）。
- アニメ: `blender -b file.blend -a`、範囲 `-s 10 -e 500`、エンジン `-E CYCLES`（`-E help` で一覧）、スレッド `-t`。
- Python: `-P`/`--python <file>`、`--python-expr <式>`、`--python-exit-code <0..255>`（「コマンドラインから実行したスクリプトで Python の例外が出たら、その終了コードで抜ける」）。`--factory-startup`（ユーザーの startup.blend を読まない）。**`--` の後の引数はそのまま `sys.argv` に渡る**。
- Cycles の GPU: 「Cycles のオプションは `--` の後に書く」。`--cycles-device CPU|CUDA|OPTIX|HIP|ONEAPI|METAL`、`+CPU` で併用。例: `blender -b file.blend -f 20 -- --cycles-device OPTIX`。
- GPU の裏側: `--gpu-backend vulkan|metal|opengl`。

### Cycles の GPU（Manual「GPU Rendering」）

- **OptiX**: Windows と Linux、compute capability 5.0 以上、**ドライバ 575 以上**。RTX の光線追跡ハードを使う。CUDA も同じ条件。OpenImageDenoise の GPU 加速は compute capability 7.0 以上（全 RTX）。
- 制限: Path Guiding は GPU 非対応。OSL は OptiX のみ（制限付き）。

### EEVEE を画面なしで描く

- 2022-08-15 の commit「Linux で headless の OpenGL 描画を入れる」: 「通常のビルドで headless の裏側が常に使え、**background mode で他の裏側の初期化に失敗したら、それに逃げる**」「**headless の裏側は Linux だけ。Mac と Windows は EGL を使わないから**」。
- 5.2 の Python API の notes: 「`gpu.init()` を足した。**`--background` で動かすとき GPU の裏側を初期化する**」。
- 5.1 の EEVEE の notes: マテリアルのシェーダのコンパイルが速くなった（barbershop_interior の cold で OpenGL 44.19 → 30.39、Vulkan 24.87 → 11.67。単位は表に無いが秒と読める）。
- iRender の記事（宣伝）: 「EEVEE-Next（4.2 以後）は Vulkan か OpenGL 4.3 の表示の文脈を要し、表示サーバーの無い仮想化した headless のコンテナでは落ちるか真っ黒なコマを出す」と書く。根拠の資料は示していない。Blender の公式の文書でこの主張を確かめることはできなかった。

### 5.0〜5.2 の API の変化（LLM が覚えている書き方と食い違う所）

- 5.0: **EEVEE の描画エンジンの識別子が `BLENDER_EEVEE_NEXT` から `BLENDER_EEVEE` に変わった**（5.0 より前の書き方は `BLENDER_EEVEE_NEXT`）。
- 5.0: 「`ImageFormatSettings` に `media_type` が入り、**`file_format` を設定する前に適切な型に設定する必要がある**」。`media_type` は `'IMAGE' | 'MULTI_LAYER_IMAGE' | 'VIDEO'`（既定 `'IMAGE'`）。
- 5.0: VSE は `context.sequencer_scene` を使い、`context.scene` と別になりうる。Grease Pencil の旧 API は Annotation に改名（[[web-means-3d-blender-grease-pencil]]）。
- 4.3: Grease Pencil を書き直し、Python API も別物になった（同）。

### Blender を Python のモジュールとして（bpy）

- PyPI の `bpy` 5.2.3（2026-10-22）: 「Python のモジュールとしての Blender」。**`requires_python ==3.13.*`**、wheel は Windows x64・Linux x86_64（manylinux_2_28）・macOS arm64。「各 Blender の版は一つの Python の版だけに対応し、パッケージはその版とだけ互換」。LTS の窓の外の版は PyPI から消え、download.blender.org に置かれる。
- API docs: 「多くの点で background mode（`-b`）でスクリプトを動かすのと同じ」。`bpy.app.binary_path` は既定で空。`gpu`・`mathutils` などは `bpy` の後に import する。コマンドライン引数は使えない。

### 日本語の文字（Manual の文字オブジェクト）

- 文字オブジェクトは曲線と同じ系統の物（フォントはベクターのデータ）。組み込みのフォント（データブロックの一覧で「Bfont」）のほか、**PostScript Type 1・OpenType・TrueType の外部フォント**を読める。押し出し（厚み）・ベベルで立体にできる。
- 「同じスタイルの文字には同じフォントが当たる。スタイルごとに別のフォントが要る（標準・斜体・太字・太字斜体の最大 4 つ）」。対応しないフォントを選ぶと `Not a valid font` のエラー。1 つの文字オブジェクトの上限は 50,000 字。
- 組み込みの Bfont に日本語の字形があるか、足りない字形を別のフォントで補うかは、読んだ Manual の頁に書かれていない。

### エージェントから Blender を動かす経路

- `blender-mcp`（MIT）: 「Blender を任意の LLM で操作するコミュニティのプラグイン」。Blender のアドオンがソケットのサーバーを立て、MCP のクライアント（Claude Code など）とつなぐ。`claude mcp add blender uvx mcp-for-blender`。**警告: 「`execute_blender_code` は Blender の中で任意の Python を走らせる。強力だが危険になりうる。必ず先に保存せよ」**。Poly Haven の素材のダウンロード機能がある（チェックで切れる）。テレメトリは「内容の収集は opt-in」だが、**既定でも匿名の利用記録**（ランダムな ID、ツール名、成否、所要、版、OS、時刻）を送る。`DISABLE_TELEMETRY=true` で全部止まる。
- 作品の作者の申告（cases.csv、168 件中 Blender を名指ししたのは 15 件）: 日本語の作者が「Opus が Python で Blender に 9 場面を作り、**Cycles で 720 コマを約 15 分で描画**、その後 Python で文字を重ねた」（BGM はローカルのモデル、画像と事実のメモは人が用意）。別の作者は「Higgsfield の Blender bridge / MCP 経由で Blender 5.2 / EEVEE を動かし、272 個の物体を作り爆発のアニメの衝突を確かめた」。「headless の Blender で GLB を 21 個作って Three.js の場面にした」例、「Blender の草モデルで機位と動きを決め、それを参照に動画生成モデルで最終の絵を作る」例もある。いずれも作者の自己申告で、工程や時間は検証されていない（repo の編者の注記）。

## この wiki への含意

- **西尾の方式との差**: 西尾の HTML 方式は「1 コマを JS の関数で描く」。Blender は「場面（物体・光・カメラ・キーフレーム）を Python で組み、描画はエンジンに任せる」。純関数の契約は「.blend と Python のスクリプトとコマ番号で絵が決まる」に置き換わる。`-f <番号>` で 1 コマだけ描けるので、`capture.mjs stills` に当たる確認はそのまま作れる。
- **増える表現**: 写実的な光・影・質感（Cycles の光線追跡）、物理（剛体・布・流体）、立体の文字（押し出し・ベベル）。promo の「質感」（[[exp-polis-magi-op]] で「腰を据えないとできない」とされた所）に効く可能性がある。talk・embed では立体の構造を回して見せる図。
- **galleria では Windows 版**: Linux の headless の EGL の逃げ道は WSL で働くか分からない。Windows には EGL の逃げ道が無いが、Windows の Blender はデスクトップの GPU（RTX 5080）の文脈を普通に作れるはず（推測）。Cycles は CUDA/OptiX なので表示の文脈が要らず、WSL でも動く可能性が高い（NVIDIA の CUDA on WSL、[[web-means-3d-threejs-headless-webgl]]）。
- **LLM に書かせるときの落とし穴**: 5.0 の `BLENDER_EEVEE`・`media_type`、4.3 の Grease Pencil の書き直しは、モデルが 4.x 以前の書き方で書きやすい所（推測）。`--python-exit-code 1` を付けて例外で止まるようにし、終了コードで失敗を拾う。
- **pip の bpy は Python 3.13 専用**: galleria の Windows 側の Python は 3.12（共通の決まり）なので合わない。uv で 3.13 の venv を作るか、Blender の本体（同梱の Python）を `-b -P` で使う。
- 費用は 0（GPL、登録不要、ネット接続不要）。会社の機械で作る発信物でも、作ったものは作者のもの、と公式が書く。

## 着手の仕方（未検証。galleria で確かめる）

- **何が表現できるようになるか / 効く型**: 写実的な 3D の場面（光線追跡の光・影・質感）、物理、立体の日本語タイトル。promo に一番効く。talk・embed では立体の図
- **機械**: **galleria Windows**（GPU 要。Cycles の OptiX は driver 575 以上。VRAM は簡単な場面で数 GB の見込み〈推測〉。ローカルの LLM・ComfyUI と同時に使わない〈[[exp-local-scene-studio]]〉）。入れるもの: Blender 5.2.3 LTS の Windows x64 の **portable の zip**（管理者権限の要るインストーラーを避ける。推測）、日本語フォントのファイル。費用 0、アカウント不要。GPL、出力は作者のもの
- **成熟度**: 5.2 LTS（2026-07-14）、5.2.3。3 か月ごとに版が出る
- **最小の手順（Windows の PowerShell。Python の中身は推測を含む）**:
  ```powershell
  cd $HOME\video-tools-trial\blender
  $B = "$HOME\tools\blender-5.2.3-windows-x64\blender.exe"   # zip を展開した場所（推測）
  & $B --version
  & $B -b --factory-startup --python-exit-code 1 -P scene.py -- out\frame_ 1 90
  # scene.py（推測。API 名は 5.2 の docs で確かめる）:
  #   import bpy, sys
  #   out, s, e = sys.argv[sys.argv.index('--') + 1:]
  #   bpy.ops.wm.read_factory_settings(use_empty=True)
  #   sc = bpy.context.scene
  #   sc.render.engine = 'CYCLES'; sc.cycles.device = 'GPU'
  #   p = bpy.context.preferences.addons['cycles'].preferences
  #   p.compute_device_type = 'OPTIX'; p.get_devices(); [setattr(d, 'use', True) for d in p.devices]
  #   sc.render.resolution_x, sc.render.resolution_y, sc.render.fps = 1920, 1080, 30
  #   sc.render.image_settings.media_type = 'IMAGE'; sc.render.image_settings.file_format = 'PNG'   # 5.0 以後の順
  #   f = bpy.data.fonts.load(r'C:\Users\...\fonts\NotoSansJP-Bold.otf')
  #   bpy.ops.object.text_add(); t = bpy.context.object; t.data.body = '合意の地図'; t.data.font = f; t.data.extrude = 0.1
  #   （カメラ・光を足し、t.rotation_euler に keyframe_insert で 1 コマ目と 90 コマ目を打つ）
  #   sc.frame_start, sc.frame_end = int(s), int(e); sc.render.filepath = out
  #   bpy.ops.render.render(animation=True)
  ffmpeg -framerate 30 -i out\frame_%04d.png -c:v libx264 -pix_fmt yuv420p -crf 18 out.mp4
  ```
  EEVEE で試すときは `sc.render.engine = 'BLENDER_EEVEE'`（5.0 以後の名前）。WSL からは `/mnt/c/.../blender.exe` を呼べる（WSL の相互運用。パスは `wslpath -w` で Windows の形にする。推測）
- **動いたと言える確かめ方**: (1) `--version` が `Blender 5.2.3` を出す、(2) 描画のログに OptiX の装置名（"NVIDIA GeForce RTX 5080"）が出る（ログの書式は推測。出なければ `--cycles-device OPTIX` を `--` の後に足して比べる）、(3) `out\frame_0001.png`〜`frame_0090.png` の 90 枚、(4) 日本語が豆腐でない、(5) スクリプトに誤りを入れたとき終了コードが 1 になる（`$LASTEXITCODE`）、(6) 1 コマあたりの秒数を CPU（`--cycles-device CPU`）と比べる
- **所要の見込み（推測）**: 最小の場面で半日。見せられる質の場面は数日〜（モデリング・光・質感を詰める時間）

## Open Questions

- Windows の `blender.exe -b` で EEVEE が headless で正しく描けるか（iRender の「真っ黒なコマ」の主張は Linux の仮想化環境の話として書かれている）。5.2 の `gpu.init()` が要るのは何の場合か
- WSL の Linux 版 Blender で Cycles の OptiX が動くか（CUDA は WSL で使えるが、OptiX の記述は NVIDIA の WSL のガイドに無い）
- 組み込みの Bfont に日本語の字形があるか、足りない字形の扱い（豆腐か空白か）。.ttc（Windows の游ゴシックなど）を読めるか
- blender-mcp の既定の匿名テレメトリが会社の機械での利用に許されるか（西尾が決めること）。MCP で対話的に作るのと、`-b -P` のスクリプトで再現可能に作るのと、どちらが西尾の「時刻表とコードで全部回す」方式に合うか
- 作品の作者の申告（720 コマ約 15 分など）は場面の重さ・解像度・サンプル数が分からず、目安にならない
