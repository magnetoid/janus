---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/lsp/manager.py

Symbols in `agent/lsp/manager.py`.

- L64 `_BackgroundLoop` (class) — A daemon thread that owns one asyncio event loop.
- L71 `__init__(self)` (method)
- L76 `start(self)` (method)
- L87 `_run_forever(self)` (method)
- L100 `run(self, coro, *, timeout: Optional[float]=None)` (method) — Submit a coroutine to the loop and block until done.
- L119 `stop(self)` (method)
- L133 `LSPService` (class) — The process-wide LSP service.
- L146 `__init__(self, *, enabled: bool, wait_mode: str, wait_timeout: float, install_strategy: str, binary_overrides: Optional[Dict[str, List[str]]]=None, env_overrides: Optional[Dict[str, Dict[str, str]]]=None, init_overrides: Optional[Dict[str, Dict[str, Any]]]=None, disabled_servers: Optional[List[str]]=None, idle_timeout: float=DEFAULT_IDLE_TIMEOUT)` (method)
- L187 `create_from_config(cls)` (method) — Build a service from ``hermes_cli.config`` settings.
- L244 `is_active(self)` (method) — Return True iff this service should be consulted at all.
- L248 `enabled_for(self, file_path: str)` (method) — Return True iff LSP should run for this specific file.
- L281 `snapshot_baseline(self, file_path: str)` (method) — Snapshot current diagnostics for ``file_path`` as the delta baseline.
- L302 `get_diagnostics_sync(self, file_path: str, *, delta: bool=True, timeout: Optional[float]=None, line_shift: Optional[Callable[[int], Optional[int]]]=None)` (method) — Synchronously open ``file_path`` in the right server, wait for
- L386 `_mark_broken_for_file(self, file_path: str, exc: BaseException)` (method) — Mark the (server_id, workspace_root) pair as broken so subsequent
- L434 `shutdown(self)` (method) — Tear down all clients and stop the background loop.
- L449 `_snapshot_async(self, file_path: str)` (method)
- L462 `_open_and_wait_async(self, file_path: str)` (method)
- L476 `_current_diags_async(self, file_path: str)` (method)
- L487 `_get_or_spawn(self, file_path: str)` (method)
- L569 `_shutdown_async(self)` (method)
- L584 `get_status(self)` (method) — Return a snapshot of the service for the CLI status command.
- L608 `_diag_key(d: Dict[str, Any])` (function) — Content equality key used for cross-edit delta filtering.
