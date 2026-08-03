# Cybersecurity Research Wiki — Schema

This file is the **schema**: it tells you (the LLM) how to operate this workspace. Everything else is either a raw source, a wiki page, or a meta file. Read this on every session start. Active workstreams + open decisions live in `ROADMAP.md`, not here.

## Purpose

Local knowledge hub for **cybersecurity research, training, and offensive/defensive operations** — scoped to:

1. **Offensive security** (pentesters, red teamers, bug-bounty hunters) who need ingestable references for engagements, certification prep, and tool selection. Running case: a working pentester building toward CRTO / OSCP / eCPTX while documenting tradecraft per-target-class (web, Windows AD, cloud, mobile, IoT/OT).
2. **Defensive security** (SOC analysts, incident responders, threat hunters, blue teamers) who need detection-engineering references, low-cost tooling stacks, and adversary-emulation playbooks to build labs against.
3. **Career + education** (students, career switchers, parents of kids, recruiters) who need orientation on the cybersecurity job-family map, certification paths, and age-appropriate safety material (cyberbullying, child internet safety, school-attack survival).

The wiki is a librarian that **manages, curates, and applies** that knowledge:

- **Manage** — inventory raw sources (PDFs, slide decks, video transcripts, repo snapshots, blog posts); track what's been read, extracted, and applied
- **Curate** — pull relevant fragments out of raw sources; structure them as interlinked wiki pages on attack techniques, defense controls, tools, frameworks, certifications, and threat actors
- **Apply** — route findings to a real workflow:
  - **claude.ai / Claude Desktop** — context for engagement reports, exam study, threat-model write-ups, training material
  - **Direct hands-on use** — paste a brief into a pentest report, a SOC runbook, a CTF write-up, or a kid-safety conversation

This is a laptop-only workspace. No remote servers, no team distribution. Everything lives on this MacBook.

## Architecture — three layers

1. **Raw sources** — immutable. Canonical archive: `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/` via OSINT `archive_raw_to_egress.sh`.
   - PDFs (e-books, vendor whitepapers, conference talks — much of the seed corpus is from [Joas A Santos](wiki/entities/people/joas-a-santos.md), a prolific Brazilian cybersecurity educator)
   - Slide decks from conference talks (RoadSec, TDC, Red Team Village, etc.)
   - GitHub repos (cloned snapshots of relevant FOSS tools — Caldera, Metasploit, Cobalt-Strike-detections, Wazuh rule packs, etc.)
   - Video transcripts saved as `.md`
   - **Drop pattern**: `research to be indexed/` → ingest → archive to egress-fi (local copy removed on success)

2. **The wiki** — LLM-written, human-read. Lives in `wiki/`. Structured pages on certifications, tools, frameworks, threat actors, platforms, people, vendors, programming languages, and concepts.

3. **The schema** — this file.

Staging/output lives outside the wiki:
- `briefs/` — one-off deliverables (gitignored): engagement-prep briefings, SOC-runbook drafts, certification cram sheets, kid-safety conversation scripts
- `research to be indexed/` — transient drop zone for new raw sources (gitignored)
- `LESSONS.md` — meta-lessons about *how we work* (distinct from `wiki/log.md`)
- `hot.md` — ephemeral session-state cache (gitignored)
- `ROADMAP.md` — active workstreams + open decisions (tracked)

## Folder layout

