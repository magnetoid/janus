"""Shared team memory — a common knowledge layer across assistants / people.

Each profile keeps its PRIVATE memory (MEMORY.md / USER.md). This adds an
OPTIONAL SHARED layer: a ``TEAM.md`` in a configured directory
(``memory.team_dir``) that any profile pointing at the same path can read — so a
team (or your own several assistants) share common facts while keeping
per-assistant isolation. Point ``memory.team_dir`` at a synced folder, a network
share, or a git repo to share across machines.

Reads are merged into the agent's memory snapshot (sanitized — a teammate's
entry is untrusted input). Writes go explicitly to the shared file with author
attribution, never silently from the private memory tool.
"""
from __future__ import annotations

import logging
from pathlib import Path
from typing import List, Optional

logger = logging.getLogger(__name__)

TEAM_FILE = "TEAM.md"
ENTRY_DELIMITER = "\n§\n"  # matches tools/memory_tool.ENTRY_DELIMITER


def get_team_dir() -> Optional[Path]:
    """The configured shared-memory directory (``memory.team_dir``), or None."""
    try:
        import yaml
        from janus_constants import get_janus_home

        cfg_path = get_janus_home() / "config.yaml"
        if not cfg_path.is_file():
            return None
        cfg = yaml.safe_load(cfg_path.read_text(encoding="utf-8")) or {}
        td = (cfg.get("memory") or {}).get("team_dir", "")
        if isinstance(td, str) and td.strip():
            return Path(td.strip()).expanduser()
    except Exception:
        pass
    return None


def is_enabled() -> bool:
    return get_team_dir() is not None


def _team_file() -> Optional[Path]:
    d = get_team_dir()
    return (d / TEAM_FILE) if d else None


def load_team_entries() -> List[str]:
    """Read shared team entries (empty if disabled or missing)."""
    f = _team_file()
    if not f or not f.is_file():
        return []
    try:
        text = f.read_text(encoding="utf-8")
    except OSError:
        return []
    seen, out = set(), []
    for e in text.split(ENTRY_DELIMITER):
        e = e.strip()
        if e and e not in seen:
            seen.add(e)
            out.append(e)
    return out


def add_team_entry(content: str, *, author: str = "") -> bool:
    """Append a fact to the shared team memory. Returns True on success."""
    content = content.strip()
    if not content:
        return False
    d = get_team_dir()
    if d is None:
        return False
    stamped = f"{content}  — {author}" if author else content
    try:
        d.mkdir(parents=True, exist_ok=True)
        entries = load_team_entries()
        if stamped in entries:
            return True
        entries.append(stamped)
        _team_file().write_text(ENTRY_DELIMITER.join(entries) + "\n", encoding="utf-8")
        return True
    except OSError as exc:
        logger.debug("team memory write failed: %s", exc)
        return False


def remove_team_entry(substring: str) -> bool:
    """Remove the first shared entry containing ``substring``. Returns True if removed."""
    substring = substring.strip()
    f = _team_file()
    if not substring or not f or not f.is_file():
        return False
    entries = load_team_entries()
    kept = []
    removed = False
    for e in entries:
        if not removed and substring in e:
            removed = True
            continue
        kept.append(e)
    if removed:
        try:
            f.write_text(ENTRY_DELIMITER.join(kept) + ("\n" if kept else ""), encoding="utf-8")
        except OSError:
            return False
    return removed


def render_team_block() -> str:
    """Render shared entries for system-prompt injection (label included)."""
    entries = load_team_entries()
    if not entries:
        return ""
    body = "\n".join(f"- {e}" for e in entries)
    return f"[Shared team memory]\n{body}"
