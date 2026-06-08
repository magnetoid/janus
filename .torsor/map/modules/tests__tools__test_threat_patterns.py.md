---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_threat_patterns.py

Symbols in `tests/tools/test_threat_patterns.py`.

- L22 `TestScopes` (class)
- L23 `test_unknown_scope_raises(self)` (method)
- L27 `test_empty_content_returns_empty(self)` (method)
- L31 `test_all_scope_narrower_than_context(self)` (method)
- L38 `test_context_scope_narrower_than_strict(self)` (method)
- L48 `test_all_patterns_present_in_strict(self)` (method)
- L69 `TestBrainwormPayload` (class) — Anchor regression — the real Brainworm payload must trigger
- L74 `test_brainworm_caught_at_context_scope(self)` (method)
- L85 `test_brainworm_caught_at_strict_scope(self)` (method)
- L91 `test_brainworm_passes_at_all_scope(self)` (method)
- L110 `TestC2Patterns` (class)
- L111 `test_node_registration(self)` (method)
- L116 `test_heartbeat_to(self)` (method)
- L122 `test_pull_tasking(self)` (method)
- L127 `test_connect_to_the_network(self)` (method)
- L132 `test_forced_register_verb(self)` (method)
- L137 `test_anti_forensic_oneliner(self)` (method)
- L142 `test_anti_forensic_disk(self)` (method)
- L147 `test_env_var_unset_agent(self)` (method)
- L152 `test_identity_override(self)` (method)
- L157 `test_known_c2_framework_names(self)` (method)
- L164 `test_c2_explicit(self)` (method)
- L178 `TestFalsePositives` (class) — Patterns we explicitly DID NOT include because they fire on
- L184 `test_you_are_obligated_does_not_trip_alone(self)` (method)
- L192 `test_you_must_alone_does_not_trip(self)` (method)
- L199 `test_legitimate_node_mention_about_distributed_systems(self)` (method)
- L217 `test_do_not_respond_alone_does_not_trip(self)` (method)
- L225 `test_security_research_text_passes_at_all_scope(self)` (method)
- L241 `TestClassicInjection` (class) — Confirm the prompt-injection / exfiltration patterns we INHERITED
- L246 `test_ignore_previous_instructions(self)` (method)
- L251 `test_disregard_rules(self)` (method)
- L256 `test_exfil_curl_with_api_key(self)` (method)
- L261 `test_read_dotenv(self)` (method)
- L266 `test_html_comment_injection(self)` (method)
- L271 `test_hidden_div(self)` (method)
- L276 `test_translate_execute(self)` (method)
- L287 `TestInvisibleUnicode` (class)
- L288 `test_zero_width_space_detected(self)` (method)
- L292 `test_directional_isolate_detected(self)` (method)
- L296 `test_invisible_chars_set_is_frozenset(self)` (method)
- L307 `TestFirstThreatMessage` (class)
- L308 `test_returns_none_on_clean_content(self)` (method)
- L311 `test_returns_message_for_pattern(self)` (method)
- L317 `test_returns_message_for_invisible_unicode(self)` (method)
