#!/usr/bin/env bash
# K303/K298 Cursor deny hook — fail-closed. Do not echo stdin (may contain file contents).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
exec python3 "$ROOT/scripts/k303_k298_policy.py" --hook
