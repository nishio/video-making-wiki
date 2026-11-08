---
type: source
summary: PowerPoint・Keynote・Google Slides の公式ヘルプが書く、スライドに埋め込んだ動画の再生の決まり（いつ始まるか、ループ、トリミング、音量、発表中のキー操作）と、プレゼンの専門家が動きについて書いたこと（Tufte「時間に積むと比較しにくい」、Duarte の slide:ology 付録「アニメーションは物語を語るべき」）。三つのソフトとも既定は「スライドを送る操作で再生が始まる」で、Keynote は「次へ進むまでループ」と発表中の一時停止キー（K）を公式に書く
video_types: [embed]
url: https://support.apple.com/guide/keynote/edit-video-and-audio-tan9c4a69ca6/mac
author: Microsoft（PowerPoint サポート）, Apple（Keynote User Guide for Mac）, Google（Docs Editors Help）／ Edward Tufte, Nancy Duarte
published: unknown（ヘルプは継続更新。Keynote は 15.4 の版の記述）／ 2003-09-01（Tufte, Wired）／ 2008（slide:ology。付録ページは 2013 頃）
retrieved: 2026-11-09
sources:
  - https://support.microsoft.com/en-us/office/set-the-play-options-for-a-video-in-your-presentation-f0d5b3f1-37ba-4a0d-9d94-f8e33cef29bf（取得時は "Insert and play a video file from your computer" に統合されていた）
  - https://support.microsoft.com/en-us/powerpoint/play-a-video-automatically-in-a-slide-show
  - https://support.microsoft.com/en-us/powerpoint/trim-a-video-music-clip-or-sound-clip-in-powerpoint
  - https://support.microsoft.com/en-us/powerpoint/set-a-video-to-play-full-screen
  - https://support.microsoft.com/en-us/powerpoint/training/add-or-delete-audio-in-your-powerpoint-presentation
  - https://support.apple.com/guide/keynote/edit-video-and-audio-tan9c4a69ca6/mac
  - https://support.apple.com/guide/keynote/keyboard-shortcuts-tanfde4a3e6d/mac
  - https://support.google.com/docs/answer/97447?hl=en&co=GENIE.Platform%3DDesktop
  - https://support.google.com/docs/answer/1696717?hl=en（Google Slides のキーボードショートカット）
  - https://www.wired.com/2003/09/ppt2/（Tufte "PowerPoint Is Evil"）
  - https://diagrammer.duarte.com/book/slideology/（slide:ology の付録ページ）
---

# スライドに動画を埋め込む作法: PowerPoint・Keynote・Google Slides の公式ヘルプと、プレゼンの専門家

## 何の文献か

- **公式ヘルプ**（Microsoft・Apple・Google）: 機能の説明。どう使うと伝わるかは書いていない。2026-11-09 に curl で取得し本文を読んだ。版によって画面の名前が変わる（Keynote は 15.4 の版の記述）
- **Edward Tufte "PowerPoint Is Evil"**（Wired, 2003-09-01）: 情報デザインの研究者による論説。モノグラフ "The Cognitive Style of PowerPoint" の要約。モノグラフ本体は読んでいない
- **Nancy Duarte "slide:ology"**（2008）の付録ページ（diagrammer.duarte.com）: 本に載せた作例のファイルと短い説明。**本文は読んでいない**。duarte.com のブログ記事は取得するとトップページに転送され読めなかった
- Garr Reynolds（Presentation Zen）は、動画の埋め込みについての本人の文章を見つけられなかった。Hans Rosling の動くグラフの見せ方を紹介した記事は [[web-roslingifier-data-presentations]] に書いた

## 書いてあること

### 公式ヘルプ: 再生の決まり

