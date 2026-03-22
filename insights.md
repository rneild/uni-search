---
layout: page
title: Insights
permalink: /insights/
---

This page captures conclusions we've reached together, things discovered about
what actually matters, and moments of clarity along the way. Every insight here
has been confirmed by the applicant before being recorded.

{% assign insights = site.data.insights.insights %}
{% assign total = insights | size %}

{% if total == 0 %}
<div class="empty-state">
  <p>No insights recorded yet — these will build up through the interview and research process.</p>
</div>
{% else %}

{% assign categories = "priorities,self-knowledge,universities,process,finance" | split: "," %}
{% assign labels = "What Actually Matters (Priorities),Self-Knowledge,Universities,Process & Approach,Finance" | split: "," %}

{% for cat in categories %}
  {% assign cat_insights = insights | where: "category", cat %}
  {% if cat_insights.size > 0 %}
    {% assign idx = forloop.index0 %}
<section class="insight-group">
<h2>{{ labels[idx] }}</h2>
    {% for insight in cat_insights %}
<div class="insight-card">
  <div class="insight-body">
    {% if insight.quote and insight.quote != "" %}
    <blockquote class="insight-quote">&ldquo;{{ insight.quote }}&rdquo;</blockquote>
    {% endif %}
    <p class="insight-text">{{ insight.text }}</p>
    {% if insight.evolved and insight.evolved != "" %}
    <p class="insight-evolved"><em>Refined: {{ insight.evolved }}</em></p>
    {% endif %}
  </div>
  <div class="insight-meta">
    <span class="insight-date">{{ insight.date }}</span>
    {% if insight.tags.size > 0 %}
    <span class="tag-list">{% for t in insight.tags %}<span class="tag">{{ t }}</span>{% endfor %}</span>
    {% endif %}
  </div>
</div>
    {% endfor %}
</section>
  {% endif %}
{% endfor %}

{% endif %}
