---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_loop_exception_handler.py

Symbols in `tests/gateway/test_loop_exception_handler.py`.

- L31 `TimedOut` (class) — Stand-in for ``telegram.error.TimedOut``.
- L35 `NetworkError` (class) — Stand-in for ``telegram.error.NetworkError``.
- L39 `ConnectError` (class) — Stand-in for ``httpx.ConnectError``.
- L43 `ReadTimeout` (class) — Stand-in for ``httpx.ReadTimeout``.
- L47 `PoolTimeout` (class) — Stand-in for ``httpx.PoolTimeout``.
- L51 `ClientConnectorError` (class) — Stand-in for ``aiohttp.ClientConnectorError``.
- L55 `SomeUnrelatedBug` (class) — A non-transient error that should NOT be swallowed.
- L75 `test_transient_classifier_matches_known_network_errors(exc_cls)` (function) — Every well-known transient network exception class is classified.
- L80 `test_transient_classifier_rejects_unrelated_errors()` (function) — Real bugs (ValueError, KeyError, custom app errors) are NOT swallowed.
- L86 `test_transient_classifier_unwraps_cause_chain()` (function) — A NetworkError wrapping a ConnectError is still classified.
- L94 `test_transient_classifier_unwraps_context_chain()` (function) — Implicit ``__context__`` wrapping is also unwrapped.
- L108 `test_transient_classifier_does_not_infinite_loop_on_cyclic_cause()` (function) — A pathological self-referential cause chain terminates.
- L121 `test_handler_swallows_transient_error_and_logs_warning(caplog)` (function) — Transient errors are logged at WARNING but not re-raised.
- L139 `test_handler_delegates_unknown_errors_to_default(monkeypatch)` (function) — A non-transient error is forwarded to ``loop.default_exception_handler``.
- L160 `test_handler_tolerates_missing_exception_key(monkeypatch)` (function) — Contexts without an ``exception`` key fall through to the default handler.
- L180 `test_unhandled_transient_error_in_task_does_not_propagate_to_loop()` (function) — Smoke test the wiring as a loop would actually use it.
