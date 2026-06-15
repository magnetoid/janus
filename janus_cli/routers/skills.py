from fastapi import APIRouter, HTTPException, Request, Response, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import Any, Dict, List, Optional, Tuple, Union
import janus_cli.web_server as web_server_mod

router = APIRouter()

@router.get("/api/skills/graph")
async def get_skill_graph():
    try:
        from agent import skill_graph as sg

        sg.build_graph_from_skills()
        nodes = []
        for name in sg.graph_node_keys():
            node = sg.get_node(name) or {}
            a = sg.assess_promotability(name)
            nodes.append({
                "name": name,
                "promotion_level": node.get("promotion_level", 0),
                "verdict": ("promotable" if a["promotable"]
                            else "refine" if a["refinement_needed"] else "stable"),
                "success_rate": a.get("success_rate"),
                "uses": a.get("uses"),
                "dependencies": sg.dependencies_of(name),
            })
        return {"nodes": nodes, "edges": sg.load_graph().get("edges", [])}
    except Exception as exc:
        raise web_server_mod.HTTPException(status_code=500, detail=f"skill graph unavailable: {exc}")

@router.post("/api/skills/hub/install")
async def install_skill_hub(body: web_server_mod.SkillInstallRequest):
    identifier = (body.identifier or "").strip()
    if not identifier:
        raise web_server_mod.HTTPException(status_code=400, detail="identifier is required")
    try:
        proc = web_server_mod._spawn_janus_action(["skills", "install", identifier], "skills-install")
    except Exception as exc:
        web_server_mod._log.exception("Failed to spawn skills install")
        raise web_server_mod.HTTPException(status_code=500, detail=f"Failed to install skill: {exc}")
    return {"ok": True, "pid": proc.pid, "name": "skills-install"}

@router.post("/api/skills/hub/uninstall")
async def uninstall_skill_hub(body: web_server_mod.SkillUninstallRequest):
    name = (body.name or "").strip()
    if not name:
        raise web_server_mod.HTTPException(status_code=400, detail="name is required")
    try:
        proc = web_server_mod._spawn_janus_action(["skills", "uninstall", name, "--yes"], "skills-uninstall")
    except Exception as exc:
        web_server_mod._log.exception("Failed to spawn skills uninstall")
        raise web_server_mod.HTTPException(status_code=500, detail=f"Failed to uninstall skill: {exc}")
    return {"ok": True, "pid": proc.pid, "name": "skills-uninstall"}

@router.post("/api/skills/hub/update")
async def update_skills_hub():
    try:
        proc = web_server_mod._spawn_janus_action(["skills", "update"], "skills-update")
    except Exception as exc:
        web_server_mod._log.exception("Failed to spawn skills update")
        raise web_server_mod.HTTPException(status_code=500, detail=f"Failed to update skills: {exc}")
    return {"ok": True, "pid": proc.pid, "name": "skills-update"}

@router.get("/api/skills/hub/sources")
async def list_skills_hub_sources():
    """List the configured skill-hub sources and installed-skill provenance.

    Gives the dashboard something to show BEFORE a search runs — which hubs
    are wired up, their trust tier, and a set of featured skills pulled from
    the centralized index (zero extra API calls).  Without this the Browse-hub
    tab is a blank page with no indication it's even connected to anything.
    """

    def _run():
        from tools.skills_hub import create_source_router

        sources = create_source_router()
        out = []
        index_available = False
        featured = []
        for src in sources:
            sid = src.source_id()
            entry = {
                "id": sid,
                "label": web_server_mod._SKILL_HUB_SOURCE_LABELS.get(sid, sid),
            }
            # GitHub exposes a rate-limit flag; the index an availability flag.
            if sid == "github":
                try:
                    entry["rate_limited"] = bool(getattr(src, "is_rate_limited", False))
                except Exception:
                    entry["rate_limited"] = False
            if sid == "janus-index":
                try:
                    index_available = bool(getattr(src, "is_available", False))
                except Exception:
                    index_available = False
                entry["available"] = index_available
                # Empty-query search on the index returns featured/popular skills.
                if index_available:
                    try:
                        featured = [
                            web_server_mod._skill_meta_to_payload(m) for m in src.search("", limit=12)
                        ]
                    except Exception:
                        featured = []
            out.append(entry)
        return {
            "sources": out,
            "index_available": index_available,
            "featured": featured,
            "installed": web_server_mod._installed_hub_identifiers(),
        }

    try:
        return await web_server_mod.asyncio.to_thread(_run)
    except Exception as exc:
        web_server_mod._log.exception("skills hub sources listing failed")
        raise web_server_mod.HTTPException(status_code=502, detail=f"Hub sources failed: {exc}")

