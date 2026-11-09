---
type: source
summary: 編集の決定（どの素材のどこからどこまでを、どの順に、どのトラックに）を書く交換形式 3 つ。OpenTimelineIO（ASWF、v0.18.1 2025-11-09、Apache-2.0）は JSON で LLM が書きやすく、DaVinci Resolve と Premiere（26.0、2026-01 から）が直接読む。CMX 3600 EDL は映像 1 トラックだけ・fps を持たない。FCPXML は Final Cut Pro 12.0 で 1.14 だが Apple の開発者向け docs は古い版のまま。LLM には OTIO を書かせ、EDL・FCPXML はアダプタで変換するのが筋
video_types: [any]
url: https://github.com/AcademySoftwareFoundation/OpenTimelineIO
author: Academy Software Foundation（OpenTimelineIO）／OpenTimelineIO の各アダプタ repo／Apple（Final Cut Pro release notes・FCPXML Reference）／Adobe（Premiere release notes）／Blackmagic Design（Resolve scripting README）／Remotion
published: OTIO v0.18.1 は 2025-11-09。FCP 12.0 は 2026-01-28、12.4 は 2026-09-29。Premiere 26.0 は 2026-01
retrieved: 2026-11-09
sources:
  - https://github.com/AcademySoftwareFoundation/OpenTimelineIO（README、最終 push 2026-11-07）
  - https://pypi.org/project/OpenTimelineIO/（0.18.1、2025-11-09、Python >3.9）
  - https://pypi.org/project/OpenTimelineIO-Plugins/（0.18.1）
  - https://opentimelineio.readthedocs.io/en/latest/tutorials/adapters.html
  - https://opentimelineio.readthedocs.io/en/latest/tutorials/feature-matrix.html
  - https://opentimelineio.readthedocs.io/en/latest/tutorials/ai-policy.html（Revised 20-Oct-2026）
  - https://github.com/AcademySoftwareFoundation/OpenTimelineIO/blob/main/examples/build_simple_timeline.py
  - https://github.com/OpenTimelineIO/otio-cmx3600-adapter（README、v1.0.0 2023-07-07、最終 push 2025-12-12）
  - https://github.com/OpenTimelineIO/otio-fcpx-xml-adapter（README、v1.0.0 2023-07-07、最終 push 2024-06-25）
  - https://github.com/OpenTimelineIO/otio-fcp-adapter（README、v1.0.0、最終 push 2026-04-08）
  - https://github.com/OpenTimelineIO/otio-aaf-adapter（v2.0.0 2025-11-21）
  - https://support.apple.com/en-us/102825（Final Cut Pro release notes）
  - https://developer.apple.com/documentation/professional-video-applications/fcpxml-reference
  - https://helpx.adobe.com/premiere-pro/kb/fixed-issues.html（Premiere release notes）
  - https://extremraym.com/cloud/resolve-scripting-doc/（Resolve の scripting README の写し、v21.0.4）
  - https://www.remotion.dev/docs/export-opentimeline
---

# OpenTimelineIO・CMX 3600 EDL・FCPXML（LLM に編集の決定を書かせる形式）

## 何の文献か

- **OpenTimelineIO（OTIO）**: Pixar 発で今は Academy Software Foundation（ASWF）の OSS。README・公式 docs（アダプタ・機能表・AI の方針）・例のスクリプト・PyPI。2026-11-09 に GitHub API と curl で読んだ
- 各アダプタ（CMX 3600 EDL・FCP7 XML・FCPX XML・AAF）の README
- 編集ソフトの側の一次資料: Final Cut Pro の release notes（Apple）、Premiere の release notes（Adobe）、DaVinci Resolve の scripting README（Blackmagic。原本はインストール先 `Developer/Scripting/README.txt` にあり、このページは X-Raym が整形して公開している写しを読んだ。写しの見出しは「Last Updated: 24 Jul 2026 - v21.0.4」）
- Remotion の「OpenTimelineIO に書き出す」docs（Agent Skill の全文が載っている）
- 種類: すべて公式ドキュメント・README。どれも「LLM に書かせたときの成功率」は測っていない

## 書いてあること

### OpenTimelineIO

