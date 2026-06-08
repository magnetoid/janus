---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/browser_provider.py

Symbols in `agent/browser_provider.py`.

- L49 `BrowserProvider` (class) — Abstract base class for a cloud browser backend.
- L63 `name(self)` (method) — Stable short identifier used in the ``browser.cloud_provider``
- L72 `display_name(self)` (method) — Human-readable label shown in ``hermes tools``. Defaults to ``name``.
- L77 `is_available(self)` (method) — Return True when this provider can service calls.
- L90 `create_session(self, task_id: str)` (method) — Create a cloud browser session and return session metadata.
- L111 `close_session(self, session_id: str)` (method) — Release / terminate a cloud session by its provider session ID.
- L120 `emergency_cleanup(self, session_id: str)` (method) — Best-effort session teardown during process exit.
- L127 `get_setup_schema(self)` (method) — Return provider metadata for the ``hermes tools`` picker.
- L169 `is_configured(self)` (method) — Backward-compat alias for :meth:`is_available`.
- L173 `provider_name(self)` (method) — Backward-compat alias returning :attr:`display_name`.
