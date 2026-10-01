# A21: World AI Awards 2026: /awards/ title, meta, facts block, FAQ, JSON-LD, winners section and a one-hop www redirect

- **For recommendation:** Awards: /awards/ is the only non-brand page earning Search Console clicks; add the missing facts and CTR copy now, then post the winners on the same URL
- **Research lens:** demand-sweep
- **Format:** HTML snippets (head, body sections, two JSON-LD blocks, both checked as valid JSON), Apache .htaccess and nginx redirect rules, sitemap entry, homepage link snippets, and a plain-text email to winners
- **Placeholders the business must fill:**
  - PLACEHOLDER_AWARDS_SCOPE
  - PLACEHOLDER_NOMINATION_DEADLINE
  - PLACEHOLDER_CEREMONY_DATE_TIME
  - PLACEHOLDER_CEREMONY_DATE
  - PLACEHOLDER_CEREMONY_DATE_SHORT
  - PLACEHOLDER_ELIGIBILITY
  - PLACEHOLDER_SELF_NOMINATION_RULE
  - PLACEHOLDER_CATEGORY_COUNT
  - PLACEHOLDER_CATEGORY_LIST
  - PLACEHOLDER_CATEGORY_1..N and PLACEHOLDER_CATEGORY_1..N_ONE_LINE_DESCRIPTION
  - PLACEHOLDER_2026_FEE_PER_ENTRY
  - PLACEHOLDER_PAYMENT_STEP
  - PLACEHOLDER_PAYMENT_METHOD
  - PLACEHOLDER_JURY
  - PLACEHOLDER_JURY_PROCESS
  - PLACEHOLDER_SHORTLIST_DATE
  - PLACEHOLDER_AWARDS_IMAGE_URL
  - PLACEHOLDER_CURRENT_DELEGATE_PASS_PRICE_INR
  - PLACEHOLDER_WINNER_1..N
  - PLACEHOLDER_ORGANISATION_1..N
  - PLACEHOLDER_2027_NOMINATIONS_LINE
  - PLACEHOLDER_WINNER_NAME
  - PLACEHOLDER_CATEGORY
  - PLACEHOLDER_SENDER_NAME
  - PLACEHOLDER_PUBLISH_DATE_YYYY-MM-DD

## How to ship

Owners: the Elets awards team fills the business placeholders; content or web dev pastes the snippets; whoever runs the server or DNS handles section 12.

1) By 2 Oct: the awards team sends the 2026 sectors (exactly as they appear in the "Select Sectors" dropdown), fee per entry, deadline, eligibility, jury, payment step and ceremony slot. If the deadline has passed, use meta C and the "nominations closed" line.

2) By 3 Oct: web dev publishes sections 1 to 9 on https://www.worldaisummit.com/awards/. The form stays where it is, below "How to nominate". Use meta A only if categories, fee and deadline all show on the page; otherwise use meta B. Remove any 2025 or September text. Check the JSON-LD in the Rich Results Test and the Schema Markup Validator (both free).
   - Google has shown FAQ rich results only for well-known government and health sites since 2023, so the FAQ's value is the text on the page, not a rich result.
   - Do not publish the 2025 fees as 2026 fees.

3) Today, in parallel: section 12.
   - Make the redirect one hop, put the self-canonical and sitemap entry in place, and add the Domain or www property in Search Console.
   - The two-hop chain is my inference and not verified. Direct curl from this sandbox was blocked (proxy 403), so run the four curl checks after deploying.
   - The site may already set its redirect at a CDN or hosting panel rather than .htaccess or nginx. If so, add the /awards rule there, ahead of the general www rule.

4) 15-16 Oct: swap the form block for section 10, update the title and meta, and send the section 11 email to each winner.

Expectations:
- Baseline is about 19-20 clicks per 17 days (32 clicks from 31 Aug to 28 Sep). Impressions are rising.
- About 57 of the 79 clicks come from anonymised long-tail queries.
- Many "world ai awards" searchers want worldawards.ai, a different brand; the disambiguation line is there for them.
- Visitors from the USA, UAE and UK are unlikely to pay for an Indian nomination, so judge success by paid nominations, not clicks.
- Expect some churn in rankings and snippets when Google moves to www during the event window.

