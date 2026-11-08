---
type: source
summary: SIL Open Font License の公式 FAQ と、動画に使える無料の日本語フォント（Noto／源ノ、BIZ UD、M PLUS、LINE Seed JP、Zen・しっぽり・解星など、いずれも OFL）の配布元の記述を 2026-11-09 に読んだページ。OFL の FAQ は「video titling」を許される用途に挙げクレジットも不要とし、制約はフォント自体の再配布と改変だけ。明朝の太字は Noto Serif JP／Noto Serif CJK JP Black（900）、Zen Old Mincho Black（900）、しっぽり明朝・解星 特ミン ExtraBold（800）が OFL で使える
video_types: [promo, talk, embed]
url: https://openfontlicense.org/ofl-faq/
author: SIL International（OFL・FAQ）、Google Fonts（メタデータ）、Adobe・Google（Noto CJK／源ノ）
published: 2023（OFL-FAQ version 1.1-update7）、2024-07-30（Noto Serif CJK 2.003）
retrieved: 2026-11-09
sources:
  - https://openfontlicense.org/ofl-faq/
  - https://openfontlicense.org/open-font-license-official-text/
  - https://github.com/notofonts/noto-cjk
  - https://github.com/notofonts/noto-cjk/releases
  - https://github.com/adobe-fonts/source-han-serif
  - https://github.com/google/fonts/tree/main/ofl
---

# SIL OFL と無料の日本語フォント（明朝の太字を含む）

## 何の文献か

- SIL International の「OFL-FAQ」（version 1.1-update7、© 2007–2023）とライセンス本文。OFL の作り手自身による解釈の文書で、法的拘束力は本文にある
- Google Fonts のリポジトリ（github.com/google/fonts）の各ファミリーの `METADATA.pb`（ライセンス種別・ウェイト・追加日）と `OFL.txt`
- Noto CJK（notofonts/noto-cjk）と源ノ明朝（adobe-fonts/source-han-serif）の README・リリース・LICENSE

## 書いてあること

### OFL の FAQ（動画に関わる問い）

- 1.1「Can I use the fonts for a book or other print publication, to create logos or other graphics ...?」→「Yes. ... No additional license or permission is required ... Some examples of these uses are: logos, posters, business cards, stationery, **video titling**, signage ...」
- 1.1.1: 作った絵の著作者は自分で、ライセンスは及ばない。「It is only when you redistribute, bundle or modify the font itself that other conditions of the license have to be respected」
- 1.1.2「Is any kind of acknowledgement required?」→「No.」（作者は謝辞を喜ぶかもしれないが必須ではない）
- 1.12〜1.13: 文書への埋め込み（全体でもサブセットでも）は可で、文書のライセンスは変わらない
- 1.26「Can OFL fonts be used by AI-based design tools?」→「Yes, as long as the resulting work is not intended to be a font」
- Web フォントのサブセット化・変換は「Modified Versions」に当たることがあり、Reserved Font Name（RFN）がある場合は名前を変える必要がある（2 章）
- 源ノ明朝の LICENSE は「with Reserved Font Name 'Source'」。Noto CJK の LICENSE 冒頭には RFN の記載が無い（Serif/LICENSE の冒頭 5 行による）

### 無料の日本語フォント（すべて OFL。Google Fonts の METADATA.pb の記載）

| ファミリー | 系統 | ウェイト | 備考 |
|---|---|---|---|
| Noto Sans JP | ゴシック | 100〜900（可変） | 源ノ角ゴシックと同じ字形。Noto Sans CJK は 2.004 |
| Noto Serif JP | 明朝 | 200〜900（可変） | 源ノ明朝と同じ字形。Noto Serif CJK は 2.003（2024-07-30） |
| BIZ UDPGothic / BIZ UDPMincho | UD ゴシック／明朝 | 400・700 | 設計は Type Bank・モリサワ。Google Fonts 追加 2022-03-16。明朝は 700 まで |
| M PLUS 1 / M PLUS 2 | ゴシック | 100〜900（可変） | M PLUS 1p は 100〜900 の静的 7 段 |
| LINE Seed JP | ゴシック | 100・400・700・800 | LY Corporation・RixFont・Fontworks。Google Fonts 追加 2024-10-07 |
| Zen Kaku Gothic New | ゴシック | 300〜900 | |
| Zen Old Mincho | 明朝 | 400・500・600・700・**900** | 設計 大平善道 |
| Shippori Mincho（しっぽり明朝） | 明朝 | 400〜**800** | FONTDASU |
| Kaisei Tokumin（解星 特ミン） | 明朝 | 400・500・700・**800** | |
| Zen Antique | 明朝系 | 400 のみ | |

### Noto CJK と源ノの配布形式（noto-cjk の README・リリース、source-han-serif の README）

- Noto Serif CJK 2.003 のリリースには `07_NotoSerifCJKjp.zip`（日本語の地域サブセット）、`04_NotoSerifCJKOTC.zip`（全言語の OTC）、可変フォントなどがある
- **ファミリー名が配布形式で違う**: 日本語のサブセット OTF は「Noto Serif JP」（`NotoSerifJP-Black.otf` など 7 ウェイト）、全言語の OTF/OTC は「Noto Serif CJK JP」。Google Fonts でも「JP → Japanese」のように名前が違うと README が書く
- 源ノ明朝は 7 ウェイト（Super OTC は「all five languages and all seven weights in a single ... font resource that includes 35 fonts」）。Linux は「fontconfig and FreeType Version 2.5.0.1 or greater」で OTC に対応

## この wiki への含意

