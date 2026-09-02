#!/usr/bin/env bash
# K320–K322 artifact re-hunt: EvoFlint HF space, SDARE-Bench (OOD), firmware repo.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo "== K320 EvoFlint =="
for repo in reinforcelabs/EvoFlint; do
  spdx="$(gh api "repos/${repo}" --jq '.license.spdx_id // "null"' 2>/dev/null || echo "missing")"
  echo "  WATCH ${repo} spdx=${spdx} (HF space may differ from GitHub)"
done
echo "  HF space: reinforcelabs/EvoFlint — WATCH; no clone until SPDX + operator OK"

echo "== K321 construct validity =="
echo "  pattern-only — no public SPDX repo required this batch"

echo "== K322 firmware rehost =="
echo "  pattern-only — no mandatory clone this batch"

echo "== OOD SDARE-Bench (not cyber wire) =="
spdx="$(gh api repos/stephaniesyfong/SDARE-Bench --jq '.license.spdx_id // "null"' 2>/dev/null || echo "missing")"
echo "  stephaniesyfong/SDARE-Bench spdx=${spdx} — OOD stub only"

for bad in \
  "$ROOT/.local/adopts/EvoFlint" \
  "$ROOT/.local/adopts/SDARE-Bench" \
  "$ROOT/raw-sources/repos/EvoFlint"
do
  test ! -e "$bad" || { echo "FAIL forbidden clone exists: $bad"; exit 1; }
done

exit 0
