---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_mcp_oauth_metadata.py

Symbols in `tests/tools/test_mcp_oauth_metadata.py`.

- L33 `_make_metadata(token_endpoint: str='https://auth.example.com/oauth/token')` (function)
- L49 `TestMetadataStorage` (class)
- L50 `test_save_and_load_roundtrip(self, tmp_path, monkeypatch)` (method)
- L65 `test_load_missing_returns_none(self, tmp_path, monkeypatch)` (method)
- L70 `test_load_corrupt_returns_none(self, tmp_path, monkeypatch)` (method)
- L81 `test_remove_deletes_meta_file(self, tmp_path, monkeypatch)` (method)
- L97 `_manager_provider_with_context(storage: HermesTokenStorage, **context_attrs)` (function) — Build an uninitialized manager provider with a mocked context.
- L117 `TestManagerOAuthProviderMetadata` (class)
- L118 `test_initialize_restores_metadata_from_disk(self, tmp_path, monkeypatch)` (method) — Cold-load: if we have no in-memory metadata but disk has some, restore it.
- L134 `test_initialize_skips_restore_when_in_memory_present(self, tmp_path, monkeypatch)` (method) — If SDK already has metadata in memory, don't overwrite from disk.
- L151 `test_persist_metadata_if_changed_writes_on_first_discover(self, tmp_path, monkeypatch)` (method) — When nothing on disk yet, persist what the SDK discovered in-memory.
- L166 `test_persist_metadata_noop_when_unchanged(self, tmp_path, monkeypatch)` (method) — No-op write when disk already matches in-memory metadata.
- L181 `test_async_auth_flow_persists_on_completion(self, tmp_path, monkeypatch)` (method) — End-to-end: running the wrapped auth_flow persists discovered metadata.
