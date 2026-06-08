---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/platforms/slack.py

Symbols in `gateway/platforms/slack.py`.

- L70 `_ThreadContextCache` (class) — Cache entry for fetched thread context.
- L79 `check_slack_requirements()` (function) — Check if Slack dependencies are available.
- L107 `_extract_text_from_slack_blocks(blocks: list)` (function) — Extract readable text from Slack Block Kit blocks, including quoted/forwarded content.
- L202 `_serialize_slack_blocks_for_agent(blocks: list, max_chars: int=6000)` (function) — Return a compact, redacted JSON view of the current message's Block Kit payload.
- L269 `_apply_slack_proxy(client: Any, proxy_url: Optional[str])` (function) — Apply a resolved proxy to a Slack SDK client or clear it explicitly.
- L282 `_resolve_slack_proxy_url()` (function) — Resolve a proxy URL that Slack SDK clients can safely use.
- L303 `SlackAdapter` (class) — Slack bot adapter using Socket Mode.
- L321 `__init__(self, config: PlatformConfig)` (method)
- L373 `_start_socket_mode_handler(self)` (method) — Start the Slack Socket Mode background task.
- L387 `_stop_socket_mode_handler(self)` (method) — Stop Socket Mode handler and task.
- L415 `_socket_transport_connected(self)` (method) — Best-effort check of current Socket Mode transport state.
- L436 `_restart_socket_mode(self, reason: str)` (method) — Reconnect Socket Mode without rebuilding adapter state.
- L455 `_socket_watchdog_loop(self)` (method) — Monitor Socket Mode and reconnect if the task/transport dies.
- L488 `_on_socket_watchdog_done(self, task: asyncio.Task)` (method)
- L508 `_ensure_socket_watchdog(self)` (method)
- L514 `_on_socket_mode_task_done(self, task: asyncio.Task)` (method)
- L546 `_describe_slack_api_error(self, response: Any, *, file_obj: Optional[Dict[str, Any]]=None)` (method) — Convert Slack API auth/permission failures into actionable user-facing text.
- L588 `_describe_slack_download_failure(self, exc: Exception, *, file_obj: Optional[Dict[str, Any]]=None)` (method) — Translate Slack download exceptions into user-facing attachment diagnostics.
- L636 `_pop_slash_context(self, chat_id: str)` (method) — Return and remove the slash-command context for *chat_id*, if fresh.
- L677 `_send_slash_ephemeral(self, ctx: Dict[str, Any], content: str)` (method) — Replace the initial ephemeral ack via ``response_url``.
- L728 `connect(self)` (method) — Connect to Slack via Socket Mode.
- L978 `create_handoff_thread(self, parent_chat_id: str, name: str)` (method) — Create a Slack thread anchor for a session handoff.
- L1021 `disconnect(self)` (method) — Disconnect from Slack.
- L1050 `_get_client(self, chat_id: str)` (method) — Return the workspace-specific WebClient for a channel.
- L1057 `send(self, chat_id: str, content: str, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method) — Send a message to a Slack channel or DM.
- L1135 `send_private_notice(self, chat_id: str, user_id: str, content: str, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method) — Send a Slack ephemeral message visible only to one user.
- L1171 `edit_message(self, chat_id: str, message_id: str, content: str, *, finalize: bool=False)` (method) — Edit a previously sent Slack message.
- L1202 `send_typing(self, chat_id: str, metadata=None)` (method) — Show a typing/status indicator using assistant.threads.setStatus.
- L1231 `stop_typing(self, chat_id: str, metadata=None)` (method) — Clear the assistant thread status indicator.
- L1247 `_dm_top_level_threads_as_sessions(self)` (method) — Whether top-level Slack DMs get per-message session threads.
- L1261 `_resolve_thread_ts(self, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method) — Resolve the correct thread_ts for a Slack API call.
- L1299 `_upload_file(self, chat_id: str, file_path: str, caption: Optional[str]=None, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method) — Upload a local file to Slack.
- L1341 `send_multiple_images(self, chat_id: str, images: List[Tuple[str, str]], metadata: Optional[Dict[str, Any]]=None, human_delay: float=0.0)` (method) — Send a batch of images as a single Slack message with multiple file uploads.
- L1465 `_record_uploaded_file_thread(self, chat_id: str, thread_ts: Optional[str])` (method) — Treat successful file uploads as bot participation in a thread.
- L1477 `_is_retryable_upload_error(self, exc: Exception)` (method) — Best-effort detection for transient Slack upload failures.
- L1504 `format_message(self, content: str)` (method) — Convert standard markdown to Slack mrkdwn format.
- L1616 `_add_reaction(self, channel: str, timestamp: str, emoji: str)` (method) — Add an emoji reaction to a message. Returns True on success.
- L1630 `_remove_reaction(self, channel: str, timestamp: str, emoji: str)` (method) — Remove an emoji reaction from a message. Returns True on success.
- L1643 `_reactions_enabled(self)` (method) — Check if message reactions are enabled via config/env.
- L1647 `on_processing_start(self, event: MessageEvent)` (method) — Add an in-progress reaction when message processing begins.
- L1658 `on_processing_complete(self, event: MessageEvent, outcome: ProcessingOutcome)` (method) — Swap the in-progress reaction for a final success/failure reaction.
- L1679 `_resolve_user_name(self, user_id: str, chat_id: str='')` (method) — Resolve a Slack user ID to a display name, with caching.
- L1709 `send_image_file(self, chat_id: str, image_path: str, caption: Optional[str]=None, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method) — Send a local image file to Slack by uploading it.
- L1739 `send_image(self, chat_id: str, image_url: str, caption: Optional[str]=None, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method) — Send an image to Slack by uploading the URL as a file.
- L1806 `send_voice(self, chat_id: str, audio_path: str, caption: Optional[str]=None, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None, **kwargs)` (method) — Send an audio file to Slack.
- L1833 `send_video(self, chat_id: str, video_path: str, caption: Optional[str]=None, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method) — Send a video file to Slack.
- L1891 `send_document(self, chat_id: str, file_path: str, caption: Optional[str]=None, file_name: Optional[str]=None, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method) — Send a document/file attachment to Slack.
- L1950 `get_chat_info(self, chat_id: str)` (method) — Get information about a Slack channel.
- L1974 `_assistant_thread_key(self, channel_id: str, thread_ts: str)` (method) — Return a stable cache key for Slack assistant thread metadata.
- L1982 `_extract_assistant_thread_metadata(self, event: dict)` (method) — Extract Slack Assistant thread identity data from an event payload.
- L2021 `_cache_assistant_thread_metadata(self, metadata: Dict[str, str])` (method) — Remember assistant thread identity data for later message events.
- L2044 `_lookup_assistant_thread_metadata(self, event: dict, channel_id: str='', thread_ts: str='')` (method) — Load cached assistant-thread metadata that matches the current event.
- L2068 `_seed_assistant_thread_session(self, metadata: Dict[str, str])` (method) — Prime the session store so assistant threads get stable user scoping.
- L2099 `_handle_assistant_thread_lifecycle_event(self, event: dict)` (method) — Handle Slack Assistant lifecycle events that carry user/thread identity.
- L2105 `_handle_slack_message(self, event: dict)` (method) — Handle an incoming Slack message event.
- L2646 `send_exec_approval(self, chat_id: str, command: str, session_key: str, description: str='dangerous command', metadata: Optional[Dict[str, Any]]=None)` (method) — Send a Block Kit approval prompt with interactive buttons.
- L2729 `send_slash_confirm(self, chat_id: str, title: str, message: str, session_key: str, confirm_id: str, metadata: Optional[Dict[str, Any]]=None)` (method) — Send a Block Kit three-option slash-command confirmation prompt.
- L2800 `_is_interactive_user_authorized(self, user_id: str, *, channel_id: str='', user_name: Optional[str]=None)` (method) — Return whether a Slack interactive caller may perform gated actions.
- L2849 `_handle_slash_confirm_action(self, ack, body, action)` (method) — Handle a slash-confirm button click from Block Kit.
- L2967 `_handle_approval_action(self, ack, body, action)` (method) — Handle an approval button click from Block Kit.
- L3080 `_fetch_thread_context(self, channel_id: str, thread_ts: str, current_ts: str, team_id: str='', limit: int=30)` (method) — Fetch recent thread messages to provide context when the bot is
- L3220 `_fetch_thread_parent_text(self, channel_id: str, thread_ts: str, team_id: str='')` (method) — Return the raw text of the thread parent message (for reply_to_text).
- L3264 `_handle_slash_command(self, command: dict)` (method) — Handle Slack slash commands.
- L3357 `_has_active_session_for_thread(self, channel_id: str, thread_ts: str, user_id: str)` (method) — Check if there's an active session for a thread.
- L3412 `_download_slack_file(self, url: str, ext: str, audio: bool=False, team_id: str='')` (method) — Download a Slack file using the bot token for auth, with retry.
- L3470 `_download_slack_file_bytes(self, url: str, team_id: str='')` (method) — Download a Slack file and return raw bytes, with retry.
- L3521 `_slack_require_mention(self)` (method) — Return whether channel messages require an explicit bot mention.
- L3540 `_slack_strict_mention(self)` (method) — When true, channel threads require an explicit @-mention on every
- L3557 `_slack_free_response_channels(self)` (method) — Return channel IDs where no @mention is required.
- L3575 `_slack_allowed_channels(self)` (method) — Return the whitelist of channel IDs the bot will respond in.
