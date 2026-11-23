# SLC improvements

The inbox for fixing and improving this skill. Bugs and ideas land here while the user is working with an agent. Review it anywhere, including on the phone in a Claude cloud session, and pick what to patch.

**How it works**
- **Add:** one line per idea, as `- [ ] [YYYY-MM-DD] what went wrong or what's wanted — seen in: <project>`. Newest at the bottom of its group.
- **Done:** tick it, then write one line in `CHANGELOG.md` and delete it here.
- **Dropped:** delete the line.
- An agent that notices an SLC problem mid-session adds it here and says so in one line. It never patches SLC unasked.

---

## Copy-paste reference pages sub-skill
_Moved from `daily-notes/2026-09-18-0200-things-to-do-slc-copy-paste-reference-pages-sub-skill-claude-skills.md`._

- [ ] [2026-09-18] Decide the shape: a sub-skill under SLC, or its own skill SLC hands off to
- [ ] [2026-09-18] Pin down what the page always carries: every format the destination needs (hex for Figma, RGB 0–255 for AE, CMYK + Pantone for print)
- [ ] [2026-09-18] Keep the two-file rule: a local `.html` that works offline, plus a published link
- [ ] [2026-09-18] Keep the markdown twin, which is what greps and what future sessions read
- [ ] [2026-09-18] Make it add itself to the project launcher
- [ ] [2026-09-18] Where do the values come from: does the skill own extraction from the client's guide, or just presentation?
- [ ] [2026-09-18] Does it generalise past colour (type scales, screen specs, safe areas)?

## DN and SLC together
- [ ] [2026-09-26] Package DN + SLC together for sharing: one download, a readme saying DN to start and catch ideas, SLC for the session log. Check README.md and INSTALL.md before sharing (they still describe the discovery / learning templates and project knowledge-log folders) — seen in: claude-skills

## Knowledge logs, later
- [ ] [2026-10-18] Move old project knowledge logs to the central shelves (start with the 62 in the TD-SKETCHES26 repo). Ask Johno first; never touch `.toe` files — seen in: TD-SKETCHES26 jam
- [ ] [2026-10-18] A `share:` label (personal / work / client) on each log before any work log is pushed, and the work repo `knowledge-logs-for-work-JB`, only when Johno says — seen in: TD-SKETCHES26 jam

## From sessions
- [ ] [2026-10-23] **Before the closing question, check every open to-do item against the files** (a quick "still missing" list), so a forgotten deliverable shows up before filing, not after. The Lilly floor mat was found only after the sl and dn; Johno: "how come i didnt ask u to check what else im missing" — seen in: LILLY2026
- [2026-10-26] When the session's planned job finishes in the first half hour and five hours go somewhere else, the log must say where those hours went and why, not just list what got built. The 2026-10-25 rocky log needed a "what happened" line added by hand at the end. Suggest: Workflow 4 Step 2 gathers "what the session was for vs where the time actually went" as its own question before writing.
- [ ] [2026-10-29] Take the log's stamp from the jsonl's first user message at session start, and have DNC name the worksession note with the same minute (2026-10-29 rocky: DNC said 2140, the jsonl 2139; the note was renamed at sl time).
- [ ] [2026-11-02] **The sl rewrites the project's call sheet** (`START-HERE.md`: facts in force, don't touch, open threads, about 20 lines) as part of Workflow 4, before the session log; a missing one gets made. Rimrock: 280 versions in, the agent forgot the page is tested with a mouse — seen in: TD-SKETCHES-FOR-WORK26
- [ ] [2026-11-03] **A next-chat prompt pointed at a session log that was never written.** The 376–378 rimrock chat gave a `start from:` path (…-2000-…) and its sl never ran, so the next chat started from the call sheet and Johno's notes from that chat were missing. When a prompt names a log, write the log in the same turn or say in one line that it is not there yet — seen in: TD-SKETCHES-FOR-WORK26 rimrock
- [ ] [2026-11-04] **🪙 marks what saves tokens.** In the close (sl / dn), any Start · Stop · Continue, "I'll save" or "How we both get better" line that saves tokens starts with 🪙; a pitch puts 🪙 on the cheap way. Rule saved in CLAUDE.md (prefs) — seen in: TD-SKETCHES-FOR-WORK26 rimrock
- [ ] [2026-11-05] **No next-chat prompt until the log is on disk, and the job line in plain words.** The 0320 rimrock prompt pointed at an unwritten log and said "add to the questions and the multiple answers"; the next chat read it as new CSV rows for 20 minutes when it meant a sound for the question and its answers. Second time (see 2026-11-03) — seen in: TD-SKETCHES-FOR-WORK26 rimrock Seen again 2026-11-08 (rimrock): the prompt pointed at a 1406 log that was never written; the real one was 0407.; and again 2026-11-08 1922: the 1653 log was never written (v5–v20 filled in from the page and the play log).
- [ ] [2026-11-08] **A next-chat prompt that reserves a log name takes its stamp from the jsonl's first user message, not from the start line.** The rimrock prompt said 0912 (DNC's `date` after the first reply); the chat's first message was 0911, so the log and notes were 0911 and the prompt had to be re-copied. Make the prompt after the jsonl is read, or re-copy it at the sl — seen in: TD-SKETCHES-FOR-WORK26 rimrock
- [ ] [2026-11-18] **A next-chat prompt reserved a log name, but the sl never ran, so the next chat started from a missing file** (the 1957 led-pillars console log; worked from the play log, covered in the 2035 log). The prompt step should check the log exists on disk, or point at a carry note instead. Seen before: 2026-11-03, 2026-11-05, 2026-11-08 (twice) — seen in: TD-SKETCHES-FOR-WORK26 led-pillars
- [ ] [2026-11-18] **When Johno is using the browser pane's tab, test in a new tab.** Two reloads and stills overlays landed on the tab he was tuning in (his knobs survived only because of autosave). Also: the 2233 start-from log was missing again (see the open line above) — seen in: FORD2026 smoke-gif-test
