---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_atomic_replace_symlinks.py

Symbols in `tests/test_atomic_replace_symlinks.py`.

- L34 `_write_tmp(dir_: Path, content: str)` (function)
- L40 `test_atomic_replace_preserves_symlink(tmp_path: Path)` (function)
- L56 `test_atomic_replace_regular_file(tmp_path: Path)` (function)
- L68 `test_atomic_replace_first_time_create(tmp_path: Path)` (function)
- L79 `test_atomic_replace_accepts_pathlike_and_str(tmp_path: Path)` (function)
- L97 `test_atomic_json_write_preserves_symlink(tmp_path: Path)` (function)
- L110 `test_atomic_yaml_write_preserves_symlink(tmp_path: Path)` (function)
- L123 `test_atomic_json_write_preserves_symlink_permissions(tmp_path: Path)` (function) — Symlinked targets keep the real file's permission bits.
- L144 `test_atomic_replace_broken_symlink_creates_target(tmp_path: Path)` (function) — A symlink pointing at a missing file: the write should create the
