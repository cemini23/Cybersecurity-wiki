#!/usr/bin/env bash
# Phase-0 verify — K314 Recognition–enforcement gap + K315 Security-agent SLR + OOD NL2AGBench.
# In-scope are REFERENCE (no clone). No attack templates in wiki.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

# 1. Every page listed in the ingest plan exists.
for f in \
  wiki/sources/arxiv-2608-28502-recognition-without-enforcement.md \
  wiki/concepts/recognition-enforcement-gap-instruction-arbitration.md \
  wiki/sources/arxiv-2608-28490-llm-security-agents-survey.md \
  wiki/concepts/security-agent-authority-auditability-slr.md \
  wiki/sources/arxiv-2608-28481-ood-nl2agbench.md
do
  test -f "$ROOT/$f" || { echo "FAIL missing page: $f"; exit 1; }
done

# 2. No forbidden clones this batch.
for bad in \
  "$ROOT/.local/adopts/InstructionArbitrationBench" \
  "$ROOT/.local/adopts/NL2AGBench" \
  "$ROOT/raw-sources/repos/InstructionArbitrationBench" \
  "$ROOT/raw-sources/repos/NL2AGBench"
do
  test ! -e "$bad" || { echo "FAIL forbidden clone exists: $bad"; exit 1; }
done

# 3. K314–K315 wired into Phase-1 rules.
grep -q "K314 Recognition" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K315 Security-agent SLR" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K314 Recognition" "$ROOT/.cursor/rules/cemini-cybersec-mcp-tool-control.mdc"
grep -q "K314 Recognition" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K314 Recognition" "$ROOT/.cursor/rules/cemini-cybersec-k-dual-id.mdc"

# 4. Dual-ID restore check.
python3 "$ROOT/scripts/restore_cybersec_dual_id.py" --check

# 5. Index slugs present.
for slug in \
  arxiv-2608-28502-recognition-without-enforcement \
  recognition-enforcement-gap-instruction-arbitration \
  arxiv-2608-28490-llm-security-agents-survey \
  security-agent-authority-auditability-slr \
  arxiv-2608-28481-ood-nl2agbench
do
  grep -q "$slug" "$ROOT/wiki/index.md" || { echo "FAIL index missing slug: $slug"; exit 1; }
done

echo "ALL PASS K314-K315 Phase-0"
