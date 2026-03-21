#!/usr/bin/env python3
"""
fetch_scorecard.py — College Scorecard API fetcher

Queries the US Dept of Education College Scorecard API for a given
institution and writes (or updates) a university YAML file under
_universities/.

Usage:
    python3 scripts/fetch_scorecard.py "Massachusetts Institute of Technology"
    python3 scripts/fetch_scorecard.py "University of Michigan" --slug michigan

Requires:
    - .env file in repo root with COLLEGE_SCORECARD_API_KEY=...
    - pip install requests python-dotenv pyyaml (or: pip install -r scripts/requirements.txt)
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

try:
    import requests
    import yaml
    from dotenv import load_dotenv
except ImportError:
    print("Missing dependencies. Run: pip install requests python-dotenv pyyaml")
    sys.exit(1)

# ── Config ────────────────────────────────────────────────────────────────────

REPO_ROOT   = Path(__file__).parent.parent
ENV_FILE    = REPO_ROOT / ".env"
UNI_DIR     = REPO_ROOT / "_universities"
API_BASE    = "https://api.data.gov/ed/collegescorecard/v1/schools"

# Fields to request from the API
FIELDS = ",".join([
    "id",
    "school.name",
    "school.city",
    "school.state",
    "school.school_url",
    "school.ownership",                          # 1=public, 2=private nonprofit, 3=private for-profit
    "school.locale",                             # city/suburb/town/rural code
    "school.undergraduate_student_size",
    "latest.admissions.admission_rate.overall",
    "latest.admissions.sat_scores.25th_percentile.critical_reading",
    "latest.admissions.sat_scores.75th_percentile.critical_reading",
    "latest.admissions.sat_scores.25th_percentile.math",
    "latest.admissions.sat_scores.75th_percentile.math",
    "latest.admissions.act_scores.25th_percentile.cumulative",
    "latest.admissions.act_scores.75th_percentile.cumulative",
    "latest.cost.tuition.in_state",
    "latest.cost.tuition.out_of_state",
    "latest.cost.avg_net_price.private",
    "latest.cost.avg_net_price.public",
    "latest.aid.median_debt.completers.overall",
    "latest.aid.pell_grant_rate",
    "latest.aid.federal_loan_rate",
    "latest.completion.rate_suppressed.overall",
    "latest.earnings.10_yrs_after_entry.median",
    "latest.student.size",
])


# ── Helpers ───────────────────────────────────────────────────────────────────

def slugify(name: str) -> str:
    """Turn 'University of Michigan' → 'university-of-michigan'."""
    s = name.lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_]+", "-", s.strip())
    return s


def ownership_label(code) -> str:
    return {1: "public", 2: "private", 3: "private"}.get(int(code or 0), "")


def locale_label(code) -> str:
    """https://nces.ed.gov/programs/edge/docs/LOCALE_BOUNDARIES_SY1516.pdf"""
    code = int(code or 0)
    if code in (11, 12, 13): return "urban"
    if code in (21, 22, 23): return "suburban"
    if code in (31, 32, 33): return "town"
    if code in (41, 42, 43): return "rural"
    return ""


def size_category(n) -> str:
    if n is None: return ""
    n = int(n)
    if n < 5000:  return "small"
    if n < 15000: return "medium"
    return "large"


def pct(rate) -> float | None:
    """Convert 0.0–1.0 rate to rounded percentage."""
    if rate is None: return None
    return round(float(rate) * 100, 1)


def sat_range(r25_cr, r75_cr, r25_m, r75_m) -> str:
    """Combine reading + math SAT percentile ranges into a single string."""
    try:
        lo = int(r25_cr) + int(r25_m)
        hi = int(r75_cr) + int(r75_m)
        return f"{lo}–{hi}"
    except (TypeError, ValueError):
        return ""


def act_range(lo, hi) -> str:
    try:
        return f"{int(lo)}–{int(hi)}"
    except (TypeError, ValueError):
        return ""


# ── Main ──────────────────────────────────────────────────────────────────────

def fetch(name: str, api_key: str) -> dict:
    params = {
        "api_key":    api_key,
        "school.name": name,
        "fields":     FIELDS,
        "per_page":   5,
    }
    r = requests.get(API_BASE, params=params, timeout=20)
    r.raise_for_status()
    data = r.json()
    results = data.get("results", [])
    if not results:
        print(f"No results found for '{name}'")
        sys.exit(1)
    if len(results) > 1:
        print(f"Multiple matches found — picking closest:")
        for i, s in enumerate(results):
            print(f"  {i}: {s['school.name']} ({s['school.city']}, {s['school.state']})")
        idx = int(input("Enter number to use: "))
        return results[idx]
    return results[0]


