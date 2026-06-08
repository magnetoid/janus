---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/plugins/memory/test_mem0_v2.py

Symbols in `tests/plugins/memory/test_mem0_v2.py`.

- L15 `FakeClientV2` (class) — Fake Mem0 client that returns v2-style dict responses and captures call kwargs.
- L18 `__init__(self, search_results=None, all_results=None)` (method)
- L25 `search(self, **kwargs)` (method)
- L29 `get_all(self, **kwargs)` (method)
- L33 `add(self, messages, **kwargs)` (method)
- L42 `TestMem0FiltersV2` (class) — All API calls must use filters={} instead of bare user_id= kwargs.
- L45 `_make_provider(self, monkeypatch, client)` (method)
- L53 `test_search_uses_filters(self, monkeypatch)` (method)
- L66 `test_profile_uses_filters(self, monkeypatch)` (method)
- L75 `test_prefetch_uses_filters(self, monkeypatch)` (method)
- L86 `test_sync_turn_uses_write_filters(self, monkeypatch)` (method)
- L98 `test_conclude_uses_write_filters(self, monkeypatch)` (method)
- L110 `test_read_filters_no_agent_id(self)` (method) — Read filters should use user_id only — cross-session recall across agents.
- L117 `test_write_filters_include_agent_id(self)` (method) — Write filters should include agent_id for attribution.
- L130 `TestMem0ResponseUnwrapping` (class) — API v2 returns {"results": [...]} dicts; we must extract the list.
- L133 `_make_provider(self, monkeypatch, client)` (method)
- L139 `test_profile_dict_response(self, monkeypatch)` (method)
- L149 `test_profile_list_response_backward_compat(self, monkeypatch)` (method) — Old API returned bare lists — still works.
- L158 `test_search_dict_response(self, monkeypatch)` (method)
- L171 `test_search_list_response_backward_compat(self, monkeypatch)` (method) — Old API returned bare lists — still works.
- L181 `test_unwrap_results_edge_cases(self)` (method) — _unwrap_results handles all shapes gracefully.
- L189 `test_prefetch_dict_response(self, monkeypatch)` (method)
- L210 `test_save_config_sets_owner_only_permissions(tmp_path)` (function) — mem0.json must be written with 0o600 so API key is not world-readable.
- L220 `TestMem0Defaults` (class) — Ensure we don't break existing users' defaults.
- L223 `test_default_user_id_hermes_user(self, monkeypatch, tmp_path)` (method)
- L233 `test_default_agent_id_hermes(self, monkeypatch, tmp_path)` (method)
