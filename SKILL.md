---
name: session-log-companion
description: Comprehensive project session companion for documenting work sessions, creating knowledge logs when discovering or learning something, teaching agent preferences, and improving collaboration. Use when user says "start a session", "create session log", "summarize this session", "document this discovery", "create a knowledge log", "I want to improve how you work with me", "remember this preference", "let's continue", "continue from last session", "pick up where we left off", "what should I work on next", or any session/documentation-related request. Also trigger when user says "log this tangent", "log this branch", "make a tangent log", "make a branch log", "spinoff log", or "branched session log", or when one chat covered two projects belonging in two different folders — see Workflow 4b's four-test bar before suggesting a split. Also trigger when user mentions being stuck, hitting an impasse, needing to understand concepts, or wanting to capture learnings.
---

# Session Log Companion (SLC)

A comprehensive companion for project sessions that helps you document your work, capture discoveries and learnings, teach the agent your preferences, and build a knowledge base that improves collaboration over time.

**Abbreviation:** SLC - Use this when referencing this skill in documentation or conversation.

## When to Use This Skill

This skill triggers for four main scenarios:

1. **Starting a session** - "start a session", "begin session log", "let's work on X"
2. **Continuing a session** - "let's continue", "continue from last session", "pick up where we left off", "what should I work on next"
3. **Creating knowledge logs** - "document this", "create a knowledge log", "I'm stuck", "can you explain how X works"
4. **Teaching preferences** - "I want to improve how you work with me", "remember this preference", "I prefer X style"
5. **Ending a session** - "summarize this session", "create session log", "wrap up"

## Enforcement Rule

**When user requests any action covered by this skill's four workflows, you MUST follow the complete workflow steps - do not create files or take shortcuts directly.**

Key checkpoints:
- **Continue session** → Always ask intention first, then time available, before scanning session logs (Steps 1-2 of Workflow 1b)
- **Knowledge logs** → Always ask "Which tool should I document this for?" before creating (Step 3 of Workflow 2)
- **Preference logs** → Always offer Cursor rules integration after creating (Step 3 of Workflow 3)
- **Session logs** → Always check for undocumented items before finalizing (Step 2 of Workflow 4)
- **Any log** → Always extract the chat's screenshots from the session jsonl BEFORE writing anything (Step 0 of Workflow 4) — do it, never ask
- **Session logs** → **READ `references/session-log-template.md` BEFORE writing a single line.** Never work out the shape by opening a previous session log. See the pre-flight below — it is not optional.

### Pre-flight — emit this before writing any log

Immediately before writing a session log, output this line so the check is visible rather than remembered:

```
PRE-FLIGHT — template: read (N sections) · knowledge logs: asked/none · screenshots: extracted/owned-by-DNC
```

If any field cannot honestly be filled, **stop and go do that step.** The line is the point: a step you have to report on is a step you notice skipping, and a step you merely intend to take is one you will not.

**An existing log is not the template.** Opening a previous session log to see "how it's usually laid out" is the specific failure this guards against. It feels like research, it produces something that looks right, and it silently drops whatever sections that particular log happened to omit. The previous log is an *example*; `references/session-log-template.md` is the *spec*. Read the spec.

If you find yourself about to create a log file without following the workflow steps, stop and restart with Step 1 of the appropriate workflow.

**Why this matters:** Skipping workflow steps breaks folder organization, misses user preferences, and creates inconsistent documentation across projects.

**And why the reminder sits HERE, at the top, rather than only inside Step 4:** it failed twice as a numbered step buried mid-workflow — 2026-08-22 (skill not loaded at all) and 2026-09-07 (skill loaded, Step 3 obeyed, template read skipped). Both times the log was built from a previous log's headings. The second time there was a memory in context naming Step 3 by number, and Step 3 was the step that held. **Rules get followed to exactly the specificity, and the placement, they are written at.** A rule read once at the head of a three-hour session has to survive a dozen tool calls before the moment it applies; a rule that demands a visible pre-flight line does not.

## Core Workflows

### Workflow 1: Starting a Session

When the user wants to begin a work session:

1. **Capture session intent:**
   - Ask: "What's the focus of this session?"
   - Note the current timestamp: `date "+%Y-%m-%d %H%M"`
   - Identify the project context (current directory, open files)

2. **Set documentation expectations:**
   - Remind: "I'll help document discoveries and learnings as we work"
   - Explain: "Just say 'document this' when you hit something worth capturing"

3. **Begin work:**
   - Proceed with the user's stated goal
   - Stay alert for moments worth documenting (impasses, discoveries, learning opportunities)

**Note:** Starting a session does not create a session log file. Session logs are created in Workflow 4 when the user says "Summarize this session" at the end of a session.

**Example interaction:**

