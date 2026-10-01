# A72: World AI Summit 2025 archive (/1st-edition/): titles, meta, archive banner, recap, closed-pass block, 301 redirects and sitemap fix

- **For recommendation:** Fix the /1st-edition/ archive now: stop selling 2025 passes, add a 2025 recap and winners, give each page a unique archive title, fix the 302s in the sitemap
- **Research lens:** event-week-postevent
- **Format:** Plain text with ready-to-paste HTML head tags, HTML/CSS blocks, Apache .htaccess and nginx redirect rules, and a sitemap deletion list
- **Placeholders the business must fill:**
  - PLACEHOLDER_2025_SESSION_VIDEOS_URL - link to the 2025 session videos (YouTube playlist or gallery); delete the list item if none exists
  - PLACEHOLDER_2025_WINNERS_LIST - World AI Awards 2025 winners, one <li> per category (Category: Winner), from internal jury records only

## How to ship

Owner: web dev (blocks 1, 2, 4, 6, 7) and content (blocks 3, 5). The site is static HTML, so each /1st-edition/ file is edited by hand.

Order and deadlines:
1) By 5 Oct: block 4 (delete the pass cards on /1st-edition/delegate-pass.html and add the closed-pass notice) and block 2 (the banner on every /1st-edition/ page). Deploy these two together.
2) By 12 Oct: block 1 (titles and descriptions, and removing "Register now" buttons), block 6 (find the rule that makes the existing 302s and change it to the 301 rules in the Apache or nginx version, whichever the server runs), block 7 (delete the 4 sitemap entries), and block 3 (the recap).
3) Block 5 (winners), when the 2025 winners list arrives from internal records. Then switch awards.html to the "Categories and Winners" title and description.

Checks after deploy:
- Run the curl check in block 6 on all four URLs, with and without .html. Each should show one 301 to /1st-edition/, and that URL should return 200.
- View the source of 3 or 4 archive pages to confirm the new title, the description and the banner.
- Run a small OpenSEO re-crawl filtered to /1st-edition/. It should show no 302s, no duplicate "World AI Summit 2025" titles and no "Register now" descriptions.
- Search Console covers only the non-www property, so www /1st-edition/ traffic cannot be measured. Adding a Domain property for worldaisummit.com would make it measurable.

Deliberately left out:
- No Event JSON-LD on archive pages. Google shows event rich results only for upcoming events, and the 2026 Event markup (14-15 Oct 2026) belongs only on / and /delegate/. If any /1st-edition/ page already has Event markup with offers or 2026 dates, remove it.
- Do not rename /1st-edition/.

Open points:
- It is not verified whether the 2025 pass page could still take payments. The fetched text shows the price cards and the registration@ contact but no checkout link. Remove the cards either way.
- Outside this task but more urgent: the Standard tier on /delegate/ says "valid till 30 Sept 2026", which expired yesterday, and Google's snippet for /delegate/ still shows "Valid till 25th July 2025". Fix /delegate/ today, because the archive banner and the closed-pass block both send visitors there.

Placeholders: PLACEHOLDER_2025_SESSION_VIDEOS_URL (delete that list item if none is ready) and PLACEHOLDER_2025_WINNERS_LIST (internal jury records only).

## Content

WORLD AI SUMMIT 2025 ARCHIVE (/1st-edition/): READY-TO-PASTE FIXES
Built on 1 Oct 2026 from OpenSEO audit c1b16b55 (20 /1st-edition/ rows: 11 www URLs return 200 and are in the sitemap, 4 www URLs return 302 and are in the sitemap, 5 non-www URLs return 301 to www; the crawl stopped at 100 pages) and from today's page fetches.

============================================================
1. TITLES AND META DESCRIPTIONS
============================================================
Replace the existing <title> and <meta name="description"> in each page's <head>.
Today, 8 pages share the title "World AI Summit 2025". Three pages (/1st-edition/, delegate-pass.html, giveaway.html) use the "World AI Summit 2025 by Elets Technomedia ... Register now & be part of the revolution" description. All three are replaced below.

