# A15: Legacy 2025 URL redirect map for worldaisummit.com (Apache .htaccess and nginx), corrected and loop-checked

- **For recommendation:** 301 the 2025 non-www URLs that Google still knows (now 5xx or 404) to their 2026 www equivalents
- **Research lens:** search-console
- **Format:** Server config: Apache .htaccess block, nginx map and server lines, and a bash curl test script
- **Placeholders the business must fill:**
  - PLACEHOLDER_ENABLE_AFTER_CONTENT_MOVE: Elets confirms /partnership.html as the single sponsor URL, moves the 219-word partner-with-us.html copy onto it and makes it self-canonical; only then uncomment the partner-with-us.html -> /partnership.html redirect (Apache and nginx)

## How to ship

Owner: web dev. Deadline: 5 Oct 2026. Effort: about 1 hour including tests.

1. Find out which server you have: run curl -sI https://www.worldaisummit.com/ and look at the "server" header, or ask the hosting team. On Apache or LiteSpeed (cPanel), use block A. On nginx, use block B. I could not check this from here because direct HTTP to the site is blocked.
2. Back up .htaccess, or the nginx conf.
3. Delete the existing 302 that sends www /registration and /registration.html to https://worldaisummit.com/. The 1 Oct crawl c1b16b55 recorded both chains: non-www /registration goes to www /registration, then 302 to non-www /, then 301 to www /. www /registration.html goes 302 to non-www /, then 301 to www /. If that rule stays, it can still fire before or beside the new one.
4. Paste the block above the existing non-www to www rule, then run the test script (section C).
5. Loop check, done against the 1 Oct crawl c1b16b55. Every target returns 200 and is not redirected: www / (1,513 words), /ai-conference-bengaluru-2026.html (2,069), /awards/ (564), /delegate/ (631), /partnership.html (64). None of the targets matches a source pattern ("awards/" does not match ^awards$, "delegate/" does not match ^delegate$, and "partnership.html" does not match ^partnership/?$). So there is no loop on either host. Re-run section C after deploy to confirm on the live server.
6. Same day: remove /registration and /registration.html from sitemap.xml (the crawl shows both listed), plus /delegate-registration.html if it is listed, then resubmit the sitemap.
7. Leave /award.html live. It is a 2026 page (200, 851 words) with the full category list and "Entries from 30k + GST", and it had 10 key events from 61 organic sessions (3 to 30 Sep). The brief's Rs 18,000 + GST is the 2025 fee and should not be quoted anywhere. Separately, award.html canonicals to /. Making it self-canonical is a follow-up, and after that /entry-guidelines could point to it instead of /awards/.
8. Sponsor pages (needs an Elets decision): the rules send old partner URLs to /partnership.html because that URL has the organic traffic. Before you enable the PLACEHOLDER_ENABLE_AFTER_CONTENT_MOVE line, move the 219-word copy from partner-with-us.html onto partnership.html, make partnership.html self-canonical (both pages canonical to / today), and point nav links at partnership.html.
9. Expected effect (honest): in the last 28 days (31 Aug to 28 Sep), no legacy URL in this map had any impressions. Only non-www /awards (32 clicks, 1,300 impressions) and non-www / had any. So do not expect search traffic to come back before 14 Oct. The 16-month figures (for example /agenda 35 clicks and 7,566 impressions) come from the 2025 cycle. Here is what the change does fix:
   (a) Today, non-www /faqs, /ai-dialogues, /partnership and /registration 301 to the same path on www. Those www pages probably do not exist. Exa returned CRAWL_NOT_FOUND for www /agenda and www /faqs, which is inferred, not a confirmed 404. After the change they land on live pages.
   (b) /registration goes from 3 hops ending on the homepage to 1 hop to /delegate/. Note that Google calls non-www /registration "unknown to Google", so this only matters for off-site links such as mailers, social posts and listings.
   (c) /delegate-registration.html had 12 organic sessions and 0 key events (it only shows contact emails). Those visitors now reach /delegate/, which had 16 key events from 48 sessions.
   (d) Non-www /awards, the one legacy URL still earning impressions, goes straight to /awards/ in one hop.
