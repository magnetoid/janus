---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_local_env_windows_msys.py

Symbols in `tests/tools/test_local_env_windows_msys.py`.

- L36 `TestMsysToWindowsPath` (class)
- L37 `test_noop_on_non_windows(self, monkeypatch)` (method)
- L44 `test_translates_drive_path(self, monkeypatch)` (method)
- L49 `test_translates_bare_drive_root(self, monkeypatch)` (method)
- L56 `test_idempotent_on_already_windows_path(self, monkeypatch)` (method)
- L60 `test_does_not_translate_multi_char_first_segment(self, monkeypatch)` (method) — ``/tmp/foo`` and ``/home/x`` must NOT be misread as drive paths
- L68 `test_empty_string(self, monkeypatch)` (method)
- L77 `TestResolveSafeCwdWindows` (class)
- L78 `test_msys_path_resolves_to_native_when_native_exists(self, monkeypatch, tmp_path)` (method) — The whole point of this fix: a Git Bash ``/c/Users/x`` value
- L103 `TestUpdateCwdWindowsMsys` (class)
- L104 `test_marker_file_msys_path_stored_in_native_form(self, monkeypatch, tmp_path)` (method) — When Git Bash writes ``/c/Users/x`` to the cwd marker file on
- L145 `TestExtractCwdFromOutputWindowsMsys` (class)
- L146 `test_stale_msys_marker_does_not_clobber_cwd(self, monkeypatch, tmp_path)` (method) — When the cwd marker in stdout points at a non-existent path,
- L176 `test_valid_msys_marker_normalized_to_native(self, monkeypatch, tmp_path)` (method)