@router.get("/api/skills/hub/search")
async def search_skills_hub(q: str = "", source: str = "all", limit: int = 20):
    """Search the skill hub across all configured sources.

    Network-bound (parallel source search); runs in a thread so the FastAPI
    loop isn't blocked.  Returns structured results the UI installs by
    identifier via POST /api/skills/hub/install, previews via
    /api/skills/hub/preview, and scans via /api/skills/hub/scan.
    """
    query = (q or "").strip()
    if not query:
        return {"results": [], "source_counts": {}, "timed_out": [], "installed": {}}

    def _run():
        from tools.skills_hub import create_source_router, parallel_search_sources

        sources = create_source_router()
        capped = min(max(limit, 1), 50)
        all_results, source_counts, timed_out = parallel_search_sources(
            sources, query=query, source_filter=source or "all", overall_timeout=30
        )

        # Dedupe by identifier, preferring higher trust (mirrors unified_search).
        _rank = {"builtin": 2, "trusted": 1, "community": 0}
        seen = {}
        for r in all_results:
            if r.identifier not in seen:
                seen[r.identifier] = r
            elif _rank.get(r.trust_level, 0) > _rank.get(seen[r.identifier].trust_level, 0):
                seen[r.identifier] = r
        deduped = list(seen.values())[:capped]

        return {
            "results": [web_server_mod._skill_meta_to_payload(m) for m in deduped],
            "source_counts": source_counts,
            "timed_out": timed_out,
            "installed": web_server_mod._installed_hub_identifiers(),
        }

    try:
        return await web_server_mod.asyncio.to_thread(_run)
    except Exception as exc:
        web_server_mod._log.exception("skills hub search failed")
        raise web_server_mod.HTTPException(status_code=502, detail=f"Hub search failed: {exc}")

@router.get("/api/skills/hub/preview")
async def preview_skill_hub(identifier: str = ""):
    """Fetch a hub skill's SKILL.md content + metadata for in-dashboard reading.

    Resolves the identifier across configured sources (same path the CLI
    installer uses), then returns the rendered SKILL.md text and the file
    manifest WITHOUT installing anything.  This is the 'read the actual skill
    before installing' affordance the Browse-hub tab was missing.
    """
    ident = (identifier or "").strip()
    if not ident:
        raise web_server_mod.HTTPException(status_code=400, detail="identifier is required")

    def _run():
        from janus_cli.skills_hub import _resolve_source_meta_and_bundle
        from tools.skills_hub import create_source_router

        sources = create_source_router()
        meta, bundle, _src = _resolve_source_meta_and_bundle(ident, sources)
        if not bundle and not meta:
            return None

        files = {}
        skill_md = ""
        if bundle:
            for rel, content in (bundle.files or {}).items():
                if isinstance(content, bytes):
                    # Some sources (e.g. official optional skills) store every
                    # file as bytes.  Decode text so SKILL.md / docs render;
                    # only fall back to a placeholder for genuinely-binary data.
                    try:
                        files[rel] = content.decode("utf-8")
                    except UnicodeDecodeError:
                        files[rel] = "(binary file)"
                else:
                    files[rel] = content
            skill_md = files.get("SKILL.md", "") or ""

        m = meta or bundle
        return {
            "name": getattr(m, "name", ident),
            "description": getattr(m, "description", "") or "",
            "source": getattr(m, "source", "") or "",
            "identifier": getattr(m, "identifier", ident) or ident,
            "trust_level": getattr(m, "trust_level", "community") or "community",
            "repo": getattr(m, "repo", None),
            "tags": list(getattr(m, "tags", None) or []),
            "skill_md": skill_md,
            "files": sorted(files.keys()),
        }

    try:
        result = await web_server_mod.asyncio.to_thread(_run)
    except Exception as exc:
        web_server_mod._log.exception("skills hub preview failed")
        raise web_server_mod.HTTPException(status_code=502, detail=f"Hub preview failed: {exc}")
    if result is None:
        raise web_server_mod.HTTPException(status_code=404, detail=f"Skill not found: {ident}")
    return result

