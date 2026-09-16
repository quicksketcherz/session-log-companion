# Session Log Companion - Commands Reference

**Version:** 1.0  
**Created:** 2026-03-08  
**Purpose:** Living reference for all commands (standard + custom) used with this skill

---

## How to Use This Reference

### During Sessions
- Reference this file: `@COMMANDS.md` to see available commands
- The agent can suggest commands based on your current task
- Update this file as you discover new useful commands

### When Creating Preference Logs
If you're teaching the agent a preference that involves commands:
1. Create the preference log (Workflow 3)
2. Add the command to the "Custom Commands" table below
3. Reference this file in your preference log

**Example preference:**
"When I say 'check status', run: `git status && ls -la session-logs/`"
→ Add this to Custom Commands, then reference it in your preference log

### When Creating Knowledge Logs
If you discover a useful command while solving a problem:
1. Document the discovery/learning (Workflow 2)
2. Add the command to "Custom Commands" below
3. Reference it in your knowledge log: "see commands: COMMANDS.md"

---

## Standard Shell Commands

Common commands you'll use with this skill:

| Command | What it does | When to use |
|---------|--------------|-------------|
| `date "+%Y-%m-%d %H%M"` | Get current timestamp | For manual file naming |
| `mkdir -p session-logs` | Create session logs folder | If you want to set up folders manually |
| `mkdir -p resources/[tool]-knowledge-logs` | Create knowledge log folder | Replace `[tool]` with your tool name (e.g., `touchdesigner-knowledge-logs`) |
| `cp -r session-log-companion ~/.cursor/skills/session-log-companion` | Update the skill | After editing the skill folder, copy to Cursor skills folder |
| `ls -la ~/.cursor/skills/` | Check installed skills | Verify the skill is installed |
| `ls -la session-logs/` | List session logs | See all session logs with timestamps |
| `ls -la resources/[tool]-knowledge-logs/` | List knowledge logs | See all knowledge logs for a specific tool |
| `grep -r "search term" session-logs/` | Search session logs | Find specific content across all session logs |
| `tail -f session-logs/*.md` | Watch latest session log | Monitor session log as it's being written |

---

## Standard Trigger Phrases

Phrases that trigger the skill's workflows:

| Phrase | What workflow it triggers | Variations you can use |
|--------|---------------------------|------------------------|
| "Start a session for [project]" | Workflow 1: Starting a Session | "Begin session log", "Let's work on X" |
| "Document this" | Workflow 2: Creating Knowledge Logs | "Create a knowledge log", "I want to document this" |
| "I'm stuck with X" | Workflow 2: Discovery Log | "Hit an impasse", "This isn't working" |
| "Explain how X works" | Workflow 2: Learning Log | "Can you teach me X", "I need to understand X" |
| "I prefer [style]" | Workflow 3: Teaching Preferences | "Remember this preference", "I want to improve how you work with me" |
| "Summarize this session" | Workflow 4: Ending/Summarizing | "Create session log", "Wrap up", "End session" |

---

## Custom Commands (Your Additions)

**Add your project-specific commands here!**

This section is for commands you discover, create, or prefer to use in your workflow. The agent will suggest adding commands here when you:
- Document a discovery that involved useful commands
- Teach a preference about command usage
- End a session where specific commands were helpful

| Command | What it does | When to use | Notes |
|---------|--------------|-------------|-------|
| _Add your commands below_ | | | |
| | | | |
| | | | |
| | | | |

---

## Custom Trigger Phrases (Your Additions)

**Add your own natural language triggers here!**

If you have phrases you naturally use that should trigger workflows, add them here. The agent can learn to recognize these.

| Your Phrase | What it should trigger | Notes |
|-------------|------------------------|-------|
| _Add your phrases below_ | | |
| | | |
| | | |

---

## Command Preference Examples

Here are examples of command preferences you might document:

### Search Preferences
- Use `rg` (ripgrep) instead of `grep` for faster searching
- Use `fd` instead of `find` for finding files
- Use `fzf` for fuzzy finding in large directories

