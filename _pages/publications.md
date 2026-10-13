---
title: Publications
permalink: /publications/
lead: "Also on [Google Scholar](https://scholar.google.com/citations?user=-kOZ8c0AAAAJ&hl=en)."
---
{%- assign review = site.data.publications | where: "status", "review" -%}
{%- if review.size > 0 %}
<h2 class="section">under review</h2>
<ul class="pubs">
  {%- for p in review %}{% include pub.html pub=p show_year=false %}{% endfor %}
</ul>
{%- endif %}

<h2 class="section">published</h2>
{%- if site.data.pub_tags.size > 0 %}
<div class="tag-filter" id="pub-filter" role="group" aria-label="Filter by topic">
  <button type="button" data-tag="" aria-pressed="true">all</button>
  {%- for t in site.data.pub_tags %}
  <button type="button" class="c-{{ site.data.tag_colors[t.name] | default: 'slate' }}" data-tag="{{ t.slug }}" aria-pressed="false">#{{ t.name }} <span class="muted">{{ t.count }}</span></button>
  {%- endfor %}
</div>
{%- endif %}
{%- assign published = site.data.publications | where: "status", "published" | group_by: "year" -%}
{%- for g in published %}
<details class="year-group"{% if forloop.first %} open{% endif %}>
  <summary>{{ g.name }} <span class="count">· {{ g.size }} {% if g.size == 1 %}paper{% else %}papers{% endif %}</span></summary>
  <ul class="pubs">
    {%- for p in g.items %}{% include pub.html pub=p show_year=false %}{% endfor %}
  </ul>
</details>
{%- endfor %}

<script>
  // topic filter: no tag selected = everything (latest year open); otherwise OR over selected tags
  (function () {
    var bar = document.getElementById('pub-filter');
    if (!bar) return;
    var groups = document.querySelectorAll('details.year-group');
    var selected = new Set();
    function apply() {
      bar.querySelectorAll('button').forEach(function (b) {
        b.setAttribute('aria-pressed', String(b.dataset.tag ? selected.has(b.dataset.tag) : selected.size === 0));
      });
      groups.forEach(function (g, i) {
        var hits = 0;
        g.querySelectorAll('li.pub').forEach(function (li) {
          var tags = li.dataset.tags.split(' ');
          var show = selected.size === 0 || tags.some(function (t) { return selected.has(t); });
          li.hidden = !show; hits += show;
        });
        g.hidden = hits === 0;
        g.querySelector('.count').textContent = '· ' + hits + (hits === 1 ? ' paper' : ' papers');
        g.open = selected.size ? hits > 0 : i === 0;
      });
    }
    bar.addEventListener('click', function (e) {
      var b = e.target.closest('button');
      if (!b) return;
      var t = b.dataset.tag;
      if (!t) selected.clear();
      else if (selected.has(t)) selected.delete(t);
      else selected.add(t);
      apply();
    });
  })();

  document.addEventListener('click', function (e) {
    var b = e.target.closest('.bib-toggle');
    if (!b) return;
    var pre = b.closest('.pub').querySelector('.bibtex');
    pre.hidden = !pre.hidden;
    b.setAttribute('aria-expanded', String(!pre.hidden));
  });
</script>
