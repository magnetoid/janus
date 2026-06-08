---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/image_routing.py

Symbols in `agent/image_routing.py`.

- L78 `extract_image_refs(text: str)` (function) — Scan free-form text for image references the model should see.
- L159 `_coerce_capability_bool(raw: Any)` (function) — Return True/False for recognised boolean values, None otherwise.
- L176 `_supports_vision_override(cfg: Optional[Dict[str, Any]], provider: str, model: str)` (function) — Resolve user-declared vision capability from config.yaml.
- L225 `_coerce_mode(raw: Any)` (function) — Normalize a config value into one of the valid modes.
- L235 `_explicit_aux_vision_override(cfg: Optional[Dict[str, Any]])` (function) — True when the user configured a specific auxiliary vision backend.
- L260 `_lookup_supports_vision(provider: str, model: str, cfg: Optional[Dict[str, Any]]=None)` (function) — Return True/False if we can resolve caps, None if unknown.
- L287 `decide_image_input_mode(provider: str, model: str, cfg: Optional[Dict[str, Any]])` (function) — Return ``"native"`` or ``"text"`` for the given turn.
- L335 `_sniff_mime_from_bytes(raw: bytes)` (function) — Detect image MIME from magic bytes. Returns None if unrecognised.
- L370 `_guess_mime(path: Path, raw: Optional[bytes]=None)` (function) — Return image MIME type for *path*.
- L396 `_file_to_data_url(path: Path)` (function) — Encode a local image as a base64 data URL at its native size.
- L418 `build_native_content_parts(user_text: str, image_paths: List[str], image_urls: Optional[List[str]]=None)` (function) — Build an OpenAI-style ``content`` list for a user turn.
