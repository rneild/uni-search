# University Search

A Jekyll/GitHub Pages site for researching and comparing undergraduate universities (USA, Canada, UK).

## Structure

```
_data/
  profile.yml          # Student profile & preferences (filled via interview)
  criteria.yml         # Scoring criteria and weights

_universities/         # One .md file per university (YAML front matter + notes)
  example-university.md

_layouts/              # Jekyll page templates
assets/css/style.css   # Site stylesheet

index.md               # Homepage — comparison table & cards
profile.md             # Rendered profile page
criteria.md            # Scoring criteria page
```

## Workflow

1. **Profile interview** — work with Claude to fill out `_data/profile.yml`
2. **Add universities** — Claude researches each institution and creates a file in `_universities/`
3. **Adjust weights** — tweak `_data/criteria.yml` to reflect what matters most
4. **Track progress** — update each university's `status` field as you apply

## Running locally

```bash
bundle install
bundle exec jekyll serve
```

Then open http://localhost:4000
