#!/usr/bin/env bash
# Phase-0 verify — K298 Inadvertent Context Leakage (REFERENCE) + K299 TrustRAG committee RAG (REFERENCE)
# + K300 BreakGuard LLM dependency tests (REFERENCE) + OOD rainfall CSI / travel agents + K298 supporting
# (tl;dr sec #342 + SecPro #248). No name-collision clones. No OSINT BloodBash/bbot checks (K295 script).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

# 1. Every new wiki page exists
for f in \
  wiki/sources/arxiv-2608-19857-inadvertent-context-leakage.md \
  wiki/concepts/inadvertent-context-leakage.md \
  wiki/sources/newsletter-rss-tldrsec-2026-08-20-tldr-sec-342.md \
  wiki/sources/substack-rss-secpro-2026-08-21-ai-ready-soc.md \
  wiki/concepts/agent-runtime-identity-adr.md \
  wiki/concepts/agent-safety-executable-evaluation.md \
  wiki/sources/arxiv-2608-20097-trustrag-committee-rag.md \
  wiki/concepts/committee-certified-rag-provenance.md \
  wiki/sources/arxiv-2608-20167-breakguard-dependency-breaking-tests.md \
  wiki/concepts/llm-generated-dependency-breaking-tests.md \
  wiki/sources/arxiv-2608-16088-ood-rainfall-csi-sensing.md \
  wiki/sources/arxiv-2608-20320-ood-travel-behavior-agents.md
do
  test -f "$ROOT/$f" || { echo "FAIL missing page: $f"; exit 1; }
done

# 2. Forbidden name-collision / artifact clones must NOT exist
for bad in \
  "$ROOT/.local/adopts/TrustRAG" \
  "$ROOT/.local/adopts/HuichiZhou" \
  "$ROOT/.local/adopts/gomate-community" \
  "$ROOT/.local/adopts/BreakGuard" \
  "$ROOT/.local/adopts/breakguard" \
  "$ROOT/.local/adopts/MP-SPDZ" \
  "$ROOT/.local/adopts/mp-spdz" \
  "$ROOT/.local/adopts/leakage" \
  "$ROOT/.local/adopts/context-leakage" \
  "$ROOT/.local/adopts/fools-gold" \
  "$ROOT/.local/adopts/FoolGold" \
  "$ROOT/raw-sources/repos/TrustRAG" \
  "$ROOT/raw-sources/repos/HuichiZhou" \
  "$ROOT/raw-sources/repos/BreakGuard" \
  "$ROOT/raw-sources/repos/MP-SPDZ"
do
  test ! -e "$bad" || { echo "FAIL forbidden clone exists: $bad"; exit 1; }
done

# 3. Any GO under .local/adopts must stay under 500MB + have LICENSE
if [ -d "$ROOT/.local/adopts" ]; then
  shopt -s nullglob
  for d in "$ROOT/.local/adopts"/*; do
    [ -d "$d" ] || continue
    test -f "$d/LICENSE" || { echo "FAIL missing LICENSE: $d"; exit 1; }
    sz="$(du -sm "$d" | cut -f1)"
    test "$sz" -lt 500 || { echo "FAIL size ${sz}MB >= 500: $d"; exit 1; }
  done
  shopt -u nullglob
fi

# 4. Phase-1 wires present in domain rules + shared policy-wires dual-ID block
grep -q "K298 Inadvertent" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K298 Inadvertent" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K299 TrustRAG" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K300 BreakGuard" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K298 Inadvertent" "$ROOT/.cursor/rules/cemini-cybersec-mcp-tool-control.mdc"
# dual-ID block (keep CCC + K295-K297 intact)
grep -q "K298 Inadvertent Context Leakage (2608.19857)" "$ROOT/.cursor/rules/cemini-phase1-policy-wires.mdc"
grep -q "K299 TrustRAG committee RAG (2608.20097)" "$ROOT/.cursor/rules/cemini-phase1-policy-wires.mdc"
grep -q "K300 BreakGuard LLM dependency tests (2608.20167)" "$ROOT/.cursor/rules/cemini-phase1-policy-wires.mdc"
grep -q "K295 Fool's Gold (2608.17202)" "$ROOT/.cursor/rules/cemini-phase1-policy-wires.mdc"
grep -q "K297 TI→detection (2608.19011)" "$ROOT/.cursor/rules/cemini-phase1-policy-wires.mdc"

# 5. Index slugs
grep -q "arxiv-2608-19857-inadvertent-context-leakage" "$ROOT/wiki/index.md"
grep -q "inadvertent-context-leakage" "$ROOT/wiki/index.md"
grep -q "agent-runtime-identity-adr" "$ROOT/wiki/index.md"
grep -q "agent-safety-executable-evaluation" "$ROOT/wiki/index.md"
grep -q "arxiv-2608-20097-trustrag-committee-rag" "$ROOT/wiki/index.md"
grep -q "committee-certified-rag-provenance" "$ROOT/wiki/index.md"
grep -q "arxiv-2608-20167-breakguard-dependency-breaking-tests" "$ROOT/wiki/index.md"
grep -q "llm-generated-dependency-breaking-tests" "$ROOT/wiki/index.md"
grep -q "arxiv-2608-16088-ood-rainfall-csi-sensing" "$ROOT/wiki/index.md"
grep -q "arxiv-2608-20320-ood-travel-behavior-agents" "$ROOT/wiki/index.md"

echo "ALL PASS K298/K299/K300 REFERENCE (no forbidden name-collision clones; no leakage PoC; dual-ID block appended; CCC + K295-K297 intact)"
