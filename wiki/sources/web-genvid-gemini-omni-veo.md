---
type: source
summary: Google の動画生成（Gemini API の Gemini Omni 1.2 Flash と、Vertex AI 系の Veo 3.1）の 2026-11-09 時点の公式ドキュメント。Gemini API の Veo 3.1 Preview は 2026-10-22 に停止し、Omni が 3〜15 秒・最大 4K（1080p 以上は upscale）・音声つき・参照画像 6 枚・動画の編集と 30 秒までの延長を担う。公式は Omni の画面内の文字を「正しく読める」と書くが、検証済みではない
video_types: [promo, any]
url: https://ai.google.dev/gemini-api/docs/omni
author: Google（Gemini API / Google Cloud のドキュメント）
published: 2026-11-05（Gemini Omni 1.2 Flash GA。Veo 3.1 GA は 2025-11-17）
retrieved: 2026-11-09
sources:
  - https://ai.google.dev/gemini-api/docs/omni
  - https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash
  - https://ai.google.dev/gemini-api/docs/video
  - https://ai.google.dev/gemini-api/docs/changelog
  - https://ai.google.dev/gemini-api/docs/pricing
  - https://ai.google.dev/gemini-api/terms
  - https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate
  - https://cloud.google.com/vertex-ai/generative-ai/pricing
---

# Google の動画生成: Gemini Omni Flash と Veo 3.1（2026-11-09 時点）

## 何の文献か

Google の公式ドキュメント（製品ドキュメント・モデルカード・価格ページ・利用規約）。すべて 2026-11-09 に curl で取得し本文を読んだ。数値は以下すべて「2026-11-09 時点の公式ページによる」。Vertex AI 側の Veo 3.1 のモデルページは「Last updated 2026-11-07 UTC」。Gemini API 側のページには更新日の表示が無く、changelog の最新は 2026-11-05。

Google の消費者向けの Flow（と Gemini アプリ）の仕様・規約は読んでいない。

## 書いてあること

### 名前と時系列（changelog とモデルページより）

- 2025-10-15: Veo 3.1 と 3.1 Fast が Gemini API で public preview。延長、参照画像 3 枚まで、最初と最後のフレームの指定、尺 4・6・8 秒（changelog）
- 2025-11-17: Vertex AI 側で `veo-3.1-generate-001` と `veo-3.1-fast-generate-001` が GA（Veo 3.1 のモデルページ）
- 2026-01-13: Veo に 4K 出力（changelog）
- 2026-03-31: Veo 3.1 Lite Preview（changelog）。Vertex 側の `veo-3.1-lite-generate-001` は Preview、2026-04-02
- 2026-06-30: `gemini-omni-flash-preview` が public preview（3〜10 秒・720p）（changelog）
- 2026-08-27: `gemini-omni-1.1-flash` GA。延長、両端の補間、1080p と 4K は upscale で作る（changelog）
- **2026-10-22: Gemini API の Veo 3.1 Preview（標準・Fast・Lite）を停止**。移行先は Gemini Omni Flash か、Gemini Enterprise Agent Platform（Vertex AI の後継の名前）の GA の Veo 3.1（動画生成のページの警告）
- 2026-11-05: `gemini-omni-1.2-flash` GA。最長 15 秒、両端の補間と 1 回の延長は 3〜10 秒、延長で合計 30 秒まで、参照画像 6 枚、動画出力の価格を 30% 下げた（changelog）。`gemini-omni-1.1-flash` は 2026-12-03 から 1.2 へ自動で回される

つまり 2026-11 時点で「Gemini API で動画を作る」は Omni のことで、Veo 3.1 は Vertex（Gemini Enterprise Agent Platform）でだけ使える。

### Gemini Omni 1.2 Flash（Gemini API）

仕様（モデルカード・Omni のガイドより）:

