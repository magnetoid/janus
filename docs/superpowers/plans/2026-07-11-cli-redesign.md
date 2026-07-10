# Janus CLI Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship a modern-minimal professional default look for the Janus CLI (near-monochrome + refined-gold accent, geometric symbols, no emoji), redesigning banner / tool lines / spinner / response / help — while preserving today's look verbatim as `/skin classic`.

**Architecture:** A new `janus_cli/design.py` token/symbol layer resolves styling from the existing skin engine; three additive skin-schema fields (`symbols`, `layout: open|panel`, `emoji_tools`) let structures branch per skin. The old default skin is copied verbatim into a new `classic` built-in; the `default` built-in is replaced with the minimal palette. Surfaces migrate one at a time, dispatching on `layout` so `classic` keeps legacy rendering paths byte-for-byte.

**Tech Stack:** Python 3.11, Rich, prompt_toolkit, PyYAML. Spec: `docs/superpowers/specs/2026-07-11-cli-redesign-design.md`.

## Global Constraints

- **Tests run ONLY via `scripts/run_tests.sh`** (never bare pytest — CI parity). For a single test: `scripts/run_tests.sh tests/path/test_x.py::test_name`. Debug variant: `scripts/run_tests.sh --no-isolate <path>`.
- **Ruff rule PLW1514 is enforced repo-wide:** every `open()` / `write_text()` / `read_text()` must pass `encoding="utf-8"`.
- **No change-detector tests** (no snapshotting whole outputs; assert relationships/invariants). Exception: the `classic`-skin verbatim guards intentionally pin exact strings — that pinning IS the feature.
- **Never hardcode `~/.janus`** — use `get_janus_home()` (tests get an isolated home automatically via the `_isolate_janus_home` autouse fixture).
- **Spinner code must not use `\033[K`** (documented pitfall — garbles output under prompt_toolkit `patch_stdout`). Existing space-padding approach stays.
- **No behavior changes:** commands, keybindings, autocomplete, feature set stay identical. Presentation only.
- Accent hex: `#E3A857`. Symbol set: `▸ ✓ ✗ ● ❯ ▍ ─` with ASCII fallbacks `> ok x * > | -`.
- Work happens on branch `claude/cli-redesign` (already created; spec committed).
- Commit messages end with: `Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>`

## File Structure

| File | Role |
|---|---|
| `janus_cli/design.py` (create) | THE styling module: tokens, symbols, layout dispatch, `styled()`, notices, `GutterBlock`, `response_block()` |
| `janus_cli/skin_engine.py` (modify) | +3 `SkinConfig` fields, `_build_skin_config` passthrough, `classic` built-in, new `default` built-in |
| `janus_cli/skin_notice.py` (create) | One-time "new look" notice (stamp-file pattern) |
| `janus_cli/banner.py` (modify) | `_build_open_banner()` + layout dispatch in `build_welcome_banner` |
| `agent/display.py` (modify) | `_wrap()` minimal re-render in `get_cute_tool_message`, spinner minimal fallbacks |
| `agent/tool_executor.py`, `agent/conversation_loop.py` (modify) | Face-composition guards for empty faces |
| `cli.py` (modify) | Response sites (2 Panel + 4 stream-frame lines), `show_help`, `show_tools` header, `_accent_hex` fallback, notice call |
| `tests/janus_cli/test_design.py` (create) | Token/symbol/helper tests |
| `tests/janus_cli/test_classic_skin.py` (create) | Classic-verbatim guards |
| `tests/janus_cli/test_skin_notice.py` (create) | Notice one-shot tests |
| `tests/janus_cli/test_skin_engine.py`, `tests/janus_cli/test_banner.py`, `tests/agent/test_display*.py` (modify) | Updated per surface |

---

### Task 1: Skin-schema additions (`symbols`, `layout`, `emoji_tools`)

**Files:**
- Modify: `janus_cli/skin_engine.py` (SkinConfig ~line 129, `_build_skin_config` ~line 689, `"default"` builtin dict ~line 165, module docstring schema section ~line 75)
- Test: `tests/janus_cli/test_skin_engine.py` (append)

**Interfaces:**
- Produces: `SkinConfig.symbols: Dict[str,str]`, `SkinConfig.layout: str` ("open"|"panel"), `SkinConfig.emoji_tools: bool`, `SkinConfig.get_symbol(name, fallback) -> str`. Later tasks call `get_active_skin().layout` / `.emoji_tools` / `.get_symbol()`.

- [ ] **Step 1: Write the failing tests** (append to `tests/janus_cli/test_skin_engine.py`):

```python
class TestSchemaAdditions:
    """Increment-1 schema fields: symbols / layout / emoji_tools (all optional)."""

    def test_new_fields_have_safe_defaults(self):
        from janus_cli.skin_engine import SkinConfig
        s = SkinConfig(name="x")
        assert s.symbols == {}
        assert s.layout == "panel"          # behavior-preserving until the flip
        assert s.emoji_tools is True
        assert s.get_symbol("activity", "▸") == "▸"

    def test_build_config_passes_fields_through(self):
        from janus_cli.skin_engine import _build_skin_config
        cfg = _build_skin_config({
            "name": "t", "symbols": {"activity": "→"},
            "layout": "open", "emoji_tools": False,
        })
        assert cfg.get_symbol("activity", "x") == "→"
        assert cfg.layout == "open"
        assert cfg.emoji_tools is False

    def test_fields_inherit_from_default_when_missing(self):
        from janus_cli.skin_engine import _BUILTIN_SKINS, _build_skin_config
        cfg = _build_skin_config({"name": "bare"})
        d = _BUILTIN_SKINS["default"]
        assert cfg.layout == d.get("layout", "panel")
        assert cfg.emoji_tools is d.get("emoji_tools", True)

    def test_invalid_symbols_section_ignored(self):
        from janus_cli.skin_engine import _build_skin_config
        cfg = _build_skin_config({"name": "t", "symbols": "not-a-dict"})
        assert cfg.symbols == {}
```

- [ ] **Step 2: Run to verify failure**

Run: `scripts/run_tests.sh tests/janus_cli/test_skin_engine.py`
Expected: the 4 new tests FAIL (`TypeError`/`AttributeError`: unexpected fields).

- [ ] **Step 3: Implement.** In `janus_cli/skin_engine.py`:

(a) `SkinConfig` — add after `banner_hero`:

```python
    symbols: Dict[str, str] = field(default_factory=dict)  # symbol overrides (activity/ok/fail/bullet/prompt/gutter/rule)
    layout: str = "panel"        # "open" (minimal structures) | "panel" (legacy boxed structures)
    emoji_tools: bool = True     # emoji verb icons in tool lines

    def get_symbol(self, key: str, fallback: str = "") -> str:
        """Get a symbol override with fallback."""
        return self.symbols.get(key, fallback)
```

(b) `_build_skin_config` — add before the `return`:

```python
    symbol_overrides = _mapping_or_empty(data.get("symbols"), section="symbols", skin_name=skin_name)
```

and extend the constructor call:

```python
        symbols=symbol_overrides,
        layout=str(data.get("layout", default.get("layout", "panel"))),
        emoji_tools=bool(data.get("emoji_tools", default.get("emoji_tools", True))),
```

(c) In the `"default"` builtin dict (after `"tool_prefix": "┊",`) add — explicitly pinning current behavior pre-flip:

```python
        "layout": "panel",
        "emoji_tools": True,
```

(d) Module docstring: in the SKIN YAML SCHEMA section, after the `tool_emojis:` block, add:

```
    # Structures (increment-1 additions; all optional)
    symbols:                # override minimal symbols by name
      activity: "▸"         # tool line marker (also: ok, fail, bullet, prompt, gutter, rule)
    layout: open            # open (minimal structures) | panel (legacy boxed structures)
    emoji_tools: false      # emoji verb icons in tool lines (classic: true)
```

- [ ] **Step 4: Run tests**

Run: `scripts/run_tests.sh tests/janus_cli/test_skin_engine.py`
Expected: PASS (all, including pre-existing).

- [ ] **Step 5: Commit**

