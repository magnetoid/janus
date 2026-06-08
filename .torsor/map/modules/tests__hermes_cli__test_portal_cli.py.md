---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_portal_cli.py

Symbols in `tests/hermes_cli/test_portal_cli.py`.

- L18 `_args(portal_command)` (function)
- L23 `test_bare_portal_and_login_run_one_shot(monkeypatch, sub)` (function) — `hermes portal`, `hermes portal login` -> one-shot onboarding.
- L48 `test_info_and_status_alias_run_status(monkeypatch, sub)` (function) — `hermes portal info` and the `status` back-compat alias -> status.
- L70 `test_open_and_tools_dispatch(monkeypatch)` (function)
- L80 `test_unknown_subcommand_returns_error(capsys)` (function)
- L87 `test_login_cancelled_returns_one(monkeypatch)` (function)
- L98 `test_parser_registers_subcommands()` (function)
- L114 `test_one_shot_delegates_to_model_flow_nous(monkeypatch)` (function) — `hermes portal` must run the quick-setup Nous flow (login + MODEL PICK +
- L141 `test_one_shot_swallows_cancel_and_systemexit(monkeypatch, exc)` (function) — A cancel/abort from the delegated Nous flow must NOT escape and kill the
