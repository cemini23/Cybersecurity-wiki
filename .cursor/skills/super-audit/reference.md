# Super audit — reference

Extends [cursor-audit model delegation](../cursor-audit/reference.md). Same **premium tier** and **role-based** picks for Cursor slots 1–3; API slots 4–5 use **API roles** below.

## 5-auditor layout

| Slot | Channel | Delegation |
|------|---------|------------|
| 1–3 | Cursor Task | Mode → role matrix (cursor-audit reference) |
| 4–5 | HTTP API | Mode → API role matrix (this file) |

**Quick mode:** slots 1–3 (premium Cursor roles) + slot 5 API only (skip slot 4 adversarial).

## Selection procedure (parent — Step 2)

1. Classify **mode** (add **`prod-ship`** for bot/config deploy GO/NO-GO).
2. Resolve **Cursor roles** for slots 1–3 per cursor-audit reference.
3. Resolve **API roles** for slots 4–5 per mode → API role matrix.
4. Run `discover_api_keys.py` — map available keys to API role candidates.
5. Build or select `auditors.json` from role picks (see templates below).
6. Announce:

   > Super audit — mode: `prod-ship` · Cursor roles: agentic-reasoning/codex/third-lens · API roles: adversarial/deep-reasoning · pack: `{path}`

Never paste API keys into chat.

## Mode → Cursor roles (slots 1–3)

Same as cursor-audit, plus:

| Mode | Slot 1 | Slot 2 | Slot 3 | Use when |
|------|--------|--------|--------|----------|
| **prod-ship** | agentic-reasoning | code-implementation | third-lens | Bot deploy, conviction.yaml, tournament lane (**super-audit default**) |

