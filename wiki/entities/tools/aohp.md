---
title: AOHP — Android Open Harness Project
type: entity
tags: [tool, agent-harness, android, aosp, os-level, apache-2.0]
keywords: [aohp, aohp-os, android agent harness, agent-native os, tsinghua]
related:
  - sources/arxiv-2606-23449-aohp-os-level-agent-harness.md
  - concepts/agent-runtime-guardrails.md
  - concepts/agent-vm-sandboxing.md
  - concepts/mobile-pentest.md
  - concepts/ai-for-cybersecurity.md
  - concepts/mcp-security-posture.md
  - sources/arxiv-2606-21071-clawaudit-local-agent-runtime-audit.md
maturity: draft
created: 2026-06-27
updated: 2026-07-31
phase_0_verdict: "CONDITIONAL-GO 2026-06-27 — github.com/aohp-os/aohp Apache-2.0 LICENSE, ~93★, active 2026-06; AOSP fork — validate information-flow policies on lab device before agent prod use"
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-containment.mdc"
---

## Relations

- @sources/arxiv-2606-23449-aohp-os-level-agent-harness.md — paper provenance
- @concepts/agent-runtime-guardrails.md — OS-level guard complement

## Raw Concept

Phase-0 audit 2026-06-27 on arXiv:2606.23449 artifact. Repo: [aohp-os/aohp](https://github.com/aohp-os/aohp), **Apache-2.0**, ~93 stars, pushed 2026-06-27. AOSP-derived agent harness — not a hosted SaaS.

## Narrative

AOHP extends Android into an **agent-native harness**: agents as first-class OS actors with personalized service composition, efficient agent-facing interfaces, and **secure information-flow** tracking across tool/context boundaries.

### Phase-0 audit summary

| Check | Result |
|-------|--------|
| License | Apache-2.0 `[CONFIRMED]` |
| Maturity | Early OSS (~93★); active development |
| Primary failure mode | AOSP fork — policy misconfiguration could over/under-constrain agent capabilities |
| vs existing stack | Complements Docker sandbox (@concepts/agent-vm-sandboxing.md), not replacement |

**Verdict: CONDITIONAL-GO** — adopt for **lab/agent-native OS research** and mobile agent security eval; re-audit on major AOSP merge before any production agent phone profile.

### Preliminary paper claims

+21.12% task completion, −51.55% token cost vs conventional Android agent execution on overlapping benchmarks.

See `briefs/2026-06-27_aohp-agent-native-os-harness-handoff.md` for lab checklist (dedicated device, information-flow mapping, AOSP merge re-audit).

## Snippets

[Source: arxiv-2606.23449 + github.com/aohp-os/aohp]
