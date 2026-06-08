---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# optional-skills/creative/meme-generation/scripts/generate_meme.py

Symbols in `optional-skills/creative/meme-generation/scripts/generate_meme.py`.

- L39 `_fetch_url(url: str, timeout: int=15)` (function) — Fetch URL content, using requests if available, else urllib.
- L49 `load_curated_templates()` (function) — Load templates with hand-tuned text field positions.
- L55 `_default_fields(box_count: int)` (function) — Generate sensible default text field positions for unknown templates.
- L80 `fetch_imgflip_templates()` (function) — Fetch popular meme templates from imgflip API. Cached for 24h.
- L107 `_slugify(name: str)` (function) — Convert a template name to a slug for matching.
- L112 `resolve_template(identifier: str)` (function) — Resolve a template by curated ID, imgflip name, or imgflip ID.
- L154 `get_template_image(url: str)` (function) — Download a template image, caching it locally.
- L173 `find_font(size: int)` (function) — Find a bold font for meme text. Tries Impact, then falls back.
- L197 `_wrap_text(text: str, font: ImageFont.FreeTypeFont, max_width: int)` (function) — Word-wrap text to fit within max_width pixels. Never breaks mid-word.
- L215 `draw_outlined_text(draw: ImageDraw.ImageDraw, text: str, x: int, y: int, font_size: int, max_width: int, align: str='center')` (function) — Draw white text with black outline, auto-scaled to fit max_width.
- L263 `_overlay_on_image(img: Image.Image, texts: list, fields: list)` (function) — Overlay meme text directly on an image using field positions.
- L282 `_add_bars(img: Image.Image, texts: list)` (function) — Add black bars with white text above/below the image.
- L344 `generate_meme(template_id: str, texts: list[str], output_path: str)` (function) — Generate a meme from a template and save it. Returns the path.
- L366 `generate_from_image(image_path: str, texts: list[str], output_path: str, use_bars: bool=False)` (function) — Generate a meme from a custom image (e.g. AI-generated). Returns the path.
- L386 `list_templates()` (function) — Print curated templates with custom positioning.
- L398 `search_templates(query: str)` (function) — Search imgflip templates by name.
