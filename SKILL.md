---
name: session-log-companion
description: Project session companion for documenting work sessions, creating knowledge logs when discovering or learning something, and saving preferences to CLAUDE.md. Use when user says "start a session", "create session log", "do slc", "lets do slc", "do sl", "do a session log", "summarize this session", "document this discovery", "create a knowledge log", "I want to improve how you work with me", "remember this preference", "let's continue", "continue from last session", "pick up where we left off", "what should I work on next", or any session/documentation-related request. Also trigger when user says "log this tangent", "log this branch", "make a tangent log", "make a branch log", "spinoff log", or "branched session log", or when one chat covered two projects belonging in two different folders — see references/branched-log.md before suggesting a split. Also trigger when user mentions being stuck, hitting an impasse, needing to understand concepts, or wanting to capture learnings.
---

# Session Log Companion (SLC)

Writes the **session log** at the end of a work block, and **knowledge logs** on the central shelf, so what we did and what we learned can be found again. DNC logs the time and files the daily note; SLC writes the logs.

## Before you start

- **Words:** read the index `resources/terms-and-phrases-<initials>/README.md` in the person's main vault folder (Johno: `idocs26/resources/terms-and-phrases-JB/`), then only the topic file you need; make it if missing. A word we settle goes in its topic file the same turn.
- **Replicator:** read `resources/replicator-<initials>/replicator-<initials>.md` (work: `idocs26_for_work/resources/replicator-for-work-JB/`) to find packets, templates, kits, looks and pages. "Save the pattern" adds a row; "replicate X" makes one from it.

## The rules that always hold

1. **Run the workflow, every step.** Never write a log file as a shortcut. If you notice you're about to, stop and go back to Step 1 of that workflow.
2. **The template is the spec, not an old log.** Read `references/session-log-template.md` before writing a session log. Opening a previous log to see "how it's laid out" silently drops whatever that log left out (it went wrong on 2026-08-22 and 2026-09-07).
3. **Screenshots are extracted first, never asked about** (Workflow 4, Step 0). Every log type.
4. **Knowledge logs go on the central shelf** (Workflow 2), never a project's `resources/`.
5. **Preferences go to `CLAUDE.md`** (Workflow 3). SLC writes no preference logs.
6. **Print the pre-flight line before writing a session log** (below).

### Pre-flight — emit this before writing any session log

```
PRE-FLIGHT — template: read (N sections) · knowledge logs: asked/none · screenshots: extracted/owned-by-DNC · notes: N caught / N placed
```

**In Claude Code, print it with a Bash `echo` in its own tool call,** then send the Write in the next message. A hook (`scripts/preflight_gate.py`, added by `scripts/add_preflight_hook.py`, see INSTALL.md) blocks a new `.md` in a `session-logs/` folder when no PRE-FLIGHT line is in the transcript since the last session log. A line in the same message as the Write isn't on disk yet when the hook runs, so it must be its own call. Edits to an existing log aren't checked. On claude.ai there is no hook; the line still comes first.

`notes` counts the `note.` / `fleet` lines from `list_captures.py` (Workflow 4, Step 2); `0 caught / 0 placed` is fine, leaving the field out is not. **If a field can't honestly be filled, stop and do that step.** A step you have to report on is a step you notice skipping.

---

## Workflow 1: Starting or continuing a session

"start a session", "let's continue", "pick up where we left off", "what should I work on next" → read `references/continue-session.md` and follow it. In short: ask what he wants to work on, then how much time, then read the last 5 session logs' *Decisions in force* and *Next Steps*. A "lets work on X" opener is DNC's (it logs the start).

---

## Workflow 2: Knowledge logs

A knowledge log keeps **what we learned**: the gap, what works, why. (A thing we can make again is a **pattern**, and goes in the replicator; a session often makes one of each, and they link to each other.)

### When to write one

- **Johno asks** ("document this", "log this as knowledge", "take note of this").
- **He engaged with it:** he asked a follow-up, tried it himself, or said "that makes sense". That is always a log, no judgement call. Offer it in the closing message (Workflow 4, Step 3).
- **He moved on without engaging:** your call at sl time, and only if it ties to the project or recent work. Otherwise it stays in the chat and isn't mentioned. *(2026-10-18 rimrock: side sessions and the contour lines → logs; the play_a missing file → dropped.)*
- **Not when a skill's `IMPROVEMENTS.md` line already covers it.** Check this session's new IMPROVEMENTS lines first; ask only when the knowledge is bigger than one line. *(2026-10-18: "we wrote an improvement for this … it keeps asking this.")*

