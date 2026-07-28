---
name: super-audit
description: >-
  Super audit council — three Cursor readonly subagents plus two OpenRouter API
  legs (Fusion + premium) and one free local Ollama cross-check when available
  (6-model default). Falls back to 5-model (3 Cursor + 2 OpenRouter) without
  local. Operator may override routing. Use for super audit, /super-audit,
  council super audit, pre-ship multi-opinion review.
license: MIT
metadata.author: cemini23
metadata.version: "1.6.4"
disable-model-invocation: true
permissions:
  - network
  - filesystem:read
  - filesystem:write
  - env
---

# Super audit (5–6 model council)

**Default stack:** **3 Cursor + 2 OpenRouter + 1 local Ollama** when OpenRouter key and Ollama are both up. Without local → **3 Cursor + 2 OpenRouter**. Operator may override (custom `auditors.json`, `quick` mode, `SUPER_AUDIT_SKIP_LOCAL=1`).

**Tier 1 only** — all auditors are readonly; they report, they do not edit.

## Default auditor layout

| Slot | Channel | Role | Default model |
|------|---------|------|---------------|
| 1–3 | Cursor Task | mode → roles (cursor-audit matrix) | premium Cursor slugs |
| 4 | OpenRouter API | api-adversarial | `openrouter/fusion` |
| 5 | OpenRouter API | api-deep-reasoning | `OPENROUTER_PREMIUM_MODEL` → `z-ai/glm-5.2` |
| 6 | **Ollama (local, free)** | api-local-cross-check | best **qwen\***, else largest `*b` |

**Slot 6 is additive** — not a replacement for slots 4–5. Skipped when Ollama is down or `SUPER_AUDIT_SKIP_LOCAL=1`.

### Fallback tiers (`discover_api_keys.py`)

| Tier | When | Auditors |
|------|------|----------|
| **default-6-model** | OpenRouter + Ollama | 3 Cursor + Fusion + premium + local |
| **default-5-model** | OpenRouter, no Ollama | 3 Cursor + Fusion + premium |
| **fallback-local-only** | Ollama only (no OR key) | 3 Cursor + 2× local |
| **degraded** | neither | 3 Cursor only |

### Setup

**OpenRouter** (slots 4–5) — export in the shell (or point `CEMINI_LLM_ROUTING_ENV` at a local routing file you manage outside the skill):

```bash
export OPENROUTER_API_KEY=sk-or-v1-...
export OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
export OPENROUTER_PREMIUM_MODEL=z-ai/glm-5.2
# optional: export CEMINI_LLM_ROUTING_ENV=/absolute/path/to/your-routing-file
```

**Ollama** (slot 6) — auto-discovered:

```bash
ollama serve && ollama pull qwen3.5:32b
# optional: OLLAMA_MODEL=qwen3.5:32b
```

**Verify:**

```bash
python3 .cursor/skills/super-audit/scripts/discover_api_keys.py
```

Scripts read process environment only (plus optional `CEMINI_LLM_ROUTING_ENV`). They do not scan project dotenv trees.

**Operator overrides:**

- `SUPER_AUDIT_SKIP_LOCAL=1` — force 5-model even when Ollama is running
- Custom `--auditors path.json` — full manual routing
- `quick` mode — 3 Cursor + 1 API only (see mode matrix)
- User says "local only" / "no OpenRouter" — tailor per request

**Never** paste API keys into chat.

## When to run

| Signal | Run? |
|--------|------|
| GO/NO-GO with engineering + money on the line | Yes |
| cursor-audit ran but user wants more coverage | Yes |
| Pre-prod deploy | Yes |
| Trivial fix | No — cursor-audit or direct edit |
| User says "quick" | Yes — narrowed scope |

## vs cursor-audit

| | cursor-audit | super-audit |
|---|-------------|-------------|
| Auditors | 3 Cursor | 5–6 (3 Cursor + 2–3 API) |
| Cost | 3× subagent | 3× subagent + 2× OR + 0–1 free local |
| Best for | Triage | Pre-ship council |

Read [cursor-audit](../cursor-audit/SKILL.md) for shared synthesis rules.

## Workflow (parent agent)

```
Super audit progress:
- [ ] 0. Tailor — domain prompt, mission, artifacts
- [ ] 1. Scope — target, question, constraints
- [ ] 2. Mode — Cursor roles + run discover_api_keys.py (expect 5 or 6 auditors)
- [ ] 3. Pack — build_audit_pack.py
- [ ] 4a. Cursor leg — 3× Task in ONE message, readonly
- [ ] 4b. API leg — run_api_auditors.py --discover (2–3 parallel HTTP calls)
- [ ] 5. Synthesize — N-model consensus / conflicts (N = 5 or 6)
- [ ] 6. Act — report only unless user says fix
```

Announce before dispatch:

> Super audit — mode: `{mode}` · **{N} auditors** · Cursor: `{r1,r2,r3}` · API: `{slots 4–6 from discover}` · pack: `{path}`

### Step 2 — Mode + delegation

1. Classify mode (reference.md).
2. Run `discover_api_keys.py --json` — read `auditor_count` and `tier`.
3. Respect operator overrides stated in chat before building auditors.
4. Cursor slots 1–3: cursor-audit role matrix. API slots 4+: use discovery output unless tailored.

### Step 4b — API leg

```bash
python3 .cursor/skills/super-audit/scripts/discover_api_keys.py
python3 .cursor/skills/super-audit/scripts/run_api_auditors.py \
  --pack reports/audit/pack-{slug} \
  --out reports/audit/premium-{slug} \
  --discover
```

Runs **all** discovered API slots in sequence (Fusion, premium, local when present).

### Step 5 — Synthesize

Use `auditor_count` from discovery (5 or 6). Template:

```markdown
# Super audit — {target}

**Mode:** {mode} · **Auditors:** {N} · **Tier:** {tier}

| Slot | Channel | Role | Model | Verdict |
|------|---------|------|-------|---------|
| 1–3 | cursor | … | … | … |
| 4 | api | api-adversarial | fusion | … |
| 5 | api | api-deep-reasoning | premium | … |
| 6 | local | api-local-cross-check | qwen… | … | *(if present)* |

## Consensus (≥3) · Strong (≥4, ≥5 if 6-auditor run)
## Unique · Conflicts · Patch backlog · Overall SHIP/REWORK/REJECT
```

## Invocation phrases

- `/super-audit` · `super audit on …` · `council super audit`
- Optional: `quick`, `skip local`, `5-model only`, custom auditors

## Cost discipline

- Default 6-model: 3× Cursor + 2× OpenRouter + 1× free local.
- Use **quick** or **SUPER_AUDIT_SKIP_LOCAL=1** to trim cost/time.
- Do not re-run full council on every tiny edit.

## Related

- [cursor-audit](../cursor-audit/SKILL.md)
- [reference.md](reference.md)
- [examples.md](examples.md)
- Export keys in-shell, or set `CEMINI_LLM_ROUTING_ENV` to your routing file
