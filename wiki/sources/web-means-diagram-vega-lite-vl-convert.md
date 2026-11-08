---
type: source
summary: Vega-Lite（JSON で書く宣言的なグラフ）と、それをブラウザ無しで SVG/PNG/PDF にする vl-convert の公式資料、Vega の View API、Animated Vega-Lite の論文ページ。Vega-Lite 5.23.0（2024-12）で time エンコーディングと timer の選択による「コマ送りのアニメ」が入ったが、補間は含まない。動画にするなら「フレームごとの静的な仕様を vl-convert で PNG にする」か「View の signal を外から設定して runAsync → toCanvas」で、どちらも時刻を外から決められる
video_types: [embed, talk]
url: https://github.com/vega/vl-convert
author: Vega プロジェクト（UW Interactive Data Lab ほか）、Jonathan Zong ら（MIT Visualization Group）
published: Vega-Lite v6.5.0（2026-10-08）／vl-convert v1.9.0（2026-01-20、v2.0.0rc7 が 2026-09-14）
retrieved: 2026-11-09
sources:
  - https://github.com/vega/vl-convert/blob/main/README.md
  - https://github.com/vega/vl-convert/blob/main/docs/source/_topics/output-and-appearance/fonts.md
  - https://github.com/vega/vl-convert/releases/tag/v1.9.0
  - https://pypi.org/project/vl-convert-python/
  - https://github.com/vega/vega-lite/blob/main/CHANGELOG.md
  - https://github.com/vega/vega-lite/pull/8921
  - https://github.com/vega/vega/blob/main/docs/docs/api/view.md
  - https://vis.csail.mit.edu/pubs/animated-vega-lite/
---

# Vega-Lite と vl-convert: JSON のグラフをコマごとに書き出す

## 何の文献か

- vl-convert（BSD-3-Clause、star 約 170）の README と fonts の docs（main ブランチ、v2 系の記述）、v1.9.0 のリリースの添付ファイル一覧、PyPI。GitHub の最新リリースは v1.9.0（2026-01-20）、PyPI の安定版は 1.9.0.post1（2026-01-21）、v2 は rc7（2026-09-14）まで
- Vega-Lite（BSD-3-Clause、star 約 5,500）の CHANGELOG と PR #8921（time エンコーディング）。最新 v6.5.0（2026-10-08）
- Vega の View API の docs（signal・runAsync・toCanvas・toSVG）
- Animated Vega-Lite の論文ページ（Zong, Pollock, Wootton, Satyanarayan、IEEE TVCG／VIS、2023。抄録を読んだ。本文の PDF は読んでいない）
- すべて作り手・著者の一次資料

## 書いてあること

### vl-convert（README）

- 「Vega-Lite・Vega・SVG を、文書・アプリ・Web ページ用の形式に変換する」。Vega/Vega-Lite から SVG・PNG・JPEG・PDF・HTML・シーングラフなどを出す。「公式の Vega と Vega-Lite の JavaScript を埋め込んでいるので、ブラウザも Node.js も要らない」
- 形: Rust ライブラリ・CLI・HTTP サーバ・Python パッケージ。CLI は `cargo install vl-convert --locked`、`vl-convert vl2svg --input chart.vl.json --output chart.svg`。Python は `vlc.vegalite_to_png(spec, scale=2)`
- v1.9.0 のリリースには Linux・macOS・Windows の CLI の zip と Python の wheel が添付されている
- 描画の仕組み: 「埋め込みの V8 で公式の Vega-Lite コンパイラと Vega の描画器を動かす。PNG は Vega の canvas 描画器を vl-convert の Canvas 2D 実装で動かす。JPEG と PDF は SVG から作る」
- ネットワーク: 「同梱の Vega は通信を要さない」が、仕様が求めれば外のデータ・画像・Google Fonts を読む。相対パスのサンプルデータは vega-datasets の CDN を既定で使う。ローカルのファイルは既定で読めない
- フォント（fonts.md、v2 系の docs）: 「ホストに入っているフォントを読み、fallback として Liberation Sans を同梱する」。フォントのディレクトリを登録でき（CLI `--font-dir`、Python `vlc.register_font_directory`）、Google Fonts を指定でき、第一候補のフォントが無いときの動作を `fallback`（既定、黙って置き換え）・`warn`・`error` から選べる

### Vega-Lite の time エンコーディング（CHANGELOG・PR #8921）

- 5.23.0（2024-12-10）の Features に「time エンコーディングと timer パラメタによるフレームアニメーション（#8921）」
- PR #8921（Jonathan Zong、2024-11 にマージ）: 「Animated Vega-Lite の基本機能を実装。`time` エンコーディング、`timer` 点選択、`filter` 変換でフレームアニメを作れる」「補間・独自の述語・rescale・インタラクティブなスライダー・データ駆動の一時停止など、より複雑な機能は含まない」。経過時間は `anim_clock`、今の値は `anim_value`、定義域の中の位置は `t_index` という signal で持つ
- 公式 docs（site/docs の encoding・parameter）には time の記述を見つけられなかった

### Animated Vega-Lite（論文の抄録）

- 「アニメした可視化を時間で変わるデータの問い合わせとしてモデル化する」。静的な可視化と組むために「時間をエンコーディングのチャンネルとして」、インタラクションと組むために「時間をイベントの流れとして」表す。評価は例のギャラリーと、既存のアニメ文法の開発者 5 人へのインタビュー。インタビューは「言語設計の過程・対応する遷移の種類・キーフレームのモデル化」の 3 つのトレードオフを挙げた

