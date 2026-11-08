---
type: source
summary: ByteDance の Seedance 2.5 / 2.0 系の 2026-11-09 時点の公式ドキュメント（BytePlus ModelArk の解説・プロンプトガイド・価格、ByteDance Seed の製品ページ、Dreamina の利用規約）。1 回 30 秒・参照素材 50 個・動画の編集と延長ができる一方、公式が画面の文字の綴り誤り・禁止しても出る字幕・実在の顔は直接入れられないことを自分で書いている
video_types: [promo, any]
url: https://docs.byteplus.com/en/docs/modelark/seedance-2-5
author: ByteDance（ByteDance Seed / BytePlus ModelArk / Dreamina）
published: 2026（Seedance 2.5 の公開日は公式ページに記述なし。model ID は dreamina-seedance-2-5-260628）
retrieved: 2026-11-09
sources:
  - https://seed.bytedance.com/en/seedance2_5
  - https://seed.bytedance.com/en/seedance2_0
  - https://docs.byteplus.com/en/docs/modelark/seedance-2-5
  - https://docs.byteplus.com/en/docs/modelark/seedance-2-5-prompt-guide
  - https://docs.byteplus.com/en/docs/modelark/seedance-portrait-asset-guide
  - https://docs.byteplus.com/en/docs/ModelArk/1544106
  - https://dreamina.capcut.com/clause/dreamina-terms-of-service?lang=en
  - https://dreamina.capcut.com/clause/dreamina-user-safety-guide
---

# ByteDance の Seedance 2.5 / 2.0（2026-11-09 時点）

## 何の文献か

ByteDance の公式ページ群。製品の説明は ByteDance Seed のサイト、API の仕様・価格は BytePlus ModelArk（ByteDance の法人向けクラウドの国際版）のドキュメント、消費者向けの規約は Dreamina（CapCut 系の生成サービス）の利用規約と安全ガイド。BytePlus のドキュメントは JavaScript で描くページだが、HTML に埋め込まれた本文（Markdown）を取り出して読んだ。BytePlus の各ページは 2026-11-07 に更新されている（埋め込みの `UpdatedTime`）。数値は以下すべて「2026-11-09 時点の公式ページによる」。

CapCut アプリ内の提供条件、BytePlus ModelArk の利用規約（法人契約）、中国本土の Volcengine 版は読んでいない。

## 書いてあること

### モデルの並び

ModelArk の Seedance 2.5 解説ページの表（Capabilities overview）より:

| モデル | model ID | 尺 | 解像度 | 参照素材の上限 |
|---|---|---|---|---|
| Seedance 2.5 | `dreamina-seedance-2-5-260628` | 4〜30 秒 | 480p・720p（8bit）、1080p（10bit、H.265） | 50（画像 30・動画 10・音声 10） |
| Seedance 2.0 | `dreamina-seedance-2-0-260128` | 4〜15 秒 | 480p・720p・1080p（8bit）、4K（10bit） | 15（画像 9・動画 3・音声 3） |
| Seedance 2.0 fast | `dreamina-seedance-2-0-fast-260128` | 4〜15 秒 | 480p・720p | 15 |
| Seedance 2.0 mini | `dreamina-seedance-2-0-mini-260615` | 4〜15 秒 | 480p・720p | 15 |

- 縦横比はどれも 21:9・16:9・4:3・1:1・3:4・9:16・adaptive。`duration: -1` でモデルに尺を選ばせられる
- 出力の fps は読んだ範囲に記述が無い（入力動画は 24〜60 FPS と書かれている）。2.5 は mp4 のほかに mov（H.264・yuv444p・PCM 音声）を出せる
- どのモデルも text-to-video、最初のフレーム、最初と最後のフレーム、画像・動画の参照、**動画の編集、動画の延長**、音声つき生成ができる（✓ の表）
- 2.5 だけ Draft mode（480p 固定で試作し、良ければ同じ内容を高解像度で作る）がある
- Seed の製品ページは 2.5 を「1 回で最長 30 秒、さらに 2 回延長できる」「white-model control と green-screen editing」と書いている
- 公開日: Seed のページにも ModelArk のページにも日付の記述は見つけられなかった。model ID の末尾（260128、260628）は日付の形をしているが、公開日だと公式が書いているわけではない。Runway Dev のモデル一覧では Seedance 2.0 が 2026-05-28、2.5 が 2026-08-07 に追加されている（[[web-genvid-sora-kling-runway]]）
- 旧モデルの `seedance-1-5-pro-251215` は **2026-11-11 に退役**（価格ページ）

### 音声と言語

