# A55: World AI Summit 2026 post-event homepage hero, 2027 interest form and supporting page changes (go live 15 Oct 2026 evening)

- **For recommendation:** Post-event retention for 15-17 Oct: keep one evergreen URL and add winners and 'next edition' capture (Inc42 and BTS pattern)
- **Research lens:** competitors
- **Format:** Copy deck in Markdown with paste-ready HTML snippets and one validated schema.org Event JSON-LD block
- **Placeholders the business must fill:**
  - PLACEHOLDER_DELEGATE_COUNT: final number of delegates who attended (from registration data)
  - PLACEHOLDER_SPEAKER_COUNT: final number of speakers who appeared (from the agenda or on-ground data)
  - PLACEHOLDER_HIGHLIGHTS_URL: URL of the highlights video or recap post; hide the button until it exists
  - PLACEHOLDER_FORM_ENDPOINT: handler URL for the 2027 interest form (reuse the /awards/ form handler or a CRM form)
  - PLACEHOLDER_HERO_IMAGE_PATH: path to a real event photo (1200px or wider) for JSON-LD; delete the image line if none is available
  - PLACEHOLDER_FINAL_PASS_PRICE_NUMBER: business decision on which pass price (plain number, INR) to keep in Event offers, or delete the price line
  - PLACEHOLDER_AWARDS_DATE: date the World AI Awards 2026 were presented (14 or 15 October 2026)
  - PLACEHOLDER_WINNERS_LIST: final category-wise winners list (category, organisation, entry title)
  - PLACEHOLDER_DECISION_2025_BUY_BUTTONS: after checking whether the 2025 pass buttons on /1st-edition/delegate-pass.html open a live checkout, either remove them or point them to /delegate/

## How to ship

Owner: content and web dev. About 2-3 hours, split across 1 Oct and 15 Oct.

WHEN
- Now (any day before 14 Oct): ship section 7. That means the new title and the pre-event banner on /1st-edition/delegate-pass.html, plus the check on whether its buy buttons lead to a live checkout. Also prepare the form endpoint and a staging copy of sections 1-6.
- 15 Oct 2026 evening, right after the closing session: ship sections 1-6 together. The /awards/winners-2026/ page must be live before the hero links to it. If the winners list is not final, hide that button rather than link to an empty page. If the highlights video is not ready, hide "Watch highlights" and add it on 16-17 Oct.

Why 15 Oct and not 16-17 Oct: in 2025 the event ran on 25-26 Sep 2025. On the non-www Search Console property, impressions were 35 on 24 Sep, 46 on 25 Sep (3 clicks) and 12 on 26 Sep, then 0-6 a day through Oct-Nov 2025. That property covers non-www URLs only, so the data is partial, but post-event branded demand fell away within about 48 hours. Expect small traffic: tens of visits at most. The real value is a list of 2027 sponsor, delegate and awards leads.

STEPS
1. Fill in every PLACEHOLDER_ marker. Do not invent the delegate or speaker counts; take them from the final registration and agenda data.
2. Form: the site is static HTML, so point PLACEHOLDER_FORM_ENDPOINT at the handler the /awards/ nomination form already uses, or at your CRM or form tool. The checkbox name interest[] suits PHP handlers; rename it to interest if the handler is not PHP. Send leads tagged sponsor to partnerships@worldaisummit.com.
3. JSON-LD: replace the existing Event block on the homepage; do not add a second one. Before publishing, delete any performer who did not appear on the day. Set price to a plain number (for example 30000) or delete the price line; never leave the placeholder text live. Replace the image path with a real 1200px+ event photo, or delete the image line. Test in Google's Rich Results Test and validator.schema.org.
4. Keep exactly one H1 on the homepage (the new hero H1 replaces the old one). Keep "World AI Summit 2026" and "Bengaluru" in the title and H1, because the homepage holds #1 for world ai summit, world ai summit 2026 and world ai summit bengaluru.
5. Add /awards/winners-2026/ to sitemap.xml and link it from /awards/ and the homepage. In Search Console, request indexing for / and /awards/winners-2026/ on 15-16 Oct.
6. Do not change URLs and do not add redirects (section 8). The site already moved the 2025 edition to /1st-edition/ at some later date, so the only rule that matters is to keep / evergreen.

