---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_kanban_notifier_watcher_dispatch_gate.py

Symbols in `tests/gateway/test_kanban_notifier_watcher_dispatch_gate.py`.

- L15 `_make_runner(with_adapter=False)` (function)
- L23 `_fake_config(dispatch_in_gateway)` (function)
- L27 `test_notifier_watcher_skips_when_dispatch_disabled()` (function) — dispatch_in_gateway=false returns before opening any board DB.
- L36 `test_notifier_watcher_env_override_disables(monkeypatch)` (function) — HERMES_KANBAN_DISPATCH_IN_GATEWAY=false skips config load entirely.
- L47 `test_notifier_watcher_runs_when_dispatch_enabled()` (function) — dispatch_in_gateway=true proceeds past the gate to the board fan-out.
