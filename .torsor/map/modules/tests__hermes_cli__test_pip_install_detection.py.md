---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_pip_install_detection.py

Symbols in `tests/hermes_cli/test_pip_install_detection.py`.

- L4 `test_pip_install_detected_when_no_git_dir(tmp_path)` (function) — When PROJECT_ROOT has no .git, detect as pip install.
- L13 `test_git_install_detected_when_git_dir_exists(tmp_path)` (function) — When PROJECT_ROOT has .git, detect as git install.
- L23 `test_managed_install_takes_precedence(tmp_path)` (function) — When HERMES_MANAGED is set, that takes precedence over git detection.
- L33 `test_recommended_update_command_pip()` (function) — Pip installs recommend pip install --upgrade.
- L42 `test_stamp_file_takes_precedence(tmp_path)` (function)
- L51 `test_container_without_stamp_is_not_docker(tmp_path)` (function) — An unstamped install in a generic container must NOT be flagged as docker.
- L70 `test_container_pip_install_without_stamp_is_pip(tmp_path)` (function) — Container + no .git + no stamp -> pip, not docker (issue #34397).
- L79 `test_recommended_update_command_docker()` (function)
- L84 `test_banner_warns_on_pip_install(tmp_path)` (function) — The welcome banner surfaces a warning when the install method is pip.
- L110 `test_banner_no_pip_warning_on_git_install(tmp_path)` (function) — Git installs must not show the pip-install warning.
