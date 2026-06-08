---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/disk-cleanup/disk_cleanup.py

Symbols in `plugins/disk-cleanup/disk_cleanup.py`.

- L48 `get_state_dir()` (function) — State dir — separate from ``$HERMES_HOME/logs/``.
- L53 `get_tracked_file()` (function)
- L57 `get_log_file()` (function) — Audit log — intentionally NOT under ``$HERMES_HOME/logs/``.
- L66 `is_safe_path(path: Path)` (function) — Accept only paths under HERMES_HOME or ``/tmp/hermes-*``.
- L88 `_log(message: str)` (function)
- L104 `load_tracked()` (function) — Load tracked.json.  Restores from ``.bak`` on corruption.
- L127 `save_tracked(tracked: List[Dict[str, Any]])` (function) — Atomic write: ``.tmp`` → backup old → rename.
- L154 `_is_protected_cron_path(p: Path)` (function) — Return True if *p* is a cron control-plane file/directory that must
- L175 `fmt_size(n: float)` (function)
- L187 `track(path_str: str, category: str, silent: bool=False)` (function) — Register a file for tracking. Returns True if newly tracked.
- L223 `forget(path_str: str)` (function) — Remove a path from tracking without deleting the file.
- L240 `dry_run()` (function) — Return (auto_delete_list, needs_prompt_list) without touching files.
- L284 `quick()` (function) — Safe deterministic cleanup — no prompts.
- L399 `deep(confirm: Optional[callable]=None)` (function) — Deep cleanup.
- L470 `status()` (function) — Return per-category breakdown and top 10 largest tracked files.
- L493 `format_status(s: Dict[str, Any])` (function) — Human-readable status string (for slash command output).
- L521 `guess_category(path: Path)` (function) — Return a category label for *path*, or None if we shouldn't track it.
