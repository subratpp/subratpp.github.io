---
title: Code
permalink: /code/
redirect_from: [/giving-back/, /giving/]
lead: Research code from my papers, and from-scratch notebooks I write to give back.
---
{%- for s in site.data.projects %}
<h2 class="section">{{ s.section }}</h2>
{%- if s.note %}<p class="muted">{{ s.note }}</p>{% endif %}
<ul class="projects">
  {%- for p in s.items %}
  <li>
    <a class="name" href="{{ p.repo }}">{{ p.name }}</a>
    {%- if p.paper %} <span class="paper">· {{ p.paper }}</span>{% endif %}
    <p class="desc">{{ p.desc }}</p>
  </li>
  {%- endfor %}
</ul>
{%- endfor %}
