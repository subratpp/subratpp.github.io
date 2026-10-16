---
permalink: /
layout: default
redirect_from: [/about/, /about.html]
---
{%- assign a = site.author -%}
<div class="home">
<aside class="home-left">
<section class="intro home-intro">
  <img src="{{ a.avatar | relative_url }}" alt="{{ a.name }}">
  <div>
    <h1>{{ a.name }}</h1>
    {%- assign role_head = a.role | split: " · " | first %}
    <p class="role"><span>{{ role_head }}</span> <span>{{ a.role | remove_first: role_head | remove_first: " · " }}</span></p>
    <p class="tagline">{{ a.tagline }}</p>
    {% include email.html %}
    <div class="social">
      <a href="{{ a.scholar }}">{% include icon.html name="scholar" %}scholar</a>
      <a href="https://github.com/{{ a.github }}">{% include icon.html name="github" %}github</a>
      <a href="https://linkedin.com/in/{{ a.linkedin }}">{% include icon.html name="linkedin" %}linkedin</a>
      <a href="https://orcid.org/{{ a.orcid }}">{% include icon.html name="orcid" %}orcid</a>
      <span class="cv-pair">
        <a href="{{ a.cv_academic | relative_url }}" target="_blank" rel="noopener">{% include icon.html name="cv" %}cv-acad</a>
        <a href="{{ a.cv_industry | relative_url }}" target="_blank" rel="noopener">{% include icon.html name="cv" %}cv-industry</a>
      </span>
    </div>
  </div>
</section>

<details class="interests" id="interests" data-desktop-open>
  <summary><span class="prompt">$ ls interests/</span> <span class="preview">{% for i in site.data.interests %}<b class="pill c-{{ i.color | default: 'slate' }}">{{ i.short }}</b>{% endfor %}</span></summary>
  <dl>
    {%- for i in site.data.interests %}
    <div class="area" tabindex="0">
      <dt><b class="pill c-{{ i.color | default: 'slate' }}">{{ i.area }}</b> <span class="area-count">+{{ i.items.size }}</span></dt>
      <dd><ul class="chips c-{{ i.color | default: 'slate' }}">{% for x in i.items %}<li>{{ x }}</li>{% endfor %}</ul></dd>
    </div>
    {%- endfor %}
  </dl>
</details>
</aside>

<div class="home-center">
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
</div>

<aside class="home-right">
<div class="home-callouts">
<details class="callout">
  <summary><strong>Looking for postdoc / research roles.</strong></summary>
  <p>I’ll submit my thesis around Dec 2026 and am looking for roles from Feb 2027 in neurosymbolic RL for trustworthy deployment: differentiable symbolic methods for interpretability and safety, and symbolic knowledge for sample efficiency, with applications in robotics and energy systems.</p>
</details>

<details class="callout callout-alt">
  <summary><strong>Writing an RL book: <em>Zero to Hero</em>.</strong></summary>
  <p>From bandits and MDPs to modern deep RL, with from-scratch code for every algorithm, written to be read alongside the maths. Work in progress; code at <a href="https://github.com/subratpp/deep-rl-jutsu">deep-rl-jutsu</a>.</p>
</details>
</div>

<div class="feed-block feed-news">
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

</div>

<div class="feed-block feed-writing">
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
</div>
</aside>
</div>

<script>
  (function () {
    var wide = matchMedia('(min-width: 1100px)').matches;
    if (!wide) return;

    // the interests sidebar is always expanded
    document.querySelectorAll('[data-desktop-open]').forEach(function (d) { d.open = true; });

    // interests: a floating card with the area's topics follows the pointer
    var pop = document.createElement('div');
    pop.className = 'skill-pop'; pop.setAttribute('role', 'tooltip');
    document.body.appendChild(pop);
    function place(x, y) {
      var r = pop.getBoundingClientRect(), pad = 12;
      var left = Math.min(x + 16, innerWidth - r.width - pad);
      var top = y + 16 + r.height > innerHeight - pad ? y - r.height - 12 : y + 16;
      pop.style.left = Math.max(pad, left) + 'px'; pop.style.top = Math.max(pad, top) + 'px';
    }
    function show(area) {
      var color = area.querySelector('dd ul').className.match(/c-\w+/);
      pop.className = 'skill-pop ' + (color ? color[0] : '');
      pop.innerHTML = area.querySelector('dt .pill').outerHTML + area.querySelector('dd').innerHTML;
      requestAnimationFrame(function () { pop.classList.add('show'); });
    }
    function hide() { pop.classList.remove('show'); }
    document.querySelectorAll('.home-left .area').forEach(function (area) {
      area.addEventListener('mouseenter', function (e) { show(area); place(e.clientX, e.clientY); });
      area.addEventListener('mousemove', function (e) { place(e.clientX, e.clientY); });
      area.addEventListener('mouseleave', hide);
      area.addEventListener('focus', function () { var r = area.getBoundingClientRect(); show(area); place(r.right - 16, r.top - 16); });
      area.addEventListener('blur', hide);
    });
    document.querySelector('.home-left .interests').addEventListener('scroll', hide, { passive: true });

    // callouts open on hover; a click keeps one open
    if (matchMedia('(hover: hover)').matches) {
      document.querySelectorAll('.home-callouts details').forEach(function (d) {
        var pinned = false;
        d.querySelector('summary').addEventListener('click', function (e) {
          e.preventDefault(); pinned = !pinned; d.open = pinned;
        });
        d.addEventListener('mouseenter', function () { d.open = true; });
        d.addEventListener('mouseleave', function () { if (!pinned) d.open = false; });
      });
    }

    // news slowly scrolls through itself, then glides back to the top
    var box = document.querySelector('.feed-news');
    if (!box || matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    var SPEED = 18, PAUSE = 2500;          // px per second, ms to wait at either end
    var pos = 0, last = null, holdUntil = performance.now() + PAUSE, hovering = false;
    box.addEventListener('mouseenter', function () { hovering = true; });
    box.addEventListener('mouseleave', function () { hovering = false; pos = box.scrollTop; });
    ['wheel', 'touchstart', 'keydown'].forEach(function (ev) {
      box.addEventListener(ev, function () { holdUntil = performance.now() + 4000; pos = box.scrollTop; }, { passive: true });
    });
    function tick(now) {
      var dt = last === null ? 0 : (now - last) / 1000; last = now;
      var max = box.scrollHeight - box.clientHeight;
      if (max > 2 && getComputedStyle(box).overflowY === 'auto' && !hovering && now > holdUntil) {
        pos += SPEED * dt;
        if (pos >= max) {
          box.scrollTop = max;
          holdUntil = now + 2 * PAUSE;       // released by the timeout below
          setTimeout(function () { box.scrollTo({ top: 0, behavior: 'smooth' }); pos = 0; holdUntil = performance.now() + PAUSE; }, PAUSE);
          pos = 0;
        } else {
          box.scrollTop = pos;
        }
      }
      requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  })();
</script>
