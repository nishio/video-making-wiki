---
type: source
summary: 撮った素材を Claude Code などのエージェントに編集させる実例 3 つ。browser-use の video-use（MIT、star 30,758、2026-04 作成・2026-10-08 まで更新）は「LLM は動画を見ず、単語ごとの時刻付きの文字起こしを読み、迷う所だけ映像の帯を画像で見る」設計で、方針の合意 → EDL → 書き出し → 切れ目ごとの自己点検を回す。video-editing-skill（2026-10-30）は検出を決まった規則に、判断（言い直し・脱線）をエージェントに分ける。Kapwing（2026-11-04、自社記事）は 70.7 秒のショートを約 42 分・API 費用 $9.92・手直し 0 で作ったと報告する。どれも使ったモデル名を書いていない
video_types: [promo, talk]
url: https://github.com/browser-use/video-use
author: Browser Use（video-use）／Frank Heijdenrijk・WoopSocial（video-editing-skill）／Emily Peng・Kapwing
published: video-use は 2026-04-12 作成、最終 commit 2026-10-08。dev.to の記事は 2026-10-30。Kapwing の記事は 2026-11-04
retrieved: 2026-11-09
sources:
  - https://github.com/browser-use/video-use（README.md、SKILL.md、helpers/transcribe.py、pyproject.toml、commits）
  - https://dev.to/fheijdenrijk/video-editing-skill-for-claude-code-an-agent-that-plans-every-cut-then-renders-with-ffmpeg-518a（2026-10-30）
  - https://github.com/social-media-skills/video-editing-skill（2026-10-30 作成、MIT）
  - https://www.kapwing.com/resources/how-to-edit-videos-with-claude-code-free-ai-video-editing-skill/（2026-11-04）
  - https://elevenlabs.io/docs/overview/capabilities/speech-to-text.md（Scribe v2 の言語と WER の区分）
  - https://elevenlabs.io/docs/overview/models.md（scribe_v1 は「outclassed by v2 models」）
  - https://elevenlabs.io/pricing/api（Scribe v2 $0.22/時間、2026-11-09）
---

# 撮った素材をエージェントに編集させた実例（video-use・video-editing-skill・Kapwing）

## 何の文献か

- **video-use**（Browser Use。ブラウザを操作するエージェントの会社）: GitHub の README・SKILL.md（Claude Code などの skill の本文、約 26KB）・文字起こしのスクリプト・依存。README は「Cloud-hosted video-use is coming」とクラウド版の waitlist に誘う。2026-04-12 作成で Opus 5.5 の公開（2026-09-22）より前からあるが、2026-09-24・10-08 にも更新がある。star 30,758（2026-11-09）
- **video-editing-skill**: 作者の dev.to 記事（2026-10-30）。作者は投稿サービス WoopSocial の関係者で、記事の末尾に開示があり、最後の手順は WoopSocial の MCP での投稿。repo は記事と同じ日に作られ star 1
- **Kapwing**: 動画編集サービス Kapwing の自社ブログ（2026-11-04、Emily Peng）。自社の MCP と、無料で配る skill（`/shorts-editor`）を紹介する記事で、宣伝の性格がある。結果の数字は 1 回の実験の自己申告
- 3 つとも、**どのモデル（Opus 5.5 など）で動かしたかを書いていない**（本文を「opus」「sonnet」「model」で検索して見当たらなかった）。既存の [[web-opus2-awesome-claude-5-5-videos]] などは「コードで描く」側の実例で、このページは「撮った素材を切る」側

## 書いてあること

### video-use（browser-use）

