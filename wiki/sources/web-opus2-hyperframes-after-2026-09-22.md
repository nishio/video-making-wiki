---
type: source
summary: HyperFrames（HeyGen の OSS）の 2026-09-22 以後の公式の変化。リリースは 194 個（v0.8.6x〜v0.9.23）。エージェント向けの skill を 21 から 7 に減らし「強いコーディングエージェントは自分で計画・確認する。足りないのは非公開の事実」と理由を書いた。解説動画のガイド（「~60 秒」と書け、尺はナレーションが決める）、発表用デッキ（`present`、デッキは 1 本の MP4 に書き出せない）、文字起こし・音の読み取り・ラウドネスとダッキングが入った。Opus 5.5 に同じ依頼で Remotion と HyperFrames を 1 回ずつ使わせた比較も載せている
video_types: [talk, embed, promo]
url: https://github.com/heygen-com/hyperframes
author: HeyGen（HyperFrames チーム。公式の release notes・docs・PR）
published: 2026-09-22〜2026-11-08（v0.9.23）
retrieved: 2026-11-09
sources:
  - https://github.com/heygen-com/hyperframes/releases （2026-09-15 以後のリリースの本文を API で取得）
  - https://github.com/heygen-com/hyperframes/blob/main/docs/weekly-updates.mdx （Week of September 21 〜 October 26, 2026）
  - https://github.com/heygen-com/hyperframes/pull/5651 （skill を 21 → 7 に、2026-10-21 マージ）
  - https://github.com/heygen-com/hyperframes/blob/main/docs/guides/faceless-explainer.mdx （最終更新 2026-10-26）
  - https://github.com/heygen-com/hyperframes/blob/main/docs/guides/slideshow.mdx （最終更新 2026-10-26）
  - https://github.com/heygen-com/hyperframes/blob/main/docs/guides/voice-and-audio.mdx （最終更新 2026-11-02）
  - https://github.com/heygen-com/hyperframes/blob/main/docs/guides/hyperframes-vs-remotion.mdx （Opus 5.5 の比較は 2026-10-25 の commit 5353171 で追加）
  - https://github.com/heygen-com/hyperframes/blob/main/docs/guides/with-claude-code.mdx （2026-10-25 作成）
---

# HyperFrames の 2026-09-22 以後

基本（HTML＋シーク可能なアニメを 1 コマずつシークして撮る決定論的な描画、Docker でのフォント固定など）は [[web-timesnap-timecut-hyperframes-webcodecs]] にある。ここはその後に変わったことだけ。

## 何の文献か

- HeyGen（AI 動画の会社）の OSS の公式の release notes・週次のまとめ・docs・PR。一次資料だが作り手自身の説明で、Remotion との比較や品質の主張は自社に有利でありうる。HeyGen の有料のサービス（声のクローン、クラウド描画など）への導線を含む
- リリースの数: 2026-09-22 以後に 194 個（GitHub の releases の API 値。1 日に複数）。週次のまとめは docs の `weekly-updates.mdx`
- デスクトップアプリ（Studio app、会話するエージェントの名前は Framey）は 9 月末〜10 月に CLI との連携が入った。Product Hunt での公開（10-06 ごろ）は第三者の記事の記述で、公式の告知は読んでいない

## 書いてあること

### エージェント向けの skill を 21 → 7 に（PR #5651、2026-10-21 マージ）

- 公開する skill を 21 から 7（`hyperframes`、`hyperframes-cli`、`hyperframes-registry`、`media-use`、`figma`、`slideshow`、`remotion-to-hyperframes`）に減らし、「どの skill も、エージェントが推論できない知識を持ち、手順は持たない」。引退したのは 8 個の workflow skill（`product-launch-video`、`faceless-explainer`、`pr-to-video`、`general-video`、`motion-graphics`、`music-to-video`、`embedded-captions`、`talking-head-recut`）など
- 理由（原文）: "Strong coding agents plan, sequence and check their own work; what they lack are private facts." 同じ組み替えを Studio の側で行ったとき「ツールと CLI の正しさが 5% から 83% に上がった」と書く（内部の issue の参照で、詳細は非公開）
- 毎ターン読まれる説明は 10.9 KB → 2.2 KB、`hyperframes` の入口は 21.8 KB → 6.7 KB
- 端末のエージェントでの評価（PR に表）: `claude -p`、**Sonnet 5.5（medium）**、19 ケース×2 回、コマだけを見る Opus の盲検の審査。main と比べて「HyperFrames として正しい」74% → 82〜84%、「CLI と道具を正しく使った」13% → 34%（→ 「変えたところを snapshot せよ」の一文を足して 79%）、両方 11% → 71%、1 回あたり $0.117 → $0.089。審査の点は 6.86/6.94 → 7.11〜7.21 で、PR は「審査はコマしか見ず、回ごとに揺れる。同じ main の実行が 1 勝から 7 勝に変わった。ファイルとコマンドから採点した合格率のほうが安定した信号」と書く

