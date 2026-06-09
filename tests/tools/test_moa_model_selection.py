"""Task-aware reference/aggregator model selection for Mixture-of-Agents."""
import pytest

from agent import model_strengths as ms
from tools import mixture_of_agents_tool as moa


def test_no_task_uses_hardcoded_defaults():
    assert moa._select_reference_models(None) == moa.REFERENCE_MODELS
    assert moa._select_aggregator_model(None) == moa.AGGREGATOR_MODEL


def test_unknown_task_falls_back_to_defaults():
    # Empty KB -> no entries for this task -> defaults.
    assert moa._select_reference_models("nonexistent-task") == moa.REFERENCE_MODELS
    assert moa._select_aggregator_model("nonexistent-task") == moa.AGGREGATOR_MODEL


def test_task_with_kb_entries_uses_ranked_models():
    ms.record("coding", "claude-opus-4.6", score=9)
    ms.record("coding", "deepseek-v3.2", score=8)
    ms.record("coding", "gpt-5.4", score=7)
    refs = moa._select_reference_models("coding")
    assert refs == ["claude-opus-4.6", "deepseek-v3.2", "gpt-5.4"]
    # aggregator = single strongest
    assert moa._select_aggregator_model("coding") == "claude-opus-4.6"


def test_selection_is_capped_at_four():
    for i, m in enumerate(["m1", "m2", "m3", "m4", "m5", "m6"]):
        ms.record("research", m, score=10 - i)
    assert len(moa._select_reference_models("research")) == 4
