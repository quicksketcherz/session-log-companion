# Branched / tangent session log

Read this when one chat covered two bodies of work in two different folders, or Johno says "log this tangent". Moved out of `SKILL.md` on 2026-10-22.

**Use when:** One chat covered two genuinely different bodies of work. Rather than one log that half-belongs in each project's folder, spin off a second log scoped to the tangent and file it where that work actually lives.

**Why this exists — findability.** A log about skill maintenance sitting in COA2026's `session-logs/` is a log nobody will find when they go looking for skill maintenance. Two logs, each in the right folder, each carrying a cross-reference to the other, beat one log in the wrong place. The cross-reference is what makes the split safe: nothing gets orphaned, either log leads you to the other.

## When to suggest it (and when not to)

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

## Step 1: Identify the branch's start point

Two approaches, in order of preference:

1. **Scan the chat for the topic-shift cue.** Look back through the conversation for the message where the new scope began. Tells include: a new project name appearing, phrases like "by the way," "while we're here," "let's shift to X," "i'm noticing X," or a hard pivot from one tool/domain to another. Use the timestamp of that message (from the session jsonl) as the branch's start.
2. **If the shift point is ambiguous, ask** — one short line: *"where do you see the tangent starting? Around when we started talking about X?"* Don't guess silently.

## Step 2: Determine the branch's scope

Quickly characterize the branch:
- **Project / domain** — what is the tangent about? (often different from the original session)
- **Artifacts produced** — what got built/decided/created in the branch
- **Where does the branch log belong?** — usually the branch's project folder, NOT the original session's folder (e.g. a DNC-skill tangent spun off from a COA2026 session belongs in DNC's `session-logs/`, not COA2026's)

## Step 3: Create the branched session log

Follow Workflow 4 (Steps 0, 2-4) normally — review for "document later" items, do the session assessment, generate the log. With three differences:

1. **Timestamp:** use the branch's START time (from Step 1), not chat-open and not filing time.
2. **First line under the title:** add a `**spun off from:** <vault-relative-path-to-original-session-log>` line so the navigation thread is preserved.
3. **Scope:** the "Session Focus," "What We Accomplished," "Files Created/Modified," etc. cover ONLY the branch — don't re-include the original session's work.

## Step 4: Cross-reference BOTH logs — the link goes both ways

A one-way link only works if you already know the branch log exists. Someone opening the original log has no idea. So both logs get a pointer:

- **Branch log** → `**spun off from:** <vault-relative-path-to-original-session-log>` (added in Step 3).
- **Original log** → add a `see notes:` line pointing at the branch log, using the same convention every other log in the vault uses.

That is the **only** edit to the original. Do **not** go back and strip the branch material out of it, and do not rewrite its scope. It already records what happened honestly — it just gains one line saying where the rest of the story went.

**Why this changed (2026-09-15):** this step used to say "leave the original untouched — the branch log links back, that's enough." It isn't enough. The whole point of splitting is findability, and a link you can only follow in one direction means anyone starting from the original hits a dead end.

## Step 5: If DNC also ran in the original session, spin off a branched daily note too

If you spun off a session log, you almost certainly want a matching branched daily note. Tell DNC: "also branch the daily note from the same start point." DNC's branched-filing rule will fire (see DNC's "Branched filing" subsection).

## Example interaction

User: *(during a chat that started as COA2026 video editing, then drifted into updating the DNC skill)* "log this branch — the DNC skill maintenance part"

Agent: *Scans chat, finds the shift point around "by the way, would we do or add something in the skill that..." at 0500*

Agent: "Branch starts at 0500 when we shifted from COA2026 editing to DNC skill maintenance. Creating spinoff log scoped to the DNC promotion pass + new rule + repackage. Saving to `resources/skills-JB/daily-notes-companion/session-logs/2026-06-19-0500-DNC-Promotion-Pass.md`."

*Writes the branched log with the `**spun off from:** .../2026-06-19-0314-COA2026-Multicam-Edit-Setup.md` line at the top. Original COA2026 log stays untouched.*

## Side sessions: link both ways when the log is written

A side session (one started from another chat, like the glass-port session from rimrock) writes its own log. **At write time**, find the parent session's log and daily note (same project, same day) and add both links then: `**spun off from:**` at the top of the side log, and a `see notes:` line in the parent log. If the parent log isn't written yet, put the side log's path in the shared notes folder so the parent picks it up. *(2026-10-19, rimrock: the glass-port side log had neither link, and Johno had to ask to fold it in afterwards.)*
