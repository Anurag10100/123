# A38: indiaaisummit.in to World AI Summit 2026 funnel: announcement bar, homepage section, notes for old pages, redirects (Apache and nginx)

- **For recommendation:** Turn indiaaisummit.in into a World AI Summit funnel: announcement bar, deep links and stale-page cleanup
- **Research lens:** elets-network
- **Format:** Paste-ready HTML snippets plus Apache .htaccess and nginx config, in numbered sections
- **Placeholders the business must fill:**
  - PLACEHOLDER_AWARDS_CLOSING_DATE: closing date for World AI Awards 2026 nominations (section 3). Delete the sentence if no date has been set.

## How to ship

Owner: web dev for indiaaisummit.in. Deadline: 3 Oct 2026. Time needed: under 2 hours. No change on worldaisummit.com is needed.

Steps:
1. Do this first: stop pass sales on indiaaisummit.in/delegate/. Use the redirect in section 6, or use the note in section 4 and remove the checkout form. I could not tell whether that checkout still takes payments; it may be live.
2. Find out which server runs the site with `curl -sI https://www.indiaaisummit.in/ | grep -i server`. The site loads Google Sign-In and has a coupon checkout, so it may also be a PHP or Node app with its own router. In that case, add the redirects in the app's router, or in the Cloudflare/CDN Redirect Rules if a CDN sits in front.
3. Add the redirects:
   - /award/ always gets the redirect.
   - /delegate/ gets the redirect unless the note-plus-form-removal option is chosen.
   - /awards gets the note (section 3) by default; the redirect for it is optional.
   - Remove /delegate/ and /award/ from the indiaaisummit.in sitemap.
4. Add the announcement bar (section 1) to the shared header so it appears on every page. If the site header is position:fixed, put the bar inside the header so it is not hidden behind it.
5. Add the homepage section (section 2) right below the hero, and hide the January 2026 pass blocks on the homepage.
6. Add the notes:
   - Section 3 goes on /awards. Also remove its "Nominate Now" buttons.
   - Section 5 goes on /1st-edition/index.
7. Fill PLACEHOLDER_AWARDS_CLOSING_DATE, or delete that sentence.
8. Run the curl checks in 6c.
9. Measure in GA4 on worldaisummit.com: Session source = indiaaisummit.in, medium = referral, split by utm_content (bar, home_section, awards_note, delegate_note, 1st_edition_note). Compare 1-15 Oct with the earlier claim of zero referral sessions, which was never verified.

Left out on purpose:
- The optional homepage retitle is dropped. Verifier finding 7: even in the best case worldaisummit.com only moves from #15 to #14, which is still page 2.
- No Event JSON-LD is included. Event markup belongs on the worldaisummit.com event pages, not on a sibling site whose page is about a different event.
- Redirects use 302, because the recurring Delhi edition is likely to reuse these URLs. Switch to 301 only if Elets confirms they will not be reused.

What I could not check:
- The agent proxy blocked direct requests to indiaaisummit.in and worldaisummit.com (403), so server headers and status codes were not checked.
- Every page fact comes from the verifier's Exa fetches on 1 Oct 2026 and the project context.
- I did not use any OpenSEO paid tools.

## Content

WORLD AI SUMMIT 2026 FUNNEL ON indiaaisummit.in
Prepared 1 Oct 2026. Ship by 3 Oct 2026. Every link goes to www.worldaisummit.com. No prices are shown, so nothing here goes out of date before the event.
UTM rule: utm_medium=referral, so GA4 files these visits under the Referral channel. The original "referral_bar" medium would show up as Unassigned. utm_content records which block on the page sent the click.

============================================================
1. SITEWIDE ANNOUNCEMENT BAR
Where: every indiaaisummit.in page, right after <body>, through the shared header/template.
============================================================
<div role="region" aria-label="Next Elets AI event" style="background:#0b1f4d;color:#fff;padding:10px 16px;text-align:center;font:500 15px/1.4 system-ui,sans-serif">Next Elets AI event: <strong>World AI Summit 2026</strong>, Bengaluru, 14&ndash;15 October 2026 &middot; <a href="https://www.worldaisummit.com/delegate/?utm_source=indiaaisummit.in&amp;utm_medium=referral&amp;utm_campaign=world_ai_summit_2026_delegate&amp;utm_content=bar" style="color:#ffd84d;text-decoration:underline">Book a delegate pass</a> &middot; <a href="https://www.worldaisummit.com/awards/?utm_source=indiaaisummit.in&amp;utm_medium=referral&amp;utm_campaign=world_ai_awards_2026&amp;utm_content=bar" style="color:#ffd84d;text-decoration:underline">Nominate for the World AI Awards 2026</a></div>

