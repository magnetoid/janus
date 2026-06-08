---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_skills_install_flags.py

Symbols in `tests/hermes_cli/test_skills_install_flags.py`.

- L13 `test_cli_skills_install_yes_sets_skip_confirm(monkeypatch)` (function) — --yes should set skip_confirm=True but NOT force.
- L38 `test_cli_skills_install_y_alias(monkeypatch)` (function) — -y should behave the same as --yes.
- L61 `test_cli_skills_install_force_sets_force(monkeypatch)` (function) — --force should set force=True but NOT yes.
- L84 `test_cli_skills_install_force_and_yes_together(monkeypatch)` (function) — --force --yes should set both flags.
- L107 `test_cli_skills_install_no_flags(monkeypatch)` (function) — Without flags, both force and yes should be False.
