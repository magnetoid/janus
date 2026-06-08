---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_discord_voice_mixer.py

Symbols in `tests/gateway/test_discord_voice_mixer.py`.

- L36 `TestVoiceMixerCore` (class)
- L37 `test_frame_geometry_matches_discord(self)` (method)
- L43 `test_empty_mixer_returns_silence_frames(self)` (method)
- L50 `test_is_opus_false(self)` (method)
- L54 `test_ambient_loops_and_is_quiet(self)` (method)
- L65 `test_speech_audible_over_ambient_then_releases(self)` (method)
- L83 `test_clipping_prevents_int16_wraparound(self)` (method)
- L92 `test_stop_speech_clears_in_flight(self)` (method)
- L102 `test_set_ambient_none_clears(self)` (method)
- L109 `test_cleanup_silences(self)` (method)
- L115 `test_pcm_not_frame_aligned_is_padded(self)` (method)
- L122 `test_synth_ambient_is_stereo_and_frame_aligned(self)` (method)
- L132 `_make_adapter(fx_cfg=None)` (function)
- L158 `TestVoiceMixerActive` (class)
- L159 `test_false_when_no_mixer(self)` (method)
- L163 `test_true_when_mixer_present(self)` (method)
- L168 `test_false_when_attr_missing(self)` (method)
- L177 `TestPlayInVoiceChannelMixerPath` (class)
- L179 `test_routes_through_mixer_when_present(self)` (method)
- L210 `test_falls_back_when_decode_fails(self)` (method)
- L237 `TestPlayAckInVoice` (class)
- L239 `test_noop_when_ack_disabled(self)` (method)
- L245 `test_noop_when_no_mixer(self)` (method)
- L250 `test_plays_speech_when_armed(self, tmp_path)` (method)
