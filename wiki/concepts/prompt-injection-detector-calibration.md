---
title: Prompt injection detector calibration
type: concept
tags: [llm-security, prompt-injection, guard-model, calibration, mcp]
keywords: [2606.22659, severity metric, confident false negatives, protectai, prompt-guard, content-keying, bipia]
related:
  - concepts/ai-for-cybersecurity.md
  - sources/arxiv-2606-22659-confidently-wrong-prompt-injection-calibration.md
  - entities/tools/picalib-research.md
  - concepts/agent-runtime-guardrails.md
  - concepts/mcp-security-posture.md
  - entities/tools/llm-defense-lattice.md
  - concepts/llm-adversarial-fuzzing.md
  - sources/arxiv-2606-02822-owasp-llm-defense-attribution.md
  - sources/arxiv-2606-26904-confidence-aware-tool-orchestration-robust-to.md
  - concepts/confidence-aware-tool-orchestration.md
  - sources/arxiv-2606-30587-cognitive-heuristics-llm-vuln-detection.md
  - sources/arxiv-2606-30587-cognitive-heuristics-llm-vuln-detection.md
  - concepts/cognitive-heuristics-llm-vuln-detection.md
  - concepts/piminer-agentic-prompt-injection-redteam.md
  - sources/arxiv-2608-05108-piminer-prompt-injection-redteam.md
  - entities/tools/piminer.md
  - sources/arxiv-2608-16806-esti-state-semantic-injection.md
  - concepts/planner-state-integrity-embodied-agents.md
  - sources/arxiv-2608-16852-rule-blindness-compliance-detectors.md
  - concepts/compliance-detector-rule-blindness.md
maturity: draft
created: 2026-06-23
updated: 2026-08-06
---

## Relations

- @sources/arxiv-2606-22659-confidently-wrong-prompt-injection-calibration.md — primary source
- @entities/tools/llm-defense-lattice.md — OWASP LLM01 probe attribution complement
- @concepts/piminer-agentic-prompt-injection-redteam.md
- @sources/arxiv-2608-05108-piminer-prompt-injection-redteam.md
- @entities/tools/piminer.md

## Narrative

Ingest 2026-06-23: arXiv:2606.22659 — **guard-model accuracy is the wrong metric** when detectors assign **high confidence to missed attacks** under distribution shift.

### Severity metric S

| Signal | Meaning |
|--------|---------|
| Low S miss | Detector uncertain on failure — safer to fail open for human review |
| **High S miss (≈1.0)** | Detector **confidently wrong** — downstream system auto-trusts exploit |

Paper finding: ProtectAI-v2 + Prompt-Guard-2 miss with **S ∈ [0.99, 1.00]** across five shifts while FNR spans 0.01–0.97.

### Universal blind spot

**Indirect behavior-hijack** (BIPIA-style embedded instructions) — missed by **both vendors** across 4× model size range. Root cause: **content-keying** (looks like benign document text), not jailbreak tokens.

### Production controls

1. **Shift-test guards** — freeze threshold on clean set; evaluate on indirect injection + tool-output channels
2. **Never trust high-confidence alone** — pair guards with structural controls (AIRGuard, allowlists, ePCA where applicable)
3. **Log confident passes** of untrusted content for SOC review
4. **MCP/lazy-tool:** tool-return path is indirect injection surface — guards tuned on standalone prompts will miss

See `briefs/2026-06-23_prompt-guard-severity-calibration-handoff.md`.
