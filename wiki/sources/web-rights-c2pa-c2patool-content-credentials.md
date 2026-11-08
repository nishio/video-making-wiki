---
type: source
summary: C2PA の Content Credentials を自分の動画に付ける道具 c2patool（v0.28.6、2026-11-06）の公式 README・docs と、信頼リスト・Adobe Content Authenticity・各配信先の読み方を並べたページ。c2patool は mp4・mov に署名付きの来歴を埋め込め、「AI で作った」は IPTC の digitalSourceType で書く。ただし同梱の試験用証明書は信頼リストに無く、Adobe の Web アプリは JPG・PNG だけ。YouTube・TikTok・LinkedIn は C2PA を読み、YouTube は C2PA 由来の AI ラベルを作り手が外せない
video_types: [any]
url: https://github.com/contentauth/c2patool
author: Content Authenticity Initiative（Adobe ほか）／C2PA
published: 2026-11-06（c2patool v0.28.6 のリリース）
retrieved: 2026-11-09
sources:
  - https://github.com/contentauth/c2patool （README、docs/usage.md、docs/signing.md、docs/manifest.md、Releases）
  - https://github.com/contentauth/c2pa-rs/blob/main/docs/supported-formats.md （対応形式）
  - https://github.com/contentauth/c2pa-rs （README: C2PA 仕様 2.4 の一部を実装、v2 claim が既定）
  - https://opensource.contentauthenticity.org/docs/conformance/trust-lists （信頼リスト、ITL の凍結）
  - https://helpx.adobe.com/creative-cloud/apps/adobe-content-authenticity/beta-overview.html （Adobe 側は Access Denied、Internet Archive の 2026 年の保存版で読んだ。ページの更新日 2025-09-02）
  - https://helpx.adobe.com/creative-cloud/apps/adobe-content-authenticity/troubleshoot/unable-to-apply-content-credentials.html （同、保存版）
  - https://support.google.com/youtube/answer/15447836?hl=en 、https://support.google.com/youtube/answer/14328491?hl=en （YouTube）
  - https://www.tiktok.com/transparency/en/supporting-responsible-transparent-ai-generated-content （TikTok）
  - https://www.linkedin.com/help/linkedin/answer/a6282984 （LinkedIn）
---

# C2PA の Content Credentials を動画に付ける（c2patool）

## 何の文献か

C2PA（Coalition for Content Provenance and Authenticity）の仕様を実装した公式の道具 c2patool の README と docs（GitHub、Apache-2.0）、Rust の SDK c2pa-rs の対応形式表、CAI のオープンソース文書の信頼リストのページ、Adobe Content Authenticity（Beta）のヘルプ、配信先の公式ヘルプ。仕様そのもの（C2PA Specification 2.x）は読んでいない。

版: c2patool は 2026-09 に c2pa-rs の monorepo から独立した repo に戻った（README「v0.27.15 以前は c2pa-rs の Releases に `c2patool-vX.Y.Z` で」）。独立後の最新は **v0.28.6（2026-11-06）**、v0.28.0 が 2026-09-22。月に数回出ている。c2pa-rs は c2pa-v0.91.11（2026-11-04）。

## 書いてあること

### c2patool でできること（README・usage.md）

- 読む: `c2patool <ファイル>` で C2PA マニフェストの要約 JSON を標準出力に。`--detailed`、`--info`、`--tree`、`--certs`（署名の証明書チェーンを PEM で）
- 付ける: `c2patool in.jpg -m manifest.json -o signed.jpg`。出力の拡張子は入力と同じでなければならず、形式の変換はしない。出力名が入力と同じなら上書き
- 意図（intent）の 3 種:
  - Create（`--create <source-type>`）: 新しい創作。IPTC の digitalSourceType を渡す。`digitalCapture`（カメラ・マイクの撮影）、`algorithmicMedia`（アルゴリズムだけで作った）、`trainedAlgorithmicMedia`（学習した AI モデルが作った）、`compositeWithTrainedAlgorithmicMedia`（AI 生成の要素を含む合成）など。`c2pa.created` の action を自動で足す
  - Edit（既定）: 元のファイルを親（parent ingredient）にして `c2pa.opened` を足す。`-p` で別の親を指定
  - Update（`--update`）: 署名済みのファイルへの非編集的な変更（再エンコード・形式変換）
- マニフェストは JSON で書く（`-m` でファイル、`-c` で文字列）。例は `c2pa.actions.v2` の assertion に `digitalSourceType` を入れる形
- `--sidecar` で外部の `.c2pa` ファイルに、`--remote` で URL 参照に
- `fragment` サブコマンドで断片化 BMFF（DASH）にも付けられる

### 対応形式（c2pa-rs の supported-formats.md）

- 動画: **mp4**（`video/mp4`。断片化 MP4 は Rust ライブラリのファイル操作のみ）、mov、avi。音声: wav、mp3、m4a、flac。画像: jpg、png、webp、avif、heic、gif、svg、tiff、dng。pdf も
- 拡張子で形式を決める（中身と食い違っても拡張子を優先）

