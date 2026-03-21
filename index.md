---
layout: default
title: University Comparison
---

{% assign criteria = site.data.criteria.criteria %}

# University Comparison

{% assign universities = site.universities | where_exp: "u", "u.name != 'Example University'" %}
{% assign total_unis = universities | size %}

<p class="summary">{{ total_unis }} universities tracked · <a href="{{ '/profile/' | relative_url }}">View profile</a> · <a href="{{ '/criteria/' | relative_url }}">Scoring criteria</a> · <a href="{{ '/insights/' | relative_url }}">Insights</a> · <a href="{{ '/open-items/' | relative_url }}">Open items</a> · <a href="{{ '/log/' | relative_url }}">Session log</a></p>

{% if total_unis == 0 %}
<div class="empty-state">
  <p>No universities added yet. University profiles will appear here as they are researched.</p>
</div>
{% else %}

## All Universities

<div class="uni-cards">
{% assign sorted = universities | sort: "weighted_score" | reverse %}
{% for u in sorted %}
  {% assign total_weight = 0 %}
  {% assign weighted_sum = 0 %}
  {% for c in criteria %}
    {% assign key = c[0] %}
    {% assign criterion = c[1] %}
    {% assign score = u.scores[key] %}
    {% if score %}
      {% assign contrib = score | times: criterion.weight %}
      {% assign weighted_sum = weighted_sum | plus: contrib %}
      {% assign total_weight = total_weight | plus: criterion.weight %}
    {% endif %}
  {% endfor %}
  {% if total_weight > 0 %}
    {% assign overall = weighted_sum | divided_by: total_weight %}
  {% else %}
    {% assign overall = null %}
  {% endif %}

  <a href="{{ u.url | relative_url }}" class="uni-card status-border-{{ u.status }}">
    <div class="uni-card-header">
      <span class="uni-card-name">{{ u.name }}</span>
      <span class="status-badge status-{{ u.status }}">{{ u.status | replace: "_", " " }}</span>
    </div>
    <div class="uni-card-location">{{ u.city }}, {{ u.country }}</div>
    <div class="uni-card-meta">
      {% if u.rankings.qs_world %}<span>QS #{{ u.rankings.qs_world }}</span>{% endif %}
      {% if u.admissions.acceptance_rate_pct %}<span>{{ u.admissions.acceptance_rate_pct }}% accept</span>{% endif %}
      {% if u.finances.total_cost_estimate_usd %}<span>${{ u.finances.total_cost_estimate_usd | divided_by: 1000 | round }}k/yr</span>{% endif %}
    </div>
    <div class="uni-card-score">
      {% if total_weight > 0 %}
        <span class="score-pill">{{ overall | round: 1 }}/10</span>
      {% else %}
        <span class="score-pill pending">scoring pending</span>
      {% endif %}
    </div>
  </a>
{% endfor %}
</div>

## Comparison Table

<div class="table-scroll">
<table class="comparison-table">
  <thead>
    <tr>
      <th>University</th>
      <th>Country</th>
      <th>QS Rank</th>
      <th>Accept %</th>
      <th>Intl. Tuition (USD)</th>
      <th>Total Cost/yr (USD)</th>
      <th>Status</th>
      <th>Score</th>
    </tr>
  </thead>
  <tbody>
  {% for u in sorted %}
    {% assign total_weight2 = 0 %}
    {% assign weighted_sum2 = 0 %}
    {% for c in criteria %}
      {% assign key = c[0] %}
      {% assign criterion = c[1] %}
      {% assign score = u.scores[key] %}
      {% if score %}
        {% assign contrib = score | times: criterion.weight %}
        {% assign weighted_sum2 = weighted_sum2 | plus: contrib %}
        {% assign total_weight2 = total_weight2 | plus: criterion.weight %}
      {% endif %}
    {% endfor %}
    {% if total_weight2 > 0 %}{% assign ov2 = weighted_sum2 | divided_by: total_weight2 %}{% else %}{% assign ov2 = nil %}{% endif %}
    <tr>
      <td><a href="{{ u.url | relative_url }}">{{ u.name }}</a></td>
      <td>{{ u.country }}</td>
      <td>{% if u.rankings.qs_world %}#{{ u.rankings.qs_world }}{% else %}—{% endif %}</td>
      <td>{% if u.admissions.acceptance_rate_pct %}{{ u.admissions.acceptance_rate_pct }}%{% else %}—{% endif %}</td>
      <td>{% if u.finances.tuition_international_usd %}${{ u.finances.tuition_international_usd | number_with_delimiter }}{% else %}—{% endif %}</td>
      <td>{% if u.finances.total_cost_estimate_usd %}${{ u.finances.total_cost_estimate_usd | number_with_delimiter }}{% else %}—{% endif %}</td>
      <td><span class="status-badge status-{{ u.status }}">{{ u.status | replace: "_", " " }}</span></td>
      <td>{% if ov2 %}<strong>{{ ov2 | round: 1 }}</strong>{% else %}—{% endif %}</td>
    </tr>
  {% endfor %}
  </tbody>
</table>
</div>

{% endif %}