- 「Drop raw footage in a folder, chat with Claude Code, get `final.mp4` back」。できること: 言いよどみ（umm、uh、言い直し）とテイク間の空白を切る、区間ごとの色補正、「30ms audio fades at every cut」、字幕の焼き込み（既定は 2 語ずつの大文字）、HyperFrames・Remotion・Manim・PIL で作る重ねのアニメーション（1 つにつきサブエージェント 1 つを並列に）、書き出した結果の自己点検、`project.md` に次回のための記録
- **見る方法**: 「The LLM never watches the video. It **reads** it」
  - 層 1（常に読む）: ElevenLabs Scribe を素材ごとに 1 回呼び、単語ごとの時刻・話者・音の出来事（`(laughter)` など）を取る。全テイクを約 12KB の `takes_packed.md` にまとめる（0.5 秒以上の無音か話者の交代で区切った句ごとに `[002.52-005.36] S0 ...`）
  - 層 2（必要なときだけ）: `timeline_view` が指定区間のフィルムストリップ＋波形＋単語のラベルの PNG を作る。「Called only at decision points — ambiguous pauses, retake comparisons, cut-point sanity checks」
  - 「Naive approach: 30,000 frames × 1,500 tokens = 45M tokens of noise. Video Use: 12KB text + a handful of PNGs」
- 工程: 「Transcribe ──> Pack ──> LLM Reasons ──> EDL ──> Render ──> Self-Eval」。自己点検で問題があれば直して書き出し直す（最大 3 回）
- SKILL.md の工程: 目録（ffprobe・文字起こし）→ 問題の下見（言い間違いの一覧）→ 会話で聞く（種類・長さ・縦横比・残す所・切る所・字幕）→ **4〜8 文の方針を出して確認を待つ** → EDL を作る（テイク選びはサブエージェントに渡す）→ 720p のプレビュー → 自己点検 → 直す → `project.md` に追記
- 自己点検: 書き出した結果の**すべての切れ目の ±1.5 秒**を `timeline_view` で見て、映像の飛び・波形の跳ね・重ねに隠れた字幕を探す。最初と最後の 2 秒と途中 2〜3 か所も見る。`ffprobe` で長さが EDL と合うか。音は `ebur128` で測り「You cannot listen: say so, and report the numbers」。公開するもの（launch・promo・広告）には**批評役のサブエージェント**を 1 つ立て「Brief it to roast, not to praise」
- テイク選びのサブエージェントへの指示の形: 型（「Tech launch / demo: HOOK → PROBLEM → SOLUTION → BENEFIT → EXAMPLE → CTA」「Tutorial: INTRO → SETUP → STEPS → GOTCHAS → RECAP」など）、規則（単語の境界で切る、30〜200 ms の余白、400 ms 以上の無音を優先、尺を超えたら拍を落とす）、出力は `[{"source","start","end","beat","quote","reason"}]`
- EDL は CMX 3600 ではなく独自の JSON（`sources`・`ranges`・`grade`・`overlays`・`subtitles`・`total_duration_s`）
- 「Anti-patterns」に「Hand-tuned moment-scoring functions. The LLM picks better than any heuristic you'll write」「Running Whisper locally on CPU. Slow and it normalizes fillers. Use hosted Scribe」
- 切り貼りの決まり（Hard Rules）は [[web-edit-agent-moviepy-ffmpeg-concat]] に書いた
- 文字起こしのコード（`helpers/transcribe.py`）は `model_id: "scribe_v1"`、`timestamps_granularity: "word"`、`diarize: true`。ElevenLabs の models の docs は scribe_v1 を「First generation speech recognition (outclassed by v2 models)」と書く
- 依存: requests・librosa・matplotlib・pillow・numpy（Python 3.10 以上）、ffmpeg、ElevenLabs の API キー。インストールの説明は `brew install ffmpeg` で macOS 向けに書かれている

### video-editing-skill（dev.to、2026-10-30）

