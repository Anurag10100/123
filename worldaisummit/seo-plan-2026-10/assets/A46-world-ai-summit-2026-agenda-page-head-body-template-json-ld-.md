# A46: World AI Summit 2026 /agenda/ page: head, body template, JSON-LD, internal links, redirects (v1 for 2 Oct)

- **For recommendation:** Publish a 2026 /agenda/ page with Event subEvent markup and link every session to speaker pages and /delegate/
- **Research lens:** news-content
- **Format:** HTML (head + body + JSON-LD) with Apache .htaccess, nginx and sitemap snippets
- **Placeholders the business must fill:**
  - PLACEHOLDER_LAST_UPDATED_ISO / PLACEHOLDER_LAST_UPDATED_DISPLAY: date of each update, for example 2026-10-02 / 2 October 2026
  - PLACEHOLDER_SESSION_ID: short unique row ID per session, for example 01, 02
  - PLACEHOLDER_START / PLACEHOLDER_END: confirmed session times in HH:MM IST (programme team)
  - PLACEHOLDER_HALL: confirmed hall name at the Sheraton (programme team; final by 13 Oct)
  - PLACEHOLDER_SESSION_TITLE: approved session title (programme team)
  - PLACEHOLDER_TRACK_ID / PLACEHOLDER_TRACK_NAME: one of the seven tracks and its anchor ID
  - PLACEHOLDER_FORMAT: Keynote / Panel / Fireside / Masterclass
  - PLACEHOLDER_CONFIRMED_SPEAKER / PLACEHOLDER_SPEAKER_SLUG / PLACEHOLDER_SPEAKER_TITLE_ROLE: only speakers with confirmed_2026 = true who are confirmed for that session; copy name, slug and title_role from speakers.json
  - PLACEHOLDER_CURRENT_PASS_PRICE: reconciled live delegate pass price; add it to the Offer and to speakers.json pass_price_inr only once /delegate/ and the homepage agree

## How to ship

Expectations first. The verifier found almost no search demand: Search Console has no "world ai summit" plus "agenda" or "schedule" queries, and the homepage already ranks #3 for "world ai summit 2026 agenda" and #1 for "world ai summit bengaluru agenda". Treat this page mainly as a conversion page for people about to buy a pass, not as a source of new traffic.

v1 by 2 Oct:
1. Web dev creates /agenda/index.html from sections 1 and 2 using the site's normal header and footer. That is about 3 hours.
2. If the programme team has not approved any session yet, ship with the "will be published here as they are confirmed" row in all four half-day tables and no subEvent. The JSON-LD in section 1 is valid as it stands.
3. Add the redirects (section 6), the sitemap entry (section 7) and the internal links (section 5). The nav link and the /1st-edition banner are the priority.
4. In Search Console, add a Domain property (DNS TXT) or a https://www.worldaisummit.com/ URL-prefix property. The only verified property today is the non-www one, which cannot inspect www URLs. Then use URL Inspection on https://www.worldaisummit.com/agenda/, request indexing and resubmit the sitemap.
5. Run the page through the Rich Results Test before it goes live.

Daily until 13 Oct:
- The Elets programme team approves sessions. The 2025 draft agenda was public about three months before the event, so a draft probably exists and approval is the bottleneck.
- For each approved session, the web dev adds a table row with a data-track ID matching one of the seven anchors, a subEvent (section 3) and the speakers.json session block (section 4).
- Then rebuild the speaker pages, update dateModified, the lastmod and the "Last updated" line.
- Speaker links to /speakers/<slug>/ go live only after the speaker generator is deployed. Until then, link names to /speaker.html or leave them as plain text, and leave Person url and @id out of the JSON-LD.
- Final version with every hall: 13 Oct.

Do not:
- Name any speaker who is not confirmed for a session.
- Write bios on this page.
- Add a price to the Offer before /delegate/ and the homepage show the same live tier.
- Add a second Event with a different name, dates or url from the homepage's.