```bash
git add janus_cli/skin_engine.py tests/janus_cli/test_skin_engine.py
git commit -m "feat(skins): additive schema — symbols, layout, emoji_tools [redesign 1.1]

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 2: `classic` built-in skin (verbatim preservation)

**Files:**
- Modify: `janus_cli/skin_engine.py` (`_BUILTIN_SKINS`, insert `"classic"` right after `"default"`)
- Test: `tests/janus_cli/test_classic_skin.py` (create)

**Interfaces:**
- Produces: built-in skin `classic`. Guarded strings later tasks rely on: goodbye `"Until next time. ⟡"`, help header `"(^_^)? Available Commands"`, response label `" ⟡ Janus "`, tool prefix `"┊"`, kawaii spinner faces.

- [ ] **Step 1: Write the failing tests** — create `tests/janus_cli/test_classic_skin.py`:

```python
"""Classic-skin verbatim guards.

`classic` preserves the pre-redesign default look EXACTLY — these tests
intentionally pin exact strings (that pinning IS the feature: it guards the
"/skin classic restores the old look" promise, not implementation drift).
"""
from janus_cli.skin_engine import load_skin


def test_classic_exists_and_is_panel_layout_with_emoji():
    s = load_skin("classic")
    assert s.name == "classic"
    assert s.layout == "panel"
    assert s.emoji_tools is True


def test_classic_branding_matches_old_default_verbatim():
    s = load_skin("classic")
    assert s.get_branding("goodbye") == "Until next time. ⟡"
    assert s.get_branding("response_label") == " ⟡ Janus "
    assert s.get_branding("help_header") == "(^_^)? Available Commands"
    assert s.get_branding("prompt_symbol") == "❯"
    assert s.tool_prefix == "┊"


def test_classic_colors_match_old_default_verbatim():
    s = load_skin("classic")
    assert s.get_color("banner_title") == "#FFD700"
    assert s.get_color("banner_border") == "#CD7F32"
    assert s.get_color("ui_accent") == "#FFBF00"
    assert s.get_color("banner_text") == "#FFF8DC"


def test_classic_carries_the_kawaii_spinner():
    """The kawaii faces move INTO classic data so the display.py fallback can
    go minimal later without changing classic behavior."""
    s = load_skin("classic")
    assert "(⌐■_■)" in s.spinner.get("thinking_faces", [])
    assert "(｡◕‿◕｡)" in s.spinner.get("waiting_faces", [])
    assert "pondering" in s.spinner.get("thinking_verbs", [])
```

- [ ] **Step 2: Run to verify failure**

Run: `scripts/run_tests.sh tests/janus_cli/test_classic_skin.py`
Expected: FAIL — `load_skin("classic")` falls back to default (warning logged), assertions on layout/spinner fail.

- [ ] **Step 3: Implement.** In `_BUILTIN_SKINS`, insert after the `"default"` entry a `"classic"` entry that is a **complete copy** of the current `"default"` values (do not rely on inheritance — the default gets replaced in Task 5): copy the entire `colors` dict verbatim (lines ~168–185), plus:

```python
    "classic": {
        "name": "classic",
        "description": "The pre-redesign Janus look — gold and kawaii",
        "colors": {
            # verbatim copy of the pre-redesign default colors dict:
            "banner_border": "#CD7F32",
            "banner_title": "#FFD700",
            "banner_accent": "#FFBF00",
            "banner_dim": "#B8860B",
            "banner_text": "#FFF8DC",
            "ui_accent": "#FFBF00",
            "ui_label": "#DAA520",
            "ui_ok": "#4caf50",
            "ui_error": "#ef5350",
            "ui_warn": "#ffa726",
            "prompt": "#FFF8DC",
            "input_rule": "#CD7F32",
            "response_border": "#FFD700",
            "status_bar_bg": "#1a1a2e",
            "session_label": "#DAA520",
            "session_border": "#8B8682",
        },
        "spinner": {
            # the KawaiiSpinner hardcoded defaults, moved into skin data so the
            # code fallback can go minimal without changing classic:
            "waiting_faces": [
                "(｡◕‿◕｡)", "(◕‿◕✿)", "٩(◕‿◕｡)۶", "(✿◠‿◠)", "( ˘▽˘)っ",
                "♪(´ε` )", "(◕ᴗ◕✿)", "ヾ(＾∇＾)", "(≧◡≦)", "(★ω★)",
            ],
            "thinking_faces": [
                "(｡•́︿•̀｡)", "(◔_◔)", "(¬‿¬)", "( •_•)>⌐■-■", "(⌐■_■)",
                "(´･_･`)", "◉_◉", "(°ロ°)", "( ˘⌣˘)♡", "ヽ(>∀<☆)☆",
                "٩(๑❛ᴗ❛๑)۶", "(⊙_⊙)", "(¬_¬)", "( ͡° ͜ʖ ͡°)", "ಠ_ಠ",
            ],
            "thinking_verbs": [
                "pondering", "contemplating", "musing", "cogitating", "ruminating",
                "deliberating", "mulling", "reflecting", "processing", "reasoning",
                "analyzing", "computing", "synthesizing", "formulating", "brainstorming",
            ],
        },
        "branding": {
            "agent_name": "Janus",
            "welcome": "Welcome to Janus! Type your message or /help for commands.",
            "goodbye": "Until next time. ⟡",
            "response_label": " ⟡ Janus ",
            "prompt_symbol": "❯",
            "help_header": "(^_^)? Available Commands",
        },
        "tool_prefix": "┊",
        "layout": "panel",
        "emoji_tools": True,
    },
```

- [ ] **Step 4: Run tests**

Run: `scripts/run_tests.sh tests/janus_cli/test_classic_skin.py tests/janus_cli/test_skin_engine.py`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add janus_cli/skin_engine.py tests/janus_cli/test_classic_skin.py
git commit -m "feat(skins): classic built-in — the pre-redesign look, verbatim [redesign 1.2]

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 3: `janus_cli/design.py` — tokens, symbols, layout

**Files:**
- Create: `janus_cli/design.py`
- Test: `tests/janus_cli/test_design.py` (create)

**Interfaces:**
- Produces: `tok(name) -> str` (hex or "" when color off), `sym(name) -> str`, `layout() -> str`, `styled(text, token, bold=False) -> str` (Rich markup or plain). Token names: `accent fg muted faint ok warn error`. Symbol names: `activity ok fail bullet prompt gutter rule`.
- Consumes: `janus_cli.skin_engine.get_active_skin` (Task 1 fields), `janus_cli.colors.should_use_color`.

- [ ] **Step 1: Write the failing tests** — create `tests/janus_cli/test_design.py`:

```python
"""Design-token layer (janus_cli/design.py) — the single home of styling."""
import pytest

from janus_cli import design
from janus_cli.skin_engine import set_active_skin


@pytest.fixture(autouse=True)
def _reset_skin():
    set_active_skin("default")
    yield
    set_active_skin("default")


def test_tokens_resolve_from_active_skin(monkeypatch):
    monkeypatch.setattr(design, "_color_on", lambda: True)
    assert design.tok("accent") == "#FFBF00"   # old default ui_accent (pre-flip)
    assert design.tok("ok") == "#4caf50"


def test_tokens_empty_when_color_off(monkeypatch):
    monkeypatch.setattr(design, "_color_on", lambda: False)
    assert design.tok("accent") == ""
    assert design.tok("error") == ""


def test_unknown_token_is_empty_not_a_crash(monkeypatch):
    monkeypatch.setattr(design, "_color_on", lambda: True)
    assert design.tok("nonsense") == ""


def test_symbols_default_to_minimal_set(monkeypatch):
    monkeypatch.setattr(design, "_unicode_ok", lambda: True)
    assert design.sym("activity") == "▸"
    assert design.sym("fail") == "✗"
    assert design.sym("gutter") == "▍"


def test_symbols_ascii_fallback(monkeypatch):
    monkeypatch.setattr(design, "_unicode_ok", lambda: False)
    assert design.sym("activity") == ">"
    assert design.sym("ok") == "ok"
    assert design.sym("rule") == "-"


def test_skin_can_override_symbols(monkeypatch):
    monkeypatch.setattr(design, "_unicode_ok", lambda: True)
    from janus_cli.skin_engine import get_active_skin
    get_active_skin().symbols["activity"] = "→"
    assert design.sym("activity") == "→"


def test_layout_reads_active_skin():
    assert design.layout() == "panel"          # pre-flip default
    set_active_skin("classic")
    assert design.layout() == "panel"


