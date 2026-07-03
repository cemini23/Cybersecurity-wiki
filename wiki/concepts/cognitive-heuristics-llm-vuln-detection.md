---
title: Cognitive heuristics in LLM vulnerability detection
type: concept
tags: [concept, llm-security, code-review, cognitive-bias, devsecops, red-team]
keywords: [halo-effect, framing-effect, anchoring-effect, blind-trust, cognitive-attack, llm-scanner, copilot-autofix]
related:
  - sources/arxiv-2606-30587-cognitive-heuristics-llm-vuln-detection.md
  - concepts/llm-code-review-agent-security.md
  - concepts/llm-vulnerability-discovery.md
  - concepts/social-engineering.md
  - concepts/prompt-injection-detector-calibration.md
  - concepts/ai-for-cybersecurity.md
  - concepts/agent-runtime-guardrails.md
  - sources/arxiv-2606-13757-sevra-bench-social-engineering-review-agents.md
  - entities/tools/sevra-bench.md
  - entities/tools/defending-code-reference-harness.md
maturity: draft
created: 2026-07-03
updated: 2026-07-03
---

**Briefs:** `briefs/2026-07-03_cognitive-heuristics-llm-scanner-redteam-checklist.md`, `briefs/2026-07-03_ci-merge-gate-cognitive-context-hardening-handoff.md`

## Relations

- @sources/arxiv-2606-30587-cognitive-heuristics-llm-vuln-detection.md — primary source (2606.30587)
- @concepts/llm-code-review-agent-security.md — SEVRA merge-gate framing (orthogonal attack surface)

## Raw Concept

Ingest 2026-07-03: arXiv 2606.30587 — LLM vulnerability scanners are deployed as CI/CD gatekeepers but evaluated as `code → verdict` functions. **Non-code context** (author, task framing, prior scan results) systematically flips verdicts on **identical code** via cognitive heuristics.

## Narrative

### Three heuristic attack surfaces

| Heuristic | Prod context vector | Defender impact |
|-----------|---------------------|-----------------|
| **Halo** | PR author, committer reputation, "senior engineer" labels | Trust signal suppresses scrutiny (+ false negatives) |
| **Framing** | "routine refactor" vs "security-critical patch" | Urgency/objective shifts detection rate |
| **Anchoring** | Prior bot comment, stale SAST result, CI badge | Anchored to wrong prior verdict |

Cross-model average susceptibility: **framing 33.2%** > **anchoring 23.5%** > **halo 18.4%** [Source: 2606.30587].

### Black-box cognitive attack

Chained heuristic prompts can **suppress up to 97%** of vulnerabilities a neutral prompt would catch — without changing code. Semantic-reasoning flaws (logic bugs, null-deref chains) more susceptible than pattern-match CWEs.

### Eval stack (pair, don't substitute)

| Eval | What it measures |
|------|------------------|
| **Neutral code-only baseline** | Raw detection capability |
| **Heuristic perturbation suite (2606.30587)** | Context-manipulation robustness |
| **SEVRA-BENCH (2606.13757)** | Adversarial diff + PR narrative merge approval |
| **SAST/DCI + ASAN verify** | Independent ground truth (@entities/tools/defending-code-reference-harness.md) |

### Hardening checklist [TENTATIVE]

1. **Strip or normalize** author/reputation fields from LLM scanner prompts
2. **Fixed security system prompt** — never "routine-only" framing on merge bots
3. **Ignore prior-bot anchors** — re-scan from neutral template each run
4. **Regression-test** halo/framing/anchoring variants before model swaps
5. **Human gate** on approve/merge MCP tools when LLM reviewer is in loop
6. **Never sole gate** — parallel deterministic scanner required

### Limits

- Paper uses API black-box access; white-box fine-tunes may differ.
- No MCP/agent trajectory eval — single-shot verdict only.
- Author reputation explicitly excluded in SEVRA but is a **primary halo vector** here — prod systems often include it.

## Snippets

> "Vulnerabilities that require semantic reasoning for detection are more susceptible to cognitive heuristics than those identifiable through pattern matching."
[Source: arxiv-2606.30587 abstract]
