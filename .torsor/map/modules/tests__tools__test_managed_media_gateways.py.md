---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_managed_media_gateways.py

Symbols in `tests/tools/test_managed_media_gateways.py`.

- L14 `_load_tool_module(module_name: str, filename: str)` (function)
- L24 `_restore_tool_and_agent_modules()` (function)
- L50 `_enable_managed_nous_tools(monkeypatch)` (function) — Patch the source modules so managed_nous_tools_enabled() returns True
- L64 `_install_fake_tools_package()` (function)
- L83 `_install_fake_fal_client(captured)` (function)
- L135 `_install_fake_openai_module(captured, transcription_response=None)` (function)
- L176 `test_managed_fal_submit_uses_gateway_origin_and_nous_token(monkeypatch)` (function)
- L204 `test_managed_fal_submit_reuses_cached_sync_client(monkeypatch)` (function)
- L225 `test_openai_tts_uses_managed_audio_gateway_when_direct_key_absent(monkeypatch, tmp_path)` (function)
- L247 `test_openai_tts_accepts_openai_api_key_as_direct_fallback(monkeypatch, tmp_path)` (function)
- L265 `test_transcription_uses_model_specific_response_formats(monkeypatch, tmp_path)` (function)
- L313 `_load_video_gen_plugin(monkeypatch)` (function) — Load the FAL video gen plugin in isolation.
- L338 `test_video_gen_managed_fal_submit_uses_gateway(monkeypatch)` (function) — Video gen routes through the managed gateway when FAL_KEY is absent.
- L365 `test_video_gen_managed_client_reused_across_calls(monkeypatch)` (function) — The managed video client is cached and reused across requests.
- L383 `test_video_gen_direct_mode_when_fal_key_set(monkeypatch)` (function) — When FAL_KEY is set and gateway not preferred, uses direct fal_client.submit.
- L426 `test_video_gen_gateway_4xx_raises_actionable_valueerror(monkeypatch)` (function) — A 4xx from the managed gateway surfaces a clear ValueError with remediation hints.
- L459 `test_video_gen_is_available_true_via_gateway(monkeypatch)` (function) — is_available() returns True when FAL_KEY is absent but managed gateway is configured.
- L471 `test_video_gen_prefers_gateway_overrides_direct_key(monkeypatch)` (function) — When FAL_KEY is set but prefers_gateway('video_gen') is True, routes through gateway.
- L495 `test_video_gen_happy_horse_uses_alibaba_namespace()` (function) — Verify the happy-horse family uses alibaba/ not fal-ai/ endpoints.
