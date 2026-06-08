---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_subagent_stop_hook.py

Symbols in `tests/agent/test_subagent_stop_hook.py`.

- L22 `_make_parent(depth: int=0, session_id: str='parent-1')` (function)
- L47 `_fresh_plugin_manager()` (function) — Each test gets a fresh PluginManager so hook callbacks don't
- L57 `_stub_child_builder(monkeypatch)` (function) — Replace _build_child_agent with a MagicMock factory so delegate_task
- L72 `_register_capturing_hook()` (function)
- L87 `TestSingleTask` (class)
- L88 `test_fires_once(self)` (method)
- L109 `test_fires_on_parent_thread(self)` (method)
- L123 `test_payload_includes_parent_session_id(self)` (method)
- L143 `TestBatchMode` (class)
- L144 `test_fires_per_child(self)` (method)
- L170 `test_all_fires_on_parent_thread(self)` (method)
- L195 `TestPayloadShape` (class)
- L196 `test_role_absent_becomes_none(self)` (method)
- L209 `test_result_does_not_leak_child_role_field(self)` (method) — The internal _child_role key must be stripped before the
