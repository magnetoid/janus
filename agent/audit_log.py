"""Tamper-evident autonomy audit log (gap G12).

A hash-chained, append-only JSONL stream of autonomy-critical events — freeze /
unfreeze of the kill switch, self-modification promotions and rollbacks, kanban
injection blocks. Each row commits to the previous row's hash:

    hash = sha256(prev_hash + canonical_json(ts, kind, data))

so removing, reordering, or editing any row breaks the chain from that point on.
``verify()`` recomputes the chain and reports the first broken index — an
operator or a governance review can prove the record is intact without trusting
the process that wrote it. This is the "unified tamper-evident audit stream" the
self-improvement audit flagged as missing (docs/self-improvement-evaluation-2026.md
§8): today freeze/spawn/promote events are scattered across debug logs and
per-task event tables with no integrity guarantee.

Best-effort and never raises into a caller: an audit-write failure must not halt
the action being audited (the action's own gate is the control; the log is the
record). Appends are serialized with the shared store lock so a concurrent
writer can't interleave a torn row into the chain.
"""
from __future__ import annotations

import hashlib
import json
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

logger = logging.getLogger(__name__)


def audit_path() -> Path:
    from janus_constants import get_janus_home
    return get_janus_home() / "learning" / "autonomy_audit.jsonl"


def _now_iso() -> str:
    try:
        from janus_time import now as _now
        return _now().isoformat()
    except Exception:
        return ""


def _row_digest(prev_hash: str, ts: str, kind: str, data: Dict[str, Any]) -> str:
    """Deterministic hash over the row's committed content + the prior hash."""
    payload = json.dumps(
        {"ts": ts, "kind": kind, "data": data},
        sort_keys=True, ensure_ascii=False, separators=(",", ":"),
    )
    return hashlib.sha256((prev_hash + payload).encode("utf-8")).hexdigest()


def _last_hash(path: Path) -> str:
    """The hash of the final row, or '' when the log is empty/absent."""
    try:
        if not path.is_file():
            return ""
        last = ""
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line:
                last = line
        if not last:
            return ""
        return str(json.loads(last).get("hash", ""))
    except Exception:
        return ""


def append_event(kind: str, data: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
    """Append one hash-chained event. Returns the written row, or None on error.
    Best-effort — never raises; an audit failure must not block the audited action."""
    try:
        data = data if isinstance(data, dict) else {}
        # Reject an un-serializable payload up front so a bad row never enters
        # the chain (which would make every later row fail to verify).
        try:
            json.dumps(data, ensure_ascii=False)
        except (TypeError, ValueError):
            logger.debug("audit append: non-serializable payload for %r — skipped", kind)
            return None
        ts = _now_iso()
        path = audit_path()
        from agent.store_lock import locked_store
        with locked_store(path):
            prev = _last_hash(path)
            digest = _row_digest(prev, ts, str(kind), data)
            row = {"ts": ts, "kind": str(kind), "data": data,
                   "prev_hash": prev, "hash": digest}
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("a", encoding="utf-8") as f:
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
        return row
    except Exception as exc:
        logger.debug("audit append failed: %s", exc)
        return None


def _load_rows(path: Path) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    if not path.is_file():
        return rows
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            rows.append(json.loads(line))
    return rows


def verify() -> Tuple[bool, Optional[int]]:
    """Recompute the hash chain. Returns ``(ok, first_broken_index)``.

    A row is broken when its recorded ``prev_hash`` doesn't match the running
    chain hash, or its ``hash`` doesn't match a recompute over its own content —
    i.e. the row was edited, removed, or reordered. ``(True, None)`` on an intact
    (or empty) log. A read/parse error is reported as broken at index 0 rather
    than silently passing."""
    try:
        rows = _load_rows(audit_path())
    except Exception:
        return False, 0
    prev = ""
    for i, row in enumerate(rows):
        if not isinstance(row, dict):
            return False, i
        if row.get("prev_hash", "") != prev:
            return False, i
        expected = _row_digest(prev, row.get("ts", ""), row.get("kind", ""),
                               row.get("data", {}) if isinstance(row.get("data"), dict) else {})
        if row.get("hash", "") != expected:
            return False, i
        prev = row.get("hash", "")
    return True, None
