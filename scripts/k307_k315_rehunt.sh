#!/usr/bin/env bash
# SPDX re-hunt: K307 StepGuard + K310–K313 name collisions + K314 IAB watch.
# Never clones attack templates. Exit 0 = check complete (HOLD is not failure);
# exit 3 if any gh lookup failed, so an unverified state is never read as "absent".
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
. "$ROOT/scripts/gh_lookup.sh"
GH_LOOKUP_FAILED=0

echo "== K307 StepGuard =="
bash "$ROOT/scripts/stepguard_inventory.sh" check || {
  rc=$?; echo "  WARN stepguard_inventory exited ${rc}"; GH_LOOKUP_FAILED=1
}

echo "== K310–K313 name-collision HOLD (do not clone) =="
for repo in \
  kamatampadmasree56-ece/RTLGuardai \
  blessingcharles/AbacusCTF \
  getathelas/LoopHarness
do
  if gh_repo_exists "$repo"; then
    spdx="$(gh_repo_spdx "$repo")"
    case "$spdx" in
      "$GH_MISSING_SENTINEL") echo "  HOLD ${repo} — vanished between lookups" ;;
      "$GH_FAIL_SENTINEL") GH_LOOKUP_FAILED=1; echo "  HOLD ${repo} — license lookup failed, SPDX unknown" ;;
      *) echo "  HOLD ${repo} spdx=${spdx}" ;;
    esac
  else
    case "$?" in
      1) echo "  HOLD ${repo} missing" ;;
      *) GH_LOOKUP_FAILED=1; echo "  HOLD ${repo} — lookup failed, existence unknown" ;;
    esac
  fi
done

echo "== K314 InstructionArbitrationBench =="
bash "$ROOT/scripts/instruction_arbitration_bench_inventory.sh" || {
  rc=$?; echo "  WARN instruction_arbitration_bench_inventory exited ${rc}"; [[ "$rc" -eq 3 ]] && GH_LOOKUP_FAILED=1
}

echo "== K316–K319 SIR / EvoSkill / BLOOM-WILT =="
bash "$ROOT/scripts/k316_k319_inventory.sh" || {
  rc=$?; echo "  WARN k316_k319_inventory exited ${rc}"; [[ "$rc" -eq 3 ]] && GH_LOOKUP_FAILED=1
}

echo "== K320–K322 EvoFlint / construct validity / firmware =="
bash "$ROOT/scripts/k320_k322_inventory.sh" || {
  rc=$?; echo "  WARN k320_k322_inventory exited ${rc}"; [[ "$rc" -eq 3 ]] && GH_LOOKUP_FAILED=1
}

if [[ "$GH_LOOKUP_FAILED" -ne 0 ]]; then
  echo "FAIL re-hunt $(date +%F): at least one gh lookup failed — some results are unknown, not empty"
  exit 3
fi

echo "OK re-hunt $(date +%F): see inventory sections above"
