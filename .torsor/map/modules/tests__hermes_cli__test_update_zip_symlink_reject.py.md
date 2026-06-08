---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_update_zip_symlink_reject.py

Symbols in `tests/hermes_cli/test_update_zip_symlink_reject.py`.

- L19 `_build_zip_with_symlink_member(zip_path: str, link_name: str, target: str)` (function) — Write a ZIP containing a single member with S_IFLNK mode bits set.
- L29 `_build_normal_zip(zip_path: str)` (function) — Write a regular ZIP with a normal file member (no symlink).
- L35 `test_update_via_zip_rejects_symlink_member(tmp_path, monkeypatch)` (function) — A symlink member in the update ZIP must raise before extractall.
- L83 `test_update_via_zip_accepts_normal_member(tmp_path, monkeypatch, capsys)` (function) — A ZIP with only regular file members must extract without raising.
