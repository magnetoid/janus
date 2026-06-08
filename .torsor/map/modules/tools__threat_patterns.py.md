---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/threat_patterns.py

Symbols in `tools/threat_patterns.py`.

- L147 `_compile()` (function) — Compile pattern sets for each scope (all / context / strict).
- L187 `scan_for_threats(content: str, scope: str='context')` (function) — Return a list of matched pattern IDs in ``content`` at the given scope.
- L227 `first_threat_message(content: str, scope: str='strict')` (function) — Return a human-readable error string for the first threat found, or None.
