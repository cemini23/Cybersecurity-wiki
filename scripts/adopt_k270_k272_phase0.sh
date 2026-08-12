#!/usr/bin/env bash
# Phase-0 verify — K270 GFlowNet attacks (REFERENCE) + K271 REDAgentBench (REFERENCE) + K272 Cross-lingual safety (REFERENCE) + OOD routes
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
for f in \
  wiki/sources/arxiv-2608-10171-gflownets-llm-attacks-turkcell.md \
  wiki/concepts/gflownet-automated-redteam-attack-generation.md \
  wiki/sources/arxiv-2608-10669-redagentbench-faithful-agent-asr.md \
  wiki/concepts/faithful-agent-asr-measurement.md \
  wiki/entities/tools/redagentbench.md \
  wiki/sources/arxiv-2608-11146-illusion-cross-lingual-safety-lrl.md \
  wiki/concepts/cross-lingual-safety-transfer-lrl.md \
  wiki/sources/arxiv-2608-11044-ood-teammix-htc.md \
  wiki/sources/arxiv-2608-11121-ood-genai-statistical-research.md
do
  test -f "$ROOT/$f"
done
# All three in-scope papers REFERENCE — assert NO clones exist
test ! -d "$ROOT/raw-sources/repos/redagentbench"
test ! -d "$ROOT/raw-sources/repos/gflownet-llm-attacks"
test ! -d "$ROOT/raw-sources/repos/lodna-cross-lingual"
rg -q 'K270 GFlowNet attacks' "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
rg -q 'K271 REDAgentBench' "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
rg -q 'K272 Cross-lingual safety' "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
rg -q 'K271 REDAgentBench' "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
rg -q 'K270' "$ROOT/wiki/sources/arxiv-2608-10171-gflownets-llm-attacks-turkcell.md"
rg -q 'K271' "$ROOT/wiki/sources/arxiv-2608-10669-redagentbench-faithful-agent-asr.md"
rg -q 'K272' "$ROOT/wiki/sources/arxiv-2608-11146-illusion-cross-lingual-safety-lrl.md"
echo "ALL PASS K270/K271/K272 REFERENCE (no clones); OOD 11044/11121 stubbed; wires in lab-redteam + agent-audit"
