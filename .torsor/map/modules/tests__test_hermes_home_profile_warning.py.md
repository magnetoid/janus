---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_hermes_home_profile_warning.py

Symbols in `tests/test_hermes_home_profile_warning.py`.

- L22 `fresh_constants(monkeypatch, tmp_path)` (function) — Import hermes_constants fresh and reset the one-shot warn flag.
- L32 `TestGetHermesHomeProfileWarning` (class)
- L33 `test_classic_mode_no_active_profile_no_warning(self, fresh_constants, tmp_path, capsys)` (method) — Classic mode: no active_profile file → silent, returns ~/.hermes.
- L41 `test_default_active_profile_no_warning(self, fresh_constants, tmp_path, capsys)` (method) — active_profile=default → still no warning, returns ~/.hermes.
- L52 `test_named_profile_unset_home_warns_once(self, fresh_constants, tmp_path, capsys)` (method) — active_profile=coder + HERMES_HOME unset → warn loudly, still return fallback.
- L76 `test_hermes_home_set_suppresses_warning(self, fresh_constants, tmp_path, capsys, monkeypatch)` (method) — Even if active_profile is 'coder', setting HERMES_HOME suppresses warning.
- L90 `test_unreadable_active_profile_no_crash(self, fresh_constants, tmp_path, capsys)` (method) — active_profile that can't be decoded → fall through silently.
- L105 `test_empty_active_profile_no_warning(self, fresh_constants, tmp_path, capsys)` (method) — Empty active_profile file → treated as default, no warning.
