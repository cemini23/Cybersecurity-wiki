#!/usr/bin/env bash
# SPDX re-hunt: K307 StepGuard + K310–K313 name collisions + K314 IAB watch.
# Never clones attack templates. Exit 0 = check complete (HOLD is not failure).
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

echo "== K314 InstructionArbitrationBench =="
bash "$ROOT/scripts/instruction_arbitration_bench_inventory.sh"

echo "== K316–K319 SIR / EvoSkill / BLOOM-WILT =="
bash "$ROOT/scripts/k316_k319_inventory.sh"

echo "== K320–K322 EvoFlint / construct validity / firmware =="
bash "$ROOT/scripts/k320_k322_inventory.sh"

echo "OK re-hunt $(date +%F): see inventory sections above"
