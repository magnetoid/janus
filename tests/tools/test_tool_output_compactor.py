"""Invariants for tool-output compaction (tools/tool_output_compactor.py).

These assert *relationships* (never-grows, structure-preserved, fail-open,
multibyte-safe, gating) rather than exact compacted strings, so they don't
turn into change-detector snapshots when the heuristics are tuned.
"""

from __future__ import annotations

import json

import pytest

from tools.tool_output_compactor import compact_tool_result

# Enabled config with no size floor, so the pure function actually runs.
ON = {"enabled": True, "min_chars": 0}


def _on(**overrides):
    return {**ON, **overrides}


# ── Gating ───────────────────────────────────────────────────────────────


def test_disabled_by_default_is_passthrough():
    big = "<div>" + "x " * 5000 + "</div>"
    # No config → defaults → enabled=False → unchanged.
    assert compact_tool_result(big) == big


def test_below_min_chars_is_passthrough():
    text = "<div>hello</div>"
    assert compact_tool_result(text, config={"enabled": True, "min_chars": 10_000}) == text


def test_excluded_tool_is_passthrough():
    payload = "data:image/png;base64," + "A" * 500
    out = compact_tool_result(
        payload, tool_name="read_file", config=_on(exclude_tools=["read_file"])
    )
    assert out == payload


def test_non_excluded_tool_is_compacted():
    payload = "data:image/png;base64," + "A" * 500
    out = compact_tool_result(payload, tool_name="browser_snapshot", config=_on())
    assert "base64" not in out
    assert len(out) < len(payload)


# ── Core invariant: never grows ──────────────────────────────────────────


@pytest.mark.parametrize(
    "text",
    [
        "<html><body><p>" + "word " * 2000 + "</p></body></html>",
        "data:font/woff2;base64," + "Z" * 4000,
        "\n\n\n\n\n".join(["line"] * 200),
        json.dumps({"content": "<div><p>" + "a " * 3000 + "</p></div>"}),
        "plain text with no markup " * 300,
    ],
)
def test_never_grows(text):
    out = compact_tool_result(text, config=_on())
    assert len(out) <= len(text)


# ── data: URI stripping ──────────────────────────────────────────────────


def test_data_uri_replaced_with_placeholder():
    blob = "before data:image/png;base64," + "Q" * 1000 + " after"
    out = compact_tool_result(blob, config=_on(html_to_markdown=False))
    assert "QQQQ" not in out
    assert "data-uri omitted" in out
    assert "before" in out and "after" in out


def test_small_inline_value_not_touched():
    # Short payload after data: must not be clobbered (below the 64-char floor).
    text = "url(data:image/gif;base64,R0lGOD) " * 50  # short payloads, repeated
    out = compact_tool_result(text, config=_on(html_to_markdown=False, collapse_repeats=False))
    assert "R0lGOD" in out


# ── HTML → markdown ──────────────────────────────────────────────────────


def test_html_converted_and_shrunk():
    html = (
        "<html><head><style>.x{color:red}</style></head><body>"
        "<h1>Title</h1><p>Hello <a href='https://example.com'>link</a> world.</p>"
        "<ul><li>one</li><li>two</li></ul></body></html>"
    )
    out = compact_tool_result(html, config=_on(min_chars=0))
    assert "<style>" not in out and "color:red" not in out  # script/style dropped
    assert "<h1>" not in out and "</p>" not in out           # tags stripped
    assert "Title" in out and "Hello" in out                 # text kept
    assert "https://example.com" in out                      # link target kept


def test_prose_with_stray_angle_bracket_not_treated_as_html():
    text = "if a < b and b > c then x " * 200  # comparisons, not markup
    out = compact_tool_result(text, config=_on(collapse_repeats=False, strip_data_uris=False))
    # No HTML path → text returned unchanged (it has no data URIs either).
    assert out == text.strip() or out == text


# ── JSON-aware leaf compaction ───────────────────────────────────────────


def test_json_structure_preserved_long_leaf_compacted():
    payload = {
        "status": "ok",
        "id": "abc-123",
        "body": "<div><p>" + "content " * 2000 + "</p></div>",
    }
    raw = json.dumps(payload)
    out = compact_tool_result(raw, config=_on(min_leaf_chars=200))
    reparsed = json.loads(out)  # still valid JSON
    assert reparsed["status"] == "ok"
    assert reparsed["id"] == "abc-123"            # short leaf untouched
    assert "<div>" not in reparsed["body"]        # long leaf compacted
    assert len(out) < len(raw)


def test_malformed_json_falls_back_to_text():
    # Looks like JSON (leading brace) but isn't — must not raise.
    text = "{not valid json " + "data:image/x;base64," + "B" * 200 + "}"
    out = compact_tool_result(text, config=_on())
    assert "BBBB" not in out  # text path still stripped the data URI


# ── collapse repeats ─────────────────────────────────────────────────────


def test_identical_line_run_collapsed():
    text = "\n".join(["DEBUG spam"] * 100)
    out = compact_tool_result(text, config=_on(html_to_markdown=False, strip_data_uris=False))
    assert "identical lines omitted" in out
    assert out.count("DEBUG spam") <= 3
    assert len(out) < len(text)


def test_blank_line_runs_collapsed():
    text = "head" + "\n" * 12 + ("tail " * 1000)
    out = compact_tool_result(text, config=_on(html_to_markdown=False, strip_data_uris=False))
    assert "\n\n\n" not in out


# ── max_chars cap ────────────────────────────────────────────────────────


def test_max_chars_enforced():
    text = "alpha beta gamma " * 1000
    out = compact_tool_result(
        text, config=_on(html_to_markdown=False, strip_data_uris=False, max_chars=500)
    )
    assert len(out) <= 500 + 64  # cap plus the truncation marker
    assert "truncated" in out


# ── robustness ───────────────────────────────────────────────────────────


def test_non_string_passthrough():
    assert compact_tool_result(None, config=_on()) is None  # type: ignore[arg-type]
    assert compact_tool_result(12345, config=_on()) == 12345  # type: ignore[arg-type]


def test_empty_string_passthrough():
    assert compact_tool_result("", config=_on()) == ""


def test_multibyte_text_preserved():
    # CJK + emoji must survive intact (no byte-level slicing corruption).
    cjk = "汉字测试 " * 50
    emoji = "👨‍👩‍👧‍👦 family " * 50
    text = "<p>" + cjk + emoji + "</p>" + ("data:image/x;base64," + "C" * 200)
    out = compact_tool_result(text, config=_on())
    assert "汉字测试" in out
    assert "👨‍👩‍👧‍👦" in out
    assert "CCCC" not in out  # data URI still stripped around the multibyte text


def test_compaction_is_fail_open_on_bad_config():
    # Garbage config values must not raise; result is returned (possibly unchanged).
    text = "<div>" + "x " * 3000 + "</div>"
    out = compact_tool_result(text, config={"enabled": True, "min_chars": "not-an-int"})
    assert isinstance(out, str)
