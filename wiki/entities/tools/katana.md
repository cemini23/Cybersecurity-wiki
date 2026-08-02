---
title: "katana — scriptable web crawler with headless-browser mode (MIT, Go)"
type: entity
tags: [entity, tool, recon, web-crawler, headless-browser, endpoint-discovery, bug-bounty, projectdiscovery, mit, adopt]
keywords: [katana, projectdiscovery, web-crawler, headless-crawling, spa-crawling, js-endpoint-extraction, go-api, newcrawleroptions, classifypage]
related:
  - concepts/web-pentest-methodology.md
  - concepts/bug-bounty.md
  - entities/tools/cariddi.md
  - entities/tools/gau.md
  - entities/tools/osmedeus.md
  - "@osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md"
  - concepts/operator-lab-playbook.md
maturity: draft
created: 2026-05-17
updated: 2026-08-02
cross-wiki-source: "@osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md"
wire_status: policy_wired
wire_target: "CLAUDE.md#hands-on-rules-ethics--legality"
---

## Relations

- @concepts/operator-lab-playbook.md — start-here operator lab hub (local AI → owned lab → product → bounty)

- @concepts/web-pentest-methodology.md — crawling for URLs / JS paths / API endpoints is a core web-app recon step
- @concepts/bug-bounty.md — deep SPA crawling expands the testable attack surface in bounty engagements
- @entities/tools/cariddi.md — sibling Go crawler; the cariddi audit explicitly recommends katana to fill cariddi's headless-browser (G5) gap
- @entities/tools/gau.md — complementary: gau supplies passive known-URL seeds, katana actively crawls from them
- @entities/tools/osmedeus.md — orchestration engine that can wrap crawlers like katana into recon workflows
- @osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md — cross-routing source (OSINT 56-repo tool eval)

## Raw Concept

Cross-routed from the OSINT workspace 56-repo multi-wiki tool eval, 2026-05-17. The eval verdict is **Adopt** tier, cybersec primary fit; OSINT-wiki gets a secondary mention (automated deep-crawling of unstructured data). Doc-level verdict — a Phase-0 clone audit is still owed before adoption on any production surface.

**Local adoption (2026-05-17)**: installed on the OSINT-workspace laptop via `go install github.com/projectdiscovery/katana/cmd/katana@latest` — binary at `~/go/bin/katana` (**v1.6.1**). Smoke-tested (crawled a test domain, returned URLs). The laptop is a curation/workflow surface, not a production surface, so this install does not pre-empt the Phase-0 gate owed before any server-side deployment. Note: `~/go/bin` is not on the laptop's default `PATH` — invoke by full path or add to `PATH`.

## Narrative

**katana** is a scriptable web crawler from ProjectDiscovery. It operates in two modes: standard HTTP crawling, and a **headless-browser** mode that executes JavaScript via a real browser engine. The headless mode is the differentiator — it lets katana see the URLs, JS paths, and API endpoints that modern single-page-application (SPA) frameworks generate dynamically at runtime, which a pure-HTTP crawler never renders. [Source: https://github.com/projectdiscovery/katana (retrieved 2026-05-17)]

Beyond the CLI, katana exposes a **Go API** for programmatic integration — entry points such as `NewCrawlerOptions` (constructing a configured crawler) and `ClassifyPage` (categorizing crawled pages). This makes it embeddable inside larger Go-based recon orchestration rather than only invokable as a shell tool.

The eval notes roughly **1,567 commits** and enterprise-grade lifecycle controls (scope rules, depth limits, rate controls, field filtering) — a mature, actively maintained project rather than a one-off script. [Source: @osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md]

It pairs naturally with passive discovery: a common pattern is to seed katana with the known-URL output of @entities/tools/gau.md, then let katana actively crawl and expand from those seeds.

**License: MIT.** Permissive — clears the Cemini IP-sale licensing bar with no copyleft or no-license contamination risk.

### Cemini fit

- **Cybersec (primary)** — active web crawling for endpoint / JS-path / API discovery in web-app pentest and bug-bounty recon.
- **OSINT-wiki (secondary)** — its headless mode makes it a general automated deep-crawler for JavaScript-heavy, unstructured web data.

## Snippets

> "katana ... a next-generation crawling and spidering framework ... standard and headless crawling, supports JavaScript parsing / crawling." [Source: https://github.com/projectdiscovery/katana (retrieved 2026-05-17)]

> Programmatic integration is via the Go API — `NewCrawlerOptions` and `ClassifyPage` among the exposed entry points. [Source: @osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md]
