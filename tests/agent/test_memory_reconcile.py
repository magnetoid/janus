"""Per-candidate write-time reconciliation decision."""
from types import SimpleNamespace

from agent import memory_gardener as mg


def _fake_llm(reply):
    def _caller(**kwargs):
        return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=reply))])
    return _caller


_EXISTING = ["User is on Python 3.11.", "Deploy script is scripts/deploy.sh."]


def test_add_new_fact():
    d = mg.reconcile_candidate("User prefers dark mode.", _EXISTING, llm_caller=_fake_llm('{"action": "ADD"}'))
    assert d["action"] == "ADD"


def test_update_supersedes():
    d = mg.reconcile_candidate(
        "User is on Python 3.12.", _EXISTING,
        llm_caller=_fake_llm('{"action": "UPDATE", "target_index": 0}'))
    assert d["action"] == "UPDATE" and d["target_index"] == 0


def test_delete_contradiction():
    d = mg.reconcile_candidate(
        "Deploy is now via CI, no script.", _EXISTING,
        llm_caller=_fake_llm('{"action": "DELETE", "target_index": 1}'))
    assert d["action"] == "DELETE" and d["target_index"] == 1


def test_noop_already_known():
    d = mg.reconcile_candidate("User is on Python 3.11.", _EXISTING,
                               llm_caller=_fake_llm('{"action": "NOOP"}'))
    assert d["action"] == "NOOP"


def test_bad_index_falls_back_to_add():
    d = mg.reconcile_candidate("x", _EXISTING,
                               llm_caller=_fake_llm('{"action": "UPDATE", "target_index": 99}'))
    assert d["action"] == "ADD"


def test_garbage_reply_falls_back_to_add():
    d = mg.reconcile_candidate("x", _EXISTING, llm_caller=_fake_llm("nonsense"))
    assert d["action"] == "ADD"
