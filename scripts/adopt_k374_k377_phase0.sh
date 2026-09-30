#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
for f in \
  wiki/sources/arxiv-2609-30383-skill-cascading-attacks-skill-based-agents.md \
  wiki/concepts/skill-cascading-attacks-skill-based-agents.md \
  wiki/sources/arxiv-2609-31318-agentxploit-repository-runtime-red-teaming.md \
  wiki/concepts/agentxploit-repository-runtime-red-teaming.md \
  wiki/sources/arxiv-2609-31552-fragtoken-inference-cost-amplification.md \
  wiki/concepts/fragtoken-inference-cost-amplification-lab.md \
  wiki/sources/arxiv-2609-31575-configuration-not-conscience-system-prompts.md \
  wiki/concepts/llm-system-prompt-corpus-audit.md \
  wiki/sources/arxiv-2609-31506-haitian-creole-cultural-awareness-ood.md
do
  test -f "$ROOT/$f"
done
grep -q "K374 Skill cascading" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K377 System-prompt operational configuration" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
python3 "$ROOT/scripts/restore_cybersec_dual_id.py" --check
python3 "$ROOT/scripts/k374_skill_cascading_precheck.py" selftest
python3 "$ROOT/scripts/k375_agentxploit_precheck.py" selftest
python3 "$ROOT/scripts/k376_fragtoken_precheck.py" selftest
python3 "$ROOT/scripts/k377_system_prompt_corpus_precheck.py" selftest
test -f "$ROOT/.cursor/skills/skill-cascading-precheck/SKILL.md"
echo ALL PASS K374-K377 Phase-0
