---
type: source
summary: Google の BudouX（Apache-2.0、Python・JavaScript・Java、最新 0.10.3＝2026-11-06）は、日本語の文を文節（改行してよい切れ目）に分ける約 15KB の機械学習モデル。外部の形態素解析を使わず、AdaBoost で字と字の間ごとに「切るか」を判定する。Chrome 119 以降の CSS `word-break: auto-phrase`（lang="ja"）は BudouX の C++ 移植を使う。字幕・テロップの改行を「語の途中で切らない」ための部品になる
video_types: [any]
url: https://github.com/google/budoux
author: Google（BudouX）／Chrome 開発チーム（CSS の auto-phrase）
published: 2026-11-06（PyPI・npm の 0.10.3）／2023（Chrome 119 の auto-phrase）
retrieved: 2026-11-09
sources:
  - https://github.com/google/budoux（README.md、LICENSE）
  - https://pypi.org/project/budoux/（0.10.3、2026-11-06。0.10.1 が 2026-10-26、0.10.2 が 2026-10-29）
  - https://www.npmjs.com/package/budoux（0.10.3、2026-11-06）
  - https://developer.chrome.com/blog/css-i18n-features（word-break: auto-phrase）
---

# BudouX（日本語の文節で改行する）

## 何の文献か

- Google の GitHub の公開ソフト BudouX の README（公式ドキュメント）と、Chrome の開発者ブログの CSS の国際化機能の記事
- ライセンス: **Apache-2.0**（LICENSE）。版: Python・npm とも **0.10.3（2026-11-06）**。10 月末から 3 回出ていて、更新が続いている（2026-11-09 時点の PyPI・npm）。Python は 3.11 以上（PyPI の requires_python）

## 書いてあること

- 位置づけ: 「BudouX is the successor to Budou, the machine learning powered line break organizer tool.」「standalone」（Google Cloud Natural Language API のような外部の分かち書きに頼らない）、「small」（「around 15 KB including its machine learning model」）、「language-neutral」（学習データを与えれば他の言語も作れる）
- 学習済みのモデル: 日本語、簡体字中国語、繁体字中国語、タイ語。韓国語は空白で語を区切るので CSS の `word-break: keep-all` で足りる、と書く
- 仕組み: 「BudouX uses the AdaBoost algorithm to segment a sentence into phrases by considering the task as a binary classification problem to predict whether to break or not between all characters.」特徴は前後の字、Unicode のブロック、その組み合わせ。モデルは特徴と重みの JSON
- Python: `pip install budoux` → `parser = budoux.load_default_japanese_parser()` → `parser.parse('今日は天気です。')` が `['今日は', '天気です。']`
- HTML: `parser.translate_html_string(...)` が `<span style="word-break: keep-all; overflow-wrap: anywhere;">` で包み、文節の間にゼロ幅スペース（U+200B）を入れる。「BudouX doesn't sanitize any inputs.」（HTML の消毒はしない）
- CLI: `budoux 本日は晴天です。`（既定は日本語）、`-H` で HTML、`-l ja|zh-hans|zh-hant|th`、`-m` で自作モデル、`-d` で区切りの文字
- 自作モデル: 文節を「▁」（U+2581）で区切った学習文から `scripts/encode_data.py` → `train.py` → `build_model.py`
- JavaScript 版・Java 版もある。JavaScript 版は Web Components（`<budoux-ja>`）も持つ（README のリンク先。本文は読んでいない）

### Chrome の `word-break: auto-phrase`（開発者ブログ）

- 「From Chrome 119: Japanese phrase line breaking with `word-break: auto-phrase`.」`lang="ja"` が必須
- 「Currently, Chrome supports this feature only for Japanese, using the BudouX」（C++ への移植）
- 「The boundary detection is performed by a machine learning engine, and therefore it may not result in what you intend.」そのときは `<wbr>` かゼロ幅スペースで切れ目を足し、ゼロ幅接合子（`&zwj;`）で切れ目を消す

## この wiki への含意

