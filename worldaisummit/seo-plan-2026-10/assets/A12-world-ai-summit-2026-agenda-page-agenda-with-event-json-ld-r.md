# A12: World AI Summit 2026 Agenda page (/agenda/) with Event JSON-LD, redirects, sitemap and internal-link snippets

- **For recommendation:** Publish a 2026 agenda page with sessions by time; it does not exist yet, and the speaker pages already promise one
- **Research lens:** site-deep-read
- **Format:** HTML page (/agenda/index.html) with inline JSON-LD @graph (WebPage + Event + BreadcrumbList), plus a subEvent JSON template, Apache .htaccess and nginx redirect rules, sitemap.xml changes and internal-link HTML snippets
- **Placeholders the business must fill:**
  - PLACEHOLDER_LAST_UPDATED_DATE / PLACEHOLDER_LAST_UPDATED_ISO - publish or last-edit date, e.g. '6 October 2026' / '2026-10-06' (also used in sitemap lastmod and WebPage.dateModified)
  - PLACEHOLDER_D1_REGISTRATION_TIME / PLACEHOLDER_D2_REGISTRATION_TIME - registration opening time each day (programme team)
  - PLACEHOLDER_REGISTRATION_DESK - registration desk location in the hotel
  - PLACEHOLDER_TIME, PLACEHOLDER_SESSION_TITLE, PLACEHOLDER_FORMAT, PLACEHOLDER_TRACK, PLACEHOLDER_HALL - one row per session from the signed-off running order; never drafted
  - PLACEHOLDER_SPEAKER_NAME, PLACEHOLDER_SLUG, PLACEHOLDER_ROLE_AND_ORG - only speakers confirmed on /assets/speaker_details/index.html; slug must match the live profile URL
  - PLACEHOLDER_AWARDS_TIME - World AI Awards ceremony day and time; keep the row only on the confirmed day
  - PLACEHOLDER_DINNER_TIME - exclusive networking dinner day and time; keep the row only on the confirmed day
  - PLACEHOLDER_HIGHER_TIER_NAME - exact name of the pass tier that includes the special sessions and dinner (the 'VIP' label is unverified)
  - PLACEHOLDER_HALL_1_NAME / _USE, PLACEHOLDER_HALL_2_NAME / _USE - hall names and use (add or remove lines as needed)
  - PLACEHOLDER_CURRENT_PASS_PRICE - visible 'from' price, e.g. 'Rs 30,000 + GST' (Standard pricing ended 30 Sep 2026; business decision)
  - PLACEHOLDER_CURRENT_PASS_PRICE_NUMBER - the same price as a bare number for JSON-LD, e.g. 30000
  - PLACEHOLDER_OFFER_VALID_FROM_ISO - date the current price tier opened, e.g. 2026-10-01
  - PLACEHOLDER_GROUP_BOOKING_LINE - confirm whether 'Groups of 3 or more delegates get 10% off.' still applies; otherwise delete
  - PLACEHOLDER_EVENT_IMAGE_URL - absolute URL of a 1200x630 event image (og:image and Event.image)
  - PLACEHOLDER_HH:MM (FILE 2 subEvent) - session start and end times in 24-hour IST

## How to ship

Summary: this is mainly a page to help visitors decide to book. It is not a traffic play. Get the running order first, then ship by 7 Oct. No repo files were edited.

1. The URL is /agenda/, not /agenda.html. The speaker generator already links there: worldaisummit/speakers/speakers.json has site.agenda_url = "/agenda/". The redirects send /agenda.html and /agenda to /agenda/, because Exa found nothing at either URL.

2. The programme team has to supply the content. No running order exists anywhere yet. Verifier check 7 confirmed that session, time, hall, day and track are null for all 76 entries. Fill each table row from the team's signed-off sheet and never draft session titles. If the sheet is not ready by 7 Oct, either:
   - hold the page, or
   - publish it with the commented "PRE-FINAL STATE" paragraph in place of both tables.
   Do not publish placeholder rows.

