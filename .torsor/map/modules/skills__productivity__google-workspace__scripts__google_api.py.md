---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# skills/productivity/google-workspace/scripts/google_api.py

Symbols in `skills/productivity/google-workspace/scripts/google_api.py`.

- L57 `_normalize_authorized_user_payload(payload: dict)` (function)
- L64 `_ensure_authenticated()` (function)
- L71 `_stored_token_scopes()` (function)
- L82 `_gws_binary()` (function)
- L89 `_gws_env()` (function)
- L95 `_run_gws(parts: list[str], *, params: dict | None=None, body: dict | None=None)` (function)
- L131 `_headers_dict(msg: dict)` (function)
- L139 `_extract_message_body(msg: dict)` (function)
- L157 `_extract_doc_text(doc: dict)` (function)
- L168 `_datetime_with_timezone(value: str)` (function)
- L181 `get_credentials()` (function) — Load and refresh credentials from token file.
- L203 `build_service(api, version)` (function)
- L214 `gmail_search(args)` (function)
- L278 `gmail_get(args)` (function)
- L318 `gmail_send(args)` (function)
- L361 `gmail_reply(args)` (function)
- L424 `gmail_labels(args)` (function)
- L438 `gmail_modify(args)` (function)
- L464 `calendar_list(args)` (function)
- L518 `calendar_create(args)` (function)
- L556 `calendar_delete(args)` (function)
- L572 `drive_search(args)` (function)
- L594 `drive_get(args)` (function) — Get metadata for a single Drive file by ID.
- L610 `drive_upload(args)` (function) — Upload a local file to Drive. Falls through to Python client even when gws
- L642 `drive_download(args)` (function) — Download a Drive file to a local path. Google-native files (Docs/Sheets/Slides)
- L691 `drive_create_folder(args)` (function)
- L723 `drive_share(args)` (function)
- L773 `drive_delete(args)` (function) — Trash or permanently delete a Drive file. Defaults to trash (reversible).
- L806 `contacts_list(args)` (function)
- L853 `sheets_get(args)` (function)
- L870 `sheets_update(args)` (function)
- L896 `sheets_append(args)` (function)
- L922 `sheets_create(args)` (function) — Create a new spreadsheet. Returns the new spreadsheet ID and URL.
- L955 `docs_get(args)` (function)
- L976 `docs_create(args)` (function) — Create a new Doc. Optionally seed it with initial body text.
- L999 `docs_append(args)` (function) — Append text to the end of an existing Doc.
- L1029 `_docs_insert_text(doc_id: str, text: str, index: int)` (function) — Send a batchUpdate with a single insertText request.
- L1054 `main()` (function)
