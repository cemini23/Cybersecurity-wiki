---
title: "musana/CF-Hero — Cloudflare origin-IP discovery"
type: entity
tags: [tool, recon, cloudflare, origin-ip, shodan, dns, go, defer]
keywords: [cf-hero, cloudflare bypass, origin ip, shodan, dns history, web recon]
related:
  - concepts/web-pentest-methodology.md
  - concepts/osint-for-cybersecurity.md
  - entities/tools/reconftw.md
maturity: draft
created: 2026-05-22
updated: 2026-07-31
cross-wiki-source: "@osint-wiki/sources/tool-eval-50urls-polymarket-kalshi-license-false-negative-2026-05-21.md"
phase_0_verdict: "Defer 2026-05-22 — gh api reports no SPDX license; verify LICENSE file before adoption."
wire_status: deferred
wire_target: "LICENSE/SPDX watch before adopt"
---

# musana/CF-Hero — Cloudflare origin-IP discovery

## Relations

- @concepts/web-pentest-methodology.md — origin-IP discovery supports WAF/CDN bypass during authorized web assessments
- @concepts/osint-for-cybersecurity.md — DNS + passive-intel correlation tradecraft
- @entities/tools/reconftw.md — complements automated recon pipelines (does not replace subdomain enumeration)

## Raw Concept

Routed from K55-2 OSINT-wiki brief (`briefs/2026-05-21_k55-2-cybersec-toolset-from-osint-tool-eval.md`, 2026-05-22). Go recon tool that discovers origin IP addresses of Cloudflare-protected sites via DNS history + Shodan-style hashing. ~2.4k stars. License not exposed via GitHub API — defer until manual LICENSE audit.

## Narrative

`musana/CF-Hero` is a **Go** reconnaissance tool focused on **Cloudflare-protected web applications**: it correlates multiple data sources (DNS history, Shodan fingerprinting) to surface likely **origin IP addresses** behind the CDN edge. Useful in authorized red-team / bug-bounty workflows where CDN unmasking is in scope and legal.

**Adoption gate**: `gh api repos/musana/CF-Hero --jq '.license.spdx_id'` returned no license (2026-05-22). Do not install from eval text alone — confirm repository LICENSE + maintenance before promoting beyond this stub.

**Ethical use**: Only against targets with explicit written authorization. Origin-IP discovery can enable direct-to-origin attacks that bypass Cloudflare WAF controls.
