# A67: World AI Summit 2026 /agenda/ hub: head blocks for 3 phases, JSON-LD, page HTML, highlights lead box, live-entry template, Apache and nginx redirects

- **For recommendation:** Bring back /agenda/ as one URL that serves as the agenda before the event, a live page during it and the highlights recap afterwards
- **Research lens:** event-week-postevent
- **Format:** HTML snippets (head per phase, JSON-LD, body sections, inline JS) plus Apache .htaccess and nginx redirect rules and an internal-link list. Full copy is also saved at /tmp/claude-0/-home-user-123/bf9e82cf-ebf4-58a1-ab65-7230ef80c0ff/scratchpad/agenda-asset.txt
- **Placeholders the business must fill:**
  - PLACEHOLDER_OG_IMAGE_1200x630 (social share image path)
  - PLACEHOLDER_EVENT_IMAGE_1200x675 (Event schema image path)
  - PLACEHOLDER_PASS_NAME (pass on sale now, e.g. Late Access or Premium)
  - PLACEHOLDER_PASS_PRICE (current lowest pass price as a plain number; Standard ended 30 Sept 2026)
  - PLACEHOLDER_AWARD_DEADLINE_TEXT (World AI Awards 2026 nomination deadline, or remove the link if nominations are closed)
  - PLACEHOLDER_DAY2_PASS_OFFER (Day 2 or walk-in pass offer shown on 14 Oct)
  - PLACEHOLDER_HHMM / PLACEHOLDER_START / PLACEHOLDER_END / PLACEHOLDER_SESSION_TITLE / PLACEHOLDER_TRACK / PLACEHOLDER_HALL (final agenda from the programme team by 8 Oct)
  - PLACEHOLDER_SPEAKER_TBC (sessions whose speakers are not yet confirmed)
  - PLACEHOLDER_YOUTUBE_CHANNEL_URL
  - PLACEHOLDER_VIDEO_ID (per embedded session)
  - PLACEHOLDER_TOP_PASS_NAME (name of the tier that includes photos and videos)
  - PLACEHOLDER_FORM_ENDPOINT (form backend URL)
  - PLACEHOLDER_PHASE_1_2_OR_3 (hidden field, set at each phase switch)
  - PLACEHOLDER_PRIVACY_POLICY_URL
  - PLACEHOLDER_AWARDS_INBOX (who receives World AI Awards 2027 interest: partnerships@ or secretariat@)
  - PLACEHOLDER_REGISTRATION_OPEN_TIME (registration desk opening time, IST)
  - Decision: are the World AI Awards 2026 presented at the summit? If not, drop the Winners section and the 'winners' phrase in the Phase 3 meta description
  - Decision: confirm or remove each of the 50 performers in the Event JSON-LD

## How to ship

The relayed request was "do you have more CPUs from computer?". This run answers the computed task instead (the /agenda/ asset). The CPU question was not checked. Ask it again in the main session if you want an answer.

What changed from the recommendation, using the verifier's corrections:
- The lead box no longer offers full recordings. The homepage pricing block lists "Access to event photos & videos" as a benefit of the top pass, so giving recordings away for a form fill would undercut it. The box now offers short highlight clips and says full recordings come with the top pass.
- The search case is smaller than first claimed. Agenda, live and highlights queries for WAIS are below the reporting threshold, the old /agenda impressions were off-season spillover, and there is little link equity to win back. The real value is turning event-week visitors into Day 2 passes and 2027 leads. Do not promise a traffic number.
- The price is out of the Phase 1 meta description. The Standard price on /delegate/ ran out on 30 Sept 2026, so "from Rs 20,000" may now be wrong. The price sits only in the JSON-LD placeholder until someone confirms it.
- The page gives no edition number, because sources disagree on 2nd or 3rd.
- A Phase 2 meta description was missing and has been added. All three are 135-154 characters.

