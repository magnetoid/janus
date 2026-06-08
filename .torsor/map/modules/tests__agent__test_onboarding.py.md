---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_onboarding.py

Symbols in `tests/agent/test_onboarding.py`.

- L22 `TestIsSeen` (class)
- L23 `test_empty_config_unseen(self)` (method)
- L26 `test_missing_onboarding_unseen(self)` (method)
- L29 `test_onboarding_not_dict_unseen(self)` (method)
- L32 `test_seen_dict_missing_flag(self)` (method)
- L35 `test_seen_flag_true(self)` (method)
- L39 `test_seen_flag_falsy(self)` (method)
- L43 `test_other_flags_isolated(self)` (method)
- L48 `TestMarkSeen` (class)
- L49 `test_creates_missing_file_and_sets_flag(self, tmp_path)` (method)
- L56 `test_preserves_other_config(self, tmp_path)` (method)
- L70 `test_preserves_other_seen_flags(self, tmp_path)` (method)
- L82 `test_idempotent(self, tmp_path)` (method)
- L94 `test_handles_non_dict_onboarding(self, tmp_path)` (method)
- L102 `test_handles_non_dict_seen(self, tmp_path)` (method)
- L111 `TestHintMessages` (class)
- L112 `test_busy_input_hint_gateway_interrupt(self)` (method)
- L117 `test_busy_input_hint_gateway_queue(self)` (method)
- L122 `test_busy_input_hint_gateway_steer(self)` (method)
- L128 `test_busy_input_hint_cli_interrupt(self)` (method)
- L132 `test_busy_input_hint_cli_queue(self)` (method)
- L136 `test_busy_input_hint_cli_steer(self)` (method)
- L142 `test_tool_progress_hints_mention_verbose(self)` (method)
- L146 `test_hints_are_not_empty(self)` (method)
- L160 `TestRoundTrip` (class) — After mark_seen, is_seen on the re-loaded config must return True.
- L163 `test_mark_then_is_seen(self, tmp_path)` (method)
- L172 `test_mark_both_flags_independently(self, tmp_path)` (method)
- L188 `TestDetectOpenclawResidue` (class)
- L189 `test_returns_true_when_openclaw_dir_present(self, tmp_path)` (method)
- L193 `test_returns_false_when_absent(self, tmp_path)` (method)
- L196 `test_returns_false_when_path_is_a_file(self, tmp_path)` (method)
- L201 `test_default_home_does_not_crash(self)` (method)
- L206 `TestOpenclawResidueHint` (class)
- L207 `test_hint_mentions_migrate_command(self)` (method)
- L213 `test_hint_mentions_cleanup_command(self)` (method)
- L217 `test_hint_warns_cleanup_breaks_openclaw(self)` (method)
- L223 `test_hint_not_empty(self)` (method)
- L227 `TestOpenclawResidueSeenFlag` (class)
- L228 `test_flag_independent_of_other_flags(self, tmp_path)` (method)
- L234 `test_flag_round_trips(self, tmp_path)` (method)
- L241 `TestProfileBuildMode` (class)
- L242 `test_default_is_ask(self)` (method)
- L249 `test_off_disables(self)` (method)
- L255 `test_unknown_value_falls_back_to_ask(self)` (method)
- L260 `test_non_mapping_config_safe(self)` (method)
- L267 `TestProfileBuildDirective` (class)
- L268 `test_directive_is_opt_in_and_consent_gated(self)` (method)
- L283 `test_directive_mentions_first_message(self)` (method)
- L289 `TestProfileBuildSeenFlag` (class)
- L290 `test_flag_round_trips(self, tmp_path)` (method)
- L298 `test_flag_independent_of_busy_input(self, tmp_path)` (method)
- L307 `TestProfileBuildConfigDefault` (class)
- L308 `test_default_config_carries_ask(self)` (method)
