# A18: /agenda/ page for World AI Summit 2026, plus the nav, venue anchor, redirects, sitemap entry and post-event swap

- **For recommendation:** Event-month brand surge: route brand-modifier searches (passes, agenda, venue, awards) to linked pages before 7 Oct, then switch the homepage after 15 Oct
- **Research lens:** demand-sweep
- **Format:** Static HTML file (/agenda/index.html) with Event, BreadcrumbList and WebPage JSON-LD, plus HTML snippets, Apache .htaccess and nginx redirect rules, a sitemap entry and post-event replacement blocks
- **Placeholders the business must fill:**
  - PLACEHOLDER_EVENT_IMAGE_URL_1200x630 (og:image and Event image)
  - PLACEHOLDER_CURRENT_PASS_PRICE (numeric INR price on sale now, for JSON-LD offers.price)
  - PLACEHOLDER_CURRENT_PASS_PRICE_TEXT (sticky bar text, e.g. Rs 30,000, once Elets confirms)
  - PLACEHOLDER_LAST_UPDATED_YYYY-MM-DD / PLACEHOLDER_LAST_UPDATED_DATE
  - PLACEHOLDER_TIME (every session row, IST)
  - PLACEHOLDER_HALL (every session row)
  - PLACEHOLDER_OPENING_SESSION_TITLE / PLACEHOLDER_SESSION_TITLE / PLACEHOLDER_CLOSING_SESSION_TITLE (programme team)
  - Track assignment per session (data-track and .track class t1-t7)
  - PLACEHOLDER_SPEAKER_SLUG / _NAME / _ROLE / _ORG (confirmed speakers only, slugs from speakers.json)
  - PLACEHOLDER_AWARDS_DATE_YYYY-MM-DD / PLACEHOLDER_AWARDS_DAY_AND_DATE / PLACEHOLDER_AWARDS_TIME / PLACEHOLDER_AWARDS_HALL
  - PLACEHOLDER_AWARD_NOMINATION_DEADLINE
  - PLACEHOLDER_PUBLISH_DATE_YYYY-MM-DD (sitemap lastmod)
  - PLACEHOLDER_HIGHLIGHTS_URL (post-event)
  - PLACEHOLDER_AWARDS_2026_WINNERS_URL (post-event)
  - Business decision: /registration and /registration.html redirect target (/delegate/ proposed)
  - Business decision: performer list pruned to speakers on the final agenda
  - Business decision: offers availability (InStock vs SoldOut, seats left)

## How to ship

I built and checked this in scratch files only. No repository files were changed.

**Before 9 Oct (web dev plus the Elets programme team):**
1. Fill every PLACEHOLDER_ marker in block 1. The programme team supplies times, halls, session titles and the track for each session.
   - Each day has seven example rows. Copy a row for every additional session.
   - Every speaker link points to /speakers/<slug>/, using the slugs in worldaisummit/speakers/speakers.json.
   - The track badge must match its class: t1 is Frontier Models & Compute, and so on to t7, Capital, Founders & Exits.
   - Do not write any speaker bios.
2. **Ship /speakers/ and /agenda/ in the same upload.** The speaker generator's pages link to /agenda/, and the agenda links to /speakers/<slug>/. If you upload either one alone, the site gets broken links.
   - The generated pages also link to /contact-us/, which does not exist on the live site. Either create that page, or change contact_url in speakers.json (for example to a mailto: address or an existing page) and rerun `python3 build_speakers.py --clean`.
   - If you decide not to ship /speakers/, change every speaker link and every performer url to the live /assets/speaker_details/<slug>.html page instead. I have not checked those slugs.
3. **Prune the JSON-LD performer list.** It lists the 50 speakers marked confirmed_2026 in speakers.json. Remove anyone who drops out or is not on the final agenda.
4. **Make the JSON-LD price a plain number.** Replace PLACEHOLDER_CURRENT_PASS_PRICE with a number, for example 30000, with no "Rs" and no comma.
   - The /delegate/ page shows Standard pricing valid only until 30 Sept 2026. Elets needs to confirm which price is on sale now; Late Access is listed at Rs 30,000/60,000.
   - If passes sell out, change availability to https://schema.org/SoldOut.
