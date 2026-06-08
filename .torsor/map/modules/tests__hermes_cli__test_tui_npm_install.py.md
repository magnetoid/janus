---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_tui_npm_install.py

Symbols in `tests/hermes_cli/test_tui_npm_install.py`.

- L11 `main_mod()` (function)
- L17 `_touch_ink(root: Path)` (function)
- L23 `_touch_tui_entry(root: Path)` (function)
- L29 `test_need_install_when_ink_missing(tmp_path: Path, main_mod)` (function)
- L34 `test_no_install_when_lock_newer_but_hidden_lock_matches(tmp_path: Path, main_mod)` (function)
- L45 `test_need_install_when_required_package_missing_from_hidden_lock(tmp_path: Path, main_mod)` (function)
- L56 `test_no_install_when_only_optional_peer_package_missing_from_hidden_lock(tmp_path: Path, main_mod)` (function)
- L67 `test_no_install_when_only_peer_annotation_differs(tmp_path: Path, main_mod)` (function) — npm 9 drops the ``peer`` flag from the hidden lock on dev-deps that are
- L88 `test_install_when_version_differs_even_with_peer_drop(tmp_path: Path, main_mod)` (function) — The peer-drop tolerance must not mask a real version skew.
- L100 `test_no_install_when_lock_older_than_marker(tmp_path: Path, main_mod)` (function)
- L109 `test_need_install_when_marker_missing(tmp_path: Path, main_mod)` (function)
- L115 `test_no_install_without_lockfile_when_ink_present(tmp_path: Path, main_mod)` (function)
- L120 `test_no_install_prebuilt_bundle_mode(tmp_path: Path, main_mod)` (function) — dist/entry.js present and no package-lock.json → prebuilt bundle, skip npm install.
- L126 `test_need_rebuild_when_tui_bundle_missing(tmp_path: Path, main_mod)` (function)
- L133 `test_no_rebuild_when_tui_bundle_newer_than_inputs(tmp_path: Path, main_mod)` (function)
- L144 `test_rebuild_when_tui_source_newer_than_bundle(tmp_path: Path, main_mod)` (function)
- L155 `test_make_tui_argv_skips_build_only_on_termux_when_fresh(tmp_path: Path, main_mod, monkeypatch)` (function)
- L175 `test_make_tui_argv_skips_install_on_termux_when_bundle_fresh(tmp_path: Path, main_mod, monkeypatch)` (function)
- L195 `test_make_tui_argv_scopes_npm_install_on_termux_workspace(tmp_path: Path, main_mod, monkeypatch)` (function)
- L233 `test_make_tui_argv_keeps_desktop_workspace_install_behaviour(tmp_path: Path, main_mod, monkeypatch)` (function)
- L268 `test_make_tui_argv_keeps_desktop_always_build_behaviour(tmp_path: Path, main_mod, monkeypatch)` (function)
- L294 `test_workspace_root_returns_parent_when_subpackage(tmp_path: Path, main_mod)` (function) — Sub-package has package.json, no lockfile; parent has lockfile → parent.
- L303 `test_workspace_root_returns_dir_when_standalone(tmp_path: Path, main_mod)` (function) — No package.json → not a sub-package, return dir itself.
- L308 `test_workspace_root_returns_dir_when_own_lockfile(tmp_path: Path, main_mod)` (function) — Has package.json AND its own lockfile → standalone, return dir.
- L316 `test_workspace_root_returns_dir_when_no_parent_lockfile(tmp_path: Path, main_mod)` (function) — Has package.json, no own lockfile, but parent also has no lockfile → standalone.
- L327 `test_workspace_root_consistent_with_need_npm_install(tmp_path: Path, main_mod)` (function) — Divergence regression: if someone creates ui-tui/package-lock.json
- L360 `test_no_stray_lockfiles_in_workspace_subdirs(main_mod)` (function) — Workspace sub-directories must not contain their own package-lock.json.
- L397 `test_tui_launch_install_uses_workspace_scope(tmp_path: Path, main_mod, monkeypatch)` (function) — TUI launch npm install must pass --workspace ui-tui to avoid pulling apps/desktop.
