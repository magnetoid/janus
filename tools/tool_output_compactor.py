"""Compress large tool results before they enter the model's context.

Web scrapes, email bodies, and HTML-heavy search payloads are the biggest
token sinks in a typical session, and today they reach the model verbatim.
This module runs a *bounded, fail-open* compaction pass over a tool result
just before it is appended back into the conversation:

  * base64 ``data:`` URIs (inlined images/fonts) → short placeholder
  * embedded HTML → compact Markdown-ish text (stdlib; ``markdownify`` used
    only if it is already importable — never auto-installed)
  * runs of blank lines / repeated identical lines collapsed
  * optional hard character cap

Design constraints (do not relax without reading them):

* **Caching-safe.** This only ever transforms the *new* result string being
  returned from ``handle_function_call``. It never rewrites prior
  conversation context, so prompt caching is untouched — the one
  load-bearing invariant this feature must respect.
* **Never grows a result.** The compacted string is returned only when it is
  strictly shorter than the original; otherwise the original is returned
  unchanged. Compaction can only ever save tokens, never add them.
* **Fail-open.** Any exception anywhere falls back to the original result.
  A compaction bug must never break a tool call.
* **Stdlib-only.** No new dependency is added to core. This keeps the
  feature inside the repo's hardline supply-chain posture; higher-fidelity
  HTML conversion is opportunistically used iff ``markdownify`` happens to
  be installed.
* **Byte-fidelity tools opt out.** Code/file tools (``read_file``,
  ``execute_code``, ``patch``, …) are excluded by default so source text is
  never reflowed. Callers gate on ``exclude_tools``.

The public entry points are :func:`maybe_compact_tool_result` (config-aware,
used by core) and :func:`compact_tool_result` (pure, used by tests).
"""

from __future__ import annotations

import json
import logging
import re
from html.parser import HTMLParser
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

# Mirrors DEFAULT_CONFIG["tool_output"]["compaction"]. Kept here too so the
# pure function works standalone (tests, plugins) without loading config.
_DEFAULTS: Dict[str, Any] = {
    "enabled": False,
    "min_chars": 4000,
    "html_to_markdown": True,
    "strip_data_uris": True,
    "collapse_repeats": True,
    "max_chars": 0,
    # Only compact long string *leaves* inside a JSON result; shorter leaves
    # are left alone so structural/identifier strings are never mangled.
    "min_leaf_chars": 200,
    "exclude_tools": [
        "read_file",
        "write_file",
        "patch",
        "search_files",
        "execute_code",
        "terminal",
        "process",
    ],
}

# A base64 (or otherwise large) data: URI. Group the prefix so the placeholder
# can name the mime type. We require a sizeable payload so we never touch
# small/legitimate inline values.
_DATA_URI_RE = re.compile(
    r"data:([a-zA-Z0-9.+-]*/?[a-zA-Z0-9.+-]*)?(?:;[a-zA-Z0-9=+.-]+)*,"
    r"[A-Za-z0-9+/=_%-]{64,}",
)

# 3+ consecutive newlines (allowing trailing spaces on the blank lines).
_BLANK_RUN_RE = re.compile(r"(?:[ \t]*\n){3,}")

# Cheap structural signal that a blob contains real HTML markup (a closing
# tag plus a recognizable block/inline element), not just stray angle
# brackets in prose or code.
_HTML_HINT_RE = re.compile(
    r"</[a-zA-Z]|<(?:div|p|span|table|tr|td|ul|ol|li|h[1-6]|a\s|br|body|html|article|section)\b",
    re.IGNORECASE,
)

_VOID_BLOCK_TAGS = {"br", "hr"}
_BLOCK_TAGS = {
    "p", "div", "section", "article", "header", "footer", "main", "aside",
    "ul", "ol", "li", "table", "tr", "thead", "tbody", "blockquote", "pre",
    "h1", "h2", "h3", "h4", "h5", "h6",
}
_SKIP_TAGS = {"script", "style", "noscript", "head", "svg", "template"}


