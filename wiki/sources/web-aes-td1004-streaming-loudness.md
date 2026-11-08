---
type: source
summary: ネット配信のラウドネスの推奨と各サービスの公式の記述。AES TD1004（2015）と EBU R 128 s2（2023）はストリームを −20〜−16 LUFS・True Peak −1 dBTP 以下にと書き、Spotify は −14 LUFS に正規化、Apple Podcasts は −16 LKFS ±1 を勧める。YouTube の公式ヘルプには目標の数値が無い
video_types: [any]
url: https://www.aes.org/technical/documents/AESTD1004_1_15_10.pdf
author: AES Technical Council（Audio Engineering Society）／EBU PLOUD／Spotify／Apple／Google（YouTube ヘルプ）／Ian Shepherd（Production Advice）
published: 2015-10-19（TD1004 v1.0）／2023-11（R 128 s2 V3）／unknown（Spotify・Apple・YouTube のヘルプは日付なし。2026-11-09 に取得）／2017-09-29（Shepherd）
retrieved: 2026-11-09
sources:
  - https://www.aes.org/technical/documents/AESTD1004_1_15_10.pdf （AES TD1004.1.15-10「Recommendation for Loudness of Audio Streaming and Network File Playback」。AES のサイトは機械からの取得を拒んだので Internet Archive の 2020 年の版 https://web.archive.org/web/2020/https://www.aes.org/technical/documents/AESTD1004_1_15_10.pdf で全文を読んだ）
  - https://tech.ebu.ch/docs/r/r128s2.pdf （EBU R 128 s2-2023「Loudness in Streaming」。全文を読んだ）
  - https://support.spotify.com/us/artists/article/loudness-normalization/ （Spotify for Artists「Loudness normalization on Spotify」。本文を読んだ）
  - https://podcasters.apple.com/support/audio-requirements （Apple Podcasts for Creators「Audio requirements」。Audio levels の節を読んだ）
  - https://support.google.com/youtube/answer/14106294 （YouTube ヘルプ「Control video volume on your device」。本文を読んだ）
  - https://support.google.com/youtube/answer/16619284 （YouTube ヘルプ「Video & audio quality enhancements」。本文を読んだ）
  - https://productionadvice.co.uk/stats-for-nerds/ （Ian Shepherd、2017-09-29。curl では本文が取れず、WebFetch で該当箇所の原文引用を頼んで読んだ）
  - https://docs.telosalliance.com/docs/understanding-loudness-for-streaming-audio （Telos Alliance の製品文書。AES TD1008 の数値の二次情報）
  - https://www.grimmaudio.com/news/aes-td1008-ends-the-loudness-war/ （Grimm Audio、2021-09-22。TD1008 の公開と AES77 への昇格の二次情報）
---

# AES TD1004・EBU R 128 s2 と配信サービスのラウドネス

## 何の文献か

- **AES TD1004.1.15-10**（2015-10-19）: 音響学会 AES の技術委員会の技術文書（Technical Document）。「radio-like」なストリームとポッドキャストのような「network file playback」向け。映画のように振れ幅の大きい内容は対象外と明記（§1）。2021 年に後継の **TD1008**（「Recommendations for Loudness of Internet Audio Streaming and On-Demand Distribution」）が出て、2023 年に AES 規格 **AES77-2023** になった（Grimm Audio の記事）。**TD1008 と AES77 の本文は読めていない**（AES のサイトが拒否、AES77 は非会員有料）
- **EBU R 128 s2**（2023-11 V3）: 放送局がストリーミングに出すときの EBU の補遺
- **Spotify・Apple Podcasts・YouTube のヘルプ**: 各社の公式の説明。日付の記載なし
- **Ian Shepherd の記事**（2017）: マスタリング技術者の実務ブログ。YouTube の「Stats for nerds」の読み方

## 書いてあること

### AES TD1004（2015）

