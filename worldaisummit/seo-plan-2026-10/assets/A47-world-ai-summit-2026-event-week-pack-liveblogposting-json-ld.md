# A47: World AI Summit 2026 event-week pack: LiveBlogPosting JSON-LD, page titles and meta, winners share kit, redirects (with verifier corrections)

- **For recommendation:** Event-week coverage on worldaisummit.com: live blog, Day-1 and Day-2 highlights, World AI Awards 2026 winners page and a same-week press release
- **Research lens:** news-content
- **Format:** Markdown with copy-ready blocks: JSON-LD (validated with python json.tool), HTML title/meta/H1, an HTML entry pattern, Apache .htaccess and nginx rules, and email/LinkedIn copy
- **Placeholders the business must fill:**
  - PLACEHOLDER_CURRENT_PASS_PRICE_INR (current delegate pass price; Standard tier expired 30 Sept 2026)
  - PLACEHOLDER_EVENT_IMAGE_URL
  - PLACEHOLDER_LIVE_BLOG_IMAGE_URL
  - PLACEHOLDER_DAY1_LEAD_PHOTO_URL
  - PLACEHOLDER_AWARDS_CEREMONY_DATE_TIME / PLACEHOLDER_AWARDS_CEREMONY_DATE (likely evening of 14 Oct, inferred, confirm)
  - PLACEHOLDER_WINNERS_LIST_LOCK_TIME
  - PLACEHOLDER_PHOTO_DEADLINE
  - PLACEHOLDER_2027_AWARD_FEES (only if a fee is quoted; 2025 was two-tier Rs 18,000 / Rs 20,000 + GST)
  - PLACEHOLDER_MMDD-HHMM, PLACEHOLDER_DDTHH:MM, PLACEHOLDER_HH:MM (per live entry)
  - PLACEHOLDER_SESSION_TITLE, PLACEHOLDER_TRACK, PLACEHOLDER_SPEAKER_NAME / ROLE / SLUG (confirmed_2026 speakers only)
  - PLACEHOLDER_TAKEAWAY_1/2 (as said on stage)
  - PLACEHOLDER_WINNER_CONTACT_NAME, PLACEHOLDER_ORGANISATION, PLACEHOLDER_AWARD_TITLE
  - PLACEHOLDER_SENDER_NAME

## How to ship

Web dev, about 2 hours plus 30 minutes for the schema. Build the three /2026/ pages and /awards/2026-winners/ on 13 Oct, with the titles, meta, H1s and canonicals from section 2. Paste the section 1 JSON-LD into the head of /2026/live/ and replace the PLACEHOLDER_ values. Make /2026/live/ public at 08:30 IST on 14 Oct.

- **Each live post:** the editor adds the HTML entry, updates dateModified and adds the matching BlogPosting at the top of the array, keeping the latest 10.
- **Redirects:** apply Block A only if the bare domain does not already redirect everything to www; Block B always.
- **Day 1 highlights:** publish by 21:00 IST on 14 Oct.
- **Winners page:** publish the text list within 1 hour of the ceremony, then send the section 4 email to every winner.
- **Search Console:** set up a property for www before 13 Oct so the new URLs can be inspected and submitted for indexing.

Expect modest results: the schema should bring about zero lift, and post-event demand drops sharply. The realistic gain is brand clicks moving to deeper pages, plus some new referring domains from winners who use the linked caption.

All JSON blocks passed python json.tool. I could not check the live site's redirects or server type, because this sandbox's proxy blocked requests to worldaisummit.com with a 403.

On your question: this cloud session runs in its own container with 4 CPUs (nproc). It cannot use CPUs from your computer. For more local power, run Claude Code on your own machine.

## Content

## 0. What changed from the brief (verifier corrections)

