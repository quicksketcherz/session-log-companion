# Session Log Companion (SLC) - Installation Guide

**Version:** 1.0  
**Created:** 2026-03-07

---
### Before You Begin Install.

Open your project folder in Cursor 1st. SLC is installed per-project at the project root.

## How to Install the Session Log Companion Skills

### Step 1: how to create a cursor skills folder (if there's is none)

1. **Ask Cursor to create a `skills` folder for this project.**
   - (You can do this by saying: “Create a skills folder for this project.”)

2. **If you already have a `/.cursor/skills` folder, continue to the next step.**

### Step 2: copy and paste the session-log-companion Folder

Copy the `session-log-companion` folder and paste it into your Cursor skills folder, so your directory looks like this: `~/.cursor/skills/session-log-companion`.

### Step 3: Restart Cursor

Close and reopen Cursor completely.

### Step 4: Test It

In Cursor, say: **"Start a session for my project"**

   *(This only checks the skill is loaded—it doesn't create a session log. Session logs are created when you say "Summarize this session" at the end of a session.)*

Done! ✓

**Note:** Comfortable with terminal? See "Quick Install Using Terminal" below for a faster method.

---

## Quick Install Using Terminal

For users comfortable with command line, here's the faster way:

1. **Open Terminal**
   - Mac: Press `Command + Space`, type "Terminal", press Enter
   - Windows: Press Windows key, type "PowerShell", press Enter
   - Linux: Press `Ctrl + Alt + T`

2. **Navigate to where you placed the skill folder**, then run:
   ```bash
   mkdir -p ~/.cursor/skills
   cp -r session-log-companion ~/.cursor/skills/session-log-companion
   ```

3. **Restart Cursor**

4. **Test it:** Say "Start a session for my project"

   *(This only checks the skill is loaded—it doesn't create a session log. Session logs are created when you say "Summarize this session" at the end of a session.)*

Done! ✓

---

## Quick Install (Alternative Method)

To install the session-log-companion skill in Cursor:

### Step 1: Copy to Cursor Skills Directory

Navigate to where you placed the skill folder, then run:

```bash
# Create the skills directory if it doesn't exist
mkdir -p ~/.cursor/skills

# Copy the skill
cp -r session-log-companion ~/.cursor/skills/session-log-companion
```

### Step 2: Restart Cursor

- Close and reopen Cursor
- Or use Command Palette: "Developer: Reload Window"

### Step 3: Test the Skill

Try one of these phrases:
- "Start a session for [your project]"
- "Document this discovery"
- "Summarize this session"

   *("Start a session" only verifies the skill is loaded—it doesn't create a session log. Session logs are created when you say "Summarize this session" at the end of a session.)*

The skill should trigger and guide you through the workflow.

---

## Alternative: Use from Workspace

If you want to test before installing globally:

1. Keep the `session-log-companion/` folder in your workspace
2. Reference it manually when needed
3. Once satisfied, follow the installation steps above (copy & paste or Quick Install Using Terminal)

---

## Verify Installation

To check if the skill is installed correctly:

```bash
# List installed skills
ls -la ~/.cursor/skills/

# You should see:
# session-log-companion/
```

Check the skill structure:

```bash
ls -la ~/.cursor/skills/session-log-companion/

# You should see:
# SKILL.md
# README.md
# TEST-SCENARIOS.md
# INSTALL.md
# references/
```

---

## Troubleshooting

### Skill Not Triggering

**Problem:** You say "start a session" but nothing happens

**Solutions:**
1. Check installation path: `~/.cursor/skills/session-log-companion/`
2. Verify SKILL.md has proper YAML frontmatter
3. Restart Cursor completely
4. Try more explicit phrases: "I want to create a session log"

### Permission Errors

**Problem:** Can't copy to `~/.cursor/skills/`

**Solutions:**
```bash
# Check if directory exists
ls -la ~/.cursor/

# Create it if needed
mkdir -p ~/.cursor/skills

# Check permissions
ls -la ~/.cursor/skills/

# If needed, fix permissions
chmod 755 ~/.cursor/skills
```

### Folders Not Created

**Problem:** Skill doesn't create `session-logs/` or `resources/` folders

**Solutions:**
1. Check you're in a writable directory
2. Verify file permissions in your workspace
3. Try creating folders manually first:
   ```bash
   mkdir -p session-logs
   mkdir -p resources/agent-companion-preference-logs
   ```

---

## Uninstall

To remove the skill:

```bash
# Remove from Cursor skills directory
rm -rf ~/.cursor/skills/session-log-companion

# Restart Cursor
```

Your documentation (session logs, knowledge logs, preference logs) will remain in your workspace.

---

## Update to Future Versions

### If you're using a source folder

**Recommended workflow:** Keep an editable source folder and copy it to Cursor when you make updates.

1. Edit your source folder (wherever you keep it)
2. Copy to Cursor (overwrites the installed version):
   ```bash
   cp -r session-log-companion ~/.cursor/skills/session-log-companion
   ```
3. Restart Cursor or reload window

**Tip:** If sharing with colleagues via Dropbox or GitHub, they can pull your updates and run the same copy command.

### If you're updating from a new release

When a new version is released:

1. Backup your current version (optional):
   ```bash
   cp -r ~/.cursor/skills/session-log-companion ~/.cursor/skills/session-log-companion.backup
   ```

2. Remove old version:
   ```bash
   rm -rf ~/.cursor/skills/session-log-companion
   ```

3. Install new version (navigate to where you placed the new version folder first):
   ```bash
   cp -r session-log-companion-v2 ~/.cursor/skills/session-log-companion-v2
   ```

4. Restart Cursor

---

## Platform-Specific Notes

### macOS

- Default install path: `~/.cursor/skills/`
- Use Terminal for installation commands
- May need to grant Terminal full disk access in System Preferences

### Linux

- Default install path: `~/.cursor/skills/`
- Use your terminal emulator
- Check file permissions if issues occur

### Windows

- Default install path: `%USERPROFILE%\.cursor\skills\`
- Use PowerShell or Command Prompt
- Adjust paths accordingly:
  ```powershell
  # PowerShell (navigate to where you placed the skill folder first)
  mkdir $env:USERPROFILE\.cursor\skills -Force
  Copy-Item -Recurse session-log-companion $env:USERPROFILE\.cursor\skills\session-log-companion
  ```

---

## Next Steps

After installation:

1. Read `README.md` for usage guide
2. Review `TEST-SCENARIOS.md` for examples
3. Try starting a session: "Start a session for [your project]"
4. Create your first knowledge log
5. Teach the agent your preferences
6. Summarize your session

---

## Support

For issues or questions:

1. Check `TEST-SCENARIOS.md` for expected behavior
2. Review `README.md` for usage tips
3. Verify installation steps above
4. Check Cursor's skill documentation

---

## What Gets Installed

```
~/.cursor/skills/session-log-companion/
├── SKILL.md                    # Main skill file with 4 workflows
├── README.md                   # Usage guide and quick reference
├── TEST-SCENARIOS.md           # Test cases (10 scenarios)
├── INSTALL.md                  # This file
└── references/
    ├── COMMANDS.md                  # Command reference (customizable!)
    ├── discovery-log-template.md    # Discovery log structure
    ├── learning-log-template.md     # Learning log structure
    ├── session-log-template.md      # Session log structure
    └── master-template.md           # Complete system guide
```

Total size: ~85KB

---

**Ready to install?** Use the copy & paste method at the top or Quick Install Using Terminal, then restart Cursor.
