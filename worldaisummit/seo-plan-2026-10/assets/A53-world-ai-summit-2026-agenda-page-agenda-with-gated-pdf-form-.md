# A53: World AI Summit 2026 agenda page (/agenda/) with gated PDF form, Event JSON-LD, thank-you page, redirects and internal-link snippets

- **For recommendation:** Publish a 2026 agenda page with a gated PDF download (Cypher /schedule, Inc42 talking points, World Summit AI 'Download Agenda')
- **Research lens:** competitors
- **Format:** HTML page (/agenda/index.html) with inline Event JSON-LD, a subEvent JSON block to add as sessions are confirmed, a noindex thank-you page, Apache .htaccess and nginx redirect rules, and HTML snippets for the homepage, the 2025 agenda page, speaker pages and sitemap.xml
- **Placeholders the business must fill:**
  - PLACEHOLDER_CURRENT_PREMIUM_PRICE / PLACEHOLDER_CURRENT_PREMIUM_PRICE_INR: price on sale from today. Standard (Rs 20,000) was valid till 30 Sept 2026 and /delegate/ lists Late Access at Rs 30,000, but the homepage still says Rs 20,000. Pick one and make the homepage, /delegate/ and the JSON-LD say the same thing. JSON-LD takes a plain number, e.g. "30000".
  - PLACEHOLDER_CURRENT_VIP_PRICE / PLACEHOLDER_CURRENT_VIP_PRICE_INR: VIP price on sale from today. /delegate/ shows Rs 35,000 Standard and Rs 60,000 Late Access.
  - PLACEHOLDER_EVENT_IMAGE_URL_1200x630: absolute URL of an event image, used for og:image and the JSON-LD image. Delete the JSON-LD image line if there isn't one.
  - PLACEHOLDER_FORM_ENDPOINT: the form handler URL, set to email registration@ and redirect to /agenda/thank-you/.
  - PLACEHOLDER_PRIVACY_POLICY_URL: Elets or World AI Summit privacy policy (needed for the DPDP consent line).
  - PLACEHOLDER_CONFIRMED_SPEAKER_COUNT: 50 as of 1 Oct 2026, per /assets/speaker_details/index.html.
  - PLACEHOLDER_LAST_UPDATED: date and time of each agenda update (two places).
  - PLACEHOLDER_SESSION_ID / _TITLE / _START / _END / _HALL / _TRACK_ID / _TRACK_NAME / _FORMAT: per confirmed session, from the Elets programme team only. Track ids: frontier, sovereign, enterprise, gcc, robotics, bharat, capital.
  - PLACEHOLDER_SPEAKER_NAME / _SLUG / _SPEAKER_TITLE_AND_ORG: confirmed 2026 speakers only, slug as in speakers.json.
  - PLACEHOLDER_AWARDS_DAY_AND_DATE / _AWARDS_TIME / _AWARDS_HALL / _AWARDS_DATE / _AWARDS_END: World AI Awards ceremony slot.
  - PLACEHOLDER_AWARDS_ACCESS_LINE: who can attend the ceremony.
  - PLACEHOLDER_AWARD_NOMINATION_DEADLINE: 2026 nomination close date. /awards/ shows no deadline today.
  - PLACEHOLDER_RECORDING_POLICY_2026: whether 2026 sessions are recorded, when and where recordings are shared, and which pass includes photo and video access.
  - PLACEHOLDER_SEATS_LEFT: optional, only if true and tracked.
  - PLACEHOLDER_DAY_AND_DATE / PLACEHOLDER_TIME: speaker-page session line.
  - PLACEHOLDER_PUBLISH_DATE_YYYY-MM-DD: sitemap lastmod.

## How to ship

The page works for lead capture and for converting visitors who are already on the site. Don't expect search traffic from it. OpenSEO returned no volume for any "world ai summit agenda/schedule" query. Search Console shows 0 "agenda" queries in the last 3 months. Publish by 6 Oct so it is live during the 7-13 Oct sales calls.

