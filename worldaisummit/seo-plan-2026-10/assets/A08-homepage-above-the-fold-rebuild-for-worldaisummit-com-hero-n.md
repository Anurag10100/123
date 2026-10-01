# A08: Homepage above-the-fold rebuild for worldaisummit.com: hero, nav, passes, awards, speakers, venue, FAQ, Event JSON-LD and redirects (corrected after verification)

- **For recommendation:** Homepage above the fold: event-name H1, Book / Nominate / Sponsor buttons instead of 'Save the date', crawlable links to the pages that bring in leads, and a new title and meta
- **Research lens:** site-deep-read
- **Format:** Markdown brief with paste-ready HTML snippets, Event JSON-LD (checked: it parses), Apache .htaccess and nginx redirect blocks
- **Placeholders the business must fill:**
  - PLACEHOLDER_CONFIRMED_SPEAKER_COUNT: events team to confirm. The live /assets/speaker_details/index.html says 50 confirmed; /speaker.html says '100+'. Use one number everywhere.
  - PLACEHOLDER_SPEAKER_SELECTION: events team to approve the 12 homepage speakers. Swap only for others marked 'Confirmed 2026' on the live index, and update JSON-LD performer to match.
  - PLACEHOLDER_PREMIUM_PRICE / PLACEHOLDER_PREMIUM_PRICE_NUMBER: current Premium price from sales. /delegate/ lists Late Access at ₹30,000 after Standard ended on 30 Sept 2026.
  - PLACEHOLDER_VIP_PRICE / PLACEHOLDER_VIP_PRICE_NUMBER: current VIP price from sales. /delegate/ lists Late Access at ₹60,000.
  - PLACEHOLDER_PRICE_VALID_TILL: date the current prices end.
  - PLACEHOLDER_GST_NOTE: whether prices include or exclude GST.
  - PLACEHOLDER_THIRD_COLUMN_DECISION: remove the third homepage pass column (VIP plus photos and videos), or name and price it and add it to /delegate/.
  - PLACEHOLDER_AWARDS_DEADLINE: World AI Awards 2026 nomination closing date. Also confirm nominations are still open.
  - PLACEHOLDER_AWARDS_FEE: 2026 entry fee (2025 was ₹18,000 + GST per entry).
  - PLACEHOLDER_AGENDA_URL: live agenda page URL, or hide the Agenda nav item until one exists.
  - PLACEHOLDER_AGENDA_STATUS: one sentence on whether the session-level agenda is published.
  - PLACEHOLDER_NEAREST_METRO: from the hotel events desk.
  - PLACEHOLDER_AIRPORT_TRAVEL_TIME: from the hotel events desk.
  - PLACEHOLDER_PARKING_DETAILS: from the hotel events desk.
  - PLACEHOLDER_EVENT_IMAGE_URL: absolute URL of an event image at least 1200px wide, for the JSON-LD.

## How to ship

Owners are web dev and content; deadline is 3 Oct 2026.

1. Get the business inputs first:
   - Sales: current Premium and VIP prices, validity date, GST note, and what to do with the third pass column.
   - Events team: the confirmed speaker count (the live speaker index says 50, /speaker.html says 100+), sign-off on the 12 names, the agenda URL and status, and the awards deadline and fee (2025 was ₹18,000 + GST).
   - Hotel events desk: nearest metro, airport travel time, parking.
2. Edit the shared homepage template so / and /index.html both change. Paste sections 1 to 9 over the matching blocks and change the second H1 ('Voices from the Main Stage') to an H2. Leave the title unchanged and replace only the meta.
3. Add the Event JSON-LD in section 10 to / only, with the prices as bare numbers and an absolute image URL. Delete any older Event markup first.
4. Same release, so the buttons do not land on stale pages:
   - Remove the expired Early Bird and Standard rows from /delegate/ and give it an H1.
   - Give /awards/ its own H1.
   - Make /partner-with-us.html self-canonical.
   - Update the 'from Rs 20,000' line in the speaker page template.
