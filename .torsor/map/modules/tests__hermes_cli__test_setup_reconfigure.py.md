---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_setup_reconfigure.py

Symbols in `tests/hermes_cli/test_setup_reconfigure.py`.

- L20 `_make_setup_args(**overrides)` (function)
- L31 `existing_install(tmp_path, monkeypatch)` (function) — Simulate a returning user with an existing configured install.
- L41 `fresh_install(tmp_path, monkeypatch)` (function) — Simulate a first-time user with no existing configuration.
- L50 `_enter_existing_install_patches(stack, **extra)` (function) — Apply standard existing-install mocks via an ExitStack.
- L77 `_enter_fresh_install_patches(stack, **extra)` (function)
- L100 `TestExistingInstallDefault` (class) — Bare `hermes setup` on an existing install = full reconfigure wizard.
- L103 `test_bare_setup_runs_full_reconfigure_without_menu(self, existing_install)` (method) — No menu, no prompt_choice — just run every section in sequence.
- L133 `test_reconfigure_flag_is_backwards_compat_noop(self, existing_install)` (method) — `hermes setup --reconfigure` behaves the same as bare `hermes setup`.
- L158 `TestQuickFlag` (class) — `--quick` on an existing install runs the fill-missing flow.
- L161 `test_quick_flag_runs_quick_setup_only(self, existing_install)` (method)
- L186 `TestFreshInstall` (class) — On a fresh install (no active provider), flags are no-ops.
- L189 `test_bare_setup_runs_first_time_flow(self, fresh_install)` (method)
- L204 `test_reconfigure_on_fresh_install_falls_through(self, fresh_install)` (method)
- L219 `test_quick_on_fresh_install_falls_through(self, fresh_install)` (method)
- L235 `TestArgparse` (class) — The flags are plumbed through argparse to cmd_setup.
- L238 `test_reconfigure_flag_reaches_cmd_setup(self, monkeypatch)` (method)
- L255 `test_quick_flag_reaches_cmd_setup(self, monkeypatch)` (method)
- L272 `test_bare_setup_has_both_flags_false(self, monkeypatch)` (method)
