---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_memory_tool.py

Symbols in `tests/tools/test_memory_tool.py`.

- L19 `TestMemorySchema` (class)
- L20 `test_discourages_diary_style_task_logs(self)` (method)
- L33 `TestScanMemoryContent` (class)
- L34 `test_clean_content_passes(self)` (method)
- L40 `test_prompt_injection_blocked(self)` (method)
- L51 `test_prompt_injection_multi_word_bypass_blocked(self)` (method) — Multi-word insertion between keywords should still match (commit 4ea29978 fix).
- L60 `test_role_hijack_blocked(self)` (method)
- L68 `test_system_override_blocked(self)` (method)
- L73 `test_bypass_restrictions_blocked(self)` (method)
- L78 `test_role_pretend_blocked(self)` (method)
- L83 `test_leak_system_prompt_blocked(self)` (method)
- L88 `test_remove_filters_blocked(self)` (method)
- L93 `test_fake_update_blocked(self)` (method)
- L98 `test_translate_execute_blocked(self)` (method)
- L103 `test_html_comment_injection_blocked(self)` (method)
- L108 `test_hidden_div_blocked(self)` (method)
- L113 `test_deception_hide_blocked(self)` (method)
- L120 `test_exfiltration_blocked(self)` (method)
- L131 `test_send_to_url_blocked(self)` (method)
- L136 `test_context_exfil_blocked(self)` (method)
- L146 `test_ssh_backdoor_blocked(self)` (method)
- L154 `test_agent_config_mod_blocked(self)` (method)
- L165 `test_hermes_config_mod_blocked(self)` (method)
- L175 `test_hardcoded_secret_blocked(self)` (method)
- L182 `test_invisible_unicode_blocked(self)` (method)
- L190 `test_invisible_unicode_directional_isolates_blocked(self)` (method) — Directional isolate characters (U+2066-U+2069) must be detected.
- L199 `test_invisible_unicode_math_operators_blocked(self)` (method) — Invisible math operators (U+2062-U+2064) must be detected.
- L210 `test_normal_preferences_pass(self)` (method) — Legitimate user preferences should not be blocked.
- L217 `test_context_exfil_no_false_positives(self)` (method) — Broad word 'context' alone should not trigger; only 'full/entire context' should.
- L224 `test_agent_config_mod_no_false_positives(self)` (method) — Merely mentioning config filenames should not trigger; only modify/write intent should.
- L231 `test_send_to_url_no_false_positives(self)` (method) — Non-URL 'send' patterns should not trigger.
- L236 `test_hardcoded_secret_no_false_positives(self)` (method) — Legitimate discussions about credentials should not trigger.
- L242 `test_role_hijack_no_false_positives(self)` (method) — Common 'you are now [state]' phrases must not trigger.
- L249 `test_hermes_config_mod_no_false_positives(self)` (method) — Merely mentioning hermes config files should not trigger; only modify intent should.
- L261 `store(tmp_path, monkeypatch)` (function) — Create a MemoryStore with temp storage.
- L269 `TestMemoryStoreAdd` (class)
- L270 `test_add_entry(self, store)` (method)
- L275 `test_add_to_user(self, store)` (method)
- L280 `test_add_empty_rejected(self, store)` (method)
- L284 `test_add_duplicate_rejected(self, store)` (method)
- L290 `test_add_exceeding_limit_rejected(self, store)` (method)
- L297 `test_add_injection_blocked(self, store)` (method)
- L303 `TestMemoryStoreReplace` (class)
- L304 `test_replace_entry(self, store)` (method)
- L311 `test_replace_no_match(self, store)` (method)
- L316 `test_replace_ambiguous_match(self, store)` (method)
- L323 `test_replace_empty_old_text_rejected(self, store)` (method)
- L327 `test_replace_empty_new_content_rejected(self, store)` (method)
- L332 `test_replace_injection_blocked(self, store)` (method)
- L338 `TestMemoryStoreRemove` (class)
- L339 `test_remove_entry(self, store)` (method)
- L345 `test_remove_no_match(self, store)` (method)
- L349 `test_remove_empty_old_text(self, store)` (method)
- L354 `TestMemoryStorePersistence` (class)
- L355 `test_save_and_load_roundtrip(self, tmp_path, monkeypatch)` (method)
- L368 `test_deduplication_on_load(self, tmp_path, monkeypatch)` (method)
- L379 `TestMemoryStoreSnapshot` (class)
- L380 `test_snapshot_frozen_at_load(self, store)` (method)
- L393 `test_empty_snapshot_returns_none(self, store)` (method)
- L401 `TestMemoryToolDispatcher` (class)
- L402 `test_no_store_returns_error(self)` (method)
- L407 `test_invalid_target(self, store)` (method)
- L411 `test_unknown_action(self, store)` (method)
- L415 `test_add_via_tool(self, store)` (method)
- L419 `test_replace_requires_old_text(self, store)` (method)
- L423 `test_remove_requires_old_text(self, store)` (method)
- L442 `TestExternalDriftGuard` (class) — Mutations must refuse to flush when on-disk content shows external drift.
- L445 `_plant_drift(self, store, target='memory')` (method) — Append free-form content (no § delimiters) past char_limit.
- L458 `test_replace_refuses_on_drift(self, store)` (method)
- L475 `test_add_refuses_on_drift(self, store)` (method)
- L486 `test_remove_refuses_on_drift(self, store)` (method)
- L497 `test_clean_file_does_not_trigger_drift(self, store)` (method) — A normally-written file (just below char_limit, §-delimited) is fine.
- L510 `test_error_message_points_at_remediation(self, store)` (method) — The error string must reference the backup AND remediation steps.
- L522 `test_drift_guard_also_protects_user_target(self, store)` (method) — USER.md gets the same guarantee as MEMORY.md.
- L532 `test_drift_backup_filename_is_unique_per_invocation(self, store)` (method) — Two drift refusals close together must not collide on bak.<ts>.
- L564 `TestLoadTimeSnapshotSanitization` (class)
- L565 `test_clean_entries_pass_through_snapshot(self, tmp_path, monkeypatch)` (method)
- L578 `test_poisoned_entry_blocked_in_snapshot_kept_in_live_state(self, tmp_path, monkeypatch)` (method)
- L603 `test_brainworm_payload_in_memory_blocked_at_load_time(self, tmp_path, monkeypatch)` (method) — The Brainworm payload, planted directly on disk, must not enter
- L624 `test_already_blocked_entry_passes_through(self, tmp_path, monkeypatch)` (method) — An entry already starting with [BLOCKED: ... ] (e.g. from a prior