### 署名（signing.md・manifest.md）

- C2PA の claim の署名は必須。CAWG の identity assertion（人・組織の身元）は任意
- 鍵と証明書を指定しないと、**バイナリに同梱の試験用の鍵と証明書**で署名し、警告を出す（「開発用」）
- 本番は subprocess signer（`--signer-path`）か遠隔の署名サービス。設定ファイル・マニフェスト・環境変数（`C2PA_SIGN_CERT`、`C2PA_PRIVATE_KEY`）に秘密鍵を置くのは試験用、と書いている
- アルゴリズムは es256（既定）など。タイムスタンプ局（`ta_url`）を指定できる（オンライン接続が要る）

### 信頼リスト（CAI の文書）

- 「適合する生成製品（conforming generator products）は、**C2PA trust list** に辿れる証明書を使わなければならない。適合する検証製品は C2PA trust list で署名の有効性を判断する」
- 暫定の信頼リスト（ITL）は **2026-01-01 に凍結**（追加・更新なし）
- C2PA の Verify ツール（verify.contentauthenticity.org）は今も ITL で判定し、知らない証明書なら「不明な出所」の表示を出す
- Adobe の Inspect も、証明書が C2PA trust list に辿れる場合にだけ署名者のアイコンを出す（manifest.md）

### Adobe Content Authenticity（Beta、ヘルプの更新日 2025-09-02）

- 無料の Web アプリで、自分の名前・SNS アカウント・生成 AI の学習の希望を付けて「署名」できる（デスクトップのみ）
- **対象は JPG と PNG だけ**（50 ファイルまで、1 つ 20MB まで、256×256 以上、RGB）。動画は対象外と書いている
- 付けた情報はファイルと Adobe の公開クラウドに保存され、「埋め込みメタデータ・見えない透かし・デジタル指紋で、**C2PA に対応しないプラットフォームがメタデータを消しても**つながりが残る」と書いている

### 配信先が C2PA をどう扱うか（各社の公式ヘルプ）

| 配信先 | 読むか | どう出るか | 出典 |
|---|---|---|---|
| YouTube | 読む | 「動画全体が AI 製」を示す C2PA 2.1 以上の安全な Content Credentials があれば「Made with AI」を引き継ぎ、作り手は外せない。撮影機器の C2PA で無編集なら「Captured with a camera」。署名者を「Info from」で出す | [[web-rights-youtube-genai-disclosure]] |
| TikTok | 読む・付ける | 一部の他プラットフォームの AIGC を C2PA で自動ラベル。TikTok 側でも C2PA を付け、ダウンロード後も残す作業中 | [[web-rights-tiktok-meta-aigc-labels]] |
| LinkedIn | 読む | 署名付きの画像・動画に C2PA のアイコン。クリックで AI の主張・アプリ・作成者・署名者・日時 | [[web-rights-x-linkedin-niconico-eu-ai-act]] |
| Meta | 画像の C2PA・IPTC を読む（2024 年の発表） | AI info。動画の C2PA を読むかの記述は見つからず | [[web-rights-tiktok-meta-aigc-labels]] |
| X | 公式の記述なし | 報道では「生成 AI ツールのメタデータ」で違反を検出 | [[web-rights-x-linkedin-niconico-eu-ai-act]] |
| ニコニコ | 記述なし | — | 同上 |

「剥がす」について: どの配信先も「再エンコードで C2PA を消す」とは書いていない。Adobe が「C2PA に対応しないプラットフォームがメタデータを消す」場合を前提にしている、という記述があるだけ。

## この wiki への含意

- **生成モデルの出力に付いてくる C2PA が先に効く**。Veo 3.1（Vertex）は C2PA 対応、Kling は C2PA に沿うメタデータ（[[web-genvid-gemini-omni-veo]]、[[web-genvid-sora-kling-runway]]）。その clip を西尾の ffmpeg の工程（[[exp-galleria-ffmpeg-measurement-and-delivery]]）で切り貼り・再エンコードしたとき、最終の mp4 に C2PA が残るかで、YouTube が外せないラベルを付けるかが変わる。残るかは文献に無いので、下の手順で確かめる
- **自分で付ける意味**: (1) 「AI で作った」を機械可読に自主開示する（grasp-nishio の「モデル名を明示する」を、画面の文字に加えてメタデータでも）、(2) LinkedIn で CR の印として見せる。ただし試験用の証明書では、Verify・Inspect で「不明な出所」になり、YouTube の「安全な」C2PA として扱われない可能性が高い（推測）。信頼リストに載る証明書を個人で得る道は、読んだ文書には書かれていない
- **コードで描く動画の digitalSourceType**: 西尾の方式（モデルが書いたコードを headless で描画、[[exp-html-capture-pipeline]]）は `algorithmicMedia`（アルゴリズムで作った）か `trainedAlgorithmicMedia`（AI モデルが作った）か、`compositeWithTrainedAlgorithmicMedia` か。IPTC の語彙の定義は読んでいないので決められない。YouTube の C2PA の自動ラベルは「動画全体が AI で作られた」と示す場合と書かれているので、どの値を選ぶかで YouTube のラベルが変わりうる。**どの値を名乗るかは西尾が決めること**
- talk・embed: スライドに埋め込む mp4 に付けても、PowerPoint・Keynote が C2PA を読む記述は無い（未確認）。embed には効きにくい

