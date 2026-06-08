---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_line_ending_preservation.py

Symbols in `tests/tools/test_line_ending_preservation.py`.

- L17 `hermes_home(monkeypatch, tmp_path)` (function) — Isolate HERMES_HOME so the tests don't pollute the real config.
- L49 `_crlf_count(b: bytes)` (function)
- L53 `_bare_lf_count(b: bytes)` (function)
- L57 `TestPatchCRLFPreservation` (class)
- L58 `test_patch_on_crlf_file_stays_pure_crlf(self, hermes_home, tmp_path)` (method) — LLM sends LF old/new; file has CRLF.  Result must be all CRLF,
- L86 `test_patch_on_lf_file_stays_lf(self, hermes_home, tmp_path)` (method) — LF file with LF new_string stays LF — no spurious CRLF added.
- L110 `test_patch_multiline_replacement_on_crlf(self, hermes_home, tmp_path)` (method) — Multi-line new_string with bare LFs should be CRLF-converted
- L137 `TestWriteFileCRLFPreservation` (class)
- L138 `test_overwrite_crlf_file_with_lf_content_preserves_crlf(self, hermes_home, tmp_path)` (method) — The agent typically sends bare-LF content; if the file existed
- L165 `test_new_file_written_as_is(self, hermes_home, tmp_path)` (method) — No pre-existing file → write content verbatim (LF by default).
- L179 `test_overwrite_lf_file_stays_lf(self, hermes_home, tmp_path)` (method) — Pre-existing LF file should not get spurious CRLFs.
- L198 `TestLineEndingHelpers` (class) — Direct unit tests for the pure helpers — easier to debug than the
- L202 `test_detect_crlf(self)` (method)
- L207 `test_detect_lf(self)` (method)
- L212 `test_detect_empty(self)` (method)
- L218 `test_detect_mixed_picks_crlf(self)` (method) — Mixed-ending content (any CRLF in the head) returns CRLF —
- L226 `test_normalize_to_lf_strips_cr(self)` (method)
- L231 `test_normalize_to_crlf_idempotent(self)` (method)
