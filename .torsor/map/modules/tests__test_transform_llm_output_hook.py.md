---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_transform_llm_output_hook.py

Symbols in `tests/test_transform_llm_output_hook.py`.

- L26 `_make_enabled_plugin(hermes_home: Path, name: str, register_body: str)` (function) — Create a plugin under <hermes_home>/plugins/<name> and opt it in.
- L47 `test_transform_llm_output_in_valid_hooks()` (function)
- L51 `test_hook_receives_expected_kwargs(tmp_path, monkeypatch)` (function) — Hook callback should see response_text + session_id + model + platform.
- L78 `test_first_non_empty_string_wins_semantics()` (function) — Simulate the run_agent.py loop: first non-empty string replaces text.
- L93 `test_empty_string_return_leaves_response_unchanged()` (function) — Empty string must not replace the response (pass-through signal).
- L106 `test_hook_exception_does_not_replace_response(tmp_path, monkeypatch)` (function) — A plugin raising an exception must not break hook dispatch.
- L146 `test_no_plugins_returns_empty_results(tmp_path, monkeypatch)` (function) — With no plugins loaded, invoke_hook returns [] and the response is unchanged.
