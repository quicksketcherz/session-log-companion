#!/usr/bin/env python3
"""List every "note." / "fleet" capture the user typed in a chat, from its session jsonl.

SLC's own copy of daily-notes-companion/scripts/list_captures.py, so SLC works
without DNC. Used in Workflow 4, Step 2 so no capture is missed. Keep the two
copies the same when either changes.
Matches at the start of ANY line of a message, not just the first, because a
capture often follows an @file line. Skips skill text, system text and tool
results. Prints one line per capture: time (Toronto) and the first words.

Usage:
  list_captures.py                 # newest jsonl under ~/.claude/projects
  list_captures.py <path.jsonl>    # a specific chat
"""
import glob
import json
import os
import re
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

TORONTO = ZoneInfo("America/Toronto")

# "note." "note:" "notes," "note to self" "fleet" "take note" "add this to the notes"
# Bare "note yet" (a typo for "not yet") does not match: "note" needs punctuation after it.
CAPTURE = re.compile(
    r"^\s*(notes?\s*[.:,!-]|note to self|fleet\b|here'?s my fleet|take (a )?note|"
    r"add (this|that) to (the|my) notes?)",
    re.IGNORECASE,
)

# Text that lands in a user turn but was not typed by the user.
NOT_TYPED = (
    "Base directory for this skill",
    "<command-name>",
    "<command-message>",
    "<system-reminder>",
    "<local-command",
    "Caveat:",
    "[Request interrupted",
)


def newest_jsonl():
    files = glob.glob(os.path.expanduser("~/.claude/projects/*/*.jsonl"))
    if not files:
        sys.exit("no session jsonl found under ~/.claude/projects")
    return max(files, key=os.path.getmtime)


def typed_text(entry):
    """Return the text the user typed in this entry, or None."""
    if entry.get("type") != "user" or entry.get("isMeta"):
        return None
    content = entry.get("message", {}).get("content")
    if isinstance(content, str):
        parts = [content]
    elif isinstance(content, list):
        parts = [b.get("text", "") for b in content if b.get("type") == "text"]
    else:
        return None
    # Filter per block: a system note often sits in its own block before the user's text.
    text = "\n".join(p for p in parts if p and not p.lstrip().startswith(NOT_TYPED))
    return text or None


def toronto_hhmm(stamp):
    if not stamp:
        return "????"
    t = datetime.fromisoformat(stamp.replace("Z", "+00:00"))
    return t.astimezone(TORONTO).strftime("%H%M")


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else newest_jsonl()
    found = []
    with open(path, encoding="utf-8") as f:
        for raw in f:
            try:
                entry = json.loads(raw)
            except json.JSONDecodeError:
                continue
            text = typed_text(entry)
            if not text:
                continue
            for line in text.splitlines():
                if CAPTURE.match(line):
                    words = " ".join(line.split()[:10])
                    found.append((toronto_hhmm(entry.get("timestamp")), words))
    print(f"{len(found)} captures in {os.path.basename(path)}")
    for i, (hhmm, words) in enumerate(found, 1):
        print(f"{i:>2}. {hhmm}  {words}")


if __name__ == "__main__":
    main()
