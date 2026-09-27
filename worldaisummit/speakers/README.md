# Speaker profile pages for worldaisummit.com

One static page per speaker (role, bio, session, time, hall) plus a speaker
directory, generated from a single data file. This is the page type that
brings Cypher most of its search traffic: people search a speaker's name, and
the event's speaker page ranks for it. Build the pages before each speaker
announcement so they exist when the searches start.

## Files

| Path | What it is |
|---|---|
| `speakers.json` | The only file you edit: event details, groups and one record per speaker |
| `templates/speaker.html` | Page template for a speaker (placeholders are `$name`, `$bio_html`, ...) |
| `templates/index.html` | Template for the `/speakers/` directory page |
| `build_speakers.py` | Generator. Python 3.8+, no packages to install |
| `dist/speakers/index.html` | Generated directory page, government names first |
| `dist/speakers/<slug>/index.html` | Generated speaker pages |
| `dist/sitemap-speakers.xml` | Sitemap for the pages above |
| `dist/build-report.md` | What was built, what is missing (bios, photos), warnings |

## Build

```bash
cd worldaisummit/speakers
python3 build_speakers.py --clean
```

The build stops with a message if a required field is empty, a slug is
duplicated or malformed, or a group id is unknown. Warnings (missing photo,
confirmed speaker without a session) are printed and written to
`dist/build-report.md`.

## Preview on your own computer

```bash
git fetch origin claude/openseo-agent-setup-qjooi1
git checkout claude/openseo-agent-setup-qjooi1
cd worldaisummit/speakers
python3 build_speakers.py --clean --base-url http://localhost:8000
python3 -m http.server 8000 --directory dist
```

Then open <http://localhost:8000/speakers/> in a browser. The `--base-url`
flag makes every link, canonical and sitemap entry point at your machine.
Rebuild without it before uploading to the live site. On Windows use `python`
instead of `python3`. Without git, download the branch as a ZIP from GitHub
(Code -> Download ZIP on the branch) and run the same two commands.

## Adding or updating a speaker

Add an object to the `speakers` array in `speakers.json`:

```json
{
  "slug": "firstname-lastname",
  "name": "Firstname Lastname, IAS",
  "honorific": "Shri",
  "role": "Principal Secretary, Department of Electronics, IT and Biotechnology",
  "title_role": "Principal Secretary, IT/BT, Karnataka",
  "org": "Government of Karnataka",
  "group": "government",
  "editions": ["2025", "2026"],
  "role_2025": "Panelist",
  "confirmed_2026": true,
  "session": {
    "title": "Karnataka's AI roadmap for public services",
    "date": "2026-10-14",
    "time": "11:15-12:00 IST",
    "hall": "Grand Ballroom",
    "format": "Panel",
    "track": "AI in governance"
  },
  "bio": "Two or three factual paragraphs, separated by a blank line.",
  "photo": "/wp-content/uploads/2026/10/firstname-lastname.jpg",
  "linkedin": "https://www.linkedin.com/in/...",
  "search_demand_in": 320,
  "publish": true
}
```

Field notes:

- `slug` is the URL: `/speakers/<slug>/`. Lowercase letters, digits and hyphens.
  Never change a slug once the page is live; add a redirect instead.
- `name` is the searchable name as people type it, with service suffix if the
  speaker uses it (`, IAS`). The suffix is moved to `honorificSuffix` in the
  structured data automatically.
- `role` is the full designation shown on the page. `title_role` is the short
  form used in the page title, cards and meta description (about 40 characters).
- `group` must be one of the ids in `groups`. Groups are printed in the order
  listed in the file. Government stays first.
- `editions` lists the years the person spoke. `role_2025` is optional
  (`Chief Guest`, `Keynote`, `Panelist`).
- `confirmed_2026` switches the page from "spoke in 2025, 2026 line-up being
  announced" to "confirmed speaker" and adds the Event to the structured data.
  Set it only after the speaker has confirmed.
- `session` is shown only when `confirmed_2026` is true. Every key is optional;
  `date` must be `YYYY-MM-DD` inside the event dates. Fill in `time` and `hall`
  as soon as the agenda is fixed; the page says "to be announced" until then.
- `bio` comes from the speaker or their office. Leave it empty rather than
  writing one: the page then shows a one-sentence factual line built from
  `role`, `org` and `editions`. Never invent biographical claims.
- `photo` is the path on the live site (or a full URL). Upload a square image,
  at least 600 x 600 px, JPG, under 150 KB, named after the slug. Drop a copy in
  `photos/` (git-ignored, optional) to silence the "not found" warning.
- `search_demand_in` is the India Google search volume for the name from the
  OpenSEO research (September 2026). It only orders the build report.
- `publish: false` keeps a record without generating a page (for example when
  the organisation still needs confirming). Add a `note` saying why.

