---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_cli_tools_command.py

Symbols in `tests/cli/test_cli_tools_command.py`.

- L8 `_make_cli(enabled_toolsets=None)` (function) — Build a minimal HermesCLI stub without running __init__.
- L20 `TestToolsSlashNoSubcommand` (class)
- L22 `test_bare_tools_shows_tool_list(self)` (method)
- L28 `test_unknown_subcommand_falls_back_to_show_tools(self)` (method)
- L38 `TestToolsSlashList` (class)
- L40 `test_list_calls_backend(self, capsys)` (method)
- L49 `test_list_does_not_modify_enabled_toolsets(self)` (method) — List is read-only — self.enabled_toolsets must not change.
- L61 `TestToolsSlashDisableWithReset` (class)
- L63 `test_disable_applies_directly_and_resets_session(self)` (method) — Disable applies immediately (no confirmation prompt) and resets session.
- L76 `test_disable_does_not_prompt_for_confirmation(self)` (method) — Disable no longer uses input() — it applies directly.
- L89 `test_disable_always_resets_session(self)` (method) — Even without a confirmation prompt, disable always resets the session.
- L101 `test_disable_missing_name_prints_usage(self, capsys)` (method)
- L111 `TestToolsSlashEnableWithReset` (class)
- L113 `test_enable_applies_directly_and_resets_session(self)` (method) — Enable applies immediately (no confirmation prompt) and resets session.
- L126 `test_enable_missing_name_prints_usage(self, capsys)` (method)
