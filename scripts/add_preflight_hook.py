#!/usr/bin/env python3
"""Add (or remove) SLC's pre-flight hook in ~/.claude/settings.json.

The hook runs scripts/preflight_gate.py before every Write in Claude Code. It
only steps in when the Write creates a new session log, and only to say "print
the PRE-FLIGHT line first". Everything else in settings.json is left as it is.

Usage:
  python3 ~/.claude/skills/session-log-companion/scripts/add_preflight_hook.py
  python3 ~/.claude/skills/session-log-companion/scripts/add_preflight_hook.py --remove

Safe to run twice: it checks first and never adds a second copy.
"""
import json
import os
import shutil
import sys

SETTINGS = os.path.expanduser("~/.claude/settings.json")
GATE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "preflight_gate.py")
# Keep the ~ form when the skill sits in the usual place, so settings.json reads the same on any Mac.
USUAL = os.path.expanduser("~/.claude/skills/session-log-companion/scripts/preflight_gate.py")
CMD = "python3 " + ("~/.claude/skills/session-log-companion/scripts/preflight_gate.py"
                    if os.path.realpath(GATE) == os.path.realpath(USUAL) else f'"{GATE}"')


def is_ours(hook):
    return "preflight_gate.py" in hook.get("command", "")


def main():
    remove = "--remove" in sys.argv[1:]
    s = {}
    if os.path.exists(SETTINGS):
        with open(SETTINGS) as f:
            text = f.read().strip()
        if text:
            try:
                s = json.loads(text)
            except json.JSONDecodeError as e:
                print(f"STOP  {SETTINGS} is not valid JSON ({e}). Fix it first; nothing changed.")
                return 1

    pre = s.setdefault("hooks", {}).setdefault("PreToolUse", [])
    found = any(is_ours(h) for e in pre for h in e.get("hooks", []))

    if remove:
        if not found:
            print("OK    no SLC pre-flight hook to remove")
            return 0
        for e in pre:
            e["hooks"] = [h for h in e.get("hooks", []) if not is_ours(h)]
        s["hooks"]["PreToolUse"] = [e for e in pre if e.get("hooks")]
        msg = "DONE  SLC pre-flight hook removed"
    else:
        if found:
            print("OK    SLC pre-flight hook is already there")
            return 0
        pre.append({"matcher": "Write", "hooks": [{
            "type": "command", "command": CMD, "timeout": 10,
            "statusMessage": "Checking SLC pre-flight"}]})
        msg = f"DONE  SLC pre-flight hook added to {SETTINGS}"

    os.makedirs(os.path.dirname(SETTINGS), exist_ok=True)
    if os.path.exists(SETTINGS):
        shutil.copy2(SETTINGS, SETTINGS + ".bak")
    with open(SETTINGS, "w") as f:
        json.dump(s, f, indent=2)
        f.write("\n")
    print(msg)
    if os.path.exists(SETTINGS + ".bak"):
        print(f"      (the old file is saved as {SETTINGS}.bak)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
