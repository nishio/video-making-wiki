---
type: concept
summary: 西尾の語「表現手段」の一覧。西尾が既に使った手段と、第 3 回サーベイ（2026-11-09）で調べたまだ使っていない手段（実物の収録、図・データ、2D/3D、人物・声、音、文字、映像を理解するモデルを批評役にする）を、何が表現できるようになるか・効く型・機械・費用・利用条件・成熟度・最小の始め方で 1 表に並べたページ。手順はすべて未検証（galleria で確かめる）
video_types: [any]
sources:
  - web-means-capture-*.md（8）
  - web-means-diagram-*.md（8）
  - web-means-3d-*.md（7）
  - web-means-voice-*.md（9）
  - web-means-sound-*.md、web-means-font-*.md（8）
  - web-means-critic-*.md（8）
  - exp-*.md（既に使った手段）
---

# 表現手段

西尾の目的「作るための手段を調査サーベイし、今後の表現手段を増やすこと」（[[origin-2026-11-09]]）の「表現手段」。ここは**手段の一覧**で、検査と仕上げは [[checks-and-finishing]]、明日から何をやるかは [[ready-to-start-2026-11-10]]。

**読み方**:
- 「手順」の列はどれも各ページの「着手の仕方」の要約で、**未検証（galleria で確かめる）**。CyEC2 では何も入れず、何も動かしていない。
- 版・価格・規約は 2026-11-09 時点の公式ページによる（各ページに日付）。
- 型の embed は流しっぱなしの前提（[[embed]]）。
- 機械の略: gW は galleria の WSL、gWin は galleria の Windows、Mac は MacBook。

## 既に使った手段（経験）

| 手段 | 何に使ったか | 出典 |
|---|---|---|
| canvas に `renderFrame(f)` を描き、headless Chrome で 1 コマずつ撮り、ffmpeg で動画にする | promo の 4 本、Polis の OP 様式、般若心経の同期解説 | [[exp-html-capture-pipeline]]、[[exp-polis-magi-op]]、[[exp-sutra-sync-subtitles]] |
| Pillow の静止スライド＋TTS＋PyAV | クオリアさんの解説 3 本 | [[exp-qualia-video]] |
| Premiere Pro の手編集 | THINKLET のデモ | [[exp-thinklet-reading-demo-video]] |
| VOICEVOX（話し声・歌唱）、AivisSpeech、Irodori-TTS、SAPI | ナレーション、読経、替え歌 | [[exp-galleria-tts-and-singing]]、[[exp-sutra-voicevox-singing]] |
| Wan2.2、FLUX.2 Klein | 短い生成動画、keyframe | [[exp-galleria-local-video-generation]]、[[exp-local-scene-studio]] |
| MiniMax H3、Live2D、PuppetLoom | キャラクターが話す数秒 | [[exp-qualia-h3-live2d-galleria]]、[[exp-puppetloom]] |
| numpy で BGM を合成 | promo の拍 | [[exp-html-capture-pipeline]] |

## まだ使っていない手段の一覧

