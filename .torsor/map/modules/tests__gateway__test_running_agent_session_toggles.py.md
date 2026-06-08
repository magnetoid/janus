---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_running_agent_session_toggles.py

Symbols in `tests/gateway/test_running_agent_session_toggles.py`.

- L33 `_make_source()` (function)
- L43 `_make_event(text: str)` (function)
- L47 `_make_runner()` (function) — Minimal GatewayRunner with an active running agent for this session.
- L113 `test_yolo_dispatches_mid_run(monkeypatch)` (function) — /yolo mid-run must dispatch to its handler, not hit the catch-all.
- L126 `test_verbose_dispatches_mid_run(monkeypatch)` (function) — /verbose mid-run must dispatch to its handler, not hit the catch-all.
- L139 `test_fast_rejected_mid_run()` (function) — /fast mid-run must hit the busy catch-all — config-only, next message.
- L155 `test_reasoning_rejected_mid_run()` (function) — /reasoning mid-run must hit the busy catch-all — config-only, next message.
- L171 `test_btw_dispatches_mid_run()` (function) — /btw mid-run must dispatch to /background's handler, not hit the catch-all.