| 項目 | 公式の記述 |
|---|---|
| 尺 | 3〜15 秒（整数秒、既定 10 秒）。両端の補間と 1 回の延長は 3〜10 秒、延長を重ねて合計 30 秒まで |
| 解像度・fps | 360p / 720p（既定）/ 1080p（upscale）/ 4K（upscale）、24 FPS |
| 縦横比 | 16:9 と 9:16 |
| 音声 | 「native audio」つきで出す。音楽はプロンプトで指定するとよい、と書く（"Prompting the audio" 節）。音声の入力・音声の参照は未対応、声の編集も未対応（Limitations） |
| 言語 | 英語は完全に対応、他の言語は「評価していない」（Technical details: "other languages have not been evaluated, so they may work but results can vary"） |
| ショット | 既定で「いくつかのショット」を作って物語を組もうとする。1 ショットにしたければ "No scene cuts" などと書く（Single scene 節）。秒数を指定した出来事・タイムコード記法（`[0-5s]`）も書ける |
| 参照画像 | 1 リクエスト 6 枚まで（1 キャラクター 3 枚 × 2 キャラクターまで）。人物・服装・物を揃えるため |
| 参照動画 | 新規生成でだけ使える。3〜10 秒の出力で 3 本まで、11〜15 秒の出力で 1 本まで、各 3 秒まで。参照動画の音声は無視される |
| 最初と最後のフレーム | 画像 2 枚で両端の補間。3〜10 秒 |
| 自分の動画の編集（video-to-video） | Files API でアップロードした 15 秒以下の動画を自然文で編集できる（"Edit your own videos"）。ただし **EEA・スイス・英国では、アップロードした動画の編集・延長はできない** |
| 延長 | 末尾にだけ足せる（先頭・途中は不可）。入力の最後の 10 秒を文脈に使う。「入力動画の最後の数フレームは、つなぎ目をなめらかにするため編集される」と書く（"Prompts for extending a video"） |
| 人物 | 「特定の認識できる人物を含む画像のアップロードと編集は未対応」。EEA・スイス・英国では未成年を含む画像も不可（Limitations） |

**文字の描画**について、Omni のガイドは "Text in videos" 節で「プロンプトで動画に文字を入れられ、Gemini Omni は正しく読める形で描く（"will render in a way that is correct and readable"）。背景に自然に文字が出るなら、何と書くかを決めておくとよい」と書いている。編集の例にも「看板の文字を "Omni Flash" に変える」がある。これは Google の主張で、正確さを測った数字（文字の誤り率など）はこのページに無い。

価格（pricing ページ、Gemini Omni 1.2 Flash、2026-11-09 取得）: 無料枠なし。入力 $1.50 / 1M tokens、動画出力 $12.00 / 1M tokens。720p は 1 秒 5,792 tokens で「およそ $0.07/秒（10 秒で約 $0.70、15 秒で約 $1.04）」、360p は $0.023/秒、1080p（upscale）は $0.104/秒、4K（upscale）は $0.209/秒、と注記に書いてある。有料枠の入出力は「製品の改善に使わない」（同じ表の "Used to improve our products: No"）。

### Veo 3.1（Gemini Enterprise Agent Platform = 旧 Vertex AI）

モデルページ（Last updated 2026-11-07）より:

- `veo-3.1-generate-001`: GA、2025-11-17 公開、退役は「2027-05-04 以降」。text-to-video、image-to-video、最初と最後のフレーム、延長、参照画像（asset images）、音声生成、**Content Credentials（C2PA）: Supported**
- 尺は 4・6・8 秒（参照画像からの生成は 8 秒だけ）。16:9 と 9:16。出力 720p / 1080p / 4K、24 FPS。1 プロンプトで最大 4 本。動画の入力は「Not supported」
- プロンプトの言語は English だけと書かれている。提供リージョンは `us-central1`
- 利用の形は Provisioned Throughput と Fixed quota で、**Pay-as-you-go は "Not supported"**（Fast・Lite も同じ表記）
- Lite（`veo-3.1-lite-generate-001`）は Preview、参照画像は未対応

価格（Vertex AI の生成 AI 価格ページ、2026-11-09 取得。単位は「/ 1 count」と書かれている。同じページの注記に「動画は秒単位で課金」とあり、Runway Dev が Veo 3.1（音声あり）を 40 credits = $0.40/秒で売っているのとも合うので、秒あたりと読んだ）:

| モデル | 音声あり | 音声なし |
|---|---|---|
| Veo 3.1 | 720p・1080p $0.40、4K $0.60 | 720p・1080p $0.20、4K $0.40 |
| Veo 3.1 Fast | 720p $0.10、1080p $0.12、4K $0.30 | 720p $0.08、1080p $0.10、4K $0.25 |
| Veo 3.1 Lite | 720p $0.05、1080p $0.08 | 720p $0.03、1080p $0.05 |

