---
type: concept
summary: 西尾の問い「作品のプロモーション的な動画を作る上での最良の方法は何か」について、丸ごと生成・コードで描く・人が実物を撮って編集する・その組み合わせを、目的・流す場所・正確さ・手間と費用・権利と開示で比べたページ。作品紹介の場の多くが「実際の画面・実物を使え」を規約にしていて、丸ごと生成は作品の中身を見せる部分に使う根拠が無い。暫定の答えは「実物の収録を正本に、コードで描く文字と図を重ね、生成は中身を見せないカットに限る」
video_types: [promo]
sources:
  - web-promo2-*.md（8 ページ）
  - web-genvid-*.md（3 ページ）
  - web-genvid2-*.md（5 ページ）
  - web-opus-howseen-claude-motion-design.md
  - exp-gyazo-resumption-video.md
  - exp-thinklet-reading-demo-video.md
  - exp-galleria-local-video-generation.md
---

# 作品のプロモーション的な動画

西尾の問い（2026-11-09）: 「作品のプロモーション的な動画を作る上での最良の方法を調べて」。最初の指示の「bytedanceなど」は西尾が思いついた例で、適切かどうかは分からない位置づけ。「作品」は西尾が作ったもの（ソフトウェア・研究・本・動画）で、**作品の中身（画面・実機・数値）を正確に見せる必要がある**。SNS 一般の promo は [[promo]]。

## 比べた方法

| 方法 | 作品の中身を正確に見せる | 手間・費用 | 権利・開示 | 文献・経験 |
|---|---|---|---|---|
| 丸ごと生成（ホスト型: Gemini Omni・Veo、Seedance、Kling、Runway） | 根拠が無い。画面の文字はどの社も保証せず測定値も出していない。ByteDance は綴りの誤りを認め、Runway は文字の生成を失敗の主な原因に挙げる。Google は Omni が文字を描けると主張するが英語以外は「評価していない」 | 15 秒 1 案で約 $1（Omni）〜 $6（Veo 3.1）。費用より選別の人手が効く | 透かしは Google が SynthID を必ず入れ、Kling は C2PA。Kling は会員でないと商用不可・表示義務、Dreamina は「一般に非商用」。Sora は 2026-09-24 に API も終了 | [[web-genvid-gemini-omni-veo]]、[[web-genvid-seedance]]、[[web-genvid-sora-kling-runway]] |
| 丸ごと生成（ローカル: Wan・LTX・HunyuanVideo・MiniMax H3） | 同上 | 16GB に公式で収まるのは HunyuanVideo 1.5（14GB）だけ。galleria の実測では Wan2.2 A14B fp8 が 15.8GB で回った | H3 は公開の場に出す内容に機械生成の目立つ開示を求める。LTX は年間売上 1,000 万ドル以上で有料 | [[web-genvid2-wan-ltx-hunyuanvideo-minimax-h3]]、[[exp-galleria-local-video-generation]] |
| コードで描く（この wiki の経験の方式） | 文字・数値・図は正確に描ける。ただし作品の画面は「描き直した図」になり、実物ではない | 1 本 1 日以内で数版（経験）。費用はほぼ 0 | 図形と文字だけなら権利の確認が要らない | [[exp-html-capture-pipeline]]、[[after-opus55]] |
| 人が実物を撮って編集する（画面収録・実機） | 実物そのもの | 撮影と編集の手間。THINKLET は約 36 分の編集（時刻から推定） | 実在の人・個人情報の映り込みに注意 | [[exp-thinklet-reading-demo-video]] |
| 実物をコードで動かして撮る（VHS・shot-scraper） | 実物そのもの。台本どおりに作品を動かして撮り、CI で撮り直せる | 台本を書く手間。作品が変わったら自動で撮り直し | 同上 | [[web-promo2-vhs-shot-scraper-demos-as-code]] |

## 作品紹介の場の規約と作法

- **「実際の画面・実物を使え」が規約になっている場が多い**。Apple の審査ガイドライン 2.3.4（2026-10-16 版）は「previews may only use video screen captures of the app itself」。Kickstarter は試作品のデモは現状を映し、存在しない機能を CGI や特殊効果で見せない。Google Play は推奨として「8 割以上を実際の体験に」「最初の 10 秒で実際の体験」（[[web-promo2-apple-app-previews-google-play-video]]、[[web-promo2-kickstarter-producthunt-launch-video]]）
- Steam は最初のトレーラーをゲームプレイに、HUD も見せる。マイクロトレーラーは最初の動画から自動で 6 秒切り出す。生成 AI の開示は「プレイヤーが消費する中身」が対象で、宣伝素材とゲームの一致を約束させている（[[web-promo2-steamworks-trailers]]）
- 学会（UIST 2026・CHI 2026）は **30 秒の video preview（広める）と査読用の video figure（理解させる）を別の動画にしている**。字幕ファイルは必須（焼き込みでなく .srt）（[[web-promo2-uist-chi-video-guides]]）
- 基本形は **実物の収録＋重ねる文字＋ナレーション**（Apple・UIST・CHI）。描き直すより実物を絞る（ズームより元の解像度、マウスを無駄に動かさない、何が起きるかを先に言う）（同）
- ゲームのトレーラーの編集者 Derek Lieu は、ロゴでなくゲームプレイで始める、仕組みを理解する時間を与える、文字とゲーム画面を同じショットに重ねない、作品にしかない hook を見せる、と書く。「the trailer cannot fabricate a design feature which doesn't exist in the game (not ethically, at least)」（[[web-promo2-derek-lieu-game-trailers]]）
- **時間と因果を偽らない**。Google の Gemini の Hands-on 動画は説明欄に「遅延を短縮、出力を短縮」と注記したが批判された。Nikola の動画は自走できない試作車を坂で転がしたもの、と SEC の訴状は主張している（訴状は SEC の主張で裁判所の認定ではない）（[[web-promo2-gemini-nikola-staged-demos]]）。howseen の skill も「画面で捏造しない」「例示のデータには Example data と出す」を決まりにしている（[[web-opus-howseen-claude-motion-design]]）
- **動画の効果の数字は弱い**。Kickstarter の動画の有無はオッズ比 4.3 で成功と結びつくが、準備の度合いの信号として使った観察研究で、出来は測っていない（Mollick 2014）。Kickstarter・Product Hunt とも「凝らなくてよい（DIY、Loom）」と書く。本のトレーラーはジャンルの印象を変えたが、「読みたい」の伸びは紹介文と同じだった（188 人、1 冊）（[[web-promo2-kickstarter-producthunt-launch-video]]、[[web-promo2-schafer-hock-hartmann-2013-book-trailers]]）

