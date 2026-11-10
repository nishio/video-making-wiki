---
type: source
summary: 西尾の自己紹介動画 4 本（15 秒モーショングラフィックス日・英、縦長ショート、写真を使った 1 分版）を 2026-09-25〜27 に作り YouTube に出した経験。写真なしの 15 秒版と、証拠写真を集めた 1 分版で、事実の確かめ方と権利の手間が大きく違った
video_types: [promo]
sources:
  - ~/nishio-showreel/README.md, 60s/README.md, 60s/assets/MANIFEST.md（冒頭の方針のみ参照）
  - ~/nishio-showreel/youtube/UPLOAD.md, youtube/UPLOAD_15s.md
  - ~/nishio-showreel/src/reel.html, reel_v.html, capture.mjs, audio.py, 60s/src/capture60.mjs, 60s/src/audio60.py
  - connecting-dot-design wiki/use-cases/profile-videos.md
  - grasp-nishio の Claude Code session 4754c834（2026-09-25〜27、西尾の発言）
  - (git 管理外の作業場。commit なし)
---

# 自己紹介の showreel（15 秒・ショート・1 分）

## 何を作ったか

| 版 | 尺・比率 | 中身 | 公開 |
|---|---|---|---|
| 15 秒（日本語） | 15 秒・1920×1080・60fps | 写真なし。1 つの点が 球 → 地図 → 島 → 流れ → 意見の地図 → 名前 と形を変えて経歴をたどる | YouTube（2026-09-27） |
| 15 秒（英語） | 同上 | 文字だけ英語にした `reel_en.html` | YouTube |
| 縦長ショート | 15 秒・1080×1920・60fps | 15 秒版のレイアウトし直し（`reel_v.html`） | YouTube ショート |
| 1 分版 | 60 秒・1920×1080・60fps | 書影・登壇写真・著名人との写真を使う。7 章（INTRO / NAME / ORIGIN / WRITING / COMMUNITY / PLURALITY / CONNECT） | YouTube（まず限定公開の方針） |

URL と出典リンクは `~/nishio-showreel/README.md` と `youtube/UPLOAD*.md`。作り方の共通部分は [[exp-html-capture-pipeline]]。

## 起点（西尾の依頼、そのまま）

- 15 秒版: 「make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out. Thema: 西尾泰和(NISHIO Hirokazu)の活動・功績」（2026-09-25）
- 1 分版: 「もう一つ別の動画を作って。1分間できちんと西尾はすごい人だと思わせるものにする。書影、Audrey Tangとの写真など箔がつくマテリアルを使いまくって。」（同日）
- YouTube 用: 「高画質版とショート動画と解説文章を作っといて、解説には出典リンクがあるといいよ」（2026-09-27）

## 作り方

### 15 秒版

- 粒子 2,400 個を球面上に均等に置き（黄金角）、7 色のクラスタに分ける。時刻表 `TL` で「seed → sphere → plane → kj → rocket → opinion → name」と配置を切り替える。各粒子に遅れ（stagger）を持たせ、イージング（expo・cubic・back）を場面ごとに変える（`src/reel.html`）。
- 最後の「西尾泰和」は、文字を別の canvas に描いて画素を拾い、粒子の行き先にする。
- 見た目の仕上げ: 粒子を加算合成で別 canvas に描き、ぼかし 14px と 4px を重ねて光らせる。床のグリッド、衝撃時のフラッシュと走査線、周辺減光、フィルムグレイン、頭と尻のフェード。
- 音: 120BPM。0〜2 秒のイントロ（whoosh・impact）→ 2〜12 秒のグルーヴ（Am–F–C–G、キック・クラップ・ハット・ベース・アルペジオ）→ 12 秒のリフト → 12.5 秒のフィナーレ（`src/audio.py`）。場面転換はすべて拍の頭。
- 縦長版は canvas と `W/H` を 1080×1920 にした別ファイル。中のレイアウトも調整した。

### 1 分版

- 素材の写真・書影を集め、`60s/assets/MANIFEST.md` に 1 点ずつ「見たままの説明・出典・日付・画面用キャプション（日英）・確信度 H/M/L・権利者」を書いてから使った。顔の照合には西尾の顔写真を基準にした。
- 画像を描くので `file://` では canvas が tainted になる。`capture60.mjs` に HTTP サーバーを入れて回避した。
- 章の切り替えは小節頭。BGM は場面の盛り上がりに合わせて `intensity` を変える関数（`60s/src/audio60.py` の `bar(s, k, intensity)`）。
- 撮影は約 10 分（`60s/README.md`）。