10. Long term: verify the https://www.worldaisummit.com/ property in Search Console. The current non-www property will go quiet because all its URLs now 301 to www. Also rename the GA4 property from "Elets World AI Summit 2025".

## Content

############################################################################
# A. APACHE / LITESPEED (.htaccess in the www document root)
#    Paste ABOVE the existing non-www -> www rule. Works on both hosts.
#    Changes from the brief's version:
#      - award.html removed. It is a live 2026 page and the best awards converter.
#      - The host condition is repeated for every rule. A RewriteCond only
#        applies to the single rule straight after it.
#      - Sponsor target set to /partnership.html (19 organic sessions and
#        2 key events, against 0 organic sessions for partner-with-us.html).
#      - A trailing slash is allowed only where it cannot loop. /awards/ and
#        /delegate/ are targets, so "awards" and "delegate" stay slash-free.
#    These rules do not touch /award.html, /partner-with-us.html (until the
#    content move) or anything under /1st-edition/. Every pattern is anchored
#    at the site root.
#    If you put this in the <VirtualHost> config instead of .htaccess, change
#    each "^(" to "^/(".
############################################################################

# STEP 0. DELETE the rule that now sends /registration and /registration.html
# to https://worldaisummit.com/ with a 302. It may be a "Redirect 302 ..." line,
# a RewriteRule with [R=302], or an entry under cPanel > Domains > Redirects.

RewriteEngine On

# 1. Agenda pages and 2025 agenda/explainer posts -> 2026 conference page
RewriteCond %{HTTP_HOST} ^(www\.)?worldaisummit\.com$ [NC]
RewriteRule ^(agenda|world-ai-agenda\.html|world-ai-agneda\.html|what-to-expect-world-ai-summit-2025-agenda-highlights(\.html)?|why-attend-the-world-ai-summit-2025-in-bengaluru-7-straightforward-reasons-to-show-up)/?$ https://www.worldaisummit.com/ai-conference-bengaluru-2026.html [R=301,L]

# 2. Awards and nomination pages -> /awards/   (award.html deliberately NOT included)
RewriteCond %{HTTP_HOST} ^(www\.)?worldaisummit\.com$ [NC]
RewriteRule ^(awards|awards\.html|nomination/?|entry-guidelines/?|world-ai-awards-2025-celebrating-architects-of-the-ai-era(\.html|/)?)$ https://www.worldaisummit.com/awards/ [R=301,L]

# 3. Delegate, pass and registration pages -> /delegate/
#    (replaces the old 3-hop 302 chain from /registration to the homepage)
RewriteCond %{HTTP_HOST} ^(www\.)?worldaisummit\.com$ [NC]
RewriteRule ^(delegate|delegate-pass(\.html)?|delegate-registration\.html|registration/?|registration\.html|theworld-ai-summit-2025-only-30-earlybird-passes-left/?)$ https://www.worldaisummit.com/delegate/ [R=301,L]

# 4. Sponsor pages -> /partnership.html (the sponsor URL that gets organic traffic)
RewriteCond %{HTTP_HOST} ^(www\.)?worldaisummit\.com$ [NC]
RewriteRule ^(partnership|partner-benefits(\.html)?|why-your-brand-needs-to-be-at-the-world-ai-summit)/?$ https://www.worldaisummit.com/partnership.html [R=301,L]

# PLACEHOLDER_ENABLE_AFTER_CONTENT_MOVE: uncomment the two lines below only after
# the 219-word copy from partner-with-us.html is on partnership.html and
# partnership.html is self-canonical.
# RewriteCond %{HTTP_HOST} ^(www\.)?worldaisummit\.com$ [NC]
# RewriteRule ^partner-with-us\.html$ https://www.worldaisummit.com/partnership.html [R=301,L]

