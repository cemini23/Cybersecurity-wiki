#!/usr/bin/env python3
"""Writer for K378–K381 ingest + RISE OOD (2026-09-29). No attack payloads in wiki."""
from __future__ import annotations

import re
from pathlib import Path

WIKI = Path(__file__).resolve().parents[1] / "wiki"
IMG = Path(__file__).resolve().parents[2] / "Image gen" / "wiki"
EGRESS = "cemini-egress-fi:/opt/cemini-bulk/research/cybersec"
DATE = "2026-09-29"
IMG_OOD = "sources/arxiv-2609-34920-rise-t2i-iterative-strategy-redteam-2026-09-29.md"
CYBER_OOD = "sources/arxiv-2609-34920-rise-t2i-redteam-ood.md"


def w(rel: str, body: str) -> None:
    p = WIKI / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(body, encoding="utf-8")
    print("wrote", rel)


def wimg(rel: str, body: str) -> None:
    p = IMG / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(body, encoding="utf-8")
    print("wrote image-gen", rel)


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
        else f".cursor/rules/cemini-cybersec-lab-redteam.mdc ({kid})"
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
| @sources/arxiv-2609-32400-skilldre-dual-stage-skill-red-team-evolution.md | draft | SkillDRE dual-stage skill evolution (2609.32400; K378) |
| @concepts/skilldre-dual-stage-malicious-skill-evolution-lab.md | draft | Pre-scan vs runtime defense feedback loop |
| @sources/arxiv-2609-33628-climbing-hill-curriculum-prompt-injection-redteam.md | draft | Curriculum RL prompt-injection red-team (2609.33628; K379) |
| @concepts/curriculum-prompt-injection-redteam-frontier-models.md | draft | Cold-start curriculum for frontier PI red-team |
| @{CYBER_OOD} | draft | OOD RISE T2I iterative strategy red-team (2609.34920) |
| @sources/arxiv-2609-35663-late-attention-entity-token-copying.md | draft | Late-layer entity token copying (2609.35663; K380) |
| @concepts/late-attention-entity-token-copying-interpretability.md | draft | Entity copy vs context dependence (audit) |
| @sources/arxiv-2609-35699-distillation-defenses-break-after-reinforcement-learning.md | draft | Distillation defenses vs post-distill RL (2609.35699; K381) |
| @concepts/distillation-defense-reinforcement-learning-threat-model.md | draft | Re-eval defenses after attacker RL continuation |
"""
    needle = "| @concepts/llm-system-prompt-corpus-audit.md | draft | Leaked prompt composition audit |"
    if "K378" not in text and needle in text:
        text = text.replace(needle, needle + block, 1)
        idx.write_text(text, encoding="utf-8")
        print("patched index.md")


def write_image_gen_ood() -> None:
    if not IMG.is_dir():
        print("skip image-gen wiki (missing)")
        return
    wimg(
        IMG_OOD,
        f"""---
title: "RISE: iterative strategy evolution red-teaming for text-to-image models (from Cybersec OOD)"
type: source
tags: [source, ood, t2i, red-team, safety]
keywords: [2609.34920, rise, t2i, red-team, ood]
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
| Title | RISE: Red-teaming via Iterative Strategy Evolution for Modern Text-to-Image Models |
| arXiv | 2609.34920 |
| Location | {EGRESS}/arxiv-2609.34920-rise-red-teaming-via-iterative-strategy-evolutio.pdf |
| Retrieved | {DATE} |

## Narrative

**RISE** evolves **reusable attack strategies** for hardened T2I APIs, with **strict category-specific success criteria** and **VLM judges calibrated to human labels**. Paper reports up to **~13% human-verified ASR** where older pipelines with ~30% reported ASR fall to **near zero** under the same calibration. **Image-gen / content-policy primary** — authorized provider eval only; **no prompt or strategy payloads in wiki**.

## Snippets

> RISE evolves reusable strategies used to generate prompts rather than rewriting them one by one. [Source: arXiv 2609.34920 abstract (retrieved {DATE})]
""",
    )
    ilog = IMG / "log.md"
    if ilog.is_file():
        head = ilog.read_text(encoding="utf-8")
        entry = f"""## [{DATE}] cross-wiki | OOD RISE T2I red-team (from Cybersec)

