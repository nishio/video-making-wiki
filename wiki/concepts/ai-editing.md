---
type: concept
summary: 西尾の言葉「動画編集をAIにさせる」の横断の整理（2026-11-09 時点）。撮った素材（画面収録・カメラ・講演の録画・既存の動画）の編集を AI に任せる方式を 5 つ（テキストで編集する道具、自動カットの OSS、長い動画からの切り抜き、LLM のエージェント、素材の中身を見る役）に分け、何を任せられるか・何が人に残るか・型への効き方・機械・費用・日本語・最小の始め方で並べた。どの方式も骨組みは「時刻付きの文字起こしを正にして、LLM は区間を選ぶ」で、研究とベンチマークではペース・筋・ショット選びが 2026 年秋でも人に及ばない。手順はすべて未検証（galleria で確かめる）
video_types: [promo, talk, embed]
sources:
  - web-edit-text-*.md（5）
  - web-edit-auto-*.md（6）
  - web-edit-agent-*.md（6）
  - web-edit-research-*.md（5）
  - web-means-critic-*.md（第 3 回の批評役）
  - exp-shortmovie-draft-generator.md
  - exp-thinklet-reading-demo-video.md
---

# 動画編集を AI にさせる

## 西尾の言葉と、このページの位置

西尾（2026-11-09）:
- 「「動画を撮って人が編集」って、事例では確かに人が編集したけど編集作業自体をAIにさせてもいいよね」
- 「動画編集をAIにさせる方法に関するサーベイが足りてないならCyEC2にやらせといて」

解説動画の台本の「作り方の三つ目」は、Mac 側で「実物を撮る方法（編集は人がしても AI にさせても構わない）」に直された。[[work-promotion-video]] の暫定の答えでは、実物の収録が正本だった。このページは、その収録の**編集を誰がやるか**を扱う。
- 描く側は [[expression-means]]、検査は [[checks-and-finishing]]、明日やることは [[ready-to-start-2026-11-10]] にある。
- 素材の中身を見るモデルは、第 3 回の批評役のページ（[[web-means-critic-gemini-video-understanding]] など）にある。

**読み方**:
- 手順はどれも各ページの「着手の仕方」の要約で、**未検証（galleria で確かめる）**。CyEC2 では何も入れず、何も動かしていない。
- 価格と規約は 2026-11-09 時点の公式ページによる。読めなかったものは各ページに書いてある。
- 道具の「できる」は公式がそう書いているということで、確かめたものではない。実例で確かめられたことは、そうと分かるように書く。

## 要点

1. **骨組みはどれも同じ**。商用の切り抜きも、OSS も、エージェントの skill も、時刻付きの文字起こしを LLM に読ませて残す区間を選ばせる。切る位置は語の時刻に合わせる。
   - Klap は規約に「WhisperX で書き起こし、LLM に渡して選ぶ」と書いている（[[web-edit-auto-vizard-klap-munch]]）。
   - OpenShorts のコードの注釈は「LLMs are bad at millisecond arithmetic; the word-level timestamps are ground truth」（[[web-edit-auto-openshorts-ai-youtube-shorts-generator-supoclip-autoclip]]）。
   - video-use と video-editing-skill も、動画は見ずに文字起こしを読み、迷う所だけコマの画像を見る。切る位置は単語の境界に、30〜250 ms の余白を足す（[[web-edit-agent-video-use-and-claude-code-editing-examples]]）。
   - これは西尾の [[exp-shortmovie-draft-generator]]（字幕のタイムスタンプを正にし、LLM には文字だけ直させる）と同じ分担。
2. **AI に任せられることは、各社が書いている範囲で揃っている**。フィラー・間・無音の削除、切り抜きの候補、字幕、縦へのリフレーム、台本からの荒つなぎ、編集ソフトへの受け渡しまで。構成の判断と出来の確認は人に残す、と製品も作り手も書いている（[[web-edit-text-adobe-premiere-text-based-editing-ai-assistant]]、[[web-edit-text-davinci-resolve-intelliscript-studio]]、[[web-edit-auto-auto-editor]]）。
3. **研究とベンチマークでは、ペース・筋・ショット選びがまだ人に及ばない**。
   - Timeline-Bench（2026-09 のプレプリント。実務の課題 56 件、Claude Code・Codex など 16 のエージェント）では、プロの編集者 43 人が 83.5% で人の完成版を選んだ。
   - 未解決の 73% は、形式と要件のテストに全部通って、質のテストだけで落ちた。
   - エージェントのカット数は人の 0.72 倍、最長の静止は 1.5 倍。自分の書き出しを点検しても、ペース・筋・ショット選びを直したのは 5.5%（人の編集者の指摘では 66%）。テストに落ちた回の 95.5% で「成功」と報告していた（[[web-edit-research-timeline-bench-medit-bench]]）。
