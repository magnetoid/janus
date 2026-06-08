---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_file_sync.py

Symbols in `tests/tools/test_file_sync.py`.

- L14 `tmp_files(tmp_path)` (function) — Create a few temp files to use as sync sources.
- L24 `_make_get_files(tmp_files, remote_base='/root/.hermes')` (function) — Return a get_files_fn that maps local files to remote paths.
- L34 `_make_manager(tmp_files, remote_base='/root/.hermes', upload=None, delete=None)` (function) — Create a FileSyncManager with test callbacks.
- L43 `TestMtimeSkip` (class)
- L44 `test_unchanged_files_not_re_uploaded(self, tmp_files)` (method)
- L55 `test_changed_file_re_uploaded(self, tmp_files)` (method)
- L70 `test_new_file_detected(self, tmp_files, tmp_path)` (method)
- L93 `TestDeletion` (class)
- L94 `test_removed_file_triggers_delete(self, tmp_files)` (method)
- L112 `test_no_delete_when_no_removals(self, tmp_files)` (method)
- L121 `TestTransactionalRollback` (class)
- L122 `test_upload_failure_rolls_back(self, tmp_files)` (method)
- L142 `test_delete_failure_rolls_back(self, tmp_files)` (method)
- L166 `TestRateLimiting` (class)
- L167 `test_sync_skipped_within_interval(self, tmp_files)` (method)
- L184 `test_force_bypasses_rate_limit(self, tmp_files, tmp_path)` (method)
- L205 `test_env_var_forces_sync(self, tmp_files, tmp_path)` (method)
- L227 `TestEdgeCases` (class)
- L228 `test_empty_file_list(self)` (method)
- L241 `test_file_disappears_between_list_and_upload(self, tmp_path)` (method) — File listed by get_files but deleted before _file_mtime_key reads it.
- L260 `TestBulkUpload` (class) — Tests for the optional bulk_upload_fn callback.
- L263 `test_bulk_upload_used_when_provided(self, tmp_files)` (method) — When bulk_upload_fn is set, it's called instead of per-file upload_fn.
- L281 `test_fallback_to_upload_fn_when_no_bulk(self, tmp_files)` (method) — Without bulk_upload_fn, per-file upload_fn is used (backwards compat).
- L294 `test_bulk_upload_rollback_on_failure(self, tmp_files)` (method) — Bulk upload failure rolls back synced state so next sync retries.
