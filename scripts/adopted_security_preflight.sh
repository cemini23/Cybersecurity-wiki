#!/usr/bin/env bash
# Thin wrapper — Cursor security preflight is federation-canon in CCC.
# Defaults to ALL Cursor workspaces so Open Folder on any repo stays covered.
# Use --local to scan only this wiki.
set -euo pipefail

CCC_SCRIPT="/Users/claudiobarone/Projects/Cemini claude code CCC/scripts/cursor_security_preflight_federation.sh"
if [[ ! -f "$CCC_SCRIPT" ]]; then
  echo "FAIL missing canon script: $CCC_SCRIPT" >&2
  exit 1
fi

# Default: federation-wide. Pass --local for this repo only.
if [[ $# -eq 0 ]]; then
  exec bash "$CCC_SCRIPT" --all
fi
exec bash "$CCC_SCRIPT" "$@"
