---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/proxy/adapters/xai.py

Symbols in `hermes_cli/proxy/adapters/xai.py`.

- L31 `XAIGrokAdapter` (class) — Proxy upstream for xAI Grok via Hermes-managed OAuth credentials.
- L36 `__init__(self)` (method)
- L41 `name(self)` (method)
- L45 `display_name(self)` (method)
- L49 `allowed_paths(self)` (method)
- L52 `is_authenticated(self)` (method)
- L56 `get_credential(self)` (method)
- L76 `get_retry_credential(self, *, failed_credential: UpstreamCredential, status_code: int)` (method)
- L111 `_load_pool(self)` (method)
- L118 `_credential_from_entry(self, entry: PooledCredential)` (method)
