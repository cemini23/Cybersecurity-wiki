#!/usr/bin/env bash
# Phase-0 verify — K316 SIR / K317 EvoSkill / K318 J-lens / K319 BLOOM-WILT + OOD OntoLearner.
# In-scope are REFERENCE (no clone). No attack templates / elicitation payloads in wiki.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

for f in \
  wiki/sources/arxiv-2608-30207-sir-cua-self-improving-redteam.md \
  wiki/concepts/failure-driven-cua-ipi-red-teaming.md \
  wiki/sources/arxiv-2608-30429-evoskill-injection.md \
  wiki/concepts/evoskill-injection-self-evolving-agents.md \
  wiki/sources/arxiv-2608-31084-j-lens-multi-token-readout.md \
  wiki/concepts/multi-token-concept-readout-audit.md \
  wiki/sources/arxiv-2608-31105-bloom-wilt-logit-tilting-audit.md \
  wiki/concepts/logit-tilting-rare-behaviour-audit.md \
  wiki/sources/arxiv-2608-31118-ontolearn-llm-size-ood.md
do
  test -f "$ROOT/$f" || { echo "FAIL missing page: $f"; exit 1; }
done

for bad in \
  "$ROOT/.local/adopts/bloom-wilt" \
  "$ROOT/.local/adopts/SIR" \
  "$ROOT/.local/adopts/EvoSkillBench" \
  "$ROOT/raw-sources/repos/bloom-wilt" \
  "$ROOT/raw-sources/repos/AdrSkapars-bloom-wilt"
do
  test ! -e "$bad" || { echo "FAIL forbidden clone exists: $bad"; exit 1; }
done

grep -q "K316 SIR" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K317 EvoSkill" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K316 SIR" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K317 EvoSkill" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K319 BLOOM-WILT" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K316 SIR" "$ROOT/.cursor/rules/cemini-cybersec-k-dual-id.mdc"

python3 "$ROOT/scripts/restore_cybersec_dual_id.py" --check

for slug in \
  arxiv-2608-30207-sir-cua-self-improving-redteam \
  failure-driven-cua-ipi-red-teaming \
  arxiv-2608-30429-evoskill-injection \
  evoskill-injection-self-evolving-agents \
  arxiv-2608-31084-j-lens-multi-token-readout \
  multi-token-concept-readout-audit \
  arxiv-2608-31105-bloom-wilt-logit-tilting-audit \
  logit-tilting-rare-behaviour-audit \
  arxiv-2608-31118-ontolearn-llm-size-ood
do
  grep -q "$slug" "$ROOT/wiki/index.md" || { echo "FAIL index missing slug: $slug"; exit 1; }
done

echo "ALL PASS K316-K319 Phase-0 + OOD OntoLearner"
