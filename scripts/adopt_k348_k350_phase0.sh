#!/usr/bin/env bash
# Phase-0 verify — K348–K350 batch + OOD stub (2026-09-20 ingest).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

for f in \
  wiki/sources/arxiv-2609-19587-auto-mode-blocking-classifier-redteam.md \
  wiki/concepts/auto-mode-blocking-classifier-redteam.md \
  wiki/sources/arxiv-2609-20722-deep-noir-steering-discovery-chronometry.md \
  wiki/concepts/deep-noir-steering-discovery-chronometry.md \
  wiki/sources/arxiv-2609-20752-llm-falsifier-cyber-physical-systems.md \
  wiki/concepts/llm-falsifier-cyber-physical-systems.md
do
  test -f "$ROOT/$f" || { echo "FAIL missing page: $f"; exit 1; }
done

grep -q "K348 Auto Mode" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K349 Deep Noir" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K350 LLM-Falsifier" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K348 Auto Mode" "$ROOT/.cursor/rules/cemini-cybersec-k-dual-id.mdc"

python3 "$ROOT/scripts/restore_cybersec_dual_id.py" --check
python3 "$ROOT/scripts/test_k348_auto_mode_redteam_precheck.py" >/dev/null

echo "ALL PASS K348-K350 Phase-0"
