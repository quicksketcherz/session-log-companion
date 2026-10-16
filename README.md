# Session Log Companion (SLC)

**For:** Claude Code (main), claude.ai and Cursor
**Install:** see [INSTALL.md](INSTALL.md). Short version below.
**Changes:** [CHANGELOG.md](CHANGELOG.md), newest first.

---

## What it does

SLC writes things down at the end of a work session, so the next session (yours, a colleague's or an agent's) starts where this one stopped.

1. **Session logs.** What got done, what was learned, what's next. Saved to `session-logs/` in your project folder.
2. **Knowledge logs.** One problem solved (a discovery log) or one idea understood (a learning log), for one tool. Saved to `resources/<tool>-knowledge-logs/`.
3. **Preferences.** "Remember this" goes into `~/.claude/CLAUDE.md`, where every agent reads it.
4. **Picking up.** "Let's continue" reads the last session log and shows what's still open.

It never writes a log you didn't ask for.

## Install (Claude Code)

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/quicksketcherz/session-log-companion.git ~/.claude/skills/session-log-companion
python3 ~/.claude/skills/session-log-companion/scripts/add_preflight_hook.py
```

The first two lines get the skill. The third adds the **pre-flight hook**: before a new session log is written, the agent has to print one check line, so it can't skip the template or forget to ask about knowledge logs. Optional, but recommended. INSTALL.md explains it, shows what it adds to `settings.json`, and how to remove it.

Update later with:

```bash
git -C ~/.claude/skills/session-log-companion pull
```

## What you say

| Say this | What happens |
|---|---|
| "do a session log", "do sl", "summarize this session" | writes the session log for this chat |
| "document this discovery", "create a knowledge log" | a knowledge log for one tool |
| "I'm stuck with X" | offers a discovery log once it's solved |
| "remember this preference" | saves it to `~/.claude/CLAUDE.md` |
| "let's continue", "pick up where we left off" | reads the last log, shows its next steps |
| "log this tangent" | a separate log for a side branch that belongs in another folder |

## Folders it makes in your project

```
your-project/
├── session-logs/                 # one file per session
└── resources/
    └── <tool>-knowledge-logs/    # e.g. touchdesigner-knowledge-logs/
```

## File names

Every log starts with the same timestamp shape, so a session log and the knowledge logs from it sort together:

```
session-logs/2026-03-07-1430-TouchDesigner-Build.md
resources/touchdesigner-knowledge-logs/2026-03-07-1445-Camera-Fix.md
```

## Works with (all optional)

- **daily-notes-companion (DNC):** SLC links to its notes and leaves the screenshots to it. Without DNC, SLC does that part itself.
- **touchdesigner-scaffolding-companion (TSC):** TouchDesigner knowledge logs land where TSC's gotchas read them.

## Files

- `SKILL.md`: the skill itself
- `references/`: the session, discovery and learning log templates
- `scripts/preflight_gate.py`: the hook; `scripts/add_preflight_hook.py` adds or removes it
- `scripts/list_captures.py`: finds the "note." lines you typed during a chat, so none get lost
- `TEST-SCENARIOS.md`: example requests and what should happen
- `IMPROVEMENTS.md`: ideas waiting to be done

## License

MIT. See [LICENSE](LICENSE).