/1st-edition/  (index.html)
<title>World AI Summit 2025 (Archive) | Bengaluru, 25-26 Sep 2025</title>
<meta name="description" content="Archive of World AI Summit 2025 in Bengaluru (25-26 Sep 2025): theme, speakers, agenda and award winners. World AI Summit 2026 runs 14-15 Oct 2026.">

/1st-edition/world-ai-agenda.html
<title>World AI Summit 2025 Agenda (Archive) | Bengaluru</title>
<meta name="description" content="Agenda archive of World AI Summit 2025 (25-26 Sep 2025, Bengaluru). World AI Summit 2026 takes place on 14-15 Oct 2026 at Sheraton Grand Bangalore.">

/1st-edition/awards.html
Today the page lists categories and past jury members but no winners. Use this title and description until the winners section (block 5) is live:
<title>World AI Awards 2025 Categories (Archive) | World AI Summit</title>
<meta name="description" content="World AI Awards 2025 categories across enterprise AI, governance, startups and AI leadership, from World AI Summit 2025 in Bengaluru (25-26 Sep 2025).">
Once the winners are published, switch to:
<title>World AI Awards 2025: Categories and Winners | World AI Summit</title>
<meta name="description" content="World AI Awards 2025 winners and categories across enterprise AI, governance, startups and AI leadership, from World AI Summit 2025 in Bengaluru.">

/1st-edition/speakers.html
<title>World AI Summit 2025 Speakers (Archive) | Bengaluru</title>
<meta name="description" content="Speakers at World AI Summit 2025 in Bengaluru (25-26 Sep 2025). For the World AI Summit 2026 line-up on 14-15 Oct 2026, see the 2026 speakers page.">

/1st-edition/delegate-pass.html
<title>World AI Summit 2025 Passes (Closed) | See 2026 Passes</title>
<meta name="description" content="Passes for World AI Summit 2025 (25-26 Sep 2025) are closed. World AI Summit 2026 takes place on 14-15 Oct 2026 in Bengaluru. See 2026 delegate passes.">

/1st-edition/faqs.html
<title>World AI Summit 2025 FAQs (Archive)</title>
<meta name="description" content="Archived FAQs for World AI Summit 2025 (25-26 Sep 2025, Bengaluru). For World AI Summit 2026 on 14-15 Oct 2026, write to registration@worldaisummit.com.">

/1st-edition/blogs.html
<title>World AI Summit 2025 Blog (Archive)</title>
<meta name="description" content="Articles published ahead of World AI Summit 2025 in Bengaluru (25-26 Sep 2025). Articles about World AI Summit 2026 are on the main blog.">

/1st-edition/partnership.html
<title>World AI Summit 2025 Partners (Archive)</title>
<meta name="description" content="Partnership archive for World AI Summit 2025 in Bengaluru (25-26 Sep 2025). For 2026 sponsorship and exhibition, write to partnerships@worldaisummit.com.">

/1st-edition/partner-benefits.html
<title>World AI Summit 2025 Partner Benefits (Archive)</title>
<meta name="description" content="Partner benefits offered at World AI Summit 2025 (archive). For 2026 sponsorship and exhibition options, write to partnerships@worldaisummit.com.">

/1st-edition/giveaway.html
<title>World AI Summit 2025 Giveaway (Archive)</title>
<meta name="description" content="Archive of the World AI Summit 2025 giveaway. World AI Summit 2026 takes place on 14-15 Oct 2026 at Sheraton Grand Bangalore, Brigade Gateway.">

Pages the audit found that were not in the original list:
/1st-edition/speaker-bio.html?name=...  (a template that is in the sitemap; it currently uses the title "World AI Summit 2025")
<title>World AI Summit 2025 Speaker Profile (Archive)</title>
<meta name="description" content="Speaker profile from World AI Summit 2025, held on 25-26 Sep 2025 in Bengaluru. Part of the 2025 archive.">
If the template can print the speaker's name on the server, use the title pattern "<Speaker name> | World AI Summit 2025 Speaker (Archive)".

