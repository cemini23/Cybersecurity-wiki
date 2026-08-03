---
title: InferScale
type: entity
category: tool
tags: [entity, tool, bsd, llm-serving, kv-cache, go]
keywords: [InferScale, saltsystemslab, vLLM, KV injection]
related:
  - sources/arxiv-2607-27090-inferscale-kv-injection.md
  - concepts/inferscale-kv-injection-personalized-serving.md
  - concepts/ai-for-cybersecurity.md
  - concepts/agent-runtime-guardrails.md
  - concepts/toktier-exact-stateful-tokenization.md
  - sources/arxiv-2607-29678-toktier-stateful-tokenization.md
maturity: draft
created: 2026-07-30
updated: 2026-08-03
phase_0_verdict: "GO 2026-07-30 — BSD-3-Clause; ~1.4MB; github.com/saltsystemslab/InferScale"
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc"
---

## Relations

- @sources/arxiv-2607-27090-inferscale-kv-injection.md
- @concepts/inferscale-kv-injection-personalized-serving.md
- @concepts/ai-for-cybersecurity.md
- @concepts/agent-runtime-guardrails.md

**Local clone:** `raw-sources/repos/InferScale` (~1.4MB)
- @concepts/toktier-exact-stateful-tokenization.md
- @sources/arxiv-2607-29678-toktier-stateful-tokenization.md

## Narrative

### Phase-0 (2026-07-30): GO

| Gate | Status |
|------|--------|
| License | **PASS** — BSD-3-Clause |
| Size | **PASS** — ~1.4MB |
| Contents | GPU-native KV injection for personalized serving |
| Verdict | **GO** — lab study TTFT + harden injection path as privileged API |
