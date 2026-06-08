---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_ws_auth_retry.py

Symbols in `tests/gateway/test_ws_auth_retry.py`.

- L18 `TestMattermostWSAuthRetry` (class) — gateway/platforms/mattermost.py — _ws_loop()
- L21 `test_401_handshake_stops_reconnect(self)` (method) — A WSServerHandshakeError with status 401 should stop the loop.
- L51 `test_403_handshake_stops_reconnect(self)` (method) — A WSServerHandshakeError with status 403 should stop the loop.
- L79 `test_transient_error_retries(self)` (method) — A transient ConnectionError should retry (not stop immediately).
- L112 `TestMatrixSyncAuthRetry` (class) — gateway/platforms/matrix.py — _sync_loop()
- L115 `test_unknown_token_sync_error_stops_loop(self)` (method) — A SyncError with M_UNKNOWN_TOKEN should stop syncing.
- L155 `test_exception_with_401_stops_loop(self)` (method) — An exception containing '401' should stop syncing.
- L190 `test_transient_error_retries(self)` (method) — A transient error should retry (not stop immediately).
