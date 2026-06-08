---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/lsp/test_lifecycle.py

Symbols in `tests/agent/lsp/test_lifecycle.py`.

- L18 `_reset_singleton()` (function) — Force a clean module state before each test.
- L32 `test_get_service_registers_atexit_handler_once(monkeypatch)` (function) — First call to ``get_service`` must register an atexit handler;
- L62 `test_atexit_shutdown_calls_shutdown_service(monkeypatch)` (function) — The atexit-registered wrapper invokes ``shutdown_service`` and
- L74 `test_atexit_shutdown_swallows_exceptions(monkeypatch)` (function)
- L83 `test_shutdown_service_idempotent(monkeypatch)` (function) — Calling shutdown twice must be safe — first call cleans up,
- L101 `test_shutdown_service_no_op_when_never_started()` (function) — Calling shutdown without ever creating the service is safe.
- L106 `test_shutdown_service_swallows_exception(monkeypatch)` (function) — An exception during ``svc.shutdown()`` must not propagate —
- L121 `test_get_service_returns_none_for_inactive_service(monkeypatch)` (function) — A service whose ``is_active()`` returns False is treated as
- L137 `test_get_service_returns_none_when_create_fails(monkeypatch)` (function) — Service factory returning ``None`` (no config, etc.) propagates.
