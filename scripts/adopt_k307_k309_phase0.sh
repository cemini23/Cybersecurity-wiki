#!/usr/bin/env bash
# Phase-0 verify — K307 StepGuard + K308 decorative CoT audit + K309 prompt security redistribution.
# StepGuard: CONDITIONAL-GO; LICENSE cleared 2026-09-30 (Apache-2.0), so a sparse REFERENCE clone
# under .local/adopts is permitted. No HF weight download.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

for f in \
  wiki/sources/arxiv-2608-24777-stepguard.md \
  wiki/concepts/step-level-agent-guardrails.md \
  wiki/entities/tools/stepguard.md \
  wiki/sources/arxiv-2608-24790-decorative-reasoning-medical-cot.md \
  wiki/concepts/chain-of-thought-decorative-reasoning-audit.md \
  wiki/sources/arxiv-2608-24857-prompt-structure-security-redistribution.md \
  wiki/concepts/llm-codegen-prompt-security-redistribution.md
do
  test -f "$ROOT/$f" || { echo "FAIL missing page: $f"; exit 1; }
done

# LICENSE cleared 2026-09-30 (Apache-2.0): a REFERENCE clone under .local/adopts is permitted.
# raw-sources/repos stays forbidden — this is a gitignored REFERENCE clone, not corpus material.
test ! -e "$ROOT/raw-sources/repos/StepGuard" \
  || { echo "FAIL StepGuard must not be copied into raw-sources/repos"; exit 1; }
if [[ -d "$ROOT/.local/adopts/StepGuard" ]]; then
  test -f "$ROOT/.local/adopts/StepGuard/LICENSE" \
    || { echo "FAIL StepGuard clone present but LICENSE missing"; exit 1; }
fi

grep -q "K307 StepGuard" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K307 StepGuard" "$ROOT/.cursor/rules/cemini-cybersec-mcp-tool-control.mdc"
grep -q "K308.*decorative\|K308.*CoT\|decorative reasoning" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K309.*prompt\|K309.*redistribut" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K307 StepGuard" "$ROOT/.cursor/rules/cemini-cybersec-k-dual-id.mdc"

python3 "$ROOT/scripts/restore_cybersec_dual_id.py" --check

bash "$ROOT/scripts/stepguard_inventory.sh" check

echo "ALL PASS K307-K309 Phase-0"
