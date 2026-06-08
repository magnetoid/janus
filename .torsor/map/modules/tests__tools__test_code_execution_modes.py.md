---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_code_execution_modes.py

Symbols in `tests/tools/test_code_execution_modes.py`.

- L28 `_force_local_terminal(monkeypatch)` (function) — Mirror test_code_execution.py — guarantee local backend under xdist.
- L47 `_mock_mode(mode)` (function) — Context manager that pins code_execution.mode to the given value.
- L54 `_mock_handle_function_call(function_name, function_args, task_id=None, user_task=None)` (function) — Minimal mock dispatcher reused across tests.
- L67 `TestGetExecutionMode` (class) — _get_execution_mode reads config.yaml only (no env var surface).
- L70 `test_default_is_project(self)` (method)
- L73 `test_config_project(self)` (method)
- L78 `test_config_strict(self)` (method)
- L83 `test_config_case_insensitive(self)` (method)
- L88 `test_config_strips_whitespace(self)` (method)
- L93 `test_empty_config_falls_back_to_default(self)` (method)
- L97 `test_bogus_config_falls_back_to_default(self)` (method)
- L102 `test_none_config_falls_back_to_default(self)` (method)
- L108 `test_execution_modes_tuple(self)` (method) — Canonical set of modes — tests + config layer rely on this shape.
- L117 `TestResolveChildPython` (class) — _resolve_child_python — picks the right interpreter per mode.
- L120 `test_strict_always_sys_executable(self)` (method) — Strict mode never leaves sys.executable, even if venv is set.
- L125 `test_project_with_no_venv_falls_back(self)` (method) — Project mode without VIRTUAL_ENV or CONDA_PREFIX → sys.executable.
- L132 `test_project_with_virtualenv_picks_venv_python(self)` (method) — Project mode + VIRTUAL_ENV pointing at a real venv → that python.
- L152 `test_project_with_broken_venv_falls_back(self)` (method) — VIRTUAL_ENV set but bin/python missing → sys.executable.
- L161 `test_project_prefers_virtualenv_over_conda(self)` (method) — If both VIRTUAL_ENV and CONDA_PREFIX are set, VIRTUAL_ENV wins.
- L184 `test_is_usable_python_rejects_nonexistent(self)` (method)
- L188 `test_is_usable_python_accepts_real_python(self)` (method)
- L197 `TestResolveChildCwd` (class)
- L199 `test_strict_uses_staging_dir(self)` (method)
- L202 `test_project_without_terminal_cwd_uses_getcwd(self)` (method)
- L207 `test_project_uses_terminal_cwd_when_set(self)` (method)
- L213 `test_project_bogus_terminal_cwd_falls_back_to_getcwd(self)` (method)
- L217 `test_project_expands_tilde(self)` (method)
- L228 `TestModeAwareSchema` (class)
- L230 `test_strict_description_mentions_temp_dir(self)` (method)
- L234 `test_project_description_mentions_session_and_venv(self)` (method)
- L239 `test_neither_description_uses_sandbox_language(self)` (method) — REGRESSION GUARD for commit 39b83f34.
- L252 `test_descriptions_are_similar_length(self)` (method) — Both modes should have roughly the same-size description.
- L258 `test_default_mode_reads_config(self)` (method) — build_execute_code_schema() with mode=None reads config.yaml.
- L281 `TestExecuteCodeModeIntegration` (class) — End-to-end: verify the subprocess actually runs where we expect.
- L284 `_run(self, code, mode, enabled_tools=None, extra_env=None)` (method)
- L297 `test_strict_mode_runs_in_tmpdir(self)` (method) — Strict mode: script's os.getcwd() is the staging tmpdir.
- L303 `test_project_mode_runs_in_session_cwd(self)` (method) — Project mode: script's os.getcwd() is the session's working dir.
- L319 `test_project_mode_interpreter_is_venv_python(self)` (method) — Project mode: sys.executable inside the child is the venv's python
- L337 `test_project_mode_can_still_import_hermes_tools(self)` (method) — Regression: hermes_tools still importable from non-tmpdir CWD.
- L354 `test_strict_mode_can_still_import_hermes_tools(self)` (method) — Regression: strict mode's tmpdir CWD still works for imports.
- L383 `TestSecurityInvariantsAcrossModes` (class)
- L385 `_run(self, code, mode)` (method)
- L396 `test_api_keys_scrubbed_in_strict_mode(self)` (method)
- L413 `test_api_keys_scrubbed_in_project_mode(self)` (method) — CRITICAL: the project-mode default does NOT leak user credentials.
- L433 `test_secret_substrings_scrubbed_in_project_mode(self)` (method) — SECRET/PASSWORD/CREDENTIAL/PASSWD/AUTH filters still apply.
- L455 `test_tool_whitelist_enforced_in_strict_mode(self)` (method) — A script cannot RPC-call tools outside SANDBOX_ALLOWED_TOOLS.
- L469 `test_tool_whitelist_enforced_in_project_mode(self)` (method) — CRITICAL: project mode does NOT widen the tool whitelist.
