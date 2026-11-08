---
type: source
summary: 海外の無料の音素材 3 つ（Pixabay、YouTube オーディオライブラリ、Freesound）の利用条件を 2026-11-09 に読んだページ。Pixabay はクレジット不要・改変可で単体の再配布と機械学習目的の取得を禁止、YouTube オーディオライブラリは Content ID に当たらない代わりに YouTube の外での利用の条文は Studio の中にあり読めなかった、Freesound は音ごとに CC0／CC BY 4.0／CC BY-NC 4.0（旧 Sampling+）でクレジットの書式を FAQ が示す
video_types: [promo, talk, embed]
url: https://pixabay.com/service/license-summary/
author: Pixabay、Google（YouTube ヘルプ）、Freesound（Music Technology Group, Universitat Pompeu Fabra）
published: 2026-10-20（Pixabay Terms の Last updated）、unknown（YouTube ヘルプ・Freesound FAQ）
retrieved: 2026-11-09
sources:
  - https://pixabay.com/service/license-summary/
  - https://pixabay.com/service/terms/
  - https://support.google.com/youtube/answer/3376882
  - https://freesound.org/help/faq/
---

# Pixabay・YouTube オーディオライブラリ・Freesound の利用条件

## 何の文献か

各サービスの公式ページ。Pixabay は Cloudflare の確認画面で直接取れず、Internet Archive の 2026-11-01（License Summary）・2026-11-05（Terms）のスナップショットを読んだ。YouTube オーディオライブラリの個々の曲の利用条件は YouTube Studio の中（ログイン要）にあり、読めたのは公開のヘルプページだけ。

## 書いてあること

### Pixabay（Terms: Last updated 20 October, 2026）

- License Summary: 「Use Content for free」「Use Content without having to attribute the author」「Modify or adapt Content into new works」
- 禁止: 「You cannot sell or distribute Content ... on a Standalone basis」。Standalone は「no creative effort has been applied to the Content and it remains in substantially the same form」。Terms は、他の画像・動画・音・文・編集と組み合わせて新しい作品にするのは Standalone ではないと書く
- 認識できる商標・ロゴを含むものを商品・サービスに関連して商用に使うことの禁止、誤解を招く使い方の禁止
- Terms: 「certain Content (including CC0 Content) may be subject to additional intellectual property rights ... audio or video samples」。「We do not warrant that any consents or licenses have been obtained in relation to any Content」。申し立てがあれば直ちに使用をやめる義務（11. Infringement claims）
- AI: サービス上のデータを「machine learning purposes」で自動取得することを禁止。投稿者の内容は Pixabay が機械学習に使うことがあり、投稿者はオプトアウトできる。生成 AI で作った内容の投稿は条件付きで可（7B）。つまり Pixabay の音には AI 生成のものが混ざりうる

### YouTube オーディオライブラリ（ヘルプ「Use music and sound effects from the Audio Library」）

- 「Copyright-safe music and sound effects downloaded from the Audio Library won't be claimed by a rights holder through the Content ID system」
- 「If you're in the YouTube Partner Program, you can monetize videos with music and sound effects from the Audio Library」
- Creative Commons の曲は「you must credit the artist in your video's description」。帰属の文は Studio で「Copy」できる。標準ライセンスの曲は帰属不要（フィルタ「Attribution not required」）
- 使った動画には「Music in this Video」の欄が付く
- **YouTube の外（X・会場・スライド埋め込み）で使えるか**は、このヘルプに書かれていない。第三者のブログは「標準ライセンスの曲は YouTube の動画に限る」「CC BY の曲は外でも可」と書くが、一次資料ではない（担当の検索結果。原典未読）

### Freesound（FAQ）

- ライセンスは音ごとに 3 種: CC0、CC BY 4.0、CC BY-NC 4.0。旧 Freesound 1 の Sampling+ が残っており、Freesound の解釈は「BY-NC に加えて商業広告に使えない」
- クレジットの書式例:「This [video/...] uses these sounds from freesound: "sound1" by user1 ( http://freesound.org/s/soundID/ ) licensed under CCBYNC 4.0」。自分がダウンロードした音の一覧は attribution list のページで見られる
- YouTube の申し立て:「if an artist creates a song that contains all of, or even a snippet of, a "raw" sound effect from this site, and then the artist also submits their song to the YouTube Content ID ... if another person uses the same sound effect in a YouTube video, the ID scan will discover a match」。対処は異議申し立てで、Freesound の投稿日が相手の曲の公開日より前である証拠を出す。加工した音は当たりにくい、と書く
- AI の学習には音ごとの CC の条件を守れば可（BY は帰属、NC は商用の学習から除外）。生成モデルの学習には投稿者の意向による追加の制限がありうる

## この wiki への含意

- YouTube に出すだけの talk・promo なら、オーディオライブラリが一番事故が少ない（Content ID に当たらないと公式が書く）。ただし X・会場（embed）・Apple の App Preview など YouTube 以外にも同じ動画を出す西尾の使い方（[[exp-democracy-river-video]] は X と YouTube の両方）では、YouTube の外の条件を Studio で曲ごとに確かめる必要がある
- Freesound は音ごとにライセンスが違う。**CC BY-NC は収益化した動画・会社の発信物に使わない**。CC BY は概要欄に帰属を書く。台帳にライセンス種別を書く
- Pixabay の音は AI 生成のものが混ざりうるうえ、Pixabay は権利の保証をしないと明記する。Content ID の申し立てが来たら使用をやめる義務が利用者にある
- 効果音ラボ・OpenTracks（[[web-means-sound-soundeffect-lab-maoudamashii-opentracks]]）と同じく、「素材の URL・取得日・ライセンス種別」の台帳が、申し立ての時の唯一の根拠になる
- numpy で合成した音（[[exp-html-capture-pipeline]]）は台帳が要らない。素材集を混ぜると台帳の手間が増える。物音が要る時だけ素材集を使う、という使い分けが考えられる（推測）

## 着手の仕方（未検証。galleria で確かめる）

- **何が表現できるようになるか**: Content ID に当たらない BGM（オーディオライブラリ）と、実在の物音の大量の選択肢（Freesound・Pixabay）。効く型: talk・promo（YouTube）
- **機械**: どこでも（ブラウザ）。YouTube オーディオライブラリは YouTube Studio のログインが要る（西尾の YouTube アカウント）。Freesound のダウンロードはアカウント要。Pixabay はアカウント無しでダウンロードできる場合がある（未確認）。費用 0
- **最小の手順**: Studio → オーディオ ライブラリ → フィルタ「Attribution not required」→ 曲の行のライセンス欄を開いて YouTube の外での利用条件を読み、台帳に転記 → ダウンロード（MP3）
- **動いたと言える確かめ方**: 限定公開でアップロード後、動画の詳細に「Music in this Video」が出て、Studio の著作権の欄に申し立てが無い。台帳に曲ごとのライセンス欄の文言が写されている
- **所要の見込み（推測）**: 20 分

## Open Questions

- YouTube オーディオライブラリの標準ライセンスの条文（YouTube の外での利用）は Studio の中にあり、この調査では読めなかった。西尾のアカウントで曲のライセンス欄を開いて確かめる
- Pixabay の音楽が Content ID に当たった時の Pixabay 側の対応（ホワイトリスト等）は、読んだ Terms・FAQ に書かれていなかった
- Freesound の Sampling+ の音を収益化した YouTube 動画に使えるか（Freesound の解釈では BY-NC 相当なので不可）
