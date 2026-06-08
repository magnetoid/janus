---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/acp/test_entry.py

Symbols in `tests/acp/test_entry.py`.

- L11 `test_main_enables_unstable_protocol(monkeypatch)` (function)
- L26 `test_main_version_prints_without_starting_server(monkeypatch, capsys)` (function)
- L36 `test_main_check_prints_ok_without_starting_server(monkeypatch, capsys)` (function)
- L44 `test_main_setup_runs_model_configuration(monkeypatch)` (function)
- L61 `test_main_setup_offers_browser_install_when_tty(monkeypatch)` (function) — When stdin is a TTY and the user answers yes, model setup is followed
- L80 `test_main_setup_skips_browser_prompt_on_no(monkeypatch)` (function)
- L97 `test_main_setup_browser_calls_ensure_dependency(monkeypatch)` (function) — `hermes-acp --setup-browser` routes through dep_ensure.ensure_dependency.
- L113 `test_main_setup_browser_forwards_yes_flag(monkeypatch)` (function) — --yes suppresses interactive prompts in ensure_dependency.
- L129 `test_main_setup_browser_stops_on_node_failure(monkeypatch)` (function) — If node install fails, browser install is not attempted.
- L146 `test_main_setup_browser_propagates_browser_failure(monkeypatch)` (function) — If browser install fails, exit code is 1.