def build_front_matter(s: dict, existing: dict | None = None) -> dict:
    """Map Scorecard fields to our YAML schema. Preserves existing manual edits."""

    size = s.get("school.undergraduate_student_size") or s.get("latest.student.size")
    net  = s.get("latest.cost.avg_net_price.private") or s.get("latest.cost.avg_net_price.public")
    tuition_out = s.get("latest.cost.tuition.out_of_state")
    tuition_in  = s.get("latest.cost.tuition.in_state")
    living_est  = 18000  # rough US estimate; override manually

    total_est = None
    if tuition_out and net:
        total_est = int(net) + living_est   # net price already includes living for Title IV
    elif tuition_out:
        total_est = int(tuition_out) + living_est

    fm = {
        "name":        s.get("school.name", ""),
        "short_name":  "",
        "country":     "USA",
        "city":        s.get("school.city", ""),
        "state_province": s.get("school.state", ""),
        "website":     f"https://{s['school.school_url']}" if s.get("school.school_url") else "",

        "type":            "research_university",
        "size_category":   size_category(size),
        "total_undergrad_enrollment": int(size) if size else None,
        "public_private":  ownership_label(s.get("school.ownership")),

        "rankings": {
            "qs_world":                None,
            "times_world":             None,
            "us_news_national":        None,
            "guardian_uk":             None,
            "complete_university_guide": None,
            "subject_rank":            None,
            "subject_rank_source":     "",
        },

        "admissions": {
            "acceptance_rate_pct":    pct(s.get("latest.admissions.admission_rate.overall")),
            "a_level_typical":        "",
            "a_level_minimum":        "",
            "ib_typical":             None,
            "sat_range":              sat_range(
                                        s.get("latest.admissions.sat_scores.25th_percentile.critical_reading"),
                                        s.get("latest.admissions.sat_scores.75th_percentile.critical_reading"),
                                        s.get("latest.admissions.sat_scores.25th_percentile.math"),
                                        s.get("latest.admissions.sat_scores.75th_percentile.math"),
                                      ),
            "act_range":              act_range(
                                        s.get("latest.admissions.act_scores.25th_percentile.cumulative"),
                                        s.get("latest.admissions.act_scores.75th_percentile.cumulative"),
                                      ),
            "gpa_typical":            None,
            "application_system":     "Common App",
            "application_deadline":   "",
            "early_deadline":         "",
            "early_type":             "",
        },

        "finances": {
            "tuition_domestic_usd":        int(tuition_in)  if tuition_in  else None,
            "tuition_international_usd":   int(tuition_out) if tuition_out else None,
            "living_cost_estimate_usd":    living_est,
            "total_cost_estimate_usd":     total_est,
            "financial_aid_available":     True,
            "aid_for_international":       None,
            "merit_scholarships":          None,
            "average_aid_package_usd":     int(net) if net else None,
        },

        "relevant_courses": [{"name": "", "degree": "", "duration_years": 4, "course_url": "", "notes": ""}],

        "scores": {k: None for k in [
            "academic_reputation", "overall_ranking", "course_fit",
            "entry_requirements", "cost", "financial_aid", "location",
            "campus_life", "size", "employability",
            "research_opportunities", "international_community",
        ]},

        "weighted_score": None,
        "status": "researching",
        "pros": [],
        "cons": [],
        "open_questions": [
            "Confirm international tuition — out-of-state rate used as proxy",
            "Check financial aid availability for international students",
            "Add relevant course URLs",
        ],

        # Scorecard metadata — for auditability
        "_scorecard_id":      s.get("id"),
        "_scorecard_fetched": __import__("datetime").date.today().isoformat(),
    }

    # Preserve manual edits from existing file
    if existing:
        preserve = ["short_name", "status", "pros", "cons", "relevant_courses",
                    "scores", "weighted_score", "open_questions", "rankings"]
        for key in preserve:
            if key in existing and existing[key] not in (None, [], {}, ""):
                fm[key] = existing[key]

    return fm


def write_file(slug: str, fm: dict, body: str = "") -> Path:
    path = UNI_DIR / f"{slug}.md"
    existing_body = ""

    # Read existing file if present
    existing_fm = None
    if path.exists():
        content = path.read_text()
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                try:
                    existing_fm = yaml.safe_load(parts[1])
                    existing_body = parts[2].strip()
                except yaml.YAMLError:
                    pass
        fm = build_front_matter.__wrapped__(fm) if hasattr(build_front_matter, "__wrapped__") else fm
        # Re-merge with existing
        fm = {**fm}
        if existing_fm:
            for key in ["short_name", "status", "pros", "cons", "relevant_courses",
                        "scores", "weighted_score", "open_questions", "rankings"]:
                if key in existing_fm and existing_fm[key] not in (None, [], {}, ""):
                    fm[key] = existing_fm[key]

    body_out = existing_body or body or "<!-- Add narrative notes about this university here. -->"

    yaml_str = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)
    out = f"---\n{yaml_str}---\n\n{body_out}\n"
    path.write_text(out)
    return path


# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Fetch College Scorecard data for a US university")
    parser.add_argument("name",  help="University name to search for")
    parser.add_argument("--slug", help="File slug override (default: auto-generated)")
    args = parser.parse_args()

    load_dotenv(ENV_FILE)
    api_key = os.getenv("COLLEGE_SCORECARD_API_KEY")
    if not api_key:
        print(f"No API key found. Add COLLEGE_SCORECARD_API_KEY to {ENV_FILE}")
        sys.exit(1)

    print(f"Searching College Scorecard for: {args.name!r}")
    school = fetch(args.name, api_key)
    print(f"Found: {school['school.name']} ({school['school.city']}, {school['school.state']})")

    fm = build_front_matter(school)
    slug = args.slug or slugify(school["school.name"])
    path = write_file(slug, fm)

    print(f"Written to: {path.relative_to(REPO_ROOT)}")
    print()
    print("Key data:")
    print(f"  Acceptance rate : {fm['admissions']['acceptance_rate_pct']}%")
    print(f"  SAT range       : {fm['admissions']['sat_range']}")
    print(f"  ACT range       : {fm['admissions']['act_range']}")
    print(f"  Tuition (out)   : ${fm['finances']['tuition_international_usd']:,}" if fm['finances']['tuition_international_usd'] else "  Tuition         : not available")
    print(f"  Avg net price   : ${fm['finances']['average_aid_package_usd']:,}" if fm['finances']['average_aid_package_usd'] else "  Avg net price   : not available")
    print()
    print("Still needed (fill manually):")
    print("  - Rankings (QS, US News, subject rank)")
    print("  - Financial aid for international students")
    print("  - Relevant course URLs and details")
    print("  - Application deadlines")


if __name__ == "__main__":
    main()
