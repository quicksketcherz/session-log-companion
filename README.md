# Session Log Companion Skill

**Version:** 1.0  
**Created:** 2026-03-07  
**For:** Cursor AI / Claude Code

---

## What This Skill Does

A comprehensive project session companion that helps you:

1. **Start sessions** with clear documentation intent
2. **Create knowledge logs** when discovering or learning something
3. **Teach the agent** your preferences and communication style
4. **Summarize sessions** with comprehensive yet concise logs

---

## Quick Reference - Commands

**Full command reference:** See `references/COMMANDS.md` for complete list of commands, trigger phrases, and customization guide.

**Common commands:**

| Command | What it does |
|---------|--------------|
| `date "+%Y-%m-%d %H%M"` | Get current timestamp for file naming |
| `mkdir -p session-logs` | Create session logs folder |
| `mkdir -p resources/[tool]-knowledge-logs` | Create knowledge log folder for specific tool |
| `cp -r session-log-companion ~/.cursor/skills/session-log-companion` | Update the skill after editing |

**Trigger phrases:**
- "Start a session for [project]" → Begin session
- "Document this" → Create knowledge log
- "I prefer [style]" → Teach preference
- "Summarize this session" → End session

**Customization:** You can add your own commands and trigger phrases to `references/COMMANDS.md`. The agent will suggest adding useful commands as you work.

---

## Installation

Full step-by-step instructions are in **INSTALL.md** (copy & paste method first, terminal option for a faster install).

**Summary:**
- **Copy & paste:** Copy `session-log-companion` into `~/.cursor/skills/`, restart Cursor.
- **Terminal:** See "Quick Install Using Terminal" in INSTALL.md.
- **Test first:** Keep the folder in your workspace and reference it manually; when ready, follow INSTALL.md to install globally.

## How to Use

### Starting a Session

Just say:
- "Start a session for [project/task]"
- "Begin session log"
- "Let's work on X"

The skill will capture your intent and remind you about documentation as you work.

### Creating Knowledge Logs

When you hit something worth documenting:
- "Document this discovery"
- "Create a knowledge log"
- "I'm stuck with X" (triggers Discovery Log)
- "Can you explain how X works?" (triggers Learning Log)

The skill will:
1. Detect whether it's a Discovery or Learning log
2. Ask which tool to document for
3. Guide you through filling in the template
4. Save to the appropriate folder

### Teaching Preferences

When you want to improve how the agent works with you:
- "I want to improve how you work with me"
- "Remember this preference"
- "I prefer [communication style/pattern]"

The skill will:
1. Document your preference in a portable format
2. Offer to add it to `.cursor/rules/` for automatic enforcement
3. Explain when the preference applies

### Ending a Session

When you're ready to wrap up:
- "Summarize this session"
- "Create session log"
- "Wrap up"

The skill will:
1. Review what was accomplished
2. Check for undocumented items
3. Generate a comprehensive session log
4. Cross-reference any knowledge logs created

## Folder Structure Created

The skill creates these folders in your workspace as needed:

```
your-project/
├── session-logs/                           # Session summaries
├── resources/
│   ├── [tool]-knowledge-logs/             # Tool-specific discoveries/learnings
│   └── agent-companion-preference-logs/   # Your preferences for the agent
└── .cursor/
    └── rules/                             # Optional: Cursor-specific rules
```

## File Naming Convention

All logs use the same timestamp format for easy cross-referencing:

**Format:** `YYYY-MM-DD-HHMM-Brief-Title.md`

**Get timestamp:** `date "+%Y-%m-%d %H%M"`

**Example:**
- Session: `session-logs/2026-03-07-1430-TouchDesigner-Build.md`
- Knowledge: `resources/touchdesigner-knowledge-logs/2026-03-07-1445-Camera-Fix.md`
- Both share the date/time → instant cross-referencing

## What Makes This Different

**Smart detection:** Automatically suggests Discovery vs Learning log based on your language

**Platform-agnostic:** Preference logs work with any AI platform (Claude.ai, ChatGPT, Gemini)

**Cross-referencing:** Timestamp-based linking makes it easy to find related documentation

**Progressive disclosure:** Templates are bundled but only loaded when needed

**User control:** Never auto-creates logs - always asks first

## Reference Files

The skill includes these reference templates:

- `references/COMMANDS.md` - Command reference (customizable!)
- `references/discovery-log-template.md` - For problem-solving moments
- `references/learning-log-template.md` - For understanding concepts
- `references/session-log-template.md` - For session summaries
- `references/master-template.md` - Complete documentation system

## Tips for Best Results

1. **Start sessions explicitly** - Helps the skill understand your intent
2. **Document as you go** - Don't wait until the end
3. **Be specific about tools** - Helps organize knowledge logs properly
4. **Review before finalizing** - The skill generates drafts, you refine them
5. **Use cross-references** - Link related logs via "see notes:" pattern

## Troubleshooting

**Skill not triggering?**
- Check that it's installed in `~/.cursor/skills/`
- Try reloading the Cursor window
- Use explicit phrases like "start a session" or "create a knowledge log"

**Wrong log type suggested?**
- Just tell the skill which type you want - it will adapt
- The detection is a suggestion, not a requirement

**Folders not created?**
- The skill creates folders as needed
- Make sure you're in a writable directory
- Check file permissions

## Version History

**v1.0 (2026-03-08)**
- Initial release
- Four core workflows: start, document, teach, summarize
- Smart log type detection
- Platform-agnostic preference system
- Cursor rules integration
- COMMANDS.md reference file (customizable)
- Command tracking across all log types
- Agent prompts to update COMMANDS.md as you work

## Future Enhancements

Potential improvements for future versions:
- Auto-suggest documentation opportunities (with user confirmation)
- Template customization per project
- Integration with other documentation tools
- Team collaboration features
- Analytics on documentation patterns

## Feedback

This is a first iteration! Please provide feedback on:
- What works well
- What's confusing
- What's missing
- What could be better

The skill will evolve based on real usage patterns.
