---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cron/test_cron_workdir.py

Symbols in `tests/cron/test_cron_workdir.py`.

- L21 `tmp_cron_dir(tmp_path, monkeypatch)` (function) — Isolate cron job storage into a temp dir so tests don't stomp on real jobs.
- L33 `TestNormalizeWorkdir` (class)
- L34 `test_none_returns_none(self)` (method)
- L38 `test_empty_string_returns_none(self)` (method)
- L43 `test_absolute_existing_dir_returns_resolved_str(self, tmp_path)` (method)
- L48 `test_tilde_expands(self, tmp_path, monkeypatch)` (method)
- L54 `test_relative_path_rejected(self)` (method)
- L59 `test_missing_dir_rejected(self, tmp_path)` (method)
- L65 `test_file_not_dir_rejected(self, tmp_path)` (method)
- L77 `TestCreateJobWorkdir` (class)
- L78 `test_workdir_stored_when_set(self, tmp_cron_dir)` (method)
- L88 `test_workdir_none_preserves_old_behaviour(self, tmp_cron_dir)` (method)
- L96 `test_create_rejects_invalid_workdir(self, tmp_cron_dir)` (method)
- L106 `TestUpdateJobWorkdir` (class)
- L107 `test_set_workdir_via_update(self, tmp_cron_dir)` (method)
- L113 `test_clear_workdir_with_none(self, tmp_cron_dir)` (method)
- L121 `test_clear_workdir_with_empty_string(self, tmp_cron_dir)` (method)
- L129 `test_update_rejects_invalid_workdir(self, tmp_cron_dir)` (method)
- L140 `TestCronjobToolWorkdir` (class)
- L141 `test_create_with_workdir_json_roundtrip(self, tmp_cron_dir)` (method)
- L155 `test_create_without_workdir_hides_field_in_format(self, tmp_cron_dir)` (method)
- L169 `test_update_clears_workdir_with_empty_string(self, tmp_cron_dir)` (method)
- L188 `test_schema_advertises_workdir(self)` (method)
- L199 `TestTickWorkdirPartition` (class) — tick() must run workdir jobs sequentially (outside the ThreadPoolExecutor)
- L207 `test_workdir_jobs_run_sequentially(self, tmp_path, monkeypatch)` (method)
- L259 `TestRunJobTerminalCwd` (class) — run_job sets TERMINAL_CWD + flips skip_context_files=False when workdir
- L267 `_install_stubs(monkeypatch, observed: dict)` (method) — Patch enough of run_job's deps that it executes without real creds.
- L321 `test_workdir_sets_and_restores_terminal_cwd(self, tmp_path, monkeypatch)` (method)
- L355 `test_no_workdir_leaves_terminal_cwd_untouched(self, monkeypatch)` (method) — When workdir is absent, run_job must not touch TERMINAL_CWD at all —