5. Deploy the redirects in section 11 (Apache or nginx, on both the www and non-www hosts) after deleting the existing /registration 302.
6. Run the QA checklist in section 12: one H1, plain hrefs, speaker URLs return 200, single-hop 301s, Rich Results Test, no PLACEHOLDER_ left. Then request indexing in Search Console and re-run the OpenSEO site audit to confirm /delegate/, /awards/, /partner-with-us.html and /speaker.html are at crawl depth 1.

Measure success by bookings, nominations and sponsor enquiries from homepage visits, not by ranking changes. Search impact is expected to be small, and there is no first-party CTR data for the www homepage.

## Content

# worldaisummit.com homepage: paste-ready changes (1 Oct 2026, ship by 3 Oct)

Pages: https://www.worldaisummit.com/ and /index.html (same template).

## 0. Changes from the original recommendation (verifier corrections)

- **Title: no change.** The audit (c1b16b55, 1 Oct) and the live Google India SERP for 'ai summit 2026' both show `World AI Summit 2026 | AI Summit India, Bengaluru, 14-15 October` (64 characters). It already gives the dates and the city, so a rewrite has no expected click gain. Exa's cache still shows the older title ('...Global Artificial Intelligence Conference by Elets Technomedia'). That title is now live only on /award.html, /partnership.html and /partner-with-us.html.
- **Do not expect much search gain.** 'ai summit 2026' (#7) is mostly people looking for India AI Impact Summit (Feb 2026), and the 40,500/mo average is inflated by February. We have no first-party CTR data for the www homepage. The likely gains are conversion, because the page now has a route to passes, awards and sponsorship, and link value passed to the pages that bring in leads.
- **Prices are not filled in.** /delegate/ (Exa, 1 Oct) says Standard Access (₹20,000 / ₹35,000) was valid till 30 Sept 2026 and then lists Late Access at ₹30,000 / ₹60,000. Sales must confirm the current prices.
- **Two tiers, not three.** /delegate/ sells only Premium and VIP. The third homepage column (VIP plus event photos and videos) has no matching tier.
- **The speaker count is a placeholder.** The live /assets/speaker_details/index.html (Exa, 1 Oct) says '50 confirmed speakers so far', but /speaker.html says '100+ speakers'. The events team must confirm one number and use it everywhere.
- **FAQ:** this is for conversion on the page only. Since Aug 2023 Google shows FAQ rich results only for authoritative government and health sites, so do not add FAQPage schema expecting a SERP feature.

Sources checked today:
- Venue address: Marriott rooms page for Sheraton Grand Bangalore Hotel at Brigade Gateway, plus Google Hotels and Apple Maps listings (via Exa, 1 Oct).
- Speakers: names come from the live /assets/speaker_details/index.html (Exa, 1 Oct), where each is marked 'Confirmed 2026'. The profile URL pattern was confirmed live for pankaj-kumar-pandey.html and sandeep-varaganti.html.
- Pass benefits: /delegate/ and the homepage (Exa, 1 Oct).

---

## 1. `<head>` (homepage and /index.html)

```html
<title>World AI Summit 2026 | AI Summit India, Bengaluru, 14-15 October</title>
<meta name="description" content="India's AI summit for enterprise, government and GCC leaders. 14-15 Oct 2026, Sheraton Grand Bangalore at Brigade Gateway. 7 tracks. Book your pass.">
<link rel="canonical" href="https://www.worldaisummit.com/">
```

- The title is unchanged. The meta is 148 characters and replaces the current 182-character one.
- If the events team confirms the count, use this 155-character variant: `India's AI summit for enterprise, government and GCC leaders. 14-15 Oct 2026, Sheraton Grand Bangalore at Brigade Gateway. PLACEHOLDER_CONFIRMED_SPEAKER_COUNT confirmed speakers. Book now.`
- /speaker.html currently uses the same meta as the homepage. Give it its own.

## 2. Header nav (plain links only)

If the mobile menu uses JavaScript, it must still output these `<a href>` tags in the HTML source. Do not use `href="#"` or onclick links.

```html
<nav class="site-nav" aria-label="Main">
  <a href="/speaker.html">Speakers</a>
  <a href="PLACEHOLDER_AGENDA_URL">Agenda</a>
  <a href="/delegate/">Passes</a>
  <a href="/awards/">Awards</a>
  <a href="/partner-with-us.html">Partner</a>
  <a href="/blog/">Blog</a>
  <a href="/#venue">Venue</a>
  <a class="nav-cta" href="/delegate/">Book pass</a>
</nav>
```

## 3. Hero (replaces the theme H1 and 'Save the date')

```html
<section class="hero" id="top">
  <h1>World AI Summit 2026: 14-15 October, Bengaluru</h1>
  <p class="hero-theme">AI for All: Accelerating India's Journey Towards Inclusive, Responsible and Future-Ready AI</p>
  <p class="hero-sub">Sheraton Grand Bangalore Hotel at Brigade Gateway · 7 tracks · PLACEHOLDER_CONFIRMED_SPEAKER_COUNT confirmed speakers</p>
  <div class="hero-cta">
    <a class="btn btn-primary" href="/delegate/">Book delegate pass</a>
    <a class="btn btn-secondary" href="/awards/">Nominate for World AI Awards 2026</a>
    <a class="btn btn-secondary" href="/partner-with-us.html">Sponsor or exhibit</a>
  </div>
</section>
```

- The page must have exactly one H1. Change `<h1>Voices from the Main Stage</h1>` to `<h2>`.
- /awards/ uses the same theme H1 and 'Save the date' hero. Give it its own H1, for example `World AI Awards 2026: Nominations`.

## 4. 'Secure your seat' block

```html
<section id="passes">
  <h2>Delegate passes</h2>
  <p>Two passes, both covering 14 and 15 October 2026. Prices valid till PLACEHOLDER_PRICE_VALID_TILL. PLACEHOLDER_GST_NOTE</p>

  <div class="pass">
    <h3>Premium Pass</h3>
    <p class="price">₹PLACEHOLDER_PREMIUM_PRICE / delegate</p>
    <ul>
      <li>Full summit access</li>
      <li>Delegate kit, lunch and refreshments</li>
      <li>Certificate of participation</li>
    </ul>
    <a class="btn" href="/delegate/">Book Premium Pass</a>
  </div>

  <div class="pass">
    <h3>VIP Pass</h3>
    <p class="price">₹PLACEHOLDER_VIP_PRICE / delegate</p>
    <ul>
      <li>All Premium benefits</li>
      <li>Priority seating</li>
      <li>Speaker lounge access</li>
      <li>Exclusive networking dinner</li>
      <li>Special sessions on GenAI, Agentic AI and AI Safety</li>
    </ul>
    <a class="btn" href="/delegate/">Book VIP Pass</a>
  </div>

  <!-- PLACEHOLDER_THIRD_COLUMN_DECISION: remove the third column (VIP + event photos and videos), or name it, price it and add it to /delegate/ -->

  <p>Group booking: 3 or more delegates get 10% off. Write to <a href="mailto:registration@worldaisummit.com">registration@worldaisummit.com</a>.</p>
</section>
```

- Delete the line 'Three release phases. The earlier you commit, the better the price.'
- Dependency: /delegate/ still shows the expired Early Bird (25 Jul 2025) and Standard (30 Sept 2026) rows and has no H1. Fix it the same day, or the new buttons will land on stale prices.
- Each speaker profile page also says 'Delegate passes from Rs 20,000'. Update that in the template.

## 5. Awards block (replaces 'World AI Awards · Previous edition')

```html
<section id="awards">
  <p class="eyebrow">World AI Awards 2026</p>
  <h2>World AI Awards 2026: nominations open</h2>
  <p>Recognising real-world applications of AI advancing industries, enhancing public services, and redefining innovation at global scale — across business innovation, public sector transformation, startups, leadership, and platforms.</p>
  <p>Nominations close PLACEHOLDER_AWARDS_DEADLINE. Entry fee: PLACEHOLDER_AWARDS_FEE per entry.</p>
  <a class="btn" href="/awards/">Nominate for World AI Awards 2026</a>
</section>
```

## 6. 'Meet The Visionaries': 12 confirmed 2026 speakers as HTML text

All 12 are marked 'Confirmed 2026' on the live /assets/speaker_details/index.html. PLACEHOLDER_SPEAKER_SELECTION: the events team may swap names, but only for others marked Confirmed 2026. Keep the existing 2025 testimonial quotes below this list.

```html
<section id="speakers">
  <h2>Meet The Visionaries</h2>
  <p>Confirmed speakers for World AI Summit 2026. Roles and organisations as at announcement.</p>
  <ul class="speaker-grid">
    <li><a href="/assets/speaker_details/pankaj-kumar-pandey.html"><strong>Pankaj Kumar Pandey, IAS</strong><span>Principal Secretary, e-Governance</span><span>Government of Karnataka</span></a></li>
    <li><a href="/assets/speaker_details/sanjeev-gupta.html"><strong>Sanjeev Gupta</strong><span>CEO</span><span>Karnataka Digital Economy Mission</span></a></li>
    <li><a href="/assets/speaker_details/ram-mohan-rao.html"><strong>Ram Mohan Rao</strong><span>Executive Director</span><span>SEBI</span></a></li>
    <li><a href="/assets/speaker_details/mahesh-hariharan-iyer.html"><strong>Mahesh Hariharan Iyer</strong><span>VP Engineering</span><span>Reserve Bank Innovation Hub</span></a></li>
    <li><a href="/assets/speaker_details/sandeep-varaganti.html"><strong>Sandeep Varaganti</strong><span>CEO, JioMart</span><span>Reliance Retail</span></a></li>
    <li><a href="/assets/speaker_details/anand-thakur.html"><strong>Anand Thakur</strong><span>Chief Product and Technology Officer</span><span>Reliance Retail</span></a></li>
    <li><a href="/assets/speaker_details/tulshekar-gangireddy.html"><strong>Tulshekar Gangireddy</strong><span>ED and Head of Data Strategy</span><span>JPMorgan Chase</span></a></li>
    <li><a href="/assets/speaker_details/pawan-sachdeva.html"><strong>Pawan Sachdeva</strong><span>Senior MD and Technology Head, India</span><span>Carelon Global Solutions</span></a></li>
    <li><a href="/assets/speaker_details/deepika-sandeep.html"><strong>Deepika Sandeep</strong><span>Head, AI/ML CoE</span><span>HSBC</span></a></li>
    <li><a href="/assets/speaker_details/suman-guha.html"><strong>Suman Guha</strong><span>Chief Digital and Technology Officer</span><span>Croma</span></a></li>
    <li><a href="/assets/speaker_details/shalini-kapoor.html"><strong>Shalini Kapoor</strong><span>Chief Strategist, Data and AI</span><span>EkStep Foundation</span></a></li>
    <li><a href="/assets/speaker_details/sandhya-vasudevan.html"><strong>Sandhya Vasudevan</strong><span>Board Member</span><span>TiE Bangalore</span></a></li>
  </ul>
  <a class="btn" href="/assets/speaker_details/index.html">See all PLACEHOLDER_CONFIRMED_SPEAKER_COUNT confirmed speakers</a>
</section>
```

This links to /assets/speaker_details/index.html because that page lists every confirmed name. /speaker.html shows only one name and says '100+'. Keep /speaker.html in the nav, and align its count with the events team's number.

## 7. Venue block

```html
<section id="venue">
  <h2>Venue: Sheraton Grand Bangalore Hotel at Brigade Gateway</h2>
  <address>26/1 Dr Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru, Karnataka 560055</address>
  <ul>
    <li>Nearest metro station: PLACEHOLDER_NEAREST_METRO</li>
    <li>From Kempegowda International Airport: PLACEHOLDER_AIRPORT_TRAVEL_TIME</li>
    <li>Parking: PLACEHOLDER_PARKING_DETAILS</li>
  </ul>
  <a href="[keep existing Get Directions href]">Get directions</a>
</section>
```

Get the metro, airport and parking details from the hotel's events desk. Do not fill them in from memory.

## 8. FAQ (replaces or extends the 10 generic questions)

Keep the answers in the HTML source. A `<details>` accordion is fine; answers loaded by JavaScript are not.

**When and where is World AI Summit 2026?**
On 14 and 15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, 26/1 Dr Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru 560055. [Plan your visit](/#venue)

**How much is a delegate pass, and what is included?**
There are two passes.
- Premium Pass (₹PLACEHOLDER_PREMIUM_PRICE): full summit access, delegate kit, lunch and refreshments, and a certificate of participation.
- VIP Pass (₹PLACEHOLDER_VIP_PRICE): all Premium benefits, plus priority seating, speaker lounge access, an exclusive networking dinner, and special sessions on GenAI, Agentic AI and AI Safety.

PLACEHOLDER_GST_NOTE [Book a pass](/delegate/)

**Is there a group discount?**
Yes. Groups of 3 or more delegates get 10% off. Write to [registration@worldaisummit.com](mailto:registration@worldaisummit.com).

**How do I nominate for the World AI Awards 2026, and what are the deadline and fee?**
Apply online: choose a sector, describe the project, its impact and scale, and upload supporting documents. Nominations close PLACEHOLDER_AWARDS_DEADLINE. The entry fee is PLACEHOLDER_AWARDS_FEE per entry. [Nominate now](/awards/)

**How can my organisation sponsor or exhibit?**
Write to [partnerships@worldaisummit.com](mailto:partnerships@worldaisummit.com) or see the [partnership options](/partner-with-us.html).

**Who is speaking?**
PLACEHOLDER_CONFIRMED_SPEAKER_COUNT speakers are confirmed so far, from government, regulators, banks, GCCs and enterprises. More names are added as they are announced. [See all confirmed speakers](/assets/speaker_details/index.html)

**Is the agenda out?**
The programme runs across seven tracks:
- Frontier Models & Compute
- Sovereign AI & Geopolitics
- Enterprise AI in Production
- Global Capability Centres (GCCs)
- Robotics, Agents & Embodied AI
- AI for Bharat
- Capital, Founders & Exits

PLACEHOLDER_AGENDA_STATUS. Session times and halls appear on each speaker page and on the agenda once the programme is final. [View agenda](PLACEHOLDER_AGENDA_URL)

**How do I reach the venue?**
The hotel is at 26/1 Dr Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru 560055.
- Nearest metro station: PLACEHOLDER_NEAREST_METRO
- From the airport: PLACEHOLDER_AIRPORT_TRAVEL_TIME
- Parking: PLACEHOLDER_PARKING_DETAILS

**Can I speak at the summit?**
Write to [secretariat@worldaisummit.com](mailto:secretariat@worldaisummit.com) with your name, role, organisation and proposed topic.

**Who organises World AI Summit?**
World AI Summit is organised by Elets Technomedia.

## 9. Footer links (plain `<a href>`)

```html
<footer>
  <nav aria-label="Footer">
    <a href="/delegate/">Delegate passes</a>
    <a href="/awards/">World AI Awards 2026</a>
    <a href="/partner-with-us.html">Sponsor or exhibit</a>
    <a href="/speaker.html">Speakers</a>
    <a href="/assets/speaker_details/index.html">All confirmed speakers</a>
    <a href="PLACEHOLDER_AGENDA_URL">Agenda</a>
    <a href="/ai-conference-bengaluru-2026.html">AI conference in Bengaluru, October 2026</a>
    <a href="/blog/">Blog</a>
  </nav>
  <p>Delegates: <a href="mailto:registration@worldaisummit.com">registration@worldaisummit.com</a> · Partnerships: <a href="mailto:partnerships@worldaisummit.com">partnerships@worldaisummit.com</a> · Speaking: <a href="mailto:secretariat@worldaisummit.com">secretariat@worldaisummit.com</a></p>
</footer>
```

Also: /partner-with-us.html currently has its canonical set to /. Make it self-canonical (`<link rel="canonical" href="https://www.worldaisummit.com/partner-with-us.html">`) so Google can index the Sponsor button's target page.

## 10. Event JSON-LD (homepage only; delete any existing Event block first)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Event",
  "@id": "https://www.worldaisummit.com/#event",
  "name": "World AI Summit 2026",
  "description": "India's AI summit for enterprise, government and GCC leaders, with seven tracks: Frontier Models & Compute; Sovereign AI & Geopolitics; Enterprise AI in Production; Global Capability Centres (GCCs); Robotics, Agents & Embodied AI; AI for Bharat; Capital, Founders & Exits.",
  "url": "https://www.worldaisummit.com/",
  "image": ["PLACEHOLDER_EVENT_IMAGE_URL"],
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
  "offers": [
    {
      "@type": "Offer",
      "name": "Premium Pass",
      "url": "https://www.worldaisummit.com/delegate/",
      "price": "PLACEHOLDER_PREMIUM_PRICE_NUMBER",
      "priceCurrency": "INR",
      "availability": "https://schema.org/InStock",
      "validFrom": "2026-10-01"
    },
    {
      "@type": "Offer",
      "name": "VIP Pass",
      "url": "https://www.worldaisummit.com/delegate/",
      "price": "PLACEHOLDER_VIP_PRICE_NUMBER",
      "priceCurrency": "INR",
      "availability": "https://schema.org/InStock",
      "validFrom": "2026-10-01"
    }
  ],
  "performer": [
    {"@type": "Person", "name": "Pankaj Kumar Pandey", "honorificSuffix": "IAS", "jobTitle": "Principal Secretary, Department of Personnel and Administrative Reforms (e-Governance)", "worksFor": {"@type": "Organization", "name": "Government of Karnataka"}, "url": "https://www.worldaisummit.com/assets/speaker_details/pankaj-kumar-pandey.html"},
    {"@type": "Person", "name": "Sanjeev Gupta", "jobTitle": "Chief Executive Officer", "worksFor": {"@type": "Organization", "name": "Karnataka Digital Economy Mission"}, "url": "https://www.worldaisummit.com/assets/speaker_details/sanjeev-gupta.html"},
    {"@type": "Person", "name": "Ram Mohan Rao", "jobTitle": "Executive Director", "worksFor": {"@type": "Organization", "name": "Securities and Exchange Board of India (SEBI)"}, "url": "https://www.worldaisummit.com/assets/speaker_details/ram-mohan-rao.html"},
    {"@type": "Person", "name": "Mahesh Hariharan Iyer", "jobTitle": "Vice President of Engineering", "worksFor": {"@type": "Organization", "name": "Reserve Bank Innovation Hub (RBIH)"}, "url": "https://www.worldaisummit.com/assets/speaker_details/mahesh-hariharan-iyer.html"},
    {"@type": "Person", "name": "Sandeep Varaganti", "jobTitle": "CEO, JioMart", "worksFor": {"@type": "Organization", "name": "Reliance Retail"}, "url": "https://www.worldaisummit.com/assets/speaker_details/sandeep-varaganti.html"},
    {"@type": "Person", "name": "Anand Thakur", "jobTitle": "Chief Product and Technology Officer", "worksFor": {"@type": "Organization", "name": "Reliance Retail"}, "url": "https://www.worldaisummit.com/assets/speaker_details/anand-thakur.html"},
    {"@type": "Person", "name": "Tulshekar Gangireddy", "jobTitle": "Executive Director & Head of Data Strategy", "worksFor": {"@type": "Organization", "name": "JPMorgan Chase & Co"}, "url": "https://www.worldaisummit.com/assets/speaker_details/tulshekar-gangireddy.html"},
    {"@type": "Person", "name": "Pawan Sachdeva", "jobTitle": "Senior Managing Director and Technology Head - India", "worksFor": {"@type": "Organization", "name": "Carelon Global Solutions"}, "url": "https://www.worldaisummit.com/assets/speaker_details/pawan-sachdeva.html"},
    {"@type": "Person", "name": "Deepika Sandeep", "jobTitle": "Head - AI/ML CoE", "worksFor": {"@type": "Organization", "name": "HSBC"}, "url": "https://www.worldaisummit.com/assets/speaker_details/deepika-sandeep.html"},
    {"@type": "Person", "name": "Suman Guha", "jobTitle": "Chief Digital & Technology Officer", "worksFor": {"@type": "Organization", "name": "Tata Croma (Tata Digital)"}, "url": "https://www.worldaisummit.com/assets/speaker_details/suman-guha.html"},
    {"@type": "Person", "name": "Shalini Kapoor", "jobTitle": "Chief Strategist - Data and AI", "worksFor": {"@type": "Organization", "name": "EkStep Foundation"}, "url": "https://www.worldaisummit.com/assets/speaker_details/shalini-kapoor.html"},
    {"@type": "Person", "name": "Sandhya Vasudevan", "jobTitle": "Board Member", "worksFor": {"@type": "Organization", "name": "TiE Bangalore"}, "url": "https://www.worldaisummit.com/assets/speaker_details/sandhya-vasudevan.html"}
  ]
}
</script>
```

- Before publishing, replace the price placeholders with bare numbers (for example `30000`, no ₹ sign or comma) and replace the image placeholder with an absolute URL to a 1200px or wider event image.
- If the events team swaps names in section 6, change `performer` to match.

## 11. Redirects

Today /registration and /registration.html return a 302 to the homepage through the non-www host, which takes 3 hops. The fix sends them to the pass page in one 301. It also adds a 301 from /index.html to /. Apply the rules on both the www and the non-www vhosts, and delete the existing 302 rule for /registration first.

### Apache (.htaccess at the web root)

```apache
RewriteEngine On

# /registration, /registration/ and /registration.html -> pass page, one hop
RewriteRule ^registration(\.html)?/?$ https://www.worldaisummit.com/delegate/ [R=301,L,NC]

# /index.html -> / (only when requested directly, so DirectoryIndex does not loop)
RewriteCond %{THE_REQUEST} \s/index\.html[\s?] [NC]
RewriteRule ^index\.html$ https://www.worldaisummit.com/ [R=301,L]
```

Apache keeps query strings such as UTM tags by default.

### nginx (inside each `server {}` block for www and non-www)

```nginx
# /registration, /registration/ and /registration.html -> pass page, one hop
location ~* ^/registration(\.html)?/?$ {
    return 301 https://www.worldaisummit.com/delegate/$is_args$args;
}

# /index.html -> / (match on $request_uri so the internal index lookup does not loop)
if ($request_uri ~* "^/index\.html(\?|$)") {
    return 301 https://www.worldaisummit.com/$is_args$args;
}
```

Optional: redirect /award.html to /awards/ and /partnership.html to /partner-with-us.html, but only if a content check shows each one duplicates its target. Both still carry the old title and have their canonical set to /.

## 12. QA before release (3 Oct)

1. View the source of / and check that it has exactly one `<h1>` and that every nav, hero, pass, awards, speaker and footer link is a plain `<a href>` to a real URL. There should be no `#` or `javascript:` links.
2. Check that all 12 speaker profile links return 200:
   ```bash
   for s in pankaj-kumar-pandey sanjeev-gupta ram-mohan-rao mahesh-hariharan-iyer sandeep-varaganti anand-thakur tulshekar-gangireddy pawan-sachdeva deepika-sandeep suman-guha shalini-kapoor sandhya-vasudevan; do
     curl -s -o /dev/null -w "%{http_code} $s\n" https://www.worldaisummit.com/assets/speaker_details/$s.html
   done
   ```
3. Check the redirects. Each should be a single 301 to its final URL:
   ```bash
   curl -sIL https://www.worldaisummit.com/registration | grep -iE '^(HTTP|location)'
   curl -sIL https://worldaisummit.com/registration.html | grep -iE '^(HTTP|location)'
   curl -sIL https://www.worldaisummit.com/index.html | grep -iE '^(HTTP|location)'
   ```
4. Run Google's Rich Results Test on / and check that the Event is detected with no price or image errors.
5. Search the page source for `PLACEHOLDER_` and make sure nothing is left.
6. In Search Console, request indexing for /, /delegate/, /awards/ and /partner-with-us.html. Then run a new OpenSEO audit and check that these pages now have crawl depth 1.
