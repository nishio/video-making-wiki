---
type: source
summary: Adobe Premiere（デスクトップ。26.x、2026）の AI 機能の公式ヘルプ（Internet Archive の保存版で読んだ）と、AI Assistant の公開ベータの公式告知（2026-06-23）。文字起こしで編集する Text-Based Editing（日本語の文字起こしに対応、つなぎ言葉・間の一括削除）、26.5 の Paper Edit、端末内で動く Media Intelligence の検索、Firefly の Generative Extend（映像 2 秒・音 10 秒、台詞は伸ばさない）、Generative Media Tool、そしてビン整理・文字起こし・マーカー・荒つなぎまでをする AI Assistant（英語に最適化、ベータ）。素材は学習に使わないと各ページが書く
video_types: [talk, promo, embed]
url: https://helpx.adobe.com/premiere/desktop/whats-new/whats-new.html
author: Adobe（Premiere のヘルプ、Adobe Community の公式告知、Adobe Generative AI User Guidelines）
published: What's new は Last updated 2026-09-09（26.5 まで）。AI Assistant の告知は 2026-06-23
retrieved: 2026-11-09
sources:
  - https://web.archive.org/web/20261013221647/https://helpx.adobe.com/premiere-pro/using/whats-new.html
  - https://web.archive.org/web/20250902160008/https://helpx.adobe.com/premiere/desktop/edit-projects/edit-video-using-text-based-editing/overview-of-text-based-editing.html
  - https://web.archive.org/web/20250824235458/https://helpx.adobe.com/premiere/desktop/edit-projects/edit-video-using-text-based-editing/detect-and-delete-pauses-in-transcripts.html
  - https://web.archive.org/web/20260910034539/https://helpx.adobe.com/premiere/desktop/edit-projects/edit-video-using-text-based-editing/create-a-sequence-with-paper-edit.html
  - https://web.archive.org/web/20260309071817/https://helpx.adobe.com/premiere/desktop/add-text-images/insert-captions/languages-supported-by-speech-to-text.html
  - https://web.archive.org/web/20250826161858/https://helpx.adobe.com/premiere/desktop/edit-projects/edit-with-generative-ai/generative-extend-overview.html
  - https://web.archive.org/web/20250831082608/https://helpx.adobe.com/premiere/desktop/edit-projects/edit-with-generative-ai/generative-extend-faq.html
  - https://web.archive.org/web/20260823171334/https://helpx.adobe.com/premiere/desktop/edit-projects/edit-with-generative-ai/generative-media-tool-faq.html
  - https://web.archive.org/web/20260414055814/https://helpx.adobe.com/premiere/desktop/edit-projects/edit-with-generative-ai/user-data-storage-for-model-output-feedback.html
  - https://web.archive.org/web/20260415002306/https://helpx.adobe.com/premiere/desktop/organize-media/file-organization/media-intelligence-and-search-panel.html
  - https://community.adobe.com/announcements-727/meet-your-new-assistant-editor-ai-assistant-in-premiere-pro-is-now-in-public-beta-1629317
  - https://web.archive.org/web/20261030031407/https://www.adobe.com/legal/licenses-terms/adobe-gen-ai-user-guidelines.html
  - https://www.gizmodo.jp/2023/10/premiere-pro-filler-word.html（日本語のつなぎ言葉の検出を試した記事。二次）
---

# Adobe Premiere — Text-Based Editing、Paper Edit、AI Assistant、Generative Extend

## 何の文献か

- Adobe の Premiere（2026 年のヘルプでは製品名が「Adobe Premiere」。版は 26.0〜26.5）のヘルプページ群と、Adobe Community の公式告知（Community Manager の投稿、2026-06-23）
- **helpx.adobe.com と adobe.com は CyEC2 からの取得が 403（Akamai の Access Denied）だった**。回避はせず、Internet Archive の保存版（各 URL の日付を sources に記載）で読んだ。保存版の日付より後の変更は反映されていない。Adobe の General Terms（素材の扱いの条文）と料金ページは保存版でも本文が JS で描画され読めなかった
- 2026-11-10〜12 に Adobe MAX 2026 がある（検索による。まだ開催前）。そこで発表される機能はこのページに入っていない

