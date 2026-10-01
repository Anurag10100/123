# A19: World AI Summit 2026: listing copy, Techcanvass and MeraEvents requests, Eventbrite fields and Event JSON-LD (revised after verification)

- **For recommendation:** Discovery cluster (about 6,400 searches/mo) is owned by aggregator list pages: get World AI Summit onto the exact URLs that rank
- **Research lens:** demand-sweep
- **Format:** Markdown pack: plain-text emails, listing copy in three lengths, form field values, UTM table and a schema.org Event JSON-LD block
- **Placeholders the business must fill:**
  - PLACEHOLDER_CURRENT_PASS_PRICE: Standard tier ended 30 Sept 2026; /delegate/ shows Late Access Rs 30,000 / Rs 60,000, but the homepage still shows Premium Rs 20,000
  - PLACEHOLDER_DAILY_START_TIME: the summit's start time each day (IST)
  - PLACEHOLDER_DAILY_END_TIME: the summit's end time each day (IST)
  - PLACEHOLDER_SENDER_NAME: who sends the Techcanvass and MeraEvents emails
  - PLACEHOLDER_SENDER_TITLE: the sender's job title at Elets Technomedia
  - PLACEHOLDER_RECIPROCAL_OFFER: optional; whether to offer Techcanvass anything in return (for example a reader discount); delete the line if not approved
  - PLACEHOLDER_MERAEVENTS_CHOICE: choose (a) a new 2026 page with a redirect or (b) an 'edition ended' note with a link
  - PLACEHOLDER_EVENTBRITE_ACCOUNT_OWNER: the person who controls the existing Eventbrite event
  - PLACEHOLDER_EVENT_IMAGE_URL: absolute URL of an event image on worldaisummit.com for the JSON-LD

## How to ship

The marketing or partnerships team should do these steps by 6 Oct 2026, so each listing has about a week before the event. The earlier claim that 'this week' searches peak on 12-15 Oct is unverified and was dropped.

1. Decide the current pass price. Standard Access ended on 30 Sept 2026. /delegate/ shows Late Access at Rs 30,000 / Rs 60,000, but the homepage still says Premium Rs 20,000. Update /delegate/ so it does not show expired tiers, because every listing links there.
2. Send the MeraEvents request (section 3) from the account that owns Event ID 266617.
3. Send the Techcanvass email (section 2) through the page's "let us know" or contact route. It is framed as an addition to an October page that is already published, not as a new submission.
4. Ask the web team to check view-source on / and /delegate/ for any existing Event JSON-LD. If there is none, paste section 5 after replacing the placeholders, then validate it in Google's Rich Results Test. I could not check the live markup: direct fetches were blocked by the network proxy, and Exa strips scripts.
5. If someone can find who owns the Eventbrite account, apply section 4. Then submit section 1 to dev.events.
6. Skip conferencealerts.in, b2bangalore and the Luma city page, for the reasons in section 0.
7. Track the results in analytics: utm_medium=listing, utm_campaign=wais2026.

