---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_managed_modal_environment.py

Symbols in `tests/tools/test_managed_modal_environment.py`.

- L14 `_load_tool_module(module_name: str, filename: str)` (function)
- L23 `_reset_modules(prefixes: tuple[str, ...])` (function)
- L30 `_restore_tool_and_agent_modules()` (function) — Save and restore sys.modules entries so fakes don't leak to other tests.
- L47 `_install_fake_tools_package(*, credential_mounts=None)` (function)
- L97 `_FakeResponse` (class)
- L98 `__init__(self, status_code: int, payload=None, text: str='')` (method)
- L103 `json(self)` (method)
- L109 `test_managed_modal_execute_polls_until_completed(monkeypatch)` (function)
- L148 `test_managed_modal_create_sends_a_stable_idempotency_key(monkeypatch)` (function)
- L172 `test_managed_modal_execute_cancels_on_interrupt(monkeypatch)` (function)
- L214 `test_managed_modal_execute_returns_descriptive_error_on_missing_exec(monkeypatch)` (function)
- L241 `test_managed_modal_create_and_cleanup_preserve_gateway_persistence_fields(monkeypatch)` (function)
- L279 `test_managed_modal_rejects_host_credential_passthrough()` (function)
- L292 `test_managed_modal_execute_times_out_and_cancels(monkeypatch)` (function)
