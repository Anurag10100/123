# A63: Page outline and build kit: /awards/winners-2026/ and /awards/winners-2025/ (World AI Awards, Bengaluru)

- **For recommendation:** Publish winners pages: /awards/winners-2025/ now, and /awards/winners-2026/ live on the ceremony night with winner name, company and category
- **Research lens:** awards
- **Format:** Markdown page outline with ready-to-paste HTML head and body skeleton, schema.org JSON-LD (@graph with Event, Place/PostalAddress, Organization, ItemList, BreadcrumbList), the 2025 variant with verified rows prefilled, and redirect rules for Apache .htaccess and nginx
- **Placeholders the business must fill:**
  - PLACEHOLDER_CEREMONY_DATE_2026 (14 or 15 Oct 2026)
  - PLACEHOLDER_NUMBER_OF_AWARDS_2026
  - PLACEHOLDER_CONFIRM_2026_GROUPS (2026 award groups and titles; /awards/ lists none)
  - PLACEHOLDER_LAST_UPDATED
  - PLACEHOLDER_WINNER_ORGANISATION / PLACEHOLDER_PROJECT_OR_INDIVIDUAL / PLACEHOLDER_CITY / PLACEHOLDER_AWARD_TITLE / PLACEHOLDER_INDIVIDUAL_NAME / PLACEHOLDER_DESIGNATION (per row, from nomination forms and jury results)
  - PLACEHOLDER_AWARDS_CONTACT_EMAIL
  - PLACEHOLDER_BADGE_FILE_URLS
  - PLACEHOLDER_PRESS_KIT_URL
  - PLACEHOLDER_PHOTO_GALLERY / PLACEHOLDER_2025_PHOTOS
  - PLACEHOLDER_OG_IMAGE_URL
  - PLACEHOLDER_EVENT_IMAGE_URL / PLACEHOLDER_2025_EVENT_IMAGE_URL
  - PLACEHOLDER_CURRENT_PASS_PRICE_INR (bare number)
  - PLACEHOLDER_OFFER_VALID_FROM_ISO
  - PLACEHOLDER_PUBLISH_DATE_ISO / PLACEHOLDER_MODIFIED_DATE_ISO
  - PLACEHOLDER_DELEGATE_LINK_TEXT (before and after 15 Oct)
  - PLACEHOLDER_NOMINATIONS_STATUS and PLACEHOLDER_NOMINATION_DEADLINE (unconfirmed whether 2026 nominations are open after 6 Oct)
  - PLACEHOLDER_2025_NUMBER_OF_AWARDS_PRESENTED
  - PLACEHOLDER_GROUP / PLACEHOLDER_AWARD for Purview Services, Syngenta Group (Cropwise Grower), Altio AI, Familywala Eshop, Crisil Corporate Technology
  - PLACEHOLDER_CRISIL_INDIVIDUAL_NAME
  - PLACEHOLDER_SUPPLY_CHAIN_WINNER (AI for Enhanced Supply Chain Management, 2025)
  - PLACEHOLDER_QUALITRIX_REGISTERED_NAME

## How to ship

1) Before publishing (Elets IT, about 15 min): add a Search Console Domain property for worldaisummit.com, verified by a DNS TXT record, or a www URL-prefix property. Today only the non-www property is verified, so new www URLs cannot be inspected or submitted for indexing. Also confirm whether non-www already 301s to www site-wide. If it does, skip rule 1 in Part D.
2) 2025 page, by 6 Oct (awards team, then web, then editorial; 2-3 hours):
   - Export the presented 2025 awards from Elets records. Only award titles that were actually given go in.
   - Check the seven publicly verified rows. Fill in their award titles and the Crisil individual's name.
   - Build /awards/winners-2025/index.html from Part B and add the JSON-LD.
   - Validate at validator.schema.org and Google's Rich Results Test.
   - Add the Part C links and the sitemap entry, upload, then use URL Inspection and Request indexing.
   - Choose the nominations box version only after the business confirms whether 2026 nominations are open.
