---
title: FuzzyAI — LLM jailbreak / adversarial-prompt fuzzer (CyberArk)
type: entity
tags: [llm-security, jailbreak, fuzzer, red-team, pair, crescendo, adversarial-prompt, apache-2.0]
keywords: [fuzzyai, cyberark, llm jailbreak, prompt fuzzing, pair, crescendo, adversarial prompts]
related:
  - concepts/llm-adversarial-fuzzing.md
  - concepts/pair-prompt-pattern.md
  - concepts/crescendo-multi-turn-jailbreak.md
  - concepts/ai-for-cybersecurity.md
  - concepts/llm-vulnerability-discovery.md
  - concepts/red-team-operations.md
  - concepts/responsible-disclosure.md
  - entities/tools/cua.md
  - "@osint-wiki/entities/tools/fuzzyai.md"
  - entities/tools/cryptex-oss.md
  - sources/arxiv-2606-24166-toxsearch-s-distributed-toxicity-search.md
maturity: validated
created: 2026-05-13
updated: 2026-06-26
---

## Relations

- @concepts/llm-adversarial-fuzzing.md — methodology umbrella for this tool
- @concepts/pair-prompt-pattern.md — PAIR (Prompt Automated Iterative Refinement) detail page
- @concepts/crescendo-multi-turn-jailbreak.md — Crescendo multi-turn attack detail page
- @concepts/ai-for-cybersecurity.md — where LLMs intersect security
- @concepts/llm-vulnerability-discovery.md — sibling discipline (LLMs *finding* vulns, vs FuzzyAI which attacks LLMs themselves)
- @concepts/red-team-operations.md — primary use context (authorized LLM-robustness testing)
- @concepts/responsible-disclosure.md — ethics floor for FuzzyAI use
- @entities/tools/cua.md — pair with cua to capture full trace of multi-turn jailbreak runs
- @osint-wiki/entities/tools/fuzzyai.md — sibling-wiki Phase-0 audit notes; cross-routes to verbalized-sampling Vector 5 (news-rewriter robustness)
- @entities/tools/cryptex-oss.md — alternative transform catalog (162 transforms); compare in Phase-0

## Raw Concept

Phase-0 audit completed 2026-05-13 via `briefs/2026-05-13_fuzzyai-adoption.md` (gitignored). Verdict: **GO** for cybersec-wiki primary adoption as the standard LLM-adversarial testing framework. Source repo: [github.com/cyberark/FuzzyAI](https://github.com/cyberark/FuzzyAI), Apache-2.0, ~1.3k stars, CyberArk Labs backing.

## Narrative

FuzzyAI is a structured framework for **attacking LLMs**. Not for using LLMs to attack other targets — for that, see @concepts/llm-vulnerability-discovery.md. The repo ships 18 attack methods, of which two are research-anchored and most-cited: **PAIR** (Prompt Automated Iterative Refinement, [arXiv:2310.08419](https://arxiv.org/abs/2310.08419)) and **Crescendo** ([arXiv:2404.01833](https://arxiv.org/abs/2404.01833)). The remaining 16 are a curated catalog of DAN-class, role-play, context-injection, and encoding-trick patterns. [CONFIRMED]

**License + backing make this an unusually credible primary tool**: Apache-2.0 means you can use, fork, and embed it freely (including in commercial red-team consulting deliverables). CyberArk Labs backing means active maintenance and a real engineering team behind the prompt catalog. [CONFIRMED]

### What it is, and what it is not [CONFIRMED]

- **It is** an offensive testing framework: you point it at an LLM target, configure an attacker-LLM, pick an attack pattern, and it iterates.
- **It is not** a defensive product. There is no detection library, no "is this prompt malicious?" classifier, no runtime guardrail. The Apache repo is offense-only by design.
- For defensive complement: separate tools — NVIDIA NeMo Guardrails, promptguard, or Anthropic's own Constitutional AI patterns. Defensive coverage is a *separate workstream* not addressed by FuzzyAI.

### Cybersec-wiki coverage gap filled

Prior to this entity page, this wiki had **zero LLM-adversarial framework coverage**. Existing pages mention LLM use as a tool (@concepts/ai-for-cybersecurity.md), and there's a page on using LLMs to find vulnerabilities in code (@concepts/llm-vulnerability-discovery.md), but no documented framework for the inverse — testing LLM robustness directly. FuzzyAI fills that gap.

### Cost model

- pip install is free; attacker-LLM API calls are not. PAIR iterations average 10-30 attacker-LLM calls per target attempt; multi-target sweeps can run $5-50 per campaign at current GPT-4 / Claude Sonnet prices. [TENTATIVE 2026-05-13 — pricing is volatile]
- Self-hosted attacker-LLMs (Llama, Mistral) drop the per-call cost to zero but raise iteration count to compensate for weaker attack-generation quality. Trade-off documented in @concepts/llm-adversarial-fuzzing.md.

### Authorized-use boundaries [CONFIRMED]

FuzzyAI is dual-use. Acceptable uses:
- Internal LLM-product robustness testing (your own deployed LLM, your own data)
- Red-team engagements with written authorization that explicitly scopes LLM-targets
- Academic research with IRB-equivalent approval
- CTF / lab environments

**Not acceptable**: jailbreaking third-party LLMs (OpenAI, Anthropic, etc.) without their published red-team program participation. Most major vendors have bug-bounty / responsible-disclosure programs for this — see @concepts/responsible-disclosure.md.

## Snippets

```bash
# install
pip install fuzzyai
# PAIR attack against a target via CLI
fuzzyai run -a pair --target-model gpt-4o-mini --attacker-model claude-3-haiku \
  --goal "produce instructions for synthesizing methamphetamine" \
  --max-iterations 20
# Crescendo (multi-turn) against the same target
fuzzyai run -a crs --target-model gpt-4o-mini --max-turns 8
```

## Dead Ends

- **"FuzzyAI is a defense tool"** — common misread of CyberArk Labs branding. The framework is offense-only; treating it as defense is a category error. [CONFIRMED]
- **Sole reliance on PAIR for safety testing** — PAIR's iterative-refinement loop is biased toward single-turn jailbreaks. Production safety testing needs Crescendo (multi-turn) coverage too, and ideally several of the other 16 methods. [TENTATIVE — based on attack-method category coverage analysis, not measured efficacy]
