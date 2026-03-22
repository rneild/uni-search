---
layout: default
title: My Profile
---

{% assign p = site.data.profile %}

# My Profile

{% if p.personal.name != "" %}
This profile belongs to **{{ p.personal.name }}**.
{% else %}
*Profile not yet completed — run the profile interview with Claude.*
{% endif %}

## Personal

| Field | Value |
|-------|-------|
| Nationality | {{ p.personal.nationality | default: "—" }} |
| Current country | {{ p.personal.current_country | default: "—" }} |

## Academic Background

| Field | Value |
|-------|-------|
| Qualifications | {{ p.academic.qualifications | join: ", " | default: "—" }} |
| SAT/ACT | {% if p.academic.sat_act %}{{ p.academic.sat_act | inspect }}{% else %}—{% endif %} |
| GPA | {{ p.academic.gpa | default: "—" }} |

{% if p.academic.grades %}
### Current Grades
{% for g in p.academic.grades %}
- **{{ g[0] }}**: {{ g[1] }}
{% endfor %}
{% endif %}

## Subject Interests

{% if p.interests.subjects.size > 0 %}
{{ p.interests.subjects | join: " · " }}
{% else %}
*Not yet specified.*
{% endif %}

## Preferences Summary

| Preference | Value |
|-----------|-------|
| Regions | {{ p.preferences.location.regions | join: ", " | default: "—" }} |
| Urban/Rural | {{ p.preferences.location.urban_rural | default: "—" }} |
| Institution size | {{ p.preferences.institution.size | default: "—" }} |
| Institution type | {{ p.preferences.institution.type | default: "—" }} |
| Annual budget | {% if p.preferences.finances.budget_annual_usd %}${{ p.preferences.finances.budget_annual_usd | number_with_delimiter }}{% else %}—{% endif %} |
| Financial aid needed | {{ p.preferences.finances.financial_aid_needed | default: "—" }} |
| Year abroad | {{ p.preferences.study.year_abroad | default: "—" }} |

{% if p.notes != "" %}
## Notes

{{ p.notes }}
{% endif %}