3) 2026 page:
   - By 13 Oct, build it on staging (not live) with all rows already entered from jury results. Winners are decided before the night, so no one types 75+ rows during the event.
   - Upload once the ceremony ends on PLACEHOLDER_CEREMONY_DATE_2026, the same night or by 10:00 IST the next morning.
   - If some data is late, publish group by group and keep the "Last updated" line current.
   - The next morning, email each winner their row link (#award-slug), the badge, the press kit and the suggested post. This is the main value: referral visits and links from winners' posts.
   - Switch the /awards/ banner link and the /awards/winners/ 302 to 2026.
   - Add photos on 15-16 Oct and remove the Event offers block after 15 Oct.
4) Do not retitle /awards/. Its current queries are generic ('ai awards 2026' with 178 impressions, 'world ai awards' with 44 impressions at average position 3), so a banner link is enough.
5) Expectations to give stakeholders: search demand for winners queries is close to zero. GSC impressions for /awards fell from 25-28 a day on 24-25 Sep 2025 to 0-3 a day by 27 Sep. The head term is shared with worldawards.ai. Judge success by referral sessions and new linking domains, not rankings.
6) Before upload, replace every PLACEHOLDER_ marker. Price and similar numeric fields take bare numbers.
Note on the user's question: this agent runs in a cloud container that reports 4 CPUs (nproc). It cannot use CPUs from the user's own computer.

## Content

# /awards/winners-2026/: page outline (the 2025 variant is in Part B)

What the verifier changed in the original outline:
- The title and meta now include "Bengaluru" and "Elets". The query "world ai awards 2025 winners" is shared with a different brand: worldawards.ai ranks #1 and its Instagram account ranks #3. Our /awards (non-www) ranks #4 organic.
- The page does not promise search traffic. Its value comes from referrals and links when winners share their row.
- The 2026 rows are entered from jury results before the ceremony, on staging. Nobody types 75+ rows on the night.
- The 2025 call to action depends on whether nominations are still open.
- The unverified Cypher comparison has been dropped.

---

## Part A: /awards/winners-2026/

### A1. Head
```html
<title>World AI Awards 2026 Winners, Bengaluru | World AI Summit</title>
<meta name="description" content="World AI Awards 2026 winners, presented by Elets at World AI Summit Bengaluru on PLACEHOLDER_CEREMONY_DATE_2026: enterprises, startups, government and AI leaders.">
<link rel="canonical" href="https://www.worldaisummit.com/awards/winners-2026/">
<meta property="og:type" content="article">
<meta property="og:title" content="World AI Awards 2026: Full List of Winners">
<meta property="og:description" content="Winners of the World AI Awards 2026, presented by Elets Technomedia at World AI Summit, Bengaluru.">
<meta property="og:url" content="https://www.worldaisummit.com/awards/winners-2026/">
<meta property="og:image" content="PLACEHOLDER_OG_IMAGE_URL">  <!-- 1200x630 JPG. This is what shows when a winner shares the link on LinkedIn or WhatsApp. -->
<meta name="twitter:card" content="summary_large_image">
```
The title is 57 characters. The meta description is about 150 characters once the date is filled in.

### A2. Body copy, in page order

**H1: World AI Awards 2026: Full List of Winners**

Last updated: PLACEHOLDER_LAST_UPDATED (date and time, IST)

**Intro, for after the ceremony:**
The World AI Awards 2026 were presented on PLACEHOLDER_CEREMONY_DATE_2026 at World AI Summit 2026, held on 14-15 October 2026 at the Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. Elets Technomedia organises the awards. PLACEHOLDER_NUMBER_OF_AWARDS_2026 awards were presented across six groups. Each entry shows the award, the winning organisation, the project or individual recognised, and the city, as given on the nomination form.

**Note under the intro:**
Names appear as submitted on the nomination form and confirmed by the winner. To report a correction, write to PLACEHOLDER_AWARDS_CONTACT_EMAIL.

**Jump links**, in a `<nav aria-label="Award groups">`:
AI Enterprise & Application · Business Transformation & Innovation · Smart Tech & AI Engineering · AI in Governance · AI Startups · AI Leadership

**Six H2s**, one per group. Check PLACEHOLDER_CONFIRM_2026_GROUPS: the live /awards/ page lists no categories, so these group names come from 2025.

