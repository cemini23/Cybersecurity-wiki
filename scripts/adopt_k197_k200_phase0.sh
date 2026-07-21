#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "== K197 A-MESS =="; test -f "$ROOT/wiki/concepts/defender-centric-jailbreak-utility.md"
echo "== K198 Bio =="; test -f "$ROOT/wiki/concepts/llm-biosecurity-red-teaming.md"
echo "== K199 Smart grid =="; test -f "$ROOT/wiki/concepts/solver-grounded-agentic-ot.md"
echo "== K200 SWE-Pruner =="
test -d "$ROOT/raw-sources/repos/swe-pruner-pro"
SIZE=$(du -sk "$ROOT/raw-sources/repos/swe-pruner-pro" | awk '{print $1}')
echo "clone ${SIZE}KB"; test "$SIZE" -lt 512000
rg -q 'Apache-2.0' "$ROOT/raw-sources/repos/swe-pruner-pro/pyproject.toml"
echo "ALL PASS"