| 分野 | 手段 | 何が表現できるようになるか | 型 | 機械 | 費用・条件 | 成熟度（2026-11） | 出典 |
|---|---|---|---|---|---|---|---|
| 実物の収録 | Playwright `page.screencast`（showActions・showChapter・fps） | Web の作品を台本どおりに撮る。カーソル・クリック点・章見出しが入る | promo、embed | gW | 無料、Apache-2.0 | v1.65。カーソル描画は v1.61、fps 指定は v1.64 から | [[web-means-capture-playwright-screencast]] |
| 実物の収録 | shot-scraper `video`（YAML の台本） | 同じことを YAML で書く | promo、embed | gW | 無料 | 1.10（2026-06）で追加 | 同上、[[web-promo2-vhs-shot-scraper-demos-as-code]] |
| 実物の収録 | OBS Studio＋WebSocket | ブラウザの外（アプリ・実機・カメラ）を台本から録る。章マーカーも入る | talk、promo | gWin | 無料、GPL | 33.0.1 | [[web-means-capture-obs-studio]] |
| 実物の収録 | 自動ズームの収録アプリ（OpenScreen、Cap、Screen Studio、FocuSee、Recordly） | クリックに寄る、カーソルを滑らかにする | promo | OpenScreen・Cap は gWin、Screen Studio は Mac | OpenScreen は MIT。Cap は商用で年 $29（雇い主の製品のデモも商用に入る）。Screen Studio は月 $29（年払いで月 $9） | OpenScreen v2.2.2 は CLI あり | [[web-means-capture-openscreen]]、[[web-means-capture-cap]]、[[web-means-capture-screen-studio]]、[[web-means-capture-focusee-recordly]] |
| 実物の収録 | ffmpeg の zoompan・crop（クリックのログから寄る） | 後処理で寄る | promo | どこでも | 無料 | zoompan は揺れる不具合が 2015 年から未解決 | [[web-means-capture-ffmpeg-zoompan-screenstudio-alt]] |
| 実物の収録 | iPhone の撮影設定（H.264、HDR オフ、Auto FPS オフ） | 実機・手元を撮る | promo、talk | iPhone | 無料 | — | [[web-means-capture-iphone-camera-settings]] |
| 図・データ | Mermaid の step（v12.3.0） | 流れ図の辺に点を順に走らせる | embed、talk | gW | MIT | 2026-11-03 に追加 | [[web-means-diagram-mermaid]] |
| 図・データ | D2 の steps | 図を段階的に組み立てる。PPTX にも書き出せる | embed、talk | gW | MPL。TALA は v0.9.0 で OSS 化 | v0.9.0（2026-09-07） | [[web-means-diagram-d2]] |
| 図・データ | Excalidraw＋excalidraw-animate | 手描き風の図を、描き進めながら見せる | embed、talk | どこでも | MIT（tldraw は本番に license key が要る） | — | [[web-means-diagram-excalidraw-animate-tldraw]] |
| 図・データ | d3 の interpolate・ease（transition は使わない）、Observable Plot、Vega-Lite（vl-convert） | データが動く。フレーム番号の純関数で描ける | embed、talk | gW | 無料 | — | [[web-means-diagram-d3-transition-veltman]]、[[web-means-diagram-observable-plot-framework]]、[[web-means-diagram-vega-lite-vl-convert]] |
| 図・データ | Graphviz、PlantUML、d3-graphviz | 静止図（`style=invis` で段階表示） | talk | どこでも | 無料 | — | [[web-means-diagram-graphviz-d3-graphviz-plantuml]] |
| 図・データ | Flourish | データのストーリー | talk | ブラウザ | 無料版は書き出し無し、動画は Enterprise のみ、表記が必須 | — | [[web-means-diagram-flourish]] |
| 2D/3D | GSAP＋SVG（paused timeline を seek） | 文字ごとの出現、線を描く、形の変形（SplitText・DrawSVG・MorphSVG が無料） | any | gW | 無料・商用可。OSS ではなく Webflow の独自の許諾 | 3.15.1 | [[web-means-3d-gsap-svg-seek]] |
| 2D/3D | dotlottie-web の setFrame、Rive の scrub | 既製のベクターアニメをコマ指定で撮る | any | gW | Rive の無料版はスプラッシュ付き | Rive の状態機械は seek できない | [[web-means-3d-lottie-rive-seek]]、[[web-after-effects-lottie-rive]] |
| 2D/3D | three.js を `render(t)` で描き、headless Chrome で撮る | 3D の場面、GPU で描く粒子 | promo、talk、embed | gWin（GPU を使うなら） | MIT | r187 | [[web-means-3d-threejs-headless-webgl]]、[[web-means-3d-troika-three-text]] |
| 2D/3D | Theatre.js | AI がコードで骨組みを書き、人がグラフエディタで間合いを詰める | promo | どこでも | core は Apache-2.0、studio は AGPL | 0.7.2（2024-05）で止まっている | [[web-means-3d-theatre-js]] |
| 2D/3D | Blender の `-b -P`（bpy）、Grease Pencil | 光線追跡の質感、立体の文字、手描きの 2D アニメ | promo、talk | gWin | 無料。作ったものは作者のもの | 5.2.3 LTS。5.0 と 4.3 で API が変わった | [[web-means-3d-blender-bpy-cli]]、[[web-means-3d-blender-grease-pencil]] |
| 人物・声 | ユーザー辞書（VOICEVOX・AivisSpeech）の repo 管理 | 読み違いの直しを台本と一緒に版管理する | talk、embed | gWin | 無料 | AivisSpeech はモーラの pitch と長さを無視する | [[web-means-voice-voicevox-aivisspeech-user-dictionary]] |
| 人物・声 | Style-Bert-VITS2、GPT-SoVITS、Qwen3-TTS | 自分の声の学習・ゼロショット、別の声質 | any | gW | SBV2 は AGPL、GPT-SoVITS は MIT、Qwen3-TTS は Apache-2.0 | SBV2 は 2025-08 から更新なし、GPT-SoVITS は V5（2026-10） | [[web-means-voice-style-bert-vits2]]、[[web-means-voice-gpt-sovits]]、[[web-means-voice-fish-qwen3-sarashina-kokoro]] |
| 人物・声 | COEIROINK | 別の声 | any | gWin | クレジット必須 | v2.13.0 | [[web-means-voice-coeiroink-terms]] |
| 人物・声 | 商用 TTS（Google Chirp 3 HD の yomigana、Azure、ElevenLabs、OpenAI） | 読みとアクセントを台本に書ける（Google だけ） | any | どこでも（API） | 要アカウント・課金。OpenAI の tts-1 系は 2027-01-06 に終了 | — | [[web-means-voice-google-azure-openai-elevenlabs-tts]] |
| 人物・声 | 声の複製（ElevenLabs、Google、ローカル） | 本人の声のナレーション | any | API か gW | 同意・本人確認の条件がそれぞれ違う | — | [[web-means-voice-elevenlabs-google-openai-voice-clone-consent]] |
| 人物・声 | 口の同期（LatentSync 1.5、MuseTalk）、音声駆動の人物（InfiniteTalk、LongCat-Video-Avatar） | 既存の映像の口を直す、台詞の音声で顔ごと動かす | promo、talk | gW、GPU 要（LatentSync 1.5 で 8GB） | MuseTalk は MIT、Wav2Lip は商用禁止 | — | [[web-means-voice-latentsync-musetalk-lipsync]] |
| 人物・声 | アバター（HeyGen、Live2D） | 撮影なしで本人が話す動画 | talk | API | Live2D は売上 1,000 万円が境で、企業の活動は非営利と認めない | — | [[web-means-voice-heygen-live2d-avatar]] |
| 音 | ACE-Step 1.5 | 尺と BPM を指定したオリジナルの曲を手元で作る | promo、talk、embed | gW、GPU 要（12〜16GB 帯） | 重みは MIT、生成物の商用可 | 2026-02 | [[web-means-sound-ace-step-yue2-diffrhythm]] |
| 音 | Suno・Udio・ElevenLabs Music | 歌入りの曲 | promo | API・Web | 無料プランは動画に使えない（Udio は YouTube への掲載も禁止） | 規約は 2025-11〜2026-10 の版 | [[web-means-sound-suno-udio-elevenlabs-music-terms]] |
| 音 | 効果音の生成（ElevenLabs SFX、Stable Audio Open）、映像から音を付ける（MMAudio、HunyuanVideo-Foley） | 出来事に合わせた効果音 | any | API か gW | モデルごとに違う | — | [[web-means-sound-elevenlabs-sfx-mmaudio-foley]] |
| 音 | 素材集（効果音ラボ、魔王魂、OpenTracks、Pixabay、YouTube オーディオライブラリ、Freesound） | 既製の BGM・効果音 | any | どこでも | 商用・収益化は可。Content ID への登録と AI 学習は禁止。OpenTracks は政治・宗教の制作物に使えない | — | [[web-means-sound-soundeffect-lab-maoudamashii-opentracks]]、[[web-means-sound-pixabay-youtube-audio-library-freesound]] |
| 文字 | OFL の日本語フォントを作品に同梱する（Noto Serif CJK Black、Zen Old Mincho Black など） | 機械に依らず同じ絵、極太の明朝 | any | どこでも | OFL は video titling を許可、クレジット不要 | — | [[web-means-font-sil-ofl-noto-zen-mincho]]、[[web-means-font-fontconfig-noto-cjk-linux]] |
| 文字 | 商用フォント（Morisawa、mojimo-EVA のマティス-EB） | 特定の様式の書体 | promo | — | mojimo は個人契約で、本人のチャンネルだけ | — | [[web-means-font-morisawa-fonts-bizplus-mojimo]] |
| 批評役 | Gemini の動画入力 | 完成した mp4 を映像と音のまま通しで見せて批評させる | talk、embed | API | 要 API キー・費用。1 分で 1 回 1〜3 セント程度（担当の見積もり）。無料枠に入れた動画は人が読むことがある | — | [[web-means-critic-gemini-video-understanding]] |
| 批評役 | Qwen-Omni の API、Qwen2.5-Omni-7B-AWQ（ローカル、15 秒まで） | 音ありで通しで見る | talk | API か gW | — | Qwen3-Omni は 15 秒で 79GB 要る | [[web-means-critic-qwen-omni]] |
| 批評役 | Qwen3-VL-8B（llama.cpp、約 10GB）にコンタクトシートを見せる | 動画を外に出さずにコマで批評させる | talk、embed | gWin | Apache-2.0 | — | [[web-means-critic-qwen3-vl-open-vlms]] |
| 批評役 | Claude、OpenAI | コマ（静止画）だけ。音は入らない（OpenAI は別のモデルで） | any | API | — | — | [[web-means-critic-openai-claude-vision-docs]] |

