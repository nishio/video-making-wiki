---
type: concept
summary: 西尾の語「解説プレゼン風」の型（talk）について、マルチメディア学習の研究・教育動画の研究と、explainer の実務家の型、西尾の制作経験を並べたページ。台本の骨格は「動機（why）→ 仕組み（how）→ 結び」でほぼ揃い、研究からは「飾りを除き、要点を指し示し、ナレーションと絵を同時に」が支えられるが、効果量は Mayer の研究室の値より独立したメタ分析の値の方が小さい
video_types: [talk]
sources:
  - web-mayer-multimedia-principles.md
  - web-guo-2014-video-production-engagement.md
  - web-kim-2014-in-video-dropouts.md
  - web-brame-2016-effective-educational-videos.md
  - web-muller-2008-misconceptions.md
  - web-common-craft-script-writing-guide.md
  - web-yum-yum-videos-explainer-script.md
  - web-wistia-video-length-engagement.md
  - web-3blue1brown-exposition-advice.md
  - web-kurzgesagt-video-process.md
  - exp-*.md（本文に個別の出典）
---

# 解説プレゼン風（talk）

西尾の語のまま（[[origin-2026-11-09]]）。三つの型の比較は [[three-video-types]]。

## 台本の骨格（実務家）

- Common Craft（Lee LeFever）は「Why? → How?」の順で、聞き手が知っているほど How に寄せる（Explanation Scale）。骨格は「うなずける文脈 → 物語・つながり・記述から選ぶ → 気づき／CTA」。3 分以下で 425〜525 語と書く（[[web-common-craft-script-writing-guide]]）
- Yum Yum Videos（制作会社、宣伝目的）は 90 秒の型を「問題 0–15 秒 → 解決 → 仕組み 30–65 秒 → 信じる理由 1 つ → CTA」とし、毎分 140〜160 語、画面の列を台本と同時に書く、と書く（[[web-yum-yum-videos-explainer-script]]）
- SoME（3Blue1Brown の Grant Sanderson が主催）の審査基準は「なぜ気にかけるべきかが最初の 30 秒以内に分かる」。Sanderson の FAQ は「具体が先、定義から始めない」「Know your genre（語り手の役が違えばテンポと様式が違う）」と書く（[[web-3blue1brown-exposition-advice]]）
- Kurzgesagt は出典表を作り、台本を 10 回ほど書き直し、ナレーションがアニメーションのタイミングを決める、と制作工程を書いている（[[web-kurzgesagt-video-process]]）
- 尺は語数で決まり、速く読んでも直らないので削る（Common Craft・Yum Yum・Kurzgesagt の記述の重なり）。英語で毎分 140〜175 語

## 研究から支えられること（効果量と条件を落とさない）

- **Mayer の原則の効果量は、独立したメタ分析のおよそ 1.5〜3 倍**。modality は Mayer 1.00 対 g=0.38（出版バイアス補正後 0.20）、coherence 0.86 対 0.33、personalization 1.00 対 0.33（Noetel ら 2022 のメタメタ分析。[[web-mayer-multimedia-principles]]）。この wiki で引くときは独立のメタ分析の値を主にする
- 設計の原則は、**システムがペースを決める教材**（g=0.41 対 学習者ペース 0.27）と**複雑な教材**（0.70 対 単純 0.20）でよく効く（同）
- **誤概念を先に述べて否定する解説**は、簡潔な講義形式より学習の伸びが大きかった。大学 1 年の物理の学生 364 人、ニュートンの法則、概念調査で効果量 0.79（Refutation）・0.83（Dialogue）。関係ない面白い話を足しても足さなくても成績は変わらなかった（104 人）（[[web-muller-2008-misconceptions]]。JCAL・Sci Ed の本文は未読で、抄録と台本の抜粋から）
- **6 分**は Guo ら 2014 で「視聴時間の中央値が最大で 6 分だった」という MOOC の観察（690 万セッション）。学習効果は測っていない。話す速さについて著者自身が「熱意の表面にすぎない、無理に速くさせるな」と書く（[[web-guo-2014-video-production-engagement]]）
- 観直しの山の 61% が画面の切り替わりの前後にあり、うち 23% は「消えた画面に戻る」山。著者は急な切り替えを避けよと提言（[[web-kim-2014-in-video-dropouts]]）
- Brame 2016 は実験のないガイドで、認知負荷・エンゲージメント・能動的な学習の三本柱（[[web-brame-2016-effective-educational-videos]]）
- 長さの業界データ（Wistia）は「説明（How-to・デモ）」を 1〜5 分に置く。測っているのは平均して何割見られたかだけで、理解ではない（[[web-wistia-video-length-engagement]]）

## 経験と並べる

| 経験 | 文献 | 関係 |
|---|---|---|
| 完全静止を既定にし、説明中の語・数値だけを強調する（[[exp-qualia-video]]） | coherence（g=0.33）、signaling（g=0.43）、Sanderson「動きには目的を」 | 同じ向き。ただし経験は 1 人の好みの評価で、研究が支えるのは「飾りの動きは効かない」まで。「静止の方が学習が上がる」ではない |
| 飾りの場面絵を 36% → 0%（[[exp-qualia-video]]） | 誘惑的な細部は出しっぱなしで害が大きい（g=0.43 対 一時的 0.12）（[[web-mayer-multimedia-principles]]）。Muller の「面白い話」は害も益も無し | 足したものの種類（画面の面積を取る絵か、話か）が違う |
| 画面に出す文と読み上げる文を分ける（[[exp-qualia-video]]） | Mayer の redundancy は 0.10 で速いペース条件付き。独立のメタ分析は音声に文字を足すと g=0.29（Adesope & Nesbit） | 経験は表記の分離とチャンネルの割り振りで、字幕は残している。文献から字幕を消す根拠は弱い。TTS の聞き違いを字幕が補う可能性 |
| 冒頭 1 分で目的・失敗・できることを示す（[[exp-qualia-video]]） | SoME の 30 秒、Common Craft の Why が先 | 同じ向き。秒数は違う（基準であって測った値ではない） |
| 主役を決めて尺を割く、2分52秒 → 47 秒（[[exp-gyazo-resumption-video]]） | Yum Yum「信じる理由を 1 つ」、Common Craft の語数の上限 | 同じ向き |
| 1 分解説シリーズの台本案の芯「放り込むだけ。整理は AI がやる」（[[exp-llm-wiki-explainer-series]]） | Muller の Refutation（誤解を先に言って否定する） | 型として逆。誤解を台本の材料にする案は未検証 |
| YouTube で解説形式より「一緒に唱える」形式が残った（[[exp-forest-misc-video-notes]]） | Muller の対話版の学生は「頭を使った」と答えた | 参加させる形が効く、と同じ方向にも読めるが、題材も測度も違う |

## Open Questions

- SoME の AI 方針は AI が生成した台本・ナレーション・AI の声を名指しで不可にしている（[[web-3blue1brown-exposition-advice]]）。西尾の制作の多くはこれに当たる。発信先によって AI の関与の開示がどこまで求められるか
- redundancy（字幕を足すな）の文献は割れている。日本語の TTS ナレーション＋字幕で測ったものは無い
- Wistia・Guo の「長さ」はどちらも視聴の測度。talk の長さを理解で測った研究は今回読めていない（Mayer, Fiorella & Stull 2020 "Five ways…" は未読）