4. **AI に良し悪しを判定させるのも当てにならない**。MEDit-Bench では、LLM の判定役は並べる順を入れ替えるだけで 35 ポイント振れ、平均では人の評価と逆に AI の編集を良いとした（同）。第 3 回の批評役のページと同じ注意になる。
5. **日本語で文字起こしを使った編集が公式に動くと書いてあるのは、Premiere・DaVinci Resolve Studio（拡張言語パック）・Vrew**。Descript は日本語の文字起こしに対応しておらず、Final Cut Pro の文字起こしは米国英語だけ。研究と OSS の試験も英語が中心で、日本語の講演の切り抜きを測ったものは見つからなかった（下の表）。
6. **自動で詰める道具は「待ち時間」を消す側に働く**。
   - [[exp-thinklet-reading-demo-video]] で西尾が残して説明に変えた約 30 秒の処理待ちは、無音・止まった画面で切る道具なら「dead space」として切られる。画面が止まっていれば motion でも切られる、という見込みは推測。
   - これは [[work-promotion-video]] の「時間と因果を偽らない」との緊張になる。何が無駄で何が見せ場かを決めるのは、今は人。
7. **編集ソフトに AI がつながった**。
   - DaVinci Resolve Studio 21.1（2026-09-08）は、Claude Code などとつなぐ組み込みの MCP サーバーを持った。外からのスクリプトは Studio の機能になった。ただし業界誌による記述で、Blackmagic の一次資料は未読（[[web-edit-agent-davinci-resolve-premiere-scripting]]）。
   - Premiere は UXP が正式になった。CEP は 2027-12 から段階的に終わる（同）。
   - 受け渡しの形式は OpenTimelineIO（OTIO）が筋で、Resolve と Premiere 26 が直接読む（[[web-edit-agent-opentimelineio-edl-fcpxml]]）。

## 方式の一覧

