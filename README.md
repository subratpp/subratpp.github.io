# subratpp.github.io

Personal academic site of Subrat Prasad Panda, live at <https://subratpp.github.io>.

A small, theme-free [Jekyll](https://jekyllrb.com/) site, built and served by GitHub Pages on every push to `master`. No build step runs on GitHub's side except Jekyll itself.

## After edits

There's nothing to compile. GitHub Pages rebuilds the site about a minute after every push.

| You edited | Then |
| --- | --- |
| a blog post (`_blog/`), news, CV, code page, bio, `_config.yml`, anything else | commit and push |
| `files/references.bib` | run `pixi run pubs` first, then commit and push the `.bib` **and** `_data/*.json` |

```bash
git add -A && git commit -m "new post" && git push
```

Running the site locally (below) is optional. Use it to preview bigger changes before pushing.

## Run locally

You need [pixi](https://pixi.sh). It installs Ruby and Python into `.pixi/` inside this folder, so nothing touches your system.

```bash
# one-time
curl -fsSL https://pixi.sh/install.sh | bash   # or: brew install pixi
pixi install          # Ruby 3.3, Python 3.12, compilers
pixi run install      # Jekyll + plugins (same versions as GitHub Pages) into vendor/

# every time
pixi run serve        # http://localhost:4000, reloads on save
```

| Task | What it does |
| --- | --- |
| `pixi run serve` | Regenerate publications, then serve with live reload |
| `pixi run build` | Regenerate publications, then build into `_site/` |
| `pixi run pubs` | Only regenerate `_data/publications.json` and `_data/talks.json` from the `.bib` |

`_config.yml` is not hot-reloaded; restart `serve` after editing it.

## Where things live

```text
_config.yml              site title, your links (scholar, github, …), nav menu
_pages/about.md          home page: bio + postdoc callout
_pages/cv.md             short HTML CV (full CVs: files/cv_academic.pdf, files/cv_industry.pdf)
_data/news.yml           news items on the home page (any order; sorted by date)
_data/projects.yml       the /code/ page
_data/interests.yml      "interests & skills" panel on the home page
_data/highlights.yml     "highlights" cards on the home page (your key papers, in your words)
_data/tag_colors.yml     colour of each publication tag
files/references.bib     source of truth for /publications/ and /talks/
_data/*.json             GENERATED from the .bib; don't edit by hand
_blog/YYYY/name.md       blog posts, one folder per year
_layouts/, _includes/    HTML templates
files/                   everything served as-is: cv_academic.pdf, cv_industry.pdf, references.bib, images, style.css
scripts/bib2json.py      .bib → JSON converter (stdlib Python only)
```

## Common edits

### Add a blog post

Create `_blog/YYYY/short-name.md` (make the year folder if it's new). The URL is `/posts/YYYY/MM/short-name/`.

```markdown
---
title: My new post
date: 2026-10-13
tags: [Reinforcement Learning, Interpretability]
---

Write Markdown here. Math works: inline $\pi(a \mid s)$ or display

$$
V^\pi(s) = \mathbb{E}_\pi\left[\sum_t \gamma^t r_t \mid s_0 = s\right]
$$
```

`date` is required, because it sets the order and the URL. Tags show up as filters on `/blog/`. To keep a post unpublished, add `published: false`.

### Add a paper or talk

1. Add the entry to `files/references.bib`, choosing the type by what it is:

   | Type | Use for | Venue field |
   | --- | --- | --- |
   | `@journal` | journal article | `journal` |
   | `@conference` | conference paper | `booktitle` |
   | `@workshop` | workshop paper, student abstract | `howpublished` |
   | `@talk` | invited talk, tutorial, lecture (goes to /talks/) | `howpublished` |
   | `@underreview` | submitted paper. **Leave out the venue** to keep it double-blind | none |

   When an `@underreview` paper is accepted, change it to `@conference`/`@journal` and add the venue. The standard names (`@article`, `@inproceedings`, `@misc`, `@unpublished`) still work.

   Tag papers with `keywords = {RL, Neurosymbolic}` (any number, comma-separated). Tags on published papers become the topic filter on `/publications/`. Give a new tag a colour in `_data/tag_colors.yml` (otherwise it's grey).

   Optional link fields become buttons on the site:

   ```bibtex
   arxiv   = {https://arxiv.org/abs/...},
   code    = {https://github.com/...},
   project = {https://...},          % also: pdf, slides, video, poster, url, doi
   ```

2. Run `pixi run pubs` (or just `pixi run serve`, which runs it for you).
3. Commit the `.bib` **and** the regenerated `_data/publications.json` / `_data/talks.json`. GitHub Pages can't run Python, so it builds from the committed JSON.

### Add a news item

Add an entry to `_data/news.yml` (`date: YYYY-MM`, `text`, optional `image`). The home page shows the latest year's news; earlier years are folded under "older news", grouped by year.

## Deploy (details)

Push to `master`. GitHub Pages builds the site in about a minute.