3. Before going live, replace every PLACEHOLDER_ marker; a search for "PLACEHOLDER_" must return nothing.
   - In JSON-LD, "price" must be a plain number such as 30000, with no "Rs" and no commas. The /delegate/ page showed Standard prices valid only until 30 Sep 2026, so the current price needs a business decision.
   - Drop "image" only if no event image exists. Google recommends it.
   - Check the result in the Rich Results Test (search.google.com/test/rich-results) and the Schema Markup Validator (validator.schema.org).

4. Pass-tier naming (verifier check 8): the homepage only shows that higher tiers include "Exclusive networking dinner" and "Special sessions — GenAI, Agentic AI & AI Safety". The tier name was not verified, so the copy avoids "VIP". Use the exact tier name from /delegate/.

5. Performers: the list holds the 50 speakers marked "Confirmed 2026" on the live /assets/speaker_details/index.html (Exa fetch, 1 Oct 2026). It matches the 50 entries with confirmed_2026 = true in speakers.json. 2025-only speakers are left out, and there are no bios. One flag: speakers.json bio_notes for Sushan Rungta say "CHECK TITLE" because LinkedIn shows the Absolute CTO role ending in Feb 2026. Confirm his title, or remove jobTitle for him. Once sessions are known:
   - add one subEvent per session (FILE 2);
   - fill session data in speakers.json, then run `python3 build_speakers.py --clean` so speaker pages and the agenda show the same times;
   - check each speaker profile slug against the live /assets/speaker_details/ URLs (only sandeep-varaganti.html was confirmed).

