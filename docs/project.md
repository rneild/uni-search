# Project Log — University Search

This is a living document. It records the mission, methodology, decisions made,
things tried, lessons learned, and ideas for improvement. Claude should read and
update this file as the project evolves — before making significant decisions and
after anything meaningful is learned.

---

## Mission

Help a student make a well-informed, confident choice about which undergraduate
university to apply to and ultimately attend — across USA/Canada and UK —
by combining structured personal profiling, systematic research, and a
transparent scoring model that reflects what actually matters to *her*.

The goal is not to produce a ranked list from generic criteria. It is to build
a personalised view that makes the trade-offs visible, so the final decision
is genuinely hers and genuinely informed.

---

## Guiding Principles

1. **Her priorities drive everything.** Weights, criteria, and shortlists are
   derived from what she values — not from conventional wisdom about prestige.

2. **Transparency over magic.** Scoring is explicit and adjustable. Every score
   can be challenged, and the weighting can be changed at any point.

3. **Uncertainty is fine.** "I don't know yet" is a valid answer that shapes
   the research agenda rather than blocking progress.

4. **Interrupted process is normal.** Everything is committed to the repo so
   no session needs to start from scratch. Status and context are always
   recoverable.

5. **Data quality matters.** Where possible, use official sources (College
   Scorecard for US, Discover Uni for UK) rather than secondary summaries.
   Flag when data is estimated or uncertain.

---

## Approach

### Phase structure
The process runs in four broad stages:

1. **Profile** — interview to establish academic background, subject interests,
   preferences, and financial picture. Stored in `_data/profile.yml`.

2. **Criteria calibration** — translate preferences into weighted scoring
   criteria. Stored in `_data/criteria.yml`. Weights are revisited after
   research reveals new trade-offs.

3. **Research** — for each university, create a fully populated file in
   `_universities/`. Data sourced from College Scorecard API (US), Discover
   Uni (UK), university websites, and web research for rankings.

4. **Compare & decide** — the Jekyll site renders scores, tables, and
   individual university pages. Used as a reference throughout the application
   process. Status fields (`researching` → `shortlisted` → `applying` etc.)
   track live progress.

### Interview technique
- Conversational first, structured when helpful
- Mix of open questions, choice UI (2–4 options), and importance rankings
- Leads with her existing shortlist — her choices reveal implicit preferences
- Flags finance questions as needing parent input
- Ends with a read-back summary for confirmation before writing to files

### Data sourcing
- **US universities:** College Scorecard API (free, requires API key from
  api.data.gov) for structured data; web research for rankings and course detail
- **UK universities:** Discover Uni / HESA for outcomes and entry data; UCAS
  for application requirements; university websites for course specifics
- **Rankings:** QS, Times Higher Education, Guardian, Complete University Guide
  — looked up per-university via web search (no API available at no cost)
- **Canada:** Statistics Canada for tuition; individual university sites for
  the rest

---

## Decisions Made

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-03-21 | Jekyll + GitHub Pages for the site | Native GitHub Pages support, YAML data files, no build complexity |
| 2026-03-21 | One markdown file per university | Self-contained, human-readable, easy to edit, renders as individual pages |
| 2026-03-21 | Weighted average scoring model | Simple, transparent, adjustable — avoids black-box ranking |
| 2026-03-21 | Interview leads with existing shortlist | More efficient; existing choices reveal implicit preferences |
| 2026-03-21 | Mixed question format (conversational + choice UI + ranking) | Balances openness with structure; choice UI suits constrained preference questions |
| 2026-03-21 | docs/ excluded from Jekyll build | Reference docs shouldn't appear as site pages |
| 2026-03-21 | College Scorecard API as primary US data source | Official, free, comprehensive, structured — API key required |
| 2026-03-21 | Status file (`docs/status.md`) maintained per-exchange | Process is likely to be interrupted; full recoverability required |
| 2026-03-21 | GitHub Pages enabled at https://rneild.github.io/uni-search | Site live; `_config.yml` updated with correct baseurl and url |

---

## What We've Tried / Experiments

*This section records things attempted — including things that didn't work well —
so we don't repeat mistakes and can learn from what does work.*

*(Nothing yet — will be updated as the project progresses.)*

---

## Lessons Learned

*Insights that should change how we approach things going forward.*

*(Nothing yet — will be updated as the project progresses.)*

---

## Ideas for Improvement

*Things worth trying, raised during the process but not yet acted on.*

- **Auto-population script:** write a Python script that accepts a university
  name, queries the College Scorecard API, and writes a pre-filled YAML file
  to `_universities/`. Would significantly reduce manual data entry for US
  universities. Requires API key first.
- **Score visualisation:** a radar/spider chart on each university page would
  make the strengths/weaknesses more immediately readable than a table.
- **Comparison view:** side-by-side view of two universities on a single page.
- **Application deadline tracker:** a dedicated page or data file tracking
  UCAS and Common App deadlines as the application season approaches.
- **Financial aid calculator:** a rough calculation showing expected net cost
  for US universities that meet 100% of demonstrated need vs those that don't.

---

## Open Questions

*Things we don't yet know how to handle, or need to decide.*

- College Scorecard API key: still needed from parent/applicant before US
  auto-population can be scripted.
- How to handle universities that are only relevant for one subject (e.g. a
  specialist music conservatoire vs a broad research university) — same
  criteria may not apply equally.
- Whether to include Canadian universities on the longlist — parent indicated
  USA/Canada but this hasn't been explored with the applicant yet.

---

## Session History

| Date | Who | What happened |
|------|-----|---------------|
| 2026-03-21 | Parent + Claude | Repository created; Jekyll site structure built; interview plan, status file, and this project log established. Interview not yet started. |
