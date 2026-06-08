---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/session_recap.py

Symbols in `hermes_cli/session_recap.py`.

- L49 `_coerce_text(value: Any)` (function) — Flatten assistant/user ``content`` into a plain string.
- L74 `_tool_call_name_and_args(tool_call: Any)` (function) — Extract ``(name, arguments_dict)`` from a tool_call entry.
- L101 `_iter_assistant_tool_calls(messages: Sequence[Mapping[str, Any]])` (function)
- L118 `_count_visible_turns(messages: Sequence[Mapping[str, Any]])` (function) — Return ``(user_turn_count, assistant_turn_count, tool_message_count)``.
- L136 `_latest_user_prompt(messages: Sequence[Mapping[str, Any]])` (function)
- L147 `_latest_assistant_text(messages: Sequence[Mapping[str, Any]])` (function)
- L161 `_recent_window(messages: Sequence[Mapping[str, Any]], window: int=_RECENT_TURN_WINDOW)` (function) — Return the tail slice of ``messages`` covering at most ``window``
- L184 `_shortened_path(path: str)` (function) — Show a path relative to cwd when possible, otherwise with ~ expansion.
- L203 `_summarise_tool_activity(tool_calls: Sequence[Tuple[str, Mapping[str, Any]]])` (function) — Return ``(tool_counts_sorted, recently_edited_files)``.
- L231 `_truncate(text: str, limit: int)` (function)
- L238 `build_recap(messages: Sequence[Mapping[str, Any]], *, session_title: Optional[str]=None, session_id: Optional[str]=None, platform: Optional[str]=None)` (function) — Build a multi-line recap of recent activity.