## うまくいったこと

- 15 秒日本語版を見た西尾の反応は「great, 英語版も作って。」（2026-09-25）。英語版・縦長版・1 分版へと広がった。
- 写真を使わない 15 秒版は「すべてプログラムで描画」なので権利の確認が要らず、そのまま公開できた（`youtube/UPLOAD_15s.md`）。
- 同じ事実の集合から、長さ（15 秒 / 1 分）・言語（日 / 英）・向き（横 / 縦）の違う 4 本ができた。設計 wiki 側ではこれを「同じ事実を別の解像度と形式で見せた」と記録している（connecting-dot-design `profile-videos.md`）。

## 詰まったこと・落とし穴

- **事実を画面に出す直前に一次ソースと突き合わせたら、元データの問題が 3 件出た**（数値が古い、役割語の裏が取れない、共著の扱いが食い違う）。動画では弱めるか外した。後で西尾に確認すると、2 件は元の記述が正しかった（`60s/README.md`「事実の扱い」）。教訓として設計 wiki は「一次ソースが見つからない役割語は、弱めて画面に出すか、本人に確認する。確認すれば元の記述が正しいこともある」と書いている。
- 英語の肩書きは AI の訳では決まらない。西尾が「主観研究員はResearch Directorかな。」「東工大は Visiting Associate Professor だな。」と直した（2026-09-25）。書名などは「制作時の仮訳・未確認」として README に分けて残した。
- 1 分版は写真の大半が第三者の撮影で、書影は出版社のもの。README は「一般公開する前には許諾を確認すること」とし、UPLOAD.md は「まず限定公開。写真の許諾が取れてから公開」とした。証拠になる写真ほど権利の手間が増える。
- 素材の一部は Gyazo の障害で取れず、`60s/assets/_pending_gyazo/` に候補と取得スクリプトを残した。
- 制作物を scratchpad に置いたら、西尾に「プロジェクトのマテリアルは ~/ に適切なプロジェクト名を書いて保存すべき」と言われ、`~/nishio-showreel/` に移した（2026-09-25）。

## 西尾のフィードバックと変えたこと

| 西尾の発言 | 変えたこと |
|---|---|
| 「great, 英語版も作って。主観研究員はResearch Directorかな。」 | `reel_en.html` を作り、肩書きを直した |
| 「東工大は Visiting Associate Professor だな。」 | 英語版の肩書きを直した |
| 「短いバージョンは？」「高画質版とショート動画と解説文章を作っといて、解説には出典リンクがあるといいよ」 | 縦長ショート版を作り、UPLOAD.md に出典リンクを全部並べた |

## 再利用できる部品

- `~/nishio-showreel/src/capture.mjs` — 後の 3 件がこれを元にした
- `~/nishio-showreel/60s/src/capture60.mjs` — 画像を描くとき用（HTTP サーバー入り）
- `~/nishio-showreel/src/audio.py` — 音源関数一式（kick / clap / hat / impact / whoosh / pad / saw）
- `~/nishio-showreel/youtube/UPLOAD.md` — 出典つき説明文の型
- 素材ごとの出典・確信度・権利者を書く MANIFEST の形（`60s/assets/MANIFEST.md` 冒頭）

## Open Questions

- 公開後の再生数や視聴維持率は見ていない。どの版が効いたかは分からない。
- 1 分版の写真の許諾がその後取れたかは、この repo の記録からは分からない。
- 1 分版に対する西尾の評価の発言は、session の記録には見当たらなかった。

## Updates

- 2026-11-09: 15 秒版の依頼文は、Opus 5.5 の公開（2026-09-22）直後に流行した「履歴書用のショーリール」の一行プロンプトの形（[[web-movez-opus-motion-design-course]]）。西尾「Opus5.5がすごいってなった」後の最初の制作。時系列は [[exp-timeline-2026]]

### 2026-11-10 公開 URL（Mac の作業場から）

- ~/nishio-showreel/README.md の「公開（YouTube, 2026-09-27）」の表より: 15 秒 日本語 https://youtu.be/l7P2YNQQEnU 、英語 https://youtu.be/xSXn2iGzys0 、縦長ショート https://youtube.com/shorts/8Ao3mrbEVMU 。事例紹介 [[nishio-works]] に載せた
- 1 分版の URL も README にあるが、写真の大半が第三者の撮影なので、この wiki には書かない
