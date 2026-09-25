#!/usr/bin/env python3
import json, os, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CFG = json.loads((ROOT / "hdc" / "config.json").read_text(encoding="utf-8"))


def git(*args):
    return subprocess.check_output(["git", *args], text=True).strip()


def changed_files():
    base = os.environ.get("HDC_BASE_REF", "HEAD~1")
    try:
        out = git("diff", "--name-only", base, "HEAD")
    except Exception:
        out = git("status", "--porcelain")
        return [line[3:] for line in out.splitlines() if len(line) > 3]
    return [x for x in out.splitlines() if x]


def has_change_package(files):
    return any(f.startswith("change-packages/") and f.endswith(".json") for f in files)


def core_change_request_present(files):
    return any(f.startswith("core-change-requests/") for f in files)


def scan_text_file(path):
    try:
        return (ROOT / path).read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""


def main():
    files = changed_files()
    errors = []
    if CFG.get("required_change_package") and files and not has_change_package(files):
        errors.append("Missing change package in change-packages/*.json")

    protected = [p for p in CFG.get("protected_paths", []) if any(f.startswith(p) for f in files)]
    if protected and not core_change_request_present(files):
        errors.append("Protected Core path changed without core-change-requests/*")

    # Conservative heuristics; architecture tests should add project-specific checks later.
    direct_db = re.compile(r"domains[/\\][^/\\]+.*(SELECT\s+.+FROM|INSERT\s+INTO|UPDATE\s+.+SET)", re.I | re.S)
    hardcoded_role = re.compile(r"if\s*\([^\n]*(rector|dean|head_of_department)[^\n]*\)", re.I)
    super_agent = re.compile(r"super.?agent|global_authority\s*[:=]\s*true", re.I)

    for f in files:
        if not f.endswith((".py", ".ts", ".tsx", ".js", ".jsx", ".sql", ".json", ".yaml", ".yml")):
            continue
        txt = scan_text_file(f)
        if direct_db.search(f + "\n" + txt):
            errors.append(f"Potential direct domain DB access: {f}")
        if hardcoded_role.search(txt):
            errors.append(f"Potential hard-coded organization/role permission: {f}")
        if super_agent.search(txt):
            errors.append(f"Potential Super Agent/global authority pattern: {f}")

    if errors:
        print("HDC ARCHITECTURE GUARD: FAIL")
        for e in errors:
            print("-", e)
        raise SystemExit(1)
    print("HDC ARCHITECTURE GUARD: PASS")
    if files:
        print("Changed files:")
        for f in files:
            print("-", f)

if __name__ == "__main__":
    main()
