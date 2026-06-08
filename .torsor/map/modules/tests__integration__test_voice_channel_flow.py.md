---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/integration/test_voice_channel_flow.py

Symbols in `tests/integration/test_voice_channel_flow.py`.

- L47 `_make_secret_key()` (function) — Generate a random 32-byte key.
- L53 `_build_encrypted_rtp_packet(secret_key, opus_payload, ssrc=100, seq=1, timestamp=960)` (function) — Build a real NaCl-encrypted RTP packet matching Discord's format.
- L75 `_build_padded_rtp_packet(secret_key, opus_payload, pad_len, ssrc=100, seq=1, timestamp=960, declared_pad_len=None, ext_words=0)` (function) — Build a NaCl-encrypted RTP packet with the P bit set and padding appended.
- L119 `_make_voice_receiver(secret_key, dave_session=None, bot_ssrc=9999, allowed_user_ids=None, members=None)` (function) — Create a VoiceReceiver with real secret key.
- L142 `TestRealNaClDecrypt` (class) — End-to-end: real NaCl encrypt → _on_packet decrypt → buffer.
- L145 `test_valid_encrypted_packet_buffered(self)` (method) — Real NaCl encrypted packet → decrypted → buffered.
- L157 `test_wrong_key_packet_dropped(self)` (method) — Packet encrypted with wrong key → NaCl fails → not buffered.
- L169 `test_bot_ssrc_ignored(self)` (method) — Packet from bot's own SSRC → ignored.
- L179 `test_multiple_packets_accumulate(self)` (method) — Multiple valid packets → buffer grows.
- L194 `test_different_ssrcs_separate_buffers(self)` (method) — Packets from different SSRCs → separate buffers.
- L208 `TestRealNaClWithDAVE` (class) — NaCl decrypt + DAVE passthrough scenarios with real crypto.
- L211 `test_dave_unknown_ssrc_passthrough(self)` (method) — DAVE enabled but SSRC unknown → skip DAVE, buffer audio.
- L226 `test_dave_unencrypted_error_passthrough(self)` (method) — DAVE raises 'Unencrypted' → use NaCl-decrypted data as-is.
- L244 `test_dave_real_error_drops(self)` (method) — DAVE raises non-Unencrypted error → packet dropped.
- L258 `TestRTPPaddingStrip` (class) — RFC 3550 §5.1 — strip RTP padding before DAVE/Opus decode.
- L261 `test_padded_packet_stripped_and_buffered(self)` (method) — P bit set → trailing padding stripped → opus payload decoded.
- L274 `test_padded_packet_matches_unpadded_output(self)` (method) — Same opus payload with/without padding → same decoded PCM.
- L291 `test_padding_with_dave_passthrough(self)` (method) — Padding stripped before DAVE → passthrough buffers cleanly.
- L305 `test_invalid_padding_length_zero_dropped(self)` (method) — Declared pad_len=0 is invalid (RFC requires count includes itself).
- L318 `test_invalid_padding_length_overflow_dropped(self)` (method) — Declared pad_len > payload size → packet dropped.
- L331 `test_padding_consuming_entire_payload_dropped(self)` (method) — Padding consumes entire payload → no opus data → dropped.
- L342 `test_padding_with_extension_stripped_correctly(self)` (method) — X+P bits both set → strip extension from start, padding from end.
- L365 `TestFullVoiceFlow` (class) — End-to-end: encrypt → receive → buffer → silence detect → complete.
- L368 `test_single_utterance_flow(self)` (method) — Encrypt packets → buffer → silence → check_silence returns utterance.
- L392 `test_utterance_with_ssrc_automap(self)` (method) — No SPEAKING event → auto-map sole allowed user → utterance processed.
- L416 `test_pause_blocks_during_playback(self)` (method) — Pause receiver → packets ignored → resume → packets accepted.
- L433 `test_corrupted_packet_ignored(self)` (method) — Corrupted/truncated packet → silently ignored.
- L452 `test_stop_cleans_everything(self)` (method) — stop() clears all state cleanly.
- L473 `TestSPEAKINGHook` (class) — SPEAKING event hook correctly maps SSRC to user_id.
- L476 `test_speaking_hook_installed(self)` (method) — start() installs speaking hook on connection.
- L484 `test_map_ssrc_via_speaking(self)` (method) — SPEAKING op 5 event maps SSRC to user_id.
- L491 `test_map_ssrc_overwrites(self)` (method) — New SPEAKING event for same SSRC overwrites old mapping.
- L499 `test_speaking_mapped_audio_processed(self)` (method) — After SSRC is mapped, audio from that SSRC gets correct user_id.
- L517 `TestAuthFiltering` (class) — Only allowed users' audio should be processed.
- L520 `test_allowed_user_audio_processed(self)` (method) — Allowed user's utterance is returned by check_silence.
- L543 `test_automap_rejects_unallowed_user(self)` (method) — Auto-map refuses to map SSRC to user not in allowed list.
- L566 `test_empty_allowlist_allows_all(self)` (method) — Empty allowed_user_ids means no restriction.
- L590 `TestRejoinFlow` (class) — Leave and rejoin: state cleanup and fresh receiver.
- L593 `test_stop_then_new_receiver_clean_state(self)` (method) — After stop(), a new receiver starts with empty state.
- L614 `test_rejoin_new_ssrc_works(self)` (method) — After rejoin, user may get new SSRC — still works.
- L635 `test_rejoin_without_speaking_event_automap(self)` (method) — Rejoin without SPEAKING event — auto-map sole allowed user.
- L668 `TestMultiGuildIsolation` (class) — Each guild has independent voice state.
- L671 `test_separate_receivers_independent(self)` (method) — Two receivers (different guilds) don't interfere.
- L693 `test_stop_one_doesnt_affect_other(self)` (method) — Stopping one receiver doesn't affect another.
- L717 `TestEchoPreventionFlow` (class) — Receiver pause/resume during TTS playback prevents echo.
- L720 `test_audio_during_pause_ignored(self)` (method) — Audio arriving while paused is completely ignored.
- L735 `test_audio_after_resume_processed(self)` (method) — Audio arriving after resume is processed normally.
