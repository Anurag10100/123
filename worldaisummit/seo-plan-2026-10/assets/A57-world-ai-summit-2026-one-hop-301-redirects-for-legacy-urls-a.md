# A57: World AI Summit 2026: one-hop 301 redirects for legacy URLs (Apache + nginx), with pre-deploy gates and a test script

- **For recommendation:** Replace the 3-hop chains, 302s and 404/5xx legacy URLs with one-hop 301s to the 2026 pass, awards and partner pages
- **Research lens:** tech-indexing
- **Format:** Plain-text deploy pack: pre-deploy checklist, Apache .htaccess block, nginx config, bash test script, post-deploy tasks (sitemap, internal links, 2025 archive banner)
- **Placeholders the business must fill:**
  - PLACEHOLDER_CURRENT_TIER_NAME (the delegate pass tier on sale now that the Standard tier expired on 30 Sept 2026)
  - PLACEHOLDER_CURRENT_PASS_PRICE (current price for that tier, single and any alternate rate)
  - PLACEHOLDER_TIER_VALID_TILL (last date the current tier price is valid)
  - PLACEHOLDER_GSC_OWNER (Google account that will own the new www or Domain Search Console property; ideally the owner of the existing non-www property)

## How to ship

Owner: web dev, about 1-3 hours including testing. Deadline: 3 Oct 2026. Order:
1. Run the section 0 gates. Check www /awards in a browser. Fix the /delegate/ price block and H1, or use the TEMPORARY 302 line. Add a www or Domain Search Console property. Delete the old /registration 302 and the existing host rule. Back up .htaccess.
2. Paste section 1 (Apache) or section 2 (nginx); the stack is unknown. robots.txt has WordPress lines but the pages are static .html. On WordPress, the Apache block goes above "# BEGIN WordPress".
3. Run the section 3 script. Every legacy URL must show one 301 to its final www URL and a final 200.
4. Same day, do section 4: sitemap, internal links, archive banner and titles, and Request indexing in the www property.

Scope (verifier corrections applied):
- This change is mainly protective. Its main job is to keep the one URL with Google clicks: non-www /awards had 79 clicks and 2,419 impressions with average position 9.1 (non-www GSC, 28 Jun-28 Sep). Those clicks come from generic queries such as 'ai awards 2026', 'ai awards' and 'ai awards india'. 'world ai awards' got 66 impressions and 0 clicks.
- Don't expect it to move 'ai summit registration' or 'ai summit 2026 registration'. Those rank from the homepage, and GSC reports non-www /registration as unknown to Google.
- Only 3 non-www URLs had any impressions in 3 months. www-side legacy traffic is unknown because the www property is not connected.

Verified in this session:
- Exa web_fetch of https://www.worldaisummit.com/awards on 1 Oct 2026 still returned the 2025 awards page ('World AI Summit 2025', '25-26 September 2025 Sheraton Grand Brigade Gateway, Bengaluru'). It may be cached, so the browser check in step 0a decides.
- The redirect patterns were tested with Python regex against 38 sample paths. Every legacy path maps to its intended target. /awards/, /delegate/, /1st-edition/, /1st-edition/speakers.html and the other live pages are untouched, so no loops.
- Live curl from this session was blocked (proxy 403), so the section 3 test must be run from a normal machine after deploy.

Two defensive changes beyond the original asset:
- awards.html is added to the awards rule, in case a 2025 awards.html file is what serves www /awards.
- There is a note on removing 'agenda' from the agenda rule once /agenda/ is published. Without it, the rule would redirect the new page away.

## Content

WORLD AI SUMMIT 2026: LEGACY URL REDIRECTS (one-hop 301s)
Prepared 1 Oct 2026 for the web developer. Deploy by 3 Oct 2026.
What this fixes: the 302s and multi-hop chains on /registration and /registration.html, the 302s on /1st-edition/ slugs, the 404 and 5xx legacy URLs, and www /awards (no slash). That last URL may still serve the 2025 awards page. It matters because /awards is the only URL with real Google clicks.