- **OOD route** — arXiv 2609.34920 RISE iterative strategy evolution for modern T2I. Image-gen primary. Cybersec OOD `@cybersecurity-wiki/{CYBER_OOD}`.

"""
        if "2609.34920" not in head:
            ilog.write_text(entry + head, encoding="utf-8")
            print("patched image-gen log.md")


def main() -> int:
    src(
        "arxiv-2609-32400-skilldre-dual-stage-skill-red-team-evolution",
        "SkillDRE: dual-stage red-team evolution of agent skills via pre-execution and runtime feedback",
        "2609.32400",
        "K378",
        "arxiv-2609.32400-skilldre-dual-stage-red-team-evolution-of-agent.pdf",
        "**K378** — agent skills package instructions, code, and resources that improve from execution feedback; the same loop can evolve **malicious** skills. A candidate may pass **pre-execution scan** yet fail under **runtime defenses**, while a runtime repair can reintroduce scanner findings. **SkillDRE** holds a task-conditioned malicious objective and judge rule fixed, then evolves the skill implementation in a **dual-stage closed loop** (scanner-guided evolution ↔ runtime-guided refinement) while **preserving benign task capability**. SkillsBench (four victim models): paper reports average ASR **45.28%** (~**40.3%** above strongest baseline) with final skills clearing SkillScan findings. Repo `github.com/whfeLingYu/SkillDRE` is **REFERENCE — null SPDX; do not clone**. **No skill bodies or attack payloads in wiki.** **Runtime:** `scripts/k378_skilldre_precheck.py`. Pairs skill injection / misevolution / EvoSkill / K374 cascading.",
        "concepts/skilldre-dual-stage-malicious-skill-evolution-lab.md",
        [
            "concepts/agent-skill-injection.md",
            "concepts/skill-misevolution.md",
            "concepts/evoskill-injection-self-evolving-agents.md",
            "concepts/skill-cascading-attacks-skill-based-agents.md",
        ],
        wire=".cursor/rules/cemini-cybersec-lab-redteam.mdc (K378)",
    )
    concept_page(
        "skilldre-dual-stage-malicious-skill-evolution-lab",
        "SkillDRE dual-stage malicious skill evolution",
        "K378",
        "2609.32400",
        "Pre-execution scan and runtime defense are **different gates**. Lab eval of skill evolution must close the loop across both stages and keep a **benign-task** metric alongside attack success. HITL before evolving skills in an owned harness. **Do not clone** null-SPDX SkillDRE. **No skill payloads in wiki.**",
        [
            "sources/arxiv-2609-32400-skilldre-dual-stage-skill-red-team-evolution.md",
            "concepts/agent-skill-injection.md",
            "concepts/skill-misevolution.md",
            "concepts/evoskill-injection-self-evolving-agents.md",
            "concepts/skill-cascading-attacks-skill-based-agents.md",
        ],
        ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K378)",
    )

    src(
        "arxiv-2609-33628-climbing-hill-curriculum-prompt-injection-redteam",
        "Climbing the hill: prompt injection red-teaming against frontier models with curriculum reinforcement learning",
        "2609.33628",
        "K379",
        "arxiv-2609.33628-climbing-the-hill-prompt-injection-red-teaming-a.pdf",
        "**K379** — RL attacker LLMs for prompt injection hit a **cold-start** wall on frontier targets: every attempt fails, reward stays zero, and learning stalls. **Curriculum** training walks the attacker through a sequence of **increasingly robust** targets, with each stage warm-starting from the prior attacker; after each stage the attacker must **partially succeed** on the next target so learning signals continue. Paper reports AgentDyn ASR@10 of **93.8%** / **45.0%** on named frontier pairs where single-shot RL baselines stay at **0%**. Operator steal: document the curriculum and cold-start, use **owned / written-scope frontier lab only**, report harness + judge. **No injection payloads in wiki.** **Runtime:** `scripts/k379_curriculum_pi_redteam_precheck.py`. Pairs K327 black-box agentic red-team taxonomy.",
        "concepts/curriculum-prompt-injection-redteam-frontier-models.md",
        ["concepts/black-box-agentic-redteam-taxonomy.md"],
        wire=".cursor/rules/cemini-cybersec-lab-redteam.mdc (K379)",
    )
    concept_page(
        "curriculum-prompt-injection-redteam-frontier-models",
        "Curriculum prompt-injection red-team for frontier models",
        "K379",
        "2609.33628",
        "Single-shot RL against a hardened frontier model often yields **no learning signal**. Prefer a **documented curriculum** of rising target strength with partial success between stages. Owned / written-scope lab only; record harness and judge. **No injection payloads in wiki.**",
        [
            "sources/arxiv-2609-33628-climbing-hill-curriculum-prompt-injection-redteam.md",
            "concepts/black-box-agentic-redteam-taxonomy.md",
        ],
        ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K379)",
    )

    w(
        CYBER_OOD,
        f"""---