## 書いてあること

### Text-Based Editing（文字起こしで編集）

- 「When you select and rearrange the text, related video clips are automatically trimmed and adjusted in the timeline」。文字起こしは timecode を持ち、タイムラインと同期する（Overview、Last updated 2025-08-22）
- 主な機能: 取り込み時の自動文字起こし（Import の設定で Automatic transcription）、文字を選んで並べて荒つなぎ、「Detect and bulk-delete filler words like uh and umm」、特定の話者の発言をまとめて消す
- 「Detect and delete pauses」: Transcript パネルのフィルタで Text・Filler words・Pauses・Speakers を選び、Delete か Delete all
- 費用: 「Access the Text-Based Editing feature for free, included with your subscription」。FAQ は Speech to Text・Caption Translation・Enhance Speech を「assistive AI features」としてサブスクに含まれると書く
- 制限: 「Text-Based Editing doesn't support the captions workflow. Generate captions using your final edited sequence」
- **26.5（2026-09）の Paper Edit**: Text パネルで文字起こしの文・文の一部を複数選び、Preview で確かめ、「Create new sequence」で荒つなぎのシーケンスを作る（Last updated 2026-09-09）
- 26.3（2026-06）: 1 語ずつ出る字幕（single-word captions）。26.0 以前に Translate Captions

### 日本語の対応

- Speech to Text の対応言語に **Japanese** がある（デンマーク語・オランダ語・英語・英語(UK)・フランス語・ドイツ語・ヒンディー語・イタリア語・日本語・韓国語・ノルウェー語・ポルトガル語・ロシア語・中国語（簡体・繁体）・広東語・スペイン語・スウェーデン語。Languages supported by Speech-to-Text、Last updated 2025-08-22）。Text-Based Editing のページの言語表にも「日本語」がある（ただし見出しは「Access Text-Based Editing UI in the following languages」）
- **つなぎ言葉（フィラー）の検出が日本語で動くかを、公式ヘルプは明記していない**。GIZMODO Japan（2023-10-12、二次）は Premiere のベータ版で日本語の動画を文字起こしし、日本語版の名称は「つなぎ言葉の検出」、検出箇所が「[...]」で示され「すべて削除」で消えた、短い「えー」は最初は拾われなかった、と報告している
- AI Assistant は「will try to respond in whatever language you use, but it's currently optimized for English」（告知）

### AI Assistant（ベータ。エージェント）

- 2026-06 に公開ベータ。Premiere Pro (beta) の **Window > Assistant**。「it understands what you're trying to accomplish, breaks it down into steps, picks the right Premiere tools, and carries out the work on your behalf, inside your actual project」（告知）
- 今できること: ビンの作成・整理、クリップの移動・改名、色ラベル、**文字起こしと素材の準備**、スレートの検出とマーカー、**stringout・荒つなぎをタイムラインに置く**
- まだできないこと: 「versioning, cut-downs, and support for reference documents like scripts or production notes」（台本を渡しての編集は未対応）
- 制御: 「Always ask permission」と「Auto approve permission」の 2 モード。操作はすべて undo 履歴に入り、1 ターンぶんをまとめて戻す Undo がある。Reasoning を開くと、どう解釈し、どの道具・どの AI モデルを使ったかが見える
- ベータの注意: 毎日の無料クレジット（有料の生成クレジットとは別。GMT 0 時に回復）、英語に最適化、「Adobe explicitly recommends working with duplicates of your projects」、Firefly と提携先のモデルの混在
- 同じスレッドの利用者の報告（2026-08-15）: 433 枚の静止画からなる約 108 秒のシーケンスの作業で、1 応答あたりの tool-call の上限、日の上限、週の上限に当たり、1 日ほどで使えなくなった。別の利用者は「時間が半分になった」という知人の話を書いている（どちらも個人の報告）

### Media Intelligence と検索（26.0 前後）

- 映像を「multi-dimensional semantic」な空間に写して自然文で検索する。人物の識別はしない、OCR ではない、文字起こしと metadata は完全一致の検索（Media intelligence and Search panel、Last updated 2026-04-08）
- 「All analysis and search happen locally on your computer without using the internet」「your searches and media are not used to train Adobe's AI models」。解析は機械学習用のハードか GPU で、索引は `.prin`、取り込み時の解析は設定で切れる
- 26.0 以降、音（効果音など）を言葉で探す検索、似たショットの検索