Owners: web dev for the build, Elets programme team for session data, and whoever owns pricing for PLACEHOLDER_CURRENT_PASS_PRICE.

On your question about CPUs: this session's sandbox shows 4 CPUs (nproc). I cannot add more from inside the session.

## Content

=====================================================================
0. CORRECTIONS ALREADY APPLIED IN THIS ASSET
=====================================================================
- Title is 50 characters, not 49.
- The meta description is cut from 161 to 151 characters.
- The event is called the "second edition". The LinkedIn showcase says "2nd Edition of World AI Summit, 14-15 October 2026", and 2025 was the inaugural edition.
- The Offer has no price. /delegate/ and the homepage disagree on pricing (Standard tier ended 30 Sep 2026, homepage still shows Premium Rs 20,000). Once pricing is fixed, add "price": "PLACEHOLDER_CURRENT_PASS_PRICE" and "priceCurrency": "INR".
- The page adds no second Event that could conflict with the homepage's. It reuses one Event @id (https://www.worldaisummit.com/#event) with url = the homepage, as the speaker generator already does (build_speakers.py event_ld url = base + "/").
- The page has no subEvent and names no speaker in a session until that session is confirmed. On 1 Oct, all 76 records in speakers.json have session = null.
- The street address comes from the Marriott listing and other search results: 26/1 Dr. Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru, Karnataka 560055 (https://www.marriott.com/en-us/hotels/blrgs-sheraton-grand-bangalore-hotel-at-brigade-gateway/overview/ ; https://www.hotelplanner.com/Hotels/178731/Reservations-Sheraton-Bangalore-Hotel-at-Brigade-Gateway-Bangalore-26-1-Dr-Rajkumar-Rd-Malleswaram-Rajajinagar-560055).
- Track names and the pass inclusions ("Full Summit access", "Delegate kit + lunch & refreshments", "Certification of participation", "Group booking 3+ delegates 10% off") are copied from the live homepage, read via Exa on 1 Oct 2026.

=====================================================================
1. <head> FOR /agenda/index.html
=====================================================================
<title>World AI Summit 2026 Agenda | 14–15 Oct, Bengaluru</title>
<meta name="description" content="Day-wise agenda for World AI Summit 2026 at Sheraton Grand Bangalore, 14–15 Oct: sessions, halls and speakers in seven tracks. Book your delegate pass.">
<link rel="canonical" href="https://www.worldaisummit.com/agenda/">
<meta name="robots" content="index, follow, max-snippet:-1">
<meta property="og:type" content="website">
<meta property="og:title" content="World AI Summit 2026 Agenda | 14–15 Oct, Bengaluru">
<meta property="og:description" content="Sessions, halls and speakers for World AI Summit 2026, 14–15 October, Sheraton Grand Bangalore Hotel at Brigade Gateway.">
<meta property="og:url" content="https://www.worldaisummit.com/agenda/">
<meta name="twitter:card" content="summary_large_image">

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://www.worldaisummit.com/agenda/#webpage",
      "url": "https://www.worldaisummit.com/agenda/",
      "name": "World AI Summit 2026 Agenda",
      "inLanguage": "en-IN",
      "description": "Day-wise agenda for World AI Summit 2026 at Sheraton Grand Bangalore, 14–15 Oct: sessions, halls and speakers in seven tracks. Book your delegate pass.",
      "dateModified": "2026-10-02",
      "isPartOf": { "@type": "WebSite", "name": "World AI Summit", "url": "https://www.worldaisummit.com/" },
      "about": { "@id": "https://www.worldaisummit.com/#event" },
      "breadcrumb": {
        "@type": "BreadcrumbList",
        "itemListElement": [
          { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.worldaisummit.com/" },
          { "@type": "ListItem", "position": 2, "name": "Agenda", "item": "https://www.worldaisummit.com/agenda/" }
        ]
      }
    },
    {
      "@type": "Event",
      "@id": "https://www.worldaisummit.com/#event",
      "name": "World AI Summit 2026",
      "description": "Two-day conference on artificial intelligence in Bengaluru, organised by Elets Technomedia, with sessions across seven tracks.",
      "url": "https://www.worldaisummit.com/",
      "startDate": "2026-10-14",
      "endDate": "2026-10-15",
      "eventStatus": "https://schema.org/EventScheduled",
      "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
      "location": {
        "@type": "Place",
        "name": "Sheraton Grand Bangalore Hotel at Brigade Gateway",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "26/1 Dr. Rajkumar Road, Malleswaram-Rajajinagar",
          "addressLocality": "Bengaluru",
          "addressRegion": "Karnataka",
          "postalCode": "560055",
          "addressCountry": "IN"
        }
      },
      "organizer": { "@type": "Organization", "name": "Elets Technomedia", "url": "https://www.worldaisummit.com/" },
      "offers": {
        "@type": "Offer",
        "url": "https://www.worldaisummit.com/delegate/",
        "availability": "https://schema.org/InStock"
      }
    }
  ]
}
</script>
<!-- The block above was checked as valid JSON on 1 Oct and is ready to ship as is.
     If the homepage already has an Event block, give it the same "@id": "https://www.worldaisummit.com/#event"
     and the same name, dates and location, so Google sees one event.
     When you add sessions, add a "subEvent" array to the Event object above (see section 3). -->