====================================================================
0. BEFORE YOU DEPLOY (about 30 min)
====================================================================
a) Check www /awards now (urgent item).
   Open both of these in a private window:
     https://www.worldaisummit.com/awards    (no slash)
     https://www.worldaisummit.com/awards/   (with slash)
   On 1 Oct an Exa fetch of the no-slash URL returned a 2025 page with the headings "World AI Summit 2025" and "25-26 September 2025 Sheraton Grand Brigade Gateway, Bengaluru". That copy may be cached.
   - If /awards shows 2025 and /awards/ shows the 2026 nomination form, ship the AWARDS lines first.
   - If /awards/ also shows 2025 content, stop. Fix /awards/ before you redirect anything to it.

b) Fix /delegate/ before legacy traffic is sent to it.
   - Remove the Early Bird block (valid till 25 Jul 2025).
   - Remove the Standard tier (valid till 30 Sept 2026, now expired).
   - Show: PLACEHOLDER_CURRENT_TIER_NAME at PLACEHOLDER_CURRENT_PASS_PRICE, valid till PLACEHOLDER_TIER_VALID_TILL.
   - Add one H1: World AI Summit 2026 Delegate Pass
   If this cannot be done before deploy, use the TEMPORARY delegate line in section 1 or 2 and switch to the 301 once /delegate/ is fixed.

c) Add Search Console for www before or on deploy day.
   Use either a Domain property for worldaisummit.com (needs a DNS TXT record) or a URL-prefix property for https://www.worldaisummit.com/ (an HTML file at the web root works).
   Owner: PLACEHOLDER_GSC_OWNER
   The only connected property is non-www (URL-prefix). With everything on www it stops collecting data, and without a new property we have no first-party data during event week.

d) Delete the old /registration 302, which sends traffic to https://worldaisummit.com/.
     grep -niE 'registration|R=302|Redirect(Match)? +302|worldaisummit\.com' .htaccess
   Also check the hosting panel's Redirects page and any CDN redirect rules (for example Cloudflare). Delete any existing non-www or http-to-https rule too, because the block below replaces it.

e) Back up the current file:
     cp .htaccess .htaccess.bak-20261001

====================================================================
1. APACHE (.htaccess at web root, TOP of file)
   Put it above any extensionless .html rules and above "# BEGIN WordPress" if that block exists.
====================================================================
# ===== World AI Summit legacy redirects: START (1 Oct 2026) =====
RewriteEngine On

# Duplicate index files
RewriteCond %{THE_REQUEST} \s/index\.html[\s?] [NC]
RewriteRule ^index\.html$ https://www.worldaisummit.com/ [R=301,L]
RewriteCond %{THE_REQUEST} \s/blog/index\.html[\s?] [NC]
RewriteRule ^blog/index\.html$ https://www.worldaisummit.com/blog/ [R=301,L]

# AWARDS (urgent: www /awards may still serve the 2025 page)
RewriteRule ^(awards|awards\.html|award\.html|1st-edition/awards\.html)$ https://www.worldaisummit.com/awards/ [R=301,L,NC]
RewriteRule ^(nomination|entry-guidelines)/?$ https://www.worldaisummit.com/awards/ [R=301,L,NC]

# DELEGATE PASS (only after /delegate/ is fixed, see step 0b)
RewriteRule ^(registration|registration\.html|delegate-pass|giveaway|1st-edition/delegate-pass\.html|1st-edition/giveaway\.html)/?$ https://www.worldaisummit.com/delegate/ [R=301,L,NC]
# TEMPORARY, if /delegate/ is not fixed yet: comment out the line above and uncomment this one.
# RewriteRule ^(registration|registration\.html|delegate-pass|giveaway|1st-edition/delegate-pass\.html|1st-edition/giveaway\.html)/?$ https://www.worldaisummit.com/ [R=302,L,NC]

# PARTNERS
RewriteRule ^(partnership|partnership\.html|partner-benefits|1st-edition/partnership\.html|1st-edition/partner-benefits\.html)/?$ https://www.worldaisummit.com/partner-with-us.html [R=301,L,NC]

# 2025 INFO PAGES
RewriteRule ^(faqs|thematic-tracks|1st-edition/thematic-tracks)/?$ https://www.worldaisummit.com/ [R=301,L,NC]