## 分野ごとの要点

### 実物の収録

- 台本どおりに撮るときの最大の欠点は「録画にカーソルが映らない」だった。2026 年の Playwright で、組み込みの注釈（showActions）で解消された（[[web-means-capture-playwright-screencast]]）。
- 自動ズームのアプリは、どれも OS のクリックとカーソルを記録して寄る位置を決めている。Playwright は OS のカーソルを動かさない。だから台本で撮るなら、寄る位置は台本の側から渡すことになる（OpenScreen の zoomRegions か ffmpeg の式）（[[web-means-capture-openscreen]]、[[web-means-capture-ffmpeg-zoompan-screenstudio-alt]]）。
- 実物は実時間で撮るので、撮るたびに少しずつ違う。役を分けるのが筋になる。
  - 実物は実時間で撮る。
  - 文字と図は西尾の方式（フレーム番号の純関数）で描いて重ねる（[[work-promotion-video]] の暫定の答えの具体）。
- 実際の fps を ffprobe で測る。
  - Cap は 60 のつもりが約 58 になる。
  - recordVideo は可変フレームレート。
  - iPhone は Auto FPS で 24 に落ちる。
  - [[exp-galleria-ffmpeg-measurement-and-delivery]] の「画面録画は VFR になりやすい」と同じ向き。
