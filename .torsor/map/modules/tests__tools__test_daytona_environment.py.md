---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_daytona_environment.py

Symbols in `tests/tools/test_daytona_environment.py`.

- L14 `_make_exec_response(result='', exit_code=0)` (function)
- L18 `_make_sandbox(sandbox_id='sb-123', state='started')` (function)
- L26 `_patch_daytona_imports(monkeypatch)` (function) — Patch the daytona SDK so DaytonaEnvironment can be imported without it.
- L54 `daytona_sdk(monkeypatch)` (function) — Provide a mock daytona SDK module and return it for assertions.
- L60 `make_env(daytona_sdk, monkeypatch)` (function) — Factory that creates a DaytonaEnvironment with a mocked SDK.
- L116 `TestCwdResolution` (class)
- L117 `test_default_cwd_resolves_home(self, make_env)` (method)
- L121 `test_tilde_cwd_resolves_home(self, make_env)` (method)
- L125 `test_explicit_cwd_not_overridden(self, make_env)` (method)
- L129 `test_home_detection_failure_keeps_default_cwd(self, make_env)` (method)
- L135 `test_empty_home_keeps_default_cwd(self, make_env)` (method)
- L144 `TestPersistence` (class)
- L145 `test_persistent_resumes_via_get(self, make_env)` (method)
- L154 `test_persistent_resumes_legacy_via_list(self, make_env, daytona_sdk)` (method)
- L168 `test_persistent_creates_new_when_none_found(self, make_env, daytona_sdk)` (method)
- L181 `test_non_persistent_skips_lookup(self, make_env)` (method)
- L192 `TestCleanup` (class)
- L193 `test_persistent_cleanup_stops_sandbox(self, make_env)` (method)
- L199 `test_non_persistent_cleanup_deletes_sandbox(self, make_env)` (method)
- L205 `test_cleanup_idempotent(self, make_env)` (method)
- L210 `test_cleanup_swallows_errors(self, make_env)` (method)
- L221 `TestExecute` (class)
- L222 `test_basic_command(self, make_env)` (method)
- L237 `test_sdk_timeout_passed_to_exec(self, make_env)` (method) — SDK native timeout is passed to sandbox.process.exec().
- L256 `test_timeout_returns_exit_code_124(self, make_env)` (method) — SDK-level timeout surfaces as exit code 124 via _wait_for_process.
- L270 `test_nonzero_exit_code(self, make_env)` (method)
- L283 `test_stdin_data_wraps_heredoc(self, make_env)` (method)
- L303 `test_daytona_error_triggers_retry(self, make_env, daytona_sdk)` (method)
- L324 `TestResourceConversion` (class)
- L325 `_get_resources_kwargs(self, daytona_sdk)` (method)
- L328 `test_memory_converted_to_gib(self, make_env, daytona_sdk)` (method)
- L332 `test_disk_converted_to_gib(self, make_env, daytona_sdk)` (method)
- L336 `test_small_values_clamped_to_1(self, make_env, daytona_sdk)` (method)
- L347 `TestInterrupt` (class)
- L348 `test_interrupt_stops_sandbox_and_returns_130(self, make_env, monkeypatch)` (method)
- L383 `TestRetryExhausted` (class)
- L384 `test_both_attempts_fail(self, make_env, daytona_sdk)` (method) — DaytonaError surfaces directly as rc=1 (retry logic was removed).
- L404 `TestEnsureSandboxReady` (class)
- L405 `test_restarts_stopped_sandbox(self, make_env)` (method)
- L411 `test_no_restart_when_running(self, make_env)` (method)
