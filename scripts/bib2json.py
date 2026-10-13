#!/usr/bin/env python3
"""Convert files/references.bib into Jekyll data files.

    python scripts/bib2json.py

Writes _data/publications.json, talks.json and pub_tags.json. Entry types:

    @journal      (= @article)        @workshop     (= @misc)
    @conference   (= @inproceedings)  @talk         -> talks page
    @underreview  (= @unpublished)    listed without a venue (double-blind)

Optional link fields (ignored by BibTeX, so the LaTeX CV is unaffected):
    url, doi, arxiv, pdf, code, project, slides, video, poster
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BIB = ROOT / "files" / "references.bib"
OUT = ROOT / "_data"
ME = "Panda, Subrat Prasad"

# bib entry type -> kind; standard BibTeX names accepted as aliases
KINDS = {
    "journal": "journal", "article": "journal",
    "conference": "conference", "inproceedings": "conference",
    "workshop": "workshop", "misc": "workshop",
    "talk": "talk",
    "underreview": "preprint", "unpublished": "preprint",
}

# what the [bib] button exports, so visitors get types LaTeX understands
STANDARD = {"journal": "article", "conference": "inproceedings", "workshop": "misc", "talk": "misc", "underreview": "unpublished"}

LINK_FIELDS = ["pdf", "arxiv", "url", "doi", "code", "project", "slides", "video", "poster"]

ACCENTS = {"'": "\u0301", "`": "\u0300", "^": "\u0302", '"': "\u0308", "~": "\u0303", "c": "\u0327", "v": "\u030c"}


# --- parsing -----------------------------------------------------------------

def parse_bib(text):
    """Tiny brace-aware BibTeX parser; enough for hand-written .bib files."""
    entries, i = [], 0
    while (m := re.compile(r"@(\w+)\s*\{\s*([^,\s]+)\s*,").search(text, i)):
        etype, key, i = m.group(1).lower(), m.group(2), m.end()
        fields = {}
        while True:
            fm = re.compile(r"\s*,?\s*(\w+)\s*=\s*").match(text, i)
            if not fm:
                break
            name, i = fm.group(1).lower(), fm.end()
            value, i = read_value(text, i)
            fields[name] = value
        i = text.index("}", i) + 1  # closing brace of the entry
        if etype not in ("comment", "string", "preamble"):
            entries.append({"type": etype, "key": key, "_raw": text[m.start() : i], **fields})
    return entries


def read_value(text, i):
    if text[i] == "{":
        depth, j = 0, i
        while True:
            depth += {"{": 1, "}": -1}.get(text[j], 0)
            j += 1
            if depth == 0:
                return text[i + 1 : j - 1], j
    if text[i] == '"':
        j = text.index('"', i + 1)
        return text[i + 1 : j], j + 1
    m = re.compile(r"[^,}\s]+").match(text, i)  # bare number / macro (e.g. month = oct)
    return m.group(0), m.end()


# --- LaTeX -> text/HTML -------------------------------------------------------

def delatex(s):
    import unicodedata

    s = re.sub(r"\\href\{([^}]*)\}\{([^}]*)\}", r'<a href="\1">\2</a>', s)
    s = re.sub(r"\{?\\([`'^\"~cv])\s*\{?(\w)\}?\}?", lambda m: m.group(2) + ACCENTS[m.group(1)], s)
    s = s.replace("\\&", "&").replace("--", "–").replace("~", "\u00a0")
    s = re.sub(r"\\(emph|textit|textbf)\{([^}]*)\}", r"\2", s)
    s = s.replace("{", "").replace("}", "")
    return unicodedata.normalize("NFC", re.sub(r"\s+", " ", s).strip())


def authors(s):
    out = []
    for a in re.split(r"\s+and\s+", s):
        a = delatex(a)
        last, _, first = (p.strip() for p in a.partition(","))
        name = f"{first} {last}".strip() if first else a
        out.append({"name": name, "me": a.replace(" ", "") == ME.replace(" ", "")})
    return out


def links(e):
    out = []
    for f in LINK_FIELDS:
        if f not in e:
            continue
        href = e[f].strip()
        if f == "doi" and not href.startswith("http"):
            href = "https://doi.org/" + href
        out.append({"label": "paper" if f in ("url", "doi") else f, "href": href})
    seen = set()  # url + doi often point to the same paper; keep the first
    return [l for l in out if not (l["label"] in seen or seen.add(l["label"]))]


def clean_bibtex(raw):
    """Raw entry for the 'bib' button, without the web-only fields."""
    drop = set(LINK_FIELDS + ["keywords"]) - {"url", "doi"}
    lines = [l for l in raw.splitlines() if not re.match(r"\s*(\w+)\s*=", l) or re.match(r"\s*(\w+)", l).group(1).lower() not in drop]
    out = re.sub(r",(\s*\})$", r"\1", "\n".join(lines))
    return re.sub(r"^@(\w+)", lambda m: "@" + STANDARD.get(m.group(1).lower(), m.group(1)), out)


def to_item(e):
    kind = KINDS.get(e["type"], "workshop")
    status = "review" if kind == "preprint" else "published"
    venue = "" if status == "review" else delatex(e.get("journal") or e.get("booktitle") or e.get("howpublished") or e.get("publisher") or "")
    return {
        "key": e["key"],
        "title": delatex(e.get("title", "")),
        "authors": authors(e.get("author", "")),
        "venue": venue,
        "year": int(re.sub(r"\D", "", e.get("year", "0")) or 0),
        "kind": kind,
        "status": status,
        "note": delatex(e.get("note", "")),
        "tags": [t.strip() for t in e.get("keywords", "").split(",") if t.strip() and t.strip().lower() != "talk"],
        "links": links(e),
        "bibtex": clean_bibtex(e["_raw"]),
    }


def slug(t):
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")


def main():
    entries = parse_bib(BIB.read_text(encoding="utf-8"))
    is_talk = lambda e: e["type"] == "talk" or "talk" in e.get("keywords", "").lower()
    order = {"journal": 0, "conference": 1, "workshop": 2, "preprint": 3}
    pubs = sorted((to_item(e) for e in entries if not is_talk(e)), key=lambda p: (-p["year"], order[p["kind"]]))
    talks = sorted((to_item(e) for e in entries if is_talk(e)), key=lambda p: -p["year"])

    # tag filter on /publications/: published papers only, most used first
    counts = {}
    for p in pubs:
        if p["status"] == "published":
            for t in p["tags"]:
                counts[t] = counts.get(t, 0) + 1
    tags = [{"name": t, "slug": slug(t), "count": n} for t, n in sorted(counts.items(), key=lambda x: (-x[1], x[0]))]
    for p in pubs:
        p["tag_slugs"] = " ".join(slug(t) for t in p["tags"])

    OUT.mkdir(exist_ok=True)
    for name, data in (("publications", pubs), ("talks", talks), ("pub_tags", tags)):
        (OUT / f"{name}.json").write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"bib2json: {len(pubs)} publications, {len(talks)} talks, {len(tags)} tags -> _data/", file=sys.stderr)


if __name__ == "__main__":
    main()