§3 の推奨（原文）:
- 「the Target Loudness of the stream not exceed -16 LUFS」— ピークの潰しすぎを避け、振れ幅を残すため
- 「the Target Loudness of a stream not be lower than -20 LUFS」— モバイル機器で聞こえるようにするため
- 短尺（60 秒以下）は「Maximum Short-term Loudness to be no more than 5 LU higher than the Target Loudness」
- 「the maximum peak level not exceed −1.0 dB TP」— 非可逆圧縮の符号化で歪まないように

理由づけ（§4・付録）:
- −20 の下限は、一部のモバイル機器は利得が足りず −23・−24 LUFS では満足な音量にならないから、と書く。欧州の携帯プレーヤーの音量規制（EN 50332）が原因の一つ
- −16 に近づくほど強いダイナミクス処理が要り音質が落ちる。−18 のような低めの目標は、ピーク制限なしで peak-to-loudness ratio を大きく取れる
- 非可逆符号化の後でピークは上がるので、符号化の前に −1.0 dB TP のセーフティ・リミッタを、低ビットレートではさらに下げる
- §7: **同じ統合ラウドネスに揃えた話し声は音楽より大きく聞こえる**。番組内の話し声の区間は他の区間より 2〜4 LU（以上）低く正規化することを勧める。ただし要素間の釣り合いは制作者の芸術的判断で決めよ、とも書く

### AES TD1008（2021。本文未読、二次情報）

- 音響機器メーカー Telos Alliance の製品文書は、TD1008 に従うなら音楽は −16 LUFS、話し言葉は −18 LUFS、混在のリアルタイム配信では間を取って −17 LUFS、と要約している。製品の宣伝を含む文書で、原文の数値は確かめていない

### EBU R 128 s2（2023）

- 放送局の番組は R 128 どおり −23.0 LUFS で作り、**ストリームにもそのまま −23 で出す**のが本則（e）
- ただし再生側が小さい利得・余裕しか持たない、または騒がしい環境（スマートフォン・携帯プレーヤー）を想定するなら、メタデータで制御しない限り、配信のラウドネスを上げてよい。その暫定値は「in the range of −20.0 to −16.0 LUFS」（g）
- モバイル機器が十分な利得を持つようになったら −23 に戻せ（h）。脚注は、EN 50332-3 と IEC 62368-1 の改訂で「this situation is effectively in place」と書いている（＝もう戻せる、という含み）

### Spotify（公式ヘルプ）

- 「We adjust tracks to **-14 dB LUFS**, according to the ITU 1770 standard」。再生時に適用
- 大きいマスターは下げる（歪みは足さない）。小さいマスターは上げるが、非可逆の符号化のために 1 dB の余裕を残す。例として「-20 dB LUFS, and its True Peak maximum is -5 dB FS, we only lift the track up to -16 dB LUFS」
- Premium の利用者は Loud（−11、リミッタ付き）・Normal（−14）・Quiet（−19）を選べる
- 制作者への推奨: マスターを −14 integrated LUFS に、True Peak は −1 dB 以下。−14 より大きいなら True Peak を −2 dB 以下に

### Apple Podcasts（公式ヘルプ）

- 「preconditioned so the overall loudness remains around -16 dB LKFS, with a +/- 1 dB tolerance, and that the true-peak value doesn't exceed -1 dB FS」。測り方は BS.1770-5。前処理は符号化の前に

### YouTube（公式ヘルプ）

- 「Stable volume」が**既定でオン**。「balances the range between quiet and loud, continuously adjusting volume levels to reduce variations in sound」。全動画で使えるわけではなく、YouTube Music と公式の音楽動画では切られる
- 「Voice boost」は「makes it easier to hear dialogue by reducing background sounds and highlighting vocals」。コンピュータと TV で視聴者が入れられる。入れると Stable volume は切れる
- 「Video & audio quality enhancements」のページは、YouTube がアップロードに自動で音量・ミックスの調整を加えることがあり、投稿者が「Let YouTube enhance audio quality」で切れると書いている
- **YouTube のヘルプに目標ラウドネスの数値（LUFS）は見つからなかった**（2026-11-09 時点、上の 2 ページと検索で）

### YouTube の数値についての実務側の記述（非公式）