# AGENDA AND 2025 BLOG SLUGS
# When /agenda/ is published, remove "agenda|" from the next rule and add this line:
#   RewriteRule ^agenda$ https://www.worldaisummit.com/agenda/ [R=301,L,NC]
# Otherwise this rule would redirect the new /agenda/ page away.
RewriteRule ^(agenda|ai-dialogues|1st-edition/ai-dialogues(\.html)?|1st-edition/world-ai-agenda\.html|(1st-edition/)?what-to-expect-world-ai-summit-2025-agenda-highlights|1st-edition/why-attend-the-world-ai-summit-2025-in-bengaluru-7-straightforward-reasons-to-show-up|1st-edition/world-ai-summit-2025-bengaluru-to-host-the-most-futuristic-and-deep-tech-ai-confluence)/?$ https://www.worldaisummit.com/ai-conference-bengaluru-2026.html [R=301,L,NC]

# HOST + HTTPS LAST
# Behind Cloudflare or another proxy, replace the %{HTTPS} line with:
#   RewriteCond %{HTTP:X-Forwarded-Proto} =http
RewriteCond %{HTTP_HOST} !^www\.worldaisummit\.com$ [NC,OR]
RewriteCond %{HTTPS} off
RewriteRule ^ https://www.worldaisummit.com%{REQUEST_URI} [R=301,L,NE]
# ===== World AI Summit legacy redirects: END =====

====================================================================
2. NGINX (map blocks at http{} level; server blocks replace the existing ones)
====================================================================
map $request_uri $wais_path { "~^(?<p>[^?]*)" $p; }

map $wais_path $wais_redirect {
  default "";
  /index.html /;
  /blog/index.html /blog/;
  "~*^/(awards|awards\.html|award\.html|1st-edition/awards\.html)$" /awards/;
  "~*^/(nomination|entry-guidelines)/?$" /awards/;
  "~*^/(registration|registration\.html|delegate-pass|giveaway|1st-edition/delegate-pass\.html|1st-edition/giveaway\.html)/?$" /delegate/;
  "~*^/(partnership|partnership\.html|partner-benefits|1st-edition/partnership\.html|1st-edition/partner-benefits\.html)/?$" /partner-with-us.html;
  "~*^/(faqs|thematic-tracks|1st-edition/thematic-tracks)/?$" /;
  # When /agenda/ is published, remove "agenda|" below and add:  "~*^/agenda$" /agenda/;
  "~*^/(agenda|ai-dialogues|1st-edition/ai-dialogues(\.html)?|1st-edition/world-ai-agenda\.html|(1st-edition/)?what-to-expect-world-ai-summit-2025-agenda-highlights|1st-edition/why-attend-the-world-ai-summit-2025-in-bengaluru-7-straightforward-reasons-to-show-up|1st-edition/world-ai-summit-2025-bengaluru-to-host-the-most-futuristic-and-deep-tech-ai-confluence)/?$" /ai-conference-bengaluru-2026.html;
}

