---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# hermes_time.py

Symbols in `hermes_time.py`.

- L37 `_resolve_timezone_name()` (function) — Read the configured IANA timezone string (or empty string).
- L64 `_get_zoneinfo(name: str)` (function) — Validate and return a ZoneInfo, or None if invalid.
- L78 `get_timezone()` (function) — Return the user's configured ZoneInfo, or None (meaning server-local).
- L91 `now()` (function) — Return the current time as a timezone-aware datetime.
