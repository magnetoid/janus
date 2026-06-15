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


from agent import memory_miner as mm
from tools.memory_tool import MemoryStore


def test_write_time_update_replaces_stale(monkeypatch):
    import yaml
    from janus_constants import get_janus_home
    home = get_janus_home(); home.mkdir(parents=True, exist_ok=True)
    (home / "config.yaml").write_text(
        yaml.safe_dump({"memory": {"write_time_reconcile": True}}), encoding="utf-8")

    store = MemoryStore(); store.load_from_disk()
    store.add("memory", "User is on Python 3.11.")

    monkeypatch.setattr(mm, "_parse_facts", lambda raw: {"user": [], "memory": ["User is on Python 3.12."]})
    monkeypatch.setattr(
        "agent.memory_gardener.reconcile_candidate",
        lambda cand, existing, **k: {"action": "UPDATE", "target_index": 0},
    )
    msgs = [{"role": "user", "content": "I upgraded to Python 3.12"},
            {"role": "assistant", "content": "noted"}]
    mm.mine_session_memory(msgs, store, llm_caller=_fake_llm("{}"))

    assert "User is on Python 3.12." in store.memory_entries
    assert "User is on Python 3.11." not in store.memory_entries


def test_write_time_delete_removes_old_and_skips_candidate(monkeypatch):
    import yaml
    from janus_constants import get_janus_home
    home = get_janus_home(); home.mkdir(parents=True, exist_ok=True)
    (home / "config.yaml").write_text(
        yaml.safe_dump({"memory": {"write_time_reconcile": True}}), encoding="utf-8")

    store = MemoryStore(); store.load_from_disk()
    store.add("memory", "Deploy script is scripts/deploy.sh.")

    monkeypatch.setattr(mm, "_parse_facts",
                        lambda raw: {"user": [], "memory": ["Deploy is now via CI, no script."]})
    monkeypatch.setattr("agent.memory_gardener.reconcile_candidate",
                        lambda cand, existing, **k: {"action": "DELETE", "target_index": 0})
    msgs = [{"role": "user", "content": "we moved deploy to CI"},
            {"role": "assistant", "content": "noted"}]
    mm.mine_session_memory(msgs, store, llm_caller=_fake_llm("{}"))

    # DELETE removes the contradicted old fact AND does not add the candidate
    assert "Deploy script is scripts/deploy.sh." not in store.memory_entries
    assert "Deploy is now via CI, no script." not in store.memory_entries


def test_write_time_add_keeps_both(monkeypatch):
    import yaml
    from janus_constants import get_janus_home
    home = get_janus_home(); home.mkdir(parents=True, exist_ok=True)
    (home / "config.yaml").write_text(
        yaml.safe_dump({"memory": {"write_time_reconcile": True}}), encoding="utf-8")

    store = MemoryStore(); store.load_from_disk()
    store.add("memory", "User is on Python 3.11.")

    monkeypatch.setattr(mm, "_parse_facts",
                        lambda raw: {"user": [], "memory": ["User prefers dark mode."]})
    monkeypatch.setattr("agent.memory_gardener.reconcile_candidate",
                        lambda cand, existing, **k: {"action": "ADD", "target_index": None})
    msgs = [{"role": "user", "content": "I like dark mode"},
            {"role": "assistant", "content": "noted"}]
    mm.mine_session_memory(msgs, store, llm_caller=_fake_llm("{}"))

    # ADD keeps the existing fact and adds the new one
    assert "User is on Python 3.11." in store.memory_entries
    assert "User prefers dark mode." in store.memory_entries
