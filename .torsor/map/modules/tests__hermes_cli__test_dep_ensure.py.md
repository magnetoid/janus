---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_dep_ensure.py

Symbols in `tests/hermes_cli/test_dep_ensure.py`.

- L4 `test_ensure_dependency_skips_when_present()` (function) — ensure_dependency is a no-op when the dep is already available.
- L13 `test_ensure_dependency_returns_false_when_missing_noninteractive()` (function) — ensure_dependency returns False for missing dep in non-interactive mode.
- L23 `test_find_install_script_from_checkout(tmp_path)` (function) — _find_install_script finds scripts/install.sh in a git checkout.
- L36 `test_find_install_script_from_wheel(tmp_path)` (function) — _find_install_script finds bundled install.sh in a wheel.
- L49 `test_find_install_script_prefers_ps1_on_windows(tmp_path)` (function) — On Windows, _find_install_script should find install.ps1.
- L62 `test_find_install_script_returns_sh_on_posix(tmp_path)` (function) — On POSIX, _find_install_script should find install.sh.
- L75 `test_find_install_script_falls_back_to_repo_root(tmp_path)` (function) — When no bundled script, check repo root.
- L87 `test_find_install_script_returns_none_when_missing(tmp_path)` (function)
- L94 `test_has_system_browser_checks_windows_names()` (function)
- L102 `test_has_system_browser_checks_posix_names()` (function)
- L110 `test_has_hermes_agent_browser_windows_path(tmp_path)` (function)
- L120 `test_has_hermes_agent_browser_posix_path(tmp_path)` (function)
- L130 `test_has_hermes_agent_browser_legacy_node_modules_path(tmp_path)` (function) — Legacy git-clone installs put agent-browser in $HERMES_HOME/node_modules/.bin/.
- L141 `test_ensure_dependency_uses_powershell_on_windows(tmp_path)` (function)
