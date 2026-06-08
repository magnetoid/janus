#!/bin/bash
# Kill all running Modal apps (sandboxes, deployments, etc.)
#
# Usage:
#   bash scripts/kill_modal.sh          # Stop janus-agent sandboxes
#   bash scripts/kill_modal.sh --all    # Stop ALL Modal apps

set -uo pipefail

echo "Fetching Modal app list..."
APP_LIST=$(modal app list 2>/dev/null)

if [[ "${1:-}" == "--all" ]]; then
    echo "Stopping ALL Modal apps..."
    echo "$APP_LIST" | grep -oE 'ap-[A-Za-z0-9]+' | sort -u | while read app_id; do
        echo "  Stopping $app_id"
        modal app stop "$app_id" 2>/dev/null || true
    done
else
    echo "Stopping janus-agent sandboxes..."
    APPS=$(echo "$APP_LIST" | grep 'janus-agent' | grep -oE 'ap-[A-Za-z0-9]+' || true)
    if [[ -z "$APPS" ]]; then
        echo "  No janus-agent apps found."
    else
        echo "$APPS" | while read app_id; do
            echo "  Stopping $app_id"
            modal app stop "$app_id" 2>/dev/null || true
        done
    fi
fi

echo ""
echo "Current janus-agent status:"
modal app list 2>/dev/null | grep -E 'State|janus-agent' || echo "  (none)"
