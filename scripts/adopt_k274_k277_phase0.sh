#!/usr/bin/env bash
# Phase-0 verify — K274 WhiteNet + K275 wireless AInf + K276 withhold contract + K277 RSM (all REFERENCE, no clones)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
for f in \
  wiki/sources/arxiv-2608-06581-whitenet-spectral-whitening.md \
  wiki/concepts/spectral-whitening-wireless-protocol-id.md \
  wiki/sources/arxiv-2608-11337-association-privacy-wireless-formal.md \
  wiki/concepts/association-inference-attack-wireless.md \
  wiki/sources/arxiv-2608-12292-tutor-withhold-refusal-contract.md \
  wiki/concepts/refusal-under-knowledge-withhold-contract.md \
  wiki/sources/arxiv-2608-12311-rsm-role-specialization.md \
  wiki/concepts/role-specialization-multi-tool-coordination.md \
  wiki/sources/arxiv-2608-12290-ood-i2v-agentic-optimization.md
do
  test -f "$ROOT/$f"
done
rg -q 'K274 WhiteNet' "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
rg -q 'K275 AInf wireless' "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
rg -q 'K276 withhold contract' "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
rg -q 'K277' "$ROOT/.cursor/rules/cemini-cybersec-mcp-tool-control.mdc"
rg -q 'wont_wire' "$ROOT/wiki/sources/arxiv-2608-12290-ood-i2v-agentic-optimization.md"
rg -q 'K274\|K275\|K276\|K277' "$ROOT/wiki/index.md" || rg -q 'K274' "$ROOT/wiki/index.md"
# no clones expected — assert none were adopted
test ! -d "$ROOT/raw-sources/repos/WhiteNet"
test ! -d "$ROOT/raw-sources/repos/rsm-role-specialization"
echo "ALL PASS K274-K277 (all REFERENCE, no clones; OOD 12290 wont_wire; wires in lab-redteam + agent-audit + mcp-tool-control)"