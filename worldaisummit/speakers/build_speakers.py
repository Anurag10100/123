#!/usr/bin/env python3
"""Build static speaker profile pages for worldaisummit.com.

Reads speakers.json, renders templates/speaker.html and templates/index.html,
and writes:

  dist/speakers/index.html            speaker directory (government first)
  dist/speakers/<slug>/index.html     one page per publishable speaker
  dist/sitemap-speakers.xml           sitemap for the pages above
  dist/build-report.md                what was built and what is missing

No third-party dependencies. Run: python3 build_speakers.py [--out DIR] [--clean]

Local preview (links point at your machine instead of the live site):

  python3 build_speakers.py --clean --base-url http://localhost:8000
  python3 -m http.server 8000 --directory dist
  open http://localhost:8000/speakers/

Rebuild without --base-url before uploading to the live site.

Clickable offline copy (open index.html straight from a folder, no server):

  python3 build_speakers.py --offline --out preview

Writes preview/index.html and preview/<slug>.html with relative links between
the pages. Links to the rest of the site still point at the live domain.
"""

import argparse
import datetime as dt
import html
import json
import pathlib
import re
import shutil
import sys
from string import Template

ROOT = pathlib.Path(__file__).resolve().parent
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REQUIRED = ("slug", "name", "title_role", "role", "org", "group")
SESSION_KEYS = ("title", "date", "time", "hall", "format", "track")
TITLE_MAX = 70
DESC_MAX = 160


def esc(value):
    return html.escape("" if value is None else str(value), quote=True)


def join_url(base, path):
    if not path:
        return base
    if path.startswith("http://") or path.startswith("https://"):
        return path
    return base.rstrip("/") + "/" + path.lstrip("/")


def initials(name):
    skip = {"dr", "dr.", "shri", "smt", "smt.", "mr", "mr.", "ms", "ms.", "prof", "prof.",
            "ias", "ips", "ifs", "irs", "ifos"}
    words = [w for w in re.split(r"[\s,]+", name) if w and w.lower() not in skip]
    if not words:
        words = [w for w in re.split(r"[\s,]+", name) if w]
    return "".join(w[0].upper() for w in words[:2]) or "?"


def person_name(name):
    """Name without a trailing service suffix such as ', IAS' (used for JSON-LD)."""
    m = re.match(r"^(.*?),\s*(IAS|IPS|IFS|IRS|IFoS)$", name.strip())
    if m:
        return m.group(1).strip(), m.group(2)
    return name.strip(), ""


def format_date(iso):
    try:
        d = dt.date.fromisoformat(iso)
    except (TypeError, ValueError):
        return iso or ""
    return f"{d.strftime('%A')}, {d.day} {d.strftime('%B %Y')}"


def paragraphs(text):
    parts = [p.strip() for p in re.split(r"\n\s*\n", text.strip()) if p.strip()]
    return "".join(f"<p>{esc(p)}</p>\n" for p in parts)


# ----------------------------------------------------------------------------
# Validation
# ----------------------------------------------------------------------------

