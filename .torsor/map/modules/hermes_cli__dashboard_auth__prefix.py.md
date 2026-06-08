---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/dashboard_auth/prefix.py

Symbols in `hermes_cli/dashboard_auth/prefix.py`.

- L35 `normalise_prefix(raw: Optional[str])` (function) — Normalise an X-Forwarded-Prefix header value.
- L63 `prefix_from_request(request)` (function) — Convenience wrapper that reads the header off a Starlette/FastAPI
- L75 `_normalise_public_url(raw: Optional[str])` (function) — Normalise a ``dashboard.public_url`` value.
- L109 `_load_dashboard_section()` (function) — Return the ``dashboard`` block from ``config.yaml`` if it exists
- L135 `resolve_public_url()` (function) — Resolve the operator-declared dashboard public URL.
