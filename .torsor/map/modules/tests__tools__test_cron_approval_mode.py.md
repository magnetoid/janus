---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_cron_approval_mode.py

Symbols in `tests/tools/test_cron_approval_mode.py`.

- L15 `_clear_approval_state()` (function)
- L29 `TestCronApprovalModeParsing` (class)
- L30 `test_default_is_deny(self)` (method) — When no config is set, cron_mode defaults to 'deny'.
- L36 `test_explicit_deny(self)` (method)
- L41 `test_explicit_approve(self)` (method)
- L46 `test_off_maps_to_approve(self)` (method) — 'off' is an alias for 'approve' (matches --yolo semantics).
- L52 `test_allow_maps_to_approve(self)` (method)
- L57 `test_yes_maps_to_approve(self)` (method)
- L62 `test_case_insensitive(self)` (method)
- L67 `test_unknown_value_defaults_to_deny(self)` (method)
- L72 `test_config_load_failure_defaults_to_deny(self)` (method) — If config loading fails entirely, default to deny (safe).
- L78 `test_yaml_boolean_false_maps_to_deny(self)` (method) — YAML 1.1 parses bare 'off' as False. Ensure it maps to deny.
- L90 `TestCronDenyMode` (class) — When HERMES_CRON_SESSION is set and cron_mode=deny, dangerous commands are blocked.
- L93 `test_dangerous_command_blocked_in_cron_deny_mode(self, monkeypatch)` (method)
- L106 `test_safe_command_allowed_in_cron_deny_mode(self, monkeypatch)` (method) — Non-dangerous commands still work even with cron_mode=deny.
- L118 `test_multiple_dangerous_patterns_blocked(self, monkeypatch)` (method) — All dangerous patterns are blocked, not just rm.
- L141 `test_block_message_includes_description(self, monkeypatch)` (method) — The block message should mention what pattern was matched.
- L156 `TestCronApproveMode` (class) — When HERMES_CRON_SESSION is set and cron_mode=approve, dangerous commands pass through.
- L159 `test_dangerous_command_allowed_in_cron_approve_mode(self, monkeypatch)` (method)
- L175 `TestCronDenyModeAllGuards` (class) — The combined guard function also respects cron_mode.
- L178 `test_dangerous_command_blocked_in_combined_guard(self, monkeypatch)` (method)
- L191 `test_safe_command_allowed_in_combined_guard(self, monkeypatch)` (method)
- L203 `test_combined_guard_approve_mode(self, monkeypatch)` (method)
- L220 `TestCronModeInteractions` (class) — Cron mode should NOT interfere with other approval bypass mechanisms.
- L223 `test_container_env_still_auto_approves(self, monkeypatch)` (method) — Docker/sandbox environments bypass approvals regardless of cron_mode.
- L235 `test_yolo_overrides_cron_deny(self, monkeypatch)` (method) — --yolo still bypasses cron_mode=deny for dangerous (non-hardline) commands.
- L259 `test_non_cron_non_interactive_still_auto_approves(self, monkeypatch)` (method) — Non-cron, non-interactive sessions (e.g. scripted usage) still auto-approve.
- L270 `TestCronWithGatewayOrigin` (class) — Cron jobs originating from a gateway platform must NOT be treated as gateway.
- L281 `test_cron_with_telegram_origin_uses_cron_mode_not_gateway(self, monkeypatch)` (method) — Cron + contextvar platform=telegram + cron_mode=deny → BLOCKED, not pending.
- L303 `test_cron_with_telegram_origin_approve_mode_allows(self, monkeypatch)` (method) — Cron + contextvar platform=telegram + cron_mode=approve → allowed via cron path.
- L323 `test_cron_with_telegram_origin_combined_guard_uses_cron_mode(self, monkeypatch)` (method) — check_all_command_guards must also honor cron_mode over gateway classification.
