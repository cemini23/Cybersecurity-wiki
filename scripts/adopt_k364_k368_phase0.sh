#!/usr/bin/env bash
# Phase-0 verify — K364–K368 batch + OOD stub (2026-09-24 ingest).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

for f in \
  wiki/sources/arxiv-2609-25294-controller-only-false-confirmation-rf-uav.md \
  wiki/concepts/passive-rf-uav-controller-only-false-confirmation.md \
  wiki/sources/arxiv-2609-26079-ble-mac-randomization-reidentification.md \
  wiki/concepts/ble-mac-randomization-reidentification-lab.md \
  wiki/sources/arxiv-2609-28372-agentic-ai-surrogate-consumer-ood.md
do
  test -f "$ROOT/$f" || { echo "FAIL missing page: $f"; exit 1; }
done

grep -q "K364 Controller-only" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K365 BLE MAC" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K366 Reliable inference" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K364 Passive RF" "$ROOT/.cursor/rules/cemini-cybersec-k-dual-id.mdc"

python3 "$ROOT/scripts/restore_cybersec_dual_id.py" --check
python3 "$ROOT/scripts/test_k365_ble_reid_lab_precheck.py" >/dev/null

echo "ALL PASS K364-K368 Phase-0"
