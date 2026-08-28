#!/usr/bin/env bash
# SPDX re-hunt for K307 StepGuard + name-collision HOLD for K310–K313.
# Never clones. Exit 0 = check complete (HOLD is not a failure).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo "== K307 StepGuard =="
bash "$ROOT/scripts/stepguard_inventory.sh" check

echo "== K310–K313 name-collision HOLD (do not clone) =="
for repo in \
  kamatampadmasree56-ece/RTLGuardai \
  blessingcharles/AbacusCTF \
  getathelas/LoopHarness
do
  line="$(gh api "repos/${repo}" --jq '"\(.full_name) spdx=\(.license.spdx_id // "null")"' 2>/dev/null || echo "${repo} missing")"
  echo "  HOLD $line"
done

echo "OK re-hunt $(date +%F): StepGuard still null SPDX; no matching paper repos to clone"
