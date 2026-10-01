# A62: World AI Awards 2026 nomination CTA: homepage block, nav item, sitewide deadline banner, /awards/ deadline line, elets.net retirement copy and 301 rules

- **For recommendation:** Make the open nomination window and its deadline visible sitewide: change the homepage 'Previous edition' awards block to a live CTA, add internal links, and retire the 2025 elets.net checkout
- **Research lens:** awards
- **Format:** Paste-ready bundle: HTML snippets (static site), page copy for elets.net, Apache .htaccess and nginx redirect rules
- **Placeholders the business must fill:**
  - PLACEHOLDER_DEADLINE_DD - day in October 2026 when World AI Awards nominations close (must fall before 14 Oct)
  - PLACEHOLDER_DEADLINE_ISO - the same deadline as an ISO timestamp, e.g. 2026-10-DDT23:59:59+05:30, used by the banner to remove itself
  - PLACEHOLDER_CEREMONY_DATE - 14 or 15 October 2026 (the 2025 ceremony was on day 1)
  - PLACEHOLDER_2026_FEE - 2026 nomination fee per entry (2025 was INR 18,000 + GST Startup/Individual, INR 20,000 + GST others); show only once confirmed
  - PLACEHOLDER_AWARDS_CONTACT_EMAIL - inbox for people who already paid on elets.net (suggest secretariat@worldaisummit.com)
  - PLACEHOLDER_PAYMENT_ROUTE - Elets confirmation of how 2026 nomination fees are collected; the 301 waits for this

## How to ship

Owners: worldaisummit.com web dev (sections 1-4, about 1-2 hours) and the Elets web team (section 5, about 30 minutes). Target: 2 October 2026, so the banner runs for the whole remaining window.

1. Before anything goes live, get PLACEHOLDER_DEADLINE_DD, PLACEHOLDER_DEADLINE_ISO and PLACEHOLDER_CEREMONY_DATE from the awards team. The deadline has to fall before 14 October. The 2025 ceremony was on day 1. Do not publish any copy that still contains a PLACEHOLDER_ marker.

2. On worldaisummit.com, paste the homepage block (section 1) over the 'Previous edition' awards block. Add the nav item (section 2) to the shared header. Add the banner (section 3) to /delegate/, /ai-conference-bengaluru-2026.html, /speaker.html, /blog/ and the 5 blog posts. Add the deadline line (section 4) to /awards/. Do not add the banner to /awards/ itself. Adjust the class names to the site's existing button styles.

3. On elets.net, apply Option A today. Use Option B (the 301) only after the Elets team confirms how 2026 nomination fees are collected. The www /awards/ form shows no fee or checkout step, so payment may still run through Elets. A 301 sent before that is confirmed could break payments. Precedent: elets.net/worldaisummit-delegate/ already redirects to worldaisummit.com.

4. Check what Google is indexing. In Search Console (non-www property), run URL Inspection on https://worldaisummit.com/awards and look at the crawled page. If it still shows 2025 copy ('25-26 September 2025'), request indexing. Live www /awards/ reads 2026 and non-www /awards 301s to www. Do the same for the homepage after the block goes live.

5. Measurement. There is no current data on clicks from the homepage to /awards. The data-cta attributes are hooks for a click event if GA is present. Also add a Domain or www property in Search Console, because the www homepage is not measured today. Do not quote homepage traffic as larger than /awards until it is measured.

6. The day after the deadline, swap the homepage block to the post-deadline copy in section 1. The banner removes itself.

7. Keep competitor claims off the page. Keep 'at World AI Summit, Bengaluru' next to the awards name to separate it from the unrelated 'World AI Awards 2026' brand at worldawards.ai.

No JSON-LD is included: none is needed for a CTA block, and the Event schema is a separate deliverable. No OpenSEO credits were used; the only check was an Exa read of /1st-edition/awards.html and www /awards/ on 1 October 2026.

## Content

=====================================================================
WORLD AI AWARDS 2026: NOMINATION CTA BUNDLE (verified 1 Oct 2026)
=====================================================================
Changes after verification:
- "75+ awards" is removed. The only "75+" anywhere is an unlabelled stat on the 2025 archive page (/1st-edition/awards.html). No 2026 count is published.
- The secondary link now points to /1st-edition/awards.html (live, 2025 edition, lists 2025 categories). Its label is "See the 2025 award categories", not "winners", because that page lists categories and no winners. /awards/winners-2025/ does not exist.
- No fee appears in the homepage or banner copy. The 2025 fees were INR 18,000 + GST per entry (Startup and Individual) and INR 20,000 + GST per entry (Enterprise, Government, Leadership, Solution Provider). The 2026 fee is unpublished, so it stays PLACEHOLDER_2026_FEE.
- Venue and dates come from the live www /awards/ page: "14th - 15th October 2026 ... Sheraton Grand Bangalore Hotel at Brigade Gateway".

---------------------------------------------------------------------
1) HOMEPAGE BLOCK: https://www.worldaisummit.com/
   Replace the awards section that ends "World AI Awards · Previous edition".
   Keep the existing kicker line because Google already shows it in the homepage snippet.
---------------------------------------------------------------------
<section class="wais-awards-cta" id="world-ai-awards" aria-labelledby="wais-awards-h2">
  <p class="wais-awards-cta__kicker">Honouring the AI that's actually working</p>
  <h2 id="wais-awards-h2">World AI Awards 2026: nominations close PLACEHOLDER_DEADLINE_DD October</h2>
  <p>Recognising real-world AI across enterprises, startups, government and leadership. Winners are honoured on stage at World AI Summit 2026, Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru, on PLACEHOLDER_CEREMONY_DATE October 2026.</p>
  <p class="wais-awards-cta__actions">
    <a class="btn btn-primary" href="/awards/" data-cta="home-awards-nominate">Nominate now</a>
    <a class="wais-awards-cta__secondary" href="/1st-edition/awards.html" data-cta="home-awards-2025">See the 2025 award categories</a>
  </p>
