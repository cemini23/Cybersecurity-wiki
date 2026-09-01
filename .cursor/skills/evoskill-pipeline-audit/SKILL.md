---
name: evoskill-pipeline-audit
description: >-
  K317 advisory checklist before red-teaming autonomous skill generation/evolution
  (EvoSkill Injection). Use when operator says EvoSkill / SARGE / skill pipeline
  attack / K317 precheck. Pairs skill-misevolution governance.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
disable-model-invocation: true
federation: true
---

# EvoSkill pipeline audit — K317 advisory checklist

Canon: `@wiki/concepts/evoskill-injection-self-evolving-agents.md` (arXiv **2608.30429**). Helper: `scripts/k317_evoskill_pipeline_precheck.py`. **Authorized lab only.**

## Procedure

From **Cybersecurity wiki** WorkDir:

```bash
python3 scripts/k317_evoskill_pipeline_precheck.py checklist
python3 scripts/k317_evoskill_pipeline_precheck.py selftest
bash scripts/k316_k319_inventory.sh   # EvoSkillBench SPDX re-hunt
```

Measure **stored → retrieved → activated** persistence. Pair `@wiki/concepts/skill-misevolution.md`.

## NEVER

- Do not copy evolved/malicious skills into `.cursor/skills`.
- No malicious trajectory bodies in wiki or briefs.
- HITL on skill write does **not** cover retrieval-time harm alone.
