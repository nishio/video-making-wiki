---
type: source
summary: 商用の楽曲生成サービス（Suno・Udio・ElevenLabs Music・Stable Audio）の利用規約と YouTube の Content ID の資格規則を 2026-11-09 に条文で読んだページ。Suno は無料・Basic は非商用のみで Pro/Premier に生成物を譲渡、Udio はダウンロードも YouTube への掲載も禁止、ElevenLabs Music は Free でダウンロード不可・Starter 以上で動画に使え Free〜Pro は「個人の利用に限る」、Stable Audio の規約は読めなかった
video_types: [promo, talk, embed]
url: https://suno.com/terms
author: Suno Inc.、Udio（Uncharted Labs）、ElevenLabs、Google（YouTube ヘルプ）
published: 2026（各規約の日付は本文）
retrieved: 2026-11-09
sources:
  - https://suno.com/terms
  - https://help.suno.com/en/articles/2746945
  - https://www.udio.com/terms-of-service
  - https://elevenlabs.io/music-terms
  - https://elevenlabs.io/terms-of-use
  - https://elevenlabs.io/pricing
  - https://stableaudio.com/terms
  - https://support.google.com/youtube/answer/2605065
---

# Suno・Udio・ElevenLabs Music の規約と Content ID（2026-11-09 時点）

## 何の文献か

各サービスの利用規約の本文（一次資料）と、YouTube の公式ヘルプ「Content eligible for Content ID」。規約は事業者が一方的に改定するもので、下の内容は取得日の版。法的な解釈ではなく、条文に何が書いてあるかの記録。

| 文書 | 版 |
|---|---|
| Suno Terms of Service | Effective Date: September 3, 2026 |
| Suno ヘルプ「Do I have the copyrights to songs I made?」 | Edited September 4 2026 |
| Udio Terms of Service | Last Revised on November 12, 2025 |
| ElevenLabs Music Terms | Last updated: 09 October 2026 |
| ElevenLabs Terms of Service | Last Updated: 09 October 2026 |
| Stable Audio（stableaudio.com/terms） | **読めなかった**（ページが JavaScript で描画され、curl でも WebFetch でも本文が取れない） |

## 書いてあること

### Suno（2026-09-03 版）

- **Pro / Premier**: 「Suno hereby assigns to you all of its right, title and interest in and to any Output owned by Suno and generated from Submissions made by you」。ただし「Suno makes no representation or warranty to you that any copyright will vest in any Output」
- **Free / Basic**: 「you will only use such Outputs for your lawful, personal and non-commercial purposes」。ヘルプは「If you make music with the Basic (free) plan, Suno is the owner of the songs」と書く
- **ダウンロードの割当（新しい条項）**: 「You may commercially exploit Output solely to the extent ... you have obtained a permitted download of that Output in accordance with the download allocations for your applicable service tier」。月のダウンロード数はプランごとに suno.com/account で決まる。ダウンロード以外の方法（録音・stream ripping）で得たものは禁止。指紋・透かし・メタデータを付けることがあり、隠す目的で消すことは禁止
- 得たダウンロードの商用の権利は「perpetual and are not affected by ... the expiry, cancellation, downgrade or suspension of your subscription」
- **Remix**（他人の出力を作り変えたもの）はプランに関係なく非商用のみ
- **外部の場**: 「any use of an Output outside the Service is also subject to the terms, policies, and requirements of the third party operating the platform」「Applicable rights holders may also have the right to collect revenue related to distribution of Outputs on third party platforms」
- 入力（Submissions）には Suno の学習を含む広い利用許諾を与える（Content の条項）
- ヘルプ: 米国では AI だけで作った音楽は著作権の保護対象にならず、「Writing the prompt does not constitute the creation of the song」。歌詞を自分で書けば歌詞は自分のもの

### Udio（2025-11-12 版）

