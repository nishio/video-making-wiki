---
type: source
summary: Linux（galleria の WSL、CyEC2）で Mac と同じ日本語の絵を出すためのフォントの入れ方を、fontconfig の文書、Ubuntu のパッケージ一覧、ArchWiki の日本語・フォント設定の例、Noto CJK・源ノの README で 2026-11-09 に読んだページ。Ubuntu の fonts-noto-cjk は Regular と Bold だけで全ウェイトは -extra、版は Ubuntu の版で違う。ArchWiki は Chromium が fontconfig の言語の条件に従わないことがあると書く。版を固定するにはフォントのファイルを作品のフォルダに置いて直接指すのが確実
video_types: [any]
url: https://www.freedesktop.org/software/fontconfig/fontconfig-user.html
author: freedesktop.org（fontconfig）、Canonical（packages.ubuntu.com）、ArchWiki の寄稿者
published: unknown（fontconfig の文書）、2026-11-09 取得時点の各ページ
retrieved: 2026-11-09
sources:
  - https://www.freedesktop.org/software/fontconfig/fontconfig-user.html
  - https://packages.ubuntu.com/search?keywords=fonts-noto-cjk&searchon=names&suite=all&section=all
  - https://wiki.archlinux.org/title/Localization/Japanese
  - https://wiki.archlinux.org/title/Font_configuration/Examples
  - https://github.com/notofonts/noto-cjk
  - https://github.com/adobe-fonts/source-han-serif
---

# Linux で同じ日本語の絵を出す: fontconfig と Noto CJK

## 何の文献か

- fontconfig の利用者向け文書（fonts.conf の場所と書式）
- packages.ubuntu.com の検索結果（各 Ubuntu の版に入っているパッケージの版）
- ArchWiki「Localization/Japanese」「Font configuration/Examples」（コミュニティの wiki。公式の仕様ではない）
- Noto CJK・源ノ明朝の README（[[web-means-font-sil-ofl-noto-zen-mincho]] と同じ原典）

## 書いてあること

### Ubuntu のパッケージ（packages.ubuntu.com、2026-11-09）

| Ubuntu | fonts-noto-cjk の版 | 中身 |
|---|---|---|
| 22.04 LTS（jammy） | 1:20220127+repack1-1 | 「CJK regular and bold」 |
| 24.04 LTS（noble） | 1:20230817+repack1-3 | 同 |
| 26.04 LTS（resolute） | 1:20240730+repack1-1build1 | 同 |

- 全ウェイト（Black・ExtraLight など）は別パッケージ `fonts-noto-cjk-extra`（「CJK all weight」）
- → OS のパッケージで入れると、**Ubuntu の版によってフォントの版が違い、既定では Black が無い**

### fontconfig（fontconfig-user.html）

- 設定ファイルは `/etc/fonts/fonts.conf`、`/etc/fonts/conf.d`、利用者ごとに `$XDG_CONFIG_HOME/fontconfig/fonts.conf`（旧 `~/.fonts.conf`）
- `<dir prefix="xdg">` は `XDG_DATA_HOME` を前に付ける（利用者のフォントは慣例で `~/.local/share/fonts`）

### ArchWiki

- 日本語の表示には日本語（または中国語）のフォントが要る。推奨に源ノ角ゴシック・明朝の JP、Noto CJK、IPA フォントなど（Localization/Japanese）
- Font configuration/Examples の「Japanese」は、`lang` が `ja` の時に `Noto Sans CJK JP` を前に置く `fonts.conf` の例を載せる。同じページのアラビア語の節に「some applications like Chromium do not work with the language match test」とあり、`<alias><prefer>` で並べる方法を代わりに示す
- → 中国語用のグリフ（SC）が日本語の字に当たる「中華フォント」の問題は、fontconfig の言語の条件だけでは Chrome で防げない場合がある（推論）

## この wiki への含意