### Step 1: Pick the shelf (don't ask)

**One central folder per Dropbox. The Dropbox the session log is in decides.**

| Session log in | Knowledge logs go to |
|---|---|
| personal (`Dropbox (Personal)/idocs26/`) | `idocs26/resources/knowledge-logs-JB/` |
| work (`PSAV Dropbox/John Barros/idocs26_for_work/`) | `idocs26_for_work/resources/knowledge-logs-for-work-JB/` |
| a colleague's vault | `<their main vault>/resources/knowledge-logs-<their initials>/` (make it, with the two shelves and a README) |

Inside, two shelves:
- **`tools/<tool>/`** — how an app works: `illustrator`, `after-effects`, `premiere`, `blender`, `git`...
- **`interests/<interest>/`** — how a kind of work goes: `presenter-xp`, `live-events`, `storyboarding`, `ai-agents`...

**Pick the shelf yourself and say it in one line:** "Saving to `tools/illustrator/`, since it's about how Illustrator works." Ask only when two shelves fit equally. A new `<tool>` or `<interest>` folder is fine; make it.

**TouchDesigner is the one exception:** a TD log always goes on TSC's shelf, `idocs26_for_work/areas/how-to-maintain-improve-the-touchdesigner-scaffolding-companion-skill/resources/touchdesigner-knowledge-logs/`, from any project. TSC's gotchas count (`count_waiting_gotchas.py`) reads only that folder. *(2026-10-19: 9 TD logs had piled up in a project where the count never saw them.)*

**Old logs stay where they are.** Never move a log from a project's `resources/*-knowledge-logs/` unless Johno asks.

### Step 2: Read the shelf's index