### Generative Extend・Generative Media Tool（生成）

- Generative Extend（Firefly）: クリップの頭か尻に**映像は最大 2 秒、音は最大 10 秒**を足す。クラウドで生成し要ネット。**「Generative Extend cannot create or extend spoken dialog」**（台詞は伸ばさず、伸ばす間は無音にする）。音楽を含むクリップは対象外。出力は 30fps・8-bit・SDR に落ちる（26.5 で 360p〜4K・任意の縦横比・インターレースに拡大）。生成クレジットを使う「premium generative AI feature」。生成部分は「Revert to Original」で戻せる
- 「Your media is never used to train Adobe's AI model」（Overview）。出来の feedback を送ると、生成物と、選べば元素材の低解像度 3 秒が送られる（User data storage、2026-04-02）
- Generative Media Tool（26.5、ベータ）: タイムラインの中で映像と効果音を文から生成。映像は Firefly と提携モデル（Google Veo、Kling、Luma）を選べ、自分の素材から参照フレームを取れる。「Your prompts, media, and reference frames ... aren't used to train Adobe or partner AI models」。一部のモデルは個人プランだけで、法人プランは審査中（FAQ、2026-07-09）

### 生成 AI の利用条件（Adobe Generative AI User Guidelines、Last Updated 2026-05-15）

- 第三者の権利を侵す入力・出力の禁止。入力と出力は濫用防止のため自動・手動で見られることがある
- 「Quality may be reduced for languages not explicitly supported by Adobe」
- **6. Content Credentials**: 「Adobe may attach or publish Content Credentials for content created or modified with generative AI features ... You must not remove, alter, or disable any Content Credentials」
- 26.2（2026-04）から書き出し設定で Content Credentials（生成 AI の使用の情報を含む）を付けられる（What's new）
- 素材一般の扱い（Adobe General Terms の content の条項）は本文を読めなかった

### 費用

- 料金ページ（adobe.com/jp/products/premiere/plans.html）は 403、保存版も価格が JS で描画され読めなかった。検索で出た二次情報では、単体プランの年間契約・月払いが ¥3,280/月、月々契約が ¥4,980/月（第三者のブログ。公式で未確認）
- Text-Based Editing・Speech to Text・Media Intelligence はサブスクに含まれ、Generative Extend・Generative Media Tool は生成クレジットを使う（ヘルプ）

## この wiki への含意

- **西尾の唯一の手編集は Premiere 25.0 だった**（[[exp-thinklet-reading-demo-video]]）。同じ道具の中に、文字起こしで切る・つなぎ言葉を消す・Paper Edit で荒つなぎ・AI Assistant に整理と荒つなぎを頼む、が入っている。THINKLET の 52 秒は「実機の待ち 30 秒を説明に変える」という構成の判断が要の編集で、これは AI Assistant の「今できること」（整理・文字起こし・荒つなぎ）の外にある
- 日本語の文字起こしに公式に対応している点で、Descript（[[web-edit-text-descript-underlord]]）と違う。日本語の講演の録画を「文字を消すと切れる」編集にかけるなら、2026-11 時点の候補になる
- **Generative Extend は台詞を伸ばさない**。講演・解説の素材では、映像の尻を 2 秒伸ばしてトランジションや余韻に使う用途に限られる。[[exp-shortmovie-draft-generator]] で西尾が入れた「カットの終わりを 3 秒延ばす」は元素材を延ばす処理で、生成の延長とは別物
- AI Assistant が台本・制作メモをまだ受け取れない点は、台本を正本にするこの wiki の作り方（[[exp-sutra-sync-subtitles]]）と合わない。台本からの荒つなぎなら DaVinci Resolve の IntelliScript が近い（[[web-edit-text-davinci-resolve-intelliscript-studio]]）
- 生成を使うと Content Credentials が付きうる。YouTube の扱いは [[web-rights-c2pa-c2patool-content-credentials]]

## 何を AI に任せられるか／何が人に残るか