@router.get("/api/skills/hub/scan")
async def scan_skill_hub(identifier: str = ""):
    """Run the install-time security scan on a hub skill WITHOUT installing it.

    Fetches the bundle, quarantines it, and runs the same `scan_skill` /
    `should_allow_install` pipeline the CLI installer uses — then cleans up the
    quarantine.  Returns the verdict, per-finding detail, trust tier, and the
    install-policy decision so the dashboard can show a visual safety result
    on demand (the 'scan' button the Browse-hub tab was missing).
    """
    ident = (identifier or "").strip()
    if not ident:
        raise web_server_mod.HTTPException(status_code=400, detail="identifier is required")

    def _run():
        import shutil as _shutil

        from janus_cli.skills_hub import _resolve_source_meta_and_bundle
        from tools.skills_hub import create_source_router, quarantine_bundle
        from tools.skills_guard import scan_skill, should_allow_install

        sources = create_source_router()
        meta, bundle, _src = _resolve_source_meta_and_bundle(ident, sources)
        if not bundle:
            return None

        if bundle.source == "official":
            scan_source = "official"
        else:
            scan_source = (
                getattr(bundle, "identifier", "")
                or getattr(meta, "identifier", "")
                or ident
            )

        q_path = None
        try:
            q_path = quarantine_bundle(bundle)
            result = scan_skill(q_path, source=scan_source)
        finally:
            if q_path is not None:
                _shutil.rmtree(q_path, ignore_errors=True)

        allowed, reason = should_allow_install(result, force=False)
        # `allowed` may be None ("ask") for agent-created/dangerous gates.
        if allowed is True:
            policy = "allow"
        elif allowed is None:
            policy = "ask"
        else:
            policy = "block"

        findings = [
            {
                "severity": f.severity,
                "category": f.category,
                "file": f.file,
                "line": f.line,
                "description": f.description,
            }
            for f in result.findings
        ]
        # Per-severity tally for an at-a-glance summary.
        counts = {"critical": 0, "high": 0, "medium": 0, "low": 0}
        for f in result.findings:
            if f.severity in counts:
                counts[f.severity] += 1

        return {
            "name": result.skill_name,
            "identifier": ident,
            "source": result.source,
            "trust_level": result.trust_level,
            "verdict": result.verdict,
            "summary": result.summary,
            "policy": policy,
            "policy_reason": reason,
            "findings": findings,
            "severity_counts": counts,
        }

    try:
        result = await web_server_mod.asyncio.to_thread(_run)
    except Exception as exc:
        web_server_mod._log.exception("skills hub scan failed")
        raise web_server_mod.HTTPException(status_code=502, detail=f"Hub scan failed: {exc}")
    if result is None:
        raise web_server_mod.HTTPException(status_code=404, detail=f"Skill not found: {ident}")
    return result

@router.get("/api/skills")
async def get_skills():
    from tools.skills_tool import _find_all_skills
    from janus_cli.skills_config import get_disabled_skills
    config = web_server_mod.load_config()
    disabled = get_disabled_skills(config)
    skills = _find_all_skills(skip_disabled=True)
    for s in skills:
        s["enabled"] = s["name"] not in disabled
    return skills

@router.put("/api/skills/toggle")
async def toggle_skill(body: web_server_mod.SkillToggle):
    from janus_cli.skills_config import get_disabled_skills, save_disabled_skills
    config = web_server_mod.load_config()
    disabled = get_disabled_skills(config)
    if body.enabled:
        disabled.discard(body.name)
    else:
        disabled.add(body.name)
    save_disabled_skills(config, disabled)
    return {"ok": True, "name": body.name, "enabled": body.enabled}