- **Schema value is about zero.** Google Search Central documents no LiveBlogPosting rich result for a site like this. The LIVE badge it documents is for BroadcastEvent video livestreams. Treat the markup as a cheap description of the page and spend no more than 30 minutes on it. Do not count on it for traffic.
- **Titles lead with brand terms that have measured demand.** 'world ai summit highlights', 'world ai awards winners' and 'world ai summit bengaluru' returned no volume. 'world ai summit 2026' and 'world ai summit bangalore' did (880 in Sep 2025). So the titles use "Bangalore" and keep "Bengaluru" in the H1 and body copy. 'world ai summit' is also searched for the India AI Impact Summit and for worldsummit.ai in Amsterdam, so every title and description names Bangalore/Bengaluru, and the descriptions name Elets.
- **Demand falls sharply after the event.** In 2025, 'world ai summit bangalore' went from 880 in Sep to 40 in Oct. Put the effort into the live blog and the Day 1 page. The Day 2 page and the 17 Oct hero switch will get little search traffic.
- **The awards ceremony is probably on the evening of 14 Oct (inferred).** In 2025 the awards were presented on Day 1, 25 Sep 2025 (Elets LinkedIn post; cio.eletsonline.com kick-off release). Day 1 highlights should therefore include the awards. Confirm the time: PLACEHOLDER_AWARDS_CEREMONY_DATE_TIME.
- **The winners page is effort L, not M.** 2025 had "75+ award titles spanning 6 broad categories" (egov.eletsonline.com, Jul 2025), and the 2025 winners list appeared about 15 days after the ceremony. Build the page in draft from a locked list before the ceremony. Publish the text list within 1 hour and add photos by PLACEHOLDER_PHOTO_DEADLINE.
- **Winners do not link back unless asked.** Qualitrix's 29 Sep 2025 win post has no link to worldaisummit.com. That is why the share kit below puts the URL in the caption itself.
- **Award fee wording.** The 2025 fee was two-tier: Rs 18,000 + GST for Startup and Individual entries, and Rs 20,000 + GST for Enterprise, Government, Leadership and Solution Provider (elets.net/worldaisummit-awards/). On these pages, link to /awards/ and do not quote a fee. If a fee must appear, use PLACEHOLDER_2027_AWARD_FEES.
- **Search Console covers only the non-www property.** The new URLs are on www. Before 13 Oct, add a Domain property (DNS TXT) or a www URL-prefix property (HTML-file upload to the site root, which the web developer can do). Without one of these, URL Inspection and "Request indexing" will not work for /2026/* and /awards/2026-winners/.

---

## 1. JSON-LD for https://www.worldaisummit.com/2026/live/ (paste in <head>)

Before going live, replace the PLACEHOLDER_ values or delete those lines. Speakers (performer) are left out on purpose. Add only people with `confirmed_2026: true` in speakers.json (50 of 76), and only after the /speakers/ pages are deployed.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://www.worldaisummit.com/#organizer",
      "name": "Elets Technomedia",
      "url": "https://eletsonline.com/"
    },
    {
      "@type": "Event",
      "@id": "https://www.worldaisummit.com/#event",
      "name": "World AI Summit 2026",
      "url": "https://www.worldaisummit.com/",
      "description": "World AI Summit 2026 in Bengaluru, organised by Elets Technomedia, with seven tracks: Frontier Models & Compute; Sovereign AI & Geopolitics; Enterprise AI in Production; GCCs; Robotics, Agents & Embodied AI; AI for Bharat; Capital, Founders & Exits.",
      "startDate": "2026-10-14",
      "endDate": "2026-10-15",
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
      "organizer": { "@id": "https://www.worldaisummit.com/#organizer" },
      "offers": {
        "@type": "Offer",
        "url": "https://www.worldaisummit.com/delegate/",
        "price": "PLACEHOLDER_CURRENT_PASS_PRICE_INR",
        "priceCurrency": "INR",
        "availability": "https://schema.org/InStock"
      },
      "image": "PLACEHOLDER_EVENT_IMAGE_URL"
    },
    {
      "@type": "LiveBlogPosting",
      "@id": "https://www.worldaisummit.com/2026/live/#liveblog",
      "url": "https://www.worldaisummit.com/2026/live/",
      "mainEntityOfPage": "https://www.worldaisummit.com/2026/live/",
      "headline": "World AI Summit 2026 Live: Day 1 and Day 2 updates from Bengaluru",
      "description": "Session-by-session updates from World AI Summit 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru, on 14-15 October 2026.",
      "inLanguage": "en-IN",
      "datePublished": "2026-10-14T08:30:00+05:30",
      "dateModified": "2026-10-14T09:00:00+05:30",
      "coverageStartTime": "2026-10-14T09:00:00+05:30",
      "coverageEndTime": "2026-10-15T19:00:00+05:30",
      "about": { "@id": "https://www.worldaisummit.com/#event" },
      "author": { "@id": "https://www.worldaisummit.com/#organizer" },
      "publisher": { "@id": "https://www.worldaisummit.com/#organizer" },
      "image": "PLACEHOLDER_LIVE_BLOG_IMAGE_URL",
      "liveBlogUpdate": [
        {
          "@type": "BlogPosting",
          "@id": "https://www.worldaisummit.com/2026/live/#update-1014-0900",
          "url": "https://www.worldaisummit.com/2026/live/#update-1014-0900",
          "headline": "World AI Summit 2026 opens in Bengaluru",
          "datePublished": "2026-10-14T09:00:00+05:30",
          "articleBody": "Day 1 of World AI Summit 2026 is under way at Sheraton Grand Bangalore Hotel at Brigade Gateway. Sessions run across seven tracks: Frontier Models & Compute; Sovereign AI & Geopolitics; Enterprise AI in Production; GCCs; Robotics, Agents & Embodied AI; AI for Bharat; and Capital, Founders & Exits. This page is updated through the day."
        }
      ]
    }
  ]
}
</script>
```

**For each new post:** (1) set `dateModified` to the time of the post, and (2) add the entry below at the top of `liveBlogUpdate`. Keep only the latest 10 entries in the JSON-LD; the page itself keeps every entry. If the editor cannot keep the JSON-LD in step with the page, update only `dateModified` and leave the opening entry. Markup that covers only some of the entries is fine. Markup that contradicts the page is not.

```json
{
  "@type": "BlogPosting",
  "@id": "https://www.worldaisummit.com/2026/live/#update-PLACEHOLDER_MMDD-HHMM",
  "url": "https://www.worldaisummit.com/2026/live/#update-PLACEHOLDER_MMDD-HHMM",
  "headline": "PLACEHOLDER_SESSION_TITLE",
  "datePublished": "2026-10-PLACEHOLDER_DDTHH:MM:00+05:30",
  "articleBody": "PLACEHOLDER_TRACK. PLACEHOLDER_SPEAKER_NAME_AND_ROLE_CONFIRMED_2026_ONLY. PLACEHOLDER_2_TO_3_TAKEAWAYS_AS_SAID_ON_STAGE"
}
```

**Matching visible HTML for each entry.** The id must match the #fragment above.

```html
<article class="live-entry" id="update-PLACEHOLDER_MMDD-HHMM">
  <time datetime="2026-10-PLACEHOLDER_DDTHH:MM+05:30">PLACEHOLDER_HH:MM IST</time>
  <h2>PLACEHOLDER_SESSION_TITLE</h2>
  <p class="meta">Track: PLACEHOLDER_TRACK · <a href="/speakers/PLACEHOLDER_SLUG/">PLACEHOLDER_SPEAKER_NAME</a>, PLACEHOLDER_ROLE</p>
  <ul>
    <li>PLACEHOLDER_TAKEAWAY_1 (as said on stage)</li>
    <li>PLACEHOLDER_TAKEAWAY_2</li>
  </ul>
</article>
```

Link to /speakers/<slug>/ only after those pages are deployed. Until then, use plain text. Never write speaker bios or quotes from memory.

---

## 2. Titles, meta descriptions and H1s

**/2026/live/**
- `<title>World AI Summit 2026 Live Updates | Bangalore, 14–15 Oct</title>` (56 chars)
- `<meta name="description" content="Session-by-session updates from World AI Summit 2026, Bengaluru, 14–15 October, organised by Elets Technomedia: key points, speakers and announcements.">` (151)
- H1: World AI Summit 2026 Live: Day 1 and Day 2 updates from Bengaluru
- `<link rel="canonical" href="https://www.worldaisummit.com/2026/live/">`

**/2026/day-1-highlights/**
- `<title>World AI Summit 2026 Day 1 Highlights | Bangalore</title>` (49)
- `<meta name="description" content="The main statements, launches and MoUs from Day 1 of World AI Summit 2026 in Bengaluru on 14 October, with links to the live blog and agenda.">` (141)
- H1: World AI Summit 2026 Day 1 highlights: key announcements from Bengaluru
- If the awards are confirmed for 14 Oct, add a section "World AI Awards 2026" that links to /awards/2026-winners/.

**/2026/day-2-highlights/**
- `<title>World AI Summit 2026 Day 2 Highlights | Bangalore</title>` (49)
- `<meta name="description" content="The main statements, launches and MoUs from Day 2 of World AI Summit 2026 in Bengaluru on 15 October, with links to the live blog and agenda.">` (141)
- H1: World AI Summit 2026 Day 2 highlights: key announcements from Bengaluru

**/awards/2026-winners/**
- `<title>World AI Awards 2026 Winners | World AI Summit Bangalore</title>` (56)
- `<meta name="description" content="All World AI Awards 2026 winners, presented at World AI Summit 2026 in Bengaluru: category, organisation, project and citation for each award.">` (142)
- H1: World AI Awards 2026: winners
- Intro line: "The World AI Awards 2026 were presented at World AI Summit 2026, Sheraton Grand Bangalore Hotel at Brigade Gateway, on PLACEHOLDER_AWARDS_CEREMONY_DATE. Winners are listed below by category."
- Table columns: Category | Award title | Winner organisation | Project | Citation (one line) | Photo
- No schema is needed here, because Google has no rich result for award lists.

**Article JSON-LD for the highlights pages.** Optional. Day 1 is shown; for Day 2, change the headline and URL, and set the dates to 15 Oct.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "World AI Summit 2026 Day 1 highlights: key announcements from Bengaluru",
  "url": "https://www.worldaisummit.com/2026/day-1-highlights/",
  "mainEntityOfPage": "https://www.worldaisummit.com/2026/day-1-highlights/",
  "inLanguage": "en-IN",
  "datePublished": "2026-10-14T21:00:00+05:30",
  "dateModified": "2026-10-14T21:00:00+05:30",
  "image": "PLACEHOLDER_DAY1_LEAD_PHOTO_URL",
  "about": { "@type": "Event", "@id": "https://www.worldaisummit.com/#event", "name": "World AI Summit 2026" },
  "author": { "@type": "Organization", "name": "Elets Technomedia", "url": "https://eletsonline.com/" },
  "publisher": { "@type": "Organization", "name": "Elets Technomedia", "url": "https://eletsonline.com/" }
}
</script>
```

---

## 3. Redirects

Block A sends the new paths on the bare domain to www, so links that winners share without "www" all end up on one URL. Skip Block A if the bare domain already sends all traffic to www with a 301; I could not check this from here. It covers only the new paths and leaves the existing non-www /awards untouched during event week. Block B sets up temporary short links for stage slides, QR codes and the press release.

**Apache (.htaccess at the site root)**
```apache
RewriteEngine On

# A) New event-week URLs: bare domain -> www (301)
RewriteCond %{HTTP_HOST} ^worldaisummit\.com$ [NC]
RewriteRule ^(2026(/.*)?|awards/2026-winners(/.*)?)$ https://www.worldaisummit.com/$1 [R=301,L]

# B) Short links (302, temporary; remove or repoint after 31 Oct)
RewriteRule ^live/?$ https://www.worldaisummit.com/2026/live/ [R=302,L]
RewriteRule ^winners/?$ https://www.worldaisummit.com/awards/2026-winners/ [R=302,L]
```

**nginx**
```nginx
# A) in the server block for worldaisummit.com (bare domain)
location ~ ^/(2026(/.*)?|awards/2026-winners(/.*)?)$ {
    return 301 https://www.worldaisummit.com$request_uri;
}

# B) in BOTH server blocks (www and bare)
location ~ ^/live/?$    { return 302 https://www.worldaisummit.com/2026/live/; }
location ~ ^/winners/?$ { return 302 https://www.worldaisummit.com/awards/2026-winners/; }
```

Add the four new URLs to sitemap.xml with `<lastmod>` on the day each goes live. Link them from the homepage hero and from /awards/; /awards/ is not linked internally today.

---

## 4. Winner share kit (email within 1 hour of the winners page going live)

**Subject:** Your World AI Awards 2026 winner kit

Dear PLACEHOLDER_WINNER_CONTACT_NAME,

Congratulations to PLACEHOLDER_ORGANISATION on receiving the PLACEHOLDER_AWARD_TITLE at the World AI Awards 2026, presented at World AI Summit 2026 in Bengaluru.

The full winners list is now live: https://www.worldaisummit.com/awards/2026-winners/

Attached are your winner badge (PNG) and the official photograph. When you share the news on LinkedIn or in your newsroom, please link to the winners page above so readers can see the full list and the citation.

Suggested LinkedIn caption:
"We are pleased to share that PLACEHOLDER_ORGANISATION has received the PLACEHOLDER_AWARD_TITLE at the World AI Awards 2026, presented at World AI Summit 2026 in Bengaluru. Thank you to our team and partners. Full list of winners: https://www.worldaisummit.com/awards/2026-winners/ #WorldAISummit #WorldAIAwards"

Newsroom line (HTML):
`Recognised at the <a href="https://www.worldaisummit.com/awards/2026-winners/">World AI Awards 2026</a>, World AI Summit, Bengaluru.`

Badge alt text: "World AI Awards 2026 Winner – World AI Summit, Bengaluru"

Regards,
PLACEHOLDER_SENDER_NAME
World AI Awards Secretariat, Elets Technomedia
secretariat@worldaisummit.com

---

## 5. Pre-flight checklist (by 13 Oct)

1. Verify a Search Console property for www: Domain (DNS TXT) or www URL-prefix (HTML file).
2. Get the ceremony date and time from the awards team: PLACEHOLDER_AWARDS_CEREMONY_DATE_TIME.
3. Get the locked winners spreadsheet (category, title, organisation, project, citation) by PLACEHOLDER_WINNERS_LIST_LOCK_TIME, and build the page in draft from it.
4. Make sure the live blog shows "Coverage starts 09:00 IST, 14 October" until the first entry goes up.
5. Run each page through the Rich Results Test or validator.schema.org after replacing the placeholders.
6. Concluding press release on 16 Oct, linking to /awards/2026-winners/ and /2026/day-1-highlights/.

Sources: venue address from marriott.com/en-us/hotels/blrgs-sheraton-grand-bangalore-hotel-at-brigade-gateway/overview/ and hotelplanner.com (26/1 Dr. Rajkumar Road, Malleswaram-Rajajinagar, 560055). All other facts are from the verifier notes and the project context supplied.
