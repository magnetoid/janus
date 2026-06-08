---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_shell_hooks_consent.py

Symbols in `tests/agent/test_shell_hooks_consent.py`.

- L19 `_isolated_home(tmp_path, monkeypatch)` (function)
- L27 `_write_hook_script(tmp_path: Path)` (function)
- L37 `TestTTYPromptFlow` (class)
- L38 `test_first_use_prompts_and_approves(self, tmp_path)` (method)
- L57 `test_first_use_prompts_and_rejects(self, tmp_path)` (method)
- L74 `test_subsequent_use_does_not_prompt(self, tmp_path)` (method) — After the first approval, re-registration must be silent.
- L107 `TestNonTTYFlow` (class)
- L108 `test_no_tty_no_flag_skips_registration(self, tmp_path)` (method)
- L122 `test_no_tty_with_argument_flag_accepts(self, tmp_path)` (method)
- L136 `test_no_tty_with_env_accepts(self, tmp_path, monkeypatch)` (method)
- L151 `test_no_tty_with_config_accepts(self, tmp_path)` (method)
- L172 `TestAllowlistOps` (class)
- L173 `test_mtime_recorded_on_approval(self, tmp_path)` (method)
- L185 `test_revoke_removes_entry(self, tmp_path)` (method)
- L198 `test_revoke_unknown_returns_zero(self, tmp_path)` (method)
- L201 `test_tilde_path_approval_records_resolvable_mtime(self, tmp_path, monkeypatch)` (method) — If the command uses ~ the approval must still find the file.
- L216 `test_duplicate_approval_replaces_mtime(self, tmp_path)` (method) — Re-approving the same pair refreshes the approval timestamp.
- L247 `TestHooksAutoAcceptParsing` (class) — Regression guard: YAML-string values must not silently auto-accept.
- L255 `test_bool_true_accepts(self)` (method)
- L260 `test_bool_false_rejects(self)` (method)
- L265 `test_string_false_rejects(self)` (method)
- L271 `test_string_no_rejects(self)` (method)
- L276 `test_string_true_accepts(self)` (method)
- L281 `test_string_true_case_insensitive(self)` (method)
- L286 `test_string_yes_on_one_accept(self)` (method)
- L292 `test_missing_key_rejects(self)` (method)
- L297 `test_none_rejects(self)` (method)
- L302 `test_integer_ignored(self)` (method)
- L308 `test_cli_arg_overrides_config(self)` (method)