def _merge_config(config: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    cfg = dict(_DEFAULTS)
    if config:
        for key, val in config.items():
            if val is not None:
                cfg[key] = val
    return cfg


def _looks_like_html(text: str) -> bool:
    # Require at least a couple of markup hits so a single ``<thing>`` in
    # prose doesn't trip the HTML path.
    return len(_HTML_HINT_RE.findall(text, 0, 20000)) >= 2


class _HTMLToText(HTMLParser):
    """Minimal, dependency-free HTML → Markdown-ish text converter.

    Not a full Markdown renderer — just enough structure (headings, links,
    list bullets, block breaks) to keep the text readable after tags are
    stripped, while dropping script/style and attribute noise.
    """

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._out: list[str] = []
        self._skip_depth = 0
        self._href: Optional[str] = None
        self._link_text: list[str] = []

    # -- helpers --
    def _emit(self, text: str) -> None:
        if self._skip_depth:
            return
        if self._href is not None:
            self._link_text.append(text)
        else:
            self._out.append(text)

    def _newline(self) -> None:
        if not self._skip_depth:
            self._out.append("\n")

    # -- handlers --
    def handle_starttag(self, tag: str, attrs: list) -> None:
        tag = tag.lower()
        if tag in _SKIP_TAGS:
            self._skip_depth += 1
            return
        if self._skip_depth:
            return
        if tag in _VOID_BLOCK_TAGS:
            self._newline()
            return
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self._newline()
            self._out.append("#" * int(tag[1]) + " ")
            return
        if tag == "li":
            self._newline()
            self._out.append("- ")
            return
        if tag == "a":
            for name, value in attrs:
                if name == "href" and value:
                    self._href = value
                    self._link_text = []
            return
        if tag in _BLOCK_TAGS:
            self._newline()

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in _SKIP_TAGS:
            self._skip_depth = max(0, self._skip_depth - 1)
            return
        if self._skip_depth:
            return
        if tag == "a" and self._href is not None:
            text = "".join(self._link_text).strip()
            href = self._href
            self._href = None
            self._link_text = []
            if text and href and text != href:
                self._out.append(f"[{text}]({href})")
            elif text:
                self._out.append(text)
            elif href:
                self._out.append(href)
            return
        if tag in _BLOCK_TAGS:
            self._newline()

    def handle_data(self, data: str) -> None:
        if not data.strip():
            # Preserve a single separating space for inter-tag whitespace.
            if self._href is None and self._out and not self._out[-1].endswith((" ", "\n")):
                self._out.append(" ")
            return
        self._emit(re.sub(r"[ \t\r\f\v]+", " ", data))

    def get_text(self) -> str:
        return "".join(self._out)


def _html_to_markdown(text: str) -> str:
    # Prefer markdownify *only* if already installed — never auto-install.
    try:
        from markdownify import markdownify as _md  # type: ignore

        return _md(text, heading_style="ATX")
    except Exception:
        pass
    try:
        parser = _HTMLToText()
        parser.feed(text)
        parser.close()
        return parser.get_text()
    except Exception:
        logger.debug("stdlib HTML conversion failed; leaving text as-is", exc_info=True)
        return text


def _collapse_repeats(text: str) -> str:
    # Collapse 3+ blank lines into one blank line.
    text = _BLANK_RUN_RE.sub("\n\n", text)
    # Collapse long runs of identical adjacent lines (log/boilerplate spam):
    # keep the first two, replace the rest with a one-line summary.
    out: list[str] = []
    i = 0
    lines = text.split("\n")
    n = len(lines)
    while i < n:
        j = i
        while j < n and lines[j] == lines[i]:
            j += 1
        run = j - i
        if lines[i] and run > 3:
            out.append(lines[i])
            out.append(lines[i])
            out.append(f"… ({run - 2} identical lines omitted)")
        else:
            out.extend(lines[i:j])
        i = j
    return "\n".join(out)


def _compact_text(text: str, cfg: Dict[str, Any]) -> str:
    if cfg.get("strip_data_uris", True):
        text = _DATA_URI_RE.sub(
            lambda m: f"[data-uri omitted: {m.group(1) or 'data'}]", text
        )
    if cfg.get("html_to_markdown", True) and _looks_like_html(text):
        text = _html_to_markdown(text)
    if cfg.get("collapse_repeats", True):
        text = _collapse_repeats(text)
    text = text.strip()
    max_chars = int(cfg.get("max_chars", 0) or 0)
    if max_chars > 0 and len(text) > max_chars:
        # str slicing is codepoint-safe; cut on a whitespace boundary near
        # the cap when one is close, to avoid splitting mid-word.
        cut = text.rfind(" ", max(0, max_chars - 200), max_chars)
        cut = cut if cut > 0 else max_chars
        omitted = len(text) - cut
        text = text[:cut] + f"\n… [{omitted} chars truncated]"
    return text


def _compact_json_leaves(obj: Any, cfg: Dict[str, Any], min_leaf: int) -> Any:
    if isinstance(obj, str):
        if len(obj) >= min_leaf:
            return _compact_text(obj, cfg)
        return obj
    if isinstance(obj, list):
        return [_compact_json_leaves(v, cfg, min_leaf) for v in obj]
    if isinstance(obj, dict):
        return {k: _compact_json_leaves(v, cfg, min_leaf) for k, v in obj.items()}
    return obj


def compact_tool_result(
    result: str,
    *,
    tool_name: str = "",
    config: Optional[Dict[str, Any]] = None,
) -> str:
    """Return a compacted copy of ``result``, or ``result`` unchanged.

    Pure and fail-open: never raises, never returns a longer string than it
    was given. ``config`` overlays :data:`_DEFAULTS`; ``enabled`` and
    ``exclude_tools`` are honored here too so the function is safe to call
    directly in tests.
    """
    try:
        if not isinstance(result, str) or not result:
            return result
        cfg = _merge_config(config)
        if not cfg.get("enabled", False):
            return result
        if tool_name and tool_name in set(cfg.get("exclude_tools") or ()):
            return result
        if len(result) < int(cfg.get("min_chars", 0) or 0):
            return result

        min_leaf = int(cfg.get("min_leaf_chars", 200) or 200)
        compacted: str
        stripped = result.lstrip()
        if stripped[:1] in ("{", "["):
            try:
                parsed = json.loads(result)
            except (ValueError, TypeError):
                compacted = _compact_text(result, cfg)
            else:
                new = _compact_json_leaves(parsed, cfg, min_leaf)
                compacted = json.dumps(new, ensure_ascii=False)
        else:
            compacted = _compact_text(result, cfg)

        # Only ever shrink. Guarantees compaction cannot cost tokens.
        return compacted if len(compacted) < len(result) else result
    except Exception:
        logger.debug("tool-output compaction failed; returning original", exc_info=True)
        return result


def maybe_compact_tool_result(result: str, tool_name: str = "") -> str:
    """Config-aware wrapper used by ``model_tools.handle_function_call``.

    Reads ``tool_output.compaction`` from the active config (mtime-cached, so
    cheap per call) and delegates to :func:`compact_tool_result`. Fully
    fail-open: if config can't be read, the result passes through untouched.
    """
    try:
        from janus_cli.config import load_config

        cfg = (load_config() or {}).get("tool_output", {})
        comp = cfg.get("compaction", {}) if isinstance(cfg, dict) else {}
        if not isinstance(comp, dict) or not comp.get("enabled", False):
            return result
        return compact_tool_result(result, tool_name=tool_name, config=comp)
    except Exception:
        logger.debug("maybe_compact_tool_result: config read failed", exc_info=True)
        return result
