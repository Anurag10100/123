# A68: World AI Awards 2026 winners page, link snippets, redirects and winner share-kit email

- **For recommendation:** Publish the World AI Awards 2026 winners page the night of the ceremony and send winners a share kit
- **Research lens:** event-week-postevent
- **Format:** Six paste-ready blocks: (1) a full static HTML page for /awards/winners-2026/index.html with scoped CSS and schema.org JSON-LD; (2) a Python snippet builder and the results-sheet CSV header; (3) internal-link snippets for /awards/, the homepage, the nav and sitemap.xml; (4) Apache .htaccess and nginx redirect rules; (5) the winner email, a variant for individual winners and a follow-up after 10 days; (6) notes on what the verifier corrections changed.
- **Placeholders the business must fill:**
  - PLACEHOLDER_CEREMONY_DATE (e.g. '14 October 2026'; ceremony date and time not yet confirmed on /awards/)
  - PLACEHOLDER_CURRENT_PASS_PRICE (number in INR for JSON-LD offers; Standard pricing ended 30 Sept 2026)
  - PLACEHOLDER_OG_IMAGE_URL (absolute 1200x630 image URL, used for og:image and Event image)
  - PLACEHOLDER_FORM_ENDPOINT (backend for the 2027 register-interest form)
  - PLACEHOLDER_CONSENT_LINE (data-use line and privacy policy link for the form)
  - PLACEHOLDER_CATEGORY_GROUP / PLACEHOLDER_CATEGORY (official 2026 category list, entered in the sheet before 12 Oct)
  - PLACEHOLDER_WINNER / PLACEHOLDER_PROJECT / PLACEHOLDER_CITY / PLACEHOLDER_PHOTO_FILE (from the official results sheet on the night, via build_winners.py)
  - PLACEHOLDER_JURY_NAME / PLACEHOLDER_JURY_DESIGNATION / PLACEHOLDER_JURY_ORGANISATION (official 2026 jury list)
  - PLACEHOLDER_BADGE_FILE (winner badge PNG)
  - PLACEHOLDER_SENDER_NAME / PLACEHOLDER_SENDER_TITLE (who signs the winner emails)
  - PLACEHOLDER_PUBLISH_DATE (sitemap lastmod, YYYY-MM-DD)
  - PLACEHOLDER_2026_FORM_CLOSE_DECISION (when to close or remove the 2026 nomination form on /awards/)

## How to ship

Owners: web dev builds the page and redirects, the awards team (Elets editorial) supplies the data and approves it, and marketing sends the emails.

By 12 Oct (template ready, NOT live):
1) Web dev: build /awards/winners-2026/index.html from block 1 on staging or locally. Do not upload it to the live site, so an empty winners page cannot be indexed or shared. Wrap it in the site's header and footer includes. Check at 375px width (the table turns into stacked cards with no horizontal scroll).
2) Awards team: create winners-2026.csv with the header in block 2, and enter category_group and category for every 2026 category from the official list. Also prepare the official jury list, the badge PNG, the photographer's shot list (one photo per winner) and the form endpoint. Test build_winners.py with 3 dummy rows.
3) Fill in all placeholders that are not decided on the night: PLACEHOLDER_CURRENT_PASS_PRICE (a number with no commas, e.g. 30000, or remove the "offers" price lines if no single price applies), PLACEHOLDER_OG_IMAGE_URL (1200x630 absolute URL), PLACEHOLDER_FORM_ENDPOINT, PLACEHOLDER_CONSENT_LINE, the category options in the select, and the jury entries. Paste the JSON-LD into validator.schema.org and Google's Rich Results Test (code mode). Any PLACEHOLDER_ left in a JSON value makes that field invalid.
4) In Search Console, add a www URL-prefix property or a Domain property (DNS). The current property covers only non-www, so it cannot inspect or report on the www winners URL.