def validate(data):
    errors, warnings = [], []
    site = data.get("site", {})
    for key in ("base_url", "site_name", "speakers_path", "event_name", "event_start",
                "event_end", "event_dates_text", "venue", "city", "organiser", "pass_url",
                "agenda_url", "pass_from"):
        if not site.get(key):
            errors.append(f"site.{key} is missing")
    group_ids = [g.get("id") for g in data.get("groups", [])]
    if not group_ids:
        errors.append("groups is empty")
    seen = set()
    for i, s in enumerate(data.get("speakers", [])):
        label = s.get("slug") or s.get("name") or f"speaker #{i}"
        for key in REQUIRED:
            if not s.get(key):
                (errors if s.get("publish", True) else warnings).append(f"{label}: '{key}' is empty")
        slug = s.get("slug", "")
        if slug and not SLUG_RE.match(slug):
            errors.append(f"{label}: slug must be lowercase letters, digits and hyphens")
        if slug in seen:
            errors.append(f"{label}: duplicate slug")
        seen.add(slug)
        if s.get("group") and s["group"] not in group_ids:
            errors.append(f"{label}: unknown group '{s['group']}'")
        session = s.get("session")
        if session is not None:
            if not isinstance(session, dict):
                errors.append(f"{label}: session must be an object or null")
            else:
                for key in session:
                    if key not in SESSION_KEYS:
                        warnings.append(f"{label}: unknown session key '{key}'")
                if session.get("date"):
                    try:
                        d = dt.date.fromisoformat(session["date"])
                        start = dt.date.fromisoformat(site.get("event_start", "1970-01-01"))
                        end = dt.date.fromisoformat(site.get("event_end", "2999-12-31"))
                        if not (start <= d <= end):
                            warnings.append(f"{label}: session date {session['date']} is outside the event dates")
                    except ValueError:
                        errors.append(f"{label}: session.date must be YYYY-MM-DD")
        if s.get("confirmed_2026") and not session:
            warnings.append(f"{label}: confirmed for 2026 but no session details yet")
        if session and not s.get("confirmed_2026"):
            warnings.append(f"{label}: has a session but confirmed_2026 is false (session is hidden until confirmed)")
        if s.get("photo"):
            photo = s["photo"]
            local = ROOT / "photos" / pathlib.Path(photo).name
            if not photo.startswith("http") and not local.exists():
                warnings.append(f"{label}: photo '{photo}' not found in photos/ (upload it to the site at that path)")
    return errors, warnings


# ----------------------------------------------------------------------------
# Rendering helpers
# ----------------------------------------------------------------------------

def site_vars(site):
    base = site["base_url"].rstrip("/")
    idx = join_url(base, site["speakers_path"])
    if not idx.endswith("/"):
        idx += "/"
    return {
        "site_name": esc(site["site_name"]),
        "home_url": base + "/",
        "speakers_index_url": idx,
        "agenda_url": join_url(base, site["agenda_url"]),
        "awards_url": join_url(base, site.get("awards_url", "/")),
        "pass_url": join_url(base, site["pass_url"]),
        "contact_url": join_url(base, site.get("contact_url", "/")),
        "event_name": esc(site["event_name"]),
        "event_dates_text": esc(site["event_dates_text"]),
        "venue": esc(site["venue"]),
        "city": esc(site["city"]),
        "organiser": esc(site["organiser"]),
        "pass_from": esc(site["pass_from"]),
        "og_image_tag": (f'<meta property="og:image" content="{esc(join_url(base, site["og_image"]))}">'
                         if site.get("og_image") else ""),
    }


def speaker_url(site, s):
    base = site["base_url"].rstrip("/")
    path = site["speakers_path"].strip("/")
    return f"{base}/{path}/{s['slug']}/"


def page_title(site, s):
    """Name first (that is the query people type), then role, then brand.

    Falls back to shorter forms so the title stays within TITLE_MAX characters.
    """
    for title in (
        f"{s['name']} | {s['title_role']} | {site['event_name']}",
        f"{s['name']} | {s['title_role']} | {site['site_name']}",
        f"{s['name']} | {site['event_name']}",
    ):
        if len(title) <= TITLE_MAX:
            return title
    return title


def short_dates(site):
    try:
        a = dt.date.fromisoformat(site["event_start"])
        b = dt.date.fromisoformat(site["event_end"])
    except (KeyError, ValueError):
        return site.get("event_dates_text", "")
    if a == b:
        return f"{a.day} {a:%b %Y}"
    if a.month == b.month:
        return f"{a.day}-{b.day} {a:%b %Y}"
    return f"{a.day} {a:%b}-{b.day} {b:%b %Y}"