- **字幕・テロップの改行が語の途中で切れる問題の部品**。西尾の経験では、機械用の区切り（小節・4 モーラ群）をそのまま画面に出すと「おんばさ｜らくしゃ」「だば さらなん」のように語の途中で切れた。そこで画面の区切りを意味単位で別に持つ設計にした（[[exp-sutra-sync-subtitles]]、[[exp-sutra-hype-editions]]）。経文・真言は人が区切りを決めるのが正しいが、**ナレーションの字幕・解説のテロップのような普通の日本語**なら、BudouX で文節に分けて 1 行の字数（Netflix の 13 字、[[web-type-netflix-timed-text-style-guide]]）に詰めるのが最初の一手になる
- **HTML で描く作り**（[[exp-html-capture-pipeline]]、HyperFrames・Remotion）なら、Chrome の `word-break: auto-phrase` を CSS に 1 行書くだけで同じ効果が出る（headless Chrome が 119 以降なら。推測）。Python で SRT / ASS を作る作り（[[web-check-subs-ffmpeg-libass-youtube-caption-files]]）なら、BudouX で区切ってから改行 `\N` を自分で入れる。libass の自動の折り返しは Unicode の改行規則で、日本語ではどの字の間でも切れる（同ページ）
- 経文・真言・固有名詞（「Opus 5.5」「Plurality」）は BudouX の学習データの外なので、切れ目を人が直す前提にする。Chrome のブログの `<wbr>` / ゼロ幅接合子の直し方がそのまま使える
- 型に依らない（any）。字幕を読ませる embed（流しっぱなし）と、X の無音再生の promo（[[exp-democracy-river-video]]）で特に効く

## 着手の仕方（未検証。galleria で確かめる）

- **何ができるようになるか**: 台本の文を、文節の切れ目だけで 1 行 N 字以内・2 行までの字幕の塊に自動で割る。表示の区切りの正本（screen-text）の下書きを機械で作れる。効く型: any
- **機械**: どこでも（galleria WSL、Mac）。GPU 不要
- **入れるもの**: `budoux` 0.10.3（Python 3.11 以上）。費用 0、アカウント不要、Apache-2.0
- **成熟度**: 2026-10〜11 に 3 回リリース。Chrome に組み込まれている

### 最小の手順

```bash
mkdir -p ~/video-tools-trial/budoux && cd ~/video-tools-trial/budoux
uv venv --python 3.12 && . .venv/bin/activate && uv pip install budoux==0.10.3
budoux 本日は晴天です。          # 「本日は」「晴天です。」が 2 行で出れば成功
cat > wrap_ja.py <<'EOF'
# 文節を 1 行 MAX 字以内に詰め、2 行で 1 枚の字幕にする（貪欲法。推測で組んだ手順）
import sys, budoux
MAX = int(sys.argv[2]) if len(sys.argv) > 2 else 13
p = budoux.load_default_japanese_parser()
for sent in open(sys.argv[1], encoding="utf-8").read().split("\n"):
    if not sent.strip(): continue
    lines, cur = [], ""
    for ph in p.parse(sent.strip()):
        if len(cur) + len(ph) <= MAX: cur += ph
        else:
            if cur: lines.append(cur)
            cur = ph            # 1 文節が MAX を超えるときはそのまま 1 行（人が直す）
    if cur: lines.append(cur)
    for i in range(0, len(lines), 2):
        print("\\N".join(lines[i:i+2]))   # ASS の改行。SRT なら "\n"
EOF
python3 wrap_ja.py script.txt 13 > cards.txt
```

- 13 字は Netflix の日本語字幕（横書き）の 1 行の上限（[[web-type-netflix-timed-text-style-guide]]）。焼き込みのテロップなら画面の幅と字の大きさで決める
- `len()` は字数で、Netflix の「半角は 0.5」の数え方ではない。半角を含む行は数え方を直す

### 動いたと言える確かめ方

- `budoux 本日は晴天です。` が「本日は」「晴天です。」の 2 行を出す
- `cards.txt` の各行（`\N` で割った各部分）が 13 字以内で、行末・行頭が文節の切れ目（「は」「を」の前で切れていない）。台本の文字をつなぎ直すと元の文と一致する（字が落ちていない）
- 人の目で 20 枚ほど見て、直したい切れ目の割合を数える（固有名詞・数字・英字の周りに偏るはず。推測）

### 所要の見込み（推測）

- 導入から最初の出力まで 15 分

## Open Questions

- BudouX の切れ目と、Netflix の「改行は句読点の後・接続詞の前」のような字幕の作法がどれだけ一致するか。文節の切れ目は「改行してよい所」で、「改行すべき所」ではない
- 1 枚の字幕にどこまで入れるか（文の途中で 2 枚に分けるときの切り方）は BudouX の外の問題。字幕の速さ（1 秒 4〜6 字。[[web-check-ja-toyokura-yamada-2017-subtitle-4-chars]]）と合わせて決める
- 経文・真言・漢文の読み下しに BudouX を当てたときの崩れ方（試していない）
- headless Chrome で `word-break: auto-phrase` が効くか（フォントや Chrome の版で変わるか）