| 方式 | 何を AI に任せられるか（公式・作り手の記述） | 何が人に残るか | 効く型 | 機械 | 費用・アカウント | 出典 |
|---|---|---|---|---|---|---|
| テキストで編集する道具（Premiere・Resolve Studio・Descript・CapCut・Vrew） | 文字起こし、文字を消して映像を切る、フィラーと間の一括削除、台本からの荒つなぎ（IntelliScript）、切り抜きと縦化、字幕、リフレーム | 消す候補を 1 件ずつ見る判断、別テイクの選び直し、閾値、意味が保たれているかの確認 | talk（主）、promo | Mac（Premiere・FCP）、galleria Windows（Resolve）、クラウド（Descript・CapCut） | 有料が中心。Resolve Studio は $236 の表示、Premiere は契約、Descript は日本語に使えない | [[web-edit-text-adobe-premiere-text-based-editing-ai-assistant]]、[[web-edit-text-davinci-resolve-intelliscript-studio]]、[[web-edit-text-descript-underlord]]、[[web-edit-text-capcut-desktop-editpilot-terms]]、[[web-edit-text-final-cut-pro-vrew]] |
| 自動カットの OSS（auto-editor・PySceneDetect・ffmpeg silencedetect） | 無音・動きの止まった所・黒コマの荒切り、場面の切れ目の一覧、Premiere・Resolve・FCP 用の XML や v3 JSON での受け渡し | 閾値と余白、残すべき「間」（デモの待ち・強調の溜め）、どの切れ目を使うか | talk（主）、素材の下ごしらえ | galleria WSL / Windows | 0 円、アカウント不要。auto-editor はキーなしだと 3200×1800 超の書き出しが縮む | [[web-edit-auto-auto-editor]]、[[web-edit-auto-pyscenedetect-unsilence-jumpcutter-silencedetect]] |
| 長い動画からの切り抜き（OpusClip・Vizard・Klap・OSS の OpenShorts など） | 候補の区間の選択と点数、冒頭のフック、縦へのリフレーム、字幕、フィラーの検出 | 候補から選ぶこと、公開してよいか、上げてよい素材か | promo（主） | クラウド（商用）、galleria（OSS。Docker と LLM が要る） | OpusClip は Starter $15/月・Pro $29/月、無料は透かしあり。OSS は 0 円＋LLM の費用 | [[web-edit-auto-opusclip]]、[[web-edit-auto-vizard-klap-munch]]、[[web-edit-auto-openshorts-ai-youtube-shorts-generator-supoclip-autoclip]]、[[web-edit-auto-autoclip-what-drives-views-2026]] |
| LLM のエージェント（OTIO・EDL・FCPXML、ffmpeg・MoviePy、Resolve・Premiere の API と MCP、video-use などの skill） | 区間の一覧を書く、timeline を組む、マーカー、書き出し、言いよどみと空白の削除、テイク選び、字幕、重ね、切れ目の自己点検 | 方針の承認（承認まで切らせない作り）、テイクの良し悪し、通しで見ること、ペースと筋 | talk、promo。embed は短いので手でも足りる | galleria WSL（エージェントと ffmpeg）＋ Windows の Resolve、Mac の Premiere 26 以上 | OTIO・ffmpeg は 0 円。Resolve の外部操作と MCP は Studio。video-use は ElevenLabs の API キー（10 分で約 $0.04） | [[web-edit-agent-opentimelineio-edl-fcpxml]]、[[web-edit-agent-moviepy-ffmpeg-concat]]、[[web-edit-agent-davinci-resolve-premiere-scripting]]、[[web-edit-agent-video-editing-mcp-servers]]、[[web-edit-agent-video-use-and-claude-code-editing-examples]] |
| 素材の中身を見る役（Gemini・Qwen3-VL・文字起こし） | 使う区間の候補を秒の単位で挙げる、映っているものの検索 | 切る位置（語の境界に合わせる）。時刻の精度は公表されていない | 全部（下見） | クラウド（Gemini）、galleria（Qwen3-VL） | Gemini は API キー | [[web-edit-agent-gemini-scene-selection-timestamps]]、[[web-means-critic-gemini-video-understanding]]、[[web-means-critic-qwen3-vl-open-vlms]] |

## 方式ごとの要点

### 1. テキストで編集する道具

- **Premiere**（26.x）:
  - Text-Based Editing が日本語の文字起こしに対応している。フィラーと間は一括で削除でき、26.5 には Paper Edit がある。
  - 日本語のフィラーの検出は、2023 年の試用記事という二次情報しかない。
  - AI Assistant（2026-06 から公開ベータ、英語に最適化）が担うのは、整理・文字起こし・マーカー・荒つなぎまで。台本を渡しての編集と短縮版づくりは未対応と書いている。
  - 素材は学習に使わないと、機能ごとに書いている（[[web-edit-text-adobe-premiere-text-based-editing-ai-assistant]]）。
- **DaVinci Resolve Studio**（20/21）:
  - 台本を正本にする作り方に一番近い。IntelliScript は台本と文字起こしを照合して荒つなぎを作る。21 の Import and Detect Timing は、字幕を取り込んで語の時刻を検出する。
  - 最良のテイクは台詞の一致だけで選ぶ、と公式が書いている。
  - AI の機能はほぼ Studio 限定で、日本語は拡張言語パックが要る（[[web-edit-text-davinci-resolve-intelliscript-studio]]）。
- **Descript**:
  - Underlord（モデルを選べ、Claude Opus 5.5 も入る）・API・MCP がある。
  - **文字起こしはラテン文字の言語だけで、日本語は未対応**。
  - 規約（2025-02-25 版）は素材に永続で取り消せないライセンスを取り、学習は opt-out 制（[[web-edit-text-descript-underlord]]）。
