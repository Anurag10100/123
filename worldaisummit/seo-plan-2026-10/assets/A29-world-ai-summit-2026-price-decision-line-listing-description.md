# A29: World AI Summit 2026: price decision line, listing description (long and short), AllEvents field edits and /delegate/ price block

- **For recommendation:** Choose one current pass price and put it on every listing and on /delegate/ (AllEvents and HappeningNext are live but out of date)
- **Research lens:** events-aggregators
- **Format:** Plain text blocks to paste into AllEvents, Eventbrite, 10times, MeraEvents, Townscript and GlobalTradeFairs (GTF) listings. Also plain-text edit notes for the /delegate/ page and homepage, and an optional schema.org Event JSON-LD block for /delegate/. Replace every PLACEHOLDER_ marker before publishing.
- **Placeholders the business must fill:**
  - PLACEHOLDER_PREMIUM_PRICE – 20,000 (Option A, Standard extended to 13 Oct) or 30,000 (Option B, Late Access)
  - PLACEHOLDER_VIP_PRICE – 35,000 (Option A) or 60,000 (Option B)
  - PLACEHOLDER_PREMIUM_PRICE_DIGITS / PLACEHOLDER_VIP_PRICE_DIGITS – the same prices as plain digits for the JSON-LD (for example 30000 / 60000)
  - PLACEHOLDER_GST_WORDING – confirmed tax wording, for example '+ GST' or 'inclusive of GST' (not stated on the site or the listing today)
  - PLACEHOLDER_EDITION – edition number; add only after the organiser confirms (LinkedIn says 3rd, some pages say 2nd, /1st-edition/ is 2025)
  - PLACEHOLDER_ATTENDANCE_FIGURES – delegate, speaker and startup counts; include only if the organiser signs off, otherwise delete the line
  - PLACEHOLDER_REFUND_TERMS – cancellation and refund terms for the AllEvents Refund Policy field (business decision; none published)
  - PLATFORM – utm_source per platform (allevents, eventbrite, 10times, meraevents, townscript, globaltradefairs)

## How to ship

Order of work (by 3 Oct 2026):

1. Owner signs off on the section 0 line (Option A or B, plus the GST wording).

2. Web dev edits /delegate/ (and the homepage card under Option B) per section 5, and deletes the 2025 Early Bird row.
   Under Option B, change the AllEvents ticket price in the same hour.

3. Marketing applies section 4 on the AllEvents dashboard and pastes section 1 with utm_source=allevents.
   They also check whether AllEvents takes payment (4e), which matters more than the cosmetic edits.
   They then paste the same text into the Eventbrite and 10times pages that already exist, and into MeraEvents and Townscript if listings are created there. Change only utm_source.
   On GTF, fix the "Entry: Free" pages.

4. After 24–48h, check that HappeningNext shows the new text.

5. Track the result in GA4 by utm_source and utm_medium=event_listing.

Sources checked now:
- /delegate/ (Exa web_fetch, 1 Oct 2026) confirms:
  - the tier names "Premium Pass" and "VIP Pass"
  - Early Bird "valid till 25th July 2025"
  - Standard Rs 20,000 / Rs 35,000 "valid till 30th Sept 2026"
  - Late Access Rs 30,000 / Rs 60,000
  - the partnerships@ and secretariat@ contacts
  No GST wording appears.
- Homepage (Exa web_fetch, 1 Oct) confirms the theme, the dates, the venue, the seven track names, "Premium Pass Rs 20,000/delegate" and "Group booking · 3+ delegates → 10% off · registration@worldaisummit.com". It says "previous edition" with no number.
- Partner posts:
  - KDEM as 2026 Strategic Partner: LinkedIn, 7 Sep 2026.
  - Successive Digital and Kagen as Bronze Partners: LinkedIn, 10 Aug 2026.
  - WD as AI & Data Infrastructure Partner: LinkedIn, 18 Aug 2026.
  - HighTable as AI Impact Partner: HappeningNext copy.
