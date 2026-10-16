# SLC improvements

The inbox for fixing and improving this skill. Bugs and ideas land here while the user is working with an agent. Review it anywhere, including on the phone in a Claude cloud session, and pick what to patch.

**How it works**
- **Add:** one line per idea, as `- [ ] [YYYY-MM-DD] what went wrong or what's wanted — seen in: <project>`. Newest at the bottom of its group.
- **Done:** tick it, then write one line in `CHANGELOG.md` and delete it here.
- **Dropped:** delete the line.
- An agent that notices an SLC problem mid-session adds it here and says so in one line. It never patches SLC unasked.

---

## Tighten and modernise
_Moved from `daily-notes/2026-09-17-1910-things-to-do-tighten-and-modernise-slc-claude-skills.md`, which has the full detail for each item._


- [ ] [2026-10-03] `TEST-SCENARIOS.md` is out of date: it still tests preference logs, COMMANDS.md and Cursor. Rewrite it for what SLC does now, or remove it. README.md and INSTALL.md need the same check before sharing (goes with the DN + SLC packaging item) — seen in: claude-skills

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
_Moved from `daily-notes/2026-09-26-1415-things-to-do-dn-and-slc-working-together-claude-skills.md`._

- [ ] [2026-09-26] Package DN + SLC together for sharing: one download, a readme saying DN to start and catch ideas, SLC for the session log

## New

## From sessions
- [ ] [2026-10-04] `list_captures.py` misses a `note.` sent while the agent is working: it is stored as `queue-operation` / `attachment.queued_command` in the jsonl, not as a user message. Found 0 when there was 1 — seen in: TD-GRADIENTS26
- [ ] [2026-10-06] For a TouchDesigner knowledge log, Workflow 2 Step 3 points at the project's `resources/touchdesigner-knowledge-logs/`, but the gotchas only read `idocs26_for_work/areas/how-to-maintain-improve-the-touchdesigner-scaffolding-companion-skill/resources/touchdesigner-knowledge-logs/`. The log first landed in `idocs26_for_work/resources/touchdesigner-knowledge-logs/` and had to be moved. Name the intake folder in SLC — seen in: TD-GRADIENTS26

## Hand-offs to other skills
- [ ] [2026-10-14] **End-of-session motion catch.** Before writing the session log, ask "did this session teach a feel or a motion rule?" (a timing, ease, spring, hold, idle, loop or transition Johno liked or called too fast). Each one goes to the **motion-design-companion** (MDC): a named feel into `library/feels.json`, a rule into `references/motion-design.md`. One line in the session log says what went there, like the gotchas reminder. Why: MDC only catches feels live (when Johno says "perfect" / "keep that"); the will-o-wisp feels (Thor catch, balloon float, Tinker Bell dart...) sat unfound in a knowledge log until he asked — seen in: TD-SKETCHES26 will-o-wisp
