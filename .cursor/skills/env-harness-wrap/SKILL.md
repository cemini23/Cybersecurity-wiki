---
name: env-harness-wrap
description: >-
  Wrap an existing task environment or eval; keep the original verifier. Use
  when adapting a harness, adding a lane/tool, or when the user says EnvHarness
  / wrap don't rebuild. Do not synthesize EnvRigger plug-ins or rewrite pass
  criteria.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
disable-model-invocation: true
federation: true
---

# EnvHarness wrap — keep the verifier

Canon: CCC `@wiki/sources/arxiv-k244-harness-skill-selection-cluster.md` (arXiv **2608.19880**). EnvHarness is a plug-in layer around a **static** env so behavior can change without rewriting the env’s logic. **Every reshaped env keeps the original verifier.** EnvRigger (auto-synthesize plug-ins from trajectories) is **WATCH only** — no unattended harness mutation.

## Cemini mapping

| Keep (verifier / contract) | Wrap (adapter) | Do not rebuild |
|----------------------------|----------------|----------------|
| `wiki_lint.py`, OpenSpec AC, route `## Verify`, tests, prod observe | New executor lane, MCP, skill, clone behind the same gate | New scoring rubric that matches a failing agent |
| Thinkingbox-style terminal-state checks | Isolated session / extra trace | Pass@1 as “done” |

Paper reported up to +9.0 held-out and 9.8% fewer steps vs rebuilding envs — by **keeping the scorer** and changing only the wrap.

## Procedure

1. Name the **existing verifier** before changing the env or tool loop.
2. Add adapters (prompts, wrappers, extra logs) that still fail/pass on that verifier.
3. If the verifier is wrong, **HITL** to change it — do not silently rewrite `## Verify` or lint rules to match the agent (pairs K162 / K281 / K298).
4. Do not run EnvRigger-style “diagnose flaws → synthesize plug-ins → redeploy” on prod Cursor/Claude skills.

## NEVER

- Do not install EnvHarness/EnvRigger trainers or clone without SPDX + Phase-0.
- Do not skip Image-gen / 3D local wires as a “new env.”
- No closed self-eval loop.
