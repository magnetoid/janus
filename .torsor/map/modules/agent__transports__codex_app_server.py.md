---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/transports/codex_app_server.py

Symbols in `agent/transports/codex_app_server.py`.

- L34 `CodexAppServerError` (class) — Raised on JSON-RPC errors from the app-server.
- L41 `__str__(self)` (method)
- L46 `_Pending` (class)
- L52 `CodexAppServerClient` (class) — Minimal JSON-RPC 2.0 client for `codex app-server` over stdio.
- L69 `__init__(self, codex_bin: str='codex', codex_home: Optional[str]=None, extra_args: Optional[list[str]]=None, env: Optional[dict[str, str]]=None)` (method)
- L142 `initialize(self, client_name: str='hermes', client_title: str='Hermes Agent', client_version: str='0.1', capabilities: Optional[dict]=None, timeout: float=10.0)` (method) — Send `initialize` + `initialized` handshake. Returns the server's
- L167 `close(self, timeout: float=3.0)` (method) — Close stdin and wait for the subprocess to exit, escalating to kill.
- L187 `__enter__(self)` (method)
- L190 `__exit__(self, *exc: Any)` (method)
- L195 `request(self, method: str, params: Optional[dict]=None, timeout: float=30.0)` (method) — Send a JSON-RPC request and block on the response. Returns `result`,
- L225 `notify(self, method: str, params: Optional[dict]=None)` (method) — Send a JSON-RPC notification (no id, no response expected).
- L229 `respond(self, request_id: Any, result: dict)` (method) — Reply to a server-initiated request (e.g. approval prompts).
- L233 `respond_error(self, request_id: Any, code: int, message: str, data: Optional[Any]=None)` (method) — Reply to a server-initiated request with an error.
- L242 `take_notification(self, timeout: float=0.0)` (method) — Pop the next streaming notification, or return None on timeout.
- L254 `take_server_request(self, timeout: float=0.0)` (method) — Pop the next server-initiated request (e.g. exec/applyPatch approval).
- L265 `stderr_tail(self, n: int=20)` (method) — Return last n lines of codex's stderr (for error reports).
- L270 `is_alive(self)` (method)
- L275 `_take_id(self)` (method)
- L283 `_send(self, obj: dict)` (method)
- L296 `_read_stdout(self)` (method)
- L321 `_dispatch(self, msg: dict)` (method)
- L340 `_read_stderr(self)` (method)
- L358 `parse_codex_version(output: str)` (function) — Parse `codex --version` output. Returns (major, minor, patch) or None.
- L369 `check_codex_binary(codex_bin: str='codex', min_version: tuple[int, int, int]=MIN_CODEX_VERSION)` (function) — Verify codex CLI is installed and meets minimum version.
