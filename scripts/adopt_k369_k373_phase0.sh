#!/usr/bin/env bash
# Phase-0 verify — K369–K373 batch + OOD stub (2026-09-25 ingest).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

for f in \
  wiki/sources/arxiv-2609-28940-calibrated-decision-models-pentest-harness-jev.md \
  wiki/concepts/calibrated-decision-models-pentest-harness-jev.md \
  wiki/sources/arxiv-2609-29213-ble-backscatter-polarization-shift-identification.md \
  wiki/concepts/ble-backscatter-polarization-shift-identification-lab.md \
  wiki/sources/arxiv-2609-30217-instrumental-monitor-evasion-evaluation.md \
  wiki/concepts/instrumental-monitor-evasion-evaluation.md \
  wiki/sources/arxiv-2609-30266-llm-agents-trace-tampering.md \
  wiki/concepts/agent-execution-trace-tampering-audit.md \
  wiki/sources/arxiv-2609-30233-coding-agents-generalized-tamp-ood.md
do
  test -f "$ROOT/$f" || { echo "FAIL missing page: $f"; exit 1; }
done

grep -q "K369 Calibrated" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K370 BLE backscatter" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K371 Instrumental monitor" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K373 Agent execution trace" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K369 Calibrated pentest" "$ROOT/.cursor/rules/cemini-cybersec-k-dual-id.mdc"

python3 "$ROOT/scripts/restore_cybersec_dual_id.py" --check
python3 "$ROOT/scripts/test_k371_instrumental_monitor_evasion_precheck.py" >/dev/null
python3 "$ROOT/scripts/test_k373_agent_trace_tampering_precheck.py" >/dev/null

echo "ALL PASS K369-K373 Phase-0"
