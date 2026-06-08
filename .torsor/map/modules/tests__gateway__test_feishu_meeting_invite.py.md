---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_feishu_meeting_invite.py

Symbols in `tests/gateway/test_feishu_meeting_invite.py`.

- L16 `_user_id(open_id, union_id='on_1', user_id='e65g874e')` (function)
- L24 `_make_payload(event_id='evt_1')` (function)
- L66 `_make_payload_with_numeric_inviter_id()` (function)
- L72 `_Adapter` (class)
- L73 `__init__(self, duplicate=False)` (method)
- L79 `_is_duplicate(self, key)` (method)
- L83 `build_source(self, **kwargs)` (method)
- L86 `_resolve_sender_profile(self, sender_id)` (method)
- L94 `_handle_message_with_guards(self, event)` (method)
- L98 `TestMeetingInviteParsing` (class)
- L99 `test_parse_actual_payload_string_int64_fields(self)` (method)
- L112 `test_parse_body_content_payload(self)` (method)
- L133 `test_parse_requires_inviter(self)` (method)
- L139 `test_parse_requires_meeting_no(self)` (method)
- L145 `test_prompt_contains_meeting_and_inviter_context(self)` (method)
- L165 `TestMeetingInviteHandler` (class)
- L166 `_run(self, coro)` (method)
- L169 `test_routes_as_synthetic_message_to_inviter_open_id(self)` (method)
- L192 `test_duplicate_event_is_dropped(self)` (method)
- L200 `test_inviter_without_open_id_is_dropped(self)` (method)
- L209 `TestMeetingInviteSendRouting` (class)
- L210 `_run(self, coro)` (method)
- L213 `test_feishu_user_id_prefix_sends_with_user_id_receive_type(self)` (method)
