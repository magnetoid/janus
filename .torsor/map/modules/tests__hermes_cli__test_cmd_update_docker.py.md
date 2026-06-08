---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_cmd_update_docker.py

Symbols in `tests/hermes_cli/test_cmd_update_docker.py`.

- L33 `test_cmd_update_in_docker_prints_guidance_and_exits(mock_run, _mock_method, _mock_managed, capsys)` (function) — ``hermes update`` inside Docker → friendly message + exit 1, no git calls.
- L55 `test_cmd_update_check_in_docker_prints_guidance_and_exits(mock_run, _mock_method, _mock_managed, capsys)` (function) — ``hermes update --check`` inside Docker → same message + exit 1, no fetch.
- L74 `test_cmd_update_in_docker_ignores_yes_and_force(mock_run, _mock_method, _mock_managed, capsys)` (function) — ``--yes`` / ``--force`` don't bypass the Docker bail-out.
- L96 `test_cmd_update_check_direct_in_docker(mock_run, _mock_method, capsys)` (function) — Calling ``_cmd_update_check`` directly (no apply path) also bails.
- L116 `test_cmd_update_on_git_install_does_not_print_docker_message(_mock_run, _mock_method, _mock_managed, capsys)` (function) — Source/git installs MUST NOT hit the Docker branch.
- L148 `test_cmd_update_check_on_pip_install_still_uses_pypi(_mock_pypi, _mock_method, capsys)` (function) — PyPI installs route to PyPI check, not the Docker bail-out.
- L162 `test_format_docker_update_message_contents()` (function) — Lock in the high-value content of the Docker update message.
