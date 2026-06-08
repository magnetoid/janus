---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_command_guards.py

Symbols in `tests/tools/test_command_guards.py`.

- L25 `_tirith_result(action='allow', findings=None, summary='')` (function)
- L36 `_clean_state()` (function) — Clear approval state and relevant env vars between tests.
- L59 `TestContainerSkip` (class)
- L60 `test_docker_skips_both(self)` (method)
- L64 `test_singularity_skips_both(self)` (method)
- L68 `test_modal_skips_both(self)` (method)
- L72 `test_daytona_skips_both(self)` (method)
- L81 `TestTirithAllowSafeCommand` (class)
- L83 `test_both_allow(self, mock_tirith)` (method)
- L89 `test_noninteractive_skips_external_scan(self, mock_tirith)` (method)
- L99 `TestTirithBlock` (class) — Tirith 'block' is now treated as an approvable warning (not a hard block).
- L110 `test_tirith_block_prompts_user(self, mock_tirith)` (method) — tirith block goes through approval flow (user gets prompted).
- L122 `test_tirith_block_plus_dangerous_prompts_combined(self, mock_tirith)` (method) — tirith block + dangerous pattern → combined approval prompt.
- L134 `TestTirithAllowDangerous` (class)
- L137 `test_dangerous_only_cli_deny(self, mock_tirith)` (method)
- L151 `TestTirithWarnSafe` (class)
- L156 `test_warn_cli_prompts_user(self, mock_tirith)` (method)
- L170 `test_warn_session_approved(self, mock_tirith)` (method)
- L181 `test_warn_non_interactive_auto_allow(self, mock_tirith)` (method)
- L191 `TestCombinedWarnings` (class)
- L197 `test_combined_cli_deny(self, mock_tirith)` (method)
- L211 `test_combined_cli_session_approves_both(self, mock_tirith)` (method)
- L225 `TestAlwaysVisibility` (class)
- L227 `test_dangerous_only_allows_permanent(self, mock_tirith)` (method)
- L241 `TestTirithImportError` (class)
- L242 `test_import_error_allows(self)` (method) — When tools.tirith_security can't be imported, treated as allow.
- L262 `TestWarnEmptyFindings` (class)
- L265 `test_warn_empty_findings_cli_prompts(self, mock_tirith)` (method)
- L281 `TestProgrammingErrorsPropagateFromWrapper` (class)
- L283 `test_attribute_error_propagates(self, mock_tirith)` (method) — Non-ImportError exceptions from tirith wrapper should propagate.
