---
title: Bug Bounty
type: concept
tags: [responsible-disclosure, vrp, platform]
keywords: [bug bounty, hackerone, bugcrowd, intigriti, vrp, responsible disclosure]
related:
  - concepts/web-pentest-methodology.md
  - concepts/responsible-disclosure.md
  - entities/tools/burp-suite.md
  - sources/bug-bounty-career.md
  - sources/bug-bounty-how-to-start.md
  - sources/complete-bug-bounty-cheat-sheet.md
  - sources/how-to-report-a-vulnerability-and-generate-its-cve.md
  - sources/dicas-como-reportar-uma-falha.md
  - entities/people/joas-a-santos.md
  - entities/programming-languages/javascript.md
  - entities/certifications/ewpt.md
  - entities/certifications/oswe.md
  - entities/tools/pentest-ai-agents.md
  - concepts/llm-pentest-automation.md
  - entities/tools/raptor.md
  - entities/tools/src-hunter-skill.md
  - entities/tools/reconftw.md
  - entities/tools/bug-bounty-agents.md
  - entities/tools/cariddi.md
  - entities/tools/osmedeus.md
  - entities/tools/gau.md
  - entities/tools/katana.md
  - concepts/operator-lab-playbook.md
  - concepts/local-abliterated-llm-pentest-stack.md
  - concepts/owned-target-whitehat-lab.md
  - concepts/pre-release-product-pentest.md
  - entities/tools/cyberstrike.md
  - concepts/ai-pentest-harness-landscape.md
  - sources/penligent-bug-bounty-hunter-software-2026.md
  - sources/rizvi-automating-bug-bounty-recon-2026.md
  - entities/tools/strix.md
  - entities/tools/hacktools.md
maturity: draft
created: 2026-05-12
updated: 2026-08-03
---

## Relations

- @entities/tools/hacktools.md — K220 browser cheatsheet (license gate)
- @entities/tools/strix.md — Strix AI pentest harness (Apache-2.0 CONDITIONAL-GO Phase-0)
- @sources/rizvi-automating-bug-bounty-recon-2026.md — anti-noise recon automation (Rizvi 2026)
- @sources/penligent-bug-bounty-hunter-software-2026.md — 2026 bounty stack roundup (Penligent)
- @concepts/ai-pentest-harness-landscape.md — AI pentest harness landscape; bounty use only under program rules + authorization
- @entities/tools/cyberstrike.md — AGPL AI offensive harness — CONDITIONAL-GO lab/VM only (Phase-0 2026-08-02)
- @concepts/web-pentest-methodology.md
- @concepts/responsible-disclosure.md
- @concepts/operator-lab-playbook.md — operator-facing lab playbook that maps bounty-style recon + exploit loops onto owned lab surfaces
- @concepts/local-abliterated-llm-pentest-stack.md — local abliterated LLM stack for offline recon triage, report drafting, and low-risk Tier-1 assist without cloud egress
- @concepts/owned-target-whitehat-lab.md — owned / whitehat lab targets as the authorization-safe practice ground before public program work
- @concepts/pre-release-product-pentest.md — separate lane: owned pre-release product test vs public bounty programs
- @entities/tools/burp-suite.md
- @sources/bug-bounty-career.md
- @sources/bug-bounty-how-to-start.md
- @sources/complete-bug-bounty-cheat-sheet.md
- @sources/how-to-report-a-vulnerability-and-generate-its-cve.md
- @sources/dicas-como-reportar-uma-falha.md
- @entities/people/joas-a-santos.md
- @entities/programming-languages/javascript.md
- @entities/certifications/ewpt.md
- @entities/certifications/oswe.md
- @entities/tools/pentest-ai-agents.md
- @concepts/llm-pentest-automation.md
- @entities/tools/bug-bounty-agents.md — 43-persona offensive-security agent library for bug-bounty workflows
- @entities/tools/cariddi.md — domain crawler hunting exposed secrets, API keys, and sensitive endpoints
- @entities/tools/osmedeus.md — orchestration engine; declarative YAML workflows automate the recon pipeline bug-bounty hunters rebuild per target
- @entities/tools/gau.md — passive known-URL discovery (Wayback / OTX / Common Crawl); front of the recon pipeline
- @entities/tools/katana.md — active web crawler with headless mode; expands the testable attack surface in SPA targets
- @entities/tools/reconftw.md — apex deterministic recon automation (subdomains / web / vulns / OSINT / Axiom fleet); mid-pipeline bulk recon after passive URL seeds

