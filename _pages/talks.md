---
title: Talks & Teaching
permalink: /talks/
lead: Invited talks, tutorials and lectures.
---
<ul class="pubs">
  {%- for t in site.data.talks %}
  <li class="pub">
    <span class="pub-title">{{ t.title }}</span>
    <span class="pub-venue">{{ t.venue }}, {{ t.year }}</span>
    {%- if t.links.size > 0 %}
    <span class="links">{% for l in t.links %}<a href="{{ l.href }}">{{ l.label }}</a>{% endfor %}</span>
    {%- endif %}
  </li>
  {%- endfor %}
</ul>
