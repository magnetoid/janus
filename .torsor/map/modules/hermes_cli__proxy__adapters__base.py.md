---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/proxy/adapters/base.py

Symbols in `hermes_cli/proxy/adapters/base.py`.

- L22 `UpstreamCredential` (class) — A resolved bearer + base URL ready to forward to.
- L38 `UpstreamAdapter` (class) — Contract for an upstream provider the proxy can forward to.
- L43 `name(self)` (method) — Adapter key used on the CLI (e.g. ``"nous"``).
- L48 `display_name(self)` (method) — Human-readable provider name for logs and ``proxy status``.
- L53 `allowed_paths(self)` (method) — Set of relative request paths the upstream accepts.
- L63 `is_authenticated(self)` (method) — Return True if the user has usable credentials for this upstream.
- L71 `get_credential(self)` (method) — Return a fresh credential, refreshing or rotating if necessary.
- L84 `get_retry_credential(self, *, failed_credential: UpstreamCredential, status_code: int)` (method) — Return an alternate credential after an upstream auth failure.
- L98 `describe(self)` (method) — One-line status summary for ``proxy status``.