| | PowerPoint（Microsoft 365 / 2016〜2024） | Keynote（Mac） | Google Slides |
|---|---|---|---|
| 既定の始まり方 | **In Click Sequence**: スライドの次の段へ進む操作（クリック、スペース、右矢印など）で再生 | 「Start movie on click」にチェックでクリックで開始、外すとスライドが出たら自動 | **Play (on click)**: スライドを送る操作で再生。「これが既定」 |
| ほかの始まり方 | **Automatically**（前にアニメーションの段があればそれが先）、**When Clicked On**（動画そのものをクリックしたときだけ） | 「Play movie across slides」で複数スライドをまたいで流し続ける | **Play (automatically)**、**Play (manual)**（動画そのものをクリックしたとき。「以前はこれが既定だった」） |
| ループ | 音声の説明に **Loop until Stopped**（Play/Pause を押すまで繰り返す）。動画の Loop until Stopped は現行の公式ページでは確かめられなかった（コミュニティ Q&A では Video Options にあるとされる） | **Repeat → Loop**（連続ループ）、**Loop Back and Forth**（順再生の後に逆再生）。「**次へ進むまで**繰り返す」と書く | 現行のヘルプには動画のループの記述が無い |
| トリミング | **Trim Video**: 開始（緑）と終了（赤）の印を動かす。コマ送りボタンあり。ウェブから挿入した動画はトリミングできない | Edit Movie の Trim スライダ | 現行のヘルプには記述が無い（第三者の手引きは開始・終了位置を設定できると書く。未確認） |
| 音 | 音量（Volume）。音声にはフェードの長さ（Fade Duration） | 音量スライダ | 発表中に **m** で消音の切り替え（ショートカット一覧） |
| 動画の出どころ | 埋め込み（ファイルが大きくなる）か、リンク（小さいが切れうる。同じフォルダに置け）。推奨は H.264 + AAC の .mp4。ウェブ版は 256 MB まで | ファイルを置く | **YouTube・URL・Google Drive** から。共有された発表で再生するには、発表者に動画ファイルの権限が要る |

### 公式ヘルプ: 発表中の操作

- **Keynote**（キーボードショートカット「Control a video during a presentation」）: スペースで再生、**K で一時停止・再開**、J で巻き戻し（止めているときはコマ単位）、L で早送り（同）、I で先頭へ、O で末尾へ
- **Google Slides**（ショートカット一覧の「Video Player」）: k で再生・一時停止、u で 10 秒戻る、o で 10 秒進む、止めているとき Shift + , / . でコマ送り、Shift + 0〜9 で長さの 0〜90% の位置へ、c で字幕、m で消音
- **PowerPoint**: 動画を選ぶと再生・一時停止・進む・戻る・音量のバーが出る、と書く（編集画面の説明）。発表中のキー操作は今回読んだページには無い
- **PowerPoint の全画面再生**: Play Full Screen。元の解像度によっては歪むので事前に確かめよ、と書く。動画の枠をスライドの外に置くか隠すなら、自動再生かトリガー（クリックで動作を起こす図形など）を設定しないと再生されない、と書く
- **Keynote のポスターフレーム**: スライド上で動画を代表する一コマを選べる

### Tufte "PowerPoint Is Evil"（2003）

- 企業の PowerPoint のスライドは平均 40 語ほどで、黙読なら約 8 秒分。情報が少ないので枚数が増え、聴衆は「容赦ない逐次性、次から次へのスライド」に耐えることになる、と書く
- 「情報が**時間に積まれる**と、文脈を理解し関係を評価するのが難しい。視覚的な推論は、関連する情報が**横に並べて**示されるときの方がふつうはうまくいく」。統計データでは特にそうで、根本の分析の行為は比較だから、と書く
- 「数字が退屈なら、数字が間違っている。言葉や絵が要点を外しているなら、それを**色付きで踊らせても**関係のあるものにはならない。聴衆の退屈はふつう中身の失敗で、飾りの失敗ではない」
- アニメーションや動画の埋め込みを直接論じてはいない。上の二点は、時間で見せること一般と飾りとしての動きへの批判として読める

### Duarte slide:ology の付録ページ

- 本の作例に付けた短い説明だけを読んだ
  - p.176 "Incorporating Video": 埋め込み動画があるので、PowerPoint より高画質の動画を扱える Keynote で作った、と書く（2008 年当時の事情）
  - p.184 "Animation Serves a Purpose": 「アニメーションは物語を語るべきで、小さな映画の一場面を模すことさえできる」
  - p.188 "Objects Move and Change": 二つのアニメーションを同時に再生すると新しい意味が生まれる例
  - p.192 "Creating Scenes, Not Slides": スライドからスライドへ切り替える代わりに、一つの場面の中をパンする。空間の広がりと場面のつながりが出る、と書く

## この wiki への含意

### embed に効くこと

