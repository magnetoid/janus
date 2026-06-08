---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/gateway/test_agent_cache.py

Symbols in `tests/gateway/test_agent_cache.py`.

- L17 `_make_runner()` (function) — Create a minimal GatewayRunner with just the cache infrastructure.
- L27 `TestAgentConfigSignature` (class) — Config signature produces stable, distinct keys.
- L30 `test_same_config_same_signature(self)` (method)
- L39 `test_model_change_different_signature(self)` (method)
- L48 `test_same_token_prefix_different_full_token_changes_signature(self)` (method) — Tokens sharing a JWT-style prefix must not collide.
- L70 `test_provider_change_different_signature(self)` (method)
- L79 `test_toolset_change_different_signature(self)` (method)
- L87 `test_reasoning_not_in_signature(self)` (method) — Reasoning config is set per-message, not part of the signature.
- L102 `test_cache_keys_default_omitted_matches_empty(self)` (method) — Omitted cache_keys must produce the same signature as empty {}.
- L112 `test_context_length_change_busts_cache(self)` (method) — Editing model.context_length in config must produce a new signature.
- L127 `test_max_tokens_change_busts_cache(self)` (method) — Editing model.max_tokens in config must produce a new signature.
- L142 `test_compression_threshold_change_busts_cache(self)` (method)
- L156 `test_compression_enabled_toggle_busts_cache(self)` (method)
- L170 `test_cache_keys_key_order_does_not_matter(self)` (method) — Signature must be stable regardless of dict key insertion order.
- L185 `test_tool_registry_generation_change_busts_cache(self)` (method) — MCP reloads mutate the tool registry, so cached agents must rebuild.
- L202 `TestExtractCacheBustingConfig` (class) — Verify _extract_cache_busting_config pulls the documented subset of
- L206 `test_reads_model_context_length(self)` (method)
- L221 `test_reads_compression_subkeys(self)` (method)
- L240 `test_missing_keys_yield_none(self)` (method) — Absent config keys must produce None values (still contribute to signature).
- L250 `test_non_dict_section_treated_as_missing(self)` (method)
- L261 `test_none_config_is_safe(self)` (method)
- L269 `test_extract_includes_live_tool_registry_generation(self, monkeypatch)` (method)
- L280 `test_skips_honcho_config_read_when_provider_is_not_honcho(self, monkeypatch)` (method) — Non-Honcho gateways must not read/parse honcho.json on every message.
- L299 `test_reads_honcho_config_only_when_provider_is_honcho(self, monkeypatch)` (method)
- L322 `test_memory_provider_change_busts_signature(self, monkeypatch)` (method) — Switching memory.provider must itself change the cache-busting
- L343 `test_honcho_cache_busting_config_memoized_by_mtime(self, monkeypatch, tmp_path)` (method) — Repeated Honcho extraction for unchanged honcho.json should reuse parse result.
- L384 `test_full_round_trip_busts_cache_on_real_edit(self)` (method) — End-to-end: simulate a config edit on main and verify the
- L413 `TestAgentCacheLifecycle` (class) — End-to-end cache behavior with real AIAgent construction.
- L416 `test_cache_hit_returns_same_agent(self)` (method) — Second message with same config reuses the cached agent instance.
- L443 `test_cache_miss_on_model_change(self)` (method) — Model change produces different signature → cache miss.
- L470 `test_evict_on_session_reset(self)` (method) — _evict_cached_agent removes the entry.
- L491 `test_evict_does_not_affect_other_sessions(self)` (method) — Evicting one session leaves other sessions cached.
- L504 `test_reasoning_config_updates_in_place(self)` (method) — Reasoning config can be set on a cached agent without eviction.
- L527 `test_system_prompt_frozen_across_cache_reuse(self)` (method) — The cached agent's system prompt stays identical across turns.
- L546 `test_callbacks_update_without_cache_eviction(self)` (method) — Per-message callbacks can be set on cached agent.
- L574 `TestAgentCacheBoundedGrowth` (class) — LRU cap and idle-TTL eviction prevent unbounded cache growth.
- L577 `_bounded_runner(self)` (method) — Runner with an OrderedDict cache (matches real gateway init).
- L587 `_fake_agent(self, last_activity: float | None=None)` (method) — Lightweight stand-in; real AIAgent is heavy to construct.
- L597 `test_cap_evicts_lru_when_exceeded(self, monkeypatch)` (method) — Inserting past _AGENT_CACHE_MAX_SIZE pops the oldest entry.
- L617 `test_cap_respects_move_to_end(self, monkeypatch)` (method) — Entries refreshed via move_to_end are NOT evicted as 'oldest'.
- L639 `test_cap_triggers_cleanup_thread(self, monkeypatch)` (method) — Evicted agent has release_clients() called for it (soft cleanup).
- L676 `test_idle_ttl_sweep_evicts_stale_agents(self, monkeypatch)` (method) — _sweep_idle_cached_agents removes agents idle past the TTL.
- L695 `test_idle_sweep_skips_agents_without_activity_ts(self, monkeypatch)` (method) — Agents missing _last_activity_ts are left alone (defensive).
- L709 `test_plain_dict_cache_is_tolerated(self)` (method) — Test fixtures using plain {} don't crash _enforce_agent_cache_cap.
- L726 `test_main_lookup_updates_lru_order(self, monkeypatch)` (method) — Cache hit via the main-lookup path refreshes LRU position.
- L748 `TestAgentCacheActiveSafety` (class) — Safety: eviction must not tear down agents currently mid-turn.
- L758 `_runner(self)` (method)
- L768 `_fake_agent(self, idle_seconds: float=0.0)` (method)
- L774 `test_cap_skips_active_lru_entry(self, monkeypatch)` (method) — Active LRU entry is skipped; cache stays over cap rather than
- L811 `test_cap_evicts_when_multiple_excess_and_some_inactive(self, monkeypatch)` (method) — Mixed active/idle in the LRU excess window: only the idle ones go.
- L846 `test_cap_leaves_cache_over_limit_if_all_active(self, monkeypatch, caplog)` (method) — If every over-cap entry is mid-turn, the cache stays over cap.
- L882 `test_cap_pending_sentinel_does_not_block_eviction(self, monkeypatch)` (method) — _AGENT_PENDING_SENTINEL in _running_agents is treated as 'not active'.
- L909 `test_idle_sweep_skips_active_agent(self, monkeypatch)` (method) — Idle-TTL sweep must not tear down an active agent even if 'stale'.
- L927 `test_eviction_does_not_close_active_agent_client(self, monkeypatch)` (method) — Live test: evicting an active agent does NOT null its .client.
- L971 `TestAgentCacheSpilloverLive` (class) — Live E2E: fill cache with real AIAgent instances and stress it.
- L974 `_runner(self)` (method)
- L984 `_real_agent(self)` (method) — A genuine AIAgent; no API calls are made during these tests.
- L995 `test_fill_to_cap_then_spillover(self, monkeypatch)` (method) — Fill to cap with real agents, insert one more, oldest evicted.
- L1028 `test_spillover_all_active_keeps_cache_over_cap(self, monkeypatch, caplog)` (method) — Every slot active: cache goes over cap, no one gets torn down.
- L1062 `test_evicted_session_next_turn_gets_fresh_agent(self, monkeypatch)` (method) — After eviction, the same session_key can insert a fresh agent.
- L1108 `TestAgentCacheIdleResume` (class) — End-to-end: idle-TTL-evicted session resumes cleanly with task state.
- L1121 `_runner(self)` (method)
- L1131 `test_release_clients_does_not_touch_process_registry(self, monkeypatch)` (method) — release_clients must not call process_registry.kill_all for task_id.
- L1162 `test_release_clients_does_not_touch_terminal_or_browser(self, monkeypatch)` (method) — release_clients must not call cleanup_vm or cleanup_browser.
- L1201 `test_release_clients_closes_llm_client(self)` (method) — release_clients IS expected to close the OpenAI/httpx client.
- L1219 `test_close_vs_release_full_teardown_difference(self, monkeypatch)` (method) — close() tears down task state; release_clients() does not.
- L1266 `test_idle_evicted_session_rebuild_inherits_task_id(self, monkeypatch)` (method) — After idle-TTL eviction, a fresh agent with the same session_id
- L1325 `TestCachedAgentInactivityReset` (class) — Inactivity-clock reset must be gated on _interrupt_depth == 0.
- L1336 `_fake_agent(self, stale_seconds: float=1800.0)` (method)
- L1343 `test_fresh_turn_resets_idle_clock(self)` (method) — interrupt_depth=0: clock resets so a post-idle turn gets a
- L1362 `test_fresh_turn_resets_desc(self)` (method) — interrupt_depth=0: description is updated to reflect the new turn.
- L1374 `test_interrupt_turn_preserves_idle_clock(self)` (method) — interrupt_depth=1: clock preserved so accumulated stuck-turn
- L1389 `test_interrupt_turn_preserves_desc(self)` (method) — interrupt_depth=1: desc preserved — it is semantically paired with ts.
- L1402 `test_deep_interrupt_recursion_preserves_idle_clock(self)` (method) — interrupt_depth=MAX-1: clock still preserved at any non-zero depth.
- L1413 `test_api_call_count_reset_regardless_of_depth(self)` (method) — _api_call_count is always reset to 0 for the new turn, at any depth.
- L1428 `test_watchdog_accumulation_across_recursive_turns(self)` (method) — Scenario: stuck turn + user interrupt → recursive turn.
- L1451 `TestAgentConfigSignatureUserId` (class) — Shared-thread cache must not reuse an agent across users.
- L1465 `test_signature_changes_with_user_id(self)` (method)
- L1476 `test_signature_stable_with_same_user_id(self)` (method)
- L1487 `test_signature_changes_with_user_id_alt(self)` (method)
- L1500 `test_signature_omits_user_id_when_absent(self)` (method) — Default-None user_id must not change signatures vs unset call.
