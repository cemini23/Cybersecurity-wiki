---
title: Words Speak Louder Than Code — cognitive heuristics in LLM vuln detection (arXiv 2606.30587)
type: source
tags: [source, arxiv, llm-security, code-review, cognitive-heuristics, vuln-detection]
keywords: [2606.30587, halo-effect, framing-effect, anchoring-effect, cognitive-attack, copilot-autofix, zeropath]
related:
  - concepts/cognitive-heuristics-llm-vuln-detection.md
  - concepts/prompt-injection-detector-calibration.md
  - concepts/llm-code-review-agent-security.md
  - concepts/llm-vulnerability-discovery.md
  - concepts/social-engineering.md
  - concepts/ai-for-cybersecurity.md
  - concepts/agent-runtime-guardrails.md
  - sources/arxiv-2606-13757-sevra-bench-social-engineering-review-agents.md
  - entities/tools/sevra-bench.md
  - entities/tools/defending-code-reference-harness.md
maturity: draft
read_status: read
created: 2026-07-03
updated: 2026-07-31
phase_0_verdict: "Reference 2026-07-03 — no public code artifact; controlled evaluation framework + black-box cognitive attack PoC"
wire_status: wont_wire
wire_target: "REFERENCE / steal-from — paper or methodology only"
---

**Briefs:** `briefs/2026-07-03_cognitive-heuristics-llm-scanner-redteam-checklist.md`, `briefs/2026-07-03_ci-merge-gate-cognitive-context-hardening-handoff.md`

## Relations

- @concepts/cognitive-heuristics-llm-vuln-detection.md — synthesis
- @concepts/llm-code-review-agent-security.md — merge-gate / CI scanner complement to SEVRA

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Words Speak Louder Than Code: Investigating Cognitive Heuristics in LLM-Based Code Vulnerability Detection |
| Authors | Asif Shahriar, Hongyu Cai, Hadjer Benkraouda, Gang Wang, Z. Berkay Celik |
| Affiliation | BRAC University; Purdue; UIUC |
| arXiv | 2606.30587 |
| Code | None published at ingest |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2606.30587-words-speak-louder-cognitive-heuristics-llm-vuln-detection.pdf` |
| Retrieved | 2026-07-03 |
| Read status | **read** (framework, three heuristics, 8-model eval, cognitive attack PoC, semantic vs pattern susceptibility) |

## Narrative

First systematic study of **cognitive heuristics** biasing LLM **code vulnerability detection**. Prior work tests `code → verdict` in isolation; deployed scanners (Copilot Autofix, ZeroPath, Claude Opus Firefox audit) also ingest **non-code context** — author reputation, task framing, prior analysis — that psychology research shows biases human judgment.

### Controlled framework

**Code fixed; only surrounding context varies** across three heuristics:

| Heuristic | Manipulation | Example |
|-----------|--------------|---------|
| **Halo** | Author attribution polarity | "junior developer" vs "principal security engineer" |
| **Framing** | Task objective / consequences | Security-critical audit vs routine refactor check |
| **Anchoring** | Prior analysis result | Injected "prior scan: SAFE" vs "prior scan: VULNERABLE" |

Eight LLMs × three languages; neutral baseline: *"Review the following code to identify whether it is safe or vulnerable."*

### Key findings

| Metric | Value |
|--------|-------|
| Cross-model avg susceptibility — framing | **33.2%** |
| Cross-model avg susceptibility — anchoring | **23.5%** |
| Cross-model avg susceptibility — halo | **18.4%** |
| Black-box cognitive attack suppression | **up to 97%** of previously detected vulns |
| Semantic-reasoning vulns | More heuristic-susceptible than pattern-match CWEs |
| Verdict flips | Models flip safe↔vulnerable without correctly identifying the actual flaw |

**Model notes [TENTATIVE]:** Claude and Gemini show worst halo utility; GPT exhibits inverse halo under some conditions; DeepSeek/Qwen most affected by combined attacks.

### vs SEVRA (2606.13757)

| Dimension | SEVRA | This paper (2606.30587) |
|-----------|-------|-------------------------|
| Setting | Adversary controls diff + PR narrative | **Fixed vulnerable code**; context-only manipulation |
| Decision | Merge approve/decline | Safe/vulnerable verdict |
| Attack class | 15 PR framing strategies | Psychology heuristics (halo/framing/anchoring) |
| Overlap | Both show narrative beats code for LLM scanners | Complementary eval lanes |

### Phase-0 (2026-07-03)

| Gate | Status |
|------|--------|
| Artifact | No public repo |
| Domain | LLM AppSec / CI gate reliability |
| Verdict | **Reference** — methodology + red-team checklist; re-audit if benchmark code releases |

## Snippets

> "Models often change their verdict from safe to vulnerable based on the cognitive condition, without accurately identifying the actual vulnerability."
[Source: arxiv-2606.30587-words-speak-louder-cognitive-heuristics-llm-vuln-detection.pdf abstract]

> "We demonstrate a proof-of-concept black-box cognitive attack that can suppress up to 97% of previously detected vulnerabilities."
[Source: arxiv-2606.30587-words-speak-louder-cognitive-heuristics-llm-vuln-detection.pdf abstract]