- **CapCut**（デスクトップ）:
  - EditPilot は PC 版のみで、指示は英語を勧めている。
  - 規約（2026-04-15 版）は、送った素材を秘密扱いしない（non-confidential）。永続・譲渡・再許諾できるライセンスを取り、肖像を sponsored content に使う許諾まで取る。EU・英国はこの節を外しているが、日本は外していない。
  - 担当は「会社の素材には使えない」と判断した（[[web-edit-text-capcut-desktop-editpilot-terms]]）。
- **Final Cut Pro / Vrew**:
  - FCP 12.x には文字で切る編集が無く、字幕生成と文字起こしの検索は米国英語だけ。
  - Vrew は日本語の字幕、原稿の読み込み、無音の短縮を掲げ、創作物を AI 学習に使わないと明記している。規約と料金は JS で描画され、読めなかった（[[web-edit-text-final-cut-pro-vrew]]）。

### 2. 自動カットの OSS

- **auto-editor 31.8.0**（2026-10-30）:
  - 無音・動き・黒コマ・字幕との一致で切る。Premiere・Resolve・FCP・Shotcut・Kdenlive 用の XML と、v3 の JSON タイムラインを出す。
  - 作者自身が本編集の前の「first pass」と位置づけている。`--preview` や、切った側だけを書き出す機能など、人が確かめる前提の作り。
  - 公式の skill（`npx skills add WyattBlue/auto-editor`）がある。
  - repo は Public Domain。ただしキーなしだと、3200×1800 を超える書き出しが縮められ、複数素材のエディタ書き出しは有料（[[web-edit-auto-auto-editor]]）。
- **PySceneDetect** v0.7.3（2026-11-08）は場面の切れ目を見つけて分割する道具で、無音を詰めるものではない。unsilence と jumpcutter は更新が止まっている。ffmpeg の silencedetect は、無音の区間を記録に出すだけ（[[web-edit-auto-pyscenedetect-unsilence-jumpcutter-silencedetect]]）。

### 3. 長い動画からの切り抜き

- **選ぶ基準は「冒頭 2〜3 秒」と「単独で意味が通るか」に揃っている**。
  - OpenShorts は「THE 2-SECOND TEST」と「STANDS ALONE」を規則にしている。SamurAIGPT は 3 秒、OpusClip は Hook。
  - OpusClip の Virality Score（0〜99、Hook・Flow・Value・Trend）は、式も重みも検証の数字も公開されていない（[[web-edit-auto-opusclip]]）。
- **AutoClip の作者たちの観察**（2026-10-09。同じアカウントの公開の短尺 158 本。査読なし、道具の作り手による）は、「誰が・何が映っているか」と「どこから始まるか」のほうが、編集より再生数をよく分けたと書いている。カット率には一貫した効果が見られなかった（[[web-edit-auto-autoclip-what-drives-views-2026]]）。
- **研究（HIVE、EMNLP 2025 Industry）**は、文字起こしだけを渡して一発で区間を選ばせる方式（FunClip など）を測った。唐突な変わり目が来るまでの平均は、人の 6.84 分、HIVE の 4.48 分に対して 0.65 分だった。冒頭と結末を無作為に選ぶと、効き目の率が 0.28・0.30 に落ちた（[[web-edit-research-hive-avt-long-to-short]]）。
- 素材の扱い:
  - OpusClip の個人プランのデータは、AI の改善に「使うことがある」。
  - Vizard は、顧客のデータで学習しないと書いている。
  - Klap は、書き起こしを OpenRouter・OpenAI の LLM に渡すと書いている。

### 4. LLM のエージェントに編集させる

- **受け渡しの形式**:
  - OTIO（v0.18.1）は JSON で、時刻を整数のコマ数と fps の組で持つ。Resolve と Premiere 26.0 以上が読む。EDL・FCP XML は `OpenTimelineIO-Plugins` で出す。
  - エフェクト・文字・色はどの形式でも運べない。
  - Remotion は公式の skill で、OTIO を優先し、描いた部分は透明の ProRes 4444 に焼いて上に置く方針を書いている（[[web-edit-agent-opentimelineio-edl-fcpxml]]）。
- **ffmpeg・MoviePy**:
  - MoviePy v2.2.1 は破壊的変更があり、メンテナを募集中。
  - ffmpeg の concat の inpoint/outpoint は、キーフレームの間では正確に切れない（公式の記述）。
  - 区間ごとに書き出して `-c copy` でつなぐ（video-use）か、1 つの filter graph でつなぐ（video-editing-skill）かで、道具の主張が逆になっている。どちらも測った数字は出していない（[[web-edit-agent-moviepy-ffmpeg-concat]]）。
