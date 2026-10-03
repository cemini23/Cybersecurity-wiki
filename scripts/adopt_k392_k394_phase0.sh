#!/usr/bin/env bash
# Phase-0 verify — K392-K394 (2026-10-03).
# K392/K393: protocol design papers, no public artifact -> REFERENCE, no clone.
# K394: OOD (computational art) -> stub only, routed to image-gen.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

for f in \
  wiki/sources/arxiv-2609-31519-wpa3-sae-asymmetric-pe-tickets.md \
  wiki/concepts/wpa3-sae-dos-cost-asymmetry.md \
  wiki/sources/arxiv-2610-01580-pld-eap-teap-wifi-authentication.md \
  wiki/concepts/physical-layer-deception-enterprise-wifi-auth.md \
  wiki/sources/arxiv-2610-02045-form-and-void-agent-ood.md
do
  test -f "$ROOT/$f" || { echo "FAIL missing page: $f"; exit 1; }
done

# No wireless-lab clones this batch.
for bad in \
  "$ROOT/.local/adopts/PLD-WiFi" \
  "$ROOT/.local/adopts/hostap-pld" \
  "$ROOT/raw-sources/repos/hostap-pld"
do
  test ! -e "$bad" || { echo "FAIL clone present for a REFERENCE-only paper: $bad"; exit 1; }
done

grep -q "K392 WPA3" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K393 PLD" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K392" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K394 Form and Void" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K392" "$ROOT/.cursor/rules/cemini-cybersec-k-dual-id.mdc"
grep -q "K394" "$ROOT/.cursor/rules/cemini-cybersec-k-dual-id.mdc"
grep -q "K300–K3" "$ROOT/.cursor/rules/cemini-cybersec-k-dual-id.mdc"
grep -q "K392" "$ROOT/.cursor/rules/overlays/cybersec-k-dual-id.fragment.mdc"
grep -q "K300–K3" "$ROOT/.cursor/rules/overlays/cybersec-k-dual-id.fragment.mdc"

python3 "$ROOT/scripts/restore_cybersec_dual_id.py" --check
python3 "$ROOT/scripts/k392_wpa3_sae_dos_precheck.py" selftest
test -f "$ROOT/.cursor/skills/wpa3-sae-dos-precheck/SKILL.md"

echo "ALL PASS K392-K394 Phase-0"