============================================================
2. HOMEPAGE SECTION: "Next Elets AI event"
Where: homepage, right below the hero, so it shows on the first screen. Remove or hide the January 2026 Early Bird and Regular pass blocks on the homepage.
============================================================
<section aria-labelledby="next-elets-ai-event" style="max-width:960px;margin:24px auto;padding:20px 16px;border:1px solid #c9d3ea;border-radius:8px;background:#f5f8ff;color:#0b1f4d;font:400 16px/1.55 system-ui,sans-serif">
  <h2 id="next-elets-ai-event" style="margin:0 0 8px;font-size:22px;line-height:1.3;color:#0b1f4d">Next Elets AI event: World AI Summit 2026, Bengaluru</h2>
  <p style="margin:0 0 10px">Elets AI Summit 2026 in New Delhi (22 January 2026) has concluded. Elets Technomedia&rsquo;s next AI summit is <a href="https://www.worldaisummit.com/?utm_source=indiaaisummit.in&amp;utm_medium=referral&amp;utm_campaign=world_ai_summit_2026&amp;utm_content=home_section" style="color:#0b3fb3;text-decoration:underline">World AI Summit 2026, Bengaluru, 14&ndash;15 October</a>, at Sheraton Grand Bangalore Hotel at Brigade Gateway.</p>
  <p style="margin:0 0 14px">Seven tracks: Frontier Models &amp; Compute; Sovereign AI &amp; Geopolitics; Enterprise AI in Production; GCCs; Robotics, Agents &amp; Embodied AI; AI for Bharat; Capital, Founders &amp; Exits.</p>
  <p style="margin:0">
    <a href="https://www.worldaisummit.com/delegate/?utm_source=indiaaisummit.in&amp;utm_medium=referral&amp;utm_campaign=world_ai_summit_2026_delegate&amp;utm_content=home_section" style="display:inline-block;margin:0 12px 8px 0;padding:10px 16px;border-radius:6px;background:#0b1f4d;color:#fff;text-decoration:none;font-weight:600">Book a delegate pass for World AI Summit 2026</a>
    <a href="https://www.worldaisummit.com/awards/?utm_source=indiaaisummit.in&amp;utm_medium=referral&amp;utm_campaign=world_ai_awards_2026&amp;utm_content=home_section" style="display:inline-block;margin:0 0 8px;color:#0b3fb3;text-decoration:underline;font-weight:600">Nominate for the World AI Awards 2026</a>
  </p>
</section>

============================================================
3. /awards: NOTE AT THE TOP (recommended instead of a redirect)
Where: indiaaisummit.in/awards, above the first heading of the main content. Also remove or disable every "Nominate Now" button on this page, because they collect entries for a cycle that has closed.
Why a note instead of a redirect: this page is a different programme (Elets India AI Awards, Delhi). The redirect target, worldaisummit.com/awards/, currently has no category, fee or deadline text, so nominees would land on a thinner page.
============================================================
<div role="note" style="max-width:960px;margin:16px auto;padding:14px 16px;border-left:4px solid #0b1f4d;background:#fff8db;color:#1a1a1a;font:400 16px/1.5 system-ui,sans-serif"><strong>Nominations for the Elets India AI Awards 2025 are closed.</strong> Entries are open for the World AI Awards 2026 from Elets Technomedia, organiser of World AI Summit 2026 in Bengaluru (14&ndash;15 October 2026). <a href="https://www.worldaisummit.com/awards/?utm_source=indiaaisummit.in&amp;utm_medium=referral&amp;utm_campaign=world_ai_awards_2026&amp;utm_content=awards_note" style="color:#0b3fb3;text-decoration:underline">Nominate for the World AI Awards 2026</a>. Entries close on PLACEHOLDER_AWARDS_CLOSING_DATE.</div>
(If no closing date has been set, delete the last sentence.)

============================================================
4. /delegate/: REDIRECT (recommended, see section 6). The note below is the fallback if no redirect is possible.
This page still runs a live checkout for the finished January 2026 event ("Buy Conference Pass", Final Release Rs 20,000/40,000). Stopping those sales matters more than anything else in this pack. If you use the note instead of the redirect, also remove or disable the checkout form and the coupon field.
============================================================
<div role="note" style="max-width:960px;margin:16px auto;padding:14px 16px;border-left:4px solid #0b1f4d;background:#fff8db;color:#1a1a1a;font:400 16px/1.5 system-ui,sans-serif"><strong>Elets AI Summit 2026, New Delhi (22 January 2026) has concluded, and passes for it are no longer on sale.</strong> Elets Technomedia&rsquo;s next AI summit is World AI Summit 2026, Bengaluru, 14&ndash;15 October 2026, at Sheraton Grand Bangalore Hotel at Brigade Gateway. <a href="https://www.worldaisummit.com/delegate/?utm_source=indiaaisummit.in&amp;utm_medium=referral&amp;utm_campaign=world_ai_summit_2026_delegate&amp;utm_content=delegate_note" style="color:#0b3fb3;text-decoration:underline">Book a World AI Summit 2026 delegate pass</a>. For help with passes, write to <a href="mailto:registration@worldaisummit.com" style="color:#0b3fb3;text-decoration:underline">registration@worldaisummit.com</a>.</div>

