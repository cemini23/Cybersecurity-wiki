#!/usr/bin/env python3
"""Canonical wiki link resolution, shared by wiki_lint.py and the merge harness.

One code path serves two layouts. Before the federation merge a wiki is a single
repository, its `related:` entries are relative to `wiki/`, and a peer reference
like `@ccc-wiki/concepts/x.md` names a sibling checkout on disk. After the merge
all eight wikis live under one `wiki/`, and the same reference names
`wiki/ccc/concepts/x.md` inside the same tree.

The federation table decides which. An entry whose path sits inside the wiki root
names a local domain; one that does not is an external peer. Nothing else changes.

This module exists so the linter and the migration harness cannot disagree about
whether a link resolves. Duplicating the logic in the harness would defeat the
point of the harness.
"""

from __future__ import annotations

import re
from pathlib import Path

# ARA typed dependencies: @I (imports), @B (bounds), @M (measure).
_ARA_RE = re.compile(r"^@?[IBM]\s+(?=\S)")

# Rows of the CLAUDE.md "Related Wikis" table: | `alias` | `path/to/wiki/` | ...
_TABLE_RE = re.compile(
    r"^\|\s*`([a-z0-9_-]+)`\s*\|\s*`?([^`\n\|]+)`?\s*\|", re.MULTILINE
)


def normalize_path(p):
    """Strip an ARA typed prefix, a leading slash, and a stray wiki/ segment."""
    p = p.strip()
    p = _ARA_RE.sub("", p)
    p = p.lstrip("/")
    if p.startswith("wiki/"):
        p = p[len("wiki/"):]
    return p


# -- link extraction -------------------------------------------------------
# The linter and the harness must find the SAME references, or a comparison
# between them measures the extractor rather than the wiki.

AT_PATH_RE = re.compile(r"(@[a-z0-9_./-]+\.md)")
# Quote and bracket chars are excluded: related: entries are YAML-quoted and inline
# refs sit inside [Source: ...] tags, so a naive class swallows the closing delimiter.
CROSS_WIKI_RE = re.compile(r"""@([a-z0-9_-]+)/([^\s`)\]"']+)""")
RELATED_BLOCK_RE = re.compile(r"^related:\s*\n((?:\s+-\s+.+\n?)*)", re.MULTILINE)
RELATED_INLINE_RE = re.compile(r"^related:\s*\[([^\]]*)\]", re.MULTILINE)
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def inside_backticks(text, start, end):
    """True when [start, end) sits inside a `...` span on the same line."""
    line_start = text.rfind("\n", 0, start) + 1
    line_end = text.find("\n", end)
    if line_end == -1:
        line_end = len(text)
    line = text[line_start:line_end]
    return line.count("`", 0, start - line_start) % 2 == 1


