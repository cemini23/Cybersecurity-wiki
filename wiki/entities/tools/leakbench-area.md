---
title: LeakBench + AREA — prompt leakage benchmark and attention re-anchoring defense
type: entity
tags: [tool, llm-security, benchmark, prompt-leaking, area, leakbench, reference]
keywords: [leakbench, area, attention re-anchoring, nesa-lab, 2606.18673, prompt leaking]
related:
  - concepts/mcp-security-posture.md
  - sources/arxiv-2606-18673-prompt-leaking-attacks-area.md
  - concepts/system-prompt-leakage.md
  - concepts/llm-adversarial-fuzzing.md
  - entities/tools/llm-defense-lattice.md
  - entities/tools/cryptex-oss.md
  - concepts/agent-runtime-guardrails.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
created: 2026-06-22
updated: 2026-06-22
phase_0_verdict: "Reference 2026-06-22 — github.com/NESA-Lab/AREA: LeakBench/AREA code present, 0★, no LICENSE file on GitHub API; use benchmark methodology until SPDX verified"
---

## Relations

- @sources/arxiv-2606-18673-prompt-leaking-attacks-area.md — ACM CCS 2026 paper provenance
- @concepts/system-prompt-leakage.md — threat model + defense ladder
- @entities/tools/llm-defense-lattice.md — OWASP LLM07 complementary BAS axis

## Raw Concept

Entity stub from ingest 2026-06-22 — **LeakBench** evaluation corpus + **AREA (Attention Re-Anchoring)** soft-prompt defense from Zhejiang University (NESA-Lab).

## Narrative

### LeakBench

Open benchmark in [github.com/NESA-Lab/AREA](https://github.com/NESA-Lab/AREA):

| Component | Contents |
|-----------|----------|
| 50 system prompts | Task-oriented, curated from real-world sources (Awesome ChatGPT Prompts lineage) |
| 600 adversarial queries | 200 per victim LLM × 3 models |
| Benign query sets | Usability / functionality preservation per prompt |

Evaluates **7 defenses** across leakage effectiveness + application usability. Metrics include **PLS** (leakage score) and **SS** (semantic similarity to ground-truth prompt).

### AREA defense

Trainable soft-prompt tail appended after defensive instruction — counteracts **attention drift** without editing core system prompt logic. Paper claims parity with PromptObfuscation/SysVec on leakage resistance with **+33% usability** and **~3×** faster optimization.

### Phase-0 adoption gate

| Check | Result |
|-------|--------|
| Repo exists | ✓ NESA-Lab/AREA |
| LICENSE | ✗ null/404 on GitHub API (2026-06-22) |
| Stars / maturity | 0★; pushed 2026-06-14 |
| **Verdict** | **Reference** — cite LeakBench methodology; no production deploy until license audit |

### Operator use

- **Red team:** adapt LeakBench query patterns against client GPT wrappers / copilot apps
- **Lab:** pair with @entities/tools/cryptex-oss.md mutators for paraphrase sweeps
- **Do not** treat prompt-append-only client defenses as sufficient without output-side controls
