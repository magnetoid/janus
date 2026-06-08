---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/environments/managed_modal.py

Symbols in `tools/environments/managed_modal.py`.

- L23 `_request_timeout_env(name: str, default: float)` (function)
- L32 `_ManagedModalExecHandle` (class)
- L36 `ManagedModalEnvironment` (class) — Gateway-owned Modal sandbox with Hermes-compatible execute/cleanup.
- L46 `__init__(self, image: str, cwd: str='/root', timeout: int=60, modal_sandbox_kwargs: Optional[Dict[str, Any]]=None, persistent_filesystem: bool=True, task_id: str='default')` (method)
- L72 `_start_modal_exec(self, prepared: PreparedModalExec)` (method)
- L121 `_poll_modal_exec(self, handle: _ManagedModalExecHandle)` (method)
- L148 `_cancel_modal_exec(self, handle: _ManagedModalExecHandle)` (method)
- L151 `_timeout_result_for_modal(self, timeout: int)` (method)
- L154 `cleanup(self)` (method)
- L172 `_create_sandbox(self)` (method)
- L214 `_guard_unsupported_credential_passthrough(self)` (method) — Managed Modal does not sync or mount host credential files.
- L229 `_request(self, method: str, path: str, *, json: Dict[str, Any] | None=None, timeout: int=30, extra_headers: Dict[str, str] | None=None)` (method)
- L248 `_cancel_exec(self, exec_id: str)` (method)
- L259 `_coerce_number(value: Any, default: float)` (method)
- L268 `_format_error(prefix: str, response: requests.Response)` (method)
