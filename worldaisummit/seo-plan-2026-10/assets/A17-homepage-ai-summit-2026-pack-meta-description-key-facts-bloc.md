# A17: Homepage 'ai summit 2026' pack: meta description, key facts block, rewritten FAQ, Event and FAQPage JSON-LD, supporting-page link, indiaaisummit.in banner

- **For recommendation:** Homepage: lift the only large non-brand October demand, 'ai summit 2026' and 'ai summit' (both #7), with a disambiguating facts and FAQ block
- **Research lens:** demand-sweep
- **Format:** HTML snippets + JSON-LD (static HTML site), one block per section
- **Placeholders the business must fill:**
  - PLACEHOLDER_CURRENT_PASS_PRICE_INR (the Rs 20,000 homepage Premium Pass vs /delegate/ Late Access Rs 30,000/60,000 conflict; the Standard tier expired 30 Sept 2026)
  - PLACEHOLDER_EVENT_IMAGE_URL (absolute URL of an event image on worldaisummit.com at least 1200 px wide, or delete the image line)
  - PLACEHOLDER_AWARD_DEADLINE (optional sentence for the World AI Awards answer; 2026 deadline and fee not published)
  - Performer list: confirm all eight confirmed_2026 speakers are publicly announced and visible on the live homepage before publishing; remove any who are not

## How to ship

Ship by 3 Oct 2026. Web dev, about 1-2 hours on the static HTML.

1. In index.html (the homepage; /index.html already canonicalises to /):
   - Swap the meta description (section 1).
   - Insert the key facts block under the hero (section 2).
   - Replace the existing FAQ accordion markup with section 3. Edit it in place and keep a single FAQ block.
   - Add the two JSON-LD scripts (sections 4 and 5). Before adding them, search the page source for "FAQPage" and "\"Event\"" and delete any older blocks, so there is only one of each.
2. Fill in or remove the PLACEHOLDER_ values before going live:
   - Price: digits, or delete the price and priceCurrency lines.
   - Image: an absolute URL, or delete the line.
   - The optional sentences stay out until decided.
3. Check that each Event performer is visible on the live homepage. Remove any who are not.
4. Add the link on /ai-conference-bengaluru-2026.html (section 6).
5. Add the banner on indiaaisummit.in (section 7).
6. Run https://www.worldaisummit.com/ through Google's Rich Results Test and the validator at validator.schema.org. Expect Event to pass. FAQPage will validate but will not show as a Google rich result, because Google limits FAQ rich results to authoritative government and health sites. Its value here is the visible FAQ text and machine-readable answers for AI Overviews.
7. Request indexing for / in Search Console. Only the non-www property is connected, so add the https://www.worldaisummit.com/ property (or a Domain property) first, or the inspection will not cover the www URL.
8. Recheck positions for 'ai summit 2026' and 'ai summit' on 8 and 15 Oct.

The verifier said the FAQ has 5 questions; the live FAQ has 10, and the mapping is listed in section 3. The Google snippet already shows the date and venue, so expect most of the gain from the disambiguation FAQ and facts text, not from the meta description.

## Content

=====================================================================
1. META DESCRIPTION  (https://www.worldaisummit.com/ , replaces the 182-character tag)
=====================================================================
<meta name="description" content="World AI Summit 2026, an AI summit in Bengaluru on 14-15 October: 7 tracks, policymakers, CXOs, GCC heads and founders. Book your delegate pass.">

- 144 characters. Following verifier note 5, "India's AI summit" is now "an AI summit in Bengaluru", so the copy no longer sounds like a claim to be the national summit.
- If og:description or twitter:description still carry the old 182-character copy, put this same text in them.
- Leave the <title> as it is. Google already rewrites it as "World AI Summit 2026 | AI Summit India, Bengaluru, 14-15 ...".

=====================================================================
2. KEY FACTS BLOCK  (put directly under the hero, after the "Bengaluru, India / Sheraton Grand..." line; 142 words)
=====================================================================
<section id="key-facts" aria-labelledby="key-facts-title">
  <h2 id="key-facts-title">AI Summit 2026 in Bengaluru: key facts</h2>
  <p>World AI Summit 2026 is a two-day artificial intelligence conference organised by Elets Technomedia in Bengaluru, India.</p>
  <ul>
    <li><strong>Dates:</strong> Wednesday 14 and Thursday 15 October 2026</li>
    <li><strong>Venue:</strong> Sheraton Grand Bangalore Hotel at Brigade Gateway, 26/1 Dr Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru 560055</li>
    <li><strong>Seven tracks:</strong> Frontier Models &amp; Compute; Sovereign AI &amp; Geopolitics; Enterprise AI in Production; Global Capability Centres (GCCs); Robotics, Agents &amp; Embodied AI; AI for Bharat; Capital, Founders &amp; Exits</li>
    <li><strong>Who attends:</strong> policymakers and government officials, CIOs, CTOs and CDOs, AI and data science leaders, GCC leaders, startup founders, investors, researchers and technology vendors</li>
    <li><strong>Awards:</strong> the <a href="/awards/">World AI Awards</a> recognise real-world applications of AI</li>
    <li><strong>Group booking:</strong> 10% off for 3 or more delegates</li>
  </ul>
  <p>Not to be confused with the India AI Impact Summit (New Delhi, February 2026) or World Summit AI (Amsterdam).</p>
  <p><a class="btn" href="/delegate/">Book delegate pass</a></p>
</section>

Once the price conflict is settled, you may add this line: <li><strong>Delegate pass:</strong> Rs PLACEHOLDER_CURRENT_PASS_PRICE_INR per delegate</li>

=====================================================================
3. FAQ: REPLACE THE EXISTING HOMEPAGE ACCORDION IN PLACE (keep one FAQ block only)
=====================================================================
Note: the live FAQ (Exa fetch, 1 Oct 2026) has 10 questions, not 5.
- Rewritten: "What is the World AI Summit?", "What topics...", "How can I register..." (the generic "official website" answer now links to /delegate/), "Can startups participate?", "Are exhibition and sponsorship opportunities available?", "How can I become a speaker or partner?", "Are there networking opportunities?" and "certificate".
- Dropped: "What are the key benefits of attending?" and "How can I stay updated?". They are generic and repeat other answers. You can keep them if you like, but keep them out of the JSON-LD unless they stay visible.
- Added: "When and where", the two disambiguation questions, "Who should attend?" and the awards question.

<section id="faq" aria-labelledby="faq-title">
  <h2 id="faq-title">Frequently asked questions</h2>
  <details>
    <summary>When and where is World AI Summit 2026?</summary>
    <p>World AI Summit 2026 takes place on Wednesday 14 and Thursday 15 October 2026 at the Sheraton Grand Bangalore Hotel at Brigade Gateway, 26/1 Dr Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru 560055.</p>
  </details>
  <details>
    <summary>Is World AI Summit the same as the India AI Impact Summit?</summary>
    <p>No. The India AI Impact Summit was the Government of India's summit held at Bharat Mandapam, New Delhi, on 16-20 February 2026. World AI Summit 2026 is a separate conference organised by Elets Technomedia in Bengaluru on 14-15 October 2026.</p>
  </details>
  <details>
    <summary>Is World AI Summit the same as World Summit AI?</summary>
    <p>No. World Summit AI is a separate event held in Amsterdam and run by a different organiser. World AI Summit 2026 is organised by Elets Technomedia in Bengaluru, India.</p>
  </details>
  <details>
    <summary>How do I register for World AI Summit 2026?</summary>
    <p>Book your delegate pass on the <a href="/delegate/">delegate pass page</a>. Groups of 3 or more delegates get 10% off. For group bookings, write to <a href="mailto:registration@worldaisummit.com">registration@worldaisummit.com</a>.</p>
  </details>
  <details>
    <summary>What is the World AI Summit?</summary>
    <p>World AI Summit is an artificial intelligence conference organised by Elets Technomedia in Bengaluru. The 2026 edition brings together policymakers, enterprise technology leaders, GCC leaders, researchers, startup founders and investors to discuss how India builds, governs and adopts AI responsibly.</p>
  </details>
  <details>
    <summary>What topics will the summit cover?</summary>
    <p>The 2026 programme runs across seven tracks: Frontier Models &amp; Compute; Sovereign AI &amp; Geopolitics; Enterprise AI in Production; Global Capability Centres (GCCs); Robotics, Agents &amp; Embodied AI; AI for Bharat; and Capital, Founders &amp; Exits.</p>
  </details>
  <details>
    <summary>Who should attend?</summary>
    <p>Government officials and policymakers, CIOs, CTOs and CDOs, AI and data science leaders, startup founders, investors and venture capitalists, academia and researchers, international organisations and think tanks, and technology vendors.</p>
  </details>
  <details>
    <summary>Can startups take part?</summary>
    <p>Yes. Founders can attend as delegates, and the Capital, Founders &amp; Exits track covers AI startup funding, investment trends, scaling and exits. To exhibit or partner, write to <a href="mailto:partnerships@worldaisummit.com">partnerships@worldaisummit.com</a>.</p>
  </details>
  <details>
    <summary>Can my company sponsor or exhibit?</summary>
    <p>Yes. For sponsorship, exhibition and partnership options, write to <a href="mailto:partnerships@worldaisummit.com">partnerships@worldaisummit.com</a>.</p>
  </details>
  <details>
    <summary>How can I become a speaker?</summary>
    <p>Send speaking and collaboration proposals to <a href="mailto:secretariat@worldaisummit.com">secretariat@worldaisummit.com</a>. The organising team reviews each proposal for relevance to the seven tracks.</p>
  </details>
  <details>
    <summary>How do I nominate for the World AI Awards?</summary>
    <p>Submit a nomination on the <a href="/awards/">World AI Awards page</a>. The awards recognise real-world applications of AI across business innovation, public sector transformation, startups, leadership and platforms.</p>
  </details>
  <details>
    <summary>Are there networking opportunities?</summary>
    <p>Yes. The programme includes networking with policymakers, industry leaders, investors and startups, along with curated roundtables and masterclasses.</p>
  </details>
  <details>
    <summary>Will delegates receive a certificate of participation?</summary>
    <p>Yes. Delegates who attend receive a certificate of participation.</p>
  </details>
</section>

Optional sentences. Add each one to the visible answer and to the JSON-LD at the same time, and only once the business has decided:
- Register answer: "Delegate passes currently cost Rs PLACEHOLDER_CURRENT_PASS_PRICE_INR per delegate."
- Awards answer: "Nominations close on PLACEHOLDER_AWARD_DEADLINE."

=====================================================================
4. FAQPage JSON-LD  (in <head> or before </body>; the text matches the visible FAQ exactly; checked as valid JSON)
=====================================================================
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"When and where is World AI Summit 2026?","acceptedAnswer":{"@type":"Answer","text":"World AI Summit 2026 takes place on Wednesday 14 and Thursday 15 October 2026 at the Sheraton Grand Bangalore Hotel at Brigade Gateway, 26/1 Dr Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru 560055."}},{"@type":"Question","name":"Is World AI Summit the same as the India AI Impact Summit?","acceptedAnswer":{"@type":"Answer","text":"No. The India AI Impact Summit was the Government of India's summit held at Bharat Mandapam, New Delhi, on 16-20 February 2026. World AI Summit 2026 is a separate conference organised by Elets Technomedia in Bengaluru on 14-15 October 2026."}},{"@type":"Question","name":"Is World AI Summit the same as World Summit AI?","acceptedAnswer":{"@type":"Answer","text":"No. World Summit AI is a separate event held in Amsterdam and run by a different organiser. World AI Summit 2026 is organised by Elets Technomedia in Bengaluru, India."}},{"@type":"Question","name":"How do I register for World AI Summit 2026?","acceptedAnswer":{"@type":"Answer","text":"Book your delegate pass on the <a href=\"https://www.worldaisummit.com/delegate/\">delegate pass page</a>. Groups of 3 or more delegates get 10% off. For group bookings, write to registration@worldaisummit.com."}},{"@type":"Question","name":"What is the World AI Summit?","acceptedAnswer":{"@type":"Answer","text":"World AI Summit is an artificial intelligence conference organised by Elets Technomedia in Bengaluru. The 2026 edition brings together policymakers, enterprise technology leaders, GCC leaders, researchers, startup founders and investors to discuss how India builds, governs and adopts AI responsibly."}},{"@type":"Question","name":"What topics will the summit cover?","acceptedAnswer":{"@type":"Answer","text":"The 2026 programme runs across seven tracks: Frontier Models & Compute; Sovereign AI & Geopolitics; Enterprise AI in Production; Global Capability Centres (GCCs); Robotics, Agents & Embodied AI; AI for Bharat; and Capital, Founders & Exits."}},{"@type":"Question","name":"Who should attend?","acceptedAnswer":{"@type":"Answer","text":"Government officials and policymakers, CIOs, CTOs and CDOs, AI and data science leaders, startup founders, investors and venture capitalists, academia and researchers, international organisations and think tanks, and technology vendors."}},{"@type":"Question","name":"Can startups take part?","acceptedAnswer":{"@type":"Answer","text":"Yes. Founders can attend as delegates, and the Capital, Founders & Exits track covers AI startup funding, investment trends, scaling and exits. To exhibit or partner, write to partnerships@worldaisummit.com."}},{"@type":"Question","name":"Can my company sponsor or exhibit?","acceptedAnswer":{"@type":"Answer","text":"Yes. For sponsorship, exhibition and partnership options, write to partnerships@worldaisummit.com."}},{"@type":"Question","name":"How can I become a speaker?","acceptedAnswer":{"@type":"Answer","text":"Send speaking and collaboration proposals to secretariat@worldaisummit.com. The organising team reviews each proposal for relevance to the seven tracks."}},{"@type":"Question","name":"How do I nominate for the World AI Awards?","acceptedAnswer":{"@type":"Answer","text":"Submit a nomination on the <a href=\"https://www.worldaisummit.com/awards/\">World AI Awards page</a>. The awards recognise real-world applications of AI across business innovation, public sector transformation, startups, leadership and platforms."}},{"@type":"Question","name":"Are there networking opportunities?","acceptedAnswer":{"@type":"Answer","text":"Yes. The programme includes networking with policymakers, industry leaders, investors and startups, along with curated roundtables and masterclasses."}},{"@type":"Question","name":"Will delegates receive a certificate of participation?","acceptedAnswer":{"@type":"Answer","text":"Yes. Delegates who attend receive a certificate of participation."}}]}
</script>

