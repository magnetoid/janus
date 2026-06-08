---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_stage2_hook_puid_pgid.py

Symbols in `tests/tools/test_stage2_hook_puid_pgid.py`.

- L29 `stage2_text()` (function)
- L35 `_alias_lines(text: str)` (function) — The stage2 hook lines that resolve HERMES_UID/HERMES_GID from aliases.
- L44 `test_stage2_hook_resolves_puid_pgid_aliases(stage2_text: str)` (function)
- L54 `_resolve(stage2_text: str, env: dict[str, str])` (function) — Run the stage2 hook's alias-resolution lines in isolation and report the
- L72 `test_puid_pgid_populate_hermes_uid_gid(stage2_text: str)` (function)
- L76 `test_hermes_uid_gid_take_precedence_over_aliases(stage2_text: str)` (function)
- L84 `test_no_uid_vars_leaves_values_empty(stage2_text: str)` (function)
- L89 `test_stage2_hook_creates_s6_envdir_before_writing_browser_path(stage2_text: str)` (function) — Regression guard for browser-path export on runtimes where the
- L104 `test_stage2_hook_runs_config_migration_as_hermes(stage2_text: str)` (function)
- L109 `test_stage2_hook_documents_config_migration_opt_out(stage2_text: str)` (function)
