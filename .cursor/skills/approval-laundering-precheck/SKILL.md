---
name: approval-laundering-precheck
description: >-
  K395 approval laundering precheck. Checklist and JSON gate for entry approval vs
  transitive workflow effects. Pairs K310/K302/K333. Operator-invoked only.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
disable-model-invocation: true
federation: true
---

# Approval laundering precheck (K395)

Canon: `@wiki/concepts/agent-approval-laundering-transitive-effects.md`. Helper: `scripts/approval_laundering_precheck.py`.

```bash
python3 scripts/approval_laundering_precheck.py checklist
python3 scripts/approval_laundering_precheck.py json --json config/approval_laundering_precheck.example.json
python3 scripts/approval_laundering_precheck.py selftest
```

| Verdict | Exit |
|---------|------|
| PASS | 0 |
| REVIEW | 2 |
| REJECT | 1 |

## NEVER

- No PoCs or exploit templates. Not a substitute for external broker products.