def meta_description(site, s):
    """Name + role, then the 2026/2025 relationship, then dates, city and price.

    Tries the fullest version first and shortens the tail until it fits DESC_MAX.
    """
    session = s.get("session") if s.get("confirmed_2026") else None
    if session and session.get("title"):
        middle = f"Speaking at {site['event_name']}: {session['title']}."
    elif s.get("confirmed_2026"):
        middle = f"Confirmed speaker at {site['event_name']}."
    elif "2025" in s.get("editions", []):
        middle = "Spoke at World AI Summit 2025, Bengaluru."
    else:
        middle = ""
    city = site["city"].split(",")[0].strip()
    lead = f"{s['name']}, {s['title_role']}."
    tails = (
        f"{site['event_name']}: {site['event_dates_text']}, {city}. Delegate passes from {site['pass_from']}.",
        f"{site['event_name']}: {short_dates(site)}, {city}. Passes from {site['pass_from']}.",
        f"{site['event_name']}: {short_dates(site)}, {city}.",
        f"{site['event_name']}, {city}.",
    )
    for tail in tails:
        desc = " ".join(p for p in (lead, middle, tail) if p)
        if len(desc) <= DESC_MAX:
            return desc
    return " ".join(p for p in (lead, tails[-1]) if p)


def badges(site, s):
    out = []
    if s.get("confirmed_2026"):
        out.append(f'<span class="badge confirmed">Confirmed speaker, {esc(site["event_name"])}</span>')
    for ed in s.get("editions", []):
        if ed == "2025":
            role = s.get("role_2025")
            label = f"Speaker, World AI Summit 2025" + (f" ({esc(role)})" if role else "")
            out.append(f'<span class="badge">{label}</span>')
    return "".join(out)


def links(s):
    out = []
    if s.get("linkedin"):
        out.append(f'<a href="{esc(s["linkedin"])}" target="_blank" rel="noopener">LinkedIn</a>')
    if s.get("website"):
        out.append(f'<a href="{esc(s["website"])}" target="_blank" rel="noopener">Website</a>')
    return "".join(out)


def photo_html(site, s, css_class="photo", size=180, lazy=False):
    if s.get("photo"):
        src = esc(join_url(site["base_url"], s["photo"]))
        loading = "lazy" if lazy else "eager"
        return (f'<img class="{css_class}" src="{src}" alt="{esc(s["name"])}, {esc(s["title_role"])}" '
                f'width="{size}" height="{size}" loading="{loading}">')
    return f'<div class="{css_class} placeholder" aria-hidden="true">{esc(initials(s["name"]))}</div>'


def session_block(site, s):
    session = s.get("session") if s.get("confirmed_2026") else None
    if not session:
        if s.get("confirmed_2026"):
            return (f"Session at {esc(site['event_name'])}",
                    f"<p>{esc(s['name'])} is a confirmed speaker at {esc(site['event_name'])}, "
                    f"{esc(site['event_dates_text'])}, {esc(site['venue'])}, {esc(site['city'])}. "
                    f"Session title, time and hall will be published on this page once the agenda is final. "
                    f"<a href=\"{esc(join_url(site['base_url'], site['agenda_url']))}\">See the agenda</a>.</p>")
        heading = f"{esc(site['event_name'])} session"
        past = ""
        if "2025" in s.get("editions", []):
            role = s.get("role_2025")
            past = (f"{esc(s['name'])} spoke at the first edition, World AI Summit 2025 in Bengaluru"
                    + (f", as {esc(role)}" if role else "") + ". ")
        return (heading,
                f"<p>{past}The 2026 line-up is being announced. "
                f"{esc(site['event_name'])} takes place on {esc(site['event_dates_text'])} at "
                f"{esc(site['venue'])}, {esc(site['city'])}. "
                f"<a href=\"{esc(join_url(site['base_url'], site['agenda_url']))}\">See the agenda</a>.</p>")
    rows = []
    if session.get("format"):
        rows.append(("Format", session["format"]))
    if session.get("date"):
        rows.append(("Date", format_date(session["date"])))
    if session.get("time"):
        rows.append(("Time", session["time"]))
    if session.get("hall"):
        rows.append(("Hall", session["hall"]))
    if session.get("track"):
        rows.append(("Track", session["track"]))
    dl = "".join(f"<dt>{esc(k)}</dt><dd>{esc(v)}</dd>" for k, v in rows)
    title = esc(session.get("title") or "Session details to be announced")
    body = f'<p class="title">{title}</p>' + (f"<dl>{dl}</dl>" if dl else "")
    return (f"Session at {esc(site['event_name'])}", body)


