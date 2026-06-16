"""Tests for task complexity classification (agent/task_complexity.py)."""
from types import SimpleNamespace

from agent import task_complexity as tc


def test_bands_constant():
    assert tc.BANDS == ("simple", "mid", "hard")


def test_simple_short_lookups():
    assert tc.classify_complexity("What is the capital of France?") == "simple"
    assert tc.classify_complexity("summarize this in one line") == "simple"
    assert tc.classify_complexity("translate 'hello' to French") == "simple"


def test_hard_design_and_reasoning():
    p = ("Design a fault-tolerant distributed rate limiter, analyze the "
         "tradeoffs between token-bucket and sliding-window, then prove the "
         "correctness of your approach step by step.")
    assert tc.classify_complexity(p) == "hard"


def test_hard_code_debugging():
    p = ("Refactor this module and debug the race condition:\n```python\n"
         "def worker():\n    ...\n```\nWhy does the deadlock happen?")
    assert tc.classify_complexity(p) == "hard"


# A genuinely middle-band prompt: moderate length, no simple/hard/code signals.
_MID = ("Write a helper that reads a JSON config file and returns its contents, "
        "falling back to a built-in default when the file is not present.")


def test_mid_is_the_default_middle():
    assert tc.classify_complexity(_MID) == "mid"


def test_empty_or_garbage_is_safe():
    assert tc.classify_complexity("") in tc.BANDS
    assert tc.classify_complexity(None) in tc.BANDS


def test_model_mode_only_overrides_mid(monkeypatch):
    # A clearly-simple prompt is NOT sent to the model even in model mode.
    calls = {"n": 0}

    def _llm(**kw):
        calls["n"] += 1
        return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content="hard"))])

    assert tc.classify_complexity("what is 2+2", mode="model", llm_caller=_llm) == "simple"
    assert calls["n"] == 0  # heuristic already decided; no model call

    # An ambiguous (mid) prompt IS escalated to the model, which can override.
    out = tc.classify_complexity(_MID, mode="model", llm_caller=_llm)
    assert calls["n"] == 1
    assert out == "hard"


def test_model_mode_best_effort_on_error():
    def _bad(**kw):
        raise RuntimeError("provider down")

    # Falls back to the heuristic band, never raises.
    assert tc.classify_complexity(_MID, mode="model", llm_caller=_bad) == "mid"