### Vega の View API（view.md）

- `view.signal(name, value)`: signal を読む・書く。「すぐには更新しない。準備ができたら runAsync を呼ぶ」
- `view.toCanvas(scaleFactor)`: 描いたビットマップの canvas を Promise で返す（ブラウザなら HTML の canvas、Node なら node-canvas）。`toSVG` もある

## この wiki への含意

- **時刻を外から決める道が 2 つある**: (1) フレームごとに「その時刻のデータ（補間済み）を入れた静的な仕様」を作って vl-convert で PNG にする。ブラウザが要らず、Python から回せる（vl-convert の README の API から。未検証）。(2) ブラウザで Vega を動かし、自分の signal（例: `t`）を `view.signal('t', f/FPS).runAsync()` で進めて `toCanvas()` を取る。どちらも [[exp-html-capture-pipeline]] の「フレーム番号の純関数」に当たる。(1) は Chrome を使わないので、[[web-timesnap-timecut-hyperframes-webcodecs]] の「Chrome とフォントの版の差」を受けにくい
- **time エンコーディングはそのままでは使いにくい**: 時計（`anim_clock`）を Vega の timer が進め、補間も無い（PR の記述）。値が飛び飛びに切り替わるだけなので、流しっぱなしの embed で「変化を見せる」用途には補間を自分で書く必要がある（推測）
- **Python で回せる**: galleria の WSL には python3 と uv がある。Altair（Python から Vega-Lite を書く）の PNG 保存も vl-convert を使う（担当の知識。このページでは Altair の docs を読んでいない）。数値処理を Python で済ませる流れ（[[exp-html-capture-pipeline]] の BGM は numpy）と同じ言語で書ける
- **日本語**: 同梱は Liberation Sans だけで、日本語の字形は含まない（推測）。`missing_fonts="error"` にしておけば、日本語フォントが無いまま豆腐の PNG を作る事故を止められる（fonts.md の機能。v2 系の docs なので v1.9.0 にあるかは確かめる）

## 着手の仕方（未検証。galleria で確かめる）

- **増える表現**: 棒・折れ線・散布図が値の変化に沿って動く embed を、Python だけで（ブラウザ無しで）PNG 列にして ffmpeg でつなぐ
- **機械**: galleria WSL（python3・uv がある）。Windows の CLI zip・wheel もある。Mac でも可
- **入れるもの**: `vl-convert-python==1.9.0.post1`（安定版。v2 は rc）、日本語フォント（Noto Sans JP の TTF を `~/video-tools-trial/vl/fonts/` に）。費用 0、アカウント不要、BSD-3
- **成熟度**: v1 は 2026-01 から更新が無く、v2 が rc で 2026-09 まで出ている。docs（main）は v2 の記述なので、v1 で使えない引数があるかもしれない
- **最小の手順**（WSL）
  1. `mkdir -p ~/video-tools-trial/vl && cd $_ && uv init && uv add "vl-convert-python==1.9.0.post1"`
  2. `frames.py`（推測で書いた骨格）:
     ```python
     import vl_convert as vlc, math, pathlib
     vlc.register_font_directory(str(pathlib.Path('fonts').resolve()))
     FPS, DUR = 30, 20
     A, B = [12, 30, 8], [40, 18, 25]
     ease = lambda t: 0.5 - 0.5*math.cos(math.pi*min(1, max(0, t)))
     pathlib.Path('png').mkdir(exist_ok=True)
     for f in range(FPS*DUR):
         t = ease((f/FPS - 3) / 1.5)
         vals = [{"k": k, "v": a + (b-a)*t} for k, a, b in zip(["東", "西", "南"], A, B)]
         spec = {"width": 1600, "height": 800, "data": {"values": vals}, "mark": "bar",
                 "encoding": {"x": {"field": "k", "type": "nominal"},
                              "y": {"field": "v", "type": "quantitative", "scale": {"domain": [0, 50]}}},
                 "config": {"font": "Noto Sans JP"}}
         open(f"png/{f:05d}.png", "wb").write(vlc.vegalite_to_png(spec, scale=1))
     ```
  3. `uv run python frames.py && ffmpeg -framerate 30 -i png/%05d.png -c:v libx264 -pix_fmt yuv420p bars.mp4`
- **動いたと言える確かめ方**: (1) `png/` に 600 枚、(2) `png/00000.png` に「東・西・南」が出ていて豆腐でない、(3) 同じ f を 2 回出して sha256 が一致、(4) y の domain を固定したので、軸の目盛りの領域がコマ間で変わらない（差分画像）
- **所要の見込み（推測）**: 1〜2 時間。600 枚の書き出しの時間は測っていない

## Open Questions

- vl-convert 1.9.0 に同梱の Vega-Lite の版（time エンコーディングを含む 5.23 以降か）は確かめていない
- vl-convert 1.9.0 で `register_font_directory` と `missing_fonts` が使えるか（docs は v2 系）
- PNG 1 枚の書き出しの速さ。V8 の起動が 1 回で済むか（Python の 1 プロセスで回せば済むはず、推測）
- Animated Vega-Lite の論文本文（ギャラリーとインタビューの詳細）は読んでいない。抄録の「対応する遷移の種類」のトレードオフが補間の欠如を指すかは未確認