User: "Start a session for building a TouchDesigner particle system"

Agent: "Got it! We're starting a session on TouchDesigner particle systems. I'll help document any discoveries or learnings as we work. What's the first thing you want to tackle?"

---

### Workflow 1b: Continuing a Session

When the user says "let's continue", "pick up where we left off", "what should I work on next", or similar:

#### Step 1: Ask Intention

Ask: "What do you want to work on?"

The user may already know exactly what they want to do (from a session hours ago, or an idea they had offline). Let them state it first — don't dump a list of options before they've had a chance to think.

#### Step 2: Ask Time Available

Ask: "How much time do you have?"

This scopes what's realistic. A 10-minute session is different from an hour — don't suggest deep refactoring work for a quick session.

#### Step 3: Scan Recent Session Logs

Read the last 5 session logs in `session-logs/` (sorted by filename, most recent first). Extract the **Next Steps** section from each.

**If user stated a clear intention** → Match their intention against the collected Next Steps. Surface any relevant items and note which session they came from. This helps the user see connections they might have forgotten ("Oh right, that's related to what I was doing last week").

**If user draws a blank** → Present the Next Steps from recent sessions as a menu of options, grouped by session. Let the user pick what feels right.

#### Step 4: Scope to Time

Based on the time available, help the user pick a realistic slice:
- **10 min** → one small, contained task (a single next step item, a quick note, a review)
- **20-30 min** → one substantial task or 2-3 small ones
- **1+ hour** → a full work block, potentially spanning multiple next steps

Don't over-plan — just confirm the focus and begin.

#### Step 5: Begin Work

Proceed with Workflow 1 (set documentation expectations, stay alert for moments worth documenting). The continue workflow feeds into the regular session flow.

**Example interactions:**

User: "Let's continue"

Agent: "What do you want to work on?"

User: "The deep modules thing for TD containers"

Agent: "How much time do you have?"

User: "About 20 minutes"

Agent: *Scans last 5 session logs, finds relevant Next Steps from 2026-05-20-0219*

Agent: "From your last session, you had these next steps related to that:
- Decide whether to create a separate `/td-deepen-architecture` skill or fold it into TSC
- Adapt the vocabulary mapping into a proper SKILL.md
- Test the deletion test against real TD scaffold outputs

With 20 minutes, we could tackle the first decision and sketch the outline if you go separate skill. Want to start there?"

---

User: "What should I work on next?"

Agent: "What are you thinking? Anything specific on your mind?"

User: "Not really, just have some time"

Agent: "How much time?"

User: "Like an hour"

Agent: *Scans last 5 session logs, presents Next Steps grouped by session*

Agent: "Here's what's open from recent sessions:
**From 2026-05-20 (Deep Modules Research):**
- Decide on separate skill vs folding into TSC
- Test deletion test against real TD scaffolds