| H2 | Section id |
|---|---|
| AI Enterprise & Application | group-ai-enterprise-application |
| Business Transformation & Innovation | group-business-transformation-innovation |
| Smart Tech & AI Engineering | group-smart-tech-ai-engineering |
| AI in Governance | group-ai-in-governance |
| AI Startups | group-ai-startups |
| AI Leadership | group-ai-leadership |

The table pattern is the same for every group. The example below is AI Startups.
```html
<section id="group-ai-startups" aria-labelledby="h-ai-startups">
  <h2 id="h-ai-startups">AI Startups</h2>
  <div class="table-wrap"><!-- .table-wrap{overflow-x:auto} keeps phones free of page-level horizontal scroll -->
  <table>
    <caption>World AI Awards 2026: AI Startups winners</caption>
    <thead><tr>
      <th scope="col">Award</th><th scope="col">Winner (organisation)</th>
      <th scope="col">Project or individual</th><th scope="col">City</th>
    </tr></thead>
    <tbody>
      <tr id="most-promising-ai-startup">
        <th scope="row"><a href="#most-promising-ai-startup">Most Promising AI Startup</a></th>
        <td>PLACEHOLDER_WINNER_ORGANISATION</td>
        <td>PLACEHOLDER_PROJECT_OR_INDIVIDUAL</td>
        <td>PLACEHOLDER_CITY</td>
      </tr>
      <!-- one <tr> per award. id = award title in lower case, hyphenated.
           If two winners share an award, give the second row the id slug-2. -->
    </tbody>
  </table>
  </div>
</section>
```
- Add `tr:target{background:var(--highlight)}` so a deep link highlights the row.
- Add `[id]{scroll-margin-top:80px}` so the sticky header does not cover the row.
- In AI Leadership, put the person's name and designation in "Project or individual" and the organisation in "Winner (organisation)".

**H2: Winners: download your badge and press kit**
Winners can download the official winner badge (PNG and SVG) and the press kit, which holds the logo, approved boilerplate and photographs. Use the badge only with the award and year shown. When you share the news, please link to your row on this page so readers can see the full list.
- Badge: PLACEHOLDER_BADGE_FILE_URLS
- Press kit: PLACEHOLDER_PRESS_KIT_URL
- Suggested post: "We have received the [Award] at the World AI Awards 2026, presented by Elets Technomedia at World AI Summit, Bengaluru. Full list: https://www.worldaisummit.com/awards/winners-2026/#[award-slug]"
- For a certificate copy or high-resolution photos, write to PLACEHOLDER_AWARDS_CONTACT_EMAIL.

**H2: Photos from the awards night**
- Until 15-16 Oct, the section reads: "Photos from the awards night will be added on 15-16 October 2026."
- After that it holds PLACEHOLDER_PHOTO_GALLERY: WebP images with explicit width and height and `loading="lazy"`.
- Alt text and caption pattern: "[Winner organisation] receives the [Award] at the World AI Awards 2026, Bengaluru".

**H2: About the World AI Awards**
Elets Technomedia presents the World AI Awards at World AI Summit in Bengaluru. They recognise applied AI work by enterprises, government bodies and startups, and by individual leaders. The 2025 awards were presented on 25 September 2025. <a href="/awards/winners-2025/">See the World AI Awards 2025 winners</a>.

**Closing links**
- <a href="/awards/">About the World AI Awards and nominations</a>
- <a href="/delegate/">PLACEHOLDER_DELEGATE_LINK_TEXT</a>. Before 15 Oct: "Book a delegate pass for World AI Summit, 14-15 October 2026". After 15 Oct: the next-edition wording the business decides.
- <a href="/awards/winners-2025/">World AI Awards 2025 winners</a>

### A3. JSON-LD for the 2026 page (one script tag, in the head)

