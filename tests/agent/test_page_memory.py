"""Tests for PageMem (agent/page_memory.py)."""
from agent import page_memory as pm

SNAP = """- heading "Welcome" [e1]
- searchbox "Search" [e2]
- button "Search" [e3]
- link "Sign in" [e4]
- text "some copy"
- button "" [e5]
"""


def test_domain_normalizes():
    assert pm._domain("https://www.Example.com/path?q=1") == "example.com"
    assert pm._domain("http://shop.example.com") == "shop.example.com"


def test_parse_elements_keeps_interactive_named_only():
    els = pm._parse_elements(SNAP)
    pairs = {(e["role"], e["name"]) for e in els}
    assert ("searchbox", "Search") in pairs
    assert ("button", "Search") in pairs
    assert ("link", "Sign in") in pairs
    assert ("heading", "Welcome") not in pairs   # not interactive
    assert all(e["name"] for e in els)            # the unnamed button is dropped
    assert all("@e" not in e["name"] and "[e" not in e["name"] for e in els)  # refs gone


def test_enabled_default_on():
    assert pm.enabled({}) is True
    assert pm.enabled({"page_memory": {"enabled": False}}) is False


def test_capture_merges_dedups_and_persists():
    pm.capture("https://site-a.com", SNAP)
    pm.capture("https://site-a.com/other", SNAP)  # same domain, same elements
    rec = pm.recall("https://www.site-a.com")
    names = {(e["role"], e["name"]) for e in rec["profile_elements"]}
    assert ("button", "Search") in names
    # dedup: not duplicated despite two captures
    assert sum(1 for e in rec["profile_elements"] if e["name"] == "Search" and e["role"] == "button") == 1


def test_record_playbook_and_recall_ordering():
    pm.record_playbook("https://site-b.com", "search for shoes",
                       [{"action": "type", "target": 'searchbox "Search"', "value": "shoes"},
                        {"action": "click", "target": 'button "Search"'}])
    pid2 = pm.record_playbook("https://site-b.com", "sign in",
                              [{"action": "click", "target": 'link "Sign in"'}])
    pm.note_outcome("https://site-b.com", pid2, ok=True)  # boost the 2nd
    rec = pm.recall("https://site-b.com")
    assert rec["playbooks"][0]["task"] == "sign in"  # higher net success first


def test_record_playbook_scrubs_secrets():
    pid = pm.record_playbook("https://site-c.com", "login",
                             [{"action": "type", "target": 'textbox "Password"', "value": "hunter2"},
                              {"action": "type", "target": 'searchbox "Search"', "value": "ok"}])
    steps = pm.recall("https://site-c.com")["playbooks"][0]["steps"]
    pw = next(s for s in steps if "Password" in s["target"])
    assert pw["value"] != "hunter2" and "scrub" in pw["value"].lower()
    keep = next(s for s in steps if "Search" in s["target"])
    assert keep["value"] == "ok"  # non-secret value retained


def test_note_outcome_decays_after_consecutive_fails():
    pid = pm.record_playbook("https://site-d.com", "x", [{"action": "click", "target": 'button "X"'}])
    for _ in range(3):
        pm.note_outcome("https://site-d.com", pid, ok=False)
    assert pm.recall("https://site-d.com")["playbooks"] == []  # decayed away


def test_note_outcome_streak_resets_on_success():
    pid = pm.record_playbook("https://site-e.com", "x", [{"action": "click", "target": 'button "X"'}])
    pm.note_outcome("https://site-e.com", pid, ok=False)
    pm.note_outcome("https://site-e.com", pid, ok=False)
    pm.note_outcome("https://site-e.com", pid, ok=True)   # resets the streak
    pm.note_outcome("https://site-e.com", pid, ok=False)
    assert len(pm.recall("https://site-e.com")["playbooks"]) == 1  # not decayed


def test_format_recall():
    pm.capture("https://site-f.com", SNAP)
    pm.record_playbook("https://site-f.com", "do search", [{"action": "click", "target": 'button "Search"'}])
    out = pm.format_recall(pm.recall("https://site-f.com"))
    assert "PageMem" in out and "Search" in out and "do search" in out
    assert pm.format_recall({"profile_elements": [], "playbooks": []}) == ""


def test_caps_respected():
    big = "\n".join(f'- button "btn{i}" [e{i}]' for i in range(200))
    pm.capture("https://site-g.com", big, config={"page_memory": {"max_elements": 10}})
    assert len(pm.recall("https://site-g.com")["profile_elements"]) <= 10


def test_best_effort_never_raises():
    assert pm._parse_elements(None) == []
    assert pm.recall("not a url") == {"profile_elements": [], "playbooks": []}
    assert pm.capture("x", None) is None or True  # never raises
    assert pm.format_recall(None) == ""