**From 2026-05-20 (First Complete Draft):**
- [items from that session's next steps]

What catches your eye?"

---

### Workflow 2: Creating Knowledge Logs

When the user wants to document something or you detect a documentation opportunity:

#### Step 1: Detect Log Type

Analyze the user's language and context to suggest the appropriate log type:

**Discovery Log indicators:**
- User says: "stuck", "not working", "error", "impasse", "AI suggested X but Y works"
- Context: Spent >15 min on problem, found non-obvious solution, AI was wrong
- Pattern: Problem → Solution flow

**Learning Log indicators:**
- User says: "explain", "how does", "understand", "what is", "can you teach me"
- Context: Q&A session, building foundational knowledge, filling gaps
- Pattern: Question → Understanding flow

**If unclear:** Ask the user which type fits better.

#### Step 2: Gather Information

**For Discovery Logs:**
- What were you trying to do?
- What did the AI suggest (if applicable)?
- What broke or didn't work?
- What actually works?
- What tool/version are you using?

**For Learning Logs:**
- What did you need to understand?
- Why does it matter to your project?
- What questions did you have?
- What concepts did we cover?

#### Step 3: Determine Folder Location

Ask: "Which tool should I document this for?"

**Folder naming convention:** `resources/[tool]-knowledge-logs/`

Examples:
- TouchDesigner → `resources/touchdesigner-knowledge-logs/`
- After Effects → `resources/aftereffects-knowledge-logs/`
- General development → `resources/general-development-knowledge-logs/`

Create the folder if it doesn't exist.

#### Step 4: Create the Knowledge Log

0. **Extract the chat's screenshots first** — Step 0 of Workflow 4 applies here too. Knowledge logs are not exempt.
1. Generate timestamp: `date "+%Y-%m-%d %H%M"`
2. Ask for a brief title (or suggest one based on topic)
3. Read the appropriate template:
   - Discovery: `references/discovery-log-template.md`
   - Learning: `references/learning-log-template.md`
   - **If not found in the project directory**, read from the global install: `~/.claude/skills/session-log-companion/references/`
4. Fill in the template with information gathered
5. Include any commands used in the "Commands Used" section
6. Save to: `resources/[tool]-knowledge-logs/YYYY-MM-DD-HHMM-Brief-Title.md` — or, if Step 0 pulled out screenshots, to `resources/[tool]-knowledge-logs/YYYY-MM-DD-HHMM-Brief-Title/` with the `.md` and `attachments/` inside

#### Step 5: Offer to Update COMMANDS.md

After creating the knowledge log, if commands were used:

Ask: "Would you like me to add any of these commands to `references/COMMANDS.md` for future reference?"

If yes:
1. Read `references/COMMANDS.md`
2. Add the command(s) to the "Custom Commands" table
3. Include context about when/why to use them

**Example interaction:**

User: "I'm stuck with this camera CHOP chain - it's not driving the camera. Document this."

Agent: "This sounds like a Discovery Log (you hit an impasse). Which tool should I document this for - TouchDesigner?"

User: "Yes"

Agent: *Creates discovery log at `resources/touchdesigner-knowledge-logs/2026-03-07-1430-Camera-CHOP-Chain-Not-Driving-Camera.md`*

Agent: "I noticed you used `touchdesigner -debug` to solve this. Want to add it to COMMANDS.md?"

---

### Workflow 3: Teaching Agent Preferences

When the user wants to teach you their preferences or improve collaboration:

#### Step 1: Identify the Preference

Listen for preferences about:
- **Communication style:** Technical depth, formality, verbosity
- **Documentation patterns:** How detailed, what structure
- **Code commenting:** When and how to comment
- **Explanation style:** Analogies vs theory, examples vs concepts
- **Workflow patterns:** How they like to work, what to assume

#### Step 2: Create Preference Log

1. Generate timestamp: `date "+%Y-%m-%d %H%M"`
2. Create folder if needed: `resources/agent-companion-preference-logs/`
3. Document the preference with:
   - What the preference is
   - Why it matters to the user
   - Examples of good vs bad
   - When to apply it
4. Save to: `resources/agent-companion-preference-logs/YYYY-MM-DD-HHMM-Preference-Title.md`

**Template for preference logs:**

```markdown
# [Preference Title]

**Date:** YYYY-MM-DD  
**Time:** HHMM  
**Category:** [Communication/Documentation/Code/Explanation/Workflow]  
**Type:** Agent Preference

---

## The Preference

**What:** [Clear statement of the preference]

**Why:** [Why this matters to the user]

---

## Good Examples

**Example 1:**
[What this looks like when done right]

**Example 2:**
[Another good example]

---

## Avoid

**Example 1:**
[What NOT to do]

**Why it's wrong:** [Explanation]

---

## When to Apply

[Contexts where this preference matters]

---

## Notes

[Any additional context or exceptions]

---

## Commands (if applicable)

**If this preference involves commands, list them here:**
- `[command]` - [When/how to use it]

**see commands:** `references/COMMANDS.md` for full command reference
```

#### Step 3: Check for Command Preferences

If the preference involves commands or workflows:

Ask: "Should I add this command to `references/COMMANDS.md` for easy reference?"

If yes:
1. Read `references/COMMANDS.md`
2. Add the command to the "Custom Commands" table
3. Note the preference in the command's "Notes" column

#### Step 4: Offer Cursor Rules Integration

If the user is in Cursor, ask:

"Would you like me to also add this to `.cursor/rules/` so it's automatically enforced in Cursor?"

If yes:
1. Create or update `.cursor/rules/preferences.md`
2. Add a rule that references the preference log
3. Format: "See `resources/agent-companion-preference-logs/[filename]` for details"

**Example interaction:**

User: "I prefer more technical explanations with less hand-holding. Don't explain basic concepts unless I ask."

Agent: "Got it. I'll document this preference. This is about communication style - you want me to assume technical knowledge and skip basics unless requested."

*Creates preference log*

Agent: "Would you like me to also add this to `.cursor/rules/` so it's automatically enforced in Cursor?"

---

### Workflow 4: Ending/Summarizing a Session

When the user wants to wrap up and create a session log:

#### Step 0: Extract every image from the session jsonl FIRST

**Before deciding anything else.** This is step zero, not an afterthought. Any screenshot the user posted in this chat gets pulled out, visually verified against the project, and saved into the log's `attachments/` folder — which makes that log a **folder-log** (see *Attachments & log folders*). Applies to **every log type** — session logs, knowledge logs, branched logs — not just the ones that feel visual. Never ask permission ("want me to attach it?" is wrong — just do it). Never skip it because the image's content was already transcribed into the body. An older log with no attachments is a bug, **never** a precedent to copy.

**How:** find the most recently modified jsonl at `~/.claude/projects/<project-slug>/<session-uuid>.jsonl` and extract every uploaded image. **Visually verify each image belongs to this project and prune strays** — `@`-referencing another note folder during the chat embeds that folder's images into the jsonl, so the extractor picks those up too.

**The one thing that can stop this step:** DNC owns the images for this work block. See *Who owns the screenshots: DNC or SLC* — check that first, and if DNC owns them, link to them instead of copying. Nothing else stops this step.

#### Step 1: Prepare

1. **Read `references/session-log-template.md` NOW** — before the investigation, not after it. It moved here from Step 4 on 2026-09-07 because by the time Step 4 arrived, writing had already effectively begun and the template read got skipped. Reading it first puts the required sections in mind while you are still gathering, so you gather the right things. If not found in the project, use `~/.claude/skills/session-log-companion/references/session-log-template.md`.
2. Check if `session-logs/` exists
3. **List `resources/` folder** to discover existing `*-knowledge-logs/` folders
4. **Read `resources/README-KNOWLEDGE-LOGS.md`** (if exists) to get templates and folder index

**There is no `session-logs/README.md` step any more.** Dropped 2026-09-15. It sent the agent hunting for READMEs in folders that have none, and worse, it implied a session log's shape could come from somewhere other than this skill. **"Do a session log" has always meant: run this skill.** It has never meant "go find a README somewhere and follow that." The spec is `references/session-log-template.md` — not a README, not a previous log. (Item 4 above survives because `README-KNOWLEDGE-LOGS.md` is a folder index, not a spec for the log.)

#### Step 2: Review the Session for "Document Later" Requests

**⚠️ CRITICAL: Go through the entire session/conversation BEFORE writing the log.** Don't start writing until you've reviewed for items the user asked to add.

**Check for these phrases:**
- "document this later" / "document later"
- "log this as knowledge"
- "create a knowledge log" / "add this to the knowledge logs"
- "will document this" / "remind me to document"
- "take note of this" / "note this" / "note it"
- "update the docs (if this works)" / "add to the project docs"
- "update the guide" / "fix the guide" / "update instructions"
- "this doesn't match the guide" / "the guide says X but Y works"
- User shared screenshots/files and said to document
- User asked to retrieve info from another chat for documentation

**If found:** These become **separate knowledge log files**, referenced in the session log with "see notes:" — NOT included inline in the session log.

#### Step 3: Session Assessment

**Ask yourself these questions before creating the session log:**

1. **Was there substantial Q&A?** (>3 questions about concepts) → Likely needs Learning Log
2. **Did we solve a non-obvious problem?** (>15 min debugging, AI was wrong) → Likely needs Discovery Log
3. **Did user learn foundational concepts?** (understanding principles, "why" explanations) → Likely needs Learning Log
4. **Is this knowledge reusable?** (Would user benefit from reference material?) → Suggest knowledge log

**If any are YES, ask user BEFORE creating session log:**
"This session covered [topic] for [tool]. Should I create a knowledge log in `[tool]-knowledge-logs/`? It would be useful as reference material for [specific benefit]."

Wait for confirmation before proceeding.

#### Step 4: Generate Session Log

1. Generate timestamp: `date "+%Y-%m-%d %H%M"`
2. **Emit the PRE-FLIGHT line** (see Enforcement Rule). The template was read back in Step 1 — if it was not, stop and read it now; do not proceed from memory or from a previous log.
3. Fill in all sections based on session review
4. Use "see notes:" pattern to reference any knowledge logs created
5. Include "AI Rules to Create Later" or "Guides to Update Later" sections if applicable
6. **Always include an "Honest Self-Assessment" section** — see required sections below
7. **Always end with a "Session Insight" section** — see required sections below
8. Save to: `session-logs/YYYY-MM-DD-HHMM-Session-Title.md` — or, if Step 0 pulled out screenshots, to `session-logs/YYYY-MM-DD-HHMM-Session-Title/` with the `.md` and `attachments/` inside (see *Attachments & log folders*)

**Required sections (always include):**

- **Honest Self-Assessment** — placed after testing/accomplishments and before "Carry Forward to Next Session." Names what didn't work, what's untested, what's parked, and what the agent or user might be pattern-matching ahead of evidence. The point is to prevent future-self from reading the log and assuming everything was settled when it wasn't. Keep it short — 2–4 honest bullet points or a short paragraph. If the session genuinely had no caveats worth flagging, write "No significant caveats — everything tested was validated by results" rather than skipping the section.

- **Session Insight** — the final section of every session log. One sentence (not a list, not a paragraph) on what changed about how the user works, or what design principle the session surfaced. The constraint of "one sentence" is the design — it forces a *meta* observation rather than a recap. If you can't condense it to one sentence, the insight isn't ready yet.

**Key principles for session logs:**
- Keep it concise - use "see notes:" to reference detailed documentation
- Cross-reference knowledge logs by timestamp
- Only list project files in "Files Created/Modified" (not the logs themselves)
- Capture the "why" behind decisions, not just the "what"
- Capture the texture of the session, not just the outputs — the *how* of the work is what makes logs worth re-reading later
- Leave "USER_FILL_WHAT_AI_MODEL_NAME_WAS_USED" as-is (the agent cannot detect the model name in Cursor; the user will fill it in manually from their model selector)

**Note on template file:** If `references/session-log-template.md` exists in the project, it should also be updated to include the Honest Self-Assessment and Session Insight sections so the template and this SKILL.md stay aligned.

**Documenting code/expressions:** When including code snippets, expressions, scripts, or configurations in session logs, always include context: **Where used** (which file/operator/parameter), **What it does** (brief explanation), and **How it connects** (integration with the rest of the system). Code without context is hard to reuse.

#### Step 5: Update Project Docs

If the project maintains reference documentation (setup guides, quick reference, troubleshooting, implementation guides, etc.), apply any **new discoveries or solutions that worked** from this session to those docs. Update only relevant sections — do not rewrite entire docs.

**Living Documentation Principle:** Guides should reflect reality through real-world testing, not just initial research. Check for guide updates needed:

- Did we discover version-specific differences? (parameters, pages, behavior)
- Did we find corrections to existing documentation?
- Did implementation steps need clarification based on actual usage?
- Are there inaccuracies between guide and current tool version?

**If YES:** Update the guide with corrections. Document what was wrong vs what actually works. Add to the "Guides Updated" section of the session log.

#### Step 6: Check for AI Rules Log Need

**Did this session involve improving the documentation system or updating AI rules?**

- Updated or created **Cursor rules** (`.cursor/rules/`) or **rules/instructions on another platform** → **Always create an AI rules log** (don't ask, don't skip)
- Corrected AI behavior about session/knowledge log workflow → Create AI rules log
- Updated/created README instructions → Ask if AI rules log is needed
- Clarified ambiguous phrasing in documentation system → Ask if AI rules log is needed

**When creating:** Save to `ai_rules_logs/YYYY-MM-DD-HHMM-Brief-Description.md` using the template in `ai_rules_logs/README.md`, and reference in session log with "see notes:".

#### Step 7: Post-Session Log Workflow

**⚠️ CRITICAL: After the session log is created, immediately check for undocumented items and offer to create them.**

This workflow prevents breaking the user's flow during discovery while ensuring everything gets documented.

**Check these sections of the session log:**

1. **"AI Rules to Create Later" section** — If any rules are listed with "📝 To document" status:
   - Say: "I noticed we have [N] AI rules to document. Want me to create those AI rules logs now?"
   - If yes, create each AI rule log in `ai_rules_logs/` folder using same timestamp
   - Update session log's section to show ✅ status

2. **"Knowledge Logs Created" section** — If discoveries/learnings happened but no logs were created:
   - Say: "I noticed we discovered [X]. Should I create a knowledge log for this?"
   - If yes, create appropriate knowledge log in `resources/[tool]-knowledge-logs/`
   - Update session log to include the new knowledge log

3. **"Guides to Update Later" section** — If guide corrections are listed:
   - Say: "Should I update the guides now with the corrections we found?"
   - If yes, apply corrections to guides
   - If no, note for next session

**Why this matters:** Doesn't interrupt flow during active discovery/implementation. Converts "to do later" items into actual documentation. User can choose to defer if in a hurry.

#### Step 8: Offer to Update COMMANDS.md

After creating the session log, if useful commands were used:

Ask: "Would you like me to add any of the commands from this session to `references/COMMANDS.md`?"

If yes:
1. Read `references/COMMANDS.md`
2. Add the command(s) to the "Custom Commands" table
3. Include context about the session where they were useful

#### Step 9: Confirm Completion

Summarize what was documented:
- Session log location
- Knowledge logs created (with links)
- Preference logs created (if any)
- AI rules logs created (if any)
- Guides updated (if any)

#### Post-Session Knowledge Log Creation

**If user requests additional knowledge logs AFTER session log is written:**

1. **Create the knowledge log** — Use same timestamp as session log
2. **Update the session log** — Add new knowledge log to "Knowledge Logs Created" section with "see notes:" reference and "(added post-session)" notation
3. **Keep it accurate** — Session log should reflect ALL knowledge logs from that session

**Example interaction:**

User: "Summarize this session"

Agent: *Reviews conversation, checks for "document later" items, identifies accomplishments*

Agent: "Before I create the session log — this session had substantial Q&A about [topic]. Should I create a knowledge log for that?"

User: "Yes"

Agent: *Creates knowledge log, then session log with "see notes:" cross-reference*

Agent: *Checks post-session items:* "I noticed we have 2 AI rules to document from this session. Want me to create those now?"

User: "Yes"

Agent: *Creates AI rules logs, updates session log*

Agent: "Session documented! Created:
- Session log: `session-logs/2026-03-07-1430-TouchDesigner-Particle-System-Build.md`
- Knowledge log: `resources/touchdesigner-knowledge-logs/2026-03-07-1430-Camera-CHOP-Chain-Fix.md`
- AI rules log: `ai_rules_logs/2026-03-07-1430-Session-Log-Timing-Rule.md`"

---

### Workflow 4b: Branched / Tangent Session Log

**Use when:** One chat covered two genuinely different bodies of work. Rather than one log that half-belongs in each project's folder, spin off a second log scoped to the tangent and file it where that work actually lives.

**Why this exists — findability.** A log about skill maintenance sitting in COA2026's `session-logs/` is a log nobody will find when they go looking for skill maintenance. Two logs, each in the right folder, each carrying a cross-reference to the other, beat one log in the wrong place. The cross-reference is what makes the split safe: nothing gets orphaned, either log leads you to the other.

#### When to suggest it (and when not to)

You **may** suggest a split — the user often won't think to ask, and the filing benefit is real. But suggest it only when **all four** of these hold:

1. **Different project or area.** Not a different topic within the same project — a different folder, a different tag. COA2026 → skill maintenance qualifies. COA2026 titles → COA2026 exports does not.
2. **It produced its own artifacts.** Files written, decisions made, something that exists now. Discussion alone is not a branch.
3. **It could stand alone.** Enough substance that the log is worth opening on its own. A two-message aside is not a branch.
4. **The two would be filed in different folders.** If both logs would land in the same `session-logs/`, there is no findability gain — so there is no reason to split.

**If any one of the four fails → one log, Workflow 4, and don't raise it.**

**How to suggest it — once, in one line, naming the actual split:**

> *"This chat covered two things — COA2026 editing and the DNC skill update. Want them as two logs, one in each project's folder, cross-referenced? Or one log?"*

Rules for the ask:
- **Ask once.** No answer, or an unclear one → one log. Don't re-raise it later in the same session.
- **Name both halves** so the user can judge it instantly. Never ask the vague "should this be separate?" — that makes them do the thinking.
- Ask **before** writing, not after. Offering to split a log you already wrote wastes both of you.
- If the user said a number ("just do a session log", "one log"), that settles it. Don't ask.

**The 2026-09-07 failure this bar is calibrated against:** a branch log was proposed for a tangent that was really just the same session continuing — same project, no separate artifacts, both logs would have landed in the same folder. It failed tests 1, 2 and 4. Two logs were proposed where one was wanted. The capability was never the problem; the missing bar was.

**Trigger phrases — when the user asks directly, skip the bar and just do it:**
- "log this tangent" / "log this branch" *(canonical)*
- "make a tangent log" / "make a branch log"
- "spin off a log for [X]" / "separate log for [X]"
- "branched session log" / "spinoff log"

#### Step 1: Identify the branch's start point

Two approaches, in order of preference:

1. **Scan the chat for the topic-shift cue.** Look back through the conversation for the message where the new scope began. Tells include: a new project name appearing, phrases like "by the way," "while we're here," "let's shift to X," "i'm noticing X," or a hard pivot from one tool/domain to another. Use the timestamp of that message (from the session jsonl) as the branch's start.
2. **If the shift point is ambiguous, ask** — one short line: *"where do you see the tangent starting? Around when we started talking about X?"* Don't guess silently.

#### Step 2: Determine the branch's scope

Quickly characterize the branch:
- **Project / domain** — what is the tangent about? (often different from the original session)
- **Artifacts produced** — what got built/decided/created in the branch
- **Where does the branch log belong?** — usually the branch's project folder, NOT the original session's folder (e.g. a DNC-skill tangent spun off from a COA2026 session belongs in DNC's `session-logs/`, not COA2026's)

#### Step 3: Create the branched session log

Follow Workflow 4 (Steps 0, 2-4) normally — review for "document later" items, do the session assessment, generate the log. With three differences:

1. **Timestamp:** use the branch's START time (from Step 1), not chat-open and not filing time.
2. **First line under the title:** add a `**spun off from:** <vault-relative-path-to-original-session-log>` line so the navigation thread is preserved.
3. **Scope:** the "Session Focus," "What We Accomplished," "Files Created/Modified," etc. cover ONLY the branch — don't re-include the original session's work.

#### Step 4: Cross-reference BOTH logs — the link goes both ways

A one-way link only works if you already know the branch log exists. Someone opening the original log has no idea. So both logs get a pointer:

- **Branch log** → `**spun off from:** <vault-relative-path-to-original-session-log>` (added in Step 3).
- **Original log** → add a `see notes:` line pointing at the branch log, using the same convention every other log in the vault uses.

That is the **only** edit to the original. Do **not** go back and strip the branch material out of it, and do not rewrite its scope. It already records what happened honestly — it just gains one line saying where the rest of the story went.

**Why this changed (2026-09-15):** this step used to say "leave the original untouched — the branch log links back, that's enough." It isn't enough. The whole point of splitting is findability, and a link you can only follow in one direction means anyone starting from the original hits a dead end.

#### Step 5: If DNC also ran in the original session, spin off a branched daily note too

If you spun off a session log, you almost certainly want a matching branched daily note. Tell DNC: "also branch the daily note from the same start point." DNC's branched-filing rule will fire (see DNC's "Branched filing" subsection).

