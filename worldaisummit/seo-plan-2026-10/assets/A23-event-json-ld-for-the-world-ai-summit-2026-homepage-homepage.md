# A23: Event JSON-LD for the World AI Summit 2026 homepage (homepage only)

- **For recommendation:** Add Event JSON-LD to the homepage, /delegate/ and the Bengaluru landing page so the summit can appear in Google's Events carousel and event rich results
- **Research lens:** serp-features
- **Format:** schema.org JSON-LD in an HTML script tag, followed by fill-in notes. Validated as JSON with Python json.load. The placeholders are strings, so the block parses as written.
- **Placeholders the business must fill:**
  - PLACEHOLDER_PREMIUM_PASS_PRICE_INR (marketing: "30000" if Late Access applies, "20000" if Standard is kept; must match the homepage, /delegate/ and AllEvents)
  - PLACEHOLDER_VIP_PASS_PRICE_INR (marketing: "60000" if Late Access applies, "35000" if Standard is kept)
  - PLACEHOLDER_PRICE_PHASE_START (start of the current price phase, e.g. "2026-10-01T00:00:00+05:30" for Late Access)
  - PLACEHOLDER_EVENT_IMAGE_URL (absolute URL of an image already on worldaisummit.com, at least 720px wide and ideally 1920px; otherwise delete the image line)
  - PLACEHOLDER_CONFIRMED_SPEAKER_NAME (optional performer field; only speakers marketing has confirmed for 2026)

## How to ship

Owner: web dev, once marketing has decided the price (about 30 minutes). Target date: 3 Oct 2026.

1. Get the price decision from marketing. Then update the homepage price text, /delegate/ and the AllEvents listing so all three show the same live price. Put the same numbers into the placeholders (see fill-in note 1). Also fill in or remove the image line, and decide date-only or timed values (notes 2 and 3).

2. Paste the script block into the <head> of https://www.worldaisummit.com/ only. Do not add it to /delegate/ or /ai-conference-bengaluru-2026.html. Google's Event guideline says each event needs one leaf URL that carries the markup, and the feature supports only pages that focus on a single event. The homepage already holds all the event rankings. Duplicating the block on other pages adds risk and little value. If /index.html serves the same file, that is fine, because it canonicalises to /.

3. Before publishing, check the homepage source for any existing Event JSON-LD. This was not checked: Exa returns only text, and the proxy blocked a direct fetch from here. If an Event block is already there, replace it so the page has exactly one Event node.

4. Validate the page with the Rich Results Test (search.google.com/test/rich-results) and the Schema Markup Validator (validator.schema.org). Both must show 0 errors. Any warning that says PLACEHOLDER means a placeholder was left unfilled.

5. Add and verify the property https://www.worldaisummit.com/ in Search Console. Only the non-www property is connected today. Then run URL Inspection on the homepage and click Request Indexing. Google recrawls the homepage often: the non-www homepage was last crawled at 2026-10-01T09:45Z, with the www URL as Google's chosen canonical. Google should therefore see the markup within days. How long it takes to appear in the Events carousel is a separate delay, and nobody knows how long.

6. Keep expectations modest. The event is probably already in Google's event search through AllEvents, which calls itself the official ticketing partner and links to /delegate/. That is an inference; I could not see the carousel. Markup on the site mainly adds the official site as an extra source and ticket link.

7. Consistency follow-up, with no edit made here: before /speakers/ is deployed, update "pass_price_inr" and "pass_from" in /home/user/123/worldaisummit/speakers/speakers.json to the same live price. event_ld() in build_speakers.py otherwise prints 20000 on every speaker page.

Not verified by me: the carousel's presence on 3 of 22 SERPs and the WAIS positions on those queries (from the lens run; not re-run, 0 credits used). Search volumes for those queries are unknown.

## Content

