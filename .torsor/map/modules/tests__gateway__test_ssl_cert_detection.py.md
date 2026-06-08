---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_ssl_cert_detection.py

Symbols in `tests/gateway/test_ssl_cert_detection.py`.

- L6 `test_ensure_ssl_certs_ignores_stale_ssl_cert_file(monkeypatch, tmp_path)` (function) — A missing SSL_CERT_FILE should be treated as unset, not trusted.
- L35 `test_ensure_ssl_certs_keeps_existing_ssl_cert_file(monkeypatch, tmp_path)` (function) — A valid user-provided SSL_CERT_FILE must not be overwritten.
