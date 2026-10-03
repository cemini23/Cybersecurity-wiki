---
name: harness-eval-gate
description: >-
  K334 harness-as-eval-artifact gate before persisting a harness version.
  Use when evaluating Creation/Evolution harness changes, HarnessDev-style
  iterations, or when the user says harness eval gate / held-out harness /
  executor swap. Does not rewrite pass criteria or auto-evolve skills.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
disable-model-invocation: true
federation: true
---

# Harness eval gate (K334)

Canon: `@ccc-wiki/concepts/harness-as-eval-artifact.md` (arXiv **2609.01437**). Helper: `scripts/harness_eval_checklist.py`. Evaluate **runnable harness infrastructure**, not only terminal task output.

## Procedure

```bash
python3 scripts/harness_eval_checklist.py checklist
python3 scripts/harness_eval_checklist.py selftest
```

JSON keys: `hidden_held_out`, `executor_swap`, `state_fires`, `external_eval`, `no_skill_autowrite`, `trace_recheck`, `state_owned`, `limits_enforced`, `trajectory_scored` — all must be true for SHIP.

Pair with: K281/K292 external eval contract, K332 vague-goal self-evolution (judge vs base model), `env-harness-wrap` (keep the verifier).

## State and enforcement (K278)

The harness owns the state a run depends on. arXiv **2610.02036** measured it: when a deciding event was hidden, model accuracy was compatible with chance, and **one restoring sentence returned it to 40 of 40**. When a run fails with every step looking locally correct, look for missing or unowned state before blaming the model.

Visibility is not enforcement. The same paper gave a team a live count of its remaining budget; the team still overspent in **4 of 5** runs. Commit enforcement took it to **0 of 5**. A counter an agent can read is not a gate. Enforce at the point of action.

## Trajectory scoring (K279)

A passing final result does not certify the process. arXiv **2610.01833** measured it: of **175 runs that passed every final numerical check, 162 (92.6%) still had at least one process deviation**, and 227 of 240 runs failed at least one check overall.

Score the outcome and the process separately — tool selection, arguments, ordering, scope. Take ground truth from an **independent call**, never from the agent's account of itself: a separate review found **116 of 262 agent decisions (44.3%) were absent from the agent's own report** (arXiv 2610.01769).

A safety metric can also be inflated by refusing more. Report safety and accuracy separately, and keep a middle label.

## Evidence integrity (K276 + K277)

A visible chain-of-thought trace is weak evidence for the process. arXiv **2609.38107** measured it: on the hardest iGSM instances, 31.6% of correct answers carry invalid traces, and over half of those pass every syntax and arithmetic check and fail a semantic dependency check.

A summary is not the document. Research summarised by Klement (2026-10-01) reported a buy-or-sell call flipping in one case in four to one in three when an agent read a summary instead of the full filing.

Rule: score the re-run and the source, not the trace and the summary.

## NEVER

- Do not rewrite `## Verify` or lint rules to match a failing agent (K162).
- Do not auto-evolve `.cursor/skills` from harness-dev feedback.
- Visible feedback alone ≠ held-out transfer.
- Do not accept a chain-of-thought trace or an agent summary as proof that the check ran.
- Do not accept a passing final result as evidence the process was correct.
- Do not take the agent's own report as ground truth for what it did.
- Do not blame model strength for a failure that a missing state explains.
- Do not treat a displayed counter as a limit.
