#!/usr/bin/env bash
# Phase-0 verify — K323 CodePoisonRAG / K324 SafeEvolve / K325 illegibility / K326 WiFi RF.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

for f in \
  wiki/sources/arxiv-2609-02774-codepoisonrag-knowledge-poisoning.md \
  wiki/concepts/codepoisonrag-racg-knowledge-poisoning.md \
  wiki/sources/arxiv-2609-02786-safeevolve-harness-policy-co-evolution.md \
  wiki/concepts/safeevolve-harness-policy-co-evolution.md \
  wiki/sources/arxiv-2609-02852-linguistic-illegibility-llm-security.md \
  wiki/concepts/linguistic-illegibility-llm-security.md \
  wiki/sources/arxiv-2609-02007-c2t-openmax-wifi-rf-fingerprinting.md \
  wiki/concepts/wifi-rf-fingerprinting-open-set.md
do
  test -f "$ROOT/$f" || { echo "FAIL missing page: $f"; exit 1; }
done

grep -q "K323 CodePoisonRAG" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K324 SafeEvolve" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K325 Linguistic illegibility" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K326 C²T-OpenMax" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K323 CodePoisonRAG" "$ROOT/.cursor/rules/cemini-cybersec-k-dual-id.mdc"

python3 "$ROOT/scripts/restore_cybersec_dual_id.py" --check

for slug in \
  arxiv-2609-02774-codepoisonrag-knowledge-poisoning \
  codepoisonrag-racg-knowledge-poisoning \
  arxiv-2609-02786-safeevolve-harness-policy-co-evolution \
  safeevolve-harness-policy-co-evolution \
  arxiv-2609-02852-linguistic-illegibility-llm-security \
  linguistic-illegibility-llm-security \
  arxiv-2609-02007-c2t-openmax-wifi-rf-fingerprinting \
  wifi-rf-fingerprinting-open-set
do
  grep -q "$slug" "$ROOT/wiki/index.md" || { echo "FAIL index missing slug: $slug"; exit 1; }
done

python3 "$ROOT/scripts/test_k323_codepoisonrag_precheck.py" >/dev/null
python3 "$ROOT/scripts/test_k324_safeevolve_precheck.py" >/dev/null

echo "ALL PASS K323-K326 Phase-0"