6. Venue address: 26/1 Dr Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru 560055 (+91 80 4252 1000). Sources: a WebSearch on 1 Oct 2026 covering the Marriott listing (https://www.marriott.com/en-us/hotels/blrgs-sheraton-grand-bangalore-hotel-at-brigade-gateway/overview/) and HotelPlanner (https://www.hotelplanner.com/Hotels/178731/Reservations-Sheraton-Bangalore-Hotel-at-Brigade-Gateway-Bangalore-26-1-Dr-Rajkumar-Rd-Malleswaram-Rajajinagar-560055). Also confirm the organiser URL https://eletsonline.com/ is the preferred Elets home page.

7. Redirects (FILE 3): use the Apache or the nginx block, whichever the host runs. The 301 from the 2025 /1st-edition/world-ai-agenda.html is tidying, not a ranking lever (verifier check 3). The second stale URL currently returns a 302; this makes it a 301. Remove both from sitemap.xml (FILE 4). Test with `curl -sI https://www.worldaisummit.com/agenda.html` and expect a single 301 to /agenda/.

8. Internal links (FILE 5): add them in the same deploy. The page is otherwise orphaned, like /delegate/ and /awards/ today.

9. Indexing (verifier check 9): Search Console covers only the non-www property, so URL Inspection cannot request indexing for the www URL. Verify https://www.worldaisummit.com/ or a Domain property through a DNS TXT record, then submit the sitemap and request indexing. Until then, rely on the sitemap lastmod and the homepage nav link.

10. Expectations (verifier checks 4-6): four of the five agenda queries had no measurable India volume. "ai summit agenda" is 140 a month and probably belongs to a different event. The non-www Search Console data showed zero agenda queries. worldsummit.ai/programme (Amsterdam) ranks first in a US search. The title's "Bengaluru" and "14-15 Oct" and the opening line separate this event from that one. Treat the page as a booking aid for visitors already on the site and for sponsors. Do not promise new rankings. Day names were checked: 14 Oct 2026 is a Wednesday and 15 Oct is a Thursday. Title is 50 characters, meta description 153.

11. Your question about more CPUs: this container has 4 CPUs (nproc). I cannot add more from inside the session.

## Content

=== FILE 1: /agenda/index.html (served at https://www.worldaisummit.com/agenda/) ===
<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>World AI Summit 2026 Agenda | 14-15 Oct, Bengaluru</title>
<meta name="description" content="Day-by-day agenda for World AI Summit 2026, Bengaluru: keynotes, panels and sessions across 7 tracks on 14-15 October. Session times, halls and speakers.">
<link rel="canonical" href="https://www.worldaisummit.com/agenda/">
<meta name="robots" content="index, follow">
<meta property="og:type" content="website">
<meta property="og:site_name" content="World AI Summit">
<meta property="og:locale" content="en_IN">
<meta property="og:url" content="https://www.worldaisummit.com/agenda/">
<meta property="og:title" content="World AI Summit 2026 Agenda | 14-15 Oct, Bengaluru">
<meta property="og:description" content="Day-by-day agenda for World AI Summit 2026, Bengaluru: keynotes, panels and sessions across 7 tracks on 14-15 October. Session times, halls and speakers.">
<meta property="og:image" content="PLACEHOLDER_EVENT_IMAGE_URL">
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
      "description": "Day-by-day agenda for World AI Summit 2026, Bengaluru: keynotes, panels and sessions across 7 tracks on 14-15 October. Session times, halls and speakers.",
      "inLanguage": "en-IN",
      "dateModified": "PLACEHOLDER_LAST_UPDATED_ISO",
      "about": {
        "@id": "https://www.worldaisummit.com/#event-2026"
      },
      "breadcrumb": {
        "@id": "https://www.worldaisummit.com/agenda/#breadcrumb"
      }
    },
    {
      "@type": "Event",
      "@id": "https://www.worldaisummit.com/#event-2026",
      "name": "World AI Summit 2026",
      "description": "Day-by-day agenda for World AI Summit 2026, Bengaluru: keynotes, panels and sessions across 7 tracks on 14-15 October. Session times, halls and speakers.",
      "url": "https://www.worldaisummit.com/",
      "image": [
        "PLACEHOLDER_EVENT_IMAGE_URL"
      ],
      "startDate": "2026-10-14",
      "endDate": "2026-10-15",
      "eventStatus": "https://schema.org/EventScheduled",
      "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
      "inLanguage": "en-IN",
      "location": {
        "@type": "Place",
        "name": "Sheraton Grand Bangalore Hotel at Brigade Gateway",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "26/1 Dr Rajkumar Road, Malleswaram-Rajajinagar",
          "addressLocality": "Bengaluru",
          "addressRegion": "Karnataka",
          "postalCode": "560055",
          "addressCountry": "IN"
        }
      },
      "organizer": {
        "@type": "Organization",
        "name": "Elets Technomedia",
        "url": "https://eletsonline.com/"
      },
      "offers": {
        "@type": "Offer",
        "name": "Delegate pass",
        "url": "https://www.worldaisummit.com/delegate/",
        "price": "PLACEHOLDER_CURRENT_PASS_PRICE_NUMBER",
        "priceCurrency": "INR",
        "availability": "https://schema.org/InStock",
        "validFrom": "PLACEHOLDER_OFFER_VALID_FROM_ISO"
      },
      "performer": [
        {"@type": "Person", "name": "Pankaj Kumar Pandey, IAS", "jobTitle": "Principal Secretary, e-Governance, Karnataka"},
        {"@type": "Person", "name": "T Bhoobalan, IAS", "jobTitle": "CEO, Centre for e-Governance, Karnataka"},
        {"@type": "Person", "name": "Sanjeev Rastogi", "jobTitle": "Head, Group Policy Services, Adani Group"},
        {"@type": "Person", "name": "Shalini Kapoor", "jobTitle": "Chief Strategist, Data and AI, EkStep"},
        {"@type": "Person", "name": "Dr Ravikumar Surpur, IAS", "jobTitle": "Secretary, IT & Communication, Rajasthan"},
        {"@type": "Person", "name": "Aman Mittal, IAS", "jobTitle": "Joint CEO, MITRA, Maharashtra"},
        {"@type": "Person", "name": "Sanjeev Gupta", "jobTitle": "CEO, Karnataka Digital Economy Mission"},
        {"@type": "Person", "name": "Hemant Garg", "jobTitle": "Deputy Director, Ministry of Labour and Employment"},
        {"@type": "Person", "name": "Prajeet Prabhakaran", "jobTitle": "Regional Director, Embassy of Austria"},
        {"@type": "Person", "name": "Ram Mohan Rao", "jobTitle": "Executive Director, SEBI"},
        {"@type": "Person", "name": "M. Balasubramaniam (Bala MS)", "jobTitle": "Chairman, Southern Regional Committee, AICTE"},
        {"@type": "Person", "name": "Mahesh Hariharan Iyer", "jobTitle": "VP Engineering, Reserve Bank Innovation Hub"},
        {"@type": "Person", "name": "Dr. Sushil Kumar Meher", "jobTitle": "Head, IT and CISO, AIIMS"},
        {"@type": "Person", "name": "Sandeep Varaganti", "jobTitle": "CEO, JioMart, Reliance Retail"},
        {"@type": "Person", "name": "George Inasu", "jobTitle": "MD and Country Head, Fidelity National Financial India"},
        {"@type": "Person", "name": "Anand Ramakrishnan", "jobTitle": "Managing Director, Equiniti India"},
        {"@type": "Person", "name": "Tulshekar Gangireddy", "jobTitle": "ED and Head of Data Strategy, JPMorgan Chase"},
        {"@type": "Person", "name": "Deepak Mohanty", "jobTitle": "Executive Director, Wells Fargo"},
        {"@type": "Person", "name": "Anand Thakur", "jobTitle": "CPTO, Reliance Retail"},
        {"@type": "Person", "name": "Pawan Sachdeva", "jobTitle": "Senior MD and Technology Head India, Carelon"},
        {"@type": "Person", "name": "Pranav Saxena", "jobTitle": "CPTO, API Holdings"},
        {"@type": "Person", "name": "Suman Guha", "jobTitle": "Chief Digital and Technology Officer, Croma"},
        {"@type": "Person", "name": "Avinash Naik", "jobTitle": "CIO, Bajaj Allianz General Insurance"},
        {"@type": "Person", "name": "Harsh Vardhan", "jobTitle": "Global Head, AI and Digital Innovation, Apollo Tyres"},
        {"@type": "Person", "name": "Vijaya Kadiyala", "jobTitle": "Executive Director, DBS Bank"},
        {"@type": "Person", "name": "Shanmugam Manivannan", "jobTitle": "Chief Digital Officer, Equitas Small Finance Bank"},
        {"@type": "Person", "name": "Rajesh Choudhary", "jobTitle": "CIO, CSB Bank"},
        {"@type": "Person", "name": "Dipayan Chakraborty", "jobTitle": "Head, India Analytics Center, eBay"},
        {"@type": "Person", "name": "Archana Menon", "jobTitle": "Head of Analytics and Watches, Titan"},
        {"@type": "Person", "name": "Deepika Sandeep", "jobTitle": "Head, AI/ML CoE, HSBC"},
        {"@type": "Person", "name": "Anil Varma", "jobTitle": "CTO, Multi Commodity Exchange Clearing Corporation"},
        {"@type": "Person", "name": "Deepak Sharma", "jobTitle": "Independent Director, Suryoday Small Finance Bank"},
        {"@type": "Person", "name": "Animesh Kishore", "jobTitle": "Head, Digital and Analytics CoE, ITC"},
        {"@type": "Person", "name": "Sandeep Sharma", "jobTitle": "Head of Technology and Product, Shoppers Stop"},
        {"@type": "Person", "name": "Shireen Ali", "jobTitle": "Head, UK Data Enablement and Standards, HSBC"},
        {"@type": "Person", "name": "Vishal Chugh", "jobTitle": "EVP, Head Risk FRM, Tata Capital"},
        {"@type": "Person", "name": "Shantanu Dasgupta", "jobTitle": "Head of Digital Initiatives, Treasury and Transaction Banking, Axis Bank"},
        {"@type": "Person", "name": "Sushan Rungta", "jobTitle": "CTO, Absolute"},
        {"@type": "Person", "name": "Ganesh Joshi", "jobTitle": "CIO, Nilons Enterprises"},
        {"@type": "Person", "name": "Praveen Bist", "jobTitle": "CIO, Amrita Hospitals"},
        {"@type": "Person", "name": "Kuldeep T", "jobTitle": "CISO and DPO, BigBasket"},
        {"@type": "Person", "name": "Anshuma (Dogra) Singh", "jobTitle": "Senior Director, India IT Head, Applied Materials"},
        {"@type": "Person", "name": "Padmanaban TA", "jobTitle": "DGM and Head of Digital Banking, Karnataka Bank"},
        {"@type": "Person", "name": "Joyce Rodriguez", "jobTitle": "Head of Digital Cybersecurity, Airbus India"},
        {"@type": "Person", "name": "Pavankumar Gurazada", "jobTitle": "Associate Director, Great Learning"},
        {"@type": "Person", "name": "Aneelkumar (Aneel) Savalagi", "jobTitle": "Global Chapter Leader, ICC, Takeda"},
        {"@type": "Person", "name": "Sivakumar Selva Ganapathy", "jobTitle": "VP Software Engineering, Johnson Controls"},
        {"@type": "Person", "name": "Sandhya Vasudevan", "jobTitle": "Board Member, TiE Bangalore"},
        {"@type": "Person", "name": "Suman Dash", "jobTitle": "COO, Acsel Technology Forum"},
        {"@type": "Person", "name": "Shashank Randev", "jobTitle": "Founder and General Partner, 247VC"}
      ]
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://www.worldaisummit.com/agenda/#breadcrumb",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://www.worldaisummit.com/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Agenda",
          "item": "https://www.worldaisummit.com/agenda/"
        }
      ]
    }
  ]
}</script>
<style>
  .wais-agenda{max-width:1100px;margin:0 auto;padding:24px 16px 48px;line-height:1.55}
  .wais-agenda .crumbs,.wais-agenda .updated{font-size:.9rem;opacity:.8}
  .wais-agenda .jump a{margin-right:12px;white-space:nowrap}
  .wais-agenda .day-head{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:12px;margin-top:40px}
  .wais-agenda .btn{display:inline-block;padding:10px 18px;border-radius:6px;background:#0b3d91;color:#fff;text-decoration:none;font-weight:600}
  .wais-agenda .table-wrap{overflow-x:auto;-webkit-overflow-scrolling:touch}
  .wais-agenda table{width:100%;min-width:760px;border-collapse:collapse;font-size:.95rem}
  .wais-agenda caption{text-align:left;font-size:.85rem;opacity:.75;padding:6px 0}
  .wais-agenda th,.wais-agenda td{border-bottom:1px solid #d9dde3;padding:10px 8px;text-align:left;vertical-align:top}
  .wais-agenda th{background:#f3f5f8}
  .wais-agenda .tier{font-size:.8rem;font-weight:600;white-space:nowrap}
  .wais-agenda .note{border-left:3px solid #0b3d91;padding:8px 12px;background:#f3f5f8}
</style>
</head>
<body>
<!-- Site header include. Add <a href="/agenda/">Agenda</a> to the main nav on every page. -->
<main class="wais-agenda">

  <p class="crumbs"><a href="/">Home</a> / Agenda</p>

  <h1>World AI Summit 2026 Agenda</h1>

  <p>The programme for World AI Summit 2026 in Bengaluru, organised by Elets Technomedia on Wednesday 14 and Thursday 15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway. Sessions run across seven tracks. Each row gives the time, format, track, hall and speakers.</p>

  <p class="updated">Last updated: <time datetime="PLACEHOLDER_LAST_UPDATED_ISO">PLACEHOLDER_LAST_UPDATED_DATE</time>. All times are IST. Programme subject to change.</p>

  <p class="jump">
    <a href="#day-1">Day 1, 14 Oct</a>
    <a href="#day-2">Day 2, 15 Oct</a>
    <a href="#tracks">Tracks</a>
    <a href="#venue">Venue and halls</a>
    <a href="/assets/speaker_details/index.html">Speakers</a>
    <a href="/delegate/">Book your pass</a>
  </p>

  <!-- ===== DAY 1 ===== -->
  <section id="day-1" aria-labelledby="day-1-h">
    <div class="day-head">
      <h2 id="day-1-h">Day 1: Wednesday, 14 October 2026</h2>
      <a class="btn" href="/delegate/">Book your pass</a>
    </div>

    <!-- PRE-FINAL STATE: if the running order is not signed off at publication, use only this paragraph
         in place of the table, and the same for Day 2. Do not draft or guess session titles.
    <p>Session times and halls for Day 1 will be published here once the programme is final. See the <a href="/assets/speaker_details/index.html">confirmed speakers</a> in the meantime.</p>
    -->

    <div class="table-wrap">
      <table>
        <caption>Day 1, Wednesday 14 October 2026. Times in IST.</caption>
        <thead>
          <tr><th scope="col">Time</th><th scope="col">Session</th><th scope="col">Format</th><th scope="col">Track</th><th scope="col">Hall</th><th scope="col">Speakers</th></tr>
        </thead>
        <tbody>
          <tr><td>PLACEHOLDER_D1_REGISTRATION_TIME</td><td>Registration and badge collection</td><td>-</td><td>-</td><td>PLACEHOLDER_REGISTRATION_DESK</td><td>-</td></tr>
          <!-- One row per session, copied from the programme team's running order.
               Format: Keynote, Panel, Fireside chat or Masterclass. Track: one of the seven names in #tracks.
               Speakers: link each name to the live profile /assets/speaker_details/<slug>.html; use only names on the confirmed list.
               For sessions limited to a higher pass tier, add after the title: <span class="tier">PLACEHOLDER_HIGHER_TIER_NAME pass</span> -->
          <tr><td>PLACEHOLDER_TIME</td><td>PLACEHOLDER_SESSION_TITLE</td><td>PLACEHOLDER_FORMAT</td><td>PLACEHOLDER_TRACK</td><td>PLACEHOLDER_HALL</td><td><a href="/assets/speaker_details/PLACEHOLDER_SLUG.html">PLACEHOLDER_SPEAKER_NAME</a>, PLACEHOLDER_ROLE_AND_ORG</td></tr>
          <!-- Keep the next two rows on whichever day the programme team confirms, and delete them from the other day. -->
          <tr><td>PLACEHOLDER_AWARDS_TIME</td><td><a href="/awards/">World AI Awards</a> ceremony</td><td>Awards</td><td>-</td><td>PLACEHOLDER_HALL</td><td>-</td></tr>
          <tr><td>PLACEHOLDER_DINNER_TIME</td><td>Exclusive networking dinner <span class="tier">PLACEHOLDER_HIGHER_TIER_NAME pass</span></td><td>Networking</td><td>-</td><td>PLACEHOLDER_HALL</td><td>-</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- ===== DAY 2 ===== -->
  <section id="day-2" aria-labelledby="day-2-h">
    <div class="day-head">
      <h2 id="day-2-h">Day 2: Thursday, 15 October 2026</h2>
      <a class="btn" href="/delegate/">Book your pass</a>
    </div>
    <div class="table-wrap">
      <table>
        <caption>Day 2, Thursday 15 October 2026. Times in IST.</caption>
        <thead>
          <tr><th scope="col">Time</th><th scope="col">Session</th><th scope="col">Format</th><th scope="col">Track</th><th scope="col">Hall</th><th scope="col">Speakers</th></tr>
        </thead>
        <tbody>
          <tr><td>PLACEHOLDER_D2_REGISTRATION_TIME</td><td>Registration and badge collection</td><td>-</td><td>-</td><td>PLACEHOLDER_REGISTRATION_DESK</td><td>-</td></tr>
          <tr><td>PLACEHOLDER_TIME</td><td>PLACEHOLDER_SESSION_TITLE</td><td>PLACEHOLDER_FORMAT</td><td>PLACEHOLDER_TRACK</td><td>PLACEHOLDER_HALL</td><td><a href="/assets/speaker_details/PLACEHOLDER_SLUG.html">PLACEHOLDER_SPEAKER_NAME</a>, PLACEHOLDER_ROLE_AND_ORG</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- ===== PASS ACCESS ===== -->
  <section id="pass-access" aria-labelledby="pass-h">
    <h2 id="pass-h">What each pass includes</h2>
    <p>Sessions marked <span class="tier">PLACEHOLDER_HIGHER_TIER_NAME pass</span> are open only to holders of that pass. They include the special sessions on GenAI, Agentic AI and AI Safety and the exclusive networking dinner. All other sessions are open to every delegate pass. <a href="/delegate/">Compare passes</a>.</p>
  </section>

  <!-- ===== TRACKS ===== -->
  <section id="tracks" aria-labelledby="tracks-h">
    <h2 id="tracks-h">The seven tracks</h2>
    <ol>
      <li>Frontier Models &amp; Compute</li>
      <li>Sovereign AI &amp; Geopolitics</li>
      <li>Enterprise AI in Production</li>
      <li>GCCs</li>
      <li>Robotics, Agents &amp; Embodied AI</li>
      <li>AI for Bharat</li>
      <li>Capital, Founders &amp; Exits</li>
    </ol>
  </section>

  <!-- ===== VENUE ===== -->
  <section id="venue" aria-labelledby="venue-h">
    <h2 id="venue-h">Venue and halls</h2>
    <p><strong>Sheraton Grand Bangalore Hotel at Brigade Gateway</strong><br>
      26/1 Dr Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru, Karnataka 560055<br>
      <a href="https://www.google.com/maps/search/?api=1&amp;query=Sheraton+Grand+Bangalore+Hotel+at+Brigade+Gateway" rel="noopener">Open in Google Maps</a></p>
    <ul>
      <li>PLACEHOLDER_HALL_1_NAME: PLACEHOLDER_HALL_1_USE (for example, main stage)</li>
      <li>PLACEHOLDER_HALL_2_NAME: PLACEHOLDER_HALL_2_USE</li>
      <li>Registration desk: PLACEHOLDER_REGISTRATION_DESK</li>
    </ul>
  </section>

  <!-- ===== CTA ===== -->
  <section id="book" aria-labelledby="book-h" class="note">
    <h2 id="book-h">Book your pass</h2>
    <p>Delegate passes start at PLACEHOLDER_CURRENT_PASS_PRICE. PLACEHOLDER_GROUP_BOOKING_LINE</p>
    <p><a class="btn" href="/delegate/">Book your pass</a></p>
    <p>Registration queries: <a href="mailto:registration@worldaisummit.com">registration@worldaisummit.com</a><br>
      Sponsorship and exhibition: <a href="mailto:partnerships@worldaisummit.com">partnerships@worldaisummit.com</a><br>
      Speaking enquiries: <a href="mailto:secretariat@worldaisummit.com">secretariat@worldaisummit.com</a></p>
  </section>

  <p class="updated">Programme subject to change. Session times and halls on this page and on each <a href="/assets/speaker_details/index.html">speaker page</a> are updated together.</p>

</main>
<!-- Site footer include -->
</body>
</html>

=== FILE 2: subEvent template (add to the Event node once the running order is final; one object per session, only verified speakers) ===
"subEvent": [
  {
    "@type": "Event",
    "name": "PLACEHOLDER_SESSION_TITLE",
    "startDate": "2026-10-14TPLACEHOLDER_HH:MM:00+05:30",
    "endDate": "2026-10-14TPLACEHOLDER_HH:MM:00+05:30",
    "eventStatus": "https://schema.org/EventScheduled",
    "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
    "location": { "@type": "Place", "name": "PLACEHOLDER_HALL, Sheraton Grand Bangalore Hotel at Brigade Gateway", "address": { "@type": "PostalAddress", "streetAddress": "26/1 Dr Rajkumar Road, Malleswaram-Rajajinagar", "addressLocality": "Bengaluru", "addressRegion": "Karnataka", "postalCode": "560055", "addressCountry": "IN" } },
    "superEvent": { "@id": "https://www.worldaisummit.com/#event-2026" },
    "performer": [ { "@type": "Person", "name": "PLACEHOLDER_SPEAKER_NAME", "url": "https://www.worldaisummit.com/assets/speaker_details/PLACEHOLDER_SLUG.html" } ]
  }
]

=== FILE 3: Redirects ===
# Apache (.htaccess in the web root; needs mod_rewrite)
RewriteEngine On
RewriteRule ^agenda\.html$ https://www.worldaisummit.com/agenda/ [R=301,L]
RewriteRule ^agenda$ https://www.worldaisummit.com/agenda/ [R=301,L]
RewriteRule ^1st-edition/world-ai-agenda\.html$ https://www.worldaisummit.com/agenda/ [R=301,L]
RewriteRule ^1st-edition/what-to-expect-world-ai-summit-2025-agenda-highlights/?$ https://www.worldaisummit.com/1st-edition/ [R=301,L]

# nginx (inside the server block for www.worldaisummit.com, and in the non-www block if it serves files)
location = /agenda.html { return 301 https://www.worldaisummit.com/agenda/; }
location = /agenda { return 301 https://www.worldaisummit.com/agenda/; }
location = /1st-edition/world-ai-agenda.html { return 301 https://www.worldaisummit.com/agenda/; }
location ~ ^/1st-edition/what-to-expect-world-ai-summit-2025-agenda-highlights/?$ { return 301 https://www.worldaisummit.com/1st-edition/; }
# Make sure the server block has: index index.html;

=== FILE 4: sitemap.xml changes ===
ADD:
<url>
  <loc>https://www.worldaisummit.com/agenda/</loc>
  <lastmod>PLACEHOLDER_LAST_UPDATED_ISO</lastmod>
</url>
REMOVE the <url> entries for:
https://www.worldaisummit.com/1st-edition/world-ai-agenda.html
https://www.worldaisummit.com/1st-edition/what-to-expect-world-ai-summit-2025-agenda-highlights

=== FILE 5: Internal link snippets ===
Homepage main nav (every page that shares the header):
  <a href="/agenda/">Agenda</a>
Homepage hero, next to the existing pass button:
  <a href="/agenda/">See the agenda</a>
Homepage, under the heading "Seven tracks. One agenda":
  <a href="/agenda/">See the full agenda by day and hall</a>
/delegate/ (above the pass cards):
  <p>Not sure which day or pass suits you? <a href="/agenda/">See the agenda</a>.</p>
/assets/speaker_details/index.html, replace the closing note (verified wording, 1 Oct) with the linked version below; add the same link to /speaker.html:
  <p>Speaker names, roles and organisations are as at the time of announcement. Session times and halls are confirmed on each speaker page and on the <a href="/agenda/">agenda</a> once the programme is final. Programme subject to change.</p>
Each /assets/speaker_details/<slug>.html, replace the pending-session sentence with:
  <p>Session title, time and hall will be published on this page and on the <a href="/agenda/">agenda</a> once the programme is final.</p>
  <p><a href="/agenda/">See the agenda</a></p>
/ai-conference-bengaluru-2026.html, in the section that lists the seven tracks:
  <p><a href="/agenda/">See the World AI Summit 2026 agenda</a> for session times, halls and speakers.</p>
