---
title: Robust-TO — confidence-aware tool orchestration (arXiv 2606.26904)
type: source
tags: [source, arxiv, agent-orchestration, tool-confidence, video-understanding, robust-to]
keywords: [2606.26904, robust-to, blind-trust-problem, confidence-aware, grpo, tool-routing, reliability-relevance]
related:
  - concepts/confidence-aware-tool-orchestration.md
  - concepts/tool-environment-unreliability-eval.md
  - concepts/agent-runtime-guardrails.md
  - concepts/seclaw-agent-security-evaluation.md
  - concepts/prompt-injection-detector-calibration.md
  - concepts/agent-least-privilege-tool-selection.md
  - concepts/llm-pentest-automation.md
  - concepts/mcp-security-posture.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-07-02
updated: 2026-07-02
phase_0_verdict: "Reference 2026-07-02 — no public code repo; CV/video embodied benchmark; steal orchestration pattern only"
---

**Briefs:** `briefs/2026-07-02_robust-to-confidence-aware-tool-routing-handoff.md`, `briefs/2026-07-02_prod-mcp-tool-confidence-contract-checklist.md`

## Relations

- @concepts/confidence-aware-tool-orchestration.md — transferable (result, confidence) orchestration synthesis
- @concepts/tool-environment-unreliability-eval.md — complementary hazard/recovery eval axis

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Confidence-Aware Tool Orchestration for Robust Video Understanding |
| Authors | Yangfan He, Yujin Choi, Jaehong Yoon |
| Affiliation | NTU Singapore; U Minnesota; UNIST |
| arXiv | 2606.26904 |
| Project | https://rova-v2.github.io/ |
| Code | Promised ("We release code and checkpoints") — **no public GitHub at ingest** |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2606.26904-confidence-aware-tool-orchestration-robust-to.pdf` |
| Retrieved | 2026-07-02 |
| Read status | **read** (Blind Trust Problem, Robust-TO pipeline, GRPO reward, UV-Bench / VSI-Bench + RoVA corruptions) |

## Narrative

**Robust-TO** is an agentic **video understanding** framework addressing the **Blind Trust Problem**: Video-LLMs treat every frame and tool output as equally reliable; under motion blur, glare, occlusion, low light, or noise, frontier models lose **15–30 percentage points** on embodied benchmarks while **self-reported confidence stays flat** — silent failure for downstream planners.

### Pipeline (steal-for agent MCP eval)

1. **Quality profiling** — rank inputs by `reliability × relevance`; prune untrustworthy or irrelevant observations before tool calls.
2. **Unified evidence interface** — each tool returns `(result, confidence)` with calibrated reliability; corruption type routes to the best-matched tool (e.g., blur → caption; occlusion → action recognition).
3. **Three-tier synthesis** — fuse HIGH / MEDIUM / LOW evidence; discard contradictory MEDIUM facts rather than averaging.
4. **Confidence-cost GRPO** — reward jointly optimizes correctness, evidence reliability, and efficiency; frozen disturbance estimator prevents reward gaming.

### Results [CONFIRMED from paper tables]

| Setting | Robust-TO + Qwen3-VL-7B | Notes |
|---------|-------------------------|-------|
| Clean avg (8 tasks) | **56.4%** | +10.6pp vs strongest OSS; beats Gemini-2.5-Pro (46.2%) |
| RoVA corrupted avg | **54.3%** | +5.8pp vs Video-R1; **Δ=3.0** clean→corrupt (smallest among compared) |
| Frames read | **20.7** vs 32 baseline | −35% frames, <5% latency overhead on clean |

### Cybersec-wiki relevance

Primary domain is **CV/embodied video**, not MCP security. Ingest value is the **orchestration pattern**: explicit tool-output confidence, disturbance-aware routing, tiered evidence fusion — maps to prod MCP agents that must not treat HTTP 200 + garbage JSON as HIGH-trust evidence (@concepts/tool-environment-unreliability-eval.md). Cross-route video/drone recon steal to physical-pentest labs only when authorized.

### Phase-0 (2026-07-02)

| Gate | Status |
|------|--------|
| Public repo | **FAIL** — project page only; no LICENSE to audit |
| Domain fit | **PARTIAL** — agent orchestration pattern, not offensive/defensive security tool |
| Verdict | **Reference** — cite methodology; re-audit when code ships |

## Snippets

> "We formalize this implicit assumption as the Blind Trust Problem: every frame is treated as equally informative, every perception output as equally reliable, and the model's confidence in its answer is decoupled from the visual conditions that produced it."
[Source: arxiv-2606.26904-confidence-aware-tool-orchestration-robust-to.pdf §Introduction]

> "Each tool returns evidence in a shared format: a concrete prediction … temporal grounding, and a calibrated reliability score."
[Source: arxiv-2606.26904-confidence-aware-tool-orchestration-robust-to.pdf abstract — paraphrase anchor]
