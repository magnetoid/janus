---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_signal_media.py

Symbols in `tests/tools/test_signal_media.py`.

- L13 `_make_httpx_mock()` (function) — Create a mock httpx module with proper sync json().
- L45 `inject_httpx(monkeypatch)` (function) — Inject mock httpx into sys.modules before imports.
- L50 `TestSendSignalMediaFiles` (class) — Test that _send_signal correctly handles media_files parameter.
- L53 `test_send_signal_basic_text_without_media(self)` (method) — Backward compatibility: text-only signal messages work.
- L65 `test_send_signal_with_attachments(self, tmp_path)` (method) — Signal messages with media_files include attachments in JSON-RPC.
- L81 `test_send_signal_with_missing_media_file(self)` (method) — Missing media files should generate warnings but not fail.
- L96 `TestSendSignalMediaRestrictions` (class) — Test that the restriction block handles Signal media correctly.
- L99 `test_signal_allows_text_only_media_via_send_to_platform(self)` (method) — Signal should accept text-only media files (no message) via _send_to_platform.
- L124 `test_non_media_platforms_reject_text_only_media(self)` (method) — Slack should reject text-only media (no MESSAGE content).
- L150 `TestSendSignalMediaWarningMessages` (class) — Test warning messages are updated to include signal.
- L153 `test_warning_includes_signal_when_media_omitted(self)` (method) — Non-media platforms should show a warning mentioning signal in the supported list.
- L182 `TestSendSignalGroupChats` (class) — Test that _send_signal handles group chats correctly.
- L185 `test_send_signal_group_with_attachments(self, tmp_path)` (method) — Group chat messages with attachments should use groupId parameter.
- L201 `TestSendSignalConfigLoading` (class) — Verify Signal config loading works.
- L204 `test_signal_platform_exists(self)` (method) — Platform.SIGNAL should be a valid platform.
