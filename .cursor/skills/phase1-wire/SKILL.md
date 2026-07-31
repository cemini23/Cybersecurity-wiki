---
name: phase1-wire
description: >-
  Phase-1 adopt-wire: turn Phase-0 ADOPT/GO verdicts into concrete wires
  (Cursor rules, CLAUDE.md bullets, rare MCP/PATH/skill installs). Use when
  the user invokes /phase1, says "wire adopts", or after an ingest with
  ADOPT/GO items still unwired.
metadata.author: cemini23
metadata.version: "1.0.0"
disable-model-invocation: false
federation: true
---
# /phase1 — adopt-wire (federation)

Canon: `@wiki/concepts/phase1-adopt-wire.md` (CCC). Phase-0 audits; Phase-1 wires.
Deploy: `federation: true` → `scripts/sync_federation_cursor_skills.sh` (CCC post-commit autosync).

## Triggers

| Invoke | Action |
|--------|--------|
| `/phase1` or “wire adopts” | Backlog sweep (inventory → classify → wire Top N) |
| End of ingest with ADOPT/GO | Propose Phase-1 for **this batch only**; wire unless user declines |
| “phase1 inventory” | Run inventory script only; no writes |

## Hard stops

- No secrets in rules/handoffs
- No `curl … \| sh`
- No LIVE Discord without LIVE OK
- **No Image-gen / 3D-printing local wires** (operator does not run those locally)
- Ask before editing `~/.cursor/mcp.json`, project MCP, or `settings.json`
- Do **not** install GRPO trainers, Harbor/Modal fleets, or ARC full runners as “wired”

## Wire classes

| Phase-0 posture | Phase-1 class | What to write |
|-----------------|---------------|---------------|
| **ADOPT** pattern | `policy_wired` | 3–7 bullets in Cursor rule and/or owning `CLAUDE.md` |
| **GO** drop-in client/plugin | `runtime_wired` | MCP / PATH / `.cursor/skills` — after operator OK |
| **GO** REFERENCE / paper repro | `wont_wire` or leave `unwired` | Keep clone; mark `wont_wire` + reason |
| **NO-GO** / OOD | `wont_wire` | No harness edit |

Prefer **one rule file per theme**, not one rule per arXiv id.

## Procedure

1. **Inventory** (backlog) or list batch entities (ingest):
   ```bash
   python3 scripts/phase1_adopt_inventory.py --write-brief
   ```
2. **Classify** each candidate → policy / runtime / wont_wire / deferred.
3. **Wire policy** → `.cursor/rules/*.mdc` and/or `CLAUDE.md` on the owning surface (CCC, TipDrop, poker, OSINT, …).
4. **Wire runtime** only if drop-in + operator confirmed.
5. **Update entity frontmatter:**
   - `wire_status: unwired | policy_wired | runtime_wired | wont_wire | deferred`
   - `wire_target: path/to/rule-or-claude-or-mcp` when wired
6. **Verify:** re-read wired bullets; optional `scripts/adopt_k*_phase0.sh` still pass; `wiki_lint.py`.
7. **Log** one line in `wiki/log.md` + mention in ingest handoff if mid-ingest.

## Active surfaces (wire here)

CCC · OSINT · TipDrop kit · Atto · poker arena · Cybersec · Game-dev · Gambling · SEO · CeminiSuite

**Skip local wire backlog:** Image-gen · 3D-printing

## Success criteria

- [ ] Every batch ADOPT/GO item has `wire_status` ≠ `unwired` (or explicit `deferred` with next action)
- [ ] Policy wires are reachable by agents (alwaysApply rule or CLAUDE.md)
- [ ] Trainer/Modal/REFERENCE-only clones marked `wont_wire` with reason
- [ ] Inventory brief updated when sweeping backlog
- [ ] No Image-gen/3D local wire attempted