def bio_block(site, s):
    if s.get("bio"):
        return paragraphs(s["bio"])
    # No bio supplied: one factual sentence built only from the data file.
    first = f"{s['name']} is {s['role']}, {s['org']}"
    if "2025" in s.get("editions", []):
        role = s.get("role_2025")
        first += (", and spoke at the first edition of World AI Summit in Bengaluru in 2025"
                  + (f" as {role}" if role else ""))
    parts = [first + "."]
    if s.get("confirmed_2026"):
        parts.append(f"{s['name']} returns as a speaker at {site['event_name']}.")
    return f"<p>{esc(' '.join(parts))}</p>\n"


def others_block(site, s, published):
    same = [o for o in published if o["group"] == s["group"] and o["slug"] != s["slug"]]
    rest = [o for o in published if o["group"] != s["group"]]
    picks = (same + rest)[:6]
    items = []
    for o in picks:
        items.append(f'          <li><a href="{esc(speaker_url(site, o))}">{esc(o["name"])}</a>'
                     f'<small>{esc(o["title_role"])}</small></li>')
    return "\n".join(items)


def event_ld(site):
    base = site["base_url"].rstrip("/")
    city = site["city"].split(",")[0].strip()
    ev = {
        "@type": "Event",
        "name": site["event_name"],
        "startDate": site["event_start"],
        "endDate": site["event_end"],
        "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
        "eventStatus": "https://schema.org/EventScheduled",
        "url": base + "/",
        "location": {
            "@type": "Place",
            "name": site["venue"],
            "address": {"@type": "PostalAddress", "addressLocality": city, "addressCountry": "IN"},
        },
        "organizer": {"@type": "Organization", "name": site["organiser"]},
    }
    if site.get("pass_price_inr"):
        ev["offers"] = {
            "@type": "Offer",
            "url": join_url(base, site["pass_url"]),
            "price": str(site["pass_price_inr"]),
            "priceCurrency": "INR",
            "availability": "https://schema.org/InStock",
        }
    return ev


def speaker_ld(site, s, url, description):
    base = site["base_url"].rstrip("/")
    name, suffix = person_name(s["name"])
    person = {
        "@type": "Person",
        "@id": url + "#person",
        "name": name,
        "url": url,
        "jobTitle": s["role"],
        "worksFor": {"@type": "Organization", "name": s["org"]},
        "description": description,
    }
    if s.get("honorific"):
        person["honorificPrefix"] = s["honorific"]
    if suffix:
        person["honorificSuffix"] = suffix
    if s.get("photo"):
        person["image"] = join_url(base, s["photo"])
    same_as = [u for u in (s.get("linkedin"), s.get("website")) if u]
    if same_as:
        person["sameAs"] = same_as
    if s.get("confirmed_2026"):
        ev = event_ld(site)
        session = s.get("session") or {}
        if session.get("title"):
            sub = {"@type": "Event", "name": session["title"], "location": ev["location"]}
            if session.get("date"):
                sub["startDate"] = session["date"]
            if session.get("hall"):
                sub["location"] = {"@type": "Place", "name": f"{session['hall']}, {site['venue']}",
                                   "address": ev["location"]["address"]}
            ev["subEvent"] = sub
        person["performerIn"] = ev
    crumbs = {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": base + "/"},
            {"@type": "ListItem", "position": 2, "name": "Speakers",
             "item": join_url(base, site["speakers_path"])},
            {"@type": "ListItem", "position": 3, "name": name, "item": url},
        ],
    }
    page = {
        "@type": "ProfilePage",
        "@id": url,
        "url": url,
        "name": page_title(site, s),
        "mainEntity": {"@id": url + "#person"},
        "isPartOf": {"@type": "WebSite", "name": site["site_name"], "url": base + "/"},
    }
    return {"@context": "https://schema.org", "@graph": [page, person, crumbs]}


