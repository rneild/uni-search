---
layout: default
title: Scoring Criteria
---

{% assign criteria = site.data.criteria.criteria %}

# Scoring Criteria & Weights

Each university is scored 0–10 against every criterion below. The weighted score is the weighted average.
Weights can be adjusted at any time by editing `_data/criteria.yml`.

| Criterion | Weight | Notes |
|-----------|--------|-------|
{% for c in criteria %}{% assign key = c[0] %}{% assign criterion = c[1] %}| {{ criterion.label }} | **{{ criterion.weight }}** | {{ criterion.notes }} |
{% endfor %}

## How scores are calculated

`weighted_score = Σ(score × weight) / Σ(weights of scored criteria)`

Only criteria that have been scored contribute to the total — so universities with partial data can still be compared fairly within the criteria that have been researched.
