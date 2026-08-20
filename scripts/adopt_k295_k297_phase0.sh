#!/usr/bin/env bash
# Phase-0 verify — K295 Fool's Gold (REFERENCE no clone) + K296 TWR (REFERENCE) + K297 AUTOSIGMA (REFERENCE)
# + OOD DiSCO/self-prompting + inbound BloodBash/bbot Extract pointers + rule-blindness Watch + CCC K290 excess-authority
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
for f in \
  wiki/sources/arxiv-2608-17202-fools-gold-defensive-deception.md \
  wiki/concepts/decoy-hardening-open-weight-abliteration.md \
  wiki/sources/arxiv-2608-17361-trusted-workflow-relays.md \
  wiki/concepts/trusted-workflow-relay-email-abuse.md \
  wiki/sources/arxiv-2608-19011-ti-to-detection-rule-grounding.md \
  wiki/concepts/knowledge-driven-detection-rule-grounding.md \
  wiki/sources/arxiv-2608-17067-ood-disco-t2i-defense.md \
  wiki/sources/arxiv-2608-19025-ood-self-prompting-literature-extraction.md \
  wiki/entities/tools/bloodbash.md \
  wiki/entities/tools/bbot.md \
  wiki/sources/arxiv-2608-16852-rule-blindness-compliance-detectors.md \
  wiki/concepts/compliance-detector-rule-blindness.md \
  wiki/sources/arxiv-2608-18351-excess-authority-least-privilege.md \
  wiki/concepts/task-conditioned-excess-authority.md
do
  test -f "$ROOT/$f"
done

# Forbidden clones must NOT exist in this wiki
for bad in \
  "$ROOT/.local/adopts/H.I.V.E" \
  "$ROOT/.local/adopts/Hive" \
  "$ROOT/.local/adopts/WireTapper" \
  "$ROOT/.local/adopts/PrivFu" \
  "$ROOT/raw-sources/repos/PrivFu" \
  "$ROOT/.local/adopts/QUIC-C2" \
  "$ROOT/.local/adopts/pwneye" \
  "$ROOT/.local/adopts/FoolGold" \
  "$ROOT/.local/adopts/fools-gold" \
  "$ROOT/.local/adopts/JailbreakSkill" \
  "$ROOT/.local/adopts/bbot" \
  "$ROOT/.local/adopts/BloodBash" \
  "$ROOT/.local/adopts/AUTOSIGMA" \
  "$ROOT/.local/adopts/DiSCO"
do
  test ! -e "$bad"
done

# OSINT shelf pointers (REFERENCE; not re-cloned here)
OSINT_BB="/Users/claudiobarone/Projects/OSINT WORKSPACE/.local/adopts/BloodBash"
OSINT_BBOT="/Users/claudiobarone/Projects/OSINT WORKSPACE/.local/adopts/bbot"
test -d "$OSINT_BB"
test -f "$OSINT_BB/LICENSE"
grep -q "MIT License" "$OSINT_BB/LICENSE"
bb_size="$(du -sm "$OSINT_BB" | cut -f1)"
test "$bb_size" -lt 500
test -d "$OSINT_BBOT"
test -f "$OSINT_BBOT/LICENSE"
grep -q "AFFERO GENERAL PUBLIC LICENSE" "$OSINT_BBOT/LICENSE"
bbot_size="$(du -sm "$OSINT_BBOT" | cut -f1)"
test "$bbot_size" -lt 500

# Any GO under cyber .local/adopts must stay under 500MB + have LICENSE
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

# Wires
grep -q "K295 Fool's Gold" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K296 Trusted Workflow Relays" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "CCC K290 excess-authority" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "Rule-blindness 2608.16852" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K290 CHIVE" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K295 Fool's Gold" "$ROOT/.cursor/rules/cemini-phase1-policy-wires.mdc"
grep -q "K290 CHIVE (2608.16747)" "$ROOT/.cursor/rules/cemini-phase1-policy-wires.mdc"
# CCC K290–K294 still present
grep -q "CCC wave K290–K294" "$ROOT/.cursor/rules/cemini-phase1-policy-wires.mdc"
grep -q "Task-conditioned least-privilege learning (K290)" "$ROOT/.cursor/rules/cemini-phase1-policy-wires.mdc"
grep -q "SPADE self-play executable environments (K294)" "$ROOT/.cursor/rules/cemini-phase1-policy-wires.mdc"

# Index
grep -q "decoy-hardening-open-weight-abliteration" "$ROOT/wiki/index.md"
grep -q "trusted-workflow-relay-email-abuse" "$ROOT/wiki/index.md"
grep -q "knowledge-driven-detection-rule-grounding" "$ROOT/wiki/index.md"
grep -q "entities/tools/bloodbash.md" "$ROOT/wiki/index.md"
grep -q "entities/tools/bbot.md" "$ROOT/wiki/index.md"

echo "ALL PASS K295/K296/K297 REFERENCE (no forbidden clones; BloodBash OSINT ${bb_size}MB MIT; bbot OSINT ${bbot_size}MB AGPL; dual-ID restored; CCC K290–K294 intact)"
