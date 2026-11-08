---
type: source
summary: Anthropic が 2026-10-08 に Team・Enterprise のベータで出した Claude Motion（Claude アプリの機能）の公式の説明。報告書・グラフ・製品の手順を、動画生成モデルを使わずコードで動かす短いアニメにし、語・数値・タイミングを個別に直して MP4 で書き出す。例は「全社集会の 30 秒の解説」「取締役会の資料のグラフに動き」「顧客向けの手順」で、流行のショーリールとは用途の置き方が違う
video_types: [talk, embed, promo]
url: https://support.claude.com/en/articles/17454997-get-started-with-claude-motion
author: Anthropic
published: 2026-10-08
retrieved: 2026-11-09
sources:
  - https://support.claude.com/en/articles/17454997-get-started-with-claude-motion （ヘルプセンター「Get started with Claude Motion」、ページの日付 2026-10-08。2026-11-09 時点の本文）
  - https://claude.com/resources/articles/dashboards-and-motion （「Build live dashboards and animate explainers with Claude」、2026-10-08、製品の更新の記事）
  - https://x.com/claudeai/status/2108271558170976743 （@claudeai の告知、2026-10-08 19:01 UTC。いいね 2,173・表示 405,453 を api.fxtwitter.com 経由で 2026-11-09 に取得）
---

# Anthropic「Claude Motion」（2026-10-08、ベータ）

## 何の文献か

- Anthropic の公式の製品説明（ヘルプセンターの記事と製品の更新の記事、X の告知）。**製品の宣伝を兼ねる**。使い方と仕様の説明で、効果の測定は無い
- 2026-11-09 時点の公式ページによる。ヘルプの記事に表示された日付は 2026-10-08。プランや提供範囲は変わりうる
- Opus 5.5 公開（2026-09-22）の 16 日後。Claude Code の利用者が skill とハーネスで作っていた「コードで描く動画」（[[web-opus-hculap-skill-motion-graphic]] など）を、Claude アプリの中の機能として出したもの、と位置づけられる（この wiki の見方。Anthropic は流行との関係を書いていない）

## 書いてあること

### 何をするか（ヘルプの記事「How Claude Motion works」）

- アニメは「Motion テンプレートから作る artifact」。Claude が依頼からコードを書き、その中の**文字・グラフ・図形・画像を動かし、短い動画のように再生**する
- **動画生成モデルを使わない**ので、写実的な映像や人物は作らない。コードなので「一語、一つの数値、タイミングなど一か所を変えても、残りはそのまま」
- 書き出しは「Export」から MP4。作ったものは Artifacts のタブに残り、初めは本人だけに見え、「Share」で共有する
- 使用量はプランの上限に数える。長い・複雑なアニメは普通のメッセージより多く使う
- 提供: Team と Enterprise のベータ。Team は既定で有効、Enterprise は既定で無効で管理者が「Organization settings > Artifacts」で有効にする

### 何に使う想定か

- ヘルプの記事の冒頭: "an explainer for an all-hands, an animated chart for a board deck, or a product walkthrough for customer onboarding"
- 依頼の例: 「この四半期報告を全社集会向けの 30 秒の解説に」「料金プランの比較を、営業キックオフ向けに動かして」「新規顧客向けにセットアップの手順の短い説明を」
- 製品記事: 「動きで伝えたほうが伝わる考えは、たいてい静的なスライドがもう 1 枚増えるだけで終わる」。Claude Motion は「自分の仕事を説明するために作られている」。さらに先へ進めたいときは Adobe・Descript・HeyGen・Higgsfield・invideo・Luma AI・Runway で開ける（Canva・Captions は近日）、と書いている

### よくするための助言（ヘルプの記事「Tips for better results」）

- **誰が見るか、どこで流すか、だいたいの長さ**を言う
- 使ってほしい報告書・データ・画像を添付し、自分の中身から作らせる
- 直しはチャットで「2 つ目の場面を遅く」「Q3 の数字を 18% に」のように頼むか、エディタで直接直す

## この wiki への含意

- **公式の例は talk と embed に寄っている**: 流行の作品群は広告・ローンチのモーショングラフィックスが中心だった（athemeroy の分類で広告・ローンチの 71.6% がモーショングラフィックス／UI、[[web-opus-athemeroy-awesome-opus-5-5-videos]]）。Anthropic の例は「全社集会の解説」（talk に近い）、「取締役会の資料のグラフ」（プレゼンに埋め込む、embed）、「顧客向けの手順」。西尾の embed（プレゼンの中で流しっぱなしにする特定概念の解説、[[three-video-types]]）に、公式の用途の置き方が一番近い
- **助言の「誰が・どこで・どれくらい」は、西尾の経験の「型を決めたのは流す場所だった」と同じ軸**（[[three-video-types]]、[[exp-gyazo-resumption-video]]）。流行の一行プロンプトはこの 3 つを言わない（[[web-opus-stephanlivera-showreel-prompt]]）
- **「自分の中身から作らせる」は、skill 群の「本物の素材だけ」「捏造しない」と同じ向き**（[[web-opus-howseen-claude-motion-design]]、[[web-opus-hculap-skill-motion-graphic]]）。西尾の発信の「画面の主張 → 一次ソース」（[[exp-html-capture-pipeline]]）とも同じ
- **公式の説明に、自分のフレームを見て直す批評ループの記述は無い**。直しは人がチャットかエディタでやる形で書かれている。Claude Code の skill 群がハーネスの中に置いた「コンタクトシートで自己採点」は、この製品の説明には出てこない（中で何をしているかは書かれていない）。西尾の経験の「人の評価が要る」は、この製品では最初から人が直す前提になっている
- 西尾の方式（Mac の Claude Code で canvas を描き headless Chrome で撮る、[[exp-html-capture-pipeline]]）と、「コードで描き、一か所を直すと残りはそのまま」という性質は同じ。西尾の方式は Claude アプリの機能ではなく、Claude Code で一から組んだもの

## Open Questions

- Claude Motion の中で、Claude が自分の描いたコマを見て直す段があるかは公式の説明に無い
- 「プレゼンに埋め込む」用途で、音（ナレーション・BGM）を扱うかは書かれていない。例はどれも音に触れていない。西尾の embed は流しっぱなしの前提で、動画の側の音をどうするかが未解決（[[three-video-types]] の Updates）
- 尺の上限、fps、解像度は公式の説明に無い（2026-11-09 時点）