- 収録アプリの「読み込みを詰める」編集は、待ちを隠す向き。[[exp-thinklet-reading-demo-video]] が待ちを説明に変えたのと逆で、Gemini の事例（[[web-promo2-gemini-nikola-staged-demos]]）の「時間と因果を偽らない」に触れうる。

### 図・データ

- 西尾の方式に載るかは、道具の時刻の持ち方で決まる（[[web-means-diagram-mermaid]]、[[web-means-diagram-excalidraw-animate-tldraw]]、[[web-means-diagram-d3-transition-veltman]]）。
  - **SMIL**（excalidraw-animate、Mermaid の step）: `pauseAnimations()`＋`setCurrentTime()` で外から止める。
  - **CSS**（D2 の animated SVG）: `document.getAnimations()` で止める。
  - **d3 の timer**: 仮想時間が要り、前にしか進めない。
  - **遷移を持たない道具**（Plot、Vega-Lite）: 一番載りやすい。
- SVG・DOM の道具は、西尾の `canvas.toDataURL` では撮れない。`page.screenshot` か、canvas に描き写す工程が要る（GSAP・Lottie の svg 描画も同じ）。
- 組み込みの動画書き出しはどれも合わない。
  - excalidraw-animate の WebM は実時間の画面収録。
  - Flourish の動画は Enterprise 限定。
  - D2 の段階表示は 1ms のカットのループ。

### 2D/3D