============================================================
5. /1st-edition/index (India AI Summit Bengaluru 2024): NOTE AT THE TOP
Where: above the first heading of the main content.
============================================================
<div role="note" style="max-width:960px;margin:16px auto;padding:14px 16px;border-left:4px solid #0b1f4d;background:#f5f8ff;color:#1a1a1a;font:400 16px/1.5 system-ui,sans-serif">This page is the archive of India AI Summit Bengaluru 2024. Elets Technomedia&rsquo;s next AI summit in Bengaluru is <a href="https://www.worldaisummit.com/?utm_source=indiaaisummit.in&amp;utm_medium=referral&amp;utm_campaign=world_ai_summit_2026&amp;utm_content=1st_edition_note" style="color:#0b3fb3;text-decoration:underline">World AI Summit 2026, Bengaluru, 14&ndash;15 October 2026</a>, at Sheraton Grand Bangalore Hotel at Brigade Gateway.</div>

============================================================
6. REDIRECTS
Covers /delegate/ (live checkout for the finished event) and /award/ (singular; an indexed copy of the homepage that the earlier "Redirect 301 /awards" rule did not cover). /awards is optional and commented out, because section 3 is the recommended treatment for it.
Status code: 302, because the recurring Delhi edition is likely to reuse these URLs, and browsers cache a 301 indefinitely. Switch every 302 to 301 only if Elets confirms these URLs will not be reused.
Server type is not confirmed. Check it first with: curl -sI https://www.indiaaisummit.in/ | grep -i '^server'
============================================================

--- 6a. Apache: .htaccess in the document root ---
Put this at the very top, above any existing RewriteRule. The site already sends unknown paths such as /award/ to the homepage, and a plain mod_alias "Redirect" line can lose to that rewrite.

# World AI Summit 2026 funnel (added Oct 2026). Remove when the next Delhi edition reuses these URLs.
<IfModule mod_rewrite.c>
RewriteEngine On
# Finished Jan 2026 checkout -> World AI Summit 2026 delegate page
RewriteRule ^delegate/?$ https://www.worldaisummit.com/delegate/ [R=302,L]
# /award/ (singular) serves a copy of the homepage and is indexed as "India AI Summit 2025"
RewriteRule ^award/?$ https://www.worldaisummit.com/awards/ [R=302,L]
# OPTIONAL: only if you choose the redirect over the note in section 3
# RewriteRule ^awards/?$ https://www.worldaisummit.com/awards/ [R=302,L]
</IfModule>

(In an Apache <VirtualHost> block instead of .htaccess, add a leading slash to each pattern: ^/delegate/?$ , ^/award/?$ , ^/awards/?$ )

--- 6b. nginx: inside the server {} block(s) for indiaaisummit.in and www.indiaaisummit.in ---
Exact-match locations take priority over prefix and regex locations. If a "location = /delegate/" block already exists, merge into it.

# World AI Summit 2026 funnel (added Oct 2026). Remove when the next Delhi edition reuses these URLs.
location = /delegate  { return 302 https://www.worldaisummit.com/delegate/$is_args$args; }
location = /delegate/ { return 302 https://www.worldaisummit.com/delegate/$is_args$args; }
location = /award     { return 302 https://www.worldaisummit.com/awards/$is_args$args; }
location = /award/    { return 302 https://www.worldaisummit.com/awards/$is_args$args; }
# OPTIONAL: only if you choose the redirect over the note in section 3
# location = /awards  { return 302 https://www.worldaisummit.com/awards/$is_args$args; }
# location = /awards/ { return 302 https://www.worldaisummit.com/awards/$is_args$args; }

Then run: sudo nginx -t && sudo systemctl reload nginx

--- 6c. Check after deploying (each should return 302 and the Location shown) ---
curl -sI https://www.indiaaisummit.in/delegate/ | grep -iE '^(HTTP|location)'   -> https://www.worldaisummit.com/delegate/
curl -sI https://www.indiaaisummit.in/award/    | grep -iE '^(HTTP|location)'   -> https://www.worldaisummit.com/awards/
curl -sI https://www.indiaaisummit.in/awards    | grep -iE '^(HTTP|location)'   -> 200 if you kept the note, 302 if you enabled the optional rule