Veo 3.1 の画面内の文字について、読んだページに公式の記述はない。

### 規約（Gemini API Additional Terms の "Use of Generated Content"）

- 「Google は生成されたコンテンツの所有権を主張しない（"Google won't claim ownership over that content"）。同じか似たものを他の人にも生成しうる」
- 生成物の使用は利用者の責任で、法律に従う。商用を禁じる文言はこの節に無い
- 開示: Omni の生成物には**すべて SynthID の透かし**が入る（見えないが、プログラムで検出できる）（Omni のガイド "Technical details"）。Veo 3.1（Vertex）は C2PA 対応と書かれている（モデルページ）。利用者が「AI 生成」と表示する義務は、読んだ範囲には書かれていない（公式の記述なし）
- 入力・出力の両方に安全フィルタがかかり、地域で違う（Omni の Technical details）

## この wiki への含意

問い（まとめ役の訂正後）:「作品（ソフトウェア・研究・本・動画）の promo を作る最良の方法」に照らして。

1. **作品の中身（画面・実機・数値・文字）を正確に見せられるか**: Google は Omni について「文字を正しく読める形で描く」と書く唯一の会社だった（ByteDance と Runway は逆に失敗を認めている。[[web-genvid-seedance]]、[[web-genvid-sora-kling-runway]]）。ただし公式は測定を出しておらず、英語以外は「評価していない」。日本語の画面文字・日本語の台詞を正確に出す用途は、公式にも保証が無い。[[exp-qualia-h3-live2d-galleria]] で MiniMax H3 の一体生成が日本語の一部を壊したのと同じ所で詰まる可能性がある（未検証）。[[exp-local-scene-studio]] の「正確な文字・字幕・ロゴは生成後に合成する」は、Omni の主張とは食い違うが、日本語では今も安全側の手順
2. **実在の画面や素材を入れられるか**: Omni は 15 秒以下の自分の動画を編集できる（EEA・英国・スイスを除く）。画面録画を入れて「背景だけ変える」「光を変える」ような使い方は仕様上できる。ただし編集は生成モデルが描き直すので、**画面の画素がそのまま残る保証は書かれていない**。延長では「最後の数フレームを編集する」と明記している。[[exp-galleria-local-video-generation]] の実測（Wan2.2 の FLF2V で、終点は VAE 往復と h264 の床まで再現された）は「指定した端のフレームは保てるが、間はモデルが発明する」で、Omni の両端の補間にも同じ構図が当てはまると考えられる（Omni では未測定）
3. **費用**: 720p で約 $0.07/秒（10 秒 $0.70）。15 秒の promo の 1 案を作って捨てる費用としては小さい。Veo 3.1 は音声ありで $0.40/秒と約 6 倍で、しかも従量課金が無い（Provisioned Throughput か Fixed quota）。個人の試作には Omni の方が入りやすい
4. **規約**: 所有権は主張しない。SynthID が必ず入る。promo を X・YouTube に出すとき、各 SNS の AI 表示の決まりは別に要る（このページの範囲外）

[[exp-galleria-local-video-generation]] の「試していないもの」にある「Veo 3.1 は 48kHz の同期音声と台詞」（二次情報）は、2026-11 時点では Gemini API の Veo 3.1 Preview が停止しているので古い。Gemini API で同じことをするなら Omni になる。

grasp-nishio の決まり「動画ではモデル名を明示する」に従うなら、使ったのが `gemini-omni-1.2-flash` か `veo-3.1-generate-001` かを書く。1.1 は 12-03 から 1.2 に自動で回されるので、同じ ID でも中身が変わる点に注意。

## Open Questions

- Omni の「文字を正しく読める形で描く」は、日本語・小さな文字・UI の細かい表記でどこまで成り立つか。公式の測定は無い
- Omni の動画編集で、入力した画面録画の文字・数値がどれだけ保たれるか（画素が描き直されるのか、編集しない領域は保存されるのか）。公式に記述なし
- 日本（EEA 外）から使う場合、アップロード動画の編集は使えるはずだが、未確認
- Veo 3.1 の従量課金が Vertex で「Not supported」なのは、個人のプロジェクトで使えないことを意味するのか（Fixed quota の取り方）は確かめていない
- Flow・Gemini アプリ（消費者向け）での生成物の規約・透かし・尺は読んでいない
