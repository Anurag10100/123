# A77: World AI Summit 2026 event-week news kit: four Elets headlines, a live updates page with LiveBlogPosting markup, and the 16 Oct recap switch

- **For recommendation:** Event-week news coverage through Elets publications and a crawlable live-updates page for Top Stories / Discover
- **Research lens:** missing-levers
- **Format:** Markdown with paste-ready HTML, JSON-LD, XML sitemap entry, and Apache and nginx redirect blocks
- **Placeholders the business must fill:**
  - PLACEHOLDER_DELEGATE_COUNT (one figure for every piece: 1,200+ on 22 Sep vs 1,000+ on 30 Sep)
  - PLACEHOLDER_EDITION_NUMBER (2nd vs 3rd; leave out if not confirmed)
  - PLACEHOLDER_SPEAKERS_FROM_OFFICIAL_AGENDA
  - PLACEHOLDER_KEYNOTE_SPEAKER and PLACEHOLDER_TOPIC (Day 1 headline)
  - PLACEHOLDER_ONE_SENTENCE_FROM_SESSION_NOTES
  - PLACEHOLDER_SPEAKER_SLUG and PLACEHOLDER_THEME_SLUG
  - PLACEHOLDER_SESSION_THEME (Day 2 headline)
  - PLACEHOLDER_SPEAKER_NAMES_FROM_AGENDA
  - PLACEHOLDER_AWARDS_DATE
  - PLACEHOLDER_OFFICIAL_RESULTS_SHEET (award categories and winners)
  - PLACEHOLDER_LATEST_UPDATE_TIME and PLACEHOLDER_LATEST_UPDATE_TEXT
  - PLACEHOLDER_COVERAGE_END_TIME (end of live coverage on 15 Oct, ISO with +05:30)
  - PLACEHOLDER_HERO_16x9/4x3/1x1_MIN_1200PX_WIDE_URL and PLACEHOLDER_HERO_ALT_TEXT
  - PLACEHOLDER_ELETS_LOGO_URL
  - PLACEHOLDER_CURRENT_PASS_PRICE_NUMBER_ONLY (the /delegate/ page shows Standard valid till 30 Sept 2026, so check which price applies now)
  - PLACEHOLDER_PRICE_VALID_FROM_DATE
  - PLACEHOLDER_SPEAKER_NAME_AS_IN_OFFICIAL_AGENDA / PLACEHOLDER_ROLE_AS_IN_OFFICIAL_AGENDA / PLACEHOLDER_ORGANISATION / PLACEHOLDER_SPEAKER_PAGE_URL (only verified speakers who are in the agenda)
  - PLACEHOLDER_SPEAKER_DIRECTORY_URL (live /speaker.html now, or /speakers/ if the generated pages are deployed)
  - PLACEHOLDER_UPDATE_HEADLINE / PLACEHOLDER_UPDATE_TEXT_SAME_AS_ON_PAGE / PLACEHOLDER_UPDATE_TIME / PLACEHOLDER_YYYYMMDD-HHMM
  - PLACEHOLDER_QUOTE_FROM_SESSION_RECORD / PLACEHOLDER_TRACK / PLACEHOLDER_HALL
  - PLACEHOLDER_RECAP_PUBLISH_TIME
  - PLACEHOLDER_2027_DATES_SENTENCE_IF_ANNOUNCED

## How to ship

