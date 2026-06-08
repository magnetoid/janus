---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_delivery_silence_filter.py

Symbols in `tests/gateway/test_delivery_silence_filter.py`.

- L56 `test_is_silence_narration_positive(content)` (function)
- L61 `test_is_silence_narration_negative(content)` (function)
- L65 `test_is_silence_narration_none_safe()` (function)
- L69 `test_length_guard_rejects_long_strings()` (function)
- L77 `RecordingAdapter` (class)
- L78 `__init__(self)` (method)
- L81 `send(self, chat_id, content, metadata=None)` (method)
- L87 `test_silence_narration_dropped_pre_send(tmp_path, monkeypatch)` (function)
- L105 `test_real_message_is_delivered(tmp_path, monkeypatch)` (function)
- L122 `test_config_opt_out_lets_silence_through(tmp_path, monkeypatch)` (function)
- L138 `test_env_override_disables_filter(tmp_path, monkeypatch)` (function)
- L153 `test_env_override_enables_filter_over_config(tmp_path, monkeypatch)` (function)
- L169 `test_local_delivery_not_filtered(tmp_path, monkeypatch)` (function)
- L189 `test_config_flag_defaults_true()` (function)
- L193 `test_config_from_dict_parses_flag()` (function)
- L198 `test_config_to_dict_roundtrip()` (function)
