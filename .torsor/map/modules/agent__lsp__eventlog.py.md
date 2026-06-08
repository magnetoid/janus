---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/lsp/eventlog.py

Symbols in `agent/lsp/eventlog.py`.

- L60 `_short_path(file_path: str)` (function) — Render *file_path* relative to the cwd when sensible, else absolute.
- L78 `_emit(server_id: str, level: int, message: str)` (function)
- L82 `_announce_once(bucket: set, key: Tuple)` (function) — Return True if *key* has not been announced for *bucket* yet.
- L100 `log_clean(server_id: str, file_path: str)` (function) — No diagnostics emitted for *file_path*.  DEBUG (silent at default).
- L105 `log_disabled(server_id: str, file_path: str, reason: str)` (function) — LSP intentionally skipped for this file (feature off, ext unmapped,
- L111 `log_active(server_id: str, workspace_root: str)` (function) — A new LSP client started for (server_id, workspace_root).
- L124 `log_diagnostics(server_id: str, file_path: str, count: int)` (function) — Diagnostics arrived for a file.  INFO every time — these are the
- L131 `log_no_project_root(server_id: str, file_path: str)` (function) — File had no recognised project marker.  INFO once per file,
- L141 `log_server_unavailable(server_id: str, binary_or_pkg: str)` (function) — The server binary couldn't be resolved.  WARNING once per
- L157 `log_no_server_configured(server_id: str)` (function) — No spawn recipe for this language.  WARNING once.
- L163 `log_timeout(server_id: str, file_path: str, kind: str='diagnostics')` (function) — A request to the server timed out.  WARNING every time — these are
- L173 `log_server_error(server_id: str, file_path: str, exc: BaseException)` (function) — An unexpected exception bubbled out of the LSP layer.  WARNING.
- L182 `log_spawn_failed(server_id: str, workspace_root: str, exc: BaseException)` (function) — The LSP server failed to spawn or initialize.  WARNING.
- L191 `reset_announce_caches()` (function) — Test-only: clear the dedup caches.  Production code never calls this.
