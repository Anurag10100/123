# A01: World AI Summit 2026: pass-path fixes (redirects, sitemap, /delegate/ H1, homepage links, 2025 banner, speaker CTA)

- **For recommendation:** 2. Close the dead ends in the pass path: send every register URL and CTA to /delegate/
- **Research lens:** cro-leads
- **Format:** Markdown with code blocks: Apache .htaccess, nginx and Cloudflare redirect variants, sitemap edit, HTML snippets, curl QA commands
- **Placeholders the business must fill:**
  - PLACEHOLDER_CURRENT_PASS_PRICE: the live delegate pass price from 1 Oct 2026. /delegate/ shows Standard Rs 20,000/35,000 valid till 30 Sept, then Late Access Rs 30,000/60,000, while the homepage and allevents.in still say Rs 20,000. The business must decide before any priced CTA ships.

## How to ship

1) Today (1-2 Oct): web dev finds where the current 302 is set (.htaccess, the cPanel Redirects screen, or Cloudflare/host), deletes it, and adds the 301 block from section 1a, 1b or 1c, whichever matches the stack. The block goes at the top of .htaccess, above the www/https rules. Run the curl checks in 1d. Each should return a single 301 to https://www.worldaisummit.com/delegate/ with the UTMs kept. I could not confirm the server type myself: direct requests to worldaisummit.com from this sandbox were blocked by the proxy (403), so the Apache assumption still needs checking. 2) Remove /registration and /registration.html from sitemap.xml and resubmit it. Add a www or Domain property in Search Console. 3) In GA4, find the source and medium of the September /delegate-registration.html traffic and repoint that mailer or ad to /delegate/. 4) Add the H1 to /delegate/. 5) Click through the homepage CTAs in a browser before changing them. Always add the text link (4a) and the FAQ link (4c). Repoint a button only if it currently goes nowhere. Watch homepage form_submit and /delegate/success.php views weekly, and undo the button changes if homepage submissions fall. 6) Paste the 2025 banner. 7) Ship the speaker CTA only after the business confirms the live pass price (PLACEHOLDER_CURRENT_PASS_PRICE). It is low traffic, so it can wait. No files in the repo were edited and no OpenSEO credits were spent. On the relayed question about more CPUs: this container has 4 CPUs (nproc) and cannot get more capacity from your computer.

## Content

WORLD AI SUMMIT 2026: PASS-PATH FIXES (rec 2)
Owner: web dev. Ship by: 2 Oct 2026.
Order of work: 1 Redirects, 2 Sitemap, 3 /delegate/ H1, 4 Homepage links (check in a browser first), 5 2025 banner, 6 Speaker CTA (lowest; needs a price decision first).

Why the redirects come first: /delegate-registration.html had 400 views from 312 users between 1 Jul and 30 Sep. All of them came in September, and only 12 sessions were organic. Engagement was about 7 s with 0 key events. A live link, probably a September mailer or ad, is sending people to a page that has no form. /registration and /registration.html are in sitemap.xml and send a 302 to https://worldaisummit.com/, which then sends a 301 to www. That is 2 hops to a page that is not the pass page.

====================================================================
1. REDIRECTS
====================================================================

STEP 0: Find and remove the existing 302 before adding anything.
It may be in .htaccess, in the cPanel "Redirects" screen (cPanel writes these into .htaccess), or at host or CDN level (for example Cloudflare Redirect Rules or Page Rules). Delete any line like these:

    Redirect 302 /registration https://worldaisummit.com/
    RedirectMatch 302 ^/registration ...
    RewriteCond %{HTTP_HOST} ^worldaisummit\.com$ [OR]
    RewriteCond %{HTTP_HOST} ^www\.worldaisummit\.com$
    RewriteRule ^registration(\.html)?$ "https\:\/\/worldaisummit\.com\/" [R=302,L]

If the 302 lives in the CDN or hosting panel, delete it there and create the 301 in that same panel (see 1c). If you don't, the server rule never runs.

