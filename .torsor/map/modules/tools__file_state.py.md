---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/file_state.py

Symbols in `tools/file_state.py`.

- L59 `FileStateRegistry` (class) — Process-wide coordinator for cross-agent file edits.
- L62 `__init__(self)` (method)
- L70 `_lock_for(self, resolved: str)` (method)
- L79 `lock_path(self, resolved: str)` (method) — Acquire the per-path lock for a read→modify→write section.
- L93 `record_read(self, task_id: str, resolved: str, *, partial: bool=False, mtime: Optional[float]=None)` (method)
- L114 `note_write(self, task_id: str, resolved: str, *, mtime: Optional[float]=None)` (method) — Record a successful write.
- L142 `check_stale(self, task_id: str, resolved: str)` (method) — Return a model-facing warning if this write would be stale.
- L218 `writes_since(self, exclude_task_id: str, since_ts: float, paths: Iterable[str])` (method) — Return ``{writer_task_id: [paths]}`` for writes done after
- L244 `known_reads(self, task_id: str)` (method) — Return the list of resolved paths this agent has read.
- L252 `clear(self)` (method) — Reset all state.  Intended for tests only.
- L265 `get_registry()` (function)
- L269 `_disabled()` (function)
- L274 `_fmt_ts(ts: float)` (function)
- L280 `_cap_dict(d: dict, limit: int)` (function) — Trim a dict to ``limit`` entries by dropping insertion-order oldest.
- L295 `record_read(task_id: str, resolved_or_path: str | Path, *, partial: bool=False)` (function)
- L299 `note_write(task_id: str, resolved_or_path: str | Path)` (function)
- L303 `check_stale(task_id: str, resolved_or_path: str | Path)` (function)
- L307 `lock_path(resolved_or_path: str | Path)` (function)
- L311 `writes_since(exclude_task_id: str, since_ts: float, paths: Iterable[str | Path])` (function)
- L319 `known_reads(task_id: str)` (function)
