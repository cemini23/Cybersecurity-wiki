#!/usr/bin/env bash
# K320–K322 artifact re-hunt: EvoFlint HF space, SDARE-Bench (OOD), firmware repo.
# Exit 1 if a forbidden clone exists on disk, 3 if a gh lookup failed; otherwise 0.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
. "$ROOT/scripts/gh_lookup.sh"
GH_LOOKUP_FAILED=0

echo "== K320 EvoFlint =="
for repo in reinforcelabs/EvoFlint; do
  spdx="$(gh_repo_spdx "$repo")"
  case "$spdx" in
    "$GH_MISSING_SENTINEL") echo "  WATCH ${repo} — no GitHub repo (HF space only)" ;;
    "$GH_FAIL_SENTINEL") GH_LOOKUP_FAILED=1; echo "  WATCH ${repo} spdx=unknown (lookup failed) (HF space may differ from GitHub)" ;;
    *) echo "  WATCH ${repo} spdx=${spdx} (HF space may differ from GitHub)" ;;
  esac
done
echo "  HF space: reinforcelabs/EvoFlint — WATCH; no clone until SPDX + operator OK"

echo "== K321 construct validity =="
echo "  pattern-only — no public SPDX repo required this batch"

echo "== K322 firmware rehost =="
echo "  pattern-only — no mandatory clone this batch"

echo "== OOD SDARE-Bench (not cyber wire) =="
spdx="$(gh_repo_spdx stephaniesyfong/SDARE-Bench)"
case "$spdx" in
  "$GH_MISSING_SENTINEL") echo "  stephaniesyfong/SDARE-Bench — not found on GitHub — OOD stub only" ;;
  "$GH_FAIL_SENTINEL") GH_LOOKUP_FAILED=1; echo "  stephaniesyfong/SDARE-Bench spdx=unknown (lookup failed) — OOD stub only" ;;
  *) echo "  stephaniesyfong/SDARE-Bench spdx=${spdx} — OOD stub only" ;;
esac

for bad in \
  "$ROOT/.local/adopts/EvoFlint" \
  "$ROOT/.local/adopts/SDARE-Bench" \
  "$ROOT/raw-sources/repos/EvoFlint"
do
  test ! -e "$bad" || { echo "FAIL forbidden clone exists: $bad"; exit 1; }
done

if [[ "$GH_LOOKUP_FAILED" -ne 0 ]]; then
  echo "FAIL: at least one gh lookup failed — results above are incomplete, not empty"
  exit 3
fi

exit 0
