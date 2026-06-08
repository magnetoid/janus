---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_doctor_command_install.py

Symbols in `tests/hermes_cli/test_doctor_command_install.py`.

- L13 `_setup_doctor_env(monkeypatch, tmp_path, venv_name='venv')` (function) — Create a minimal HERMES_HOME + PROJECT_ROOT for doctor tests.
- L58 `_run_doctor(fix=False)` (function) — Run doctor and capture stdout.
- L69 `TestDoctorCommandInstallation` (class) — Tests for the ◆ Command Installation section.
- L73 `test_correct_symlink_shows_ok(self, monkeypatch, tmp_path)` (method)
- L90 `test_missing_symlink_shows_fail(self, monkeypatch, tmp_path)` (method)
- L103 `test_fix_creates_missing_symlink(self, monkeypatch, tmp_path)` (method)
- L118 `test_wrong_target_symlink_shows_warn(self, monkeypatch, tmp_path)` (method)
- L136 `test_fix_repairs_wrong_symlink(self, monkeypatch, tmp_path)` (method)
- L157 `test_missing_venv_entry_point_shows_warn(self, monkeypatch, tmp_path)` (method)
- L193 `test_dot_venv_dir_is_found(self, monkeypatch, tmp_path)` (method) — The check finds entry points in .venv/ as well as venv/.
- L211 `test_non_symlink_regular_file_shows_ok(self, monkeypatch, tmp_path)` (method) — If ~/.local/bin/hermes is a regular file (not symlink), accept it.
- L226 `test_termux_uses_prefix_bin(self, monkeypatch, tmp_path)` (method) — On Termux, the command link dir is $PREFIX/bin.
- L242 `test_windows_skips_check(self, monkeypatch, tmp_path)` (method) — On Windows, the Command Installation section is skipped.
