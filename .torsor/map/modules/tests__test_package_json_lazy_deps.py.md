---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_package_json_lazy_deps.py

Symbols in `tests/test_package_json_lazy_deps.py`.

- L40 `_root_package_json()` (function)
- L45 `test_camofox_is_not_in_root_dependencies()` (function) — Camofox must be opt-in, installed lazily by its post_setup handler.
- L57 `test_agent_browser_stays_eager()` (function) — agent-browser is the default backend; it must remain eager.
- L69 `test_root_lockfile_has_no_camofox_entries()` (function) — Regenerated lockfiles should not contain Camofox tree entries.