</section>

Swap in this copy the day after nominations close (avoids stale deadline copy):
  H2: World AI Awards 2026: winners honoured on PLACEHOLDER_CEREMONY_DATE October
  Body: Recognising real-world AI across enterprises, startups, government and leadership, on stage at World AI Summit 2026, Bengaluru.
  Button: About the awards -> /awards/

---------------------------------------------------------------------
2) MAIN NAVIGATION: add on every page that uses the shared header
---------------------------------------------------------------------
<li><a href="/awards/">Awards</a></li>

---------------------------------------------------------------------
3) SITEWIDE DEADLINE BANNER
   Add to /delegate/, /ai-conference-bengaluru-2026.html, /speaker.html, /blog/ and the 5 blog posts.
   Place it directly after <body> or under the header. It removes itself after the deadline.
---------------------------------------------------------------------
<div class="wais-awards-banner" role="region" aria-label="World AI Awards 2026 nominations" data-expires="PLACEHOLDER_DEADLINE_ISO">
  <p><a href="/awards/">World AI Awards 2026</a>: nominations close PLACEHOLDER_DEADLINE_DD October. Winners honoured at World AI Summit, Bengaluru. <a class="wais-awards-banner__cta" href="/awards/" data-cta="banner-awards-nominate">Nominate now &rarr;</a></p>
</div>
<script>
(function () {
  var b = document.querySelector('.wais-awards-banner');
  if (!b) return;
  var t = Date.parse(b.getAttribute('data-expires'));
  if (!isNaN(t) && Date.now() > t) { b.parentNode.removeChild(b); }
})();
</script>
<style>
.wais-awards-banner{padding:10px 16px;text-align:center;font-size:15px;line-height:1.4;border-bottom:1px solid rgba(0,0,0,.12)}
.wais-awards-banner p{margin:0}
.wais-awards-banner a{font-weight:600;text-decoration:underline}
.wais-awards-banner__cta{white-space:nowrap;margin-left:6px}
</style>
(PLACEHOLDER_DEADLINE_ISO format: 2026-10-DDT23:59:59+05:30. If the date is not filled in, the banner simply stays visible.)

---------------------------------------------------------------------
4) /awards/ PAGE: deadline line above the "Select Sectors" form (no self-link)
---------------------------------------------------------------------
<p class="wais-awards-deadline"><strong>Nominations for the World AI Awards 2026 close on PLACEHOLDER_DEADLINE_DD October 2026.</strong> Winners are honoured at World AI Summit 2026, Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru, on PLACEHOLDER_CEREMONY_DATE October 2026.</p>
<!-- Optional, only once confirmed: -->
<p class="wais-awards-fee">Nomination fee: PLACEHOLDER_2026_FEE + GST per entry.</p>

---------------------------------------------------------------------
5) ELETS.NET: https://elets.net/worldaisummit-awards/
   OPTION A (do this now, until the 2026 payment flow is confirmed): update the page in place.
---------------------------------------------------------------------
Remove: the 2025 fee table (INR 18,000 / 20,000 + GST), the 2025 nomination form, and the checkout product "Conference Attendee Pass" (INR 30,000). Unpublish or disable the products themselves, not only the buttons.

<title>World AI Awards 2026 | World AI Summit, Bengaluru, 14-15 Oct 2026</title>
<meta name="description" content="Nominations for the World AI Awards 2026 are made on the official World AI Summit website. Winners are honoured at World AI Summit, Bengaluru, 14-15 October 2026.">
<link rel="canonical" href="https://www.worldaisummit.com/awards/">

H1: World AI Awards 2026 — World AI Summit, Bengaluru, 14-15 Oct 2026

Body:
Nominations for the World AI Awards 2026 are taken only on the official World AI Summit website.

Nominate on the official page: https://www.worldaisummit.com/awards/

World AI Summit 2026 takes place on 14-15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. Nominations close on PLACEHOLDER_DEADLINE_DD October 2026.

The 2025 nomination form and payment on this page are closed. If you have already paid here for a nomination, please write to PLACEHOLDER_AWARDS_CONTACT_EMAIL with your order number and we will confirm your entry.

Button: Nominate on worldaisummit.com -> https://www.worldaisummit.com/awards/

---------------------------------------------------------------------
   OPTION B (only after PLACEHOLDER_PAYMENT_ROUTE confirms the 2026 nomination payment does not run through this elets.net checkout): 301 the page.
   Use a server-side 301, not a JS redirect like elets.net/worldaisummit-delegate/ uses.
---------------------------------------------------------------------
Apache (.htaccess in the elets.net web root, ABOVE the "# BEGIN WordPress" block if present):

<IfModule mod_rewrite.c>
RewriteEngine On
RewriteRule ^worldaisummit-awards/?$ https://www.worldaisummit.com/awards/ [R=301,L]
</IfModule>

nginx (inside the elets.net server { } block, before any try_files / PHP location):

location = /worldaisummit-awards/ { return 301 https://www.worldaisummit.com/awards/; }
location = /worldaisummit-awards  { return 301 https://www.worldaisummit.com/awards/; }

Test after deploy:
curl -sI https://elets.net/worldaisummit-awards/ | grep -iE "^(HTTP|location)"
  expected: HTTP/... 301 and location: https://www.worldaisummit.com/awards/
curl -sI https://www.worldaisummit.com/awards/ | head -1
  expected: 200 (one hop, no chain)
