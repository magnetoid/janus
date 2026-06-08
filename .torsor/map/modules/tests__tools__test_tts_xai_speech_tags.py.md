---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_tts_xai_speech_tags.py

Symbols in `tests/tools/test_tts_xai_speech_tags.py`.

- L8 `test_apply_xai_auto_speech_tags_adds_light_pause_after_first_sentence()` (function)
- L16 `test_apply_xai_auto_speech_tags_preserves_explicit_tags()` (function)
- L22 `test_apply_xai_auto_speech_tags_preserves_all_documented_xai_tags()` (function)
- L28 `test_apply_xai_auto_speech_tags_multi_paragraph_emits_single_pause()` (function) — Regression for #29417 — multi-paragraph input doubled the pause.
- L53 `test_apply_xai_auto_speech_tags_single_paragraph_still_gets_first_sentence_pause()` (function) — Sanity guard — the fix only suppresses the first-sentence pass when
- L64 `test_apply_xai_auto_speech_tags_single_newline_still_gets_first_sentence_pause()` (function) — A single newline isn't a paragraph break — no ``[pause]`` injected by
- L75 `test_generate_xai_tts_sends_auto_speech_tags_when_enabled(tmp_path, monkeypatch)` (function)
- L108 `test_generate_xai_tts_leaves_text_plain_by_default(tmp_path, monkeypatch)` (function)
