# Install — Session Log Companion (SLC)

**Main platform:** Claude Code (CLI, desktop app, or IDE extension)
**Also works in:** claude.ai (upload as a skill) and Cursor. See *Other places* at the bottom.
**Tested on:** macOS
**Repo:** <https://github.com/quicksketcherz/session-log-companion> (public, no access needed)

---

## 1. Get the skill

Clone it straight into your Claude Code skills folder. One command, and `git pull` works for updates later:

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/quicksketcherz/session-log-companion.git ~/.claude/skills/session-log-companion
```

No restart needed. Claude Code picks up new skills right away.

**Editing it yourself?** Clone it where you keep your code and link it in instead, so edits take effect at once:

```bash
git clone https://github.com/quicksketcherz/session-log-companion.git ~/dev/session-log-companion
mkdir -p ~/.claude/skills
ln -s ~/dev/session-log-companion ~/.claude/skills/session-log-companion
```

## 2. Add the pre-flight hook (recommended)

Before it writes a session log, SLC prints one check line:

```
PRE-FLIGHT — template: read (N sections) · knowledge logs: asked/none · screenshots: extracted/owned-by-DNC · notes: N caught / N placed
```

The line makes the agent do the steps it would otherwise skip (read the template, ask about knowledge logs, catch your notes). Words in the skill alone were not enough, so a small hook makes sure the line comes first. It runs before every file write in Claude Code. It only steps in when a **new `.md` file in a `session-logs/` folder** is being written and no PRE-FLIGHT line was printed since the last log. Then it stops the write and tells the agent to print the line. Edits to an existing log are never checked. If anything goes wrong inside the hook, it lets the write through.

Add it with one command:

```bash
python3 ~/.claude/skills/session-log-companion/scripts/add_preflight_hook.py
```

It adds this to `~/.claude/settings.json`, keeps everything else there, saves the old file as `settings.json.bak`, and never adds a second copy:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/skills/session-log-companion/scripts/preflight_gate.py",
            "timeout": 10,
            "statusMessage": "Checking SLC pre-flight"
          }
        ]
      }
    ]
  }
}
```

Prefer to add it by hand? Paste the `PreToolUse` entry above into your own `settings.json`. To take it out again:

```bash
python3 ~/.claude/skills/session-log-companion/scripts/add_preflight_hook.py --remove
```

Needs `python3` on your PATH (any Mac with the Xcode command line tools has it).

## 3. Check it works

```bash
ls ~/.claude/skills/session-log-companion/
```

You should see `SKILL.md`, `references/` and `scripts/`.

Then, at the end of any Claude Code session, say:

> do a session log

The agent should print the PRE-FLIGHT line first (as a shell `echo`), then write the log to `session-logs/YYYY-MM-DD-HHMM-<title>.md` in your project folder.

---

## What you say

| Say this | What happens |
|---|---|
| "do a session log", "do sl", "summarize this session" | writes the session log for this chat |
| "document this discovery", "create a knowledge log" | a log of a problem solved, or a concept learned, for one tool |
| "I'm stuck with X" | offers a discovery log once it's solved |
| "remember this preference" | saves how you like to work into `~/.claude/CLAUDE.md` |
| "let's continue", "pick up where we left off" | reads the last session log and shows its next steps |
| "log this tangent" | a separate log for a side branch that belongs in another folder |

## Other skills it works with (all optional)

SLC works on its own. It mentions these when they are installed:

- **daily-notes-companion (DNC):** if you use it, SLC links to its notes and leaves the screenshots to it. Without it, SLC does that part itself.
- **touchdesigner-scaffolding-companion (TSC):** TouchDesigner knowledge logs go in `resources/touchdesigner-knowledge-logs/`, where TSC's gotchas pick them up.

## Update

```bash
git -C ~/.claude/skills/session-log-companion pull
```

## Uninstall

```bash
python3 ~/.claude/skills/session-log-companion/scripts/add_preflight_hook.py --remove
rm -rf ~/.claude/skills/session-log-companion
```

Your session logs and knowledge logs stay in your project folders.

---

## Troubleshooting

**The skill does not start.** Check the folder is at `~/.claude/skills/session-log-companion/` and holds `SKILL.md`. Then use a plain phrase: "do a session log".

**A session log write gets blocked with "SLC pre-flight missing".** That is the hook working. The agent should print the PRE-FLIGHT line with a shell `echo` in its own step, then write the log again in the next step. A line printed in the same step as the write is not saved yet when the hook looks, so it gets missed.

**The hook never seems to run.** Look in `~/.claude/settings.json` for `preflight_gate.py`. Run `add_preflight_hook.py` again; it says if the hook is already there. Check `python3 --version` works in a terminal.

**"is not valid JSON" from the hook installer.** Your `settings.json` has a typo (often a trailing comma). Fix it, then run the installer again. It changes nothing until the file reads cleanly.

---

## Other places

**claude.ai:** zip the folder and upload it under Settings → Capabilities → Skills. There is no hook there, so the PRE-FLIGHT line relies on the skill's own words.

**Cursor:** copy the folder into `~/.cursor/skills/` and reload the window:

```bash
mkdir -p ~/.cursor/skills
git clone https://github.com/quicksketcherz/session-log-companion.git ~/.cursor/skills/session-log-companion
```

The hook is Claude Code only. Preferences go to your own rules file instead of `~/.claude/CLAUDE.md`.

## What gets installed

```
~/.claude/skills/session-log-companion/
├── SKILL.md                 # the skill itself
├── README.md                # what it does, in short
├── INSTALL.md               # this file
├── CHANGELOG.md             # what changed, newest first
├── IMPROVEMENTS.md          # ideas waiting to be done
├── TEST-SCENARIOS.md        # example requests and what should happen
├── references/              # the session, discovery and learning log templates
└── scripts/
    ├── preflight_gate.py      # the hook
    ├── add_preflight_hook.py  # adds or removes the hook
    └── list_captures.py       # finds the "note." lines you typed in a chat
```
