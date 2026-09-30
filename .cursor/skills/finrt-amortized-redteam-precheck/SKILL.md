---
name: finrt-amortized-redteam-precheck
description: >-
  K382 FinRT amortized adversarial-generator red-team checklist. Score coverage,
  severity, realism, and diversity jointly. No high-severity prompts in wiki.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
federation: true
disable-model-invocation: true
---

# FinRT Precheck (K382)

From **Cybersecurity Wiki** WorkDir:

```bash
python3 scripts/k382_finrt_amortized_redteam_precheck.py checklist
python3 scripts/k382_finrt_amortized_redteam_precheck.py selftest
```

Canon: `@cybersecurity-wiki/concepts/finrt-amortized-redteam-generator.md` (arXiv **2609.36474**).

Separate red-team search from generation; amortize into a reusable generator; report the offline cost.

## NEVER

- No high-severity prompts, target adapters, or attack recipes in wiki.
- No repo at hunt (authors withhold prompts and adapters) — REFERENCE.
- Owned or procured models only; no LIVE third-party targets.

## Related

- `@cybersecurity-wiki/concepts/experience-driven-redteam-skill-evolution.md`
- `@cybersecurity-wiki/concepts/ai-redteam-evidential-ceiling.md`
