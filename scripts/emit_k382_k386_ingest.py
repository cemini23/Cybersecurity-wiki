#!/usr/bin/env python3
"""Writer for K382–K386 ingest (2026-09-30). No attack payloads in wiki."""
from __future__ import annotations

import re
from pathlib import Path

WIKI = Path(__file__).resolve().parents[1] / "wiki"
EGRESS = "cemini-egress-fi:/opt/cemini-bulk/research/cybersec"
DATE = "2026-09-30"


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
    wire: str = "",
) -> None:
    rels = ([f"  - {concept}"] if concept else []) + [f"  - {r}" for r in (extra_related or [])]
    rel_yaml = "related:\n" + "\n".join(rels) if rels else "related: []"
    rel_sec = f"\n## Relations\n\n- @{concept}\n" if concept else "\n## Relations\n\n"
    if extra_related:
        rel_sec += "".join(f"- @{r}\n" for r in extra_related)
    wire_line = wire or f".cursor/rules/cemini-cybersec-lab-redteam.mdc ({kid})"
    body = f"""---
title: "{title}"
type: source
tags: [source, arxiv, agent-security]
keywords: [{arxiv}, {kid.lower()}]
{rel_yaml}
maturity: draft
read_status: read
created: {DATE}
updated: {DATE}
phase_0_verdict: "REFERENCE {DATE} — no attack payloads in wiki."
wire_status: policy_wired
wire_target: "{wire_line}"
---

## Relations
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

> See arXiv {arxiv} abstract. [Source: arXiv {arxiv} (retrieved {DATE})]
"""
    w(f"concepts/{slug}.md", body)


def patch_index() -> None:
    idx = WIKI / "index.md"
    text = idx.read_text(encoding="utf-8")
    block = """
| @sources/arxiv-2609-36474-finrt-amortized-redteam-generator.md | draft | FinRT amortized adversarial-generator red-team (2609.36474; K382) |
| @concepts/finrt-amortized-redteam-generator.md | draft | Amortize red-team search into a reusable generator |
| @sources/arxiv-2609-36570-countersteer-activation-steering-ipi-defense.md | draft | CounterSteer inference-time IPI steering (2609.36570; K383) |
| @concepts/countersteer-activation-steering-ipi-defense.md | draft | Always-on tool-span steering vs indirect prompt injection |
| @sources/arxiv-2609-36739-frontier-autolab-temporal-leakage.md | draft | Frontier Autolab org-memory temporal leakage (2609.36739; K384) |
| @concepts/frontier-autolab-organizational-memory-leakage.md | draft | Leakage measures for historically scored agent evals |
| @sources/arxiv-2609-38021-auditable-long-term-memory-retrieval-chain.md | draft | Auditable long-term memory retrieval chain (2609.38021; K385) |
| @concepts/auditable-long-term-memory-retrieval-chain.md | draft | Deterministic retrieval chain for agent memory audit |
| @sources/arxiv-2609-38099-rice-in-context-dense-retrieval.md | draft | RICE in-context dense retrieval (2609.38099; K386) |
| @concepts/rice-in-context-dense-retrieval.md | draft | Dense retrieval trained from in-context examples only |
"""
    needle = "| @concepts/distillation-defense-reinforcement-learning-threat-model.md | draft | Re-eval defenses after attacker RL continuation |"
    if "K382" not in text and needle in text:
        text = text.replace(needle, needle + block, 1)
        idx.write_text(text, encoding="utf-8")
        print("patched index.md")
    else:
        print("index.md already patched or needle missing")