- **MCP サーバー**: 12 個を表にした（Resolve 系 3、Premiere 系 2、FCP、ffmpeg 系 3、クラウド 3）。Resolve MCP の作者は「演技は波形からも文字起こしからも測れない」と書いている。人が見ていないカットは書き出させない作りのものもある（[[web-edit-agent-video-editing-mcp-servers]]）。
- **Opus 5.5 公開（2026-09-22）以後の実例**:
  - browser-use の video-use は、方針を人が承認するまで切らない（Hard Rule 11）。書き出した後に切れ目を自分で点検する。
  - video-editing-skill（2026-10-30）。
  - Kapwing（2026-11-04）は、70.7 秒の動画を 42 分・$9.92・手直し 0 で作ったと書いている。
  - **どの例も、使ったモデル名を書いていない**（[[web-edit-agent-video-use-and-claude-code-editing-examples]]）。

### 5. 素材の中身を見る役

- Gemini は動画を 1 fps で読み、毎秒タイムスタンプを付ける。時刻の指定は MM:SS で、精度は公表されていない。長い素材で特定の場面を探すなら、agentic な使い方を公式が推している。
- Qwen3-VL は、各コマの前に「<3.0 seconds>」のような時刻を置く方式（[[web-edit-agent-gemini-scene-selection-timestamps]]）。
- 批評役としての性能と注意は、第 3 回のページ（[[web-means-critic-gemini-video-understanding]]、[[web-means-critic-qwen-omni]]、[[web-means-critic-video-bench-spotlight]]）。編集のための場面選びでは、モデルが挙げた秒を語の境界に合わせ直すのが、上の骨組みと同じ扱いになる。

### 研究: 何がうまくいき、何がまだ人か

| 時期 | うまくいったこと | 人に残ったこと | 出典 |
|---|---|---|---|
| 2012〜2019（文字起こしで編集） | 単語の時刻合わせ、切ってよい位置の表示、言いよどみの削除、B-roll の位置の推薦 | 何を残すか、どの B-roll か（位置の推薦の F1 は 0.23。専門家どうしでも 0.26） | [[web-edit-research-transcript-editing-lineage]] |
| 2024（LLM の支援。LAVE は 8 人、ExpressEdit は初心者 10 人） | 素材の検索（評価が一番高い）、「どこに何をするか」の候補。具体的な指示ほど通じる | 時刻・長さ・パラメータの詰め。発想と構成の支援は熟練者ほど断った。提案の受け入れは 46% で、受け入れたものの 58% は人が直した | [[web-edit-research-lave-expressedit]] |
| 2025（全自動のエージェント） | 依頼に合う素材探し、尺を満たすこと | 切る位置とペース。Ding らでは「編集の職人性」が 5 段階で 2.75（人の編集は 4.38）。長い動画からの Descript・OpusClip の自動選択は「使えない」「つながらない」と評された | [[web-edit-research-editduet-prompt-driven-agentic]] |
| 2026（ベンチマーク） | 依頼に書ける要件と形式 | リズム、ショット選び、仕上げ、筋の順序、自分の編集の良し悪しの判断 | [[web-edit-research-timeline-bench-medit-bench]] |

- Timeline-Bench の公開順位表（2026-11-09 閲覧）では、Claude Opus 5.5（Claude Code）が 32.1%（18/56）で 1 位。ただしこの構成は人の編集者が評価しておらず、Opus 5.5 は質のテストの判定役の一つでもある（同）。
- UGC の課題では、文字と図の出来が判断の 91% を決め、AI はそこで一番負けた（勝ちか引き分けは 6.8%）（同）。[[work-promotion-video]] の「文字・図はコードで描いて重ねる」と同じ向き。
- embed（発表の中で流しっぱなし）を直接扱った研究と、日本語の講演・LT の録画を LLM で自動編集した査読付きの研究は、見つからなかった。

## 型への効き方