- The exhibitors RWS, Exatron and indierouter.ai come from the brief and were not re-verified as text, because the homepage shows logos only. Confirm them before pasting.
- Venue address "26/1 Dr. Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru, Karnataka 560055" comes from the marriott.com rooms page and the Google hotels entity (Exa search, 1 Oct).
- The 9:00 AM – 6:00 PM IST timings come from the verified AllEvents listing.
- Speakers are taken verbatim (names and title_role) from /home/user/123/worldaisummit/speakers/speakers.json. All 10 have confirmed_2026: true and publish: true. No bios were written.

Caveats:
- Direct fetches of worldaisummit.com are blocked from this sandbox (proxy 403), so nobody checked whether the site already has Event JSON-LD. Check the page source first (section 6).
- Exa may serve a cached copy.
- The stale "Rs 15,000 / Rs 25,000" search-index summary cannot be fixed directly. It refreshes when the page is recrawled.
- The SERP check showed no Google events block for "world ai summit 2026 tickets". The value of this work is conversion and consistency, not event-panel placement.

No OpenSEO paid tools were used, and no repository files were edited.

## Content

=====================================================================
0. PRICE DECISION (sign this off first; every block below depends on it)
=====================================================================
Pick one line, fill in the GST wording, and send it to marketing and web dev.

OPTION A (extend Standard to 13 Oct):
From 1 Oct 2026 the delegate pass is Rs 20,000 (Premium Pass) / Rs 35,000 (VIP Pass) PLACEHOLDER_GST_WORDING, valid till 13 Oct 2026; group of 3+ delegates gets 10% off.
-> All live listings already show Rs 20,000. Only /delegate/ needs an edit (section 5A). Adding the VIP ticket type on AllEvents (section 4b) becomes optional.

OPTION B (Late Access now):
From 1 Oct 2026 the delegate pass is Rs 30,000 (Premium Pass) / Rs 60,000 (VIP Pass) PLACEHOLDER_GST_WORDING; group of 3+ delegates gets 10% off.
-> You must update the AllEvents ticket price, the homepage "Premium Pass Rs 20,000/delegate" card and /delegate/ in the same hour (section 5B). Otherwise the listing undersells the pass.

Below, PLACEHOLDER_PREMIUM_PRICE and PLACEHOLDER_VIP_PRICE stand for the figures in the chosen line: 20,000 and 35,000 under A, or 30,000 and 60,000 under B.
PLACEHOLDER_GST_WORDING stands for the confirmed tax wording, for example "+ GST" or "inclusive of GST". Neither the site nor the listing states it today.