- 音声と映像を一緒に生成する（Seed の 2.0 のページ: "unified multimodal audio-video joint generation architecture"）
- 2.5 は 11 言語に対応すると書く: 中国語・英語・スペイン語・インドネシア語・マレー語・タイ語・アラビア語・ポルトガル語・ベトナム語・**日本語**・韓国語（解説ページ "Native multilingual support"）
- プロンプトの書き方の決まり: `()` は音楽、`<>` は効果音、`{}` は台詞、`【】` は字幕（解説ページ "Prompt rules"）

### 公式が自分で書いている苦手なこと（プロンプトガイドの「典型的な問題」節）

ModelArk の Seedance 2.5 プロンプトガイドには、問題と対処が並んでいる。作品の中身を見せる用途に関わるものを原文から:

- **文字の綴り誤り**（"Text spelling errors"）:「動画内の文字は誤ることがある。英単語の文字が置き換わる・増える・抜ける。E が A や I になるのがよくある誤り。中国語も誤字が出る（"稳健" が "稳键" になる）」。対処は (1) 単語を 1 文字ずつ順に出させる、(2) **正確に出したい文字を画像にして参照素材として渡す**。実例: "DIHETAO" が "DIHERTAO" になった
- **禁止しても字幕が出る**（"Subtitles generated despite prompt constraints"）:「プロンプトで字幕を出すなと明示しても出ることがある。2.0 より大きく改善したが、まだ起きる」「現時点では完全には消せない」
- **"no BGM" でも BGM が出る**: 効果音を音楽として描くことがある。対処は music・BGM・score・melody などの語を列挙して禁じる
- **複雑な指示は不安定**: 参照と編集を 1 回に詰めると崩れる（例: 赤い軌跡の線が出た）。参照の段と編集の段に分けて複数回で作る
- **縦横比を変える編集は不安定**: 広がった画面を埋めるために絵を足し、元の映像や時間の並びと食い違う
- **編集すると約 0.33 秒短くなる**: 入力のフレーム数を 8n+1 にすると揃う（解説ページでは「最大 0.4 秒短い」とも）
- **指紋のような模様**: 高解像度の AI 生成画像を参照にすると、草や葉のような細かい所に指紋・靴跡のような模様が出る
- 絵コンテを参照に渡すなら 15 コマ以下、線画で、**絵コンテに文字を書き込まない**

プロンプトガイドの作例には、ゲームの UI 画像（@Image 6）を最後のショットで画面に滑り込ませる「キーフレーム参照」の例がある（"The UI interface from @Image 6 slides into the frame from the right"、"Text and UI must remain clear and stable"）。出力は動画ファイルなので見ていない（動画はダウンロードしない決まり）。UI がどれだけ正確に保たれたかは確かめていない。

### 実在の人物（顔）

- 「Seedance 2.5 と 2.0 系は、実在の人の顔を含む参照画像・動画の直接アップロードに対応しない」（解説ページ "Usage limits"、肖像のガイド冒頭）
- 代わりに 3 つの道: (1) プラットフォームの用意したデジタル人物、(2) 同じアカウントで過去 30 日に ModelArk の対象モデルが出した顔入りの出力（元のファイルのまま。再編集・圧縮・転送で信頼が外れることがある）、(3) **本人の実在人物確認と許諾を経て資産登録した素材**（`asset://<ID>` で渡す）
- 西尾が自分の顔を promo に出すなら (3) の手続きが要る、と読める（手続きの中身は読んでいない）

### 価格（ModelArk の価格ページ、2026-11-09 取得）

トークン単価（USD / 1M tokens、オンライン推論）:

| モデル | 動画入力なし 480p・720p | 1080p | 4K | 動画入力あり 480p・720p | 1080p |
|---|---|---|---|---|---|
| Seedance 2.5 | $10.70 | $11.7 | 未対応 | $6.40 | $7.0 |
| Seedance 2.0 | $7.0 | $7.7 | $4.0 | $4.3 | $4.7 |
| 2.0 fast | $5.6 | 未対応 | 未対応 | $3.3 | 未対応 |
| 2.0 mini | $3.5 | 未対応 | 未対応 | $2.1 | 未対応 |

- トークン数の目安 =（入力動画の秒数 ＋ 出力の秒数）× 幅 × 高さ × fps ÷ 1024。動画入力ありには最低トークン数がある。モデレーションなどで失敗した生成には課金しない
- 価格ページの計算例（16:9、5 秒、動画入力なし）: 2.5 は 480p $0.103/秒、720p $0.231/秒、1080p $0.569/秒。2.0 は 480p $0.07/秒、720p $0.15/秒、1080p $0.37/秒、4K $0.78/秒。2.0 mini は 720p $0.08/秒
- 2.5 で動画を入れて 5 秒を出すと、720p で $1.244（入力 2〜4 秒）〜$4.838（入力 30 秒）。入力した動画の長さも課金される
- 2.5 を有効にするには BytePlus の残高 USD 30 超などの条件がある（解説ページ冒頭）