- 1.2「You may not download copies of any Output ... You covenant and agree not to download, reproduce, transmit, display, publish or otherwise distribute ... on any streaming platform or user generated content platform (e.g., YouTube, Facebook, Instagram, TikTok, Spotify, Soundcloud and similar platforms)」。承認済みの外部サイトにハイパーリンクを共有することだけ認める
- 6. Ownership: 「the Company and/or its licensors own all right, title and interest in and to the Services and the Output」。利用者は「solely for your personal and non-commercial purposes」
- 禁止事項に「exploit the Services, any Output ... for any commercial purpose」、出力を他の AI の学習に使うこと
- → 2026-11 時点の Udio は、動画の BGM を作る道具としては規約上使えない

### ElevenLabs Music（Music Terms、2026-10-09 版）

- 入力の禁止（2.1）: 実在のアーティスト名・作曲家名・曲名・アルバム名・出版社名・レーベル名、特定の曲と分かる歌詞の一部をプロンプトに入れてはいけない
- 生成物のクリアランスは利用者の責任（3.1）。AI 生成の印を付けることがあるが、それで開示義務は満たされない（3.4）
- Exhibit A（Music Commercial Rights Table）の抜粋:

| | Free | Starter | Creator | Pro | Scale | Business | Enterprise |
|---|---|---|---|---|---|---|---|
| 資格 | 個人の利用のみ | 個人のみ | 個人のみ | 個人のみ | 10 人未満の組織 | 50 人未満の組織 | 制限なし |
| 月の生成 | 11 分 | 17 分 | 62 分 | 304 分 | 1,100 分 | 4,800 分 | 個別 |
| 月のダウンロード | 不可 | 30 分 | 250 分 | 500 分 | 1,500 分 | 4,000 分 | 個別 |
| 音楽配信（Spotify 等） | 禁止 | 禁止 | 可 | 可 | 可 | 可 | 可 |
| Media Rights（映像への同期を含む） | 映画・TV・ラジオ・Studio Game を除くオンライン・オフラインの商用可 | 同 | 同 | 同 | 同 | 同 | 全て可（Enterprise Music） |
| クレジット | 要（「Eleven Music」と明記） | 不要 | 不要 | 不要 | 不要 | 不要 | 不要 |
| 高音質ダウンロード（WAV 等） | 無 | 無 | 無 | 有 | 有 | 有 | 有 |

- 「Media Rights」は「the right to synchronize Output in timed relation to audiovisual content」を含む（4.8(d)）。YouTube の動画の BGM はこの範囲と読める
- 「Music Library」（他人が使える素材集）を作ることは禁止（4.2）
- 価格（pricing ページ、月額・年払い換算の表示）: Free $0、Starter $5、Creator $18.33、Pro $82.50、Scale $249.17、Business $825
- 基本の ToS（2026-10-09 版）: 「if you access or use our Services free of charge ... you may only use the Services for non-commercial purposes」。「as between you and ElevenLabs, you retain all rights in and to your Output」。内容を学習に使われたくなければ設定でオプトアウトできる

### YouTube の Content ID（ヘルプ「Content eligible for Content ID」）

- 「You must have exclusive rights to the material in the reference file」。登録してはいけない例に「Content licensed non-exclusively from a third party」「Content released under Creative Commons or similar free of charge/open licenses」「Public domain ... recordings, or compositions」「Sound effects, soundbeds, or production loops」
- 「So-called "royalty free" production music libraries」に当たった一致は、申し立ての前に manual review に回す
- AI 生成の音楽についての記述はこのページに無い

## この wiki への含意

- galleria の 2026-09-04 の判断「収益化する作品の楽曲は ElevenLabs Music を第一候補、Suno/Udio は scratch に留める（Suno は有料 plan でも自らを author と称するため）」（[[exp-galleria-tts-and-singing]]）と照らすと:
  - Udio は 2025-11 の版で既に「YouTube への掲載禁止」で、scratch 以外に使えない。一致
  - Suno の 2026-09-03 版は Pro/Premier に「assigns to you all of its right」と書く。「有料でも Suno が author と称する」に当たる条文は、この版では見つからなかった。ただし「ダウンロードの割当の範囲だけ商用可」「著作権が生じる保証は無い」の条件が新しく付いている。判断の根拠が古い版だった可能性がある（galleria の整理が読んだ版は経験ページから分からない）
  - ElevenLabs Music は Free でダウンロード不可。動画に使うには最低 Starter（$5/月）。**Free〜Pro は「For Individual Use Only」**。会社の発信物（[[work-promotion-video]] の文脈）に使うなら Scale（10 人未満の組織）以上が条文上の候補で、ここは西尾が決めること
