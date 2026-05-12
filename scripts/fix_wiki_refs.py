#!/usr/bin/env python3
"""Fix slug mismatches + bidirectional gaps in the wiki.

Three passes:
1. Slug correction — replace broken refs (Portuguese accent-stripping artifacts) with actual slugs.
2. Frontmatter cross-wiki strip — `@wiki-alias/...` paths don't belong in `related:` frontmatter; strip them.
3. Bidirectional backlink injection — for every page A whose `related:` lists B, ensure B's `related:` lists A back.

Idempotent: safe to re-run.

Run from repo root:
    python3 scripts/fix_wiki_refs.py
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"

# Map of broken Drive-stub slugs (Portuguese accents collapsed to "-o-") → actual file slug.
SLUG_FIXES: dict[str, str | None] = {
    "sources/introdu-o-ao-pentest-mobile-pt-1.md": "sources/introducao-ao-pentest-mobile-pt-1.md",
    "sources/metaverso-e-a-inova-o-tecnol-gica.md": "sources/metaverso-e-a-inovacao-tecnologica.md",
    "sources/dicas-b-sicas-para-ingressar-no-mercado-de-seguran-a.md": "sources/dicas-basicas-para-ingressar-no-mercado-de-seguranca.md",
    "sources/enumera-o-de-grupos-de-ti-e-seguran-a-para-tech-recruiters.md": "sources/enumeracao-de-grupos-de-ti-e-seguranca-para-tech-recruiters.md",
    "sources/roadmap-seguran-a-da-informa-o-pt-1.md": "sources/roadmap-seguranca-da-informacao-pt-1.md",
    "sources/conceitos-b-sicos-de-p-s-explora-o-1.md": "sources/conceitos-basicos-de-pos-exploracao-1.md",
    "sources/introdu-o-a-p-s-explora-o.md": "sources/introducao-a-pos-exploracao.md",
    "sources/introdu-o-a-network-security-1-0.md": "sources/introducao-a-network-security-1-0.md",
    "sources/introdu-o-a-network-security-e-firewall.md": "sources/introducao-a-network-security-e-firewall.md",
    "sources/cyberbullying-e-as-consequ-ncias.md": "sources/cyberbullying-e-as-consequencias.md",
    "sources/seguran-a-infantil-um-problema-s-rio-mas-pouco-falado.md": "sources/seguranca-infantil-um-problema-serio-mas-pouco-falado.md",
    "sources/seguran-a-na-internet-para-crian-as.md": "sources/seguranca-na-internet-para-criancas.md",
    "sources/introdu-o-b-sica-a-analise-de-malware-1.md": "sources/introducao-basica-a-analise-de-malware-1.md",
    "sources/investigation-using-osint-with-a-focus-on-intelligence-operations-and-dark-web-operations-training.md": "sources/investigation-using-osint-with-a-focus-on-intelligence-operations-and-dark-web-o.md",
    "sources/introdu-o-ao-buffer-overflow-1.md": "sources/introducao-ao-buffer-overflow-1.md",
    "sources/introdu-o-ao-desenvolvimento-de-exploits.md": "sources/introducao-ao-desenvolvimento-de-exploits.md",
    "sources/introdu-o-ao-desenvolvimento-de-exploits-2.md": "sources/introducao-ao-desenvolvimento-de-exploits-2.md",
    "sources/introdu-o-a-engenharia-social-pr-tica.md": "sources/introducao-a-engenharia-social-pratica.md",
    "sources/versao-final-atualizada-vulnerabilidades-comuns-em-aplica-es-web-roadsec-2023.md": "sources/versao-final-atualizada-vulnerabilidades-comuns-em-aplicacoes-web-roadsec-2023.md",
    "sources/programa-o-c-e-c-para-seguran-a-ofensiva-digital.md": "sources/programacao-c-e-c-para-seguranca-ofensiva-digital.md",
    "sources/introdu-o-ao-mitre-att-ck-e-ao-cyber-kill-chain.md": "sources/introducao-ao-mitre-att-ck-e-ao-cyber-kill-chain.md",
    "@seo-wiki/concepts/web-vitals.md": None,
}

FRONTMATTER_RE = re.compile(r"^---\n(.*?\n)---\n(.*)$", re.DOTALL)


def split_frontmatter(text: str) -> tuple[str, str, str] | None:
    """Return (pre, frontmatter_body, body) or None if not parseable.
    pre is empty for standard docs (frontmatter at top)."""
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    return "", text[4:end + 1], text[end + 5:]


def parse_related(frontmatter: str) -> list[str]:
    out: list[str] = []
    in_related = False
    for line in frontmatter.split("\n"):
        if line.startswith("related:"):
            in_related = True
            continue
        if in_related:
            if line.startswith("  - ") or (line.startswith("- ") and not line.startswith("---")):
                ref = line.split("-", 1)[1].strip()
                if ref and not ref.startswith("@") and not ref.startswith("["):
                    out.append(ref)
            elif line and not line.startswith(" "):
                break
    return out


def is_related_item(line: str) -> bool:
    """Recognize both `  - foo` and `- foo` YAML list items inside related:."""
    return line.startswith("  - ") or (line.startswith("- ") and not line.startswith("---"))


def set_related(frontmatter: str, new_related: list[str]) -> str:
    """Rewrite the `related:` block in frontmatter to `new_related`."""
    lines = frontmatter.split("\n")
    out: list[str] = []
    in_related = False
    written = False
    for line in lines:
        if line.startswith("related:"):
            in_related = True
            out.append("related:")
            if not written:
                for r in new_related:
                    out.append(f"  - {r}")
                written = True
            continue
        if in_related:
            if is_related_item(line):
                # Skip existing related items (we already wrote the merged set)
                continue
            elif line and not line.startswith(" "):
                in_related = False
                out.append(line)
            else:
                # Blank line inside related block — skip
                if not line.strip():
                    continue
                out.append(line)
        else:
            out.append(line)
    return "\n".join(out)


def fix_slugs(text: str) -> tuple[str, int]:
    changes = 0
    for broken, fixed in SLUG_FIXES.items():
        if fixed is None:
            for variant in (f"  - {broken}\n", f"- @{broken}\n", f"- {broken}\n"):
                if variant in text:
                    text = text.replace(variant, "")
                    changes += 1
        elif broken in text:
            text = text.replace(broken, fixed)
            changes += 1
    return text, changes


def strip_at_prefix_from_frontmatter(frontmatter: str) -> tuple[str, int]:
    lines = frontmatter.split("\n")
    out: list[str] = []
    in_related = False
    stripped = 0
    for line in lines:
        if line.startswith("related:"):
            in_related = True
            out.append(line)
            continue
        if in_related:
            if line.startswith("  - "):
                if line[4:].strip().startswith("@"):
                    stripped += 1
                    continue
            elif line and not line.startswith(" "):
                in_related = False
        out.append(line)
    return "\n".join(out), stripped


def main() -> None:
    md_files = list(WIKI.rglob("*.md"))

    # ---- Pass 1: slug fixes + strip @-prefix ----
    slug_changes = 0
    strip_changes = 0
    for f in md_files:
        text = f.read_text()
        text, n = fix_slugs(text)
        slug_changes += n
        parts = split_frontmatter(text)
        if parts is None:
            f.write_text(text)
            continue
        _, fm, body = parts
        fm, m = strip_at_prefix_from_frontmatter(fm)
        strip_changes += m
        f.write_text("---\n" + fm + "---\n" + body)
    print(f"Pass 1: applied {slug_changes} slug fixes; stripped {strip_changes} @-prefix frontmatter refs")

    # ---- Pass 2: build inbound-edge map ----
    rel_paths: dict[str, Path] = {}
    for p in md_files:
        rel = str(p.relative_to(WIKI)).replace("\\", "/")
        rel_paths[rel] = p

    inbound: dict[str, set[str]] = {r: set() for r in rel_paths}
    for rel_a, path_a in rel_paths.items():
        if rel_a in ("index.md", "log.md"):
            continue
        parts = split_frontmatter(path_a.read_text())
        if parts is None:
            continue
        _, fm, _ = parts
        for ref_b in parse_related(fm):
            if ref_b in rel_paths:
                inbound[ref_b].add(rel_a)

    # ---- Pass 3: write inbound backlinks into every page's `related:` ----
    added = 0
    for rel_b, path_b in rel_paths.items():
        if rel_b in ("index.md", "log.md"):
            continue
        text = path_b.read_text()
        parts = split_frontmatter(text)
        if parts is None:
            continue
        _, fm, body = parts
        existing = set(parse_related(fm))
        wanted = sorted(existing | inbound[rel_b])
        # Detect whether the file currently has any one-space `- ` (non-normalized) related items
        # so we always rewrite to normalize even when no new edges are added.
        non_normalized = any(
            line.startswith("- ") and not line.startswith("---")
            for line in fm.split("\n")
        )
        if set(wanted) == existing and not non_normalized:
            continue
        new_fm = set_related(fm, wanted)
        # Update `## Relations` inline block too — rebuild it.
        relations_lines = [f"- @{r}" for r in wanted] if wanted else ["_(none yet)_"]
        relations_block = "\n".join(relations_lines)
        body = re.sub(
            r"## Relations\n\n[\s\S]*?(?=\n##|\Z)",
            f"## Relations\n\n{relations_block}\n\n",
            body,
            count=1,
        )
        path_b.write_text("---\n" + new_fm + "---\n" + body)
        added += len(set(wanted) - existing)
    print(f"Pass 3: added {added} bidirectional backlinks")


if __name__ == "__main__":
    main()