Notes on the JSON-LD:
- `performer` is left out on purpose. This page names award winners, not speakers, so it only ever lists verified people.
- The `offers` block should come out after 15 Oct 2026.
- `eventStatus` stays EventScheduled after the event. That is Google's guidance for events that took place.
- The address is from Marriott's hotel page and Apple Maps. The geo coordinates are from Google Places data via Exa.

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://www.worldaisummit.com/awards/winners-2026/#webpage",
      "url": "https://www.worldaisummit.com/awards/winners-2026/",
      "name": "World AI Awards 2026: Full List of Winners",
      "description": "World AI Awards 2026 winners, presented by Elets Technomedia at World AI Summit, Bengaluru.",
      "inLanguage": "en-IN",
      "datePublished": "PLACEHOLDER_PUBLISH_DATE_ISO",
      "dateModified": "PLACEHOLDER_MODIFIED_DATE_ISO",
      "isPartOf": { "@type": "WebSite", "@id": "https://www.worldaisummit.com/#website", "url": "https://www.worldaisummit.com/", "name": "World AI Summit" },
      "about": { "@id": "https://www.worldaisummit.com/#event-2026" },
      "publisher": { "@id": "https://www.worldaisummit.com/#elets" },
      "breadcrumb": { "@id": "https://www.worldaisummit.com/awards/winners-2026/#breadcrumb" },
      "mainEntity": { "@id": "https://www.worldaisummit.com/awards/winners-2026/#winners" }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://www.worldaisummit.com/awards/winners-2026/#breadcrumb",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.worldaisummit.com/" },
        { "@type": "ListItem", "position": 2, "name": "World AI Awards", "item": "https://www.worldaisummit.com/awards/" },
        { "@type": "ListItem", "position": 3, "name": "Winners 2026", "item": "https://www.worldaisummit.com/awards/winners-2026/" }
      ]
    },
    {
      "@type": "Organization",
      "@id": "https://www.worldaisummit.com/#elets",
      "name": "Elets Technomedia",
      "url": "https://www.eletsonline.com/"
    },
    {
      "@type": "Event",
      "@id": "https://www.worldaisummit.com/#event-2026",
      "name": "World AI Summit 2026",
      "description": "World AI Summit 2026 and the World AI Awards, organised by Elets Technomedia in Bengaluru.",
      "startDate": "2026-10-14",
      "endDate": "2026-10-15",
      "eventStatus": "https://schema.org/EventScheduled",
      "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
      "image": ["PLACEHOLDER_EVENT_IMAGE_URL"],
      "url": "https://www.worldaisummit.com/",
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
        },
        "geo": { "@type": "GeoCoordinates", "latitude": 13.01247, "longitude": 77.55484 }
      },
      "organizer": { "@id": "https://www.worldaisummit.com/#elets" },
      "offers": {
        "@type": "Offer",
        "url": "https://www.worldaisummit.com/delegate/",
        "price": "PLACEHOLDER_CURRENT_PASS_PRICE_INR",
        "priceCurrency": "INR",
        "availability": "https://schema.org/InStock",
        "validFrom": "PLACEHOLDER_OFFER_VALID_FROM_ISO"
      }
    },
    {
      "@type": "ItemList",
      "@id": "https://www.worldaisummit.com/awards/winners-2026/#winners",
      "name": "World AI Awards 2026 winners",
      "itemListOrder": "https://schema.org/ItemListUnordered",
      "itemListElement": [
        {
          "@type": "ListItem", "position": 1,
          "item": {
            "@type": "Organization",
            "name": "PLACEHOLDER_WINNER_ORGANISATION",
            "award": "PLACEHOLDER_AWARD_TITLE, World AI Awards 2026",
            "address": { "@type": "PostalAddress", "addressLocality": "PLACEHOLDER_CITY", "addressCountry": "IN" }
          }
        },
        {
          "@type": "ListItem", "position": 2,
          "item": {
            "@type": "Person",
            "name": "PLACEHOLDER_INDIVIDUAL_NAME",
            "jobTitle": "PLACEHOLDER_DESIGNATION",
            "award": "PLACEHOLDER_AWARD_TITLE, World AI Awards 2026",
            "worksFor": { "@type": "Organization", "name": "PLACEHOLDER_WINNER_ORGANISATION" }
          }
        }
      ]
    }
  ]
}
```
- Use one ListItem per table row. Organisation awards use the Organization type; individual awards (AI Leadership and similar) use Person.
- Put a bare number in `price`, for example 20000, once the business confirms the price.

---

## Part B: /awards/winners-2025/ (same template, publish by 6 Oct)

**Title:** World AI Awards 2025 Winners, Bengaluru | World AI Summit (57 characters)

**Meta:** World AI Awards 2025 winners, presented by Elets at World AI Summit Bengaluru on 25 September 2025: enterprises, startups, government and AI leaders. (about 149 characters)

**Canonical:** https://www.worldaisummit.com/awards/winners-2025/

**H1: World AI Awards 2025: Full List of Winners**

**Intro:**
The World AI Awards 2025 were presented on 25 September 2025 at World AI Summit 2025 (25-26 September 2025), Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. Elets Technomedia organised the awards. PLACEHOLDER_2025_NUMBER_OF_AWARDS_PRESENTED awards were presented across six groups. Each entry shows the award, the winning organisation, the project or individual recognised, and the city, as given on the nomination form.

**Box above the tables.** Choose one version through PLACEHOLDER_NOMINATIONS_STATUS. The live /awards/ page shows no deadline, so this is unconfirmed.
- If nominations are open: "Nominations for the World AI Awards 2026 close on PLACEHOLDER_NOMINATION_DEADLINE. <a href="/awards/">Submit a nomination</a>."
- If nominations are closed: "The World AI Awards 2026 will be presented at World AI Summit, 14-15 October 2026, Bengaluru. <a href="/delegate/">Book a delegate pass</a>."

**Group H2s and table:** the same six groups and four columns as Part A.
- /1st-edition/awards.html lists 96 award titles: 26 in AI Enterprise & Application, 13 in Business Transformation & Innovation, 16 in Smart Tech & AI Engineering, 4 in AI in Governance, 19 in AI Startups and 18 in AI Leadership. The page headline says "75+".
- List only the titles that were actually presented, taken from Elets records.

**Rows verified from public sources.** Check each one against Elets records before publishing.

| Group | Award | Winner (organisation) | Project or individual | City | Source |
|---|---|---|---|---|---|
| Smart Tech & AI Engineering | AI Validation & Testing Excellence | PLACEHOLDER_QUALITRIX_REGISTERED_NAME (Qualitrix) | PLACEHOLDER | PLACEHOLDER_CITY | qualitrix.com release, 29 Sep 2025 |
| AI Enterprise & Application | AI for Enhanced Supply Chain Management | PLACEHOLDER_SUPPLY_CHAIN_WINNER | PLACEHOLDER | PLACEHOLDER_CITY | winner's LinkedIn post, 27 Sep 2025 |
| PLACEHOLDER_GROUP | PLACEHOLDER_AWARD | Purview Services | PLACEHOLDER | PLACEHOLDER_CITY | Elets LinkedIn, 10 Oct 2025 |
| PLACEHOLDER_GROUP | PLACEHOLDER_AWARD | Syngenta Group | Cropwise Grower | PLACEHOLDER_CITY | Elets LinkedIn, 10 Oct 2025 |
| PLACEHOLDER_GROUP | PLACEHOLDER_AWARD | Altio AI | PLACEHOLDER | PLACEHOLDER_CITY | Elets LinkedIn, 10 Oct 2025 |
| PLACEHOLDER_GROUP | PLACEHOLDER_AWARD | Familywala Eshop | PLACEHOLDER | PLACEHOLDER_CITY | Elets LinkedIn, 10 Oct 2025 |
| PLACEHOLDER_GROUP | PLACEHOLDER_AWARD (individual award) | Crisil Corporate Technology | PLACEHOLDER_CRISIL_INDIVIDUAL_NAME, PLACEHOLDER_DESIGNATION | PLACEHOLDER_CITY | Elets LinkedIn, 10 Oct 2025 |

Do not guess any award title for these rows. The remaining rows come only from Elets records.

**Remaining H2s**, the same as Part A with "2025" in place of "2026":
- "Winners: download your badge and press kit"
- "Photos from the 2025 awards night" (PLACEHOLDER_2025_PHOTOS)
- "About the World AI Awards", linking to /awards/winners-2026/ once that page is live
- Closing links: /awards/, /delegate/ and /awards/winners-2026/

**JSON-LD for the 2025 page.** Copy the Part A @graph and change the following:
1. Replace every `winners-2026` with `winners-2025` in the WebPage, BreadcrumbList and ItemList @ids and URLs. The breadcrumb name becomes "Winners 2025".
2. Point WebPage `about` to `https://www.worldaisummit.com/#event-2025`.
3. Add an Event node with:
   - "@id": "https://www.worldaisummit.com/#event-2025"
   - "name": "World AI Summit 2025"
   - "startDate": "2025-09-25"
   - "endDate": "2025-09-26"
   - "url": "https://www.worldaisummit.com/1st-edition/"
   - eventStatus EventScheduled and OfflineEventAttendanceMode
   - the same location and organizer as Part A, image PLACEHOLDER_2025_EVENT_IMAGE_URL, and no offers.