- 「the agent does the reading and judging」、3 つの Python スクリプトが ffmpeg と Pillow で決まった仕事をする。流れは文字起こし（単語の時刻）→ エージェントが全文を読み `edit.json`（切る区間と理由・残す区間・置換・章）→ `--plan` で `edit-plan.md` → **人が承認** → 書き出し（mp4・SRT・章・`cuts.jpg`・レポート）→ エージェントが `cuts.jpg` と警告を見る
- 「Transcript-driven editing quietly breaks when the transcript is too clean」: OpenAI の文字起こしは言いよどみを省くことがあるので、言いよどみ入りのプロンプトを渡す。固有名詞は `--terms` で渡し、なお間違えたら `replace`（例「Cyrus Rex」→「OSIRIS-REx」）
- 自動で切るもの: 言いよどみ（um、uh ほか。隣の語とくっついていなければ）、どもり、言い直しの合図（「let me say that again」など）、途中で止めて言い直した断片。**自動で切らないもの**: 書き出しが同じ 2 文（「Possible retakes」。エージェントと人が 1 つずつ決める）、「like」「so」などの口癖（opt-in）。脱線・「聞こえますか」・前置きの長さはエージェントが `cut` に理由付きで足す
- 間は消さずに縮める（youtube の型: 0.50 秒を超える間を、文中 0.30・文の後 0.45・長い間 0.90 秒に）。「a dozen tiny cuts save a few seconds and make the video look nervous」ので 0.40 秒未満の削除はしない
- 1 秒以上削った切れ目では 1.1 倍の寄り（punch-in）で飛びを隠す。目線を画面の高さ 38% に固定、最大 1.2 倍。画面収録では `"punch_in": 0`
- 例: NASA の公開インタビュー 6:39 → 5:57、12 カット。「9 s from inside the talking, 34 s from long gaps, cards, opening and ending」と、話の中から削った分と周りから削った分を分けて報告する
- `cuts.jpg`（大きな切れ目の前後のコマを並べた画像）を見るのは「instead of claiming it watched the whole video」

### Kapwing（自社記事、2026-11-04）

- Claude Code に素材・ブランドの素材・効果音・**過去に公開したショート 3〜10 本**を渡し、`/shorts-editor learn my style from ./references` で `layout-guide.md`（配置・出る時刻・長さ・トランジション）を作らせてから編集させた
- 結果（同社の表）: 70.7 秒、編集と書き出しで約 42 分、「Reported API cost $9.92」（Claude Code の API の定価での見積もり）、1080×1920、98 クリップ・13 トラック、効果音 18、-14 LUFS、「Manual edits after export: 0」。過去に公開した同じショートの完成版は参考から外したと書く
- 自己点検で見つけて直したもの: 名前の重複で全画面の話者のショットが 49 秒間レイアウトを覆っていた、切り抜いた人物に壁のランプが入り髪が欠けた、文字がカードの端からはみ出た、話の静かな所で音楽が大きすぎた
- 「this was a single controlled experiment using a prepared folder of assets and a custom skill. It doesn't mean Claude will produce a publish-ready video from any collection of footage without supervision」
- 助言: 画面収録は手順・話題ごとに別のファイルに分けて撮る（話と映像を対応させやすい）。音楽は使う権利があるものだけ。Whisper は固有名詞（「Kapwing」）を間違えた

## 何を AI に任せられるか

| 作業 | 作り手が「任せられる」と書く | 実例で確かめられた（作り手の報告） |
|---|---|---|
| 言いよどみ・言い直し・空白の削除 | 3 つとも | NASA の例（12 カット）、Kapwing のショート |
| テイク選び（同じ文の複数テイク） | video-use（サブエージェント） | 記録なし |
| 脱線・前置きの削除 | video-editing-skill（エージェントが理由付きで） | NASA の例 |
| 字幕・章 | 3 つとも | NASA の例（SRT・章）、Kapwing |
| 重ね・アニメーション・B-roll の配置 | video-use、Kapwing | Kapwing（98 クリップ・13 トラック） |
| 自分の出力の点検（切れ目のコマ・音量） | 3 つとも | Kapwing（4 つの問題を見つけて直した） |
| 過去の作品から型を学んで真似る | Kapwing | Kapwing の 1 回 |

## 何が人の判断として残るか