<!-- World AI Summit 2026: Event structured data. Place inside <head> of https://www.worldaisummit.com/ only. -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Event",
  "@id": "https://www.worldaisummit.com/#event-2026",
  "name": "World AI Summit 2026",
  "description": "Two-day AI conference in Bengaluru for policymakers, enterprise CXOs, GCC leaders, founders and investors. Seven tracks: Frontier Models & Compute; Sovereign AI & Geopolitics; Enterprise AI in Production; Global Capability Centres; Robotics, Agents & Embodied AI; AI for Bharat; Capital, Founders & Exits. Includes the World AI Awards.",
  "startDate": "2026-10-14",
  "endDate": "2026-10-15",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
  "eventStatus": "https://schema.org/EventScheduled",
  "url": "https://www.worldaisummit.com/",
  "image": ["PLACEHOLDER_EVENT_IMAGE_URL"],
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
    }
  },
  "organizer": {
    "@type": "Organization",
    "name": "Elets Technomedia",
    "url": "https://www.eletsonline.com/",
    "email": "registration@worldaisummit.com"
  },
  "offers": [
    {
      "@type": "Offer",
      "name": "Premium Pass",
      "url": "https://www.worldaisummit.com/delegate/",
      "price": "PLACEHOLDER_PREMIUM_PASS_PRICE_INR",
      "priceCurrency": "INR",
      "availability": "https://schema.org/InStock",
      "validFrom": "PLACEHOLDER_PRICE_PHASE_START"
    },
    {
      "@type": "Offer",
      "name": "VIP Pass",
      "url": "https://www.worldaisummit.com/delegate/",
      "price": "PLACEHOLDER_VIP_PASS_PRICE_INR",
      "priceCurrency": "INR",
      "availability": "https://schema.org/InStock",
      "validFrom": "PLACEHOLDER_PRICE_PHASE_START"
    }
  ]
}
</script>

FILL-IN NOTES (do not paste these lines into the page)

1. Prices. Marketing decides these. Do not ship until the decision is made.
   - Late Access, the phase /delegate/ shows from 1 Oct 2026: PLACEHOLDER_PREMIUM_PASS_PRICE_INR = "30000", PLACEHOLDER_VIP_PASS_PRICE_INR = "60000", PLACEHOLDER_PRICE_PHASE_START = "2026-10-01T00:00:00+05:30".
   - If marketing instead keeps Standard Access: use "20000" and "35000". In that case /delegate/ must stop showing "Valid till 30th Sept 2026" and must stop showing Late Access as the current price.
   - Whichever prices you choose, the homepage line "Rs 20,000/delegate" under "Three release phases" and the AllEvents listing ("Delegates Passes INR 20,000") must show the same prices before this markup goes live. The markup has to describe what the page shows.
   - Write prices as plain digits in quotes, with no "Rs", no commas and no GST text.

2. Image. Google recommends an image but does not require one. Replace PLACEHOLDER_EVENT_IMAGE_URL with the absolute URL of an event image that is already on worldaisummit.com. It must be at least 720px wide, and 1920px is recommended. If you have 16x9, 4x3 and 1x1 versions, list all three in the array. If you have no suitable image, delete the whole "image" line. Do not ship the placeholder text.

3. Times. The dates above are date-only on purpose. The only sources for 09:00-18:00 IST are the AllEvents and happeningnext listings, which the organiser supplied. These times do not appear on worldaisummit.com. If the times are confirmed internally, you can change the two date lines to:
   "startDate": "2026-10-14T09:00:00+05:30",
   "endDate": "2026-10-15T18:00:00+05:30",

4. Venue address. "26/1, Dr Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru 560055" matches the hotel's own listings (Marriott, hotelplanner). No change is needed.

5. Availability. "InStock" is correct while passes are on sale. If a pass sells out, change that offer to "https://schema.org/SoldOut". If the event is postponed or cancelled, change eventStatus to EventPostponed or EventCancelled. Do not delete the block.

6. Performers. There is deliberately no performer field. Add one only for speakers marketing has confirmed for 2026, in this format: "performer": [{"@type": "Person", "name": "PLACEHOLDER_CONFIRMED_SPEAKER_NAME"}]
