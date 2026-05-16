---
title: xullexer/PYDNS-Scanner — async DNS recon (Slipstream + SlipNet)
type: entity
tags: [tool, dns-recon, async, recon, attack-surface-mapping, mit, offensive-security]
keywords: [pydns-scanner, xullexer, async dns recon, slipstream, slipnet, subdomain enumeration, external recon]
related:
  - entities/tools/pydns-scanner.md
  - concepts/network-security.md
  - "@osint-wiki/sources/eval-github-repos-2026-05-13.md"
maturity: draft
created: 2026-05-13
updated: 2026-05-15
cross-wiki-source: @osint-wiki/sources/eval-github-repos-2026-05-13.md
---

# xullexer/PYDNS-Scanner — async DNS recon (Slipstream + SlipNet)

## Relations

- @entities/tools/pydns-scanner.md — primary entity page for the same xullexer project (DNS-server-discovery TUI framing + ethical-use addendum)
- @concepts/network-security.md — broader recon / attack-surface discipline
- @osint-wiki/sources/eval-github-repos-2026-05-13.md  (cross-wiki source)

## Raw Concept

Cross-wiki stub routed from `@osint-wiki/sources/eval-github-repos-2026-05-13.md` during ingest.
What prompted this page + which sources synthesize into it — fill in on next
ingest pass.

## Narrative

## Raw Concept

What prompted this page: Phase-0 eval (May 13 2026) in osint-wiki flagged `xullexer/PYDNS-Scanner` as ADOPT-tier. The OSINT-side use is shallow (entity-resolution / domain inventory); the **primary fit is cybersecurity** — async DNS recon for reconnaissance, attack-surface mapping, subdomain enumeration.

## Narrative

### Identity

- **Repo**: `xullexer/PYDNS-Scanner` (GitHub)
- **License**: **MIT** (verified during eval)
- **Language**: Python
- **Async**: yes — designed for high-throughput DNS resolution

### Two operational modes

1. **Slipstream** — single-host deep scan. Enumerates all DNS record types (A, AAAA, MX, TXT, CNAME, NS, SOA, SRV, PTR) for one target. Use-case: deep recon on a specific company / asset.
2. **SlipNet** — subnet sweep. Bulk DNS-resolution across an IP range or wordlist of hostnames. Use-case: attack-surface mapping, bulk subdomain discovery.

### Cybersecurity use-cases

- **External recon** (red-team / bug-bounty engagement opening) — enumerate target company's external DNS footprint without active scanning
- **Subdomain takeover hunting** — find dangling CNAMEs / NS records pointing to expired services
- **Mail-server enumeration** — MX + SPF/DKIM/DMARC discovery for phishing-infrastructure prep (defensive use: threat-intel)
- **Asset inventory** — defensive use: map your own org's DNS surface against expected baseline
- **CDN / WAF fingerprinting** — IP-block analysis of A-record responses

### Adoption posture (cybersecurity context)

**ADOPT** for any cybersec workflow that needs scriptable DNS recon. MIT license is clean. Async architecture handles bulk workloads without sync-tool latency.

### Operational discipline

1. **Rate-limit when scanning external targets** — even passive DNS recon can trigger detection
2. **Respect TOS** — DNS recon against systems you don't own or have authorization to test is legally distinct from "passive observation"
3. **Resolver choice matters** — use a dedicated resolver (Quad9, Cloudflare 1.1.1.1) rather than ISP default to avoid logged-by-default scenarios

### Comparable tools

- `dnsx` (projectdiscovery) — Go-based, similarly async
- `massdns` — C-based, faster but harder to script around
- `amass` (OWASP) — passive + active reconnaissance suite

PYDNS-Scanner fits where Python-scriptability matters more than raw throughput.

## Snippets

> "xullexer/PYDNS-Scanner: MIT, async DNS recon with Slipstream/SlipNet modes. ADOPT." [Source: @osint-wiki/sources/eval-github-repos-2026-05-13.md]

## Dead Ends

- **Scanning targets without authorization** — DNS recon is the gateway scenario for unauthorized testing claims. Stay inside scope.
- **Treating bulk DNS sweep as zero-footprint** — even passive queries get logged by recursive resolvers; choose resolver intentionally.
