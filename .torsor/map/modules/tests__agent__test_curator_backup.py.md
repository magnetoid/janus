---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_curator_backup.py

Symbols in `tests/agent/test_curator_backup.py`.

- L17 `backup_env(monkeypatch, tmp_path)` (function) — Isolate HERMES_HOME + reload modules so every test starts clean.
- L33 `_write_skill(skills_dir: Path, name: str, body: str='body')` (function)
- L47 `test_snapshot_creates_tarball_and_manifest(backup_env)` (function)
- L61 `test_snapshot_excludes_backups_dir_itself(backup_env)` (function) — The backup must NOT contain .curator_backups/ — that would recurse
- L77 `test_snapshot_excludes_hub_dir(backup_env)` (function) — .hub/ is managed by the skills hub. Rolling it back would break
- L92 `test_snapshot_disabled_returns_none(backup_env, monkeypatch)` (function)
- L101 `test_snapshot_uniquifies_when_same_second(backup_env, monkeypatch)` (function) — Two snapshots in the same wallclock second must not clobber each
- L115 `test_snapshot_prunes_to_keep_count(backup_env, monkeypatch)` (function)
- L135 `test_list_backups_empty(backup_env)` (function)
- L140 `test_list_backups_returns_manifest_data(backup_env)` (function)
- L150 `test_resolve_backup_newest_when_no_id(backup_env, monkeypatch)` (function)
- L164 `test_resolve_backup_unknown_id_returns_none(backup_env)` (function)
- L175 `test_rollback_restores_deleted_skill(backup_env)` (function) — The whole point of this feature: user loses a skill, rollback
- L194 `test_rollback_is_itself_undoable(backup_env)` (function) — A rollback creates its own safety snapshot before replacing the
- L229 `test_rollback_no_snapshots_returns_error(backup_env)` (function)
- L236 `test_rollback_rejects_unsafe_tarball(backup_env, monkeypatch)` (function) — Tarballs with absolute paths or .. components must be refused even
- L266 `test_real_run_takes_pre_snapshot(backup_env, monkeypatch)` (function) — A real (non-dry) curator pass must snapshot the tree before calling
- L297 `test_dry_run_skips_snapshot(backup_env, monkeypatch)` (function) — Dry-run previews must not spend disk on a snapshot — they don't
- L324 `_write_cron_jobs(home: Path, jobs: list)` (function) — Write a synthetic cron/jobs.json under HERMES_HOME. Returns the path.
- L338 `_reload_cron_jobs(home: Path)` (function) — Reload cron.jobs so its module-level HERMES_DIR picks up the tmp HOME.
- L351 `test_snapshot_includes_cron_jobs(backup_env)` (function) — With a cron/jobs.json present, snapshot writes cron-jobs.json and records it in manifest.
- L369 `test_snapshot_without_cron_jobs_file_still_succeeds(backup_env)` (function) — No cron/jobs.json on disk → snapshot succeeds, manifest records absence.
- L384 `test_snapshot_cron_jobs_malformed_json_still_captured(backup_env)` (function) — Malformed jobs.json is still copied to the snapshot (fidelity over
- L403 `test_rollback_restores_cron_skill_links(backup_env)` (function) — End-to-end: snapshot with job [alpha,beta], curator-style in-place
- L437 `test_rollback_only_touches_skill_fields(backup_env)` (function) — Every field other than skills/skill must remain untouched across rollback.
- L482 `test_rollback_skips_jobs_the_user_deleted(backup_env)` (function) — If the user deleted a cron job after the snapshot, rollback must
- L508 `test_rollback_leaves_new_jobs_untouched(backup_env)` (function) — Jobs created AFTER the snapshot must pass through rollback unchanged.
- L535 `test_rollback_with_snapshot_missing_cron_succeeds(backup_env)` (function) — Older snapshots (created before this feature shipped) have no
- L563 `test_restore_cron_skill_links_standalone(backup_env)` (function) — Unit-level test on _restore_cron_skill_links without the full rollback.