=====================================================================
2. <body> CONTENT
=====================================================================
<main id="agenda">
  <nav aria-label="Breadcrumb" class="crumbs"><a href="/">Home</a> / Agenda</nav>

  <h1>World AI Summit 2026 Agenda</h1>
  <p class="lede">Wednesday 14 and Thursday 15 October 2026, Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. This is the second edition of the World AI Summit, organised by Elets Technomedia. It runs over two days and seven tracks.</p>
  <p class="status">The programme is being finalised. Each session appears below once confirmed, with time, hall, format and speakers. Last updated: <time datetime="PLACEHOLDER_LAST_UPDATED_ISO">PLACEHOLDER_LAST_UPDATED_DISPLAY</time>.</p>
  <p class="actions">
    <a class="btn btn-primary" href="/delegate/">Book your delegate pass</a>
    <a class="btn" href="/speaker.html">See confirmed speakers</a>
  </p>

  <section id="tracks" aria-labelledby="tracks-h">
    <h2 id="tracks-h">Seven tracks</h2>
    <p>Select a track to show only its sessions. <a href="#agenda" data-track-reset>Show all sessions</a></p>
    <ul class="track-list">
      <li id="frontier-models-compute"><a href="#frontier-models-compute"><strong>Frontier Models &amp; Compute</strong></a>: breakthroughs in frontier AI models, advanced computing and the infrastructure powering next-generation AI.</li>
      <li id="sovereign-ai"><a href="#sovereign-ai"><strong>Sovereign AI &amp; Geopolitics</strong></a>: AI sovereignty, national capabilities, data security and the evolving global AI landscape.</li>
      <li id="enterprise-ai"><a href="#enterprise-ai"><strong>Enterprise AI in Production</strong></a>: how enterprises deploy AI at scale for efficiency and business transformation.</li>
      <li id="gcc"><a href="#gcc"><strong>Global Capability Centres (GCCs)</strong></a>: how GCCs drive AI innovation, talent development, R&amp;D and global technology leadership.</li>
      <li id="robotics-agents"><a href="#robotics-agents"><strong>Robotics, Agents &amp; Embodied AI</strong></a>: advances in AI agents, robotics and autonomous systems in real-world use.</li>
      <li id="ai-for-bharat"><a href="#ai-for-bharat"><strong>AI for Bharat</strong></a>: AI for inclusive growth across governance, healthcare, education, agriculture and public services.</li>
      <li id="capital-founders-exits"><a href="#capital-founders-exits"><strong>Capital, Founders &amp; Exits</strong></a>: AI startup funding, investment trends, scaling and pathways to exits.</li>
    </ul>
  </section>

  <!-- ===================== DAY 1 ===================== -->
  <section id="day-1" aria-labelledby="day-1-h">
    <h2 id="day-1-h">Day 1: Wednesday, 14 October 2026</h2>

    <h3 id="day-1-morning">Morning</h3>
    <div class="table-wrap">
    <table class="agenda-table">
      <caption>Day 1 morning sessions, 14 October 2026 (times in IST)</caption>
      <thead><tr><th scope="col">Time (IST)</th><th scope="col">Hall</th><th scope="col">Session</th><th scope="col">Track</th><th scope="col">Format</th><th scope="col">Speakers</th></tr></thead>
      <tbody>
        <!-- ROW TEMPLATE: copy one row per CONFIRMED session. Delete any row that is not confirmed. Never list an unconfirmed speaker. -->
        <tr id="d1-PLACEHOLDER_SESSION_ID" data-track="PLACEHOLDER_TRACK_ID">
          <td><time datetime="2026-10-14TPLACEHOLDER_START+05:30">PLACEHOLDER_START</time>–<time datetime="2026-10-14TPLACEHOLDER_END+05:30">PLACEHOLDER_END</time></td>
          <td>PLACEHOLDER_HALL</td>
          <td>PLACEHOLDER_SESSION_TITLE</td>
          <td><a href="#PLACEHOLDER_TRACK_ID">PLACEHOLDER_TRACK_NAME</a></td>
          <td>PLACEHOLDER_FORMAT <!-- Keynote / Panel / Fireside / Masterclass --></td>
          <td><a href="/speakers/PLACEHOLDER_SPEAKER_SLUG/">PLACEHOLDER_CONFIRMED_SPEAKER</a>, PLACEHOLDER_SPEAKER_TITLE_ROLE</td>
        </tr>
        <!-- If this half-day has no confirmed sessions yet, use this row only: -->
        <tr class="tba"><td colspan="6">Sessions for this half-day will be published here as they are confirmed.</td></tr>
      </tbody>
    </table>
    </div>
    <aside class="cta">
      <p>Every delegate pass covers full summit access, the delegate kit, lunch and refreshments, and a certificate of participation. Groups of three or more delegates get 10% off.</p>
      <a class="btn btn-primary" href="/delegate/">Book your delegate pass</a>
      <a href="mailto:partnerships@worldaisummit.com?subject=Sponsor%20a%20session%20-%20World%20AI%20Summit%202026">Sponsor a session</a>
    </aside>

    <h3 id="day-1-afternoon">Afternoon</h3>
    <!-- Same table as the morning, caption "Day 1 afternoon sessions, 14 October 2026 (times in IST)", dates 2026-10-14 -->
    <!-- Same CTA aside after it -->
  </section>

  <!-- ===================== DAY 2 ===================== -->
  <section id="day-2" aria-labelledby="day-2-h">
    <h2 id="day-2-h">Day 2: Thursday, 15 October 2026</h2>
    <h3 id="day-2-morning">Morning</h3>
    <!-- Same table, caption "Day 2 morning sessions, 15 October 2026 (times in IST)", every datetime 2026-10-15T..+05:30 -->
    <!-- CTA aside -->
    <h3 id="day-2-afternoon">Afternoon</h3>
    <!-- Same table, caption "Day 2 afternoon sessions, 15 October 2026 (times in IST)" -->
    <!-- CTA aside -->
  </section>

  <section id="venue" aria-labelledby="venue-h">
    <h2 id="venue-h">Venue</h2>
    <p>Sheraton Grand Bangalore Hotel at Brigade Gateway, 26/1 Dr. Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru, Karnataka 560055.</p>
  </section>

  <section id="contact" aria-labelledby="contact-h">
    <h2 id="contact-h">Questions about the programme</h2>
    <ul>
      <li>Delegate passes and group bookings: <a href="mailto:registration@worldaisummit.com">registration@worldaisummit.com</a></li>
      <li>Sponsoring a session or exhibiting: <a href="mailto:partnerships@worldaisummit.com">partnerships@worldaisummit.com</a></li>
      <li>Other enquiries: <a href="mailto:secretariat@worldaisummit.com">secretariat@worldaisummit.com</a></li>
    </ul>
    <p>Looking for last year's programme? See the <a href="/1st-edition/world-ai-agenda.html">World AI Summit 2025 agenda</a>.</p>
  </section>
