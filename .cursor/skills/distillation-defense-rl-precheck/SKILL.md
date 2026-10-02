---
name: distillation-defense-rl-precheck
description: >-
  K381 distillation-defense vs post-distill RL checklist. Dual pre/post-RL
  metrics on owned or procured models. No distill attack recipes in wiki.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
federation: true
federation_owner: cybersecurity-wiki
disable-model-invocation: true
---

# Distillation Defense RL Precheck (K381)

From **Cybersecurity wiki** WorkDir:

```bash
python3 scripts/k381_distillation_defense_rl_precheck.py checklist
python3 scripts/k381_distillation_defense_rl_precheck.py selftest
```

Canon: `@cybersecurity-wiki/concepts/distillation-defense-reinforcement-learning-threat-model.md` (arXiv **2609.35699**).

Threat model must include attacker RL after distillation; report dual metrics.

## NEVER

- No distillation attack recipes or stolen traces in wiki.
- No eval on models outside owned or procured scope.
