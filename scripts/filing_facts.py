#!/usr/bin/env python3
"""Every fact filing needs from one chat, in one step (the filing card, step 1).

Prints: the start stamp, the active blocks (split on gaps over 30 min), the
active total and the span, the gaps to ask about, every note. / fleet capture,
and how many screenshots the user posted. With --out DIR it also saves those
screenshots there as 01-image.png, 02-image.jpg ... (rename them after, and
prune any that came from an @-referenced note of another project).

Reads only the jsonl. Uses list_captures.py (same folder) for what counts as
typed text and as a capture, so the two never disagree.

Usage:
  filing_facts.py                      # newest jsonl under ~/.claude/projects
  filing_facts.py <path.jsonl>
  filing_facts.py <path.jsonl> --out <log folder>/attachments
"""
import base64
import json
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from list_captures import CAPTURE, TORONTO, newest_jsonl, typed_text  # noqa: E402

GAP_MIN = 30
EXT = {"image/png": "png", "image/jpeg": "jpg", "image/gif": "gif", "image/webp": "webp"}


def images_in(entry):
    if entry.get("isMeta"):
        return []
    if entry.get("type") == "user":
        content = entry.get("message", {}).get("content")
    elif entry.get("type") == "attachment":
        att = entry.get("attachment", {})
        if att.get("type") != "queued_command":
            return []
        content = att.get("prompt")
    else:
        return []
    if not isinstance(content, list):
        return []
    out = []
    for b in content:
        src = b.get("source", {}) if b.get("type") == "image" else {}
        if src.get("type") == "base64" and src.get("data"):
            out.append((src.get("media_type", "image/png"), src["data"]))
    return out


def hm(minutes):
    h, m = divmod(int(round(minutes)), 60)
    return f"{h}hr{m:02d}min" if h else f"{m}min"


def main():
    args = [a for a in sys.argv[1:] if a != "--out"]
    out_dir = None
    if "--out" in sys.argv:
        out_dir = sys.argv[sys.argv.index("--out") + 1]
        args.remove(out_dir)
    path = args[0] if args else newest_jsonl()

    times, captures, images = [], [], []
    with open(path, encoding="utf-8") as f:
        for raw in f:
            try:
                entry = json.loads(raw)
            except json.JSONDecodeError:
                continue
            stamp = entry.get("timestamp")
            text = typed_text(entry)
            imgs = images_in(entry)
            if (text or imgs) and stamp:
                t = datetime.fromisoformat(stamp.replace("Z", "+00:00")).astimezone(TORONTO)
                times.append(t)
                for line in (text or "").splitlines():
                    if CAPTURE.match(line):
                        captures.append((t.strftime("%H%M"), " ".join(line.split()[:10])))
            images.extend(imgs)

    if not times:
        sys.exit("no typed messages found")
    times.sort()
    blocks, gaps = [[times[0], times[0]]], []
    for t in times[1:]:
        if (t - blocks[-1][1]).total_seconds() / 60 > GAP_MIN:
            gaps.append((blocks[-1][1], t))
            blocks.append([t, t])
        else:
            blocks[-1][1] = t
    active = sum((b - a).total_seconds() / 60 for a, b in blocks)
    span = (times[-1] - times[0]).total_seconds() / 60

    print(f"jsonl: {path}")
    print(f"start stamp: {times[0].strftime('%Y-%m-%d-%H%M')}")
    print("blocks: " + " · ".join(f"{a:%H%M}-{b:%H%M}" for a, b in blocks))
    print(f"time line: {times[0]:%H%M}-{times[-1]:%H%M}-{hm(active)} "
          f"(active, {len(blocks)} block{'s' if len(blocks) > 1 else ''} · {hm(span)} span)")
    for a, b in gaps:
        print(f"ask: quiet {a:%H%M}-{b:%H%M} ({hm((b - a).total_seconds() / 60)}) — away, or working off-screen?")
    print(f"captures: {len(captures)}")
    for i, (hhmm, words) in enumerate(captures, 1):
        print(f"  {i}. {hhmm}  {words}")
    print(f"screenshots: {len(images)}")
    if out_dir and images:
        os.makedirs(out_dir, exist_ok=True)
        for i, (mt, data) in enumerate(images, 1):
            p = os.path.join(out_dir, f"{i:02d}-image.{EXT.get(mt, 'png')}")
            with open(p, "wb") as fh:
                fh.write(base64.b64decode(data))
            print(f"  saved {p}")


if __name__ == "__main__":
    main()