All other modes: see [cursor-audit reference](../cursor-audit/reference.md#mode--role-matrix).

## Mode → API roles (slots 4–5)

| Mode | Slot 4 role | Slot 5 role |
|------|-------------|-------------|
| **prod-ship** | api-adversarial | api-deep-reasoning |
| **code-debug** | api-adversarial | api-deep-reasoning |
| **security** | api-adversarial | api-deep-reasoning |
| **config-infra** | api-deep-reasoning | api-adversarial |
| **brief-plan** | api-strategic | api-deep-reasoning |
| **architecture** | api-adversarial | api-deep-reasoning |
| **quick** | *(skip)* | api-deep-reasoning |

## API + local catalog

| API role | Purpose | Provider | Candidates (best first) |
|----------|---------|----------|---------------------------|
| **api-adversarial** | Red-team, contrarian deploy takes | OpenRouter | **`openrouter/fusion`** |
| **api-adversarial** | Same role, **free** | **Ollama** | Best **qwen\***, then largest `*b` (`discover_api_keys.py`) |
| **api-deep-reasoning** | Quant depth, patch ranking | OpenRouter | **`OPENROUTER_PREMIUM_MODEL`** → `z-ai/glm-5.2` |
| **api-deep-reasoning** | Same role, **free** | **Ollama** | Same local model, reasoning system prompt |
| **api-strategic** | Brief GO/NO-GO | OpenRouter | `anthropic/claude-opus-4.6` |
| **api-advisor** | Domain-tuned | `ADVISOR_*` or OR | pro-tier `ADVISOR_MODEL` |

**Auto-routing (`--discover`) — operator default:**

| OpenRouter | Ollama | Auditors | API slots |
|------------|--------|----------|-----------|
| yes | yes | **6** | Fusion + premium + **local cross-check** |
| yes | no | **5** | Fusion + premium |
| no | yes | **5** (fallback) | 2× local |
| no | no | **3** (degraded) | none |

Slot 6 local is **additive** when Ollama is up. `SUPER_AUDIT_SKIP_LOCAL=1` forces 5-model. Operator chat overrides win.

### Tailoring API roles by domain

| Domain | Slot 4 | Slot 5 |
|--------|--------|--------|
| Poker / trading bot | api-adversarial (`openrouter/fusion`) | api-deep-reasoning (`OPENROUTER_PREMIUM_MODEL` / GLM 5.2) |
| WC bot / conviction | api-advisor (pro `ADVISOR_MODEL`) | api-deep-reasoning (premium @ OR) |
| Adoption brief | api-strategic (Opus @ OR) | api-deep-reasoning (GLM 5.2 @ OR) |
| Security | api-adversarial (Fusion) | api-deep-reasoning (premium @ OR) |

Use OpenRouter model IDs from [openrouter.ai/models](https://openrouter.ai/models).

## API key discovery (run before Step 4b)

Sources (process environment wins over file values for the same key):

| Priority | Source |
|----------|--------|
| 1 | Process environment (`OPENROUTER_*`, `OLLAMA_*`, `ADVISOR_*`, …) |
| 2 | Optional file at `$CEMINI_LLM_ROUTING_ENV` (operator-set absolute path) |

Scripts **do not** scan project dotenv trees or hardcoded home secret paths.

**Variables to probe:**

| Variable | Used for |
|----------|----------|
| `OPENROUTER_API_KEY` | Premium legs — Fusion + slot 5 (optional if Ollama running) |
| `OPENROUTER_BASE_URL` | Default `https://openrouter.ai/api/v1` |
| `OPENROUTER_PREMIUM_MODEL` | Slot 5 paid default — **`z-ai/glm-5.2`** |
| **`OLLAMA_BASE_URL`** | Default `http://localhost:11434/v1` — **free local leg** |
| **`OLLAMA_MODEL`** | Override; else auto-pick best qwen* / largest `*b` |
| `SUPER_AUDIT_SKIP_LOCAL` | `1` = drop slot 6 even when Ollama is running |
| `ADVISOR_*` | Optional api-advisor override |

Without OpenRouter **or** Ollama, super-audit runs **3-model cursor-audit only**.

**Session setup (keys already exported):**

```bash
python3 .cursor/skills/super-audit/scripts/discover_api_keys.py
python3 .cursor/skills/super-audit/scripts/run_api_auditors.py --pack ... --out ... --discover
```

Discovery writes recommended slots; `--discover` on run_api_auditors uses them automatically.
Provider keys come from the process environment (or `CEMINI_LLM_ROUTING_ENV`).

## auditors.json (build from roles)

Pass `--auditors path/to/auditors.json` to `run_api_auditors.py`. Labels should reflect **role**, not vendor lock-in.

### Schema (required)

```json
{
  "slots": [
    {
      "label": "api-adversarial",
      "model": "openrouter/fusion"
    }
  ]
}
```

| Field | Required | Notes |
|-------|----------|--------|
| `slots` | **yes** | Array. A bare single-slot object at the root is **rejected**. |
| `label` | **yes** | Output filename stem; unique per run preferred |
| `model` | **yes*** | OpenAI-compat model id. *Or* set `model_env` with a non-empty fallback `model` |
| `role` | no | Documentation / synthesis only |
| `base_url_env` | no | Env var for host. Defaults when unset: `OPENROUTER_*` → openrouter.ai, `DEEPSEEK_*` → `https://api.deepseek.com/v1`, `OLLAMA_*` → localhost:11434 |
| `api_key_env` | no | Default `OPENROUTER_API_KEY`. `ADVISOR_API_KEY` falls back to OpenRouter key |
| `api_key_optional` | no | `true` for local Ollama |
| `model_env` | no | Override `model` from env (e.g. `OPENROUTER_PREMIUM_MODEL`) |
| `fallback_model` | no | Retry once with this model id if the primary call fails |
| `extra` | no | Merged into chat-completions body. Fusion: `{"plugins":[{"id":"fusion"}]}` |
| `system` | no | System prompt |
| `local` | no | Forces Ollama base default |
| `max_tokens` | no | Default 16000 |
| `provider` | no | Log label only |

**Default fallback** (`auditors.default.json`) — prod-ship generic: api-adversarial + api-deep-reasoning. Used when discovery finds no API keys **and** no `--auditors` file was passed.

```json
{
  "slots": [
    {
      "label": "api-adversarial",
      "role": "api-adversarial",
      "base_url_env": "OPENROUTER_BASE_URL",
      "api_key_env": "OPENROUTER_API_KEY",
      "model": "openrouter/fusion",
      "extra": { "plugins": [{ "id": "fusion" }] },
      "system": "Super audit — adversarial readonly reviewer. Follow required output format exactly."
    },
    {
      "label": "api-deep-reasoning",
      "role": "api-deep-reasoning",
      "base_url_env": "OPENROUTER_BASE_URL",
      "api_key_env": "OPENROUTER_API_KEY",
      "model_env": "OPENROUTER_PREMIUM_MODEL",
      "model": "z-ai/glm-5.2",
      "system": "Super audit — deep reasoning readonly reviewer. Follow required output format exactly."
    }
  ]
}
```

**Brief-plan example** — swap slot 4 to api-strategic (still wrapped in `slots`):

```json
{
  "slots": [
    {
      "label": "api-strategic",
      "role": "api-strategic",
      "base_url_env": "OPENROUTER_BASE_URL",
      "api_key_env": "OPENROUTER_API_KEY",
      "model": "anthropic/claude-opus-4.6",
      "system": "Super audit — strategic readonly reviewer. Follow required output format exactly."
    }
  ]
}
```

**DeepSeek / non-OpenRouter legs** — always set `base_url_env` to `DEEPSEEK_BASE_URL` (runner defaults to `https://api.deepseek.com/v1` when the env var is empty). Do **not** rely on the OpenRouter host for DeepSeek keys.

Parent **rewrites `model`** fields when discovery or tailoring picks a different premium candidate for the role.

## Audit pack checklist

- [ ] Tailored prompt with `{{MODEL_SLOT}}` and `{pack_index}` placeholder
- [ ] `PACK_INDEX.md` lists every artifact with absolute paths
- [ ] Mission is one sharp question
- [ ] Regime boundaries explicit (no cross-pool claims)
- [ ] Required output format block in prompt
- [ ] Ruled-out hypotheses section
- [ ] `meta.json` records build timestamp
- [ ] Synthesis header lists roles + resolved slugs for all 5 slots

## Synthesis thresholds (5 auditors)

| Pattern | Verdict |
|---------|---------|
| ≥4 agree on critical issue | FAIL → REJECT or REWORK |
| ≥3 agree on critical | FAIL |
| Critical from 1–2 only | WARN → investigate |
| ≥4 PASS | SHIP (note unique warns) |
| Split on deploy commit / root cause | REWORK until conflict resolved |

## HTTP requirements

API script needs `httpx` (`uv pip install httpx` or project venv). Timeout 600s per call. Temperature 0.2.

## Integration with static brief audit

For `briefs/` handoffs:

1. Super audit synthesis (qualitative, 5-model)
2. `python3 scripts/skill_audit.py briefs/<file>.md`

Static REJECT overrides multi-model SHIP.