--------------------------------------------------------------------
1a. Apache .htaccess
--------------------------------------------------------------------
Use the document root .htaccess shared by www and non-www. Put this block at the very top, above the http->https and non-www->www rules, so that non-www /registration also reaches www /delegate/ in one hop.

    # --- World AI Summit 2026: old registration URLs -> delegate pass page (301) ---
    RewriteEngine On
    RewriteRule ^registration(\.html)?/?$ https://www.worldaisummit.com/delegate/ [R=301,L,NC]
    RewriteRule ^delegate-registration\.html$ https://www.worldaisummit.com/delegate/ [R=301,L,NC]
    # --- end ---

Notes:
- The file needs only one "RewriteEngine On". If one already exists higher up, drop this one.
- The rules have no QSD flag, so UTM parameters on mailer and ad links pass through to /delegate/ and GA4 keeps the campaign.
- The old files (registration.html, delegate-registration.html) can stay on disk because the rule runs first.

--------------------------------------------------------------------
1b. nginx variant (use only if the server turns out to be nginx)
--------------------------------------------------------------------
Add these lines at server level in the server blocks for BOTH worldaisummit.com and www.worldaisummit.com (and the port-80 block if it is separate). Place them ABOVE any line like "return 301 https://www.worldaisummit.com$request_uri;". Server-level rewrite and return run in file order.

    rewrite ^/registration(\.html)?/?$ https://www.worldaisummit.com/delegate/ permanent;
    rewrite ^/delegate-registration\.html$ https://www.worldaisummit.com/delegate/ permanent;

Remove any old "location = /registration { return 302 ...; }". nginx keeps the original query string automatically. Then run: nginx -t && systemctl reload nginx

--------------------------------------------------------------------
1c. Cloudflare or CDN variant (use only if the 302 is configured there)
--------------------------------------------------------------------
Rules > Redirect Rules > Create rule (single redirect)
- Custom filter expression:
    (http.host in {"worldaisummit.com" "www.worldaisummit.com"} and http.request.uri.path in {"/registration" "/registration/" "/registration.html" "/delegate-registration.html"})
- Then: Static, URL https://www.worldaisummit.com/delegate/, Status code 301, Preserve query string ON.
- Delete the old 302 rule or Page Rule.

--------------------------------------------------------------------
1d. Check the result. Each line should show ONE 301 straight to the pass page.
--------------------------------------------------------------------
    curl -sI "https://www.worldaisummit.com/registration" | grep -iE "^HTTP|^location"
    curl -sI "https://worldaisummit.com/registration.html" | grep -iE "^HTTP|^location"
    curl -sI "https://www.worldaisummit.com/delegate-registration.html?utm_source=test" | grep -iE "^HTTP|^location"
    curl -sI "https://www.worldaisummit.com/delegate/" | grep -iE "^HTTP"

Expected: 301 with location https://www.worldaisummit.com/delegate/ (the third line keeps ?utm_source=test), and 200 for /delegate/.

--------------------------------------------------------------------
1e. Find the September source and fix it at the root
--------------------------------------------------------------------
In GA4 (Explore, or Engagement > Pages and screens), filter on page path /delegate-registration.html for 1-30 Sep and add Session source / medium and Session campaign. Change that mailer, ad or partner link to point at https://www.worldaisummit.com/delegate/ directly. The redirect then becomes a safety net instead of the main path.

====================================================================
2. SITEMAP.XML
====================================================================
Delete these two <url> entries. The crawl shows both with inSitemap=true. Match whichever host form the file uses (www or non-www).

    <url><loc>https://www.worldaisummit.com/registration</loc> ... </url>
    <url><loc>https://www.worldaisummit.com/registration.html</loc> ... </url>

/delegate-registration.html is neither in the sitemap nor linked internally, so there is nothing to remove for it. Keep https://www.worldaisummit.com/delegate/ in the sitemap, then resubmit the sitemap in Search Console. Search Console is set up only for the non-www URL-prefix property. Add the www property, or a Domain property, so the www sitemap can be submitted and monitored.

====================================================================
3. /delegate/: ADD THE MISSING H1
====================================================================
The page has no H1. Add one at the top of the main content. To keep the design from moving, you can instead change the tag of the existing hero heading to h1 and keep its class. The page should have only one H1.

    <h1>World AI Summit 2026 Delegate Passes – Bengaluru, 14-15 October</h1>

