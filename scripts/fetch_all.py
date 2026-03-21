#!/usr/bin/env python3
"""
fetch_all.py — Batch university data fetcher

Reads scripts/universities.yml and fetches data for every entry:
  - USA    → College Scorecard API (automatic)
  - UK     → prints a research checklist for manual / web lookup
  - Canada → prints a research checklist for manual / web lookup

Usage:
    python3 scripts/fetch_all.py                  # process all
    python3 scripts/fetch_all.py --country USA    # only US entries
    python3 scripts/fetch_all.py --dry-run        # show what would run, no writes

Requirements:
    pip install -r scripts/requirements.txt
"""

import argparse
import subprocess
import sys
import time
from pathlib import Path

try:
    import yaml
    from dotenv import load_dotenv
except ImportError:
    print("Missing dependencies. Run: pip install -r scripts/requirements.txt")
    sys.exit(1)

REPO_ROOT    = Path(__file__).parent.parent
UNIVERSITIES = Path(__file__).parent / "universities.yml"
ENV_FILE     = REPO_ROOT / ".env"
FETCH_SCRIPT = Path(__file__).parent / "fetch_scorecard.py"

# Manual research checklist — printed for UK / Canada entries
UK_CHECKLIST = """
  Manual research needed for UK universities:
    [ ] UCAS entry requirements (https://www.ucas.com/explore/search/undergraduate)
    [ ] Tuition fees for international students (university website)
    [ ] Discover Uni satisfaction & outcomes (https://discoveruni.gov.uk)
    [ ] QS World Ranking (https://www.topuniversities.com/qs-world-university-rankings)
    [ ] Complete University Guide subject rank (https://www.thecompleteuniversityguide.co.uk)
    [ ] Guardian subject rank (https://www.theguardian.com/education/universityguide)
    [ ] Relevant course page URL
"""

CA_CHECKLIST = """
  Manual research needed for Canadian universities:
    [ ] Admission requirements (university website)
    [ ] Tuition fees for international students (university website)
    [ ] Maclean's ranking (https://education.macleans.ca/universities/)
    [ ] QS World Ranking
    [ ] Relevant course page URL
"""


def load_config() -> list[dict]:
    if not UNIVERSITIES.exists():
        print(f"Config not found: {UNIVERSITIES}")
        sys.exit(1)
    with open(UNIVERSITIES) as f:
        data = yaml.safe_load(f)
    entries = data.get("universities") or []
    return [e for e in entries if e]  # skip nulls from commented-out lines


def run_scorecard(entry: dict, dry_run: bool) -> bool:
    name  = entry["name"]
    slug  = entry.get("slug", "")
    cmd   = [sys.executable, str(FETCH_SCRIPT), name]
    if slug:
        cmd += ["--slug", slug]

    if dry_run:
        print(f"  [dry-run] would run: {' '.join(cmd)}")
        return True

    result = subprocess.run(cmd, capture_output=False)
    return result.returncode == 0


def main():
    parser = argparse.ArgumentParser(description="Batch-fetch university data")
    parser.add_argument("--country", choices=["USA", "UK", "Canada"],
                        help="Only process entries for this country")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would run without making any changes")
    args = parser.parse_args()

    load_dotenv(ENV_FILE)

    entries = load_config()
    if not entries:
        print("No universities listed in scripts/universities.yml yet.")
        print("Add entries to the file, then re-run.")
        sys.exit(0)

    if args.country:
        entries = [e for e in entries if e.get("country", "").upper() == args.country.upper()]

    if not entries:
        print(f"No entries found for country={args.country}")
        sys.exit(0)

    usa = [e for e in entries if e.get("country", "").upper() == "USA"]
    uk  = [e for e in entries if e.get("country", "").upper() == "UK"]
    ca  = [e for e in entries if e.get("country", "").upper() == "CANADA"]

    total   = len(entries)
    success = 0
    failed  = []

    print(f"\n{'='*60}")
    print(f"  University fetch — {total} institution(s)")
    print(f"  USA: {len(usa)}   UK: {len(uk)}   Canada: {len(ca)}")
    print(f"{'='*60}\n")

    # ── USA via College Scorecard ─────────────────────────────────────────
    if usa:
        print(f"── USA ({len(usa)} universities) ──────────────────────────────\n")
        for i, entry in enumerate(usa, 1):
            name = entry["name"]
            notes = entry.get("notes", "")
            print(f"[{i}/{len(usa)}] {name}")
            if notes:
                print(f"  Note: {notes}")
            ok = run_scorecard(entry, args.dry_run)
            if ok:
                success += 1
                print(f"  ✓ done\n")
            else:
                failed.append(name)
                print(f"  ✗ failed — check output above\n")
            if i < len(usa):
                time.sleep(0.5)  # gentle rate limiting

    # ── UK — manual research checklist ───────────────────────────────────
    if uk:
        print(f"\n── UK ({len(uk)} universities) — manual research required ────\n")
        for entry in uk:
            name = entry["name"]
            slug = entry.get("slug", "")
            notes = entry.get("notes", "")
            print(f"  {name}{(' → ' + slug) if slug else ''}")
            if notes:
                print(f"  Note: {notes}")
        print(UK_CHECKLIST)
        print("  Once researched, create or edit the file in _universities/")
        print("  and populate the YAML fields manually (or ask Claude to do it).\n")

    # ── Canada — manual research checklist ───────────────────────────────
    if ca:
        print(f"\n── Canada ({len(ca)} universities) — manual research required ─\n")
        for entry in ca:
            name = entry["name"]
            notes = entry.get("notes", "")
            print(f"  {name}")
            if notes:
                print(f"  Note: {notes}")
        print(CA_CHECKLIST)
        print("  Once researched, create or edit the file in _universities/")
        print("  and populate the YAML fields manually (or ask Claude to do it).\n")

    # ── Summary ───────────────────────────────────────────────────────────
    print(f"{'='*60}")
    print(f"  Done.")
    if usa:
        print(f"  USA fetched : {success - (len(usa) - len(failed))} / {len(usa)} succeeded")
    if failed:
        print(f"  Failed      : {', '.join(failed)}")
    if uk or ca:
        print(f"  UK/Canada   : {len(uk) + len(ca)} need manual research (see above)")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
