#!/usr/bin/env bash
# Phase-0 verify — K355–K363 batch + OOD stub (2026-09-23 ingest).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

for f in \
  wiki/sources/arxiv-2609-23894-agentic-ai-cross-dimensional-taxonomy.md \
  wiki/concepts/cross-dimensional-agentic-ai-security-taxonomy.md \
  wiki/sources/arxiv-2609-24972-rrsi-regularized-harness-self-improvement.md \
  wiki/concepts/rrsi-regularized-harness-self-improvement.md \
  wiki/sources/arxiv-2609-26725-figma-ai-product-design-ood.md
do
  test -f "$ROOT/$f" || { echo "FAIL missing page: $f"; exit 1; }
done

grep -q "K358 RRSI" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K361 Rouxii" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K362 GenAI access-control" "$ROOT/.cursor/rules/cemini-cybersec-mcp-tool-control.mdc"
grep -q "K355 Cross-dimensional" "$ROOT/.cursor/rules/cemini-cybersec-k-dual-id.mdc"

python3 "$ROOT/scripts/restore_cybersec_dual_id.py" --check
python3 "$ROOT/scripts/test_k358_rrsi_harness_precheck.py" >/dev/null
python3 "$ROOT/scripts/test_k359_covert_agentic_comm_precheck.py" >/dev/null
python3 "$ROOT/scripts/test_k361_rouxii_honeypot_precheck.py" >/dev/null

echo "ALL PASS K355-K363 Phase-0"
