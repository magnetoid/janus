---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_local_shell_init.py

Symbols in `tests/tools/test_local_shell_init.py`.

- L21 `TestResolveShellInitFiles` (class)
- L22 `test_auto_sources_bashrc_when_present(self, tmp_path, monkeypatch)` (method)
- L36 `test_auto_sources_profile_when_present(self, tmp_path, monkeypatch)` (method) — ~/.profile is where ``n`` / ``nvm`` installers typically write
- L53 `test_auto_sources_bash_profile_when_present(self, tmp_path, monkeypatch)` (method)
- L66 `test_auto_sources_profile_before_bashrc(self, tmp_path, monkeypatch)` (method) — Both files present: profile runs first so PATH exports in
- L87 `test_skips_bashrc_when_missing(self, tmp_path, monkeypatch)` (method)
- L99 `test_auto_source_bashrc_off_suppresses_default(self, tmp_path, monkeypatch)` (method)
- L114 `test_explicit_list_wins_over_auto(self, tmp_path, monkeypatch)` (method)
- L131 `test_expands_home_and_env_vars(self, tmp_path, monkeypatch)` (method)
- L153 `test_missing_explicit_files_are_skipped_silently(self, tmp_path, monkeypatch)` (method)
- L164 `TestPrependShellInit` (class)
- L165 `test_empty_list_returns_command_unchanged(self)` (method)
- L168 `test_prepends_guarded_source_lines(self)` (method)
- L178 `test_escapes_single_quotes(self)` (method)
- L189 `TestSnapshotEndToEnd` (class) — Spin up a real LocalEnvironment and confirm the snapshot sources
- L193 `test_snapshot_picks_up_init_file_exports(self, tmp_path, monkeypatch)` (method)
- L216 `test_profile_path_export_survives_bashrc_interactive_guard(self, tmp_path, monkeypatch)` (method) — Reproduces the Debian/Ubuntu + ``n``/``nvm`` case.
