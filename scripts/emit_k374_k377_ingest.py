#!/usr/bin/env python3
"""Writer for K374–K377 ingest (2026-09-28). No attack payloads in wiki."""
from __future__ import annotations

import re
from pathlib import Path

WIKI = Path(__file__).resolve().parents[1] / "wiki"
CCC = Path(__file__).resolve().parents[2] / "Cemini claude code CCC" / "wiki"
EGRESS = "cemini-egress-fi:/opt/cemini-bulk/research/cybersec"
DATE = "2026-09-28"
CCC_OOD = "sources/arxiv-2609-31506-haitian-creole-cultural-awareness-ood-2026-09-28.md"
CYBER_OOD = "sources/arxiv-2609-31506-haitian-creole-llm-cultural-awareness-ood.md"


def w(rel: str, body: str) -> None:
    p = WIKI / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(body, encoding="utf-8")
    print("wrote", rel)


def bump_updated(text: str) -> str:
    return re.sub(r"^updated: \d{4}-\d{2}-\d{2}", f"updated: {DATE}", text, count=1, flags=re.M)


def add_related(rel: str, ref: str, note: str) -> None:
    p = WIKI / rel
    t = p.read_text(encoding="utf-8")
    yaml_line = f"  - {ref}"
    if yaml_line not in t:
        t = t.replace("related:\n", f"related:\n{yaml_line}\n", 1)
    body_line = f"- @{ref} — {note}"
    if f"- @{ref}" not in t:
        t = t.replace("## Relations\n\n", f"## Relations\n\n{body_line}\n", 1)
    t = bump_updated(t)
    p.write_text(t, encoding="utf-8")
    print("patched related", rel, "→", ref)


def src(
    slug: str,
    title: str,
    arxiv: str,
    kid: str,
    pdf: str,
    narrative: str,
    concept: str,
    extra_related: list[str] | None = None,
    ood: bool = False,
    wire: str = "",
) -> None:
    rels = ([f"  - {concept}"] if concept else []) + [f"  - {r}" for r in (extra_related or [])]
    rel_yaml = "related:\n" + "\n".join(rels) if rels else "related: []"
    rel_sec = f"\n## Relations\n\n- @{concept}\n" if concept else "\n## Relations\n\n"
    if extra_related:
        rel_sec += "".join(f"- @{r}\n" for r in extra_related)
    tags = "source, ood" if ood else "source, arxiv, agent-security"
    keywords = f"{arxiv}, ood" if ood else f"{arxiv}, {kid.lower()}"
    wire_line = wire or (
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (OOD)"
        if ood
        else f".cursor/rules/cemini-cybersec-agent-audit.mdc ({kid})"
    )
    body = f"""---
title: "{title}"
type: source
tags: [{tags}]
keywords: [{keywords}]
{rel_yaml}
maturity: draft
read_status: read
created: {DATE}
updated: {DATE}
phase_0_verdict: "REFERENCE {DATE} — no attack payloads in wiki."
wire_status: policy_wired
wire_target: "{wire_line}"
---
{rel_sec}
## Raw Concept

| Field | Value |
|-------|-------|
| Title | {title} |
| arXiv | {arxiv} |
| Location | {EGRESS}/{pdf} |
| Retrieved | {DATE} |
| Read status | read (abstract + triage) |

## Narrative

{narrative}

## Snippets

> See arXiv {arxiv} abstract. [Source: arXiv {arxiv} (retrieved {DATE})]
"""
    w(f"sources/{slug}.md", body)