1) Today to 3 Oct (Elets editorial): agree one delegate figure (PLACEHOLDER_DELEGATE_COUNT). Then add a dated update note to the 22 Sep Elets CIO piece (cio.eletsonline.com/.../76367/) so its delegate number and its seven tracks match the site. The 30 Sep piece (/76379/) already follows the current tracks and only needs the number checked. Fill PLACEHOLDER_EDITION_NUMBER or leave the edition out.
2) By 13 Oct (web dev plus whoever controls DNS): verify the Search Console Domain property for worldaisummit.com using a DNS TXT record. Build the live page from Part B using the existing /blog/ post template. Check both JSON-LD blocks at validator.schema.org; note that Google's Rich Results Test does not list LiveBlogPosting as a supported type, so use it only for the Article and Event fields. Prepare three crops of the hero image at least 1200 px wide (16:9, 4:3 and 1:1). Both JSON-LD blocks were checked as valid JSON on 1 Oct.
3) 13 Oct (Elets editorial): publish the preview article (Part A, item 1) with the delegate and awards links.
4) 14 Oct, 09:00 IST: put the live page up. Add the homepage strip and the sitemap entry (Part D). Request indexing once in Search Console. On the morning of 14 Oct, add the live-page link to the preview article. Post updates when there is real news, aiming for about one an hour. Each update needs a matching HTML <article> id and liveBlogUpdate @id, and dateModified, article:modified_time, the visible "Updated" time and the sitemap lastmod all set to that update's time. Publish the Day 1 article that evening.
5) 15 Oct: publish the Day 2 article. Remove the #delegate-cta block and the /delegate/ link paragraph once passes stop selling. Publish the awards article from the official results sheet on 15 or 16 Oct.
6) 16 Oct: do the recap switch (Part C) on the same URL and request indexing once. Change the homepage strip text.
Caveats: the LIVE badge depends on Google treating the site as a news publisher and on compliance with Google News content policies. Google News and Discover eligibility of worldaisummit.com and cio.eletsonline.com has not been verified. The non-www Search Console property shows 0 Discover rows for all of 1 Jun 2025-28 Sep 2026, and www cannot be measured until its property is verified. Sources: venue address from marriott.com/en-us/hotels/blrgs-sheraton-grand-bangalore-hotel-at-brigade-gateway/overview/ and hotelplanner.com (26/1 Dr Rajkumar Rd, Malleswaram Rajajinagar 560055). LIVE badge and LiveBlogPosting: seoforgooglenews.com/p/structured-data-for-news-publishers, jimrobinson.info/liveblogposting-schema/, tickaroo.com/en/blog/how-to-get-the-red-live-badge-on-google-using-liveblogs. IndexNow not supported by Google: pressonify.ai/blog/indexnow-instant-indexing-press-releases-2026 and indexernow.com/google-indexnow. No OpenSEO paid tools were used and no repository files were edited. On the question about CPUs: this session runs on 4 vCPUs (Intel Xeon, 2.8 GHz) with 15 GB RAM, and that allocation cannot be raised from inside the session.

## Content

# World AI Summit 2026: event-week news kit

Facts used here come from the project brief or were checked on 1 Oct 2026. Any text marked PLACEHOLDER_ is a business or editorial decision. Fill it before publishing.

Changes from the original recommendation:
- The live page uses **LiveBlogPosting**, not NewsArticle. Google ties the red LIVE badge in Top Stories to LiveBlogPosting with `coverageStartTime`, `coverageEndTime` and `liveBlogUpdate` (seoforgooglenews.com/p/structured-data-for-news-publishers; jimrobinson.info/liveblogposting-schema/). NewsArticle is still used, but only for the recap from 16 Oct.
- **IndexNow is not used for Google**, because Google does not support it (only Bing, Yandex, Naver, Seznam and Yep do). The Google steps are listed in Part E.
- **Delegate figure.** Elets CIO said "1,200+" on 22 Sep (/76367/) and "1,000+" on 30 Sep (/76379/). Every piece below uses PLACEHOLDER_DELEGATE_COUNT until one figure is agreed.
- **Venue address** checked on 1 Oct 2026: 26/1, Dr Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru, Karnataka 560055 (Marriott hotel page and hotelplanner.com listing).

---

## Part A. Elets editorial: four articles (13, 14, 15 and 16 Oct)

Rules for all four articles:
- Start each headline with "World AI Summit 2026" ("World AI Awards 2026" for the winners). Put "Bengaluru" in the headline or the first sentence. World Summit AI Amsterdam (05-09 October 2026) competes for the same search words.
- Quote speakers only from the session recording or the official session notes. Give each speaker's name, role and organisation exactly as the official agenda prints them. Do not write bios from memory.
- Use a lead image you own or have licensed, at least 1200 px wide, with alt text that describes the scene.
- Use one delegate figure, PLACEHOLDER_DELEGATE_COUNT, everywhere. Do not give an edition number unless PLACEHOLDER_EDITION_NUMBER has been confirmed (some pages say 2nd, others 3rd).

