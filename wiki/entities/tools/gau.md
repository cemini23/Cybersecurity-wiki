---
title: "gau (getallurls) — multi-provider known-URL discovery (MIT, Go)"
type: entity
tags: [entity, tool, recon, url-discovery, passive-recon, bug-bounty, attack-surface-mapping, mit, adopt, kali-linux]
keywords: [gau, getallurls, lc-gau, wayback-machine, alienvault-otx, common-crawl, passive-url-discovery, go-cli, kali]
related:
  - concepts/bug-bounty.md
  - concepts/web-pentest-methodology.md
  - concepts/osint-for-cybersecurity.md
  - entities/tools/cariddi.md
  - entities/tools/katana.md
  - "@osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md"
  - concepts/operator-lab-playbook.md
  - sources/penligent-bug-bounty-hunter-software-2026.md
maturity: draft
created: 2026-05-17
updated: 2026-08-02
cross-wiki-source: "@osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md"
wire_status: policy_wired
wire_target: "CLAUDE.md#hands-on-rules-ethics--legality"
---

## Relations
- @sources/penligent-bug-bounty-hunter-software-2026.md — 2026 bounty stack roundup
- @concepts/operator-lab-playbook.md — start-here operator lab hub (local AI → owned lab → product → bounty)

- @concepts/bug-bounty.md — known-URL harvesting is a core passive-recon step in bounty workflows
- @concepts/web-pentest-methodology.md — discovered historical URLs feed endpoint + parameter enumeration
- @concepts/osint-for-cybersecurity.md — OTX / Common Crawl / Wayback are open-data archives mined for attack-surface OSINT
- @entities/tools/cariddi.md — complementary tool: gau gathers known URLs passively, cariddi actively crawls and scans them for secrets
- @entities/tools/katana.md — complementary: gau is passive-archive discovery, katana is active crawling; commonly chained `gau | katana`
- @osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md — cross-routing source (OSINT 56-repo tool eval)

## Raw Concept

Cross-routed from the OSINT workspace 56-repo multi-wiki tool eval, 2026-05-17. The eval verdict is **Adopt** tier, cybersec primary fit; OSINT-wiki gets a secondary mention (data gathering from OTX / Common Crawl) and CCC-wiki a tertiary one (Go CLI pattern). Doc-level verdict — a Phase-0 clone audit is still owed before adoption on any production surface.

**Local adoption (2026-05-17)**: installed on the OSINT-workspace laptop via `go install github.com/lc/gau/v2/cmd/gau@latest` — binary at `~/go/bin/gau` (**v2.2.4**). Smoke-tested (returned known URLs for a test domain). The laptop is a curation/workflow surface, not a production surface, so this install does not pre-empt the Phase-0 gate owed before any server-side deployment. Note: `~/go/bin` is not on the laptop's default `PATH` — invoke by full path or add to `PATH`.

## Narrative

**gau** (short for *getallurls*) is a Go command-line tool that fetches the set of *known* URLs for a given domain by querying multiple public archives **simultaneously**: AlienVault's Open Threat Exchange (OTX), the Internet Archive's Wayback Machine, and Common Crawl. The result is a deduplicated list of historical and indexed URLs for a target — without ever sending a request to the target itself. [Source: https://github.com/lc/gau (retrieved 2026-05-17)]

This makes gau a **passive** URL-discovery / reconnaissance tool. It sits at the front of a recon pipeline: it answers "what URLs for this domain has the internet already seen?" before any active crawling begins. The output is typically piped into downstream tools — active crawlers (@entities/tools/katana.md), parameter-discovery tools, or secret scanners (@entities/tools/cariddi.md).

It is an established part of the recon tooling baseline and ships in / is readily installable on Kali Linux, alongside sibling ProjectDiscovery-era recon utilities. Its niche is breadth-of-archive: rather than relying on a single source (e.g. waybackurls, which queries only the Wayback Machine), gau fans out across three providers in one invocation.

**License: MIT.** Permissive — clears the Cemini IP-sale licensing bar with no copyleft or no-license contamination risk. [Source: @osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md]

### Cemini fit

- **Cybersec (primary)** — passive attack-surface mapping for pentest / bug-bounty recon.
- **OSINT-wiki (secondary)** — gau is also a generic open-data-archive harvester (OTX / Common Crawl), usable for non-security data gathering.
- **CCC-wiki (tertiary)** — a clean, single-purpose Go CLI; a reference pattern for compact Go command-line tooling.

## Snippets

> "gau ... fetches known URLs from AlienVault's Open Threat Exchange, the Wayback Machine, and Common Crawl for any given domain." [Source: https://github.com/lc/gau (retrieved 2026-05-17)]
