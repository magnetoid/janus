from fastapi import APIRouter, HTTPException, Request, Response, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import Any, Dict, List, Optional, Tuple, Union
import janus_cli.web_server as web_server_mod

router = APIRouter()

@router.get("/api/dashboard/themes")
async def get_dashboard_themes():
    """Return available themes and the currently active one.

    Built-in entries ship name/label/description only (the frontend owns
    their full definitions in `web/src/themes/presets.ts`).  User themes
    from `~/.janus/dashboard-themes/*.yaml` ship with their full
    normalised definition under `definition`, so the client can apply
    them without a stub.
    """
    config = web_server_mod.load_config()
    active = web_server_mod.cfg_get(config, "dashboard", "theme", default="default")
    user_themes = web_server_mod._discover_user_themes()
    seen = set()
    themes = []
    for t in web_server_mod._BUILTIN_DASHBOARD_THEMES:
        seen.add(t["name"])
        themes.append(t)
    for t in user_themes:
        if t["name"] in seen:
            continue
        themes.append({
            "name": t["name"],
            "label": t["label"],
            "description": t["description"],
            "definition": t,
        })
        seen.add(t["name"])
    return {"themes": themes, "active": active}

@router.put("/api/dashboard/theme")
async def set_dashboard_theme(body: web_server_mod.ThemeSetBody):
    """Set the active dashboard theme (persists to config.yaml)."""
    config = web_server_mod.load_config()
    if "dashboard" not in config:
        config["dashboard"] = {}
    config["dashboard"]["theme"] = body.name
    web_server_mod.save_config(config)
    return {"ok": True, "theme": body.name}

@router.get("/api/dashboard/font")
async def get_dashboard_font():
    """Return the active font override (``"theme"`` = use the theme's font)."""
    config = web_server_mod.load_config()
    font = web_server_mod.cfg_get(config, "dashboard", "font", default=web_server_mod._FONT_DEFAULT_ID)
    if font not in web_server_mod._FONT_CHOICES:
        font = web_server_mod._FONT_DEFAULT_ID
    return {"font": font}

@router.put("/api/dashboard/font")
async def set_dashboard_font(body: web_server_mod.FontSetBody):
    """Set the dashboard font override (persists to config.yaml).

    Accepts any id in the curated catalog, or ``"theme"`` to clear the
    override and fall back to the active theme's own font. Unknown ids are
    coerced to ``"theme"`` rather than 400'd so a stale client can't wedge
    the picker.
    """
    font = body.font if body.font in web_server_mod._FONT_CHOICES else web_server_mod._FONT_DEFAULT_ID
    config = web_server_mod.load_config()
    if "dashboard" not in config:
        config["dashboard"] = {}
    config["dashboard"]["font"] = font
    web_server_mod.save_config(config)
    return {"ok": True, "font": font}

@router.get("/api/dashboard/plugins")
async def get_dashboard_plugins():
    """Return discovered dashboard plugins (excludes user-hidden ones)."""
    plugins = web_server_mod._get_dashboard_plugins()
    # Read user's hidden plugins list from config.
    config = web_server_mod.load_config()
    hidden: list = web_server_mod.cfg_get(config, "dashboard", "hidden_plugins", default=[]) or []
    # Strip internal fields before sending to frontend and filter out hidden.
    return [
        {k: v for k, v in p.items() if not k.startswith("_")}
        for p in plugins
        if p["name"] not in hidden
    ]

@router.get("/api/dashboard/plugins/rescan")
async def rescan_dashboard_plugins():
    """Force re-scan of dashboard plugins."""
    plugins = web_server_mod._get_dashboard_plugins(force_rescan=True)
    return {"ok": True, "count": len(plugins)}

@router.get("/api/dashboard/plugins/hub")
async def get_plugins_hub(request: web_server_mod.Request):
    """Unified agent plugins + dashboard extension metadata (session protected)."""
    web_server_mod._require_token(request)
    try:
        return web_server_mod._merged_plugins_hub()
    except Exception as exc:
        web_server_mod._log.warning("plugins/hub failed: %s", exc)
        raise web_server_mod.HTTPException(status_code=500, detail="Failed to build plugins hub.") from exc

