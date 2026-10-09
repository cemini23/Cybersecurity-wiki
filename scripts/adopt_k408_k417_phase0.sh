#!/usr/bin/env bash
# Phase-0 verify — K408-K417 (2026-10-09). All REFERENCE; no clones this batch.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

# Every source page this batch must exist.
for f in \
  wiki/sources/arxiv-2610-09240-adversarial-images-hijack-web-agents.md \
  wiki/sources/arxiv-2610-09892-defensive-sufficiency-stackelberg.md \
  wiki/sources/arxiv-2610-09906-constrained-action-ai-remediation-siem.md \
  wiki/sources/arxiv-2610-10455-phrbench-post-hallucination-reasoning.md \
  wiki/sources/arxiv-2610-10533-engramedit-conditional-memory-knowledge-updates.md \
  wiki/sources/arxiv-2610-11112-false-claims-credible-images.md \
  wiki/sources/arxiv-2610-12233-resi-recursive-safety-improvement.md \
  wiki/sources/arxiv-2610-12313-verdict-without-the-rule-compliance-invariance.md \
  wiki/sources/arxiv-2610-12361-cited-but-not-consulted-authority-swap-audit.md \
  wiki/sources/arxiv-2610-12415-orcagen-context-aware-malware-deception.md
do
  test -f "$f" || { echo "FAIL missing page: $f"; exit 1; }
done

# No doubled .md extensions anywhere (a repeat emit-script bug).
test -z "$(find wiki -name '*.md.md' -print -quit)" \
  || { echo "FAIL a page has a doubled .md extension"; exit 1; }

# No clone of any tool this batch; WebMirage / EpiReal are REFERENCE only.
for bad in \
  .local/adopts/WebMirage .local/adopts/EpiReal-Bench .local/adopts/ORCAGen \
  raw-sources/repos/WebMirage raw-sources/repos/EpiReal-Bench raw-sources/repos/ORCAGen
do
  test ! -e "$bad" || { echo "FAIL clone present for a REFERENCE-only paper: $bad"; exit 1; }
done

# Lane wires.
grep -q "K408 adversarial images" .cursor/rules/cemini-cybersec-lab-redteam.mdc
grep -q "K414 ReSI" .cursor/rules/cemini-cybersec-lab-redteam.mdc
grep -q "K415+K416 compliance verdicts" .cursor/rules/cemini-cybersec-agent-audit.mdc
grep -q "K413 verification-generation gap" .cursor/rules/cemini-cybersec-agent-audit.mdc

# Dual-ID.
grep -q "K408 Adversarial images" .cursor/rules/cemini-cybersec-k-dual-id.mdc
grep -q "K417 ORCAGen" .cursor/rules/cemini-cybersec-k-dual-id.mdc
grep -q "K300–K3" .cursor/rules/cemini-cybersec-k-dual-id.mdc
grep -q "K408 Adversarial images" .cursor/rules/overlays/cybersec-k-dual-id.fragment.mdc
grep -q "K300–K3" .cursor/rules/overlays/cybersec-k-dual-id.fragment.mdc

python3 scripts/restore_cybersec_dual_id.py --check
echo "ALL PASS K408-K417 Phase-0"