def concept_page(
    slug: str,
    title: str,
    kid: str,
    arxiv: str,
    narrative: str,
    related: list[str],
    wire: str,
) -> None:
    rel_yaml = "\n".join(f"  - {r}" for r in related)
    rel_inline = "\n".join(f"- @{r}" for r in related)
    body = f"""---
title: "{title} ({kid})"
type: concept
tags: [concept, agent-security, {kid.lower()}]
keywords: [{arxiv}, {kid}]
related:
{rel_yaml}
maturity: draft
created: {DATE}
updated: {DATE}
wire_status: policy_wired
wire_target: "{wire}"
---

## Relations

{rel_inline}

## Raw Concept

Question: **{title}** — operator steal from arXiv {arxiv}?

## Narrative

{narrative}

## Snippets

> Triage from arXiv {arxiv} abstract. [Source: arXiv {arxiv} (retrieved {DATE})]
"""
    w(f"concepts/{slug}.md", body)


def patch_index() -> None:
    idx = WIKI / "index.md"
    text = idx.read_text(encoding="utf-8")
    block = f"""
| @sources/arxiv-2609-30383-skill-cascading-attacks.md | draft | Skill cascading attacks on skill-based agents (2609.30383; K374) |
| @concepts/skill-cascading-attacks-cross-skill.md | draft | Per-skill scan ≠ system-level skill-suite safety |
| @sources/arxiv-2609-31318-agentxploit-repo-to-runtime.md | draft | AgentXploit repo-to-runtime agent red-team (2609.31318; K375) |
| @concepts/agentxploit-repo-to-runtime-redteam.md | draft | Analyzer vs Exploiter + external verifier |
| @{CYBER_OOD} | draft | OOD Haitian Creole LLM cultural awareness (2609.31506) |
| @sources/arxiv-2609-31552-fragtoken-inference-cost-amplification.md | draft | FragToken noncanonical token cost inflation (2609.31552; K376) |
| @concepts/fragtoken-noncanonical-token-cost-audit.md | draft | Token inflation vs visible length (supply-chain) |
| @sources/arxiv-2609-31575-configuration-not-conscience-system-prompts.md | draft | System-prompt operational configuration corpus (2609.31575; K377) |
| @concepts/system-prompt-operational-configuration-corpus.md | draft | Leaked prompts are ops config, not conscience |
"""
    needle = "| @concepts/agent-execution-trace-tampering-audit.md | draft | Independent trace logging audit pattern |"
    if "K374" not in text:
        text = text.replace(needle, needle + block, 1)
        idx.write_text(text, encoding="utf-8")
        print("patched index.md")


def write_ccc_ood() -> None:
    dest = CCC / CCC_OOD
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(
        f"""---
title: "Evaluating cultural awareness of LLMs for Haitian Creole (cross-wiki from Cybersec OOD)"
type: source
tags: [source, ood, nlp, cultural-eval, haitian-creole]
keywords: [2609.31506, haitian-creole, cultural-awareness, ood]
related:
  - "@cybersecurity-wiki/{CYBER_OOD}"
maturity: draft
read_status: read
created: {DATE}
updated: {DATE}
cross-wiki-routed: cybersecurity-wiki
---

## Relations

- @cybersecurity-wiki/{CYBER_OOD} — cyber ingest OOD stub + PDF on cybersec egress

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Evaluating Cultural Awareness of LLMs for Haitian Creole |
| arXiv | 2609.31506 |
| Location | {EGRESS}/arxiv-2609.31506-evaluating-cultural-awareness-of-llms-for-haitia.pdf |
| Retrieved | {DATE} |

## Narrative

Telecom Paris **Haitian Creole cultural-awareness** eval (CAMeL-style entity infilling + story generation). Four dimensions: **specificity, bias, diversity, variation**. Native-speaker curated prompts; gap vs higher-resource French; French linguistic interference; stereotypical hardship/resilience narratives. **NLP / cultural eval** primary — not cyber-primary. Steal for CCC multilingual eval notes only; no security payloads.

## Snippets

> First systematic evaluation of cultural awareness in LLMs for Haitian Creole, a language spoken by millions but severely underrepresented in digital resources. [Source: arXiv 2609.31506 abstract (retrieved {DATE})]
""",
        encoding="utf-8",
    )
    print("wrote CCC", dest)

    clog = CCC / "log.md"
    if clog.is_file():
        head = clog.read_text(encoding="utf-8")
        entry = f"""## [{DATE}] cross-wiki | OOD Haitian Creole cultural LLM eval (from Cybersec)

- **OOD route** — arXiv 2609.31506 cultural-awareness infilling/story eval for Haitian Creole. NLP primary. Cybersec OOD stub `@cybersecurity-wiki/{CYBER_OOD}`.
- **friend brief:** n/a

"""
        if "2609.31506" not in head:
            clog.write_text(entry + head, encoding="utf-8")
            print("patched CCC log.md")

    cidx = CCC / "index.md"
    if cidx.is_file():
        it = cidx.read_text(encoding="utf-8")
        row = "| [`arxiv-2609-31506-haitian-creole-cultural-awareness-ood-2026-09-28`](sources/arxiv-2609-31506-haitian-creole-cultural-awareness-ood-2026-09-28.md) | draft | Haitian Creole cultural LLM eval OOD — 2609.31506 (from Cybersec) |\n"
        needle = "| [`arxiv-muslim-arabic-voice-ai-platform-2609.31511`](sources/arxiv-muslim-arabic-voice-ai-platform-2609.31511.md) | draft | Muslim voice platform OOD — 2609.31511 |\n"
        if "2609.31506" not in it and needle in it:
            cidx.write_text(it.replace(needle, needle + row, 1), encoding="utf-8")
            print("patched CCC index.md")


