#!/usr/bin/env bash
# Phase-0 verify — K307 StepGuard + K308 decorative CoT audit + K309 prompt security redistribution.
# StepGuard: CONDITIONAL-GO pending LICENSE; no clone until SPDX. No HF weight download.
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

# No StepGuard clone without LICENSE
for bad in \
  "$ROOT/.local/adopts/StepGuard" \
  "$ROOT/raw-sources/repos/StepGuard"
do
  test ! -e "$bad" || { echo "FAIL StepGuard clone exists before LICENSE verify: $bad"; exit 1; }
done

grep -q "K307 StepGuard" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K307 StepGuard" "$ROOT/.cursor/rules/cemini-cybersec-mcp-tool-control.mdc"
grep -q "K308.*decorative\|K308.*CoT\|decorative reasoning" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K309.*prompt\|K309.*redistribut" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K307 StepGuard" "$ROOT/.cursor/rules/cemini-cybersec-k-dual-id.mdc"

python3 "$ROOT/scripts/restore_cybersec_dual_id.py" --check

echo "ALL PASS K307-K309 Phase-0"
