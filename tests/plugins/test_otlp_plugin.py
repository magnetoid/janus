"""Tests for the bundled observability/otlp plugin.

The OTel SDK is an optional dep absent from the test env, so these exercise the
manifest, the register() wiring, the pure extractors, graceful inert behaviour,
and the emit path against MOCK instruments — no opentelemetry install required.
"""
from __future__ import annotations

import importlib
from pathlib import Path
from unittest.mock import MagicMock

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
PLUGIN_DIR = REPO_ROOT / "plugins" / "observability" / "otlp"


def _mod():
    return importlib.import_module("plugins.observability.otlp")


class TestManifest:
    def test_layout(self):
        assert PLUGIN_DIR.is_dir()
        assert (PLUGIN_DIR / "plugin.yaml").exists()
        assert (PLUGIN_DIR / "__init__.py").exists()

    def test_manifest_hooks_match_register(self):
        data = yaml.safe_load((PLUGIN_DIR / "plugin.yaml").read_text())
        assert data["name"] == "otlp"
        assert set(data["hooks"]) == {"post_api_request", "pre_tool_call", "post_tool_call"}


class TestRegister:
    def test_registers_expected_hooks(self):
        ctx = MagicMock()
        _mod().register(ctx)
        registered = {c.args[0] for c in ctx.register_hook.call_args_list}
        assert registered == {"post_api_request", "pre_tool_call", "post_tool_call"}
        # post_llm_call is per-turn → intentionally NOT registered (would double-count)
        assert "post_llm_call" not in registered


class TestPureExtractors:
    def test_tool_succeeded(self):
        m = _mod()
        assert m._tool_succeeded('{"ok": 1}') is True
        assert m._tool_succeeded('{"error": "boom"}') is False
        assert m._tool_succeeded("Error: nope") is False
        assert m._tool_succeeded(None) is True  # empty = no error marker

    def test_llm_metrics_without_usage(self):
        m = _mod()._llm_metrics(model="opus", provider="anthropic", api_duration=1.5)
        assert m["model"] == "opus" and m["provider"] == "anthropic"
        assert m["input_tokens"] == 0 and m["output_tokens"] == 0
        assert m["latency_s"] == 1.5 and m["cost_usd"] == 0.0


class TestInert:
    def test_hooks_noop_without_instruments(self, monkeypatch):
        m = _mod()
        monkeypatch.setattr(m, "_get_instruments", dict)  # always {} → inert
        # None of these should raise.
        m.on_post_api_request(model="opus", usage=None, api_duration=0.1)
        m.on_pre_tool_call(tool_name="read_file", task_id="t", tool_call_id="c")
        m.on_post_tool_call(tool_name="read_file", result='{"ok":1}', task_id="t", tool_call_id="c")


class TestEmit:
    def _instruments(self):
        return {k: MagicMock() for k in
                ("llm_tokens", "llm_cost", "llm_latency", "tool_calls", "tool_latency")}

    def test_llm_emit_records_latency_skips_zero_tokens(self, monkeypatch):
        m = _mod()
        inst = self._instruments()
        monkeypatch.setattr(m, "_get_instruments", lambda: inst)
        m.on_post_api_request(model="opus", provider="anthropic", usage=None, api_duration=2.0)
        inst["llm_latency"].record.assert_called_once()
        assert inst["llm_latency"].record.call_args.args[0] == 2.0
        inst["llm_tokens"].add.assert_not_called()  # 0 tokens → skipped

    def test_tool_emit_labels_status_and_latency(self, monkeypatch):
        m = _mod()
        inst = self._instruments()
        monkeypatch.setattr(m, "_get_instruments", lambda: inst)
        m.on_pre_tool_call(tool_name="terminal", task_id="t", session_id="s", tool_call_id="c")
        m.on_post_tool_call(tool_name="terminal", result='{"error":"x"}',
                            task_id="t", session_id="s", tool_call_id="c")
        inst["tool_calls"].add.assert_called_once()
        n, labels = inst["tool_calls"].add.call_args.args
        assert n == 1 and labels["tool"] == "terminal" and labels["status"] == "error"
        inst["tool_latency"].record.assert_called_once()