4. Keep the Part A `#event-2026` node unchanged, with startDate 2026-10-14, endDate 2026-10-15 and offers url /delegate/, because this page promotes the 2026 edition.
5. In the ItemList, change the award suffix to "World AI Awards 2025".

---

## Part C: internal links (paste as is)

On /awards/, at the top of the content. Keep the existing title. It ranks #2-3 for "world ai awards", and none of the /awards queries asks about winners.
```html
<p class="notice"><a href="/awards/winners-2025/">See the World AI Awards 2025 winners</a></p>
<!-- after the ceremony, change to: <a href="/awards/winners-2026/">See the World AI Awards 2026 winners</a> -->
```
On /1st-edition/awards.html, below the H1:
```html
<p class="notice"><a href="/awards/winners-2025/">See the full list of World AI Awards 2025 winners</a></p>
```
Sitemap: add both URLs with `<lastmod>` and update lastmod each time rows change.

---

## Part D: redirects

These rules apply only to the new paths, so the non-www /awards URL that currently ranks is not touched.

### Apache (.htaccess at the web root)
```apache
RewriteEngine On

# 1) non-www to www, new winners paths only (skip if a site-wide host rule already exists)
RewriteCond %{HTTP_HOST} ^worldaisummit\.com$ [NC]
RewriteRule ^awards/winners-(2025|2026)(/.*)?$ https://www.worldaisummit.com/awards/winners-$1/ [R=301,L]

# 2) /index.html to folder URL (THE_REQUEST avoids a loop with DirectoryIndex)
RewriteCond %{THE_REQUEST} \s/awards/winners-(2025|2026)/index\.html[\s?] [NC]
RewriteRule ^ /awards/winners-%1/ [R=301,L]

# 3) missing trailing slash
RewriteRule ^awards/winners-(2025|2026)$ /awards/winners-$1/ [R=301,L]

# 4) short share link to the current year (302 so it can move each year)
RewriteRule ^awards/winners/?$ /awards/winners-2026/ [R=302,L]
```

