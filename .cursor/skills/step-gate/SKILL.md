---
name: step-gate
description: >-
  Classify a candidate step as proceed / hold / escalate before a high-blast
  action (StepGuard-style step gate, K312). Use when the operator says step-gate
  / gate this / is this safe / check before you run. Operator-invoked only;
  NOT a Claude Code PreToolUse hook.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
disable-model-invocation: true
federation: true
---

# Step gate — proceed / hold / escalate (K312)

Canon: CCC `@concepts/step-level-tool-guardrails.md` (arXiv **2608.24777**, K312). Helper: CCC `scripts/step_gate.py`. **HITL:** operator-invoked before high-blast steps; not a hook install; do not auto-evolve this skill.

## Procedure

1. State the candidate `(tool, args_summary)`.
2. Run `python3 scripts/step_gate.py check <tool> <args...>`.
3. Act on the verdict:

| Verdict | Meaning | Action |
|---------|---------|--------|
| `HOLD` | Closed high-blast list | Do **not** proceed without explicit operator OK (LIVE Discord, scp to cemini-prod, watches.json, `.cursor/skills` mutation, secrets, `git push --force`) |
| `PROCEED` | Low-blast allowlist | Safe routine action (wiki read, `wiki_lint`, `git status`, local lint) |
| `ESCALATE` | Unknown high-blast / ambiguous | Ask the operator before acting |

Pairs K239 preview-before-effect and `aid-guard-commit` (admission ≠ effect).

## Selftest

`python3 scripts/step_gate.py selftest` — 8 closed cases must classify correctly.

## NEVER

- Do not treat this as a Claude Code `PreToolUse` hook — it is operator-invoked.
- Do not auto-proceed on HOLD. Do not silent-default an ESCALATE.
- No pipe-to-shell install patterns (`curl` piped to `bash`). No network calls. No secrets in args echoes.
- Do not rewrite `## Verify`. Do not rewrite `route-task.ps1`. Do not edit `~/.claude/settings.json`.