EVIDENCE (corrected per verifier)
- Bengaluru Tech Summit keeps one evergreen root URL. bengalurutechsummit.com now shows the 29th edition, 17-19 Nov 2026 at BIEC (verified). Its #1 rankings for the 2025 and 2026 queries were not re-checked.
- Cypher's awards page (cypher.analyticsindiamag.com/awards) links winner archives for 2025, 2024, 2023, 2022, 2018 and 2017 (verified). That supports a permanent /awards/winners-2026/ URL.
- Inc42 is weak evidence. After its event, events.inc42.com/ai-summit/ only added an "Announcing Soon" ticker and still shows pre-event copy, with no winners, recap or interest form. It is not a model for this full pattern.
- /1st-edition/delegate-pass.html: the title, indexable status and sitemap entry are confirmed by audit c1b16b55. The claim that it "still sells 2025 passes" is unverified: the page lists undated Rs 30,000 and Rs 60,000 tiers, and nobody has checked whether the checkout is live.
- Venue address (26/1 Dr. Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru, Karnataka 560055) verified via Exa on marriott.com (blrgs-sheraton-grand-bangalore-hotel-at-brigade-gateway) and Google Hotels.
- The performers come from /home/user/123/worldaisummit/speakers/speakers.json (50 entries with confirmed_2026 true). No bios are used.

No OpenSEO paid tools were used, and no files were edited.

## Content

# World AI Summit 2026: post-event hero and 2027 interest capture

Go live: Thursday 15 October 2026, evening, after the closing session. Keep https://www.worldaisummit.com/ as the one event URL. No redirects are needed or wanted.

---

## 1. Homepage <head> (replace title, description and OG tags)

```html
<title>World AI Summit 2026 Bengaluru: Highlights and Award Winners</title>
<meta name="description" content="World AI Summit 2026 took place on 14-15 October in Bengaluru. See the World AI Awards 2026 winners, watch highlights and register interest for 2027.">
<meta property="og:title" content="World AI Summit 2026 Bengaluru: Highlights and Award Winners">
<meta property="og:description" content="World AI Summit 2026 took place on 14-15 October in Bengaluru. See the World AI Awards 2026 winners, watch highlights and register interest for 2027.">
<link rel="canonical" href="https://www.worldaisummit.com/">
```
(The title is 60 characters and the description 149. This also fixes the current 182-character homepage description.)

---

## 2. Homepage hero (replaces the current hero and its H1; keep one H1 on the page)

```html
<section class="wais-hero wais-hero--post" aria-labelledby="wais-hero-title">
  <p class="wais-hero__eyebrow">World AI Summit 2026 · 14-15 October · Bengaluru</p>
  <h1 id="wais-hero-title">World AI Summit 2026: thank you, Bengaluru</h1>
  <p class="wais-hero__lede">Thank you to PLACEHOLDER_DELEGATE_COUNT delegates and PLACEHOLDER_SPEAKER_COUNT speakers who joined us at Sheraton Grand Bangalore Hotel at Brigade Gateway for two days and seven tracks, from frontier models and sovereign AI to enterprise AI in production and AI for Bharat.</p>
  <ul class="wais-hero__ctas">
    <li><a class="btn btn-primary" href="/awards/winners-2026/">See the World AI Awards 2026 winners &rarr;</a></li>
    <li><a class="btn btn-secondary" href="PLACEHOLDER_HIGHLIGHTS_URL">Watch highlights &rarr;</a></li>
    <li><a class="btn btn-secondary" href="#wais-2027">Be first to hear about World AI Summit 2027: register interest &rarr;</a></li>
  </ul>
</section>
```

Short version for the top ticker or mobile bar:
`World AI Summit 2027: announcing soon. Register interest →` (link to `#wais-2027`)

Replace every "Book your pass" or "Register now" button on the homepage with "Register interest for 2027", linking to `#wais-2027`. 2026 delegate passes stop selling once the event ends.

---

## 3. 2027 interest section (place directly below the hero)

