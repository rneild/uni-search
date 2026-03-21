# CLAUDE.md — University Search Project

This file is read automatically at session start. It tells you what this
project is, what to do when you arrive, and what the rules are.

---

## What This Project Is

A structured university search tool helping a student choose where to apply
for undergraduate study (USA/Canada and UK). The Jekyll site at
https://rneild.github.io/uni-search (live after merging to main) displays
scored, compared university profiles. Everything is stored in this repo so
any session is fully recoverable.

---

## Session Start Protocol

**Always do this first, every session:**

1. Read `docs/status.md` — current phase, what's done, what's pending
2. Read `docs/project.md` — decisions made, lessons learned, open questions
3. If a university interview was completed, also read `_data/profile.yml`

Do not make any changes until you've read status.md. It tells you exactly
where things were left off.

---

## Session End Protocol

**Always do this before ending a session or after any substantial update:**

1. Update `docs/status.md` — change the last-updated date and current status
2. Append a new entry to `log.md` under a `## Session N — YYYY-MM-DD` heading
3. Commit all changes with a clear message
4. Push to the current working branch (`claude/university-search-database-fbbxc`)

The branch is merged to main periodically by the parent — you don't need to
handle that. Just push to the feature branch.

---

## Key File Locations

| File | Purpose |
|------|---------|
| `docs/status.md` | Current phase and immediate next steps — read first |
| `docs/project.md` | Mission, decisions, lessons, session history |
| `docs/interview-plan.md` | Script for the student profiling interview |
| `docs/setup-actions.md` | One-off setup checklist |
| `_data/profile.yml` | Student profile (populated after interview) |
| `_data/criteria.yml` | Scoring criteria and weights |
| `_universities/*.md` | One file per university |
| `log.md` | Published session log (Jekyll page at /log/) |
| `scripts/fetch_scorecard.py` | Fetches US university data from College Scorecard API |
| `scripts/fetch_all.py` | Batch fetcher — reads `scripts/universities.yml` |
| `.env` | API key (gitignored, local only) |

---

## Adding a University

**US university:**
```bash
python3 scripts/fetch_scorecard.py "University Name"
# optionally: --slug custom-slug
```
Then fill in manually: rankings, financial aid for internationals, course
URLs, application deadlines, scores.

**UK or Canada university:**
Copy `_universities/example-university.md` to a new file, rename it using
the slug convention (see below), and fill in all fields manually.

**Slug convention:** lowercase, hyphens, no punctuation.
Examples: `mit.md`, `university-of-oxford.md`, `mcgill-university.md`

---

## Scoring Rules

- Scores are **1–10** per criterion (not 0–10; 0 means "not yet scored")
- Higher is always better (for cost and entry requirements: higher score = more affordable / more achievable)
- `weighted_score` in the front matter is left `null` — the Jekyll template computes it
- **Do not change criteria weights without explicit approval from the parent/applicant.** Weights are set during the interview and reflect her actual priorities.

---

## Status Values

University files use these status values (in rough lifecycle order):

`researching` → `shortlisted` → `applying` → `applied` → `offer` → `accepted`

Also valid: `rejected`, `withdrawn`

---

## Committing

- Commit after every meaningful unit of work (one university added, interview completed, criteria updated, etc.)
- Commit messages should say what changed and why, not just what files were touched
- Always push to `claude/university-search-database-fbbxc` — never to main directly

---

## Data Sources

| Source | Used for | Access |
|--------|---------|--------|
| College Scorecard API | US university stats | API key in `.env` |
| Discover Uni / HESA | UK outcomes data | Download from discoveruni.gov.uk |
| QS World Rankings | Global rankings | Web search per university |
| Times Higher Education | Global rankings | Web search per university |
| US News | US national rankings | Web search per university |
| Guardian University Guide | UK rankings | Web search per university |
| Complete University Guide | UK rankings | Web search per university |
| UCAS | UK application requirements | ucas.com per course |
| Common App / Coalition | US application systems | university websites |

---

## Rules

1. **Her priorities drive everything.** Don't impose conventional wisdom about prestige.
2. **Don't change weights** in `_data/criteria.yml` without being explicitly asked.
3. **Flag uncertainty.** If a data point is estimated or from a secondary source, note it in `open_questions`.
4. **Read before writing.** Always read the relevant files before making changes.
5. **Commit often.** An interrupted session should lose no more than one exchange of work.
6. **Insights require her confirmation.** Before adding anything to `_data/insights.yml`, share the proposed wording with the applicant and get her agreement. Refine it until she's happy, then set `confirmed: true` and commit. Never commit an insight she hasn't signed off on.

---

## Adding an Insight

When a conclusion, realisation, or meaningful quote emerges during conversation:

1. **Check for conflicts first.** Read `_data/insights.yml` and ask: does this new insight
   sit comfortably alongside what's already there, or does it tension with something?
   - If it conflicts: surface the tension explicitly — *"This seems to sit in tension with
     what you said earlier about X. Has your thinking changed, or is there a nuance we're
     missing?"* — then resolve it before writing anything new.
   - If it refines or supersedes an existing insight: update the old one rather than
     leaving two contradictory entries in the file.
2. Draft the insight — keep it in her voice where it came from something she said
3. Show it to her: *"I'd like to record this — does this capture it accurately?"*
4. Refine based on her feedback until she's satisfied
5. Add to `_data/insights.yml` with `confirmed: true`

Structure of each entry:
```yaml
- date: "YYYY-MM-DD"
  category: priorities        # priorities | self-knowledge | universities | process | finance
  text: "The insight in plain language."
  quote: ""                   # her exact words, if applicable — leave blank otherwise
  source: applicant           # applicant | research | conversation | parent
  tags: []                    # optional, e.g. [location, culture]
  confirmed: true
```

## Maintaining Insight Accuracy

Insights are a living record, not an archive. At any point in the process:

- **When something new is discovered**, re-read the relevant insights and ask whether
  they still hold. If research on a university reveals something that challenges a
  stated priority, name it.
- **When she changes her mind**, don't delete the old insight — update it and add a note
  explaining what changed and why. This preserves the journey.
- **When two insights conflict**, don't let both stand silently. Resolve the tension
  with her and update accordingly.
- **When an insight is refined**, edit the `text` in place and update the `date` to
  reflect when it was last confirmed. Keep the original `quote` unchanged if there is one.

The goal is a set of insights that are *accurate at the end of the process* — not a
chronological log of every passing thought.
