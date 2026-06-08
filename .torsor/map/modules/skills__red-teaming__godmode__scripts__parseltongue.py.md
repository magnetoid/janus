---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# skills/red-teaming/godmode/scripts/parseltongue.py

Symbols in `skills/red-teaming/godmode/scripts/parseltongue.py`.

- L113 `_apply_raw(word)` (function) — Raw — no transformation (baseline).
- L117 `_apply_leetspeak(word)` (function) — L33t — basic leetspeak substitution.
- L121 `_apply_unicode(word)` (function) — Unicode — Cyrillic/homoglyph substitution.
- L132 `_apply_bubble(word)` (function) — Bubble — circled letter Unicode characters.
- L143 `_apply_spaced(word)` (function) — Spaced — insert spaces between characters.
- L147 `_apply_fullwidth(word)` (function) — Fullwidth — fullwidth Unicode characters.
- L158 `_apply_zwj(word)` (function) — ZeroWidth — zero-width joiners between characters.
- L162 `_apply_mixedcase(word)` (function) — MiXeD — alternating case.
- L166 `_apply_semantic(word)` (function) — Semantic — replace with synonym/description.
- L170 `_apply_dotted(word)` (function) — Dotted — dots between characters.
- L174 `_apply_underscored(word)` (function) — Under_score — underscores between characters.
- L180 `_apply_reversed(word)` (function) — Reversed — reverse the characters.
- L184 `_apply_superscript(word)` (function) — Superscript — superscript Unicode characters.
- L188 `_apply_smallcaps(word)` (function) — SmallCaps — small capital Unicode characters.
- L192 `_apply_morse(word)` (function) — Morse — morse code representation.
- L196 `_apply_piglatin(word)` (function) — PigLatin — pig latin transformation.
- L207 `_apply_brackets(word)` (function) — [B.r.a.c.k] — each character in brackets.
- L211 `_apply_mathbold(word)` (function) — MathBold — mathematical bold Unicode.
- L222 `_apply_mathitalic(word)` (function) — MathItalic — mathematical italic Unicode.
- L233 `_apply_strikethrough(word)` (function) — S̶t̶r̶i̶k̶e̶ — strikethrough combining characters.
- L237 `_apply_leetheavy(word)` (function) — L33t+ — heavy leetspeak with extended map.
- L241 `_apply_hyphenated(word)` (function) — Hyphen — hyphens between characters.
- L247 `_apply_leetunicode(word)` (function) — L33t+Uni — alternating leet and unicode.
- L258 `_apply_spacedmixed(word)` (function) — S p A c E d — spaced + alternating case.
- L262 `_apply_reversedleet(word)` (function) — Rev+L33t — reversed then leetspeak.
- L266 `_apply_bubblespaced(word)` (function) — Bubble+Spaced — bubble text with spaces.
- L277 `_apply_unicodezwj(word)` (function) — Uni+ZWJ — unicode homoglyphs with zero-width non-joiners.
- L285 `_apply_base64hint(word)` (function) — Base64 — base64 encode the word.
- L292 `_apply_hexencode(word)` (function) — Hex — hex encode each character.
- L296 `_apply_acrostic(word)` (function) — Acrostic — NATO alphabet expansion.
- L307 `_apply_dottedunicode(word)` (function) — Dot+Uni — unicode homoglyphs with dots.
- L315 `_apply_fullwidthmixed(word)` (function) — FW MiX — fullwidth + mixed case alternating.
- L326 `_apply_triplelayer(word)` (function) — Triple — leet + unicode + uppercase rotating with ZWJ.
- L392 `to_braille(text)` (function) — Convert text to braille Unicode characters.
- L396 `to_leetspeak(text)` (function) — Convert text to leetspeak.
- L400 `to_bubble(text)` (function) — Convert text to bubble/circled text.
- L412 `to_morse(text)` (function) — Convert text to Morse code.
- L437 `detect_triggers(text, custom_triggers=None)` (function) — Detect trigger words in text. Returns list of found triggers.
- L449 `obfuscate_query(query, technique_name, triggers=None)` (function) — Apply one obfuscation technique to trigger words in a query.
- L481 `generate_variants(query, tier='standard', custom_triggers=None)` (function) — Generate obfuscated variants of a query up to the tier limit.
- L507 `escalate_encoding(query, level=0)` (function) — Get an encoding-escalated version of the query.
