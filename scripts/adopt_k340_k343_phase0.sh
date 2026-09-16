#!/usr/bin/env bash
# Phase-0 verify — K340–K343 batch + OOD stub (2026-09-16 ingest).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

for f in \
  wiki/sources/arxiv-2609-16541-cyber-range-incident-response-agents.md \
  wiki/concepts/cyber-range-autonomous-incident-response-agents.md \
  wiki/sources/arxiv-2609-16694-secure-ai-pentest-agents.md \
  wiki/concepts/secure-ai-powered-pentest-agents.md \
  wiki/sources/arxiv-2609-16777-multi-conversation-persuasion-robustness.md \
  wiki/concepts/multi-conversation-persuasion-factual-robustness.md \
  wiki/sources/arxiv-2609-17516-chain-of-self-questioning-abstention.md \
  wiki/concepts/chain-of-self-questioning-selective-abstention.md
do
  test -f "$ROOT/$f" || { echo "FAIL missing page: $f"; exit 1; }
done

grep -q "K340 Cyber-range" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K341 Secure AI-powered pentest" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K340 Cyber-range" "$ROOT/.cursor/rules/cemini-cybersec-k-dual-id.mdc"

python3 "$ROOT/scripts/restore_cybersec_dual_id.py" --check
python3 "$ROOT/scripts/test_k341_secure_pentest_agent_precheck.py" >/dev/null

echo "ALL PASS K340-K343 Phase-0"