## 着手の仕方（未検証。galleria で確かめる）

- **表現できるようになること**: 書き出した mp4 に「誰が・どの道具で・AI をどう使って作ったか」の署名付き来歴を埋め込み、手元で検証する。生成 clip の C2PA が編集の工程で残るか消えるかを測る。効く型は promo（生成カットを含むもの）が主、talk も
- **機械**: galleria WSL（Linux 版のバイナリ）。Windows 版（`x86_64-pc-windows-msvc.zip`）もある。Mac は Homebrew（`brew install c2patool`）
- **入れるもの**: c2patool v0.28.6（2026-11-06）の Linux 版 `c2patool-v0.28.6-x86_64-unknown-linux-gnu.tar.gz`（ファイル名は README の命名規則 `c2patool-vx.y.z-x86_64-unknown-linux-gnu.tar.gz` からの推測。Releases の一覧で確かめる）。費用 0、アカウント不要（試験用の証明書で署名する範囲）。ライセンス Apache-2.0。**信頼リストに載る証明書は「要: 費用・手続き（未調査）」**
- **成熟度**: 2026-09 以降も月に数回のリリース。SDK は C2PA 仕様 2.4 の一部を実装、v2 claim が既定（c2pa-rs README）
- **最小の手順**（WSL。コマンドは README・usage.md の例を mp4 に置き換えたもの。mp4 で動くかは推測）:
  ```sh
  mkdir -p ~/video-tools-trial/c2pa && cd ~/video-tools-trial/c2pa
  # Releases から tar.gz を取得して展開（URL は Releases ページで確かめる）
  tar xzf c2patool-v0.28.6-x86_64-unknown-linux-gnu.tar.gz
  ./c2patool -V
  # 1) 西尾の既存の書き出し（例: 15 秒版の mp4）のコピーに、試験用証明書で Create の来歴を付ける
  cp /path/to/existing.mp4 in.mp4
  ./c2patool in.mp4 -c '{"assertions":[]}' --create compositeWithTrainedAlgorithmicMedia -o signed.mp4
  # 2) 読む
  ./c2patool signed.mp4 > signed.json
  ./c2patool signed.mp4 --info
  # 3) 再エンコードで残るか（推測: 残らない）
  ffmpeg -i signed.mp4 -c:v libx264 -c:a aac reenc.mp4
  ffmpeg -i signed.mp4 -c copy remux.mp4
  ./c2patool reenc.mp4 ; ./c2patool remux.mp4
  # 4) 生成モデルの clip（Veo・Kling の出力が手元にあれば）を読む
  ./c2patool generated_clip.mp4 > gen.json
  ```
- **動いたと言える確かめ方**:
  - `./c2patool -V` が `0.28.6` を含む版を出す
  - `signed.json` に `active_manifest` と `c2pa.actions.v2`（または `c2pa.actions`）の `c2pa.created` と、指定した `digitalSourceType` の URL（`.../compositeWithTrainedAlgorithmicMedia`）が出る。同時に試験用証明書の警告が出る（signing.md・manifest.md の記述どおりなら）
  - `signed.mp4` が元と同じく再生でき（`ffprobe` で長さ・解像度が元と一致）、ファイルが数十 KB 程度だけ大きい（推測）
  - 再エンコード・remux 後に `c2patool` が「マニフェストが無い」旨を返すか、検証エラーを返すかを記録する（どちらでも「工程で消える／壊れる」の実測になる）
- **所要の見込み**（推測）: 30〜60 分
- **西尾が決めること**: 自主的に C2PA を付けるか／付けるなら digitalSourceType をどれにするか／信頼リストの証明書に費用をかけるか／YouTube に限定公開で上げて自動ラベルの出方を確かめるか（外に出る行為）

## Open Questions

- ffmpeg の再エンコード・`-c copy` の remux で C2PA の box が残るか（文献なし。上の手順で実測する）
- 試験用証明書の C2PA を YouTube・LinkedIn・TikTok がどう扱うか（無視か、ラベルか、「不明な出所」か）
- 個人が C2PA trust list に辿れる証明書を得る方法と費用（CAI の文書には適合プログラムの話だけ）
- IPTC digitalSourceType の各値の正確な定義（cv.iptc.org の語彙ページは読んでいない）
- Premiere Pro・Media Encoder の書き出しで動画に C2PA を付ける機能（Adobe のヘルプが Access Denied で、保存版も無く読めなかった）
