---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/skill_provenance.py

Symbols in `tools/skill_provenance.py`.

- L48 `set_current_write_origin(origin: str)` (function) — Bind the active write origin to the current context.
- L57 `reset_current_write_origin(token: contextvars.Token[str])` (function) — Restore the prior write origin context.
- L62 `get_current_write_origin()` (function) — Return the active write origin.
- L75 `is_background_review()` (function) — Convenience: True iff the current write origin is the background