- **「話し手が送ると始まる」が三つとも既定**: PowerPoint（In Click Sequence）、Google Slides（Play (on click)）、Keynote（Start movie on click）。発表のソフトは、embed の動画を「話し手が自分の話の区切りで始めるもの」として扱う設計になっている。勝手に始まるのは設定を変えたときだけ
- **ループさせるか、止めて話すか（Open Question への手がかり）**: ソフトの機能から言えるのは次まで
  - **ループ**は Keynote が「次へ進むまで繰り返す」と公式に書く。ループは、話し手が話している間、背景で同じ動きを見せ続ける使い方を想定した機能と読める（使い方の推奨は書いていない）
  - **止めて話す**には、Keynote は K、Google Slides は k のキーがある。PowerPoint は、今回読んだ公式ページの範囲では発表中の一時停止キーを確かめられなかった（トリガーで再生を始めるやり方は全画面再生のページに書いてある）
  - どちらが伝わるかを比べた記述は、公式ヘルプにも Tufte・Duarte の文にも無い。話し手が止める・遅くする・巻き戻す使い方の実例分析は [[web-roslingifier-data-presentations]]
- **動画の音**: どのソフトも動画の音量を下げる・消せる。PowerPoint の音声にはフェードの長さがある。話し手の声と動画の音（BGM・TTS）がぶつかるなら、**動画側を無音か小さくして話し手が話す**のがソフトの機能だけで実現できる最も単純な形。般若心経の同期解説は唱える音そのものが中身なので、無音にはできない（[[exp-sutra-sync-subtitles]]）。この場合、話し手は流している間は黙る、という選択になる（推測）
- **ループの継ぎ目**: 般若心経の同期解説は一つの唱えを 3 回繰り返す 45 秒で、周回の継ぎ目（4 句目 → 次の周の 1 句目）を実フレームで確かめていた（[[exp-sutra-sync-subtitles]]）。発表で Keynote の Loop にかけるなら、動画の中で 3 回繰り返すのでなく **1 周分を書き出してソフトにループさせる**という選択肢がある。その場合も継ぎ目の確認は同じく要る（推測）
- **Google Slides は動画を YouTube か Drive から入れる**: 会場のネットワークと、共有した相手の Drive の権限に依存する。ヘルプは「発表者が再生できるように」動画ファイルを共有せよと書く。会場で確実に流すなら、PowerPoint・Keynote にファイルとして埋め込む方が依存が少ない（推測。会場での失敗の記録はこの wiki に無い）
- **形式**: PowerPoint は H.264 + AAC の .mp4 を推奨する。この wiki の経験では、出力は ffprobe で 1920×1080・H.264/AAC を確かめていた（[[exp-sutra-sync-subtitles]]）。その形式なら PowerPoint の推奨と合う
- **Tufte の「時間に積むと比較しにくい」**: embed の動画は時間で見せるので、Tufte の批判をそのまま受ける。比較が要点なら、動画より**横に並べた静止図**の方が良いかもしれない。クオリアさんの動画の 4 秒の A/B/C 比較は、同じ尺の三案を作って人が見比べたもの（[[exp-qualia-video]]）で、発表で見せるなら三つを並べて同時に流すか、一つずつ流すかの選択になる。Tufte の論からは前者が示唆される（推測）
- **Duarte の「場面を作る、スライドを作らない」**: 切り替えでなく一つの場面の中を動く、は Motion Canvas の presentation mode（一つのアニメーションの中に区切りを置いて送る）と同じ発想（[[web-motion-canvas-presentation-mode]]）

### talk・promo への含意

- talk（録画した解説動画）では、ここのソフトの機能は関係しない。PowerPoint の Record（発表の録画）や Keynote の「ナレーションを録って動画として書き出す」機能はあるが、この wiki の talk の経験は Pillow・PyAV など自前の組み立てだった（[[exp-qualia-video]]）
- promo の「無音で自動再生される前提」（[[three-video-types]]）は、発表のソフトの既定（送ると始まる、音あり）と逆。同じ動画を promo と embed に使い回すなら、始まり方と音の扱いを別にする必要がある

## Open Questions

- PowerPoint の動画の Loop until Stopped・Rewind after Playing・Hide While Not Playing は、取得した現行の公式ページでは確かめられなかった（古い URL は "Insert and play a video file from your computer" に統合されていた）。版ごとに画面で確かめる
- Google Slides の動画のループ・トリミング（開始・終了位置）・消音のオプションは、現行のヘルプに記述が無い（第三者の手引きにはある）。実機で確かめていない
- ループと一時停止のどちらが聴衆の理解に良いかは、どの文献にも無い。Rosling の実演の分析（[[web-roslingifier-data-presentations]]）は「止める・遅くする・巻き戻す」の実例だが、比較実験ではない
- Duarte の slide:ology 本文と Tufte のモノグラフ本体は読んでいない。動画やアニメーションの埋め込みについて、付録ページと論説の要約以上のことが書いてあるかは未確認
- 動画を埋め込んだ発表ファイルを会場で再生して失敗した経験は、この wiki にまだ無い
