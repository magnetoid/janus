---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/scripts/test_release_acp_registry.py

Symbols in `tests/scripts/test_release_acp_registry.py`.

- L18 `_load_release_module(monkeypatch, tmp_root: Path)` (function) — Import scripts/release.py with REPO_ROOT pinned to a temp tree.
- L35 `_write_manifest(root: Path, version: str)` (function)
- L59 `test_update_acp_registry_versions_bumps_manifest_and_pin(monkeypatch, tmp_path)` (function)
- L74 `test_update_acp_registry_versions_is_silent_when_manifest_missing(monkeypatch, tmp_path)` (function) — Older release branches predate the ACP Registry asset — must no-op.
- L84 `test_update_version_files_bumps_manifest_alongside_pyproject(monkeypatch, tmp_path)` (function) — End-to-end: update_version_files() is the function release.py actually
