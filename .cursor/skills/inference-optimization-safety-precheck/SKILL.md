---
name: inference-optimization-safety-precheck
description: >-
  K405 checklist before adding an inference optimisation. A draft model enters
  the token path and the TCB. Re-run the safety eval, not just the quality eval.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
federation: true
federation_owner: cybersecurity-wiki
disable-model-invocation: true
---

# Inference-Optimisation Safety Precheck (K405)

From **Cybersecurity wiki** WorkDir:

```bash
python3 scripts/k405_inference_optimization_safety_precheck.py checklist
python3 scripts/k405_inference_optimization_safety_precheck.py selftest
```

Canon: `@cybersecurity-wiki/concepts/speculative-decoding-safety-asymmetry.md` (arXiv **2610.08678**).

Speculative decoding lets a small draft model write tokens a large target model verifies. The check is
tuned for distributional agreement, not safety — so a weak draft raised jailbreak and prompt-injection
ASR while utility barely moved. **The cost of the weakness does not appear on a utility benchmark.**

## NEVER

- No jailbreak payloads, decoding exploits, or attack code in wiki.
- Do not ship an optimisation that adds a model to the token path without re-running the safety eval.
- Owned or procured models only.