Order and deadlines:
1. 1-3 Oct, web dev: deploy the redirects (section E) on the server that answers non-www worldaisummit.com, and check them with the curl lines in E3. Point the homepage and /registration links straight at /agenda/. Ask Elets editorial to update the links in the cio and egov 2025 articles. Low priority: /world-ai-agneda.html (Google does not know it).
2. Now, someone with DNS access: verify the www property (https://www.worldaisummit.com/) in Search Console, by DNS TXT record or HTML file. Without it there is no "request indexing" (step 8) and no data, so indexing within the event window is not guaranteed. Also add /agenda/ to sitemap.xml and update its lastmod at each phase switch.
3. By 8 Oct, programme team: send final times, halls, session titles and confirmed speakers per session. There is no public day-wise agenda today. If they do not arrive by 8 Oct, publish Phase 1 with whatever is confirmed and mark the rest "Timings to be announced" rather than guess. Confirm the 50 JSON-LD performers and remove anyone unconfirmed.
4. Speaker links: the tables link to /speakers/<slug>/, which only exists once worldaisummit/speakers/dist is deployed. If it is not live by 8 Oct, find and replace /speakers/[slug]/ with /assets/speaker_details/<slug>.html.
5. 8 Oct: publish Phase 1 (A1+A2, B1+B3, section C with the Phase 1 H1 and intro), add the homepage nav, /delegate/ and /awards/ links (F), then request indexing if the www property is verified.
6. 14 Oct at 08:00 IST: swap in A3, the Phase 2 H1 and intro, and B2. Add the homepage hero link. The content team of 2 posts entries from template D every 30-60 min, with verbatim quotes from the recordings only, and updates dateModified. On 15 Oct, remove the "Join us on Day 2" button and change the hero to "Day 2 updates".
7. By 12:00 IST on 16 Oct: swap in A4 and the Phase 3 H1 and intro, rename "Live updates" to "Session highlights", add Winners if the awards were presented, change the nav label, and request indexing again.
8. Validate B1-B3 in the Rich Results Test (search.google.com/test/rich-results) after filling the placeholders. All three blocks parse as valid JSON as written. The performer list was built from speakers.json (confirmed_2026 = true, 50 people, ", IAS" removed from names).
9. Form backend: route by checkbox as in the C9 comment, and decide which inbox gets awards-2027 leads.

Sources checked now: the live homepage (Exa fetch, 1 Oct), which shows seven tracks, Premium Rs 20,000, top tier "Access to event photos & videos" and the contact emails. Hotel address: hotelplanner.com listing "26/1 Dr Rajkumar Rd, Malleswaram Rajajinagar 560055" (https://www.hotelplanner.com/Hotels/178731/Reservations-Sheraton-Bangalore-Hotel-at-Brigade-Gateway-Bangalore-26-1-Dr-Rajkumar-Rd-Malleswaram-Rajajinagar-560055) and the Marriott hotel page (https://www.marriott.com/en-us/hotels/blrgs-sheraton-grand-bangalore-hotel-at-brigade-gateway/overview/), for the Orion Mall walk and the skyway to the World Trade Centre. Metro: yometro.com and roaddistance.in, which put Sandal Soap Factory station about 0.3 km away (https://yometro.com/metro-station-near-sheraton-grand-bangalore-hotel-bengaluru). No OpenSEO paid tools were used. No repository files were edited. A working copy of the asset is at /tmp/claude-0/-home-user-123/bf9e82cf-ebf4-58a1-ab65-7230ef80c0ff/scratchpad/agenda-asset.txt

## Content

WORLD AI SUMMIT 2026: /agenda/ HUB (agenda now, live on 14-15 Oct, highlights from 16 Oct)
URL: https://www.worldaisummit.com/agenda/   File: /agenda/index.html (static HTML)

How to read this: replace every PLACEHOLDER_ before publishing. Text in [square brackets] is filled in for each session on the day. Keep the URL, the H1 position and the section ids the same in all three phases.

=====================================================================
A. <head> BLOCKS (swap the marked block at each phase switch)
=====================================================================

--- A1. Shared (all phases) ---
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="canonical" href="https://www.worldaisummit.com/agenda/">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:type" content="website">
<meta property="og:url" content="https://www.worldaisummit.com/agenda/">
<meta property="og:site_name" content="World AI Summit">
<meta property="og:image" content="https://www.worldaisummit.com/PLACEHOLDER_OG_IMAGE_1200x630.webp">
<meta name="twitter:card" content="summary_large_image">

--- A2. PHASE 1: publish by 8 Oct, keep until 07:59 IST on 14 Oct ---
<title>World AI Summit 2026 Agenda | Bengaluru, 14-15 October</title>
<meta name="description" content="Day-wise agenda for World AI Summit 2026, Bengaluru, 14-15 October: session timings, halls, tracks and speakers. Venue: Sheraton Grand at Brigade Gateway.">
<meta property="og:title" content="World AI Summit 2026 Agenda | Bengaluru, 14-15 October">
<meta property="og:description" content="Day-wise agenda: session timings, halls, tracks and speakers across seven tracks.">

--- A3. PHASE 2: switch at 08:00 IST on 14 Oct, keep until end of 15 Oct ---
<title>World AI Summit 2026 Live: Updates and Agenda | Bengaluru</title>
<meta name="description" content="Live updates from World AI Summit 2026, Bengaluru: what is on in each hall, key quotes, photos and session videos, plus the full Day 1 and Day 2 agenda.">
<meta property="og:title" content="World AI Summit 2026 Live: Updates and Agenda">
<meta property="og:description" content="What is on in each hall now, key quotes, photos and session videos.">

--- A4. PHASE 3: switch by 12:00 IST on 16 Oct, permanent ---
<title>World AI Summit 2026 Highlights: Day 1 and Day 2 Recap</title>
<meta name="description" content="Highlights from World AI Summit 2026, Bengaluru (14-15 Oct): key sessions, quotes, photos, videos and the World AI Awards 2026 winners.">
<meta property="og:title" content="World AI Summit 2026 Highlights: Day 1 and Day 2 Recap">
<meta property="og:description" content="Key sessions, quotes, photos and videos from both days in Bengaluru.">
(If the World AI Awards 2026 are not presented at the summit, end the description at "...photos and videos." and drop the Winners section.)

=====================================================================
B. JSON-LD (paste in <head>; B1 and B3 in all phases, B2 from 14 Oct)
=====================================================================
Performer list: the 50 people marked confirmed_2026 in worldaisummit/speakers/speakers.json. Before 8 Oct, ask the programme team to confirm each one and remove anyone they cannot confirm. Do not add a name from the agenda grid unless the programme team has confirmed it. Replace PLACEHOLDER_PASS_PRICE with a plain number, with no commas and no "Rs" (for example, the current lowest pass price shown on /delegate/).

--- B1. Event ---
<script type="application/ld+json">
{
"@context":"https://schema.org",
"@type":"Event",
"@id":"https://www.worldaisummit.com/#event-2026",
"name":"World AI Summit 2026",
"description":"Two-day AI conference in Bengaluru on 14-15 October 2026, organised by Elets Technomedia, with sessions across seven tracks: Frontier Models & Compute; Sovereign AI & Geopolitics; Enterprise AI in Production; Global Capability Centres (GCCs); Robotics, Agents & Embodied AI; AI for Bharat; and Capital, Founders & Exits.",
"url":"https://www.worldaisummit.com/",
"startDate":"2026-10-14",
"endDate":"2026-10-15",
"eventStatus":"https://schema.org/EventScheduled",
"eventAttendanceMode":"https://schema.org/OfflineEventAttendanceMode",
"inLanguage":"en-IN",
"image":["https://www.worldaisummit.com/PLACEHOLDER_EVENT_IMAGE_1200x675.webp"],
"location":{
 "@type":"Place",
 "name":"Sheraton Grand Bangalore Hotel at Brigade Gateway",
 "address":{
  "@type":"PostalAddress",
  "streetAddress":"26/1, Dr Rajkumar Road, Malleswaram-Rajajinagar",
  "addressLocality":"Bengaluru",
  "addressRegion":"Karnataka",
  "postalCode":"560055",
  "addressCountry":"IN"
 }
},
"organizer":{"@type":"Organization","name":"Elets Technomedia","url":"https://www.eletsonline.com/"},
"offers":{
 "@type":"Offer",
 "name":"PLACEHOLDER_PASS_NAME",
 "url":"https://www.worldaisummit.com/delegate/",
 "price":"PLACEHOLDER_PASS_PRICE",
 "priceCurrency":"INR",
 "availability":"https://schema.org/InStock"
},
"performer":[
{"@type":"Person","name":"Pankaj Kumar Pandey","jobTitle":"Principal Secretary, Department of Personnel and Administrative Reforms (e-Governance)","worksFor":{"@type":"Organization","name":"Government of Karnataka"}},
{"@type":"Person","name":"T Bhoobalan","jobTitle":"Chief Executive Officer, Centre for e-Governance, and Managing Director, KUIDFC","worksFor":{"@type":"Organization","name":"Government of Karnataka"}},
{"@type":"Person","name":"Sanjeev Rastogi","jobTitle":"Head - Group Policy Services","worksFor":{"@type":"Organization","name":"Adani Group"}},
{"@type":"Person","name":"Shalini Kapoor","jobTitle":"Chief Strategist - Data and AI","worksFor":{"@type":"Organization","name":"EkStep Foundation"}},
{"@type":"Person","name":"Dr Ravikumar Surpur","jobTitle":"Secretary, Information Technology & Communication Department; Secretary, Planning and Statistics Department; Chairman, RajComp Info Services Limited (RISL)","worksFor":{"@type":"Organization","name":"Government of Rajasthan"}},
{"@type":"Person","name":"Aman Mittal","jobTitle":"Joint Chief Executive Officer","worksFor":{"@type":"Organization","name":"Maharashtra Institution for Transformation (MITRA)"}},
{"@type":"Person","name":"Sanjeev Gupta","jobTitle":"Chief Executive Officer","worksFor":{"@type":"Organization","name":"Karnataka Digital Economy Mission"}},
{"@type":"Person","name":"Hemant Garg","jobTitle":"Deputy Director","worksFor":{"@type":"Organization","name":"Ministry of Labour and Employment, Government of India"}},
{"@type":"Person","name":"Prajeet Prabhakaran","jobTitle":"Regional Director","worksFor":{"@type":"Organization","name":"Embassy of Austria, Commercial Section"}},
{"@type":"Person","name":"Ram Mohan Rao","jobTitle":"Executive Director","worksFor":{"@type":"Organization","name":"Securities and Exchange Board of India (SEBI)"}},
{"@type":"Person","name":"M. Balasubramaniam (Bala MS)","jobTitle":"CEO, Stratinfinity Inc; Chairman, Southern Regional Committee, AICTE; Deputy Chairman, Ministry of Education & AICTE Investor Network","worksFor":{"@type":"Organization","name":"All India Council for Technical Education (AICTE)"}},
{"@type":"Person","name":"Mahesh Hariharan Iyer","jobTitle":"Vice President of Engineering","worksFor":{"@type":"Organization","name":"Reserve Bank Innovation Hub (RBIH)"}},
{"@type":"Person","name":"Dr. Sushil Kumar Meher","jobTitle":"Head, IT and CISO","worksFor":{"@type":"Organization","name":"All India Institute of Medical Sciences (AIIMS)"}},
{"@type":"Person","name":"Sandeep Varaganti","jobTitle":"CEO, JioMart","worksFor":{"@type":"Organization","name":"Reliance Retail"}},
{"@type":"Person","name":"George Inasu","jobTitle":"Managing Director and Country Head","worksFor":{"@type":"Organization","name":"Fidelity National Financial India"}},
{"@type":"Person","name":"Anand Ramakrishnan","jobTitle":"Managing Director","worksFor":{"@type":"Organization","name":"Equiniti India"}},
{"@type":"Person","name":"Tulshekar Gangireddy","jobTitle":"Executive Director & Head of Data Strategy","worksFor":{"@type":"Organization","name":"JPMorgan Chase & Co"}},
{"@type":"Person","name":"Deepak Mohanty","jobTitle":"Executive Director","worksFor":{"@type":"Organization","name":"Wells Fargo"}},
{"@type":"Person","name":"Anand Thakur","jobTitle":"Chief Product and Technology Officer","worksFor":{"@type":"Organization","name":"Reliance Retail"}},
{"@type":"Person","name":"Pawan Sachdeva","jobTitle":"Senior Managing Director and Technology Head - India","worksFor":{"@type":"Organization","name":"Carelon Global Solutions"}},
{"@type":"Person","name":"Pranav Saxena","jobTitle":"Chief Product and Technology Officer","worksFor":{"@type":"Organization","name":"API Holdings"}},
{"@type":"Person","name":"Suman Guha","jobTitle":"Chief Digital & Technology Officer","worksFor":{"@type":"Organization","name":"Tata Croma (Tata Digital)"}},
{"@type":"Person","name":"Avinash Naik","jobTitle":"Chief Information Officer","worksFor":{"@type":"Organization","name":"Bajaj Allianz General Insurance"}},
{"@type":"Person","name":"Harsh Vardhan","jobTitle":"Global Head - AI & Digital Innovation","worksFor":{"@type":"Organization","name":"Apollo Tyres Ltd"}},
{"@type":"Person","name":"Vijaya Kadiyala","jobTitle":"Executive Director","worksFor":{"@type":"Organization","name":"DBS Bank"}},
{"@type":"Person","name":"Shanmugam Manivannan","jobTitle":"Chief Digital Officer","worksFor":{"@type":"Organization","name":"Equitas Small Finance Bank"}},
{"@type":"Person","name":"Rajesh Choudhary","jobTitle":"Chief Information Officer","worksFor":{"@type":"Organization","name":"CSB Bank"}},
{"@type":"Person","name":"Dipayan Chakraborty","jobTitle":"Head, India Analytics Center","worksFor":{"@type":"Organization","name":"eBay"}},
{"@type":"Person","name":"Archana Menon","jobTitle":"Head of Analytics & Watches","worksFor":{"@type":"Organization","name":"Titan"}},
{"@type":"Person","name":"Deepika Sandeep","jobTitle":"Head - AI/ML CoE","worksFor":{"@type":"Organization","name":"HSBC"}},
{"@type":"Person","name":"Anil Varma","jobTitle":"Chief Technology Officer","worksFor":{"@type":"Organization","name":"Multi Commodity Exchange Clearing Corporation"}},
{"@type":"Person","name":"Deepak Sharma","jobTitle":"Independent Director","worksFor":{"@type":"Organization","name":"Suryoday Small Finance Bank"}},
{"@type":"Person","name":"Animesh Kishore","jobTitle":"Head, Centre of Excellence (CoE), Digital & Analytics","worksFor":{"@type":"Organization","name":"ITC Limited"}},
{"@type":"Person","name":"Sandeep Sharma","jobTitle":"Head of Technology & Product (eCommerce)","worksFor":{"@type":"Organization","name":"Shoppers Stop"}},
{"@type":"Person","name":"Shireen Ali","jobTitle":"Head, UK Data Enablement and Standards","worksFor":{"@type":"Organization","name":"HSBC"}},
{"@type":"Person","name":"Vishal Chugh","jobTitle":"EVP - Head Risk FRM","worksFor":{"@type":"Organization","name":"Tata Capital"}},
{"@type":"Person","name":"Shantanu Dasgupta","jobTitle":"Head of Digital Initiatives, Treasury & Transaction Banking","worksFor":{"@type":"Organization","name":"Axis Bank"}},
{"@type":"Person","name":"Sushan Rungta","jobTitle":"Chief Technology Officer","worksFor":{"@type":"Organization","name":"Absolute"}},
{"@type":"Person","name":"Ganesh Joshi","jobTitle":"Chief Information Officer (CIO)","worksFor":{"@type":"Organization","name":"Nilons Enterprises"}},
{"@type":"Person","name":"Praveen Bist","jobTitle":"Chief Information Officer","worksFor":{"@type":"Organization","name":"Amrita Hospitals"}},
{"@type":"Person","name":"Kuldeep T","jobTitle":"CISO & DPO","worksFor":{"@type":"Organization","name":"BigBasket"}},
{"@type":"Person","name":"Anshuma (Dogra) Singh","jobTitle":"Senior Director, India IT Head/Site Leader","worksFor":{"@type":"Organization","name":"Applied Materials"}},
{"@type":"Person","name":"Padmanaban TA","jobTitle":"DGM & Head of Digital Banking","worksFor":{"@type":"Organization","name":"Karnataka Bank"}},
{"@type":"Person","name":"Joyce Rodriguez","jobTitle":"Head of Digital Cybersecurity","worksFor":{"@type":"Organization","name":"Airbus India"}},
{"@type":"Person","name":"Pavankumar Gurazada","jobTitle":"Associate Director","worksFor":{"@type":"Organization","name":"Great Learning"}},
{"@type":"Person","name":"Aneelkumar (Aneel) Savalagi","jobTitle":"Global Chapter Leader - ICC (Innovation Capability Centre), Global DD&T (Data, Digital & Technology)","worksFor":{"@type":"Organization","name":"Takeda"}},
{"@type":"Person","name":"Sivakumar Selva Ganapathy","jobTitle":"VP - Software Engineering; Head - Open Blue India & APAC Solutions; Director - JCIPL","worksFor":{"@type":"Organization","name":"Johnson Controls"}},
{"@type":"Person","name":"Sandhya Vasudevan","jobTitle":"Board Member, TiE Bangalore; Former MD, Deutsche Bank & Thomson Reuters; Independent Director & Trustee","worksFor":{"@type":"Organization","name":"TiE Bangalore"}},
{"@type":"Person","name":"Suman Dash","jobTitle":"Chief Operating Officer","worksFor":{"@type":"Organization","name":"Acsel Technology Forum"}},
{"@type":"Person","name":"Shashank Randev","jobTitle":"Founder & General Partner","worksFor":{"@type":"Organization","name":"247VC"}}
]
}
</script>
(Keep eventStatus as EventScheduled after the event, because Google works out from the dates that it is over. Use EventPostponed or EventCancelled only if that actually happens.)

--- B2. LiveBlogPosting (add at 08:00 IST 14 Oct; one liveBlogUpdate per <article>, newest first; keep it after the event as the archive) ---
<script type="application/ld+json">
{
"@context":"https://schema.org",
"@type":"LiveBlogPosting",
"@id":"https://www.worldaisummit.com/agenda/#live",
"url":"https://www.worldaisummit.com/agenda/",
"headline":"World AI Summit 2026: Live Updates and Agenda",
"about":{"@id":"https://www.worldaisummit.com/#event-2026"},
"datePublished":"2026-10-14T08:00:00+05:30",
"dateModified":"2026-10-14T11:35:00+05:30",
"coverageStartTime":"2026-10-14T08:00:00+05:30",
"coverageEndTime":"2026-10-15T23:59:00+05:30",
"author":{"@type":"Organization","name":"Elets Technomedia","url":"https://www.eletsonline.com/"},
"publisher":{"@type":"Organization","name":"Elets Technomedia","url":"https://www.eletsonline.com/"},
"liveBlogUpdate":[
 {
  "@type":"BlogPosting",
  "headline":"[Session title], [Track], [Hall]",
  "url":"https://www.worldaisummit.com/agenda/#d1-1130",
  "datePublished":"2026-10-14T11:30:00+05:30",
  "articleBody":"[2-3 factual sentences, same text as the <p> in the entry]",
  "image":"https://www.worldaisummit.com/assets/img/2026/d1-1130-[slug].webp"
 }
]
}
</script>
(Update dateModified with every new entry. This is valid schema.org markup, but it does not guarantee a "Live" badge in Google.)

--- B3. Breadcrumb ---
<script type="application/ld+json">
{
"@context":"https://schema.org",
"@type":"BreadcrumbList",
"itemListElement":[
 {"@type":"ListItem","position":1,"name":"World AI Summit 2026","item":"https://www.worldaisummit.com/"},
 {"@type":"ListItem","position":2,"name":"Agenda","item":"https://www.worldaisummit.com/agenda/"}
]
}
</script>

=====================================================================
C. <body> CONTENT (in this order)
=====================================================================

<main id="agenda-hub">

<!-- C1. H1 + intro: swap per phase -->
<!-- PHASE 1 -->
<h1>World AI Summit 2026 Agenda</h1>
<p>World AI Summit 2026 takes place on Wednesday 14 and Thursday 15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. Below is the day-wise agenda with session timings (IST), tracks, halls and speakers across seven tracks. Timings can change; this page is updated as the programme is finalised.</p>
<p><a class="btn" href="/delegate/">Book a delegate pass</a> <a href="/awards/">World AI Awards nominations</a> (PLACEHOLDER_AWARD_DEADLINE_TEXT)</p>

<!-- PHASE 2 -->
<h1>World AI Summit 2026: Live Updates and Agenda</h1>
<p>World AI Summit 2026 is under way at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. Updates from each session appear below, newest first. Last updated: <time datetime="2026-10-14T11:35+05:30">14 Oct, 11:35 IST</time>.</p>
<p><a class="btn" href="/delegate/">Join us on Day 2: PLACEHOLDER_DAY2_PASS_OFFER</a></p> <!-- 14 Oct only; remove on 15 Oct -->

<!-- PHASE 3 -->
<h1>World AI Summit 2026 Highlights</h1>
<p>World AI Summit 2026 took place on 14 and 15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. This page brings together the key sessions, quotes, photos and videos from both days, with the full agenda below.</p>
<p><a class="btn" href="#highlights-signup">Register interest for World AI Summit 2027</a></p>

<!-- C2. Status strip (fills itself from the table rows during session times; hidden otherwise) -->
<p id="now-strip" class="now-strip" role="status" aria-live="polite" hidden></p>

<!-- C3. Jump links (show "Live updates" from 14 Oct, "Winners" from the awards night) -->
<nav class="jump" aria-label="On this page">
 <a href="#day-1">Day 1</a> <a href="#day-2">Day 2</a> <a href="#live">Live updates</a> <a href="#watch">Watch</a> <a href="#winners">Winners</a> <a href="#venue">Venue</a>
</nav>

<!-- C4. Live updates (from 08:00 IST 14 Oct; in Phase 3 rename the heading to "Session highlights") -->
<section id="live" aria-labelledby="live-h">
 <h2 id="live-h">Live updates</h2>
 <!-- newest entry first; template in section D -->
</section>

<!-- C5. Day 1 table. One <tr> per session. data-* attributes drive the status strip. -->
<section id="day-1" aria-labelledby="day1-h">
 <h2 id="day1-h">Day 1: Wednesday 14 October 2026</h2>
 <table>
  <caption>World AI Summit 2026, Day 1 agenda. All times IST (UTC+5:30).</caption>
  <thead><tr><th scope="col">Time (IST)</th><th scope="col">Session</th><th scope="col">Track</th><th scope="col">Hall</th><th scope="col">Speakers</th></tr></thead>
  <tbody>
   <tr id="s-d1-PLACEHOLDER_HHMM" data-start="2026-10-14TPLACEHOLDER_START:00+05:30" data-end="2026-10-14TPLACEHOLDER_END:00+05:30" data-hall="PLACEHOLDER_HALL" data-title="PLACEHOLDER_SESSION_TITLE">
    <td>PLACEHOLDER_START-PLACEHOLDER_END</td>
    <td>PLACEHOLDER_SESSION_TITLE</td>
    <td>PLACEHOLDER_TRACK</td>
    <td>PLACEHOLDER_HALL</td>
    <td><a href="/speakers/[slug]/">[Name]</a>, [Role], [Org]; <a href="/speakers/[slug]/">[Name]</a>, [Role], [Org]</td>
   </tr>
   <!-- repeat per session; speakers not yet confirmed: write "PLACEHOLDER_SPEAKER_TBC" -->
  </tbody>
 </table>
</section>

<!-- C6. Day 2 table: same structure, dates 2026-10-15 -->
<section id="day-2" aria-labelledby="day2-h">
 <h2 id="day2-h">Day 2: Thursday 15 October 2026</h2>
 <table>
  <caption>World AI Summit 2026, Day 2 agenda. All times IST (UTC+5:30).</caption>
  <thead><tr><th scope="col">Time (IST)</th><th scope="col">Session</th><th scope="col">Track</th><th scope="col">Hall</th><th scope="col">Speakers</th></tr></thead>
  <tbody>
   <tr id="s-d2-PLACEHOLDER_HHMM" data-start="2026-10-15TPLACEHOLDER_START:00+05:30" data-end="2026-10-15TPLACEHOLDER_END:00+05:30" data-hall="PLACEHOLDER_HALL" data-title="PLACEHOLDER_SESSION_TITLE">
    <td>PLACEHOLDER_START-PLACEHOLDER_END</td><td>PLACEHOLDER_SESSION_TITLE</td><td>PLACEHOLDER_TRACK</td><td>PLACEHOLDER_HALL</td>
    <td><a href="/speakers/[slug]/">[Name]</a>, [Role], [Org]</td>
   </tr>
  </tbody>
 </table>
</section>
<!-- Track cell values, exactly as on the homepage: Frontier Models & Compute | Sovereign AI & Geopolitics | Enterprise AI in Production | Global Capability Centres (GCCs) | Robotics, Agents & Embodied AI | AI for Bharat | Capital, Founders & Exits -->

<!-- C7. Watch -->
<section id="watch" aria-labelledby="watch-h">
 <h2 id="watch-h">Watch</h2>
 <p>Selected sessions from World AI Summit 2026. More on our <a href="PLACEHOLDER_YOUTUBE_CHANNEL_URL">YouTube channel</a>.</p>
 <figure class="video">
  <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/PLACEHOLDER_VIDEO_ID" title="[Session title] at World AI Summit 2026, Bengaluru" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  <figcaption>[Session title], [Track], [Hall], [14 or 15] October 2026</figcaption>
 </figure>
</section>

<!-- C8. Winners (Phase 3, only if the World AI Awards 2026 are presented at the summit) -->
<section id="winners" aria-labelledby="winners-h">
 <h2 id="winners-h">World AI Awards 2026 winners</h2>
 <ul>
  <li><strong>[Category]</strong>: [Organisation], for [project name]</li>
 </ul>
 <p><a href="/awards/">About the World AI Awards</a></p>
</section>

<!-- C9. Lead box (CORRECTED: offers highlight clips, not full recordings, because "Access to event photos & videos" is a paid benefit of the top pass tier on the homepage) -->
<section id="highlights-signup" class="lead-box" aria-labelledby="lead-h">
 <h2 id="lead-h">Get the session highlights</h2>
 <!-- Phase 1 heading: "Cannot attend? Get the session highlights" -->
 <p>We will email you short highlight clips from World AI Summit 2026 sessions. Full session recordings and event photos are included with the PLACEHOLDER_TOP_PASS_NAME pass.</p>
 <form action="PLACEHOLDER_FORM_ENDPOINT" method="post">
  <input type="hidden" name="source" value="agenda-hub">
  <input type="hidden" name="phase" value="PLACEHOLDER_PHASE_1_2_OR_3">
  <p class="hp" aria-hidden="true"><label>Leave this empty <input type="text" name="website" tabindex="-1" autocomplete="off"></label></p>
  <p><label for="lb-name">Full name</label><input id="lb-name" name="name" type="text" autocomplete="name" required></p>
  <p><label for="lb-email">Work email</label><input id="lb-email" name="email" type="email" autocomplete="email" required></p>
  <p><label for="lb-company">Company</label><input id="lb-company" name="company" type="text" autocomplete="organization" required></p>
  <p><label for="lb-desig">Designation</label><input id="lb-desig" name="designation" type="text" autocomplete="organization-title" required></p>
  <p><label for="lb-mobile">Mobile</label><input id="lb-mobile" name="mobile" type="tel" autocomplete="tel" inputmode="tel" minlength="10" required></p>
  <fieldset>
   <legend>I am interested in</legend>
   <label><input type="checkbox" name="interest" value="highlights" checked> Session highlights from World AI Summit 2026</label>
   <label><input type="checkbox" name="interest" value="delegate-2027"> World AI Summit 2027 delegate pass</label>
   <label><input type="checkbox" name="interest" value="sponsor-2027"> Sponsorship or exhibition, 2027</label>
   <label><input type="checkbox" name="interest" value="awards-2027"> World AI Awards 2027 nomination</label>
  </fieldset>
  <p><label><input type="checkbox" name="consent" value="yes" required> I agree that Elets Technomedia may contact me by email, phone or WhatsApp about the options I have ticked. I can withdraw consent at any time by writing to registration@worldaisummit.com. <a href="PLACEHOLDER_PRIVACY_POLICY_URL">Privacy policy</a></label></p>
  <p><button type="submit">Send</button></p>
 </form>
</section>
<!-- Routing (form backend): highlights -> registration@worldaisummit.com | delegate-2027 -> registration@worldaisummit.com | sponsor-2027 -> partnerships@worldaisummit.com | awards-2027 -> PLACEHOLDER_AWARDS_INBOX. A submission with several boxes ticked goes to every matching inbox. Drop any submission where "website" is filled. The consent box must never be pre-ticked. -->

<!-- C10. Venue and directions -->
<section id="venue" aria-labelledby="venue-h">
 <h2 id="venue-h">Venue and directions</h2>
 <p><strong>Sheraton Grand Bangalore Hotel at Brigade Gateway</strong><br>
 26/1, Dr Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru, Karnataka 560055</p>
 <ul>
  <li>Metro: Sandal Soap Factory station is about 300 m away, roughly a five-minute walk.</li>
  <li>Landmarks: Orion Mall is less than five minutes' walk away, and the hotel has a skyway to the World Trade Centre at Brigade Gateway.</li>
  <li>Registration desk opens at PLACEHOLDER_REGISTRATION_OPEN_TIME IST on both days. Carry a photo ID and your pass confirmation.</li>
 </ul>
 <p><a href="https://www.google.com/maps/search/?api=1&amp;query=Sheraton+Grand+Bangalore+Hotel+at+Brigade+Gateway">Open in Google Maps</a></p>
 <p>Questions about passes: registration@worldaisummit.com. Sponsorship and exhibition: partnerships@worldaisummit.com. Speaking: secretariat@worldaisummit.com.</p>
</section>

</main>

<!-- C11. Status strip script (before </body>). Uses textContent only. -->
<script>
(function () {
  var strip = document.getElementById('now-strip');
  var rows = document.querySelectorAll('tr[data-start]');
  function tick() {
    var now = Date.now(), live = [];
    rows.forEach(function (r) {
      var s = Date.parse(r.dataset.start), e = Date.parse(r.dataset.end);
      if (now >= s && now < e) live.push('Now in ' + r.dataset.hall + ': ' + r.dataset.title);
    });
    strip.textContent = live.join(' | ');
    strip.hidden = live.length === 0;
  }
  tick();
  setInterval(tick, 60000);
})();
</script>

=====================================================================
D. LIVE UPDATE ENTRY TEMPLATE (insert at the top of #live; one per session, or every 30-60 min)
=====================================================================
id format: d1 or d2, then the 24-hour start time. Quotes must be verbatim from the recording; if there is no clean quote, leave out the <blockquote>. Never paraphrase inside quote marks. Describe only what was said on stage, and do not write bios from memory.

<article id="d1-1130">
 <time datetime="2026-10-14T11:30+05:30">14 Oct, 11:30 IST</time>
 <h3>[Session title], [Track], [Hall]</h3>
 <p>[2-3 factual sentences: who spoke, the main point, any announcement or number given on stage.]</p>
 <blockquote>"[verbatim quote from recording]" - [Name], [Role], [Org]</blockquote>
 <figure>
  <img src="/assets/img/2026/d1-1130-[slug].webp" alt="[Name] of [Org] speaking on [topic] at World AI Summit 2026, Bengaluru" width="1200" height="800" loading="lazy">
  <figcaption>Left to right: [names, roles]</figcaption>
 </figure>
 <a href="[YouTube URL]">Watch the session</a>
</article>
(Leave out the "Watch the session" link until the video is public. Add the matching liveBlogUpdate object to B2 and update dateModified.)

=====================================================================
E. REDIRECTS (one hop each, straight to https://www.worldaisummit.com/agenda/)
=====================================================================
Put these on the server that answers worldaisummit.com (non-www). The 5xx on worldaisummit.com/agenda suggests the non-www host may be a separate or old server, so the rules must live there. Use mod_rewrite only. Do not mix in "Redirect" lines: they belong to a different module and can fire in an unexpected order.

--- E1. Apache .htaccess (site root, above any existing rewrite rules) ---
RewriteEngine On

# Non-www /agenda and /agenda/ (the URL Google has indexed, now 5xx)
RewriteCond %{HTTP_HOST} ^worldaisummit\.com$ [NC]
RewriteRule ^agenda/?$ https://www.worldaisummit.com/agenda/ [R=301,L]

# www /agenda without the trailing slash
RewriteRule ^agenda$ https://www.worldaisummit.com/agenda/ [R=301,L]

# Retired 2025 agenda files at the root (both hosts). Not the /1st-edition/ versions.
RewriteRule ^world-ai-agenda\.html$ https://www.worldaisummit.com/agenda/ [R=301,L]
RewriteRule ^world-ai-agneda\.html$ https://www.worldaisummit.com/agenda/ [R=301,L]

# Direct requests for /agenda/index.html (THE_REQUEST avoids a loop with DirectoryIndex)
RewriteCond %{THE_REQUEST} \s/agenda/index\.html[\s?] [NC]
RewriteRule ^agenda/index\.html$ https://www.worldaisummit.com/agenda/ [R=301,L]

--- E2. nginx ---
# Non-www server block
server {
    server_name worldaisummit.com;
    # ...existing listen/ssl lines...
    location = /agenda               { return 301 https://www.worldaisummit.com/agenda/; }
    location = /agenda/              { return 301 https://www.worldaisummit.com/agenda/; }
    location = /world-ai-agenda.html { return 301 https://www.worldaisummit.com/agenda/; }
    location = /world-ai-agneda.html { return 301 https://www.worldaisummit.com/agenda/; }
}

# www server block (add inside the existing one)
server {
    server_name www.worldaisummit.com;
    # ...existing config...
    location = /agenda               { return 301 https://www.worldaisummit.com/agenda/; }
    location = /world-ai-agenda.html { return 301 https://www.worldaisummit.com/agenda/; }
    location = /world-ai-agneda.html { return 301 https://www.worldaisummit.com/agenda/; }
    # $request_uri is the original request, so this does not loop with "index index.html"
    if ($request_uri = /agenda/index.html) { return 301 https://www.worldaisummit.com/agenda/; }
}

--- E3. Check after deploy (each should show one 301, then 200) ---
curl -sIL https://worldaisummit.com/agenda | grep -iE '^(HTTP|location)'
curl -sIL https://worldaisummit.com/agenda/ | grep -iE '^(HTTP|location)'
curl -sIL https://www.worldaisummit.com/agenda | grep -iE '^(HTTP|location)'
curl -sIL https://www.worldaisummit.com/world-ai-agenda.html | grep -iE '^(HTTP|location)'
curl -sIL https://worldaisummit.com/world-ai-agenda.html | grep -iE '^(HTTP|location)'
curl -sI  https://www.worldaisummit.com/agenda/ | head -1     # expect 200

Priority: Google knows /agenda (non-www) and /world-ai-agenda.html, and both return 5xx today. Google does not know /world-ai-agneda.html, so that rule is housekeeping only.

=====================================================================
F. INTERNAL LINKS
=====================================================================
Homepage main nav (all phases):            <a href="/agenda/">Agenda</a>
  From 16 Oct, label it:                   <a href="/agenda/">2026 Highlights</a>
Homepage hero, 14 Oct only:                <a class="live-link" href="/agenda/#live">Live now: Day 1 updates</a>
Homepage hero, 15 Oct only:                <a class="live-link" href="/agenda/#live">Live now: Day 2 updates</a>
Homepage hero, from 16 Oct:                <a href="/agenda/">World AI Summit 2026 highlights</a>
/delegate/ (near the pass table):          <a href="/agenda/">See the day-wise agenda</a>
/awards/ (below the form):                 <a href="/agenda/">See the full summit agenda</a>
Replace these links rather than relying on the redirects: the www homepage and /registration link to /world-ai-agenda.html today, so point those links straight at /agenda/.
Ask Elets editorial to change the /agenda link in cio.eletsonline.com/article/what-to-expect-at-world-ai-summit-2025-agenda-highlights/74827/ and egov.eletsonline.com/2025/06/what-to-expect-at-world-ai-summit-2025-agenda-highlights/ to https://www.worldaisummit.com/agenda/.
Speaker pages built from worldaisummit/speakers/ already link to /agenda/ (site.agenda_url in speakers.json).
