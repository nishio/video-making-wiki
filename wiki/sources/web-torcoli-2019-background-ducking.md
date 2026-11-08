---
type: source
summary: 声の下で BGM・環境音をどれだけ下げるか（ダッキング）の聴取実験 Torcoli ら（JAES 2019）と、ffmpeg の sidechaincompress・loudnorm・alimiter の公式文書。Torcoli らは解説の声と音楽で少なくとも 10 LU、環境音で 15 LU の差を勧め、専門家でない人は専門家より 4 LU 大きい差を好んだと報告している
video_types: [talk, promo, embed]
url: https://doi.org/10.17743/jaes.2019.0052
author: Matteo Torcoli, Alex Freke-Morin, Jouni Paulus, Christian Simon, Ben Shirley（Fraunhofer IIS／University of Salford）／FFmpeg developers
published: 2019-12（JAES 67(12)）／2019-03（AES 146th Convention 版）／unknown（ffmpeg-filters の文書。2026-11-09 に取得した版）
retrieved: 2026-11-09
sources:
  - https://doi.org/10.17743/jaes.2019.0052 （Torcoli, M., Freke-Morin, A., Paulus, J., Simon, C., & Shirley, B. (2019). Preferred Levels for Background Ducking to Produce Esthetically Pleasing Audio for TV with Clear Speech. J. Audio Eng. Soc. 67(12), 1003–1011。**原典未読**: AES・Salford の全文は Cloudflare で取得できず、Semantic Scholar の abstract と FAU CRIS の書誌で読んだ）
  - https://audioblog.iis.fraunhofer.com/?p=4251 （Fraunhofer IIS Audio Blog「Awards for Fraunhofer IIS Scientists at AES 146」2019-04-12。会議版の紹介）
  - https://ffmpeg.org/ffmpeg-filters.html （FFmpeg Filters Documentation。8.97 loudnorm、8.105 sidechaincompress、8.31 alimiter、8.2 acompressor の節を読んだ）
  - https://www.aes.org/technical/documents/AESTD1004_1_15_10.pdf （AES TD1004 §7。Internet Archive の版で読んだ。[[web-aes-td1004-streaming-loudness]]）
  - https://tech.ebu.ch/docs/tech/tech3343.pdf （EBU Tech 3343-2023 の前景音の節。[[web-ebu-r128-itu-bs1770]]）
---

# Torcoli ら 2019（ダッキングの好みの差）と ffmpeg のダッキング・正規化フィルタ

## 何の文献か

- **Torcoli ら（2019）**: 査読論文（Journal of the Audio Engineering Society）。Fraunhofer IIS（MPEG-H などの音声符号化の研究所）と Salford 大学の共著。同年の AES 146 回大会の版は大会の最優秀査読論文賞（Fraunhofer の blog）。**全文は読めておらず、以下は abstract と blog による**
- **FFmpeg のフィルタ文書**: 公式ドキュメント。各フィルタの引数と既定値の仕様で、使い方の推奨値は書いていない
- 補足として AES TD1004 §7 と EBU Tech 3343 の前景音の記述を並べる（規格の本文は別ページ）

## 書いてあること

### Torcoli ら（abstract・blog から）

- 背景: ダッキング（声のある間だけ背景を下げる）は声の明瞭さと、背景の役目（雰囲気・気分・意味の手がかり）を両立させる手法だが、「Technical details for recommended ducking practices are not currently documented in the literature」と書く
- 方法: (1) TV ドキュメンタリーのダッキングの実例を分析、(2) 聴力の正常な 22 人（専門家 11・非専門家 11、blog による）に、ダッキング中の解説（commentary）と背景のラウドネス差（Loudness Difference, LD）の好みを聞いた
- 結果（abstract の原文）:
  - 「Highly personal preferences were observed」— 個人差が大きく、聞き手が自分で調整できるオブジェクトベース音声の重要さを示す、と書く
  - 「On average, non-experts preferred LDs that were 4 LU higher than the ones preferred by experts」（統計的に有意）
  - 解説＋音楽（CoM）と解説＋環境音（CoA）の間にも有意差
  - 「we recommend at least 10 LU difference for CoM and at least 15 LU for CoA」
  - 計算モデル（BiDWGP）は各素材の好みの中央値を平均絶対誤差 1.97 LU で当てた
- blog は、現場録音の台詞（location dialogue）には解説より大きい LD が要ると書いている（数値なし）
- 原典未読のため、LD をどの区間・どの測り方（統合か short-term か）で数えたか、ドキュメンタリーの実例の LD がいくつだったか、素材の長さ・再生環境は確かめていない

### AES TD1004 §7・EBU Tech 3343（別の角度から）

- TD1004: 同じ統合ラウドネスに揃えた話し声は音楽より大きく聞こえるので、話し声の区間を他の区間より 2〜4 LU 低く。これは**順番に並ぶ区間どうし**の話で、声の下に BGM を敷くときの差ではない
- Tech 3343: 声・タイトル音楽・主要な効果音などの「foreground sounds」が大きさの印象を決める。要素の釣り合いは芸術的判断で、ラウドネス計はそれを目で確かめる道具

### ffmpeg の sidechaincompress（8.105）