=====================================================================
5. EVENT JSON-LD  (homepage only; checked as valid JSON; replace PLACEHOLDER_ values before publishing)
=====================================================================
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Event",
  "@id": "https://www.worldaisummit.com/#event-2026",
  "name": "World AI Summit 2026",
  "description": "World AI Summit 2026 is a two-day artificial intelligence conference in Bengaluru organised by Elets Technomedia, with seven tracks: Frontier Models & Compute; Sovereign AI & Geopolitics; Enterprise AI in Production; Global Capability Centres (GCCs); Robotics, Agents & Embodied AI; AI for Bharat; and Capital, Founders & Exits.",
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
      "streetAddress": "26/1 Dr Rajkumar Road, Malleswaram-Rajajinagar",
      "addressLocality": "Bengaluru",
      "addressRegion": "Karnataka",
      "postalCode": "560055",
      "addressCountry": "IN"
    }
  },
  "image": ["PLACEHOLDER_EVENT_IMAGE_URL"],
  "organizer": {
    "@type": "Organization",
    "name": "Elets Technomedia",
    "url": "https://eletsonline.com/"
  },
  "offers": {
    "@type": "Offer",
    "name": "Delegate pass",
    "url": "https://www.worldaisummit.com/delegate/",
    "price": "PLACEHOLDER_CURRENT_PASS_PRICE_INR",
    "priceCurrency": "INR",
    "availability": "https://schema.org/InStock"
  },
  "performer": [
    {"@type": "Person", "name": "Pankaj Kumar Pandey", "honorificSuffix": "IAS", "jobTitle": "Principal Secretary, Department of Personnel and Administrative Reforms (e-Governance)", "worksFor": {"@type": "Organization", "name": "Government of Karnataka"}, "sameAs": "https://www.linkedin.com/in/pankaj-pandey-i-a-s-6b6882191"},
    {"@type": "Person", "name": "Sanjeev Gupta", "jobTitle": "Chief Executive Officer", "worksFor": {"@type": "Organization", "name": "Karnataka Digital Economy Mission"}, "sameAs": "https://in.linkedin.com/in/sanjeevkgupta"},
    {"@type": "Person", "name": "Ram Mohan Rao", "jobTitle": "Executive Director", "worksFor": {"@type": "Organization", "name": "Securities and Exchange Board of India (SEBI)"}, "sameAs": "https://in.linkedin.com/in/g-ram-mohan-rao"},
    {"@type": "Person", "name": "Shalini Kapoor", "jobTitle": "Chief Strategist - Data and AI", "worksFor": {"@type": "Organization", "name": "EkStep Foundation"}, "sameAs": "https://www.linkedin.com/in/kshalini"},
    {"@type": "Person", "name": "Sandeep Varaganti", "jobTitle": "CEO, JioMart", "worksFor": {"@type": "Organization", "name": "Reliance Retail"}, "sameAs": "https://in.linkedin.com/in/sandeepvaraganti"},
    {"@type": "Person", "name": "Deepika Sandeep", "jobTitle": "Head - AI/ML CoE", "worksFor": {"@type": "Organization", "name": "HSBC"}, "sameAs": "https://in.linkedin.com/in/deepika-sandeep"},
    {"@type": "Person", "name": "Sandhya Vasudevan", "jobTitle": "Board Member", "worksFor": {"@type": "Organization", "name": "TiE Bangalore"}, "sameAs": "https://www.linkedin.com/in/sandhya-vasudevan-2b14278"},
    {"@type": "Person", "name": "Shashank Randev", "jobTitle": "Founder & General Partner", "worksFor": {"@type": "Organization", "name": "247VC"}, "sameAs": "https://in.linkedin.com/in/shashankrandev"}
  ]
}
</script>

