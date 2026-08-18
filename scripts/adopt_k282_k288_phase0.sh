#!/usr/bin/env bash
# Phase-0 verify — K282 ARENA-audio (REFERENCE) + K283 JailbreakSkill (NO-GO clone) + K288 ESTI (REFERENCE)
# + K290 CHIVE (GO REFERENCE clone) + K240 Tripwire (Watch) + inbound SVP/RA-Bench/DFI stubs
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
for f in \
  wiki/sources/arxiv-2608-15578-arena-audio-lalm-redteam.md \
  wiki/concepts/audio-grounded-lalm-redteaming.md \
  wiki/entities/tools/arena-audio-redteam.md \
  wiki/sources/arxiv-2608-16465-jailbreakskill.md \
  wiki/concepts/evolving-attack-skill-libraries.md \
  wiki/entities/tools/jailbreakskill.md \
  wiki/sources/arxiv-2608-16806-esti-state-semantic-injection.md \
  wiki/concepts/planner-state-integrity-embodied-agents.md \
  wiki/entities/tools/esti-bench.md \
  wiki/sources/arxiv-2608-16747-chive-counterfactual-explanations.md \
  wiki/concepts/counterfactual-simulatability-llm-explanations.md \
  wiki/entities/tools/chive.md \
  wiki/sources/arxiv-2608-16795-ood-historical-backtesting-astronomy.md \
  wiki/sources/arxiv-2608-14392-tripwire-safety-neuron-clamp.md \
  wiki/concepts/tripwire-safety-neuron-clamp.md \
  wiki/sources/arxiv-2608-14529-deterministic-gapsvp-hardness.md \
  wiki/concepts/lattice-pqc-hardness-watch.md \
  wiki/sources/arxiv-2608-14391-ood-ra-bench-crisis-video.md \
  wiki/concepts/differential-fault-injection-llm-code-stub.md
do
  test -f "$ROOT/$f"
done
# CHIVE GO REFERENCE
test -d "$ROOT/.local/adopts/chive"
test -f "$ROOT/.local/adopts/chive/LICENSE"
grep -q "MIT License" "$ROOT/.local/adopts/chive/LICENSE"
du_size="$(du -sm "$ROOT/.local/adopts/chive" | cut -f1)"
test "$du_size" -lt 500
# JailbreakSkill must NOT be cloned
test ! -d "$ROOT/raw-sources/repos/JailbreakSkill" -a ! -d "$ROOT/.local/adopts/JailbreakSkill"
# Wires
grep -q "K282 ARENA" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K283 JailbreakSkill" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K288 ESTI" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K288 ESTI" "$ROOT/.cursor/rules/cemini-cybersec-mcp-tool-control.mdc"
grep -q "K290 CHIVE" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K240 Tripwire" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K282 ARENA-audio" "$ROOT/.cursor/rules/cemini-phase1-policy-wires.mdc"
# Index
grep -q "audio-grounded-lalm-redteaming" "$ROOT/wiki/index.md"
grep -q "evolving-attack-skill-libraries" "$ROOT/wiki/index.md"
grep -q "planner-state-integrity-embodied-agents" "$ROOT/wiki/index.md"
grep -q "counterfactual-simulatability-llm-explanations" "$ROOT/wiki/index.md"
echo "ALL PASS K282/K283/K288/K290 (ARENA+ESTI REFERENCE; JailbreakSkill NO clone; CHIVE GO ${du_size}MB; Tripwire Watch; wires lab-redteam+audit+mcp-tool-control)"