def related_entries(text):
    """The raw `related:` entries from a page's frontmatter, in order."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return []
    fm = m.group(1)
    block = RELATED_BLOCK_RE.search(fm)
    if block:
        out = []
        for line in block.group(1).splitlines():
            s = line.strip()
            if s.startswith("- "):
                v = s[2:].strip()
                if len(v) >= 2 and v[0] == v[-1] and v[0] in ("'", '"'):
                    v = v[1:-1].strip()
                out.append(v)
        return out
    inline = RELATED_INLINE_RE.search(fm)
    if inline:
        return [v.strip().strip("'\"") for v in inline.group(1).split(",") if v.strip()]
    return []


def iter_refs(text):
    """Every @path reference in a page, as (raw, kind) with kind 'related' or 'body'.

    Body references are de-duplicated against the frontmatter so one page does not
    contribute the same edge twice.
    """
    seen = set()
    for raw in related_entries(text):
        key = ("related", raw)
        if key not in seen:
            seen.add(key)
            yield (raw, "related")
    for pattern in (AT_PATH_RE, CROSS_WIKI_RE):
        for m in pattern.finditer(text):
            if inside_backticks(text, m.start(), m.end()):
                continue
            raw = m.group(1) if pattern is AT_PATH_RE else f"@{m.group(1)}/{m.group(2)}"
            key = ("body", raw)
            if key not in seen:
                seen.add(key)
                yield (raw, "body")


def load_federation_table(claude_md):
    """Map each federation id to its base directory, from the CLAUDE.md table.

    Paths are relative to the CLAUDE.md that declares them, so resolution is
    correct whichever wiki is being scanned.
    """
    claude_md = Path(claude_md)
    table = {}
    if not claude_md.is_file():
        return table
    text = claude_md.read_text(encoding="utf-8", errors="replace")
    for m in _TABLE_RE.finditer(text):
        alias = m.group(1).strip()
        path_str = m.group(2).strip().rstrip("/")
        target = (claude_md.parent / path_str).resolve()
        if target.is_dir():
            table[alias] = target
        elif (target / "wiki").is_dir():
            table[alias] = target / "wiki"
    return table


class WikiResolver:
    """Resolve one @path reference to a canonical page key.

    A page key is the path relative to the wiki root: `concepts/foo.md` before the
    merge, `osint/concepts/foo.md` after.
    """

    def __init__(self, wiki_root, table):
        self.wiki = Path(wiki_root).resolve()
        self.table = dict(table)
        self.domains = self._local_domains()

    def _local_domains(self):
        doms = set()
        for _alias, base in self.table.items():
            try:
                rel = Path(base).resolve().relative_to(self.wiki)
            except ValueError:
                continue  # an external peer, not an in-tree domain
            if rel.parts:
                doms.add(rel.parts[0])
        return doms

    def domain_of(self, rel_path):
        """The domain prefix of a page key, or '' when the wiki holds one domain."""
        head = rel_path.split("/", 1)[0]
        return head if head in self.domains else ""

    def key_if_inside(self, path):
        """The page key for *path* when it is a markdown file inside the wiki root."""
        try:
            rel = Path(path).resolve().relative_to(self.wiki)
        except (ValueError, OSError):
            return None
        return str(rel) if rel.suffix == ".md" else None

    def resolve(self, src_rel, raw, known_keys):
        """Resolve one @path reference.

        Returns (kind, value):
          'local'     value is a page key present in known_keys
          'out'       value is a Path that exists outside the wiki tree
                      (repo-root briefs/, prompts/, scripts/)
          'ambiguous' value is a list of page keys that all match
          'missing'   value is the Path that was looked for
        """
        p = normalize_path(raw)
        src_dom = self.domain_of(src_rel)

        # 1. Peer form. The table decides whether the target is in-tree, so the same
        #    call works before the merge (sibling repo) and after (wiki/<domain>/).
        for alias, base in self.table.items():
            prefix = f"@{alias}/"
            if not p.startswith(prefix):
                continue
            rel = p[len(prefix):]
            for cand in (base / rel, base.parent / rel):
                key = self.key_if_inside(cand)
                if key is not None and key in known_keys:
                    return ("local", key)
                if key is None and cand.exists():
                    return ("out", cand)
            return ("missing", base / rel)

        # 2. Bare path, relative to the source page's own domain. The leading @ is
        #    stripped here; normalize_path keeps it so step 1 can match it.
        rel = p.lstrip("@")
        if rel.startswith("wiki/"):
            rel = rel[len("wiki/"):]
        cand = (self.wiki / src_dom / rel) if src_dom else (self.wiki / rel)
        key = self.key_if_inside(cand)
        if key is not None and key in known_keys:
            return ("local", key)

        # 3. The same path in another domain. Report rather than pick when more than
        #    one matches: duplicated pages are not byte-identical, so a silent choice
        #    would bind the link to the wrong file with no warning.
        hits = []
        for dom in sorted(self.domains):
            if dom == src_dom:
                continue
            k = self.key_if_inside(self.wiki / dom / rel)
            if k is not None and k in known_keys:
                hits.append(k)
        if len(hits) == 1:
            return ("local", hits[0])
        if len(hits) > 1:
            return ("ambiguous", hits)

        # 4. Repo-root trees beside wiki/ (briefs/, prompts/, scripts/).
        out = self.wiki.parent / rel
        if out.exists():
            return ("out", out)
        return ("missing", cand)
