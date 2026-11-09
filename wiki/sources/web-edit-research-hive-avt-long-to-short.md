---
type: source
summary: 長い動画から短い動画を自動で切り出す 2 本。HIVE（EMNLP 2025 Industry、ByteDance ほか）は、文字起こしだけを LLM に渡して区間を一発で選ばせる方式（FunClip などの方式）では場面の変わり目が唐突になると指摘し、場面に分けてから見どころ・冒頭と結末・不要な場面の削除の 3 段に分けた。人の編集との差は縮んだが、途切れずに見られる長さ（Smoothness）は人の 6.84 に対し 4.48 で残った。Agent-based Video Trimming（2024-12、Insta360 ほか）は利用者の撮った 10 分の素材を GPT-4o で説明文にして無駄な映像を捨て、物語の順に並べ直した（17 人の盲検で既存の見どころ検出より上）
video_types: [promo, talk]
url: https://arxiv.org/abs/2507.02790
author: Xiangfeng Wang, Xiao Li ほか（HIVE。中国科学技術大学・ByteDance）／Lingfeng Yang, Zhenyuan Chen ほか（AVT。南京理工大学・南開大学・Insta360）
published: 2025（HIVE。arXiv v1 2025-07、v2 2025-10-03、EMNLP 2025 Industry Track）、2024-12-12（AVT、arXiv v1）
retrieved: 2026-11-09
sources:
  - https://arxiv.org/abs/2507.02790（From Long Videos to Engaging Clips: A Human-Inspired Video Editing Framework with Multimodal Narrative Understanding。v2 の本文を読んだ）
  - https://aclanthology.org/2025.emnlp-industry.185.pdf（同、EMNLP 2025 Industry の版。検索結果で所在を確かめただけで、本文は arXiv 版を読んだ）
  - https://huggingface.co/datasets/wonderful9462/DramaAD（DramaAD データセット。所在のみ確認、利用条件は読んでいない）
  - https://arxiv.org/abs/2412.09513（Agent-based Video Trimming。v1 の本文を読んだ）
  - https://github.com/ylingfeng/AVT（AVT のコード。2026-11-09 時点で GitHub の API にライセンスの記載なし、最終 push 2025-01-20）
---

# HIVE と Agent-based Video Trimming（長い動画から短い動画を切り出す）

## 何の文献か

- **HIVE**: EMNLP 2025 の Industry Track（産業応用の査読部門）の論文。著者の大半が ByteDance。短尺ドラマの広告用の切り抜きという、実際の業務の需要から出発している
- **AVT**: arXiv のプレプリント。共著者に Insta360（カメラの会社）。利用者が撮った長い素材（日常・スポーツ・旅行の vlog）を短くする課題
- 2 本とも、[[exp-shortmovie-draft-generator]] と同じ「長い動画 → 短い動画」の問題を扱う。ただし素材は、HIVE は台詞のある短尺ドラマ、AVT は話の少ない vlog で、講演ではない

## 書いてあること

### HIVE（Wang ら 2025）

- 既存の方式への批判（1 節）: FunClip（ModelScope）や AI YouTube Shorts Generator のような LLM の方式は、**音声認識の文字起こしを LLM に渡し、どの区間を使うかを一発で予測させる**。これは (1) 表情・身振りなど映像の手がかりを見落とし、(2) プロンプトの工夫だけで区間を選ぶので、**ショットの変わり目が唐突になり、見る体験を損なう**、と書く
- 仕組み（3 節）: ショットの境界を検出（AutoShot）→ Qwen2-VL で各ショットを記述 → Gemini 2.0 Flash で同じ場面のショットをまとめる（ショットより大きい「場面」の単位で切る）。人物の抽出・台詞の分析・物語の要約を MLLM でする。編集は、プロの広告編集者に聞いた手順を 3 つの小課題に分ける: **見どころの検出 → 冒頭と結末の選択 → 筋に関係の薄い場面の削除**。冒頭と結末の候補の評価と削除の判断は GPT-4o（プロンプトは付録に全文）
- データ（4 節）: DramaAD。短尺ドラマ 2,582 話（1 話 1〜3 分、作品あたり平均約 40 分、縦 9:16・1080p）と、**プロが編集した広告用の切り抜き 500 本以上**。素材は著作権者の許諾を得た、プロの編集は 1 本約 30 分かかった、と書く（倫理の節）
- 測度（4.3 節）:
  - Diversity（同じ素材から作る複数の切り抜きの違い）
  - **Smoothness**（不自然・唐突な変わり目が来るまでの平均の分数）
  - **Engagement**（見る人に、つまらなければ 2 倍速にするか飛ばしてよいと伝え、等速で見た割合）
  - VEI = Engagement × Smoothness
  - 広告向けに Hook Rate（冒頭で止まって見るか）と Suspense Rate（結末で続きを見たくなるか）
  - 評価した人の人数・属性は、本文に見つけられなかった
- 結果（表 2。素材は 220 話から選んだ約 10 話・20〜30 分の筋）:

  | | Diversity | Smoothness | Engagement | VEI | Hook | Suspense |
  |---|---|---|---|---|---|---|
  | 人の編集（正解） | 0.74 | 6.84 | 0.93 | 6.35 | 0.87 | 0.91 |
  | 文字起こしで一発（ASR） | 0.75 | 0.65 | 0.82 | 0.54 | 0.64 | 0.47 |
  | 場面の記述で一発 | 0.48 | 1.28 | 0.88 | 1.14 | 0.62 | 0.52 |
  | HIVE | 0.66 | 4.48 | 0.89 | 4.01 | 0.71 | 0.73 |

  - 文字起こしで一発の方式は、違いの多い切り抜きを作るが、**唐突な変わり目が 1 分に 1 回以上**（Smoothness 0.65 分）。著者は「産業での使い道を限る」と書く
  - 冒頭と結末を無作為に選ぶと Hook と Suspense が 0.28・0.30 に落ちた（切り抜きの効き目は**冒頭と結末の選び方**に強く依る）
