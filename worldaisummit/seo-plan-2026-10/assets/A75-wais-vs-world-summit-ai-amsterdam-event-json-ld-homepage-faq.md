# A75: WAIS vs World Summit AI (Amsterdam): Event JSON-LD, homepage FAQ copy and one-line identity

- **For recommendation:** Separate WAIS from World Summit AI (Amsterdam) for Google and AI answer engines before Amsterdam's 7-8 Oct news peak
- **Research lens:** missing-levers
- **Format:** HTML snippets (JSON-LD script blocks) + plain-text FAQ copy + one-line identity text
- **Placeholders the business must fill:**
  - PLACEHOLDER_CURRENT_PASS_PRICE_INR (digits only; homepage says Rs 20,000 Premium, /delegate/ says Standard Rs 20,000 expired 30 Sept and Late Access is Rs 30,000/60,000)
  - PLACEHOLDER_CURRENT_PASS_NAME (e.g. Late Access Delegate Pass)
  - PLACEHOLDER_CURRENT_PHASE_START_DATE (ISO date, or delete the validFrom line)
  - PLACEHOLDER_EVENT_IMAGE_URL (absolute URL of the 2026 banner, at least 1200px wide)
  - Business sign-off: Elets confirms there is no affiliation with World Summit AI (Amsterdam) before 'separate event' / 'not connected with' goes live
  - Optional performer array: only speakers confirmed in speakers.json and already shown on the live site

## How to ship

Owner: web dev. Deadline: 5 Oct 2026, before Amsterdam's 7-8 Oct news peak. About 45 minutes.

1) Sign-off first (Elets). Before publishing, confirm in writing that Elets has no affiliation with World Summit AI (Amsterdam). The phrases "separate event" and "not connected with" depend on it. Then fill the four PLACEHOLDER_ values in Block A. The price must match what the homepage and /delegate/ show from today.

2) Check the homepage source. Open the live homepage source and search for "application/ld+json". I could not check this: the sandbox proxy blocks worldaisummit.com, and Exa returns only page text.
   - If an Event block already exists, replace it with Block A. There should be one Event block per event.
   - If an Organization block exists, leave it, but do not add the Organization block from the original recommendation. Google's Organization documentation does not use disambiguatingDescription or parentOrganization. Event markup with organizer = Elets Technomedia and a location is the correct type, and it is eligible for Google's event features.
   - Paste Block A just before </head> on / only. /index.html already canonicalises to /, so either update the shared template or edit both files.

3) Edit the FAQ accordion. Replace the first answer with B1, and insert B2 as the second item using the same markup. The visible text must match any JSON-LD word for word. Block C is optional.

4) Test. Run https://search.google.com/test/rich-results and https://validator.schema.org/ on the live URL. Expect 0 errors. A warning about missing "performer" is acceptable. Then use URL Inspection and Request Indexing for https://www.worldaisummit.com/. Search Console only covers the non-www property today, so add the www property (or a Domain property) first. Without it, CTR and any leak to Amsterdam cannot be measured.

5) Same day, outside the website: paste the Block D short and long lines into the LinkedIn showcase About, the YouTube channel and video descriptions, and the listings on allevents.in, 10times, Eventbrite and globaltradefairs (which currently says "Entry: Free"). Fix events.eletsonline.com/aidemo/registration.html, whose Google snippet still says "September 2026".

6) Before publishing, open each organizer sameAs URL once. Remove any that does not load as the official Elets profile; the JSON stays valid as long as the commas are fixed.

7) Re-check after 5 Oct by searching 'world ai summit October 2026 dates venue' and 'world ai summit' (Google India). Expected impact: small and indirect. This does not move rankings. It improves how Google and AI answer engines describe WAIS during 5-15 Oct.

Both JSON blocks were parsed with python json.load: valid.

## Content

=====================================================================
BLOCK A. Event JSON-LD for the homepage <head> (https://www.worldaisummit.com/)
This replaces the Organization block in the original recommendation (see the note at the end).
=====================================================================

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Event",
  "@id": "https://www.worldaisummit.com/#event-2026",
  "name": "World AI Summit 2026",
  "alternateName": ["World AI Summit India 2026", "World AI Summit Bengaluru 2026"],
  "description": "World AI Summit 2026 is an artificial intelligence conference in Bengaluru, India, organised by Elets Technomedia. The 2nd edition takes place on 14-15 October 2026 at the Sheraton Grand Bangalore Hotel at Brigade Gateway. It is a separate event from World Summit AI in Amsterdam.",
  "url": "https://www.worldaisummit.com/",
  "startDate": "2026-10-14",
  "endDate": "2026-10-15",
  "eventStatus": "https://schema.org/EventScheduled",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
  "inLanguage": "en-IN",
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
    "sameAs": [
      "https://www.linkedin.com/company/elets-technomedia/",
      "https://www.instagram.com/eletsonline/",
      "https://www.youtube.com/user/eletsvideos/",
      "https://x.com/eletsonline",
      "https://www.facebook.com/eletsTechnomedia/"
    ]
  },
  "offers": {
    "@type": "Offer",
    "name": "PLACEHOLDER_CURRENT_PASS_NAME",
    "url": "https://www.worldaisummit.com/delegate/",
    "price": "PLACEHOLDER_CURRENT_PASS_PRICE_INR",
    "priceCurrency": "INR",
    "availability": "https://schema.org/InStock",
    "validFrom": "PLACEHOLDER_CURRENT_PHASE_START_DATE"
  },
  "superEvent": {
    "@type": "EventSeries",
    "name": "World AI Summit",
    "url": "https://www.worldaisummit.com/",
    "sameAs": ["https://www.linkedin.com/showcase/world-ai-summit/"]
  }
}
</script>

