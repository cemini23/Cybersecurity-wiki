---
name: skill-cascading-precheck
description: >-
  K374 skill cascading / joint-skill suite audit checklist. Audit suites as one
  unit; watch shared-context writes. No cascade recipes in wiki.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
federation: true
federation_owner: cybersecurity-wiki
disable-model-invocation: true
---

# Skill Cascading Precheck (K374)

From **Cybersecurity wiki** WorkDir:

```bash
python3 scripts/k374_skill_cascading_precheck.py checklist
python3 scripts/k374_skill_cascading_precheck.py selftest
```

Canon: `@cybersecurity-wiki/concepts/skill-cascading-attacks-skill-based-agents.md` (arXiv **2609.30383**).

Per-skill SAFE is not enough. Cascades split harm across two or more skills. Audit co-installed
suites as one unit, and audit what each skill writes into the shared context window.

## NEVER

- No cascade recipes, modified skills, or attack payloads in wiki.
- Never auto-evolve skills from red-team runs.
- No LIVE third-party eval without written scope.