/1st-edition/ai-dialogues.html and /1st-edition/startup-competition.html
The audit saw these only as non-www 301s because the crawl ended at 100 pages. Check their content before applying these titles:
<title>World AI Summit 2025 AI Dialogues (Archive)</title>
<title>World AI Summit 2025 Startup Competition (Archive)</title>

Remove "Register now" wording: on every /1st-edition/ page, change any "Register now", "Book now" or "Buy pass" button to the text "See 2026 passes" and point it to /delegate/. Change any 2025 nomination link to /awards/.

============================================================
2. ARCHIVE BANNER (every /1st-edition/ page)
============================================================
Paste the CSS once into each page's <head>, or into the shared stylesheet:

<style>
.archive-banner{display:block;background:#fff4d6;color:#3d2f00;border-bottom:1px solid #e3c467;padding:10px 16px;font-size:15px;line-height:1.5;text-align:center}
.archive-banner a{color:#0a4a94;font-weight:600;text-decoration:underline}
.archive-banner a:focus-visible{outline:2px solid #0a4a94;outline-offset:2px}
</style>

Paste the HTML as the first element after <body>, above the site header. If the header is fixed or sticky, add top margin so the header does not cover the banner.

<div class="archive-banner" role="note">You are viewing the 2025 archive. <a href="/">World AI Summit 2026</a> takes place on 14-15 October 2026 at Sheraton Grand Bangalore, Brigade Gateway. <a href="/delegate/">Get your 2026 pass</a></div>

============================================================
3. 2025 RECAP BLOCK (/1st-edition/, directly below the existing H1)
============================================================
Every fact in this block is sourced (see SOURCES). If no video URL is ready, delete the videos <li>. Do not link to #winners until block 5 is live.

<section class="archive-recap" aria-labelledby="recap-2025-title">
  <h2 id="recap-2025-title">World AI Summit 2025 at a glance</h2>
  <p>World AI Summit 2025 took place on 25-26 September 2025 at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru, under the theme "AI for All: Powering India's Inclusive and Responsible AI Future".</p>
  <p>The summit was organised by Elets Technomedia, with the Department of Electronics, IT, Biotechnology and Science &amp; Technology, Government of Karnataka, as Host Partner and the Karnataka Digital Economy Mission (KDEM) as Strategic Partner.</p>
  <p>According to the organiser's closing release, the summit brought together over 150 global speakers and 1,000+ key stakeholders, including AI innovators, industry leaders, policy-makers and technology pioneers (<a href="https://cio.eletsonline.com/press-release/world-ai-summit-2025-concludes-successfully-in-bengaluru-showcasing-indias-ai-leadership/75237/" rel="noopener">Elets CIO, 29 September 2025</a>).</p>
  <ul>
    <li><a href="PLACEHOLDER_2025_SESSION_VIDEOS_URL">Watch 2025 session videos</a></li>
    <li><a href="/1st-edition/awards.html#winners">World AI Awards 2025 winners</a></li>
    <li><a href="/1st-edition/speakers.html">2025 speakers</a></li>
    <li><a href="/1st-edition/world-ai-agenda.html">2025 agenda</a></li>
  </ul>
  <p>The next edition, World AI Summit 2026, takes place on 14-15 October 2026 at the same venue. <a href="/">See World AI Summit 2026</a> or <a href="/delegate/">get your 2026 pass</a>.</p>
</section>

Optional: the hero copy below this block is still written in the future tense ("will convene", "will be a launchpad"). Change it to the past tense when convenient.

============================================================
4. CLOSED-PASS BLOCK (/1st-edition/delegate-pass.html)
============================================================
Delete both pass cards (Rs 30,000 and Rs 60,000) and any buy or register button. Those prices are the same as the 2026 Late Access prices, so visitors could take them as current. Paste this block where the cards were, and use its heading as the page's only H1. Keep the URL returning 200 and leave it indexable.

<section class="archive-closed" aria-labelledby="passes-closed-title">
  <h1 id="passes-closed-title">Passes for World AI Summit 2025 are closed</h1>
  <p>World AI Summit 2025 took place on 25-26 September 2025 in Bengaluru. This page is kept as part of the 2025 archive, and passes for that edition are no longer on sale.</p>
  <p>World AI Summit 2026 takes place on 14-15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, 26/1 Dr. Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru, Karnataka 560055.</p>
  <p><a class="archive-cta" href="/delegate/">See 2026 delegate passes</a></p>
  <p>For group bookings or questions about passes, write to <a href="mailto:registration@worldaisummit.com">registration@worldaisummit.com</a>.</p>
</section>

============================================================
5. WINNERS SECTION (/1st-edition/awards.html, above "Award Categories")
============================================================
<section id="winners" aria-labelledby="winners-2025-title">
  <h2 id="winners-2025-title">World AI Awards 2025 winners</h2>
  <p>Winners of the World AI Awards 2025, announced at World AI Summit 2025 in Bengaluru (25-26 September 2025).</p>
  <ul>
    PLACEHOLDER_2025_WINNERS_LIST  <!-- one <li> per award: Category: Winner (organisation or person). Take this from internal jury records only. -->
  </ul>
</section>

If awards.html still links to a 2025 nomination form or to the 2025 checkout at elets.net/worldaisummit-awards/, point that link to /awards/ instead.

============================================================
6. REDIRECTS: CHANGE THE FOUR 302s TO SINGLE-HOP 301s
============================================================
Audit c1b16b55 found these four URLs, all listed in the sitemap:
/1st-edition/thematic-tracks  -> 302 to /1st-edition/
/1st-edition/what-to-expect-world-ai-summit-2025-agenda-highlights  -> 302 to /1st-edition (no trailing slash, so a second hop follows)
/1st-edition/why-attend-the-world-ai-summit-2025-in-bengaluru-7-straightforward-reasons-to-show-up  -> 302 to /1st-edition/
/1st-edition/world-ai-summit-2025-bengaluru-to-host-the-most-futuristic-and-deep-tech-ai-confluence  -> 302 to /1st-edition (no trailing slash)
Today, the .html versions of the three blog slugs serve the same content as /1st-edition/, so the rules below send them to the same place.
All of them go to /1st-edition/, which will carry the 2025 recap. That page is the closest archive equivalent because the original posts no longer exist.

These 302s are created somewhere already: a "Redirect" line with no status code, a RewriteRule with [R] or [R=302], or a rule in the hosting panel. Find that rule and edit or delete it first. Otherwise it may run before the new rule.

Apache (.htaccess in the web root; place above other rules that match these paths and above the non-www to www rule):

RewriteEngine On
RewriteRule ^1st-edition/thematic-tracks/?$ https://www.worldaisummit.com/1st-edition/ [R=301,L]
RewriteRule ^1st-edition/what-to-expect-world-ai-summit-2025-agenda-highlights(\.html)?/?$ https://www.worldaisummit.com/1st-edition/ [R=301,L]
RewriteRule ^1st-edition/why-attend-the-world-ai-summit-2025-in-bengaluru-7-straightforward-reasons-to-show-up(\.html)?/?$ https://www.worldaisummit.com/1st-edition/ [R=301,L]
RewriteRule ^1st-edition/world-ai-summit-2025-bengaluru-to-host-the-most-futuristic-and-deep-tech-ai-confluence(\.html)?/?$ https://www.worldaisummit.com/1st-edition/ [R=301,L]
RewriteRule ^1st-edition$ https://www.worldaisummit.com/1st-edition/ [R=301,L]

(If the .htaccess file sits inside /1st-edition/, remove "1st-edition/" from each pattern and change the last rule's pattern to ^$.)

nginx (add to the server blocks for www.worldaisummit.com and worldaisummit.com, before other location blocks; a "location ^~ /1st-edition/" block would override these regex rules):

location = /1st-edition { return 301 https://www.worldaisummit.com/1st-edition/; }
location ~ ^/1st-edition/thematic-tracks/?$ { return 301 https://www.worldaisummit.com/1st-edition/; }
location ~ ^/1st-edition/(what-to-expect-world-ai-summit-2025-agenda-highlights|why-attend-the-world-ai-summit-2025-in-bengaluru-7-straightforward-reasons-to-show-up|world-ai-summit-2025-bengaluru-to-host-the-most-futuristic-and-deep-tech-ai-confluence)(\.html)?/?$ { return 301 https://www.worldaisummit.com/1st-edition/; }

Check (each URL should give one 301 to https://www.worldaisummit.com/1st-edition/, and that URL should return 200):
curl -sI https://www.worldaisummit.com/1st-edition/thematic-tracks | grep -iE '^(HTTP|location)'

============================================================
7. SITEMAP (https://www.worldaisummit.com/sitemap.xml)
============================================================
Delete the whole <url>...</url> entry that contains each of these <loc> values. A sitemap should list only URLs that return 200. Do this as well as adding the 301s.
<loc>https://www.worldaisummit.com/1st-edition/thematic-tracks</loc>
<loc>https://www.worldaisummit.com/1st-edition/what-to-expect-world-ai-summit-2025-agenda-highlights</loc>
<loc>https://www.worldaisummit.com/1st-edition/why-attend-the-world-ai-summit-2025-in-bengaluru-7-straightforward-reasons-to-show-up</loc>
<loc>https://www.worldaisummit.com/1st-edition/world-ai-summit-2025-bengaluru-to-host-the-most-futuristic-and-deep-tech-ai-confluence</loc>
Keep the 11 /1st-edition/ URLs that return 200. If the sitemap uses <lastmod>, set it to the deploy date for each archive page you edit.

Related: /1st-edition/blogs.html lists 9 post titles, and their posts now lead back to /1st-edition/. Either restore the posts from a backup or remove the links from the titles.

============================================================
SOURCES
============================================================
- OpenSEO audit c1b16b55 (get_audit_pages, urlContains=1st-edition, 1 Oct 2026): status codes, redirect targets, sitemap flags, current titles and descriptions. https://app.openseo.so/p/eb76fdff-f482-423c-9a6d-08afeccaa111/audit?auditId=c1b16b55-baaa-4f13-9d3a-16bd61e341a2
- Elets CIO, "World AI Summit 2025 Concludes Successfully in Bengaluru, Showcasing India's AI Leadership", 29 Sep 2025: ended 26 Sep 2025, over 150 global speakers, 1,000+ key stakeholders. https://cio.eletsonline.com/press-release/world-ai-summit-2025-concludes-successfully-in-bengaluru-showcasing-indias-ai-leadership/75237/
- Elets CIO kick-off release, 24 Sep 2025 (Day 1 on 25 Sep, Day 2 on 26 Sep 2025). https://cio.eletsonline.com/press-release/world-ai-summit-2025-kicks-off-in-bengaluru-tomorrow-bringing-together-global-ai-leaders-and-innovator/75231/
- https://www.worldaisummit.com/1st-edition/ : theme, Host Partner (Dept of Electronics, IT, BT and S&T, Govt of Karnataka) and Strategic Partner (KDEM).
- https://www.worldaisummit.com/1st-edition/awards.html : 25-26 Sep 2025 dates, category list, no winners shown (fetched 1 Oct 2026).
- https://www.worldaisummit.com/1st-edition/delegate-pass.html : Rs 30,000 and Rs 60,000 cards, no checkout link in the fetched text.
- Venue address: 26/1 Dr. Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru, Karnataka 560055. https://www.marriott.com/en-us/hotels/blrgs-sheraton-grand-bangalore-hotel-at-brigade-gateway/overview/ and https://www.hotelplanner.com/Hotels/178731/Reservations-Sheraton-Bangalore-Hotel-at-Brigade-Gateway-Bangalore-26-1-Dr-Rajkumar-Rd-Malleswaram-Rajajinagar-560055
