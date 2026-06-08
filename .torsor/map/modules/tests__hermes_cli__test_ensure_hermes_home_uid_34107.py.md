---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_ensure_hermes_home_uid_34107.py

Symbols in `tests/hermes_cli/test_ensure_hermes_home_uid_34107.py`.

- L29 `TestResolveHermesUidGid` (class)
- L30 `test_returns_parsed_values_when_both_set(self, monkeypatch)` (method)
- L38 `test_returns_none_when_unset(self, monkeypatch)` (method)
- L46 `test_uid_only_returns_gid_none(self, monkeypatch)` (method)
- L54 `test_invalid_uid_returns_none_for_that_field(self, monkeypatch)` (method)
- L62 `test_empty_string_treated_as_unset(self, monkeypatch)` (method)
- L70 `test_whitespace_padded_values(self, monkeypatch)` (method)
- L79 `test_windows_returns_none_none(self, monkeypatch)` (method)
- L93 `TestChownToHermesUid` (class)
- L94 `test_calls_os_chown_when_both_set(self, tmp_path, monkeypatch)` (method)
- L106 `test_uses_minus_one_for_missing_field(self, tmp_path, monkeypatch)` (method) — When only one env var is set, the other field passes -1 to
- L120 `test_no_op_when_neither_set(self, tmp_path, monkeypatch)` (method)
- L132 `test_eperm_is_silently_swallowed(self, tmp_path, monkeypatch)` (method) — When running as non-root, os.chown raises EPERM. That's fine —
- L151 `test_attributeerror_swallowed_for_windows_compat(self, tmp_path, monkeypatch)` (method) — os.chown doesn't exist on Windows. Catching AttributeError keeps
- L170 `TestSecureDirChown` (class)
- L172 `test_secure_dir_invokes_chown_when_env_set(self, tmp_path, monkeypatch)` (method)
- L185 `test_secure_dir_no_chown_when_env_unset(self, tmp_path, monkeypatch)` (method)
