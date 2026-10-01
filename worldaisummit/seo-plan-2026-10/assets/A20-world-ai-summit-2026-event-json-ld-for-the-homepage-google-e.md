# A20: World AI Summit 2026: Event JSON-LD for the homepage (Google event results)

- **For recommendation:** Get into the Google Events carousel on 5 Bangalore discovery SERPs with one Event JSON-LD on the homepage and /delegate/
- **Research lens:** demand-sweep
- **Format:** HTML snippet: one schema.org Event JSON-LD script block. Paste it inside <head> of https://www.worldaisummit.com/ only.
- **Placeholders the business must fill:**
  - PLACEHOLDER_CURRENT_LOWEST_DELEGATE_PASS_PRICE_INR: the current lowest delegate pass price. The registration or commercial team must settle the conflict between Rs 20,000 (homepage, AllEvents) and Late Access Rs 30,000 (/delegate/, from 1 Oct) and make the pages match before publishing.

## How to ship

Owner: web dev, with a price decision from the registration or commercial team first. Deadline: 4 Oct 2026. Effort: under 1 hour once the price is settled.

WHAT CHANGED FROM THE ORIGINAL RECOMMENDATION, AND WHY
- Dates are date only ("2026-10-14" / "2026-10-15"). The 09:00 to 18:00 IST times appear only on AllEvents (the listing with Elets UTMs). The official homepage shows only "14th - 15th October 2026", and Google says to leave the time out when the page does not show it. If the web team adds a visible line such as "9:00 am to 6:00 pm IST, both days" to the homepage, switch to "2026-10-14T09:00:00+05:30" and "2026-10-15T18:00:00+05:30".
- The address is filled in. It comes from the Marriott property page (marriott.com/en-us/hotels/blrgs-sheraton-grand-bangalore-hotel-at-brigade-gateway/rooms/: "26/1 Dr. Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru, Karnataka, India, 560055"). Google Hotels and Apple Maps match it. Checked through Exa on 1 Oct 2026.
- "World AI Awards" is out of the description. The live homepage (Exa fetch, 1 Oct) labels the awards "Previous edition", and the markup must match what the page shows. Put it back only if the homepage confirms 2026 awards at this event.
- Ship on the homepage only, not on /delegate/. Google needs one leaf URL per event, and the homepage carries every event ranking. /delegate/ has no H1 and no internal links, so markup there adds little. Keep the same @id if /delegate/ is added after it gets an H1 and a homepage link.
- No performer. The homepage text from Exa shows no 2026 speaker names ("Meet The Visionaries" renders no names). Add performer only for names visibly shown on the homepage. Candidates with confirmed_2026: true in /home/user/123/worldaisummit/speakers/speakers.json are Pankaj Kumar Pandey, T Bhoobalan, Sanjeev Gupta, Ram Mohan Rao and Shalini Kapoor. The format is "performer":[{"@type":"Person","name":"..."}]. Do not add bios.

STEPS
1. Price decision (registration or commercial team; the web team cannot settle this). /delegate/ shows Standard Rs 20,000 / 35,000 "valid till 30th Sept 2026", then Late Access Rs 30,000 / 60,000, which by its own terms applies from 1 Oct. The homepage still shows "Premium Pass Rs 20,000/delegate" and AllEvents shows INR 20,000. Choose one current lowest delegate price and make the homepage, /delegate/ and AllEvents show it. Also remove the stale "Early Bird ... Valid till 25th July 2025" row on /delegate/.
2. Replace PLACEHOLDER_CURRENT_LOWEST_DELEGATE_PASS_PRICE_INR with that number and no symbols or commas, for example "30000". Do not publish while the placeholder is still in place. A non-numeric price fails validation.
3. Check the image. Confirm https://www.worldaisummit.com/assets/images/past-editions/main-stage.webp returns 200 and is at least 1200px wide; it was not checked because direct HTTP is blocked. The homepage does show a "Main Stage" tile under "Scenes from Bengaluru". If the file is missing or small, use any large, crawlable photo URL from the homepage. Google prefers 16:9, 4:3 and 1:1 versions.
4. Paste the block into <head> of the homepage. Before that, view the page source and search for "application/ld+json". If an Event block already exists (unverified so far), replace it; do not add a second one. Do not add it to /index.html. That URL canonicals to /.
5. Run the page through the Rich Results Test (search.google.com/test/rich-results) and fix any errors. "Missing performer" is only a warning.
6. Indexing: Google crawled the homepage on 1 Oct 2026 09:45 UTC and chose https://www.worldaisummit.com/ as the canonical, so a manual request is optional. To request indexing, add the www (or Domain) property in Search Console; only the non-www URL-prefix property is connected now.
7. Keep third-party listings in line. AllEvents (allevents.in/bangalore/world-ai-summit-2026-tickets/80002987560857) already feeds Google the event with 9:00 am to 6:00 pm and INR 20,000. Update its ticket price after step 1. Fix the globaltradefairs pages that say "Entry: Free".

EXPECTATIONS
Google has probably indexed the event already through AllEvents (a ticketing site integrated with Google). The main gain is that the official site becomes the info and ticket source. Inclusion in the carousel is up to Google and is unverified. "events in bangalore this week" can match this event only during 12 to 18 Oct. The four target queries add up to about 4,400 searches a month at the upper bounds.

## Content

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Event",
  "@id": "https://www.worldaisummit.com/#event",
  "name": "World AI Summit 2026",
  "url": "https://www.worldaisummit.com/",
  "description": "Two-day AI conference in Bengaluru organised by Elets Technomedia, on the theme 'AI for All: Accelerating India's Journey Towards Inclusive, Responsible and Future-Ready AI'. Seven tracks: Frontier Models & Compute; Sovereign AI & Geopolitics; Enterprise AI in Production; Global Capability Centres (GCCs); Robotics, Agents & Embodied AI; AI for Bharat; Capital, Founders & Exits.",
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
  "image": [
    "https://www.worldaisummit.com/assets/images/past-editions/main-stage.webp"
  ],
  "organizer": {
    "@type": "Organization",
    "name": "Elets Technomedia",
    "url": "https://www.eletsonline.com/"
  },
  "offers": {
    "@type": "Offer",
    "url": "https://www.worldaisummit.com/delegate/",
    "price": "PLACEHOLDER_CURRENT_LOWEST_DELEGATE_PASS_PRICE_INR",
    "priceCurrency": "INR",
    "availability": "https://schema.org/InStock",
    "validFrom": "2026-10-01T00:00:00+05:30"
  }
}
</script>
