---
layout: page
title: Session Log
permalink: /log/
---

This page is updated at the end of each working session. It records what was
built, what decisions were made, and what the next steps are — so the project
is always recoverable and progress is transparent.

---

## Session 1 — 2026-03-21

**Who:** Parent + Claude
**Status at start:** No repository
**Status at end:** Repository created, site live, ready for interview

### What was built

- **GitHub repository** (`rneild/uni-search`) created and initialised
- **Jekyll site** with the `minima` theme, configured for GitHub Pages
- **University collection** — one markdown file per university under `_universities/`, with a YAML front-matter schema covering:
  - Identity fields (name, country, city, website)
  - Course-specific fields (course name, entry requirements, duration)
  - Financial fields (annual fees, scholarship notes)
  - Scoring fields (weighted criteria scores, overall score)
  - Status tracking (`researching` → `shortlisted` → `applying` → `offer` → `declined` / `accepted`)
- **Scoring model** — weights defined in `_data/criteria.yml`; overall score computed from weighted average of per-criterion scores (1–10 scale)
- **Jekyll templates** — index page with sortable summary table; individual university pages; this log page
- **Interview plan** (`docs/interview-plan.md`) — structured guide for the student interview covering subject, environment, career, finance, wellbeing, and application logistics
- **Status file** (`docs/status.md`) — single file to read at session start; records current phase, what's done, what's pending, and what to do next
- **Project log** (`docs/project.md`) — mission, principles, approach, decisions, lessons learned, and session history
- **Setup actions tracker** (`docs/setup-actions.md`) — checklist of one-off setup steps (API key, Discover Uni download, Pages, `.env`)

### Setup actions completed this session

| Action | Notes |
|--------|-------|
| GitHub Pages enabled | Live at <https://rneild.github.io/uni-search> |
| College Scorecard API key | Key obtained and stored in `.env` (gitignored) |
| `.env` file created | Ready for use by future data-fetch scripts |

### Key decisions

| Decision | Rationale |
|----------|-----------|
| Jekyll + GitHub Pages | Native support, YAML data files, no build complexity |
| One markdown file per university | Self-contained, human-readable, easy to edit |
| Weighted average scoring | Transparent, adjustable, avoids black-box ranking |
| Interview leads with existing shortlist | Her choices reveal implicit preferences |
| `docs/` excluded from Jekyll build | Reference docs shouldn't become site pages |
| Session log published to site | Progress visible and recoverable from anywhere |

### Not yet done

- **Student interview** — the core profiling session has not happened yet.
  Nothing in `_data/profile.yml` or `_data/criteria.yml` has been filled in.
  All university files are empty templates.
- **Discover Uni download** — UK data source, useful once UK universities confirmed
- **College Scorecard auto-population script** — possible future time-saver;
  needs API key wired in first

### Next session should start with

1. Read `docs/status.md` for current phase and immediate next step
2. Begin the student interview using `docs/interview-plan.md` as a guide
3. After interview: populate `_data/profile.yml` and `_data/criteria.yml`,
   then start adding universities one by one

---
