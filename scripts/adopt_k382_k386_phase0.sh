#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
for f in \
  wiki/sources/arxiv-2609-36474-finrt-amortized-redteam-generator.md \
  wiki/concepts/finrt-amortized-redteam-generator.md \
  wiki/sources/arxiv-2609-36570-countersteer-activation-steering-ipi-defense.md \
  wiki/concepts/countersteer-activation-steering-ipi-defense.md \
  wiki/sources/arxiv-2609-36739-frontier-autolab-temporal-leakage.md \
  wiki/concepts/frontier-autolab-organizational-memory-leakage.md \
  wiki/sources/arxiv-2609-38021-auditable-long-term-memory-retrieval-chain.md \
  wiki/concepts/auditable-long-term-memory-retrieval-chain.md \
  wiki/sources/arxiv-2609-38099-rice-in-context-dense-retrieval.md \
  wiki/concepts/rice-in-context-dense-retrieval.md
do
  test -f "$ROOT/$f"
done
grep -q "K382 FinRT" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K383 CounterSteer" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K384 Frontier Autolab" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K382 FinRT" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K383 CounterSteer" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K384 Frontier Autolab" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K385 Auditable long-term memory" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K386 RICE" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K383 CounterSteer" "$ROOT/.cursor/rules/cemini-cybersec-mcp-tool-control.mdc"
grep -q "K382 FinRT" "$ROOT/.cursor/rules/cemini-cybersec-k-dual-id.mdc"
grep -q "K386 RICE" "$ROOT/.cursor/rules/cemini-cybersec-k-dual-id.mdc"
grep -q "K300–K386" "$ROOT/.cursor/rules/cemini-cybersec-k-dual-id.mdc"
grep -q "K382 FinRT" "$ROOT/.cursor/rules/overlays/cybersec-k-dual-id.fragment.mdc"
grep -q "K300–K386" "$ROOT/.cursor/rules/overlays/cybersec-k-dual-id.fragment.mdc"
python3 "$ROOT/scripts/restore_cybersec_dual_id.py" --check
python3 "$ROOT/scripts/k382_finrt_amortized_redteam_precheck.py" selftest
python3 "$ROOT/scripts/k383_countersteer_ipi_precheck.py" selftest
python3 "$ROOT/scripts/k384_frontier_autolab_leakage_precheck.py" selftest
test -f "$ROOT/.cursor/skills/finrt-amortized-redteam-precheck/SKILL.md"
test -f "$ROOT/.cursor/skills/countersteer-ipi-precheck/SKILL.md"
test -f "$ROOT/.cursor/skills/frontier-autolab-leakage-precheck/SKILL.md"
echo ALL PASS K382-K386 Phase-0
