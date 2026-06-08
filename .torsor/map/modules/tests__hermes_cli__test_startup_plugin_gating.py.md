---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_startup_plugin_gating.py

Symbols in `tests/hermes_cli/test_startup_plugin_gating.py`.

- L41 `_live_subcommand_names()` (function) — Run ``hermes --help`` in-process and parse the subcommand block.
- L102 `test_first_positional_argv(argv, expected)` (function)
- L126 `test_discovery_skipped_for_builtins(argv)` (function)
- L139 `test_discovery_runs_for_unknown_positional(argv)` (function)
- L147 `test_builtin_set_covers_every_registered_subcommand()` (function) — Every subcommand registered in main() must appear in the set.
- L167 `test_builtin_set_has_no_phantom_entries()` (function) — No entry in the set should refer to a subcommand that no longer exists.
