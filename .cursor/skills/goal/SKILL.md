---
name: goal
description: >-
  Single-shot meta-prompt envelope for non-trivial tasks (/goal). Expands user
  intent into context, success criteria, operating rules, and completion proof.
  Use when the user invokes /goal or asks for a full-prompt goal session.
disable-model-invocation: true
federation: true
---
# /goal — full-prompt single-shot meta-template

Cemini modal pattern for non-trivial Cursor sessions. Canon wiki: `@wiki/entities/patterns/full-prompt-goal-template.md` (CCC repo).

## Parse

Accept `/goal <task description>` or a message starting with `/goal` followed by the goal text.

- **Empty body:** show usage below and ask what "done" looks like.
- **Body present:** expand into the full envelope, then execute (plan first, then work).

## When to use

| Use `/goal` | Skip (lighter prompt) |
|-------------|------------------------|
| Multi-file features, ingests, Phase-0 audits, refactors | Single-file edit, status, lint-only |
| Needs explicit done-criteria + proof | Ambiguous intent — ask first instead of AUTONOMOUSLY |

## Output envelope (produce before heavy execution)

Fill every section; omit only what truly does not apply.

```markdown
/goal <one-line done statement>

── CONTEXT ──
- Project:
- Stack:
- Current state:
- Working dir:
- Constraints: (include NO PUSH / laptop-only / Tier-2 if relevant)
- Audience:

── SUCCESS CRITERIA (ALL MUST BE TRUE) ──
1. …
N. Runs without errors; agent can show proof.

── OPERATING RULES — NON-NEGOTIABLE ──
1. PLAN FIRST — numbered task list before code/docs edits.
2. WORK AUTONOMOUSLY — no clarifying Qs unless genuinely blocked.
3. SELF-VERIFY — after each step: tests, lint, inspect output.
4. DEBUG YOURSELF — diagnose and fix; do not hand back broken state.
5. USE EVERY TOOL — MCP, terminal, web — within project allowlists.
6. NO PLACEHOLDERS — real implementations, not TODO stubs.
7. PROGRESS LOG — completed / in-flight / decisions / blockers.
8. STAY ON GOAL — off-spec discoveries noted, then back to SC.
9. IF BLOCKED — log wall; parallelize everything else.
10. CHECK SUCCESS BEFORE STOPPING — re-read every SC; confirm each.

── QUALITY BAR ──
Clean, typed where applicable; document new patterns; cite sources on wiki work.

── FINAL DELIVERABLE ──
Per-SC confirmation · files touched · run/test steps · proof · decisions · known limits
```

## Cemini optional success criteria (add when relevant)

| Tag | When | SC snippet |
|-----|------|------------|
| **CLAIM DRIFT (K122)** | Research / multi-step synthesis | Mechanism preserved; citations match workspace |
| **HARNESS TAG (K124)** | Hooks, skills, MCP, rules edits | Six-responsibility + ETCLOVG layer recorded |
| **COMPACT RUBRIC (K124)** | Expected >50 turns | `hot.md` Checkpoint + Compact OK before `/compact` |
| **SKILL PROMOTION (K124)** | New skill pages | ≥2 independent reuses logged or wiki-only |
| **VERIFY HIERARCHY (K162)** | Self-improving agents / harness evolution | Name stop signal; prefer formal/execution over judge/intrinsic; evaluator cannot rewrite pass criteria; document loop-closure (in/on/closed) |
| **CAPABILITY TREE (K164)** | Multi-tool / multi-MCP agents | Mutually exclusive top domains; lazy child manifests only; nested push/pop; Prebind at binding leaves |
| **LINEAGE (K155)** | Research briefs / proposal or patch eval | Score mechanism inheritance (GenomeDiff), not citation proximity; joint parent+driver+fate consistency |
| **CROSS-WIKI** | Federation ingest | Bidirectional `@wiki-alias/` backlinks |
| **LOCAL-ONLY** | Laptop wikis | Explicit NO REMOTE / commit only when asked |

## Workspace-specific hooks

| Workspace | Session start | Session end |
|-----------|---------------|-------------|
| **CCC / wikis** | Read `CLAUDE.md`, `hot.md` if present | Rewrite `hot.md` + Checkpoint / Compact OK |
| **OSINT** | `CLAUDE.md`, inbox, lazy-tool defaults | Same + `wiki/log.md` on ingest |
| **CeminiSuite / apps** | Read relevant README / ROADMAP | Tests green before done |

## Cursor vs Claude Code

- **Cursor:** this skill replaces Claude Code's `/goal` slash command + Stop-hook gating. **You** must enforce rule 10 (check SC before ending turn).
- **Claude Code:** same envelope; Stop hook may block until goal satisfied [NEEDS VERIFICATION on hook timing].

## Pair with /loop

- `/goal` = single-shot to completion.
- `/loop` = recurring or dynamic re-runs of a sub-prompt. Do not nest unless user asks.

## Usage

```
/goal Ingest inbox PDFs: preingest, 7 source pages, lint clean, commit when asked
```

```
/goal Phase-0 audit github.com/foo/bar — GO/NO-GO with license API proof
```