- GSAP は 2025-04-30 に全機能が無料・商用可になった。ただし OSS ではない（[[web-means-3d-gsap-svg-seek]]）。
  - 禁止されているのは、Webflow と競合する視覚的なアニメ作成ツールに組み込むことだけ。
  - 動画への書き出しは条文に明記が無い。
  - 撮る決まりは Remotion の禁止事項（コールバック、seed の無い random、壁時計で進む gsap.to）がそのまま使える。
- three.js は、撮る直前に描けば描画バッファの消失を避けられる。問題は headless で GPU が切られること。`--use-gl=angle` を使い、最初に `UNMASKED_RENDERER_WEBGL` をログに出して GPU が使われているかを確かめる（[[web-means-3d-threejs-headless-webgl]]）。
- Blender は galleria の Windows 側で `-b -P` で回すのが近道（[[web-means-3d-blender-bpy-cli]]、[[web-means-3d-blender-grease-pencil]]）。
  - headless の EGL は Linux だけ。
  - pip の bpy 5.2.3 は Python 3.13 専用。
  - 5.0 と 4.3（Grease Pencil）で API が変わり、LLM が覚えている古い書き方とずれる。
- 流行の作品で 3D を使ったものは promo の側に偏っていた（Three.js 10 件・Blender 15 件、教育の解説は 0 件。[[web-opus2-awesome-claude-5-5-videos]] の数え方による）。

### 人物・声

- 読みの直し方はエンジンで違う（[[web-means-voice-voicevox-aivisspeech-user-dictionary]]、[[web-means-voice-google-azure-openai-elevenlabs-tts]]）。
  - VOICEVOX: 辞書と AquesTalk 風記法。
  - AivisSpeech: 辞書だけ。モーラの pitch と長さは無視され、複合語・英単語で辞書が効かないことがある。
  - Style-Bert-VITS2: `moraToneList`。
  - Google: SSML の yomigana で、読みとアクセントを台本の中に書ける。
  - Gemini-TTS・OpenAI: 指示文だけ。
- 担当が出した三層の運用案（未実測）:
  1. 台本の narration 欄を書き換える。
  2. repo に置いた辞書を合成の前に入れ、辞書の hash を記録する。
  3. それでも直らないアクセントだけ、区間ごとに上書きする。
- OpenAI の `gpt-4o-mini-tts` は 2027-01-06 に終了する。[[exp-democracy-river-video]] の英語版は、そのままでは作り直せなくなる。
- 利用条件は名義と売上で変わる。どの名義（個人か会社か）で出すかで結論が変わる。
  - Fish は年商 50 万ドルまで商用可。
  - Live2D は売上 1,000 万円が境で、企業の活動は非営利と認めない。
  - ElevenLabs の Free〜Pro は個人の利用に限る。
- 口の同期の道具は「既存の口を直す」型で、[[exp-qualia-h3-live2d-galleria]] の「口を直す道具を演技の代わりに置かない」と同じ位置にある。

### 音・文字

- 「楽曲は実用的なローカルモデルが無い」（[[exp-galleria-tts-and-singing]]、2026-09-04 の整理）は古い。ACE-Step 1.5（2026-02、MIT、生成物の商用可）が既にある（[[web-means-sound-ace-step-yue2-diffrhythm]]）。
- 商用の楽曲サービスは、無料プランを動画に使えない（[[web-means-sound-suno-udio-elevenlabs-music-terms]]）。
- 素材を使ったら、URL と取得日の台帳を作る。台帳が Content ID の申し立てへの異議の根拠になる（[[web-means-sound-pixabay-youtube-audio-library-freesound]]）。
- [[exp-polis-magi-op]] の書体（マティス-EB）は、正規に入れる手段の mojimo-EVA が個人契約で、会社の発信物には使えない。OFL の 900 の明朝（Noto Serif CJK JP Black、Zen Old Mincho Black）で置き換えられる（[[web-means-font-morisawa-fonts-bizplus-mojimo]]、[[web-means-font-sil-ofl-noto-zen-mincho]]）。
- Ubuntu の `fonts-noto-cjk` は Regular と Bold だけで、Black は `-extra` に入っている。フォントのファイルを作品のフォルダに置き、`@font-face` で直接指すのが確実（推測）（[[web-means-font-fontconfig-noto-cjk-linux]]）。