Open `<shelf>/README.md` (the shelf's table of contents; the top `README.md` lists the shelves). Note the logs on the same topic: they go on the new log's **Related:** line. **Every session writes its own new log; never append to an old one.** One file per session keeps each log small and its story whole, the way TSC's gotchas were split for the same reason. *(Replaced 2026-10-22: the 2026-10-18 jam said "add to an existing log"; Johno changed it to a new log with Related: links.)*

### Step 3: Write it

1. **Screenshots first** — Workflow 4, Step 0 applies to knowledge logs too.
2. **Stamp:** the session log's `YYYY-MM-DD-HHMM` (the session's start), so the two match.
3. **Read `references/knowledge-log-template.md`** and fill it: The Gap → Working Example → Why This Matters → Commands Used → Questions to Explore Next → Links, plus the optional *Test your understanding* block when he's learning a tool. If the file isn't in the project, read it from `~/.claude/skills/session-log-companion/references/`.
4. **The header carries `Session log:`** (the path back to this session's log) **and `Related:`** (from Step 2). Every log links back to its session log; the session log is where the client, the people and the file paths live.
5. **Save** as `<shelf>/YYYY-MM-DD-HHMM-Brief-Title.md`, or a folder of that name with the `.md` and `attachments/` inside when there are screenshots.
6. **Client names are allowed.** When the log names one, say so in one line as you write it ("this log names Lilly").

### Step 4: File it

- Add one line to `<shelf>/README.md`, under its topic: `- YYYY-MM-DD · [Title](file.md) — one line on what it holds`. A new shelf: make its README, and add the shelf to the top `README.md`.
- In the session log, link it under its Key Learning with `see notes:`.
- **GitHub:** the personal folder is the private repo `quicksketcherz/knowledge-logs-JB`; commit and push it with the sl + dn. The work folder: ask "ok to push this to GitHub?" every time (no work repo yet; some work knowledge must stay in Dropbox).

**Logs written after the session log:** same stamp, then add the `see notes:` line to the session log with "(added post-session)".

---

## Workflow 3: Preferences go to CLAUDE.md, not a log

"remember this", "make this a pref", "I want to improve how you work with me" → save it where agents read it, and say in one line where it went:

- **How he works with any agent, across his work** → his global `CLAUDE.md` (`idocs26/resources/my-claude-preferences/CLAUDE.md`, then commit and push that repo).
- **One project only** → that project's `CLAUDE.md` or memory.
- **How one skill works** → that skill's `IMPROVEMENTS.md`.
- **How he writes daily notes** → DNC's `references/learned-patterns*.md`.

The global `CLAUDE.md` has the same rule under *Where my preferences get saved*; it wins if the two differ.

---

## Workflow 4: Ending a session

### Step 0: Extract every image from the session jsonl FIRST

Before anything else. Every screenshot Johno posted is pulled out, checked that it belongs to this project (an `@`-referenced note folder drags its images in too; prune them), and saved into the log's `attachments/`, which makes the log a folder. Never ask. Never skip because the image was already described. **Run the extractor again just before saving**: he often posts one more. How, and the folder shape: `references/attachments.md`.

**The one exception: DNC owns the images for this block** when it files a *folder* note for it (the normal case). Then the log links to the daily note's `attachments/` instead of copying. One copy, never two, never zero.

### Step 1: Prepare

1. **Read `references/session-log-template.md` now**, before gathering, so the required sections are in mind while you look.
2. Find this chat's jsonl (`~/.claude/projects/<project-slug>/<session-uuid>.jsonl`). Its **first user message's timestamp** (in Toronto time) is the session's start and the log's stamp, never filing time and never a guess.
3. Make `session-logs/` if it's missing.

### Step 2: Review the whole chat before writing

**Go through the entire chat first.** Look for:
- "document this later", "log this as knowledge", "take note of this", "note it", "remind me to document"
- "update the guide", "fix the guide", "the guide says X but Y works", "add to the project docs"
- screenshots or files he said to document, or info he asked to pull from another chat
- **every `note.` and `fleet` line.** Don't trust memory; run:
  ```bash
  python3 ~/.claude/skills/session-log-companion/scripts/list_captures.py <this chat's jsonl>
  ```
  It reads messages sent while the agent was working too (stored as `queued_command` attachments). Each capture lands somewhere (a knowledge log, an `IMPROVEMENTS.md`, memory, a things-to-do note, this log) and the log's **Notes captured** section lists where.

Also gather, for the closing message:
- **Knowledge logs** by the rules in Workflow 2 → *When to write one*.
- **Feels:** did this session teach a feel or a motion rule (a timing, ease, spring, hold, idle, loop or transition he liked, or called too fast)? Each one goes to MDC: a named feel into `library/feels.json`, a rule into `references/motion-design.md`. MDC only catches feels live, so the will-o-wisp feels sat unfound in a knowledge log until he asked (2026-10-14).
- **Patterns:** anything built this session that another sketch or project could use (an ops panel, a test dummy pose, a template, a page), with where it would live and which kit packets it links to. Each becomes a replicator row on his yes.
- **Play logs:** for each thing worked on (a construct, a packet, a sketch, a model, a comp, a cue sheet, a draft), its `play-log-<thing>.md` (in a project or sketch: its `resources/`; a construct: its own folder) has this session's tries: tried → kept / dropped → why, newest on top. Missing → make it from `references/play-log-template.md`. A line that holds beyond that one thing is offered for the skill's gotchas or `IMPROVEMENTS.md`.
- **Improvements:** what to change in how we work, each with its home (global `CLAUDE.md`, a project `CLAUDE.md`, a skill's conventions, or a skill's `IMPROVEMENTS.md`).

### Step 3: The closing ask — two turns, then write

**Turn 1, before writing anything: one closing question that fits the session**, its kind in two words:
- a build that landed → "what surprised you tonight?"
- stuck → "what would have made it easier?"
- ideas → "which one do you carry?"
- playtest → "where would a friend get lost?"
- no why yet → "why would someone walk up, and what do they leave with?"

"Anything else before I file?" is the fallback. Either way, work often keeps going after the sl; asking first saves patching the log three times (2026-10-17). His answer can be a whole reflection: it goes into the log.

**Turn 2: one message with everything to approve** (his global `CLAUDE.md`, *End of every session*, has the shape: We made · Start · Stop · Continue · I'll save · Next time · I'm curious). Under **I'll save**, one line each, as your picks: each knowledge log and its shelf, each improvement and its home with the file's size, feels for MDC, patterns for the replicator, play-log lines, and (TD) the alert level with the scale shown. **One yes saves all** ("yoq" works). If he jams past it, go with the picks and say so in one line.

The session log's own folder goes on a 🟢 line: "🟢 The session log goes in `td-project-templates-JB/session-logs/`."

### Step 4: Write the session log

1. **Echo the PRE-FLIGHT line** (Bash, its own call).
2. **Name it.** When DNC gave a worksession title (alone in a fence: `YYYY-MM-DD-HHMM-worksession-short-description-TERM`), use that exact string as the filename (`<title>.md` or `<title>/`) and the heading (`# Session: <title>`), and add one row to Files Created/Modified: `` `<title>` `` | — | worksession title. Otherwise `YYYY-MM-DD-HHMM-Session-Title`. The stamp is the session's start (Step 1). **When a next-chat prompt reserves a log name, take its stamp from the jsonl's first user message too**, never a round guess (0300 vs the real 0308 left the log and the note on different stamps, 2026-10-19).
3. **Fill every section of the template.** Link knowledge logs under their Key Learning with `see notes:`. List only project files in Files Created/Modified. Add *Guides to Update Later* when there are some.
4. **Save** to `session-logs/<name>.md`, or `session-logs/<name>/` with `attachments/` when Step 0 found screenshots.
5. **A side session's log** links to the main session's log both ways at write time: `references/branched-log.md` → *Side sessions*.

**SL and DN together** ("sl and dn"): write the session log first, run DNC to file, then come back and fill two links: `see notes:` to the daily note, and **Next Steps** as one line pointing at the things-to-do note DNC filed (`→ daily-notes/…-things-to-do-….md`). That note is the only live list. Leave out *How the Session Went*: the daily note's `**how the session went:**` has it. Without DN, Next Steps stays a list and *How the Session Went* stays.

**Required sections:**
- **How the Session Went** (without DN): five short lines — set out to · what happened · why the gap · worked well · try next time (one change in how we work together, not a task). After Notes captured, before Decisions in force.
- **Decisions in force**: just above Next Steps. The rules that still hold next time ("720 × 1280", "the build moves to `candle-flame/`"), one line each. "None new" if nothing was decided. Workflow 1 reads it, so the next chat doesn't re-argue it.
- **Patterns**: what was saved to the replicator this session, or offered, one line each with its path. Leave it out when none.

**Keep it concise:** "see notes:" instead of copying a knowledge log in; the why behind decisions, not only the what; the texture of how the work went. No header block (date, model, platform), no Applications Used table, no Knowledge Logs table, no "Session ended" line. Code in a log always says where it's used, what it does, and how it connects.

### Step 5: Update guides and docs

If the project keeps guides (setup, quick reference, troubleshooting), apply what this session proved: version differences, corrections, steps that needed clarifying. Update only the relevant sections, and list them under *Guides Updated*. Guides should match what really works, not the first research.

### Step 6: Confirm

Say where the session log went, the knowledge logs (with links and shelves), the guides updated, and the push. If a knowledge log came up that wasn't written and it fits *When to write one*, offer it now in one line.

---

## Branched / tangent logs

One chat covered two bodies of work that belong in two different folders, or he says "log this tangent" / "log this branch" / "spinoff log" → `references/branched-log.md`. Suggest a split only when all four hold: a different project or area, its own artifacts, it could stand alone, and the two logs would land in different folders. Ask once, naming both halves.

---

## Cross-referencing

The shared `YYYY-MM-DD-HHMM` stamp matches a session log to its knowledge logs and daily note:

```markdown
**see notes:** `idocs26/resources/knowledge-logs-JB/tools/illustrator/2026-10-22-1219-Laying-Out-Client-Print-Panels-In-Illustrator.md` — one section per print, with the fixes
```

The knowledge log points back with its `Session log:` line.

## Reference files

- `references/session-log-template.md` — the session log's sections (the spec)
- `references/knowledge-log-template.md` — the one knowledge-log shape
- `references/play-log-template.md` — the play log next to each thing we make
- `references/attachments.md` — extracting screenshots, folder-logs, who owns the images (DNC or SLC)
- `references/continue-session.md` — starting and continuing a session
- `references/branched-log.md` — branched, tangent and side-session logs
- `scripts/list_captures.py` — every `note.` / `fleet` line in a chat (keep it the same as DNC's copy)
- `scripts/preflight_gate.py`, `scripts/add_preflight_hook.py` — the pre-flight hook

## Works with the other skills

- **DNC** (daily-notes-companion) — logs start times, shows open things-to-do, files the daily note. The only one that records time.
- **SLC** — the session log and knowledge logs at the end.
- **TSC** — builds in TouchDesigner; its knowledge logs go on its own shelf.
- **LC** — lays out in After Effects, Illustrator, Figma and decks.
- **MDC** — gets the feels caught at sl time.
- **SSC** (script-supervisor-companion) — checks every skill and the replicator, and runs the kaizens.
- **Review Companion** — tallies the hours DNC logged.

## Improving this skill — `IMPROVEMENTS.md`

When something about **how SLC works** goes wrong or could be better, add one line to `IMPROVEMENTS.md` in the format written there, and say so in one line. Don't patch SLC unasked; it gets a kaizen once its list passes about 10 open items. History and the why behind each rule live in `CHANGELOG.md`.