Ceremony night (live by 23:00 IST):
5) As soon as the winners are announced, the awards team fills the winner columns. One named person checks every name, category and city against the official results sheet. Do not use memory or the LinkedIn post.
6) Run: python3 build_winners.py winners-2026.csv > winners-snippets.html. Paste section 1 into <tbody>, section 2 into .wn-photos and section 3 over the ItemList object in the @graph. Set PLACEHOLDER_CEREMONY_DATE in the meta description and intro (e.g. "14 October 2026"). Upload the page and photos, add the redirects (block 4), and add the /awards/ banner, homepage block, nav link and sitemap entry (block 3). Do not link from /agenda/ (Exa could not find it on www and GSC shows non-www returning 5xx). Re-run the Rich Results Test on the live URL and request indexing in the new www property.

Next day by 10:00 IST:
7) Marketing sends the block 5 email to each winner individually (mail merge from contact_name and contact_email), with the badge and that winner's photos attached.
8) After 10 days, send the follow-up to winners who have not published.

After the window (not urgent): add 2025 winners to /1st-edition/awards.html only from official internal records. The 2025 LinkedIn post shows only 5 winners, and the non-www archive URL is unknown to Google, so this gains nothing before 17 Oct.

Measure: GSC (www property) for 'world ai awards 2026 winners' and 'world ai awards'; analytics referrals from linkedin.com and lnkd.in to the winners URL; form submissions with source=winners-2026 or awards. Lead context for sales: the 2025 fee was INR 18,000 + GST (Startup & Individual) and INR 20,000 + GST (Enterprise, Government, Leadership, Solution Provider), per elets.net/worldaisummit-awards/. Do not state a 2027 fee until it is decided.

Sources checked now: venue address from the Google Hotels entry, Apple Maps and the Expedia listing via Exa (26/1, Dr Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru 560055), coordinates from Exa Places; /awards/ content (14-15 Oct, Sheraton Grand, 'Select Sectors' form, no ceremony time) from an Exa fetch on 1 Oct 2026; performer names from worldaisummit/speakers/speakers.json (confirmed_2026 true). No OpenSEO paid tools were used and no repository files were edited.

On the relayed question "do you have more CPUs from computer?": this cloud container shows 4 CPUs (nproc). It runs separately from your own computer and cannot borrow its CPUs.

## Content

=====================================================================
0. WHAT THE VERIFIER CORRECTIONS CHANGED (read before building)
=====================================================================
- No link from /agenda/. Exa found nothing at www /agenda/ (CRAWL_NOT_FOUND), and GSC shows non-www /agenda returning a 5xx error. The links go on /awards/, the homepage awards block and the main nav instead (block 3). Add an /agenda/ link only once that page works.
- The 2025 nomination fee had two tiers. Per elets.net/worldaisummit-awards/ (Exa, 1 Oct): INR 18,000 + GST per entry for Startup & Individual, and INR 20,000 + GST for Enterprise, Government, Leadership and Solution Provider. The page does NOT mention any 2027 fee. The interest form promises only to email categories, fee and deadline once nominations open.
- Winners do publish, but late. Qualitrix (AI Validation & Testing Excellence) put out a release on livemint24.com on 29 Oct 2025, 34 days after the ceremony. The share kit aims to bring that forward, and a follow-up email after 10 days is included. Expect most backlinks after the 14-17 Oct window.
- The ceremony date and time are unconfirmed (/awards/ shows only 14-15 Oct). They stay as PLACEHOLDER_CEREMONY_DATE. In 2025 the ceremony was on Day 1 evening (25 Sep 2025, per the LinkedIn post and the 24 Sep 2025 Elets release).
- The table may be large. The 1st-edition page lists about 120 categories. If 2026 is similar, enter category_group and category in the sheet BEFORE the ceremony, so that on the night only the winner, project and city columns need filling. block 2 then builds the rows, photos and JSON-LD.
- The 2025 archive (/1st-edition/awards.html) moves to after the window. Its non-www URL is "unknown to Google", so it gains nothing before 17 Oct. When it is done, copy only from the official internal 2025 results, never from memory.
- GSC covers only the non-www property ('world ai awards': 155 impressions over 16 months). It cannot inspect or measure the www winners URL, so add a www URL-prefix or Domain property before 12 Oct.
- The meta description is shortened from about 177 to about 158 characters, so Google does not cut it off.
- Venue address verified: 26/1, Dr Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru, Karnataka 560055 (Google Hotels listing, Apple Maps and Expedia via Exa, 1 Oct 2026). The geo coordinates (13.01247, 77.55484) come from Exa Places.
- Performers in the JSON-LD: six speakers marked confirmed_2026 in worldaisummit/speakers/speakers.json. Remove anyone who drops out. No bios are written.