def test_styled_wraps_markup_only_when_colored(monkeypatch):
    monkeypatch.setattr(design, "_color_on", lambda: True)
    assert design.styled("hi", "accent") == "[#FFBF00]hi[/]"
    assert design.styled("hi", "accent", bold=True) == "[bold #FFBF00]hi[/]"
    monkeypatch.setattr(design, "_color_on", lambda: False)
    assert design.styled("hi", "accent") == "hi"
```

- [ ] **Step 2: Run to verify failure**

Run: `scripts/run_tests.sh tests/janus_cli/test_design.py`
Expected: FAIL — `ModuleNotFoundError: janus_cli.design`.

- [ ] **Step 3: Implement** — create `janus_cli/design.py`:

```python
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
```

- [ ] **Step 4: Run tests**

Run: `scripts/run_tests.sh tests/janus_cli/test_design.py`
Expected: PASS. Also: `ruff check janus_cli/design.py` → clean.

- [ ] **Step 5: Commit**

```bash
git add janus_cli/design.py tests/janus_cli/test_design.py
git commit -m "feat(design): token/symbol layer over the skin engine [redesign 1.3]

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 4: design.py render helpers — notices, GutterBlock, response_block

**Files:**
- Modify: `janus_cli/design.py` (append)
- Test: `tests/janus_cli/test_design.py` (append)