- **OFL の FAQ が動画のタイトル（video titling）を名指しで許し、クレジットも不要**。西尾の HTML で描いて撮る流れ（[[exp-html-capture-pipeline]]）は、フォントで描いた絵を動画にするので、これに当たる。注意が要るのは、フォントのファイルを作品の repo に入れて公開する時（再配布。OFL の本文を同梱する）と、サブセット化したものを置く時（Modified Version。源ノのように RFN があれば名前を変える）
- **明朝の太字**: 経文の制作で「極太明朝が Mac に無く（ヒラギノ明朝は W6 まで）Noto Serif CJK JP Black を入れた」（[[exp-sutra-songs-on-music]]）は、OFL の選択肢の中で最も太い 900 の一つ。同じ 900 には Zen Old Mincho Black がある。字形の印象は違う（Zen Old Mincho はオールドスタイル、Noto は現代の明朝）ので、アニメ OP 様式（[[exp-polis-magi-op]]）に近いのはどちらかは並べて見て決める（推測。字形の比較はこの調査でしていない）
- **欠字の検査**: [[exp-sutra-hype-editions]] はヒラギノ角ゴ W9 に「埵」「罣」が無く豆腐になった。OFL のフォントもファミリーごとに収録字が違う（Noto／源ノは Adobe-Japan1 の範囲が広い。Zen・しっぽりなどは未確認）。[[exp-sutra-songs-on-music]] の「使う字が全部 cmap にあることを先に照合」は、どのフォントでも先にやる
- UD 書体（BIZ UD）は読みやすさを狙った設計で、talk・embed の小さい字や字幕に候補。ただし明朝は 700 まで
- 細い明朝は小さく出すと読みにくい（[[web-type-apple-hig-wcag-text-size-contrast]]、[[web-layout-okabe-ito-cud-wcag-contrast]]）。900 の明朝はこの問題を和らげる側

## 着手の仕方（未検証。galleria で確かめる）

- **何が表現できるようになるか**: Mac と galleria・CyEC2 で同じ字形・同じ太さの日本語を、ライセンスを気にせず動画に焼き込む。明朝の 900 を含む。効く型: promo（極太明朝・極太ゴシックの見出し）、talk・embed（UD・Noto の本文）
- **機械**: どこでも（フォントのファイルを作品のフォルダに置き、HTML から `@font-face` で読む）。Linux 側の入れ方は [[web-means-font-fontconfig-noto-cjk-linux]]。費用 0、アカウント不要
- **利用条件の要点**: OFL。動画への焼き込みは自由、クレジット不要。repo に入れて公開するなら OFL.txt を同梱
- **成熟度**: Noto Serif CJK 2.003（2024-07-30）、Noto Sans CJK 2.004。Google Fonts の各ファミリーは google/fonts の main で更新が続く
- **最小の手順（WSL。URL はリリースページとリポジトリの一覧から。版を固定する）**:
  ```bash
  mkdir -p ~/video-tools-trial/fonts && cd ~/video-tools-trial/fonts
  curl -LO https://github.com/notofonts/noto-cjk/releases/download/Serif2.003/07_NotoSerifCJKjp.zip
  unzip 07_NotoSerifCJKjp.zip -d noto-serif-cjk-jp-2.003
  curl -L -o ZenOldMincho-Black.ttf https://github.com/google/fonts/raw/main/ofl/zenoldmincho/ZenOldMincho-Black.ttf
  curl -L -o ZenOldMincho-OFL.txt https://github.com/google/fonts/raw/main/ofl/zenoldmincho/OFL.txt
  sha256sum *.ttf noto-serif-cjk-jp-2.003/*/*.otf > SHA256SUMS   # 版を固定した証拠（推測: zip の中の階層は開けて確かめる）
  # 使う字が全部あるかの照合（fontTools を一時の venv に入れる）
  uv run --with fonttools python - <<'EOF'
  from fontTools.ttLib import TTFont
  import glob
  text = open("script.txt", encoding="utf-8").read()   # 動画に出す全文
  for path in ["ZenOldMincho-Black.ttf"] + glob.glob("noto-serif-cjk-jp-2.003/**/*Black*.otf", recursive=True):
      cmap = TTFont(path, fontNumber=0).getBestCmap()
      miss = sorted({c for c in text if not c.isspace() and ord(c) not in cmap})
      print(path, "missing:", "".join(miss) or "none")
  EOF
  ```
  HTML 側は `@font-face { font-family: "MinchoBlack"; src: url("fonts/ZenOldMincho-Black.ttf"); font-weight: 900; }` のようにファイルを直接指し、OS のフォント名に頼らない（推測。名前の違い・fontconfig の置き換えを避けるため）
- **動いたと言える確かめ方**: (1) 照合の出力が「missing: none」。(2) headless Chrome で `document.fonts.check('900 48px MinchoBlack', '般若波羅蜜多')` が true、`document.fonts.ready` の後に撮った 1 コマで字が豆腐でない。(3) 同じ HTML を Mac と galleria で 1 コマずつ撮り、ImageMagick の `compare -metric AE` で差のピクセル数を記録（0 にはならない見込み。アンチエイリアスの差。字の位置がずれていないことを目で見る）
- **所要の見込み（推測）**: 30 分〜1 時間

## Open Questions

- Zen Old Mincho・しっぽり明朝・解星 特ミンの収録字数（Adobe-Japan1 のどこまでか）は読んでいない。経文の「埵」「罣」のような字があるかは cmap で確かめる
- Noto Sans CJK の最新リリースの日付（2.004）はリリースページで確かめていない（Serif 2.003 は 2024-07-30）
- OFL の「video titling」は FAQ（解釈の文書）の記述で、本文は「Font Software」の使用を広く許す形。FAQ と本文の関係は FAQ 冒頭の通り本文が拘束力を持つ
