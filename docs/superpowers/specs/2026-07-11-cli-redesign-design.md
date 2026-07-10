# Janus CLI Redesign — Design Spec

**Date:** 2026-07-11
**Status:** Approved (user), pending implementation plan
**Scope decisions (user-selected):** Full visual + UX redesign · Modern-minimal direction · Refined-gold accent · New default for everyone, old look preserved verbatim as `/skin classic`

## 1. Context & Problem

The Janus interactive CLI (`cli.py`, `janus_cli/banner.py`, `agent/display.py`) currently ships a deliberately playful default: gold/kawaii palette, kawaii spinner faces, "cute" emoji tool messages, an ornate boxed emblem banner, and a `(^_^)?` help header. The goal is a professional, modern, coherent design — while preserving the current look for users who want it.

A data-driven skin engine already exists (`janus_cli/skin_engine.py`): YAML skins control colors, spinner faces, branding strings, tool prefix, tool emojis, and banner art. It does NOT control layout/structure (banner composition, tool-line format, help layout, response framing). This redesign extends it minimally rather than replacing it.

## 2. Goals / Non-Goals

**Goals**

- A new professional default look: near-monochrome, one refined-gold accent, geometric symbols, zero emoji in default output.
- Redesign the *structures*: banner, tool-call lines, spinner, response presentation, `/help`, prompt, status bar, error/notice styling.
- One semantic design-token layer so styling decisions live in exactly one module.
- Preserve the current look verbatim as the built-in `classic` skin (`/skin classic`).
- Every increment shippable, revertable, and testable on its own.

**Non-Goals**

- No behavior changes: commands, keybindings, autocomplete behavior, verbosity semantics, feature set — all unchanged.
- No TUI (`ui-tui/`), dashboard, or gateway surface changes (separate surfaces).
- No rewrite of cli.py's control flow; only its output call sites migrate.

## 3. Design Language

### 3.1 Semantic tokens

All rendering goes through named tokens resolved from the active skin. Raw hex values never appear at call sites.

| Token | Default-skin value | Used for |
|---|---|---|
| `accent` | `#E3A857` (refined gold) | prompt symbol, active states, section headers, response gutter |
| `fg` | terminal default | primary content |
| `muted` | `#8A8A8A` | labels, tool verbs, secondary info |
| `faint` | `#5C5C5C` | rules, durations, timestamps, session ids |
| `ok` | `#7CB87C` | success semantics only |
| `warn` | `#D4A24E` | warning semantics only |
| `error` | `#D47C7C` | failure semantics only |

Color is semantic, never decorative: `ok/warn/error` appear only when something succeeded/warned/failed.

### 3.2 Symbols

| Symbol | ASCII fallback | Meaning |
|---|---|---|
| `▸` | `>` | tool/activity line |
| `✓` | `ok` | success |
| `✗` | `x` | failure |
| `●` | `*` | bullet / active item |
| `❯` | `>` | input prompt |
| `▍` | `\|` | response gutter |
| `─` | `-` | horizontal rule |

ASCII fallbacks activate on encodings that can't render the glyphs (legacy Windows console / cp1252), reusing the codebase's existing encoding detection. Default output contains **no emoji**; emoji tool icons remain a skin feature (`classic` keeps them).

### 3.3 Voice

Lowercase-calm microcopy. No exclamation marks, no kaomoji, no faces in the default skin. "done", not "✨ All done!!". Branding strings stay skin-driven, so `classic` keeps its personality.

## 4. Surface Specifications

### 4.1 Banner (`janus_cli/banner.py`)

Current: boxed gold emblem panel + an "Available Tools" dump of up to 8 toolsets with tool names, red/yellow coloring for unavailable tools.

New (default skin, `layout: open`):

```
  janus 1.4.2
  ────────────────────────────────────────────────
  opus-4.8 · 1M context · ~/projects/api
  session a4f2c9 · 12 toolsets · 47 tools · 8 skills
```