- 「acts like normal compressor but has the ability to compress detected signal using second input signal」。第 1 入力（BGM）を第 2 入力（声）の大きさで圧縮する
- 主な引数と既定値: `threshold` 0.125（線形。約 −18 dBFS）、`ratio` 2（範囲 1〜20）、`attack` 20 ms、`release` 250 ms、`makeup` 1、`knee` 2.82843、`detection` rms、`link` average、`level_sc`（サイドチェインの利得）1、`mix` 1
- 文書の例: `[1:a]asplit=2[sc][mix];[0:a][sc]sidechaincompress[compr];[compr][mix]amerge`
- 仕組みの帰結（AI の計算。文書は推奨値を書いていない）: 通常の圧縮と同じく、減る量は「サイドチェインが threshold を超えた量 ×（1 − 1/ratio）」。既定の ratio 2 では、声が threshold を 8 dB 超えても BGM は約 4 dB しか下がらない。**固定量（例: −12 dB）だけ下げる「ダッキング」ではなく、声の大きさに比例して下げ幅が揺れる**。大きく・一定に下げたいなら ratio を上げるか、BGM をそもそも低く置く

### ffmpeg の loudnorm（8.97）

- 「EBU R128 loudness normalization. Includes both dynamic and linear normalization modes」。単パス（ライブ・ファイル）と 2 パス（ファイル）がある
- 既定値: `I` −24.0（範囲 −70〜−5）、`LRA` 7.0、`TP` −2.0
- **`linear`（既定 true）でも、`measured_I`・`measured_LRA`・`measured_TP`・`measured_thresh` を全部与えないと線形にならない**。また、目標 LRA が元の LRA より小さい、または上げた結果 True Peak が目標を超える場合も「normalization mode will revert to dynamic」
- 「In dynamic mode, to accurately detect true peaks, the audio stream will be upsampled to 192 kHz. Use the `-ar` option or `aresample` filter to explicitly set an output sample rate」
- `dual_mono`: モノラルを 2ch で鳴らす前提なら補正する（既定 false）

### ffmpeg の alimiter（8.31）

- 先読み（lookahead）で閾値を超えさせないリミッタ。`limit` 既定 1、`attack` 5 ms、`release` 50 ms。attack と同じだけ遅延が出る

## この wiki への含意

- **経験との照合**（[[exp-html-capture-pipeline]]、[[exp-democracy-river-video]] 英語版）: 「`sidechaincompress` で声の間だけ BGM を下げ、`alimiter`、最後に `loudnorm=I=-16:TP=-1.5:LRA=11`」は、Torcoli らの言うダッキングそのもの。ただし経験ページには sidechaincompress の引数も、声と BGM の LD の実測も書かれていない。Torcoli らの推奨（音楽で 10 LU 以上）を満たしていたかは**分からない**
- **単パスの loudnorm は線形でない**（ffmpeg 文書）。経験の書き方（`loudnorm=I=-16:TP=-1.5:LRA=11` のみ）が単パスなら dynamic mode で、統合値を合わせるために時間とともに利得を動かしている。ダッキングで作った声と BGM の差を、最後の loudnorm がさらに動かす可能性がある。また dynamic mode は 192 kHz に上げるので、`-ar` を付けないと出力の標本化周波数が変わりうる。2 パス（1 回目で測り、2 回目に `measured_*` を渡す）にすると線形になる。**経験の mix.py が単パスだったかは、この wiki の情報では確かめられない**
- **声の帯域で測る経験との対応**: [[exp-sutra-voicevox-singing]] は、声が伴奏に埋もれた版を「800–4kHz 帯で +1dB」と測り、声を別バスで重ねて「伴奏比 +8〜11dB」にした。Torcoli らの「音楽の上の解説は 10 LU 以上」と桁は近いが、測り方（帯域 RMS と K 特性の統合ラウドネス）も素材（歌と伴奏、解説と背景音楽）も違うので、そのまま比べられない
- **専門家と非専門家の差 4 LU**: 作り手（西尾や AI）が「ちょうどいい」と感じる BGM は、視聴者には大きすぎる側に寄りうる、という読み方ができる（Torcoli らは専門家を「音声の専門家」として数えている。動画の作り手がどちらに近いかは分からない）
- **型ごと**:
  - talk: ナレーション主体なので Torcoli らの CoM（解説＋音楽）が直接の参考。YouTube の Voice boost（[[web-aes-td1004-streaming-loudness]]）が背景を下げる機能を視聴者側に持つことも、背景を大きくしすぎない方向の材料
  - promo: X 用の字幕だけの版（音は BGM のみ、[[exp-democracy-river-video]]）にはダッキングの対象が無い。ナレーション版を作るときに効く
  - embed: 講演の中で流すなら、背景音は話者の生の声とも競合する（推論）
- 学習への影響（BGM は理解を妨げるか）は別の問いで、[[web-moreno-mayer-2000-coherence-sounds]] に置いた

## Open Questions

- Torcoli らの全文（ドキュメンタリーの実測の LD、LD の測り方、素材の長さ）。AES の e-library は Open Access とされるが機械から取れなかった
- 経験の英語版（87 秒）の声と BGM の LD はいくつだったか。stem（声・BGM）を ffmpeg の `ebur128` で別々に測れば分かる
- 10 LU 以上離すと BGM はスマホのスピーカーでほぼ聞こえなくなるのでは、という懸念と、BGM の役目（雰囲気）の釣り合い。Torcoli らは TV 向けで、スマホでの再生は条件に入っていない（abstract から読み取れる範囲では）
- 聴力の衰えた視聴者は大きい LD を好むという研究（BBC の 1991 年の研究などの二次記述を検索で見た）は原典を読んでいない
