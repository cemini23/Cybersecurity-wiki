---
name: skill-cascade-precheck
description: >-
  K374 skill cascading / joint-skill suite audit checklist. No cascade recipes in wiki.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
federation: true
disable-model-invocation: true
---

# Skill Cascade Precheck (K374)

From **Cybersecurity wiki** WorkDir:

```bash
python3 scripts/k374_skill_cascade_precheck.py checklist
python3 scripts/k374_skill_cascade_precheck.py selftest
```

Canon: `@cybersecurity-wiki/concepts/skill-cascading-attacks-cross-skill.md` (arXiv **2609.30383**).

Treat co-installed skill suites as one unit; audit shared-context writes.

## NEVER

- No cascade recipes, modified skills, or attack payloads in wiki.
- No LIVE third-party eval without written scope.