- Ian Shepherd（2017-09-29）は、YouTube の「Stats for nerds」の「content loudness」は「the difference between YouTube's estimate of the loudness and their reference playback level」で、正なら下げられ、負なら何もされない、「YouTube doesn't turn up quieter videos」と書いている。この記事自体は基準の LUFS 値を書いていない
- 「YouTube は約 −14 LUFS」という値は多くの二次記事が書いているが、測定の手順を示した一次の出典は今回見つけられなかった。2017 年の記事は Stable volume（後から入った機能）より前のもの

## この wiki への含意

- **経験の `loudnorm=I=-16:TP=-1.5` が何に当たるか**（[[exp-html-capture-pipeline]]、[[exp-democracy-river-video]] 英語版）:
  - AES TD1004 の範囲（−20〜−16）の**上限ちょうど**、EBU R 128 s2 の暫定範囲の上端、Apple Podcasts の −16 ±1 の中心。TD1008 の要約（Telos）でいう「音楽 −16」にあたり、「話し言葉 −18」より 2 LU 大きい
  - True Peak −1.5 は TD1004・R 128・Apple・Spotify（−14 以下のマスター）の −1 dBTP より 0.5 dB 余裕がある
  - Spotify の −14 よりは 2 LU 小さい。YouTube は公式の数値が無く、Shepherd の記述どおり「小さいものは上げない」なら、−16 の動画はそのまま −16 で鳴る（−14 前後の動画と並ぶと少し小さく聞こえる、という推論。測っていない）
  - X（旧 Twitter）の正規化については公式の記述を探していない
- **[[exp-sutra-hype-editions]] の「−9.6 LUFS で書き出した（配信で −14 へ下げられる前提）」**: Spotify については公式の記述どおり（−14 に下げられる）。Spotify は −14 より大きいマスターに True Peak −2 dB 以下を勧めている。YouTube の「−14 へ下げられる」は公式の数値ではなく、実務の通説に当たる。下げられる前提で大きく作ると、正規化の無い場面（ダウンロードした mp4、講演会場での再生、X）ではそのまま大きく鳴る
- **型ごと**:
  - promo（X・YouTube ショート）: 各サービスの正規化の有無と目標がばらばらなので、−16〜−14 あたりで True Peak −1 以下に揃えるのが、TD1004・Spotify・Apple の推奨の重なり（推論）
  - talk（ナレーション主体）: TD1004 §7 と TD1008 の要約は「話し言葉は音楽より 2 LU ほど低く」の向き。ナレーション主体の解説動画を −16 に揃えるのは、話し言葉としては大きめの側
  - embed: 講演のスライドに埋め込んで流すと、配信の正規化は効かない。動画の音を講演の PA で鳴らすなら、動画同士・話者の声との釣り合いは会場で決まる（推論）
- **無音で見られる前提との兼ね合い**: YouTube の Voice boost は視聴者の側で「背景音を下げ声を強める」機能。BGM を声から十分離していない動画は、視聴者の装置で勝手に下げられうる。逆に、R 128 s2 は「スマートフォンは利得が小さく騒がしい環境」を前提に配信の値を上げることを許している。音ありで見られるときの多くがスマホのスピーカーなら、[[exp-sutra-hype-editions]] の「低域だけの太鼓は聞こえない」と同じく、小型スピーカーで鳴る帯域に意味のある音を置く必要がある（規格の数値は帯域を保証しない）

## Open Questions

- YouTube の参照レベル（−14 LUFS と言われる）は公式に確かめられない。手元で上げた動画の「content loudness」を Stats for nerds で読めば測れる（未実施）
- AES TD1008（2021）・AES77-2023 の本文の数値（音楽 −16、話し言葉 −18 など）は二次情報のまま
- X・TikTok・Instagram が再生時に正規化しているか、公式の記述は未調査
- 経験の英語版（ナレーション＋BGM）を −16 に揃えたのは、TD1008 の要約でいう「話し言葉 −18」と「音楽 −16」のどちらの扱いが適切だったか
