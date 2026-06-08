---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/curator_backup.py

Symbols in `agent/curator_backup.py`.

- L70 `_backups_dir()` (function)
- L74 `_skills_dir()` (function)
- L78 `_cron_jobs_file()` (function) — Source path for the live cron jobs store (``~/.hermes/cron/jobs.json``).
- L86 `_backup_cron_jobs_into(dest: Path)` (function) — Copy the live cron jobs.json into ``dest`` as ``cron-jobs.json``.
- L132 `_utc_id(now: Optional[datetime]=None)` (function) — UTC ISO-ish filesystem-safe timestamp: ``2026-05-01T13-05-42Z``.
- L143 `_load_config()` (function)
- L159 `is_enabled()` (function) — Default ON — the whole point of the backup is safety by default.
- L164 `get_keep()` (function)
- L177 `_count_skill_files(base: Path)` (function)
- L186 `_write_manifest(dest: Path, reason: str, archive_path: Path, skills_counted: int, cron_info: Optional[Dict[str, Any]]=None)` (function)
- L211 `snapshot_skills(reason: str='manual')` (function) — Create a tar.gz snapshot of ``~/.hermes/skills/`` and prune old ones.
- L284 `_prune_old(keep: int)` (function) — Delete regular snapshots beyond the newest *keep*. Returns deleted
- L325 `_read_manifest(snap_dir: Path)` (function)
- L335 `list_backups()` (function) — Return all restorable snapshots, newest first. Only entries with a
- L364 `_resolve_backup(backup_id: Optional[str])` (function) — Return the path of the requested backup, or the newest one if
- L386 `_restore_cron_skill_links(snapshot_dir: Path)` (function) — Reconcile backed-up cron skill links into the live ``cron/jobs.json``.
- L529 `rollback(backup_id: Optional[str]=None)` (function) — Restore ``~/.hermes/skills/`` from a snapshot.
- L674 `format_size(n: int)` (function)
- L682 `summarize_backups()` (function)
