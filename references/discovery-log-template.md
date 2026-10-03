# Discovery Log Template

**Use when:** AI got it wrong, hit impasse (>15 min), found non-obvious behavior

**Structure:** Gap → Working Example → Why → Questions to Explore

---

```markdown
# [Feature/Operator/Node Name]

**Date:** YYYY-MM-DD  
**Time:** HHMM  
**Application:** [Tool name + version]  
**Discovered in:** [Project name]  
**Type:** Discovery Log

---

## The Gap

**Trying to do:** [Goal]

**AI suggested:** `[wrong parameter/approach]`

**Where it broke:** [Specific error/failure]

**What works:** `[correct parameter/approach]`

---

## Working Example

```
Setup: Input → Step1 (Setting: Value) → Step2 → Output
```

**Key settings:**
- `param1`: `value` — [Why this matters]
- `param2`: `value` — [Why this matters]

**Expected result:** [What you should see]

---

## Why This Matters

**Why AI gets it wrong:** [Brief reason - outdated docs, version differences, etc.]

**Tool principle:** [What this reveals about how the tool works]

---

## Commands Used

**Commands that helped solve this:**
- `[command]` - [What it did / Why it was useful]


---

## Questions to Explore Next

1. [Experiment or variation]
2. [Related scenario]
3. [Edge case to test]

---

## Links

**Official docs:** [Link]  
**Version tested:** [Specific version]
```
