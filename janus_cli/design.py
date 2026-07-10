"""Janus CLI design system — the single home of styling decisions.

Semantic tokens (accent/fg/muted/faint/ok/warn/error) and geometric symbols
(activity/ok/fail/bullet/prompt/gutter/rule) resolved from the active skin,
plus shared render helpers. Rendering code asks for MEANING ("the accent
color", "the failure mark"); this module decides presentation. Raw hex values
and glyph literals must not appear at call sites.

Color routing honors NO_COLOR / TERM=dumb / non-TTY through the one existing
gate (janus_cli.colors.should_use_color). Symbols degrade to an ASCII set on
encodings that can't render them (legacy Windows console).
"""
from __future__ import annotations

import sys
from typing import Dict, Tuple

# token -> (skin color key, minimal-design fallback hex)
_TOKEN_KEYS: Dict[str, Tuple[str, str]] = {
    "accent": ("ui_accent", "#E3A857"),
    "fg": ("banner_text", "#C9C9C9"),
    "muted": ("ui_label", "#8A8A8A"),
    "faint": ("banner_dim", "#5C5C5C"),
    "ok": ("ui_ok", "#7CB87C"),
    "warn": ("ui_warn", "#D4A24E"),
    "error": ("ui_error", "#D47C7C"),
}

_SYMBOLS_MINIMAL: Dict[str, str] = {
    "activity": "▸", "ok": "✓", "fail": "✗", "bullet": "●",
    "prompt": "❯", "gutter": "▍", "rule": "─",
}
_SYMBOLS_ASCII: Dict[str, str] = {
    "activity": ">", "ok": "ok", "fail": "x", "bullet": "*",
    "prompt": ">", "gutter": "|", "rule": "-",
}


def _skin():
    from janus_cli.skin_engine import get_active_skin
    return get_active_skin()


def _color_on() -> bool:
    from janus_cli.colors import should_use_color
    return should_use_color()


def _unicode_ok() -> bool:
    """True when stdout's encoding can render the minimal symbol set."""
    enc = getattr(sys.stdout, "encoding", None) or "utf-8"
    try:
        "".join(_SYMBOLS_MINIMAL.values()).encode(enc)
        return True
    except (UnicodeEncodeError, LookupError):
        return False


def tok(name: str) -> str:
    """Resolve a semantic color token to a hex string ('' when color is off
    or the token is unknown). Callers must treat '' as 'no styling'."""
    if not _color_on():
        return ""
    entry = _TOKEN_KEYS.get(name)
    if entry is None:
        return ""
    skin_key, fallback = entry
    try:
        return _skin().get_color(skin_key, fallback) or fallback
    except Exception:
        return fallback


def sym(name: str) -> str:
    """Resolve a symbol by meaning. Skin overrides apply only when the
    terminal can render unicode; the ASCII fallback set is never overridden."""
    if not _unicode_ok():
        return _SYMBOLS_ASCII.get(name, "")
    base = _SYMBOLS_MINIMAL.get(name, "")
    try:
        return _skin().get_symbol(name, base)
    except Exception:
        return base


def layout() -> str:
    """Active structural layout: 'open' (minimal) or 'panel' (legacy boxed)."""
    try:
        return getattr(_skin(), "layout", "panel") or "panel"
    except Exception:
        return "panel"


def styled(text: str, token: str, *, bold: bool = False) -> str:
    """Wrap *text* in Rich markup for *token*; plain text when color is off."""
    color = tok(token)
    if not color:
        return f"[bold]{text}[/]" if bold and _color_on() else text
    style = f"bold {color}" if bold else color
    return f"[{style}]{text}[/]"
