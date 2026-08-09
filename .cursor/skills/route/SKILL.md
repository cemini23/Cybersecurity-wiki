---
name: route
description: >-
  Sort any task into easy / mid / hard / money and outsource it via one unified
  chain (OpenRouter free, Grok CLI, claude-ds / DeepSeek, Cursor Grok). Always-approve
  is the skill default. Use when the user says /route, "route this", "route as
  recommended", or asks to auto-pick cheap executors. Sibling habit to "hand it
  to grok" — handoff-to-grok is under-the-hood, not a separate workflow. Base case
  for all Cemini projects — not TipDrop-specific.
license: MIT
metadata.author: cemini23
metadata.version: "2.1.0"
federation: true
---

# /route — unified task sorter (easy · mid · hard · money)

**Cemini base-case task router.** Say **route as recommended** / `/route` / `route this`. Works for Atto, CCC, OSINT, TipDrop, wikis — whatever the current project WorkDir is.

**Canon script host:** private repo [`cemini23/agent-toolkit`](https://github.com/cemini23/agent-toolkit) (`~/Projects/agent-toolkit`, or `/opt/cemini/agent-toolkit` on prod). Set `ROUTE_KIT` if needed. TipDrop workspace-kit only has deprecated redirect stubs. `handoff-to-grok.ps1` is an implementation helper called by `route-task` — operators should not maintain a separate "handoff vs route" habit.

## Skill contract (non-negotiable)

**Always-approve is the default on every route executor — all machines, all profiles.**

| Executor | Default (MUST) | Opt out only when operator asks |
|----------|----------------|----------------------------------|
| **Grok CLI** (plan mid / implement hard) | `--always-approve` via `handoff-to-grok.ps1` | `-NoApprove` |
| **claude-ds** (easy fallback + mid execute) | `--dangerously-skip-permissions` via `claude-ds.ps1` / `claude-ds.sh` | `-NoSkipPermissions` / `CLAUDE_DS_ASK=1` |
| **Cursor Grok** (fallback plan/implement) | Auto-run / full tool approve | UI Auto-run off / ask mode |
| Easy API scripts | no tool sandbox — N/A | — |

**DeepSeek Claude names (all hosts):** prefer **`claude-ds`**. On cemini-prod / older Linux the same tool may be **`deepseek-claude`** (`~/.deepseek-claude` on PATH). Resolve either — do not fail the chain if only one exists. Order: `claude-ds` → `deepseek-claude` → `~/.deepseek-claude/deepseek-claude` → `agent-toolkit/scripts/claude-ds.ps1` / `claude-ds.sh`.

Without always-approve, headless tools cancel → chain falls through to Cursor → burns quota. That is a skill bug, not an operator preference.

Secret deny rules on Grok still apply (K172). LIVE Discord / `.env` flips still need explicit OK.

Adopt on any machine once: `pwsh -File ~/Projects/agent-toolkit/scripts/adopt-route-always-approve.ps1`

## Parse

Accept `/route <task>`, `route as recommended: …`, or a message starting with `/route` / `route this:`.

- **Empty body:** ask what the task is.
- **Body present:** classify, announce lane + why, then **outsource** (never implement in the parent Cursor session except Cursor Grok fallback).

## Critical: parent Cursor is not the default implementer

When this skill runs **inside Cursor Agent**:

1. Announce lane + one-line why.
2. **Easy:** shell `route-task` (OpenRouter free → claude-ds). Do not draft in Cursor.
3. **Mid:** pack repo/task context into the handoff (or let `route-task` auto-pack), then shell `route-task` so **Grok CLI plans** and **claude-ds executes**. If Grok CLI is out of usage/auth: launch Task `grok-implementer` for **plan only**, then re-run execute via `route-task` / claude-ds. If claude-ds/DeepSeek is out: script picks **best live OpenRouter free** model for chat execute fallback.
4. **Hard/money:** write the **plan** in this session with a **premium** model (Fable / Opus / session premium) into the handoff `## Plan` section, then shell `route-task` / `handoff-to-grok` so **Grok CLI implements**. On Grok failure: Task `grok-implementer` to **implement**.
5. Summarize executor results only (lane, executor chain, verify evidence, residual risk from `_route_runs/`). Re-implement in the parent Cursor session **only** when the script prints Cursor Grok fallback and points at a handoff file.

Preferred operator habit: `route-task` from a project terminal — or `/route` in Agent when Cursor context/premium plan is needed.

```bash
# Mac (shims on PATH) — cwd = project
cd ~/Projects/atto
route-task -Profile claudio "route as recommended: fix allowlist drift"
# Refresh shims once:
pwsh -File ~/Projects/agent-toolkit/scripts/adopt-route-always-approve.ps1
```

```powershell
$kit = "$HOME/Projects/agent-toolkit"
pwsh -File "$kit/scripts/route-task.ps1" -WorkDir "$HOME/Projects/atto" -Profile claudio "hard: …"
```

## WorkDir (base case)

Resolution order:

1. `-WorkDir` / `ROUTE_WORKDIR` / `CEMINI_ROUTE_WORKDIR`
2. `Repo:` / `WorkDir:` path in the task text
3. **Current project directory** (cwd with `.git` / `AGENTS.md` / `pyproject.toml` / …)
4. TipDrop scanner **only** if the task is clearly scanner/TipDrop work
5. Else fail and ask for `-WorkDir`

### Paths with spaces (Cybersecurity wiki, CCC, OSINT, …)

Federation roots like `~/Projects/Cybersecurity wiki` previously truncated at the space when `Start-Process -ArgumentList` joined tokens. **Fixed in agent-toolkit** (`Invoke-PwshScriptNamedArgs` EncodedCommand splat + `claude-ds` `Repair-SpacedWorkDirBinding`).

Operator hygiene still:

1. Prefer quoted `-WorkDir "/Users/…/Cybersecurity wiki"` (or let the `route-task` bash shim pass `"$(pwd)"`).
2. Optional: `export CLAUDE_DS_WORKDIR="$PWD"` / `export ROUTE_WORKDIR="$PWD"` before routing.
3. Smoke: `pwsh -File ~/Projects/agent-toolkit/scripts/test-route-workdir-spaces.ps1`
4. Mid/hard implement: use **`route-task` / `handoff-to-grok.ps1 --always-approve`**, not bare Task `grok-implementer` with `acceptEdits` (headless cancels writes).

## SIP + verify gates (v2.1)

Mid execute and hard/money implement require a SIP handoff: **WorkDir**, **Success criteria**, **Verify**, **NEVER**; hard/money also need a real **Plan**. Incomplete → SDR exit **3** (not silent Grok). Opt out: `-NoSip`.

After implement, `## Verify` commands run in WorkDir; failure fails the route. Opt out: `-SkipVerify`.

Mid tasks that look like multi-file/tests/LIVE/secrets auto-escalate to hard/money unless forced with `mid:` / `deepseek:`.

Run logs: `agent-toolkit/briefs/handoffs/_route_runs/`. Parent summaries must include verify evidence — no status-only "done".

## Lanes (must follow)

| Lane | Meaning | Action |
|------|---------|--------|
| **easy** | Words / drafts / rewrite / wiki notes | **OpenRouter free** (`openrouter/free`) → **claude-ds** (DeepSeek tools) |
| **mid** | Plan then cheap tool execute | Cursor context pack → **Grok CLI plan** (`-PlanOnly`) → **claude-ds** execute. Fallbacks: Cursor Grok plan; best live OR free execute |
| **hard** | Code / tests / multi-file | **Cursor premium plan** → **Grok CLI implement** → Cursor Grok implement |
| **money** | Scoring, Stripe, Greeks, P&L, LIVE / ship | **Same as hard** + stricter money guardrails. Do not auto-LIVE. |
| **ambiguous** | Unclear | Ask: easy / mid / hard / money? |

**Fallbacks:** never hard-stop on first provider credit/usage failure — walk the chain. Grok **auth** on hard still prints `grok login` and offers Cursor Grok implement.

Force prefixes: `easy:`, `mid:` / `deepseek:`, `hard:`, `money:` (first line of multi-line prompts). Bare mentions of "DeepSeek" in NEVER lists do **not** force mid — use `use deepseek` or `deepseek:` prefix.

## Profiles

- Env `ROUTE_PROFILE=david|claudio` (aliases: `CEMINI_ROUTE_PROFILE`, `TIPDROP_ROUTE_PROFILE`) or `-Profile` on the script.
- Profiles no longer change easy provider order (free OR → claude-ds for both). Kept for logging / future local opts.
- Always-approve does **not** change by profile.

## Operating rules

1. Announce lane + one-line why before acting.
2. Hard **and money**: Cursor premium writes plan; Grok CLI implements — parent Cursor only as Cursor Grok fallback.
3. Money: same execute path as hard; require LIVE OK for live flips.
4. On provider credit/auth failure: try next fallback leg **and notify** (console banner + Desktop `ROUTE-FALLBACK-NOTICE.txt` with top-up link).
5. No secrets in handoff files. No LIVE Discord unless user says LIVE OK. **Do not send secrets to free OpenRouter models** (they may log prompts).
6. **Always pass always-approve** on Grok + claude-ds unless the operator explicitly requested ask mode (`-NoApprove` / `CLAUDE_DS_ASK=1`).
7. K172 carve-out: only the reviewed handoff path (`handoff-to-grok.ps1` / `route-task`) with scoped `--cwd`, secret deny rules, and optional `--sandbox workspace`. No free-form `grok` against home trees.
8. Mid Grok auth/usage failure → **Cursor Grok plan** (do not invent a plan in the parent session). Hard Grok failure → **Cursor Grok implement**.
9. Do not claim done without verify evidence (or explicit SDR/block).

## PowerShell one-liners

```powershell
cd ~/Projects/agent-toolkit
.\scripts\adopt-route-always-approve.ps1   # once per machine
.\scripts\route-task.ps1 -WorkDir ~/Projects/atto "Draft support FAQ"
.\scripts\route-task.ps1 "mid: strengthen this wiki note"
.\scripts\route-task.ps1 -Interactive "hard: Fix the allowlist drift"
.\scripts\route-task.ps1 -DryClassify "Is this Stripe soft-gate safe to ship?"
.\scripts\route-task.ps1 -NoApprove "…"   # rare: ask mode for this run only
.\scripts\select-openrouter-free-model.ps1  # print best live free model id
```

## Related

- `~/Projects/agent-toolkit/scripts/adopt-route-always-approve.ps1` — machine adopt
- `.../handoff-to-grok.ps1` — Grok CLI plan (`-PlanOnly`) or implement
- `.../ask-openrouter.ps1` / `claude-ds.ps1` — easy / mid execute
- `.../lib/Test-RouteHandoffSip.ps1` — SIP contract
- `.cursor/rules/cemini-route-outsource.mdc` — always-on outsource + always-approve (`tipdrop-route-outsource.mdc` is a filename alias)