Notes on the Event JSON-LD:
- price: use digits only (for example "30000"). If the Rs 20,000 vs Late Access question is still open on 3 Oct, delete the "price" and "priceCurrency" lines. The Offer is still valid with url and availability; Google only shows a warning.
- image: use the absolute URL of an event image at least 1200 px wide on worldaisummit.com. If there is none, delete the "image" line, since image is recommended, not required.
- performer: all eight have confirmed_2026: true in worldaisummit/speakers/speakers.json, with bio_confidence "high". Keep a name only if it also appears in the speaker section of the live homepage. Remove any name the programme team has not publicly announced. Add more only from confirmed_2026: true entries.
- startDate and endDate are dates only, which is valid. Add times with +05:30 (for example 2026-10-14T09:00:00+05:30) once the agenda timings are final.

=====================================================================
6. SUPPORTING PAGE LINK  (/ai-conference-bengaluru-2026.html, in the first or second paragraph)
=====================================================================
<p>For dates, venue, tracks and delegate passes, see <a href="/">AI summit 2026 in Bengaluru</a>.</p>
(Do not change this page's title or H1 to target "ai summit 2026" or "ai summit". The homepage stays the target for those terms.)

=====================================================================
7. indiaaisummit.in TOP BANNER  (first element inside <body>, on all pages)
=====================================================================
<div class="wais-next" role="note" style="background:#0b1f3a;color:#ffffff;text-align:center;padding:10px 16px;font-size:15px;line-height:1.4;">
  Next: <a href="https://www.worldaisummit.com/" style="color:#ffffff;text-decoration:underline;">World AI Summit 2026, Bengaluru, 14-15 October</a>
</div>
(Keep the indiaaisummit.in line "Official Pre-Summit Event of the AI Impact Summit 2026" as it is. That line is about the 22 Jan 2026 Delhi event. The banner does not say World AI Summit is part of the AI Impact Summit, so the two sites stay consistent with the homepage FAQ.)

Redirects: this change needs none. The 3-hop /registration redirect is a separate fix.

Sources checked now:
- Homepage content and current FAQ: Exa fetch of https://www.worldaisummit.com/, 1 Oct 2026.
- Venue address: https://www.marriott.com/en-us/hotels/blrgs-sheraton-grand-bangalore-hotel-at-brigade-gateway/overview/ and https://www.hotelplanner.com/Hotels/178731/Reservations-Sheraton-Bangalore-Hotel-at-Brigade-Gateway-Bangalore-26-1-Dr-Rajkumar-Rd-Malleswaram-Rajajinagar-560055 (via WebSearch).
- India AI Impact Summit dates (16-20 Feb 2026, Bharat Mandapam) and World Summit AI Amsterdam: verifier notes 2 and 4.
- Speakers: worldaisummit/speakers/speakers.json.