Steps:
1) Web dev: create /agenda/index.html from FILE 1, wrapped in the site header and footer, and create /agenda/thank-you/index.html from FILE 2. Point the form at the handler the /awards/ nomination form already uses. It should email registration@worldaisummit.com, then redirect to /agenda/thank-you/. Upload the PDF to /assets/agenda/world-ai-summit-2026-agenda.pdf. This is a soft gate: anyone with the PDF URL can open it, and the X-Robots-Tag header keeps it out of search results.
2) The page can go live today at track level with no sessions. In that case, delete the two placeholder table rows and keep the "Further sessions are added" lines. Add rows only for sessions the Elets programme team has confirmed. No session-level 2026 agenda exists anywhere public, and speakers.json has session = null for all 76 entries. Don't invent hall names; the hall name in the generator README is only an example.
3) Before publishing, fill the price placeholders (see placeholders) and the og/JSON-LD image. Then remove the EDITOR comments and test the JSON-LD in Google's Rich Results Test. The main Event block is valid JSON (checked by parsing it). Add the FILE 1b subEvent entries only after the times are fixed, and use 2026-10-15 for Day 2. They have no rich-result value. A cheaper schema win is separate from this page: the indexed /awards Event markup is missing organizer, offers and performer, and adding those fixes the warnings Google shows for it.
4) Apply the FILE 3 redirects (Apache or nginx, whichever serves the site). They point straight at the www URL, so the agenda redirects don't add a hop (the site already has 3-hop chains on /registration). Retargeting the 2025 "agenda-highlights" URL is optional and needs a decision first.
5) Add the snippets: Agenda in the homepage nav, a link under "Seven tracks. One agenda", a banner on the 2025 agenda page, and the sitemap entry. Speaker-page session lines are a per-page job. The live /assets/speaker_details pages use the exact wording build_speakers.py produces ("Session title, time and hall will be published on this page once the agenda is final."). Check whether they were generated. If they were, fill session {title, date, time, hall, format, track} in speakers.json and rebuild instead of editing about 51 files by hand.

Verified today (1 Oct 2026):
- Venue address: 26/1 Dr. Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru, Karnataka 560055, from the Marriott rooms page (marriott.com/en-us/hotels/blrgs-sheraton-grand-bangalore-hotel-at-brigade-gateway/rooms/) and the Google Hotels listing.
- Seven track names and descriptions, the theme line, "Premium Pass Rs 20,000" and the group 10% offer: Exa fetch of https://www.worldaisummit.com/. The live homepage shows seven tracks, so the six-track copy is a stale /index.html cache. I could not curl /index.html directly (proxy 403).
- Pass benefits and price tiers: /delegate/.
- The 50 performers: https://www.worldaisummit.com/assets/speaker_details/index.html says "50 confirmed speakers so far", and those names match the confirmed_2026 entries in speakers.json. URL pattern checked on two speaker pages. Priyank Kharge is left out: /speaker.html "welcomes" him, but speakers.json has confirmed_2026 = false. Add him only if the programme team confirms.
- 14 Oct 2026 is a Wednesday and 15 Oct a Thursday.

Left out on purpose: the edition number (sources conflict: 2nd vs 3rd), bios, and Inc42-style "talking points" (that format was not verified).

Organizer url eletsonline.com is inferred from Elets' own domains (events.eletsonline.com). Confirm it is the corporate site. No OpenSEO paid tools used; no files edited.

On the relayed question about CPUs: this sandbox reports 4 CPUs (nproc). I cannot add more from here.

## Content

