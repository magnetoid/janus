---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/platforms/feishu_meeting_invite.py

Symbols in `gateway/platforms/feishu_meeting_invite.py`.

- L24 `MeetingInviteUser` (class)
- L32 `MeetingInviteMeeting` (class)
- L42 `MeetingInvitedPayload` (class)
- L49 `_as_dict(value: Any)` (function) — Coerce a lark SDK object / dict / JSON string into a plain dict.
- L64 `_content_payload(container: Dict[str, Any])` (function) — Unwrap a Feishu ``body.content`` list carrying an application/json payload.
- L81 `_int_field(value: Any)` (function)
- L90 `_parse_user(value: Any)` (function)
- L103 `_parse_meeting(value: Any)` (function)
- L117 `parse_meeting_invited_event(data: Any)` (function)
- L138 `build_meeting_invite_prompt(payload: MeetingInvitedPayload)` (function)
- L159 `_dedup_key(payload: MeetingInvitedPayload)` (function)
- L167 `handle_meeting_invited_event(adapter: Any, data: Any)` (function) — Convert a vc.bot.meeting_invited_v1 event into a gateway MessageEvent.
