---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/lsp/client.py

Symbols in `agent/lsp/client.py`.

- L81 `file_uri(path: str)` (function) — Return ``file://`` URI for an absolute filesystem path.
- L97 `uri_to_path(uri: str)` (function) — Inverse of :func:`file_uri`.
- L107 `_end_position(text: str)` (function) — Return the LSP Position at the end of ``text``.
- L127 `LSPClient` (class) — Async LSP client tied to one server process and one workspace root.
- L144 `__init__(self, *, server_id: str, workspace_root: str, command: List[str], env: Optional[Dict[str, str]]=None, cwd: Optional[str]=None, initialization_options: Optional[Dict[str, Any]]=None, seed_diagnostics_on_first_push: bool=False)` (method)
- L222 `is_running(self)` (method)
- L226 `state(self)` (method)
- L229 `start(self)` (method) — Spawn the server and complete the initialize handshake.
- L249 `_win_wrap_cmd(cmd: List[str])` (method) — On Windows, wrap .cmd/.bat shims so CreateProcess can run them.
- L256 `_spawn(self)` (method)
- L286 `_drain_stderr(self)` (method)
- L300 `_reader_loop(self)` (method)
- L329 `_initialize(self)` (method)
- L393 `_extract_sync_kind(capabilities: dict)` (method)
- L403 `shutdown(self)` (method) — Best-effort graceful shutdown.
- L426 `_cleanup_process(self)` (method)
- L461 `_send_request(self, method: str, params: Any)` (method)
- L480 `_send_request_with_retry(self, method: str, params: Any, *, timeout: float)` (method) — Send a request, retrying on ``ContentModified`` (-32801).
- L496 `_send_notification(self, method: str, params: Any)` (method)
- L505 `_send_response(self, req_id: Any, result: Any)` (method)
- L514 `_send_error_response(self, req_id: Any, code: int, message: str)` (method)
- L523 `_dispatch_response(self, req_id: int, msg: dict)` (method)
- L539 `_dispatch_request(self, req_id: Any, msg: dict)` (method)
- L554 `_dispatch_notification(self, method: str, msg: dict)` (method)
- L567 `_handle_work_done_create(self, params: Any)` (method)
- L571 `_handle_workspace_configuration(self, params: Any)` (method)
- L596 `_handle_register_capability(self, params: Any)` (method)
- L609 `_handle_unregister_capability(self, params: Any)` (method)
- L620 `_handle_workspace_folders(self, params: Any)` (method)
- L623 `_handle_diagnostic_refresh(self, params: Any)` (method)
- L631 `_handle_publish_diagnostics(self, params: Any)` (method)
- L673 `open_file(self, path: str, *, language_id: str='plaintext')` (method) — Send didOpen (first time) or didChange (subsequent) for ``path``.
- L747 `save_file(self, path: str)` (method) — Send didSave for ``path``.  Some linters re-scan only on save.
- L761 `_pull_document_diagnostics(self, path: str)` (method) — Send ``textDocument/diagnostic`` for one file.
- L793 `wait_for_diagnostics(self, path: str, version: int, *, mode: str='document')` (method) — Wait for the server to publish diagnostics for ``path`` at ``version``.
- L846 `_wait_for_fresh_push(self, path: str, version: int, timeout: float)` (method) — Wait until a publishDiagnostics arrives for ``path`` at ``version``+.
- L883 `diagnostics_for(self, path: str)` (method) — Return current merged + deduped diagnostics for one file.
- L896 `_dedupe(*lists: List[Dict[str, Any]])` (function)
- L911 `_diagnostic_key(d: Dict[str, Any])` (function) — Content-equality key for a diagnostic.
