---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_browser_supervisor_healthcheck.py

Symbols in `tests/tools/test_browser_supervisor_healthcheck.py`.

- L18 `_FakeLoop` (class)
- L19 `__init__(self, running: bool)` (method)
- L22 `is_running(self)` (method)
- L26 `_make_fake_supervisor(cdp_url: str, *, thread_alive: bool, loop_running: bool)` (function) — Build a minimal stand-in for a CDPSupervisor entry in the registry.
- L57 `isolated_registry()` (function) — A fresh registry instance, independent of the global SUPERVISOR_REGISTRY.
- L63 `stub_cdp_supervisor(monkeypatch)` (function) — Replace CDPSupervisor in the module so recreate paths don't touch Chrome.
- L105 `test_cache_hit_returns_same_instance_when_healthy(isolated_registry, stub_cdp_supervisor)` (function) — Sanity: healthy cached supervisor is returned without recreate.
- L117 `test_dead_thread_triggers_recreate(isolated_registry, stub_cdp_supervisor)` (function) — Cached supervisor with a non-live thread must not be reused.
- L133 `test_stopped_loop_triggers_recreate(isolated_registry, stub_cdp_supervisor)` (function) — Cached supervisor whose event loop is no longer running is recreated.
- L151 `test_missing_thread_and_loop_attrs_trigger_recreate(isolated_registry, stub_cdp_supervisor)` (function) — Defensive: None _thread or None _loop counts as unhealthy.