- Tool inventory collapses to counts; the full listing already exists behind `/tools` — the banner points there when relevant (e.g., `N unavailable · /tools for details` in `warn` when tools are misconfigured).
- YOLO-mode warning line stays (semantic `error` styling).
- `classic` skin (`layout: panel`) keeps today's emblem-panel rendering path unchanged.
- Wordmark is text (`janus` + version), not ASCII art, in the default skin; `banner_logo`/`banner_hero` skin fields still work for skins that supply art.

### 4.2 Tool lines (`agent/display.py::get_cute_tool_message` and live spinner lines)

Current: `┊ 💻 $         git status  0.2s` (emoji, prefix `┊`, ad-hoc column widths).

New (default skin):

```
  ▸ terminal   git status                        0.2s
  ▸ read       src/main.py                       0.1s
  ✗ patch      src/api.py — no match at hunk 2   0.3s
```

- Columns: symbol (`▸` — accent while running, muted once complete; failures switch to `✗` in `error`; the `✓` symbol is reserved for notices, not tool lines), verb (muted, fixed width 10), detail (fg, truncation rules unchanged), duration (faint, two-space gap).
- Failure detail appends the trimmed reason (existing `_detect_tool_failure` logic reused).
- Emoji verb icons render only when the active skin sets `emoji_tools: true` (classic).
- The per-tool verb/detail extraction logic in `get_cute_tool_message` is preserved; only the formatting layer changes (renamed `format_tool_line`, with a compatibility alias).

### 4.3 Spinner (`agent/display.py::KawaiiSpinner`)

Current: kawaii faces + verbs, optional skin "wings".

New (default skin): braille-dots spinner + muted verb + faint elapsed: `⠋ thinking · 4s`. Faces/wings remain skin-driven — `classic` supplies today's faces; skins with no faces get the minimal dots. No `\033[K` usage (documented pitfall); existing line-clearing approach unchanged.

### 4.4 Response presentation (cli.py Panel sites ~4660, ~9485, ~12806)

Current: Rich `Panel` box labeled `⚕ Janus`.

New (default skin): open block with a thin accent gutter, no box — full width, clean copy-paste:

```
  ▍ The fix is in the retry logic — three call
  ▍ sites needed the new timeout parameter.
```

- Markdown rendering inside the block unchanged (same Rich renderable, different frame).
- `classic` (`layout: panel`) keeps the labeled Panel exactly as today.
- All three Panel call sites route through one design.py `response_block()` helper.

### 4.5 `/help` (cli.py `show_help` ~6362)

Current: `(^_^)? Available Commands` header, flat list.

New: rendered from `COMMAND_REGISTRY` (already category-tagged): accent category headers, two-column aligned name/description rows, faint footer (`/help <command> for details` if per-command help exists, else version + docs pointer). Header string remains skin-driven (`help_header`); default skin sets it to `commands`.

### 4.6 Prompt & status bar (cli.py ~12993, ~3466)

- Prompt symbol `❯` in `accent` (skin-driven as today); input rule becomes a single faint `─` rule.
- Status bar: identical content and context-usage thresholds; colors remapped to tokens (`status_bar_*` skin keys stay, defaults change in the new default skin). Completion menu colors likewise remapped.

### 4.7 Errors / notices (spread across cli.py)

One API in design.py replaces ad-hoc `⚠ ...` / `✓ ...` prints:

- `ok(msg)` → `✓ msg` (`ok`)
- `warn(msg)` → `! msg` (`warn`)
- `error(msg)` → `✗ msg` (`error`)
- `note(msg)` → `● msg` (`muted`)

Call sites migrate opportunistically in increment 5; unmigrated prints keep working (no flag day).

## 5. Architecture

### 5.1 `janus_cli/design.py` (new, ~200 lines)

The single home of styling decisions.

```python
# tokens & symbols (resolved from active skin, cached per skin activation)
tok(name: str) -> str            # "accent" -> "#E3A857" (or "" when color off)
sym(name: str) -> str            # "activity" -> "▸" (or ASCII fallback)

# render helpers (return Rich-markup strings; plain text when color off)
header(text) / rule(width=None) / kv(label, value)
tool_line(verb, detail, duration, failed=False, reason="")
response_block(renderable) -> renderable      # gutter or Panel per skin layout
ok(msg) / warn(msg) / error(msg) / note(msg)  # print-helpers
```

