---
permalink: /
layout: default
redirect_from: [/about/, /about.html]
---
{%- assign a = site.author -%}
<section class="intro">
  <img src="{{ a.avatar | relative_url }}" alt="{{ a.name }}">
  <div>
    <h1>{{ a.name }}</h1>
    <p class="role">{{ a.role }}</p>
    <p class="tagline">{{ a.tagline }}</p>
    <div class="social">
      <a href="mailto:{{ a.email }}">{% include icon.html name="email" %}email</a>
      <a href="{{ a.scholar }}">{% include icon.html name="scholar" %}scholar</a>
      <a href="https://github.com/{{ a.github }}">{% include icon.html name="github" %}github</a>
      <a href="https://linkedin.com/in/{{ a.linkedin }}">{% include icon.html name="linkedin" %}linkedin</a>
      <a href="https://orcid.org/{{ a.orcid }}">{% include icon.html name="orcid" %}orcid</a>
      <a href="{{ a.cv_academic | relative_url }}" target="_blank" rel="noopener">{% include icon.html name="cv" %}cv-academic</a>
      <a href="{{ a.cv_industry | relative_url }}" target="_blank" rel="noopener">{% include icon.html name="cv" %}cv-industry</a>
    </div>
  </div>
</section>

<details class="interests" id="interests">
  <summary><span class="prompt">$ ls interests/</span> <span class="preview">{% for i in site.data.interests %}<b class="pill c-{{ i.color | default: 'slate' }}">{{ i.short }}</b>{% endfor %}</span></summary>
  <dl>
    {%- for i in site.data.interests %}
    <dt><b class="pill c-{{ i.color | default: 'slate' }}">{{ i.area }}</b></dt>
    <dd><ul class="chips c-{{ i.color | default: 'slate' }}">{% for x in i.items %}<li>{{ x }}</li>{% endfor %}</ul></dd>
    {%- endfor %}
  </dl>
</details>

<div class="bio" markdown="1">
I'm a PhD candidate in Computer Science at NTU Singapore, advised by [Arvind Easwaran](https://personal.ntu.edu.sg/arvinde/) (NTU) and [Blaise Genest](https://perso.crans.org/genest/) (CNRS IPAL, France), working on **trustworthy reinforcement learning** for safety-critical systems: making RL policies transparent, safe and verifiable. In particular, I work on **neurosymbolic** techniques, especially **symbolic policies** that are amenable to formal verification, and on learning methods to train them.

More broadly, I'm interested in neurosymbolic AI that integrates intuitive (System 1) learning with explicit, deliberative (System 2) reasoning, and in the maths underneath it all: learning theory and statistics.

Before NTU, I did an M.Tech in Computer Science at [ISI Kolkata](https://www.isical.ac.in/) and a B.Tech in Electronics & Instrumentation at [NIT Silchar](https://www.nits.ac.in/).
</div>

<h2 class="section">highlights</h2>
<div class="highlights">
  {%- for h in site.data.highlights %}
  <article class="hl c-{{ h.color | default: 'slate' }}">
    <h3><span class="hl-name">{{ h.name }}</span> <span class="hl-tagline">{{ h.tagline }}</span></h3>
    <p>{{ h.desc }}</p>
    <div class="hl-foot">
      <span class="hl-venues">{% for v in h.venues %}<span class="pill">{{ v }}</span>{% endfor %}</span>
      <span class="links">{% for l in h.links %}<a href="{{ l.href }}">{{ l.label }}</a>{% endfor %}</span>
    </div>
  </article>
  {%- endfor %}
</div>
<p class="hl-more"><a href="{{ '/publications/' | relative_url }}">all publications →</a></p>

<details class="callout">
  <summary><strong>Looking for postdoc / research roles.</strong></summary>
  <p>I’ll submit my thesis around Dec 2026 and am looking for roles from Feb 2027 in neurosymbolic RL for trustworthy deployment: differentiable symbolic methods for interpretability and safety, and symbolic knowledge for sample efficiency, with applications in robotics and energy systems.</p>
</details>

<details class="callout callout-alt">
  <summary><strong>Writing an RL book: <em>Zero to Hero</em>.</strong></summary>
  <p>From bandits and MDPs to modern deep RL, with from-scratch code for every algorithm, written to be read alongside the maths. Work in progress; code at <a href="https://github.com/subratpp/deep-rl-jutsu">deep-rl-jutsu</a>.</p>
</details>

<h2 class="section">news</h2>
{%- comment -%} Latest year shown; earlier years folded under "older news", one heading per year. {%- endcomment -%}
{%- assign news_years = site.data.news | sort: "date" | reverse | group_by_exp: "n", "n.date | slice: 0, 4" %}
<ul class="dated">
  {%- for n in news_years.first.items %}
  {% include news-item.html n=n %}
  {%- endfor %}
</ul>
{%- if news_years.size > 1 %}
<details class="more">
  <summary>older news</summary>
  {%- for y in news_years offset: 1 %}
  <details class="news-year">
    <summary>{{ y.name }} <span class="count">· {{ y.size }}</span></summary>
    <ul class="dated">
      {%- for n in y.items %}
      {% include news-item.html n=n %}
      {%- endfor %}
    </ul>
  </details>
  {%- endfor %}
</details>
{%- endif %}

<h2 class="section">recent writing</h2>
{%- assign posts = site.blog | reverse %}
<ul class="dated">
  {%- for post in posts limit: 2 %}
  <li><time>{{ post.date | date: '%Y-%m-%d' }}</time><a href="{{ post.url | relative_url }}">{{ post.title }}</a></li>
  {%- endfor %}
</ul>
{%- if posts.size > 2 %}
{%- assign older_years = posts | slice: 2, posts.size | group_by_exp: "p", "p.date | date: '%Y'" %}
<details class="more">
  <summary>older posts</summary>
  {%- for y in older_years %}
  <details class="news-year">
    <summary>{{ y.name }} <span class="count">· {{ y.size }}</span></summary>
    <ul class="dated">
      {%- for post in y.items %}
      <li><time>{{ post.date | date: '%Y-%m-%d' }}</time><a href="{{ post.url | relative_url }}">{{ post.title }}</a></li>
      {%- endfor %}
    </ul>
  </details>
  {%- endfor %}
</details>
{%- endif %}
