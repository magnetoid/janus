---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/skills/test_youtube_quiz.py

Symbols in `tests/skills/test_youtube_quiz.py`.

- L16 `_run(capsys, argv: list[str])` (function) — Run main() with given argv and return parsed JSON output.
- L24 `TestNormalizeSegments` (class)
- L25 `test_basic(self)` (method)
- L29 `test_empty_segments(self)` (method)
- L32 `test_whitespace_only(self)` (method)
- L35 `test_collapses_multiple_spaces(self)` (method)
- L40 `TestFetchMissingDependency` (class)
- L41 `test_missing_youtube_transcript_api(self, capsys, monkeypatch)` (method) — When youtube-transcript-api is not installed, report the error.
- L63 `TestFetchWithMockedAPI` (class)
- L64 `_make_mock_module(self, segments=None, raise_exc=None)` (method) — Create a mock youtube_transcript_api module.
- L81 `test_successful_fetch(self, capsys)` (method)
- L93 `test_fetch_error(self, capsys)` (method)
- L104 `test_empty_transcript(self, capsys)` (method)
- L115 `test_segments_without_to_raw_data(self, capsys)` (method) — Handle plain list segments (no to_raw_data method).
