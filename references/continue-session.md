# Starting and continuing a session

Read this when Johno says "start a session", "let's continue", "pick up where we left off" or "what should I work on next". Moved out of `SKILL.md` on 2026-10-22 to keep it under 500 lines.

When he opens with "lets work on X", DNC runs first (it logs the start). This file is for the SLC-only openers.

## Starting a session

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

## Continuing a session

When the user says "let's continue", "pick up where we left off", "what should I work on next", or similar:

### Step 1: Ask Intention

Ask: "What do you want to work on?"

The user may already know exactly what they want to do (from a session hours ago, or an idea they had offline). Let them state it first — don't dump a list of options before they've had a chance to think.

### Step 2: Ask Time Available

Ask: "How much time do you have?"

This scopes what's realistic. A 10-minute session is different from an hour — don't suggest deep refactoring work for a quick session.

### Step 3: Scan Recent Session Logs

Read the last 5 session logs, newest first by filename. Look in the project's own `session-logs/` **and** in every `session-logs/` one folder down (a project like TD-SKETCHES26 keeps one per sketch: `ghost/`, `spider-web/`, `candle-flame/`). Pool them, then take the newest 5:

```bash
find session-logs */session-logs -maxdepth 1 -name "20[0-9][0-9]-*" 2>/dev/null \
  | awk -F/ '{print $NF "\t" $0}' | sort -r | head -5 | cut -f2
```

From each, take two sections: **Decisions in force** and **Next Steps**. Show the decisions first. They are the rules still holding, and the next steps only make sense inside them. Older logs have no Decisions section; skip it there.

When Next Steps is a link to a `daily-notes/…-things-to-do-…` note, read that note and show only its unticked items. If the link no longer resolves because the note was archived into `daily-notes/zz-archives/`, it's done. Skip it.

**If user stated a clear intention** → Match their intention against the collected Next Steps. Surface any relevant items and note which session they came from. This helps the user see connections they might have forgotten ("Oh right, that's related to what I was doing last week").

**If user draws a blank** → Present the Next Steps from recent sessions as a menu of options, grouped by session. Let the user pick what feels right.

### Step 4: Scope to Time

Based on the time available, help the user pick a realistic slice:
- **10 min** → one small, contained task (a single next step item, a quick note, a review)
- **20-30 min** → one substantial task or 2-3 small ones
- **1+ hour** → a full work block, potentially spanning multiple next steps

Don't over-plan — just confirm the focus and begin.

### Step 5: Begin Work

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