### Project-Specific Shortcuts
- `npm run dev:local` - Start dev server with local config
- `td-setup.sh` - Initialize TouchDesigner project
- `./build-and-test.sh` - Run full build and test suite
- `make clean && make` - Clean rebuild

### Documentation Shortcuts
- `session-start` - Alias for starting a session
- `session-end` - Alias for summarizing a session
- `doc-this` - Quick alias for documenting discoveries

### Tool-Specific Commands
- **TouchDesigner:** `touchdesigner -p project.toe` - Open project file
- **After Effects:** `aerender -project file.aep` - Render project
- **Git:** `git log --oneline --graph` - Visual commit history
- **Docker:** `docker-compose up -d` - Start containers in background

### Workflow Commands
- `git add session-logs/ && git commit -m "session: $(date +%Y-%m-%d)"` - Commit session logs
- `rsync -av session-logs/ backup/` - Backup session logs
- `tar -czf sessions-backup.tar.gz session-logs/` - Archive session logs

---

## How to Add Commands

### Method 1: During Knowledge Log Creation
When documenting a discovery or learning:
1. Include the commands you used in the "Commands Used" field
2. The agent will ask: "Want to add any of these to COMMANDS.md?"
3. Review and confirm which commands to add

### Method 2: During Preference Log Creation
When teaching the agent a preference about commands:
1. Create the preference log (Workflow 3)
2. The agent will ask: "Should I add this command to COMMANDS.md?"
3. Confirm and the agent will update this file

### Method 3: Manual Addition
You can edit this file directly:
1. Open `references/COMMANDS.md`
2. Add your command to the "Custom Commands" table
3. Save the file
4. The agent will see it next time you reference this file

---

## Cross-Referencing Commands

Use these patterns to reference commands in your logs:

**In Knowledge Logs:**
```markdown
**Commands Used:**
- `rg "search term" -t md` - Fast search across markdown files
- `fd "*.toe"` - Find all TouchDesigner files

**see commands:** `references/COMMANDS.md` for full command reference
```

**In Preference Logs:**
```markdown
**The Preference:**
Use `rg` instead of `grep` for all searching tasks.

**Commands:**
See `references/COMMANDS.md` - Custom Commands section

**Why:**
`rg` is 10x faster and has better syntax highlighting.
```

**In Session Logs:**
```markdown
**Commands Used:**
- `npm run dev` - Started development server
- `git commit -m "feature: X"` - Committed changes

**see commands:** `references/COMMANDS.md` for project command reference
```

---

## Tips for Building Your Command Reference

1. **Start small** - Don't try to document every command at once
2. **Add as you go** - When you discover a useful command, add it immediately
3. **Include context** - Note when/why to use each command
4. **Share with team** - This becomes a team knowledge base
5. **Keep it updated** - Remove commands you no longer use
6. **Add aliases** - Document your shell aliases for consistency
7. **Version control** - Commit this file so the team can track changes

---

## Platform-Specific Commands

### macOS
- `open .` - Open current directory in Finder
- `pbcopy < file.txt` - Copy file contents to clipboard
- `pbpaste > file.txt` - Paste clipboard to file

### Linux
- `xdg-open .` - Open current directory in file manager
- `xclip -sel clip < file.txt` - Copy file contents to clipboard
- `xclip -sel clip -o > file.txt` - Paste clipboard to file

### Windows (PowerShell)
- `explorer .` - Open current directory in Explorer
- `Get-Content file.txt | Set-Clipboard` - Copy file to clipboard
- `Get-Clipboard | Set-Content file.txt` - Paste clipboard to file

---

## Next Steps

1. **Review standard commands** - Familiarize yourself with the built-in commands
2. **Add your first custom command** - Start with one command you use frequently
3. **Reference in logs** - Use "see commands: COMMANDS.md" pattern in your documentation
4. **Build over time** - Let this reference grow naturally from your work

---

**This is a living document!** Update it as your workflow evolves. The more you use it, the more valuable it becomes.
