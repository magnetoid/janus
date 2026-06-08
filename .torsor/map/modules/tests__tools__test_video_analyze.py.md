---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_video_analyze.py

Symbols in `tests/tools/test_video_analyze.py`.

- L23 `TestDetectVideoMimeType` (class) — Extension-based MIME detection for video files.
- L26 `test_mp4(self, tmp_path)` (method)
- L31 `test_webm(self, tmp_path)` (method)
- L36 `test_mov(self, tmp_path)` (method)
- L41 `test_avi_fallback_mp4(self, tmp_path)` (method)
- L46 `test_mkv_fallback_mp4(self, tmp_path)` (method)
- L51 `test_mpeg(self, tmp_path)` (method)
- L56 `test_mpg(self, tmp_path)` (method)
- L61 `test_unsupported_extension(self, tmp_path)` (method)
- L66 `test_case_insensitive(self, tmp_path)` (method)
- L77 `TestVideoToBase64DataUrl` (class) — Base64 encoding of video files.
- L80 `test_produces_data_url(self, tmp_path)` (method)
- L86 `test_custom_mime_type(self, tmp_path)` (method)
- L92 `test_default_mime_for_unknown_ext(self, tmp_path)` (method)
- L105 `TestVideoAnalyzeSchema` (class) — Schema structure is correct.
- L108 `test_schema_name(self)` (method)
- L111 `test_schema_has_required_fields(self)` (method)
- L117 `test_schema_description_mentions_video(self)` (method)
- L126 `TestHandleVideoAnalyze` (class) — Tests for the registry handler wrapper.
- L129 `test_returns_awaitable(self, tmp_path, monkeypatch)` (method)
- L143 `test_uses_auxiliary_video_model_env(self, tmp_path, monkeypatch)` (method)
- L155 `test_falls_back_to_vision_model_env(self, tmp_path, monkeypatch)` (method)
- L173 `TestVideoAnalyzeTool` (class) — Core video analysis function tests.
- L176 `_run(self, coro)` (method)
- L179 `test_local_file_success(self, tmp_path, monkeypatch)` (method) — Analyze a local video file — happy path.
- L196 `test_local_file_not_found(self, tmp_path)` (method) — Non-existent file raises appropriate error.
- L203 `test_unsupported_format(self, tmp_path)` (method) — Unsupported extension raises error.
- L213 `test_video_too_large(self, tmp_path, monkeypatch)` (method) — Video exceeding max size is rejected.
- L228 `test_interrupt_check(self, tmp_path)` (method) — Tool respects interrupt flag.
- L239 `test_empty_response_retries(self, tmp_path)` (method) — Retries once on empty model response.
- L262 `test_file_scheme_stripped(self, tmp_path)` (method) — file:// prefix is stripped correctly.
- L278 `test_api_message_format(self, tmp_path)` (method) — Verify the message sent to LLM uses video_url content type.
- L311 `TestVideoToolsetRegistration` (class) — Verify the tool is registered correctly.
- L314 `test_registered_in_video_toolset(self)` (method)
- L322 `test_not_in_core_tools(self)` (method) — video_analyze should NOT be in _HERMES_CORE_TOOLS (default disabled).
- L327 `test_in_video_toolset_definition(self)` (method) — Toolset 'video' should contain video_analyze.