- README: 「OpenTimelineIO is an interchange format and API for editorial cut information. OTIO contains information about the order and length of cuts and references to external media. It is not however, a container format for media.」（カットの順と長さと素材への参照だけを持つ。映像そのものは入らない）
- 「It is natively supported in most non-linear editing applications」「The API for OpenTimelineIO is considered stable」と書く（README の DEVELOPMENT STATUS）
- 最新は **v0.18.1（2025-11-09、GitHub の release は prerelease 扱い）**。Python 3.9〜3.15、VFX Platform 2023〜2027。main への push は 2026-11-07 まで続いている。2025-11 以後の 1 年はリリースが出ていない
- **v0.16 より後、`opentimelineio` の PyPI パッケージは中核と自前の形式（`.otio`・`.otioz`・`.otiod`）だけ**。EDL・FCP XML・AAF などは `OpenTimelineIO-Plugins`（同じ 0.18.1）を入れる（README の注記、Issue #1386）
- アダプタの区分（adapters の docs）:
  - Plugins に入るもの（"Batteries-Included"）: AAF・ale・burnins・cmx_3600・fcp_xml（FCP7 XML。Premiere の XML もこの形）・maya_sequencer・svg・xges
  - 入らないもの（"Additional"）: **fcpx_xml**（Final Cut Pro X の FCPXML）・hls_playlist。別に入れる
  - 「These adapters are supported by the broader OpenTimelineIO community ... they may be maintained and supported at varying levels」
- 機能表（feature-matrix の docs。抜粋）:

| 機能 | OTIO | EDL | FCP7 XML | FCP X | AAF |
|---|---|---|---|---|---|
| 映像トラック複数 | ✔ | **✖** | ✔ | ✔ | ✔ |
| 音声トラック | ✔ | ✔ | ✔ | ✔ | ✔ |
| マーカー | ✔ | ✔ | ✔ | ✔ | ✔ |
| ネスト | ✔ | ✖ | ✔ | ✔ | ✔ |
| トランジション | ✔ | ✔ | ✖ | ✖ | ✔ |
| 音声・映像のエフェクト | ✖ | ✖ | ✖ | ✖ | ✖ |
| 一定の速度変更 | ✔ | ✔ | ✖ | ✖ | 読みのみ |

  エフェクト（色・文字・合成）は**どの形式でも運べない**
- アダプタの更新: fcpx_xml は v1.0.0（2023-07-07）のまま、最終 push 2024-06-25。cmx_3600 は v1.0.0 のまま最終 push 2025-12-12。fcp_xml は最終 push 2026-04-08。AAF は v2.0.0（2025-11-21）、push 2026-10-22（GitHub API、2026-11-09）
- CMX 3600 アダプタの README: 「EDLs don't contain metadata specifying the rate」なので読むときに `rate`（既定 24）を渡す。書き出しは `avid`（既定）・`nucoda`・`premiere` の 3 つの方言
- Python の最小形（`examples/build_simple_timeline.py` から）: `otio.schema.Timeline` に `otio.schema.Track` を足し、`otio.schema.Clip(media_reference=otio.schema.ExternalReference(target_url=...), source_range=otio.opentime.TimeRange(start_time=RationalTime(値, fps), duration=RationalTime(値, fps)))` を `append` し、`otio.adapters.write_to_file(tl, path)` で書く。時刻は**整数のコマ数と fps の組**（`RationalTime`）で持つ
- **プロジェクトの AI の方針**（2026-10-20 改訂）: 「A human must always be in the loop」「DO NOT "vibe code."」、PR には `Assisted-by: TOOL / MODEL` を書くよう求める。これは OTIO 本体へ貢献するときの決まりで、OTIO を使う側の決まりではない

### どの編集ソフトが読むか（各社の一次資料）

- **DaVinci Resolve**: scripting README の `MediaPool.ImportTimelineFromFile(filePath, {importOptions})` は「AAF/EDL/XML/FCPXML/DRT/ADL/OTIO」から timeline を作ると書く。書き出しの定数に `resolve.EXPORT_OTIO`・`EXPORT_EDL`・`EXPORT_FCPXML_1_8〜1_10` などがある（README v21.0.4 の写し）。手で読み込むのは無料版でもメニューからできる（API の無料版の制限は [[web-edit-agent-davinci-resolve-premiere-scripting]]）
- **Premiere**: release notes の January 2026（version 26.0）に「Premiere now supports importing and exporting OpenTimelineIO (OTIO) projects」。April 2026（26.2）に「Export sequences to FCP XML and OTIO formats, and access a new scripting API for the Preset Object」。EDL と FCP XML の書き出しは以前からある（ヘルプの目次）
  - Remotion の skill は「DaVinci Resolve and Adobe Premiere **25.6** or later」が OTIO を読むと書き、Adobe の release notes（26.0）と食い違う（25.6 の時点で beta だった可能性。未確認）