- **方針の合意**: video-use は方針（4〜8 文）を人が承認するまで切らない（Hard Rule 11）。video-editing-skill は `edit-plan.md` を人が承認してから書き出す
- **紛らわしい言い直し**: video-editing-skill は「書き出しが同じ 2 文」を自動では切らず、人と決める
- **通しで見ること**: Kapwing は「You should still watch the finished MP4 before publishing ... it can't reliably judge every creative decision」。video-use は「You cannot listen」と数字で報告させる。video-editing-skill の `cuts.jpg` は「全部見たと言わない」ための仕組み
- **権利**: Kapwing は音楽の使用権を人が確かめるよう書く

## 日本語の対応

- video-use の文字起こし（ElevenLabs Scribe v2）は日本語を「Excellent (≤ 5% WER)」の区分に入れている（ElevenLabs の docs）。ただし docs は日本語を「languages that don't use spaces」として扱い、**単語ごとの時刻が日本語で何の単位（文字か形態素か）になるかは書いていない**。video-use の「単語の境界で切る」「句は 0.5 秒の無音で区切る」が日本語でそのまま効くかは未確認。video-use のコードは古い scribe_v1 を呼んでいる
- video-editing-skill の言いよどみ・口癖の一覧は英語（um、uh、like、so）。日本語の「えー」「あの」は入っていない。経験の [[exp-shortmovie-draft-generator]] も日本語のフィラーの除去でつまずいていた（正規表現が効いていない）
- Kapwing の記事は英語の素材だけ

## 費用・アカウント・利用条件

- video-use: MIT。**要: ElevenLabs の API キー**（Scribe v2 は $0.22/時間、2026-11-09 の価格ページ）。ElevenLabs の基本の利用規約は Free の利用を非商用に限る（[[web-means-sound-suno-udio-elevenlabs-music-terms]]）。会社の素材を ElevenLabs に送るかは西尾が決める。STT の入力が学習に使われるかの条文は今回読んでいない
- video-editing-skill: MIT。文字起こしは既存の字幕・Groq/OpenAI の API（「Groq is about $0.04 per audio hour」）・ローカルの faster-whisper（「Free, private」）から選べる
- Kapwing: skill は無料配布（ZIP）。Claude Code の API 費用は 1 本 $9.92（同社の見積もり）。Kapwing MCP は Kapwing のアカウントとプランのクレジット。素材を Kapwing に上げる。規約は未読
- Claude Code の利用料（サブスクリプションか API）は別

## この wiki への含意

- **「LLM は見ずに読む」は経験と同じ設計**: [[exp-shortmovie-draft-generator]] は字幕（時刻付きの文字）だけを LLM に渡して切り抜きを選ばせた。video-use はそれに「迷う所だけフィルムストリップの PNG を見る」と「書き出した後に切れ目を見て直す」を足した形。経験の道具には書き出し後の点検が無かった
- **経験と食い違う点**: (1) 経験は「タイムスタンプは字幕データを正とし、LLM には触らせない」で、LLM には区間を選ばせるだけだった。video-use は LLM に秒（`start: 2.42`）を書かせ、規則（単語の境界・余白）で縛る。どちらが日本語で壊れにくいかは未確認。(2) 経験の「カットの終わりを 3 秒延ばす」は、文献の余白（30〜200 ms、Out は最大 250 ms）より 1 桁大きい
- **人が編集した THINKLET（[[exp-thinklet-reading-demo-video]]）と並べる**: 西尾がやったのは「処理待ちの 30 秒に、待ちの説明のナレーション 3 本を当てる」編集で、言いよどみの削除ではない。3 つの実例はどれも「話した素材を詰める」編集で、**実機の待ちをどう見せるかという判断**（待ちを削らず説明に変える、[[work-promotion-video]] の「時間と因果を偽らない」）はどの道具の規則にも無い。エージェントに任せると、空白として詰められる側に入る（推測）
- **Mac 側の解説動画の合成（ffmpeg の overlay で THINKLET のデモと Gyazo の動画を枠に重ねた `compose.py`）**: この機械には `~/video-making-explainer` が無く読めない。video-use の重ねの決まり（重ねは PTS をずらす、字幕は最後）と照らすのは Mac 側で
- **promo の批評役**: video-use の「公開するものには批評役のサブエージェントを立て、褒めずに叩かせる」は、第 3 回の批評役（[[web-means-critic-gemini-video-understanding]]）を編集の工程に組み込んだ形。ただし video-use の批評役は Claude（音を聞けない）で、Gemini のように音を入れて聞く役ではない

