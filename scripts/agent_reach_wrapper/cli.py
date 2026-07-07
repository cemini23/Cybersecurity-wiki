"""CLI for validating manual Agent-Reach social snapshots."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .allowlist import AllowlistError, SourceAllowlist
from .manual_snapshot import load_snapshot, process_captures, write_audit_log, write_output


DEFAULT_OUT = Path(".local/agent-reach-wrapper/normalized-social-items.json")
DEFAULT_AUDIT = Path(".local/agent-reach-wrapper/audit.jsonl")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate a local manual social snapshot in DRY_RUN mode.")
    parser.add_argument("--snapshot", required=True, type=Path, help="Local manual snapshot JSON file.")
    parser.add_argument("--allowlist", required=True, type=Path, help="Source allowlist JSON config.")
    parser.add_argument("--out", default=DEFAULT_OUT, type=Path, help="Local DRY_RUN output JSON path.")
    parser.add_argument("--audit", default=DEFAULT_AUDIT, type=Path, help="Local JSONL audit path.")
    parser.add_argument("--workspace", default=Path.cwd(), type=Path, help="Workspace root for write confinement.")
    parser.add_argument(
        "--no-write-output",
        action="store_true",
        help="Validate only; still writes an audit event.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        allowlist = SourceAllowlist.from_file(args.allowlist)
        captures = load_snapshot(args.snapshot)
        result = process_captures(captures, allowlist)
        audit_path = _require_workspace_path(args.audit, args.workspace)
        output_path = _require_workspace_path(args.out, args.workspace)
        write_audit_log(
            audit_path,
            connector="manual_snapshot",
            snapshot_path=args.snapshot,
            result=result,
        )
        if not result.ok:
            for rejection in result.rejections:
                print(
                    f"rejected[{rejection.index}]: {rejection.reason} - {rejection.detail}",
                    file=sys.stderr,
                )
            return 1

        if not args.no_write_output:
            write_output(output_path, result.items)
        print(f"accepted {len(result.items)} item(s) in DRY_RUN mode")
        return 0
    except (OSError, ValueError, AllowlistError) as exc:
        print(f"failed closed: {exc}", file=sys.stderr)
        return 2


def _require_workspace_path(path: Path, workspace: Path) -> Path:
    resolved_path = path.resolve()
    resolved_workspace = workspace.resolve()
    if resolved_path != resolved_workspace and resolved_workspace not in resolved_path.parents:
        raise ValueError(f"write path must stay inside workspace: {path}")
    return resolved_path


if __name__ == "__main__":
    raise SystemExit(main())
