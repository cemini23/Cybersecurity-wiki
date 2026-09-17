---
name: eval-first-rubric
description: >-
  Eval-first rubric before Integrate or WIRE — SPDX check, held-out harness eval,
  claim+locator. Use when triaging eval docx, tool URLs, or before marking something
  WIRE. Pairs harness-eval-gate; does not auto-evolve skills.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
disable-model-invocation: true
federation: true
---

# Eval-first rubric

Canon: `@wiki/entities/tools/llm-as-a-verifier.md` · `@wiki/concepts/file-keep-wire-harness.md`. Harness gate: `harness-eval-gate` skill.

## Procedure

1. **License:** `gh api repos/{owner}/{repo} --jq .license.spdx_id` — never trust eval docx SPDX alone.
2. **Verb:** FILE (wiki only) · KEEP (clone to `.local/adopts/`) · WIRE (executable + ledger row).
3. **Harness changes:** run `python3 scripts/harness_eval_checklist.py checklist` before SHIP.
4. **Claims:** durable artifacts need claim + source locator or `NO_EVIDENCE`.

## NEVER

- No Integrate GO without verified SPDX.
- No `curl | sh`. No HF weight downloads by default.
- Do not rewrite pass criteria mid-run.
