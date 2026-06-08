---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_stream_consumer_draft.py

Symbols in `tests/gateway/test_stream_consumer_draft.py`.

- L27 `_make_draft_capable_adapter(*, supports_draft: bool=True, draft_succeeds: bool=True)` (function) — Build a minimal BasePlatformAdapter subclass with draft support.
- L80 `TestDraftTransportSelection` (class) — Verify _resolve_draft_streaming picks the right transport.
- L83 `test_default_transport_stays_on_edit(self)` (method)
- L88 `test_auto_dm_with_draft_capable_adapter_picks_draft(self)` (method)
- L94 `test_auto_group_falls_back_to_edit(self)` (method)
- L100 `test_explicit_edit_never_uses_drafts(self)` (method)
- L106 `test_explicit_draft_unsupported_falls_back(self)` (method)
- L112 `test_magicmock_adapter_falls_back_to_edit(self)` (method) — MagicMock adapters (used in many existing tests) must default to
- L121 `TestDraftStreamingHappyPath` (class) — End-to-end: stream a few deltas in a DM, verify drafts animated and
- L126 `test_dm_stream_animates_draft_then_finalizes_with_send(self)` (method)
- L164 `test_group_chat_skips_draft_path(self)` (method)
- L184 `TestDraftFallbackOnFailure` (class) — When a draft frame fails, the consumer disables drafts for the rest
- L189 `test_first_draft_failure_disables_drafts_for_run(self)` (method)
- L212 `TestDraftIdLifecycle` (class) — Each response gets its own draft_id (no animation collision across
- L217 `test_consecutive_responses_use_distinct_draft_ids(self)` (method)
- L250 `test_tool_boundary_bumps_draft_id(self)` (method) — After a segment break (tool boundary), the next text segment
- L291 `TestAlreadySentInDraftMode` (class) — Drafts must NOT mark _already_sent — that flag gates the gateway's
- L297 `test_drafts_do_not_set_already_sent_until_real_message(self)` (method)