Sources checked on 1 Oct 2026: the venue address came from Marriott (https://www.marriott.com/en-us/hotels/blrgs-sheraton-grand-bangalore-hotel-at-brigade-gateway/overview/) and HotelPlanner, which both give 26/1 Dr. Rajkumar Road, Malleswaram-Rajajinagar, 560055. The /delegate/ pricing text came from an Exa fetch. No OpenSEO paid tools were used. Expected impact is still small: tens of referral visits and a handful of pass leads.

On your CPU question: this session's machine reports 4 CPUs (nproc), and I cannot add more from inside the session.

## Content

## 0. Revised priority (based on verifier findings, 1 Oct 2026)

Do now, in this order:
1. MeraEvents fix. Confirmed: meraevents.com/event/worldaisummit (Event ID 266617) still shows 25-26 Sep 2025 and "Sold Out". Request in section 3.
2. Techcanvass request. The October'26 list is already published with 10 entries, so this asks an editor to change a finished page. The email in section 2 is written that way and aimed at their audience of business analysts and product managers.
3. Event JSON-LD on / and /delegate/. Google's Events block appears on the 'tech events in bangalore' results page, and that block is fed by Event structured data (inferred). This is the cheapest step the site controls. Before pasting, use view-source to check that no Event schema already exists. Section 5.
4. Eventbrite field fix, only if the account owner can be found. This makes the event eligible for category pages but does not make it visible. Section 4.
5. dev.events (#10 for 'tech events in bangalore'): submit using the listing copy in section 1.

Skip (do not spend time):
- conferencealerts.in/bangalore/ai: lists academic paper-presentation conferences for researchers and students. Poor fit for paid CXO passes.
- b2bangalore: states that every listing links to a free registration page. A paid event may not qualify.
- Luma city page (luma.com/bengaluru): a feed of community meetups ranked by RSVPs. A paid conference is unlikely to appear there (inferred), and there is no confirmed way to submit to it.
- conferencealerts.co.in, allconferencealert.com, internationalconferencealerts.com: not checked. They are probably the same academic format as conferencealerts.in (inferred). Only do these if the form is free and takes under 5 minutes.

Before sending any traffic: on 1 Oct 2026, /delegate/ still shows "Early Bird ... Valid till 25th July 2025" and "Standard Access (Valid till 30th Sept 2026)", so both shown tiers have expired. Confirm the current price (PLACEHOLDER_CURRENT_PASS_PRICE) and update that page first.

---

## 1. Listing copy (for dev.events, Eventbrite and any other aggregator form)

### One-liner (about 185 characters)
World AI Summit 2026, 14-15 October, Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. Two-day AI conference with the World AI Awards, organised by Elets Technomedia.

### Summary (about 135 characters, fits Eventbrite's summary field)
Two-day AI conference in Bengaluru with seven tracks and the World AI Awards, for CXOs, GCC heads, policymakers, founders and investors.

### Full description
World AI Summit 2026 | 14-15 October 2026 | Sheraton Grand Bangalore Hotel at Brigade Gateway, 26/1 Dr. Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru 560055 | Organiser: Elets Technomedia

A two-day AI conference with the World AI Awards. Seven tracks:
- Frontier Models & Compute
- Sovereign AI & Geopolitics
- Enterprise AI in Production
- GCCs
- Robotics, Agents & Embodied AI
- AI for Bharat
- Capital, Founders & Exits

For CXOs, GCC heads, policymakers, founders and investors.

Passes: paid delegate passes from PLACEHOLDER_CURRENT_PASS_PRICE. Groups of 3 or more get 10% off.
Register: https://www.worldaisummit.com/delegate/?utm_source=<site>&utm_medium=listing&utm_campaign=wais2026
Contact: registration@worldaisummit.com
Partnerships and exhibition: partnerships@worldaisummit.com

### Form field values
- Event name: World AI Summit 2026
- Start: 14 October 2026, PLACEHOLDER_DAILY_START_TIME IST
- End: 15 October 2026, PLACEHOLDER_DAILY_END_TIME IST
- Time zone: Asia/Kolkata (IST, UTC+5:30)
- Format: In person, conference
- Venue: Sheraton Grand Bangalore Hotel at Brigade Gateway
- Address: 26/1 Dr. Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru, Karnataka 560055, India
- Organiser: Elets Technomedia
- Price: Paid (PLACEHOLDER_CURRENT_PASS_PRICE)
- Topics and tags: Artificial Intelligence, Enterprise AI, GCC, AI Agents, Robotics, Bengaluru
- Contact email: registration@worldaisummit.com

### UTM link per site (replace <site>)
- dev.events: https://www.worldaisummit.com/delegate/?utm_source=devevents&utm_medium=listing&utm_campaign=wais2026
- Techcanvass: https://www.worldaisummit.com/delegate/?utm_source=techcanvass&utm_medium=listing&utm_campaign=wais2026
- Eventbrite: https://www.worldaisummit.com/delegate/?utm_source=eventbrite&utm_medium=listing&utm_campaign=wais2026
- MeraEvents: https://www.worldaisummit.com/delegate/?utm_source=meraevents&utm_medium=listing&utm_campaign=wais2026

---

## 2. Techcanvass email (send through the page's "let us know" / contact route)

Subject: Possible addition to your October'26 Bangalore list: World AI Summit, 14-15 Oct

Hi Techcanvass team,

I saw that "Top 10 Upcoming Tech Conference In Bangalore October'26" is now live. If you are open to adding an entry or updating the page, World AI Summit 2026 may be useful to business analysts and product managers who work on AI projects.

- What: World AI Summit 2026, organised by Elets Technomedia, with the World AI Awards
- When: 14-15 October 2026
- Where: Sheraton Grand Bangalore Hotel at Brigade Gateway, Dr. Rajkumar Road, Bengaluru
- Tracks most relevant to your readers: Enterprise AI in Production; GCCs; Robotics, Agents & Embodied AI
- Passes: paid delegate passes, with 10% off for groups of 3 or more
- Details and registration: https://www.worldaisummit.com/delegate/?utm_source=techcanvass&utm_medium=listing&utm_campaign=wais2026

I can send a logo, a 50-word description or an entry written in your list's format. If the October page is already final, we would be glad to be considered for a later list on AI or GCC events.

[Optional, include only if approved: PLACEHOLDER_RECIPROCAL_OFFER]

Thank you for considering it.

Regards,
PLACEHOLDER_SENDER_NAME
PLACEHOLDER_SENDER_TITLE, Elets Technomedia
registration@worldaisummit.com

---

## 3. MeraEvents update request (send from the account that owns Event ID 266617, or through MeraEvents support)

Subject: Update request for World AI Summit page (Event ID 266617)

Hello MeraEvents team,

The page https://www.meraevents.com/event/worldaisummit (Event ID 266617) still shows World AI Summit on Thursday 25 September to Friday 26 September 2025, marked "Sale Date Ended / Sold Out". People searching for the 2026 edition are landing on it.

World AI Summit 2026 takes place on 14-15 October 2026 at the Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. Could you please PLACEHOLDER_MERAEVENTS_CHOICE:
(a) set up a 2026 event page and redirect this URL to it, or
(b) add a clear note to this page that the 2025 edition has ended, with a link to https://www.worldaisummit.com/delegate/?utm_source=meraevents&utm_medium=listing&utm_campaign=wais2026

Thank you.

Regards,
PLACEHOLDER_SENDER_NAME
Elets Technomedia | registration@worldaisummit.com

---

## 4. Eventbrite fields (for PLACEHOLDER_EVENTBRITE_ACCOUNT_OWNER, whoever controls the existing event)

- Title: World AI Summit 2026, Bengaluru
- Date and time: 14 Oct 2026, PLACEHOLDER_DAILY_START_TIME to 15 Oct 2026, PLACEHOLDER_DAILY_END_TIME, time zone IST (Asia/Kolkata)
- Location: Venue, Sheraton Grand Bangalore Hotel at Brigade Gateway, 26/1 Dr. Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru 560055
- Type: Conference
- Category: Science & Technology
- Tags: artificial intelligence, AI, Bengaluru, GCC, enterprise AI
- Summary: use the summary from section 1
- Description: use the full description from section 1
- Registration: link out to the Eventbrite UTM link in section 1, or use Eventbrite ticketing at PLACEHOLDER_CURRENT_PASS_PRICE (business decision)
Note: this makes the event eligible for the Bangalore conference and tech category pages. Those pages sort by Eventbrite's relevance and RSVP signals, so the event will not necessarily appear.

---

## 5. Event JSON-LD (paste into <head> on https://www.worldaisummit.com/ and /delegate/)

Check first: view-source the page and search for "application/ld+json" and "Event". If an Event block already exists, correct that one instead of adding a second. Replace every PLACEHOLDER value before publishing. "price" must be a number such as "30000". The image must be an absolute URL on worldaisummit.com, ideally 1200 px wide or more. Then run it through Google's Rich Results Test.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Event",
  "name": "World AI Summit 2026",
  "description": "Two-day AI conference in Bengaluru with the World AI Awards. Seven tracks: Frontier Models & Compute; Sovereign AI & Geopolitics; Enterprise AI in Production; GCCs; Robotics, Agents & Embodied AI; AI for Bharat; Capital, Founders & Exits.",
  "startDate": "2026-10-14",
  "endDate": "2026-10-15",
  "eventStatus": "https://schema.org/EventScheduled",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
  "url": "https://www.worldaisummit.com/",
  "image": [
    "PLACEHOLDER_EVENT_IMAGE_URL"
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
    "price": "PLACEHOLDER_CURRENT_PASS_PRICE",
    "priceCurrency": "INR",
    "availability": "https://schema.org/InStock"
  }
}
</script>

The "performer" property is left out on purpose. Add it only for speakers confirmed for 2026 (the status field in worldaisummit/speakers/speakers.json), one {"@type": "Person", "name": "..."} per speaker. Never add unconfirmed names. If passes sell out, change availability to https://schema.org/SoldOut.