- Respects `should_use_color()` (janus_cli/colors.py) as the single color gate; honors `NO_COLOR` / `TERM=dumb` / non-TTY.
- Depends only on `skin_engine` + `colors`; no imports from cli.py (no cycles).

### 5.2 Skin schema additions (all optional, backward-compatible)

```yaml
symbols:            # override any symbol; missing -> minimal defaults
  activity: "┊"
layout: open        # open | panel   (banner + response framing)
emoji_tools: false  # emoji verb icons in tool lines
```

Existing skins without these fields get `layout: open`, `emoji_tools: false`, minimal symbols — except `classic`, which sets all three explicitly.

### 5.3 Skins

- **`classic` (new built-in):** verbatim copy of today's `default` skin values + `layout: panel`, `emoji_tools: true`, current kawaii spinner faces/verbs, current branding (`(^_^)?` help header, `⚕ Janus` response label, goodbye `Until next time. ⟡`), tool prefix `┊`.
- **`default` (replaced):** the token palette from §3.1, minimal branding (`janus`, `commands`, goodbye `until next time.`), no spinner faces (dots), `layout: open`.
- Other built-ins (`ares`, `mono`, `slate`, `daylight`, `warm-lightmode`) untouched; they inherit minimal structures via defaults.

### 5.4 Migration

Config default `display.skin: default` means everyone flips on upgrade; `/skin classic` is a one-command revert. Release notes + a one-line notice on first launch after upgrade ("new look — `/skin classic` restores the previous one", shown once via a stamp file, same pattern as `learning_onboarding`).

## 6. Degradation & Constraints

- `NO_COLOR` / `TERM=dumb` / non-TTY → plain text through the one gate; symbols still render (they're characters, not colors); ASCII fallback for non-Unicode encodings.
- Narrow terminals (<60 cols): durations trail after detail instead of aligning; rules clamp to width.
- Known pitfalls respected: no `\033[K` in spinner writes; no `simple_term_menu`; cp1252-safe fallbacks; prompt-caching untouched (pure presentation).
- Windows: verified against CONTRIBUTING.md footguns; encoding detection reused, not reinvented.

## 7. Testing

Invariant-style (no snapshot tests, per CLAUDE.md):

- Tool lines always contain a duration suffix; failed lines contain the failure symbol and reason.
- Default-skin output contains no emoji (scan rendered strings for emoji ranges).
- `classic` skin reproduces the exact current strings for: goodbye, help header, response label, tool prefix, spinner faces (guards the verbatim promise).
- With `NO_COLOR=1`, rendered output contains no ANSI escapes.
- Every surface renders without crashing at 50-col width and in non-TTY mode.
- design.py token resolution falls back safely when a skin lacks new fields.
- Existing tests asserting old default strings are updated in the same increment that migrates their surface.

## 8. Rollout (each increment = one commit series, shippable & revertable)

1. **Foundations** — design.py, skin-schema additions, `classic` skin added. No visible change (default untouched).
2. **The flip** — new `default` skin + banner redesign + first-launch notice.
3. **Tool lines + spinner.**
4. **Response block.**
5. **/help + unified notices.**
6. **Prompt, input rule, status bar, completion menu.**
7. **Consistency sweep** — grep for stray raw hexes/emoji/ad-hoc prints in migrated surfaces; docs + README visuals.

## 9. Risks

| Risk | Mitigation |
|---|---|
| Tests asserting old strings break | Per-surface test updates inside the same increment; classic-skin verbatim tests catch accidental drift |
| Users dislike the change | `/skin classic` one-command revert + first-launch notice |
| Mid-rollout inconsistency (migrated vs not) | Increment order goes top-of-funnel first (banner) → conversation surfaces; sweep at the end |
| Windows/encoding regressions | ASCII fallback set + reuse of existing encoding detection; CI runs the affected test files |
| cli.py size makes call-site migration error-prone | Only formatting call sites change; each increment's diff stays narrow and mechanical |