title: "RISE: T2I iterative strategy evolution red-team (OOD)"
type: source
tags: [source, ood]
keywords: [2609.34920, ood, t2i, rise]
related:
  - "@image-gen-wiki/{IMG_OOD}"
maturity: draft
read_status: read
created: {DATE}
updated: {DATE}
phase_0_verdict: "REFERENCE {DATE} — OOD T2I red-team; image-gen primary; no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (OOD)"
cross-wiki-source: "@image-gen-wiki/{IMG_OOD}"
---

## Relations

- @image-gen-wiki/{IMG_OOD} — image-gen wiki **primary steal** (RISE T2I iterative strategy red-team).

## Raw Concept

| Field | Value |
|-------|-------|
| Title | RISE: Red-teaming via Iterative Strategy Evolution for Modern Text-to-Image Models |
| arXiv | 2609.34920 |
| Location | {EGRESS}/arxiv-2609.34920-rise-red-teaming-via-iterative-strategy-evolutio.pdf |
| Retrieved | {DATE} |
| Read status | read (abstract + triage) |

## Narrative

**RISE** evolves **reusable attack strategies** for hardened T2I APIs under **strict category-specific success criteria** and **VLM judges calibrated to human labels**. Paper reports up to ~**13%** human-verified ASR where older pipelines with ~30% reported ASR fall to **near zero** under the same calibration. **Image-gen / content-policy primary** — cybersec keeps this **OOD stub** only. **No prompt or strategy payloads in wiki.**

## Snippets