### 1. Preview, publish 13 Oct
**Headline:** World AI Summit 2026: What to expect in Bengaluru on 14-15 October
**Standfirst:** Organised by Elets Technomedia, the two-day summit at Sheraton Grand Bangalore Hotel at Brigade Gateway brings together PLACEHOLDER_DELEGATE_COUNT delegates across seven tracks, from frontier models and compute to capital, founders and exits.
**Slug:** world-ai-summit-2026-what-to-expect-bengaluru
**Track list (as on worldaisummit.com):** Frontier Models & Compute; Sovereign AI & Geopolitics; Enterprise AI in Production; GCCs; Robotics, Agents & Embodied AI; AI for Bharat; Capital, Founders & Exits.
**Speakers:** PLACEHOLDER_SPEAKERS_FROM_OFFICIAL_AGENDA (name, role, organisation only)

### 2. Day 1 report, publish 14 Oct evening
**Headline:** World AI Summit 2026 Day 1: PLACEHOLDER_KEYNOTE_SPEAKER on PLACEHOLDER_TOPIC
**Standfirst:** PLACEHOLDER_ONE_SENTENCE_FROM_SESSION_NOTES. The summit continues at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru, on 15 October.
**Slug:** world-ai-summit-2026-day-1-PLACEHOLDER_SPEAKER_SLUG

### 3. Day 2 report, publish 15 Oct evening
**Headline:** World AI Summit 2026 Day 2: PLACEHOLDER_SESSION_THEME takeaways
**Standfirst:** The second day of World AI Summit 2026 in Bengaluru focused on PLACEHOLDER_SESSION_THEME, with PLACEHOLDER_SPEAKER_NAMES_FROM_AGENDA.
**Slug:** world-ai-summit-2026-day-2-PLACEHOLDER_THEME_SLUG

### 4. Awards results, publish 15 or 16 Oct
**Headline:** World AI Awards 2026: Full list of winners
**Standfirst:** The World AI Awards were presented at World AI Summit 2026 in Bengaluru on PLACEHOLDER_AWARDS_DATE. Winners are listed by category below.
**Body:** a table with the columns Category | Winner | Organisation, filled only from PLACEHOLDER_OFFICIAL_RESULTS_SHEET.
**Slug:** world-ai-awards-2026-winners

### Links to paste into the body of each article
Use the first paragraph only in articles published before the end of 15 Oct. Use the third paragraph only once the live page is up (from 09:00 IST on 14 Oct). Add it to the 13 Oct preview on the morning of 14 Oct.

```html
<p>Delegate passes for World AI Summit 2026 are available on the <a href="https://www.worldaisummit.com/delegate/">World AI Summit delegate page</a>. Groups of three or more delegates receive 10 per cent off.</p>
<p>Details of the World AI Awards are on the <a href="https://www.worldaisummit.com/awards/">World AI Awards page</a>.</p>
<p>Updates from both days are on the <a href="https://www.worldaisummit.com/blog/world-ai-summit-2026-live-updates.html">World AI Summit 2026 live page</a>.</p>
```

---

## Part B. Live page, publish 14 Oct at 09:00 IST

URL: `https://www.worldaisummit.com/blog/world-ai-summit-2026-live-updates.html` (set `<html lang="en-IN">`)

### B1. Paste into `<head>`
Write timestamps in ISO 8601 with the +05:30 offset, for example 2026-10-14T11:30:00+05:30. `dateModified`, `article:modified_time` and the "Updated" line on the page must all show the time of the newest visible update. Change them only when an update is actually added.

