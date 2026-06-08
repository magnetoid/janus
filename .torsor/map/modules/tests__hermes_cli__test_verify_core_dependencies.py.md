---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_verify_core_dependencies.py

Symbols in `tests/hermes_cli/test_verify_core_dependencies.py`.

- L28 `temp_pyproject(tmp_path, monkeypatch)` (function) — Point hermes_cli.main.PROJECT_ROOT at a tmp dir with a minimal pyproject.
- L51 `fake_venv_python(tmp_path)` (function) — Create a fake venv python shim path that exists on disk.
- L61 `TestVerifyCoreDependencies` (class)
- L62 `test_no_action_when_all_deps_present(self, temp_pyproject, fake_venv_python)` (method) — The happy path: nothing missing, no repair install fires.
- L79 `test_triggers_reinstall_when_dep_missing(self, temp_pyproject, fake_venv_python)` (method) — The regression: one base dep is missing → trigger --reinstall.
- L108 `test_falls_back_to_per_package_install_when_reinstall_did_not_help(self, temp_pyproject, fake_venv_python)` (method) — If --reinstall doesn't repair the partial install (uv resolver
- L145 `test_skips_deps_excluded_by_environment_markers(self, temp_pyproject, fake_venv_python)` (method) — ``ptyprocess ; sys_platform != 'win32'`` should NOT be reported as
- L181 `test_no_pyproject_is_noop(self, tmp_path, monkeypatch)` (method) — If pyproject.toml is missing (unusual but possible in some test
- L194 `test_repair_reinstall_quarantines_running_shim_on_windows(self, temp_pyproject, fake_venv_python)` (method) — Regression: the ``--reinstall -e .`` repair must
- L238 `TestResolveInstallTargetPython` (class)
- L239 `test_uses_virtual_env_from_environment(self, tmp_path)` (method) — When VIRTUAL_ENV is set, the verification step must probe THAT
- L257 `test_returns_none_when_venv_python_missing(self, tmp_path)` (method) — If the path we'd point at doesn't exist (uv install failed before
