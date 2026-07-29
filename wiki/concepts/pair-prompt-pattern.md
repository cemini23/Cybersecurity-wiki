---
title: PAIR — Prompt Automated Iterative Refinement
type: concept
tags: [llm-security, jailbreak, pair, single-turn, attacker-llm, arxiv-2310-08419]
keywords: [pair, prompt automated iterative refinement, single-turn jailbreak, attacker llm, chao chen et al]
related:
  - entities/tools/fuzzyai.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/crescendo-multi-turn-jailbreak.md
  - concepts/ai-for-cybersecurity.md
  - concepts/amt-x-phase-structured-multi-turn-red-teaming.md
  - sources/arxiv-2607-11151-amt-x-phase-structured-multi-turn-red-teaming.md
  - concepts/defender-centric-jailbreak-utility.md
  - sources/arxiv-2607-17152-a-mess-defender-centric-jailbreak.md
  - concepts/ai-redteam-evidential-ceiling.md
  - concepts/concept2scenario-refusal-suppression.md
  - sources/arxiv-2607-21735-ai-redteam-evidential-ceiling.md
  - sources/arxiv-2607-23496-concept2scenario-vulnerable-scenarios.md
maturity: validated
created: 2026-05-13
updated: 2026-07-29
---

## Relations

- @sources/arxiv-2607-17152-a-mess-defender-centric-jailbreak.md
- @concepts/defender-centric-jailbreak-utility.md
- @entities/tools/fuzzyai.md — reference implementation (CLI flag `-a pair`)
- @concepts/llm-adversarial-fuzzing.md — methodology umbrella; PAIR is one pattern under it
- @concepts/crescendo-multi-turn-jailbreak.md — companion multi-turn pattern; PAIR is single-turn
- @concepts/ai-for-cybersecurity.md — LLM × security context
- @concepts/ai-redteam-evidential-ceiling.md
- @concepts/concept2scenario-refusal-suppression.md
- @sources/arxiv-2607-21735-ai-redteam-evidential-ceiling.md
- @sources/arxiv-2607-23496-concept2scenario-vulnerable-scenarios.md

## Raw Concept

PAIR (Prompt Automated Iterative Refinement) was introduced in Chao et al, "Jailbreaking Black-Box Large Language Models in Twenty Queries" ([arXiv:2310.08419](https://arxiv.org/abs/2310.08419), October 2023). The paper's claim is that ~20 attacker-LLM queries suffice to discover a working jailbreak for typical commercial LLMs of that era — single-turn, black-box, no model internals needed. [Source: arXiv:2310.08419 (retrieved 2026-05-13)]

## Narrative

**PAIR is a single-turn, black-box jailbreak generator.** An attacker LLM is given a goal ("get the target to produce X") and the target's most recent refusal; it generates a new prompt that attempts to overcome the refusal; the new prompt is sent to the target; the cycle repeats until either the target produces the requested output, or the attacker exhausts its iteration budget. [CONFIRMED]

### Mechanism

1. **Attacker LLM** = a sufficiently-capable model (the paper used GPT-4 / Vicuna-13B; current practice favors Claude 3+ or GPT-4o for attacker quality).
2. **Target LLM** = the model under test.
3. **Judge** = either the attacker itself (cheap, biased toward declaring victory) or a separate classifier (more robust, slower).
4. **Loop** — attacker reads (goal, last refusal) → generates candidate prompt → target responds → judge scores → either stop or feed back to attacker.

The attacker-LLM is the bottleneck: a weak attacker produces weak prompts and iteration counts balloon. A strong attacker compresses the search.

### Why "20 queries"

The paper's headline number; it's a median, not a guarantee. For hardened modern targets (Claude 3.5+, GPT-4o, Gemini 1.5+ with full safety stacks), median climbs to 50-100+, and some goals are not reachable single-turn at all — which is when you switch to @concepts/crescendo-multi-turn-jailbreak.md. [TENTATIVE 2026-05-13 — informal practitioner consensus, not a published replication]

### Coverage characteristics [CONFIRMED]

- **Strong on**: refusal-evasion via reframing, hypotheticalization ("in a fictional setting..."), role-play, deontological-vs-consequentialist framing.
- **Weak on**: goals requiring sustained context that doesn't fit one turn (long-form harmful content, multi-step harmful procedures with state).
- **Useless on**: provider-level safety filters (e.g., content moderation that runs *before* the model sees input). Those need a different attack class.

### Where PAIR fits in this wiki

PAIR is one of FuzzyAI's 18 attack methods (CLI flag `-a pair`) — see @entities/tools/fuzzyai.md. It's the most-cited because of the paper, the easiest to explain, and the cheapest to run. **Do not rely on PAIR alone** for production LLM-robustness testing; pair (no pun intended) with Crescendo-class multi-turn coverage at minimum.

## Snippets

```bash
# FuzzyAI invocation (verbose)
fuzzyai run \
  -a pair \
  --target-model gpt-4o-mini \
  --attacker-model claude-3-5-sonnet \
  --judge-model claude-3-5-sonnet \
  --goal "your-explicit-policy-violating-goal-string" \
  --max-iterations 20 \
  --output traces/pair-run-2026-05-13.jsonl
```

## Dead Ends

- **Using a weak attacker LLM to save cost** — PAIR quality degrades roughly linearly with attacker quality. Cheap attacker = more iterations, not fewer. Total cost is roughly constant; spend it on stronger attacker, not more iterations. [TENTATIVE — practitioner heuristic, not measured]
- **Self-judging the attacker** — the attacker is incentivized to claim victory. Use a separate judge model or human-sampled scoring. [CONFIRMED]
- **Replaying old PAIR-discovered prompts** — vendors patch fast. A prompt that worked last quarter may not work this quarter. PAIR is a *discovery* mechanism; its outputs aren't durable. [CONFIRMED]