Sources:
- Venue address: [Marriott hotel page](https://www.marriott.com/en-us/hotels/blrgs-sheraton-grand-bangalore-hotel-at-brigade-gateway/overview/) and [HotelPlanner](https://www.hotelplanner.com/Hotels/178731/Reservations-Sheraton-Bangalore-Hotel-at-Brigade-Gateway-Bangalore-26-1-Dr-Rajkumar-Rd-Malleswaram-Rajajinagar-560055) (26/1 Dr Rajkumar Road, Malleswaram-Rajajinagar, 560055).
- Live form fields, current title and the secretariat@ contact: Exa fetch of https://www.worldaisummit.com/awards/ on 1 Oct 2026.
- 2025 fees and categories: elets.net/worldaisummit-awards/ (verifier).
- Search Console and URL Inspection facts: verifier, 1 Oct.
- No OpenSEO paid tools were used. No files were edited.

On the question in the triggering message ("do you have more CPUs from computer?"): this sandbox reports 4 CPUs (nproc). It cannot use CPUs from your own computer.

## Content

=== 0. EDITOR NOTES (internal, do not publish) ===
- 2025 reference only. Do not put these on the page as 2026 facts. Source: elets.net/worldaisummit-awards/ (page still titled "Elets World AI Summit 2025", still live):
  Fee: Rs 18,000 + GST per entry (Startup and Individual categories); Rs 20,000 + GST per entry (Enterprise, Government, Leadership, Solution Provider).
  Categories: AI in Enterprises; Business Transformation & Innovation; AI in Governance; AI Startups; AI Leadership; SmartTech AI Awards.
  The 2026 fee, categories and deadline are not published anywhere (checked with WebSearch and Exa). The awards team must supply them.
- The live /awards/ form already has a "Select Sectors" dropdown. PLACEHOLDER_CATEGORY_LIST must match those options word for word.
- Before publishing, search the page source for "2025" and "September" and remove any text left over from last year. Exa's cached copy of non-www /awards still showed "25-26 September 2025".
- If nominations have closed by the time this goes live, use meta variant C and the "nominations closed" line in section 2.

=== 1. <head> (replace the current title "World AI Awards 2026 | Celebrating AI Excellence") ===
<title>World AI Awards 2026 | AI Awards India, Bengaluru, 14-15 Oct</title>
<meta name="description" content="Nominate for the World AI Awards 2026, presented at World AI Summit, Bengaluru (14-15 Oct). Categories, nomination fee, deadline and how to apply.">
<link rel="canonical" href="https://www.worldaisummit.com/awards/">
<meta property="og:title" content="World AI Awards 2026 | AI Awards India, Bengaluru, 14-15 Oct">
<meta property="og:description" content="Nominate for the World AI Awards 2026, presented at World AI Summit, Bengaluru (14-15 Oct). Categories, nomination fee, deadline and how to apply.">
<meta property="og:url" content="https://www.worldaisummit.com/awards/">
<meta property="og:type" content="website">

Title length: 60 characters. Meta A: 146 characters. Use meta A only if the page shows the categories, fee and deadline.
Meta B (148 chars). Use it if the fee or categories are not confirmed by 3 Oct:
"Nominate for the World AI Awards 2026, presented at World AI Summit, Bengaluru (14-15 Oct). Sectors, who can apply, process and the nomination form."
Meta C (135 chars). Use it if nominations have closed:
"World AI Awards 2026 nominations are closed. Winners are announced at World AI Summit, Bengaluru (14-15 Oct). Ceremony details and FAQ."

=== 2. TOP OF PAGE (H1 and intro; the summit theme moves from H1 to a normal line) ===
<p class="eyebrow">AI for All: Accelerating India's Journey Towards Inclusive, Responsible and Future-Ready AI</p>
<h1>World AI Awards 2026</h1>
<p>The World AI Awards 2026 are presented at World AI Summit 2026, organised by Elets Technomedia, on 14-15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. The awards recognise PLACEHOLDER_AWARDS_SCOPE.</p>
<p>Nominations are open until PLACEHOLDER_NOMINATION_DEADLINE. <a href="#nominate">Go to the nomination form</a>.</p>
<!-- If nominations have closed, use this line instead: <p>Nominations for 2026 are now closed. Winners will be announced at the ceremony on PLACEHOLDER_CEREMONY_DATE_TIME.</p> -->
<p class="note">These awards are presented at World AI Summit, Bengaluru, and organised by Elets Technomedia. They are not connected with other awards programmes that use a similar name.</p>

=== 3. KEY FACTS BLOCK ===
<h2>World AI Awards 2026 at a glance</h2>
<table class="facts">
  <tr><th scope="row">Presented at</th><td>World AI Summit 2026, Bengaluru</td></tr>
  <tr><th scope="row">Summit dates</th><td>14-15 October 2026</td></tr>
  <tr><th scope="row">Awards ceremony</th><td>PLACEHOLDER_CEREMONY_DATE_TIME</td></tr>
  <tr><th scope="row">Venue</th><td>Sheraton Grand Bangalore Hotel at Brigade Gateway, 26/1 Dr Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru 560055</td></tr>
  <tr><th scope="row">Who can nominate</th><td>PLACEHOLDER_ELIGIBILITY</td></tr>
  <tr><th scope="row">Categories</th><td>PLACEHOLDER_CATEGORY_COUNT sectors (<a href="#categories">see the list</a>)</td></tr>
  <tr><th scope="row">Nomination fee</th><td>PLACEHOLDER_2026_FEE_PER_ENTRY + GST per entry</td></tr>
  <tr><th scope="row">Nomination deadline</th><td>PLACEHOLDER_NOMINATION_DEADLINE</td></tr>
  <tr><th scope="row">Jury</th><td>PLACEHOLDER_JURY</td></tr>
  <tr><th scope="row">Organiser</th><td>Elets Technomedia</td></tr>
  <tr><th scope="row">Questions</th><td><a href="mailto:secretariat@worldaisummit.com">secretariat@worldaisummit.com</a></td></tr>
</table>

=== 4. CATEGORIES ===
<h2 id="categories">2026 award categories</h2>
<p>Each nomination is entered under one sector. Choose your sector in the nomination form below.</p>
<ul>
  <li>PLACEHOLDER_CATEGORY_1: PLACEHOLDER_CATEGORY_1_ONE_LINE_DESCRIPTION</li>
  <li>PLACEHOLDER_CATEGORY_2: PLACEHOLDER_CATEGORY_2_ONE_LINE_DESCRIPTION</li>
  <li>PLACEHOLDER_CATEGORY_N: PLACEHOLDER_CATEGORY_N_ONE_LINE_DESCRIPTION</li>
</ul>
<!-- The list must match the "Select Sectors" dropdown options exactly. -->

=== 5. HOW TO NOMINATE (steps follow the live form fields) ===
<h2 id="nominate">How to nominate</h2>
<ol>
  <li>Select the sector for your entry.</li>
  <li>Add the project or innovation details: the project's duration (MM/YYYY to MM/YYYY), a brief overview, the problem it solves and who benefits, how you have scaled it or plan to scale it, the approximate budget or investment, and the key stakeholders and technology partners.</li>
  <li>Add the applicant's details.</li>
  <li>Upload supporting documents.</li>
  <li>Pay the nomination fee: PLACEHOLDER_PAYMENT_STEP.</li>
  <li>The jury reviews entries: PLACEHOLDER_JURY_PROCESS. Shortlisted nominees are informed by PLACEHOLDER_SHORTLIST_DATE.</li>
</ol>
<!-- Keep the existing nomination form directly below this list. -->

=== 6. FAQ (visible on the page; section 8 carries the same text as JSON-LD) ===
<h2>World AI Awards 2026: frequently asked questions</h2>

<h3>Who can nominate for the World AI Awards 2026?</h3>
<p>PLACEHOLDER_ELIGIBILITY. PLACEHOLDER_SELF_NOMINATION_RULE. Each nomination form covers one sector, so submit a separate form for each sector you wish to enter.</p>

<h3>What are the 2026 award categories?</h3>
<p>Entries are made under PLACEHOLDER_CATEGORY_COUNT sectors: PLACEHOLDER_CATEGORY_LIST. Select the sector in the nomination form on this page.</p>

<h3>What is the nomination fee and deadline?</h3>
<p>The nomination fee is PLACEHOLDER_2026_FEE_PER_ENTRY plus GST per entry. Nominations close on PLACEHOLDER_NOMINATION_DEADLINE. PLACEHOLDER_PAYMENT_METHOD.</p>

<h3>When and where are the winners announced?</h3>
<p>Winners are announced at the World AI Awards 2026 ceremony on PLACEHOLDER_CEREMONY_DATE_TIME, during World AI Summit 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. The full list of winners will be published on this page after the ceremony.</p>

=== 7. EVENT JSON-LD (in <head>; checked as valid JSON) ===
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Place",
      "@id": "https://www.worldaisummit.com/#venue",
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
    {
      "@type": "Organization",
      "@id": "https://www.worldaisummit.com/#organizer",
      "name": "Elets Technomedia",
      "url": "https://eletsonline.com/"
    },
    {
      "@type": "Event",
      "@id": "https://www.worldaisummit.com/awards/#event",
      "name": "World AI Awards 2026",
      "description": "World AI Awards 2026, presented at World AI Summit 2026 in Bengaluru on 14-15 October 2026. Organised by Elets Technomedia.",
      "url": "https://www.worldaisummit.com/awards/",
      "image": "PLACEHOLDER_AWARDS_IMAGE_URL",
      "startDate": "2026-10-14",
      "endDate": "2026-10-15",
      "eventStatus": "https://schema.org/EventScheduled",
      "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
      "location": { "@id": "https://www.worldaisummit.com/#venue" },
      "organizer": { "@id": "https://www.worldaisummit.com/#organizer" },
      "offers": {
        "@type": "Offer",
        "url": "https://www.worldaisummit.com/delegate/",
        "price": "PLACEHOLDER_CURRENT_DELEGATE_PASS_PRICE_INR",
        "priceCurrency": "INR",
        "availability": "https://schema.org/InStock"
      },
      "superEvent": {
        "@type": "Event",
        "name": "World AI Summit 2026",
        "url": "https://www.worldaisummit.com/",
        "startDate": "2026-10-14",
        "endDate": "2026-10-15",
        "eventStatus": "https://schema.org/EventScheduled",
        "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
        "location": { "@id": "https://www.worldaisummit.com/#venue" },
        "organizer": { "@id": "https://www.worldaisummit.com/#organizer" }
      }
    }
  ]
}
</script>
<!-- "performer" is left out on purpose. No awards jury or presenter is verified. Add one only for a confirmed name.
     "price" must be a plain number such as "30000", with no symbol or commas. If the homepage already marks up the summit with an @id, use that @id in superEvent. -->

