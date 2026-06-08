---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cron/test_cron_script.py

Symbols in `tests/cron/test_cron_script.py`.

- L23 `cron_env(tmp_path, monkeypatch)` (function) — Isolated cron environment with temp HERMES_HOME.
- L42 `TestJobScriptField` (class) — Test that the script field is stored and retrieved correctly.
- L45 `test_create_job_with_script(self, cron_env)` (method)
- L58 `test_create_job_without_script(self, cron_env)` (method)
- L64 `test_create_job_empty_script_normalized_to_none(self, cron_env)` (method)
- L70 `test_update_job_add_script(self, cron_env)` (method)
- L79 `test_update_job_clear_script(self, cron_env)` (method)
- L89 `TestRunJobScript` (class) — Test the _run_job_script() function.
- L92 `test_successful_script(self, cron_env)` (method)
- L102 `test_script_relative_path(self, cron_env)` (method)
- L112 `test_script_not_found(self, cron_env)` (method)
- L119 `test_script_nonzero_exit(self, cron_env)` (method)
- L135 `test_script_empty_output(self, cron_env)` (method)
- L145 `test_script_timeout(self, cron_env, monkeypatch)` (method)
- L159 `test_script_json_output(self, cron_env)` (method) — Scripts can output structured JSON for the LLM to parse.
- L176 `TestBuildJobPromptWithScript` (class) — Test that script output is injected into the prompt.
- L179 `test_script_output_injected(self, cron_env)` (method)
- L194 `test_script_error_injected(self, cron_env)` (method)
- L206 `test_no_script_unchanged(self, cron_env)` (method)
- L216 `TestCronjobToolScript` (class) — Test the cronjob tool's script parameter.
- L219 `test_create_with_script(self, cron_env, monkeypatch)` (method)
- L232 `test_update_script(self, cron_env, monkeypatch)` (method)
- L251 `test_clear_script(self, cron_env, monkeypatch)` (method)
- L271 `test_list_shows_script(self, cron_env, monkeypatch)` (method)
- L288 `TestScriptPathContainment` (class) — Regression tests for path containment bypass in _run_job_script().
- L296 `test_absolute_path_outside_scripts_dir_blocked(self, cron_env)` (method) — Absolute paths outside ~/.hermes/scripts/ must be rejected.
- L308 `test_absolute_path_tmp_blocked(self, cron_env)` (method) — Absolute paths to /tmp must be rejected.
- L316 `test_tilde_path_blocked(self, cron_env)` (method) — ~ prefixed paths must be rejected (expanduser bypasses check).
- L324 `test_tilde_traversal_blocked(self, cron_env)` (method) — ~/../../../tmp/evil.py must be rejected.
- L332 `test_relative_traversal_still_blocked(self, cron_env)` (method) — ../../etc/passwd style traversal must still be blocked.
- L340 `test_relative_path_inside_scripts_dir_allowed(self, cron_env)` (method) — Relative paths within the scripts dir should still work.
- L351 `test_subdirectory_inside_scripts_dir_allowed(self, cron_env)` (method) — Relative paths to subdirectories within scripts/ should work.
- L364 `test_absolute_path_inside_scripts_dir_allowed(self, cron_env)` (method) — Absolute paths that resolve WITHIN scripts/ should work.
- L379 `test_symlink_escape_blocked(self, cron_env, tmp_path)` (method) — Symlinks pointing outside scripts/ must be rejected.
- L396 `TestCronjobToolScriptValidation` (class) — Test API-boundary validation of cron script paths in cronjob_tools.
- L399 `test_create_with_absolute_script_rejected(self, cron_env, monkeypatch)` (method)
- L412 `test_create_with_tilde_script_rejected(self, cron_env, monkeypatch)` (method)
- L425 `test_create_with_traversal_script_rejected(self, cron_env, monkeypatch)` (method)
- L438 `test_create_with_relative_script_allowed(self, cron_env, monkeypatch)` (method)
- L451 `test_update_with_absolute_script_rejected(self, cron_env, monkeypatch)` (method)
- L470 `test_update_clear_script_allowed(self, cron_env, monkeypatch)` (method) — Clearing a script (empty string) should always be permitted.
- L491 `test_windows_absolute_path_rejected(self, cron_env, monkeypatch)` (method)
- L504 `TestRunJobEnvVarCleanup` (class) — Test that run_job() env vars are cleaned up even on early failure.
- L507 `test_env_vars_cleaned_on_early_error(self, cron_env, monkeypatch)` (method) — Origin env vars must be cleaned up even if run_job fails early.
