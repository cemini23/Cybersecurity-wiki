---
name: skill-set-budget
description: >-
  Select a complementary skill set under a token budget instead of top-k
  semantic ranking (BPS / Best Prefix Selection steal). Use when many skills
  could apply, when auditing the skill library for distractors, or when the
  user says BPS / skill-set budget.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
disable-model-invocation: true
federation: true
---

# Skill-set budget — set, not top-k (BPS steal)

Canon: CCC `@wiki/concepts/skill-set-selection-under-budget.md`. Paper: arXiv **2608.19993** Best Prefix Selection. **Do not** implement the paper’s polynomial BPS solver or clone a repo. Steal the *decision rule*.

## Problem

Agents score skills independently by semantic relevance, then pack top-k. Redundant or distractor skills waste context and can hurt. BPS chooses a **set** under a hard token budget: monotone submodular benefit minus context penalty (paper: 0.73 vs 0.20–0.52 routers; ~28% fewer tokens).

## This-turn procedure

When more than two skills look relevant:

1. List candidates (name + why + rough token cost: short vs long SKILL.md).
2. **Greedy set:** add a skill only if it supplies a *capability the current set lacks* (complement). Skip near-duplicates (distractors).
3. Stop when the next add’s token cost exceeds its marginal benefit, or when three skills already cover the task.
4. Read **only** the chosen set. Do not dump the rest of `.cursor/skills`.
5. Federation alwaysApply rules already in context are not “selected skills” — do not re-read them.

## Complements vs distractors

| Complement | Distractor |
|------------|------------|
| Adds a missing verifier, domain, or tool class | Overlaps a skill already loaded; keyword-match only |
| Needed for a required check | Never fires given this task’s tools |

A skill that scores well standalone but adds nothing in-set is a distractor.

## NEVER

- Do not auto-promote / auto-evolve `.cursor/skills` from this audit (misevolution).
- Do not treat BPS as a reason to load *more* skills.
- No third-party skill-catalog mirroring.