- **任せられる（公式）**: 文字起こし（日本語可）、文字の選択による荒つなぎ（Paper Edit）、フィラー・間・特定話者の一括削除、映像と音の意味検索（端末内）、字幕の生成・翻訳、映像の 2 秒・音の 10 秒の延長、生成カット、ビン整理・スレート・マーカー・荒つなぎ（AI Assistant、ベータ）
- **人に残る（公式）**: AI Assistant は「leaving the creative judgment exactly where it belongs, with the editor」（告知の利用者の言葉を Adobe が引用）、出力は「fully editable」、許可モードで 1 手ずつ確認できる。Generative AI User Guidelines は「use your judgment when reviewing and validating generated outputs」。台本に沿った編集・版の作り分け・短縮（cut-downs）は AI Assistant の範囲外と告知が書く
- 日本語のつなぎ言葉の検出は二次の記事（2023）でしか確かめられていない

## 着手の仕方（未検証。galleria で確かめる）

- **何が表現できるようになるか**: 日本語の講演・デモの録画を、文字起こしの上で切って荒つなぎし、つなぎ言葉と間を一括で消し、字幕を付ける。AI Assistant に素材の整理と荒つなぎを頼む。効く型: talk（講演の録画の短縮版）、promo（切り抜き）、embed（デモの短縮）
- **機械**: galleria Windows（RTX 5080。Media Intelligence は GPU を使うと書く）または Mac。西尾の Mac には Premiere 25.0 の実績がある（[[exp-thinklet-reading-demo-video]]）。AI Assistant は **Premiere Pro (beta)** アプリで、Creative Cloud デスクトップから入れる（告知）
- **入れるもの・費用・アカウント**: **要: Adobe アカウントと Premiere を含むプラン（西尾の Mac は契約がある可能性が高いが、galleria で使うかは西尾が決める）**。生成（Generative Extend・Generative Media Tool）は生成クレジットを使う。AI Assistant はベータ中は毎日の無料クレジット
- **成熟度**: Premiere 26.5（2026-09）。AI Assistant と Generative Media Tool はベータ
- **最小の手順（GUI。メニュー名はヘルプと告知から。細部は推測）**:
  1. 新規プロジェクト → Import 画面右上の Import settings で「Automatic transcription」を入れ、Language を Japanese にして、日本語の 3〜5 分の録画を取り込む
  2. Text-Based Editing のワークスペースで文字起こしを開く → Transcript パネルのフィルタ（…）で Filler words → 「Delete all」、次に Pauses → 「Delete all」
  3. Text パネルの Paper Edit アイコン → 残したい文を 3〜5 個選ぶ → Preview → Create new sequence
  4. （任意）Premiere Pro (beta) で Window > Assistant → 許可モードを「Always ask permission」→「この素材を話題ごとにビンに分け、話者の発言だけの stringout を作って」と頼む（作業はプロジェクトの複製で）
  5. 書き出し（File > Export > Media、H.264）
- **動いたと言える確かめ方**: 手順 1 で Text パネルに日本語の文字起こしが出る。手順 2 の後、シーケンスの尺が元より短くなり、[...] の表示が消える（短い「えー」は残りうる）。手順 3 で新しいシーケンスができ、尺が Paper Edit の「total selected duration」と一致する。手順 4 で History パネルに Assistant の操作が並び、Undo で一度に戻る。書き出しを ffprobe して duration を記録
- **所要の見込み（推測）**: 導入済みなら 1 時間。AI Assistant の試しは日の上限に当たりうる

## Open Questions

- 日本語でのつなぎ言葉の検出の精度と対象語（「えー」「あの」「えっと」「まあ」）。2023 のベータ版の記事しかない
- Adobe General Terms の素材の扱い（content の利用・学習）の条文を、2026-11 時点の版で読めていない。ヘルプの「学習に使わない」は機能ごとの記述
- AI Assistant の日本語での指示の出来。「optimized for English」の程度
- AI Assistant が使う提携モデルの出力について、Adobe は「you're responsible for determining whether they're appropriate」と書く。どの操作で提携モデルが使われるかは Reasoning を開かないと分からない
- MAX 2026（2026-11-10〜12）で AI Assistant の正式版や台本対応が出るか
