---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/credential_persistence.py

Symbols in `agent/credential_persistence.py`.

- L97 `_normalize_key(key: Any)` (function)
- L103 `is_borrowed_credential_source(source: Any, provider_id: Any=None)` (function) — Return True when ``source`` points at a borrowed/reference-only secret.
- L114 `_is_secret_payload_key(key: Any)` (function)
- L123 `_fingerprint_value(value: Any)` (function)
- L133 `_credential_secret_fingerprint(payload: Mapping[str, Any])` (function)
- L151 `sanitize_borrowed_credential_payload(payload: Mapping[str, Any], provider_id: Any=None)` (function) — Return a disk-safe credential-pool payload.