- 限界: 回想や時系列を崩す語りには対応しない。場面の単位はショットより粗く、編集の自由が減る。**人の編集に比べ、Diversity と Smoothness でまだ劣る**

### Agent-based Video Trimming（Yang ら 2024）

- 課題（1 節）: 見どころの検出は「区間を選ぶ」だけで、区間どうしのつながりや並べ方を見ない。そこで「Video Trimming」を、**無駄な映像の検出 → 価値のある区間の選択 → 筋の通る並べ方**、と定義した
- 仕組み（3 節）: 素材を短い区間に切り、GPT-4o で各区間を構造化した説明文にし（内容と、ぶれ・暗さなど無駄の度合い）、無駄な区間を捨て、配置役のエージェントが物語の順に並べる（**撮った順に並べるとは限らない**）。冒頭と結末は、目立たなくても入れる
- データ: YouTube から集めた利用者の動画 42 本（30 話題、平均 10 分）に、区間ごとに「無駄・曖昧・普通・見どころ」の 4 段階の注釈
- 人の評価（表 1）: 17 人の盲検、1〜10 点、30 本の完成版。AVT は素材の豊かさ 7.21、魅力 7.78、興奮 5.57、無駄の少なさ 6.72、総合 7.15 で、既存の見どころ検出（UniVTG 総合 6.30、UVCOM 6.23）より高い。**人の編集とは比べていない**
- コードとモデルは公開と書く（ylingfeng.github.io/AVT → github.com/ylingfeng/AVT）

## この wiki への含意

- **[[exp-shortmovie-draft-generator]] はまさに「文字起こしを LLM に渡して区間を選ばせる」方式**（Whisper／YouTube 字幕 → GPT-4o／o3 → 開始・終了時刻）。HIVE はこの方式を比較の基準に置き、**唐突な変わり目が多い**と測った。あの道具が「基本は連続した一区間、中抜きは 1 つまで」にしたのは、この弱さを避ける設計に読める（推測）。講演の切り抜きは映像の変化が少ないので、ドラマほど唐突さは目立たない可能性もある（推測）
- **冒頭と結末を別の欄で書かせる**（[[exp-shortmovie-draft-generator]] の `first_impact` と `last_conclusion`）は、HIVE の「冒頭と結末の選択を独立した段にする」と同じ考え。HIVE では、冒頭と結末を無作為にすると Hook と Suspense が半分以下に落ちた。**西尾の道具の設計は、この研究で効くと測られた所を押さえていた**（ただし HIVE の測度は短尺ドラマの広告で、講演の切り抜きでは測っていない）
- **promo（SNS の短尺）に一番効く**。HIVE の Hook／Suspense は SNS の広告の指標で、[[exp-shortmovie-draft-generator]] のプロンプトの「冒頭 2 秒」「視聴時間」と同じ方向を見ている
- **talk の切り抜きへの当てはめには注意**: どちらも講演・解説を素材にしていない。講演では「話の途中で切らない」（[[web-edit-research-transcript-editing-lineage]] の Berthouzoz 2012）が先に効き、映像の場面の区切りはあまり役に立たない（スライドが変わる所が場面の区切りに当たる、という対応は推測）
- AVT の「撮った順に並べるとは限らない」は、作品紹介の素材（画面収録の断片）を並べ直す promo には使える考え方。ただし時間と因果を偽らない（[[work-promotion-video]] の規約の節）こととの兼ね合いがある（推測）

## 着手の仕方（未検証。galleria で確かめる）

- **HIVE: コードの公開は見つけていない**（データセット DramaAD は Hugging Face で公開。利用条件は読んでいない。中身は中国語の短尺ドラマと推測され、この wiki の用途には合わない）
- **AVT: コードの公開あり**（github.com/ylingfeng/AVT）。ただし 2026-11-09 時点で GitHub の API にライセンスの記載が無く、利用条件は読めない。最終 push 2025-01-20 で、更新は止まっている。GPT-4o（OpenAI の API キーと費用）を使う設計（要: API キー・費用。西尾が決めること）。README は読んでいないので、最小の手順は書かない
- 考え方を借りるなら、[[exp-shortmovie-draft-generator]] の 2 の流れ（Whisper → 企画 5 案）に、(1) 区間の端を無音・文の終わりに寄せる、(2) 冒頭候補と結末候補を別々に挙げさせて人が組み合わせる、を足す形が一番近い（推測。この 2 点の効果は講演では測られていない）

## Open Questions

- HIVE の Engagement・Hook・Suspense を誰が何人で測ったかが本文に無い（付録を含む全文を「participants」「viewers」などで検索したが見つけられなかった）。数値の重みは割り引いて読む
- HIVE の Smoothness で、人の編集が 6.84 分あたり 1 回の唐突な変わり目を持つ、という前提の測り方（誰が「唐突」と判断したか）が不明
- 講演・LT の録画で、文字起こしだけで区間を選ぶ方式がどれだけ唐突さを生むかは、どの研究も測っていない
