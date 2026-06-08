---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/google_meet/meet_bot.py

Symbols in `plugins/google_meet/meet_bot.py`.

- L57 `_is_safe_meet_url(url: str)` (function) — Return True if *url* is a Google Meet URL we're willing to navigate to.
- L64 `_meeting_id_from_url(url: str)` (function) — Extract the 3-segment meeting code from a Meet URL.
- L85 `_BotState` (class) — Single-process mutable state, flushed to ``status.json`` on each change.
- L88 `__init__(self, out_dir: Path, meeting_id: str, url: str)` (method)
- L120 `record_caption(self, speaker: str, text: str)` (method) — Append a caption line if we haven't seen this exact (speaker, text).
- L141 `_flush(self)` (method)
- L170 `set(self, **kwargs)` (method)
- L247 `_enable_captions_js()` (function) — Return a small JS snippet that tries to click the 'Turn on captions' button.
- L265 `_start_realtime_speaker(*, rt: dict, out_dir: Path, bridge_info: dict, api_key: str, model: str, voice: str, instructions: str, stop_flag: dict, state: '_BotState')` (function) — Wire up the OpenAI Realtime session + speaker thread + PCM pump.
- L414 `_mac_audio_device_index(device_name: str)` (function) — Return the ffmpeg ``-audio_device_index`` for *device_name*, as a string.
- L447 `run_bot()` (function)
- L731 `_try_guest_name(page, guest_name: str)` (function) — If Meet is showing a guest-name input, type *guest_name* into it.
- L742 `_detect_admission(page)` (function) — True if we're clearly past the lobby and in the call itself.
- L777 `_detect_denied(page)` (function) — True when Meet is showing a 'you were denied' / 'no one admitted' page.
- L796 `_looks_like_human_speaker(speaker: str, bot_guest_name: str)` (function) — Whether a caption line's speaker is probably a human, not our bot echo.
- L816 `_click_join(page, state: _BotState)` (function) — Click 'Join now' or 'Ask to join' if either button is visible.
- L834 `_parse_duration(raw: str)` (function) — Parse ``30m`` / ``2h`` / ``90`` (seconds) → float seconds, or None.
