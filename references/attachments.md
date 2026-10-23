# Screenshots: extracting, folder-logs, and who owns them

The rule in `SKILL.md` (Workflow 4, Step 0) is: extract every image from the chat's jsonl first, never ask. This file has the how. Moved out of `SKILL.md` on 2026-10-22.

## How to extract

**How:** find the most recently modified jsonl at `~/.claude/projects/<project-slug>/<session-uuid>.jsonl` and extract every uploaded image. **Visually verify each image belongs to this project and prune strays** — `@`-referencing another note folder during the chat embeds that folder's images into the jsonl, so the extractor picks those up too.

**Scan the jsonl again just before saving.** The user often posts one more screenshot while the log is being written, or after the ask in Step 3. Run the extractor a second time right before the save, and add anything new. Why (2026-09-30, td-project-templates-JB): the last screenshot came in after Step 0 had run and had to be copied by hand.

**Pictures sent while the agent is mid-task** sit in `type: attachment` entries (`attachment.type == "queued_command"`, in `attachment.prompt[]` as base64 images), not in user messages. Read both. *(2026-10-19, rimrock: the treetops reference was only found that way.)*

## Log folders

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

- **Knowledge logs use the same shape:** `<shelf>/YYYY-MM-DD-HHMM-Brief-Title/` (on the central shelf, Workflow 2) with the `.md` and `attachments/` inside.
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
