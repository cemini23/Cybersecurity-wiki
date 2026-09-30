---
name: progressive-skill-access-precheck
description: >-
  K390 staged skill/tool disclosure precheck. Validate JSON plan forbids flat catalog dump and caps tools per stage.
  Use when operator says progressive skill access / staged disclosure / skill access control.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
disable-model-invocation: true
federation: true
---

# Progressive skill access precheck (K390)

Helper: `scripts/progressive_skill_access_precheck.py`. Canon: `@wiki/concepts/progressive-skill-discovery-access-control.md`.

```bash
python3 scripts/progressive_skill_access_precheck.py checklist
python3 scripts/progressive_skill_access_precheck.py json --json config/progressive_skill_access.example.json
python3 scripts/progressive_skill_access_precheck.py selftest
```

## NEVER

- No auto-evolve skills tree. Pair scout-tool-search for lazy load.
