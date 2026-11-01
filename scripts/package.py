#!/usr/bin/env python3
"""package.py: validate SKILL.md and build dist/<name>.zip for upload to Claude.

Usage:
  python3 scripts/package.py           # validate and build
  python3 scripts/package.py --check   # validate only (used in CI)

Checks the frontmatter (name, description), the SKILL.md length, that every relative
link in SKILL.md resolves and that every file in references/ is linked from SKILL.md,
so the skill loads its references one level deep. The zip has the skill folder at its
root, named after the skill, as the Claude apps expect.
"""
from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INCLUDE = ["SKILL.md", "LICENSE", "agents", "assets", "references", "examples", "scripts/lint.py", "scripts/render.mjs"]
DESCRIPTION_MAX = 200   # Claude apps; the API and Claude Code allow 1024
NAME_MAX = 64
BODY_MAX_LINES = 500


def frontmatter(text: str) -> tuple[dict[str, str], str]:
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise SystemExit("SKILL.md must start with a YAML frontmatter block between --- lines")
    fields = {}
    for line in m.group(1).splitlines():
        km = re.match(r"^([a-z_-]+):\s*(.*)$", line)
        if km and not line.startswith(" "):
            value = km.group(2).strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
                value = value[1:-1]
            fields[km.group(1)] = value
    return fields, m.group(2)


def validate() -> tuple[str, list[str]]:
    errors = []
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    fields, body = frontmatter(text)
    name, desc = fields.get("name", ""), fields.get("description", "")
    if not re.fullmatch(r"[a-z0-9-]+", name) or len(name) > NAME_MAX:
        errors.append(f"name must be lowercase letters, digits and hyphens, at most {NAME_MAX} characters: {name!r}")
    if any(word in name for word in ("anthropic", "claude")):
        errors.append("name must not contain a reserved word (anthropic, claude)")
    if not desc:
        errors.append("description is empty")
    if len(desc) > DESCRIPTION_MAX:
        errors.append(f"description is {len(desc)} characters; the Claude apps accept at most {DESCRIPTION_MAX}")
    if re.search(r"[<>]", desc):
        errors.append("description must not contain angle brackets")
    lines = body.count("\n") + 1
    if lines > BODY_MAX_LINES:
        errors.append(f"SKILL.md body is {lines} lines; keep it under {BODY_MAX_LINES}")
    links = set(re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", body))
    for link in sorted(links):
        if re.match(r"^[a-z]+:", link):
            continue
        if not (ROOT / link).exists():
            errors.append(f"SKILL.md links to a missing file: {link}")
    for ref in sorted((ROOT / "references").glob("*.md")):
        if f"references/{ref.name}" not in links:
            errors.append(f"references/{ref.name} is not linked from SKILL.md")
    print(f"name: {name}\ndescription: {len(desc)} characters\nSKILL.md body: {lines} lines, {len(links)} links")
    return name, errors


def build(name: str) -> Path:
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    target = dist / f"{name}.zip"
    files = []
    for item in INCLUDE:
        path = ROOT / item
        if path.is_dir():
            files += [p for p in sorted(path.rglob("*")) if p.is_file() and "__pycache__" not in p.parts and not p.name.startswith(".")]
        elif path.is_file():
            files.append(path)
        else:
            raise SystemExit(f"Missing from the package: {item}")
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in files:
            zf.write(path, f"{name}/{path.relative_to(ROOT).as_posix()}")
    size = target.stat().st_size / 1024
    print(f"{len(files)} files → {target.relative_to(ROOT)} ({size:.0f} kB)")
    return target


def main():
    name, errors = validate()
    if errors:
        print("\n".join(f"error: {e}" for e in errors), file=sys.stderr)
        sys.exit(1)
    print("SKILL.md checks passed")
    if "--check" not in sys.argv:
        build(name)


if __name__ == "__main__":
    main()
