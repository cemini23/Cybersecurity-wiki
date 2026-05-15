---
title: "Multi-Cloud Red Team"
type: concept
tags: [cloud, multi-cloud, red-team, aws, azure, gcp]
keywords: [multi-cloud, red team, AWS, Azure, GCP, cloud penetration testing]
related:
  - concepts/cloud-pentest.md
  - concepts/red-team-operations.md
  - sources/cloud-hacking-playbook.md
  - sources/multi-cloud-red-team-pt-1.md
maturity: draft
created: 2026-05-15
updated: 2026-05-15
---

## Raw Concept

Stub created during Redteam Kit 22-PDF ingest (2026-05-15). New source documents reference this topic area but no concept page existed. Will be filled in during subsequent deep-reads.

## Narrative

Red team operations spanning multiple cloud providers (AWS, Azure, GCP). Each provider has unique attack surfaces: AWS (IAM misconfigurations, S3 bucket exposure, Lambda backdoors, EC2 metadata service), Azure (Managed Identities, Key Vault, conditional access bypass, Azure AD Connect), GCP (service account impersonation, confidential VMs, organization policy bypass). Multi-cloud requires chaining techniques across providers. Reference: Joas A Santos' multi-cloud red team material.

## Relations

- @concepts/cloud-pentest.md
- @concepts/red-team-operations.md
- @sources/cloud-hacking-playbook.md
- @sources/multi-cloud-red-team-pt-1.md