- [[exp-html-capture-pipeline]] は「Hiragino Sans など Mac のシステムフォント。別の機械で撮ると変わる」「galleria や CyEC2（Linux）で同じ絵が出るかは試していない」と書く。原因は 2 つに分けられる: (1) フォントが無い・違う（ヒラギノは Linux に無く、別のフォントに置き換わる）、(2) 同じフォントでも描画（ヒンティング・アンチエイリアス）が違う。(1) はフォントを作品に同梱して直接指せば消せる。(2) は残る（推測）
- 経文の制作で「Noto Serif CJK JP Black（OFL）を入れた」（[[exp-sutra-songs-on-music]]）は Mac の話。galleria で同じものを使うには apt の `fonts-noto-cjk` では足りず（Black が無い）、`-extra` か、リリースのファイルを直接置く
- 「OS にフォントを入れる」より「作品のフォルダにフォントを置いて `@font-face` で読む」方が、Mac・galleria・CyEC2 で同じフォントの同じ版が当たる。ファミリー名の違い（「Noto Serif JP」と「Noto Serif CJK JP」）や fontconfig の置き換えにも左右されない（推測。fontconfig を通らないため）
- HTML に `lang="ja"` を書くのは、Chrome が CJK の代替フォントを選ぶ時の手がかりになる（推測。ArchWiki の「Chromium は fontconfig の言語条件に従わないことがある」と合わせて、フォントを直接指すのが確実）
- [[exp-polis-magi-op]] の `document.fonts.ready` を待ってから撮る作り、[[exp-html-capture-pipeline]] の `document.fonts.load` を Promise にする作りは、`@font-face` でファイルを読む形と相性が良い（読み込みの完了を待てる）

## 着手の仕方（未検証。galleria で確かめる）

- **何が表現できるようになるか**: Mac で作った HTML の動画を galleria・CyEC2 でも同じ字で撮れる。描く機械を選ばなくなる。効く型: any
- **機械**: galleria WSL（distro 未確認）。CyEC2 では何も入れない決まりなので、CyEC2 での確認は西尾の判断が出るまでしない
- **入れるもの**: フォントのファイル（[[web-means-font-sil-ofl-noto-zen-mincho]] の手順で版を固定して取得）。OS のパッケージを使う場合は `fonts-noto-cjk-extra`（Ubuntu なら）。費用 0、アカウント不要
- **最小の手順（WSL）**:
  ```bash
  cat /etc/os-release | head -3          # distro と版を確かめる（galleria は未確認）
  fc-list :lang=ja family | sort -u | head -30   # 今ある日本語フォント
  fc-match "sans-serif:lang=ja"; fc-match "serif:lang=ja"   # 既定で何が当たるか
  # 方法 1（推奨）: 作品に同梱して直接指す。OS は触らない
  #   fonts/ に OTF/TTF と OFL.txt を置き、CSS で @font-face { src: url("fonts/NotoSerifJP-Black.otf") }
  # 方法 2: 利用者のフォントとして入れる（sudo 不要）
  mkdir -p ~/.local/share/fonts/video
  cp ~/video-tools-trial/fonts/noto-serif-cjk-jp-2.003/*/*.otf ~/.local/share/fonts/video/   # zip の中の階層は推測
  fc-cache -f ~/.local/share/fonts
  fc-list | grep -i "Noto Serif CJK JP\|Noto Serif JP" | head
  # 方法 3: パッケージ（Ubuntu の場合。sudo 要、版は OS 依存）
  # sudo apt install fonts-noto-cjk fonts-noto-cjk-extra
  ```
  比べるための試験ページ（推測で作る）: `test-fonts.html` に `lang="ja"`、明朝 900・ゴシック 700 で「般若波羅蜜多 埵 罣 0123 ABC」を 96px で描き、headless Chrome で 1 枚撮る（既存の capture のスクリプトの `stills` モードを使う）
- **動いたと言える確かめ方**: (1) `fc-match "Noto Serif CJK JP:weight=210"` が Black の OTF のパスを返す（weight 210 は fontconfig の Black。推測）、(2) 試験ページの PNG で、字が豆腐でなく、「直」「骨」など日中で字形が違う字が日本の字形になっている、(3) Mac で撮った同じページの PNG と並べ（ImageMagick の `montage`）、字の位置と太さが揃っている。差のピクセル数を `compare -metric AE` で記録する
- **所要の見込み（推測）**: 30 分

## Open Questions

- galleria の WSL の distro と版（Ubuntu なら 22.04 か 24.04 か）は未確認。apt で入る Noto CJK の版がそれで決まる
- Linux の Chrome と Mac の Chrome で、同じフォントファイルの描画差がどれくらいあるか（実測なし）。動画の圧縮の後で目に見える差かどうか
- WSL から Windows のフォント（`/mnt/c/Windows/Fonts`）を fontconfig に足す使い方の、ライセンス上の扱い（[[web-means-font-morisawa-fonts-bizplus-mojimo]] の Microsoft の FAQ は Windows のアプリでの使用を想定）
- 「直」「骨」で日中の字形を見分ける確かめ方は、JP のサブセットのフォントを直接指していれば不要になる。fontconfig 経由（方法 2・3）の時だけ要る