### 解説動画（Explainer）のガイド（2026-11-09 時点、最終更新 10-26）

- 「段落ごとに場面を作らない。教える背骨を見つけ、脇道を除き、見る人に残す一つの考えの周りに並べる」「図は仕組みを見せ、グラフは主張を証明し、動きは何が変わるかを見せる」と書く
- 狙いの 4 型: 一つの考えを理解させる（役に立つ問いで始め、仕組みを一層ずつ見せる）／手順を追わせる（一つの舞台で、見る人が要る順に各段を見せる）／三点を覚えさせる／物語で学ばせる
- **尺はナレーションが決める**: 「"60 seconds" でなく "~60 seconds" と書く。台本があるとき実際の長さはナレーションが決める。正確な数字はエージェントに台本を削らせるか水増しさせる」「台本を渡すとき、組み替えてよいか一語も変えないかを言う」
- 「一つの場面に一つの考え（one idea per scene）が品質の最大のレバー」「一つの場面に詰め込むと動かす焦点が無くなり、文字の羅列に見える」
- 例の 16:9・約 30 秒の版について「YouTube やエンベッド向け」と書き、ナレーションが長さを決めたので「26 秒」になった、と添える
- 見直しの項目: 冒頭が問い・緊張・驚きを作るか／主な考えが 2 場面目までに明らかか／本文の各場面が一つの仕組み・段階・例・含意を進めるか／数と事実の主張が元と合うか／終わりが覚えてほしい一文で着地するか

### 発表用のデッキ（Presentation / slideshow）

- 「HyperFrames のプレゼンテーションは生きたまま。動画を再生する代わりに、デッキのようにクリックで進め、段階的な表示・分岐・話し手のノートを持つ」。`npx hyperframes present <dir>` で開き、P で発表者モード（ノート・次・タイマー）
- 「**誰も話さずに最初から最後まで流すなら、デッキでなく動画を作る。デッキはまだ 1 本の MP4 に書き出せない**」
- 警告: 「デッキに `hyperframes render` を使わない。失敗しない — デッキには親の root composition が無いので、最初のスライドだけを描いて黙って切り詰めた MP4 を書く。40 秒のデッキの 6 秒分が、何かが欠けたという警告無しに出てくる」
- 最終スライドの段階表示まで Next が効くようにする修正が 10-25（#6233）。slideshow の skill は 7 個に残った

### 声・文字起こし・音

- `hyperframes transcribe` に Parakeet（09-28、v0.8.82）、Whisper が英語と決めつけず言語を検出（10-06、v0.8.137）、`--to srt|vtt` で字幕ファイルを直接（10-10、v0.8.144）、英語以外の文字起こしが失敗していた件の修正（10-19、v0.8.177）、Whisper の CJK のトークンを別々の時刻つきの語として保つ（10-22、v0.8.186）
- TTS: ローカルの Kokoro（速度の指定を渡す）、Gemini TTS（09-24、v0.8.70）、HeyGen の声とクローン
- Studio が音の編集に: レベルメーター、ラウドネスの正規化と声の下でのダッキング、リミッターの報告（10-02、v0.8.108）
- `hyperframes audio --read`: 音楽の立ち上がり・効果音のピーク・間・音楽に対する声を読む（10-27、v0.8.208）。週次（10-12〜19）は「エージェントが、音が映画のどこに落ちるか（onset・peak・tail）、拍・BPM・セクションを測れる」と書く
- `check` が「切り抜きの後ろに隠れた字幕の語」を指摘（10-30、v0.8.220）
- ガイドの「Check the mix」: 「音ありで 1 回、無音で 1 回、見ずに聞くだけで 1 回」

