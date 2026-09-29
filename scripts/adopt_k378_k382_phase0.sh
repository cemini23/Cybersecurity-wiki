#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
for f in \
  wiki/sources/arxiv-2609-32400-skilldre-dual-stage-skill-red-team-evolution.md \
  wiki/concepts/skilldre-dual-stage-malicious-skill-evolution-lab.md \
  wiki/sources/arxiv-2609-33628-climbing-hill-curriculum-prompt-injection-redteam.md \
  wiki/concepts/curriculum-prompt-injection-redteam-frontier-models.md \
  wiki/sources/arxiv-2609-34920-rise-t2i-redteam-ood.md \
  wiki/sources/arxiv-2609-35663-late-attention-entity-token-copying.md \
  wiki/concepts/late-attention-entity-token-copying-interpretability.md \
  wiki/sources/arxiv-2609-35699-distillation-defenses-break-after-reinforcement-learning.md \
  wiki/concepts/distillation-defense-reinforcement-learning-threat-model.md
do
  test -f "$ROOT/$f"
done
grep -q "K378 SkillDRE" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K379 Climbing the hill" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K378 SkillDRE" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K379 Climbing the hill" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K380 Late-attention" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K381 Distillation defenses" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K378 SkillDRE" "$ROOT/.cursor/rules/cemini-cybersec-mcp-tool-control.mdc"
grep -q "K378 SkillDRE" "$ROOT/.cursor/rules/cemini-cybersec-k-dual-id.mdc"
grep -q "K381 Distillation" "$ROOT/.cursor/rules/cemini-cybersec-k-dual-id.mdc"
grep -q "K300–K381" "$ROOT/.cursor/rules/cemini-cybersec-k-dual-id.mdc"
grep -q "K378 SkillDRE" "$ROOT/.cursor/rules/overlays/cybersec-k-dual-id.fragment.mdc"
grep -q "K300–K381" "$ROOT/.cursor/rules/overlays/cybersec-k-dual-id.fragment.mdc"
python3 "$ROOT/scripts/restore_cybersec_dual_id.py" --check
python3 "$ROOT/scripts/k378_skilldre_precheck.py" selftest
python3 "$ROOT/scripts/k379_curriculum_pi_redteam_precheck.py" selftest
python3 "$ROOT/scripts/k381_distillation_defense_rl_precheck.py" selftest
test -f "$ROOT/.cursor/skills/skilldre-precheck/SKILL.md"
test -f "$ROOT/.cursor/skills/curriculum-pi-redteam-precheck/SKILL.md"
test -f "$ROOT/.cursor/skills/distillation-defense-rl-precheck/SKILL.md"
echo ALL PASS K378-K381 Phase-0
