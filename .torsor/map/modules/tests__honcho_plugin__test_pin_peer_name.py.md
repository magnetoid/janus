---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/honcho_plugin/test_pin_peer_name.py

Symbols in `tests/honcho_plugin/test_pin_peer_name.py`.

- L31 `TestPinPeerNameConfigParsing` (class)
- L32 `test_default_is_false(self)` (method) — Default preserves existing behaviour — multi-user bots unaffected.
- L37 `test_root_level_true(self, tmp_path, monkeypatch)` (method)
- L50 `test_host_block_true(self, tmp_path, monkeypatch)` (method) — Host-level flag works the same as root-level.
- L65 `test_host_block_overrides_root(self, tmp_path, monkeypatch)` (method) — Host block wins over root — matches how every other flag behaves.
- L84 `test_explicit_false_parses(self, tmp_path, monkeypatch)` (method)
- L97 `TestRuntimePeerMappingConfigParsing` (class)
- L98 `test_defaults_are_empty(self)` (method)
- L103 `test_root_level_aliases_and_prefix_parse(self, tmp_path)` (method)
- L121 `test_host_aliases_override_root_aliases_as_whole_map(self, tmp_path)` (method)
- L137 `test_host_empty_aliases_disable_root_aliases(self, tmp_path)` (method)
- L153 `test_host_empty_prefix_disables_root_prefix(self, tmp_path)` (method)
- L169 `test_malformed_alias_config_is_ignored(self, tmp_path)` (method)
- L186 `_patch_manager_for_resolution_test(mgr: HonchoSessionManager)` (function) — Stub out the Honcho client so ``get_or_create`` doesn't try to talk
- L198 `TestPeerResolutionOrder` (class) — Matrix of (runtime_id, pin_peer_name, peer_name) → expected user_peer_id.
- L201 `_config(self, *, peer_name: str | None, pin_peer_name: bool, user_peer_aliases: dict[str, str] | None=None, runtime_peer_prefix: str='', session_peer_prefix: bool=False)` (method)
- L223 `test_runtime_wins_when_pin_is_false(self)` (method) — Regression guard: default behaviour must stay unchanged.
- L241 `test_alias_wins_for_known_runtime_id(self)` (method) — Known platform IDs can preserve an existing stable Honcho peer.
- L258 `test_unknown_runtime_id_uses_prefix(self)` (method) — Unknown gateway users stay isolated but become platform-scoped.
- L274 `test_prefixed_runtime_id_hashes_when_sanitization_is_lossy(self)` (method) — Generated prefixed IDs avoid merges caused by lossy sanitization.
- L292 `test_prefixed_runtime_id_hashes_when_it_collides_with_peer_name(self)` (method) — Unknown generated peers should not silently merge into peerName.
- L310 `test_prefixed_runtime_id_hashes_when_it_collides_with_alias_target(self)` (method) — Unknown generated peers should not silently merge into alias targets.
- L329 `test_prefixed_runtime_id_extends_hash_when_short_hash_collides(self)` (method)
- L350 `test_alias_value_is_sanitized_after_selection(self)` (method)
- L365 `test_alias_keys_match_raw_runtime_id_before_sanitization(self)` (method) — Alias selection is exact on platform IDs before Honcho ID cleanup.
- L384 `test_session_peer_prefix_is_orthogonal_to_runtime_peer_prefix(self)` (method) — sessionPeerPrefix scopes session IDs; runtimePeerPrefix scopes user peers.
- L402 `test_config_wins_when_pin_is_true(self)` (method) — With pin enabled, configured peer_name beats runtime ID.
- L423 `test_pin_noop_when_peer_name_missing(self)` (method) — Safety: pinPeerName alone (no peer_name) must not silently drop
- L442 `test_pin_noop_without_peer_name_or_mapping_preserves_runtime(self)` (method)
- L453 `test_alt_runtime_id_can_match_alias_without_changing_raw_fallback(self)` (method) — Stable alternate IDs can map known users while primary ID fallback stays unchanged.
- L471 `test_alt_runtime_id_does_not_replace_primary_prefix_fallback(self)` (method)
- L488 `test_runtime_missing_falls_back_to_peer_name(self)` (method) — CLI-mode (no gateway runtime identity) uses config peer_name —
- L501 `test_everything_missing_falls_back_to_session_key(self)` (method) — Deepest fallback: no runtime identity, no peer_name, no pin.
- L515 `test_pin_does_not_affect_assistant_peer(self)` (method) — The flag only pins the USER peer — the assistant peer continues
- L538 `TestCrossPlatformMemoryUnification` (class) — The same physical user talking to Hermes via Telegram AND Discord
- L543 `_config_pinned(self)` (method)
- L552 `test_telegram_and_discord_collapse_to_one_peer_when_pinned(self)` (method) — Single-user deployment: Telegram UID and Discord snowflake
- L581 `test_multiuser_default_keeps_platforms_separate(self)` (method) — Negative control: with pinPeerName=false (the default), two
- L612 `TestPinUserPeerAlias` (class) — ``pinUserPeer`` and ``pinPeerName`` both resolve to the same internal
- L618 `test_root_pinUserPeer_true_pins(self, tmp_path)` (method)
- L630 `test_host_pinUserPeer_wins_over_root_pinPeerName(self, tmp_path)` (method)
- L643 `test_host_pinUserPeer_false_disables_root_pinPeerName(self, tmp_path)` (method)
- L659 `test_pinPeerName_still_works_unchanged(self, tmp_path)` (method)
- L672 `TestPinTransition` (class) — Behavior when honcho.json flips ``pinPeerName`` true → false.
- L682 `_pinned(self)` (method)
- L691 `_unpinned(self)` (method)
- L700 `test_fresh_manager_after_flip_resolves_to_runtime(self)` (method)
- L722 `test_cached_session_survives_config_flip_in_same_manager(self)` (method)
- L740 `test_cache_busting_signature_reflects_pin_peer_name(self, tmp_path, monkeypatch)` (method) — Gateway agent cache must bust when honcho.json's pinPeerName flips.
- L755 `test_cache_busting_signature_reflects_user_peer_aliases(self, tmp_path, monkeypatch)` (method)
- L773 `test_cache_busting_signature_reflects_runtime_peer_prefix(self, tmp_path, monkeypatch)` (method)
- L791 `test_cache_busting_signature_reflects_ai_peer(self, tmp_path, monkeypatch)` (method) — Editing ``aiPeer`` mid-flight must invalidate the cached agent.
- L820 `TestProfilePeerUniqueness` (class) — Each Hermes profile can pin to its own unique peerName.
- L829 `_pinned_to(self, name: str)` (method)
- L838 `test_two_profiles_pinned_to_different_peer_names_resolve_distinctly(self)` (method)
- L862 `test_host_peer_name_overrides_root_when_pinned(self, tmp_path, monkeypatch)` (method) — Host-level peerName wins so each profile can pin uniquely while
