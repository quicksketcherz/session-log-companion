# Session Log Companion - Test Scenarios

**Purpose:** Test scenarios to verify the skill triggers correctly and provides appropriate guidance.

---

## Test Scenario 1: Starting a Session

**User prompt:** "Start a session for building a TouchDesigner particle system"

**Expected behavior:**
- Skill triggers
- Asks for session focus confirmation
- Notes timestamp
- Reminds about documentation
- Begins work on the stated goal

**Success criteria:**
- ✅ Skill recognizes "start a session" trigger phrase
- ✅ Captures project context (TouchDesigner)
- ✅ Sets documentation expectations
- ✅ Proceeds with user's goal

---

## Test Scenario 2: Discovery Log (Stuck/Impasse)

**User prompt:** "I'm stuck with this camera CHOP chain - it's not driving the camera. Document this."

**Expected behavior:**
- Skill triggers
- Detects "stuck" → suggests Discovery Log
- Asks which tool (should suggest TouchDesigner based on context)
- Gathers information about the gap
- Creates discovery log with proper template

**Success criteria:**
- ✅ Recognizes "stuck" and "document this" triggers
- ✅ Correctly suggests Discovery Log type
- ✅ Asks for tool confirmation
- ✅ Uses discovery-log-template.md structure
- ✅ Includes "Commands Used" section in the log
- ✅ Offers to add commands to COMMANDS.md
- ✅ Saves to correct folder with timestamp naming

---

## Test Scenario 3: Learning Log (Understanding)

**User prompt:** "Can you explain how LSystem turtle graphics works? I want to understand the angle symbols."

**Expected behavior:**
- Skill triggers
- Detects "explain" and "understand" → suggests Learning Log
- Provides explanation first
- After explanation, asks if user wants to document it
- If yes, creates learning log with proper template

**Success criteria:**
- ✅ Recognizes "explain" and "understand" triggers
- ✅ Correctly suggests Learning Log type
- ✅ Provides explanation before documenting
- ✅ Uses learning-log-template.md structure
- ✅ Includes Q&A, concepts, examples
- ✅ Includes "Commands Used" section in the log
- ✅ Offers to add commands to COMMANDS.md

---

## Test Scenario 4: Teaching Preferences

**User prompt:** "I prefer more technical explanations with less hand-holding. Don't explain basic concepts unless I ask."

**Expected behavior:**
- Skill triggers
- Recognizes preference statement
- Confirms understanding of the preference
- Creates preference log in agent-companion-preference-logs/
- Asks if user wants to add to .cursor/rules/

**Success criteria:**
- ✅ Recognizes preference expression
- ✅ Categorizes as "Communication style"
- ✅ Creates preference log with examples
- ✅ Checks if preference involves commands
- ✅ Offers to add commands to COMMANDS.md (if applicable)
- ✅ Offers Cursor rules integration
- ✅ Explains when preference applies

---

## Test Scenario 5: Ending a Session

**User prompt:** "Summarize this session"

**Expected behavior:**
- Skill triggers
- Reviews conversation history
- Extracts accomplishments, learnings, files
- Asks about undocumented items
- Creates session log with cross-references

**Success criteria:**
- ✅ Recognizes "summarize" trigger
- ✅ Reviews full session context
- ✅ Identifies knowledge logs created
- ✅ Lists commands used in the session
- ✅ Offers to add useful commands to COMMANDS.md
- ✅ Uses "see notes:" pattern for cross-references
- ✅ Generates comprehensive yet concise log

---

## Test Scenario 6: Ambiguous Context

**User prompt:** "Document what we just did with the particle system"

**Expected behavior:**
- Skill triggers
- Context is ambiguous (could be Discovery or Learning)
- Asks user which type fits better
- Proceeds based on user's choice

**Success criteria:**
- ✅ Recognizes "document" trigger
- ✅ Identifies ambiguity
- ✅ Asks clarifying question
- ✅ Adapts to user's choice

---

## Test Scenario 7: No Trigger (Should NOT activate)

**User prompt:** "What's the weather like today?"

**Expected behavior:**
- Skill does NOT trigger
- Normal conversation continues
- No documentation workflow initiated

**Success criteria:**
- ✅ Skill correctly stays inactive
- ✅ No false positive triggering

---

## Test Scenario 8: Cross-Referencing

**User prompt:** "Create a session log for today's work. We created a camera fix knowledge log earlier."

**Expected behavior:**
- Skill triggers
- Reviews session
- Finds the camera fix knowledge log
- Cross-references it in session log using "see notes:" pattern
- Uses matching timestamps

**Success criteria:**
- ✅ Identifies existing knowledge log
- ✅ Uses "see notes:" pattern correctly
- ✅ Includes timestamp-based cross-reference
- ✅ Lists in "Knowledge Logs Created" section

---

## Test Scenario 9: Command Reference and Customization

**User prompt:** "I used `rg 'search term' -t md` to find something. Document this and add it to my command reference."

**Expected behavior:**
- Skill triggers
- Creates knowledge log with command in "Commands Used" section
- Asks: "Would you like me to add this command to `references/COMMANDS.md`?"
- If yes, adds command to Custom Commands table in COMMANDS.md
- Includes context about when/why to use it

**Success criteria:**
- ✅ Captures command in knowledge log
- ✅ Offers to update COMMANDS.md
- ✅ Adds command to Custom Commands section
- ✅ Includes usage context in Notes column
- ✅ User can reference @COMMANDS.md later

---

## Test Scenario 10: Command Preference

**User prompt:** "I prefer using `rg` instead of `grep` for all searching. Remember this."

**Expected behavior:**
- Skill triggers (Workflow 3: Teaching Preferences)
- Creates preference log about command preference
- Asks: "Should I add `rg` to your COMMANDS.md?"
- If yes, adds to Custom Commands with preference note
- Offers Cursor rules integration

**Success criteria:**
- ✅ Recognizes command preference
- ✅ Creates preference log with command details
- ✅ Offers to update COMMANDS.md
- ✅ Links preference log to COMMANDS.md
- ✅ Offers Cursor rules integration

---

## Manual Testing Checklist

To test this skill manually:

1. [ ] Copy skill to `~/.cursor/skills/session-log-companion/` — see INSTALL.md for steps
2. [ ] Restart Cursor or reload window
3. [ ] Test each scenario above
4. [ ] Verify folder creation works
5. [ ] Check timestamp generation
6. [ ] Verify template usage
7. [ ] Test cross-referencing
8. [ ] Test COMMANDS.md updates
9. [ ] Test command tracking in logs
10. [ ] Test Cursor rules integration

---

## Known Limitations (v1.0)

- Skill does not auto-suggest documentation (requires explicit user request)
- Template customization requires manual editing
- No analytics on documentation patterns
- Single-user focused (no team collaboration features yet)

---

## Future Test Scenarios

For future versions, consider testing:
- Multiple knowledge logs in one session
- Editing existing logs
- Template customization
- Team collaboration workflows
- Integration with other tools
