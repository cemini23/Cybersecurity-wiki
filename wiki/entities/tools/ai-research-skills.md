---
title: Orchestra AI-Research-SKILLs — ML engineering skill library
type: entity
tags: [tool, skills, mlops, offensive-ml, k113]
keywords: [orchestra-research, peft, rlhf, llamaguard, skill-audit]
related:
  - concepts/seclaw-agent-security-evaluation.md
  - concepts/google-discovery-document-api-fuzzing.md
  - concepts/ai-for-cybersecurity.md
  - concepts/mcp-security-posture.md
  - entities/tools/nvidia-skillspector.md
  - entities/tools/seclaw-eval.md
  - sources/brief-k113-cybersec-ai-research-skills-2026-06-12.md
  - "@osint-wiki/entities/tools/ai-research-skills.md"
  - "@osint-wiki/sources/multi-wiki-tool-eval-v5-k113-2026-06-12.md"
maturity: draft
created: 2026-06-12
updated: 2026-07-31
phase_0_verdict: CONDITIONAL-GO 2026-06-12 — 98 SKILL.md inventory; cherry-pick only; skill_audit before harness
license_verified: MIT
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc"
---

## Relations

- @concepts/seclaw-agent-security-evaluation.md — trajectory eval harness; skills supply context under test
- @concepts/google-discovery-document-api-fuzzing.md — API-surface offensive lane (complements model/MLOps surface)
- @entities/tools/nvidia-skillspector.md — static skill supply-chain scan before install
- @osint-wiki/entities/tools/ai-research-skills.md — eval + laptop trial canonical

## Raw Concept

- **Repo:** `github.com/Orchestra-Research/AI-Research-SKILLs`
- **Tier:** Adopt → **CONDITIONAL-GO** (cybersec cherry-pick subset)
- **License:** MIT `[CONFIRMED]` 2026-06-12
- **Scale:** 98 `SKILL.md` files across 23 categories (repo README 2026-06-12)

## Narrative

Research-engineering skills for AI agents — **not** a security product. Cybersec value is **offensive ML literacy** and **MLOps abuse scenarios** for agent-eval and red-team coursework.

### Cherry-pick map (install subset only)

| Folder | Skills | Cybersec use |
|--------|--------|--------------|
| `07-safety-alignment/` | constitutional-ai, llamaguard, nemo-guardrails, prompt-guard | Alignment bypass, guardrail evasion study |
| `06-post-training/` | grpo-rl-training, trl-fine-tuning, verl, … | Reward hacking / RLHF pipeline review |
| `03-fine-tuning/` | peft, axolotl, llama-factory, unsloth | Adapter poisoning, LoRA tampering scenarios |
| `08-distributed-training/` | deepspeed, megatron-core, ray-train, … | Cluster misconfig, supply-chain training paths |
| `13-mlops/` + `17-observability/` | mlflow, wandb, langsmith, phoenix | Drift detection, compromised pipeline observability |

### Install discipline

```bash
# Verify current flags in repo README before running
npx @orchestra-research/ai-research-skills install --category safety-alignment --local
```

1. Run **SkillSpector** (or static review) on each `SKILL.md` before adding to agent harness
2. Run OSINT `scripts/skill_audit.py` on any skill staged for Cemini-adjacent workflows
3. **No prod** `/opt/cemini` install — laptop research + SeClaw eval context only

### Laptop trial (2026-06-12)

Clone inventory PASS (98 skills). Full npx install not run this session — category install is operator-gated.

## Sources

- @sources/brief-k113-cybersec-ai-research-skills-2026-06-12.md
- @osint-wiki/sources/multi-wiki-tool-eval-v5-k113-2026-06-12.md (URL 9)
