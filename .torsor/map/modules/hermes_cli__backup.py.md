---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/backup.py

Symbols in `hermes_cli/backup.py`.

- L68 `_should_exclude(rel_path: Path)` (function) — Return True if *rel_path* (relative to hermes root) should be skipped.
- L88 `_should_skip_backup_file(abs_path: Path, rel_path: Path, out_path: Path)` (function) — Return True when a candidate file should not be written to a backup zip.
- L108 `_safe_copy_db(src: Path, dst: Path)` (function) — Copy a SQLite database safely using the backup() API.
- L135 `_format_size(nbytes: int)` (function) — Human-readable file size.
- L144 `run_backup(args)` (function) — Create a zip backup of the Hermes home directory.
- L265 `_validate_backup_zip(zf: zipfile.ZipFile)` (function) — Check that a zip looks like a Hermes backup.
- L292 `_detect_prefix(zf: zipfile.ZipFile)` (function) — Detect if the zip has a common directory prefix wrapping all entries.
- L316 `run_import(args)` (function) — Restore a Hermes backup from a zip file.
- L507 `_quick_snapshot_root(hermes_home: Optional[Path]=None)` (function)
- L512 `create_quick_snapshot(label: Optional[str]=None, hermes_home: Optional[Path]=None, keep: Optional[int]=None)` (function) — Create a quick state snapshot of critical files.
- L598 `list_quick_snapshots(limit: int=20, hermes_home: Optional[Path]=None)` (function) — List existing quick state snapshots, most recent first.
- L624 `restore_quick_snapshot(snapshot_id: str, hermes_home: Optional[Path]=None)` (function) — Restore state from a quick snapshot.
- L678 `_count_cron_jobs(path: Path)` (function) — Return the number of cron jobs stored in ``path``.
- L705 `restore_cron_jobs_if_emptied(snapshot_id: str, hermes_home: Optional[Path]=None)` (function) — Safety net for silent cron-job loss across ``hermes update``.
- L772 `_prune_quick_snapshots(root: Path, keep: int=_QUICK_DEFAULT_KEEP)` (function) — Remove oldest quick snapshots beyond the keep limit. Returns count deleted.
- L794 `prune_quick_snapshots(keep: int=_QUICK_DEFAULT_KEEP, hermes_home: Optional[Path]=None)` (function) — Manually prune quick snapshots. Returns count deleted.
- L802 `run_quick_backup(args)` (function) — CLI entry point for hermes backup --quick.
- L819 `_write_full_zip_backup(out_path: Path, hermes_root: Path)` (function) — Write a full zip snapshot of ``hermes_root`` to ``out_path``.
- L889 `_pre_update_backup_dir(hermes_home: Optional[Path]=None)` (function)
- L894 `_prune_pre_update_backups(backup_dir: Path, keep: int)` (function) — Remove oldest pre-update backups beyond the keep limit.
- L931 `create_pre_update_backup(hermes_home: Optional[Path]=None, keep: int=_PRE_UPDATE_DEFAULT_KEEP)` (function) — Create a full zip backup of HERMES_HOME under ``backups/``.
- L975 `_prune_pre_migration_backups(backup_dir: Path, keep: int)` (function) — Remove oldest pre-migration backups beyond the keep limit.
- L1003 `create_pre_migration_backup(hermes_home: Optional[Path]=None, keep: int=_PRE_MIGRATION_DEFAULT_KEEP)` (function) — Create a full zip backup of HERMES_HOME under ``backups/`` before a