</main>

<!-- Track filter, vanilla JS, no dependency. Rows carry data-track. -->
<script>
(function () {
  var ids = ["frontier-models-compute","sovereign-ai","enterprise-ai","gcc","robotics-agents","ai-for-bharat","capital-founders-exits"];
  function apply() {
    var t = location.hash.slice(1);
    var on = ids.indexOf(t) !== -1;
    document.querySelectorAll(".agenda-table tbody tr[data-track]").forEach(function (r) {
      r.hidden = on && r.getAttribute("data-track") !== t;
    });
  }
  window.addEventListener("hashchange", apply);
  apply();
})();
</script>

<style>
.table-wrap{overflow-x:auto;-webkit-overflow-scrolling:touch}
.agenda-table{width:100%;border-collapse:collapse;min-width:640px}
.agenda-table th,.agenda-table td{padding:.6rem .75rem;border-bottom:1px solid #e3e3e3;text-align:left;vertical-align:top}
.agenda-table caption{text-align:left;font-weight:600;padding:.5rem 0}
.cta{margin:1.25rem 0 2rem;padding:1rem;border:1px solid #e3e3e3;border-radius:8px}
</style>

=====================================================================
3. subEvent TEMPLATE (add to the Event object in section 1 only for CONFIRMED sessions)
=====================================================================
"subEvent": [
  {
    "@type": "Event",
    "name": "PLACEHOLDER_SESSION_TITLE",
    "startDate": "2026-10-14TPLACEHOLDER_START:00+05:30",
    "endDate": "2026-10-14TPLACEHOLDER_END:00+05:30",
    "eventStatus": "https://schema.org/EventScheduled",
    "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
    "url": "https://www.worldaisummit.com/agenda/#d1-PLACEHOLDER_SESSION_ID",
    "location": {
      "@type": "Place",
      "name": "PLACEHOLDER_HALL, Sheraton Grand Bangalore Hotel at Brigade Gateway",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "26/1 Dr. Rajkumar Road, Malleswaram-Rajajinagar",
        "addressLocality": "Bengaluru",
        "addressRegion": "Karnataka",
        "postalCode": "560055",
        "addressCountry": "IN"
      }
    },
    "performer": [
      {
        "@type": "Person",
        "@id": "https://www.worldaisummit.com/speakers/PLACEHOLDER_SPEAKER_SLUG/#person",
        "name": "PLACEHOLDER_CONFIRMED_SPEAKER",
        "url": "https://www.worldaisummit.com/speakers/PLACEHOLDER_SPEAKER_SLUG/"
      }
    ]
  }
]
Rules for this block:
- The performer must be a speaker with confirmed_2026 = true in worldaisummit/speakers/speakers.json who is named for that session. Copy the slug exactly from the data file, for example "sanjeev-rastogi".
- Leave out "url" and "@id" on the Person until /speakers/<slug>/ is live. Those pages are not deployed yet and would return 404.
- Day 2 sessions use 2026-10-15.
- If a session has no confirmed time, leave the whole subEvent out. Do not guess a time.
- After each edit, update "dateModified" and run the page through https://validator.schema.org/ and https://search.google.com/test/rich-results.

=====================================================================
4. FILL THE SAME DATA INTO speakers.json (programme team, per confirmed speaker)
=====================================================================
"session": {
  "title": "PLACEHOLDER_SESSION_TITLE",
  "date": "2026-10-14",
  "time": "PLACEHOLDER_START-PLACEHOLDER_END IST",
  "hall": "PLACEHOLDER_HALL",
  "format": "PLACEHOLDER_FORMAT",
  "track": "PLACEHOLDER_TRACK_NAME"
}
Then run: python3 build_speakers.py --clean, and upload dist/. Each speaker page then shows its slot and links to /agenda/.
Before you build, set "pass_price_inr" in the "site" block to the reconciled live price (PLACEHOLDER_CURRENT_PASS_PRICE), or to null. It is 20000 today, and every speaker page would publish that possibly stale Offer price.

=====================================================================
5. INTERNAL LINKS (copy to paste)
=====================================================================
Homepage nav (all templates): <a href="/agenda/">Agenda</a>
Homepage hero, next to the existing CTA: <a class="btn" href="/agenda/">View the 2026 agenda</a>
Homepage "Seven tracks. One agenda" section, last line: <a href="/agenda/">See sessions by track and day</a>
/speaker.html, under the intro: <p>See when and where each speaker appears on the <a href="/agenda/">World AI Summit 2026 agenda</a>.</p>
/ai-conference-bengaluru-2026.html, first mention of sessions: <a href="/agenda/">the day-wise agenda for 14–15 October</a>
All 5 blog posts, footer line: <p>Plan your two days: <a href="/agenda/">World AI Summit 2026 agenda</a>, 14–15 October, Bengaluru.</p>
Banner on /1st-edition/world-ai-agenda.html, top of the content:
<div class="notice" role="note"><strong>Looking for the 2026 agenda?</strong> World AI Summit 2026 takes place on 14–15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway. <a href="/agenda/">See the 2026 agenda</a></div>

=====================================================================
6. REDIRECTS
=====================================================================
--- Apache (.htaccess at the web root, above existing rules) ---
RewriteEngine On
# Common type-in variants -> /agenda/
RewriteRule ^agenda\.html$ /agenda/ [R=301,L]
RewriteRule ^schedule/?$ /agenda/ [R=301,L]
RewriteRule ^schedule\.html$ /agenda/ [R=301,L]
# 2025 article: replace the current 302 to /1st-edition with a single 301 to the 2025 agenda (that page carries the 2026 banner)
RewriteRule ^1st-edition/what-to-expect-world-ai-summit-2025-agenda-highlights/?$ /1st-edition/world-ai-agenda.html [R=301,L]
# /agenda -> /agenda/ is handled by mod_dir (DirectorySlash On, the default) once /agenda/index.html exists.
# Host canonicalisation, ONLY if no site-wide non-www -> www rule exists yet:
# RewriteCond %{HTTP_HOST} ^worldaisummit\.com$ [NC]
# RewriteRule ^(.*)$ https://www.worldaisummit.com/$1 [R=301,L]

--- nginx (inside the server block for www.worldaisummit.com) ---
location = /agenda      { return 301 /agenda/; }
location = /agenda.html { return 301 /agenda/; }
location ~ ^/schedule(/|\.html)?$ { return 301 /agenda/; }
location ~ ^/1st-edition/what-to-expect-world-ai-summit-2025-agenda-highlights/?$ { return 301 /1st-edition/world-ai-agenda.html; }
location /agenda/ { try_files $uri $uri/index.html =404; }
# ONLY if not already present, a separate server block for the bare domain:
# server { listen 443 ssl; server_name worldaisummit.com; return 301 https://www.worldaisummit.com$request_uri; }

=====================================================================
7. SITEMAP ENTRY (update lastmod every time a session is added)
=====================================================================
<url>
  <loc>https://www.worldaisummit.com/agenda/</loc>
  <lastmod>PLACEHOLDER_LAST_UPDATED_ISO</lastmod>
  <changefreq>daily</changefreq>
</url>