- **Final Cut Pro**: OTIO を直接は読まない（Apple の資料に記述なし）。FCPXML を読む。release notes は「Final Cut Pro 12.0（2026-01-28）: Updates FCPXML to version 1.14」「11.0: 1.13」。一方 Apple の開発者向け FCPXML Reference の本文は「FCPXML 1.9 requires Final Cut Pro 10.4.9 or later」までで、**1.14 の仕様書は developer.apple.com で見つからなかった**
- **Remotion**: 「It is not possible to deterministically export a Remotion project to the OpenTimelineIO format」として、エージェントに Remotion のコードを読ませて OTIO を作らせる skill を docs に載せている。方針は「Prefer OpenTimelineIO (`.otio`) ... Only produce EDL, FCPXML or Premiere XML if the user explicitly asks」、OTIO で表せない文字・図形・アニメーションは**透明の ProRes 4444 に描き出して上に置く**、「Never leave both a fallback and the media it replaces active」

## 何を AI に任せられるか

- **公式が書いていること**: OTIO はカットの順・長さ・素材の参照・マーカー・トラック（EDL は映像 1 本）を運ぶ。だから LLM には「どの素材の何秒から何秒を、どの順で」を書かせ、OTIO にして編集ソフトに渡せる。Remotion は実際にエージェントに OTIO を書かせる skill を公式に出している
- **実例で確かめられたこと**: このページの文献には、LLM が OTIO・EDL・FCPXML を書いて編集ソフトで開けた成功率の記録は無い。Remotion の skill は手順の指示で、結果の報告ではない
- 運べないもの: 色・文字・合成・エフェクト（どの形式も ✖）。字幕は Premiere の OTIO の往復で落ちるという利用者の声がある（Adobe community。一次資料として確かめていない）。字幕は SRT で別に渡す

## 何が人の判断として残るか

- 形式の側は「人が編集ソフトで直す」ことを前提にした受け渡し（Remotion の docs の目的は「hand a Remotion video over to a video editor」）。どのカットを残すかの判断を形式は助けない
- OTIO の AI の方針は「人がループにいること」を求めるが、これは OTIO のコードへの貢献についての決まり。動画の編集の判断について書いた文献ではない（推測で広げない）

## 日本語の対応

- OTIO は JSON（UTF-8）なので、クリップ名・マーカーの文字は日本語を入れられるはず（推測。docs に日本語の記述は無い）
- **CMX 3600 EDL は文字の制限が強い**（固定幅の古い形式。OTIO のアダプタの README は文字コードに触れていない）。日本語のクリップ名・ファイル名は EDL で崩れる見込み（推測。galleria で確かめる）。日本語のファイル名を使うなら OTIO か FCP7 XML にする

## 費用・アカウント・利用条件

- OTIO・各アダプタ: Apache-2.0、無料、アカウント不要。README: 「Nothing in the license file or this project grants any right to use Pixar or any other contributor's trade names」
- 読む側: DaVinci Resolve は無料版でも OTIO を手で読み込める（API で読ませるのは Studio、$236。[[web-edit-agent-davinci-resolve-premiere-scripting]]）。Premiere は Creative Cloud の契約（西尾は Mac で 25.0 を使った記録がある。26.0 以上でないと OTIO を読まない）。Final Cut Pro は Mac の有料アプリ
- 素材は手元に残り、形式自体はどこにも送らない

## この wiki への含意

- **「LLM が編集の決定を書き、人が編集ソフトで仕上げる」の受け渡し口**。THINKLET のデモ（[[exp-thinklet-reading-demo-video]]）は西尾が Premiere で 36 分ほどで手編集した。LLM が「どの区間を残すか」を OTIO に書いて Premiere 26 に読ませれば、人の仕事は「並んだ下書きを直す」に変わる（未検証）。ただし Premiere 26.0 以上が要る（西尾の記録は 25.0）
- **shortmovie-draft-generator の出力の形と並べる**: [[exp-shortmovie-draft-generator]] は企画書 Markdown と SRT を出し、切り出しは ffmpeg で焼いた。カット案を OTIO で出していれば、人は編集ソフトで「下書きのタイムライン」として開けた。経験の「タイムスタンプは字幕データを正とし、LLM には触らせない」は OTIO でも同じで、LLM に書かせるのは区間の番号（どの字幕の chunk からどの chunk まで）にして、秒への変換はプログラムがやるのが安全（このページの提案、未検証）
- **Remotion と経験の方式の出口**: 西尾の描画は HTML/canvas を 1 コマずつ撮る方式（[[exp-html-capture-pipeline]]）で、Remotion ではない。Remotion の skill の考え方（描いた部分は透明の動画に焼いて上に置き、素材は OTIO のクリップのまま渡す）は、実物の収録と描いた重ねを混ぜる promo（[[work-promotion-video]] の暫定の答え）を「編集ソフトで直せる形」で渡すのに使える
- EDL は映像 1 トラックしか持たないので、画面収録の上に重ねを置く形には向かない。切り抜き（1 トラックの順のつなぎ）なら足りる

