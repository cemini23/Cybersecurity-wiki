---
name: ocp-claim-check
description: >-
  K371 overclaiming propensity (OCP) check — compare agent done-claims to
  on-disk evidence locators and verify_ran. Use when reviewing completion
  reports or before marking a task success. Pairs claim-ledger locator habit.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
disable-model-invocation: true
federation: true
---

# OCP claim check (K371)

Canon: `@wiki/concepts/overclaiming-propensity-agent-measurement.md` (arXiv **2609.20812**). Helper: `scripts/ocp_claim_check.py`. Status labels ≠ endpoints (K277).

## Procedure

JSON input keys: `claim_text`, `claimed_status` (`done` | `partial` | `blocked`), `evidence_paths`, `verify_ran` (bool).

```bash
python3 scripts/ocp_claim_check.py json --json claim.json
python3 scripts/ocp_claim_check.py selftest
```

| Verdict | When |
|---------|------|
| `OVERCLAIM` | `done` without `verify_ran`, or missing evidence path |
| `DRIFT_SEMANTIC` | Claim keywords do not match evidence (K122) |
| `DRIFT_EXPERIMENTAL` | Evidence outside claimed scope |
| `DRIFT_MECHANISTIC` | Success without component locator (pairs K370) |
| `OK` | Status matches locators |

Pairs: `claim-ledger`, `agent-queue-labels`, K325 bounded eval.

## NEVER

- Do not write `watches.json`, Discord, wiki, or git from this helper.
- Do not treat model refusal as authorization.
- No LIVE Discord without LIVE OK.