#### Example interaction

User: *(during a chat that started as COA2026 video editing, then drifted into updating the DNC skill)* "log this branch — the DNC skill maintenance part"

Agent: *Scans chat, finds the shift point around "by the way, would we do or add something in the skill that..." at 0500*

Agent: "Branch starts at 0500 when we shifted from COA2026 editing to DNC skill maintenance. Creating spinoff log scoped to the DNC promotion pass + new rule + repackage. Saving to `resources/agent-skills-library/daily-notes-companion/session-logs/2026-06-19-0500-DNC-Promotion-Pass.md`."

*Writes the branched log with the `**spun off from:** .../2026-06-19-0314-COA2026-Multicam-Edit-Setup.md` line at the top. Original COA2026 log stays untouched.*

---

## AI Rules Logs

**Purpose:** Track how AI assistants learn to work with your documentation system. Capture improvements and corrections so they're portable across projects and platforms.

**Folder:** `ai_rules_logs/` at project level (visible, not hidden — matches `session-logs/` pattern)

**File format:** `YYYY-MM-DD-HHMM-Brief-Description.md`

**Create when:**
- Updated or created Cursor rules (`.cursor/rules/`) → always create (don't skip)
- Updated rules/instructions on another platform (Claude Projects, ChatGPT, Gemini) → always create
- Corrected AI behavior about documentation workflows
- Updated/created README instructions (session_logs, knowledge logs, etc.)
- Clarified ambiguous phrasing in documentation system

**Don't create when:**
- One-time correction specific to current project task
- Session was about project work only (no documentation system changes)
- AI made a simple mistake that won't repeat

**Workflow:** When creating a session log after discussing rule improvements, create the AI rules log in `ai_rules_logs/` and reference in session log with "see notes:". If Cursor rules or rules on any other AI platform were updated, always create an AI rules log. For README-only or phrasing changes, ask the user first.

**Template:** Read `ai_rules_logs/README.md` in the project for the full template.

---

## Use with Any AI or Platform

These instructions apply whether using Cursor, Claude, Gemini, ChatGPT, or another AI. The core workflow is the same: review the session for notes to add, run the checklist (document later → knowledge logs, update project docs if applicable, AI rules log if rules/instructions were updated). If your platform uses a different place for rules (e.g. not `.cursor/rules/`), treat updates there the same way — create an AI rules log and reference it in the session log with "see notes:".

---

## Smart Defaults

To make the workflows smooth, use these smart defaults:

**Timestamps:**
- Always generate with: `date "+%Y-%m-%d %H%M"`
- Use same timestamp for cross-referencing related logs

**Project context:**
- Detect current directory and open files
- Suggest tool based on file extensions (.toe = TouchDesigner, .aep = After Effects, etc.)

**Pre-fill known info:**
- AI model: Leave as `WHAT_AI_MODEL_USED?` (agent cannot detect model in Cursor; user fills in manually)
- AI platform: Cursor (or current platform)
- Date: Current date

**Folder creation:**
- Create `session-logs/` if it doesn't exist
- Create `resources/[tool]-knowledge-logs/` as needed
- Create `resources/agent-companion-preference-logs/` as needed
- Create `ai_rules_logs/` as needed

---

## Attachments & log folders

Most logs are a single plain `.md`. A log that carries screenshots becomes a **folder** instead — named exactly like the log, with the `.md` inside keeping that same name so it stays self-identifying if it's ever moved or searched:

```
session-logs/
  2026-09-06-2140-SLC-Screenshot-Saving/
    2026-09-06-2140-SLC-Screenshot-Saving.md      ← the log (same name as the folder)
    attachments/
      01-jsonl-extract-output-claude-skills.png    ← NN-short-descriptor-TERM.ext
      02-attachments-folder-in-finder-claude-skills.png
```

**The rule, in one line:** screenshots? → folder. None? → just the `.md`.

- **Knowledge logs use the same shape:** `resources/[tool]-knowledge-logs/YYYY-MM-DD-HHMM-Brief-Title/` with the `.md` and `attachments/` inside.
- **Naming:** `NN-short-descriptor-TERM.ext`, 2-digit chronological prefix, matching DNC exactly.
- **In the body:** one line — `N screenshots attached (see attachments/)` — rather than listing each.
- **Cross-referencing is unchanged.** The shared `YYYY-MM-DD-HHMM` stamp still does the matching whether the log is a file or a folder.

**Why folder-per-log and not one shared `attachments/` inside `session-logs/`:** a shared folder can't say which log an image belongs to, and SLC logs move — they get dropped into a DNC note folder for the same work block. A folder-log moves in one piece, and it is the shape DNC already uses.

---

## Who owns the screenshots: DNC or SLC

Both skills read the same session jsonl, so without a rule the same screenshot lands in two places.

**The rule: whoever files the *folder* for that work block owns the images. The other one links.**

- **DNC files a folder-note for this block** (the normal case — a worksession note with extras) → **DNC owns the images.** They live in the daily note's `attachments/`. The SLC log for the same block does NOT copy them; it points at them by vault-relative path in its `see notes:` block.
- **DNC files a plain `.md` for this block** — which is exactly what DNC's *Special case* does when the worksession's whole point was building or modifying a Claude skill, because those logs live in the skill's repo rather than the vault → **SLC owns the images.** Extract into the log's own `attachments/`.
- **DNC never ran**, or this is a knowledge log or branched log with no matching daily note → **SLC owns the images.**

**How to tell, at filing time:** look in `daily-notes/` for a note covering the same block — same day, same term, matching or adjacent `YYYY-MM-DD-HHMM` stamp. Found a *folder* note with `attachments/` → link. Found a plain `.md`, or found nothing → extract.

One copy exists; the other side carries a path to it. Never both, and never zero.

---

## Cross-Referencing System

Use timestamp-based cross-referencing to link related documentation:

**Example:**
1. Session at `2026-03-07 14:30`
2. Session log: `session-logs/2026-03-07-1430-Session-Title.md`
3. Knowledge log: `resources/touchdesigner-knowledge-logs/2026-03-07-1430-Discovery-Title.md`
4. Both share `2026-03-07-1430` → instant match

**In session logs, use "see notes:" pattern:**

```markdown
**see notes:** `resources/touchdesigner-knowledge-logs/2026-03-07-1430-Discovery-Title.md` for complete technical details
```

---

## Platform Awareness

### Cursor-Specific Features

When the user is in Cursor:
- Offer to create `.cursor/rules/` files for preferences
- Reference `.cursor/rules/` in examples
- Explain that rules persist across all Cursor sessions

### Platform-Agnostic Core

The core system works everywhere:
- Preference logs are portable (work with Claude.ai, ChatGPT, Gemini, etc.)
- Session logs and knowledge logs are just markdown files
- Other platforms have similar systems:
  - **Claude.ai:** Project instructions
  - **ChatGPT:** Custom instructions
  - **Windsurf/Cline:** Similar to Cursor

---

## Reference Files

This skill bundles several reference files for detailed templates:

- `references/discovery-log-template.md` - Full Discovery Log structure
- `references/learning-log-template.md` - Full Learning Log structure
- `references/session-log-template.md` - Full Session Log structure
- `references/master-template.md` - Complete documentation system guide

Read these files when you need the full template structure or additional guidance.

---

## Important Notes

**Do NOT auto-create logs without user request:**
- Only create knowledge logs when user explicitly asks
- The criteria (impasse, AI wrong, etc.) describe WHAT to document, not WHEN to automatically create logs
- Always wait for user to say "document this" or similar

**Keep the user in control — with one carve-out:**
- **Screenshots are never a question.** Step 0 of Workflow 4 is not gated on asking, on log type, or on whether the image was already transcribed into the body. Extract, verify, save. "Want me to attach it?" is the wrong move.
- Ask which log type if unclear
- Ask which tool to document for
- Confirm before creating Cursor rules
- Let user review and edit logs

**Explain the "why":**
- Help users understand why they might want to document something
- Explain the benefit of different log types
- Show how the system improves collaboration over time

---

## Success Criteria

This skill succeeds when:

1. Users can start sessions with clear documentation intent
2. Knowledge logs are created quickly without thinking about structure
3. Preferences are captured in a portable, reusable way
4. Session summaries are comprehensive yet concise
5. Cross-referencing via timestamps works seamlessly
6. The knowledge base improves collaboration over time
7. Every screenshot the user posted in the chat is in the log's `attachments/` — or in the DNC note folder the log links to — without anyone having asked for it