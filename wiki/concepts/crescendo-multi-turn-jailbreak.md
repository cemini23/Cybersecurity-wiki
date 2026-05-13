---
title: Crescendo — multi-turn jailbreak escalation
type: concept
tags: [llm-security, jailbreak, multi-turn, crescendo, escalation, microsoft-research, arxiv-2404-01833]
keywords: [crescendo, multi-turn jailbreak, escalation attack, mark russinovich, microsoft research, conversational drift]
related:
  - entities/tools/fuzzyai.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/pair-prompt-pattern.md
  - concepts/social-engineering.md
  - concepts/ai-for-cybersecurity.md
maturity: validated
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- @entities/tools/fuzzyai.md — reference implementation (CLI flag `-a crs`)
- @concepts/llm-adversarial-fuzzing.md — methodology umbrella
- @concepts/pair-prompt-pattern.md — companion single-turn pattern
- @concepts/social-engineering.md — Crescendo is structurally a social-engineering attack against the model
- @concepts/ai-for-cybersecurity.md — LLM × security context

## Raw Concept

Crescendo was introduced in Russinovich et al, "The Crescendo Multi-Turn LLM Jailbreak Attack" ([arXiv:2404.01833](https://arxiv.org/abs/2404.01833), April 2024). Microsoft Research authorship. The paper's claim is that even policy-hardened LLMs can be walked across the refusal boundary in 5-10 turns of *individually-benign* exchanges, by chaining incremental commitments. [Source: arXiv:2404.01833 (retrieved 2026-05-13)]

## Narrative

**Crescendo is multi-turn escalation.** Each turn is, in isolation, a benign exchange the model would accept. The attack lives in the *trajectory*: by turn N, the model has made small accommodations on turns 1 through N-1 that, taken together, constitute the policy-violating output the attacker wanted. The attack is named after the musical term — gradual increase — and the structural analogy is exact. [CONFIRMED]

### Why it works on hardened models

PAIR-class single-turn attacks are well-defended against in recent frontier models: classifiers see "the bad prompt" in one turn and can refuse. Crescendo bypasses single-turn classifiers because **no single turn is the bad prompt**. The harm emerges from conversational state, which most production safety stacks track poorly.

The pattern recapitulates classic social-engineering: incremental commitment, foot-in-the-door, consistency bias. Models, like humans, are reluctant to contradict their own prior turns. See @concepts/social-engineering.md for the human-target analog.

### Mechanism [CONFIRMED]

1. **Attacker LLM** plans a multi-turn trajectory toward the target goal. Each turn's prompt is calibrated to: (a) reference the model's prior commitments, (b) advance by one small step, (c) remain individually defensible.
2. **Target LLM** answers each turn. If it refuses, attacker backs off one step and tries a smaller increment.
3. **Judge** evaluates the *cumulative* output, not turn-N in isolation. This is critical — turn-N alone often looks fine. The state matters.
4. Stop when target produces the goal-output, or attacker exhausts turn budget (typical ceiling: 8-12 turns).

### Coverage characteristics [CONFIRMED]

- **Strong on**: long-form harmful content, multi-step harmful procedures, persona-drift attacks where the model is incrementally walked into an unsafe role.
- **Strong against**: single-turn safety classifiers, refusal-policy stacks that lack multi-turn state awareness.
- **Weak against**: stateful safety architectures that re-evaluate the conversation in aggregate at each turn (still rare in production, common in research).
- **Cost**: 5-10× a PAIR-equivalent run, because each "attempt" is 5-10 turns instead of one.

### Why it's the more important production-coverage attack

Real adversarial users of deployed LLMs converse multi-turn. They don't send one optimized jailbreak — they have a conversation. A production-robustness test program that runs PAIR-only is **systematically blind** to the dominant real-world attack pattern. [CONFIRMED]

### Authorized use

Same floor as @concepts/llm-adversarial-fuzzing.md. Crescendo is dual-use; test only LLMs you own or have explicit authorization to test.

## Snippets

```bash
# FuzzyAI Crescendo invocation
fuzzyai run \
  -a crs \
  --target-model gpt-4o \
  --attacker-model claude-3-5-sonnet \
  --judge-model claude-3-5-sonnet \
  --goal "your-explicit-policy-violating-goal-string" \
  --max-turns 10 \
  --output traces/crescendo-run-2026-05-13.jsonl
```

## Dead Ends

- **Judging turn-N in isolation** — turn-N often looks innocuous. Judging must run on the cumulative conversation state. This is the most common implementation error in Crescendo evaluators. [CONFIRMED]
- **Hard turn-budget cutoffs without back-off** — Crescendo's success rate increases nonmonotonically with turn budget if back-off is implemented (try smaller increment after refusal). Without back-off, raising the budget plateaus quickly. [TENTATIVE — practitioner observation, not in paper]
- **Treating Crescendo as social-engineering theory only** — the social-engineering analog is real, but Crescendo is a *measurable, automatable* attack. Skipping it because "it's just social engineering" leaves a measurable production-robustness gap. [CONFIRMED]