5. **Venue data.** The address (26/1, Dr Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru, Karnataka 560055) and the coordinates (13.01247, 77.55484) were checked today against Google Hotels, Apple Maps, Cvent and Exa Places.
   - If the homepage already has Event JSON-LD, use the same "@id" (https://www.worldaisummit.com/#event) and keep the two blocks consistent.
   - Test with Google's Rich Results Test and validator.schema.org before you publish.

**By 7 Oct:**
6. Add the nav in block 2 to every page.
7. Add id="venue" to the homepage's existing venue section (block 3). This is only an anchor; the section and its content are already there.
8. Check the canonical on /partner-with-us.html. The audit suggests it may point to /. If it does, make it self-referencing so the 'Partner' nav link can count as its own page.
9. Add the redirects in block 4: use the Apache rules on Apache hosting and the nginx rules on nginx. Leave out the host rule if one already exists, and run the two curl tests after uploading.
   - Sending /registration to /delegate/ replaces today's 3-hop 302 chain to the homepage. Elets needs to approve that change.
10. Add the sitemap entry (block 5).
11. Add the www URL-prefix property or a Domain property in Search Console, then request indexing for /agenda/ and /delegate/.

**On 16 Oct:** apply blocks 6a to 6d. These need the highlights page URL and the World AI Awards 2026 winners URL.

Copy uses Indian English with no exclamation marks. No OpenSEO paid tools were used.

**Your CPU question:** this session's container reports 4 CPUs (nproc). I cannot add more from here; the cloud environment settings control that.

## Content

==================================================================
1) /agenda/index.html (new page, full file; upload as /agenda/index.html so the URL is https://www.worldaisummit.com/agenda/)
==================================================================
<!DOCTYPE html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Agenda | World AI Summit 2026, Bengaluru, 14-15 October</title>
<meta name="description" content="Day-by-day agenda for World AI Summit 2026, 14-15 October at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru: sessions, halls and speakers.">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="https://www.worldaisummit.com/agenda/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="World AI Summit">
<meta property="og:title" content="World AI Summit 2026 Agenda">
<meta property="og:description" content="Sessions, halls, tracks and speakers for 14-15 October 2026, Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru.">
<meta property="og:url" content="https://www.worldaisummit.com/agenda/">
<meta property="og:image" content="PLACEHOLDER_EVENT_IMAGE_URL_1200x630">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://www.worldaisummit.com/agenda/#webpage",
      "url": "https://www.worldaisummit.com/agenda/",
      "name": "Agenda | World AI Summit 2026, Bengaluru, 14-15 October",
      "inLanguage": "en-IN",
      "isPartOf": {
        "@type": "WebSite",
        "@id": "https://www.worldaisummit.com/#website",
        "url": "https://www.worldaisummit.com/",
        "name": "World AI Summit"
      },
      "about": {
        "@id": "https://www.worldaisummit.com/#event"
      },
      "breadcrumb": {
        "@id": "https://www.worldaisummit.com/agenda/#breadcrumb"
      }
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
    },
    {
      "@type": "Event",
      "@id": "https://www.worldaisummit.com/#event",
      "name": "World AI Summit 2026",
      "description": "Two-day AI conference organised by Elets Technomedia on 14-15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru, with seven tracks and the World AI Awards presentation.",
      "url": "https://www.worldaisummit.com/",
      "startDate": "2026-10-14",
      "endDate": "2026-10-15",
      "eventStatus": "https://schema.org/EventScheduled",
      "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
      "inLanguage": "en-IN",
      "image": [
        "PLACEHOLDER_EVENT_IMAGE_URL_1200x630"
      ],
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
        "geo": {
          "@type": "GeoCoordinates",
          "latitude": 13.01247,
          "longitude": 77.55484
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
        "price": "PLACEHOLDER_CURRENT_PASS_PRICE",
        "priceCurrency": "INR",
        "availability": "https://schema.org/InStock",
        "validThrough": "2026-10-15"
      },
      "performer": [
        {"@type": "Person", "name": "Pankaj Kumar Pandey, IAS", "url": "https://www.worldaisummit.com/speakers/pankaj-kumar-pandey/"},
        {"@type": "Person", "name": "T Bhoobalan, IAS", "url": "https://www.worldaisummit.com/speakers/t-bhoobalan/"},
        {"@type": "Person", "name": "Sanjeev Rastogi", "url": "https://www.worldaisummit.com/speakers/sanjeev-rastogi/"},
        {"@type": "Person", "name": "Shalini Kapoor", "url": "https://www.worldaisummit.com/speakers/shalini-kapoor/"},
        {"@type": "Person", "name": "Dr Ravikumar Surpur, IAS", "url": "https://www.worldaisummit.com/speakers/ravikumar-surpur/"},
        {"@type": "Person", "name": "Aman Mittal, IAS", "url": "https://www.worldaisummit.com/speakers/aman-mittal/"},
        {"@type": "Person", "name": "Sanjeev Gupta", "url": "https://www.worldaisummit.com/speakers/sanjeev-gupta/"},
        {"@type": "Person", "name": "Hemant Garg", "url": "https://www.worldaisummit.com/speakers/hemant-garg/"},
        {"@type": "Person", "name": "Prajeet Prabhakaran", "url": "https://www.worldaisummit.com/speakers/prajeet-prabhakaran/"},
        {"@type": "Person", "name": "Ram Mohan Rao", "url": "https://www.worldaisummit.com/speakers/ram-mohan-rao/"},
        {"@type": "Person", "name": "M. Balasubramaniam (Bala MS)", "url": "https://www.worldaisummit.com/speakers/m-balasubramaniam/"},
        {"@type": "Person", "name": "Mahesh Hariharan Iyer", "url": "https://www.worldaisummit.com/speakers/mahesh-hariharan-iyer/"},
        {"@type": "Person", "name": "Dr. Sushil Kumar Meher", "url": "https://www.worldaisummit.com/speakers/sushil-kumar-meher/"},
        {"@type": "Person", "name": "Sandeep Varaganti", "url": "https://www.worldaisummit.com/speakers/sandeep-varaganti/"},
        {"@type": "Person", "name": "George Inasu", "url": "https://www.worldaisummit.com/speakers/george-inasu/"},
        {"@type": "Person", "name": "Anand Ramakrishnan", "url": "https://www.worldaisummit.com/speakers/anand-ramakrishnan/"},
        {"@type": "Person", "name": "Tulshekar Gangireddy", "url": "https://www.worldaisummit.com/speakers/tulshekar-gangireddy/"},
        {"@type": "Person", "name": "Deepak Mohanty", "url": "https://www.worldaisummit.com/speakers/deepak-mohanty/"},
        {"@type": "Person", "name": "Anand Thakur", "url": "https://www.worldaisummit.com/speakers/anand-thakur/"},
        {"@type": "Person", "name": "Pawan Sachdeva", "url": "https://www.worldaisummit.com/speakers/pawan-sachdeva/"},
        {"@type": "Person", "name": "Pranav Saxena", "url": "https://www.worldaisummit.com/speakers/pranav-saxena/"},
        {"@type": "Person", "name": "Suman Guha", "url": "https://www.worldaisummit.com/speakers/suman-guha/"},
        {"@type": "Person", "name": "Avinash Naik", "url": "https://www.worldaisummit.com/speakers/avinash-naik/"},
        {"@type": "Person", "name": "Harsh Vardhan", "url": "https://www.worldaisummit.com/speakers/harsh-vardhan/"},
        {"@type": "Person", "name": "Vijaya Kadiyala", "url": "https://www.worldaisummit.com/speakers/vijaya-kadiyala/"},
        {"@type": "Person", "name": "Shanmugam Manivannan", "url": "https://www.worldaisummit.com/speakers/shanmugam-manivannan/"},
        {"@type": "Person", "name": "Rajesh Choudhary", "url": "https://www.worldaisummit.com/speakers/rajesh-choudhary/"},
        {"@type": "Person", "name": "Dipayan Chakraborty", "url": "https://www.worldaisummit.com/speakers/dipayan-chakraborty/"},
        {"@type": "Person", "name": "Archana Menon", "url": "https://www.worldaisummit.com/speakers/archana-menon/"},
        {"@type": "Person", "name": "Deepika Sandeep", "url": "https://www.worldaisummit.com/speakers/deepika-sandeep/"},
        {"@type": "Person", "name": "Anil Varma", "url": "https://www.worldaisummit.com/speakers/anil-varma/"},
        {"@type": "Person", "name": "Deepak Sharma", "url": "https://www.worldaisummit.com/speakers/deepak-sharma/"},
        {"@type": "Person", "name": "Animesh Kishore", "url": "https://www.worldaisummit.com/speakers/animesh-kishore/"},
        {"@type": "Person", "name": "Sandeep Sharma", "url": "https://www.worldaisummit.com/speakers/sandeep-sharma/"},
        {"@type": "Person", "name": "Shireen Ali", "url": "https://www.worldaisummit.com/speakers/shireen-ali/"},
        {"@type": "Person", "name": "Vishal Chugh", "url": "https://www.worldaisummit.com/speakers/vishal-chugh/"},
        {"@type": "Person", "name": "Shantanu Dasgupta", "url": "https://www.worldaisummit.com/speakers/shantanu-dasgupta/"},
        {"@type": "Person", "name": "Sushan Rungta", "url": "https://www.worldaisummit.com/speakers/sushan-rungta/"},
        {"@type": "Person", "name": "Ganesh Joshi", "url": "https://www.worldaisummit.com/speakers/ganesh-joshi/"},
        {"@type": "Person", "name": "Praveen Bist", "url": "https://www.worldaisummit.com/speakers/praveen-bist/"},
        {"@type": "Person", "name": "Kuldeep T", "url": "https://www.worldaisummit.com/speakers/kuldeep-t/"},
        {"@type": "Person", "name": "Anshuma (Dogra) Singh", "url": "https://www.worldaisummit.com/speakers/anshuma-singh/"},
        {"@type": "Person", "name": "Padmanaban TA", "url": "https://www.worldaisummit.com/speakers/padmanaban-ta/"},
        {"@type": "Person", "name": "Joyce Rodriguez", "url": "https://www.worldaisummit.com/speakers/joyce-rodriguez/"},
        {"@type": "Person", "name": "Pavankumar Gurazada", "url": "https://www.worldaisummit.com/speakers/pavankumar-gurazada/"},
        {"@type": "Person", "name": "Aneelkumar (Aneel) Savalagi", "url": "https://www.worldaisummit.com/speakers/aneel-savalagi/"},
        {"@type": "Person", "name": "Sivakumar Selva Ganapathy", "url": "https://www.worldaisummit.com/speakers/sivakumar-selva-ganapathy/"},
        {"@type": "Person", "name": "Sandhya Vasudevan", "url": "https://www.worldaisummit.com/speakers/sandhya-vasudevan/"},
        {"@type": "Person", "name": "Suman Dash", "url": "https://www.worldaisummit.com/speakers/suman-dash/"},
        {"@type": "Person", "name": "Shashank Randev", "url": "https://www.worldaisummit.com/speakers/shashank-randev/"}
      ]
    }
  ]
}
</script>
<style>
:root{--ink:#14213d;--muted:#5b6478;--line:#e3e6ee;--accent:#0b5fff;--accent-ink:#fff;--bg:#fff;--soft:#f5f7fb;
--t1:#0b5fff;--t2:#7a3db8;--t3:#0f7b6c;--t4:#b45309;--t5:#be185d;--t6:#15803d;--t7:#334155}
*{box-sizing:border-box}
html{scroll-padding-top:80px}
body{margin:0;font-family:Inter,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;color:var(--ink);background:var(--bg);line-height:1.55}
a{color:var(--accent)}
.wrap{max-width:1040px;margin:0 auto;padding:0 16px}
.topbar{border-bottom:1px solid var(--line);background:var(--bg)}
.topbar .wrap{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;min-height:64px;gap:8px 16px;padding-top:8px;padding-bottom:8px}
.brand{font-weight:800;text-decoration:none;color:var(--ink);font-size:18px}
.site-nav{display:flex;flex-wrap:wrap;gap:6px 18px}
.site-nav a{text-decoration:none;color:var(--ink);font-weight:600;font-size:15px}
.site-nav a[aria-current="page"]{color:var(--accent)}
.crumbs{font-size:14px;color:var(--muted);padding:16px 0 0}
.crumbs a{color:var(--muted);text-decoration:none}
.intro{padding:20px 0 8px;border-bottom:1px solid var(--line)}
.intro h1{margin:0 0 8px;font-size:34px;line-height:1.15}
.intro p{margin:0 0 8px;color:var(--muted)}
.daynav{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0 0}
.daynav a{padding:6px 12px;border:1px solid var(--line);border-radius:999px;text-decoration:none;font-weight:600;font-size:14px}
.day{padding:28px 0 8px}
h2{font-size:24px;margin:0 0 14px}
.sessions{list-style:none;margin:0;padding:0}
.session{display:grid;grid-template-columns:150px 1fr;gap:16px;padding:14px 0;border-top:1px solid var(--line)}
.session[data-track]{border-left:4px solid var(--line);padding-left:12px}
.when{margin:0;font-weight:700}
.when .hall{display:block;font-weight:500;font-size:14px;color:var(--muted)}
.session h3{margin:2px 0 4px;font-size:18px;line-height:1.3}
.speakers{margin:0;font-size:15px;color:var(--muted)}
.track{display:inline-block;font-size:12px;font-weight:700;padding:2px 8px;border-radius:999px;color:#fff}
.t1{background:var(--t1)}.t2{background:var(--t2)}.t3{background:var(--t3)}.t4{background:var(--t4)}.t5{background:var(--t5)}.t6{background:var(--t6)}.t7{background:var(--t7)}
[data-track="t1"]{border-left-color:var(--t1)}[data-track="t2"]{border-left-color:var(--t2)}[data-track="t3"]{border-left-color:var(--t3)}[data-track="t4"]{border-left-color:var(--t4)}[data-track="t5"]{border-left-color:var(--t5)}[data-track="t6"]{border-left-color:var(--t6)}[data-track="t7"]{border-left-color:var(--t7)}
.legend ul{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:8px 16px}
.legend li{display:flex;align-items:center;gap:10px}
.awards{margin:28px 0;padding:20px;border:1px solid var(--line);border-radius:12px;background:var(--soft)}
.awards h2{margin-bottom:6px}
.venue{padding:8px 0 28px;color:var(--muted)}
.sticky-cta{position:sticky;bottom:0;z-index:10;background:var(--ink);color:#fff}
.sticky-cta .wrap{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:8px 16px;padding-top:10px;padding-bottom:10px}
.sticky-cta p{margin:0;font-size:15px}
.sticky-cta a{background:var(--accent);color:var(--accent-ink);padding:10px 16px;border-radius:8px;font-weight:700;text-decoration:none;white-space:nowrap}
footer{padding:24px 0 40px;font-size:14px;color:var(--muted)}
@media (max-width:640px){.intro h1{font-size:28px}.session{grid-template-columns:1fr;gap:4px}.site-nav a{font-size:14px}}
</style>
</head>
<body>
<header class="topbar">
  <div class="wrap">
    <a class="brand" href="/">World AI Summit</a>
    <nav class="site-nav" aria-label="Primary">
      <a href="/delegate/">Passes</a>
      <a href="/agenda/" aria-current="page">Agenda</a>
      <a href="/speaker.html">Speakers</a>
      <a href="/awards/">Awards</a>
      <a href="/#venue">Venue</a>
      <a href="/partner-with-us.html">Partner</a>
    </nav>
  </div>
</header>

<main class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / Agenda</nav>

  <section class="intro">
    <h1>World AI Summit 2026 Agenda</h1>
    <p>14-15 October 2026, Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. Seven tracks over two days, organised by Elets Technomedia.</p>
    <p>All times are IST. Sessions are added as speakers confirm, and the programme may change. Last updated <time datetime="PLACEHOLDER_LAST_UPDATED_YYYY-MM-DD">PLACEHOLDER_LAST_UPDATED_DATE</time>.</p>
    <div class="daynav">
      <a href="#day-1">Day 1, 14 Oct</a>
      <a href="#day-2">Day 2, 15 Oct</a>
      <a href="#tracks">Tracks</a>
      <a href="#awards">World AI Awards</a>
    </div>
  </section>

  <section class="day" id="day-1" aria-labelledby="day-1-h">
    <h2 id="day-1-h">Day 1, 14 Oct</h2>
    <ol class="sessions">
      <!-- One <li> per session, in time order. Copy a row, set data-track and the .track class to t1-t7, link every speaker to /speakers/<slug>/ (slugs as in speakers.json). Leave out any speaker who is not confirmed. -->
      <li class="session">
        <p class="when"><time>PLACEHOLDER_TIME</time> <span class="hall">PLACEHOLDER_HALL</span></p>
        <div>
          <h3>Registration and networking</h3>
        </div>
      </li>
      <li class="session">
        <p class="when"><time>PLACEHOLDER_TIME</time> <span class="hall">PLACEHOLDER_HALL</span></p>
        <div>
          <h3>PLACEHOLDER_OPENING_SESSION_TITLE</h3>
          <p class="speakers"><a href="/speakers/PLACEHOLDER_SPEAKER_SLUG/">PLACEHOLDER_SPEAKER_NAME</a>, PLACEHOLDER_SPEAKER_ROLE, PLACEHOLDER_SPEAKER_ORG; <a href="/speakers/PLACEHOLDER_SPEAKER_SLUG_2/">PLACEHOLDER_SPEAKER_NAME_2</a>, PLACEHOLDER_SPEAKER_ROLE_2, PLACEHOLDER_SPEAKER_ORG_2</p>
        </div>
      </li>
      <li class="session" data-track="t1">
        <p class="when"><time>PLACEHOLDER_TIME</time> <span class="hall">PLACEHOLDER_HALL</span></p>
        <div>
          <span class="track t1">T1 &middot; Frontier Models &amp; Compute</span>
          <h3>PLACEHOLDER_SESSION_TITLE</h3>
          <p class="speakers"><a href="/speakers/PLACEHOLDER_SPEAKER_SLUG/">PLACEHOLDER_SPEAKER_NAME</a>, PLACEHOLDER_SPEAKER_ROLE, PLACEHOLDER_SPEAKER_ORG; <a href="/speakers/PLACEHOLDER_SPEAKER_SLUG_2/">PLACEHOLDER_SPEAKER_NAME_2</a>, PLACEHOLDER_SPEAKER_ROLE_2, PLACEHOLDER_SPEAKER_ORG_2</p>
        </div>
      </li>
      <li class="session" data-track="t2">
        <p class="when"><time>PLACEHOLDER_TIME</time> <span class="hall">PLACEHOLDER_HALL</span></p>
        <div>
          <span class="track t2">T2 &middot; Sovereign AI &amp; Geopolitics</span>
          <h3>PLACEHOLDER_SESSION_TITLE</h3>
          <p class="speakers"><a href="/speakers/PLACEHOLDER_SPEAKER_SLUG/">PLACEHOLDER_SPEAKER_NAME</a>, PLACEHOLDER_SPEAKER_ROLE, PLACEHOLDER_SPEAKER_ORG; <a href="/speakers/PLACEHOLDER_SPEAKER_SLUG_2/">PLACEHOLDER_SPEAKER_NAME_2</a>, PLACEHOLDER_SPEAKER_ROLE_2, PLACEHOLDER_SPEAKER_ORG_2</p>
        </div>
      </li>
      <li class="session">
        <p class="when"><time>PLACEHOLDER_TIME</time> <span class="hall">PLACEHOLDER_HALL</span></p>
        <div>
          <h3>Lunch and networking</h3>
        </div>
      </li>
      <li class="session" data-track="t3">
        <p class="when"><time>PLACEHOLDER_TIME</time> <span class="hall">PLACEHOLDER_HALL</span></p>
        <div>
          <span class="track t3">T3 &middot; Enterprise AI in Production</span>
          <h3>PLACEHOLDER_SESSION_TITLE</h3>
          <p class="speakers"><a href="/speakers/PLACEHOLDER_SPEAKER_SLUG/">PLACEHOLDER_SPEAKER_NAME</a>, PLACEHOLDER_SPEAKER_ROLE, PLACEHOLDER_SPEAKER_ORG; <a href="/speakers/PLACEHOLDER_SPEAKER_SLUG_2/">PLACEHOLDER_SPEAKER_NAME_2</a>, PLACEHOLDER_SPEAKER_ROLE_2, PLACEHOLDER_SPEAKER_ORG_2</p>
        </div>
      </li>
      <li class="session">
        <p class="when"><time>PLACEHOLDER_TIME</time> <span class="hall">PLACEHOLDER_HALL</span></p>
        <div>
          <h3>PLACEHOLDER_CLOSING_SESSION_TITLE</h3>
        </div>
      </li>
    </ol>
  </section>

  <section class="day" id="day-2" aria-labelledby="day-2-h">
    <h2 id="day-2-h">Day 2, 15 Oct</h2>
    <ol class="sessions">
      <!-- One <li> per session, in time order. Copy a row, set data-track and the .track class to t1-t7, link every speaker to /speakers/<slug>/ (slugs as in speakers.json). Leave out any speaker who is not confirmed. -->
      <li class="session">
        <p class="when"><time>PLACEHOLDER_TIME</time> <span class="hall">PLACEHOLDER_HALL</span></p>
        <div>
          <h3>Registration and networking</h3>
        </div>
      </li>
      <li class="session">
        <p class="when"><time>PLACEHOLDER_TIME</time> <span class="hall">PLACEHOLDER_HALL</span></p>
        <div>
          <h3>PLACEHOLDER_OPENING_SESSION_TITLE</h3>
          <p class="speakers"><a href="/speakers/PLACEHOLDER_SPEAKER_SLUG/">PLACEHOLDER_SPEAKER_NAME</a>, PLACEHOLDER_SPEAKER_ROLE, PLACEHOLDER_SPEAKER_ORG; <a href="/speakers/PLACEHOLDER_SPEAKER_SLUG_2/">PLACEHOLDER_SPEAKER_NAME_2</a>, PLACEHOLDER_SPEAKER_ROLE_2, PLACEHOLDER_SPEAKER_ORG_2</p>
        </div>
      </li>
      <li class="session" data-track="t1">
        <p class="when"><time>PLACEHOLDER_TIME</time> <span class="hall">PLACEHOLDER_HALL</span></p>
        <div>
          <span class="track t1">T1 &middot; Frontier Models &amp; Compute</span>
          <h3>PLACEHOLDER_SESSION_TITLE</h3>
          <p class="speakers"><a href="/speakers/PLACEHOLDER_SPEAKER_SLUG/">PLACEHOLDER_SPEAKER_NAME</a>, PLACEHOLDER_SPEAKER_ROLE, PLACEHOLDER_SPEAKER_ORG; <a href="/speakers/PLACEHOLDER_SPEAKER_SLUG_2/">PLACEHOLDER_SPEAKER_NAME_2</a>, PLACEHOLDER_SPEAKER_ROLE_2, PLACEHOLDER_SPEAKER_ORG_2</p>
        </div>
      </li>
      <li class="session" data-track="t2">
        <p class="when"><time>PLACEHOLDER_TIME</time> <span class="hall">PLACEHOLDER_HALL</span></p>
        <div>
          <span class="track t2">T2 &middot; Sovereign AI &amp; Geopolitics</span>
          <h3>PLACEHOLDER_SESSION_TITLE</h3>
          <p class="speakers"><a href="/speakers/PLACEHOLDER_SPEAKER_SLUG/">PLACEHOLDER_SPEAKER_NAME</a>, PLACEHOLDER_SPEAKER_ROLE, PLACEHOLDER_SPEAKER_ORG; <a href="/speakers/PLACEHOLDER_SPEAKER_SLUG_2/">PLACEHOLDER_SPEAKER_NAME_2</a>, PLACEHOLDER_SPEAKER_ROLE_2, PLACEHOLDER_SPEAKER_ORG_2</p>
        </div>
      </li>
      <li class="session">
        <p class="when"><time>PLACEHOLDER_TIME</time> <span class="hall">PLACEHOLDER_HALL</span></p>
        <div>
          <h3>Lunch and networking</h3>
        </div>
      </li>
      <li class="session" data-track="t3">
        <p class="when"><time>PLACEHOLDER_TIME</time> <span class="hall">PLACEHOLDER_HALL</span></p>
        <div>
          <span class="track t3">T3 &middot; Enterprise AI in Production</span>
          <h3>PLACEHOLDER_SESSION_TITLE</h3>
          <p class="speakers"><a href="/speakers/PLACEHOLDER_SPEAKER_SLUG/">PLACEHOLDER_SPEAKER_NAME</a>, PLACEHOLDER_SPEAKER_ROLE, PLACEHOLDER_SPEAKER_ORG; <a href="/speakers/PLACEHOLDER_SPEAKER_SLUG_2/">PLACEHOLDER_SPEAKER_NAME_2</a>, PLACEHOLDER_SPEAKER_ROLE_2, PLACEHOLDER_SPEAKER_ORG_2</p>
        </div>
      </li>
      <li class="session">
        <p class="when"><time>PLACEHOLDER_TIME</time> <span class="hall">PLACEHOLDER_HALL</span></p>
        <div>
          <h3>PLACEHOLDER_CLOSING_SESSION_TITLE</h3>
        </div>
      </li>
    </ol>
  </section>

  <section class="legend" id="tracks" aria-labelledby="tracks-h">
    <h2 id="tracks-h">Tracks</h2>
    <ul>
      <li><span class="track t1">T1</span> Frontier Models &amp; Compute</li>
      <li><span class="track t2">T2</span> Sovereign AI &amp; Geopolitics</li>
      <li><span class="track t3">T3</span> Enterprise AI in Production</li>
      <li><span class="track t4">T4</span> GCCs</li>
      <li><span class="track t5">T5</span> Robotics, Agents &amp; Embodied AI</li>
      <li><span class="track t6">T6</span> AI for Bharat</li>
      <li><span class="track t7">T7</span> Capital, Founders &amp; Exits</li>
    </ul>
  </section>

  <section class="awards" id="awards" aria-labelledby="awards-h">
    <h2 id="awards-h">World AI Awards presentation</h2>
    <p><time datetime="PLACEHOLDER_AWARDS_DATE_YYYY-MM-DD">PLACEHOLDER_AWARDS_DAY_AND_DATE</time>, PLACEHOLDER_AWARDS_TIME IST, PLACEHOLDER_AWARDS_HALL.</p>
    <p>The World AI Awards 2026 are presented at the summit. <a href="/awards/">Nominations, categories and deadline</a> (PLACEHOLDER_AWARD_NOMINATION_DEADLINE).</p>
  </section>

  <p class="venue">Venue: Sheraton Grand Bangalore Hotel at Brigade Gateway, 26/1, Dr Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru, Karnataka 560055. <a href="/#venue">Venue and directions</a></p>
</main>

<aside class="sticky-cta" aria-label="Book your pass">
  <div class="wrap">
    <p>World AI Summit 2026, 14-15 October, Bengaluru. Delegate pass from PLACEHOLDER_CURRENT_PASS_PRICE_TEXT.</p>
    <a href="/delegate/">Book delegate pass</a>
  </div>
</aside>

<footer class="wrap">
  <p>Registration: <a href="mailto:registration@worldaisummit.com">registration@worldaisummit.com</a> &middot; Partnerships: <a href="mailto:partnerships@worldaisummit.com">partnerships@worldaisummit.com</a> &middot; Secretariat: <a href="mailto:secretariat@worldaisummit.com">secretariat@worldaisummit.com</a></p>
</footer>
</body>
</html>

==================================================================
2) HEADER NAV, EVERY PAGE (homepage, /delegate/, /awards/, /speaker.html, /blog/ and posts, /partner-with-us.html, /ai-conference-bengaluru-2026.html, speaker pages)
Plain <a href> links in the HTML, not built by JavaScript, so Googlebot can crawl them. Add aria-current="page" on the link for the page it sits on.
==================================================================
<nav class="site-nav" aria-label="Primary">
  <a href="/delegate/">Passes</a>
  <a href="/agenda/">Agenda</a>
  <a href="/speaker.html">Speakers</a>
  <a href="/awards/">Awards</a>
  <a href="/#venue">Venue</a>
  <a href="/partner-with-us.html">Partner</a>
</nav>


==================================================================
3) HOMEPAGE VENUE ANCHOR (no new content)
The homepage already has the 'Where It All Comes Together' section with dates, venue and a 'Get Directions' link. Add the id to that section's existing opening tag. Add the scroll offset only if the header is sticky.
==================================================================
<section id="venue" ...existing attributes...>   <!-- the existing 'Where It All Comes Together' section -->

html { scroll-padding-top: 80px; }   /* only if the homepage header is sticky */


==================================================================
4) REDIRECTS (put these above any existing rules; every target is the final https://www URL, so each is one hop)
==================================================================
--- Apache (.htaccess at the web root) ---
RewriteEngine On

# /agenda without slash and /agenda.html -> /agenda/
RewriteRule ^agenda$ https://www.worldaisummit.com/agenda/ [R=301,L]
RewriteRule ^agenda\.html$ https://www.worldaisummit.com/agenda/ [R=301,L]

# /registration and /registration.html: today a 3-hop 302 chain to the homepage; send buyers to the pass page in one hop
RewriteRule ^registration(\.html)?/?$ https://www.worldaisummit.com/delegate/ [R=301,L]

# Host: non-www -> https://www (skip if this rule already exists; leave http->https to the host or CDN to avoid loops)
RewriteCond %{HTTP_HOST} ^worldaisummit\.com$ [NC]
RewriteRule ^(.*)$ https://www.worldaisummit.com/$1 [R=301,L]

--- nginx (inside the server blocks) ---
# in the https server block for www.worldaisummit.com
location = /agenda       { return 301 https://www.worldaisummit.com/agenda/; }
location = /agenda.html  { return 301 https://www.worldaisummit.com/agenda/; }
location ~ ^/registration(\.html)?/?$ { return 301 https://www.worldaisummit.com/delegate/; }

# host and protocol (skip if already present)
server {
    listen 80;
    server_name worldaisummit.com www.worldaisummit.com;
    return 301 https://www.worldaisummit.com$request_uri;
}
server {
    listen 443 ssl;
    server_name worldaisummit.com;
    # ssl_certificate / ssl_certificate_key as for the www block
    return 301 https://www.worldaisummit.com$request_uri;
}

Test after upload (each should show a single 301 to the final URL):
curl -sI https://www.worldaisummit.com/agenda | grep -i -E '^(HTTP|location)'
curl -sI https://worldaisummit.com/registration.html | grep -i -E '^(HTTP|location)'


==================================================================
5) SITEMAP ENTRY (add to the existing sitemap.xml)
==================================================================
<url>
  <loc>https://www.worldaisummit.com/agenda/</loc>
  <lastmod>PLACEHOLDER_PUBLISH_DATE_YYYY-MM-DD</lastmod>
</url>


==================================================================
6) POST-EVENT CHANGES, 16 OCTOBER 2026
==================================================================
--- 6a) Homepage hero: replace the hero text and buttons. If the existing H1 already contains 'World AI Summit', keep it. ---
<section class="hero hero-post-event" aria-label="World AI Summit 2026 is over">
  <p class="hero-lead">World AI Summit 2026 is over. Thank you, Bengaluru.</p>
  <p>Read the <a href="PLACEHOLDER_HIGHLIGHTS_URL">highlights</a> and the <a href="PLACEHOLDER_AWARDS_2026_WINNERS_URL">World AI Awards 2026 winners</a>.</p>
  <p>Partner with World AI Summit 2027: <a href="mailto:partnerships@worldaisummit.com?subject=World%20AI%20Summit%202027%20partnership">partnerships@worldaisummit.com</a></p>
</section>

--- 6b) /agenda/ sticky bar: replace the <aside class="sticky-cta"> contents ---
<aside class="sticky-cta" aria-label="Partner with World AI Summit 2027">
  <div class="wrap">
    <p>World AI Summit 2026 is over. Thank you, Bengaluru.</p>
    <a href="mailto:partnerships@worldaisummit.com?subject=World%20AI%20Summit%202027%20partnership">Partner with World AI Summit 2027</a>
  </div>
</aside>

--- 6c) /agenda/ intro: replace the second intro paragraph ---
<p>World AI Summit 2026 took place on 14-15 October at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. This is the programme as it ran. Read the <a href="PLACEHOLDER_HIGHLIGHTS_URL">highlights</a>.</p>

--- 6d) /agenda/ JSON-LD: delete the whole "offers" object from the Event. Keep eventStatus as EventScheduled, because schema.org has no 'completed' status. Keep the page live and do not redirect it.
