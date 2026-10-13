---
title: Blog
permalink: /blog/
redirect_from: [/year-archive/, /posts/]
lead: Notes on RL, interpretability and whatever else I'm thinking about.
---
{%- assign posts = site.blog | reverse -%}
{%- assign tags = posts | map: "tags" | join: "|" | split: "|" | uniq | sort -%}
{%- if tags.size > 0 %}
<div class="tag-filter" role="group" aria-label="Filter by tag">
  <button type="button" data-tag="" aria-pressed="true">all</button>
  {%- for t in tags %}
  {%- assign n = posts | where_exp: "p", "p.tags contains t" | size %}
  <button type="button" data-tag="{{ t | slugify }}" aria-pressed="false">#{{ t | slugify }} <span class="muted">{{ n }}</span></button>
  {%- endfor %}
</div>
{%- endif %}

{%- assign years = posts | group_by_exp: "p", "p.date | date: '%Y'" -%}
{%- for y in years %}
<section class="post-year">
  <h2 class="section">{{ y.name }}</h2>
  <ul class="dated">
    {%- for post in y.items %}
    <li data-tags="{% for t in post.tags %}{{ t | slugify }} {% endfor %}">
      <time>{{ post.date | date: '%m-%d' }}</time>
      <div>
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
        {% include tags.html tags=post.tags %}
      </div>
    </li>
    {%- endfor %}
  </ul>
</section>
{%- endfor %}

<script>
  (function () {
    var buttons = document.querySelectorAll('.tag-filter button');
    function apply(tag) {
      buttons.forEach(function (b) { b.setAttribute('aria-pressed', String(b.dataset.tag === tag)); });
      document.querySelectorAll('.post-year').forEach(function (sec) {
        var visible = 0;
        sec.querySelectorAll('li[data-tags]').forEach(function (li) {
          var show = !tag || (' ' + li.dataset.tags).indexOf(' ' + tag + ' ') !== -1;
          li.hidden = !show; visible += show;
        });
        sec.hidden = visible === 0;
      });
      var url = new URL(location); tag ? url.searchParams.set('tag', tag) : url.searchParams.delete('tag');
      history.replaceState(null, '', url);
    }
    buttons.forEach(function (b) { b.addEventListener('click', function () { apply(b.dataset.tag); }); });
    apply(new URLSearchParams(location.search).get('tag') || '');
  })();
</script>
