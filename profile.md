---
layout: default
title: Applicant Profile
---

{% assign p = site.data.profile %}

# Applicant Profile

## Academic Background

| Field | Value |
|-------|-------|
| School | {{ p.personal.school | default: "—" }} |
| Year | {{ p.academic.year_group | default: "—" }} |
| Entry year | {{ p.academic.entry_year | default: "—" }} |
| GPA | {{ p.academic.gpa | default: "—" }} |
| Nationality | {{ p.personal.nationality | default: "—" }} |
| Based in | {{ p.personal.current_city | default: p.personal.current_country | default: "—" }} |

### Test Scores

| Test | Score |
|------|-------|
{% if p.academic.sat_act.PSAT %}| PSAT | {{ p.academic.sat_act.PSAT }} (R&W {{ p.academic.sat_act.PSAT_breakdown.reading_writing }} / Math {{ p.academic.sat_act.PSAT_breakdown.math }}) |
{% endif %}{% if p.academic.sat_act.SAT %}| SAT | {{ p.academic.sat_act.SAT }} |
{% else %}| SAT | Pending (target {{ p.academic.sat_act.SAT_target | default: "TBD" }}) |
{% endif %}

### Qualifications

{% if p.academic.completed_courses.size > 0 %}
**Completed:** {{ p.academic.completed_courses | join: " · " }}

{% endif %}{% if p.academic.current_courses.size > 0 %}
**Current:** {{ p.academic.current_courses | join: " · " }}

{% endif %}{% if p.academic.planned_courses.size > 0 %}
**Planned:** {{ p.academic.planned_courses | join: " · " }}
{% endif %}

---

## Subject Interests

{% if p.interests.subjects.size > 0 %}**Subjects:** {{ p.interests.subjects | join: " · " }}{% endif %}

{% if p.interests.career_directions.size > 0 %}
**Career directions:**
{% for c in p.interests.career_directions %}
- {{ c }}
{% endfor %}
{% endif %}

{% if p.interests.extracurricular.size > 0 %}
**Extracurricular:**
{% for e in p.interests.extracurricular %}
- **{{ e.activity }}** ({{ e.duration }}){% if e.events %} — {{ e.events | join: ", " }}{% endif %}
{% endfor %}
{% endif %}

---

## Preferences

| Preference | Value |
|-----------|-------|
| Regions | {{ p.preferences.location.regions | join: ", " | default: "—" }} |
| Climate | {{ p.preferences.climate.preference | default: "—" }} |
| Institution size | {{ p.preferences.institution.size | default: "—" }} |
| Institution type | {{ p.preferences.institution.type | default: "—" }} |
| Course style | {{ p.preferences.study.course_style | default: "—" }} |
| Pre-med track | {{ p.preferences.study.premed | default: "—" }} |
| Annual budget | {% if p.preferences.finances.budget_annual_usd %}${{ p.preferences.finances.budget_annual_usd }}{% else %}—{% endif %} |
| Financial aid | {{ p.preferences.finances.financial_aid_needed | default: "—" }} |

{% if p.must_haves.size > 0 %}
### Must-haves
{% for m in p.must_haves %}
- {{ m }}
{% endfor %}
{% endif %}

{% if p.deal_breakers.size > 0 %}
### Deal-breakers
{% for d in p.deal_breakers %}
- {{ d }}
{% endfor %}
{% endif %}

---

## Notes

{{ p.qualitative_notes }}
