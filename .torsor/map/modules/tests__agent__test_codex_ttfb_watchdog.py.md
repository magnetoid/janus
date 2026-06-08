---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_codex_ttfb_watchdog.py

Symbols in `tests/agent/test_codex_ttfb_watchdog.py`.

- L32 `_make_codex_agent(tmp_path, monkeypatch)` (function)
- L60 `test_ttfb_kills_when_no_stream_event(tmp_path, monkeypatch)` (function) — Backend accepts the connection but emits no event -> killed at the TTFB
- L105 `test_ttfb_default_tolerates_slow_first_event(tmp_path, monkeypatch)` (function) — With no env var set, the no-byte TTFB default is generous (120s), so a
- L146 `test_ttfb_includes_silent_hang_hint_for_gpt_5_5(tmp_path, monkeypatch)` (function) — The no-first-byte watchdog should surface the same actionable hint as the
- L193 `test_ttfb_high_env_is_capped_for_openai_codex(tmp_path, monkeypatch)` (function) — A stale local env value like 90s must not make openai-codex wait 90s
- L236 `test_ttfb_does_not_kill_when_events_flow(tmp_path, monkeypatch)` (function) — Once a stream event has arrived, a generation that runs past the TTFB
- L274 `test_event_idle_kills_after_first_event_then_silence(tmp_path, monkeypatch)` (function) — If Codex emits an opening SSE event and then goes silent, kill it via
- L319 `test_ttfb_disabled_via_env_zero(tmp_path, monkeypatch)` (function) — Setting HERMES_CODEX_TTFB_TIMEOUT_SECONDS=0 disables the TTFB watchdog;
- L354 `test_large_codex_request_waits_instead_of_ttfb_reconnect(tmp_path, monkeypatch)` (function) — Large Codex inputs can legitimately take longer than the small-request
- L389 `test_large_codex_request_strict_ttfb_env_still_reconnects(tmp_path, monkeypatch)` (function) — Operators can force the old early-reconnect behavior for large inputs
