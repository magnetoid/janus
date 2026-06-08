---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/memory/honcho/session.py

Symbols in `plugins/memory/honcho/session.py`.

- L28 `HonchoSession` (class) — A conversation session backed by Honcho.
- L45 `add_message(self, role: str, content: str, **kwargs: Any)` (method) — Add a message to the local cache.
- L56 `get_history(self, max_messages: int=50)` (method) — Get message history for LLM context.
- L65 `clear(self)` (method) — Clear all messages in the session.
- L71 `HonchoSessionManager` (class) — Manages conversation sessions using Honcho.
- L79 `__init__(self, honcho: Honcho | None=None, context_tokens: int | None=None, config: Any | None=None, runtime_user_peer_name: str | None=None, runtime_user_peer_name_alt: str | None=None)` (method) — Initialize the session manager.
- L156 `honcho(self)` (method) — Get the Honcho client, initializing if needed.
- L162 `_get_or_create_peer(self, peer_id: str)` (method) — Get or create a Honcho peer.
- L178 `_get_or_create_honcho_session(self, session_id: str, user_peer: Any, assistant_peer: Any)` (method) — Get or create a Honcho session with peers configured.
- L272 `_sanitize_id(self, id_str: str)` (method) — Sanitize an ID to match Honcho's pattern: ^[a-zA-Z0-9_-]+
- L276 `_runtime_user_ids(self)` (method) — Return runtime identity candidates in lookup order.
- L287 `_session_key_fallback_peer_id(self, key: str)` (method)
- L293 `_explicit_user_peer_ids(self)` (method) — Return sanitized user peer IDs that came from explicit config.
- L311 `_generated_runtime_peer_id(self, prefix: str, runtime_id: str)` (method) — Return a stable peer ID for an unknown prefixed runtime user.
- L328 `_resolve_user_peer_id(self, key: str)` (method) — Resolve the Honcho user peer ID for this manager/session.
- L360 `get_or_create(self, key: str)` (method) — Get an existing session or create a new one.
- L419 `_flush_session(self, session: HonchoSession)` (method) — Internal: write unsynced messages to Honcho synchronously.
- L458 `_async_writer_loop(self)` (method) — Background daemon thread: drains the async write queue.
- L497 `save(self, session: HonchoSession)` (method) — Save messages to Honcho, respecting write_frequency.
- L521 `flush_all(self)` (method) — Flush all pending unsynced messages for all cached sessions.
- L545 `shutdown(self)` (method) — Gracefully shut down the async writer thread.
- L552 `delete(self, key: str)` (method) — Delete a session from local cache.
- L560 `new_session(self, key: str)` (method) — Create a new session, preserving the old one for user modeling.
- L594 `_default_reasoning_level(self)` (method) — Return the configured default reasoning level.
- L598 `dialectic_query(self, session_key: str, query: str, reasoning_level: str | None=None, peer: str='user')` (method) — Query Honcho's dialectic endpoint about a peer.
- L663 `prefetch_context(self, session_key: str, user_message: str | None=None)` (method) — Fire get_prefetch_context in a background thread, caching the result.
- L678 `set_context_result(self, session_key: str, result: dict[str, str])` (method) — Store a prefetched context result in a thread-safe way.
- L685 `pop_context_result(self, session_key: str)` (method) — Return and clear the cached context result for this session.
- L694 `get_prefetch_context(self, session_key: str, user_message: str | None=None)` (method) — Pre-fetch user and AI peer context from Honcho.
- L749 `migrate_local_history(self, session_key: str, messages: list[dict[str, Any]])` (method) — Upload local session history to Honcho as a file.
- L791 `_format_migration_transcript(session_key: str, messages: list[dict[str, Any]])` (method) — Format local messages as an XML transcript for Honcho file upload.
- L821 `migrate_memory_files(self, session_key: str, memory_dir: str)` (method) — Upload MEMORY.md and USER.md to Honcho as files.
- L921 `_normalize_card(card: Any)` (method) — Normalize Honcho card payloads into a plain list of strings.
- L929 `_fetch_peer_card(self, peer_id: str, *, target: str | None=None)` (method) — Fetch a peer card directly from the peer object.
- L947 `_fetch_peer_context(self, peer_id: str, search_query: str | None=None, *, target: str | None=None)` (method) — Fetch representation + peer card directly from a peer object.
- L991 `get_session_context(self, session_key: str, peer: str='user')` (method) — Fetch full session context from Honcho including summary.
- L1042 `_resolve_peer_id(self, session: HonchoSession, peer: str | None)` (method) — Resolve a peer alias or explicit peer ID to a concrete Honcho peer ID.
- L1060 `_resolve_observer_target(self, session: HonchoSession, peer: str | None)` (method) — Resolve observer and target peer IDs for context/search/profile queries.
- L1076 `get_peer_card(self, session_key: str, peer: str='user')` (method) — Fetch a peer card — a curated list of key facts.
- L1102 `search_context(self, session_key: str, query: str, max_tokens: int=800, peer: str='user')` (method) — Semantic search over Honcho session context.
- L1148 `create_conclusion(self, session_key: str, content: str, peer: str='user')` (method) — Write a conclusion about a target peer back to Honcho.
- L1197 `delete_conclusion(self, session_key: str, conclusion_id: str, peer: str='user')` (method) — Delete a conclusion by ID. Use only for PII removal.
- L1229 `set_peer_card(self, session_key: str, card: list[str], peer: str='user')` (method) — Update a peer's card.
- L1265 `seed_ai_identity(self, session_key: str, content: str, source: str='manual')` (method) — Seed the AI peer's Honcho representation from text content.
- L1310 `get_ai_representation(self, session_key: str)` (method) — Fetch the AI peer's current Honcho representation.
- L1331 `list_sessions(self)` (method) — List all cached sessions.
