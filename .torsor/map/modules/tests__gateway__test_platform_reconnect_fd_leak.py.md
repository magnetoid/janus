---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_platform_reconnect_fd_leak.py

Symbols in `tests/gateway/test_platform_reconnect_fd_leak.py`.

- L36 `_make_runner()` (function) — Create a minimal GatewayRunner via object.__new__ to skip __init__.
- L56 `_run_watcher_one_iteration(runner: GatewayRunner)` (function) — Drive ``_platform_reconnect_watcher`` for exactly one retry pass.
- L81 `_CountingAdapter` (class) — Adapter that records every disconnect() call for fd-leak assertions.
- L92 `__init__(self, *, succeed: bool=False, fatal_error: str | None=None, fatal_retryable: bool=True, raise_during_connect: bool=False)` (method)
- L106 `connect(self)` (method)
- L116 `disconnect(self)` (method)
- L120 `send(self, chat_id, content, reply_to=None, metadata=None)` (method)
- L123 `send_typing(self, chat_id, metadata=None)` (method)
- L126 `get_chat_info(self, chat_id)` (method)
- L130 `_seed_runner_with_one_failure(runner: GatewayRunner)` (function) — Queue a single platform for the reconnect watcher to pick up.
- L139 `TestReconnectFDLeakRegression` (class) — All three reconnect failure paths must dispose the unowned adapter.
- L149 `test_nonretryable_failure_disposes_unowned_adapter(self)` (method) — A fatal error (bad auth, etc.) must call disconnect() exactly once.
- L187 `test_retryable_failure_disposes_unowned_adapter(self)` (method) — A retryable failure (network blip) must also call disconnect().
- L213 `test_exception_during_connect_disposes_unowned_adapter(self)` (method) — An exception escaping connect() (aiohttp start crash, etc.) disposes.
- L235 `test_dispose_helper_handles_none(self)` (method) — ``_dispose_unused_adapter(None)`` is a no-op (defensive).
- L240 `test_dispose_helper_swallows_disconnect_exception(self)` (method) — A disconnect() that itself raises must not abort the watcher loop.
- L278 `TestAPIServerDisconnectClosesResponseStore` (class) — The platform-level fix: ``APIServerAdapter.disconnect()`` must close its ResponseStore.
- L288 `_build_adapter_with_store(self, store: ResponseStore)` (method) — Build an APIServerAdapter with the required internal state.
- L304 `test_disconnect_closes_response_store(self, tmp_path)` (method) — Closing the adapter's ResponseStore releases its SQLite connection.
- L331 `test_disconnect_swallows_response_store_close_exception(self, tmp_path)` (method) — A misbehaving ResponseStore.close() must not abort adapter shutdown.
