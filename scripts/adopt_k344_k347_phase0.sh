#!/usr/bin/env bash
# Phase-0 verify — K344–K347 batch + OOD stub (2026-09-17 ingest).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

for f in \
  wiki/sources/arxiv-2609-12443-through-wall-detection-sdr-pca.md \
  wiki/concepts/through-wall-detection-sdr-pca.md \
  wiki/sources/arxiv-2609-18173-indirect-third-party-sensor-tracking.md \
  wiki/concepts/indirect-third-party-sensor-vehicle-tracking.md \
  wiki/sources/arxiv-2609-18862-cashews-malicious-package-detection.md \
  wiki/concepts/cashews-llm-malicious-package-detection.md \
  wiki/sources/arxiv-2609-18864-asleval-privacy-exposure-displacement.md \
  wiki/concepts/asleval-privacy-exposure-displacement.md
do
  test -f "$ROOT/$f" || { echo "FAIL missing page: $f"; exit 1; }
done

grep -q "K344 Through-wall" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K347 ASLEval" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K344 Through-wall" "$ROOT/.cursor/rules/cemini-cybersec-k-dual-id.mdc"

python3 "$ROOT/scripts/restore_cybersec_dual_id.py" --check
python3 "$ROOT/scripts/test_k347_asleval_precheck.py" >/dev/null

echo "ALL PASS K344-K347 Phase-0"
