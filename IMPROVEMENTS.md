# SLC improvements

The inbox for fixing and improving this skill. Bugs and ideas land here while Johno is working with an agent. Review it anywhere, including on the phone in a Claude cloud session, and pick what to patch.

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

- [ ] [2026-10-03] **Streamline SL, in its own chat.** Go through the session log format with Johno: cut sections that repeat the daily note, and reshape Next Steps now that it links to the things-to-do note when DN runs. Do DN in the same pass (DNC IMPROVEMENTS.md has the twin item). The grill on how DN and SL work together was done 2026-10-03: one message, SL first, then DN — seen in: claude-skills
- [ ] [2026-09-26] Package DN + SLC together for sharing: one download, a readme saying DN to start and catch ideas, SLC for the session log

## New

## From sessions