```html
<title>World AI Summit 2026 Live Updates: Bengaluru, 14-15 Oct</title>
<meta name="description" content="Live updates from World AI Summit 2026 in Bengaluru, 14-15 October: sessions, speakers and World AI Awards results, newest first.">
<link rel="canonical" href="https://www.worldaisummit.com/blog/world-ai-summit-2026-live-updates.html">
<meta name="robots" content="max-image-preview:large">
<meta property="og:type" content="article">
<meta property="og:site_name" content="World AI Summit">
<meta property="og:title" content="World AI Summit 2026: Live updates from Bengaluru">
<meta property="og:description" content="Sessions, speakers and World AI Awards results from 14-15 October, newest first.">
<meta property="og:url" content="https://www.worldaisummit.com/blog/world-ai-summit-2026-live-updates.html">
<meta property="og:image" content="PLACEHOLDER_HERO_16x9_MIN_1200PX_WIDE_URL">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="675">
<meta property="article:published_time" content="2026-10-14T09:00:00+05:30">
<meta property="article:modified_time" content="PLACEHOLDER_LATEST_UPDATE_TIME">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LiveBlogPosting",
  "@id": "https://www.worldaisummit.com/blog/world-ai-summit-2026-live-updates.html#liveblog",
  "url": "https://www.worldaisummit.com/blog/world-ai-summit-2026-live-updates.html",
  "mainEntityOfPage": "https://www.worldaisummit.com/blog/world-ai-summit-2026-live-updates.html",
  "headline": "World AI Summit 2026: Live updates from Bengaluru, 14-15 October",
  "description": "Live updates from World AI Summit 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru: sessions, speakers and World AI Awards results across both days.",
  "inLanguage": "en-IN",
  "datePublished": "2026-10-14T09:00:00+05:30",
  "dateModified": "PLACEHOLDER_LATEST_UPDATE_TIME",
  "coverageStartTime": "2026-10-14T09:00:00+05:30",
  "coverageEndTime": "PLACEHOLDER_COVERAGE_END_TIME",
  "image": [
    "PLACEHOLDER_HERO_16x9_MIN_1200PX_WIDE_URL",
    "PLACEHOLDER_HERO_4x3_MIN_1200PX_WIDE_URL",
    "PLACEHOLDER_HERO_1x1_MIN_1200PX_WIDE_URL"
  ],
  "author": {
    "@type": "Organization",
    "name": "Elets Technomedia",
    "url": "https://www.eletsonline.com/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Elets Technomedia",
    "url": "https://www.eletsonline.com/",
    "logo": {
      "@type": "ImageObject",
      "url": "PLACEHOLDER_ELETS_LOGO_URL"
    }
  },
  "about": {
    "@type": "Event",
    "name": "World AI Summit 2026",
    "description": "Two-day AI summit in Bengaluru organised by Elets Technomedia, with seven tracks: Frontier Models & Compute; Sovereign AI & Geopolitics; Enterprise AI in Production; GCCs; Robotics, Agents & Embodied AI; AI for Bharat; Capital, Founders & Exits.",
    "url": "https://www.worldaisummit.com/",
    "image": [
      "PLACEHOLDER_HERO_16x9_MIN_1200PX_WIDE_URL"
    ],
    "startDate": "2026-10-14",
    "endDate": "2026-10-15",
    "eventStatus": "https://schema.org/EventScheduled",
    "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
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
      "url": "https://www.eletsonline.com/"
    },
    "offers": {
      "@type": "Offer",
      "url": "https://www.worldaisummit.com/delegate/",
      "price": "PLACEHOLDER_CURRENT_PASS_PRICE_NUMBER_ONLY",
      "priceCurrency": "INR",
      "availability": "https://schema.org/InStock",
      "validFrom": "PLACEHOLDER_PRICE_VALID_FROM_DATE"
    },
    "performer": [
      {
        "@type": "Person",
        "name": "PLACEHOLDER_SPEAKER_NAME_AS_IN_OFFICIAL_AGENDA",
        "jobTitle": "PLACEHOLDER_ROLE_AS_IN_OFFICIAL_AGENDA",
        "affiliation": {
          "@type": "Organization",
          "name": "PLACEHOLDER_ORGANISATION"
        },
        "url": "PLACEHOLDER_SPEAKER_PAGE_URL"
      }
    ]
  },
  "liveBlogUpdate": [
    {
      "@type": "BlogPosting",
      "@id": "https://www.worldaisummit.com/blog/world-ai-summit-2026-live-updates.html#update-20261014-0900",
      "url": "https://www.worldaisummit.com/blog/world-ai-summit-2026-live-updates.html#update-20261014-0900",
      "headline": "Live coverage of World AI Summit 2026 begins in Bengaluru",
      "datePublished": "2026-10-14T09:00:00+05:30",
      "articleBody": "World AI Summit 2026 opens today at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. This page carries updates from sessions on 14 and 15 October and the World AI Awards results when they are announced. The newest update is at the top.",
      "author": {
        "@type": "Organization",
        "name": "Elets Technomedia"
      }
    }
  ]
}
</script>
```

To add an update, put a new object at the **top** of `liveBlogUpdate`:

