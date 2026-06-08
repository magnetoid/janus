---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cron/test_cron_context_from.py

Symbols in `tests/cron/test_cron_context_from.py`.

- L13 `cron_env(tmp_path, monkeypatch)` (function) — Isolated cron environment with temp HERMES_HOME.
- L30 `TestJobContextFromField` (class) — Test that context_from is stored and retrieved correctly.
- L33 `test_create_job_with_context_from_string(self, cron_env)` (method)
- L47 `test_create_job_with_context_from_list(self, cron_env)` (method)
- L60 `test_create_job_without_context_from(self, cron_env)` (method)
- L66 `test_context_from_empty_string_normalized_to_none(self, cron_env)` (method)
- L72 `test_context_from_empty_list_normalized_to_none(self, cron_env)` (method)
- L79 `TestBuildJobPromptContextFrom` (class) — Test that _build_job_prompt() injects context from referenced jobs.
- L82 `test_injects_latest_output(self, cron_env)` (method)
- L105 `test_uses_most_recent_output(self, cron_env)` (method)
- L127 `test_graceful_when_no_output_yet(self, cron_env)` (method)
- L143 `test_injects_multiple_context_jobs(self, cron_env)` (method)
- L164 `test_context_injected_before_prompt(self, cron_env)` (method) — Context should appear before the job's own prompt.
- L184 `test_output_truncated_at_8k_chars(self, cron_env)` (method) — Output longer than 8000 chars should be truncated.
- L202 `test_graceful_when_file_deleted_between_listing_and_reading(self, cron_env)` (method) — Job should not crash if output file is deleted mid-read.
- L230 `test_graceful_when_permission_error(self, cron_env)` (method) — Job should not crash if output directory is not readable.
- L258 `test_invalid_job_id_skipped(self, cron_env)` (method) — context_from with path traversal job_id should be skipped.
- L271 `test_invalid_job_id_log_includes_job_origin(self, cron_env, caplog)` (method) — Invalid stored context_from refs log job/source provenance.
- L302 `TestUpdateContextFrom` (class) — Verify the cronjob tool's `update` action wires context_from through.
- L309 `test_update_adds_context_from_to_existing_job(self, cron_env)` (method)
- L328 `test_update_changes_context_from_reference(self, cron_env)` (method)
- L348 `test_update_clears_context_from_with_empty_list(self, cron_env)` (method)
- L367 `test_update_clears_context_from_with_empty_string(self, cron_env)` (method)
- L385 `test_update_rejects_unknown_job_reference(self, cron_env)` (method)
- L400 `test_update_preserves_context_from_when_not_passed(self, cron_env)` (method) — Updating other fields must not clobber context_from.
