---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_file_safety_cross_profile.py

Symbols in `tests/agent/test_file_safety_cross_profile.py`.

- L27 `fake_hermes(tmp_path, monkeypatch)` (function) — Build a fake Hermes layout:
- L75 `_set_active_home(monkeypatch, hermes_home: Path)` (function) — Point file_safety._hermes_home_path at a specific profile dir.
- L86 `TestResolveActiveProfileName` (class)
- L87 `test_default_when_home_is_root(self, fake_hermes, monkeypatch)` (method)
- L92 `test_named_profile(self, fake_hermes, monkeypatch)` (method)
- L97 `test_falls_back_to_default_on_resolution_failure(self, fake_hermes, monkeypatch)` (method) — If HERMES_HOME resolution raises, return 'default' rather than crashing the tool.
- L114 `TestClassifyCrossProfileTarget` (class)
- L115 `test_same_profile_write_returns_none(self, fake_hermes, monkeypatch)` (method)
- L123 `test_security_writing_default_skill(self, fake_hermes, monkeypatch)` (method) — The exact incident from May 2026.
- L135 `test_default_writing_security_skill(self, fake_hermes, monkeypatch)` (method) — Inverse direction — default-profile session reaching into a named profile.
- L146 `test_named_to_named_cross_profile(self, fake_hermes, monkeypatch)` (method)
- L156 `test_all_profile_scoped_areas_classified(self, fake_hermes, monkeypatch, area)` (method)
- L164 `test_non_hermes_path_returns_none(self, fake_hermes, monkeypatch, tmp_path)` (method)
- L170 `test_hermes_config_not_classified_as_cross_profile(self, fake_hermes, monkeypatch)` (method) — Files under <root>/config.yaml or <root>/.env are NOT profile-scoped
- L187 `TestGetCrossProfileWarning` (class)
- L188 `test_in_profile_returns_none(self, fake_hermes, monkeypatch)` (method)
- L195 `test_cross_profile_warning_names_both_profiles(self, fake_hermes, monkeypatch)` (method)
- L210 `test_warning_is_defense_in_depth_not_boundary(self, fake_hermes, monkeypatch)` (method)