## 丸ごと生成について分かったこと（この比較に要る範囲）

- 画面の文字とレイアウト: T2VTextBench（2025）でアプリ・Web の UI の模擬は最高でも 0.50（0〜1）。要素が複数あるデザインの画面で、文字の完全一致は Sora-2 で 67%、Veo-3.1 で 42%（正解の描画は 94%）。静止しているはずの要素まで動かす（[[web-genvid2-t2vtextbench-design-video-eval]]）。測られたのは 2025〜2026 年前半のモデル
- 「丸ごと生成」の作品も、実際は大量に生成して人が選び直していた。Air Head は素材と完成の比が 300:1、Toys"R"Us は数百のショットを二十数個に絞り VFX と人の作曲を足した（[[web-genvid2-sora-air-head-toysrus]]）
- AI 生成の広告の評価は割れている。NIQ（2024）は「多くが見抜かれ、退屈でわかりにくい」、System1（2025）は Coca-Cola の AI 版に最高の 5.9 星。NIQ は「生成モデルは学習データにあるブランドの既存の表象を引き出す」と書く（[[web-genvid2-niq-system1-ai-generated-ads]]）。学習データに表象の無い新しい作品には、Coca-Cola の型の成功は当てはまりにくい（担当の推論、未検証）
- Vidmento（Adobe、CHI 2026）の参加者は「実在の対象は 100% 正しくないと不誠実に感じる。町や森の確立ショットなら余裕がある」と言い、生成の clip は撮った映像の補助（B-roll・確立ショット）として使われた（[[web-genvid2-vidmento-chi2026]]）

## 暫定の答え

目的と流す場所で答えが変わる。ただし作品の中身を見せる部分については、どの文献も同じ向きを指している。

1. **作品の中身（画面・実機・数値）は実物から取る**。ソフトウェアなら画面収録か、VHS・shot-scraper のように台本で実物を動かして撮る。規約（Apple・Kickstarter）・実務（Derek Lieu）・誤解の事例（Gemini・Nikola）が揃ってこの向き
2. **文字・図・数値の強調はコードで描いて重ねる**。この wiki の経験の方式が一番効く所。生成モデルに文字を描かせない（ByteDance・Runway の公式の記述、T2VTextBench と一致）
3. **丸ごと生成は中身を見せないカットに限る**（雰囲気・つなぎ・確立ショット）。使ったら開示する（H3 のライセンス、Steam、Kickstarter の AI 方針）
4. **広める版と理解させる版を分ける**（学会の preview と video figure）。Gyazo の 47 秒版に西尾が言った「Jevの凄さのアピール重視で技術の詳細を伝えるには適切ではない」（[[origin-2026-11-09]] の Updates）は、一本で両方を兼ねようとした問題として読める
5. 凝る前に出す。動画の出来が成果を上げるという根拠は弱い

## 経験と並べる

- THINKLET のデモ（[[exp-thinklet-reading-demo-video]]）は「実物の収録＋重ねる文字＋ナレーション」の形にほぼ当たり、待ち時間を偽らずナレーションで説明に変えた。Gemini の「遅延を短縮」の逆の例
- Gyazo の 47 秒版（[[exp-gyazo-resumption-video]]）は画面の画像をすべて図形で描き、0.5 秒ごとの叩き込み文字だった。Derek Lieu の「実際の動きで始め、理解する時間を与え、文字と画面を重ねない」と逆
- 経験の「生成モデルに文字を描かせず後で合成する」「keeper を静止画で選んでから動画にする」（[[experience-lessons-2026-11]]）は、ByteDance・Runway の公式の記述、Vidmento の工程（静止画 → 動画）と一致。Google の Omni の主張とは食い違う
- fps: Apple のプレビューの上限は 30fps。西尾の canvas の方式の書き出しは 60fps
- [[exp-galleria-local-video-generation]] に二次情報で載っているホスト型の価格は古い（Seedance 1.5 Pro は 2026-11-11 に退役、Veo 3.1 は Gemini API の Preview が停止、Kling の価格は公式（Runway 経由）では 720p 音声ありで $0.13/s）

## Open Questions

- 日本語の画面の文字を生成モデルで測ったベンチマークは見つからなかった
- 研究・本の promo（ソフトウェアのように画面が無い作品）では「実物」とは何か。本なら紙面、研究なら図と実験の映像か
- コードで描いた画面と生成のカットを混ぜる作り方の実務の一次資料は見つからなかった（ベンダーの宣伝記事だけ）
- 実画面を最初と最後のフレームに固定して間を生成させる使い方は、間でモデルが画面を発明する。作品紹介に使えるかは試していない
