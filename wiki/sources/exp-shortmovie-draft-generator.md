---
type: source
summary: 長尺の講演・対談動画から切り抜きショート動画の企画とカット案を LLM に作らせる道具 2 つ（team-mirai-volunteer の公開 repo、2025-06〜07）。字幕のタイムスタンプを正として LLM には文字だけ直させる、という分担と、冒頭 2 秒・視聴時間を軸にしたプロンプトが要点
video_types: [promo]
sources:
  - ~/shortmovie-draft-generator（github.com/team-mirai-volunteer/shortmovie-draft-generator）README.md, CLAUDE.md, CLI_README.md, src/agent_sdk/agents_registry/youtube_scenario.py, src/agent_sdk/schemas/youtube.py, src/lib/youtube/video_processing.py, src/lib/youtube/transcript_extraction.py, src/cli.py
  - ~/shortmovie-draft-generator 西尾の commit f0ad5de「3秒延長」、35a318e、c929cf7、7bf5781（2025-07-08）
  - ~/shortmovie-draft-generator2（github.com/team-mirai-volunteer/shortmovie-draft-generator2）README.md, project/summary.md, tasks/*.md, src/builders/prompt_builder.py, src/clients/whisper_client.py, src/service/srt_generator.py（最終 commit 138516d, 2025-07-10）
---

# 切り抜きショート動画の下書き生成（shortmovie-draft-generator 1 と 2）

## 何を作ったか

どちらも「長い動画 → 切り抜きショート動画（1 分程度、最大 90 秒）の企画書とカット案」を作る道具。完成動画を作るのが主目的ではなく、**人が編集するための下書き**を出す。

| | 1（shortmovie-draft-generator） | 2（shortmovie-draft-generator2） |
|---|---|---|
| 入力 | YouTube の URL | 手元の動画ファイル 1 本 |
| 文字起こし | YouTube の字幕を `youtube-transcript-api` で取得（ja → en の順） | 音声を抜いて OpenAI Whisper API（`whisper-1`、`verbose_json`、セグメント単位のタイムスタンプ） |
| 企画を作る LLM | エージェント（既定 `o3`、ツールで企画案・カットの追加/更新/削除） | ChatGPT API に 1 回投げて JSON を受ける（README の既定 `gpt-4o`） |
| 画面 | Streamlit（ログイン付き）＋ CLI | CLI のみ |
| 出力 | 企画案・カット・補正字幕、ffmpeg で縦動画も作れる | 企画書 Markdown（5 案）＋ SRT 字幕 |

- 1 は他の開発者が 2025-06-22 に始め、西尾が 2025-07-08 に 4 commit（`.env.local` 読み込み、black 整形、コード整理、**カットの終わりを 3 秒延ばす指示**）を入れた
- 2 は別の開発者が 2025-07-10 に作った。設計書（`tasks/`）を先に書き、Phase ごとに Devin に実装させて PR でまとめる進め方（git log）。西尾の commit はなく、西尾の手元で回した出力が `output/` に残っている（中身は扱わない）
- どちらも、出力が実際の切り抜き動画にどう使われ、どう受けたかの記録は見当たらない（forest を「shortmovie|切り抜き動画|ショート動画」で検索、2026-11-09）

## パイプラインの骨格

**1（URL 入力）**: yt-dlp で 720p を取得 → YouTube 字幕を取得 → 文単位に分割・句点まで結合・置換辞書で補正 → エージェントが企画案 5 本を作る → 人が選ぶ → エージェントがカット区間を作る → ffmpeg で切り出し、縦 1080×1920 の黒地の中央に横動画を置き（`scale` 1080 幅に収めて `pad`）、concat でつなぎ、字幕を焼き込み（`Fontsize=48, Outline=3, MarginV=120`）、任意で BGM を音量 0.2 で混ぜる（`video_processing.py`）

**2（ファイル入力）**: ffmpeg で音声を mp3・モノラル・16kHz・64kbps に落とす（Whisper API の 25MB 上限に収めるため）→ Whisper でセグメント付きの文字起こし → 全文と「番号・[hh:mm:ss - hh:mm:ss]・本文」の一覧をプロンプトに埋める → JSON で 5 案（冒頭のフレーズ、最後の結論、主題、開始・終了時刻、タイトル 30 字以内、SNS 用キャプション 100 字以内、要点 3 つ）→ Markdown と SRT に書く

## 企画を作るプロンプトの中身（両方に共通）

両 repo のプロンプトに、ほぼ同じ「ショート動画を作る主なポイント」が入っている（出典は書かれていない。下は要点の抜き出し）:

- **冒頭 2 秒でインパクトを出す**: 見るのはフォロワー以外の「通りすがりの人」。丁寧な挨拶は不要で、最初の数秒で面白いと思わせないとスクロールされる。「伸びている動画の9割はファーストビューを意識している」とする。冒頭 2 秒は YouTube のサムネイルにあたる
- **視聴時間を伸ばす**: 「アルゴリズムの7割が視聴時間」「すべては視聴時間に行き着く」とする。3 秒目以降も離脱させないよう、5〜10 秒程度で話を切り替えたりカットを変えたりする。終盤は視聴時間への寄与は少ないが、共感・感動・オチがあると満足度が上がる
- 企画の項目として `first_impact`（最初の 2 秒のフレーズ）と `last_conclusion`（最後に来る結論・学び・オチ）を**別の欄で必ず書かせる**。主題は「○○は○○なので○○である」の形
- 尺は 90 秒以内、理想 60 秒。基本は連続した一区間、**中抜きは 1 つまで**（1 のプロンプト）
- 2 のプロンプトには「動画の中で話している内容に肯定的な内容になるようにしてください」とある（切り抜きが話者に不利な文脈を作らないための指定と読める。意図の説明は repo にない）

これらの数字（7 割、9 割）はプロンプトの記述で、この repo で検証されたものではない。

## うまくいった設計（コードから読める判断）

- **タイムスタンプは字幕データを正とし、LLM には触らせない**。1 のプロンプトは「元のchunkのタイムスタンプは絶対に変更しない」を繰り返し、OK 例・NG 例まで付けている。LLM がやってよいのは、フィラー（「あー」「えー」）の除去、てにをはの調整、固有名詞の誤変換の修正、読点・改行の追加だけで、語調は変えない。切り抜きの時刻を LLM が作文するとずれる、という問題への対処と読める
- **加工前の字幕を使わせる**: 補正済みの字幕（`processed_transcript`）ではなく生の `transcript_chunks` でカット時刻を決めさせる
- **字幕 1 枚は改行を除いて 60 字まで**（`schemas/youtube.py` の検査。2 行表示を想定）
- **固有名詞の置換辞書を手で持つ**: 自動字幕がよく間違える語（組織名・人名・専門語）を辞書で直す（`fix_transcript_text`）
- **カットの終わりを 3 秒延ばす**（西尾の commit f0ad5de）。動画の長さを超えない範囲で、全カットの `end_time` に 3 秒足すようプロンプトに書いた。理由は commit に書かれていない
- **縦動画への変換は「縮めて黒帯」**: 横の講演動画を切り取らず、1080 幅に縮めて縦キャンバスの中央に置く。話者が画面の端にいても切れないが、画面の大半が黒になる

## 詰まったこと・落とし穴（コードから読めるもの）

- **YouTube からの取得が壊れやすい**: 1 の git log は 2025-06-25〜07-01 に Cookie、PO トークン（`yt-dlp-get-pot-rustypipe`、`rustypipe-botguard`）、Dockerfile の修正が続いている。URL を入力にすると、取得の側の保守が仕事の大半になる
- **Whisper API の 25MB 上限**: 2 は音声だけを低ビットレートのモノラルに落として回避している。それでも長い動画では上限を超えうる（超えたらエラーにする実装）
- **CLI 版の企画生成は仮実装**: 1 の `src/cli.py` の `_generate_scenarios` は「For now, create a simple mock」で、動画を等分した区間を返すだけ。AI の企画は Streamlit 版でしか動かない
- **フィラー除去の正規表現が効いていないように読める**: `fix_transcript_text` は `r"\bあ\b"` などをキーに持つが、正規表現として扱う分岐は文字列が `r'` で始まる場合だけなので、これらは普通の文字列置換になり、一致しない（コードを読んだだけで、実行して確かめてはいない）
- **字幕は YouTube の chunk 単位**: 字幕の区切りは YouTube 側の chunk のままなので、ショート動画として読みやすい長さになるとは限らない

## 西尾の関わりとフィードバック

- 西尾が 1 に入れた変更は上の 4 commit。内容上の判断は「3 秒延長」だけで、理由の記録はない
- 西尾がこの道具の出来をどう評価したかの記録は、forest にも repo にもない

## 再利用できる部品

- 企画のプロンプト: `~/shortmovie-draft-generator2/src/builders/prompt_builder.py`（JSON 形式の企画 5 案。項目の立て方がそのまま使える）
- エージェント版の指示と字幕補正の規則: `~/shortmovie-draft-generator/src/agent_sdk/agents_registry/youtube_scenario.py`
- 縦動画化・字幕焼き込み・BGM の ffmpeg の組み方: `~/shortmovie-draft-generator/src/lib/youtube/video_processing.py`
- Whisper 用の音声の落とし方: `~/shortmovie-draft-generator2/src/clients/whisper_client.py`

## Open Questions

- 「3 秒延長」は何を直したかったのか。YouTube 字幕の chunk の終わりが発話の終わりより早いのか、切り抜きの終わりに余韻が要るのか
- 黒帯の縦動画と、話者に寄せて切り取る縦動画のどちらがショートで見られるか。repo には比較がない
- 「冒頭 2 秒」「視聴時間」を軸にした規則は、promo の型には合うが、talk（解説プレゼン風）の切り抜きにもそのまま当てはまるか。make-money の YouTube の数字では、解説形式より「一緒に唱える」形式の方が残った（[[exp-forest-misc-video-notes]]）

## Updates

### 2026-11-09 動画編集を AI にさせる方法のサーベイから（[[ai-editing]]）

- 2026-10 の切り抜きの道具（OpenShorts・Klap・video-use）も、同じ「時刻付きの文字起こし → LLM が区間を選ぶ。時刻は文字起こしを正にする」骨組みだった。冒頭と結末を別の欄にしたのは HIVE（EMNLP 2025 Industry）で効くと測られた所（[[web-edit-research-hive-avt-long-to-short]]）
- 食い違い: 終わりの延長 3 秒は、OpenShorts の最大 0.45 秒、auto-editor の margin 0.2 秒より一桁大きい。この道具には、書き出し後の点検・端の fade・語の境界への吸着が無い（[[ai-editing]]）