> See arXiv 2609.34920 abstract. [Source: arXiv 2609.34920 (retrieved {DATE})]
""",
    )

    src(
        "arxiv-2609-35663-late-attention-entity-token-copying",
        "Late attention layers alone can copy entity tokens, but not without attending to their context",
        "2609.35663",
        "K380",
        "arxiv-2609.35663-late-attention-layers-alone-can-copy-entity-toke.pdf",
        "**K380** — LLMs perform **entity copying** (copy entity tokens from the prompt into the answer). On Qwen3-8B, **late layers in the second half** of the model are necessary and sufficient for that copy; **context-token attention to the entity tokens** is also required for exact copy, even when those context tokens do not store the entity themselves. Audit steal: interpretability and provenance work should not treat entity copy as a late-layer-only trick without context attention. **Audit only — no precheck script.** **No attack payloads in wiki.**",
        "concepts/late-attention-entity-token-copying-interpretability.md",
        wire=".cursor/rules/cemini-cybersec-agent-audit.mdc (K380)",
    )
    concept_page(
        "late-attention-entity-token-copying-interpretability",
        "Late-attention entity token copying",
        "K380",
        "2609.35663",
        "Entity copy depends on **late layers** plus **context attention** to the entity tokens. Treat copy behavior as context-guided, not a isolated late-layer shortcut. Audit / interpretability framing only.",
        [
            "sources/arxiv-2609-35663-late-attention-entity-token-copying.md",
        ],
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (K380)",
    )

    src(
        "arxiv-2609-35699-distillation-defenses-break-after-reinforcement-learning",
        "Distillation defenses easily break after reinforcement learning",
        "2609.35699",
        "K381",
        "arxiv-2609.35699-distillation-defenses-easily-break-after-reinfor.pdf",
        "**K381** — distillation-theft defenses are often scored **right after distillation**, which understates attackers who continue with **reinforcement learning**. Post-distill RL can restore reasoning that looked blocked at the distill checkpoint; simple trace collection from current APIs can match more elaborate hidden-trace theft once RL continues. Operator steal: threat models must include **post-distill RL**; re-eval defenses with **pre- and post-RL** metrics on **owned or procured** models. **No distillation attack recipes in wiki.** **Runtime:** `scripts/k381_distillation_defense_rl_precheck.py`.",
        "concepts/distillation-defense-reinforcement-learning-threat-model.md",
        wire=".cursor/rules/cemini-cybersec-agent-audit.mdc (K381)",
    )
    concept_page(
        "distillation-defense-reinforcement-learning-threat-model",
        "Distillation defense vs post-distill RL",
        "K381",
        "2609.35699",
        "A defense that looks strong **immediately after distillation** can fail after the attacker continues with **RL**. Require dual metrics (pre-RL and post-RL) on owned or procured models. **No attack recipes in wiki.**",
        [
            "sources/arxiv-2609-35699-distillation-defenses-break-after-reinforcement-learning.md",
        ],
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (K381)",
    )

    add_related(
        "concepts/agent-skill-injection.md",
        "concepts/skilldre-dual-stage-malicious-skill-evolution-lab.md",
        "K378 dual-stage skill evolution (pre-exec + runtime) lab gate",
    )
    add_related(
        "concepts/skill-misevolution.md",
        "concepts/skilldre-dual-stage-malicious-skill-evolution-lab.md",
        "K378 SkillDRE evolution loop vs misevolution evolve-gate",
    )
    add_related(
        "concepts/evoskill-injection-self-evolving-agents.md",
        "concepts/skilldre-dual-stage-malicious-skill-evolution-lab.md",
        "K378 dual-stage evolution vs K317 EvoSkill generation pipeline",
    )
    add_related(
        "concepts/skill-cascading-attacks-skill-based-agents.md",
        "concepts/skilldre-dual-stage-malicious-skill-evolution-lab.md",
        "K378 evolving one skill package vs K374 cross-skill cascade",
    )
    add_related(
        "concepts/black-box-agentic-redteam-taxonomy.md",
        "concepts/curriculum-prompt-injection-redteam-frontier-models.md",
        "K379 curriculum RL cold-start for frontier prompt-injection red-team",
    )
    # Source pages list extra_related concepts — those concepts must backlink the source.
    for rel in (
        "concepts/agent-skill-injection.md",
        "concepts/skill-misevolution.md",
        "concepts/evoskill-injection-self-evolving-agents.md",
        "concepts/skill-cascading-attacks-skill-based-agents.md",
    ):
        add_related(
            rel,
            "sources/arxiv-2609-32400-skilldre-dual-stage-skill-red-team-evolution.md",
            "K378 SkillDRE dual-stage skill evolution source",
        )
    add_related(
        "concepts/black-box-agentic-redteam-taxonomy.md",
        "sources/arxiv-2609-33628-climbing-hill-curriculum-prompt-injection-redteam.md",
        "K379 curriculum PI red-team source",
    )

    # Repair K374 related backlinks that pointed at a non-existent cross-skill slug.
    for rel in (
        "concepts/agent-skill-injection.md",
        "concepts/skill-misevolution.md",
        "concepts/evoskill-injection-self-evolving-agents.md",
    ):
        p = WIKI / rel
        t = p.read_text(encoding="utf-8")
        if "concepts/skill-cascading-attacks-cross-skill.md" in t:
            t = t.replace(
                "concepts/skill-cascading-attacks-cross-skill.md",
                "concepts/skill-cascading-attacks-skill-based-agents.md",
            )
            t = bump_updated(t)
            p.write_text(t, encoding="utf-8")
            print("fixed cascading related slug", rel)
        add_related(
            rel,
            "concepts/skill-cascading-attacks-skill-based-agents.md",
            "K374 cross-skill cascade: suite-as-unit shared-context audit",
        )

    patch_index()
    write_image_gen_ood()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
