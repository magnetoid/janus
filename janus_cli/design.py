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


# --- shared render helpers ---------------------------------------------------

def ok(msg: str) -> str:
    return f"{styled(sym('ok'), 'ok')} {msg}" if tok("ok") else f"{sym('ok')} {msg}"


def warn(msg: str) -> str:
    return f"{styled('!', 'warn')} {msg}" if tok("warn") else f"! {msg}"


def error(msg: str) -> str:
    return f"{styled(sym('fail'), 'error')} {msg}" if tok("error") else f"{sym('fail')} {msg}"


def note(msg: str) -> str:
    return f"{styled(sym('bullet'), 'muted')} {msg}" if tok("muted") else f"{sym('bullet')} {msg}"


def rule(width: int = 40) -> str:
    line = sym("rule") * max(1, int(width))
    return styled(line, "faint") if tok("faint") else line


def header(text: str) -> str:
    return styled(text, "accent", bold=True) if tok("accent") else text


class GutterBlock:
    """Rich renderable: the inner renderable with a left accent gutter bar —
    the open-layout response frame (full width, clean copy-paste, no box)."""

    def __init__(self, renderable, gutter_style: str = ""):
        self.renderable = renderable
        self.gutter_style = gutter_style or tok("accent")

    def __rich_console__(self, console, options):
        from rich.segment import Segment
        from rich.style import Style
        bar = sym("gutter")
        try:
            style = Style.parse(self.gutter_style) if self.gutter_style else Style()
        except Exception:
            style = Style()
        prefix = f"  {bar} "
        inner = options.update_width(max(10, options.max_width - len(prefix)))
        for line in console.render_lines(self.renderable, inner, pad=False):
            yield Segment(prefix, style)
            yield from line
            yield Segment.line()


def response_block(content, *, label: str, border_hex: str, text_hex: str,
                   width: int, attribution: str = ""):
    """The final-response frame. Panel layout replicates today's Panel kwargs
    exactly (classic stays byte-compatible); open layout returns a GutterBlock
    (attribution shown as a muted lead-in line when present)."""
    if layout() != "open":
        from rich import box as rich_box
        from rich.panel import Panel
        title_text = f"{label} {attribution}".rstrip() if attribution else label
        return Panel(
            content,
            title=f"[{border_hex} bold]{title_text}[/]",
            title_align="left",
            border_style=border_hex,
            style=text_hex,
            box=rich_box.HORIZONTALS,
            padding=(1, 4),
            width=width,
        )
    from rich.console import Group
    from rich.text import Text
    block = GutterBlock(content)
    if attribution:
        lead = Text(f"  {attribution.strip()}", style=tok("muted") or "dim")
        return Group(Text(""), lead, block)
    return Group(Text(""), block)