```json
{
  "@type": "BlogPosting",
  "@id": "https://www.worldaisummit.com/blog/world-ai-summit-2026-live-updates.html#update-PLACEHOLDER_YYYYMMDD-HHMM",
  "url": "https://www.worldaisummit.com/blog/world-ai-summit-2026-live-updates.html#update-PLACEHOLDER_YYYYMMDD-HHMM",
  "headline": "PLACEHOLDER_UPDATE_HEADLINE",
  "datePublished": "PLACEHOLDER_UPDATE_TIME",
  "articleBody": "PLACEHOLDER_UPDATE_TEXT_SAME_AS_ON_PAGE",
  "author": { "@type": "Organization", "name": "Elets Technomedia" }
},
```

Rules for `performer`: list only speakers who are both in the official agenda and marked `confirmed_2026: true` in `worldaisummit/speakers/speakers.json`, and copy one object per speaker. Before you use them, re-check the `note` field: it records a changed role for Sanjeev Rastogi and a role that may have ended for Sushan Rungta.

### B2. Paste into `<body>` (put the newest update first)

```html
<h1>World AI Summit 2026: Live updates from Bengaluru</h1>
<p class="live-meta">Updated <time datetime="PLACEHOLDER_LATEST_UPDATE_TIME">PLACEHOLDER_LATEST_UPDATE_TEXT IST</time></p>
<img src="PLACEHOLDER_HERO_16x9_MIN_1200PX_WIDE_URL" width="1200" height="675" alt="PLACEHOLDER_HERO_ALT_TEXT" fetchpriority="high">
<p>World AI Summit 2026 takes place on 14 and 15 October at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru, organised by Elets Technomedia. Speaker profiles are on the <a href="PLACEHOLDER_SPEAKER_DIRECTORY_URL">speakers page</a>, and details of the World AI Awards are on the <a href="/awards/">awards page</a>.</p>
<aside class="live-cta" id="delegate-cta">
  <p>Delegate passes are available on the <a href="/delegate/">delegate page</a>. Groups of three or more delegates receive 10 per cent off.</p>
</aside>

<article class="live-update" id="update-20261014-0900">
  <p class="live-update__time"><time datetime="2026-10-14T09:00:00+05:30">14 October, 09:00 IST</time></p>
  <h2>Live coverage of World AI Summit 2026 begins in Bengaluru</h2>
  <p>World AI Summit 2026 opens today at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. This page carries updates from sessions on 14 and 15 October and the World AI Awards results when they are announced. The newest update is at the top.</p>
</article>
```

Template for each new update. Paste it above the previous update:

```html
<article class="live-update" id="update-PLACEHOLDER_YYYYMMDD-HHMM">
  <p class="live-update__time"><time datetime="PLACEHOLDER_UPDATE_TIME">PLACEHOLDER_DD October, HH:MM IST</time></p>
  <h2>PLACEHOLDER_UPDATE_HEADLINE</h2>
  <p><a href="PLACEHOLDER_SPEAKER_PAGE_URL">PLACEHOLDER_SPEAKER_NAME</a>, PLACEHOLDER_ROLE, PLACEHOLDER_ORGANISATION, said: "PLACEHOLDER_QUOTE_FROM_SESSION_RECORD"</p>
  <p>Track: PLACEHOLDER_TRACK. Hall: PLACEHOLDER_HALL.</p>
</article>
```

---

## Part C. Recap switch, 16 Oct (same URL, no redirect)

1. Change `<title>` to: `World AI Summit 2026 Bengaluru: Highlights from 14-15 October`
2. Change `<h1>` to: `World AI Summit 2026: Highlights from Bengaluru`
3. Change the meta description to: `What happened at World AI Summit 2026 in Bengaluru on 14-15 October: key sessions, speakers and World AI Awards winners.`
4. Add a short summary at the top. Keep every live update below it under `<h2>As it happened</h2>`.
5. Delete the `#delegate-cta` block and put the sponsorship block below in its place.
6. Replace the LiveBlogPosting JSON-LD with the NewsArticle block below. Keep `<meta name="robots" content="max-image-preview:large">`. The Event block no longer has `offers`, because passes are not on sale after 15 Oct.