## Raw Concept

Five corpus PDFs anchor.

## Narrative

Bug bounty = formalized public disclosure programs that pay researchers for valid security findings. Major platforms: HackerOne, Bugcrowd, Intigriti, YesWeHack, Synack (invite-only). Career-vs-job framing: bounty income is rewarding but volatile; most full-time bounty hunters specialize (e.g., subdomain-takeover scaling, JS file mining, IDOR-heavy workflows). The corpus's *Complete Bug Bounty Cheat Sheet.pdf* + *How to report a vulnerability and generate its CVE.pdf* anchor the reporting-side discipline.

### Beefy-box ROI

A "beefy box" (multi-core CPU, 32–64 GB+ RAM, fast NVMe, optional GPU, generous bandwidth) pays off when your bottleneck is **local parallelism and large artifact sets**, not raw scan cleverness. High-ROI uses: parallel passive/active recon jobs, large URL/JS corpora in memory, hashcat/John offline cracking against *authorized* wordlists, and multi-browser headless crawl sessions. Low-ROI uses: paying for silicon to re-run the same public Nuclei templates every other hunter already ran overnight — that is cloud-burn without differentiation. Prefer a mid-tier always-on box plus short-lived Axiom-class fleets (@entities/tools/reconftw.md `axiom.sh` pattern) when you need temporary horizontal scale; keep the beefy box as the **curation surface** (dedupe, triage, Burp, report drafting). Cap spend against expected bounty velocity: if monthly infra exceeds realistic payout from your active programs, you are buying a hobby lab, not a production pipeline. Pair hardware choices with @concepts/operator-lab-playbook.md and keep practice on @concepts/owned-target-whitehat-lab.md before aiming the same firehose at live VRP scope.

### 2026 stack that still matters

Consensus “belongs in the bag” tools (roles, not religion) [Source: Penligent “Bug Bounty Hunter Software in 2026” (retrieved 2026-08-02)] [TENTATIVE]:

| Layer | Tools (wiki-linked where present) | Job |
|-------|-----------------------------------|-----|
| Manual proof | @entities/tools/burp-suite.md | Session state, replay, impact proof |
| Passive / deep recon | Subfinder, Amass, @entities/tools/gau.md | Context without loud active noise |
| Live surface | httpx, Naabu | Hosts → typed live surface |
| Crawl | @entities/tools/katana.md (+ browser) | JS/SPA routes archives miss |
| Templates | Nuclei (staged) | Known exposures / fingerprints |
| Directed fuzz | ffuf + SecLists | Hypothesis-driven content discovery |
| Orchestration | @entities/tools/reconftw.md **or** @entities/tools/osmedeus.md | One primary orchestrator per engagement |

### Recon pipeline

Default public-program recon chain (passive → active → orchestrated bulk → human):