```html
<section id="wais-2027" class="wais-interest" aria-labelledby="wais-2027-title">
  <h2 id="wais-2027-title">World AI Summit 2027: announcing soon</h2>
  <p>Dates and venue for the next edition will be announced here first. Leave your details and tell us how you would like to take part.</p>
  <form action="PLACEHOLDER_FORM_ENDPOINT" method="post">
    <input type="hidden" name="source" value="homepage-post-event-2026">
    <label for="wi-name">Full name</label>
    <input id="wi-name" name="name" type="text" autocomplete="name" required>
    <label for="wi-email">Work email</label>
    <input id="wi-email" name="email" type="email" autocomplete="email" required>
    <label for="wi-company">Company or organisation</label>
    <input id="wi-company" name="company" type="text" autocomplete="organization" required>
    <fieldset>
      <legend>I would like to</legend>
      <label><input type="checkbox" name="interest[]" value="attend"> Attend as a delegate</label>
      <label><input type="checkbox" name="interest[]" value="sponsor"> Sponsor or exhibit</label>
      <label><input type="checkbox" name="interest[]" value="speak"> Speak</label>
      <label><input type="checkbox" name="interest[]" value="awards"> Nominate for the World AI Awards</label>
    </fieldset>
    <label class="wais-consent"><input type="checkbox" name="consent" value="yes" required> I agree that Elets Technomedia may email me about World AI Summit 2027.</label>
    <button type="submit">Register interest</button>
  </form>
  <p class="wais-interest__note">For sponsorship conversations now, write to <a href="mailto:partnerships@worldaisummit.com">partnerships@worldaisummit.com</a>. For delegate queries, write to <a href="mailto:registration@worldaisummit.com">registration@worldaisummit.com</a>.</p>
</section>
```

Success message after submit:
"Thank you. We have your details and will write to you as soon as World AI Summit 2027 is announced."

---

## 4. Homepage Event JSON-LD (replace the existing Event block; checked as valid JSON)

