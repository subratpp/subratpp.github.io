---
title: Code
permalink: /code/
redirect_from: [/giving-back/, /giving/]
lead: Research code from my papers, and from-scratch notebooks I write to give back.
aside: code
---
{%- for s in site.data.projects %}
<h2 class="section" id="{{ s.section | slugify }}">{{ s.section }}</h2>
{%- if s.note %}<p class="muted">{{ s.note }}</p>{% endif %}
<ul class="projects">
  {%- for p in s.items %}
  <li>
    <a class="name" href="{{ p.repo }}">{% if p.repo contains "github.com" %}{% include icon.html name="github" %}{% endif %}{{ p.name }}</a>
    {%- if p.paper %} <span class="paper">· {{ p.paper }}</span>{% endif %}
    <p class="desc">{{ p.desc }}</p>
  </li>
  {%- endfor %}
</ul>
{%- endfor %}