### 映像を理解するモデルを批評役にする

- 通しで見て聞けるのは Gemini と Qwen-Omni の API だけ。Claude と OpenAI はコマしか見られない（[[web-means-critic-gemini-video-understanding]]、[[web-means-critic-openai-claude-vision-docs]]）。round 2 の「モデルは聞けない」（[[after-opus55]]）は、Claude については 2026-11 の docs でもそのまま正しい。
- **点を付けさせる批評は人の代わりにならない**（[[web-means-critic-videoscore]]、[[web-means-critic-video-bench-spotlight]]、[[web-means-critic-omni-judge-audiojudge]]）。
  - 汎用モデルの点が人と完全に一致するのは 26〜29%。
  - 時間・動きの評価は相関 0.40〜0.51。
  - 音と映像の同期は τ 0.02〜0.14。
  - コマの停止は、見るよう指示しても見つけられなかった。
- 効くのは聞き方の工夫（[[web-means-critic-video-bench-spotlight]]）。
  - 1 回に 1 種類の誤りを、時刻付きで聞く。
  - 例を見せる。
  - 2〜3 回回して、共通の指摘を残す。同じ設定でも 33% は点が変わる。
- talk の批評は、映像と音を両方見せる必要がある。文字起こしだけにすると、EduPanel の人との相関は 0.84 から 0.23 に落ちた。一番効きそうなのはナレーションの事実の誤りの指摘（[[web-means-critic-edupanel-paper2video]]）。
- 「モデルが要旨を言えた」は「人に伝わる」の代わりにならない。Paper2Video では、モデルを聴衆にした小テストと人の評価が逆になった（同）。
- 同期・停止・閃光・0.5 秒単位の間は、機械の検査（[[checks-and-finishing]]）と人の目に残す。

## 型ごとに効く手段（担当の報告から）

| 型 | 効く手段 |
|---|---|
| promo | 実物の収録＋寄り（Playwright・OpenScreen）、ACE-Step の曲、Blender・three.js、音声駆動の人物 |
| talk | OBS で話し手と画面、D2・Mermaid の図、ホワイトボード風（Excalidraw・Grease Pencil）、辞書の版管理、Gemini の批評（事実の誤り） |
| embed | 段階的に組み立てる図（D2・Mermaid・excalidraw-animate）、データのアニメ（d3 の interpolate を renderFrame に）、読みの辞書（流しっぱなしでは話し手がその場で直せない）、Gemini の音なし版で要旨を言い直させる |

## Open Questions

- three.js・Blender の GPU 描画が、粒子系の「1 分に約 10 分」（[[exp-html-capture-pipeline]]）を速くするかは測っていない。
- 自動ズーム（寄り）は、閃光の基準・前庭障害（[[design-fundamentals]] の「全画面の拡大・パンは避ける側」）と両立するか。寄りの大きさと速さの目安は見つからなかった。
- GSAP の許諾に、動画への書き出しの明記が無い。条文の「Webflow と競合するツール」に当たらない、というのは担当の読みで、決めるのは西尾。
- 声の複製と HeyGen の分身は、顔と声を外部に預けるか、どの名義で使うかが先に決まらないと始められない（[[ready-to-start-2026-11-10]] の「西尾が決めること」）。
- 日本語の画面文字・日本語の音声で、批評役の精度を測った研究は見つからなかった。

## Updates

### 2026-11-09 動画編集を AI にさせる方法のサーベイから（[[ai-editing]]）

- 「実物の収録」の分野に、**撮った素材の編集を AI にさせる手段**を足す（22 ページ、横断は [[ai-editing]]）。
  - 自動カット: auto-editor 31.8.0（無音・動きで荒切りし、Premiere・Resolve の XML を出す。galleria WSL、0 円、[[web-edit-auto-auto-editor]]）
  - テキストで編集: Premiere（日本語に対応）、Resolve Studio の IntelliScript（台本から荒つなぎ、$236）。Descript は日本語に使えない（[[web-edit-text-davinci-resolve-intelliscript-studio]]、[[web-edit-text-descript-underlord]]）
  - 切り抜き: OpusClip など商用と OpenShorts などの OSS。どれも「文字起こし → LLM が区間を選ぶ」（[[web-edit-auto-opusclip]]、[[web-edit-auto-openshorts-ai-youtube-shorts-generator-supoclip-autoclip]]）
  - LLM のエージェント: OTIO で編集ソフトに渡す、ffmpeg で切り貼り、Resolve Studio 21.1 の組み込み MCP、video-use などの skill（[[web-edit-agent-opentimelineio-edl-fcpxml]]、[[web-edit-agent-video-use-and-claude-code-editing-examples]]）
