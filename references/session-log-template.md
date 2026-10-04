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

Every `note.` / `fleet` line Johno typed this session (from `list_captures.py`), and where it went.
Leave this section out when there were none.

| Time | Note (first words) | Went to |
|------|--------------------|---------|
| HHMM | [first words] | [knowledge log / IMPROVEMENTS.md / memory / things-to-do / this log] |

---

## Honest Self-Assessment

**Required when SL runs without DN.** When DN runs in the same message, leave this section out:
it goes in the daily note as `**how the session went:**` instead.

What didn't work, what's untested, what's parked, and anything either party may be pattern-matching
ahead of the evidence. 2-4 honest bullets or a short paragraph. The purpose is to stop future-you
reading this log and assuming everything was settled when it wasn't.

If the session genuinely had no caveats, write "No significant caveats — everything tested was
validated by results" rather than deleting the heading.

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

---

## Session Insight

**Required when SL runs without DN — then it is the final section. One sentence, not a list, not a paragraph.**
When DN runs in the same message, leave it out: the daily note's `**how the session went:**` covers it in its "try next time" line.

What changed about how the user works, or what design principle the session surfaced. The
one-sentence limit is the design: it forces a *meta* observation instead of a recap. If it can't be
condensed to one sentence, the insight isn't ready yet.
```

---

## Session Log Best Practices

**Read this file, not a previous log.** A finished session log is an *example*; this file is the
*spec*. Working out the shape by opening the last log silently drops whatever sections that log
happened to omit — which is exactly how the Honest Self-Assessment and Session Insight sections went
missing from logs on 2026-08-22 and 2026-09-07.

**Keep it concise:** When knowledge logs exist, use brief summaries with "see notes:" references instead of duplicating content.

**Format:**
```markdown
**see notes:** `resources/[tool]-knowledge-logs/YYYY-MM-DD-HHMM-Title.md` for [what's documented there]
```

**Cross-referencing:** Use matching timestamps between session logs and knowledge logs for instant cross-referencing.