=====================================================================
1. LISTING DESCRIPTION (long field; paste the same text everywhere and change only utm_source, see section 3)
=====================================================================
World AI Summit 2026 | 14–15 October 2026 | Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru
[Insert "PLACEHOLDER_EDITION" after "2026" only once the organiser confirms the edition number. LinkedIn says 3rd, some pages say 2nd, and the site's own /1st-edition/ archive is the 2025 event.]

Theme: AI for All: Accelerating India's Journey Towards Inclusive, Responsible and Future-Ready AI.

Organised by Elets Technomedia, with Karnataka Digital Economy Mission (KDEM) as Strategic Partner. Two days of keynotes, panels and an expo for enterprise, government, GCC and startup AI leaders.

Seven tracks: Frontier Models & Compute · Sovereign AI & Geopolitics · Enterprise AI in Production · Global Capability Centres (GCCs) · Robotics, Agents & Embodied AI · AI for Bharat · Capital, Founders & Exits.

PLACEHOLDER_ATTENDANCE_FIGURES [optional line. Use it only if the organiser signs off on figures such as "Expected: 1,000+ delegates, 100+ speakers, 50+ startups". Otherwise delete the line.]

Partners include Successive Digital and Kagen.ai (Bronze Partners), WD (AI & Data Infrastructure Partner) and HighTable (AI Impact Partner). Exhibitors include RWS, Exatron and indierouter.ai.

Speakers include:
- Sanjeev Gupta – CEO, Karnataka Digital Economy Mission
- Pankaj Kumar Pandey, IAS – Principal Secretary, e-Governance, Karnataka
- Shalini Kapoor – Chief Strategist, Data and AI, EkStep
- Ram Mohan Rao – Executive Director, SEBI
- Sandeep Varaganti – CEO, JioMart, Reliance Retail
- Tulshekar Gangireddy – ED and Head of Data Strategy, JPMorgan Chase
- Deepika Sandeep – Head, AI/ML CoE, HSBC
- Harsh Vardhan – Global Head, AI and Digital Innovation, Apollo Tyres
- Dipayan Chakraborty – Head, India Analytics Center, eBay
- Shashank Randev – Founder and General Partner, 247VC
[If the field is short, keep only the first six.]

Delegate passes: Premium Pass Rs PLACEHOLDER_PREMIUM_PRICE · VIP Pass Rs PLACEHOLDER_VIP_PRICE (PLACEHOLDER_GST_WORDING). Group of 3+ delegates: 10% off. Write to registration@worldaisummit.com.

Book your pass: https://www.worldaisummit.com/delegate/?utm_source=PLATFORM&utm_medium=event_listing&utm_campaign=world_ai_summit_2026&utm_content=delegate_registration
Sponsor or exhibit: partnerships@worldaisummit.com
Nominate for the World AI Awards: https://www.worldaisummit.com/awards/?utm_source=PLATFORM&utm_medium=event_listing&utm_campaign=world_ai_summit_2026&utm_content=awards
Speaking and collaboration: secretariat@worldaisummit.com

Timings: 9:00 AM – 6:00 PM IST, both days.
Venue: Sheraton Grand Bangalore Hotel at Brigade Gateway, 26/1 Dr. Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru, Karnataka 560055.

=====================================================================
2. SHORT VERSIONS
=====================================================================
160–300-character field (279 characters with "Rs 30,000 + GST". Recount if the GST wording is longer):
World AI Summit 2026 by Elets Technomedia, 14–15 Oct 2026, Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. Seven tracks across frontier, sovereign and enterprise AI, GCCs, robotics and AI for Bharat. Delegate passes from Rs PLACEHOLDER_PREMIUM_PRICE PLACEHOLDER_GST_WORDING: worldaisummit.com/delegate/

Fields capped near 160 characters (163 with "Rs 30,000"):
World AI Summit 2026 by Elets Technomedia. 14–15 Oct 2026, Sheraton Grand Bangalore, Bengaluru. Seven AI tracks. Passes from Rs PLACEHOLDER_PREMIUM_PRICE: worldaisummit.com/delegate/

=====================================================================
3. utm_source PER PLATFORM (replace PLATFORM in both links in section 1)
=====================================================================
AllEvents: allevents
Eventbrite: eventbrite
10times: 10times
MeraEvents: meraevents
Townscript: townscript
GlobalTradeFairs: globaltradefairs
HappeningNext: do not edit. It mirrors AllEvents and keeps utm_source=allevents. Check after 24–48h that it shows the new text. If it does not, use its claim/report path.
GlobalTradeFairs: its three duplicate pages say "Entry: Free". Change entry to paid (Rs PLACEHOLDER_PREMIUM_PRICE) and ask GTF to merge the duplicates into one page.

=====================================================================
4. ALLEVENTS FIELD-BY-FIELD (organiser dashboard: allevents.in > Sign in > Manage events)
Listing: https://allevents.in/bangalore/world-ai-summit-2026-tickets/80002987560857
=====================================================================
(a) Host / organiser name: change "World AI Summit 2026" to "Elets Technomedia – World AI Summit". This is set on the organiser profile, allevents.in/org/world-ai-summit-2026/28172130.
(b) Ticket types: replace "Delegates Passes INR 20,000" with
    - Premium Pass – INR PLACEHOLDER_PREMIUM_PRICE – Full summit access, delegate kit, lunch and refreshments, certificate of participation.
    - VIP Pass – INR PLACEHOLDER_VIP_PRICE – All Premium benefits, priority seating, speaker lounge access, exclusive networking dinner, special sessions on GenAI, Agentic AI and AI Safety.
    (Benefit text is taken from /delegate/.)
(c) Description: paste section 1 with utm_source=allevents. It already carries the group 10% line and the three CTAs.
(d) Refund Policy field: remove the partnerships email and paste:
    "Cancellation, substitution and refund requests: registration@worldaisummit.com. PLACEHOLDER_REFUND_TERMS"
(e) Before you save, check whether a booking on AllEvents takes payment. The listing says "Tickets on approval", and nobody has checked whether money changes hands.
    If it does, under Option B change the ticket price in the same sitting as /delegate/. If you cannot, switch ticketing to the external "Book your pass" link.
(f) The FAQ is auto-generated and may not be editable. It says "AllEvents is the official ticketing partner" and "download the app to unlock special pricing", which conflicts with the group-discount line.
    If the dashboard lets you, turn off the auto FAQ or the app-discount text. If not, ask AllEvents support to remove them.

=====================================================================
5. /delegate/ AND HOMEPAGE PRICE BLOCK (web dev)
=====================================================================
Both options: delete the row "Early Bird Offer Limited to the First 150 Passes (Valid till 25th July 2025) Rs 20,000 Save Rs 5,000 / Rs 35,000 Save Rs 5,000".

5A (Option A):
- "Standard Access (Valid till 30th Sept 2026)" becomes "Standard Access (Valid till 13th Oct 2026)". Prices stay Rs 20,000 / Rs 35,000.
- "Late Access" becomes "Late Access (from 14th Oct 2026)". Prices stay Rs 30,000 / Rs 60,000.
- Homepage Premium Pass card stays at Rs 20,000/delegate.

5B (Option B):
- Change "Standard Access (Valid till 30th Sept 2026)" to "Standard Access (Closed on 30th Sept 2026)", or delete the row.
- "Late Access" becomes "Late Access (Valid till 15th Oct 2026)": Rs 30,000 / Rs 60,000.
- Homepage Premium Pass card: "Rs 20,000/ delegate" becomes "Rs 30,000/ delegate".

Both: add PLACEHOLDER_GST_WORDING under the price row, and the line "Group booking · 3+ delegates · 10% off · registration@worldaisummit.com".

=====================================================================
6. OPTIONAL: price-consistent Event JSON-LD for /delegate/
=====================================================================
First view the source of / and /delegate/ and search for "@type": "Event". If markup already exists, update its offers and do not add a second block. Replace the two price placeholders with plain digits (for example 30000) before deploying.
Validate at https://validator.schema.org/ and in Google's Rich Results Test.
No verified image URL is held. Add an "image" array once you have one, because Google recommends it.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Event",
  "name": "World AI Summit 2026",
  "description": "AI for All: Accelerating India's Journey Towards Inclusive, Responsible and Future-Ready AI. Two days of keynotes, panels and an expo across seven tracks, organised by Elets Technomedia with Karnataka Digital Economy Mission (KDEM) as Strategic Partner.",
  "startDate": "2026-10-14T09:00:00+05:30",
  "endDate": "2026-10-15T18:00:00+05:30",
  "eventStatus": "https://schema.org/EventScheduled",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
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
    "url": "https://www.eletsonline.com/"
  },
  "offers": [
    {
      "@type": "Offer",
      "name": "Premium Pass",
      "price": "PLACEHOLDER_PREMIUM_PRICE_DIGITS",
      "priceCurrency": "INR",
      "availability": "https://schema.org/InStock",
      "validFrom": "2026-10-01T00:00:00+05:30",
      "url": "https://www.worldaisummit.com/delegate/"
    },
    {
      "@type": "Offer",
      "name": "VIP Pass",
      "price": "PLACEHOLDER_VIP_PRICE_DIGITS",
      "priceCurrency": "INR",
      "availability": "https://schema.org/InStock",
      "validFrom": "2026-10-01T00:00:00+05:30",
      "url": "https://www.worldaisummit.com/delegate/"
    }
  ],
  "performer": [
    { "@type": "Person", "name": "Sanjeev Gupta" },
    { "@type": "Person", "name": "Pankaj Kumar Pandey" },
    { "@type": "Person", "name": "Shalini Kapoor" },
    { "@type": "Person", "name": "Ram Mohan Rao" },
    { "@type": "Person", "name": "Sandeep Varaganti" },
    { "@type": "Person", "name": "Tulshekar Gangireddy" },
    { "@type": "Person", "name": "Deepika Sandeep" },
    { "@type": "Person", "name": "Harsh Vardhan" },
    { "@type": "Person", "name": "Dipayan Chakraborty" },
    { "@type": "Person", "name": "Shashank Randev" }
  ]
}
</script>

Redirects: none needed for this change.
