---
name: prime-agent-sandbox
description: >-
  Isolated Prime Agent REFERENCE trial (inventory + K292 retention). Use when
  the user says Prime Agent sandbox / RLM trial. Do not replace Cursor, /route,
  or claude-ds. Do not run the upstream installer.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.1"
disable-model-invocation: true
federation: true
---

# Prime Agent sandbox — trial, do not swap the harness

Canon: CCC `@wiki/concepts/rlm-continual-harness.md` (arXiv **2608.23552**, K309). Clone: CCC `.local/adopts/prime-agent` (MIT REFERENCE). Script: `scripts/prime_agent_sandbox_trial.sh`. **HITL:** operator-invoked.

Prime Agent is an RLM REPL + Continual Harness. Runtime stays **`wont_wire`** on Cemini: Cursor / `/route` / claude-ds are not replaced. A trial is an **inventory + retention check**, not a PATH install.

## When

| Do | Do not |
|----|--------|
| Run the CCC trial script in the CCC repo | Run the clone's installer |
| Read the clone README / AGENTS.md | Put the binary on PATH as `/route` |
| Compare harness file hashes before/after (K292) | Change skills or prompts without HITL |
| Leave learned harness state unused | Auto-edit `.cursor/skills` |

## Procedure

From CCC WorkDir:

```bash
bash scripts/prime_agent_sandbox_trial.sh
```

The eval pack is **harness-inventory** (LICENSE, size under 500MB, RLM + Continual Harness strings, AGENTS.md / SECURITY.md) plus a **K292 retention** re-hash of `.cursor/skills` and `.cursor/rules`. It does not run ARC-AGI-3 and does not start the agent.

Other workspaces: skip the clone smoke; keep the no-swap rule.

## NEVER

- Do not run the upstream installer from the clone.
- Do not copy clone session state into Cemini without HITL + held-out retention (K292 / K162).
- Do not score harness failures as model failures — that is the paper’s measurement claim, not a reason to swap `/route`.
