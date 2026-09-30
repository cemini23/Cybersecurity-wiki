#!/usr/bin/env bash
# K307 StepGuard REFERENCE inventory — LICENSE re-hunt, optional shallow clone, no HF weights.
# Lab-only; wont_wire as default MCP. HITL before any runtime guard integration.
# Exit 1 on a hard gate, 3 if a gh lookup failed; otherwise 0.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
. "$ROOT/scripts/gh_lookup.sh"
GH_LOOKUP_FAILED=0

REPO="zheng977/StepGuard"
CLONE="$ROOT/.local/adopts/StepGuard"
MODE="${1:-check}"

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

# Resolve the license state once, and keep "lookup failed" distinct from "absent".
SPDX="$(gh_repo_spdx "$REPO")"
case "$SPDX" in
  "$GH_MISSING_SENTINEL") echo "GitHub license.spdx_id: repo not found on GitHub"; SPDX="" ;;
  "$GH_FAIL_SENTINEL") GH_LOOKUP_FAILED=1; echo "GitHub license.spdx_id: lookup failed — unknown"; SPDX="" ;;
  *) echo "GitHub license.spdx_id: ${SPDX:-null}" ;;
esac

LICENSE_FILE="unknown"
if gh_repo_path_exists "$REPO" "LICENSE"; then
  LICENSE_FILE="present"
else
  case "$?" in
    1) LICENSE_FILE="missing" ;;
    *) LICENSE_FILE="lookup-failed"; GH_LOOKUP_FAILED=1 ;;
  esac
fi
case "$LICENSE_FILE" in
  present) echo "LICENSE file: present in repo root" ;;
  missing) echo "LICENSE file: missing in repo root" ;;
  *)       echo "LICENSE file: lookup failed — presence unknown" ;;
esac

ACCEPTABLE=no
if license_ok "$SPDX"; then ACCEPTABLE=yes; fi
if [[ "$LICENSE_FILE" == "present" ]]; then ACCEPTABLE=yes; fi

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
  elif [[ "$ACCEPTABLE" == "yes" ]]; then
    mkdir -p "$ROOT/.local/adopts"
    echo "==> shallow clone $REPO"
    git clone --depth 1 "https://github.com/${REPO}.git" "$CLONE"
    test -f "$CLONE/LICENSE" || { echo "FAIL post-clone LICENSE missing"; exit 1; }
    sz="$(du -sm "$CLONE" | cut -f1)"
    test "$sz" -lt 50 || { echo "FAIL clone ${sz}MB >= 50MB cap"; exit 1; }
    echo "OK REFERENCE clone (${sz}MB) — wont_wire runtime; no HF weights"
  elif [[ "$GH_LOOKUP_FAILED" -ne 0 ]]; then
    echo "FAIL adopt blocked — gh lookup failed, SPDX unknown"
    exit 3
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

if [[ "$GH_LOOKUP_FAILED" -ne 0 ]]; then
  echo "FAIL: gh lookup failed — StepGuard license state is unknown, not 'absent'"
  exit 3
fi

if [[ "$MODE" == "check" ]] && [[ ! -d "$CLONE" ]] && [[ "$ACCEPTABLE" != "yes" ]]; then
  echo "HOLD clone — LICENSE re-hunt $(date +%F): still NO-GO"
  exit 0
fi

echo "ALL PASS stepguard_inventory ($MODE)"