=== 8. FAQPAGE JSON-LD (in <head>; checked as valid JSON; the text must match section 6 word for word) ===
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Who can nominate for the World AI Awards 2026?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "PLACEHOLDER_ELIGIBILITY. PLACEHOLDER_SELF_NOMINATION_RULE. Each nomination form covers one sector, so submit a separate form for each sector you wish to enter."
      }
    },
    {
      "@type": "Question",
      "name": "What are the 2026 award categories?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Entries are made under PLACEHOLDER_CATEGORY_COUNT sectors: PLACEHOLDER_CATEGORY_LIST. Select the sector in the nomination form on this page."
      }
    },
    {
      "@type": "Question",
      "name": "What is the nomination fee and deadline?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The nomination fee is PLACEHOLDER_2026_FEE_PER_ENTRY plus GST per entry. Nominations close on PLACEHOLDER_NOMINATION_DEADLINE. PLACEHOLDER_PAYMENT_METHOD."
      }
    },
    {
      "@type": "Question",
      "name": "When and where are the winners announced?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Winners are announced at the World AI Awards 2026 ceremony on PLACEHOLDER_CEREMONY_DATE_TIME, during World AI Summit 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. The full list of winners will be published on this page after the ceremony."
      }
    }
  ]
}
</script>

=== 9. HOMEPAGE LINKS (link to the exact canonical form, with the trailing slash) ===
Nav item:  <a href="https://www.worldaisummit.com/awards/">World AI Awards 2026</a>
Hero, second button:  <a class="btn btn-secondary" href="https://www.worldaisummit.com/awards/">Nominate for the World AI Awards 2026</a>
Also change any link on /faqs (and on any other page) that points to worldaisummit.com/awards or /awards with no slash to https://www.worldaisummit.com/awards/.