==========================================================================
FILE 1 of 3: /agenda/index.html  (new page, canonical https://www.worldaisummit.com/agenda/)
Wrap <main> in the site's normal header/footer. Delete every HTML comment marked "EDITOR" before publishing.
==========================================================================
<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Agenda | World AI Summit 2026, 14-15 Oct, Bengaluru</title>
<meta name="description" content="World AI Summit 2026 agenda for 14-15 October in Bengaluru: seven tracks, session timings, halls and speakers. Download the agenda PDF.">
<link rel="canonical" href="https://www.worldaisummit.com/agenda/">
<meta name="robots" content="index, follow">
<meta property="og:type" content="website">
<meta property="og:site_name" content="World AI Summit">
<meta property="og:title" content="World AI Summit 2026 Agenda | 14-15 October, Bengaluru">
<meta property="og:description" content="Seven tracks across two days at Sheraton Grand Bangalore Hotel at Brigade Gateway. Session timings, halls and speakers, plus the agenda PDF.">
<meta property="og:url" content="https://www.worldaisummit.com/agenda/">
<meta property="og:image" content="PLACEHOLDER_EVENT_IMAGE_URL_1200x630">
<meta name="twitter:card" content="summary_large_image">

<!-- EDITOR: Event JSON-LD. Publish as is once the two price placeholders and the image URL are filled.
     When sessions are confirmed, add "subEvent": [ ... ] from FILE 1b just before "performer". -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Event",
  "@id": "https://www.worldaisummit.com/#event",
  "name": "World AI Summit 2026",
  "description": "World AI Summit 2026, Bengaluru: AI for All: Accelerating India's Journey Towards Inclusive, Responsible and Future-Ready AI. Two days, seven tracks, organised by Elets Technomedia.",
  "url": "https://www.worldaisummit.com/",
  "image": [
    "PLACEHOLDER_EVENT_IMAGE_URL_1200x630"
  ],
  "startDate": "2026-10-14",
  "endDate": "2026-10-15",
  "eventStatus": "https://schema.org/EventScheduled",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
  "inLanguage": "en-IN",
  "location": {
    "@type": "Place",
    "@id": "https://www.worldaisummit.com/agenda/#venue",
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
  "organizer": {
    "@type": "Organization",
    "name": "Elets Technomedia",
    "url": "https://www.eletsonline.com/"
  },
  "offers": [
    {
      "@type": "Offer",
      "name": "Premium Pass",
      "url": "https://www.worldaisummit.com/delegate/",
      "price": "PLACEHOLDER_CURRENT_PREMIUM_PRICE_INR",
      "priceCurrency": "INR",
      "availability": "https://schema.org/InStock"
    },
    {
      "@type": "Offer",
      "name": "VIP Pass",
      "url": "https://www.worldaisummit.com/delegate/",
      "price": "PLACEHOLDER_CURRENT_VIP_PRICE_INR",
      "priceCurrency": "INR",
      "availability": "https://schema.org/InStock"
    }
  ],
  "performer": [
    {"@type": "Person", "name": "Pankaj Kumar Pandey", "url": "https://www.worldaisummit.com/assets/speaker_details/pankaj-kumar-pandey.html"},
    {"@type": "Person", "name": "T Bhoobalan", "url": "https://www.worldaisummit.com/assets/speaker_details/t-bhoobalan.html"},
    {"@type": "Person", "name": "Sanjeev Rastogi", "url": "https://www.worldaisummit.com/assets/speaker_details/sanjeev-rastogi.html"},
    {"@type": "Person", "name": "Shalini Kapoor", "url": "https://www.worldaisummit.com/assets/speaker_details/shalini-kapoor.html"},
    {"@type": "Person", "honorificPrefix": "Dr", "name": "Ravikumar Surpur", "url": "https://www.worldaisummit.com/assets/speaker_details/ravikumar-surpur.html"},
    {"@type": "Person", "name": "Aman Mittal", "url": "https://www.worldaisummit.com/assets/speaker_details/aman-mittal.html"},
    {"@type": "Person", "name": "Sanjeev Gupta", "url": "https://www.worldaisummit.com/assets/speaker_details/sanjeev-gupta.html"},
    {"@type": "Person", "name": "Hemant Garg", "url": "https://www.worldaisummit.com/assets/speaker_details/hemant-garg.html"},
    {"@type": "Person", "name": "Prajeet Prabhakaran", "url": "https://www.worldaisummit.com/assets/speaker_details/prajeet-prabhakaran.html"},
    {"@type": "Person", "name": "Ram Mohan Rao", "url": "https://www.worldaisummit.com/assets/speaker_details/ram-mohan-rao.html"},
    {"@type": "Person", "name": "M. Balasubramaniam (Bala MS)", "url": "https://www.worldaisummit.com/assets/speaker_details/m-balasubramaniam.html"},
    {"@type": "Person", "name": "Mahesh Hariharan Iyer", "url": "https://www.worldaisummit.com/assets/speaker_details/mahesh-hariharan-iyer.html"},
    {"@type": "Person", "honorificPrefix": "Dr", "name": "Sushil Kumar Meher", "url": "https://www.worldaisummit.com/assets/speaker_details/sushil-kumar-meher.html"},
    {"@type": "Person", "name": "Sandeep Varaganti", "url": "https://www.worldaisummit.com/assets/speaker_details/sandeep-varaganti.html"},
    {"@type": "Person", "name": "George Inasu", "url": "https://www.worldaisummit.com/assets/speaker_details/george-inasu.html"},
    {"@type": "Person", "name": "Anand Ramakrishnan", "url": "https://www.worldaisummit.com/assets/speaker_details/anand-ramakrishnan.html"},
    {"@type": "Person", "name": "Tulshekar Gangireddy", "url": "https://www.worldaisummit.com/assets/speaker_details/tulshekar-gangireddy.html"},
    {"@type": "Person", "name": "Deepak Mohanty", "url": "https://www.worldaisummit.com/assets/speaker_details/deepak-mohanty.html"},
    {"@type": "Person", "name": "Anand Thakur", "url": "https://www.worldaisummit.com/assets/speaker_details/anand-thakur.html"},
    {"@type": "Person", "name": "Pawan Sachdeva", "url": "https://www.worldaisummit.com/assets/speaker_details/pawan-sachdeva.html"},
    {"@type": "Person", "name": "Pranav Saxena", "url": "https://www.worldaisummit.com/assets/speaker_details/pranav-saxena.html"},
    {"@type": "Person", "name": "Suman Guha", "url": "https://www.worldaisummit.com/assets/speaker_details/suman-guha.html"},
    {"@type": "Person", "name": "Avinash Naik", "url": "https://www.worldaisummit.com/assets/speaker_details/avinash-naik.html"},
    {"@type": "Person", "name": "Harsh Vardhan", "url": "https://www.worldaisummit.com/assets/speaker_details/harsh-vardhan.html"},
    {"@type": "Person", "name": "Vijaya Kadiyala", "url": "https://www.worldaisummit.com/assets/speaker_details/vijaya-kadiyala.html"},
    {"@type": "Person", "name": "Shanmugam Manivannan", "url": "https://www.worldaisummit.com/assets/speaker_details/shanmugam-manivannan.html"},
    {"@type": "Person", "name": "Rajesh Choudhary", "url": "https://www.worldaisummit.com/assets/speaker_details/rajesh-choudhary.html"},
    {"@type": "Person", "name": "Dipayan Chakraborty", "url": "https://www.worldaisummit.com/assets/speaker_details/dipayan-chakraborty.html"},
    {"@type": "Person", "name": "Archana Menon", "url": "https://www.worldaisummit.com/assets/speaker_details/archana-menon.html"},
    {"@type": "Person", "name": "Deepika Sandeep", "url": "https://www.worldaisummit.com/assets/speaker_details/deepika-sandeep.html"},
    {"@type": "Person", "name": "Anil Varma", "url": "https://www.worldaisummit.com/assets/speaker_details/anil-varma.html"},
    {"@type": "Person", "name": "Deepak Sharma", "url": "https://www.worldaisummit.com/assets/speaker_details/deepak-sharma.html"},
    {"@type": "Person", "name": "Animesh Kishore", "url": "https://www.worldaisummit.com/assets/speaker_details/animesh-kishore.html"},
    {"@type": "Person", "name": "Sandeep Sharma", "url": "https://www.worldaisummit.com/assets/speaker_details/sandeep-sharma.html"},
    {"@type": "Person", "name": "Shireen Ali", "url": "https://www.worldaisummit.com/assets/speaker_details/shireen-ali.html"},
    {"@type": "Person", "name": "Vishal Chugh", "url": "https://www.worldaisummit.com/assets/speaker_details/vishal-chugh.html"},
    {"@type": "Person", "name": "Shantanu Dasgupta", "url": "https://www.worldaisummit.com/assets/speaker_details/shantanu-dasgupta.html"},
    {"@type": "Person", "name": "Sushan Rungta", "url": "https://www.worldaisummit.com/assets/speaker_details/sushan-rungta.html"},
    {"@type": "Person", "name": "Ganesh Joshi", "url": "https://www.worldaisummit.com/assets/speaker_details/ganesh-joshi.html"},
    {"@type": "Person", "name": "Praveen Bist", "url": "https://www.worldaisummit.com/assets/speaker_details/praveen-bist.html"},
    {"@type": "Person", "name": "Kuldeep T", "url": "https://www.worldaisummit.com/assets/speaker_details/kuldeep-t.html"},
    {"@type": "Person", "name": "Anshuma (Dogra) Singh", "url": "https://www.worldaisummit.com/assets/speaker_details/anshuma-singh.html"},
    {"@type": "Person", "name": "Padmanaban TA", "url": "https://www.worldaisummit.com/assets/speaker_details/padmanaban-ta.html"},
    {"@type": "Person", "name": "Joyce Rodriguez", "url": "https://www.worldaisummit.com/assets/speaker_details/joyce-rodriguez.html"},
    {"@type": "Person", "name": "Pavankumar Gurazada", "url": "https://www.worldaisummit.com/assets/speaker_details/pavankumar-gurazada.html"},
    {"@type": "Person", "name": "Aneelkumar (Aneel) Savalagi", "url": "https://www.worldaisummit.com/assets/speaker_details/aneel-savalagi.html"},
    {"@type": "Person", "name": "Sivakumar Selva Ganapathy", "url": "https://www.worldaisummit.com/assets/speaker_details/sivakumar-selva-ganapathy.html"},
    {"@type": "Person", "name": "Sandhya Vasudevan", "url": "https://www.worldaisummit.com/assets/speaker_details/sandhya-vasudevan.html"},
    {"@type": "Person", "name": "Suman Dash", "url": "https://www.worldaisummit.com/assets/speaker_details/suman-dash.html"},
    {"@type": "Person", "name": "Shashank Randev", "url": "https://www.worldaisummit.com/assets/speaker_details/shashank-randev.html"}
  ]
}
</script>

<style>
  /* EDITOR: minimal styles; drop if the site stylesheet already covers tables, forms and details. */
  .agenda-wrap{max-width:1100px;margin:0 auto;padding:24px 16px}
  .agenda-status{border-left:4px solid currentColor;padding:8px 12px;margin:16px 0}
  .agenda-tracks{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;padding:0;list-style:none}
  .agenda-table{width:100%;border-collapse:collapse;margin:12px 0}
  .agenda-table th,.agenda-table td{border-bottom:1px solid #ddd;padding:10px 8px;text-align:left;vertical-align:top}
  .agenda-form{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:12px;max-width:760px}
  .agenda-form label{display:flex;flex-direction:column;gap:4px;font-weight:600}
  .agenda-form .full{grid-column:1/-1}
  .agenda-form .hp{position:absolute;left:-9999px}
  @media (max-width:700px){
    .agenda-table thead{display:none}
    .agenda-table tr{display:block;border-bottom:1px solid #ddd;padding:8px 0}
    .agenda-table td{display:block;border:0;padding:2px 0}
    .agenda-table td::before{content:attr(data-label) ": ";font-weight:600}
  }
</style>
</head>
<body>
<!-- EDITOR: site header + nav include here (nav must include <a href="/agenda/">Agenda</a>) -->

<main class="agenda-wrap" id="agenda">
  <nav aria-label="Breadcrumb"><a href="/">Home</a> &rsaquo; Agenda</nav>

  <h1>World AI Summit 2026 Agenda</h1>
  <p><strong>14-15 October 2026 &middot; Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru &middot; Organised by Elets Technomedia</strong></p>
  <p>World AI Summit 2026 brings policymakers, enterprise leaders, founders, investors and researchers together in Bengaluru for two days under the theme <em>AI for All: Accelerating India's Journey Towards Inclusive, Responsible and Future-Ready AI</em>. The programme runs across seven tracks, from frontier models and compute to capital, founders and exits. <a href="/assets/speaker_details/index.html">See the PLACEHOLDER_CONFIRMED_SPEAKER_COUNT speakers confirmed so far</a>.</p>

  <p class="agenda-status"><strong>Programme status:</strong> session titles, timings and halls are being finalised with speakers and are added to this page as each one is confirmed. Last updated PLACEHOLDER_LAST_UPDATED (IST). Programme subject to change.</p>

  <p><a href="#download">Download the agenda PDF</a> &middot; <a href="#day-1">Day 1</a> &middot; <a href="#day-2">Day 2</a> &middot; <a href="#awards-ceremony">Awards ceremony</a> &middot; <a href="/delegate/">Book your pass</a></p>

  <section aria-labelledby="tracks-h">
    <h2 id="tracks-h">Seven tracks</h2>
    <ul class="agenda-tracks">
      <li id="track-frontier"><h3>Frontier Models &amp; Compute</h3><p>Frontier AI models, advanced computing and the infrastructure behind next-generation AI.</p></li>
      <li id="track-sovereign"><h3>Sovereign AI &amp; Geopolitics</h3><p>AI sovereignty, national capability, data security and the shifting global AI landscape.</p></li>
      <li id="track-enterprise"><h3>Enterprise AI in Production</h3><p>How enterprises deploy AI at scale for efficiency, innovation and business transformation.</p></li>
      <li id="track-gcc"><h3>Global Capability Centres (GCCs)</h3><p>How GCCs drive AI innovation, talent development, R&amp;D and global technology leadership.</p></li>
      <li id="track-robotics"><h3>Robotics, Agents &amp; Embodied AI</h3><p>AI agents, robotics and autonomous systems in real-world use.</p></li>
      <li id="track-bharat"><h3>AI for Bharat</h3><p>AI for inclusive growth across governance, healthcare, education, agriculture and public services.</p></li>
      <li id="track-capital"><h3>Capital, Founders &amp; Exits</h3><p>AI startup funding, investment trends, scaling and pathways to exits.</p></li>
    </ul>
  </section>

  <section id="download" aria-labelledby="download-h">
    <h2 id="download-h">Download the agenda PDF</h2>
    <p>Get the programme as a PDF to plan your two days or share with your team. Fill in your details and the download opens on the next page.</p>
    <!-- EDITOR: point action at the same form handler the /awards/ nomination form uses, configured to email registration@worldaisummit.com
         and redirect to /agenda/thank-you/. Do not put the email address in a hidden field. -->
    <form class="agenda-form" action="PLACEHOLDER_FORM_ENDPOINT" method="post">
      <input type="hidden" name="source" value="agenda-pdf-2026">
      <label>Full name<input type="text" name="name" autocomplete="name" required></label>
      <label>Work email<input type="email" name="email" autocomplete="email" required></label>
      <label>Phone<input type="tel" name="phone" autocomplete="tel" inputmode="tel" placeholder="+91" required></label>
      <label>Company<input type="text" name="company" autocomplete="organization" required></label>
      <label>Designation<input type="text" name="designation" autocomplete="organization-title" required></label>
      <label class="hp" aria-hidden="true">Leave this empty<input type="text" name="website" tabindex="-1" autocomplete="off"></label>
      <label class="full" style="flex-direction:row;font-weight:400"><input type="checkbox" name="consent" value="yes" required> I agree that Elets Technomedia may contact me about World AI Summit 2026, as described in the <a href="PLACEHOLDER_PRIVACY_POLICY_URL">privacy policy</a>.</label>
      <button class="full" type="submit">Download agenda PDF</button>
    </form>
    <p><small>Group bookings and delegate questions: <a href="mailto:registration@worldaisummit.com">registration@worldaisummit.com</a></small></p>
  </section>

  <section id="day-1" aria-labelledby="day1-h">
    <h2 id="day1-h">Day 1: Wednesday, 14 October 2026</h2>
    <table class="agenda-table">
      <caption>Day 1 sessions. All times IST.</caption>
      <thead><tr><th scope="col">Time</th><th scope="col">Hall</th><th scope="col">Track</th><th scope="col">Session</th><th scope="col">Speakers</th></tr></thead>
      <tbody>
        <!-- EDITOR: one row per CONFIRMED session, in time order. Copy the row, fill it, delete unused rows.
             id format: d1-HHMM-short-title (for example d1-1115-sovereign-compute). Speakers: confirmed 2026 speakers only,
             linked to /assets/speaker_details/<slug>.html. Never add a speaker the programme team has not confirmed. -->
        <tr id="PLACEHOLDER_SESSION_ID">
          <td data-label="Time">PLACEHOLDER_START-PLACEHOLDER_END</td>
          <td data-label="Hall">PLACEHOLDER_HALL</td>
          <td data-label="Track"><a href="#track-PLACEHOLDER_TRACK_ID">PLACEHOLDER_TRACK_NAME</a></td>
          <td data-label="Session"><strong>PLACEHOLDER_SESSION_TITLE</strong><br>PLACEHOLDER_FORMAT (Keynote / Panel / Fireside / Roundtable)</td>
          <td data-label="Speakers"><a href="/assets/speaker_details/PLACEHOLDER_SLUG.html">PLACEHOLDER_SPEAKER_NAME</a>, PLACEHOLDER_SPEAKER_TITLE_AND_ORG</td>
        </tr>
      </tbody>
    </table>
    <p>Further Day 1 sessions are added here as they are confirmed.</p>
  </section>

  <section id="day-2" aria-labelledby="day2-h">
    <h2 id="day2-h">Day 2: Thursday, 15 October 2026</h2>
    <table class="agenda-table">
      <caption>Day 2 sessions. All times IST.</caption>
      <thead><tr><th scope="col">Time</th><th scope="col">Hall</th><th scope="col">Track</th><th scope="col">Session</th><th scope="col">Speakers</th></tr></thead>
      <tbody>
        <!-- EDITOR: same rules as Day 1; id format d2-HHMM-short-title. -->
        <tr id="PLACEHOLDER_SESSION_ID">
          <td data-label="Time">PLACEHOLDER_START-PLACEHOLDER_END</td>
          <td data-label="Hall">PLACEHOLDER_HALL</td>
          <td data-label="Track"><a href="#track-PLACEHOLDER_TRACK_ID">PLACEHOLDER_TRACK_NAME</a></td>
          <td data-label="Session"><strong>PLACEHOLDER_SESSION_TITLE</strong><br>PLACEHOLDER_FORMAT</td>
          <td data-label="Speakers"><a href="/assets/speaker_details/PLACEHOLDER_SLUG.html">PLACEHOLDER_SPEAKER_NAME</a>, PLACEHOLDER_SPEAKER_TITLE_AND_ORG</td>
        </tr>
      </tbody>
    </table>
    <p>Further Day 2 sessions are added here as they are confirmed.</p>
  </section>

  <section id="awards-ceremony" aria-labelledby="awards-h">
    <h2 id="awards-h">World AI Awards ceremony</h2>
    <p><strong>PLACEHOLDER_AWARDS_DAY_AND_DATE, PLACEHOLDER_AWARDS_TIME IST &middot; PLACEHOLDER_AWARDS_HALL</strong></p>
    <p>The World AI Awards recognise real-world applications of AI across business innovation, public sector transformation, startups, leadership and platforms. The ceremony is part of the summit programme. PLACEHOLDER_AWARDS_ACCESS_LINE (who can attend, for example all pass holders or invitees only).</p>
    <p>Nominations close PLACEHOLDER_AWARD_NOMINATION_DEADLINE. <a href="/awards/">Nominate your organisation</a></p>
  </section>

  <section id="book" aria-labelledby="book-h">
    <h2 id="book-h">Book your pass</h2>
    <p>The Premium Pass includes full summit access, the delegate kit, lunch and refreshments, and a certificate of participation. The VIP Pass adds priority seating, speaker lounge access and the networking dinner.</p>
    <p>Premium Pass PLACEHOLDER_CURRENT_PREMIUM_PRICE (Rs) &middot; VIP Pass PLACEHOLDER_CURRENT_VIP_PRICE (Rs). Groups of three or more delegates get 10% off.</p>
    <!-- EDITOR (optional, only if true): <p>PLACEHOLDER_SEATS_LEFT delegate seats remain.</p> -->
    <p><a class="btn" href="/delegate/">Book your pass</a></p>
    <p><small>Delegate questions: <a href="mailto:registration@worldaisummit.com">registration@worldaisummit.com</a> &middot; Sponsorship and exhibition: <a href="mailto:partnerships@worldaisummit.com">partnerships@worldaisummit.com</a> &middot; Speaking: <a href="mailto:secretariat@worldaisummit.com">secretariat@worldaisummit.com</a></small></p>
  </section>

  <section id="faq" aria-labelledby="faq-h">
    <h2 id="faq-h">Agenda FAQ</h2>
    <details open>
      <summary><h3 style="display:inline">Is the agenda final?</h3></summary>
      <p>Not yet. The seven tracks are set, and session titles, timings, halls and speakers are added to this page as each one is confirmed. The PDF is refreshed at the same time. This page was last updated PLACEHOLDER_LAST_UPDATED. The programme is subject to change.</p>
    </details>
    <details>
      <summary><h3 style="display:inline">Are sessions recorded?</h3></summary>
      <p>PLACEHOLDER_RECORDING_POLICY_2026 (say whether 2026 sessions will be recorded, when and where recordings will be shared, and whether photo and video access comes with a particular pass). Selected main-stage sessions from the previous edition can be watched on the <a href="/">homepage</a> under "Voices from the Main Stage".</p>
    </details>
    <details>
      <summary><h3 style="display:inline">Where is the summit held?</h3></summary>
      <p>Sheraton Grand Bangalore Hotel at Brigade Gateway, 26/1 Dr. Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru, Karnataka 560055.</p>
    </details>
  </section>
</main>

<!-- EDITOR: site footer include here -->
</body>
</html>

==========================================================================
FILE 1b: subEvent entries (add to the JSON-LD above only when a session's title, time and hall are confirmed)
Insert as  "subEvent": [ ... ],  immediately before "performer". Repeat the first object per session (use 2026-10-15 for Day 2);
keep the awards object only once its time and hall are fixed. Each url must match the row id in the table.
Note: Google shows no rich result for subEvent, so this is housekeeping, not a ranking lever.
==========================================================================
[
  {
    "@type": "Event",
    "name": "PLACEHOLDER_SESSION_TITLE",
    "url": "https://www.worldaisummit.com/agenda/#PLACEHOLDER_SESSION_ID",
    "startDate": "2026-10-14TPLACEHOLDER_START_HH:MM:00+05:30",
    "endDate": "2026-10-14TPLACEHOLDER_END_HH:MM:00+05:30",
    "eventStatus": "https://schema.org/EventScheduled",
    "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
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
      {"@type": "Person", "name": "PLACEHOLDER_SPEAKER_NAME", "url": "https://www.worldaisummit.com/assets/speaker_details/PLACEHOLDER_SLUG.html"}
    ]
  },
  {
    "@type": "Event",
    "name": "World AI Awards ceremony",
    "url": "https://www.worldaisummit.com/agenda/#awards-ceremony",
    "startDate": "PLACEHOLDER_AWARDS_DATE_2026-10-1XTHH:MM:00+05:30",
    "endDate": "PLACEHOLDER_AWARDS_END_2026-10-1XTHH:MM:00+05:30",
    "eventStatus": "https://schema.org/EventScheduled",
    "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
    "location": {
      "@type": "Place",
      "name": "PLACEHOLDER_AWARDS_HALL, Sheraton Grand Bangalore Hotel at Brigade Gateway",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "26/1 Dr. Rajkumar Road, Malleswaram-Rajajinagar",
        "addressLocality": "Bengaluru",
        "addressRegion": "Karnataka",
        "postalCode": "560055",
        "addressCountry": "IN"
      }
    }
  }
]

==========================================================================
FILE 2 of 3: /agenda/thank-you/index.html  (form redirect target; not in sitemap)
==========================================================================
<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Agenda PDF | World AI Summit 2026</title>
<meta name="robots" content="noindex, follow">
</head>
<body>
<!-- EDITOR: site header include -->
<main class="agenda-wrap">
  <h1>Your agenda PDF is ready</h1>
  <p><a href="/assets/agenda/world-ai-summit-2026-agenda.pdf" download>Download the World AI Summit 2026 agenda (PDF)</a></p>
  <p>The programme is subject to change. The latest version is always on the <a href="/agenda/">agenda page</a>.</p>
  <p>Passes for 14-15 October are available on the <a href="/delegate/">delegate page</a>. Groups of three or more get 10% off.</p>
</main>
<!-- EDITOR: site footer include -->
</body>
</html>

==========================================================================
FILE 3 of 3: redirects and PDF header
==========================================================================
# ---- Apache (.htaccess at web root; place above any existing catch-all rules) ----
<IfModule mod_rewrite.c>
RewriteEngine On
# Common guesses for the agenda URL go straight to the www canonical (one hop, no chain)
RewriteRule ^agenda$ https://www.worldaisummit.com/agenda/ [R=301,L]
RewriteRule ^(agenda|schedule|programme|program)\.html$ https://www.worldaisummit.com/agenda/ [R=301,L,NC]
RewriteRule ^(schedule|programme|program)/?$ https://www.worldaisummit.com/agenda/ [R=301,L,NC]
# Optional (decide first): the 2025 "agenda highlights" URL currently 302s to /1st-edition and sits in the sitemap.
# Make it a 301 to the 2026 agenda and remove it from sitemap.xml.
RewriteRule ^1st-edition/what-to-expect-world-ai-summit-2025-agenda-highlights/?$ https://www.worldaisummit.com/agenda/ [R=301,L]
</IfModule>
# Keep the gated PDF out of search results
<IfModule mod_headers.c>
<FilesMatch "^world-ai-summit-2026-agenda\.pdf$">
  Header set X-Robots-Tag "noindex, nofollow"
</FilesMatch>
</IfModule>

# ---- nginx (inside the server block for www.worldaisummit.com) ----
location = /agenda { return 301 https://www.worldaisummit.com/agenda/; }
location ~* ^/(agenda|schedule|programme|program)\.html$ { return 301 https://www.worldaisummit.com/agenda/; }
location ~* ^/(schedule|programme|program)/?$ { return 301 https://www.worldaisummit.com/agenda/; }
# Optional, same decision as above
location ~ ^/1st-edition/what-to-expect-world-ai-summit-2025-agenda-highlights/?$ { return 301 https://www.worldaisummit.com/agenda/; }
location = /assets/agenda/world-ai-summit-2026-agenda.pdf { add_header X-Robots-Tag "noindex, nofollow" always; }

==========================================================================
SNIPPETS for existing pages
==========================================================================
1) Homepage nav (and footer): add  <a href="/agenda/">Agenda</a>

2) Homepage, under the "Seven tracks. One agenda" heading block, after the seventh track:
   <p><a href="/agenda/">See the full agenda and download the PDF</a></p>

3) /1st-edition/world-ai-agenda.html (2025 archive), first line inside <main>:
   <p><strong>This is the 2025 programme.</strong> For 14-15 October 2026, see the <a href="https://www.worldaisummit.com/agenda/">World AI Summit 2026 agenda</a>.</p>

4) Speaker pages /assets/speaker_details/<slug>.html, once that speaker's session is confirmed. Replace the sentence
   "Session title, time and hall will be published on this page once the agenda is final." with:
   <p><strong>Session:</strong> PLACEHOLDER_SESSION_TITLE, PLACEHOLDER_DAY_AND_DATE, PLACEHOLDER_TIME IST, PLACEHOLDER_HALL &middot; <a href="/agenda/#PLACEHOLDER_SESSION_ID">View in agenda</a></p>

5) sitemap.xml:
   <url><loc>https://www.worldaisummit.com/agenda/</loc><lastmod>PLACEHOLDER_PUBLISH_DATE_YYYY-MM-DD</lastmod></url>
