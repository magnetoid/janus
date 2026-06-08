---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_ignore_user_config_flags.py

Symbols in `tests/hermes_cli/test_ignore_user_config_flags.py`.

- L27 `_clean_env(monkeypatch)` (function) — Ensure the two env-var gates start AND end each test in a known state.
- L42 `TestIgnoreUserConfigEnvGate` (class) — ``load_cli_config()`` must honour ``HERMES_IGNORE_USER_CONFIG=1``.
- L50 `_write_user_config(self, tmp_path, model_default)` (method)
- L62 `_reload_cli(self, monkeypatch, tmp_path)` (method) — Point cli._hermes_home at tmp_path and return a fresh load_cli_config.
- L68 `test_user_config_loaded_when_flag_unset(self, tmp_path, monkeypatch)` (method)
- L78 `test_user_config_skipped_when_flag_set(self, tmp_path, monkeypatch)` (method) — With HERMES_IGNORE_USER_CONFIG=1, user config.yaml is ignored.
- L98 `test_flag_ignored_when_set_to_other_value(self, tmp_path, monkeypatch)` (method) — Only the literal value "1" activates the bypass, matching the yolo pattern.
- L110 `TestIgnoreRulesEnvGate` (class) — The constructor / env var must propagate to ``HermesCLI.ignore_rules``
- L116 `test_env_var_enables_ignore_rules(self, monkeypatch)` (method) — Setting HERMES_IGNORE_RULES=1 flips HermesCLI.ignore_rules True.
- L136 `test_constructor_flag_alone_enables_ignore_rules(self, monkeypatch)` (method)
- L144 `test_neither_flag_nor_env_leaves_rules_enabled(self, monkeypatch)` (method)
- L153 `TestCmdChatWiring` (class) — The wiring inside ``cmd_chat()`` in ``hermes_cli/main.py`` must set
- L159 `_simulate_cmd_chat_env_setup(self, args)` (method) — Replicate the exact snippet from cmd_chat in main.py.
- L166 `test_both_flags_set_both_env_vars(self, monkeypatch)` (method)
- L179 `test_only_ignore_user_config(self, monkeypatch)` (method)
- L192 `test_flags_absent_sets_nothing(self, monkeypatch)` (method)
- L205 `TestArgparseFlagsRegistered` (class) — Verify the `chat` subparser actually exposes --ignore-user-config
- L210 `test_flags_present_in_chat_parser(self)` (method) — Parse a synthetic chat invocation and check both attributes exist.
- L226 `test_main_py_registers_both_flags(self)` (method) — E2E: the real hermes parser accepts both flags.