@router.post("/api/dashboard/agent-plugins/install")
async def post_agent_plugin_install(request: web_server_mod.Request, body: web_server_mod._AgentPluginInstallBody):
    web_server_mod._require_token(request)
    from janus_cli.plugins_cmd import dashboard_install_plugin

    result = dashboard_install_plugin(
        body.identifier.strip(),
        force=body.force,
        enable=body.enable,
    )
    if not result.get("ok"):
        raise web_server_mod.HTTPException(
            status_code=400,
            detail=result.get("error") or "Install failed.",
        )
    web_server_mod._get_dashboard_plugins(force_rescan=True)
    # Strip internal paths from the response
    result.pop("after_install_path", None)
    return result

@router.post("/api/dashboard/agent-plugins/{name:path}/enable")
async def post_agent_plugin_enable(request: web_server_mod.Request, name: str):
    web_server_mod._require_token(request)
    name = web_server_mod._validate_plugin_name(name)
    from janus_cli.plugins_cmd import dashboard_set_agent_plugin_enabled

    result = dashboard_set_agent_plugin_enabled(name, enabled=True)
    if not result.get("ok"):
        raise web_server_mod.HTTPException(status_code=400, detail=result.get("error") or "Enable failed.")
    return result

@router.post("/api/dashboard/agent-plugins/{name:path}/disable")
async def post_agent_plugin_disable(request: web_server_mod.Request, name: str):
    web_server_mod._require_token(request)
    name = web_server_mod._validate_plugin_name(name)
    from janus_cli.plugins_cmd import dashboard_set_agent_plugin_enabled

    result = dashboard_set_agent_plugin_enabled(name, enabled=False)
    if not result.get("ok"):
        raise web_server_mod.HTTPException(status_code=400, detail=result.get("error") or "Disable failed.")
    return result

@router.post("/api/dashboard/agent-plugins/{name:path}/update")
async def post_agent_plugin_update(request: web_server_mod.Request, name: str):
    web_server_mod._require_token(request)
    name = web_server_mod._validate_plugin_name(name)
    from janus_cli.plugins_cmd import dashboard_update_user_plugin

    result = dashboard_update_user_plugin(name)
    if not result.get("ok"):
        raise web_server_mod.HTTPException(status_code=400, detail=result.get("error") or "Update failed.")
    web_server_mod._get_dashboard_plugins(force_rescan=True)
    return result

@router.delete("/api/dashboard/agent-plugins/{name:path}")
async def delete_agent_plugin(request: web_server_mod.Request, name: str):
    web_server_mod._require_token(request)
    name = web_server_mod._validate_plugin_name(name)
    from janus_cli.plugins_cmd import dashboard_remove_user_plugin

    result = dashboard_remove_user_plugin(name)
    if not result.get("ok"):
        raise web_server_mod.HTTPException(status_code=400, detail=result.get("error") or "Remove failed.")
    web_server_mod._get_dashboard_plugins(force_rescan=True)
    return result

@router.put("/api/dashboard/plugin-providers")
async def put_plugin_providers(request: web_server_mod.Request, body: web_server_mod._PluginProvidersPutBody):
    """Persist memory provider / context engine selection (writes config.yaml)."""
    web_server_mod._require_token(request)
    from janus_cli.plugins_cmd import (
        _save_context_engine,
        _save_memory_provider,
    )

    if body.memory_provider is not None:
        _save_memory_provider(body.memory_provider)
    if body.context_engine is not None:
        _save_context_engine(body.context_engine)
    return {"ok": True}

@router.post("/api/dashboard/plugins/{name:path}/visibility")
async def post_plugin_visibility(request: web_server_mod.Request, name: str, body: web_server_mod._PluginVisibilityBody):
    """Toggle a plugin's sidebar visibility (persists to config.yaml dashboard.hidden_plugins)."""
    web_server_mod._require_token(request)
    name = web_server_mod._validate_plugin_name(name)

    config = web_server_mod.load_config()
    if "dashboard" not in config or not isinstance(config.get("dashboard"), dict):
        config["dashboard"] = {}
    hidden_list: list = config["dashboard"].get("hidden_plugins") or []
    if not isinstance(hidden_list, list):
        hidden_list = []

    if body.hidden and name not in hidden_list:
        hidden_list.append(name)
    elif not body.hidden and name in hidden_list:
        hidden_list.remove(name)

    config["dashboard"]["hidden_plugins"] = hidden_list
    web_server_mod.save_config(config)
    return {"ok": True, "name": name, "hidden": body.hidden}