### エージェントのための確認の道具

- `check --range`／`--components`、`snapshot --range`／`--composition` で、触った部分だけを確かめる。結果は作ったときの版に対応づけて保存（週次 10-12〜19）
- `@hyperframes/inspector`: 要素がどの HTML・CSS・GSAP のソースから来たか、アニメの予定を問い合わせる
- skill が「最終の描画の前に必ず Studio を開く」（10-04、v0.8.124）、絵コンテは「静止画の一枚の板」に統一し、人が「進めて」と言うまで映画を変えない（10-14、10-21）

### Opus 5.5 での Remotion との比較（docs、10-25 追加）

- 「Claude Code（Opus 5.5）に同じ一段落の依頼を 2 回渡した。1 回は Remotion の公式 agent skills だけ、1 回は HyperFrames のだけ。各 1 回、再試行なし、後から編集なし」。依頼は架空のノートアプリの 15 秒のローンチ動画（声なし）
- 結果の表: MP4 まで 12 分 30 秒と 11 分 50 秒、TypeScript 10 ファイル 1,037 行と HTML 4 ファイル 822 行、`node_modules` 約 950 MB と追加なし、音は無しと「音楽と効果音 5 つ」
- 「どちらも良い動画で、1 回の実行は品質について何も決めない」と自ら書き、「Remotion のほうが古く確立していて、テンプレート・解説・実績が多い」「フレーム番号の純関数というモデルは頭に入れやすい。HyperFrames は決まり（一時停止したタイムライン、壁時計なし、seed の無い乱数なし）を守らないと静かに壊れる」とも書く

## この wiki への含意

- **道具の側が「モデルが強くなった」前提で作り替えた**: 手順（workflow）を skill から外し、エージェントが知り得ない事実だけを渡す、という PR の理由は、[[exp-timeline-2026]] の「何が変わったか」の問い（モデルか道具か）への、道具の作り手自身の答え。ただし評価に使ったのは Sonnet 5.5 で、Opus 5.5 ではない。また手順の側（計画・批評ループ）を誰が持つべきかは、別の担当の主題
- **talk に効く変化**: 「尺はナレーションが決める（~60 秒）」「一場面一考え」「台本を一語も変えないか組み替えてよいかを言う」は、[[exp-democracy-river-video]] の英語版で 60 秒の台本が TTS で約 107 秒になり削って 87 秒にした経験と同じ問題を、ガイドで先回りしている。[[exp-qualia-video]] の「耳で分かる量まで台本を削る」とも同じ向き
- **embed に効く変化**: 公式のガイド自身が「誰も話さず最初から最後まで流すなら動画」「デッキは 1 本の MP4 にできない」と分けている。西尾の embed は流しっぱなし（[[embed]] の Updates）なので、HyperFrames でも作るのは動画（`render`）で、`present` のデッキではない。デッキに `render` を使うと最初のスライドだけの MP4 が警告なしに出る、は embed 用に書き出すときの落とし穴
- **聞けないモデルへの補助**: `audio --read`（音がどこに落ちるかを数値で）、字幕の隠れの検査、ラウドネスとダッキングは、[[web-opus2-opus-5-5-explainer-posts-on-x]] の作者たちが自前で組んだ機械検査を道具の側が持ち始めた形。それでもガイドは「音ありで 1 回、無音で 1 回、聞くだけで 1 回」と人の視聴を求めている（[[exp-qualia-video]] の教訓と一致）
- **CJK の文字起こし**: Whisper の CJK の語を分けて時刻を保つ修正は、日本語の字幕を語の単位で合わせるときに効く可能性がある（試していない）

## Open Questions

- skill の組み替えの「5% → 83%」は内部の issue の数字で、条件が公開されていない。公開された表は Sonnet 5.5 での 19 ケース×2 回
- 解説ガイドの見直し項目（数と事実が元と合うか等）は人に向けた項目で、エージェントが自動で確かめる仕組みは書かれていない
- Opus 5.5 での Remotion との比較は各 1 回の promo（15 秒・声なし）。talk（ナレーションあり・数分）で同じ比較をした記録は無い
- HyperFrames の版は 0.9 台で週に 20 個以上リリースされる。このページの記述は 2026-11-09 時点で、すぐ古くなる