## 着手の仕方（未検証。galleria で確かめる）

- **何ができるようになるか**: LLM に書かせた「残す区間の一覧（JSON）」から `.otio`（と、必要なら `.edl`・FCP7 `.xml`）を作り、Resolve／Premiere で下書きのタイムラインとして開く。効く型: promo（切り抜き・実物の収録の組み立て）、talk（講演の録画の詰め）。embed は短いので手でも足りる
- **機械**: galleria WSL（OTIO の書き出し）、開くのは galleria Windows の Resolve（無料版で手で読み込み）か Mac の Premiere 26 以上。入れるもの: `OpenTimelineIO-Plugins==0.18.1`（uv で一時環境）。費用 0、アカウント不要
- **成熟度**: 本体は安定と自称、最新 0.18.1（2025-11-09）から 1 年リリースなし、push は続いている。fcpx_xml アダプタは 2024-06 で止まっている
- **最小の手順**（WSL。OTIO の例を元にし、JSON の形はこのページの提案）:
  ```bash
  mkdir -p ~/video-tools-trial/otio && cd ~/video-tools-trial/otio
  ffprobe -v error -select_streams v:0 -show_entries stream=r_frame_rate,duration -of json talk.mp4
  # cuts.json は LLM が書く: {"fps":30,"source":"talk.mp4","ranges":[[12.40,25.10],[40.00,58.30]]}
  uv run --with OpenTimelineIO-Plugins==0.18.1 python cuts_to_otio.py cuts.json out
  ```
  `cuts_to_otio.py`（推測で書いた最小形）:
  ```python
  import json, sys, opentimelineio as otio
  c = json.load(open(sys.argv[1])); fps = c["fps"]; RT = otio.opentime.RationalTime
  tl = otio.schema.Timeline(name="draft"); tr = otio.schema.Track(name="V1"); tl.tracks.append(tr)
  for i, (s, e) in enumerate(c["ranges"]):
      ref = otio.schema.ExternalReference(target_url=c["source"])
      tr.append(otio.schema.Clip(name=f"cut{i+1}", media_reference=ref,
          source_range=otio.opentime.TimeRange(RT(round(s*fps), fps), RT(round((e-s)*fps), fps))))
  out = sys.argv[2]
  otio.adapters.write_to_file(tl, out + ".otio")
  otio.adapters.write_to_file(tl, out + ".edl", adapter_name="cmx_3600")
  otio.adapters.write_to_file(tl, out + ".xml", adapter_name="fcp_xml")
  print(tl.duration().to_seconds())
  ```
  映像と音声を両方運ぶには音声トラック（`kind=otio.schema.TrackKind.Audio`）にも同じクリップを足す（推測。Resolve・Premiere が映像トラックだけの OTIO で音を付けるかは未確認）。`target_url` は Windows 側から見えるパス（`file:///C:/...` か相対パス）にする必要がある見込み（推測）
- **動いたと言える確かめ方**: (1) スクリプトが出す長さ（秒）が `ranges` の合計と 1 コマ以内で一致する。(2) `otio.adapters.read_from_file("out.otio")` で読み戻してクリップ数が同じ。(3) Resolve の File > Import > Timeline で `out.otio` を開き、タイムラインのクリップ数・各クリップの In/Out のタイムコードが JSON と合う（スクリーンショット 1 枚で記録）。(4) 同じものを `.edl` と `.xml` でも開き、どれが崩れるか（日本語のファイル名を含む版も）を表にする
- **所要の見込み（推測）**: 書き出しまで 30 分。Resolve で 3 形式を開き比べて 1 時間

## Open Questions

- Premiere が OTIO を読むのは 25.6 からか 26.0 からか（Remotion の docs と Adobe の release notes が食い違う）。西尾の Mac の Premiere の版
- FCPXML 1.14 の仕様書の所在（Apple の開発者向け docs は古い版のまま）。fcpx_xml アダプタ（2023-07 の v1.0.0）が 1.13・1.14 を読み書きできるかは未確認
- 日本語のクリップ名・ファイル名が EDL・FCP7 XML・OTIO でそれぞれ Resolve・Premiere に通るか
- LLM が OTIO の JSON を直接書く（API を使わない）と、どのくらい壊れるか。測った文献は見つからなかった
- 字幕・文字の重ねを運べない問題: 字幕は SRT、文字の重ねは透明の動画（Remotion の方式）で足りるか

