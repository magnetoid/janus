---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_skills_hub_clawhub.py

Symbols in `tests/tools/test_skills_hub_clawhub.py`.

- L9 `_MockResponse` (class)
- L10 `__init__(self, status_code=200, json_data=None, text='', headers=None)` (method)
- L16 `json(self)` (method)
- L20 `TestClawHubSource` (class)
- L21 `setUp(self)` (method)
- L28 `tearDown(self)` (method)
- L36 `test_search_uses_listing_endpoint_as_fallback(self, mock_get, _mock_load_catalog, _mock_read_cache, _mock_write_cache)` (method)
- L80 `test_search_falls_back_to_exact_slug_when_search_results_are_irrelevant(self, mock_get, _mock_load_catalog, _mock_read_cache, _mock_write_cache)` (method)
- L122 `test_search_repairs_poisoned_cache_with_exact_slug_lookup(self, mock_get)` (method)
- L165 `test_search_matches_space_separated_query_to_hyphenated_slug(self, _mock_exact_slug)` (method)
- L174 `test_inspect_maps_display_name_and_summary(self, mock_get)` (method)
- L193 `test_inspect_handles_nested_skill_payload(self, mock_get)` (method)
- L216 `test_fetch_resolves_latest_version_and_downloads_raw_files(self, mock_get)` (method)
- L251 `test_fetch_falls_back_to_versions_list(self, mock_get)` (method)
- L270 `test_fetch_blocks_private_raw_url(self, mock_get, mock_safe, _mock_policy)` (method)
- L304 `test_search_empty_query_paginates_full_catalog(self, mock_get, _mock_read_cache, _mock_write_cache)` (method) — Empty query must walk the cursor-paginated catalog.
