---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/platforms/dingtalk.py

Symbols in `gateway/platforms/dingtalk.py`.

- L113 `check_dingtalk_requirements()` (function) — Check if DingTalk dependencies are available and configured.
- L146 `DingTalkAdapter` (class) — DingTalk chatbot adapter using Stream Mode.
- L164 `SUPPORTS_MESSAGE_EDITING(self)` (method) — Edits only meaningful when AI Cards are configured.
- L173 `REQUIRES_EDIT_FINALIZE(self)` (method) — AI Card lifecycle requires an explicit ``finalize=True`` edit
- L181 `__init__(self, config: PlatformConfig)` (method)
- L235 `connect(self)` (method) — Connect to DingTalk via Stream Mode.
- L301 `_run_stream(self)` (method) — Run the async stream client with auto-reconnection.
- L323 `disconnect(self)` (method) — Disconnect from DingTalk.
- L388 `_dingtalk_require_mention(self)` (method) — Return whether group chats should require an explicit bot trigger.
- L397 `_dingtalk_free_response_chats(self)` (method)
- L405 `_dingtalk_allowed_chats(self)` (method) — Return the whitelist of group chat IDs the bot will respond in.
- L419 `_compile_mention_patterns(self)` (method) — Compile optional regex wake-word patterns for group triggers.
- L457 `_load_allowed_users(self)` (method) — Load allowed-users list from config.extra or env var.
- L472 `_is_user_allowed(self, sender_id: str, sender_staff_id: str)` (method)
- L479 `_message_mentions_bot(self, message: 'ChatbotMessage')` (method) — True if the bot was @-mentioned in a group message.
- L487 `_message_matches_mention_patterns(self, text: str)` (method)
- L492 `_should_process_message(self, message: 'ChatbotMessage', text: str, is_group: bool, chat_id: str)` (method) — Apply DingTalk group trigger rules.
- L520 `_spawn_bg(self, coro)` (method) — Start a fire-and-forget coroutine and track it for cleanup.
- L528 `_close_streaming_siblings(self, chat_id: str)` (method) — Finalize any previously-open streaming cards for this chat.
- L558 `_fire_done_reaction(self, chat_id: str)` (method) — Swap 🤔Thinking → 🥳Done on the original user message.
- L587 `_on_message(self, message: 'ChatbotMessage')` (method) — Process an incoming DingTalk chatbot message.
- L706 `_extract_text(message: 'ChatbotMessage')` (method) — Extract plain text from a DingTalk chatbot message.
- L752 `_extract_media(self, message: 'ChatbotMessage')` (method) — Extract media info from message. Returns (MessageType, [urls], [mime_types]).
- L821 `send(self, chat_id: str, content: str, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method) — Send a markdown reply via DingTalk session webhook.
- L929 `send_typing(self, chat_id: str, metadata=None)` (method) — DingTalk does not support typing indicators.
- L933 `send_image(self, chat_id: str, image_url: str, caption: Optional[str]=None, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method) — Send an image via DingTalk markdown.
- L957 `send_image_file(self, chat_id: str, image_path: str, caption: Optional[str]=None, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None, **kwargs)` (method) — DingTalk webhook replies cannot send local image files directly.
- L975 `send_document(self, chat_id: str, file_path: str, caption: Optional[str]=None, file_name: Optional[str]=None, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None, **kwargs)` (method) — DingTalk webhook replies cannot send local file attachments directly.
- L994 `get_chat_info(self, chat_id: str)` (method) — Return basic info about a DingTalk conversation.
- L1001 `_get_valid_webhook(self, chat_id: str)` (method) — Get a valid (non-expired) session webhook for the given chat_id.
- L1017 `_create_and_stream_card(self, chat_id: str, message: Any, content: str, *, finalize: bool=True)` (method) — Create an AI Card, deliver it to the conversation, and stream initial content.
- L1137 `edit_message(self, chat_id: str, message_id: str, content: str, *, finalize: bool=False)` (method) — Edit an AI Card by streaming updated content.
- L1184 `_stream_card_content(self, out_track_id: str, token: str, content: str, finalize: bool=False)` (method) — Stream content to an existing AI Card.
- L1211 `_get_access_token(self)` (method) — Get access token using SDK's cached token.
- L1223 `_send_emotion(self, open_msg_id: str, open_conversation_id: str, emoji_name: str, *, recall: bool=False)` (method) — Add or recall an emoji reaction on a message.
- L1294 `_resolve_media_codes(self, message: 'ChatbotMessage')` (method) — Resolve download codes in message to actual URLs.
- L1333 `_fetch_download_url(self, code: str, robot_code: str, token: str, obj, key: str)` (method) — Fetch download URL for a single code using the robot SDK.
- L1373 `_normalize_markdown(text: str)` (method) — Normalize markdown for DingTalk's parser.
- L1402 `_IncomingHandler` (class) — dingtalk-stream ChatbotHandler that forwards messages to the adapter.
- L1412 `__init__(self, adapter: DingTalkAdapter, loop: Optional[asyncio.AbstractEventLoop]=None)` (method)
- L1418 `pre_start(self)` (method) — No-op pre-start hook required by dingtalk-stream SDK.
- L1428 `process(self, message: 'CallbackMessage')` (method) — Called by dingtalk-stream (>=0.20) when a message arrives.
- L1496 `_safe_on_message(self, chatbot_msg: 'ChatbotMessage')` (method) — Wrapper that catches exceptions from _on_message.