Placeholder rules:
- PLACEHOLDER_CURRENT_PASS_PRICE_INR: digits only, no comma and no Rs sign (for example 30000). The homepage shows "Premium Pass Rs 20,000", but /delegate/ says Standard Rs 20,000 was valid until 30 Sept 2026 and Late Access is Rs 30,000/60,000. Use the price a buyer actually pays from today, and make the homepage show the same figure.
- PLACEHOLDER_CURRENT_PASS_NAME: for example "Late Access Delegate Pass".
- PLACEHOLDER_CURRENT_PHASE_START_DATE: ISO date (for example 2026-10-01). If you do not want to state it, delete the whole "validFrom" line, including the comma on the line before it.
- PLACEHOLDER_EVENT_IMAGE_URL: an absolute URL to the 2026 banner on worldaisummit.com, at least 1200px wide (16:9, 4:3 or 1:1).
- If passes sell out, change "availability" to "https://schema.org/SoldOut". If the date or venue changes, update "eventStatus" (EventRescheduled or EventCancelled) on the same day.
- performer: left out on purpose. Add a "performer" array of {"@type":"Person","name":"...","jobTitle":"...","worksFor":{"@type":"Organization","name":"..."}} only for speakers who are confirmed in worldaisummit/speakers/speakers.json AND already shown on the live site. Do not add anyone else, and do not add bios.

=====================================================================
BLOCK B. Visible homepage FAQ copy (paste into the existing FAQ accordion, using the same markup as the current items)
=====================================================================

B1. REPLACE the answer to the existing first question.

Q: What is the World AI Summit?
A: World AI Summit is an artificial intelligence conference in Bengaluru, India, organised by Elets Technomedia. The 2026 edition takes place on 14-15 October 2026 at the Sheraton Grand Bangalore Hotel at Brigade Gateway. It brings together policymakers, business leaders, technology experts, researchers, startups and investors across seven tracks, from frontier models and sovereign AI to enterprise AI, GCCs and AI for Bharat. The focus is responsible, inclusive and impactful AI adoption.

B2. ADD as the second FAQ item, directly below B1.

Q: Is World AI Summit the same as World Summit AI in Amsterdam?
A: No. World AI Summit is organised by Elets Technomedia and takes place on 14-15 October 2026 at the Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru, India. World Summit AI is a separate event held in Amsterdam.

=====================================================================
BLOCK C (optional). FAQPage JSON-LD that mirrors B1 and B2 word for word
Google no longer shows FAQ rich results for event sites, so this only gives AI crawlers a clean copy. Skip it if you would rather not keep two copies in sync.
=====================================================================

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the World AI Summit?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "World AI Summit is an artificial intelligence conference in Bengaluru, India, organised by Elets Technomedia. The 2026 edition takes place on 14-15 October 2026 at the Sheraton Grand Bangalore Hotel at Brigade Gateway. It brings together policymakers, business leaders, technology experts, researchers, startups and investors across seven tracks, from frontier models and sovereign AI to enterprise AI, GCCs and AI for Bharat. The focus is responsible, inclusive and impactful AI adoption."
      }
    },
    {
      "@type": "Question",
      "name": "Is World AI Summit the same as World Summit AI in Amsterdam?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. World AI Summit is organised by Elets Technomedia and takes place on 14-15 October 2026 at the Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru, India. World Summit AI is a separate event held in Amsterdam."
      }
    }
  ]
}
</script>

=====================================================================
BLOCK D. One-line identity. Use these exact words everywhere the event is described.
=====================================================================

Short (LinkedIn tagline, listing headline, YouTube first line):
World AI Summit 2026, Bengaluru: 14-15 October 2026, Sheraton Grand Bangalore Hotel at Brigade Gateway. Organised by Elets Technomedia.

Long (LinkedIn About opening, YouTube description, allevents / 10times / Eventbrite / globaltradefairs blurbs):
World AI Summit 2026 is the 2nd edition of the artificial intelligence conference organised by Elets Technomedia in Bengaluru, India, on 14-15 October 2026 at the Sheraton Grand Bangalore Hotel at Brigade Gateway. It is not connected with World Summit AI in Amsterdam. Delegate passes: https://www.worldaisummit.com/delegate/

Sources checked on 1 Oct 2026:
- Venue address: 26/1 Dr Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru 560055 (marriott.com/en-us/hotels/blrgs-sheraton-grand-bangalore-hotel-at-brigade-gateway/overview/ and hotelplanner.com via WebSearch).
- Dates, venue, organiser, seven tracks and the existing FAQ wording: Exa fetch of https://www.worldaisummit.com/.
- Organiser profiles: instagram.com/eletsonline is the "Elets Technomedia" profile (Exa). youtube.com/user/eletsvideos, twitter.com/eletsonline and facebook.com/eletsTechnomedia are linked by Elets itself on insights.eletsonline.com/2021/09/model-gaon/. The LinkedIn company page is confirmed by the verifier.
- "2nd edition": LinkedIn showcase About ("2nd Edition of World AI Summit, 14-15 October 2026"), as confirmed by the verifier.
