# A11: World AI Summit 2026: one speaker directory on /speaker.html (50 confirmed names as HTML), booking button on each profile, Priyank Kharge fixes

- **For recommendation:** Merge the two speaker directories into /speaker.html with all 50 confirmed names as HTML text, and fix the contradictory Priyank Kharge details
- **Research lens:** site-deep-read
- **Format:** HTML snippets (head, body, JSON-LD), Apache .htaccess and nginx redirect rules, and find-and-replace copy for the speaker profile pages. Plain text with section headers.
- **Placeholders the business must fill:**
  - PLACEHOLDER_CURRENT_PASS_PRICE (visible copy, e.g. '30,000'; Standard Rs 20,000 lapsed on 30 Sept 2026 per /delegate/)
  - PLACEHOLDER_CURRENT_PASS_PRICE_INR (JSON-LD offers.price, number only, e.g. 30000)
  - PLACEHOLDER_EVENT_IMAGE_URL (absolute URL of an event image for og:image and JSON-LD; delete the JSON-LD image line if none)
  - PLACEHOLDER_AGENDA_URL (agenda page URL; omit the 'See the agenda' link until it exists)
  - PLACEHOLDER_KHARGE_2026_CONFIRMED (secretariat to confirm in writing whether Shri Priyank Kharge is attending 2026; until then he stays framed as 2025 Chief Guest and is excluded from the 50 and from performer)
  - PLACEHOLDER_CONFIRMED_SPEAKER_COUNT (only if sales wants to restate an expected total such as '100+'; otherwise drop the claim)
  - PLACEHOLDER_SESSION_TITLE / PLACEHOLDER_DAY_DATE / PLACEHOLDER_TIME / PLACEHOLDER_HALL (per profile, once the agenda is final)

## How to ship

Owner: web dev, plus the Elets secretariat for the Priyank Kharge check. Deadline: 5 Oct 2026. Effort: about 3 hours of dev work and 15 minutes for the secretariat.

Order of work:
1. Sales/secretariat fill in PLACEHOLDER_CURRENT_PASS_PRICE and PLACEHOLDER_CURRENT_PASS_PRICE_INR. On 1 Oct, /delegate/ shows Standard "valid till 30th Sept 2026" (now lapsed) and Late Access at Rs 30,000 / Rs 60,000, while every profile still says "from Rs 20,000". They also supply PLACEHOLDER_EVENT_IMAGE_URL, decide on PLACEHOLDER_AGENDA_URL (leave the link out if there is no agenda page) and answer PLACEHOLDER_KHARGE_2026_CONFIRMED.
2. On /speaker.html, paste sections 1 to 4: head tags, hero, the 50-name list in static HTML, and the JSON-LD. Remove the "100+ speakers" H1 and the "Welcoming Shri Priyank M Kharge" block.
3. Redirect /assets/speaker_details/index.html (section 5). Use Option A (.htaccess or nginx 301) if the host allows server rules, otherwise Option B (canonical plus instant meta refresh). Update sitemap.xml and the "All speakers" links on the profiles. In the two weeks before the event this is mainly cleanup: Google crawled both pages in the last 1-2 days, so crawling is not the bottleneck.
4. Add the booking block (section 6) to each of the 50 confirmed profiles. Apply the Priyank Kharge edits 7a to 7c now and 7d only after written confirmation.
5. Run the checks in section 8: Rich Results Test, view-source, a status-code check on all 50 links, and a curl check on the redirect.

What was verified on 1 Oct 2026: the 50 names, groups and short roles come from the live /assets/speaker_details/index.html (Exa fetch). /speaker.html, priyank-kharge.html, sanjeev-gupta.html and /delegate/ were fetched live. The venue address is 26/1 Dr Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru 560055 (Google Hotels, Apple Maps, Cvent). Kharge's June 2026 portfolio comes from Deccan Chronicle, as cited in the task. Profile slugs come from the local speakers.json and match the slug list collected by another lens. Only sanjeev-gupta and priyank-kharge were opened directly, so check that all 50 links return 200 after deploy. Nothing on disk was changed and no paid OpenSEO tools were used.