- **Content ID との関係**: 生成した曲は非独占のことが多い（Suno の Basic は Suno の所有、ElevenLabs は他の利用者も似た曲を作りうる）。YouTube の規則では、非独占・CC・効果音・ループは登録できない。自分の動画が誰かの Content ID に当たる事故は、他人が同じ素材（または似た生成物）を不正に登録した時に起きる。素材集の側の注意は [[web-means-sound-soundeffect-lab-maoudamashii-opentracks]]
- 概要欄の「音楽: オリジナル（プログラムで合成）」（[[exp-html-capture-pipeline]]）のように、生成サービスを使ったら「音楽: ElevenLabs Music で生成（Starter プラン、2026-11 の規約）」のように版まで書いておくと、後で規約が変わっても判断を辿れる（推測。規約はプランと版で権利が変わるため）
- promo は曲が主役なのでクレジット・権利の確かさが要る。talk・embed の控えめなインストなら、手元のモデル（[[web-means-sound-ace-step-yue2-diffrhythm]]）か numpy 合成で外部規約を避けられる

## 着手の仕方（未検証。galleria で確かめる）

- **何が表現できるようになるか**: 歌付き・インストの完成度の高い曲を、ブラウザで数分で作る。効く型: promo
- **機械**: どこでも（ブラウザ）。API は Starter 以上（ElevenLabs）
- **費用・アカウント**: 要: アカウント・費用（ElevenLabs Music は動画に使うなら Starter $5/月以上。会社の発信物なら Scale 以上が条文上の候補。Suno は Pro 以上）。西尾が決める
- **利用条件の要点**: 上の表。Free の出力は動画に使わない
- **最小の手順**: 西尾がアカウントとプランを決めた後、ブラウザで 60 秒・インスト・BPM 指定のプロンプトで 3 本生成し、ダウンロード（Starter は MP3）。手元の制作フォルダに `music/ledger.md` を作り、サービス名・プラン・規約の版（例: ElevenLabs Music Terms 2026-10-09）・生成日・プロンプトを 1 行ずつ書く
- **動いたと言える確かめ方**: ダウンロードした音声が `ffprobe` で指定の長さ、台帳に版が記録されている。YouTube に限定公開で上げ、Studio の「著作権」の欄に申し立てが出ないこと（数時間〜1 日待つ）
- **所要の見込み（推測）**: アカウント作成後 30 分

## Open Questions

- Stable Audio（stableaudio.com）の現行規約の本文は読めなかった。Stable Audio 2.x の生成物の権利、無料プランの扱いは未確認
- Suno の「Pro and Premier」で作り、ダウンロード割当を使い切った後の未ダウンロード曲は商用不可（条文）。割当の数は suno.com/account（ログイン要）にあり読んでいない
- ElevenLabs の Music Terms の表は Free の列にも「All online and offline commercial use permitted」と書くが、基本の ToS は Free の利用者を非商用に限り、Free はダウンロード不可。条文どうしが食い違って見える。ToS が「Supplemental Terms will control for that conflict」と書くので Music Terms が優先とも読めるが、ダウンロードできない以上、実務上は Free を動画に使えない
- ElevenLabs の「individual use only」の「Individual」の定義（会社員が業務で使う場合）は Music Terms に無い。Underlying Agreement の定義を確かめていない
- YouTube が AI 生成の音楽を Content ID の参照として受け付けるかの公式記述は見つからなかった（ブログ・Reddit には「不可と言われた」「登録できた」の両方の報告があるが、一次資料ではない）
- 日本の著作権法での AI 生成物の扱い（著作物性）は、この担当の範囲外として読んでいない
