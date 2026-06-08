---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/plugins/test_teams_pipeline_plugin.py

Symbols in `tests/plugins/test_teams_pipeline_plugin.py`.

- L19 `FakeGraphClient` (class)
- L20 `__init__(self)` (method)
- L24 `_transcript_meeting_resolver(client, *, meeting_id=None, join_web_url=None, tenant_id=None)` (function)
- L34 `_no_call_record(*args, **kwargs)` (function)
- L38 `test_register_adds_cli_only()` (function)
- L52 `test_runtime_config_uses_existing_teams_platform_settings()` (function)
- L84 `test_build_pipeline_runtime_reuses_existing_teams_adapter_surface(monkeypatch, tmp_path)` (function)
- L116 `test_bind_gateway_runtime_attaches_scheduler(monkeypatch, tmp_path)` (function)
- L156 `test_bind_gateway_runtime_drops_notifications_when_unavailable(monkeypatch)` (function)
- L188 `test_store_persists_subscription_event_and_job_state(tmp_path)` (function)
- L214 `test_store_notification_receipts_are_idempotent(tmp_path)` (function)
- L232 `TestTeamsMeetingPipeline` (class)
- L233 `test_transcript_first_path_persists_state_and_skips_recording(self, tmp_path, monkeypatch)` (method)
- L293 `test_recording_fallback_uses_stt_and_updates_sink_records(self, tmp_path, monkeypatch)` (method)
- L385 `test_missing_transcript_and_recording_schedules_retry(self, tmp_path, monkeypatch)` (method)
- L413 `test_duplicate_notification_reuses_completed_job(self, tmp_path, monkeypatch)` (method)
