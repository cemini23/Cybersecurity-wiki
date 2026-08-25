---
title: "OOD — Supporting the Many Lives of Personal Data with Rebite (arXiv 2608.21289)"
type: source
tags: [source, arxiv, ood, hci, personal-informatics, food-journaling, llm]
keywords: [2608.21289, Rebite, goal-directed framing, personal informatics, food journaling, goal-at-view-time, UIST]
related:
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: skimmed
created: 2026-08-25
updated: 2026-08-25
phase_0_verdict: "OOD 2026-08-25 — HCI/personal-informatics (food journaling), not a cyber runtime. No CCC runtime. Steal (optional): goal-at-view-time vs capture-time metric framing — a data-modeling lesson, not cyber tradecraft."
wire_status: wont_wire
wire_target: "OOD — HCI; goal-framing contrast only"
---

## Relations

- @concepts/ai-for-cybersecurity.md — contrast only (LLM-in-the-loop data interpretation, no cyber runtime)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Supporting The Many Lives of Personal Data with Rebite: LLM-Powered Goal-Directed Framing in Food Journaling |
| Authors | Weijun Li, Daniel A. Epstein (UC Irvine) |
| arXiv | 2608.21289 (14 pp; UIST '26) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.21289-supporting-the-many-lives-of-personal-data-with.pdf` |
| Retrieved | 2026-08-25 |
| Read status | **skimmed** — OOD |
| Public code | none claimed for cyber adopt |

## Narrative

**Rebite** is a photo-based food journaling system that implements **goal-directed framing**: instead of fixing data meaning at capture time, the system keeps records unstructured and applies the *current* goal at **viewing** time — an LLM reads unstructured meal photos and produces goal-directed feedback. In a one-week deployment with 21 participants managing multiple dietary goals, reframing past meals under a changed goal exposed overlaps/conflicts and helped participants negotiate trade-offs. UIST '26 paper (Li & Epstein, UC Irvine).

**Why filed (OOD with an optional steal):** the **goal-at-view-time vs capture-time metrics** distinction is a data-modeling lesson — a record's meaning should be re-interpretable as context/goals change rather than locked at collection. For cyber runtime this is only a *contrast* (personal-informatics metrics are not attack/defense telemetry); no cyber adopt. **No personal health data handling implied; nothing to run.**

## Snippets

> Instead of fixing the meaning of data at capture time, the approach frames the collected data through the current goal and reframes it whenever the goal changes. [Source: arXiv 2608.21289 abstract]
