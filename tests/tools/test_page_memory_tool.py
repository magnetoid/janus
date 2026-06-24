"""Tests for pagemem_remember tool + the browser_navigate PageMem hook."""
import json

from agent import page_memory as pm
import tools.page_memory_tool as t


def test_pagemem_remember_records_and_confirms():
    out = t.pagemem_remember("https://shop.example.com", "search shoes",
                             [{"action": "type", "target": 'searchbox "Search"', "value": "shoes"},
                              {"action": "click", "target": 'button "Search"'}])
    assert "PageMem" in out and "search shoes" in out
    assert pm.recall("https://shop.example.com")["playbooks"][0]["task"] == "search shoes"


def test_pagemem_remember_json_string_steps_parsed():
    # models sometimes stringify the array — it should be parsed back, not rejected
    out = t.pagemem_remember("https://x.com", "do",
                             json.dumps([{"action": "click", "target": 'button "Go"'}]))
    assert "PageMem" in out


def test_pagemem_remember_garbage_string_steps_errors():
    assert json.loads(t.pagemem_remember("https://x.com", "do", "just one step"))["success"] is False


def test_pagemem_remember_missing_args_errors():
    assert json.loads(t.pagemem_remember("https://x.com", "", []))["success"] is False


def test_tool_registered_and_exposed():
    from toolsets import TOOLSETS
    assert "pagemem_remember" in TOOLSETS["browser"]["tools"]
    from tools.registry import registry
    assert "pagemem_remember" in registry.list_tools() if hasattr(registry, "list_tools") else True


def test_navigate_hook_injects_when_playbook_exists():
    from tools.browser_tool import _apply_pagemem
    url = "https://hooksite.com"
    pm.record_playbook(url, "search", [{"action": "click", "target": 'button "Go"'}])
    result = json.dumps({"success": True, "snapshot": '- button "Go" [e1]'})
    out = json.loads(_apply_pagemem(url, result))
    assert "PageMem" in out["snapshot"] and "search" in out["snapshot"]


def test_navigate_hook_no_playbook_no_injection_but_captures():
    from tools.browser_tool import _apply_pagemem
    url = "https://freshsite.com"
    result = json.dumps({"success": True, "snapshot": '- searchbox "Find" [e1]'})
    out = json.loads(_apply_pagemem(url, result))
    assert "PageMem" not in out["snapshot"]                  # no first-visit noise
    assert any(e["name"] == "Find" for e in pm.recall(url)["profile_elements"])  # but captured


def test_navigate_hook_passthrough_on_failure():
    from tools.browser_tool import _apply_pagemem
    fail = json.dumps({"success": False, "error": "nope"})
    assert _apply_pagemem("https://x.com", fail) == fail


def test_navigate_hook_disabled_passthrough():
    from tools.browser_tool import _apply_pagemem
    url = "https://disabledsite.com"
    pm.record_playbook(url, "x", [{"action": "click", "target": 'button "Y"'}])
    result = json.dumps({"success": True, "snapshot": '- button "Y" [e1]'})
    import agent.page_memory as pmem
    orig = pmem.enabled
    pmem.enabled = lambda *a, **k: False
    try:
        assert _apply_pagemem(url, result) == result  # unchanged when disabled
    finally:
        pmem.enabled = orig