| | promo | talk | embed（流しっぱなし） |
|---|---|---|---|
| 一番効く方式 | 切り抜き（冒頭 2 秒・単独で通じる）、エージェントでの短縮版 | 自動カット（auto-editor の荒切り）、テキストで編集（Premiere・Resolve）、エージェント（video-use） | 尺が 20〜60 秒なので、手でも足りる。素材の下見（場面の切れ目の一覧、モデルでの場面選び）が効く |
| 人に残る判断 | 何が映っているか・どこから始まるか（AutoClip の観察）、公開してよいか | ペースと筋（研究で人に及ばない所）、残すべき間 | 待ち時間を説明に変えるか（[[exp-thinklet-reading-demo-video]]）、時間と因果を偽らないか |
| 注意 | 文字と図は AI が一番負ける所なので、コードで描いて重ねる | 日本語の文字起こしに対応した道具を選ぶ | 自動で詰めると、処理の待ちが消えて因果が偽られうる |

## 経験との突合

- **[[exp-shortmovie-draft-generator]]**:
  - 一致する点:
    - 字幕の時刻を正にし、LLM に時刻を作らせない分担は、2026-10 の道具（OpenShorts、video-use、IntelliScript）と同じ向き。Berthouzoz 2012 とも同じ。
    - 冒頭と結末を別の欄で書かせたのは、HIVE で効くと測られた所。中抜きを 1 つまでにしたのは、文字起こしだけで区間を選ぶ方式の唐突さを避ける形になっている。
  - 食い違う点:
    - 終わりの延長は、西尾の 3 秒に対して OpenShorts は最大 0.45 秒、auto-editor の margin は 0.2 秒、video-use は 30〜250 ms で、一桁違う。Ding らの参加者が挙げた「声が途中で切れる」と同じ種類の問題への対処に見えるが、推測。
    - 西尾の道具のプロンプトは「5〜10 秒でカットを変える」とテンポも求めたが、AutoClip の観察ではカット率に一貫した効果が無かった。どちらも検証された数字ではないので、両方残す。
    - 縦動画は、西尾の道具では黒帯にしたが、OpenShorts は話者に寄せたり 2 人を上下に積んだりを場面ごとに選ぶ。
    - 経験の道具には、書き出した後の点検、端の fade、単語の境界に合わせる処理が無い。
- **[[exp-thinklet-reading-demo-video]]**:
  - 一致する点: 西尾は Premiere で手で編集した。auto-editor も OpusClip（Pro）も Premiere の XML を出すので、「荒切りは自動、仕上げは Premiere」の分担がそのまま作れる。
  - 食い違う点: 「待ち時間 30 秒を説明に変える」判断は、どの道具の規則にも無い。研究で AI が人に及ばなかったペースと構成の判断そのものに当たる。
  - 西尾の Premiere は 25.0 で、UXP の正式版（25.6）も、OTIO の読み込み（26.0）も無い版。
- **解説動画の合成**: Mac 側で THINKLET のデモと Gyazo の動画を ffmpeg の overlay で枠に重ねた（~/video-making-explainer の compose.py）。この機械には無いので読んでいない。video-use の重ねの決まり（重ねは PTS をずらす、字幕は最後）との突き合わせは、Mac 側でやる。

## 日本語の対応（公式の記述）

| 道具 | 日本語の文字起こし・字幕 | 出典 |
|---|---|---|
| Premiere | ○（Text-Based Editing）。フィラーの検出は二次情報のみ | [[web-edit-text-adobe-premiere-text-based-editing-ai-assistant]] |
| DaVinci Resolve Studio | ○（拡張言語パック） | [[web-edit-text-davinci-resolve-intelliscript-studio]] |
| Vrew | ○ | [[web-edit-text-final-cut-pro-vrew]] |
| Descript | ×（ラテン文字の言語だけ） | [[web-edit-text-descript-underlord]] |
| Final Cut Pro | ×（米国英語だけ） | [[web-edit-text-final-cut-pro-vrew]] |
| OpusClip | BETA | [[web-edit-auto-opusclip]] |
| Vizard | 書き起こしは○と明記 | [[web-edit-auto-vizard-klap-munch]] |
| auto-editor の whisper | `-l ja` の例あり（多言語のモデルが要る） | [[web-edit-auto-auto-editor]] |
| エージェントの skill・MCP | 日本語の試験はどれにも無い | [[web-edit-agent-video-use-and-claude-code-editing-examples]] |

