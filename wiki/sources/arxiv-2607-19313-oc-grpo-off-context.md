---
title: Off-Context GRPO — privileged guidance for hard RLVR (arXiv 2607.19313)
type: source
tags: [source, arxiv, rlvr, grpo, reasoning, meta]
keywords: [2607.19313, OC-GRPO, off-context, privileged information, RLVR]
related:
  - entities/tools/oc-grpo.md
  - concepts/off-context-privileged-rlvr.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-07-22
updated: 2026-07-31
phase_0_verdict: "GO 2026-07-22 — github.com/AgPriyank/OC-GRPO Apache-2.0 ~24MB shallow; Meta/Columbia reference impl"
wire_status: wont_wire
wire_target: "REFERENCE / steal-from — paper or methodology only"
---

**Briefs:** `briefs/2026-07-22_k204-oc-grpo-prod.md`

## Relations

- @entities/tools/oc-grpo.md
- @concepts/off-context-privileged-rlvr.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Off-Context GRPO: Learning to Reason on Hard Problems using Privileged Information |
| Authors | Priyank Agrawal et al. (Meta AI; Columbia) |
| arXiv | 2607.19313 |
| Code | [github.com/AgPriyank/OC-GRPO](https://github.com/AgPriyank/OC-GRPO) (Apache-2.0) |
| Local clone | `raw-sources/repos/OC-GRPO` (~24MB) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.19313-off-context-grpo-learning-to-reason-on-hard-prob.pdf` |
| Retrieved | 2026-07-22 |

## Narrative

When GRPO gets zero reward on hard problems (no correct samples), learning stalls. **OC-GRPO** generates guided (“off-context”) rollouts with privileged prefixes, then importance-corrects the update back to the unguided objective. **+3.9 pp absolute** (~13.8% relative) avg over vanilla GRPO on math reasoning benches at negligible extra cost.

### Steal (CCC / harness)

1. Use privileged guidance only at train time with importance correction — avoid train/test mismatch
2. Lab reference for hard-spot RLVR; not a security exploit tool

### Phase-0

| Gate | Status |
|------|--------|
| License | **PASS** — Apache-2.0 |
| Size | **PASS** — ~24MB |
| Verdict | **GO** lab |