## 着手の仕方（未検証。galleria で確かめる）

- **何ができるようになるか**: 西尾の講演の録画（例: LT の録画）を Claude Code に渡し、言いよどみと空白を詰めた下書きと、切れ目ごとの点検画像を出させる。効く型: talk（講演の詰め）、promo（切り抜き）
- **機械**: galleria WSL。入れるもの: video-use（git の repo を `uv sync`。依存は librosa など）、ffmpeg（既にある）。**要: ElevenLabs の API キーと費用（西尾が決める）**。キー無しで試すなら video-editing-skill のローカルの faster-whisper の道（GPU 要・VRAM の見込み数 GB、根拠: 推測。[[web-check-subs-whisperx-stable-ts-faster-whisper]]）
- **成熟度**: video-use は 2026-10-08 が最後の commit、star 30,758。video-editing-skill は 2026-10-30 作成で若い
- **最小の手順**（video-use の README の Manual install を WSL に置き換えた。brew の行は apt で既にある ffmpeg に置き換え、推測）:
  ```bash
  mkdir -p ~/video-tools-trial/agent-edit && cd ~/video-tools-trial/agent-edit
  git clone https://github.com/browser-use/video-use ~/video-tools-trial/video-use
  ln -sfn ~/video-tools-trial/video-use ~/.claude/skills/video-use
  (cd ~/video-tools-trial/video-use && uv sync && cp .env.example .env)   # .env に ELEVENLABS_API_KEY（西尾が用意）
  mkdir footage && cp /path/to/lt-recording.mp4 footage/
  cd footage && claude   # 「この録画の言いよどみと長い間を詰めて、5 分以内の下書きにして。方針を先に出して」
  ```
  キー無しの代わり（video-editing-skill。記事の install の行）: `npx skills add social-media-skills/video-editing-skill -g -a claude-code -y`、文字起こしは `pip install faster-whisper`（記事の「Local」の道）
- **動いたと言える確かめ方**: (1) `footage/edit/` に `takes_packed.md`・`edl.json`・`final.mp4`（か `preview.mp4`）・`project.md` ができる。(2) Claude Code が方針を出して承認を待った（会話のログ）。(3) `edl.json` の `total_duration_s` と `ffprobe final.mp4` の長さが 1 コマ以内。(4) `edit/verify/` に切れ目の点検画像があり、Claude Code が `ebur128` の数字を報告した。(5) 日本語で: `takes_packed.md` の 1 行が何文字・何秒の単位になっているか（単語ごとの時刻が日本語で効いているか）を記録。(6) 西尾が通しで見て、切りすぎた所（文末の間・言いかけの言葉）を時刻で 3 つ書く
- **所要の見込み（推測）**: インストールと 1 本目で 1〜2 時間。10 分の録画で文字起こしは数分、ElevenLabs の費用は 10 分で約 $0.04（$0.22/時間から）

## Open Questions

- 3 つとも使ったモデルを書いていない。Opus 5.5 以後で編集の質が変わったかは、この文献から言えない（grasp-nishio の「動画ではモデル名を明示する」の観点では、どの実例も条件が不足）
- ElevenLabs Scribe の日本語の「単語ごとの時刻」の単位と精度。video-use の 0.5 秒で句を切る規則が日本語の話し方に合うか
- 「LLM に秒を書かせ規則で縛る」（video-use）と「LLM には区間の番号だけ選ばせる」（経験）のどちらが壊れにくいか
- 実機の待ち・沈黙を「説明に変える」編集（THINKLET）は、どのエージェントの規則にも無い。指示で頼めば扱えるのか、空白として詰められるのか
- Kapwing の「手直し 0」は同社の 1 回の実験。何本試して 1 本を出したかは書かれていない

