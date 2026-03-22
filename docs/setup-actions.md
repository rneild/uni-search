# Setup Actions Required

Things the parent or applicant needs to do to give Claude access to
the data sources and APIs that support this research.

---

## 1. College Scorecard API Key (US university data)

**What it unlocks:** Automatic population of acceptance rates, SAT/ACT ranges,
tuition fees, net price after financial aid, graduation rates, and graduate
earnings for every US university — from a single query per institution.

**Steps:**
1. Go to **https://api.data.gov/signup**
2. Enter your name and email address
3. You will receive an API key by email within a few minutes
4. Paste the key into this chat (or store it in a `.env` file in the repo root)

**Cost:** Free. No credit card required.
**Time:** ~2 minutes.

---

## 2. Discover Uni Data Download (UK university data)

**What it unlocks:** Official UK data on course-level student satisfaction,
graduate employment rates, and entry qualifications for all UK universities.

**Steps:**
1. Go to **https://discoveruni.gov.uk/data-and-downloads/**
2. Download the latest dataset (CSV/JSON format)
3. Place the file in `_data/raw/discover-uni/` in this repo

**Cost:** Free. No registration required.
**Time:** ~5 minutes.

---

## 3. GitHub Pages (publish the site)

**What it unlocks:** The Jekyll site becomes a live website, viewable in any
browser — useful for reviewing universities on a phone or sharing with others
(e.g. school counsellor, other family members).

**Steps:**
1. Go to the repository on GitHub: **https://github.com/rneild/uni-search**
2. Click **Settings** → **Pages** (left sidebar)
3. Under *Source*, select **Deploy from a branch**
4. Set branch to `main` (or whichever branch you want to publish), folder `/` (root)
5. Click **Save**
6. The site will be live at `https://rneild.github.io/uni-search` within a minute or two

**Note:** You will want to merge the current working branch into `main` first,
or set Pages to deploy from the working branch.
**Cost:** Free (included with GitHub).
**Time:** ~5 minutes.

---

## 4. Optional — `.env` file for API keys

Once you have the College Scorecard key, create a file called `.env` in the
repo root (this file is already gitignored and will never be committed):

```
COLLEGE_SCORECARD_API_KEY=your_key_here
```

Claude can then reference this when running data-fetch scripts locally.

---

## Status

| Action | Status | Notes |
|--------|--------|-------|
| College Scorecard API key | Done | Key stored in `.env` |
| Discover Uni data download | Not done | Useful for UK university research |
| GitHub Pages enabled | Done | Live at https://rneild.github.io/uni-search |
| `.env` file created | Done | Gitignored, stays local |
