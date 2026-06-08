---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/credential_pool.py

Symbols in `agent/credential_pool.py`.

- L43 `_load_config_safe()` (function) — Load config.yaml, returning None on any error.
- L129 `PooledCredential` (class)
- L154 `__post_init__(self)` (method)
- L158 `__getattr__(self, name: str)` (method)
- L164 `from_dict(cls, provider: str, payload: Dict[str, Any])` (method)
- L180 `to_dict(self)` (method)
- L202 `runtime_api_key(self)` (method)
- L224 `runtime_base_url(self)` (method)
- L230 `label_from_token(token: str, fallback: str)` (function)
- L239 `_next_priority(entries: List[PooledCredential])` (function)
- L243 `_is_manual_source(source: str)` (function)
- L248 `_exhausted_ttl(error_code: Optional[int])` (function) — Return cooldown seconds based on the HTTP status that caused exhaustion.
- L257 `_parse_absolute_timestamp(value: Any)` (function) — Best-effort parse for provider reset timestamps.
- L287 `_extract_retry_delay_seconds(message: str)` (function)
- L310 `_normalize_error_context(error_context: Optional[Dict[str, Any]])` (function)
- L335 `_exhausted_until(entry: PooledCredential)` (function)
- L346 `_normalize_custom_pool_name(name: str)` (function) — Normalize a custom provider name for use as a pool key suffix.
- L351 `_iter_custom_providers(config: Optional[dict]=None)` (function) — Yield (normalized_name, entry_dict) for each valid custom_providers entry.
- L377 `get_custom_provider_pool_key(base_url: str, provider_name: Optional[str]=None)` (function) — Look up the custom_providers list in config.yaml and return 'custom:<name>' for a matching base_url.
- L407 `list_custom_pool_providers()` (function) — Return all 'custom:*' pool keys that have entries in auth.json.
- L418 `_get_custom_provider_config(pool_key: str)` (function) — Return the custom_providers config entry matching a pool key like 'custom:together.ai'.
- L429 `get_pool_strategy(provider: str)` (function) — Return the configured selection strategy for a provider.
- L448 `CredentialPool` (class)
- L449 `__init__(self, provider: str, entries: List[PooledCredential])` (method)
- L458 `has_credentials(self)` (method)
- L461 `has_available(self)` (method) — True if at least one entry is not currently in exhaustion cooldown.
- L465 `entries(self)` (method)
- L468 `current(self)` (method)
- L473 `_replace_entry(self, old: PooledCredential, new: PooledCredential)` (method) — Swap an entry in-place by id, preserving sort order.
- L480 `_persist(self)` (method)
- L486 `_is_terminal_auth_failure(self, status_code: Optional[int], normalized_error: Dict[str, Any])` (method) — Detect upstream-permanent OAuth failures that won't recover on TTL.
- L509 `_mark_exhausted(self, entry: PooledCredential, status_code: Optional[int], error_context: Optional[Dict[str, Any]]=None)` (method)
- L540 `_sync_anthropic_entry_from_credentials_file(self, entry: PooledCredential)` (method) — Sync a claude_code pool entry from ~/.claude/.credentials.json if tokens differ.
- L577 `_sync_codex_entry_from_auth_store(self, entry: PooledCredential)` (method) — Sync a Codex device_code pool entry from auth.json if tokens differ.
- L641 `_sync_xai_oauth_entry_from_auth_store(self, entry: PooledCredential)` (method) — Sync an xAI OAuth pool entry from auth.json if tokens differ.
- L699 `_sync_nous_entry_from_auth_store(self, entry: PooledCredential)` (method) — Sync a Nous pool entry from auth.json if tokens differ.
- L771 `_sync_device_code_entry_to_auth_store(self, entry: PooledCredential)` (method) — Write refreshed pool entry tokens back to auth.json providers.
- L859 `_refresh_entry(self, entry: PooledCredential, *, force: bool)` (method)
- L1198 `_entry_needs_refresh(self, entry: PooledCredential)` (method)
- L1222 `select(self)` (method)
- L1226 `_available_entries(self, *, clear_expired: bool=False, refresh: bool=False)` (method) — Return entries not currently in exhaustion cooldown.
- L1341 `_select_unlocked(self)` (method)
- L1374 `peek(self)` (method)
- L1381 `mark_exhausted_and_rotate(self, *, status_code: Optional[int], error_context: Optional[Dict[str, Any]]=None, api_key_hint: Optional[str]=None)` (method)
- L1427 `acquire_lease(self, credential_id: Optional[str]=None)` (method) — Acquire a soft lease on a credential.
- L1458 `release_lease(self, credential_id: str)` (method) — Release a previously acquired credential lease.
- L1467 `try_refresh_current(self)` (method)
- L1471 `_try_refresh_current_unlocked(self)` (method)
- L1480 `reset_statuses(self)` (method)
- L1504 `remove_index(self, index: int)` (method)
- L1517 `resolve_target(self, target: Any)` (method)
- L1542 `add_entry(self, entry: PooledCredential)` (method)
- L1549 `_upsert_entry(entries: List[PooledCredential], provider: str, source: str, payload: Dict[str, Any])` (function)
- L1590 `_normalize_pool_priorities(provider: str, entries: List[PooledCredential])` (function)
- L1624 `_seed_from_singletons(provider: str, entries: List[PooledCredential])` (function)
- L1944 `_seed_from_env(provider: str, entries: List[PooledCredential])` (function)
- L2063 `_prune_stale_seeded_entries(entries: List[PooledCredential], active_sources: Set[str])` (function)
- L2083 `_seed_custom_pool(pool_key: str, entries: List[PooledCredential])` (function) — Seed a custom endpoint pool from custom_providers config and model config.
- L2156 `load_pool(provider: str)` (function)