### 規約と透かし

- **API（ModelArk）**: `watermark: true` で「AI 生成の結果であることを示す透かし」を右下に入れる。既定は false（解説ページ "Add a watermark"）。見えない透かし・C2PA について、読んだ ModelArk のページに記述は無い
- **Dreamina の利用規約**（Bytedance Pte. Ltd.、"Last updated: January 22, 2026"、英語版）:
  - 「サービスは一般に、私的で非商用の利用のために提供される（"generally provided for private, non-commercial use"）」
  - 「規約を守る限り、アップロードした入力と、それに応じて生成された出力は利用者が所有する」
  - ただし利用者は、ByteDance（と関連会社）**とプラットフォームの他の利用者**に、その入力・出力を「あらゆる目的で」使う永久・取消不能・無償・再許諾可能なライセンスを与える
  - 規約の冒頭の説明は「画像を生成する」サービスとして書かれていて、動画についての独自の条項は見当たらない
- **Dreamina の安全ガイド**: 画像をダウンロードして他の場所に出すと見える透かしが入り、透かしを残すよう勧める。さらに「見えない透かしとコンテンツの来歴メタデータ（content provenance metadata）」を加えると書く。C2PA という語は使っていない。政治家の画像は不可

## この wiki への含意

問い:「作品（ソフトウェア・研究・本・動画）の promo を作る最良の方法」。ByteDance は西尾が思いついた例で、適切かは分からない位置づけ（まとめ役の訂正）。

1. **作品の中身を正確に見せられるか**: 公式自身が「画面の文字は綴りを誤る」「字幕を禁じても出る」と書いている。対処として公式が勧めるのが「正確な文字は画像にして渡す」で、これは**文字をモデルに描かせず、正しい文字を外から与える**という点で [[exp-local-scene-studio]]・[[experience-lessons-2026-11]] の「生成モデルに文字を描かせず、字幕・ロゴは後から合成する」と同じ向き。ただし公式の手は「参照として渡す」で、生成の中で描き直されるので、後から重ねるより弱い（画素がそのまま残る保証は無い）
2. **実在の画面や素材を入れられるか**: 参照素材 50 個、最初と最後のフレーム、2〜30 秒の動画の参照・編集・延長と、入れ口は今回調べた中で一番広い。画面録画（顔なし）を参照・編集に入れることは仕様上できる。**顔が映る実機デモ・本人出演は、許諾済みの資産登録を経ないと入らない**
3. **費用**: 2.5 の 720p で約 $0.23/秒（5 秒 $1.16）、試作は Draft mode（480p、$0.10/秒）。動画を入れると入力の秒数も払う。Omni（720p 約 $0.07/秒、[[web-genvid-gemini-omni-veo]]）の約 3 倍
4. **規約**: API で作れば Dreamina の規約（非商用が原則、他の利用者にもライセンス）は直接はかからないはずだが、ModelArk の規約は読んでいないので未確認。Dreamina のアプリで作って promo に使うのは、「一般に私的・非商用」の文言と、他の利用者へのライセンスがあるので、作品の宣伝（商用に当たりうる）には向かない、と読める

[[exp-galleria-local-video-generation]] が二次情報として書いた「Seedance 1.5 Pro $0.0247/s〜」は、1.5 Pro が 2026-11-11 に退役するので、もう比較に使えない。

[[exp-qualia-h3-live2d-galleria]] の「知覚的整合性は生成が強く、記号的正確さ（文字・語・数値）は組み立て型が強い」という整理は、ByteDance の公式ガイドの問題一覧（綴り・字幕・BGM の取り違え）とよく合う。公式の問題一覧は、生成モデルが離散的な記号を誤るという同じ形を、メーカー自身が書いたもの。

## Open Questions

- 「正確な文字を画像で渡す」ことで、日本語の UI・数値がどこまで正しく出るか。公式は中国語と英語の例しか出していない
- 画面録画を「編集」に入れたとき、編集を頼まなかった領域（画面の文字）は保たれるのか描き直されるのか。公式に記述なし
- BytePlus ModelArk の利用規約（生成物の権利・商用・開示）は未読
- 見えない透かし・C2PA が API の出力にも入るのか（Dreamina は来歴メタデータを入れると書くが、ModelArk には記述なし）
- Seedance 2.5 の公開日（Seed の公式ページに日付が無い）
