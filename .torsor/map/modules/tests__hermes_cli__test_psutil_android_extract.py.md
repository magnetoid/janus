---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_psutil_android_extract.py

Symbols in `tests/hermes_cli/test_psutil_android_extract.py`.

- L22 `_add_dir(tf: tarfile.TarFile, name: str)` (function)
- L29 `_add_file(tf: tarfile.TarFile, name: str, content: str)` (function)
- L37 `_build_psutil_archive(archive: Path, *, malicious_symlink: bool)` (function)
- L54 `test_prepare_patched_psutil_sdist_rejects_symlink_member(tmp_path)` (function) — A symlink member must be rejected before any file payload is written.
- L66 `test_install_psutil_android_compat_uses_patched_tree(tmp_path)` (function) — Updater path should install from the patched temporary sdist tree.
- L100 `test_install_psutil_android_script_uses_patched_tree(tmp_path, monkeypatch, capsys)` (function) — Standalone installer script should reuse the same safe patched tree.