def main() -> int:
    # ---- K382 FinRT -------------------------------------------------------
    src(
        "arxiv-2609-36474-finrt-amortized-redteam-generator",
        "FinRT: distilling adaptive red-teaming strategies into reusable adversarial generators in consumer finance",
        "2609.36474",
        "K382",
        "arxiv-2609.36474-finrt-distilling-adaptive-red-teaming-strategies.pdf",
        "**K382** — automated red-teaming trades attack effectiveness against generation cost and treats coverage, severity, and diversity as incidental. **FinRT** separates search from generation: forward elicitation searches policy × domain × strategy and scores attackability (uncensored surrogate), realism, and structural fidelity; inverse elicitation fine-tunes a **reusable adversarial-prompt generator** (Mistral-7B + LoRA) on spec → prompt pairs; **calibrated proxy DPO** approximates target-specific DPO from a small calibration subset. Held-out consumer finance (419 policy–domain–behavior specs, six victim models, K=10): ASR **32.9%** (FinRT-DPO-calibrated) vs Rainbow Teaming **17.2%** and PAIR-Lite **15.5%**; max severity **3.54** vs **2.66**; realism-constrained coverage@10 **1.0** vs **0.86**. Cost is front-loaded (~1.52M target-independent LLM calls) and **amortized**, not cheaper. Operator steal: report ASR + severity + realism-constrained coverage + diversity **jointly**; human-audit a sample of judge labels (97.9% agreement on 700); keep the reusable generator separate from target-facing calls. **No repo; the authors withhold high-severity prompts and target adapters.** **Runtime:** `scripts/k382_finrt_amortized_redteam_precheck.py`. Pairs K313 red-team skill evolution and K248 PIMiner.",
        "concepts/finrt-amortized-redteam-generator.md",
        [
            "concepts/experience-driven-redteam-skill-evolution.md",
            "concepts/piminer-agentic-prompt-injection-redteam.md",
            "concepts/ai-redteam-evidential-ceiling.md",
        ],
        wire=".cursor/rules/cemini-cybersec-lab-redteam.mdc (K382)",
    )
    concept_page(
        "finrt-amortized-redteam-generator",
        "FinRT amortized adversarial-generator red-team",
        "K382",
        "2609.36474",
        "Separate red-team **search** from **generation**: search once, then amortize into a reusable generator. Score **coverage, severity, realism, and diversity jointly** — success rate alone hides regressions. Use **realism-constrained coverage**, not raw prompt count. Report the offline generator cost and what it is amortized over. Human-audit judge labels. **No high-severity prompts or target adapters in wiki.**",
        [
            "sources/arxiv-2609-36474-finrt-amortized-redteam-generator.md",
            "concepts/experience-driven-redteam-skill-evolution.md",
            "concepts/piminer-agentic-prompt-injection-redteam.md",
            "concepts/ai-redteam-evidential-ceiling.md",
        ],
        ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K382)",
    )

    # ---- K383 CounterSteer ------------------------------------------------
    src(
        "arxiv-2609-36570-countersteer-activation-steering-ipi-defense",
        "CounterSteer: suppressing indirect prompt injection with activation steering",
        "2609.36570",
        "K383",
        "arxiv-2609.36570-countersteer-suppressing-indirect-prompt-injecti.pdf",
        "**K383** — indirect prompt injection (IPI) makes an agent treat untrusted retrieved text as instructions. **CounterSteer** is an **inference-time** defense: per model, a five-step recipe fits a residual-stream direction from paired episodes that differ only in whether an embedded instruction is followed, keeps it only if it passes pre-specified **causal** (subtract lowers follow, add raises follow) and **capability** gates, then subtracts a fixed dose from **every tool-result token during prefill**. Always-on — no detector to evade; needs white-box serving + tool-span tags; no fine-tune, auxiliary model, or added tokens. Five open-weights models (8B–106B): held-out ASR **0.00–0.17** vs **0.21–1.00** undefended; AgentDojo compromise **0.006–0.079** vs **0.10–0.49**; benign utility **93–100%** typography-normalized. None of **2,052** replayed LLMail-Inject attacks succeeds. **Residual gap:** parameter manipulation — attacker-chosen arguments in otherwise legitimate calls — is only partly resisted (**13/18** cracked); steering does not remove it, so pair with **argument-provenance controls**. Artifact ships attack drivers (**code-available**, license not stated) → **no clone**. **Runtime:** `scripts/k383_countersteer_ipi_precheck.py`. Pairs K248 PIMiner and IPI detector calibration.",
        "concepts/countersteer-activation-steering-ipi-defense.md",
        [
            "concepts/prompt-injection-detector-calibration.md",
            "concepts/piminer-agentic-prompt-injection-redteam.md",
        ],
        wire=".cursor/rules/cemini-cybersec-mcp-tool-control.mdc (K383)",
    )
    concept_page(
        "countersteer-activation-steering-ipi-defense",
        "CounterSteer inference-time IPI steering defense",
        "K383",
        "2609.36570",
        "A **suppression** defense, not a detector: fit one residual direction per model, gate it causally and on capability, then subtract it from **every tool-result token at prefill**. Always on, so there is no detection decision to evade. Needs **white-box serving** and marked tool-result spans. **Steering does not fix parameter manipulation** — add argument-provenance controls. **No injection payloads or fitted directions in wiki.**",
        [
            "sources/arxiv-2609-36570-countersteer-activation-steering-ipi-defense.md",
            "concepts/prompt-injection-detector-calibration.md",
            "concepts/piminer-agentic-prompt-injection-redteam.md",
        ],
        ".cursor/rules/cemini-cybersec-mcp-tool-control.mdc (K383)",
    )

    # ---- K384 Frontier Autolab -------------------------------------------
    src(
        "arxiv-2609-36739-frontier-autolab-temporal-leakage",
        "Frontier Autolab: organizational memory, adversarial dissent and temporal leakage in multi-agent LLM firms",
        "2609.36739",
        "K384",
        "arxiv-2609.36739-frontier-autolab-organizational-memory-adversari.pdf",
        "**K384** — multi-agent LLM systems are structured like firms but evaluated on minute-long tasks. **Frontier Autolab** runs one simulated firm (16 personas + a Red Team) through nine temporally gated eras, 1990–2040; a historian-judge reveals outcomes and scores a five-dimension rubric; lessons enter a persistent Playbook. Across four trajectories (36 era decisions, 180 subscores): a **foresight–commitment gap** in **24/24** historically scored eras (mean gap **1.88**, SD 0.80) — the judge rated recognition of the coming shift above the choice of where to build. Design shaped character: a Red Team with numeric **kill gates** produced fifty simulated years of gated pilots and **no product**, yet scored the highest. The paper also shows why the numbers are hard to trust: published totals rise across eras while the judge's own hindsight subscore falls (within-run **r = −0.58**), confounding apparent learning with recall of history. Operator steal: report a **leakage measure**, **separate the briefing author from the scorer**, compute totals **in code**, and fix the rubric's treatment of **caution** in advance. Repo `github.com/LoopGlitch26/Frontier-Autolab` is **MIT** — REFERENCE (testbed, not a security tool; no clone this batch). **Runtime:** `scripts/k384_frontier_autolab_leakage_precheck.py`. Pairs GT-MCP trajectory-context-control and K238 memory poisoning.",
        "concepts/frontier-autolab-organizational-memory-leakage.md",
        [
            "concepts/trajectory-context-control.md",
            "concepts/salami-collusive-memory-poisoning.md",
        ],
        wire=".cursor/rules/cemini-cybersec-agent-audit.mdc (K384)",
    )
    concept_page(
        "frontier-autolab-organizational-memory-leakage",
        "Frontier Autolab organizational memory + temporal leakage",
        "K384",
        "2609.36739",
        "Long-horizon multi-agent evals sit on **temporal leakage**: the judge knows how the era turned out. Require a **hindsight-leakage measure** and a **briefing-selection-leakage** measure, **separate the briefing author from the scorer**, and compute totals **in code**. The judge rated **caution** (numeric kill gates) highest while the firm shipped nothing — fix the rubric's treatment of caution in advance. **No briefing bodies or judge prompts in wiki.**",
        [
            "sources/arxiv-2609-36739-frontier-autolab-temporal-leakage.md",
            "concepts/trajectory-context-control.md",
            "concepts/salami-collusive-memory-poisoning.md",
        ],
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (K384)",
    )

    # ---- K385 Auditable long-term memory ----------------------------------
    src(
        "arxiv-2609-38021-auditable-long-term-memory-retrieval-chain",
        "Auditable long-term memory: a deterministic retrieval chain measured at 479/475 of 500 on LongMemEval-S",
        "2609.38021",
        "K385",
        "arxiv-2609-38021-auditable-long-term-memory-a-deterministic-retri.pdf",
        "**K385** — a long-term-memory answer can fail as a **quiet retrieval miss**: the system never retrieves the session that states the fact, then answers fluently and wrongly. Archivist's auditable chain keeps **stages 1–4 deterministic code** (hybrid candidate retrieval, cross-encoder rerank, coverage-first packet compilation, deterministic scaffolds) and uses the LLM only as a **replaceable final reader**. On LongMemEval-S it places all gold sessions in the candidate pool for **468/470** answerable questions and builds gold-complete packets for **462/470**; the headline reader scores **479/500** and **475/500** across two passes, bracketing Chronos High's **478/500** — the authors state the pair shows **neither superiority nor equivalence**. Operator steal: report **retrieval** metrics separately from the **reader** score; the reader choice moves the score by up to **386** points; measure **judge variance** (second judge 98.6% agreement, 472/500) and **verdict flips** on byte-identical answers; freeze a two-pass promotion rule; run **negative controls** (one verifier repaired 3 wrong drafts but broke **11** correct ones). Measurement-integrity surface: some reader lanes had tools enabled plus ~**59k–62k** characters of extra operator context per call — **not a closed-book measurement**. Repo `github.com/cjchanh/longmemeval-evidence` is **MIT evidence-only** (retrieval and scaffold sources held) — REFERENCE. **Audit only — no precheck script.** Pairs GT-MCP trajectory-context-control and K228 KAMR.",
        "concepts/auditable-long-term-memory-retrieval-chain.md",
        [
            "concepts/trajectory-context-control.md",
            "concepts/kamr-knowledge-aligned-multihop-retrieval.md",
        ],
        wire=".cursor/rules/cemini-cybersec-agent-audit.mdc (K385)",
    )
    concept_page(
        "auditable-long-term-memory-retrieval-chain",
        "Auditable long-term memory retrieval chain",
        "K385",
        "2609.38021",
        "Keep the **retrieval chain deterministic** and the LLM a **replaceable reader**. Report retrieval coverage (gold sessions in the pool, gold-complete packets) **separately** from the reader score, and measure **judge variance** and **verdict flips** on identical answers. Pre-commit a two-pass rule and run **negative controls** before accepting a verifier. Disclose operator context padded into reader calls. **No memory contents or scaffold sources in wiki.**",
        [
            "sources/arxiv-2609-38021-auditable-long-term-memory-retrieval-chain.md",
            "concepts/trajectory-context-control.md",
            "concepts/kamr-knowledge-aligned-multihop-retrieval.md",
        ],
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (K385)",
    )

    # ---- K386 RICE --------------------------------------------------------
    src(
        "arxiv-2609-38099-rice-in-context-dense-retrieval",
        "Effective dense retrieval using only in-context examples",
        "2609.38099",
        "K386",
        "arxiv-2609.38099-effective-dense-retrieval-using-only-in-context.pdf",
        "**K386** — turning a decoder-only LLM into a dense retriever normally needs retriever training. **RICE** is **training-free**: condition both query and document encoding on the **same few in-context query–document pairs**, and take the hidden state before the LM head at the point the model is about to emit one representative word. On 10 BEIR datasets, average Recall@100 rises to **.539** (Qwen3-8B) and **.558** (Qwen3.5-9B) vs PromptReps-Dense **.503** / **.534** — the best among training-free baselines (CSQE .513, HyDE .488) — but stays below supervised **Qwen3-Embedding-8B .645** and **BGE-base-en-v1.5 .578**. Two stated limits carry into RAG ETL: **dynamic document-side exemplars hurt** vs a fixed set, and **random representative words** degrade recall (**.697** vs **.955** on SciFact) — a corrupted or mismatched exemplar set is a retrieval-quality failure mode. Tangential to security: the paper states **no threat model**. Repo `github.com/nourj98/RICE`, license **not stated** → REFERENCE, **no clone**. Pairs K228 KAMR and K328 RAG safety bench.",
        "concepts/rice-in-context-dense-retrieval.md",
        [
            "concepts/kamr-knowledge-aligned-multihop-retrieval.md",
            "concepts/rag-safety-bench-evaluation.md",
        ],
        wire=".cursor/rules/cemini-cybersec-agent-audit.mdc (K386)",
    )
    concept_page(
        "rice-in-context-dense-retrieval",
        "RICE in-context dense retrieval",
        "K386",
        "2609.38099",
        "**Training-free** dense retrieval: give query and document the **same in-context exemplar pairs**, and read the hidden state at the representative-word emission. Beats other training-free baselines but stays below supervised retrievers. For RAG pipelines the operator risk is **exemplar quality**: dynamic document-side exemplars and random representative words both **lower** recall. Audit-only — no precheck.",
        [
            "sources/arxiv-2609-38099-rice-in-context-dense-retrieval.md",
            "concepts/kamr-knowledge-aligned-multihop-retrieval.md",
            "concepts/rag-safety-bench-evaluation.md",
        ],
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (K386)",
    )

    # ---- cross-links into existing concepts -------------------------------
    add_related(
        "concepts/experience-driven-redteam-skill-evolution.md",
        "concepts/finrt-amortized-redteam-generator.md",
        "K382 distills red-team search into a reusable generator (vs K313 skill ratchet)",
    )
    add_related(
        "concepts/piminer-agentic-prompt-injection-redteam.md",
        "concepts/finrt-amortized-redteam-generator.md",
        "K382 amortized generator red-team",
    )
    add_related(
        "concepts/piminer-agentic-prompt-injection-redteam.md",
        "concepts/countersteer-activation-steering-ipi-defense.md",
        "K383 inference-time steering defense against IPI",
    )
    add_related(
        "concepts/prompt-injection-detector-calibration.md",
        "concepts/countersteer-activation-steering-ipi-defense.md",
        "K383 suppression defense: no detector to evade, no calibration gap",
    )
    add_related(
        "concepts/trajectory-context-control.md",
        "concepts/frontier-autolab-organizational-memory-leakage.md",
        "K384 temporal leakage + org memory in long-horizon multi-agent evals",
    )
    add_related(
        "concepts/salami-collusive-memory-poisoning.md",
        "concepts/frontier-autolab-organizational-memory-leakage.md",
        "K384 persistent Playbook memory is a poisoning surface",
    )
    add_related(
        "concepts/trajectory-context-control.md",
        "concepts/auditable-long-term-memory-retrieval-chain.md",
        "K385 deterministic memory retrieval chain + reader/judge variance audit",
    )
    add_related(
        "concepts/kamr-knowledge-aligned-multihop-retrieval.md",
        "concepts/auditable-long-term-memory-retrieval-chain.md",
        "K385 auditable memory retrieval chain",
    )
    add_related(
        "concepts/kamr-knowledge-aligned-multihop-retrieval.md",
        "concepts/rice-in-context-dense-retrieval.md",
        "K386 training-free in-context dense retrieval",
    )
    add_related(
        "concepts/rag-safety-bench-evaluation.md",
        "concepts/rice-in-context-dense-retrieval.md",
        "K386 retrieval quality (exemplar sensitivity) feeds RAG safety evals",
    )

    # Extra-related concepts must backlink the source page (bidirectional).
    _src_backlinks = {
        "sources/arxiv-2609-36474-finrt-amortized-redteam-generator.md": (
            "concepts/experience-driven-redteam-skill-evolution.md",
            "concepts/piminer-agentic-prompt-injection-redteam.md",
            "concepts/ai-redteam-evidential-ceiling.md",
        ),
        "sources/arxiv-2609-36570-countersteer-activation-steering-ipi-defense.md": (
            "concepts/prompt-injection-detector-calibration.md",
            "concepts/piminer-agentic-prompt-injection-redteam.md",
        ),
        "sources/arxiv-2609-36739-frontier-autolab-temporal-leakage.md": (
            "concepts/trajectory-context-control.md",
            "concepts/salami-collusive-memory-poisoning.md",
        ),
        "sources/arxiv-2609-38021-auditable-long-term-memory-retrieval-chain.md": (
            "concepts/trajectory-context-control.md",
            "concepts/kamr-knowledge-aligned-multihop-retrieval.md",
        ),
        "sources/arxiv-2609-38099-rice-in-context-dense-retrieval.md": (
            "concepts/kamr-knowledge-aligned-multihop-retrieval.md",
            "concepts/rag-safety-bench-evaluation.md",
        ),
    }
    for source_ref, concept_refs in _src_backlinks.items():
        for concept_ref in concept_refs:
            add_related(concept_ref, source_ref, "K382–K386 ingest source page")

    patch_index()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
