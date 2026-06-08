---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_microsoft_graph_client.py

Symbols in `tests/tools/test_microsoft_graph_client.py`.

- L18 `_make_provider()` (function)
- L33 `TestMicrosoftGraphClient` (class)
- L34 `test_attaches_bearer_token_header(self)` (method)
- L49 `test_retries_on_rate_limit_and_uses_retry_after(self)` (method)
- L79 `test_raises_api_error_after_retry_budget_exhausted(self)` (method)
- L100 `test_collect_paginated_flattens_value_arrays(self)` (method)
- L119 `test_download_to_file_writes_binary_content(self, tmp_path: Path)` (method)
- L138 `test_download_to_file_streams_large_payload_in_chunks(self, tmp_path: Path, monkeypatch)` (method) — Recordings can be hundreds of MB; verify the body is streamed.
- L184 `test_download_to_file_retries_on_transient_server_error(self, tmp_path: Path)` (method)
- L220 `test_download_to_file_cleans_partial_file_on_exhausted_retries(self, tmp_path: Path)` (method)
- L243 `test_invalid_json_response_raises_client_error(self)` (method)