def index_ld(site, published, url, title):
    base = site["base_url"].rstrip("/")
    items = [{"@type": "ListItem", "position": i + 1, "name": person_name(s["name"])[0],
              "url": speaker_url(site, s)} for i, s in enumerate(published)]
    return {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "CollectionPage", "@id": url, "url": url, "name": title,
             "isPartOf": {"@type": "WebSite", "name": site["site_name"], "url": base + "/"},
             "about": event_ld(site),
             "mainEntity": {"@type": "ItemList", "itemListElement": items}},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": base + "/"},
                {"@type": "ListItem", "position": 2, "name": "Speakers", "item": url}]},
        ],
    }


def dump_ld(obj):
    # "</" cannot appear inside a script block; JSON escaping of "/" keeps it safe.
    return json.dumps(obj, ensure_ascii=False, indent=2).replace("</", "<\\/")


# ----------------------------------------------------------------------------
# Builders
# ----------------------------------------------------------------------------

def render_speaker(tpl, site, s, published, common):
    url = speaker_url(site, s)
    desc = meta_description(site, s)
    heading, session_html = session_block(site, s)
    v = dict(common)
    v.update({
        "page_title": esc(page_title(site, s)),
        "meta_description": esc(desc),
        "canonical_url": esc(url),
        "json_ld": dump_ld(speaker_ld(site, s, url, desc)),
        "name": esc(s["name"]),
        "honorific_html": f'<span class="honorific">{esc(s["honorific"])}</span>' if s.get("honorific") else "",
        "role": esc(s["role"]),
        "org": esc(s["org"]),
        "badges_html": badges(site, s),
        "links_html": links(s),
        "photo_html": photo_html(site, s),
        "session_heading": heading,
        "session_html": session_html,
        "bio_html": bio_block(site, s),
        "others_html": others_block(site, s, published),
    })
    if s.get("photo"):
        v["og_image_tag"] = f'<meta property="og:image" content="{esc(join_url(site["base_url"], s["photo"]))}">'
    return tpl.safe_substitute(v), url, desc


def render_index(tpl, site, groups, published, common):
    url = common["speakers_index_url"]
    title = f"Speakers | {site['event_name']} | {site['event_dates_text']}, {site['city'].split(',')[0]}"
    if len(title) > TITLE_MAX:
        title = f"Speakers | {site['event_name']}"
    n = len(published)
    desc = (f"Speakers at {site['event_name']}, {site['event_dates_text']}, {site['venue']}, {site['city']}: "
            f"ministers, secretaries, regulators, CXOs and founders shaping AI in India. Delegate passes from {site['pass_from']}.")
    if len(desc) > DESC_MAX:
        desc = (f"Speakers at {site['event_name']}, {site['event_dates_text']}, {site['city'].split(',')[0]}: "
                f"government, enterprise and founder voices on AI in India. Passes from {site['pass_from']}.")
    confirmed = [s for s in published if s.get("confirmed_2026")]
    if confirmed:
        intro = (f"{len(confirmed)} confirmed speakers so far for {site['event_name']} on {site['event_dates_text']} at "
                 f"{site['venue']}, {site['city']}. More names are added as they are announced. "
                 f"Speakers from the 2025 edition are listed for reference.")
    else:
        intro = (f"The speaker line-up for {site['event_name']} ({site['event_dates_text']}, {site['venue']}, "
                 f"{site['city']}) is being announced. Below are the {n} government, enterprise and founder "
                 f"speakers who addressed the first edition in 2025. Confirmed 2026 speakers are marked as they are added.")
    sections, jumps = [], []
    for g in groups:
        members = [s for s in published if s["group"] == g["id"]]
        if not members:
            continue
        jumps.append(f'<a href="#{esc(g["id"])}">{esc(g["title"])}</a>')
        cards = []
        for s in members:
            tag = (f'<span class="tag confirmed">Confirmed 2026</span>' if s.get("confirmed_2026")
                   else ('<span class="tag">2025 speaker</span>' if "2025" in s.get("editions", []) else ""))
            cards.append(
                f'    <li>{photo_html(site, s, css_class="ph", size=64, lazy=True)}'
                f'<div><a href="{esc(speaker_url(site, s))}">{esc(s["name"])}</a>'
                f'<span class="role">{esc(s["title_role"])}</span>{tag}</div></li>')
        sections.append(f'  <section id="{esc(g["id"])}">\n    <h2>{esc(g["title"])}</h2>\n'
                        f'  <ul class="cards">\n' + "\n".join(cards) + "\n  </ul>\n  </section>")
    note = (f"Speaker names, roles and organisations are as at the time of announcement. "
            f"Session times and halls are confirmed on each speaker page and on the "
            f"<a href=\"{esc(common['agenda_url'])}\">agenda</a> once the programme is final. "
            f"Programme subject to change.")
    v = dict(common)
    v.update({
        "page_title": esc(title),
        "meta_description": esc(desc),
        "canonical_url": esc(url),
        "json_ld": dump_ld(index_ld(site, published, url, title)),
        "h1": f"Speakers, {esc(site['event_name'])}",
        "intro_text": esc(intro),
        "jump_links": "".join(jumps),
        "groups_html": "\n\n".join(sections),
        "note_text": note,
    })
    return tpl.safe_substitute(v), url, title, desc