Notes: eventStatus stays EventScheduled after the event. schema.org has no "completed" value, and Google removes past events from event results by itself. The venue address is verified on Marriott's hotel page. The performers are the 50 entries marked confirmed_2026 in worldaisummit/speakers/speakers.json. Delete anyone who did not appear on the day.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Event",
  "name": "World AI Summit 2026",
  "description": "World AI Summit 2026, organised by Elets Technomedia, took place on 14-15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru, with seven tracks and the World AI Awards 2026.",
  "startDate": "2026-10-14",
  "endDate": "2026-10-15",
  "eventStatus": "https://schema.org/EventScheduled",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
  "url": "https://www.worldaisummit.com/",
  "image": [
    "https://www.worldaisummit.com/PLACEHOLDER_HERO_IMAGE_PATH.jpg"
  ],
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
  "organizer": {
    "@type": "Organization",
    "name": "Elets Technomedia",
    "url": "https://eletsonline.com/"
  },
  "offers": {
    "@type": "Offer",
    "url": "https://www.worldaisummit.com/delegate/",
    "priceCurrency": "INR",
    "price": "PLACEHOLDER_FINAL_PASS_PRICE_NUMBER"
  },
  "performer": [
    {"@type": "Person", "name": "Pankaj Kumar Pandey, IAS", "jobTitle": "Principal Secretary, e-Governance, Karnataka", "worksFor": {"@type": "Organization", "name": "Government of Karnataka"}, "sameAs": "https://www.linkedin.com/in/pankaj-pandey-i-a-s-6b6882191"},
    {"@type": "Person", "name": "T Bhoobalan, IAS", "jobTitle": "CEO, Centre for e-Governance, Karnataka", "worksFor": {"@type": "Organization", "name": "Government of Karnataka"}, "sameAs": "https://www.linkedin.com/in/bhoobalan-t-ias"},
    {"@type": "Person", "name": "Sanjeev Rastogi", "jobTitle": "Head, Group Policy Services, Adani Group", "worksFor": {"@type": "Organization", "name": "Adani Group"}, "sameAs": "https://in.linkedin.com/in/sanjeevras"},
    {"@type": "Person", "name": "Shalini Kapoor", "jobTitle": "Chief Strategist, Data and AI, EkStep", "worksFor": {"@type": "Organization", "name": "EkStep Foundation"}, "sameAs": "https://www.linkedin.com/in/kshalini"},
    {"@type": "Person", "name": "Dr Ravikumar Surpur, IAS", "jobTitle": "Secretary, IT & Communication, Rajasthan", "worksFor": {"@type": "Organization", "name": "Government of Rajasthan"}},
    {"@type": "Person", "name": "Aman Mittal, IAS", "jobTitle": "Joint CEO, MITRA, Maharashtra", "worksFor": {"@type": "Organization", "name": "Maharashtra Institution for Transformation (MITRA)"}, "sameAs": "https://www.linkedin.com/in/aman-mittal-964665ab"},
    {"@type": "Person", "name": "Sanjeev Gupta", "jobTitle": "CEO, Karnataka Digital Economy Mission", "worksFor": {"@type": "Organization", "name": "Karnataka Digital Economy Mission"}, "sameAs": "https://in.linkedin.com/in/sanjeevkgupta"},
    {"@type": "Person", "name": "Hemant Garg", "jobTitle": "Deputy Director, Ministry of Labour and Employment", "worksFor": {"@type": "Organization", "name": "Ministry of Labour and Employment, Government of India"}, "sameAs": "https://www.linkedin.com/in/dr-hemant-garg-2b26699"},
    {"@type": "Person", "name": "Prajeet Prabhakaran", "jobTitle": "Regional Director, Embassy of Austria", "worksFor": {"@type": "Organization", "name": "Embassy of Austria, Commercial Section"}, "sameAs": "https://in.linkedin.com/in/prajeet-prabhakaran-495b8049"},
    {"@type": "Person", "name": "Ram Mohan Rao", "jobTitle": "Executive Director, SEBI", "worksFor": {"@type": "Organization", "name": "Securities and Exchange Board of India (SEBI)"}, "sameAs": "https://in.linkedin.com/in/g-ram-mohan-rao"},
    {"@type": "Person", "name": "M. Balasubramaniam (Bala MS)", "jobTitle": "Chairman, Southern Regional Committee, AICTE", "worksFor": {"@type": "Organization", "name": "All India Council for Technical Education (AICTE)"}, "sameAs": "https://www.linkedin.com/in/balams03"},
    {"@type": "Person", "name": "Mahesh Hariharan Iyer", "jobTitle": "VP Engineering, Reserve Bank Innovation Hub", "worksFor": {"@type": "Organization", "name": "Reserve Bank Innovation Hub (RBIH)"}, "sameAs": "https://www.linkedin.com/in/mahesh-hariharan-iyer-80134aa"},
    {"@type": "Person", "name": "Dr. Sushil Kumar Meher", "jobTitle": "Head, IT and CISO, AIIMS", "worksFor": {"@type": "Organization", "name": "All India Institute of Medical Sciences (AIIMS)"}, "sameAs": "https://in.linkedin.com/in/dr-sushil-meher-27400a1b"},
    {"@type": "Person", "name": "Sandeep Varaganti", "jobTitle": "CEO, JioMart, Reliance Retail", "worksFor": {"@type": "Organization", "name": "Reliance Retail"}, "sameAs": "https://in.linkedin.com/in/sandeepvaraganti"},
    {"@type": "Person", "name": "George Inasu", "jobTitle": "MD and Country Head, Fidelity National Financial India", "worksFor": {"@type": "Organization", "name": "Fidelity National Financial India"}, "sameAs": "https://in.linkedin.com/in/georgeinasu"},
    {"@type": "Person", "name": "Anand Ramakrishnan", "jobTitle": "Managing Director, Equiniti India", "worksFor": {"@type": "Organization", "name": "Equiniti India"}, "sameAs": "https://www.linkedin.com/in/anand-ramakrishnan-3597383"},
    {"@type": "Person", "name": "Tulshekar Gangireddy", "jobTitle": "ED and Head of Data Strategy, JPMorgan Chase", "worksFor": {"@type": "Organization", "name": "JPMorgan Chase & Co"}, "sameAs": "https://in.linkedin.com/in/tulshekar-gangireddy"},
    {"@type": "Person", "name": "Deepak Mohanty", "jobTitle": "Executive Director, Wells Fargo", "worksFor": {"@type": "Organization", "name": "Wells Fargo"}, "sameAs": "https://in.linkedin.com/in/deepakmohanty2211"},
    {"@type": "Person", "name": "Anand Thakur", "jobTitle": "CPTO, Reliance Retail", "worksFor": {"@type": "Organization", "name": "Reliance Retail"}, "sameAs": "https://www.linkedin.com/in/anthakur"},
    {"@type": "Person", "name": "Pawan Sachdeva", "jobTitle": "Senior MD and Technology Head India, Carelon", "worksFor": {"@type": "Organization", "name": "Carelon Global Solutions"}, "sameAs": "https://www.linkedin.com/in/pawans"},
    {"@type": "Person", "name": "Pranav Saxena", "jobTitle": "CPTO, API Holdings", "worksFor": {"@type": "Organization", "name": "API Holdings"}, "sameAs": "https://in.linkedin.com/in/pranav-saxena-5226a4"},
    {"@type": "Person", "name": "Suman Guha", "jobTitle": "Chief Digital and Technology Officer, Croma", "worksFor": {"@type": "Organization", "name": "Tata Croma (Tata Digital)"}, "sameAs": "https://in.linkedin.com/in/guha-suman"},
    {"@type": "Person", "name": "Avinash Naik", "jobTitle": "CIO, Bajaj Allianz General Insurance", "worksFor": {"@type": "Organization", "name": "Bajaj Allianz General Insurance"}, "sameAs": "https://in.linkedin.com/in/avinashnaik"},
    {"@type": "Person", "name": "Harsh Vardhan", "jobTitle": "Global Head, AI and Digital Innovation, Apollo Tyres", "worksFor": {"@type": "Organization", "name": "Apollo Tyres Ltd"}, "sameAs": "https://www.linkedin.com/in/harshvardhan-ai"},
    {"@type": "Person", "name": "Vijaya Kadiyala", "jobTitle": "Executive Director, DBS Bank", "worksFor": {"@type": "Organization", "name": "DBS Bank"}, "sameAs": "https://in.linkedin.com/in/vijaya-kadiyala"},
    {"@type": "Person", "name": "Shanmugam Manivannan", "jobTitle": "Chief Digital Officer, Equitas Small Finance Bank", "worksFor": {"@type": "Organization", "name": "Equitas Small Finance Bank"}, "sameAs": "https://in.linkedin.com/in/shanmugammanivannan"},
    {"@type": "Person", "name": "Rajesh Choudhary", "jobTitle": "CIO, CSB Bank", "worksFor": {"@type": "Organization", "name": "CSB Bank"}, "sameAs": "https://www.linkedin.com/in/rc1406"},
    {"@type": "Person", "name": "Dipayan Chakraborty", "jobTitle": "Head, India Analytics Center, eBay", "worksFor": {"@type": "Organization", "name": "eBay"}, "sameAs": "https://www.linkedin.com/in/dipayan-chakraborty-2199101"},
    {"@type": "Person", "name": "Archana Menon", "jobTitle": "Head of Analytics and Watches, Titan", "worksFor": {"@type": "Organization", "name": "Titan"}, "sameAs": "https://in.linkedin.com/in/archana-menon-55360113"},
    {"@type": "Person", "name": "Deepika Sandeep", "jobTitle": "Head, AI/ML CoE, HSBC", "worksFor": {"@type": "Organization", "name": "HSBC"}, "sameAs": "https://in.linkedin.com/in/deepika-sandeep"},
    {"@type": "Person", "name": "Anil Varma", "jobTitle": "CTO, Multi Commodity Exchange Clearing Corporation", "worksFor": {"@type": "Organization", "name": "Multi Commodity Exchange Clearing Corporation"}, "sameAs": "https://in.linkedin.com/in/anilkumar-varma-2b2674a"},
    {"@type": "Person", "name": "Deepak Sharma", "jobTitle": "Independent Director, Suryoday Small Finance Bank", "worksFor": {"@type": "Organization", "name": "Suryoday Small Finance Bank"}, "sameAs": "https://www.linkedin.com/in/deepaksharma71"},
    {"@type": "Person", "name": "Animesh Kishore", "jobTitle": "Head, Digital and Analytics CoE, ITC", "worksFor": {"@type": "Organization", "name": "ITC Limited"}, "sameAs": "https://in.linkedin.com/in/animesh-kishore-81bb557"},
    {"@type": "Person", "name": "Sandeep Sharma", "jobTitle": "Head of Technology and Product, Shoppers Stop", "worksFor": {"@type": "Organization", "name": "Shoppers Stop"}, "sameAs": "https://in.linkedin.com/in/sandeep-sharma-9a7a62a"},
    {"@type": "Person", "name": "Shireen Ali", "jobTitle": "Head, UK Data Enablement and Standards, HSBC", "worksFor": {"@type": "Organization", "name": "HSBC"}, "sameAs": "https://in.linkedin.com/in/shireena"},
    {"@type": "Person", "name": "Vishal Chugh", "jobTitle": "EVP, Head Risk FRM, Tata Capital", "worksFor": {"@type": "Organization", "name": "Tata Capital"}, "sameAs": "https://www.linkedin.com/in/vishal-chugh-15276a39"},
    {"@type": "Person", "name": "Shantanu Dasgupta", "jobTitle": "Head of Digital Initiatives, Treasury and Transaction Banking, Axis Bank", "worksFor": {"@type": "Organization", "name": "Axis Bank"}, "sameAs": "https://in.linkedin.com/in/shantanu-dasgupta-267b311"},
    {"@type": "Person", "name": "Sushan Rungta", "jobTitle": "CTO, Absolute", "worksFor": {"@type": "Organization", "name": "Absolute"}, "sameAs": "https://www.linkedin.com/in/sushanrungta"},
    {"@type": "Person", "name": "Ganesh Joshi", "jobTitle": "CIO, Nilons Enterprises", "worksFor": {"@type": "Organization", "name": "Nilons Enterprises"}, "sameAs": "https://in.linkedin.com/in/ganesh-joshi-2a43982"},
    {"@type": "Person", "name": "Praveen Bist", "jobTitle": "CIO, Amrita Hospitals", "worksFor": {"@type": "Organization", "name": "Amrita Hospitals"}, "sameAs": "https://www.linkedin.com/in/praveen-bist-a56702"},
    {"@type": "Person", "name": "Kuldeep T", "jobTitle": "CISO and DPO, BigBasket", "worksFor": {"@type": "Organization", "name": "BigBasket"}, "sameAs": "https://in.linkedin.com/in/kuldeep-t-5b21316"},
    {"@type": "Person", "name": "Anshuma (Dogra) Singh", "jobTitle": "Senior Director, India IT Head, Applied Materials", "worksFor": {"@type": "Organization", "name": "Applied Materials"}, "sameAs": "https://in.linkedin.com/in/anshuma-dogra-singh-b3a4689"},
    {"@type": "Person", "name": "Padmanaban TA", "jobTitle": "DGM and Head of Digital Banking, Karnataka Bank", "worksFor": {"@type": "Organization", "name": "Karnataka Bank"}, "sameAs": "https://in.linkedin.com/in/padmanaban-t-a-781ab525"},
    {"@type": "Person", "name": "Joyce Rodriguez", "jobTitle": "Head of Digital Cybersecurity, Airbus India", "worksFor": {"@type": "Organization", "name": "Airbus India"}, "sameAs": "https://www.linkedin.com/in/joyce-rodriguez-7b980067"},
    {"@type": "Person", "name": "Pavankumar Gurazada", "jobTitle": "Associate Director, Great Learning", "worksFor": {"@type": "Organization", "name": "Great Learning"}, "sameAs": "https://in.linkedin.com/in/pavankumar-gurazada"},
    {"@type": "Person", "name": "Aneelkumar (Aneel) Savalagi", "jobTitle": "Global Chapter Leader, ICC, Takeda", "worksFor": {"@type": "Organization", "name": "Takeda"}, "sameAs": "https://in.linkedin.com/in/aneelkumar-savalagi-gcc-leader"},
    {"@type": "Person", "name": "Sivakumar Selva Ganapathy", "jobTitle": "VP Software Engineering, Johnson Controls", "worksFor": {"@type": "Organization", "name": "Johnson Controls"}, "sameAs": "https://in.linkedin.com/in/sivakumarsg"},
    {"@type": "Person", "name": "Sandhya Vasudevan", "jobTitle": "Board Member, TiE Bangalore", "worksFor": {"@type": "Organization", "name": "TiE Bangalore"}, "sameAs": "https://www.linkedin.com/in/sandhya-vasudevan-2b14278"},
    {"@type": "Person", "name": "Suman Dash", "jobTitle": "COO, Acsel Technology Forum", "worksFor": {"@type": "Organization", "name": "Acsel Technology Forum"}, "sameAs": "https://in.linkedin.com/in/sumandash84"},
    {"@type": "Person", "name": "Shashank Randev", "jobTitle": "Founder and General Partner, 247VC", "worksFor": {"@type": "Organization", "name": "247VC"}, "sameAs": "https://in.linkedin.com/in/shashankrandev"}
  ]
}
</script>
```

---

## 5. /awards/winners-2026/ (new page, must be live before the hero goes up)

```html
<title>World AI Awards 2026 Winners | World AI Summit 2026, Bengaluru</title>
<meta name="description" content="Winners of the World AI Awards 2026, presented at World AI Summit 2026 in Bengaluru. See the winners by category and register interest for 2027.">
<link rel="canonical" href="https://www.worldaisummit.com/awards/winners-2026/">
```

```html
<h1>World AI Awards 2026: winners</h1>
<p>The World AI Awards 2026 were presented at World AI Summit 2026 in Bengaluru on PLACEHOLDER_AWARDS_DATE. Congratulations to every winner and nominee. Winners are listed below by category.</p>
<!-- PLACEHOLDER_WINNERS_LIST: one row per category: category name, winning organisation, project or entry title -->
<p><a href="/awards/">About the World AI Awards</a> · <a href="/#wais-2027">Register interest for World AI Summit 2027 &rarr;</a></p>
```

Add one line to the top of /awards/: `<p><a href="/awards/winners-2026/">See the World AI Awards 2026 winners &rarr;</a></p>`

---

## 6. /delegate/ banner (from 15 October evening)

```html
<div class="wais-banner" role="note">World AI Summit 2026 took place on 14-15 October in Bengaluru. Passes for the next edition are not yet on sale. <a href="/#wais-2027">Register interest for World AI Summit 2027 &rarr;</a></div>
```

---

## 7. /1st-edition/delegate-pass.html (2025 archive page)

This page is indexable and in the sitemap. Its title is "World AI Summit 2025 | Global AI Innovation Conference by Elets Technomedia". It lists pass tiers at Rs 30,000 and Rs 60,000 with no date, which are the same figures as the 2026 Late Access tier.

New title:
```html
<title>World AI Summit 2025 Delegate Passes (Archive) | Elets Technomedia</title>
```

Banner, from now until 15 October:
```html
<div class="wais-banner" role="note">You are viewing the World AI Summit 2025 archive. Passes for World AI Summit 2026, 14-15 October 2026 in Bengaluru, are on the <a href="/delegate/">2026 delegate page &rarr;</a></div>
```

Banner, from 15 October evening:
```html
<div class="wais-banner" role="note">You are viewing the World AI Summit 2025 archive. World AI Summit 2026 took place on 14-15 October 2026 in Bengaluru. <a href="/#wais-2027">Register interest for World AI Summit 2027 &rarr;</a></div>
```

Pass buy buttons on this page: PLACEHOLDER_DECISION_2025_BUY_BUTTONS. First check whether they open a live checkout. If they do, either remove them or point them to /delegate/ until 15 October.

---

## 8. Redirects

None. Do not redirect or move the homepage after the event. Keep `/` as the evergreen event URL and update its content for each edition. If the 2026 content is ever archived (for example to `/2nd-edition/`), do it only after the 2027 page is live on `/`, and add no redirect from `/`.