**Interfaces:**
- Produces:
  - `ok(msg) / warn(msg) / error(msg) / note(msg) -> str` — formatted one-line notices (returned, not printed; callers print).
  - `rule(width=40) -> str`, `header(text) -> str`.
  - `GutterBlock(renderable, gutter_style="")` — Rich renderable, left accent bar.
  - `response_block(content, *, label, border_hex, text_hex, width, attribution="") -> renderable` — Panel (panel layout, byte-compatible with today's kwargs) or gutter block (open layout).
- Consumes: Task 3 `tok/sym/layout/styled`.

- [ ] **Step 1: Write the failing tests** (append to `tests/janus_cli/test_design.py`):

```python
def test_notices_carry_semantic_symbols(monkeypatch):
    monkeypatch.setattr(design, "_color_on", lambda: True)
    monkeypatch.setattr(design, "_unicode_ok", lambda: True)
    assert design.ok("saved").startswith("[#")          # colored
    assert "✓" in design.ok("saved") and "saved" in design.ok("saved")
    assert "!" in design.warn("careful")
    assert "✗" in design.error("broke")
    assert "●" in design.note("fyi")


def test_notices_plain_when_color_off(monkeypatch):
    monkeypatch.setattr(design, "_color_on", lambda: False)
    monkeypatch.setattr(design, "_unicode_ok", lambda: True)
    assert design.error("broke") == "✗ broke"


def test_rule_and_header(monkeypatch):
    monkeypatch.setattr(design, "_color_on", lambda: False)
    monkeypatch.setattr(design, "_unicode_ok", lambda: True)
    assert design.rule(10) == "─" * 10
    assert design.header("commands") == "commands"


def test_response_block_panel_layout_returns_panel():
    from rich.panel import Panel
    set_active_skin("classic")
    block = design.response_block(
        "body", label=" ⟡ Janus ", border_hex="#FFD700",
        text_hex="#FFF8DC", width=80)
    assert isinstance(block, Panel)
    assert block.title == "[#FFD700 bold] ⟡ Janus [/]"


def test_response_block_panel_layout_merges_attribution():
    from rich.panel import Panel
    set_active_skin("classic")
    block = design.response_block(
        "body", label=" ⟡ Janus ", border_hex="#FFD700",
        text_hex="#FFF8DC", width=80, attribution="(background #3)")
    assert isinstance(block, Panel)
    assert "(background #3)" in str(block.title)


def test_response_block_open_layout_uses_gutter(monkeypatch):
    from rich.console import Console
    monkeypatch.setattr(design, "layout", lambda: "open")
    monkeypatch.setattr(design, "_unicode_ok", lambda: True)
    block = design.response_block(
        "hello world", label=" janus ", border_hex="#E3A857",
        text_hex="", width=60)
    con = Console(record=True, width=60, force_terminal=False)
    con.print(block)
    out = con.export_text()
    assert "▍" in out
    assert "hello world" in out
    assert "╭" not in out and "─" * 10 not in out   # no box frame


def test_gutter_block_prefixes_every_line(monkeypatch):
    from rich.console import Console
    monkeypatch.setattr(design, "_unicode_ok", lambda: True)
    con = Console(record=True, width=40, force_terminal=False)
    con.print(design.GutterBlock("line one\nline two"))
    out = con.export_text()
    lines = [l for l in out.splitlines() if l.strip()]
    assert all("▍" in l for l in lines)
```

- [ ] **Step 2: Run to verify failure**

Run: `scripts/run_tests.sh tests/janus_cli/test_design.py`
Expected: new tests FAIL with `AttributeError` (missing helpers).

- [ ] **Step 3: Implement** (append to `janus_cli/design.py`):

```python
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
```

**Note:** in `test_response_block_panel_layout_returns_panel` the expected title is exactly `f"[{border_hex} bold]{label}[/]"` — no space normalization when attribution is empty. Verify the implementation matches (it does: the `attribution` branch is skipped).

- [ ] **Step 4: Run tests**

Run: `scripts/run_tests.sh tests/janus_cli/test_design.py`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add janus_cli/design.py tests/janus_cli/test_design.py
git commit -m "feat(design): notices, rule/header, GutterBlock, response_block [redesign 1.4]

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 5: New minimal `default` skin (the data flip)

**Files:**
- Modify: `janus_cli/skin_engine.py` (`_BUILTIN_SKINS["default"]`)
- Test: `tests/janus_cli/test_skin_engine.py` (append)

**Interfaces:**
- Produces: `default` skin with `layout: "open"`, `emoji_tools: False`, accent `#E3A857`, minimal branding. Every later structural task keys off these values.

- [ ] **Step 1: Write the failing tests** (append to `tests/janus_cli/test_skin_engine.py`):

```python
class TestMinimalDefault:
    def test_default_is_open_layout_no_emoji(self):
        from janus_cli.skin_engine import load_skin
        s = load_skin("default")
        assert s.layout == "open"
        assert s.emoji_tools is False

    def test_default_accent_is_refined_gold(self):
        from janus_cli.skin_engine import load_skin
        s = load_skin("default")
        assert s.get_color("ui_accent") == "#E3A857"
        assert s.get_color("banner_title") == "#E3A857"

    def test_default_branding_is_lowercase_calm(self):
        from janus_cli.skin_engine import load_skin
        s = load_skin("default")
        for key in ("welcome", "goodbye", "help_header", "response_label"):
            v = s.get_branding(key)
            assert v == v.lower(), f"{key} not lowercase: {v!r}"
            assert "!" not in v
        # no emoji / kaomoji in default branding
        assert "⚕" not in s.get_branding("response_label")
        assert "(^_^)" not in s.get_branding("help_header")

    def test_default_supplies_no_spinner_faces(self):
        from janus_cli.skin_engine import load_skin
        s = load_skin("default")
        assert s.spinner.get("waiting_faces", []) == []
        assert s.spinner.get("thinking_faces", []) == []

    def test_classic_unaffected_by_the_flip(self):
        from janus_cli.skin_engine import load_skin
        s = load_skin("classic")
        assert s.get_color("ui_accent") == "#FFBF00"
        assert s.layout == "panel"
```

- [ ] **Step 2: Run to verify failure**

Run: `scripts/run_tests.sh tests/janus_cli/test_skin_engine.py`
Expected: `TestMinimalDefault` FAILS (old values); everything else PASSES.

- [ ] **Step 3: Implement.** Replace the `"default"` entry in `_BUILTIN_SKINS` with:

```python
    "default": {
        "name": "default",
        "description": "Janus minimal — monochrome with refined gold",
        "colors": {
            "banner_border": "#5C5C5C",
            "banner_title": "#E3A857",
            "banner_accent": "#E3A857",
            "banner_dim": "#5C5C5C",
            "banner_text": "#C9C9C9",
            "ui_accent": "#E3A857",
            "ui_label": "#8A8A8A",
            "ui_ok": "#7CB87C",
            "ui_error": "#D47C7C",
            "ui_warn": "#D4A24E",
            "prompt": "#E3A857",
            "input_rule": "#3A3A3A",
            "response_border": "#E3A857",
            "status_bar_bg": "#1C1C1C",
            "status_bar_text": "#B8B8B8",
            "status_bar_strong": "#E3A857",
            "status_bar_dim": "#5C5C5C",
            "status_bar_good": "#7CB87C",
            "status_bar_warn": "#D4A24E",
            "status_bar_bad": "#D4A24E",
            "status_bar_critical": "#D47C7C",
            "session_label": "#8A8A8A",
            "session_border": "#5C5C5C",
            "completion_menu_bg": "#1C1C1C",
            "completion_menu_current_bg": "#2E2E2E",
            "completion_menu_meta_bg": "#1C1C1C",
            "completion_menu_meta_current_bg": "#2E2E2E",
        },
        "spinner": {},
        "branding": {
            "agent_name": "janus",
            "welcome": "type your message, or /help for commands.",
            "goodbye": "until next time.",
            "response_label": " janus ",
            "prompt_symbol": "❯",
            "help_header": "commands",
        },
        "tool_prefix": "▸",
        "layout": "open",
        "emoji_tools": False,
        "symbols": {},
    },
```

- [ ] **Step 4: Run the skin + design + display test files** (the flip ripples into inheritance):

Run: `scripts/run_tests.sh tests/janus_cli/test_skin_engine.py tests/janus_cli/test_classic_skin.py tests/janus_cli/test_design.py tests/agent/test_display.py tests/agent/test_display_emoji.py tests/janus_cli/test_banner.py`
Expected: skin/classic tests PASS. **`test_design.py` needs two edits** (old-default assertions): in `test_tokens_resolve_from_active_skin` change `"#FFBF00"` → `"#E3A857"`; in `test_layout_reads_active_skin` change the first assertion to `assert design.layout() == "open"` and in `test_styled_wraps_markup_only_when_colored` change `#FFBF00` → `#E3A857`. Display/banner tests: emoji_tools/layout aren't consulted by code yet, but any test asserting old default *colors/branding* must be updated to activate `classic` first (`set_active_skin("classic")`) — find them with the failure list, apply, re-run.

- [ ] **Step 5: Re-run until green, then commit**

```bash
git add janus_cli/skin_engine.py tests/janus_cli/test_skin_engine.py tests/janus_cli/test_design.py tests/agent/ tests/janus_cli/
git commit -m "feat(skins)!: minimal refined-gold default — old look is /skin classic [redesign 2.1]

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 6: Open banner layout

**Files:**
- Modify: `janus_cli/banner.py` (add `_build_open_banner`, dispatch at top of `build_welcome_banner` ~line 495)
- Test: `tests/janus_cli/test_banner.py` (append)

**Interfaces:**
- Consumes: `design.layout()`; `_skin_color()` (exists in banner.py); `janus_cli.__version__`; `_format_context_length` (exists); `get_available_skills` (exists).
- Produces: same public signature — `build_welcome_banner(console, model, cwd, tools, enabled_toolsets, session_id, get_toolset_for_tool, context_length)` now dispatches on layout.

- [ ] **Step 1: Write the failing tests** (append to `tests/janus_cli/test_banner.py`; match the file's existing fixture style for consoles — if it has none, use this):

```python
class TestOpenBanner:
    def _render(self, skin_name):
        from rich.console import Console
        from janus_cli.skin_engine import set_active_skin
        from janus_cli.banner import build_welcome_banner
        set_active_skin(skin_name)
        con = Console(record=True, width=100, force_terminal=False)
        tools = [{"function": {"name": "terminal"}}, {"function": {"name": "read_file"}}]
        build_welcome_banner(
            con, model="anthropic/claude-opus-4-8", cwd="/tmp/proj",
            tools=tools, enabled_toolsets=["core"], session_id="a4f2c9",
            get_toolset_for_tool=lambda n: "core", context_length=1000000)
        return con.export_text()

    def test_open_banner_is_compact_and_emoji_free(self):
        out = self._render("default")
        assert "janus" in out
        assert "claude-opus-4-8" in out
        assert "session a4f2c9" in out
        assert "2 tools" in out
        assert "Available Tools" not in out       # tool dump collapsed to counts
        assert "▐" not in out                     # no emblem art
        assert len(out.splitlines()) < 12         # compact

    def test_classic_banner_still_renders_the_panel(self):
        out = self._render("classic")
        assert "Available Tools" in out
```

- [ ] **Step 2: Run to verify failure**

Run: `scripts/run_tests.sh tests/janus_cli/test_banner.py`
Expected: `test_open_banner_is_compact_and_emoji_free` FAILS (old panel renders); classic test PASSES.

- [ ] **Step 3: Implement.** In `janus_cli/banner.py`, insert immediately above `build_welcome_banner`:

```python
def _build_open_banner(console, model: str, cwd: str,
                       tools: List[dict] = None,
                       session_id: str = None,
                       get_toolset_for_tool=None,
                       context_length: int = None):
    """Minimal open-layout banner (default skin): wordmark, one rule, facts.

    The full tool inventory lives behind /tools — the banner shows counts and
    points there only when something needs attention.
    """
    from model_tools import check_tool_availability
    if get_toolset_for_tool is None:
        from model_tools import get_toolset_for_tool
    tools = tools or []

    accent = _skin_color("ui_accent", "#E3A857")
    muted = _skin_color("ui_label", "#8A8A8A")
    faint = _skin_color("banner_dim", "#5C5C5C")

    try:
        from janus_cli import __version__ as _ver
    except Exception:
        _ver = ""

    model_short = model.split("/")[-1] if "/" in model else model
    if model_short.endswith(".gguf"):
        model_short = model_short[:-5]
    if len(model_short) > 40:
        model_short = model_short[:37] + "..."

    toolset_names = {get_toolset_for_tool(t["function"]["name"]) or "other" for t in tools}
    _, unavailable_toolsets = check_tool_availability(quiet=True)
    n_unavailable = sum(len(i.get("tools", [])) for i in unavailable_toolsets)
    try:
        n_skills = sum(len(v) for v in get_available_skills().values())
    except Exception:
        n_skills = 0

    width = max(20, min(60, (console.width or 80) - 4))
    console.print()
    ver_part = f" [{faint}]{_ver}[/]" if _ver else ""
    console.print(f"  [bold {accent}]janus[/]{ver_part}")
    console.print(f"  [{faint}]{'─' * width}[/]")
    ctx = f" · {_format_context_length(context_length)} context" if context_length else ""
    console.print(f"  [{muted}]{model_short}{ctx} · {cwd}[/]")
    facts = []
    if session_id:
        facts.append(f"session {session_id}")
    facts.append(f"{len(toolset_names)} toolsets")
    facts.append(f"{len(tools)} tools")
    if n_skills:
        facts.append(f"{n_skills} skills")
    console.print(f"  [{faint}]{' · '.join(facts)}[/]")
    if os.getenv("JANUS_YOLO_MODE"):
        err = _skin_color("ui_error", "#D47C7C")
        console.print(f"  [bold {err}]✗ yolo mode — approval prompts bypassed[/]")
    if n_unavailable:
        warn = _skin_color("ui_warn", "#D4A24E")
        console.print(f"  [{warn}]! {n_unavailable} tools unavailable · /tools for details[/]")
    console.print()
```

Then at the very top of `build_welcome_banner`'s body (before the `from model_tools import ...` line):

```python
    try:
        from janus_cli.design import layout as _design_layout
        if _design_layout() == "open":
            return _build_open_banner(
                console, model, cwd, tools=tools, session_id=session_id,
                get_toolset_for_tool=get_toolset_for_tool,
                context_length=context_length)
    except Exception:
        pass  # any design/skin failure falls back to the legacy panel banner
```

- [ ] **Step 4: Run tests**

Run: `scripts/run_tests.sh tests/janus_cli/test_banner.py tests/janus_cli/test_banner_skills.py tests/janus_cli/test_banner_git_state.py tests/janus_cli/test_banner_pip_update.py`
Expected: PASS. Any pre-existing banner test asserting panel content under the default skin: pin it to `classic` (add `set_active_skin("classic")` at its top) — the panel path is now classic's.

- [ ] **Step 5: Commit**

```bash
git add janus_cli/banner.py tests/janus_cli/
git commit -m "feat(banner): open minimal layout for the default skin [redesign 2.2]

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 7: One-time redesign notice

**Files:**
- Create: `janus_cli/skin_notice.py`
- Modify: `cli.py` (immediately after the `build_welcome_banner(` call at ~line 5363)
- Test: `tests/janus_cli/test_skin_notice.py` (create)

**Interfaces:**
- Produces: `maybe_show_redesign_notice(print_fn) -> bool` (True when shown).
- Consumes: `get_janus_home()`, `get_active_skin_name()`, `design.note`.

- [ ] **Step 1: Write the failing tests** — create `tests/janus_cli/test_skin_notice.py`:

```python
"""One-time 'new look' notice after the redesign ships."""
from janus_cli import skin_notice
from janus_cli.skin_engine import set_active_skin


def test_shows_once_then_never_again():
    set_active_skin("default")
    lines = []
    assert skin_notice.maybe_show_redesign_notice(print_fn=lines.append) is True
    assert any("/skin classic" in str(l) for l in lines)
    lines.clear()
    assert skin_notice.maybe_show_redesign_notice(print_fn=lines.append) is False
    assert lines == []


def test_silent_when_user_already_switched_skins():
    set_active_skin("classic")
    lines = []
    try:
        assert skin_notice.maybe_show_redesign_notice(print_fn=lines.append) is False
        assert lines == []
    finally:
        set_active_skin("default")


def test_never_raises(monkeypatch):
    monkeypatch.setattr(skin_notice, "_stamp_path",
                        lambda: (_ for _ in ()).throw(RuntimeError("disk")))
    assert skin_notice.maybe_show_redesign_notice(print_fn=print) is False
```

- [ ] **Step 2: Run to verify failure**

Run: `scripts/run_tests.sh tests/janus_cli/test_skin_notice.py`
Expected: FAIL — module missing.

- [ ] **Step 3: Implement** — create `janus_cli/skin_notice.py`:

```python
"""One-time notice shown after the CLI redesign ships.

The redesign changes the default look for everyone; this tells each user —
exactly once — that the old look is one command away. Stamp-file pattern
(same as janus_cli/learning_onboarding.py): decide-to-show writes the stamp,
so the notice can never nag."""
from __future__ import annotations

from pathlib import Path


def _stamp_path() -> Path:
    from janus_constants import get_janus_home
    return get_janus_home() / "skins" / ".redesign-notice-shown"


def maybe_show_redesign_notice(print_fn=print) -> bool:
    """Show the one-time notice when the (new) default skin is active.
    Returns True when shown. Never raises."""
    try:
        from janus_cli.skin_engine import get_active_skin_name
        if get_active_skin_name() != "default":
            return False          # user already chose a skin — nothing to say
        stamp = _stamp_path()
        if stamp.exists():
            return False
        stamp.parent.mkdir(parents=True, exist_ok=True)
        stamp.write_text("1\n", encoding="utf-8")
        from janus_cli.design import note
        print_fn(f"  {note('new look — /skin classic restores the previous one')}")
        return True
    except Exception:
        return False
```

Then in `cli.py`, find the `build_welcome_banner(` call at ~line 5363 and add immediately after its closing paren (same indentation):

```python
            try:
                from janus_cli.skin_notice import maybe_show_redesign_notice
                maybe_show_redesign_notice(print_fn=ChatConsole().print)
            except Exception:
                pass
```

- [ ] **Step 4: Run tests**

Run: `scripts/run_tests.sh tests/janus_cli/test_skin_notice.py`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add janus_cli/skin_notice.py cli.py tests/janus_cli/test_skin_notice.py
git commit -m "feat(cli): one-time redesign notice — /skin classic revert hint [redesign 2.3]

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 8: Minimal tool lines

**Files:**
- Modify: `agent/display.py` (`get_cute_tool_message` ~line 861: only the `_wrap` closure + two new module helpers; **zero per-tool branches change**)
- Test: `tests/agent/test_display_minimal_lines.py` (create)

**Interfaces:**
- Consumes: `design.sym`; `SkinConfig.emoji_tools` (Task 1); every legacy line's fixed shape `"┊ <emoji> <verb> <detail>  <dur>"`.
- Produces: minimal-mode lines `"<mark> <verb:<10><detail>  <dur>"` (plain text — this path never emitted Rich markup and still doesn't). Classic/emoji mode byte-identical to today.

- [ ] **Step 1: Write the failing tests** — create `tests/agent/test_display_minimal_lines.py`:

```python
"""Minimal tool lines (default skin): emoji-free aligned ledger.
Classic keeps the legacy emoji format byte-for-byte."""
import re

from agent.display import get_cute_tool_message
from janus_cli.skin_engine import set_active_skin


def teardown_function():
    set_active_skin("default")


def test_minimal_line_is_emoji_free_and_aligned():
    set_active_skin("default")
    line = get_cute_tool_message("terminal", {"command": "git status"}, 0.21)
    assert line.startswith("▸ ")
    assert "$" in line                       # verb preserved
    assert "git status" in line
    assert line.rstrip().endswith("0.2s")
    assert "💻" not in line and "┊" not in line


def test_minimal_failure_line_uses_fail_mark():
    set_active_skin("default")
    line = get_cute_tool_message(
        "terminal", {"command": "boom"}, 0.10,
        result='{"error": "exit 1"}')
    assert line.startswith("✗ ")


def test_minimal_line_never_contains_emoji_for_any_known_tool():
    set_active_skin("default")
    emoji_re = re.compile(r"[\U0001F000-\U0001FAFF☀-➿️]")
    cases = [
        ("web_search", {"query": "rust"}), ("read_file", {"path": "/a/b.py"}),
        ("write_file", {"path": "/a/b.py"}), ("patch", {"path": "/a/b.py"}),
        ("search_files", {"pattern": "TODO"}), ("browser_navigate", {"url": "https://x.io"}),
        ("memory", {"action": "add", "target": "user", "content": "c"}),
        ("execute_code", {"code": "print(1)"}), ("delegate_task", {"goal": "g"}),
        ("unknown_tool_xyz", {}),
    ]
    for name, args in cases:
        line = get_cute_tool_message(name, args, 0.5)
        assert not emoji_re.search(line), f"{name}: {line!r}"


def test_classic_line_is_byte_identical_to_legacy():
    set_active_skin("classic")
    line = get_cute_tool_message("terminal", {"command": "git status"}, 0.21)
    assert line == "┊ 💻 $         git status  0.2s"


def test_classic_search_line_verbatim():
    set_active_skin("classic")
    line = get_cute_tool_message("web_search", {"query": "rust"}, 1.0)
    assert line == "┊ 🔍 search    rust  1.0s"
```

- [ ] **Step 2: Run to verify failure**

Run: `scripts/run_tests.sh tests/agent/test_display_minimal_lines.py`
Expected: minimal tests FAIL (emoji lines returned); classic tests PASS.

- [ ] **Step 3: Implement.** In `agent/display.py`:

(a) Add two module-level helpers above `get_cute_tool_message`:

```python
def _emoji_tool_lines_enabled() -> bool:
    """Whether the active skin wants legacy emoji tool lines (classic: True)."""
    try:
        skin = _get_skin()
        return bool(getattr(skin, "emoji_tools", True)) if skin else True
    except Exception:
        return True


def _split_legacy_tool_line(line: str, dur: str) -> tuple[str, str]:
    """Parse the fixed legacy shape '┊ <emoji> <verb> <detail>  <dur>' into
    (verb, detail). Every branch of get_cute_tool_message emits this shape,
    so the minimal renderer can re-render without touching the branches."""
    body = line[2:] if line.startswith("┊ ") else line
    parts = body.split(None, 2)
    if len(parts) < 2:
        return body.strip(), ""
    verb = parts[1]
    rest = parts[2] if len(parts) > 2 else ""
    if rest == dur:
        return verb, ""
    suffix = f"  {dur}"
    if rest.endswith(suffix):
        rest = rest[: -len(suffix)]
    return verb, rest.rstrip()
```

(b) Replace the `_wrap` closure inside `get_cute_tool_message` (currently the `def _wrap(line: str) -> str:` block) with:

```python
    def _wrap(line: str) -> str:
        """Apply skin prefix + failure suffix (legacy path, byte-identical),
        or re-render the fixed legacy shape as a minimal emoji-free line."""
        if _emoji_tool_lines_enabled():
            if skin_prefix != "┊":
                line = line.replace("┊", skin_prefix, 1)
            if not is_failure:
                return line
            return f"{line}{failure_suffix}"
        from janus_cli.design import sym
        verb, detail = _split_legacy_tool_line(line, dur)
        mark = sym("fail") if is_failure else sym("activity")
        body = f"{mark} {verb:<10}{detail}  {dur}" if detail else f"{mark} {verb:<10}{dur}"
        if not is_failure:
            return body
        return f"{body}{failure_suffix}"
```

- [ ] **Step 4: Run the display test files**

Run: `scripts/run_tests.sh tests/agent/test_display_minimal_lines.py tests/agent/test_display.py tests/agent/test_display_emoji.py tests/agent/test_display_todo_progress.py tests/agent/test_display_tool_failure.py`
Expected: new file PASSES. Pre-existing display tests asserting legacy emoji lines under the default skin now FAIL — fix each by adding `set_active_skin("classic")` at the top (plus matching teardown resetting to `"default"`), which converts them into classic-verbatim guards. Re-run until green.

- [ ] **Step 5: Commit**

```bash
git add agent/display.py tests/agent/
git commit -m "feat(display): minimal emoji-free tool lines for the default skin [redesign 3.1]

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 9: Minimal spinner

**Files:**
- Modify: `agent/display.py` (KawaiiSpinner class constants/fallbacks ~lines 574-628, `_animate` elapsed format ~line 721-723), `agent/tool_executor.py` (face composition at lines 549, 1081, 1110, 1143, 1174), `agent/conversation_loop.py` (lines 1201-1207)
- Test: `tests/agent/test_display_minimal_lines.py` (append)

**Interfaces:**
- Consumes: classic skin's spinner faces (Task 2), `design.layout()`.
- Produces: under skins with no faces, `get_waiting_faces()/get_thinking_faces()` return `[""]` and `get_thinking_verbs()` returns `["thinking"]`; composition sites skip empty faces; open-layout elapsed renders `· 4s` instead of `(4.2s)`.

- [ ] **Step 1: Write the failing tests** (append to `tests/agent/test_display_minimal_lines.py`):

```python
def test_spinner_faces_minimal_under_default_skin():
    from agent.display import KawaiiSpinner
    set_active_skin("default")
    assert KawaiiSpinner.get_waiting_faces() == [""]
    assert KawaiiSpinner.get_thinking_faces() == [""]
    assert KawaiiSpinner.get_thinking_verbs() == ["thinking"]


def test_spinner_faces_kawaii_under_classic_skin():
    from agent.display import KawaiiSpinner
    set_active_skin("classic")
    assert "(⌐■_■)" in KawaiiSpinner.get_thinking_faces()
    assert "pondering" in KawaiiSpinner.get_thinking_verbs()


def test_compose_spinner_message_skips_empty_face():
    from agent.display import compose_spinner_message
    assert compose_spinner_message("", "running 3 tools") == "running 3 tools"
    assert compose_spinner_message("(◕‿◕)", "running 3 tools") == "(◕‿◕) ⚡ running 3 tools"
    assert compose_spinner_message("", "thinking...") == "thinking..."
```

- [ ] **Step 2: Run to verify failure**

Run: `scripts/run_tests.sh tests/agent/test_display_minimal_lines.py`
Expected: new tests FAIL (kawaii fallbacks; `compose_spinner_message` missing).

- [ ] **Step 3: Implement.**

(a) `agent/display.py` — in `KawaiiSpinner`, change the three fallback returns (keep the KAWAII_*/THINKING_VERBS constants — classic data was copied from them, and third-party skins may rely on the constants existing):

```python
    MINIMAL_WAITING = [""]      # no face — the frame + message carry the state
    MINIMAL_THINKING = [""]
    MINIMAL_VERBS = ["thinking"]
```

and in `get_waiting_faces` replace `return cls.KAWAII_WAITING` with `return cls.MINIMAL_WAITING`; in `get_thinking_faces` replace `return cls.KAWAII_THINKING` with `return cls.MINIMAL_THINKING`; in `get_thinking_verbs` replace `return cls.THINKING_VERBS` with `return cls.MINIMAL_VERBS`.

(b) `agent/display.py` — add a module-level composition helper (near `get_skin_tool_prefix`):

```python
def compose_spinner_message(face: str, message: str) -> str:
    """Join an optional spinner face with a message. Empty face (minimal
    skins) yields the bare message; a real face keeps the legacy '⚡' joiner
    so classic output is unchanged."""
    if not face:
        return message
    if message.startswith("running "):
        return f"{face} ⚡ {message}"
    return f"{face} {message}"
```

(c) `agent/display.py` `_animate` — replace the two line-format lines (721-723):

```python
            try:
                from janus_cli.design import layout as _dlayout
                _open = _dlayout() == "open"
            except Exception:
                _open = False
            elapsed_txt = f"· {elapsed:.0f}s" if _open else f"({elapsed:.1f}s)"
            if wings:
                left, right = wings[self.frame_idx % len(wings)]
                line = f"  {left} {frame} {self.message} {right} {elapsed_txt}"
            else:
                line = f"  {frame} {self.message} {elapsed_txt}"
```

(move the layout probe ABOVE the `while self.running:` loop next to the wings caching so it isn't computed per frame — cache as `_open = ...` once).

(d) `agent/tool_executor.py` line 549-550 — replace:

```python
        face = random.choice(KawaiiSpinner.get_waiting_faces())
        spinner = KawaiiSpinner(f"{face} ⚡ running {num_tools} tools concurrently", spinner_type='dots', print_fn=agent._print_fn)
```

with:

```python
        from agent.display import compose_spinner_message
        face = random.choice(KawaiiSpinner.get_waiting_faces())
        spinner = KawaiiSpinner(compose_spinner_message(face, f"running {num_tools} tools concurrently"), spinner_type='dots', print_fn=agent._print_fn)
```

At lines 1081, 1110, 1143, 1174 apply the same substitution: each site currently interpolates `f"{face} ..."` into a spinner/message — wrap with `compose_spinner_message(face, <the message without the face and without the '⚡ '>)`. Read each site first; the transform is: `f"{face} ⚡ X"` → `compose_spinner_message(face, "X")`, and `f"{face} X"` → `compose_spinner_message(face, "X")`.

(e) `agent/conversation_loop.py` lines 1201-1207 — replace:

```python
            face = random.choice(KawaiiSpinner.get_thinking_faces())
            verb = random.choice(KawaiiSpinner.get_thinking_verbs())
            if agent.thinking_callback:
                agent.thinking_callback(f"{face} {verb}...")
```

with:

```python
            from agent.display import compose_spinner_message
            face = random.choice(KawaiiSpinner.get_thinking_faces())
            verb = random.choice(KawaiiSpinner.get_thinking_verbs())
            if agent.thinking_callback:
                agent.thinking_callback(compose_spinner_message(face, f"{verb}..."))
```

(and the sibling raw-KawaiiSpinner branch below it composes its message the same way if it interpolates `face`).

- [ ] **Step 4: Run tests**

Run: `scripts/run_tests.sh tests/agent/test_display_minimal_lines.py tests/agent/test_display.py tests/run_agent/ tests/agent/test_tool_executor.py 2>/dev/null || scripts/run_tests.sh tests/agent/test_display_minimal_lines.py tests/agent/test_display.py`
Expected: PASS (fix any face-assertion tests by pinning classic, as in Task 8).

- [ ] **Step 5: Commit**

```bash
git add agent/display.py agent/tool_executor.py agent/conversation_loop.py tests/agent/
git commit -m "feat(display): minimal spinner — no faces, calm verb, clean elapsed [redesign 3.2]

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 10: Response presentation (Panel sites + streaming frame)

**Files:**
- Modify: `cli.py` — Panel sites at ~9485 and ~12806; streaming frame at ~4678 (header), ~4686 (`_emit_one` pad), ~4778 and ~12799 (closers)
- Test: `tests/janus_cli/test_design.py` already covers `response_block`; add a cli-level smoke below.

**Interfaces:**
- Consumes: `design.response_block` (Task 4 exact signature), `design.layout`, `design.sym`, `design.tok`.

- [ ] **Step 1: Replace the main final-response Panel (~line 12806).** Current code:

```python
                    _chat_console = ChatConsole()
                    _chat_console.print(Panel(
                        _render_final_assistant_content(response, mode=self.final_response_markdown),
                        title=f"[{_resp_color} bold]{label}[/]",
                        title_align="left",
                        border_style=_resp_color,
                        style=_resp_text,
                        box=rich_box.HORIZONTALS,
                        padding=(1, 4),
                        width=self._scrollback_box_width(),
                    ))
```

New code:

```python
                    from janus_cli.design import response_block
                    _chat_console = ChatConsole()
                    _chat_console.print(response_block(
                        _render_final_assistant_content(response, mode=self.final_response_markdown),
                        label=label,
                        border_hex=_resp_color,
                        text_hex=_resp_text,
                        width=self._scrollback_box_width(),
                    ))
```

- [ ] **Step 2: Replace the background-task Panel (~line 9485).** Current code builds `title=f"[{_resp_color} bold]{label} (background #{task_num})[/]"`. New code:

```python
                    from janus_cli.design import response_block
                    _chat_console = ChatConsole()
                    _chat_console.print(response_block(
                        _render_final_assistant_content(response, mode=self.final_response_markdown),
                        label=label,
                        border_hex=_resp_color,
                        text_hex=_resp_text,
                        width=self._scrollback_box_width(),
                        attribution=f"(background #{task_num})",
                    ))
```

- [ ] **Step 3: Streaming frame.** The token-streaming path draws a manual box. Make it layout-aware:

(a) Header (~line 4678), currently:

```python
            _cprint(f"\n{_ACCENT}╭─{label}{'─' * max(fill - 1, 0)}╮{_RST}")
```

New:

```python
            from janus_cli.design import layout as _dlayout
            self._stream_open_layout = _dlayout() == "open"
            if self._stream_open_layout:
                _cprint("")   # open layout: a breath, no box
            else:
                _cprint(f"\n{_ACCENT}╭─{label}{'─' * max(fill - 1, 0)}╮{_RST}")
```

(b) Line emission — `_emit_one` (~line 4686), currently:

```python
        def _emit_one(printed_line: str) -> None:
            _cprint(f"{_STREAM_PAD}{_tc}{printed_line}{_RST}" if _tc else f"{_STREAM_PAD}{printed_line}")
```

New:

```python
        def _emit_one(printed_line: str) -> None:
            pad = _STREAM_PAD
            if getattr(self, "_stream_open_layout", False):
                from janus_cli.design import sym
                pad = f"  {_ACCENT}{sym('gutter')}{_RST} "
            _cprint(f"{pad}{_tc}{printed_line}{_RST}" if _tc else f"{pad}{printed_line}")
```

(c) Closers at ~4778 and ~12799, both currently:

```python
            _cprint(f"\n{_ACCENT}╰{'─' * (w - 2)}╯{_RST}")
```

New (both sites; note 12799's variant computes `w` just above — keep that line for the panel branch):

```python
            if getattr(self, "_stream_open_layout", False):
                _cprint("")
            else:
                _cprint(f"\n{_ACCENT}╰{'─' * (w - 2)}╯{_RST}")
```

- [ ] **Step 4: Add a smoke test** (append to `tests/janus_cli/test_design.py`):

```python
def test_response_block_open_never_draws_box_chars(monkeypatch):
    from rich.console import Console
    monkeypatch.setattr(design, "layout", lambda: "open")
    con = Console(record=True, width=70, force_terminal=False)
    con.print(design.response_block(
        "multi\nline\nbody", label=" janus ", border_hex="#E3A857",
        text_hex="", width=70))
    out = con.export_text()
    for ch in ("╭", "╮", "╰", "╯"):
        assert ch not in out
```

Run: `scripts/run_tests.sh tests/janus_cli/test_design.py`
Expected: PASS.

- [ ] **Step 5: Manual smoke + commit.** Manual check (visual): `printf 'say hi\n/exit\n' | timeout 60 python run_agent.py --quiet 2>/dev/null | head -30` — verify no box glyphs in the response under the default skin (skip if no credentials; the unit tests carry the gate).

```bash
git add cli.py tests/janus_cli/test_design.py
git commit -m "feat(cli): open response frame — accent gutter replaces the box [redesign 4.1]

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 11: `/help` redesign

**Files:**
- Modify: `cli.py` `show_help` (~line 6362)
- Test: `tests/janus_cli/test_help_render.py` (create)

**Interfaces:**
- Consumes: `design.layout/header/rule`, `COMMANDS_BY_CATEGORY`, `_ensure_skill_commands`, `get_skill_bundles`, `self._command_available` (all exist).

- [ ] **Step 1: Write the failing test** — create `tests/janus_cli/test_help_render.py`:

```python
"""/help rendering: open layout is grouped/scannable; classic keeps its box."""
import pytest

from janus_cli.skin_engine import set_active_skin


@pytest.fixture()
def cli(monkeypatch):
    """A JanusCLI with output captured. Uses the real COMMAND registry."""
    import cli as cli_mod
    inst = object.__new__(cli_mod.JanusCLI)   # skip heavy __init__
    inst.enabled_toolsets = []
    monkeypatch.setattr(cli_mod.JanusCLI, "_command_available",
                        lambda self, c: True, raising=False)
    lines = []
    monkeypatch.setattr(cli_mod, "_cprint", lambda *a, **k: lines.append(" ".join(str(x) for x in a)))

    class _FakeConsole:
        def print(self, *a, **k):
            lines.append(" ".join(str(x) for x in a))
    monkeypatch.setattr(cli_mod, "ChatConsole", lambda *a, **k: _FakeConsole())
    return inst, lines


def test_open_help_has_no_ascii_box_and_lists_commands(cli):
    inst, lines = cli
    set_active_skin("default")
    inst.show_help()
    out = "\n".join(lines)
    assert "/help" in out
    assert "+----" not in out and "+-" not in out     # no ASCII box header
    assert "(^_^)?" not in out


def test_classic_help_keeps_the_boxed_header(cli):
    inst, lines = cli
    set_active_skin("classic")
    try:
        inst.show_help()
    finally:
        set_active_skin("default")
    out = "\n".join(lines)
    assert "(^_^)? Available Commands" in out
```

- [ ] **Step 2: Run to verify failure**

Run: `scripts/run_tests.sh tests/janus_cli/test_help_render.py`
Expected: open-layout test FAILS (box still rendered); classic PASSES. If the fixture needs adjustment for module internals (e.g. `_ensure_skill_commands` requiring state), stub those attributes on `inst` — keep the two assertions unchanged.

- [ ] **Step 3: Implement.** Rewrite `show_help` to branch on layout — legacy body preserved verbatim in the panel branch:

```python
    def show_help(self):
        """Display help information with categorized commands."""
        from janus_cli.commands import COMMANDS_BY_CATEGORY
        from janus_cli.design import layout as _dlayout

        if _dlayout() != "open":
            return self._show_help_panel()

        try:
            from janus_cli.skin_engine import get_active_help_header
            header = get_active_help_header("commands")
        except Exception:
            header = "commands"
        header = (header or "").strip() or "commands"
        accent = _accent_hex()
        con = ChatConsole()
        con.print(f"\n  [bold {accent}]{_escape(header)}[/]")
        con.print(f"  [dim]{'─' * 40}[/]")

        for category, commands in COMMANDS_BY_CATEGORY.items():
            rows = [(c, d) for c, d in commands.items() if self._command_available(c)]
            if not rows:
                continue
            con.print(f"\n  [bold {accent}]{_escape(category.lower())}[/]")
            for cmd, desc in rows:
                con.print(f"    [{accent}]{cmd:<16}[/][dim]{_escape(desc)}[/]")

        skill_commands = _ensure_skill_commands()
        if skill_commands:
            con.print(f"\n  [bold {accent}]skill commands[/] [dim]({len(skill_commands)} installed)[/]")
            for cmd, info in sorted(skill_commands.items()):
                con.print(f"    [{accent}]{cmd:<22}[/][dim]{_escape(info['description'])}[/]")

        _bundles_now = get_skill_bundles()
        if _bundles_now:
            con.print(f"\n  [bold {accent}]skill bundles[/] [dim]({len(_bundles_now)} installed)[/]")
            for cmd, info in sorted(_bundles_now.items()):
                skill_count = len(info.get("skills", []))
                desc = info.get("description") or f"Load {skill_count} skills"
                con.print(f"    [{accent}]{cmd:<22}[/][dim]{_escape(desc)} ({skill_count} skills)[/]")

        con.print("\n  [dim]type a message to chat · alt+enter for a new line · ctrl+g opens the draft editor[/]")
        if _is_termux_environment():
            con.print(f"  [dim]attach image: /image {_termux_example_image_path()}[/]\n")
        else:
            con.print("  [dim]paste image: alt+v (or /paste)[/]\n")

    def _show_help_panel(self):
        """Legacy boxed /help (classic and other panel-layout skins)."""
        from janus_cli.commands import COMMANDS_BY_CATEGORY
        # ... the ENTIRE current show_help body from the header try/except down
        # to the final tips block, moved here UNCHANGED ...
```

(Mechanics: cut the current body of `show_help` into `_show_help_panel` unchanged, then write the new `show_help` above it.)

- [ ] **Step 4: Run tests**

Run: `scripts/run_tests.sh tests/janus_cli/test_help_render.py`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add cli.py tests/janus_cli/test_help_render.py
git commit -m "feat(cli): grouped minimal /help; classic keeps its box [redesign 5.1]

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 12: `show_tools` header + kawaii strays on migrated surfaces

**Files:**
- Modify: `cli.py` `show_tools` (~line 6413: header + `(;_;)` line)
- Test: `tests/janus_cli/test_help_render.py` (append)

- [ ] **Step 1: Write the failing test** (append to `tests/janus_cli/test_help_render.py`):

```python
def test_open_show_tools_header_is_calm(cli, monkeypatch):
    import cli as cli_mod
    inst, lines = cli
    set_active_skin("default")
    monkeypatch.setattr(cli_mod, "get_tool_definitions",
                        lambda **k: [{"function": {"name": "terminal", "description": "Run a command."}}])
    monkeypatch.setattr(cli_mod, "get_toolset_for_tool", lambda n: "core", raising=False)
    inst.show_tools()
    out = "\n".join(lines)
    assert "(^_^)/" not in out
    assert "terminal" in out
```

- [ ] **Step 2: Run to verify failure**

Run: `scripts/run_tests.sh tests/janus_cli/test_help_render.py`
Expected: new test FAILS (`(^_^)/ Available Tools` present). Note `show_tools` uses bare `print` — if capture misses it, also monkeypatch `builtins.print` into `lines.append` for this test.

- [ ] **Step 3: Implement.** In `show_tools`, replace the header block (the `title = "(^_^)/ Available Tools"` + the three `print("+"...)` lines) with:

```python
        from janus_cli.design import layout as _dlayout, header as _dheader, rule as _drule
        print()
        if _dlayout() == "open":
            con = ChatConsole()
            con.print(f"  {_dheader('tools')}")
            con.print(f"  {_drule(40)}")
        else:
            title = "(^_^)/ Available Tools"
            width = 78
            pad = width - len(title)
            print("+" + "-" * width + "+")
            print("|" + " " * (pad // 2) + title + " " * (pad - pad // 2) + "|")
            print("+" + "-" * width + "+")
        print()
```

And replace `print("(;_;) No tools available")` with:

```python
            from janus_cli.design import warn as _dwarn
            ChatConsole().print(_dwarn("no tools available"))
```

- [ ] **Step 4: Run tests**

Run: `scripts/run_tests.sh tests/janus_cli/test_help_render.py`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add cli.py tests/janus_cli/test_help_render.py
git commit -m "feat(cli): calm /tools header + design-notice strays [redesign 5.2]

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 13: Stale fallback hexes + prompt/status verification

**Files:**
- Modify: `cli.py` `_accent_hex` (~line 1923)
- Test: existing suites (verification task)

- [ ] **Step 1: Update the fallback.** In `_accent_hex`, change both `"#FFBF00"` literals to `"#E3A857"` (the fallback should match the new default accent when the skin engine is unavailable).

- [ ] **Step 2: Verify prompt/status/completion colors are skin-driven** (no code change expected — the Task 5 skin data carries them):

Run: `scripts/run_tests.sh tests/janus_cli/test_skin_engine.py tests/janus_cli/test_design.py`
Expected: PASS.

Then confirm no stale old-gold fallbacks remain on migrated paths:

Run: `grep -n '#FFBF00\|#FFD700\|#CD7F32' cli.py janus_cli/design.py janus_cli/skin_notice.py | grep -v classic`
Expected: hits only in unmigrated legacy paths (panel-branch code and prompt_toolkit fallbacks), none in design.py/skin_notice.py.

- [ ] **Step 3: Commit**

```bash
git add cli.py
git commit -m "chore(cli): align accent fallback with the minimal default [redesign 6.1]

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 14: Consistency sweep, docs, full regression

**Files:**
- Modify: `README.md` (one short "Look & feel" note), `janus_cli/skin_engine.py` docstring BUILT-IN SKINS list (add `classic`, reword `default`)
- Test: full affected-suite run

- [ ] **Step 1: Sweep for strays on migrated surfaces**

Run: `grep -n "kawaii\|(^_^)\|(;_;)" janus_cli/banner.py janus_cli/design.py agent/display.py | grep -v classic | grep -v KAWAII`
Expected: only comments/constant names remain (KAWAII_* constants stay for third-party compat). Fix any live output strings found.

- [ ] **Step 2: Update the skin_engine docstring** BUILT-IN SKINS section:

```
- ``default`` — Janus minimal: monochrome with refined gold (the redesigned look)
- ``classic`` — The pre-redesign look: gold and kawaii, preserved verbatim
```

(keep the other lines). Add to README's feature list (near the CLI description) one line:

```
- **Professional minimal CLI** with a data-driven skin engine — `/skin classic` restores the pre-redesign look, `/skin list` shows all themes.
```

- [ ] **Step 3: Full regression across every touched suite**

Run: `scripts/run_tests.sh tests/janus_cli/test_skin_engine.py tests/janus_cli/test_classic_skin.py tests/janus_cli/test_design.py tests/janus_cli/test_skin_notice.py tests/janus_cli/test_help_render.py tests/janus_cli/test_banner.py tests/janus_cli/test_banner_skills.py tests/janus_cli/test_banner_git_state.py tests/janus_cli/test_banner_pip_update.py tests/agent/test_display.py tests/agent/test_display_emoji.py tests/agent/test_display_minimal_lines.py tests/agent/test_display_todo_progress.py tests/agent/test_display_tool_failure.py`
Expected: ALL PASS.

Also: `ruff check janus_cli/design.py janus_cli/skin_notice.py janus_cli/skin_engine.py janus_cli/banner.py agent/display.py` → clean.

- [ ] **Step 4: Visual smoke.** Launch `janus` interactively (if credentials available): confirm open banner, minimal spinner, `▸` tool lines, gutter response, `/help`, `/skin classic` full revert, `/skin default` return. Non-interactive fallback: `python -c "from rich.console import Console; from janus_cli.banner import build_welcome_banner; from janus_cli.skin_engine import set_active_skin; set_active_skin('default'); c=Console(); build_welcome_banner(c, model='opus-4.8', cwd='.', tools=[], enabled_toolsets=[], session_id='abc123', get_toolset_for_tool=lambda n:'core', context_length=1000000)"`.

- [ ] **Step 5: Commit + push**

```bash
git add README.md janus_cli/skin_engine.py
git commit -m "docs: skin catalog + README note for the CLI redesign [redesign 7.1]

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
git push -u origin claude/cli-redesign
```

---

## Plan Self-Review (completed)

- **Spec coverage:** §3 tokens/symbols/voice → Tasks 3/5; §4.1 banner → 6; §4.2 tool lines → 8; §4.3 spinner → 9; §4.4 response (incl. streaming) → 10; §4.5 help → 11; §4.6 prompt/status → 5 (data) + 13 (verify); §4.7 notices → 4 (API) + 7/12 (adoption); §5.2 schema → 1; §5.3 classic → 2, new default → 5; §5.4 migration/notice → 7; §6 degradation → 3 (gates) + tests; §7 testing → per-task; §8 rollout order → task order. Broad ad-hoc `⚠` migration (§4.7 "opportunistic") is deliberately deferred beyond Task 12's bounded set — future work, not a gap in the shipped design.
- **Placeholder scan:** all steps carry code or exact commands; Task 9(d) and 11's `_show_help_panel` move are mechanical cut-and-keep operations with the transform stated on the actual code.
- **Type consistency:** `response_block(content, *, label, border_hex, text_hex, width, attribution="")` used identically in Tasks 4/10; `sym/tok/layout/styled` names match Tasks 3→14; `compose_spinner_message(face, message)` matches Tasks 9(b)/(d)/(e); `SkinConfig.get_symbol(key, fallback)` matches Tasks 1/3.
