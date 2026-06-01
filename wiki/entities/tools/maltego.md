---
title: Maltego
type: entity
tags: [osint, graph-analysis, investigation]
keywords: [maltego, transforms, osint, link analysis, paterva]
related:
  - concepts/osint-for-cybersecurity.md
  - entities/tools/netviz.md
  - entities/people/joas-a-santos.md
  - sources/maltego-introduction-creating-a-simple-local-transform-en.md
  - sources/maltego-introduction-creating-a-simple-local-transform-pt-br.md
maturity: draft
created: 2026-05-12
updated: 2026-06-01
---

## Relations

- @concepts/osint-for-cybersecurity.md
- @entities/tools/netviz.md — FOSS self-hosted graph alternative for recon briefings
- @entities/people/joas-a-santos.md
- @sources/maltego-introduction-creating-a-simple-local-transform-en.md
- @sources/maltego-introduction-creating-a-simple-local-transform-pt-br.md


## Raw Concept

Anchored by two parallel corpus PDFs (EN + PT-BR) on Maltego local-transform development.

## Narrative

Graph-based OSINT + link-analysis tool from Maltego Technologies (formerly Paterva). The canonical tool for *investigation* — visualizing relationships between people, organizations, domains, IPs, social-media accounts, file hashes, leaked credentials, and more. [CONFIRMED]

**Architecture:** entities (typed nodes) + transforms (functions that take an entity and return related entities). Transforms can be local (Python code on your machine) or hub-based (run on a vendor server, often paid).

**Editions:** Community Edition (free, capped at 12 results per transform), Professional, Classic, XL. Cross-link: @osint-wiki/entities/tools/swarmvault.md and broader OSINT tradecraft lives in the sister wiki.