```html
<aside class="sponsor-enquiry" id="sponsor-2027">
  <h2>Enquire for 2027 sponsorship</h2>
  <p>Sponsorship and exhibition options for the next World AI Summit are available on request. PLACEHOLDER_2027_DATES_SENTENCE_IF_ANNOUNCED Write to <a href="mailto:partnerships@worldaisummit.com?subject=World%20AI%20Summit%202027%20sponsorship%20enquiry">partnerships@worldaisummit.com</a> with your organisation's name and the audience you want to reach, and the partnerships team will be in touch.</p>
</aside>
```

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "NewsArticle",
  "@id": "https://www.worldaisummit.com/blog/world-ai-summit-2026-live-updates.html#article",
  "url": "https://www.worldaisummit.com/blog/world-ai-summit-2026-live-updates.html",
  "mainEntityOfPage": "https://www.worldaisummit.com/blog/world-ai-summit-2026-live-updates.html",
  "headline": "World AI Summit 2026: Highlights from Bengaluru, 14-15 October",
  "description": "What happened at World AI Summit 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru: key sessions, speakers and World AI Awards winners.",
  "inLanguage": "en-IN",
  "datePublished": "2026-10-14T09:00:00+05:30",
  "dateModified": "PLACEHOLDER_RECAP_PUBLISH_TIME",
  "image": [
    "PLACEHOLDER_HERO_16x9_MIN_1200PX_WIDE_URL",
    "PLACEHOLDER_HERO_4x3_MIN_1200PX_WIDE_URL",
    "PLACEHOLDER_HERO_1x1_MIN_1200PX_WIDE_URL"
  ],
  "author": {
    "@type": "Organization",
    "name": "Elets Technomedia",
    "url": "https://www.eletsonline.com/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Elets Technomedia",
    "url": "https://www.eletsonline.com/",
    "logo": {
      "@type": "ImageObject",
      "url": "PLACEHOLDER_ELETS_LOGO_URL"
    }
  },
  "about": {
    "@type": "Event",
    "name": "World AI Summit 2026",
    "url": "https://www.worldaisummit.com/",
    "image": [
      "PLACEHOLDER_HERO_16x9_MIN_1200PX_WIDE_URL"
    ],
    "startDate": "2026-10-14",
    "endDate": "2026-10-15",
    "eventStatus": "https://schema.org/EventScheduled",
    "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
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
      "url": "https://www.eletsonline.com/"
    },
    "performer": [
      {
        "@type": "Person",
        "name": "PLACEHOLDER_SPEAKER_NAME_AS_IN_OFFICIAL_AGENDA",
        "jobTitle": "PLACEHOLDER_ROLE_AS_IN_OFFICIAL_AGENDA",
        "affiliation": {
          "@type": "Organization",
          "name": "PLACEHOLDER_ORGANISATION"
        },
        "url": "PLACEHOLDER_SPEAKER_PAGE_URL"
      }
    ]
  }
}
</script>
```

---

## Part D. Homepage link and sitemap entry

The homepage is the only URL that ranks for every brand query, so a link from it is the fastest way for Google to find the live page. Add this strip at 09:00 IST on 14 Oct. On 16 Oct change the text to "Read the highlights from World AI Summit 2026."

```html
<p class="live-strip"><a href="/blog/world-ai-summit-2026-live-updates.html">World AI Summit 2026 is under way in Bengaluru. Follow the live updates.</a></p>
```

Add this entry to the sitemap and update `lastmod` whenever an update is added:

```xml
<url>
  <loc>https://www.worldaisummit.com/blog/world-ai-summit-2026-live-updates.html</loc>
  <lastmod>PLACEHOLDER_LATEST_UPDATE_TIME</lastmod>
</url>
```

---

## Part E. Optional short link for stage screens and QR codes

Use this only if `/live` is not already in use. Nothing needs redirecting for the recap, because it keeps the same URL.

Apache (`.htaccess`):
```apache
RedirectMatch 301 ^/live/?$ https://www.worldaisummit.com/blog/world-ai-summit-2026-live-updates.html
```

nginx (inside the `server` block for www.worldaisummit.com):
```nginx
location ~ ^/live/?$ {
    return 301 https://www.worldaisummit.com/blog/world-ai-summit-2026-live-updates.html;
}
```

### Getting Google to index the page (replaces the IndexNow step)
- Verify a Search Console **Domain property** for worldaisummit.com through a DNS TXT record by 13 Oct. It covers both www and non-www. At present only the non-www URL-prefix property exists, so URL Inspection cannot be used on www URLs.
- Use URL Inspection and click "Request indexing" once at 09:00 on 14 Oct and once for the recap on 16 Oct. Do not repeat it every hour; it does not speed anything up.
- IndexNow is optional and reaches Bing, Yandex, Naver, Seznam and Yep only. It has no effect on Google.