=== 10. AFTER THE CEREMONY (late 15 Oct or 16 Oct; same URL; replace only the form block) ===
<title>World AI Awards 2026 Winners | AI Awards India, Bengaluru</title>   (57 chars)
<meta name="description" content="World AI Awards 2026 winners, presented at World AI Summit, Bengaluru on PLACEHOLDER_CEREMONY_DATE_SHORT. Full list of categories, winners and their organisations.">   (138 chars when the date is written as "15 Oct")

<h2 id="winners">World AI Awards 2026 winners</h2>
<p>The World AI Awards 2026 were presented on PLACEHOLDER_CEREMONY_DATE at World AI Summit 2026, Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. The winners are listed below by category.</p>
<table class="winners">
  <caption>World AI Awards 2026 winners by category</caption>
  <thead>
    <tr><th scope="col">Category</th><th scope="col">Winner</th><th scope="col">Organisation</th></tr>
  </thead>
  <tbody>
    <tr><td>PLACEHOLDER_CATEGORY_1</td><td>PLACEHOLDER_WINNER_1</td><td>PLACEHOLDER_ORGANISATION_1</td></tr>
    <tr><td>PLACEHOLDER_CATEGORY_2</td><td>PLACEHOLDER_WINNER_2</td><td>PLACEHOLDER_ORGANISATION_2</td></tr>
    <tr><td>PLACEHOLDER_CATEGORY_N</td><td>PLACEHOLDER_WINNER_N</td><td>PLACEHOLDER_ORGANISATION_N</td></tr>
  </tbody>
