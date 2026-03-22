# University Search — Interview Plan

This document records the agreed strategy for conducting the profile interview
with the applicant. It is reference material for Claude and for the parent.

---

## Context

- **Applicant:** daughter of repo owner, engaging directly (typing herself)
- **Stage:** has a shortlist in mind already — not starting from scratch
- **Countries in scope:** USA / Canada and UK
- **Level:** Undergraduate (Bachelor's)

---

## Interview Approach

### Tone & style
- Warm and conversational — not a form or an interrogation
- "I don't know yet" is always a valid answer
- Meet her where she is; don't push for certainty she doesn't have

### Question formats (mix and match as appropriate)
1. **Open conversational** — for broad, exploratory topics (e.g. *"What draws you to that subject?"*)
2. **Structured choice** — for topics where a small set of options covers most cases (presented as option selections in the UI)
3. **Importance ranking** — for preference questions where she needs to weigh competing priorities (e.g. *"How important is being in a big city — high / medium / low / not a factor?"*)

The choice and ranking formats are used selectively — when they genuinely make
it easier to answer, not just to speed things up. Conversational questions come
first to get context before narrowing.

---

## Interview Structure

Because the applicant already has a shortlist, the interview leads with that
list rather than asking abstract preference questions. Her existing choices
reveal her priorities implicitly.

### Phase 0 — Warm-up & existing shortlist
*Goal: establish rapport; get the list on the table*
- What universities are you currently thinking about?
- What first put each of them on your radar?

### Phase 1 — Academic situation
*Goal: understand qualifications, grades, timeline*
- Qualifications (A-levels / IB / other) and subjects
- Predicted or current grades
- SAT / ACT status (taken, planned, or not applicable)
- Year group and intended entry year

### Phase 2 — Subject & career interests
*Goal: understand what she wants to study and how certain she is*
- Subjects she enjoys most
- What she's thinking of studying (may already be clear from shortlist)
- Career directions, even vague ones
- Anything she's ruled out

### Phase 3 — Geography & environment
*Goal: extract location preferences from shortlist + direct questions*
- What appeals about the locations on her list?
- UK vs USA/Canada — strong pull either way, or genuinely open?
- City / campus / town preference
- Distance from home comfort level

### Phase 4 — University culture & course structure
*Goal: understand the kind of academic and social environment she wants*
- Size and culture (large research uni vs smaller, more personal)
- Course structure (broad first year vs specialised from day one — important
  UK/US difference)
- Year abroad or year in industry interest
- Campus life priorities (sports, arts, accommodation, etc.)

### Phase 5 — Finances
*Goal: understand budget and financial aid picture*
- Flag: *"This section may need a parent to chip in."*
- Rough annual budget (tuition + living, USD equivalent)
- Is financial aid / scholarships a requirement or a nice-to-have?
- US-specific: need-based aid vs merit scholarships

---

## Post-Interview Actions

1. Read back a summary for the applicant to confirm or correct
2. Populate `_data/profile.yml` from her answers
3. Review and propose adjusted weights in `_data/criteria.yml` based on her priorities
4. Create fully-researched university files in `_universities/` for each shortlist entry
5. Suggest 2–3 additional universities not on her list that match her revealed preferences
6. Flag any shortlist entries that may have significant practical issues (entry
   requirements, cost, financial aid eligibility for international students, etc.)

---

## Notes on UK vs USA/Canada Differences to Cover

These are important structural differences that many applicants aren't fully
aware of — worth touching on naturally during the interview:

| Topic | UK | USA / Canada |
|-------|-----|--------------|
| Course structure | Specialised from year 1 | Broad first 1–2 years (especially liberal arts / US) |
| Application system | UCAS (5 choices, Jan deadline) | Common App / Coalition / direct |
| Financial aid | Loans via Student Finance; limited scholarships | Need-based + merit aid; some very generous for internationals |
| Degree length | 3 years (4 in Scotland / integrated masters) | 4 years typical |
| Cost for internationals | £20–38k/yr tuition typical | $55–80k/yr at private US unis; Canadian unis cheaper |
| Entry requirements | Conditional offers based on A-level / IB predictions | Holistic — grades, essays, activities, recommendations |