=====================================================================
1. PAGE: /awards/winners-2026/index.html   (canonical https://www.worldaisummit.com/awards/winners-2026/)
=====================================================================
<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>World AI Awards 2026 Winners | World AI Summit, Bengaluru</title>
<meta name="description" content="World AI Awards 2026 winners, presented on PLACEHOLDER_CEREMONY_DATE at World AI Summit, Bengaluru: every category, winner and project. Organised by Elets Technomedia.">
<link rel="canonical" href="https://www.worldaisummit.com/awards/winners-2026/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="World AI Summit">
<meta property="og:title" content="World AI Awards 2026 Winners | World AI Summit, Bengaluru">
<meta property="og:description" content="Full list of World AI Awards 2026 winners: category, organisation, project and city. Presented at World AI Summit 2026, Bengaluru. Organised by Elets Technomedia.">
<meta property="og:url" content="https://www.worldaisummit.com/awards/winners-2026/">
<meta property="og:image" content="PLACEHOLDER_OG_IMAGE_URL">
<meta name="twitter:card" content="summary_large_image">
<!-- PASTE THE SITE'S USUAL <head> INCLUDES HERE (stylesheet, favicon, analytics) - same as /awards/ -->
<style>
.wn{max-width:1100px;margin:0 auto;padding:24px 16px 48px;line-height:1.6}
.wn-crumbs{font-size:.9rem;margin:0 0 12px}
.wn h1{margin:0 0 12px}
.wn h2{margin:40px 0 12px}
.wn-intro{font-size:1.1rem}
.wn-toc{display:flex;flex-wrap:wrap;gap:8px 20px;padding:0;margin:16px 0;list-style:none}
.wn-table{width:100%;border-collapse:collapse}
.wn-table caption{text-align:left;font-weight:600;padding:0 0 8px}
.wn-table th,.wn-table td{padding:10px 12px;border-bottom:1px solid #d9dce3;text-align:left;vertical-align:top}
.wn-table thead th{background:#f3f5f9}
.wn-jury{padding-left:20px}
.wn-photos{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px}
.wn-photos figure{margin:0}
.wn-photos img{width:100%;height:auto;display:block}
.wn-photos figcaption{font-size:.9rem;padding-top:6px}
.wn-cta{border:1px solid #d9dce3;border-radius:8px;padding:20px 16px;margin-top:40px}
.wn-cta form{display:grid;gap:8px;max-width:520px}
.wn-cta input,.wn-cta select{width:100%;box-sizing:border-box;padding:10px;font:inherit}
.wn-cta button{justify-self:start;padding:12px 18px;font:inherit}
.wn-small{font-size:.875rem}
@media (max-width:640px){
 .wn-table thead{position:absolute;left:-9999px}
 .wn-table tr{display:block;border-bottom:1px solid #d9dce3;padding:8px 0}
 .wn-table th,.wn-table td{display:block;border:0;padding:2px 0}
 .wn-table [data-label]::before{content:attr(data-label) ": ";font-weight:600}
}
</style>
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@graph": [
  {
   "@type": "WebPage",
   "@id": "https://www.worldaisummit.com/awards/winners-2026/#webpage",
   "url": "https://www.worldaisummit.com/awards/winners-2026/",
   "name": "World AI Awards 2026 Winners",
   "description": "World AI Awards 2026 winners, presented at World AI Summit 2026, Bengaluru: category, winner, project and city.",
   "inLanguage": "en-IN",
   "isPartOf": {"@id": "https://www.worldaisummit.com/#website"},
   "breadcrumb": {"@id": "https://www.worldaisummit.com/awards/winners-2026/#breadcrumb"},
   "about": {"@id": "https://www.worldaisummit.com/#event-2026"},
   "mainEntity": {"@id": "https://www.worldaisummit.com/awards/winners-2026/#winners"},
   "publisher": {"@id": "https://www.worldaisummit.com/#organizer"}
  },
  {
   "@type": "WebSite",
   "@id": "https://www.worldaisummit.com/#website",
   "url": "https://www.worldaisummit.com/",
   "name": "World AI Summit",
   "publisher": {"@id": "https://www.worldaisummit.com/#organizer"}
  },
  {
   "@type": "Organization",
   "@id": "https://www.worldaisummit.com/#organizer",
   "name": "Elets Technomedia",
   "url": "https://www.eletsonline.com/"
  },
  {
   "@type": "BreadcrumbList",
   "@id": "https://www.worldaisummit.com/awards/winners-2026/#breadcrumb",
   "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.worldaisummit.com/"},
    {"@type": "ListItem", "position": 2, "name": "World AI Awards", "item": "https://www.worldaisummit.com/awards/"},
    {"@type": "ListItem", "position": 3, "name": "2026 Winners", "item": "https://www.worldaisummit.com/awards/winners-2026/"}
   ]
  },
  {
   "@type": "Event",
   "@id": "https://www.worldaisummit.com/#event-2026",
   "name": "World AI Summit 2026",
   "url": "https://www.worldaisummit.com/",
   "description": "World AI Summit 2026, organised by Elets Technomedia at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru, on 14-15 October 2026. The World AI Awards 2026 are presented at the summit.",
   "startDate": "2026-10-14",
   "endDate": "2026-10-15",
   "eventStatus": "https://schema.org/EventScheduled",
   "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
   "image": ["PLACEHOLDER_OG_IMAGE_URL"],
   "location": {
    "@type": "Place",
    "name": "Sheraton Grand Bangalore Hotel at Brigade Gateway",
    "address": {
     "@type": "PostalAddress",
     "streetAddress": "26/1, Dr Rajkumar Road, Malleswaram-Rajajinagar",
     "addressLocality": "Bengaluru",
     "addressRegion": "Karnataka",
     "postalCode": "560055",
     "addressCountry": "IN"
    },
    "geo": {"@type": "GeoCoordinates", "latitude": 13.01247, "longitude": 77.55484}
   },
   "organizer": {"@id": "https://www.worldaisummit.com/#organizer"},
   "offers": {
    "@type": "Offer",
    "url": "https://www.worldaisummit.com/delegate/",
    "price": "PLACEHOLDER_CURRENT_PASS_PRICE",
    "priceCurrency": "INR",
    "availability": "https://schema.org/InStock"
   },
   "performer": [
    {"@type": "Person", "name": "Pankaj Kumar Pandey", "honorificSuffix": "IAS", "jobTitle": "Principal Secretary, e-Governance", "worksFor": {"@type": "GovernmentOrganization", "name": "Government of Karnataka"}},
    {"@type": "Person", "name": "T Bhoobalan", "honorificSuffix": "IAS", "jobTitle": "CEO, Centre for e-Governance", "worksFor": {"@type": "GovernmentOrganization", "name": "Government of Karnataka"}},
    {"@type": "Person", "name": "Sanjeev Gupta", "jobTitle": "CEO", "worksFor": {"@type": "Organization", "name": "Karnataka Digital Economy Mission"}},
    {"@type": "Person", "name": "Ram Mohan Rao", "jobTitle": "Executive Director", "worksFor": {"@type": "GovernmentOrganization", "name": "Securities and Exchange Board of India (SEBI)"}},
    {"@type": "Person", "name": "Sandeep Varaganti", "jobTitle": "CEO, JioMart", "worksFor": {"@type": "Organization", "name": "Reliance Retail"}},
    {"@type": "Person", "name": "Sandhya Vasudevan", "jobTitle": "Board Member", "worksFor": {"@type": "Organization", "name": "TiE Bangalore"}}
   ]
  },
  {
   "@type": "ItemList",
   "@id": "https://www.worldaisummit.com/awards/winners-2026/#winners",
   "name": "World AI Awards 2026 winners",
   "numberOfItems": 1,
   "itemListElement": [
    {"@type": "ListItem", "position": 1, "item": {"@type": "Organization", "name": "PLACEHOLDER_WINNER", "award": "World AI Awards 2026: PLACEHOLDER_CATEGORY", "address": {"@type": "PostalAddress", "addressLocality": "PLACEHOLDER_CITY"}}}
   ]
  }
 ]
}
</script>
</head>
<body>
<!-- PASTE SITE HEADER / NAV INCLUDE HERE (same as /awards/) -->
<main class="wn">
 <nav class="wn-crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/awards/">World AI Awards</a> / <span aria-current="page">2026 Winners</span></nav>

 <h1>World AI Awards 2026 Winners</h1>
 <p class="wn-intro">The World AI Awards 2026 were presented on PLACEHOLDER_CEREMONY_DATE at World AI Summit 2026, Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. Organised by Elets Technomedia.</p>
 <p>The table lists each award category with the winning organisation or person, the project recognised and its city. These are the World AI Awards presented at World AI Summit, Bengaluru; categories and nomination details are on the <a href="/awards/">World AI Awards page</a>.</p>

 <ul class="wn-toc" aria-label="On this page">
  <li><a href="#winners">Winners</a></li>
  <li><a href="#jury">Jury</a></li>
  <li><a href="#photos">Photos</a></li>
  <li><a href="#nominate-2027">World AI Awards 2027</a></li>
 </ul>

 <section id="winners" aria-labelledby="winners-h">
  <h2 id="winners-h">Winners by category</h2>
  <table class="wn-table">
   <caption>World AI Awards 2026 winners, World AI Summit 2026, Bengaluru</caption>
   <thead>
    <tr><th scope="col">Category group</th><th scope="col">Category</th><th scope="col">Winner</th><th scope="col">Project</th><th scope="col">City</th></tr>
   </thead>
   <tbody>
    <!-- Replace this example row with output section 1 of build_winners.py -->
    <tr><td data-label="Category group">PLACEHOLDER_CATEGORY_GROUP</td><th scope="row" data-label="Category">PLACEHOLDER_CATEGORY</th><td data-label="Winner">PLACEHOLDER_WINNER</td><td data-label="Project">PLACEHOLDER_PROJECT</td><td data-label="City">PLACEHOLDER_CITY</td></tr>
   </tbody>
  </table>
  <p class="wn-small">To report a spelling or detail error in this list, write to <a href="mailto:secretariat@worldaisummit.com">secretariat@worldaisummit.com</a>.</p>
 </section>

 <section id="jury" aria-labelledby="jury-h">
  <h2 id="jury-h">Jury</h2>
  <p>Jury for the World AI Awards 2026:</p>
  <ul class="wn-jury">
   <!-- One <li> per jury member, copied from the official 2026 jury list only -->
   <li><strong>PLACEHOLDER_JURY_NAME</strong>, PLACEHOLDER_JURY_DESIGNATION, PLACEHOLDER_JURY_ORGANISATION</li>
  </ul>
 </section>

 <section id="photos" aria-labelledby="photos-h">
  <h2 id="photos-h">Photos from the ceremony</h2>
  <div class="wn-photos">
   <!-- Replace with output section 2 of build_winners.py. Alt pattern: '[Org] receives [Category] at World AI Awards 2026, Bengaluru' -->
   <figure><img src="/awards/winners-2026/photos/PLACEHOLDER_PHOTO_FILE.jpg" width="1200" height="800" loading="lazy" decoding="async" alt="PLACEHOLDER_WINNER receives PLACEHOLDER_CATEGORY at World AI Awards 2026, Bengaluru"><figcaption>PLACEHOLDER_WINNER: PLACEHOLDER_CATEGORY</figcaption></figure>
  </div>
 </section>

 <section id="nominate-2027" class="wn-cta" aria-labelledby="cta-h">
  <h2 id="cta-h">World AI Awards 2027: register interest to nominate</h2>
  <p>Leave your details and we will email you when nominations for the World AI Awards 2027 open, with the categories, entry fee and deadline.</p>
  <form action="PLACEHOLDER_FORM_ENDPOINT" method="post">
   <input type="hidden" name="source" value="winners-2026">
   <label for="ri-name">Name</label>
   <input id="ri-name" name="name" autocomplete="name" required>
   <label for="ri-email">Work email</label>
   <input id="ri-email" name="email" type="email" autocomplete="email" required>
   <label for="ri-org">Organisation</label>
   <input id="ri-org" name="organisation" autocomplete="organization" required>
   <label for="ri-cat">Category of interest</label>
   <select id="ri-cat" name="category_interest" required>
    <option value="">Select a category group</option>
    <!-- One <option> per 2026 sector, copied from the 'Select Sectors' list on /awards/ -->
    <option>PLACEHOLDER_CATEGORY_GROUP</option>
    <option>Not sure yet</option>
   </select>
   <p class="wn-small">PLACEHOLDER_CONSENT_LINE (suggested: "We will use these details only to contact you about the World AI Awards." plus a link to the privacy policy)</p>
   <button type="submit">Register interest</button>
  </form>
  <p class="wn-small">To discuss partnering with the World AI Awards 2027, write to <a href="mailto:partnerships@worldaisummit.com">partnerships@worldaisummit.com</a>.</p>
 </section>

 <p><a href="/">World AI Summit 2026, 14-15 October, Bengaluru</a> | <a href="/awards/">About the World AI Awards</a> | <a href="/1st-edition/awards.html">Previous edition: categories and jury</a></p>
</main>
<!-- PASTE SITE FOOTER INCLUDE HERE -->
</body>
</html>

=====================================================================
2. SNIPPET BUILDER (run on the night; turns the results sheet into table rows, photos and JSON-LD)
=====================================================================
Results sheet: save it as winners-2026.csv (UTF-8) with this header row. Enter category_group and category for every 2026 category before 12 Oct. On the night, fill only winner_name, winner_type, winner_org, project, city and photo_file. contact_name and contact_email are for the email merge, and the script ignores them.

category_group,category,winner_name,winner_type,winner_org,project,city,photo_file,contact_name,contact_email

build_winners.py (Python 3, no dependencies; tested on sample rows that include quotes, & and <):

#!/usr/bin/env python3
"""Build winners-page snippets from the official results sheet.
Usage: python3 build_winners.py winners-2026.csv > winners-snippets.html
Columns: category_group,category,winner_name,winner_type,winner_org,project,city,photo_file
winner_type is Organization or Person. winner_org is used only for Person winners.
Rows with an empty winner_name are skipped. Extra columns (e.g. contact_email) are ignored."""
import csv, html, json, sys

PAGE = "https://www.worldaisummit.com/awards/winners-2026/"
def v(r, k): return (r.get(k) or "").strip()
def e(s): return html.escape(s)

with open(sys.argv[1], encoding="utf-8-sig", newline="") as f:
    rows = [r for r in csv.DictReader(f) if v(r, "winner_name")]

trs, figs, items = [], [], []
for i, r in enumerate(rows, 1):
    person = v(r, "winner_type").lower() == "person"
    name, cat, org = v(r, "winner_name"), v(r, "category"), v(r, "winner_org")
    shown = name + (", " + org if person and org else "")
    trs.append(
        f'<tr><td data-label="Category group">{e(v(r, "category_group"))}</td>'
        f'<th scope="row" data-label="Category">{e(cat)}</th>'
        f'<td data-label="Winner">{e(shown)}</td>'
        f'<td data-label="Project">{e(v(r, "project"))}</td>'
        f'<td data-label="City">{e(v(r, "city"))}</td></tr>')
    if v(r, "photo_file"):
        alt = f"{name} receives {cat} at World AI Awards 2026, Bengaluru"
        figs.append(
            f'<figure><img src="/awards/winners-2026/photos/{e(v(r, "photo_file"))}" width="1200" height="800" '
            f'loading="lazy" decoding="async" alt="{e(alt)}"><figcaption>{e(shown)}: {e(cat)}</figcaption></figure>')
    ent = {"@type": "Person" if person else "Organization", "name": name,
           "award": "World AI Awards 2026: " + cat}
    if person and org:
        ent["affiliation"] = {"@type": "Organization", "name": org}
    if v(r, "city"):
        ent["address"] = {"@type": "PostalAddress", "addressLocality": v(r, "city")}
    items.append({"@type": "ListItem", "position": i, "item": ent})

itemlist = {"@type": "ItemList", "@id": PAGE + "#winners", "name": "World AI Awards 2026 winners",
            "numberOfItems": len(items), "itemListElement": items}
print("<!-- 1. TBODY ROWS: replace the example row inside <tbody> -->\n" + "\n".join(trs))
print("\n<!-- 2. PHOTO FIGURES: replace the example figure inside .wn-photos -->\n" + "\n".join(figs))
print("\n<!-- 3. ITEMLIST: replace the ItemList object (last item of @graph) -->\n"
      + json.dumps(itemlist, ensure_ascii=False, indent=1).replace("</", "<\\/"))

Photos: export each photo as 1200x800 JPG, under about 200 KB, into /awards/winners-2026/photos/ with lowercase hyphenated names (e.g. org-name-category.jpg). If the photos have a different shape, change width and height in the script.

=====================================================================
3. INTERNAL LINKS (use absolute www URLs: /awards/ is indexed and ranks on non-www, so a relative link would add a redirect hop)
=====================================================================
3a. /awards/: add this banner at the top of <main>, above the 2026 nomination form:
<div class="wn-banner" role="note" style="border:1px solid #d9dce3;border-radius:8px;padding:12px 16px;margin:0 0 16px">
 <strong>World AI Awards 2026 winners announced.</strong>
 <a href="https://www.worldaisummit.com/awards/winners-2026/">See the full list of winners</a> |
 <a href="https://www.worldaisummit.com/awards/winners-2026/#nominate-2027">Register interest for 2027</a>
</div>
Also paste the whole <section id="nominate-2027">...</section> block from page 1 lower on /awards/, with the hidden field changed to value="awards". The decision on when to close or remove the 2026 nomination form is PLACEHOLDER_2026_FORM_CLOSE_DECISION.

3b. Homepage: place this in the awards block. If there is no awards block, put it after the agenda/sessions block:
<section class="home-awards">
 <h2>World AI Awards 2026</h2>
 <p>The World AI Awards 2026 were presented at World AI Summit 2026 in Bengaluru. <a href="https://www.worldaisummit.com/awards/winners-2026/">See the 2026 winners</a> or <a href="https://www.worldaisummit.com/awards/">read about the awards</a>.</p>
</section>

3c. Main navigation: add "Awards" linking to https://www.worldaisummit.com/awards/ (the crawl found /awards/ is not linked internally anywhere).

3d. sitemap.xml: add
<url><loc>https://www.worldaisummit.com/awards/winners-2026/</loc><lastmod>PLACEHOLDER_PUBLISH_DATE</lastmod></url>
(PLACEHOLDER_PUBLISH_DATE in YYYY-MM-DD form)

Do NOT link from /agenda/ until that page returns 200.

=====================================================================
4. REDIRECTS (add these on the ceremony night, at the same time as the page upload)
=====================================================================
4a. Apache: site-root .htaccess, near the top. These rules touch only this section.
RewriteEngine On

# 1. /awards/winners-2026/index.html -> folder URL (THE_REQUEST check avoids a loop with DirectoryIndex)
RewriteCond %{THE_REQUEST} \s/awards/winners-2026/index\.html[\s?] [NC]
RewriteRule ^ https://www.worldaisummit.com/awards/winners-2026/ [R=301,L]

# 2. Missing trailing slash -> trailing slash
RewriteRule ^awards/winners-2026$ https://www.worldaisummit.com/awards/winners-2026/ [R=301,L]

# 3. Non-www or http -> https://www (this section only)
RewriteCond %{HTTP_HOST} ^worldaisummit\.com$ [NC,OR]
RewriteCond %{HTTPS} !=on
RewriteRule ^awards/winners-2026/ https://www.worldaisummit.com%{REQUEST_URI} [R=301,L]

# 4. Short alias, 302 so it can point to the 2027 list next year
RewriteRule ^awards/winners/?$ https://www.worldaisummit.com/awards/winners-2026/ [R=302,L]

If TLS ends at a CDN or load balancer, change "%{HTTPS} !=on" to "%{HTTP:X-Forwarded-Proto} !https". If you are not sure, remove that one condition line (and the [OR] above it) to avoid a redirect loop.

4b. nginx
# In the www HTTPS server block (server_name www.worldaisummit.com):
if ($request_uri ~* "^/awards/winners-2026/index\.html(\?.*)?$") {
    return 301 https://www.worldaisummit.com/awards/winners-2026/;
}
location = /awards/winners-2026 { return 301 https://www.worldaisummit.com/awards/winners-2026/; }
location ~ ^/awards/winners/?$  { return 302 https://www.worldaisummit.com/awards/winners-2026/; }

# In the non-www server blocks (ports 80 and 443) and the www port-80 block,
# unless they already send everything to https://www:
location ^~ /awards/winners-2026 { return 301 https://www.worldaisummit.com$request_uri; }

Test after deploy: curl -sI https://worldaisummit.com/awards/winners-2026/ and curl -sI https://www.worldaisummit.com/awards/winners-2026/index.html should each return a single 301 to https://www.worldaisummit.com/awards/winners-2026/, and the final URL should return 200.

=====================================================================
5. WINNER EMAIL (send by 10:00 IST the day after the ceremony, one email per winner, never CC'd together)
=====================================================================
Subject: Your World AI Awards 2026 win: official badge and winners' page

Dear [First name],

Congratulations on winning [Category] at the World AI Awards 2026, presented on PLACEHOLDER_CEREMONY_DATE at World AI Summit 2026 in Bengaluru.

The official winners' list is live at https://www.worldaisummit.com/awards/winners-2026/

Attached:
- Winner badge (PNG): PLACEHOLDER_BADGE_FILE
- Stage photos from the ceremony

Suggested line for your newsroom or press release:
"[Org] won the [Category] award at the World AI Awards 2026, presented at World AI Summit 2026 in Bengaluru (14-15 October 2026), organised by Elets Technomedia."
Please link the words "World AI Awards 2026" to https://www.worldaisummit.com/awards/winners-2026/ so readers can see the full list.

Suggested LinkedIn caption:
"Honoured to receive [Category] at the World AI Awards 2026 at World AI Summit, Bengaluru. Full winners list: https://www.worldaisummit.com/awards/winners-2026/ @World AI Summit"
(When you post, type @World AI Summit and choose the World AI Summit page from the list so the tag links.)

If your organisation name, project title or city needs a correction on the winners' page, reply to this email and we will update it.

Warm regards,
PLACEHOLDER_SENDER_NAME
PLACEHOLDER_SENDER_TITLE, World AI Awards team, Elets Technomedia
secretariat@worldaisummit.com

Variant for individual awards: replace [Org] in the newsroom line with "[Name], [Designation] at [Org]," and start the LinkedIn caption with "Honoured to receive [Category] at the World AI Awards 2026 ...". The rest stays the same.

Follow-up after 10 days (only to winners who have not published; 2025 winners such as Qualitrix published about 34 days after the ceremony):
Subject: World AI Awards 2026: winners' page link for your announcement

Dear [First name],

In case it is useful for your announcement or newsroom page, the official list of World AI Awards 2026 winners, including [Org] for [Category], is at https://www.worldaisummit.com/awards/winners-2026/. The suggested line and badge from our earlier email are attached again. If you have already published, please reply with the link so we have it on record.

Warm regards,
PLACEHOLDER_SENDER_NAME
World AI Awards team, Elets Technomedia
