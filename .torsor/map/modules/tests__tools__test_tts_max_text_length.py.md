---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_tts_max_text_length.py

Symbols in `tests/tools/test_tts_max_text_length.py`.

- L18 `TestResolveMaxTextLength` (class)
- L19 `test_edge_default(self)` (method)
- L22 `test_openai_default_is_4096(self)` (method)
- L25 `test_xai_default_is_15000(self)` (method)
- L28 `test_minimax_default_is_10000(self)` (method)
- L31 `test_mistral_default(self)` (method)
- L34 `test_gemini_default(self)` (method)
- L37 `test_unknown_provider_falls_back(self)` (method)
- L40 `test_empty_provider_falls_back(self)` (method)
- L44 `test_case_insensitive(self)` (method)
- L50 `test_override_wins(self)` (method)
- L54 `test_override_zero_falls_through(self)` (method)
- L59 `test_override_negative_falls_through(self)` (method)
- L63 `test_override_non_int_falls_through(self)` (method)
- L67 `test_override_bool_falls_through(self)` (method)
- L72 `test_missing_provider_section_uses_default(self)` (method)
- L78 `test_elevenlabs_default_model_multilingual_v2(self)` (method)
- L82 `test_elevenlabs_flash_v2_5_gets_40k(self)` (method)
- L86 `test_elevenlabs_flash_v2_gets_30k(self)` (method)
- L90 `test_elevenlabs_v3_gets_5k(self)` (method)
- L94 `test_elevenlabs_unknown_model_falls_back_to_provider_default(self)` (method)
- L98 `test_elevenlabs_override_beats_model_lookup(self)` (method)
- L102 `test_elevenlabs_no_model_id_uses_default_model_mapping(self)` (method)
- L106 `test_provider_config_not_a_dict(self)` (method)
- L112 `test_all_documented_providers_have_defaults(self)` (method)
- L118 `TestTextToSpeechToolTruncation` (class) — End-to-end: verify the resolver actually drives the text_to_speech_tool
- L122 `test_openai_truncates_at_4096_not_4000(self, tmp_path, monkeypatch, caplog)` (method)
- L150 `test_xai_accepts_much_longer_input(self, tmp_path, monkeypatch)` (method)
- L173 `test_user_override_is_respected(self, tmp_path, monkeypatch)` (method)
