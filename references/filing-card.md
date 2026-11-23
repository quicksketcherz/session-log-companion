# The filing card: sl and dn in about 4 steps (facts · knowledge logs · session log · daily note)

Like the camera report at wrap: one short sheet, not the whole binder. Read this card **instead of** DNC's `filing.md` and `learned-patterns.md` and SLC's template. Open those only for a rare case (bottom). Made 2026-11-22: a 10-minute kaizen's filing read about 70k of rules to write two short files.

**What it's for:** later, Johno asks "what did we do on X?" The agent greps the daily notes' `what we did` lines (one per session, the index), opens only that session log, then only the knowledge logs it links to. So the session log holds the story, and the daily note is a 5-line index card that points to it.

## 1. One step: the facts

```bash
python3 ~/.claude/skills/session-log-companion/scripts/filing_facts.py <this chat's jsonl> --out <log folder>/attachments
```
It gives the start stamp, the time line (active blocks, gaps over 30 min to ask about), every `note.` / `fleet` capture, and saves the screenshots. Leave out `--out` when it says `screenshots: 0` on a first run without it. Rename saved images `NN-short-descriptor-TERM.ext`; delete any from another project. In the same message: `TZ="America/Toronto" date`, and `cat` the things-to-do note and call sheet (`START-HERE.md`) you'll touch.

## 1b. Knowledge logs: never skip this step

SLC is built to catch what we learned, so every filing (and every update to a session log already filed) checks for knowledge logs **before** the session log is written. *(2026-11-23, MANULIFE2026: the card left this out from 11-22, and sessions went by with none; Johno: "the session companion is built for to anticipate and create knowledge logs … make this not happen or get missed".)*

- Go through the session for each **Challenge → Solution** worth keeping: something broke and we found why, a tool did something we didn't expect, a way of working that will come up again.
- Use SKILL.md → Workflow 2 → *When to write one*: Johno engaged with it → always a log; he moved on → your call, if it ties to the work.
- **Write them, don't only offer them:** each one on its shelf (Workflow 2, Steps 1–4: the shelf's README first, the template, the README line), stamped with the session's start. A one-line `IMPROVEMENTS.md` entry that covers it is enough on its own.
- None worth it → say why in a few words on the PRE-FLIGHT line (`knowledge logs: none · only layout tweaks`). A bare `none` is not allowed.
- Updating a session log after filing (more work in the same chat) → run this step again for the new part.
- Work shelf → ask "ok to push?" in the close.

## 2. The session log (one write)

Print the PRE-FLIGHT line first (Bash echo, its own call; the hook needs it):
`PRE-FLIGHT — template: filing card · knowledge logs: written N (<titles>) / none · <why> · screenshots: extracted/none · notes: N caught / N placed`

Name: the worksession title `YYYY-MM-DD-HHMM-worksession-<words>-<TERM>` (start stamp from step 1). Goes in the project's `session-logs/` (a skill: `skills-JB/session-logs/`); a folder with `attachments/` when there are screenshots. Sections, short:
- `# Session: <title>`
- **Session Focus**: one paragraph.
- **What We Accomplished**: one `###` per job with **Summary**, **Problem** (when there was one) and **see notes:** links.
- **Key Learnings**: Challenge / Solution / see notes (the knowledge log from step 1b; every log written gets its `see notes:` here).
- **Files Created/Modified**: a table, project files only; first row the title.
- **Notes captured**: only when step 1 found any: time, first words, where it went.
- **How the Session Went**: set out to · what happened · why the gap · worked well · try next time.
- **Decisions in force**: one line each, or "None new".
- **Next Steps**: `→ daily-notes/<things-to-do note>`, or a short list when there's none.
- **see notes:** the daily note.

## 3. The daily note (5 lines) + the rest, one message

`daily-notes/<same title>.md`:
```
YYYY-MM-DD-HHMM | worksession  
  time: <the time line from step 1>  
  areas/projects: <TERM>[, <TERM>]  

---

**what we did:** <one or two lines: the words he'd search for later — the project, the thing built, the name he used>

**session log:** `<vault-relative path to the session log>`
```
Add `**see next:** \`<things-to-do note>\`` only when one was made or added to. Nothing else: decisions, challenges and how it went live in the session log.

In the same message: tick or add the things-to-do items (`✅ YYYY-MM-DD`, update `status:`, add a `see notes:` line to this worksession), rewrite the call sheet's lines, write any knowledge log (SLC Workflow 2), then commit and push the repos touched.

## Skip at filing
The expiry check, the after-filing colleague recap, the breakdown list, re-reading old logs for their layout. Do them only when Johno asks.

## Rare cases: open the long guide
- A tangent or a side chat → `daily-notes-companion/references/filing.md` → *Branched filing* / *Side chats*.
- claude.ai (no disk) → `filing.md` → the artifact-then-zip steps.
- Meetings, fleeting, ideas, references (not a worksession) → `daily-notes-companion/references/note-types.md`, words verbatim.
- A storyboarding phase or work away from the keyboard → `filing.md` → *Time tracking*.
- A long chat (well over 100k) → hand steps 2–3 to a fresh helper with a brief (SLC Workflow 4 → *Keep filing cheap*).

## 4. Close in two lines

**I'll save:** each knowledge log written (title and shelf), each improvement and its home with the file's size, one yes saves all. **Next time:** the next chat's first move. Nothing else (global CLAUDE.md, 2026-11-22).
