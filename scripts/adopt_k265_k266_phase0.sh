#!/usr/bin/env bash
# Phase-0 verify — K265 Blast Radius (REFERENCE) + K266 ShieldAI (GO clone)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
for f in \
  wiki/concepts/blast-radius-reversible-context-eviction.md \
  wiki/concepts/taxonomy-driven-oss-ai-risk-mitigation.md \
  wiki/sources/arxiv-2608-07440-blast-radius.md \
  wiki/sources/arxiv-2608-07446-shieldai-oss-ai-risk-tools.md \
  wiki/sources/arxiv-ood-qnlp-discocat-financial-2608.07439.md \
  wiki/entities/tools/blast-radius-necrophoresis.md \
  wiki/entities/tools/shieldai-risk-taxonomy-mapping.md
do
  test -f "$ROOT/$f"
done
test -d "$ROOT/raw-sources/repos/ShieldAI"
test -f "$ROOT/raw-sources/repos/ShieldAI/LICENSE.txt"
rg -q 'Apache' "$ROOT/raw-sources/repos/ShieldAI/LICENSE.txt"
SZ=$(du -sk "$ROOT/raw-sources/repos/ShieldAI" | awk '{print $1}')
test "$SZ" -lt 512000
rg -q 'Blast Radius / K265' "$ROOT/.cursor/rules/cemini-phase1-policy-wires.mdc"
rg -q 'K266 ShieldAI' "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
echo "ALL PASS ShieldAI=${SZ}KB (K265 REFERENCE no clone; K266 GO ~${SZ}KB; OOD 07439 stubbed)"
