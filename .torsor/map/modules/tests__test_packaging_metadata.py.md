---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_packaging_metadata.py

Symbols in `tests/test_packaging_metadata.py`.

- L17 `_packages_find_include()` (function)
- L22 `test_every_on_disk_subpackage_is_covered_by_packages_find()` (function) — Regression test for #34701 (and the bug class behind #34034 / #28149).
- L64 `test_faster_whisper_is_not_a_base_dependency()` (function)
- L74 `test_manifest_includes_bundled_skills()` (function)
- L81 `test_bundled_plugin_manifests_ship_in_both_wheel_and_sdist()` (function) — Regression test for #34034 / #28149.
- L130 `_version_tuple(spec: str)` (function)
- L142 `test_starlette_pinned_above_cve_2026_48710_floor_in_pyproject()` (function) — Every extra that declares Starlette must pin a patched (>=1.0.1) version.
- L176 `test_locked_starlette_is_not_vulnerable_to_cve_2026_48710()` (function) — The committed uv.lock must resolve starlette to a patched version.
- L205 `test_locale_catalogs_ship_in_both_wheel_and_sdist()` (function) — Regression test for #27632 / #35374 / #23943.
