"""Agentic RAG — multi-hop retrieval over a user-provided corpus.

Janus searches its own sessions (FTS5) and memory (agent/memory_recall.py); this
adds retrieval over an EXTERNAL corpus you register — a code repo, a docs folder,
a knowledge base. The agent drives the loop: it issues a query, gets the most
relevant chunks with ``file:line`` citations, and can issue follow-up queries
based on what it finds (multi-hop) — that agentic control is what makes it RAG
rather than a one-shot grep.

Dependency-free lexical relevance (token overlap, length-normalized) over
line-window chunks — deterministic and always available; a vector backend can
layer on later. Corpora are registered in ``~/.janus/corpora.json``.
"""
from __future__ import annotations

import json
import logging
import re
from pathlib import Path
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)

# Conservative defaults so a search over a big repo stays bounded + fast.
_TEXT_EXTS = {
    ".py", ".js", ".ts", ".tsx", ".jsx", ".go", ".rs", ".java", ".rb", ".c", ".h",
    ".cpp", ".cc", ".md", ".txt", ".rst", ".json", ".yaml", ".yml", ".toml", ".cfg",
    ".ini", ".sh", ".html", ".css", ".sql", ".tex",
}
_SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__", "dist", "build",
              ".next", ".cache", "target", ".pytest_cache", ".torsor"}
_CHUNK_LINES = 20
_MAX_FILES = 800
_MAX_FILE_BYTES = 400_000

_STOP = {
    "the", "a", "an", "is", "are", "was", "to", "of", "and", "or", "in", "on", "for",
    "with", "it", "that", "this", "as", "at", "by", "from", "be", "not", "do",
}


def get_corpora_path() -> Path:
    from janus_constants import get_janus_home
    return get_janus_home() / "corpora.json"


def load_corpora() -> Dict[str, str]:
    path = get_corpora_path()
    if not path.is_file():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except (ValueError, OSError):
        return {}


def _save_corpora(data: Dict[str, str]) -> None:
    path = get_corpora_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def register_corpus(name: str, path: str) -> Dict[str, Any]:
    name = re.sub(r"[^a-z0-9_-]+", "-", str(name).strip().lower()).strip("-")
    p = Path(path).expanduser()
    if not name:
        return {"ok": False, "error": "a corpus name is required"}
    if not p.is_dir():
        return {"ok": False, "error": f"not a directory: {p}"}
    corpora = load_corpora()
    corpora[name] = str(p.resolve())
    _save_corpora(corpora)
    return {"ok": True, "name": name, "path": str(p.resolve())}


def remove_corpus(name: str) -> bool:
    corpora = load_corpora()
    if name in corpora:
        del corpora[name]
        _save_corpora(corpora)
        return True
    return False


def _tokens(s: str) -> set:
    # split on non-alphanumerics INCLUDING underscores, so snake_case identifiers
    # (deploy_staging) match the query's individual words (deploy, staging).
    return {w for w in re.findall(r"[a-z0-9]+", str(s).lower()) if len(w) > 2 and w not in _STOP}


def _iter_chunks(root: Path):
    """Yield (file_path, start_line, text) line-window chunks across a corpus."""
    import os

    count = 0
    for dp, dns, fns in os.walk(root):
        dns[:] = [d for d in dns if d not in _SKIP_DIRS and not d.startswith(".")]
        for fn in sorted(fns):
            if Path(fn).suffix.lower() not in _TEXT_EXTS:
                continue
            fp = Path(dp) / fn
            try:
                if fp.stat().st_size > _MAX_FILE_BYTES:
                    continue
                lines = fp.read_text(encoding="utf-8", errors="ignore").splitlines()
            except OSError:
                continue
            for i in range(0, len(lines), _CHUNK_LINES):
                window = lines[i:i + _CHUNK_LINES]
                text = "\n".join(window).strip()
                if text:
                    yield fp, i + 1, text
            count += 1
            if count >= _MAX_FILES:
                return


def search_corpus(query: str, *, corpus: Optional[str] = None, n: int = 5,
                  root: Optional[Path] = None) -> List[Dict[str, Any]]:
    """Return up to ``n`` most-relevant chunks for ``query`` with file:line citations.

    ``corpus`` selects a registered corpus by name (or the only one if omitted);
    ``root`` overrides with an explicit path (used by tests). Never raises.
    """
    qt = _tokens(query)
    if not qt:
        return []
    try:
        if root is None:
            corpora = load_corpora()
            if corpus:
                root_str = corpora.get(corpus)
            elif len(corpora) == 1:
                root_str = next(iter(corpora.values()))
            else:
                root_str = None
            if not root_str:
                return []
            root = Path(root_str)
        if not Path(root).is_dir():
            return []
        scored: List[Dict[str, Any]] = []
        for fp, start, text in _iter_chunks(Path(root)):
            ct = _tokens(text)
            if not ct:
                continue
            overlap = len(qt & ct)
            if overlap == 0:
                continue
            score = round(overlap / (len(ct) ** 0.5), 4)
            try:
                rel = str(fp.relative_to(Path(root)))
            except ValueError:
                rel = str(fp)
            snippet = text if len(text) <= 280 else text[:280] + "…"
            scored.append({"file": rel, "line": start, "score": score, "snippet": snippet})
        scored.sort(key=lambda x: x["score"], reverse=True)
        return scored[:n]
    except Exception as exc:
        logger.debug("corpus search failed: %s", exc)
        return []
