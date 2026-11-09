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

## Updates

### 2026-11-09 第 2 回サーベイから

- Opus 5.5 期に、ナレーション付きの 1〜12 分の解説が多数作られた。**ナレーションを時計にする**（声の実際の長さで切れ目を決める）作り方が広がり、作り手は「モデルは聞けない・通しで見られない」と書いて、文字起こしでの読みの照合・機械検査・人が聞くことで補っている（[[after-opus55]]）
- 外の解説（Zenn・HyperFrames）は解説でも連続したカメラの動きを推していて、[[exp-qualia-video]] の「完全静止を既定」と食い違う。IBM の「込み入るほど動きは小さく」は静止の側を支える（[[design-fundamentals]]）
- 学会は 30 秒の preview（広める）と video figure（理解させる）を別の動画にしている。技術の詳細を伝える talk は、広める promo と分けて作るのが作法（[[web-promo2-uist-chi-video-guides]]、[[work-promotion-video]]）
- 字幕の数字（日本語 1 秒 4 字・1 行 13 字など）は [[design-fundamentals]]

### 2026-11-09 第 3 回サーベイから

- ナレーションの尺は 6〜7 モーラ／秒で見積もれる（JLPT の聴解で N1 は 7.07、日常会話の平均は約 6.6。[[web-check-ja-speech-rate-mora]]）
- 日本語字幕の速さの研究: 1 秒 6 字までは視線の負荷が変わらず、8 字で増えた（豊倉・山田 2017、視線は 5 人。[[web-check-ja-toyokura-yamada-2017-subtitle-4-chars]]）
- 描く過程を見せるホワイトボード・アニメは、同じ音声のスライドより得点が高かった（Türkay 2022、299 人、止められない条件。[[web-nonscreen-rsa-animate-turkay-2022-whiteboard]]）。video abstract の研究では、理解を上げたのは主に台本の平易さだった（[[web-nonscreen-zong-bonnevie-bredbenner-video-abstract-studies]]）
- 批評役のモデルには映像と音を両方見せる。文字起こしだけだと人との相関が 0.84 → 0.23 に落ちた。一番効くのはナレーションの事実の誤りの指摘（[[web-means-critic-edupanel-paper2video]]）
- 台本を AI が書くこと、コードで描くこと、字幕は、YouTube では開示不要と例示されている。AI の声は配信先で扱いが割れる（[[web-rights-youtube-genai-disclosure]]、[[web-rights-tiktok-meta-aigc-labels]]）

### 2026-11-09 解説動画 3 本の経験から

- この型で 2026-11-09 に 3 本作って公開した経験のページ: [[exp-explainer-video-2026-11]]（本編「動画の作り方 2026年11月」とプロセス動画）、[[exp-tsugigami-making]]（tsugigami の広告動画のメイキング）
- 3 本の作業場のファイルから、台本 → 事実確認 → 声 → 時刻表 → 描画 → 引用の重ね → 検査 → レビューの受け取り → 公開の順の手順を書いた: [[talk-video-making-2026-11]]。各手順に、何本で確かめたかを付けている
- 3 本の比較（使い回せたもの、毎回直しが入った所）: [[talk-three-videos-2026-11]]。読み、引用の選び方と見せ方（修正前を見せる）、言い方には 3 本とも西尾の直しが入った