```
Cybersecurity-wiki/                  # repo root
  CLAUDE.md                         # this file — the schema
  LESSONS.md                        # meta-lessons (how we work)
  ROADMAP.md                        # active workstreams + decisions + done log
  hot.md                            # session-state cache (gitignored)
  .env.example                      # env-var template (commit this)
  .env                              # actual keys (gitignored — never commit)
  claude_desktop_config.json.example  # Claude Desktop MCP config template (commit this)
  research to be indexed/           # transient drop zone (gitignored)
  raw-sources/                      # archived raw source corpus (gitignored)
  briefs/                           # staging for distribution → claude.ai or hands-on use (gitignored)
  wiki/                             # canonical wiki
    index.md                        # content-oriented catalog of all wiki pages
    log.md                          # append-only chronological operations log
    sources/                        # one page per ingested source
    entities/
      certifications/               # OSCP, CRTO, eCPPT, CEH, CompTIA Security+/PenTest+, etc.
      tools/                        # Cobalt Strike, Metasploit, Burp Suite, Caldera, Maltego, Wazuh, etc.
      frameworks/                   # MITRE ATT&CK, Cyber Kill Chain, OWASP WSTG, Zero Trust, NIST CSF
      threat-actors/                # APT28, APT29, named groups + TTP profiles
      platforms/                    # HackTheBox, VulnHub, TryHackMe, PortSwigger Web Academy
      people/                       # researchers + educators (Joas A Santos, etc.)
      vendors/                      # Offensive Security, INE/eLearnSecurity, CompTIA, EC-Council, ZeroPoint Security
      programming-languages/        # Python, C, C++, C#, PowerShell, JavaScript — security-focused usage
    concepts/                       # red-team-operations, adversary-emulation, av-edr-bypass, buffer-overflow, etc.
  scripts/                          # wiki_lint.py, wiki_gap_detect.py, preingest_check.py
  prompts/                          # reusable prompt templates
  .claude/                          # Claude Code per-project state (gitignored)
```

Pages can be nested inside `entities/` when `Domain > Topic > Subtopic` hierarchy is warranted (e.g. `entities/certifications/oscp.md`, `entities/tools/cobalt-strike.md`, `entities/threat-actors/apt28.md`). `concepts/` and `sources/` are flat by convention.

## Wiki page format

Every wiki page is a markdown file with YAML frontmatter + structured sections.

### Frontmatter (required)

