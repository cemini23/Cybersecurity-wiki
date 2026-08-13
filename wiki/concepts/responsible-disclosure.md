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
  - concepts/neuro-symbolic-auditable-reasoning.md
  - sources/arxiv-neurolog-auditable-vuln-discovery-2606.00669-2026-06-05.md
  - concepts/exceptional-access-risk-quantification.md
  - sources/arxiv-2606-18673-prompt-leaking-attacks-area.md
  - concepts/system-prompt-leakage.md
  - sources/arxiv-2606-24166-toxsearch-s-distributed-toxicity-search.md
  - concepts/llm-biosecurity-red-teaming.md
  - sources/arxiv-2607-18056-intern-biobreaker-biosecurity.md
  - concepts/ethics-autonomous-offensive-ai-agents.md
  - sources/arxiv-ethics-autonomous-offensive-ai-2607.20255.md
  - concepts/pre-release-product-pentest.md
  - concepts/owned-target-whitehat-lab.md
  - concepts/operator-lab-playbook.md
  - entities/tools/cyberstrike.md
  - concepts/ai-pentest-harness-landscape.md
  - entities/tools/strix.md
  - entities/tools/strix-omlx.md
  - sources/arxiv-2608-11337-association-privacy-wireless-formal.md
  - concepts/association-inference-attack-wireless.md
maturity: draft
created: 2026-05-12
updated: 2026-08-13
---

## Relations
- @entities/tools/strix-omlx.md
- @entities/tools/strix.md — Strix AI pentest harness (Apache-2.0 CONDITIONAL-GO Phase-0)
- @concepts/ai-pentest-harness-landscape.md — AI pentest harness landscape; agent findings still follow CVD, not public dump
- @entities/tools/cyberstrike.md — AGPL AI offensive harness — CONDITIONAL-GO lab/VM only (Phase-0 2026-08-02)
- @concepts/operator-lab-playbook.md — start-here operator lab hub (local AI → owned lab → product → bounty)

- @concepts/owned-target-whitehat-lab.md — lab practice floor; upstream bugs found in lab leave via responsible disclosure, not drive-by dumps
- @sources/arxiv-ethics-autonomous-offensive-ai-2607.20255.md
- @concepts/ethics-autonomous-offensive-ai-agents.md
- @sources/arxiv-2607-18056-intern-biobreaker-biosecurity.md
- @concepts/llm-biosecurity-red-teaming.md
- @concepts/bug-bounty.md
- @concepts/pre-release-product-pentest.md — third-party deps found in pre-release product tests use CVD, not public dump
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

- @sources/arxiv-2608-11337-association-privacy-wireless-formal.md
- @concepts/association-inference-attack-wireless.md
Anchored by How to report a vulnerability + Dicas como Reportar uma Falha.

## Narrative

Responsible Disclosure (now usually called Coordinated Vulnerability Disclosure, CVD) is the process of reporting a vulnerability to the vendor and giving them a reasonable window — typically 90 days, sometimes extended for complex fixes — before publishing details. CVE (Common Vulnerabilities and Exposures) IDs are assigned by MITRE or by CNAs (CVE Numbering Authorities, often the vendor itself). The corpus has a dedicated PDF on the CVE-request process. Industry norm: report → acknowledge → coordinated disclosure date → CVE assigned → vendor patches → researcher publishes write-up. Reporting hygiene matters — PoC clarity, impact scoring (CVSS), reproduction steps.
