#!/usr/bin/env bash
# Phase-0 verify — K395-K397 (2026-10-06).
# K395/K396: no public artifact -> REFERENCE, no clone.
# K397: repo chchenhui/frugalevo is Apache-2.0 but 305MB and only tangentially security-relevant
#       -> REFERENCE. A clone is permitted by licence but is NOT adopted this batch.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

for f in \
  wiki/sources/arxiv-2610-03531-authorship-attribution-zero-shot-representations.md \
  wiki/concepts/authorship-attribution-author-representation.md \
  wiki/sources/arxiv-2610-03585-threat-preserving-representation-sensitivity.md \
  wiki/concepts/threat-preserving-representation-sensitivity.md \
  wiki/sources/arxiv-2610-03675-frugalevo-cost-aware-program-evolution.md \
  wiki/concepts/budget-aware-agentic-search-cost.md
do
  test -f "$ROOT/$f" || { echo "FAIL missing page: $f"; exit 1; }
done

# No doubled extension from the emit-script slug bug.
test -z "$(find "$ROOT/wiki" -name '*.md.md' -print -quit)" \
  || { echo "FAIL a page has a doubled .md extension"; exit 1; }

# FrugalEvo is REFERENCE-only this batch despite a clear licence.
for bad in \
  "$ROOT/.local/adopts/frugalevo" \
  "$ROOT/.local/adopts/FrugalEvo" \
  "$ROOT/raw-sources/repos/frugalevo" \
  "$ROOT/raw-sources/repos/FrugalEvo"
do
  test ! -e "$bad" || { echo "FAIL FrugalEvo clone present (REFERENCE-only this batch): $bad"; exit 1; }
done

grep -q "K396 TPRS" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K395 Authorship" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K397 FrugalEvo" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K395" "$ROOT/.cursor/rules/cemini-cybersec-k-dual-id.mdc"
grep -q "K397" "$ROOT/.cursor/rules/cemini-cybersec-k-dual-id.mdc"
grep -q "K300–K3" "$ROOT/.cursor/rules/cemini-cybersec-k-dual-id.mdc"
grep -q "K395" "$ROOT/.cursor/rules/overlays/cybersec-k-dual-id.fragment.mdc"
grep -q "K300–K3" "$ROOT/.cursor/rules/overlays/cybersec-k-dual-id.fragment.mdc"

python3 "$ROOT/scripts/restore_cybersec_dual_id.py" --check
python3 "$ROOT/scripts/k396_benchmark_representation_precheck.py" selftest
test -f "$ROOT/.cursor/skills/benchmark-representation-precheck/SKILL.md"

echo "ALL PASS K395-K397 Phase-0"
