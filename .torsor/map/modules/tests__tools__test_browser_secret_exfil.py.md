---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_browser_secret_exfil.py

Symbols in `tests/tools/test_browser_secret_exfil.py`.

- L9 `_ensure_redaction_enabled(monkeypatch)` (function) — Ensure redaction is active regardless of host HERMES_REDACT_SECRETS.
- L15 `TestBrowserSecretExfil` (class) — Verify browser_navigate blocks URLs containing secrets.
- L18 `test_blocks_api_key_in_url(self)` (method)
- L25 `test_blocks_openrouter_key_in_url(self)` (method)
- L31 `test_allows_normal_url(self)` (method) — Normal URLs pass the secret check (may fail for other reasons).
- L45 `test_normalizes_non_ascii_url_before_navigation(self)` (method)
- L65 `TestWebExtractSecretExfil` (class) — Verify web_extract_tool blocks URLs containing secrets.
- L69 `test_blocks_api_key_in_url(self)` (method)
- L79 `test_allows_normal_url(self)` (method)
- L88 `test_normalizes_non_ascii_url_before_extract_provider(self, monkeypatch)` (method)
- L138 `TestBrowserSnapshotRedaction` (class) — Verify secrets in page snapshots are redacted before auxiliary LLM calls.
- L141 `test_extract_relevant_content_redacts_secrets(self)` (method) — Snapshot containing secrets should be redacted before call_llm.
- L173 `test_extract_relevant_content_no_task_redacts_secrets(self)` (method) — Snapshot without user_task should also redact secrets.
- L199 `test_extract_relevant_content_normal_snapshot_unchanged(self)` (method) — Snapshot without secrets should pass through normally.
- L227 `TestCamofoxAnnotationRedaction` (class) — Verify annotation context is redacted before vision LLM call.
- L230 `test_annotation_context_secrets_redacted(self)` (method) — Secrets in accessibility tree annotation should be masked.
- L246 `test_annotation_env_dump_redacted(self)` (method) — Env var dump in annotation context should be redacted.
