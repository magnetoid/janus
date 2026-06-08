---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_discord_document_handling.py

Symbols in `tests/gateway/test_discord_document_handling.py`.

- L25 `_ensure_discord_mock()` (function) — Install a mock discord module when discord.py isn't available.
- L68 `FakeDMChannel` (class)
- L69 `__init__(self, channel_id: int=1)` (method)
- L74 `FakeThread` (class)
- L75 `__init__(self, channel_id: int=10)` (method)
- L89 `_redirect_cache(tmp_path, monkeypatch)` (function) — Point document cache to tmp_path so tests never write to ~/.hermes.
- L97 `adapter(monkeypatch)` (function)
- L112 `make_attachment(*, filename: str, content_type: Optional[str], size: int=1024, url: str='https://cdn.discordapp.com/attachments/fake/file')` (function)
- L127 `make_message(attachments: list, content: str='')` (function)
- L140 `_mock_aiohttp_download(raw_bytes: bytes)` (function) — Return a patch context manager that makes aiohttp return raw_bytes.
- L160 `TestIncomingDocumentHandling` (class)
- L163 `test_pdf_document_cached(self, adapter)` (method) — A PDF attachment should be downloaded, cached, typed as DOCUMENT.
- L179 `test_txt_content_injected(self, adapter)` (method) — .txt file under 100KB should have its content injected into event.text.
- L198 `test_md_content_injected(self, adapter)` (method) — .md file under 100KB should have its content injected.
- L214 `test_log_content_injected(self, adapter)` (method) — .log file under 100KB should be treated as text/plain and injected.
- L231 `test_oversized_document_skipped(self, adapter)` (method) — A document over 32MB should be skipped — media_urls stays empty.
- L248 `test_mid_sized_zip_under_32mb_is_cached(self, adapter)` (method) — A 25MB .zip should be accepted now that Discord documents allow up to 32MB.
- L266 `test_zip_document_cached(self, adapter)` (method) — A .zip file should be cached as a supported document.
- L281 `test_download_error_handled(self, adapter)` (method) — If the HTTP download raises, the handler should not crash.
- L304 `test_large_txt_cached_not_injected(self, adapter)` (method) — .txt over 100KB should be cached but NOT injected into event.text.
- L321 `test_multiple_text_files_both_injected(self, adapter)` (method) — Two text file attachments should both be injected into event.text in order.
- L371 `test_image_attachment_unaffected(self, adapter)` (method) — Image attachments should still go through the image path, not the document path.
- L389 `TestAllowAnyAttachment` (class) — Cover the discord.allow_any_attachment config flag.
- L399 `test_unknown_type_skipped_by_default(self, adapter)` (method) — Default (flag off): unknown extension is dropped.
- L417 `test_unknown_type_cached_when_flag_on(self, adapter)` (method) — Flag on: unknown extension is cached as application/octet-stream.
- L438 `test_unknown_type_no_content_type_becomes_octet_stream(self, adapter)` (method) — Flag on + no content_type from discord: MIME falls back to octet-stream.
- L453 `test_max_attachment_bytes_caps_uploads(self, adapter)` (method) — discord.max_attachment_bytes overrides the historical 32 MiB cap.
- L471 `test_max_attachment_bytes_zero_means_unlimited(self, adapter)` (method) — max_attachment_bytes=0 disables the size cap entirely.
- L491 `test_allowlisted_doc_unchanged_when_flag_on(self, adapter)` (method) — Flag on must not change handling of types already in SUPPORTED_DOCUMENT_TYPES.
- L513 `test_helper_reads_env_fallback(self, adapter, monkeypatch)` (method) — Helper falls back to DISCORD_ALLOW_ANY_ATTACHMENT env var.
- L521 `test_helper_config_overrides_env(self, adapter, monkeypatch)` (method) — config.yaml setting wins over env var.
- L527 `test_max_bytes_helper_invalid_value_falls_back(self, adapter)` (method) — Garbage in max_attachment_bytes config falls back to 32 MiB.
