#!/usr/bin/env python3
"""Fix slug mismatches + bidirectional gaps left by build_entity_concept_pages.py.

Two passes:
1. Slug correction — replace broken refs (Portuguese-letter slugs with `-o-` placeholders)
   with the actual accent-stripped slug.
2. Bidirectional backlink injection — for every entity/concept page A that lists source B
   in `related:`, ensure B also lists A in its `related:` (and inline `## Relations`).
3. Frontmatter cross-wiki strip — `@wiki-alias/...` paths don't belong in `related:`
   frontmatter (only inline). Strip them.

Run from repo root after build_source_stubs.py + build_entity_concept_pages.py:
    python3 scripts/fix_wiki_refs.py
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"

# Manual slug-fix map. Build from lint output.
SLUG_FIXES: dict[str, str] = {
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
    # Cosmetic — these page targets that should be removed entirely (missing in sibling wikis)
    "@seo-wiki/concepts/web-vitals.md": None,  # removed — page doesn't exist in SEO wiki yet
}


def fix_slugs(text: str) -> tuple[str, int]:
    """Apply SLUG_FIXES to a file's text. Returns (new_text, changes)."""
    changes = 0
    for broken, fixed in SLUG_FIXES.items():
        if fixed is None:
            # Remove these lines entirely (frontmatter or inline)
            patterns = [
                f"  - {broken}\n",
                f"- @{broken}\n",
                f"- {broken}\n",
            ]
            for p in patterns:
                if p in text:
                    text = text.replace(p, "")
                    changes += 1
        else:
            if broken in text:
                text = text.replace(broken, fixed)
                changes += 1
    return text, changes


def strip_at_prefix_from_frontmatter(text: str) -> tuple[str, int]:
    """`related:` frontmatter list items should not have @ prefix (that's for inline blocks).
    Some entity/concept pages I wrote slipped `@wiki-alias/...` into `related:`. Strip them.
    """
    if "related:" not in text or "---" not in text:
        return text, 0
    parts = text.split("---", 2)
    if len(parts) < 3:
        return text, 0
    frontmatter = parts[1]
    body = parts[2]
    new_lines = []
    changes = 0
    in_related = False
    for line in frontmatter.split("\n"):
        if line.startswith("related:"):
            in_related = True
            new_lines.append(line)
            continue
        if in_related:
            if line.startswith("  - "):
                ref = line[4:].strip()
                if ref.startswith("@"):
                    # Cross-wiki ref doesn't belong in frontmatter; drop it
                    changes += 1
                    continue
            elif line and not line.startswith(" "):
                in_related = False
        new_lines.append(line)
    return parts[0] + "---" + "\n".join(new_lines) + "---" + body, changes


def parse_related(text: str) -> list[str]:
    """Extract `related:` list from frontmatter."""
    if "related:" not in text or "---" not in text:
        return []
    parts = text.split("---", 2)
    if len(parts) < 3:
        return []
    frontmatter = parts[1]
    out = []
    in_related = False
    for line in frontmatter.split("\n"):
        if line.startswith("related:"):
            in_related = True
            continue
        if in_related:
            if line.startswith("  - "):
                ref = line[4:].strip()
                if ref and not ref.startswith("@") and not ref.startswith("["):
                    out.append(ref)
            elif line and not line.startswith(" "):
                break
    return out


def add_related_backlink(target_path: Path, source_ref: str) -> bool:
    """If `target_path` does not yet list `source_ref` in its `related:`, add it."""
    if not target_path.exists():
        return False
    text = target_path.read_text()
    existing = parse_related(text)
    if source_ref in existing:
        return False
    # Insert at end of `related:` block, also append to `## Relations` inline list
    parts = text.split("---", 2)
    if len(parts) < 3:
        return False
    frontmatter = parts[1]
    body = parts[2]
    new_lines = []
    in_related = False
    inserted = False
    for line in frontmatter.split("\n"):
        if line.startswith("related:"):
            in_related = True
            new_lines.append(line)
            continue
        if in_related:
            if line.startswith("  - "):
                pass
            elif line and not line.startswith(" "):
                if not inserted:
                    new_lines.append(f"  - {source_ref}")
                    inserted = True
                in_related = False
        new_lines.append(line)
    if in_related and not inserted:
        new_lines.append(f"  - {source_ref}")
    new_frontmatter = "\n".join(new_lines)

    # Append to ## Relations body section
    relations_line = f"- @{source_ref}"
    if "## Relations" in body:
        body = re.sub(
            r"(## Relations\n\n)((?:- @[^\n]+\n)+|_\(none yet\)_\n)",
            lambda m: m.group(1) + (m.group(2).replace("_(none yet)_", "").rstrip() + "\n" + relations_line + "\n"),
            body,
            count=1,
        )

    target_path.write_text(parts[0] + "---" + new_frontmatter + "---" + body)
    return True


def main() -> None:
    # ---- Pass 1: slug fixes + strip @ prefix from frontmatter ----
    fixed = 0
    stripped = 0
    for md in WIKI.rglob("*.md"):
        text = md.read_text()
        new_text, n = fix_slugs(text)
        new_text, m = strip_at_prefix_from_frontmatter(new_text)
        if n or m:
            md.write_text(new_text)
        fixed += n
        stripped += m
    print(f"Pass 1: applied {fixed} slug fixes; stripped {stripped} @-prefix frontmatter refs")

    # ---- Pass 2: bidirectional backlink injection ----
    pages = list(WIKI.rglob("*.md"))
    paths_by_rel: dict[str, Path] = {}
    for p in pages:
        rel = str(p.relative_to(WIKI)).replace("\\", "/")
        paths_by_rel[rel] = p

    added = 0
    for rel_a, path_a in paths_by_rel.items():
        if rel_a in ("index.md", "log.md"):
            continue
        related_b = parse_related(path_a.read_text())
        for ref_b in related_b:
            if ref_b in paths_by_rel:
                if add_related_backlink(paths_by_rel[ref_b], rel_a):
                    added += 1
    print(f"Pass 2: added {added} bidirectional backlinks")


if __name__ == "__main__":
    main()
