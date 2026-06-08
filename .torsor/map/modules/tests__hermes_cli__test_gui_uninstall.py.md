---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_gui_uninstall.py

Symbols in `tests/hermes_cli/test_gui_uninstall.py`.

- L17 `_make_agent(hermes_home: Path)` (function) — Create a fake agent install: source package + venv.
- L26 `_make_gui_build(hermes_home: Path)` (function) — Create the source-built GUI artifacts a `hermes desktop` run produces.
- L37 `_make_user_data(hermes_home: Path)` (function)
- L43 `test_agent_is_installed_detects_source_and_venv(tmp_path)` (function)
- L51 `test_agent_is_installed_venv_only(tmp_path)` (function) — A checkout with only a venv (no package dir yet) still counts.
- L58 `test_source_built_artifacts_lists_known_paths(tmp_path)` (function)
- L69 `test_gui_is_installed_true_when_built(tmp_path, monkeypatch)` (function)
- L79 `test_gui_is_installed_false_when_nothing(tmp_path, monkeypatch)` (function)
- L87 `test_uninstall_gui_removes_only_gui_artifacts(tmp_path, monkeypatch)` (function) — The core invariant: GUI gone, agent + user data untouched.
- L120 `test_uninstall_gui_removes_userdata(tmp_path, monkeypatch)` (function)
- L134 `test_uninstall_gui_keeps_userdata_when_requested(tmp_path, monkeypatch)` (function)
- L147 `test_uninstall_gui_removes_packaged_bundle(tmp_path, monkeypatch)` (function)
- L161 `test_gui_install_summary_shape(tmp_path, monkeypatch)` (function)
- L178 `test_userdata_dir_per_platform(monkeypatch)` (function) — userData path matches Electron's app.getPath('userData') for "Hermes".
- L191 `test_userdata_dir_windows(monkeypatch)` (function)
- L200 `test_remove_path_handles_symlink(tmp_path)` (function)
- L211 `_Args` (class) — Minimal argparse-Namespace stand-in for run_uninstall.
- L214 `__init__(self, *, yes=False, full=False, gui=False, gui_summary=False)` (method)
- L221 `test_run_uninstall_yes_keep_data_is_non_interactive(tmp_path, monkeypatch)` (function) — ``--yes`` (no ``--full``) runs with no prompt, sweeps the GUI, keeps data.
- L266 `test_run_uninstall_yes_full_wipes_home(tmp_path, monkeypatch)` (function) — ``--yes --full`` removes the whole HERMES_HOME non-interactively.
- L294 `test_uninstall_module_main_gui_mode(tmp_path, monkeypatch)` (function) — `python -m hermes_cli.uninstall --mode gui` runs the GUI-only path.
- L327 `test_uninstall_module_main_rejects_bad_mode()` (function) — An invalid --mode exits non-zero (argparse), never silently full-wipes.
- L336 `test_uninstall_args_namespace_mode_mapping()` (function) — _UninstallArgs maps mode → the gui/full flags run_uninstall reads.
