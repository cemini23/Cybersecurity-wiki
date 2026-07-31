---
title: PYDNS-Scanner — async DNS server discovery TUI
type: entity
tags: [dns-recon, async, tui, textual, mit, ethical-use-required]
keywords: [pydns-scanner, dns scan, dns server discovery, slipstream, slipnet, textual tui, isp mapping, dns hijack detection]
related:
  - concepts/dns-server-discovery-vs-subdomain-enumeration.md
  - concepts/network-security.md
  - concepts/osint-for-cybersecurity.md
  - concepts/responsible-disclosure.md
  - entities/tools/nmap.md
  - entities/pydns-scanner-xullexer.md
  - "@osint-wiki/entities/tools/pydns-scanner.md"
maturity: validated
created: 2026-05-13
updated: 2026-07-31
wire_status: policy_wired
wire_target: "CLAUDE.md#hands-on-rules-ethics--legality"
---

## Relations

- @concepts/dns-server-discovery-vs-subdomain-enumeration.md — methodology context; explains how this tool differs from subfinder/amass/dnsx
- @concepts/network-security.md — broader recon discipline
- @concepts/osint-for-cybersecurity.md — DNS-attribution and ISP-mapping intersect with OSINT
- @concepts/responsible-disclosure.md — ethics floor for DNS-server scanning
- @entities/tools/nmap.md — comparison anchor (different layer of DNS-relevant recon)
- @entities/pydns-scanner-xullexer.md — companion stub framing the offensive-recon / attack-surface-mapping angle of the same xullexer project
- @osint-wiki/entities/tools/pydns-scanner.md — sibling-wiki cross-routing stub

## Raw Concept

Phase-0 audit completed 2026-05-13 via `briefs/2026-05-13_pydns-scanner-adoption.md` (gitignored). Verdict: **CONDITIONAL-GO with MANDATORY ethical-use addendum** — adoption requires this page's `## Ethical use` section. Source repo: [github.com/xullexer/PYDNS-Scanner](https://github.com/xullexer/PYDNS-Scanner), MIT, 337 stars, solo maintainer, last commit 2026-03-30 (v2.0.5 hotfix).

## Narrative

PYDNS-Scanner is a **Textual-based asynchronous DNS-server discovery TUI** with three scan modes: Slipstream (SOCKS5 proxy testing), SlipNet (DNSTT/NoiseDNS tunnel compatibility checks), and DNS Scan (direct A/AAAA/MX/TXT/NS queries against discovered servers). [CONFIRMED]

**The critical conceptual distinction** — and the reason this entity page leads with it — is that PYDNS-Scanner discovers **DNS servers**, not subdomains. It is NOT a competitor or replacement for subfinder / amass / dnsx. Those are *subdomain enumeration* tools (given a target domain, find its hostnames). PYDNS-Scanner is a *DNS-server-inventory* tool (given an IP range, find which IPs answer DNS queries, with which record sets). The full distinction is documented in @concepts/dns-server-discovery-vs-subdomain-enumeration.md. [CONFIRMED]

This narrowness is both a strength (a sharp tool for a real niche) and a risk (users picking it up expecting subfinder-like behavior will misconfigure it).

### Niche use cases [CONFIRMED]

- **Internal network DNS inventory** — find all the DNS servers an enterprise actually runs (often more than the official "two corporate DNS servers" answer)
- **ISP / AS attribution research** — which DNS infrastructure belongs to which provider in a given IP block?
- **DNS hijack detection in transit** — comparing answers from servers across a path to detect interception
- **Proxy / tunnel infrastructure testing** — Slipstream and SlipNet modes are essentially "does my tunnel survive this DNS-server topology?"

### Cost + dependencies [CONFIRMED]

- pip install + Textual 0.47.0+
- Optional external binaries: Slipstream (SOCKS5 proxy testbench), SlipNet (DNSTT/NoiseDNS) — both have their own maintenance risk
- No vendor account, no API key

## Ethical use [MANDATORY — do not delete]

The upstream repo's README emphasizes performance and scale and **provides zero ethical-use, legal-compliance, or responsible-disclosure guidance**. This is a gap. This wiki page is the substitute documentation. [CONFIRMED via repo inspection 2026-05-13]

**Authorized-use boundaries:**

- **Internal networks you administer** — fine.
- **Owned infrastructure** (your home network, your cloud VPC) — fine.
- **Engagement-scoped third-party infrastructure with written authorization** — fine, within scope.
- **Bug-bounty programs that explicitly allow DNS-server enumeration** — read the policy first; most do not.
- **Arbitrary scanning of third-party DNS infrastructure** — **not authorized.** May violate the CFAA in the US, the Computer Misuse Act in the UK, equivalent statutes elsewhere; in many jurisdictions an aggressive scan against unowned DNS infrastructure is criminal regardless of intent.

**Responsible concurrency:**

- Default to ≤50 concurrent workers. The repo allows higher; the repo is wrong to make that easy.
- Never max out concurrency on third-party infrastructure even within scope. Aggressive scanning facilitates DDoS-by-accident.
- Rate-limit per-target ISP / AS — even within scope, you can melt a small DNS provider with a default-concurrency scan.

**Cross-reference:** @concepts/responsible-disclosure.md is the broader framework. If you find something exploitable via DNS recon, the disclosure path is the same as for any other vulnerability — not "publish first."

## Snippets

```bash
# install
pip install pydns-scanner
# DNS Scan mode against an internal /24 (lab example)
pydns-scanner --mode dns-scan --range 192.168.1.0/24 --workers 32 \
  --records A,AAAA,MX,NS
# Slipstream mode (proxy testbench, requires Slipstream binary)
pydns-scanner --mode slipstream --proxy-host 127.0.0.1 --proxy-port 1080
```

## Dead Ends

- **Picking PYDNS-Scanner expecting subfinder behavior** — see @concepts/dns-server-discovery-vs-subdomain-enumeration.md. Common newcomer error. [CONFIRMED]
- **Trusting the README's tuning defaults** — concurrency defaults are aggressive for shared infrastructure. [CONFIRMED]
- **Treating solo-maintainer + 4-month-old project as "abandoned"** — niche tool, niche maintenance cadence. Last commit cadence ≠ abandonment when the surface area is small. Re-evaluate at the 12-month-no-commit mark. [TENTATIVE 2026-05-13]