server {
  listen 80; listen [::]:80;
  server_name worldaisummit.com www.worldaisummit.com;
  if ($wais_redirect) { return 301 https://www.worldaisummit.com$wais_redirect$is_args$args; }
  return 301 https://www.worldaisummit.com$request_uri;
}

server {
  listen 443 ssl http2;            # nginx 1.25.1+: "listen 443 ssl;" plus "http2 on;"
  server_name worldaisummit.com;   # the certificate must cover the apex; reuse the existing ssl_certificate lines
  if ($wais_redirect) { return 301 https://www.worldaisummit.com$wais_redirect$is_args$args; }
  return 301 https://www.worldaisummit.com$request_uri;
}

server {
  listen 443 ssl http2;
  server_name www.worldaisummit.com;
  if ($wais_redirect) { return 301 https://www.worldaisummit.com$wais_redirect$is_args$args; }
  # ...existing ssl_certificate, root, index and location config...
}

# TEMPORARY, if /delegate/ is not fixed yet: put this line ABOVE "if ($wais_redirect)" in all three server blocks.
# Remove it once /delegate/ is fixed.
# if ($wais_path ~* "^/(registration|registration\.html|delegate-pass|giveaway|1st-edition/delegate-pass\.html|1st-edition/giveaway\.html)/?$") { return 302 https://www.worldaisummit.com/$is_args$args; }

# The map uses $request_uri rather than $uri, so the internal index redirect cannot loop on /index.html.
# Run "nginx -t" and then "systemctl reload nginx".

====================================================================
3. TEST (run from a laptop after deploy; save as test-redirects.sh)
====================================================================
#!/usr/bin/env bash
chk(){ a=$(curl -s -o /dev/null -w '%{http_code} %{redirect_url}' "$1"); b=$(curl -s -o /dev/null -L -w 'hops=%{num_redirects} final=%{http_code}' "$1"); printf '%-80s %s | %s\n' "$1" "$a" "$b"; }
for h in http://worldaisummit.com https://worldaisummit.com http://www.worldaisummit.com https://www.worldaisummit.com; do
  for u in registration registration.html delegate-pass giveaway 1st-edition/delegate-pass.html awards award.html 1st-edition/awards.html nomination entry-guidelines partnership partnership.html partner-benefits faqs thematic-tracks 1st-edition/thematic-tracks agenda 1st-edition/ai-dialogues index.html blog/index.html; do
    chk "$h/$u"
  done
done
chk "https://worldaisummit.com/registration?utm_source=test"
for t in "" blog/ delegate/ awards/ partner-with-us.html ai-conference-bengaluru-2026.html 1st-edition/; do chk "https://www.worldaisummit.com/$t"; done

PASS criteria:
- Every legacy URL shows "301 https://www.worldaisummit.com/<target> | hops=1 final=200".
- The utm test keeps ?utm_source=test in the Location.
- The final group (live pages) shows "200 | hops=0 final=200".
FAIL: any 302 (except the TEMPORARY delegate line), hops=2 or more, final=404/5xx, or a redirect loop. If you see a failure, restore .htaccess.bak-20261001 and check for a leftover rule or a CDN redirect.

====================================================================
4. AFTER DEPLOY (same day)
====================================================================
a) sitemap.xml: remove every URL that now redirects. At minimum that is /registration, /registration.html and the four /1st-edition/ slug URLs that returned 302 in audit c1b16b55. List /awards/ with the slash and /delegate/. Submit the sitemap in the new www property.

b) Internal links: list and fix non-www links, then find links that still point at redirecting paths.
   grep -rnE 'https?://worldaisummit\.com' --include='*.html' .
   grep -rlE 'https?://worldaisummit\.com' --include='*.html' . | xargs -r sed -i -E 's#https?://worldaisummit\.com#https://www.worldaisummit.com#g'
   grep -rnE 'href="(https?://www\.worldaisummit\.com)?/(registration(\.html)?|awards|award\.html|nomination|entry-guidelines|partnership(\.html)?|partner-benefits|faqs|thematic-tracks|agenda|delegate-pass|giveaway)"' --include='*.html' .
   Change each match to its final URL: /delegate/, /awards/, /partner-with-us.html, / or /ai-conference-bengaluru-2026.html.

c) 2025 archive pages that stay live (/1st-edition/ and /1st-edition/speakers.html)
   Add this banner directly after <body>:
   <div style="background:#0b1f3a;color:#fff;padding:10px 16px;text-align:center;font-size:15px;line-height:1.4">
     World AI Summit 2026: 14-15 October, Bengaluru. <a href="/delegate/" style="color:#fff;text-decoration:underline">Get your pass</a>
   </div>
   Titles:
     /1st-edition/               <title>World AI Summit 2025 Archive | Bengaluru, 25-26 September 2025</title>
     /1st-edition/speakers.html  <title>World AI Summit 2025 Archive | Speakers</title>
   Meta description for both (this replaces any "Register now" text):
     <meta name="description" content="Archive of World AI Summit 2025 (25-26 Sept 2025, Bengaluru). World AI Summit 2026 is on 14-15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway.">

d) In the www Search Console property, use URL Inspection and Request indexing for https://www.worldaisummit.com/awards/ and https://www.worldaisummit.com/delegate/.

e) Optional, Elets editorial (off-site): 301 events.eletsonline.com/aidemo/registration.html to https://www.worldaisummit.com/delegate/. That page mirrors the homepage and shows a "September 2026" snippet in Google.