### nginx
```nginx
# non-www server block (or wrap in: if ($host = worldaisummit.com) { ... } in a shared block)
location ~ ^/awards/winners-(2025|2026)(/.*)?$ {
    return 301 https://www.worldaisummit.com/awards/winners-$1/;
}

# www server block, server level (checks $request_uri, so the index directive cannot loop)
if ($request_uri ~ ^/awards/winners-(2025|2026)/index\.html) {
    return 301 /awards/winners-$1/;
}
location = /awards/winners-2025 { return 301 /awards/winners-2025/; }
location = /awards/winners-2026 { return 301 /awards/winners-2026/; }
location ~ ^/awards/winners/?$  { return 302 /awards/winners-2026/; }
location /awards/ { try_files $uri $uri/ =404; }
```
Before 15 Oct, point the 302 at /awards/winners-2025/ and switch it to 2026 after the ceremony.

---

## Sources
- Award groups and the 96 titles: https://www.worldaisummit.com/1st-edition/awards.html (fetched via Exa, 1 Oct 2026).
- Venue address: Marriott page https://www.marriott.com/en-us/hotels/blrgs-sheraton-grand-bangalore-hotel-at-brigade-gateway/ (rooms page footer) and Apple Maps: "26/1 Dr. Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru, Karnataka 560055".
- Geo coordinates 13.01247, 77.55484: Google Places data via Exa.
- 2025 winners: Elets LinkedIn post of 10 Oct 2025, the qualitrix.com release of 29 Sep 2025, and a winner's LinkedIn post of 27 Sep 2025. All three are from the verifier's notes.
