#!/usr/bin/env bash
# Phase-0 verify — K320 EvoFlint / K321 construct validity / K322 firmware rehost + 2 OOD stubs.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

for f in \
  wiki/sources/arxiv-2609-00487-evoflint-multi-turn-redteam.md \
  wiki/concepts/evoflint-multi-turn-redteam-atlas.md \
  wiki/sources/arxiv-2609-01519-guardrail-construct-validity.md \
  wiki/concepts/guardrail-construct-validity-agent-eval.md \
  wiki/sources/arxiv-2608-29737-reactive-peripheral-firmware-rehosting.md \
  wiki/concepts/firmware-rehosting-peripheral-fidelity.md \
  wiki/sources/arxiv-2609-01548-ood-sdare-bench.md \
  wiki/sources/arxiv-2609-01564-ood-confusion-aware-rag.md
do
  test -f "$ROOT/$f" || { echo "FAIL missing page: $f"; exit 1; }
done

grep -q "K320 EvoFlint" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K320 EvoFlint" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K321 Guardrail construct validity" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K322 Firmware" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K320 EvoFlint" "$ROOT/.cursor/rules/cemini-cybersec-k-dual-id.mdc"

python3 "$ROOT/scripts/restore_cybersec_dual_id.py" --check

for slug in \
  arxiv-2609-00487-evoflint-multi-turn-redteam \
  evoflint-multi-turn-redteam-atlas \
  arxiv-2609-01519-guardrail-construct-validity \
  guardrail-construct-validity-agent-eval \
  arxiv-2608-29737-reactive-peripheral-firmware-rehosting \
  firmware-rehosting-peripheral-fidelity \
  arxiv-2609-01548-ood-sdare-bench \
  arxiv-2609-01564-ood-confusion-aware-rag
do
  grep -q "$slug" "$ROOT/wiki/index.md" || { echo "FAIL index missing slug: $slug"; exit 1; }
done

bash "$ROOT/scripts/k320_k322_inventory.sh" >/dev/null

for script in \
  k320_evoflint_redteam_precheck.py \
  k321_guardrail_construct_validity_precheck.py \
  k322_firmware_rehost_precheck.py
do
  test -f "$ROOT/scripts/$script" || { echo "FAIL missing $script"; exit 1; }
done

for test in \
  test_k320_evoflint_redteam_precheck.py \
  test_k321_guardrail_construct_validity_precheck.py \
  test_k322_firmware_rehost_precheck.py
do
  test -f "$ROOT/scripts/$test" || { echo "FAIL missing $test"; exit 1; }
  python3 "$ROOT/scripts/$test" >/dev/null
done

for skill in \
  evoflint-redteam-eval \
  guardrail-construct-validity-audit \
  firmware-rehost-lab-precheck
do
  test -f "$ROOT/.cursor/skills/$skill/SKILL.md" || { echo "FAIL missing skill $skill"; exit 1; }
done

echo "ALL PASS K320-K322 Phase-0 + OOD stubs"