====================================================================
4. HOMEPAGE: A CRAWLABLE PATH TO /delegate/ (check in a browser first)
====================================================================
Do not remove or repoint the homepage forms. In September, sessions landing on / produced 97 form_submit and 112 partnership_form_submit events, so those forms already work.

Before you edit anything, click each of these in Chrome on desktop and mobile and note what happens (opens a modal, scrolls to a form, goes to /delegate/, or nothing):
- the 'Secure your seat' pass-card buttons
- the nav 'Register' item
- the FAQ 'How can I register for the event?'

Then:
- If a button opens a working form, leave it alone and add the text link in 4a.
- If a button does nothing or loops back to the homepage, change it to <a href="/delegate/">.

4a. Text link directly under the pass cards (always safe to add):

    <p class="pass-link"><a href="/delegate/">See all World AI Summit 2026 pass options, group rates and booking details</a></p>

4b. Nav item. Add it, or replace 'Register' only if 'Register' currently goes nowhere:

    <a href="/delegate/">Delegate passes</a>

4c. FAQ answer for 'How can I register for the event?':

    <p>Choose your pass on the <a href="/delegate/">World AI Summit 2026 delegate pass page</a> and complete the booking form there. Groups of three or more delegates get 10% off. For help with registration, write to <a href="mailto:registration@worldaisummit.com">registration@worldaisummit.com</a>.</p>

4d. Leave out the ?pass=premium and ?pass=vip parameters unless the /delegate/ form already reads them.

How to measure: "conversion" here means a form submission, not a sale. GA4 shows 0 transactions, and /delegate/success.php had 78 views in Jul-Sep. Each week, compare these against the week before the change:
- form_submit and partnership_form_submit for sessions landing on /
- views of /delegate/success.php

If homepage form_submit drops and /delegate/success.php views do not rise, undo the button changes and keep 4a and 4c.

====================================================================
5. /1st-edition/delegate-pass.html: 2025 BANNER
====================================================================
Low traffic: 46 views in Jul-Sep and 1 organic session in September. The page shows Rs 30,000 / 60,000 cards and has no visible checkout. Paste this straight after <body>:

    <div role="note" style="background:#111;color:#fff;padding:12px 16px;text-align:center;font-size:15px;line-height:1.5">You're viewing the 2025 edition. World AI Summit 2026 is on 14-15 October in Bengaluru. <a href="/delegate/" style="color:#ffd400;font-weight:600">Book 2026 passes &rarr;</a></div>

====================================================================
6. SPEAKER PAGES AND /ai-conference-bengaluru-2026.html: CTA BLOCK
====================================================================
This is the lowest priority. /speaker.html had 38 views in September, and no /assets/speaker_details/ page appears in GA4's top rows. Hold it until the price decision below is made.

Add it once to the shared /assets/speaker_details/ template, /speaker.html and /ai-conference-bengaluru-2026.html, after the main content. The copy does not say any speaker is confirmed for 2026, because some speaker pages are still framed as 2025.

    <aside style="border:1px solid #ddd;border-radius:8px;padding:16px;margin:24px 0;text-align:center">
      <p style="margin:0 0 8px;font-weight:600">World AI Summit 2026 · 14-15 October · Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru</p>
      <p style="margin:0 0 12px">Delegate passes from PLACEHOLDER_CURRENT_PASS_PRICE. Groups of three or more delegates get 10% off.</p>
      <a href="/delegate/" style="display:inline-block;background:#111;color:#fff;padding:10px 20px;border-radius:6px;text-decoration:none">Book your pass</a>
    </aside>

If no price should be shown, change the second paragraph to: "Groups of three or more delegates get 10% off."

====================================================================
PRICE DECISION NEEDED BEFORE ANY PRICED COPY SHIPS
====================================================================
The site currently gives conflicting prices:
- /delegate/ says Standard Access is Rs 20,000 / 35,000, valid till 30 Sept 2026, followed by Late Access at Rs 30,000 / 60,000.
- The homepage and the allevents.in listing still say Rs 20,000.

As of 1 Oct these do not agree. Decide which price is live, set PLACEHOLDER_CURRENT_PASS_PRICE to it, and make the homepage, /delegate/ and allevents.in match.
