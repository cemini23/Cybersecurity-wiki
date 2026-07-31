---
title: GEAR — evidence-aware RL against repetitive copying (arXiv 2607.19345)
type: source
tags: [source, arxiv, long-context, grounding, rl]
keywords: [2607.19345, GEAR, repetitive copying, evidence-aware reward]
related:
  - concepts/evidence-aware-long-context-grounding.md
  - concepts/coding-agent-context-pruning.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-07-22
updated: 2026-07-31
phase_0_verdict: "REFERENCE 2026-07-22 — method paper (Peking/Alibaba); no public code at ingest; steal GEAR reward shape"
wire_status: wont_wire
wire_target: "REFERENCE / steal-from — paper or methodology only"
---

**Briefs:** CCC handoff; `briefs/2026-07-22_k205-gear-evidence-grounding-prod.md`

## Relations

- @concepts/evidence-aware-long-context-grounding.md
- @concepts/coding-agent-context-pruning.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Copy Less, Ground More: Overcoming Repetitive Copying in Long-Context Reasoning via Evidence-Aware Reinforcement Learning |
| Authors | Lizhe Fang, Weizhou Shen, Tianyi Tang, Yisen Wang |
| arXiv | 2607.19345 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.19345-copy-less-ground-more-overcoming-repetitive-copy.pdf` |
| Retrieved | 2026-07-22 |
| Public code | None found |

## Narrative

Long-context reasoning often **repetitively copies** prompt text instead of solving. Root cause: insufficient grounding on key evidence vs distractors. **GEAR** reward = accuracy + grounding reward − distractor penalty. Up to **+4.6** avg points vs accuracy-only RL; larger gains at longer contexts; shorter thinking traces.

### Steal

1. Penalize distractor overlap in long-context agent rewards
2. Pair with context pruning (@concepts/coding-agent-context-pruning.md)

### Phase-0

| Verdict | **REFERENCE** |
