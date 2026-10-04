#!/usr/bin/env python3
"""Block a NEW session log until the PRE-FLIGHT line has been printed in chat.

A Claude Code PreToolUse hook on Write. It reads the hook JSON on stdin and only
acts when the Write creates a new `.md` file inside a `session-logs/` folder.
Then it looks through this chat's transcript for an assistant text block with
"PRE-FLIGHT" in it, printed AFTER the last session log written in this chat.
None found -> exit 2 with a message, which stops the Write and tells the agent
to print the line first.

Edits, rewrites of an existing log, and every other file pass straight through.
If anything goes wrong reading the transcript, it lets the Write go: a broken
check must never block the user's work.

Why (2026-10-03): the pre-flight line was written after the log on 08-22,
09-07 and 09-17. Prose in SKILL.md could not make it come first; this can.
"""
import json
import os
import sys


def is_new_session_log(path):
    return (
        bool(path)
        and "/session-logs/" in path
        and path.endswith(".md")
        and not os.path.exists(path)
    )


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0
    path = (data.get("tool_input") or {}).get("file_path", "")
    if not is_new_session_log(path):
        return 0
    transcript = data.get("transcript_path") or ""
    if not os.path.exists(transcript):
        return 0

    last_preflight = -1
    last_log_write = -1
    try:
        with open(transcript) as f:
            for i, line in enumerate(f):
                try:
                    entry = json.loads(line)
                except Exception:
                    continue
                if entry.get("type") != "assistant":
                    continue
                content = (entry.get("message") or {}).get("content") or []
                if not isinstance(content, list):
                    continue
                for block in content:
                    if not isinstance(block, dict):
                        continue
                    if block.get("type") == "text" and "PRE-FLIGHT" in block.get("text", ""):
                        last_preflight = i
                    elif block.get("type") == "tool_use" and block.get("name") == "Write":
                        p = (block.get("input") or {}).get("file_path", "")
                        # An earlier session log in this chat, not the one being written now.
                        if "/session-logs/" in p and p.endswith(".md") and p != path:
                            last_log_write = i
    except Exception:
        return 0

    if last_preflight > last_log_write:
        return 0

    sys.stderr.write(
        "SLC pre-flight missing. Before writing a session log, print the PRE-FLIGHT line "
        "in chat (see SLC SKILL.md -> Pre-flight):\n"
        "PRE-FLIGHT — template: read (N sections) · knowledge logs: asked/none · "
        "screenshots: extracted/owned-by-DNC · notes: N caught / N placed\n"
        "Do any step you can't honestly fill in, then write the log again.\n"
    )
    return 2


if __name__ == "__main__":
    sys.exit(main())
