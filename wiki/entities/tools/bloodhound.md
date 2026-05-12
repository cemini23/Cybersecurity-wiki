---
title: BloodHound
type: entity
tags: [ad-recon, graph-analysis, foss]
keywords: [bloodhound, active directory, sharphound, neo4j, kingdom kerberos, specter ops]
related:
  - concepts/windows-pentest.md
  - concepts/red-team-operations.md
  - entities/people/joas-a-santos.md
maturity: draft
created: 2026-05-12
updated: 2026-05-12
---

## Relations

- @concepts/windows-pentest.md
- @concepts/red-team-operations.md
- @entities/people/joas-a-santos.md

## Raw Concept

Implicit across Active Directory pentest sources. Stub for AD-attack-path enumeration.

## Narrative

AD relationship-mapping tool from SpecterOps — uses graph theory (Neo4j) to surface attack paths within Active Directory. Indispensable for Windows enterprise pentest + red team. [CONFIRMED]

**Collector:** SharpHound (C# binary, or PowerShell equivalents) — enumerates AD users, groups, computers, sessions, ACLs. **Analyzer:** BloodHound (Electron app) loads the JSON output into Neo4j and presents pre-built Cypher queries like "Shortest path to Domain Admins from owned user." Newer release: **BloodHound CE** (containerized, web UI) and **BloodHound Enterprise** (commercial, continuous monitoring). See @concepts/windows-pentest.md.
