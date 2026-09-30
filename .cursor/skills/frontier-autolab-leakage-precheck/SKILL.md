---
name: frontier-autolab-leakage-precheck
description: >-
  K384 Frontier Autolab temporal-leakage checklist. Report hindsight and
  briefing-selection leakage; briefer != scorer; totals in code.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
federation: true
disable-model-invocation: true
---

# Frontier Autolab Precheck (K384)

From **Cybersecurity Wiki** WorkDir:

```bash
python3 scripts/k384_frontier_autolab_leakage_precheck.py checklist
python3 scripts/k384_frontier_autolab_leakage_precheck.py selftest
```

Canon: `@cybersecurity-wiki/concepts/frontier-autolab-organizational-memory-leakage.md` (arXiv **2609.36739**).

Long-horizon multi-agent evals sit on temporal leakage. The judge's hindsight subscore fell while totals
rose (within-run r = −0.58). Fix the rubric's treatment of **caution** in advance.

## NEVER

- No briefing bodies, judge prompts, or leakage recipes in wiki.
- Simulated / owned harness only — no live market or real-firm targets.
- Do not treat runs as independent replications.

## Related

- `@cybersecurity-wiki/concepts/trajectory-context-control.md`
- `@cybersecurity-wiki/concepts/salami-collusive-memory-poisoning.md`