Then run the build and upload the changed folders.

## Deploying to the live site

The pages are plain HTML with inline CSS and no scripts, so they run on any
host. On the WordPress site:

1. Upload `dist/speakers/` to the site root so that
   `https://www.worldaisummit.com/speakers/` and
   `https://www.worldaisummit.com/speakers/<slug>/` resolve. A real folder with
   an `index.html` is served before WordPress rewrites, so no plugin is needed.
   If the theme already owns `/speakers/`, either replace that page with the
   generated one or change `site.speakers_path` in `speakers.json` (for example
   `/speaker/`) and rebuild.
2. Upload `dist/sitemap-speakers.xml` to the site root and add it to the
   sitemap index (Yoast / Rank Math: add it as an extra sitemap, or list it in
   `robots.txt` as `Sitemap: https://www.worldaisummit.com/sitemap-speakers.xml`).
3. Add a "Speakers" link in the main navigation and on the homepage pointing to
   `/speakers/`, so the pages are not orphaned (the audit found `/delegate/`
   orphaned for the same reason).
4. Submit `/speakers/` in Google Search Console (URL inspection, request
   indexing) after the first upload, and again for the top names when they are
   confirmed for 2026.
5. Re-run the build and re-upload whenever `speakers.json` changes. Pages are
   idempotent: uploading the whole folder again is safe.

To match the site's own header and footer, edit the two templates (keep the
`$placeholders`) or paste the `<main>` block of each generated page into a
WordPress page template. Keep the `<head>` content as generated: title,
description, canonical and the JSON-LD block are what the pages rank with.

## SEO rules baked into the pages

- Title: `Name | Short role | World AI Summit 2026` (shortened automatically to
  stay under 70 characters). Name first because the name is the query.
- H1 is the name only. Role and organisation follow in the hero.
- Meta description: name, role, 2025/2026 relationship, dates, city and pass
  price, under 160 characters.
- Canonical URL, Open Graph and Twitter tags, `robots: index, follow`.
- JSON-LD: `ProfilePage` with `Person` (jobTitle, worksFor, image, sameAs,
  honorifics) and `BreadcrumbList`; when confirmed for 2026, `performerIn`
  carries the `Event` (dates, venue, organiser, ticket offer) and the session
  as a `subEvent` with hall.
- Every page links to the directory, the agenda, the delegate page and six
  other speakers (same group first), so link equity flows to the pass page.
- The directory page lists government names first and marks each card
  "2025 speaker" or "Confirmed 2026".
- Nothing external is loaded: no fonts, scripts or tracking. Add the site's
  analytics snippet in the template if needed.

## What is published now

Only the 50 speakers announced for 2026 are published (`publish: true`).
The 24 speakers from the 2025 edition stay in `speakers.json` with
`publish: false`; flip the flag to publish any of them (Priyank Kharge's page
alone targets 49,500 searches a month and Cypher ranks for that name with a
speaker page).

Every published page has a researched bio (LinkedIn, the organisation's own
site, press coverage; sources are kept in `bio_sources` per speaker) and a
short "About the organisation" box. Bios contain only facts found in those
sources. Read `bio_notes` before publishing: they flag stale titles on the
event site (for example Sushan Rungta's LinkedIn shows the Absolute CTO role
ending in February 2026) and spelling differences (Rajesh Choudhary, as on
CSB Bank's site, not Chaudhary).

## Priority order (India searches per month for the name, September 2026)

Get photos for these first. Names marked "shared" are common names where most
of the volume is for other people, so treat them as unproven.

| Speaker | Searches/mo | Notes |
|---|---:|---|
| Aman Mittal, IAS | 480 | |
| Ram Mohan Rao | 480 | shared |
| Dipayan Chakraborty | 390 | |
| Archana Menon | 390 | |
| Pankaj Kumar Pandey, IAS | 320 | |
| Sandeep Varaganti | 210 | |
| Avinash Naik | 210 | |
| Shashank Randev | 90 | |
| T Bhoobalan, IAS | 30 | |
| Sandeep Sharma, Harsh Vardhan, Deepak Sharma, Shalini Kapoor, Vishal Chugh, Ganesh Joshi, Sanjeev Gupta, Rajesh Choudhary, Anand Thakur | 590 to 74,000 | shared names; volume mostly for other people |

Dr Ravikumar Surpur is published with "Government of Rajasthan" as
organisation, confirmed by the Rajasthan DoIT&C page cited in his sources.

## Before the 2026 announcements

1. Collect bios (16 missing) and photos (all 28 missing) from speakers' offices.
2. As each 2026 speaker confirms: set `confirmed_2026: true`, add the session
   once known, rebuild, upload, request indexing.
3. Announce on LinkedIn and in the newsletter with a link to the speaker page,
   not the homepage: that link is what earns the page its first backlinks.
