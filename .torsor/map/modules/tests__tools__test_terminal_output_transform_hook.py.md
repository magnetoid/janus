---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_terminal_output_transform_hook.py

Symbols in `tests/tools/test_terminal_output_transform_hook.py`.

- L13 `_make_env_config(tmp_path, **overrides)` (function)
- L29 `_run_terminal(monkeypatch, tmp_path, *, output, returncode=0, invoke_hook=_UNSET, approval=None, command='echo hello')` (function)
- L61 `test_terminal_output_unchanged_when_transform_hook_not_registered(monkeypatch, tmp_path)` (function)
- L69 `test_terminal_output_unchanged_for_none_hook_result(monkeypatch, tmp_path)` (function)
- L80 `test_terminal_output_ignores_invalid_hook_results(monkeypatch, tmp_path)` (function)
- L91 `test_terminal_output_uses_first_valid_string_from_hooks(monkeypatch, tmp_path)` (function)
- L102 `test_terminal_output_transform_still_truncates_long_replacement(monkeypatch, tmp_path)` (function)
- L117 `test_terminal_output_transform_still_runs_strip_and_redact(monkeypatch, tmp_path)` (function)
- L136 `test_terminal_output_transform_hook_exception_falls_back(monkeypatch, tmp_path)` (function)
- L152 `test_terminal_output_transform_does_not_change_approval_or_exit_code_meaning(monkeypatch, tmp_path)` (function)
- L175 `test_terminal_output_transform_integration_with_real_plugin(monkeypatch, tmp_path)` (function)
