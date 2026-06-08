---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_skills_hub_browse_sh.py

Symbols in `tests/tools/test_skills_hub_browse_sh.py`.

- L41 `_MockResponse` (class)
- L42 `__init__(self, status_code=200, json_data=None, text='', headers=None)` (method)
- L48 `json(self)` (method)
- L52 `TestBrowseShSource` (class)
- L53 `setUp(self)` (method)
- L56 `test_source_id(self)` (method)
- L60 `test_search_returns_results(self, _mock_catalog)` (method)
- L72 `test_search_filters_by_query(self, _mock_catalog)` (method)
- L82 `test_fetch_returns_bundle(self, _mock_catalog, mock_get)` (method)
- L112 `test_fetch_falls_back_to_raw_github_url(self, _mock_catalog, mock_get)` (method)
- L129 `test_fetch_missing_slug_returns_none(self, _mock_catalog)` (method)
- L134 `test_inspect_returns_meta(self, _mock_catalog)` (method)
