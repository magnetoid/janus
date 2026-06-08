---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_managed_uv.py

Symbols in `tests/hermes_cli/test_managed_uv.py`.

- L17 `_make_executable(path: Path)` (function) — Create a minimal fake uv binary at *path*.
- L28 `TestManagedUvPath` (class)
- L29 `test_posix(self, tmp_path)` (method)
- L35 `test_windows(self, tmp_path)` (method)
- L46 `TestResolveUv` (class)
- L47 `test_missing_returns_none(self, tmp_path)` (method)
- L52 `test_existing_executable(self, tmp_path)` (method)
- L59 `test_non_executable_file_returns_none(self, tmp_path)` (method)
- L74 `TestEnsureUv` (class)
- L75 `test_already_installed_no_bootstrap(self, tmp_path)` (method)
- L82 `test_installs_if_missing(self, tmp_path)` (method)
- L95 `test_install_failure_returns_falsy(self, tmp_path)` (method)
- L106 `TestEnsureUvUpdateBoundary` (class) — ``ensure_uv()`` must answer to both the single-value and the legacy
- L125 `test_success_usable_as_single_value(self, tmp_path)` (method)
- L134 `test_success_unpacks_as_legacy_two_tuple(self, tmp_path)` (method)
- L143 `test_failure_unpacks_without_raising(self, tmp_path)` (method)
- L153 `TestEnsureUvWindowsSafe` (class) — On Windows ``ensure_uv()`` must return a plain ``str``/``None``.
- L169 `test_uvresult_would_break_windows_list2cmdline(self)` (method)
- L178 `test_windows_returns_plain_str_safe_for_subprocess(self, tmp_path)` (method)
- L191 `test_windows_failure_returns_none(self, tmp_path)` (method)
- L203 `TestUpdateManagedUv` (class)
- L204 `test_no_uv_returns_none(self, tmp_path)` (method)
- L209 `test_self_update_success(self, tmp_path)` (method)
- L222 `test_self_update_failure_non_fatal(self, tmp_path)` (method)
- L237 `TestInstallUvInternals` (class)
- L238 `test_posix_sets_uv_unmanaged_install(self, tmp_path)` (method)
- L247 `test_windows_sets_uv_install_dir(self, tmp_path)` (method)
