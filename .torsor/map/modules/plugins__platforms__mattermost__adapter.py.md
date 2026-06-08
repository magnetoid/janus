---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/platforms/mattermost/adapter.py

Symbols in `plugins/platforms/mattermost/adapter.py`.

- L53 `check_mattermost_requirements()` (function) — Return True if the Mattermost adapter can be used.
- L71 `MattermostAdapter` (class) — Gateway adapter for Mattermost (self-hosted or cloud).
- L74 `__init__(self, config: PlatformConfig)` (method)
- L106 `_headers(self)` (method)
- L112 `_api_get(self, path: str)` (method) — GET /api/v4/{path}.
- L127 `_api_post(self, path: str, payload: Dict[str, Any])` (method) — POST /api/v4/{path} with JSON body.
- L147 `_api_put(self, path: str, payload: Dict[str, Any])` (method) — PUT /api/v4/{path} with JSON body.
- L166 `_upload_file(self, channel_id: str, file_data: bytes, filename: str, content_type: str='application/octet-stream')` (method) — Upload a file and return its file ID, or None on failure.
- L195 `connect(self)` (method) — Connect to Mattermost and start the WebSocket listener.
- L229 `disconnect(self)` (method) — Disconnect from Mattermost.
- L253 `_resolve_root_id(self, post_id: str)` (method) — Resolve a post_id to the thread root_id for Mattermost.
- L269 `send(self, chat_id: str, content: str, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method) — Send a message (or multiple chunks) to a channel.
- L303 `get_chat_info(self, chat_id: str)` (method) — Return channel name and type.
- L317 `send_typing(self, chat_id: str, metadata: Optional[Dict[str, Any]]=None)` (method) — Send a typing indicator.
- L326 `edit_message(self, chat_id: str, message_id: str, content: str, *, finalize: bool=False)` (method) — Edit an existing post.
- L339 `send_image(self, chat_id: str, image_url: str, caption: Optional[str]=None, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method) — Download an image and upload it as a file attachment.
- L352 `send_image_file(self, chat_id: str, image_path: str, caption: Optional[str]=None, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method) — Upload a local image file.
- L365 `send_document(self, chat_id: str, file_path: str, caption: Optional[str]=None, file_name: Optional[str]=None, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method) — Upload a local file as a document.
- L379 `send_voice(self, chat_id: str, audio_path: str, caption: Optional[str]=None, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method) — Upload an audio file.
- L392 `send_video(self, chat_id: str, video_path: str, caption: Optional[str]=None, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method) — Upload a video file.
- L405 `format_message(self, content: str)` (method) — Mattermost uses standard Markdown — mostly pass through.
- L419 `_send_url_as_file(self, chat_id: str, url: str, caption: Optional[str], reply_to: Optional[str], kind: str='file')` (method) — Download a URL and upload it as a file attachment.
- L481 `_send_local_file(self, chat_id: str, file_path: str, caption: Optional[str], reply_to: Optional[str], file_name: Optional[str]=None)` (method) — Upload a local file and attach it to a post.
- L520 `send_multiple_images(self, chat_id: str, images: List[Tuple[str, str]], metadata: Optional[Dict[str, Any]]=None, human_delay: float=0.0)` (method) — Send a batch of images as a single Mattermost post with multiple attachments.
- L618 `_ws_loop(self)` (method) — Connect to the WebSocket and listen for events, reconnecting on failure.
- L652 `_ws_connect_and_listen(self)` (method) — Single WebSocket session: connect, authenticate, process events.
- L691 `_handle_ws_event(self, event: Dict[str, Any])` (method) — Process a single WebSocket event.
- L881 `_standalone_send(pconfig, chat_id: str, message: str, *, thread_id: Optional[str]=None, media_files: Optional[list]=None, force_document: bool=False)` (function) — Send via the Mattermost v4 REST API without a live gateway adapter.
- L1022 `interactive_setup()` (function) — Guide the user through Mattermost bot setup.
- L1088 `_apply_yaml_config(yaml_cfg: dict, mattermost_cfg: dict)` (function) — Translate ``config.yaml`` ``mattermost:`` keys into env vars.
- L1129 `_is_connected(config)` (function) — Mattermost is considered connected when BOTH MATTERMOST_TOKEN and
- L1150 `_build_adapter(config)` (function) — Factory wrapper that constructs MattermostAdapter from a PlatformConfig.
- L1155 `register(ctx)` (function) — Plugin entry point — called by the Hermes plugin system.
