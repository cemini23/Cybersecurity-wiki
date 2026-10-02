---
name: fragtoken-precheck
description: >-
  K376 FragToken noncanonical-token cost-audit checklist. Do not train FragToken.
  Report TIR vs visible length. No fragmentation recipes in wiki.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
federation: true
federation_owner: cybersecurity-wiki
disable-model-invocation: true
---

# FragToken Precheck (K376)

From **Cybersecurity wiki** WorkDir:

```bash
python3 scripts/k376_fragtoken_precheck.py checklist
python3 scripts/k376_fragtoken_precheck.py selftest
```

Canon: `@cybersecurity-wiki/concepts/fragtoken-inference-cost-amplification-lab.md` (arXiv **2609.31552**).

Noncanonical tokens inflate decode cost without matching the visible length. Treat third-party and
fine-tuned models as a cost supply-chain surface. Report token count against visible response length
on owned or procured models only.

## NEVER

- No fragmentation recipes, token-split tables, or attack training code in wiki.
- Do not train or fine-tune a FragToken-style fragmentation model.
- No LIVE third-party eval without written scope.