# 5. 2025 pages with no 2026 equivalent -> homepage
RewriteCond %{HTTP_HOST} ^(www\.)?worldaisummit\.com$ [NC]
RewriteRule ^(faqs|startup-competition(\.html)?|worldai-startup-competition\.php|ai-dialogues)/?$ https://www.worldaisummit.com/ [R=301,L]

# EXISTING RULE, already in the file. Keep it BELOW this block and do not add it twice:
# RewriteCond %{HTTP_HOST} ^worldaisummit\.com$ [NC]
# RewriteRule ^(.*)$ https://www.worldaisummit.com/$1 [R=301,L]


############################################################################
# B. NGINX (use this instead of A if the server is nginx)
############################################################################

# B1. In the http {} context, e.g. /etc/nginx/conf.d/wais-legacy-map.conf
map $uri $wais_legacy {
    default "";
    "~^/(agenda|world-ai-agenda\.html|world-ai-agneda\.html|what-to-expect-world-ai-summit-2025-agenda-highlights(\.html)?|why-attend-the-world-ai-summit-2025-in-bengaluru-7-straightforward-reasons-to-show-up)/?$"  /ai-conference-bengaluru-2026.html;
    "~^/(awards|awards\.html|nomination/?|entry-guidelines/?|world-ai-awards-2025-celebrating-architects-of-the-ai-era(\.html|/)?)$"  /awards/;
    "~^/(delegate|delegate-pass(\.html)?|delegate-registration\.html|registration/?|registration\.html|theworld-ai-summit-2025-only-30-earlybird-passes-left/?)$"  /delegate/;
    "~^/(partnership|partner-benefits(\.html)?|why-your-brand-needs-to-be-at-the-world-ai-summit)/?$"  /partnership.html;
    # PLACEHOLDER_ENABLE_AFTER_CONTENT_MOVE
    # "~^/partner-with-us\.html$"  /partnership.html;
    "~^/(faqs|startup-competition(\.html)?|worldai-startup-competition\.php|ai-dialogues)/?$"  /;
}

# B2. Non-www server block (443, and the port 80 block if it has its own redirect)
server {
    server_name worldaisummit.com;
    # ... existing listen / ssl lines stay as they are ...
    if ($wais_legacy) { return 301 https://www.worldaisummit.com$wais_legacy$is_args$args; }
    return 301 https://www.worldaisummit.com$request_uri;
}

# B3. In the existing www server block, as the first line after server_name:
#     if ($wais_legacy) { return 301 https://www.worldaisummit.com$wais_legacy$is_args$args; }
# Also delete any "location /registration" or rewrite that returns 302 to https://worldaisummit.com/.
# Then run: nginx -t && systemctl reload nginx


############################################################################
# C. TEST AFTER DEPLOY (run from any machine)
############################################################################
for p in agenda faqs ai-dialogues startup-competition startup-competition.html \
         awards nomination entry-guidelines delegate delegate-pass \
         registration registration.html delegate-registration.html \
         partnership partner-benefits award.html; do
  for h in worldaisummit.com www.worldaisummit.com; do
    printf '%-48s ' "$h/$p"
    curl -s -o /dev/null -w '%{http_code} -> %{redirect_url}\n' "https://$h/$p"
  done
done
# Expected: each line is "301 -> https://www.worldaisummit.com/<one of the 5 targets>",
# except award.html: 200 on www, and 301 to https://www.worldaisummit.com/award.html on non-www.

# Targets must answer 200 with no further hop (no loop):
for t in / ai-conference-bengaluru-2026.html awards/ delegate/ partnership.html award.html partner-with-us.html; do
  printf '%-40s ' "$t"
  curl -s -o /dev/null -w '%{http_code} hops=%{num_redirects}\n' -L "https://www.worldaisummit.com/$t"
done
# Expected: 200 hops=0 for every line.
# Spot-check: curl -sIL https://worldaisummit.com/awards should show one 301, then 200 on /awards/.
