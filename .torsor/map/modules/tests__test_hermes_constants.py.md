---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_hermes_constants.py

Symbols in `tests/test_hermes_constants.py`.

- L19 `TestGetDefaultHermesRoot` (class) — Tests for get_default_hermes_root() — Docker/custom deployment awareness.
- L22 `test_no_hermes_home_returns_native(self, tmp_path, monkeypatch)` (method) — When HERMES_HOME is not set, returns ~/.hermes.
- L29 `test_hermes_home_is_native(self, tmp_path, monkeypatch)` (method) — When HERMES_HOME = ~/.hermes, returns ~/.hermes.
- L37 `test_hermes_home_is_profile(self, tmp_path, monkeypatch)` (method) — When HERMES_HOME is a profile under ~/.hermes, returns ~/.hermes.
- L46 `test_hermes_home_is_docker(self, tmp_path, monkeypatch)` (method) — When HERMES_HOME points outside ~/.hermes (Docker), returns HERMES_HOME.
- L54 `test_hermes_home_is_custom_path(self, tmp_path, monkeypatch)` (method) — Any HERMES_HOME outside ~/.hermes is treated as the root.
- L62 `test_docker_profile_active(self, tmp_path, monkeypatch)` (method) — When a Docker profile is active (HERMES_HOME=<root>/profiles/<name>),
- L72 `test_no_hermes_home_returns_localappdata_root_on_windows(self, tmp_path, monkeypatch)` (method) — Native Windows falls back to %LOCALAPPDATA%\hermes, not ~/.hermes.
- L82 `test_no_hermes_home_uses_windows_path_when_localappdata_missing(self, tmp_path, monkeypatch)` (method) — Windows fallback still uses AppData/Local/hermes without LOCALAPPDATA.
- L93 `TestGetHermesHome` (class) — Tests for get_hermes_home() platform-aware fallback.
- L96 `test_windows_fallback_uses_localappdata(self, tmp_path, monkeypatch)` (method) — When HERMES_HOME is unset on Windows, use %LOCALAPPDATA%\hermes.
- L108 `TestIsContainer` (class) — Tests for is_container() — Docker/Podman detection.
- L111 `_reset_cache(self, monkeypatch)` (method) — Reset the cached detection result before each test.
- L115 `test_detects_dockerenv(self, monkeypatch, tmp_path)` (method) — /.dockerenv triggers container detection.
- L121 `test_detects_containerenv(self, monkeypatch, tmp_path)` (method) — /run/.containerenv triggers container detection (Podman).
- L127 `test_detects_cgroup_docker(self, monkeypatch, tmp_path)` (method) — /proc/1/cgroup containing 'docker' triggers detection.
- L138 `test_negative_case(self, monkeypatch, tmp_path)` (method) — Returns False on a regular Linux host.
- L149 `test_caches_result(self, monkeypatch)` (method) — Second call uses cached value without re-probing.
- L158 `TestParseReasoningEffort` (class) — Tests for parse_reasoning_effort() — string → reasoning config dict.
- L162 `test_empty_or_whitespace_returns_none(self, value)` (method) — Empty / whitespace-only input falls back to caller default (None).
- L166 `test_none_disables_reasoning(self)` (method) — The literal "none" disables reasoning explicitly.
- L171 `test_each_valid_level(self, level)` (method) — Every level listed in VALID_REASONING_EFFORTS is accepted as-is.
- L185 `test_case_and_whitespace_normalized(self, raw, expected_effort)` (method) — Mixed case and surrounding whitespace are normalized before lookup.
- L197 `test_unknown_levels_return_none(self, value)` (method) — Unrecognized strings fall back to the caller default (None).
- L201 `test_known_supported_levels_are_documented(self)` (method) — Guard against silently dropping a documented level.
- L212 `TestSecureParentDir` (class) — Tests for secure_parent_dir() — prevents chmod on / or top-level dirs.
- L215 `test_safe_path_calls_chmod(self, tmp_path, monkeypatch)` (method) — Normal nested path (depth >= 3) should call os.chmod.
- L229 `test_root_dir_skipped(self, monkeypatch)` (method) — Parent resolving to / must NOT be chmod'd.
- L238 `test_top_level_dir_skipped(self, monkeypatch)` (method) — Parent resolving to a top-level dir (depth 2) must NOT be chmod'd.
- L247 `test_two_component_path_skipped(self, monkeypatch)` (method) — Parent with < 3 resolved parts must NOT be chmod'd.
- L266 `test_oserror_suppressed(self, tmp_path, monkeypatch)` (method) — OSError from chmod should be silently caught.
- L280 `test_symlink_resolved(self, tmp_path, monkeypatch)` (method) — Symlinks should be resolved before checking depth.
