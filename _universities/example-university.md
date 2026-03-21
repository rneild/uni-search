---
# ============================================================
# UNIVERSITY DATA FILE — one file per institution
# This file is a template/example. Real entries are researched
# and populated by Claude during the search process.
# ============================================================

name: "Example University"
short_name: "ExU"
country: "USA"              # "USA", "Canada", "UK"
city: "City Name"
state_province: "State"
website: "https://www.example.edu"

# --- Classification ---
type: "research_university"   # research_university | liberal_arts | technical | other
size_category: "large"        # small (<5k) | medium (5-15k) | large (>15k)
total_undergrad_enrollment: 15000
public_private: "private"     # public | private

# --- Rankings (most recent available) ---
rankings:
  qs_world: null
  times_world: null
  us_news_national: null       # USA only
  guardian_uk: null            # UK only
  complete_university_guide: null  # UK only
  subject_rank: null           # rank in your specific subject (note which ranking)
  subject_rank_source: ""

# --- Admissions ---
admissions:
  acceptance_rate_pct: null    # e.g. 12 for 12%
  # UK entry requirements
  a_level_typical: ""          # e.g. "AAA", "A*AA"
  a_level_minimum: ""
  ib_typical: null             # e.g. 38
  # US/Canada entry requirements
  sat_range: ""                # e.g. "1400-1560"
  act_range: ""                # e.g. "32-35"
  gpa_typical: null
  application_system: ""       # "UCAS" | "Common App" | "Coalition" | "direct"
  application_deadline: ""     # e.g. "15 Jan" for UCAS, "Jan 1" for EA/ED
  early_deadline: ""
  early_type: ""               # "ED" (binding) | "EA" (non-binding) | "REA"

# --- Finances (annual, USD equivalent) ---
finances:
  tuition_domestic_usd: null
  tuition_international_usd: null
  living_cost_estimate_usd: null
  total_cost_estimate_usd: null    # tuition + living
  financial_aid_available: null    # true/false
  aid_for_international: null      # true/false
  merit_scholarships: null         # true/false
  average_aid_package_usd: null

# --- Courses relevant to applicant ---
relevant_courses:
  - name: ""
    degree: ""         # e.g. "BSc Computer Science"
    duration_years: null
    course_url: ""
    notes: ""

# --- Scoring (0-10 per criterion, matches criteria.yml) ---
# Leave null until researched; update as information is gathered
scores:
  academic_reputation: null
  overall_ranking: null
  course_fit: null
  entry_requirements: null
  cost: null
  financial_aid: null
  location: null
  campus_life: null
  size: null
  employability: null
  research_opportunities: null
  international_community: null

# Computed weighted total — leave null, calculated by template
weighted_score: null

# --- Status in your application process ---
status: "researching"   # researching | shortlisted | applying | applied | offer | rejected | withdrawn

# --- Notes ---
pros: []
cons: []
open_questions: []
---

<!-- Free-text notes go here — visited, talked to current students, etc. -->

## Notes

Add any narrative notes about this university here.
