---
title: Wazuh
type: entity
tags: [soc, siem, host-ids, foss]
keywords: [wazuh, siem, soc, ossec fork, elastic, rule management]
related:
  - concepts/soc-operations.md
  - concepts/incident-response.md
  - concepts/purple-team-operations.md
  - sources/purple-team-lab-01-wazuh-and-win2016.md
  - entities/people/joas-a-santos.md
maturity: draft
created: 2026-05-12
updated: 2026-05-12
---

## Relations

- @concepts/soc-operations.md
- @concepts/incident-response.md
- @concepts/purple-team-operations.md
- @sources/purple-team-lab-01-wazuh-and-win2016.md
- @entities/people/joas-a-santos.md

## Raw Concept

Anchored by Purple Team Lab 01 — Wazuh and Win2016.pdf — the corpus's hands-on lab.

## Narrative

Open-source security-monitoring platform — host-based IDS + log management + vulnerability assessment + cloud-workload protection in one stack. A fork of OSSEC, since rewritten with a modern API, Elastic-based dashboard, and an active vendor offering managed support. [CONFIRMED]

**Architecture:** Wazuh agent (lightweight, on every endpoint) → Wazuh manager (aggregates, applies rules) → Wazuh indexer (formerly Open Distro Elasticsearch / OpenSearch) → Wazuh dashboard. Cited in the corpus as the centerpiece of a **low-cost SOC** stack (see also @concepts/soc-operations.md and the corpus's *Low Cost SOC Tools* PDFs).