def sitemap(urls, today):
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, priority in urls:
        lines.append(f"  <url><loc>{esc(u)}</loc><lastmod>{today}</lastmod><changefreq>weekly</changefreq>"
                     f"<priority>{priority}</priority></url>")
    lines.append("</urlset>")
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", default=str(ROOT / "speakers.json"))
    ap.add_argument("--out", default=str(ROOT / "dist"))
    ap.add_argument("--clean", action="store_true", help="delete the output folder first")
    ap.add_argument("--base-url", default=None,
                    help="override site.base_url, e.g. http://localhost:8000 for a local preview")
    ap.add_argument("--offline", action="store_true",
                    help="write flat files (index.html, <slug>.html) with relative links, for opening from a folder")
    args = ap.parse_args()

    data = json.loads(pathlib.Path(args.data).read_text(encoding="utf-8"))
    preview = None
    if args.base_url:
        preview = args.base_url.rstrip("/")
        data.setdefault("site", {})["base_url"] = preview
    errors, warnings = validate(data)
    if errors:
        print("ERRORS (nothing written):", file=sys.stderr)
        for e in errors:
            print("  - " + e, file=sys.stderr)
        sys.exit(1)

    site, groups = data["site"], data["groups"]
    order = {g["id"]: i for i, g in enumerate(groups)}
    speakers = data["speakers"]
    published = [s for s in speakers if s.get("publish", True)]
    published.sort(key=lambda s: (order[s["group"]], 0 if s.get("confirmed_2026") else 1))
    skipped = [s for s in speakers if not s.get("publish", True)]

    out = pathlib.Path(args.out)
    if args.clean and out.exists():
        shutil.rmtree(out)
    spk_dir = out if args.offline else out / site["speakers_path"].strip("/")
    spk_dir.mkdir(parents=True, exist_ok=True)

    def offline_links(page_html):
        """Rewrite links between the generated pages to relative file names."""
        if not args.offline:
            return page_html
        base = site["base_url"].rstrip("/") + "/" + site["speakers_path"].strip("/") + "/"
        page_html = re.sub(r'href="' + re.escape(base) + r'([a-z0-9-]+)/"', r'href="\1.html"', page_html)
        return page_html.replace(f'href="{base}"', 'href="index.html"')

    speaker_tpl = Template((ROOT / "templates" / "speaker.html").read_text(encoding="utf-8"))
    index_tpl = Template((ROOT / "templates" / "index.html").read_text(encoding="utf-8"))
    common = site_vars(site)
    today = dt.date.today().isoformat()

    rows, urls = [], []
    index_html, index_url, index_title, index_desc = render_index(index_tpl, site, groups, published, common)
    (spk_dir / "index.html").write_text(offline_links(index_html), encoding="utf-8")
    urls.append((index_url, "0.8"))

    for s in published:
        page, url, desc = render_speaker(speaker_tpl, site, s, published, common)
        if args.offline:
            target = spk_dir / f"{s['slug']}.html"
        else:
            d = spk_dir / s["slug"]
            d.mkdir(parents=True, exist_ok=True)
            target = d / "index.html"
        target.write_text(offline_links(page), encoding="utf-8")
        urls.append((url, "0.7" if s.get("confirmed_2026") else "0.6"))
        t = page_title(site, s)
        rows.append({
            "slug": s["slug"], "name": s["name"], "url": url, "title_len": len(t), "desc_len": len(desc),
            "bio": "yes" if s.get("bio") else "FALLBACK", "photo": "yes" if s.get("photo") else "none",
            "linkedin": "yes" if s.get("linkedin") else "none",
            "session": "yes" if (s.get("confirmed_2026") and s.get("session")) else "tba",
            "demand": s.get("search_demand_in"),
        })
        if len(t) > TITLE_MAX:
            warnings.append(f"{s['slug']}: title is {len(t)} characters (over {TITLE_MAX})")
        if len(desc) > DESC_MAX:
            warnings.append(f"{s['slug']}: meta description is {len(desc)} characters (over {DESC_MAX})")

    if not args.offline:
        (out / "sitemap-speakers.xml").write_text(sitemap(urls, today), encoding="utf-8")

    # Build report
    rep = [f"# Speaker pages build report ({today})", "",
           f"- Pages written: {len(published)} speaker pages + index -> `{spk_dir}`",
           (f"- Sitemap: `{out / 'sitemap-speakers.xml'}` ({len(urls)} URLs)" if not args.offline
            else "- Offline preview build: flat files, no sitemap"),
           f"- Skipped (publish=false): {len(skipped)}", ""]
    if skipped:
        rep.append("## Not published")
        for s in skipped:
            rep.append(f"- {s.get('name', s.get('slug'))}: {s.get('note', 'publish is false')}")
        rep.append("")
    rep.append("## Pages")
    rep.append("| Priority (India searches/mo) | Speaker | Bio | Photo | LinkedIn | Session | Title chars | Desc chars |")
    rep.append("|---:|---|---|---|---|---|---:|---:|")
    for r in sorted(rows, key=lambda r: -(r["demand"] or 0)):
        rep.append(f"| {r['demand'] if r['demand'] is not None else '-'} | [{r['name']}]({r['url']}) | {r['bio']} | "
                   f"{r['photo']} | {r['linkedin']} | {r['session']} | {r['title_len']} | {r['desc_len']} |")
    rep.append("")
    missing_bio = [r["name"] for r in rows if r["bio"] == "FALLBACK"]
    missing_photo = [r["name"] for r in rows if r["photo"] == "none"]
    rep.append("## To collect before or soon after publishing")
    rep.append(f"- Bios missing ({len(missing_bio)}): " + (", ".join(missing_bio) if missing_bio else "none"))
    rep.append(f"- Photos missing ({len(missing_photo)}): " + (", ".join(missing_photo) if missing_photo else "none"))
    rep.append("")
    if warnings:
        rep.append("## Warnings")
        rep.extend("- " + w for w in warnings)
        rep.append("")
    (out / "build-report.md").write_text("\n".join(rep), encoding="utf-8")

    print(f"Built {len(published)} speaker pages + index in {spk_dir}")
    if preview:
        print(f"PREVIEW BUILD: links, canonicals and sitemap point at {preview}. "
              f"Rebuild without --base-url before uploading to the live site.")
    if args.offline:
        print("OFFLINE PREVIEW: open index.html in this folder. Not for upload to the live site.")
    else:
        print(f"Sitemap: {out / 'sitemap-speakers.xml'}")
    print(f"Report:  {out / 'build-report.md'}")
    if skipped:
        print(f"Skipped {len(skipped)} (publish=false): " + ", ".join(s.get("name", "?") for s in skipped))
    if warnings:
        print(f"{len(warnings)} warning(s):")
        for w in warnings:
            print("  - " + w)


if __name__ == "__main__":
    main()