def main() -> int:
    src(
        "arxiv-2609-30383-skill-cascading-attacks",
        "Stealth apart, harm together: skill cascading attacks on skill-based agents",
        "2609.30383",
        "K374",
        "arxiv-2609.30383-stealth-apart-harm-together-skill-cascading-atta.pdf",
        "**K374** — skill-based agents (Claude Code, OpenClaw, Codex; ClawHub third-party skills) share one **context window**. **Skill cascading** splits a harmful objective across two or more skills so each skill **passes per-skill scan**, the **joint run harms** a realistic request, and **reverting any one skill removes the harm**. SKILLCASCADE-BENCH: **213** validated cases; paper reports ~**89.4%** joint harm while evading per-skill / joint-skill scanners and runtime monitors. Patterns named: **causal**, **compositional**, **hybrid**. Operator steal: treat **skill suites as one unit**; audit **shared-context** writes, not only SKILL.md files. **No cascade recipes or skill payloads in wiki.** **Runtime:** `scripts/k374_skill_cascading_precheck.py`. Pairs K317 EvoSkill + skill injection / misevolution.",
        "concepts/skill-cascading-attacks-cross-skill.md",
        [
            "concepts/agent-skill-injection.md",
            "concepts/skill-misevolution.md",
            "concepts/evoskill-injection-self-evolving-agents.md",
        ],
        wire=".cursor/rules/cemini-cybersec-lab-redteam.mdc (K374)",
    )
    concept_page(
        "skill-cascading-attacks-cross-skill",
        "Skill cascading attacks (cross-skill)",
        "K374",
        "2609.30383",
        "Per-skill integrity is **not** system-level safety when skills share a context window. Before installing a **vendor suite**, require a **joint-skill** review: what each skill writes into shared context, and whether later skills consume that text as authority. HITL on single SKILL.md files does not cover cascade. Authorized lab only; **no attack payloads in wiki**.",
        [
            "sources/arxiv-2609-30383-skill-cascading-attacks.md",
            "concepts/agent-skill-injection.md",
            "concepts/skill-misevolution.md",
            "concepts/evoskill-injection-self-evolving-agents.md",
        ],
        ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K374)",
    )

    src(
        "arxiv-2609-31318-agentxploit-repo-to-runtime",
        "AgentXploit: autonomous repository-to-runtime red-teaming for AI agents",
        "2609.31318",
        "K375",
        "arxiv-2609.31318-agentxploit-autonomous-repository-to-runtime-red.pdf",
        "**K375** — authorized **white-box pre-deployment** audit of agent repos: **Analyzer** traces attacker-controlled inputs to sensitive operations and writes **code-supported candidate paths**; **Exploiter** may act **only** through the task-defined attacker interface on an **isolated target**; an **external deterministic verifier** (not the agent) scores success. AgentXploit-Bench: **72** pinned instances / **12** systems; paper reports **59.3%** end-to-end vs Codex **38.4%** (token-matched Codex **46.3%**). Discovery and exploitation are **distinct** failure modes. Repo `github.com/lwd17/AgentXploit` is **REFERENCE — no clone this batch**; **no exploit payloads in wiki**. **Runtime:** `scripts/k375_agentxploit_precheck.py`. Pairs K327 taxonomy + K341 pentest agents.",
        "concepts/agentxploit-repo-to-runtime-redteam.md",
        ["concepts/black-box-agentic-redteam-taxonomy.md"],
        wire=".cursor/rules/cemini-cybersec-lab-redteam.mdc (K375)",
    )
    concept_page(
        "agentxploit-repo-to-runtime-redteam",
        "AgentXploit repository-to-runtime red-team",
        "K375",
        "2609.31318",
        "Split **path discovery** (repository evidence) from **runtime confirmation** (attacker interface + isolated target). Count a finding only when an **external verifier** confirms the security outcome. Do not treat coding-agent traces as the verdict. Written-scope / owned harness only. **No attack payloads in wiki.**",
        [
            "sources/arxiv-2609-31318-agentxploit-repo-to-runtime.md",
            "concepts/black-box-agentic-redteam-taxonomy.md",
        ],
        ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K375)",
    )

    w(
        CYBER_OOD,
        f"""---
title: "Evaluating cultural awareness of LLMs for Haitian Creole (OOD)"
type: source
tags: [source, ood]
keywords: [2609.31506, ood]
related:
  - "@ccc-wiki/{CCC_OOD}"
maturity: draft
read_status: read
created: {DATE}
updated: {DATE}
phase_0_verdict: "REFERENCE {DATE} — OOD NLP cultural eval; no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (OOD)"
cross-wiki-source: "@ccc-wiki/{CCC_OOD}"
---

## Relations

- @ccc-wiki/{CCC_OOD} — CCC wiki **primary steal** (Haitian Creole cultural LLM eval).

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Evaluating Cultural Awareness of LLMs for Haitian Creole (OOD) |
| arXiv | 2609.31506 |
| Location | {EGRESS}/arxiv-2609.31506-evaluating-cultural-awareness-of-llms-for-haitia.pdf |
| Retrieved | {DATE} |
| Read status | read (abstract + triage) |

## Narrative

Multilingual **cultural-awareness** eval for Haitian Creole (entity infilling + story generation; native-speaker prompts). **NLP / culture** primary, not cyber-primary. **OOD stub** routed to @ccc-wiki ({DATE}).

## Snippets

> See arXiv 2609.31506 abstract. [Source: arXiv 2609.31506 (retrieved {DATE})]
""",
    )

    src(
        "arxiv-2609-31552-fragtoken-inference-cost-amplification",
        "FragToken: amplifying LLM inference costs through noncanonical token generation",
        "2609.31552",
        "K376",
        "arxiv-2609.31552-fragtoken-amplifying-llm-inference-costs-through.pdf",
        "**K376** — tokenizer **decode is not injective**: the same visible text can map to a **longer noncanonical token sequence**, so decoding steps (and billable tokens) can rise without a matching visible-length increase. Paper frames a **training-time / third-party model** supply-chain threat (TIR **1.99–2.46** on four models; utility mostly held). Operator steal: on **owned or procured** models, report **token count vs visible length**; treat unexpected inflation as a **provenance** signal for fine-tunes. **Do not train FragToken. No fragmentation recipes in wiki.** **Runtime:** `scripts/k376_fragtoken_precheck.py`. Pairs K366 reliable-inference procurement.",
        "concepts/fragtoken-noncanonical-token-cost-audit.md",
        ["concepts/reliable-inference-procurement-routing.md"],
        wire=".cursor/rules/cemini-cybersec-agent-audit.mdc (K376)",
    )
    concept_page(
        "fragtoken-noncanonical-token-cost-audit",
        "Noncanonical token inference-cost audit",
        "K376",
        "2609.31552",
        "Measure **token inflation ratio** against **visible text length** on ordinary prompts. A third-party or fine-tuned model that burns extra decode steps without longer answers is a **cost / availability** supply-chain issue. Keep tokenizer and serving stack vendor-canonical. **No attack training procedures in wiki.**",
        [
            "sources/arxiv-2609-31552-fragtoken-inference-cost-amplification.md",
            "concepts/reliable-inference-procurement-routing.md",
        ],
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (K376)",
    )

    src(
        "arxiv-2609-31575-configuration-not-conscience-system-prompts",
        "Configuration, not conscience: a large-scale empirical study of LLM system prompts",
        "2609.31575",
        "K377",
        "arxiv-2609.31575-configuration-not-conscience-a-large-scale-empir.pdf",
        "**K377** — merged corpus of **407** leaked / reconstructed / official system prompts from **62** vendors (29 near-duplicate clusters / 66 files). Operational text dominates: ~**58%** classified words **tool/protocol**, ~**5%** **safety policy**; strictest rule-lines guard **tool use and file safety** over harmful-content by ~**11:1**. Treat leaked prompts as **operational configuration and supply-chain**, not vendor values. Prompt **rot** (version chains, stale refs, contradictions) is a maintenance debt. Authors publish **no new extraction** and report vendor aggregates. **Do not clone leak corpora. Do not paste leaked prompt bodies into wiki.** Audit-only (no precheck script). Pairs system-prompt leakage (LLM07).",
        "concepts/system-prompt-operational-configuration-corpus.md",
        ["concepts/system-prompt-leakage.md"],
        wire=".cursor/rules/cemini-cybersec-agent-audit.mdc (K377)",
    )
    concept_page(
        "system-prompt-operational-configuration-corpus",
        "System prompts as operational configuration",
        "K377",
        "2609.31575",
        "Audit **your** system prompts as **config files**: tool/protocol weight vs safety-policy weight, version drift, and reuse. A leak is not a confession of vendor ethics. Do not ingest public leak dumps into the lab. Pairs LLM07 leakage pages — this page is **composition**, not extraction.",
        [
            "sources/arxiv-2609-31575-configuration-not-conscience-system-prompts.md",
            "concepts/system-prompt-leakage.md",
        ],
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (K377)",
    )

    add_related(
        "concepts/agent-skill-injection.md",
        "concepts/skill-cascading-attacks-cross-skill.md",
        "K374 cross-skill cascade: per-skill scan misses joint harm",
    )
    add_related(
        "concepts/skill-misevolution.md",
        "concepts/skill-cascading-attacks-cross-skill.md",
        "K374 skill-suite cascade vs evolve-gate misevolution",
    )
    add_related(
        "concepts/evoskill-injection-self-evolving-agents.md",
        "concepts/skill-cascading-attacks-cross-skill.md",
        "K374 cascade (installed suite) vs K317 generation pipeline",
    )
    add_related(
        "concepts/black-box-agentic-redteam-taxonomy.md",
        "concepts/agentxploit-repo-to-runtime-redteam.md",
        "K375 white-box repo-to-runtime complement to K327 black-box taxonomy",
    )
    add_related(
        "concepts/reliable-inference-procurement-routing.md",
        "concepts/fragtoken-noncanonical-token-cost-audit.md",
        "K376 token inflation vs visible length on procured models",
    )
    add_related(
        "concepts/system-prompt-leakage.md",
        "concepts/system-prompt-operational-configuration-corpus.md",
        "K377 leaked prompts are ops config; composition not extraction",
    )

    patch_index()
    write_ccc_ood()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