</table>
<p>PLACEHOLDER_2027_NOMINATIONS_LINE</p>
- Keep the H1, the key facts block (changed to past tense) and the FAQ below the table. Change the fee and deadline answer to "Nominations for 2026 are closed."
- Leave the Event JSON-LD as it is, with eventStatus EventScheduled. Do not delete the markup after the event.

=== 11. EMAIL TO EACH WINNER (plain text, sent 16 Oct) ===
Subject: World AI Awards 2026: your award is now listed

Dear PLACEHOLDER_WINNER_NAME,

Congratulations once again on winning the World AI Awards 2026 in the PLACEHOLDER_CATEGORY category at World AI Summit, Bengaluru.

The full list of winners is now published at:
https://www.worldaisummit.com/awards/

If you announce the award on your website, newsroom or LinkedIn, please link to the page above so readers can see the full list. The anchor text "World AI Awards 2026" works well.

Warm regards,
PLACEHOLDER_SENDER_NAME
World AI Awards Secretariat, Elets Technomedia
secretariat@worldaisummit.com

=== 12. STEP 5, CORRECTED: CANONICAL AND REDIRECT (change nothing else) ===
Situation: Google last crawled non-www /awards on 28 Sep 2026 and got a 200. It picked the non-www URL as canonical and shows it as "Submitted and indexed". The 301 to www appeared in the 1 Oct crawl, so Google has not yet moved to www. That will most likely happen during the event window, and short swings in ranking or snippets are normal then. Do not undo the redirect, and do not add noindex or change the URL.

12a. One hop from every variant to https://www.worldaisummit.com/awards/. The chain is probably two hops today (non-www /awards to www /awards to www /awards/). This has not been verified.

Apache (.htaccess in the document root; place this ABOVE the existing non-www to www rule):
RewriteEngine On
# /awards with no slash, on any host or scheme, goes straight to the final URL
RewriteCond %{HTTP_HOST} ^(www\.)?worldaisummit\.com$ [NC]
RewriteRule ^awards$ https://www.worldaisummit.com/awards/ [R=301,L]
# Existing general rule (keep only one copy): http or non-www goes to https://www
RewriteCond %{HTTP_HOST} ^worldaisummit\.com$ [NC,OR]
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://www.worldaisummit.com/$1 [R=301,L]
# Behind a CDN or load balancer, use RewriteCond %{HTTP:X-Forwarded-Proto} !https in place of %{HTTPS} off.

nginx (add the exact-match location to EVERY server block. If a non-www block uses a server-level "return 301 ...", move that return into "location /", because a server-level return runs before location matching):
server {
    listen 80;
    listen [::]:80;
    server_name worldaisummit.com www.worldaisummit.com;
    location = /awards { return 301 https://www.worldaisummit.com/awards/; }
    location / { return 301 https://www.worldaisummit.com$request_uri; }
}
server {
    listen 443 ssl;
    listen [::]:443 ssl;
    server_name worldaisummit.com;
    # existing ssl_certificate and ssl_certificate_key lines
    location = /awards { return 301 https://www.worldaisummit.com/awards/; }
    location / { return 301 https://www.worldaisummit.com$request_uri; }
}
# Inside the existing www (443) server block:
location = /awards { return 301 https://www.worldaisummit.com/awards/; }

Check (each command should show exactly one 301, then a 200 at https://www.worldaisummit.com/awards/):
curl -sIL https://worldaisummit.com/awards | grep -iE "^(HTTP|location)"
curl -sIL http://worldaisummit.com/awards | grep -iE "^(HTTP|location)"
curl -sIL https://www.worldaisummit.com/awards | grep -iE "^(HTTP|location)"
curl -sIL http://www.worldaisummit.com/awards/ | grep -iE "^(HTTP|location)"

12b. On www /awards/, a self-referencing canonical (already in section 1):
<link rel="canonical" href="https://www.worldaisummit.com/awards/">

12c. The sitemap entry must use the same URL:
<url>
  <loc>https://www.worldaisummit.com/awards/</loc>
  <lastmod>PLACEHOLDER_PUBLISH_DATE_YYYY-MM-DD</lastmod>
</url>

12d. Search Console, today. Add a Domain property for worldaisummit.com (DNS TXT verification); if DNS access is slow, add the URL-prefix property https://www.worldaisummit.com/ instead. Submit the sitemap there. Run the free URL Inspection on https://www.worldaisummit.com/awards/ and click Request indexing after the content and the redirect are live. Keep the old non-www property. Without the new property, /awards data disappears from view once Google moves to www.
