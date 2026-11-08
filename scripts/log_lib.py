"""log_lib: atomic per-entry log の読み書き（後方互換）。

背景: 構造的負債は全部atomic単位をshared Markdownに通したartifact-20260624

- 新 entry は `wiki/log/<ts>-<op>-<hash>.md` に **1 ファイル 1 entry** で atomic に追加する
  → 並行 session の entry が別ファイルになり commit 競合・hunk 外科手術が消える。
- `wiki/log.md` は **frozen archive**（cutover 以前の entry）。手で append しない。
- reader は `read_log_text()` で `log/` + `log.md` を merge して読む（従来の regex がそのまま効く）。
- `log/` が無い wiki は従来通り `log.md` だけ読む（**後方互換**。森の他 wiki は無影響）。
"""
import re
import hashlib
from pathlib import Path

# `## [YYYY-MM-DD( HH:MM)?] <ops> |` を拾う（log.md / per-entry file 共通）
TS_RE = re.compile(
    r"##\s*\[(\d{4}-\d{2}-\d{2})(?:\s+(\d{2}:\d{2}))?\]\s*([^|\n]+)\|")


def logdir_for(log_md_path: Path) -> Path:
    """log.md と同じ階層の `log/` ディレクトリ。"""
    return Path(log_md_path).parent / "log"


def entry_files(log_md_path) -> list:
    """per-entry file を新しい順（filename が ts 始まりなので逆順）に返す。"""
    d = logdir_for(log_md_path)
    if not d.is_dir():
        return []
    return sorted(d.glob("*.md"), reverse=True)


def read_log_text(log_md_path) -> str:
    """`log/` per-entry files（新しい順）＋ `log.md` archive を merge した text。

    `log/` が無ければ `log.md` の中身そのまま（後方互換）。reader はこの戻り値に
    対して従来の `## [ts] op |` regex をかければよい。
    """
    log_md_path = Path(log_md_path)
    files = entry_files(log_md_path)
    archive = log_md_path.read_text(encoding="utf-8") if log_md_path.exists() else ""
    if not files:
        return archive
    body = re.sub(r"\A#\s*Log\s*\n+", "", archive)  # archive 先頭の "# Log" header を外す
    parts = [f.read_text(encoding="utf-8").rstrip() + "\n" for f in files]
    merged = "# Log\n\n" + "\n".join(parts)
    if body.strip():
        merged += "\n" + body
    return merged


def _slug(op: str) -> str:
    op = re.sub(r"@\w+", "", op).strip()           # @model tag 除去
    op = re.sub(r"[^0-9A-Za-z]+", "-", op).strip("-")  # ASCII 以外は畳む（日本語 op は空になりうる）
    return op[:24] or "entry"


def add_entry(wiki_dir, entry_text: str) -> Path:
    """`## [ts] op | ...` で始まる 1 entry を `wiki/log/` に atomic に書く。

    ファイル名 = `<ts>-<op>-<contenthash8>.md`。同内容は同名（冪等）、別内容は別名
    （並行 session でも衝突しない）。戻り値 = 書いたパス。
    """
    wiki_dir = Path(wiki_dir)
    d = wiki_dir / "log"
    d.mkdir(exist_ok=True)
    m = TS_RE.search(entry_text)
    if not m:
        raise ValueError("entry は '## [YYYY-MM-DD HH:MM] op | ...' で始める必要があります")
    date, time, op = m.group(1), m.group(2) or "2359", m.group(3)
    ts = date.replace("-", "") + "-" + time.replace(":", "")
    h = hashlib.sha1(entry_text.encode("utf-8")).hexdigest()[:8]
    path = d / f"{ts}-{_slug(op)}-{h}.md"
    path.write_text(entry_text.rstrip() + "\n", encoding="utf-8")
    return path


def latest_ts(log_md_path):
    """最新 entry の 'YYYY-MM-DD HH:MM'（時刻なしは 23:59 扱い）。無ければ None。"""
    best = None
    for m in TS_RE.finditer(read_log_text(log_md_path)):
        ts = m.group(1) + " " + (m.group(2) or "23:59")
        if best is None or ts > best:
            best = ts
    return best
