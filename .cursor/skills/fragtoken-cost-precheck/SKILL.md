---
name: fragtoken-cost-precheck
description: >-
  K376 FragToken noncanonical token cost-audit checklist. Do not train FragToken. No fragmentation recipes in wiki.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
federation: true
disable-model-invocation: true
---

# Fragtoken Cost Precheck (K376)

From **Cybersecurity wiki** WorkDir:

```bash
python3 scripts/k376_fragtoken_cost_precheck.py checklist
python3 scripts/k376_fragtoken_cost_precheck.py selftest
```

Canon: `@cybersecurity-wiki/concepts/fragtoken-noncanonical-token-cost-audit.md` (arXiv **2609.31552**).

Report token count vs visible length on owned or procured models only.

## NEVER

- No fragmentation recipes, token-split tables, or attack training code in wiki.
- No LIVE third-party eval without written scope.
