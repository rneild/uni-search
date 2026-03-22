---
layout: page
title: Open Items
permalink: /open-items/
---

Questions and threads that came up but couldn't be resolved in the moment.
Reviewed at the start of each session and cleared as items are answered.

{% assign all_items = site.data.open_items.open_items %}
{% assign open = all_items | where: "resolved", false %}
{% assign resolved = all_items | where: "resolved", true %}

{% if open.size == 0 and resolved.size == 0 %}
<div class="empty-state">
  <p>No open items yet — these will appear as questions arise during the process.</p>
</div>
{% else %}

{% if open.size > 0 %}
## To Do ({{ open.size }})

<ul class="open-items-list">
{% assign categories = "subject,finances,university,process,personal,logistics" | split: "," %}
{% for cat in categories %}
  {% assign cat_items = open | where: "category", cat %}
  {% for item in cat_items %}
  <li class="open-item open-item--open">
    <div class="open-item-header">
      <span class="open-item-cat tag">{{ item.category }}</span>
      <span class="open-item-meta">{{ item.date }} · raised by {{ item.raised_by }}</span>
    </div>
    <p class="open-item-text">{{ item.item }}</p>
    {% if item.context and item.context != "" %}
    <p class="open-item-context">Context: {{ item.context }}</p>
    {% endif %}
  </li>
  {% endfor %}
{% endfor %}
</ul>
{% endif %}

{% if resolved.size > 0 %}
## Resolved ({{ resolved.size }})

<ul class="open-items-list">
{% for item in resolved %}
  <li class="open-item open-item--resolved">
    <div class="open-item-header">
      <span class="open-item-cat tag">{{ item.category }}</span>
      <span class="open-item-meta">Raised {{ item.date }} · resolved {{ item.resolved_date }}</span>
    </div>
    <p class="open-item-text">{{ item.item }}</p>
    {% if item.resolution and item.resolution != "" %}
    <p class="open-item-resolution"><strong>Resolution:</strong> {{ item.resolution }}</p>
    {% endif %}
  </li>
{% endfor %}
</ul>
{% endif %}

{% endif %}