1. **Passive known URLs** — @entities/tools/gau.md (Wayback / OTX / Common Crawl). Zero (or near-zero) contact with the live target; answers "what has the internet already seen?" Historical URL harvest is **not** interchangeable with active crawl (waymore/gau class ≠ Katana).
2. **Active crawl expansion** — seed @entities/tools/katana.md (HTTP + headless) from gau output; pull SPA-rendered routes, JS paths, and API endpoints a pure archive pass will miss. Optional secret/API-key pass with @entities/tools/cariddi.md on the expanded host set.
3. **Bulk recon orchestration** — either @entities/tools/reconftw.md (modular Bash: subdomains / web / vulns / OSINT / Axiom distribution) **or** @entities/tools/osmedeus.md (declarative YAML workflows, master-worker). Pick one primary orchestrator per engagement to avoid double-hitting the same surface and self-generating rate-limit noise.
4. **Manual differentiation** — @entities/tools/burp-suite.md, JS mining, auth flows, business logic, IDOR chains. Automation maps surface; payout lives in human judgment after the map is built.

Only run active steps inside program-allowed assets and rate limits. Lab the pipeline first on owned targets (@concepts/owned-target-whitehat-lab.md); optional local LLM assist for triage/report drafts lives under @concepts/local-abliterated-llm-pentest-stack.md without replacing scope gates.

### Anti-noise ROI (where automation actually pays)

2026 community consensus: **generic full-surface Nuclei is a noise factory**. Higher ROI pattern [Source: R.H Rizvi, Medium, 2026 (retrieved 2026-08-02)] [TENTATIVE]:

1. Enumerate → **tech-detect** (httpx / Wappalyzer-class fingerprints).
2. Bucket hosts by technology; run **staged** Nuclei profiles (critical/high tags first), not “all templates.”
3. Promote confirmed manual findings into **custom templates** — differentiation lives here.
4. Keep scanners **one-at-a-time** on the beefy box if RAM is the bottleneck (avoid OOM thrash from parallel nuclei+dalfox+nmap).
5. Use LLM **Tier-1** for triage/report clustering; never unscoped Tier-2 mass scan (@concepts/llm-pentest-automation.md, @concepts/ai-pentest-harness-landscape.md).

### Program selection + scope hygiene

Program selection is where most "automation ROI" is won or lost. Prefer programs with: clear asset inventory (wildcards vs exact hosts), published out-of-scope list, reasonable response SLAs, and a duplicate/N/A history you can study from disclosed reports. Avoid megaprograms as a first full-auto target — noise, duplicate density, and aggressive WAF/CDN make unattended scanners expensive and low-yield.

Scope hygiene (non-negotiable):

- Resolve **in-scope hosts / paths / mobile apps / APIs** before any active tool runs; treat wildcards as "enumerate, then re-check each child against OOS rules."
- Read **out-of-scope** and **known-issue / previously reported** lists; do not re-submit generic XSS on a marketing subdomain that 200 hunters already filed.
- Rate-limit and identify traffic per program rules; parallel fleets without spend/ceilings are how you get banned, not paid.
- Authorization boundary differs by surface: public VRP ≠ private @concepts/pre-release-product-pentest.md engagement ≠ owned lab. Do not port unscoped Tier-2 firepower across those boundaries.

**Where LLM / agent automation helps vs hurts** (per @concepts/llm-pentest-automation.md Tier 1 / Tier 2):

| Layer | Role in bounty work | Helps | Hurts (duplicates / noise) |
|---|---|---|---|
| **Tier 1** (advisory-only) | Plan recon order, score draft CVSS, rewrite clear reports, cluster similar endpoints | Faster triage + higher-quality write-ups; no live traffic | Inflated severity language if human-review is skipped; still wastes triage if you "plan" attacks already known-OOS |
| **Tier 2** (execution-capable) | Invoke recon/scanners against declared `allowed_targets` | Consistent pipeline runs when scope is pinned and rate-limited | **Duplicate factories**: unscoped mass Nuclei / crawl loops re-find the same public issues, burn program goodwill, and flood *your* queue with self-noise |

Rule of thumb: use Tier 1 liberally on *after-recon* artifacts; gate every Tier 2 call on program scope + asset allowlist (same contract as `requires_scope: true` in @concepts/llm-pentest-automation.md). Automation that cannot state *which in-scope asset* it is about to touch is not ready for public programs.
