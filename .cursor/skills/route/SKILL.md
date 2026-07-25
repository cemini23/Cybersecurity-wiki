---
name: route
description: >-
  Sort any task into easy / mid / hard / money and outsource it to cheap
  executors (Grok, claude-ds, DeepSeek, OpenRouter, Ollama). Always-approve
  is the skill default. Use when the user says /route, "route this", or asks
  to auto-pick Ollama, DeepSeek, Grok, or Cursor. Sibling habit to "hand it
  to grok". Base case for all Cemini projects — not TipDrop-specific.
metadata.author: cemini23
metadata.version: "1.1.0"
---

# /route — task sorter (easy · mid · hard · money)

**Cemini base-case task router.** Same beginner habit as **hand it to grok**, but the harness picks the lane. Works for Atto, CCC, OSINT, TipDrop, wikis — whatever the current project WorkDir is.

Scripts currently ship inside `tipdrop-workspace-kit` (historical host). That does **not** mean WorkDir defaults to TipDrop.

## Skill contract (non-negotiable)

**Always-approve is the default on every route executor — all machines, all profiles.**

| Executor | Default (MUST) | Opt out only when operator asks |
|----------|----------------|----------------------------------|
| **Grok** (headless + interactive) | `--always-approve` via `handoff-to-grok.ps1` | `-NoApprove` |
| **claude-ds** | `--dangerously-skip-permissions` via `claude-ds.ps1` | `-NoSkipPermissions` / `CLAUDE_DS_ASK=1` |
| **Cursor Agent** (last resort only) | Auto-run / full tool approve | UI Auto-run off / ask mode |
| Easy/mid API scripts | no tool sandbox — N/A | — |

Without always-approve, headless tools cancel → chain falls through to Cursor → burns quota. That is a skill bug, not an operator preference.

Secret deny rules on Grok still apply (K172). LIVE Discord / `.env` flips still need explicit OK.

Adopt on any machine once: `.\scripts\adopt-route-always-approve.ps1`

## Parse

Accept `/route <task>` or a message starting with `/route` / `route this:`.

- **Empty body:** ask what the task is.
- **Body present:** classify, announce lane + why, then **outsource** (never implement in Cursor).

## Critical: Cursor is last resort

When this skill runs **inside Cursor Agent**:

1. Announce lane + one-line why.
2. **Shell out** to `route-task` / kit `scripts/route-task.ps1` (or print the exact one-liner). Prefer running from the **current project directory**.
3. **Do not** edit code, write drafts, or “just finish it” in Cursor while waiting.
4. Summarize the script/Grok/claude-ds result only. Re-implement in Cursor **only** if the script prints that all executors failed and points at a handoff file.

Preferred operator habit (cheapest): run `route-task` in a terminal from the project — not `/route` in Agent.

```bash
# Mac (shim) — cwd = project
cd ~/Projects/atto
route-task -Profile claudio "hard: fix allowlist drift"
```

```powershell
# Or call kit script with explicit WorkDir
$kit = "$HOME/Desktop/projects/tipdrop-workspace-kit"   # script host only
pwsh -File "$kit/scripts/route-task.ps1" -WorkDir "$HOME/Projects/atto" -Profile claudio "hard: …"
```

## WorkDir (base case)

Resolution order:

1. `-WorkDir` / `ROUTE_WORKDIR` / `CEMINI_ROUTE_WORKDIR`
2. `Repo:` / `WorkDir:` path in the task text
3. **Current project directory** (cwd with `.git` / `AGENTS.md` / `pyproject.toml` / …)
4. TipDrop scanner **only** if the task is clearly scanner/TipDrop work
5. Else fail and ask for `-WorkDir`

## Lanes (must follow)

| Lane | Meaning | Action |
|------|---------|--------|
| **easy** | Words / drafts / rewrite / wiki notes | **david:** Ollama → DeepSeek → OpenRouter. **claudio (no Ollama):** DeepSeek → OpenRouter → Ollama-if-up. |
| **mid** | Stronger than local qwen / complex draft | DeepSeek → OpenRouter → Ollama. Interactive: `claude-ds` (always-approve). |
| **hard** | Code / tests / multi-file | Thin plan (DeepSeek→OpenRouter) → write handoff → **Grok** (always-approve) → claude-ds (always-approve) → Cursor note. |
| **money** | Scoring, Stripe, Greeks, P&L, LIVE / ship | **Same executor chain as hard** + stricter money guardrails in handoff. Do not auto-LIVE. |
| **ambiguous** | Unclear | Ask: easy / mid / hard / money? |

**Fallbacks:** never hard-stop on first provider credit/auth failure — walk the chain.

Force prefixes: `easy:`, `mid:` / `deepseek:`, `hard:`, `money:`.

## Profiles

- Env `ROUTE_PROFILE=david|claudio` (aliases: `CEMINI_ROUTE_PROFILE`, `TIPDROP_ROUTE_PROFILE`) or `-Profile` on the script.
- **david:** easy starts Ollama; **claudio:** easy starts DeepSeek (laptops without local models).
- Hard and money use the same plan→Grok execute path.
- Always-approve does **not** change by profile.

## Operating rules

1. Announce lane + one-line why before acting.
2. Hard **and money**: write handoff via script, then Grok — keep Cursor as last-resort execute if Grok/claude-ds fail.
3. Money: same execute path as hard; require LIVE OK for live flips.
4. On provider credit/auth failure: try next fallback leg **and notify** (console banner + Desktop `ROUTE-FALLBACK-NOTICE.txt` with top-up link).
5. No secrets in handoff files. No LIVE Discord unless user says LIVE OK.
6. **Always pass always-approve** on Grok + claude-ds unless the operator explicitly requested ask mode (`-NoApprove` / `CLAUDE_DS_ASK=1`).
7. K172 carve-out: only the reviewed handoff path (`handoff-to-grok.ps1` / `route-task`) with scoped `--cwd`, secret deny rules, and optional `--sandbox workspace`. No free-form `grok` against home trees.
8. **Grok auth failure = stop and ask operator to `grok login`.** Do not fall through to claude-ds or Cursor on login/auth errors (exit 42 / `GROK LOGIN REQUIRED`).

## PowerShell one-liners

```powershell
.\scripts\adopt-route-always-approve.ps1   # once per machine
.\scripts\route-task.ps1 -WorkDir ~/Projects/atto "Draft support FAQ"
.\scripts\route-task.ps1 "mid: strong draft of this wiki note"
.\scripts\route-task.ps1 -Interactive "Fix the allowlist drift"
.\scripts\route-task.ps1 -DryClassify "Is this Stripe soft-gate safe to ship?"
.\scripts\route-task.ps1 -NoApprove "…"   # rare: ask mode for this run only
```

## Related

- `scripts/adopt-route-always-approve.ps1` — machine adopt
- `scripts/handoff-to-grok.ps1` — hard execute
- `scripts/ask-qwen.ps1` / `scripts/ask-deepseek.ps1` / `scripts/claude-ds.ps1` — easy/mid
- `.cursor/rules/tipdrop-route-outsource.mdc` — always-on outsource + always-approve (filename historical; applies to all projects)
