---
name: aid-guard-commit
description: >-
  Revalidate the exact approved request at commit (AID-Guard). Use before MCP
  writes (GitHub create_or_update_file, stash) or when the user says AID-Guard
  / commit-revalidation / one reservation. Preview/HITL still required.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
disable-model-invocation: true
federation: true
---

# AID-Guard commit — admission ≠ effect

Canon: CCC `@wiki/concepts/authorization-to-effect-closure.md` (arXiv **2608.21159**, K302). Helper: CCC `scripts/aid_guard_commit.py`. **HITL:** operator-invoked; do not auto-evolve this skill.

Admission approval is not authority to produce a provider effect. Between preview and write the args can mutate, the response can be lost, or a retry can double-apply.

## Low-risk allowlist (this prototype)

| Tool id | When |
|---------|------|
| `local.hot_md` | Session cache rewrite (gitignored, reversible) — **default demo path** |
| `github.create_or_update_file` | GitHub MCP file write — still needs operator preview (K239) |
| `stash.write` | Stash MCP write — still needs operator preview |

LIVE Discord, trading egress, prod `scp`, and `watches.json` stay on the existing K239 gate. This skill does **not** auto-LIVE.

## Procedure (this turn)

1. Preview the write. Do not silent-default required fields (K259).
2. `reserve` the canonical `{tool, args}`:

```bash
python3 scripts/aid_guard_commit.py reserve --id <slug> --tool local.hot_md --args-json '{"path":"hot.md","body_sha256":"<sha>"}'
```

3. At the actual tool call, `commit` the **same** bytes. A mutated request is unauthorized.
4. If the outcome is unknown: `ambiguous` — hold; do not retry; do not mint a successor.
5. After observe: `release --outcome …` or `certify-no-effect` then at most **one** `successor`.

Self-test: `python3 scripts/aid_guard_commit.py selftest`

## NEVER

- Do not blind-retry a write whose result is unknown.
- Do not treat preview as proven user intent — it only bounds the request.
- No secrets in reservation JSON. Store is `.local/aid-guard/` (gitignored).
- Do not rewrite `## Verify` to match a failing commit.
