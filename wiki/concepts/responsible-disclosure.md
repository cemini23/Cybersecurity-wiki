---
title: Responsible Disclosure + CVE Process
type: concept
tags: [ethics, disclosure, cve]
keywords: [responsible disclosure, cvd, cve, mitre, vendor]
related:
  - concepts/bug-bounty.md
  - entities/people/joas-a-santos.md
  - entities/threat-actors/lockbit.md
  - sources/dicas-como-reportar-uma-falha.md
  - sources/how-to-report-a-vulnerability-and-generate-its-cve.md
  - entities/tools/pentest-ai-agents.md
  - entities/tools/pentest-ai.md
  - entities/tools/pydns-scanner.md
  - entities/tools/fuzzyai.md
  - entities/tools/cryptex-oss.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/llm-pentest-automation.md
  - concepts/dns-server-discovery-vs-subdomain-enumeration.md
  - entities/tools/defenseclaw.md
  - entities/tools/nvidia-skillspector.md
  - concepts/agent-runtime-guardrails.md
maturity: draft
created: 2026-05-12
updated: 2026-06-01
---

## Relations

- @concepts/bug-bounty.md
- @entities/people/joas-a-santos.md
- @entities/threat-actors/lockbit.md
- @sources/dicas-como-reportar-uma-falha.md
- @sources/how-to-report-a-vulnerability-and-generate-its-cve.md
- @entities/tools/pentest-ai-agents.md
- @entities/tools/pentest-ai.md
- @entities/tools/pydns-scanner.md
- @entities/tools/fuzzyai.md
- @entities/tools/cryptex-oss.md — adversarial prompt research ethics floor
- @concepts/llm-adversarial-fuzzing.md
- @concepts/llm-pentest-automation.md
- @concepts/dns-server-discovery-vs-subdomain-enumeration.md
- @entities/tools/defenseclaw.md
- @entities/tools/nvidia-skillspector.md — skill-poisoning findings follow vendor disclosure timelines
- @concepts/agent-runtime-guardrails.md — agent guardrail bypass findings use same CVD process

Anchored by How to report a vulnerability + Dicas como Reportar uma Falha.

## Narrative

Responsible Disclosure (now usually called Coordinated Vulnerability Disclosure, CVD) is the process of reporting a vulnerability to the vendor and giving them a reasonable window — typically 90 days, sometimes extended for complex fixes — before publishing details. CVE (Common Vulnerabilities and Exposures) IDs are assigned by MITRE or by CNAs (CVE Numbering Authorities, often the vendor itself). The corpus has a dedicated PDF on the CVE-request process. Industry norm: report → acknowledge → coordinated disclosure date → CVE assigned → vendor patches → researcher publishes write-up. Reporting hygiene matters — PoC clarity, impact scoring (CVSS), reproduction steps.
