---
type: concept
summary: ナレーション（TTS）・BGM・効果音の扱いを、ラウドネスの規格・配信の推奨・ダッキングの実験・学習研究と西尾の経験で並べたページ。経験の loudnorm −16 LUFS は配信向け推奨の上限に当たり、声に対して音楽を少なくとも 10 LU 下げるという実験の推奨があり、BGM が学習を妨げるかは研究が割れている
video_types: [any]
sources:
  - web-ebu-r128-itu-bs1770.md
  - web-aes-td1004-streaming-loudness.md
  - web-torcoli-2019-background-ducking.md
  - web-moreno-mayer-2000-coherence-sounds.md
  - web-mayer-2003-voice-principle-tts.md
  - web-digiday-2016-85-percent-sound-off.md
  - exp-html-capture-pipeline.md
  - exp-sutra-hype-editions.md
  - exp-qualia-video.md
---

# ナレーション・BGM・効果音

## ラウドネスの目安

| 場 | 目標 | 出典 |
|---|---|---|
| 放送（欧州） | EBU R 128: −23 LUFS、True Peak −1 dBTP | [[web-ebu-r128-itu-bs1770]] |
| 放送（米国） | ATSC A/85: 台詞を基準に −24 LKFS、−2 dBTP 未満 | 同 |
| 配信 | AES TD1004・R 128 s2: −20〜−16 LUFS、−1 dBTP | [[web-aes-td1004-streaming-loudness]] |
| Spotify | −14 LUFS に正規化 | 同 |
| Apple Podcasts | −16 ±1 LUFS を勧める | 同 |
| YouTube | 公式ヘルプに目標の LUFS は無い（Stable volume が既定でオン、という記述のみ）。「−14」は通説。Ian Shepherd（2017）は「小さい動画は上げない」と書く | 同 |

- 経験の `loudnorm=I=-16:TP=-1.5:LRA=11`（[[exp-html-capture-pipeline]]、[[exp-democracy-river-video]] 英語版）は、TD1004 の上限ちょうど、R 128 s2 の暫定範囲の上端、Apple Podcasts の中心に当たる。話し言葉は音楽より 2 LU ほど低く、という TD1004 §7 の向きからは、ナレーション主体なら大きめの側（[[web-aes-td1004-streaming-loudness]]）
- LRA=11 は短尺ではおそらく効かない。R 128 は 1 分未満で LRA を使うなとし、短尺用の補遺 s1 は LRA を不適用としている（[[web-ebu-r128-itu-bs1770]]）
- [[exp-sutra-hype-editions]] の「−9.6 LUFS で書き出す（配信で −14 へ下げられる前提）」は Spotify については公式どおり。YouTube は公式の数値が無い。正規化の無い場面（ダウンロードした mp4、講演会場、X）ではそのまま大きく鳴る（[[web-aes-td1004-streaming-loudness]] の推論）
- embed で会場の PA から鳴らすなら、配信の正規化は効かない。動画同士・話し手の声との釣り合いは会場で決まる（同、推論）

## ダッキング（声と BGM の差）

- Torcoli ら（JAES 2019、聴力の正常な 22 人）は、解説の声に対して音楽は少なくとも 10 LU、環境音は 15 LU 下げることを勧める。専門家でない人は専門家より 4 LU 大きい差を好んだ。個人差は大きい（[[web-torcoli-2019-background-ducking]]。本文は Cloudflare で取れず、abstract と Fraunhofer の blog から）
- ffmpeg の注意（同）: `loudnorm` は measured_* を全部渡さないと線形にならず dynamic mode になる（192 kHz に上げるので `-ar` が要る）。`sidechaincompress` は既定の ratio 2 だと、声が閾値を 8 dB 超えても BGM は約 4 dB しか下がらない（担当の計算）。決まった dB だけ下げる仕組みではない
- 経験の英語版は `sidechaincompress` で BGM を声の間だけ下げたが、引数・単パスか 2 パスか・声と BGM の差の実測は経験ページに書かれていない。10 LU を満たしていたかは分からない

## BGM・効果音と学習

- Moreno & Mayer（2000）: 180 秒のナレーション付きアニメ（各実験 75 人）に音楽を足すと保持とトランスファーが下がった。実験 1 の保持 11.37 → 7.65（担当の概算で d ≈ 1.06）。出来事と一対一で一度だけ鳴らした効果音は実験 1 で害にならなかった（[[web-moreno-mayer-2000-coherence-sounds]]）
- 一方、de la Mora Velasco ら（2023、47 研究のメタ分析、abstract のみ）は BGM に小さな正の効果 d=0.314 を出している。評価の前に流した研究が効いている（同）
- 経験の promo は音楽と拍が主導する（[[three-video-types]]）。学習研究の測度（保持・トランスファー）は promo の目的と違うので、ここから promo の BGM を否定はできない。talk・embed には Moreno & Mayer の向きが当てはまりうる

## ナレーションの声（TTS）

- voice principle: Mayer ら 2003 で機械の声は人の声より劣った。2017〜2019 年の Craig & Schroeder では当時の現代的 TTS（Neospeech）が一般の人の録音と学習成果で同等。Siegle & Craig 2024 ではプロの声優が現代の合成音声より保持・トランスファーとも上（[[web-mayer-2003-voice-principle-tts]]。多くは abstract のみ）
- 2024 年以降の生成系 TTS と、日本語で測った研究は見つからなかった（同）
- 経験の「SAPI は古臭い、問題は速度より読みと声質」（[[exp-qualia-video]]、[[exp-galleria-tts-and-singing]]）は研究の向きと一致する。読み違い（「こえつき」が「こわつき」）のような問題は研究の範囲外

## 無音で見られる前提との兼ね合い

- 無音前提か音あり前提かは面ごとに違う（[[promo]] の表）。X のタイムラインは無音への備え、YouTube・TikTok・Reels は音あり前提
- YouTube の Voice boost は視聴者の側で背景音を下げ声を強める機能。BGM を声から十分離していない動画は、視聴者の装置で勝手に下げられうる（[[web-aes-td1004-streaming-loudness]]）
- R 128 s2 はスマホ（利得が小さく騒がしい環境）を前提に配信の値を上げることを許している。小型スピーカーで鳴る帯域に意味のある音を置く必要がある、という点は [[exp-sutra-hype-editions]] の「低域だけの太鼓はスマホで聞こえない」と同じ向き（規格の数値は帯域を保証しない）

## Open Questions

- X・TikTok・Instagram が再生時に音量を正規化しているかの公式記述は探していない
- YouTube の参照レベルは、自分の動画の Stats for nerds で測れる（未実施）
- [[exp-sutra-voicevox-singing]] の「声の帯域で伴奏比 +8〜11 dB」と Torcoli の 10 LU は桁が近いが、測り方も素材も違うので比べられない
- 生成系の日本語 TTS（VOICEVOX・AivisSpeech・Irodori-TTS など）で voice principle を測った研究は無い

## Updates

### 2026-11-09 第 2 回サーベイから

- 表現としての音（Chion の synchresis・added value、Murch の音と映像のずれ）は [[web-layout-chion-audio-vision-murch-sound]] と [[design-fundamentals]]。学習研究（Moreno & Mayer）とは測るものが違う
- Opus 5.5 期の作り手は「モデルは聞けない」と書き、ラウドネス・同期の機械検査と TTS の文字起こしでの照合で補っている（[[after-opus55]]）