```yaml
---
title: Human-readable page title
type: source | entity | concept | brief
tags: [coarse, category, labels]
keywords: [fine, grained, search, terms]
related:
  - entities/certifications/oscp.md
  - concepts/red-team-operations.md
maturity: draft | validated | core
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

- `type` determines section template
- `maturity`: `draft` → `validated` (cross-referenced + tested in real engagement / exam / lab) → `core` (battle-tested source of truth). Move up (occasionally down) as evidence warrants
- `related[]` is **bidirectional**: if A lists B, B must list A
- `created` / `updated`: ISO dates; bump `updated` on meaningful body changes

### Body sections (in order, include only what's relevant)

- `## Relations` — inline list of `@path/to/page.md` annotations matching `related:` frontmatter
- `## Raw Concept` — provenance. For source pages: title/author/retrieval-date/filename/URL. For entity/concept pages: what prompted this page, which sources synthesized into it
- `## Narrative` — the body. Prose, tables, structured data, examples. Concept pages: synthesized understanding, neutral, well-sourced — opinion belongs in briefs, not concept pages
- `## Snippets` — verbatim quotes / commands / payloads / structured data / screenshots-as-text with citations
- `## Dead Ends` (optional) — what was tried + why it failed + what was learned (e.g. exploitation techniques that didn't survive a defender update; certifications that retired)

### Page-type quick reference

- **Source page** (`wiki/sources/<slug>.md`) — one per ingested source. Raw Concept fields: title / author / type / location / retrieved / pages / read-status (skimmed | read | deep-read | unread-stub).
- **Entity page** (`wiki/entities/<category>/<slug>.md`) — categories: certifications, tools, frameworks, threat-actors, platforms, people, vendors, programming-languages. Raw Concept: what prompted the page + which sources synthesize into it.
- **Concept page** (`wiki/concepts/<slug>.md`) — examples: red-team-operations, adversary-emulation, av-edr-bypass, buffer-overflow, osint-for-pentest, web-pentest-methodology, soc-operations, threat-hunting, incident-response, cyber-for-kids. Raw Concept: the question or topic the page answers.
- **Brief page** (`briefs/<YYYY-MM-DD>_<slug>.md`) — deliverable. Body sections: `## Target` (claude.ai | Claude Desktop | hands-on) / `## Summary` / `## Body` / `## Sources`. Examples: engagement-prep briefing, OSCP cram sheet, SOC-runbook draft, kid-safety talk script.

## Cross-link + citation conventions

**Cross-links** (`@path` syntax):
- Use `@path/to/page.md` inline (no leading slash, relative to `wiki/`)
- Bidirectional: A → B and B → A both required
- Stub pages preferred over orphan mentions: if a topic comes up without a page, create a stub

**Citation tags**:
- Source page: `[Source: filename.pdf p.5]`
- External URL: `[Source: https://... (retrieved YYYY-MM-DD)]`
- GitHub repo: `[Source: github.com/owner/repo @ <sha>]`
- Vendor doc / first-party: `[Source: offensive-security.com/... (retrieved YYYY-MM-DD)]`
- Multiple: `[Sources: filename.pdf p.5, attack.mitre.org/techniques/T1055/]`

**Claim confidence tags**:
- `[CONFIRMED]` — ≥2 independent sources, OR personally tested on a lab / engagement
- `[TENTATIVE]` — single source or untested
- `[NEEDS VERIFICATION YYYY-MM-DD]` — plausible but untested. **Always include the date** so staleness can be flagged. Especially important for technique pages — defenders patch, exploits rot, payloads get signatured.
- `[RETRACTED]` — previously believed, now disproven (e.g. an exploit blocked by a vendor patch). Keep in place with a note; don't delete

## Related Wikis

When a query needs data from another wiki, reference it using the `@wiki-alias/path/to/page.md` syntax. The LLM resolves these by reading the other wiki's files directly.

Paths below are relative to this CLAUDE.md file's directory. Resolve `../` against this file's location to get the absolute path.

| Alias | Path | Description |
|-------|------|-------------|
| `cybersecurity-wiki` | `wiki/` | Cybersecurity research — offensive security, defensive operations, certifications, threat actors, education |
| `osint-wiki` | `../../OSINT WORKSPACE/wiki/` | Financial research, quant finance, prediction markets, CeminiSuite, RL for trading. Shared territory: OSINT tradecraft + technique tooling (Maltego, Shodan, OSINT for pentest) |
| `gambling-wiki` | `../Gambling wiki/wiki/` | Sports betting, casino, poker, DFS. Shared territory: fraud/social-engineering in gambling apps when in pentest scope |
| `image-gen-wiki` | `../Image gen/wiki/` | Uncensored image generation, model cataloging, ComfyUI, LoRA, persona/character ops. Shared territory: deepfakes + adversarial-image attacks (when those surfaces appear in pentest scope) |
| `seo-wiki` | `../SEO:GEO B&M Business/wiki/` | Local SEO, GBP optimization, GEO/AEO, web design, social media, creator marketing. Shared territory: web-app security for client sites + spam-policy / fake-review attack surfaces |
| `3d-printing-wiki` | `../3D printing/wiki/` | FDM/FFF printing, Bambu, materials, slicers, print farms, store ops. Shared territory: hardware hacking when printed jigs / RFID enclosures / lock-pick aids overlap with physical-pentest tooling |
| `ccc-wiki` | `../Cemini claude code CCC/wiki/` | Cemini Claude Code meta-wiki — workflow, MCP, hooks, skills, slash commands. Shared territory: Tier-1/Tier-2 agent model (`@ccc-wiki/entities/patterns/tier1-tier2-agent-model.md` adapted from this wiki's `concepts/llm-pentest-automation.md`), cua VM-isolation entity (`@ccc-wiki/entities/tools/cua.md`), claude-code-ultimate-guide (`@ccc-wiki/entities/tools/claude-code-ultimate-guide.md`) |

### Cross-wiki link syntax

- Use `@wiki-alias/path/to/page.md` for cross-wiki references (e.g., `@osint-wiki/concepts/exploration-graph-dead-ends.md`)
- Bidirectional: if this wiki's page A references another wiki's page B, add a matching `@cybersecurity-wiki/...` backlink on page B
- When creating a stub in another wiki, note the cross-wiki dependency in `## Relations`

## Operations

### Ingest (adding a new source)

1. New source dropped into `research to be indexed/`
2. Read the source (or relevant sections for long PDFs / repo READMEs / multi-part articles)
3. **Discuss key takeaways with the user before writing**
3b. **Cross-wiki routing check** — before writing pages, evaluate whether the source contains off-topic content more relevant to another wiki. If so, route it to the correct wiki via a stub or brief. **When in doubt, prefer a brief over a stub** — briefs are cheaper and don't create maintenance burden in the target wiki.
4. Create `wiki/sources/<slug>.md` — frontmatter + Raw Concept + short Narrative
5. Identify entities + concepts the source touches. For each:
   - If page exists: update it, add `related:` backlink, bump `updated:`
   - If no page: create a stub. Real content accumulates over subsequent ingests
6. Update `wiki/index.md` — add rows for new pages
7. Append to `wiki/log.md`: `## [YYYY-MM-DD] ingest | <source title>` with bullets of what changed
8. **Archive raw to egress-fi**: `bash "../../OSINT WORKSPACE/scripts/archive_raw_to_egress.sh" --wiki-id cybersec "research to be indexed/<filename>"` — update source page `Location`
9. Update `ROADMAP.md` if the ingest opens new follow-ups; stage briefs in `briefs/` if the ingest produced something actionable
9b. **Friend brief sync (standing):** After every ingest / Phase-0 / deep-read that touches local AI, owned lab, product pentest, bug bounty, AI pentest harnesses, or ASVS — check `briefs/2026-08-02_friend-operator-lab-playbook.md` (tracked allowlist). If the friend would act differently with the new info, update the checklist / deep-research add-ons / Sources, bump `updated:`, and note `friend brief:` in the `log.md` ingest bullets. If nothing friend-relevant changed, log `friend brief: n/a`. Do not let friend-facing ops die only in chat or gitignored Phase-0 briefs.
10. A single ingest must touch 3-15 pages. If it touches 0 new pages, ask whether the source is worth ingesting

### Query (answering a question)

1. Read `wiki/index.md` first to locate relevant pages
2. Read those pages; follow `@relations` where useful
3. Synthesize the answer with inline citations to source pages and raw sources
4. **OOD signal**: if the wiki doesn't contain a real answer, say so explicitly. Don't fabricate from tangential matches. Offer to ingest sources that would fill the gap
5. **File answers back**: if the query produced a valuable synthesis, file it as a new concept page or brief. Don't let insights die in chat
6. Append a query entry to `log.md` if substantive

### Lint (periodic health check)

Mechanical checks via `scripts/wiki_lint.py` (8 checks):

- **Orphans** — pages with zero inbound `related:` references
- **Bidirectional gaps** — A lists B as related but B doesn't list A
- **Dangling links** — `related:` paths that don't resolve
- **Cited-unread stubs** — source pages with `read_status=unread-stub` and ≥1 inbound edge
- **Frontmatter quality** — missing `type`/`maturity`/mismatched `updated`
- **Stale `[NEEDS VERIFICATION YYYY-MM-DD]` tags** (≥7 days old by default)
- **@path body mentions** that reference non-existent pages
- **Index coverage** — pages not listed in `wiki/index.md`

Human/LLM judgment still needed for:
- **Contradictions** — two pages making incompatible claims. Flag with `[NEEDS VERIFICATION]` and note on both pages
- **Stale claims** — superseded by newer technique (e.g. an AV-bypass killed by a vendor update). Move to `[RETRACTED]` with pointer

## External research — MCP tools

When the wiki + raw sources can't answer, or when verifying an unverified URL:

| Tool | When to use |
|------|-------------|
| `mcp__brave-search__brave_web_search` | Quick targeted lookup — CVE details, vendor advisories, fact-check a TTP |
| `mcp__brave-search__brave_news_search` | Recent breaches, policy changes, breaking 0-day developments |
| `mcp__exa__web_search_exa` | Higher-signal web search for technique deep-dives and security research papers |
| `mcp__exa__crawling_exa` | Pull clean LLM-friendly content from a known URL — turns `[Source: https://...]` into verifiable text for `## Snippets` |
| `mcp__exa__get_code_context_exa` | GitHub repo context — README, structure, key files. Primary tool for security-tool evaluation (offensive + defensive). |
| `mcp__exa__deep_researcher_start` / `_check` | Async multi-step research — threat-actor profile build-out, comprehensive certification comparison |
| `mcp__playwright__browser_navigate` (+ snapshot, click, screenshot) | Inspect vendor surfaces, certification portals, validators |

**Workflow integration**:
- **Ingest**: when a source cites a URL or CVE, prefer `crawling_exa` to pull cited page directly into `## Snippets`
- **Query (OOD)**: before declaring a wiki gap, run `web_search_exa` or Brave. If results converge, ingest the best 1-2 hits as new source pages
- **GitHub-repo eval**: `get_code_context_exa` + Phase-0 audit pattern (below) — see `prompts/github-repo-eval.md`. Especially common for offensive-tool evaluation (C2 frameworks, recon tools, exploit kits)

Cost discipline: Exa is a paid API. Default `numResults: 3-5` for routine queries; `deep_researcher_*` reserved for genuine multi-source synthesis.

## Distribution rules

Material ready to leave the wiki goes through `briefs/` first:

- **→ claude.ai / Claude Desktop** — copy the relevant brief body into a Claude conversation for engagement-report drafting, exam study, threat-modelling, kid-safety talks
- **→ Hands-on use** — paste briefs into engagement notes, SOC runbooks, CTF write-ups, certification cram sheets. Manual transfer; no automation.

No remote server, no scp, no team distribution. Everything stays on this laptop.

### Hands-on rules — ethics + legality

- **Authorization is non-negotiable.** Every technique on these pages assumes you have written authorization for the target (engagement scope, bug-bounty program rules, owned lab). Operating outside scope is a crime in most jurisdictions.
- **CVE reporting follows responsible disclosure.** When this wiki documents a new finding, follow vendor disclosure timelines (default 90 days) before publishing details. See `concepts/responsible-disclosure.md`.
- **Tools have dual use.** Cobalt Strike, Mimikatz, BloodHound, etc. are red-team standards AND criminal-malware components. The wiki documents them for authorized use only.
- **Kid-safety content is not a kid-grooming research aid.** Pages under that umbrella are written for parents / teachers / law-enforcement context, not for the inverse use case.
- **Threat-actor pages document TTPs, not victims.** Avoid PII; cite published threat-intel reports rather than scraped data.

When in doubt, prefer the conservative interpretation and ask the user.

## Working method

- Search the wiki first. Raw sources second. External sources last (via MCP)
- Prefer paraphrase + cite over raw quote. Quotes go in `## Snippets` with full citation
- When stress-testing a claim about a technique, actively look for the matching defender mitigation — exploitation pages without an opposing defender perspective are half-pages
- Flag single-source claims explicitly. Especially common with offensive tradecraft, which often comes from a single blog post or conference talk
- File insights into wiki pages or briefs before they disappear from chat
- For real-world actions (running a tool against a live target, posting a CVE, advising a kid about a safety incident), be extra rigorous about provenance and authorization — wrong calls have real-world consequences

## Phase-1 adopt-wire (agent-security harness)

Phase-0 audits; Phase-1 wires. Cybersec owns **agent-security** operational wires for the federation.

Always-apply Cursor rules (this wiki):

| Theme | Rule |
|-------|------|
| MCP / tool control | `.cursor/rules/cemini-cybersec-mcp-tool-control.mdc` |
| Agent runtime / skill audit | `.cursor/rules/cemini-cybersec-agent-audit.mdc` |
| Agent containment | `.cursor/rules/cemini-cybersec-agent-containment.mdc` |
| Lab red-team only | `.cursor/rules/cemini-cybersec-lab-redteam.mdc` |
| Federation K230–K233 | `.cursor/rules/cemini-phase1-policy-wires.mdc` |

**Runtime (optional):** `cve-mcp` in `.cursor/mcp.json` → `raw-sources/repos/cve-mcp-server` (`uv run`). Keys stay in the clone `.env`, never in MCP JSON.

Entity/source pages carry `wire_status` / `wire_target`. Prefer policy wires; ask once before MCP/`settings.json` runtime installs. Skip Image-gen / 3D local wire backlogs. No GRPO trainers, Harbor/Modal fleets, or curl\|sh as “wired”.

Canon: `@ccc-wiki/concepts/phase1-adopt-wire.md` · skill `.cursor/skills/phase1-wire/SKILL.md`.

## Phase-0 audit pattern (before adopting an external tool)

Before adopting any external security tool into the workflow, run a Phase-0 source audit (~30 min):

1. Read the README + LICENSE + last-N-commits (or for SaaS: pricing page + terms-of-service + recent changelog)
2. Verify license — for FOSS tools, check copyleft scope (matters for closed-source consulting work); for SaaS, check data exportability + vendor-lock-in
3. Verify maturity — stars/commits/last-push/issue-responsiveness for FOSS; review sites + threat-intel-community discourse for SaaS
4. **Audit for the most-likely failure mode for this tool class:**
   - C2 frameworks: detection signature freshness (does Defender / CrowdStrike pop the default profile?)
   - Recon tools: rate-limit handling + active-vs-passive distinction
   - Exploit kits: payload reliability across patched + unpatched targets
   - SOC / SIEM tools: ingestion-rate ceiling + alert false-positive rate
5. Compare against existing wiki coverage (don't adopt parallel implementations)
6. Decide GO / CONDITIONAL-GO / NO-GO and record in the entity page
7. **If GO / CONDITIONAL-GO: actually adopt and use** — clone under `raw-sources/repos/` (space budget soft-cap **~2GB** for the tree; raise when needed for GO tools like cua), install CLIs onto `~/.local/bin`, stamp the entity page with Local adoption, then:
   - **Agent-side:** wire into `scripts/adopted_security_preflight.sh` (or equivalent) and **run** it; do not leave clones unused
   - **User-side:** write a short brief listing anything only a human can do (Lume VM install, API keys, Codex hook consent, etc.)
8. Space discipline: prefer shallow clones; skip AOSP-class trees unless there is an immediate lab device; Prefer REFERENCE over clone when no public code exists

The reusable prompt for evaluating a list of GitHub repos is at `prompts/github-repo-eval.md`.

## Session-start ritual

On every new session, **before any other work**:

### 0. Resume from hot.md

Read `hot.md` (gitignored session-state cache). Report in one line:

> "Resuming from <last position>. Workspace idle. Next: your direction."

If `hot.md` is missing (first run, deleted), say:

> "No `hot.md` found — fresh session. Want me to rebuild session state from `wiki/log.md` + `ROADMAP.md`?"

At session end, rewrite `hot.md` with updated position, open decisions, pending actions.

### 1. Inbox check

```bash
ls -1 "research to be indexed/" 2>/dev/null | grep -v '^\.'
```

If items exist that the user hasn't asked you to address, mention briefly: "Btw, you have N items in `research to be indexed/`. Want me to triage them?"

### 2. Adopted-tool / Cursor security use

Prefer the **federation** scanner so every Open Folder root stays covered:

```bash
cursor-security-preflight              # all workspaces + ~/.cursor
# or: bash scripts/adopted_security_preflight.sh   # wrapper → same CCC canon
cursor-security-preflight --local      # this wiki only
```

Agent runs this (not the user) when: (a) finishing a local-adoption batch, (b) about to enable a new third-party Cursor skill / MCP, or (c) after `sync_federation_cursor_skills.sh`. Reports: `~/.cursor/security-preflight/latest/`. Summarize HIGH/CRITICAL to the user; do not silently ignore CRITICAL.

Keep each check under 60 seconds unless an adoption/preflight run was requested.

## Related — environment + secrets

- **Brave Search API** / **Exa API**: optional but recommended for CVE lookup + threat-intel research. See `.env.example` for the template.
- **Claude Desktop MCP config**: see `claude_desktop_config.json.example` for the template that drops into `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS).

If you fork/clone this workspace to another machine: copy `.env.example` to `.env` and fill in your own keys. Never reuse anyone else's keys.
