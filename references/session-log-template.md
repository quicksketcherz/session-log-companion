# Session Log Template

**Use for:** Recording what happened in each work session

**Naming:** `YYYY-MM-DD-HHMM-Session-Title.md`, or the exact worksession title from DNC when this chat has one (`YYYY-MM-DD-HHMM-worksession-short-description-TERM.md`). Then the heading is `# Session: <that title>` and Files Created/Modified gets a row: `` `<title>` `` | — | worksession title.

**Get timestamp:** `date "+%Y-%m-%d %H%M"`

---

```markdown
# Session: [Session Title]

---

## Session Focus

[One paragraph describing what this session was about]

---

## What We Accomplished

### 1. [Task Name] ✅

**Summary:** [1-2 sentence overview of what was accomplished]

**Problem:** [what was in the way, or why this was needed — one line. Leave out when there was none]

**see notes:** [Link to knowledge log/resource/artifact if applicable - describe what's there]

---

**Note:** Keep tasks concise when knowledge logs exist. Use "see notes:" to reference detailed documentation. Only include full details for tasks without separate documentation.

---

## Key Learnings

### [Learning Topic]

**Challenge:** [Issue addressed]  
**Solution:** [How it was solved]  
**see notes:** `resources/[tool]-knowledge-logs/YYYY-MM-DD-HHMM-Title.md` (when a knowledge log covers it)

This is where knowledge logs are linked. There is no separate Knowledge Logs table.

**Note for AI:** Only create knowledge logs when user explicitly asks to document. The criteria below describe WHAT to document when asked, not when to automatically create logs:
- **Discovery Log:** Hit impasse, AI wrong, revealed tool principle
- **Learning Log:** Significant Q&A session, understanding concepts, filling knowledge gaps

When user requests documentation, ask which tool to document for, determine log type, then create in appropriate `[tool]-knowledge-logs` folder.

---

## Files Created/Modified

| File | Application | Purpose |
|------|-------------|---------|
| `path/to/file` | [Tool] | [Description] |

**Note:** Only list project files that were part of the actual work (code, assets, configs, etc.). Do NOT list the session log itself or knowledge logs - that's redundant.

---

## Guides Updated

| Guide | Changes Made | Reason |
|-------|--------------|--------|
| `path/to/guide.md` | [Brief description] | [Version difference / Correction / Clarification] |

**Note:** Only include this section if implementation guides or reference documentation were updated during the session.

---

## Notes captured

Every `note.` / `fleet` line the user typed this session (from `list_captures.py`), and where it went.
Leave this section out when there were none.

| Time | Note (first words) | Went to |
|------|--------------------|---------|
| HHMM | [first words] | [knowledge log / IMPROVEMENTS.md / memory / things-to-do / this log] |

---

## How the Session Went

**Required when SL runs without DN.** When DN runs in the same message, leave this section out:
the daily note has the same part, `**how the session went:**`.

The agent checks its own work, in five short lines (the shape of an after-action review):

- **set out to:** [the aim]
- **what happened:** [what got done, what didn't]
- **why the gap:** [the cause, often something the agent did]
- **worked well:** [a way of working worth keeping]
- **try next time:** [one change in how the user and agent work together — not a task]

If nothing went wrong, say so under "why the gap" rather than leave the section out.

---

## Decisions in force

**Required.** Rules settled this session (or earlier) that still hold next time. One line each.
The next chat reads these before Next Steps, so it doesn't re-argue them. If nothing was
decided, write "None new".

- [Decision] — [why, in a few words]

---

## Next Steps

- [ ] [Next task]

<!-- When DN ran in the same message, replace the list with one line:
→ daily-notes/YYYY-MM-DD-HHMM-things-to-do-<desc>-<TERM>.md
That note is the live list. -->

**see notes:** daily note → `daily-notes/YYYY-MM-DD-HHMM-worksession-<desc>-<TERM>.md` (when DN ran)

---

## Notes & Observations

[Additional notes, design decisions]
```

---

## Session Log Best Practices

**Read this file, not a previous log.** A finished session log is an *example*; this file is the
*spec*. Working out the shape by opening the last log silently drops whatever sections that log
happened to omit — which is exactly how the self-assessment and insight sections went
missing from logs on 2026-08-22 and 2026-09-07.

**Keep it concise:** When knowledge logs exist, use brief summaries with "see notes:" references instead of duplicating content.

**Format:**
```markdown
**see notes:** `resources/[tool]-knowledge-logs/YYYY-MM-DD-HHMM-Title.md` for [what's documented there]
```

**Cross-referencing:** Use matching timestamps between session logs and knowledge logs for instant cross-referencing.