- 増える表現: 講演・LT の録画を詰めた版、長い録画からの切り抜き、編集ソフトで直せる下書きのタイムライン。ペース・筋・ショット選びは研究で人に及ばない（[[web-edit-research-timeline-bench-medit-bench]]）

### 2026-11-10 Grok Imagine の能力の実測から（[[exp-grok-imagine-capability-probe]]）

- 「既に使った手段」に、ホスト型の生成動画 Grok Imagine（`grok-imagine-video-1.5`・`-lite`、静止画 `grok-imagine-image-2.0`）を足す。X Premium+ の週の枠で使え、枠は Imagine 換算で約 430〜450 USD 相当（実測）。720p の動画 1 秒は約 0.14 USD 相当、lite なら約 0.03 USD 相当
- 手段として効いたもの（判定は Grok が 6 コマの一覧画像を見て付けた点と画素の数値で、人の目では見ていない）
  - 図が段階的に組み上がる解説アニメ: 完成図を静止画で作り、編集で途中の段階を作り、開始の画像・keyframes・終わりの画像でつなぐ。keyframe は指定の時刻の ±0.2 秒に着いた（4 種のうち 3 種）
  - 継ぎ目の無いループ: 終わりの画像に開始画像と同じものを指定（最後のコマとの差 1.3、指定なしは 30）
  - 同じキャラクターを場面をまたいで使う: 参照画像 1 枚（`reference_images`）
  - 日本語のタイトルカード: image-2.0 は指定の文字列を正確に描き（12 枚とも）、そこから i2v でゆっくり寄っても崩れない
  - 画風: 文章だけの t2v より、先にその画風の静止画を作る（i2v に移しての効果は未測定）
  - 候補を何本も出して選ぶ: lite の i2v（約 4.5 分の 1 の費用、2 倍速い、品質はほぼ同じ）
  - 架空の人物に日本語の台詞を言わせる: 聞き取りがほぼ一致し、音声の追加の費用は無い
- 型ごとに効く手段への当てはめ: promo はキャラクターの参照・ループ・台詞、talk はタイトルカードと段階的な図、embed は段階的な図とループ（各型のページの Updates）

### 2026-11-10 Grok Imagine の実測 22:30 版（判定 668 件がすべて終わった、[[exp-grok-imagine-capability-probe]] の Updates）

- 上の 2026-11-10 の項への足し・直し（判定はどれも Grok（grok-4.3）が 6 コマの一覧画像で付けた点。人の目では見ていない）
  - 解説動画の場面の絵: 静止画 1 枚 + lite 8 秒 × 4 本から選ぶ（約 1.1 USD 相当）で、t2v full × 2（約 2.2 USD 相当）と同じ品質（組ごとの最良 8.33 と 8.29）。1 本で済ませるなら t2v full
  - 画風: 画風付きの静止画からの i2v で画風が保たれた（使える 6.7・5.8、t2v は 3.5・3.8）。この i2v は full の方が良い（lite より 1.0・0.4 高い）。「候補を出すなら lite」の例外
  - カメラワーク: 名前のついた動きの指定は 40 本中 11 本しか通らなかった（引きと固定は通り、チルト・クレーン・ピント送り・手持ちは 0/4）。あてにしない
  - 参照 2 枚（キャラクター + 図）で、キャラクターを図の中に置くのは効かない（使える 3.0、3 本とも破綻）。場所が風景なら効く（8.3）
  - 15 秒は図の組み上がりや定点の場面向き（8.0）。場面が大きく変わる長回しは破綻しやすい（6.0、3 本とも破綻）
  - 720p と 1080p: この判定（1 コマ幅 480 px に縮めた一覧画像）では差を見分けられない。費用は 1.8 倍
