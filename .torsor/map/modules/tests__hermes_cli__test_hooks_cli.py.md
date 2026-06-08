---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_hooks_cli.py

Symbols in `tests/hermes_cli/test_hooks_cli.py`.

- L19 `_isolated_home(tmp_path, monkeypatch)` (function)
- L27 `_hook_script(tmp_path: Path, body: str, name: str='hook.sh')` (function)
- L34 `_run(sub_args: SimpleNamespace)` (function) — Capture stdout for a hooks_command invocation.
- L45 `TestHooksList` (class)
- L46 `test_empty_config(self, tmp_path)` (method)
- L51 `test_shows_configured_and_consent_status(self, tmp_path)` (method)
- L82 `TestHooksTest` (class)
- L83 `test_synthetic_payload_matches_production_shape(self, tmp_path)` (method) — `hermes hooks test` must feed the script stdin in the same
- L114 `test_fires_real_subprocess_and_parses_block(self, tmp_path)` (method)
- L138 `test_for_tool_matcher_filters(self, tmp_path)` (method)
- L154 `test_unknown_event(self)` (method)
- L166 `TestHooksRevoke` (class)
- L167 `test_revoke_removes_entry(self, tmp_path)` (method)
- L177 `test_revoke_unknown(self, tmp_path)` (method)
- L187 `TestHooksDoctor` (class)
- L188 `test_flags_missing_exec_bit(self, tmp_path)` (method)
- L197 `test_flags_unallowlisted(self, tmp_path)` (method)
- L204 `test_flags_invalid_json(self, tmp_path)` (method)
- L215 `test_flags_mtime_drift(self, tmp_path, monkeypatch)` (method) — Allowlist with older mtime than current -> drift warning.
- L238 `test_clean_script_runs(self, tmp_path)` (method)
- L246 `test_unallowlisted_script_is_not_executed(self, tmp_path)` (method) — Regression for M4: `hermes hooks doctor` used to run every
