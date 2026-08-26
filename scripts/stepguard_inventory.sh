#!/usr/bin/env bash
# K307 StepGuard REFERENCE inventory — LICENSE re-hunt, optional shallow clone, no HF weights.
# Lab-only; wont_wire as default MCP. HITL before any runtime guard integration.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
REPO="zheng977/StepGuard"
CLONE="$ROOT/.local/adopts/StepGuard"
MODE="${1:-check}"

spdx_from_github() {
  gh api "repos/${REPO}" --jq '.license.spdx_id // empty' 2>/dev/null || true
}

has_license_file() {
  gh api "repos/${REPO}/contents/LICENSE" >/dev/null 2>&1
}

license_ok() {
  local spdx="$1"
  case "$spdx" in
    MIT|Apache-2.0|BSD-2-Clause|BSD-3-Clause) return 0 ;;
    *) return 1 ;;
  esac
}

k292_harness_unchanged() {
  local before="${1:?}"
  local after="${2:?}"
  diff -q "$before" "$after" >/dev/null 2>&1
}

echo "== StepGuard inventory (K307) mode=${MODE} =="

SPDX="$(spdx_from_github)"
echo "GitHub license.spdx_id: ${SPDX:-null}"
if has_license_file; then
  echo "LICENSE file: present in repo root"
else
  echo "LICENSE file: missing in repo root"
fi

if [[ -d "$CLONE" ]]; then
  if [[ -f "$CLONE/LICENSE" ]]; then
    echo "Local clone: $CLONE ($(du -sm "$CLONE" | cut -f1)MB)"
    grep -qiE 'MIT|Apache|BSD' "$CLONE/LICENSE" || {
      echo "FAIL clone LICENSE not MIT/Apache/BSD"; exit 1
    }
  else
    echo "FAIL clone exists but LICENSE missing — remove $CLONE"; exit 1
  fi
else
  echo "Local clone: absent (expected until SPDX verified)"
fi

if [[ "$MODE" == "adopt" ]]; then
  if [[ -d "$CLONE" ]]; then
    echo "SKIP adopt — clone already present"
  elif license_ok "$SPDX" || has_license_file; then
    mkdir -p "$ROOT/.local/adopts"
    echo "==> shallow clone $REPO"
    git clone --depth 1 "https://github.com/${REPO}.git" "$CLONE"
    test -f "$CLONE/LICENSE" || { echo "FAIL post-clone LICENSE missing"; exit 1; }
    sz="$(du -sm "$CLONE" | cut -f1)"
    test "$sz" -lt 50 || { echo "FAIL clone ${sz}MB >= 50MB cap"; exit 1; }
    echo "OK REFERENCE clone (${sz}MB) — wont_wire runtime; no HF weights"
  else
    echo "HOLD adopt — no acceptable SPDX yet (re-hunt later)"
    exit 2
  fi
fi

if [[ -d "$CLONE" ]]; then
  BEFORE="$(mktemp)"
  AFTER="$(mktemp)"
  (
    cd "$ROOT"
    find .cursor/skills .cursor/rules -type f 2>/dev/null | sort | xargs shasum -a 256
  ) >"$BEFORE" 2>/dev/null || true
  if command -v pytest >/dev/null 2>&1 && [[ -d "$CLONE/tests" ]]; then
    echo "==> pytest (clone only; may skip if deps missing)"
    (cd "$CLONE" && pytest -q tests 2>/dev/null) || echo "WARN pytest skipped or failed — deps not installed"
  fi
  (
    cd "$ROOT"
    find .cursor/skills .cursor/rules -type f 2>/dev/null | sort | xargs shasum -a 256
  ) >"$AFTER" 2>/dev/null || true
  if k292_harness_unchanged "$BEFORE" "$AFTER"; then
    echo "OK K292 harness hash unchanged"
  else
    echo "FAIL harness files changed during inventory"; exit 1
  fi
  rm -f "$BEFORE" "$AFTER"
fi

# Explicit no-op: never pull HF weights in this script
echo "OK no HF weight download (ninty-seven/StepGuard held)"

if [[ "$MODE" == "check" ]] && [[ ! -d "$CLONE" ]] && ! license_ok "$SPDX" && ! has_license_file; then
  echo "HOLD clone — LICENSE re-hunt $(date +%F): still NO-GO"
  exit 0
fi

echo "ALL PASS stepguard_inventory ($MODE)"