Expected impact is modest. "world ai summit speakers" is shared with the Amsterdam brand (worldsummit.ai holds #1, #3, #6 and #8), its volume is unknown, and Search Console shows zero 'speaker' rows for the non-www property. The surer gain is conversion: visitors from speakers' shared profile links during event week now see a booking button.

On your question about more CPUs: this sandbox reports 4 CPUs, and I cannot add more from inside the session.

## Content

WORLD AI SUMMIT 2026: ONE SPEAKER DIRECTORY ON /speaker.html, PROFILE BOOKING BUTTONS, PRIYANK KHARGE FIXES
Prepared 1 Oct 2026. Ship by 5 Oct 2026. Sources are in [brackets]. Replace every PLACEHOLDER_ before publishing.

====================================================================
1. /speaker.html <head>: replace the current title, meta description and any canonical/OG tags
====================================================================
<title>World AI Summit 2026 Speakers | 50 Confirmed, Bengaluru</title>
<meta name="description" content="Meet the 50 confirmed speakers at World AI Summit 2026, Bengaluru, 14-15 Oct: leaders from SEBI, KDEM, HSBC, JPMorgan Chase, Reliance Retail and more.">
<link rel="canonical" href="https://www.worldaisummit.com/speaker.html">
<meta property="og:type" content="website">
<meta property="og:url" content="https://www.worldaisummit.com/speaker.html">
<meta property="og:title" content="World AI Summit 2026 Speakers | 50 Confirmed, Bengaluru">
<meta property="og:description" content="Meet the 50 confirmed speakers at World AI Summit 2026, Bengaluru, 14-15 Oct: leaders from SEBI, KDEM, HSBC, JPMorgan Chase, Reliance Retail and more.">
<meta property="og:image" content="PLACEHOLDER_EVENT_IMAGE_URL">

Lengths: title 55 characters, meta 150 characters. The current title ("Speakers | World AI Summit 2026, Bengaluru") is already unique. The only duplicate is the meta description, which the page shares with the homepage (audit c1b16b55, duplicate-meta-description). This new meta fixes it.
Each time a speaker is confirmed, change "50" in the title, meta, og tags, sub-line and JSON-LD description, and add the speaker to the list and to "performer".

====================================================================
2. /speaker.html <body>: hero (replaces "2026 Speakers", the H1 "100+ speakers, one room in Bengaluru." and the paragraph below it)
====================================================================
The H1 "100+ speakers, one room in Bengaluru." says 100+, but the directory says 50 confirmed. Remove it. Use "100+" again only if sales confirms the number (PLACEHOLDER_CONFIRMED_SPEAKER_COUNT).

<header class="speakers-hero">
  <h1>World AI Summit 2026 Speakers</h1>
  <p class="sub">50 confirmed so far for 14-15 October 2026, Sheraton Grand Bangalore Hotel at Brigade Gateway. New names added as announced.</p>
  <p>Policymakers, regulators, enterprise technology leaders, founders and investors meet in Bengaluru across seven tracks: Frontier Models &amp; Compute; Sovereign AI &amp; Geopolitics; Enterprise AI in Production; GCCs; Robotics, Agents &amp; Embodied AI; AI for Bharat; and Capital, Founders &amp; Exits. Each name below links to the speaker's profile. Session titles, times and halls are added to each profile once the agenda is final.</p>
  <p class="cta-row">
    <a class="wais-btn wais-btn-primary" href="/delegate/">Book your delegate pass</a>
    <a class="wais-btn wais-btn-secondary" href="PLACEHOLDER_AGENDA_URL">See the agenda</a>
  </p>
</header>

(Leave out the "See the agenda" link until an agenda page is live.)

====================================================================
3. /speaker.html <body>: the 50 confirmed speakers as plain HTML (no script rendering)
====================================================================
Names and short roles are copied from the live /assets/speaker_details/index.html as fetched on 1 Oct 2026, where every one is marked "Confirmed 2026". Groups and order are unchanged. Links go to the existing profile pages. Put the list in the HTML source itself, not in markup injected by JavaScript, and check it with view-source.

<main class="speakers">
  <section class="speaker-group" id="government">
    <h2>Government, policy and regulators <span class="count">(11)</span></h2>
    <ul class="speaker-list">
      <li><a href="/assets/speaker_details/pankaj-kumar-pandey.html">Pankaj Kumar Pandey, IAS</a> <span class="role">Principal Secretary, e-Governance, Karnataka</span></li>
      <li><a href="/assets/speaker_details/t-bhoobalan.html">T Bhoobalan, IAS</a> <span class="role">CEO, Centre for e-Governance, Karnataka</span></li>
      <li><a href="/assets/speaker_details/ravikumar-surpur.html">Dr Ravikumar Surpur, IAS</a> <span class="role">Secretary, IT &amp; Communication, Rajasthan</span></li>
      <li><a href="/assets/speaker_details/aman-mittal.html">Aman Mittal, IAS</a> <span class="role">Joint CEO, MITRA, Maharashtra</span></li>
      <li><a href="/assets/speaker_details/sanjeev-gupta.html">Sanjeev Gupta</a> <span class="role">CEO, Karnataka Digital Economy Mission</span></li>
      <li><a href="/assets/speaker_details/hemant-garg.html">Hemant Garg</a> <span class="role">Deputy Director, Ministry of Labour and Employment</span></li>
      <li><a href="/assets/speaker_details/prajeet-prabhakaran.html">Prajeet Prabhakaran</a> <span class="role">Regional Director, Embassy of Austria</span></li>
      <li><a href="/assets/speaker_details/ram-mohan-rao.html">Ram Mohan Rao</a> <span class="role">Executive Director, SEBI</span></li>
      <li><a href="/assets/speaker_details/m-balasubramaniam.html">M. Balasubramaniam (Bala MS)</a> <span class="role">Chairman, Southern Regional Committee, AICTE</span></li>
      <li><a href="/assets/speaker_details/mahesh-hariharan-iyer.html">Mahesh Hariharan Iyer</a> <span class="role">VP Engineering, Reserve Bank Innovation Hub</span></li>
      <li><a href="/assets/speaker_details/sushil-kumar-meher.html">Dr. Sushil Kumar Meher</a> <span class="role">Head, IT and CISO, AIIMS</span></li>
    </ul>
  </section>
  <section class="speaker-group" id="enterprise">
    <h2>Enterprise and technology leaders <span class="count">(35)</span></h2>
    <ul class="speaker-list">
      <li><a href="/assets/speaker_details/sanjeev-rastogi.html">Sanjeev Rastogi</a> <span class="role">Head, Group Policy Services, Adani Group</span></li>
      <li><a href="/assets/speaker_details/sandeep-varaganti.html">Sandeep Varaganti</a> <span class="role">CEO, JioMart, Reliance Retail</span></li>
      <li><a href="/assets/speaker_details/george-inasu.html">George Inasu</a> <span class="role">MD and Country Head, Fidelity National Financial India</span></li>
      <li><a href="/assets/speaker_details/anand-ramakrishnan.html">Anand Ramakrishnan</a> <span class="role">Managing Director, Equiniti India</span></li>
      <li><a href="/assets/speaker_details/tulshekar-gangireddy.html">Tulshekar Gangireddy</a> <span class="role">ED and Head of Data Strategy, JPMorgan Chase</span></li>
      <li><a href="/assets/speaker_details/deepak-mohanty.html">Deepak Mohanty</a> <span class="role">Executive Director, Wells Fargo</span></li>
      <li><a href="/assets/speaker_details/anand-thakur.html">Anand Thakur</a> <span class="role">CPTO, Reliance Retail</span></li>
      <li><a href="/assets/speaker_details/pawan-sachdeva.html">Pawan Sachdeva</a> <span class="role">Senior MD and Technology Head India, Carelon</span></li>
      <li><a href="/assets/speaker_details/pranav-saxena.html">Pranav Saxena</a> <span class="role">CPTO, API Holdings</span></li>
      <li><a href="/assets/speaker_details/suman-guha.html">Suman Guha</a> <span class="role">Chief Digital and Technology Officer, Croma</span></li>
      <li><a href="/assets/speaker_details/avinash-naik.html">Avinash Naik</a> <span class="role">CIO, Bajaj Allianz General Insurance</span></li>
      <li><a href="/assets/speaker_details/harsh-vardhan.html">Harsh Vardhan</a> <span class="role">Global Head, AI and Digital Innovation, Apollo Tyres</span></li>
      <li><a href="/assets/speaker_details/vijaya-kadiyala.html">Vijaya Kadiyala</a> <span class="role">Executive Director, DBS Bank</span></li>
      <li><a href="/assets/speaker_details/shanmugam-manivannan.html">Shanmugam Manivannan</a> <span class="role">Chief Digital Officer, Equitas Small Finance Bank</span></li>
      <li><a href="/assets/speaker_details/rajesh-choudhary.html">Rajesh Choudhary</a> <span class="role">CIO, CSB Bank</span></li>
      <li><a href="/assets/speaker_details/dipayan-chakraborty.html">Dipayan Chakraborty</a> <span class="role">Head, India Analytics Center, eBay</span></li>
      <li><a href="/assets/speaker_details/archana-menon.html">Archana Menon</a> <span class="role">Head of Analytics and Watches, Titan</span></li>
      <li><a href="/assets/speaker_details/deepika-sandeep.html">Deepika Sandeep</a> <span class="role">Head, AI/ML CoE, HSBC</span></li>
      <li><a href="/assets/speaker_details/anil-varma.html">Anil Varma</a> <span class="role">CTO, Multi Commodity Exchange Clearing Corporation</span></li>
      <li><a href="/assets/speaker_details/deepak-sharma.html">Deepak Sharma</a> <span class="role">Independent Director, Suryoday Small Finance Bank</span></li>
      <li><a href="/assets/speaker_details/animesh-kishore.html">Animesh Kishore</a> <span class="role">Head, Digital and Analytics CoE, ITC</span></li>
      <li><a href="/assets/speaker_details/sandeep-sharma.html">Sandeep Sharma</a> <span class="role">Head of Technology and Product, Shoppers Stop</span></li>
      <li><a href="/assets/speaker_details/shireen-ali.html">Shireen Ali</a> <span class="role">Head, UK Data Enablement and Standards, HSBC</span></li>
      <li><a href="/assets/speaker_details/vishal-chugh.html">Vishal Chugh</a> <span class="role">EVP, Head Risk FRM, Tata Capital</span></li>
      <li><a href="/assets/speaker_details/shantanu-dasgupta.html">Shantanu Dasgupta</a> <span class="role">Head of Digital Initiatives, Treasury and Transaction Banking, Axis Bank</span></li>
      <li><a href="/assets/speaker_details/sushan-rungta.html">Sushan Rungta</a> <span class="role">CTO, Absolute</span></li>
      <li><a href="/assets/speaker_details/ganesh-joshi.html">Ganesh Joshi</a> <span class="role">CIO, Nilons Enterprises</span></li>
      <li><a href="/assets/speaker_details/praveen-bist.html">Praveen Bist</a> <span class="role">CIO, Amrita Hospitals</span></li>
      <li><a href="/assets/speaker_details/kuldeep-t.html">Kuldeep T</a> <span class="role">CISO and DPO, BigBasket</span></li>
      <li><a href="/assets/speaker_details/anshuma-singh.html">Anshuma (Dogra) Singh</a> <span class="role">Senior Director, India IT Head, Applied Materials</span></li>
      <li><a href="/assets/speaker_details/padmanaban-ta.html">Padmanaban TA</a> <span class="role">DGM and Head of Digital Banking, Karnataka Bank</span></li>
      <li><a href="/assets/speaker_details/joyce-rodriguez.html">Joyce Rodriguez</a> <span class="role">Head of Digital Cybersecurity, Airbus India</span></li>
      <li><a href="/assets/speaker_details/pavankumar-gurazada.html">Pavankumar Gurazada</a> <span class="role">Associate Director, Great Learning</span></li>
      <li><a href="/assets/speaker_details/aneel-savalagi.html">Aneelkumar (Aneel) Savalagi</a> <span class="role">Global Chapter Leader, ICC, Takeda</span></li>
      <li><a href="/assets/speaker_details/sivakumar-selva-ganapathy.html">Sivakumar Selva Ganapathy</a> <span class="role">VP Software Engineering, Johnson Controls</span></li>
    </ul>
  </section>
  <section class="speaker-group" id="founders">
    <h2>Founders, investors and ecosystem builders <span class="count">(4)</span></h2>
    <ul class="speaker-list">
      <li><a href="/assets/speaker_details/shalini-kapoor.html">Shalini Kapoor</a> <span class="role">Chief Strategist, Data and AI, EkStep</span></li>
      <li><a href="/assets/speaker_details/sandhya-vasudevan.html">Sandhya Vasudevan</a> <span class="role">Board Member, TiE Bangalore</span></li>
      <li><a href="/assets/speaker_details/suman-dash.html">Suman Dash</a> <span class="role">COO, Acsel Technology Forum</span></li>
      <li><a href="/assets/speaker_details/shashank-randev.html">Shashank Randev</a> <span class="role">Founder and General Partner, 247VC</span></li>
    </ul>
  </section>

  <section class="speaker-group" id="edition-2025">
    <h2>From the 2025 edition</h2>
    <ul class="speaker-list">
      <li><a href="/assets/speaker_details/priyank-kharge.html">Shri Priyank M Kharge</a> <span class="role">Chief Guest, World AI Summit 2025; Minister of Home Affairs, IT/BT and E-Governance, Government of Karnataka</span></li>
    </ul>
  </section>

  <p class="small">Speaker names, roles and organisations are as at the time of announcement. Programme subject to change.</p>

  <section class="speakers-cta">
    <h2>Hear them in person on 14-15 October</h2>
    <p>World AI Summit 2026, Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. Delegate passes from Rs PLACEHOLDER_CURRENT_PASS_PRICE. Groups of three or more delegates get 10% off.</p>
    <p><a class="wais-btn wais-btn-primary" href="/delegate/">Book your delegate pass</a></p>
    <p>Speaking and collaboration: <a href="mailto:secretariat@worldaisummit.com">secretariat@worldaisummit.com</a><br>
       Partnerships, sponsorship and exhibition: <a href="mailto:partnerships@worldaisummit.com">partnerships@worldaisummit.com</a><br>
       Delegate registration: <a href="mailto:registration@worldaisummit.com">registration@worldaisummit.com</a></p>
  </section>
</main>

The "From the 2025 edition" entry above replaces the "Welcoming Shri Priyank M Kharge" block on /speaker.html. He is not among the 50 names marked "Confirmed 2026" on /assets/speaker_details/index.html, so the page should not suggest he is attending in 2026. If the secretariat confirms him (PLACEHOLDER_KHARGE_2026_CONFIRMED), move him to the top of "Government, policy and regulators" with the role "Minister of Home Affairs, IT/BT and E-Governance, Government of Karnataka", change "50" to "51" everywhere, and add him to "performer" in the JSON-LD.

Minimal CSS (optional; skip it if the site's button classes already exist):
<style>
.speaker-list{list-style:none;padding:0;columns:2 280px;column-gap:32px}
.speaker-list li{break-inside:avoid;margin:0 0 12px}
.speaker-list a{font-weight:600}
.speaker-list .role{display:block;font-size:.92em;opacity:.8}
.wais-btn{display:inline-block;padding:12px 20px;border-radius:6px;text-decoration:none;font-weight:600;margin:4px 8px 4px 0}
.wais-btn-primary{background:#0b3d91;color:#fff}
.wais-btn-secondary{border:1px solid #0b3d91;color:#0b3d91}
</style>

====================================================================
4. /speaker.html: JSON-LD (in <head>, or just before </body>)
====================================================================
"performer" lists only the 50 names marked "Confirmed 2026" on the live index on 1 Oct 2026, with the short roles shown there. Priyank Kharge is left out until the secretariat confirms him.
Venue address [Google Hotels, Apple Maps and Cvent listings, checked 1 Oct 2026]: 26/1 Dr Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru, Karnataka 560055. Coordinates are from the Exa Places listing.
Before publishing, replace PLACEHOLDER_CURRENT_PASS_PRICE_INR with a number only (for example 30000) and PLACEHOLDER_EVENT_IMAGE_URL with an absolute image URL. If there is no image, delete the "image" line. If the homepage already has an Event block, use the same "@id" there so Google reads both as one event. Test with https://search.google.com/test/rich-results and https://validator.schema.org/.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {"@type": "CollectionPage", "@id": "https://www.worldaisummit.com/speaker.html#webpage", "url": "https://www.worldaisummit.com/speaker.html", "name": "World AI Summit 2026 Speakers", "description": "Meet the 50 confirmed speakers at World AI Summit 2026, Bengaluru, 14-15 Oct: leaders from SEBI, KDEM, HSBC, JPMorgan Chase, Reliance Retail and more.", "inLanguage": "en-IN", "isPartOf": {"@type": "WebSite", "name": "World AI Summit", "url": "https://www.worldaisummit.com/"}, "about": {"@id": "https://www.worldaisummit.com/#event"}},
    {
      "@type": "Event",
      "@id": "https://www.worldaisummit.com/#event",
      "name": "World AI Summit 2026",
      "description": "World AI Summit 2026 brings policymakers, regulators, enterprise technology leaders, founders and investors together in Bengaluru on 14-15 October 2026 across seven tracks, from frontier models and sovereign AI to enterprise AI in production, GCCs and AI for Bharat.",
      "startDate": "2026-10-14",
      "endDate": "2026-10-15",
      "eventStatus": "https://schema.org/EventScheduled",
      "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
      "url": "https://www.worldaisummit.com/",
      "image": ["PLACEHOLDER_EVENT_IMAGE_URL"],
      "location": {"@type": "Place", "name": "Sheraton Grand Bangalore Hotel at Brigade Gateway", "address": {"@type": "PostalAddress", "streetAddress": "26/1 Dr Rajkumar Road, Malleswaram-Rajajinagar", "addressLocality": "Bengaluru", "addressRegion": "Karnataka", "postalCode": "560055", "addressCountry": "IN"}, "geo": {"@type": "GeoCoordinates", "latitude": 13.01247, "longitude": 77.55484}},
      "organizer": {"@type": "Organization", "name": "Elets Technomedia", "url": "https://www.eletsonline.com/"},
      "offers": {"@type": "Offer", "name": "Delegate pass", "url": "https://www.worldaisummit.com/delegate/", "price": "PLACEHOLDER_CURRENT_PASS_PRICE_INR", "priceCurrency": "INR", "availability": "https://schema.org/InStock"},
      "performer": [
        {"@type": "Person", "name": "Pankaj Kumar Pandey", "honorificSuffix": "IAS", "jobTitle": "Principal Secretary, e-Governance, Karnataka", "url": "https://www.worldaisummit.com/assets/speaker_details/pankaj-kumar-pandey.html"},
        {"@type": "Person", "name": "T Bhoobalan", "honorificSuffix": "IAS", "jobTitle": "CEO, Centre for e-Governance, Karnataka", "url": "https://www.worldaisummit.com/assets/speaker_details/t-bhoobalan.html"},
        {"@type": "Person", "name": "Ravikumar Surpur", "honorificPrefix": "Dr", "honorificSuffix": "IAS", "jobTitle": "Secretary, IT & Communication, Rajasthan", "url": "https://www.worldaisummit.com/assets/speaker_details/ravikumar-surpur.html"},
        {"@type": "Person", "name": "Aman Mittal", "honorificSuffix": "IAS", "jobTitle": "Joint CEO, MITRA, Maharashtra", "url": "https://www.worldaisummit.com/assets/speaker_details/aman-mittal.html"},
        {"@type": "Person", "name": "Sanjeev Gupta", "jobTitle": "CEO, Karnataka Digital Economy Mission", "url": "https://www.worldaisummit.com/assets/speaker_details/sanjeev-gupta.html"},
        {"@type": "Person", "name": "Hemant Garg", "jobTitle": "Deputy Director, Ministry of Labour and Employment", "url": "https://www.worldaisummit.com/assets/speaker_details/hemant-garg.html"},
        {"@type": "Person", "name": "Prajeet Prabhakaran", "jobTitle": "Regional Director, Embassy of Austria", "url": "https://www.worldaisummit.com/assets/speaker_details/prajeet-prabhakaran.html"},
        {"@type": "Person", "name": "Ram Mohan Rao", "jobTitle": "Executive Director, SEBI", "url": "https://www.worldaisummit.com/assets/speaker_details/ram-mohan-rao.html"},
        {"@type": "Person", "name": "M. Balasubramaniam", "alternateName": "Bala MS", "jobTitle": "Chairman, Southern Regional Committee, AICTE", "url": "https://www.worldaisummit.com/assets/speaker_details/m-balasubramaniam.html"},
        {"@type": "Person", "name": "Mahesh Hariharan Iyer", "jobTitle": "VP Engineering, Reserve Bank Innovation Hub", "url": "https://www.worldaisummit.com/assets/speaker_details/mahesh-hariharan-iyer.html"},
        {"@type": "Person", "name": "Sushil Kumar Meher", "honorificPrefix": "Dr", "jobTitle": "Head, IT and CISO, AIIMS", "url": "https://www.worldaisummit.com/assets/speaker_details/sushil-kumar-meher.html"},
        {"@type": "Person", "name": "Sanjeev Rastogi", "jobTitle": "Head, Group Policy Services, Adani Group", "url": "https://www.worldaisummit.com/assets/speaker_details/sanjeev-rastogi.html"},
        {"@type": "Person", "name": "Sandeep Varaganti", "jobTitle": "CEO, JioMart, Reliance Retail", "url": "https://www.worldaisummit.com/assets/speaker_details/sandeep-varaganti.html"},
        {"@type": "Person", "name": "George Inasu", "jobTitle": "MD and Country Head, Fidelity National Financial India", "url": "https://www.worldaisummit.com/assets/speaker_details/george-inasu.html"},
        {"@type": "Person", "name": "Anand Ramakrishnan", "jobTitle": "Managing Director, Equiniti India", "url": "https://www.worldaisummit.com/assets/speaker_details/anand-ramakrishnan.html"},
        {"@type": "Person", "name": "Tulshekar Gangireddy", "jobTitle": "ED and Head of Data Strategy, JPMorgan Chase", "url": "https://www.worldaisummit.com/assets/speaker_details/tulshekar-gangireddy.html"},
        {"@type": "Person", "name": "Deepak Mohanty", "jobTitle": "Executive Director, Wells Fargo", "url": "https://www.worldaisummit.com/assets/speaker_details/deepak-mohanty.html"},
        {"@type": "Person", "name": "Anand Thakur", "jobTitle": "CPTO, Reliance Retail", "url": "https://www.worldaisummit.com/assets/speaker_details/anand-thakur.html"},
        {"@type": "Person", "name": "Pawan Sachdeva", "jobTitle": "Senior MD and Technology Head India, Carelon", "url": "https://www.worldaisummit.com/assets/speaker_details/pawan-sachdeva.html"},
        {"@type": "Person", "name": "Pranav Saxena", "jobTitle": "CPTO, API Holdings", "url": "https://www.worldaisummit.com/assets/speaker_details/pranav-saxena.html"},
        {"@type": "Person", "name": "Suman Guha", "jobTitle": "Chief Digital and Technology Officer, Croma", "url": "https://www.worldaisummit.com/assets/speaker_details/suman-guha.html"},
        {"@type": "Person", "name": "Avinash Naik", "jobTitle": "CIO, Bajaj Allianz General Insurance", "url": "https://www.worldaisummit.com/assets/speaker_details/avinash-naik.html"},
        {"@type": "Person", "name": "Harsh Vardhan", "jobTitle": "Global Head, AI and Digital Innovation, Apollo Tyres", "url": "https://www.worldaisummit.com/assets/speaker_details/harsh-vardhan.html"},
        {"@type": "Person", "name": "Vijaya Kadiyala", "jobTitle": "Executive Director, DBS Bank", "url": "https://www.worldaisummit.com/assets/speaker_details/vijaya-kadiyala.html"},
        {"@type": "Person", "name": "Shanmugam Manivannan", "jobTitle": "Chief Digital Officer, Equitas Small Finance Bank", "url": "https://www.worldaisummit.com/assets/speaker_details/shanmugam-manivannan.html"},
        {"@type": "Person", "name": "Rajesh Choudhary", "jobTitle": "CIO, CSB Bank", "url": "https://www.worldaisummit.com/assets/speaker_details/rajesh-choudhary.html"},
        {"@type": "Person", "name": "Dipayan Chakraborty", "jobTitle": "Head, India Analytics Center, eBay", "url": "https://www.worldaisummit.com/assets/speaker_details/dipayan-chakraborty.html"},
        {"@type": "Person", "name": "Archana Menon", "jobTitle": "Head of Analytics and Watches, Titan", "url": "https://www.worldaisummit.com/assets/speaker_details/archana-menon.html"},
        {"@type": "Person", "name": "Deepika Sandeep", "jobTitle": "Head, AI/ML CoE, HSBC", "url": "https://www.worldaisummit.com/assets/speaker_details/deepika-sandeep.html"},
        {"@type": "Person", "name": "Anil Varma", "jobTitle": "CTO, Multi Commodity Exchange Clearing Corporation", "url": "https://www.worldaisummit.com/assets/speaker_details/anil-varma.html"},
        {"@type": "Person", "name": "Deepak Sharma", "jobTitle": "Independent Director, Suryoday Small Finance Bank", "url": "https://www.worldaisummit.com/assets/speaker_details/deepak-sharma.html"},
        {"@type": "Person", "name": "Animesh Kishore", "jobTitle": "Head, Digital and Analytics CoE, ITC", "url": "https://www.worldaisummit.com/assets/speaker_details/animesh-kishore.html"},
        {"@type": "Person", "name": "Sandeep Sharma", "jobTitle": "Head of Technology and Product, Shoppers Stop", "url": "https://www.worldaisummit.com/assets/speaker_details/sandeep-sharma.html"},
        {"@type": "Person", "name": "Shireen Ali", "jobTitle": "Head, UK Data Enablement and Standards, HSBC", "url": "https://www.worldaisummit.com/assets/speaker_details/shireen-ali.html"},
        {"@type": "Person", "name": "Vishal Chugh", "jobTitle": "EVP, Head Risk FRM, Tata Capital", "url": "https://www.worldaisummit.com/assets/speaker_details/vishal-chugh.html"},
        {"@type": "Person", "name": "Shantanu Dasgupta", "jobTitle": "Head of Digital Initiatives, Treasury and Transaction Banking, Axis Bank", "url": "https://www.worldaisummit.com/assets/speaker_details/shantanu-dasgupta.html"},
        {"@type": "Person", "name": "Sushan Rungta", "jobTitle": "CTO, Absolute", "url": "https://www.worldaisummit.com/assets/speaker_details/sushan-rungta.html"},
        {"@type": "Person", "name": "Ganesh Joshi", "jobTitle": "CIO, Nilons Enterprises", "url": "https://www.worldaisummit.com/assets/speaker_details/ganesh-joshi.html"},
        {"@type": "Person", "name": "Praveen Bist", "jobTitle": "CIO, Amrita Hospitals", "url": "https://www.worldaisummit.com/assets/speaker_details/praveen-bist.html"},
        {"@type": "Person", "name": "Kuldeep T", "jobTitle": "CISO and DPO, BigBasket", "url": "https://www.worldaisummit.com/assets/speaker_details/kuldeep-t.html"},
        {"@type": "Person", "name": "Anshuma Singh", "alternateName": "Anshuma Dogra Singh", "jobTitle": "Senior Director, India IT Head, Applied Materials", "url": "https://www.worldaisummit.com/assets/speaker_details/anshuma-singh.html"},
        {"@type": "Person", "name": "Padmanaban TA", "jobTitle": "DGM and Head of Digital Banking, Karnataka Bank", "url": "https://www.worldaisummit.com/assets/speaker_details/padmanaban-ta.html"},
        {"@type": "Person", "name": "Joyce Rodriguez", "jobTitle": "Head of Digital Cybersecurity, Airbus India", "url": "https://www.worldaisummit.com/assets/speaker_details/joyce-rodriguez.html"},
        {"@type": "Person", "name": "Pavankumar Gurazada", "jobTitle": "Associate Director, Great Learning", "url": "https://www.worldaisummit.com/assets/speaker_details/pavankumar-gurazada.html"},
        {"@type": "Person", "name": "Aneelkumar Savalagi", "alternateName": "Aneel Savalagi", "jobTitle": "Global Chapter Leader, ICC, Takeda", "url": "https://www.worldaisummit.com/assets/speaker_details/aneel-savalagi.html"},
        {"@type": "Person", "name": "Sivakumar Selva Ganapathy", "jobTitle": "VP Software Engineering, Johnson Controls", "url": "https://www.worldaisummit.com/assets/speaker_details/sivakumar-selva-ganapathy.html"},
        {"@type": "Person", "name": "Shalini Kapoor", "jobTitle": "Chief Strategist, Data and AI, EkStep", "url": "https://www.worldaisummit.com/assets/speaker_details/shalini-kapoor.html"},
        {"@type": "Person", "name": "Sandhya Vasudevan", "jobTitle": "Board Member, TiE Bangalore", "url": "https://www.worldaisummit.com/assets/speaker_details/sandhya-vasudevan.html"},
        {"@type": "Person", "name": "Suman Dash", "jobTitle": "COO, Acsel Technology Forum", "url": "https://www.worldaisummit.com/assets/speaker_details/suman-dash.html"},
        {"@type": "Person", "name": "Shashank Randev", "jobTitle": "Founder and General Partner, 247VC", "url": "https://www.worldaisummit.com/assets/speaker_details/shashank-randev.html"}
      ]
    }
  ]
}
</script>

====================================================================
5. Merge the old directory: /assets/speaker_details/index.html -> /speaker.html
====================================================================
Today /speaker.html ranks #7 and /assets/speaker_details/index.html ranks #11 for "world ai summit speakers" (Google India, 1 Oct 2026). Use one of the options below.

Option A: Apache (.htaccess in the web root, above any existing catch-all rules)
RewriteEngine On
RewriteRule ^assets/speaker_details/(index\.html)?$ https://www.worldaisummit.com/speaker.html [R=301,L]

Option A: nginx (in the server block for www.worldaisummit.com, and in the non-www block too if it serves files)
location = /assets/speaker_details/index.html { return 301 https://www.worldaisummit.com/speaker.html; }
location = /assets/speaker_details/ { return 301 https://www.worldaisummit.com/speaker.html; }

Both go to the final https://www. URL in a single hop. Check: curl -sI https://www.worldaisummit.com/assets/speaker_details/index.html should return "301" and "location: https://www.worldaisummit.com/speaker.html". Run the same check without www, which should give at most two hops.

Option B: the static host does not allow server rules. Replace the <head> of /assets/speaker_details/index.html with:
<title>World AI Summit 2026 Speakers | 50 Confirmed, Bengaluru</title>
<link rel="canonical" href="https://www.worldaisummit.com/speaker.html">
<meta http-equiv="refresh" content="0; url=https://www.worldaisummit.com/speaker.html">
In the body, keep a single line: <p>The speaker list has moved to <a href="https://www.worldaisummit.com/speaker.html">World AI Summit 2026 Speakers</a>.</p>
(Google treats an instant meta refresh much like a permanent redirect. A canonical tag alone is only a hint and can take longer than the two weeks before the event to take effect.)

In both cases:
- In sitemap.xml, remove https://www.worldaisummit.com/assets/speaker_details/index.html. Keep https://www.worldaisummit.com/speaker.html and set <lastmod> to the publish date.
- On every /assets/speaker_details/*.html profile, point any "All speakers" or back link to /speaker.html.
- Do not publish the local /speakers/<slug>/ generator output as a third directory. Use it only if it replaces /assets/speaker_details/ with one 301 per profile.

====================================================================
6. Booking block for every speaker profile (/assets/speaker_details/<slug>.html)
====================================================================
The profiles already show "Delegate passes from Rs 20,000." with the date and venue. What they lack is a prominent call to action. Place this block directly under the name, role and "Confirmed speaker, World AI Summit 2026" lines. In the closing "World AI Summit 2026" block, replace "Delegate passes from Rs 20,000." with the note line below.

<div class="wais-cta">
  <a class="wais-btn wais-btn-primary" href="/delegate/">Hear [Name] live on 14-15 Oct: book your pass</a>
  <a class="wais-btn wais-btn-secondary" href="PLACEHOLDER_AGENDA_URL">See the agenda</a>
  <p class="wais-cta-note">14-15 October 2026, Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. Delegate passes from Rs PLACEHOLDER_CURRENT_PASS_PRICE. Groups of three or more delegates get 10% off.</p>
</div>

Pass price: on 1 Oct 2026, /delegate/ shows "Standard Access (Valid till 30th Sept 2026)" at Rs 20,000 / Rs 35,000, which has now lapsed, and "Late Access" at Rs 30,000 / Rs 60,000. The profiles and homepage still say "from Rs 20,000". Sales must confirm the price buyers are charged today and use it everywhere: profiles, /speaker.html, the homepage and the JSON-LD.

[Name] rule: use the name as the profile shows it, without ", IAS" and without the part in brackets. Keep "Dr" where the profile uses it. For example:
sanjeev-gupta.html | Hear Sanjeev Gupta live on 14-15 Oct: book your pass
pankaj-kumar-pandey.html | Hear Pankaj Kumar Pandey live on 14-15 Oct: book your pass
ravikumar-surpur.html | Hear Dr Ravikumar Surpur live on 14-15 Oct: book your pass
sushil-kumar-meher.html | Hear Dr Sushil Kumar Meher live on 14-15 Oct: book your pass
m-balasubramaniam.html | Hear M. Balasubramaniam live on 14-15 Oct: book your pass
anshuma-singh.html | Hear Anshuma Singh live on 14-15 Oct: book your pass
aneel-savalagi.html | Hear Aneelkumar Savalagi live on 14-15 Oct: book your pass
(The other 43 profiles follow the same pattern with the name as listed in section 3.)

Session line: when the agenda is final, replace "Session title, time and hall will be published on this page once the agenda is final." on each profile with:
<p><strong>Session:</strong> PLACEHOLDER_SESSION_TITLE<br><strong>When:</strong> PLACEHOLDER_DAY_DATE, PLACEHOLDER_TIME IST<br><strong>Where:</strong> PLACEHOLDER_HALL, Sheraton Grand Bangalore Hotel at Brigade Gateway</p>

====================================================================
7. Priyank Kharge profile (/assets/speaker_details/priyank-kharge.html)
====================================================================
His two designations are not in conflict. One is his earlier portfolio and the other his current one. In the June 2026 portfolio allocation he was given Home (excluding Intelligence), IT-BT and E-Governance, and Rural Development & Panchayat Raj went to Eshwar Khandre [Deccan Chronicle, 4-5 Jun 2026: https://www.deccanchronicle.com/southern-states/karnataka/priyank-gets-home-as-cabinet-portfolios-are-allocated-1961437]. The H1 subtitle "Minister of Home Affairs, IT/BT and E-Governance" is current and stays.

7a. "About Shri Priyank Kharge", first sentence.
REPLACE: Shri Priyank Kharge serves as the Hon'ble Minister for Electronics, IT & Biotechnology and Rural Development & Panchayat Raj, Government of Karnataka.
WITH:    Shri Priyank Kharge is the Hon'ble Minister of Home Affairs (excluding Intelligence), IT/BT and E-Governance, Government of Karnataka, following the cabinet portfolio allocation of June 2026. At the time of World AI Summit 2025, he was the then Minister for Electronics, IT & Biotechnology and Rural Development & Panchayat Raj.
(The rest of the section can stay as it is.)

7b. Meta description (136 characters), replacing the one that gives the pre-June 2026 portfolio:
<meta name="description" content="Shri Priyank Kharge, Karnataka's Minister of Home Affairs, IT/BT and E-Governance, was Chief Guest at World AI Summit 2025 in Bengaluru.">

7c. Title: keep "Shri Priyank Kharge | Chief Guest | World AI Summit 2025" until the secretariat confirms him for 2026 (PLACEHOLDER_KHARGE_2026_CONFIRMED). Do not use the per-speaker "Hear [Name] live" button on this page. Use this instead:
<div class="wais-cta"><a class="wais-btn wais-btn-primary" href="/delegate/">Book your pass for World AI Summit 2026, 14-15 October</a></div>

7d. Only after written confirmation from the secretariat:
<title>Shri Priyank Kharge | World AI Summit 2026, Bengaluru</title>   (53 characters)
<meta name="description" content="Shri Priyank Kharge, Karnataka's Minister of Home Affairs, IT/BT and E-Governance, speaks at World AI Summit 2026, Bengaluru, 14-15 October 2026.">   (145 characters)
Add "Confirmed speaker, World AI Summit 2026" under his role. Switch the button to "Hear Shri Priyank Kharge live on 14-15 Oct: book your pass". Keep the 2025 Chief Guest section as history. Then follow the notes in section 3 to move him into the 2026 list and the JSON-LD.

====================================================================
8. Checks after publishing
====================================================================
- view-source:https://www.worldaisummit.com/speaker.html shows all 50 names as plain <a> links.
- The Rich Results Test shows one valid Event and no placeholder text.
- All 50 profile links return 200. The slugs match the existing /assets/speaker_details/ file names.
- /assets/speaker_details/index.html returns a 301 (Option A) or has the canonical and meta refresh (Option B).
- In Search Console, request indexing for /speaker.html. The connected property is non-www only (https://worldaisummit.com/), so add the https://www. property to see this page's data.