## 素材を外に出すかどうか

- 手元で完結するもの: auto-editor、PySceneDetect、ffmpeg、OTIO、Resolve（Studio を含む）、Premiere の Media Intelligence（端末内）、OSS の切り抜き（ローカルの LLM を使う場合）。
- 外に送るもの: Descript、CapCut、OpusClip・Vizard・Klap、video-use（音声を ElevenLabs に送る）、Gemini。
  - 規約で素材の扱いが重いのは CapCut（日本は sponsored content の節が外れていない）と Descript（永続で取り消せないライセンス、学習は opt-out）。
  - 会社の素材を送るかどうかは、西尾が決めること。

## 最小の始め方（未検証。galleria で確かめる）

効く順の候補。詳しい手順は各ページにある。
1. **auto-editor で講演の録画を荒切りし、Premiere の XML まで出す**（talk。galleria WSL、0 円）。
   - 試験素材（2 秒鳴って 2 秒黙る、を 20 秒）で `./auto-editor test.mp4 -o test_cut.mp4` と `--export premiere` を回す。
   - 確かめ方: 尺が約 11.8 秒になり、XML にクリップが 5 つ並ぶ（計算の見込み）。
   - 本番の素材では、切った側だけを書き出して、残すべき間が入っていないか人が見る（[[web-edit-auto-auto-editor]]）。
2. **LLM が書いた区間の JSON から OTIO を作り、Resolve の無料版で開く**（promo・talk。galleria WSL＋Windows、`OpenTimelineIO-Plugins==0.18.1`、0 円）。
   - 確かめ方: Resolve に読み込んだクリップ数と In/Out が JSON と合う（[[web-edit-agent-opentimelineio-edl-fcpxml]]）。
3. **Claude Code に録画を詰めさせる**（talk）。
   - キーなしの道: ffmpeg-skill か video-editing-skill（faster-whisper）。
   - キーありの道: video-use（ElevenLabs の API キーが要る。西尾が決める）。
   - 確かめ方: 方針を出して承認を待つこと、EDL の尺と書き出しの尺が 1 コマ以内で合うこと、切れ目の点検画像が出ること、日本語で単語の時刻が効いているか（[[web-edit-agent-video-use-and-claude-code-editing-examples]]、[[web-edit-agent-video-editing-mcp-servers]]）。
4. **Timeline-Bench の破綻の検査を、自分の書き出しに ffmpeg で当てる**（any。galleria WSL、0 円）。
   - 1 分あたりのカット数、最長の静止、統合ラウドネス、無音の割合の 4 つを出す。
   - AI に編集させた動画の「遅さ」を数字で見る（[[web-edit-research-timeline-bench-medit-bench]]、[[checks-and-finishing]]）。
5. 購入の判断が要るもの:
   - Resolve Studio の IntelliScript（台本から荒つなぎ、$236 の表示）。
   - Mac の Premiere で日本語の講演の短縮版（今の契約で足りるかは西尾が確認する）。

## Open Questions

- 自動で詰める道具を使うとき、「待ち時間を説明に変える」「強調の溜めを残す」を指示として渡せるか。道具の規則に無いので、渡す口は自由記述か、閾値か、人が後で戻すかのどれか。
- 日本語の講演で、語の時刻（whisper・ElevenLabs Scribe・Premiere）がどの単位で出て、切る位置の精度がどれだけか。どの文献にも無い。
- Timeline-Bench の Opus 5.5 の 32.1% は、人の評価を経ていない。判定役に自分が入っている偏りがあるかは、検証されていない。
- ffmpeg で区間を `-c copy` でつなぐか、1 つの filter graph でつなぐか。道具の主張が逆で、測った数字は無い。
- Resolve 21.1 の組み込み MCP と、無料版で Python のスクリプトが外れたことは、業界誌と利用者の issue による。Blackmagic の release notes で確かめていない。
- Premiere が OTIO を読むのは 25.6 からか 26.0 からか。Remotion の docs と Adobe の release notes が食い違っている。
- 終わりの余白: 西尾の 3 秒延長と、道具の 0.2〜0.45 秒の差は、素材（切り抜きの話の区切り）と目的（語の切れ目）の違いによるのか。
