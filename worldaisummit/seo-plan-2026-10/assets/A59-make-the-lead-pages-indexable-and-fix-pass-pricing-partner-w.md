# A59: Make the lead pages indexable and fix pass pricing: /partner-with-us.html, /delegate/, homepage, /speaker.html, internal links (World AI Summit 2026)

- **For recommendation:** Make the three lead pages indexable and linked: self-canonical /partner-with-us.html, H1 and nav links for /delegate/ and /awards/
- **Research lens:** tech-indexing
- **Format:** HTML head and body snippets, find-and-replace steps, Event JSON-LD, Apache .htaccess and nginx redirects, link fixes, and a checklist
- **Placeholders the business must fill:**
  - PLACEHOLDER_PREMIUM_PRICE_FROM_1_OCT (and _NUMBER_ONLY in JSON-LD): Premium pass price at checkout from 1 Oct; live and indexed versions show Rs 15,000, Rs 20,000 and Rs 30,000
  - PLACEHOLDER_VIP_PRICE_FROM_1_OCT (and _NUMBER_ONLY in JSON-LD): VIP pass price at checkout from 1 Oct; live and indexed versions show Rs 25,000, Rs 35,000 and Rs 60,000
  - PLACEHOLDER_GST_INCLUSIVE_OR_PLUS_GST: whether the shown prices include GST
  - PLACEHOLDER_SEATS_LEFT: optional, only if a real number exists
  - PLACEHOLDER_LOWEST_CURRENT_PASS_PRICE: only if speaker-page metas keep a price (recommended: no price)
  - PLACEHOLDER_EVENT_IMAGE_URL_1200x630: event image for the JSON-LD
  - PLACEHOLDER_PARTNER_DECK_URL: sponsorship brochure link, or delete the line
  - PLACEHOLDER_EXISTING_BUTTON_CLASS: keep the current CTA styling
  - PLACEHOLDER_FINAL_FAQ_URL and PLACEHOLDER_FINAL_AI_DIALOGUES_URL: final www URLs for /faqs and /ai-dialogues
  - PLACEHOLDER_CONFIRM_PARTNERSHIP_AND_AWARD_HTML_ARE_DUPLICATES: go/no-go on the optional 301s
  - PLACEHOLDER_DEPLOY_DATE_YYYY-MM-DD: sitemap lastmod

## How to ship

1) Marketing (15 min, today): confirm the Premium and VIP prices that checkout charges from 1 Oct, whether prices include GST, the event image URL, and whether /partnership.html and /award.html are duplicates. Fill in every PLACEHOLDER_. 2) Web dev (1-2 h, by 3 Oct): make the edits in the static HTML source in this order: sections 1-3 (partner head/H1, delegate H1/pricing/JSON-LD, homepage meta/price/nav), 5-6 (speaker metas), 4 (the link fix across the site, run on a copy first), then 7 (redirects; use either the Apache or the nginx version to match the server). Upload, then run the section 9 checks, and grep the live HTML for "PLACEHOLDER_" to make sure none are left. 3) DNS owner: add a Domain property in Search Console, submit the sitemap, and request indexing for /partner-with-us.html and /delegate/ (section 8). 4) Before running build_speakers.py, update pass_from and pass_price_inr in worldaisummit/speakers/speakers.json. Nothing in the repo was edited. All checks used free tools only (Exa fetch and WebSearch; no paid OpenSEO tools). On the relayed user question: this container reports 4 CPUs (nproc); a subagent cannot add more.

## Content

WORLD AI SUMMIT 2026: LEAD-PAGE FIX PACK (prepared 1 Oct 2026, ship by 3 Oct 2026)
Site: https://www.worldaisummit.com/ (static HTML). Owners: web dev (1-2 h) and marketing (15 min to confirm prices).

This pack uses the verifier's corrections. The partner page already has an H1, so we replace it rather than add one. Its title is the old homepage title. The pages are not true orphans, so the link fix is to change non-www absolute links to relative www links. There are at least three pass-price versions in the wild, so every price below is a PLACEHOLDER until marketing confirms it against checkout.

================================================================
1. /partner-with-us.html  (sponsor and exhibitor lead page)
================================================================
Current state (Exa fetch, 1 Oct):
- title: "World AI Summit 2026 | Global Artificial Intelligence Conference by Elets Technomedia" (the old homepage title)
- meta description: the homepage's 182-character meta
- canonical: https://www.worldaisummit.com/
- H1: "World AI Summit Partner Benefits"
- 219 words

1a. In <head>, REPLACE the existing <title>, meta description, canonical and any og:title/og:description/og:url lines with:

<title>Sponsor or Exhibit at World AI Summit 2026, Bengaluru</title>
<meta name="description" content="Sponsorship and exhibition packages for World AI Summit 2026, 14-15 Oct, Sheraton Grand Bangalore at Brigade Gateway. Email partnerships@worldaisummit.com.">
<link rel="canonical" href="https://www.worldaisummit.com/partner-with-us.html">
<meta property="og:title" content="Sponsor or Exhibit at World AI Summit 2026, Bengaluru">
<meta property="og:description" content="Sponsorship and exhibition packages for World AI Summit 2026, 14-15 Oct, Sheraton Grand Bangalore at Brigade Gateway. Email partnerships@worldaisummit.com.">
<meta property="og:url" content="https://www.worldaisummit.com/partner-with-us.html">
(Title 53 characters, description 155 characters.)

Check there is no <meta name="robots" content="noindex"> on the page and that the page has exactly one canonical tag.

1b. Body. REPLACE the existing H1 (keep exactly one H1 on the page):
FIND:     <h1 ...>World AI Summit Partner Benefits</h1>
REPLACE:  <h1>Partner with World AI Summit 2026</h1>
          <h2>Partner benefits</h2>
(Keep the existing classes on the new H1 so the styling does not change.)

1c. Optional intro paragraph, placed directly under the H1. It adds about 90 words of factual copy and uses only confirmed facts:

<p>World AI Summit 2026 takes place on 14-15 October 2026 at the Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. Organised by Elets Technomedia, the summit runs seven tracks: Frontier Models &amp; Compute; Sovereign AI &amp; Geopolitics; Enterprise AI in Production; GCCs; Robotics, Agents &amp; Embodied AI; AI for Bharat; and Capital, Founders &amp; Exits. Partners can sponsor, exhibit, take a speaking slot, host one-on-one meetings and executive roundtables, or feature in the AI Innovation Report launched at the summit. To discuss packages, write to <a href="mailto:partnerships@worldaisummit.com">partnerships@worldaisummit.com</a>.</p>
<p><a href="PLACEHOLDER_PARTNER_DECK_URL">Download the sponsorship and exhibition brochure</a></p>   (delete this line if there is no brochure)

1d. sitemap.xml. Add this entry, or update it if it is already there:
<url><loc>https://www.worldaisummit.com/partner-with-us.html</loc><lastmod>PLACEHOLDER_DEPLOY_DATE_YYYY-MM-DD</lastmod></url>

================================================================
2. /delegate/  (pass page: missing H1, out-of-date price rows)
================================================================
Current state (Exa fetch, 1 Oct): title "World AI Summit 2026 | Delegate Pass Registration" (49 characters, keep it). There is no H1. The pricing grid shows:
- an Early Bird row "Valid till 25th July 2025" (expired)
- a Standard Access row Rs 20,000/35,000 "Valid till 30th Sept 2026" (expired as of today)
- a Late Access row Rs 30,000/60,000

2a. <head>. Keep the title. Add or replace the following:
<meta name="description" content="Delegate passes for World AI Summit 2026, 14-15 Oct, Sheraton Grand Bangalore: Premium and VIP passes, 10% off for groups of 3 or more. Book online.">
<link rel="canonical" href="https://www.worldaisummit.com/delegate/">
(Description 148 characters. It has no price on purpose, so it cannot go out of date again.)

2b. Add an H1 at the top of the hero, above the "AI For All..." tagline. Turn the tagline into a <p> if it is currently a heading:
<h1>World AI Summit 2026 Delegate Passes</h1>
<p>AI For All: Accelerating India's Journey Towards Inclusive, Responsible and Future-Ready AI. 14-15 October 2026, Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru.</p>
Keep "Delegate Passes & Pricing" as the H2.

2c. Pricing grid:
DELETE the row "Early Bird Offer Limited to the First 150 Passes (Valid till 25th July 2025)" and its Rs 20,000/Rs 35,000 "Save Rs 5,000" cells.
DELETE the row "Standard Access (Valid till 30th Sept 2026)" and its Rs 20,000/Rs 35,000 cells.
REPLACE the "Late Access" row with:
  Row label: Current price (from 1 October 2026)
  Premium Pass: Rs PLACEHOLDER_PREMIUM_PRICE_FROM_1_OCT
  VIP Pass:     Rs PLACEHOLDER_VIP_PRICE_FROM_1_OCT
  Note under the grid: <p>Prices are PLACEHOLDER_GST_INCLUSIVE_OR_PLUS_GST. Booking for three or more delegates? Groups of 3+ get 10% off. Write to <a href="mailto:registration@worldaisummit.com">registration@worldaisummit.com</a>.</p>
  Optional, only if marketing wants it and the number is real: <p>PLACEHOLDER_SEATS_LEFT passes left at this price.</p>

Marketing must confirm the price, because four versions are live or indexed:
- homepage "Secure your seat": Premium Rs 20,000
- /delegate/ Late Access: Rs 30,000 / Rs 60,000
- indexed snippets: "Was Rs 20,000, now Rs 15,000" (Premium) and "Was Rs 35,000, now Rs 25,000" (VIP)
- the checkout amount
Use the checkout amount everywhere: on /delegate/, the homepage, the speaker-page metas and the JSON-LD.

2d. Event JSON-LD for /delegate/. Paste it before </head>. Replace both price placeholders with plain numbers (for example "30000") before publishing. If the homepage already carries Event JSON-LD with the same @id, keep the two blocks identical.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Event",
  "@id": "https://www.worldaisummit.com/#event-2026",
  "name": "World AI Summit 2026",
  "description": "Two-day AI conference in Bengaluru organised by Elets Technomedia, with seven tracks: Frontier Models & Compute; Sovereign AI & Geopolitics; Enterprise AI in Production; GCCs; Robotics, Agents & Embodied AI; AI for Bharat; Capital, Founders & Exits.",
  "url": "https://www.worldaisummit.com/",
  "image": ["PLACEHOLDER_EVENT_IMAGE_URL_1200x630"],
  "startDate": "2026-10-14",
  "endDate": "2026-10-15",
  "eventStatus": "https://schema.org/EventScheduled",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
  "inLanguage": "en-IN",
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
  "organizer": {
    "@type": "Organization",
    "name": "Elets Technomedia",
    "url": "https://www.eletsonline.com/"
  },
  "performer": [
    {"@type": "Person", "name": "Pankaj Kumar Pandey", "honorificSuffix": "IAS", "jobTitle": "Principal Secretary, e-Governance", "affiliation": {"@type": "GovernmentOrganization", "name": "Government of Karnataka"}},
    {"@type": "Person", "name": "T Bhoobalan", "honorificSuffix": "IAS", "jobTitle": "CEO, Centre for e-Governance", "affiliation": {"@type": "GovernmentOrganization", "name": "Government of Karnataka"}},
    {"@type": "Person", "name": "Sanjeev Gupta", "jobTitle": "CEO", "affiliation": {"@type": "Organization", "name": "Karnataka Digital Economy Mission"}},
    {"@type": "Person", "name": "Ram Mohan Rao", "jobTitle": "Executive Director", "affiliation": {"@type": "GovernmentOrganization", "name": "Securities and Exchange Board of India (SEBI)"}}
  ],
  "offers": [
    {"@type": "Offer", "name": "Premium Pass", "url": "https://www.worldaisummit.com/delegate/", "price": "PLACEHOLDER_PREMIUM_PRICE_FROM_1_OCT_NUMBER_ONLY", "priceCurrency": "INR", "availability": "https://schema.org/InStock", "validFrom": "2026-10-01"},
    {"@type": "Offer", "name": "VIP Pass", "url": "https://www.worldaisummit.com/delegate/", "price": "PLACEHOLDER_VIP_PRICE_FROM_1_OCT_NUMBER_ONLY", "priceCurrency": "INR", "availability": "https://schema.org/InStock", "validFrom": "2026-10-01"}
  ]
}
</script>
Notes:
- The venue address is 26/1 Dr. Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru 560055 (verified via web search: Marriott/hotel listing results, 1 Oct).
- The four performers are marked confirmed_2026 in the repo's worldaisummit/speakers/speakers.json. Before publishing, check that each one also appears on the live /speaker.html, and delete any who do not. Add no other names.
- If passes sell out, change "availability" to "https://schema.org/SoldOut". If few are left, use "https://schema.org/LimitedAvailability".

================================================================
3. Homepage /
================================================================
3a. Replace the 182-character meta description (156 characters):
<meta name="description" content="World AI Summit 2026, 14-15 Oct, Sheraton Grand Bangalore: seven tracks on frontier models, sovereign AI, enterprise AI, GCCs and AI for Bharat. Get passes.">
(This uses the hotel's own name, "Sheraton Grand Bangalore", instead of "Sheraton Grand Bengaluru". The length is the same.)
Keep the current title "World AI Summit 2026 | AI Summit India, Bengaluru, 14-15 October".

3b. "Secure your seat" block:
FIND:    Premium Pass ... Rs 20,000   (or ₹20,000)
REPLACE: Premium Pass ... Rs PLACEHOLDER_PREMIUM_PRICE_FROM_1_OCT
Make sure the block's button is a plain link:
<a href="/delegate/" class="PLACEHOLDER_EXISTING_BUTTON_CLASS">See passes and prices</a>

3c. Navigation. Use plain links: no JS onclick, and no "https://worldaisummit.com/..." absolute URLs.
<a href="/delegate/">Delegate passes</a>
<a href="/speaker.html">Speakers</a>
<a href="/awards/">World AI Awards</a>
<a href="/partner-with-us.html">Partner with us</a>

3d. Awards block. Link it with <a href="/awards/">Nominate for the World AI Awards</a>.
3e. Footer, next to partnerships@worldaisummit.com, add: <a href="/partner-with-us.html">Sponsorship and exhibition packages</a>

================================================================
4. Site-wide link fix (non-www absolute links to relative www links)
================================================================
The crawl found non-www URLs (worldaisummit.com/awards, /faqs, /partnership, /registration, /ai-dialogues) that 301 to www. GSC also lists the www homepage as a referrer of non-www /awards and /faqs. Find every such link in the site source:

grep -rnoE 'href="https?://worldaisummit\.com[^"]*"' --include='*.html' .
grep -rnoE 'onclick="[^"]*(location|window\.open)[^"]*"' --include='*.html' .

Rewrite them to relative paths with the final URL, so no link goes through a redirect:
  https://worldaisummit.com/awards        -> /awards/
  https://worldaisummit.com/registration  -> /delegate/
  https://worldaisummit.com/partnership   -> /partner-with-us.html
  https://worldaisummit.com/faqs          -> PLACEHOLDER_FINAL_FAQ_URL  (check where www /faqs resolves)
  https://worldaisummit.com/ai-dialogues  -> PLACEHOLDER_FINAL_AI_DIALOGUES_URL
Bulk version, which strips the host only. Run it on a copy, then add trailing slashes to the directory URLs:
sed -i -E 's#href="https?://worldaisummit\.com/#href="/#g' $(grep -rlE 'href="https?://worldaisummit\.com/' --include='*.html' .)

Also add <a href="/delegate/">Book your delegate pass</a> to /ai-conference-bengaluru-2026.html, to every /blog/ post and to every speaker page (/assets/speaker_details/*.html).

================================================================
5. /speaker.html meta (it currently duplicates the homepage's 182-character meta)
================================================================
<meta name="description" content="Speakers at World AI Summit 2026, 14-15 Oct, Bengaluru: government leaders, enterprise and GCC heads, founders and investors. See the 2026 line-up.">
(147 characters)

================================================================
6. Speaker-page metas that say "Passes from Rs 20,000"
================================================================
These are found in: anand-thakur, deepika-sandeep, ganesh-joshi, kuldeep-t, pranav-saxena, praveen-bist, ram-mohan-rao, suman-dash, rajesh-choudhary, sushan-rungta (/assets/speaker_details/<slug>.html).
FIND:    Passes from Rs 20,000
REPLACE (recommended, cannot go out of date): See delegate passes
or, once the price is confirmed: Passes from Rs PLACEHOLDER_LOWEST_CURRENT_PASS_PRICE
grep -rln 'Passes from Rs 20,000' --include='*.html' .
The undeployed generator in the repo (worldaisummit/speakers/speakers.json) still has "pass_from": "Rs 20,000" and "pass_price_inr": 20000. Update both to the confirmed price before running build_speakers.py.

================================================================
7. Redirects (one hop each, all 301). Place these ABOVE the existing host rule.
================================================================
Fixes /registration and /registration.html. Today they 302 to the homepage through non-www (3 hops). The "ai summit registration" query is at #4 with 1,300 searches a month, so they should land on the pass page.
The two optional lines fold the duplicate pages that are canonicalised to / into their live equivalents. Use them only after a dev confirms those pages duplicate /partner-with-us.html and /awards/: PLACEHOLDER_CONFIRM_PARTNERSHIP_AND_AWARD_HTML_ARE_DUPLICATES.

Apache (.htaccess in the web root):
RewriteEngine On
RewriteRule ^registration(\.html)?/?$ https://www.worldaisummit.com/delegate/ [R=301,L,NC]
# optional, after confirmation:
RewriteRule ^partnership(\.html)?/?$ https://www.worldaisummit.com/partner-with-us.html [R=301,L,NC]
RewriteRule ^award\.html$ https://www.worldaisummit.com/awards/ [R=301,L,NC]
RewriteRule ^awards$ https://www.worldaisummit.com/awards/ [R=301,L,NC]
# host canonicalisation (keep the existing rule if it already does this in one hop):
RewriteCond %{HTTP_HOST} !^www\.worldaisummit\.com$ [NC,OR]
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://www.worldaisummit.com/$1 [R=301,L]
(Behind a CDN or proxy that ends TLS, replace the %{HTTPS} condition with RewriteCond %{HTTP:X-Forwarded-Proto} !https.)

nginx:
# non-www host: send path-specific URLs straight to the final www URL, everything else to www
server {
    listen 80; listen 443 ssl;
    server_name worldaisummit.com;
    # ssl_certificate lines as currently configured
    location ~* ^/registration(\.html)?/?$ { return 301 https://www.worldaisummit.com/delegate/; }
    location ~* ^/partnership(\.html)?/?$  { return 301 https://www.worldaisummit.com/partner-with-us.html; }   # optional
    location = /awards                     { return 301 https://www.worldaisummit.com/awards/; }
    location /                             { return 301 https://www.worldaisummit.com$request_uri; }
}
# inside the existing www HTTPS server block:
location ~* ^/registration(\.html)?/?$ { return 301 https://www.worldaisummit.com/delegate/; }
location = /partnership.html           { return 301 https://www.worldaisummit.com/partner-with-us.html; }   # optional
location = /award.html                 { return 301 https://www.worldaisummit.com/awards/; }                 # optional
If the optional redirects are not used, change the canonical on /partnership.html and /award.html to point to themselves (or to /partner-with-us.html and /awards/), not to the homepage.

================================================================
8. Search Console dependency (not in the original recommendation)
================================================================
GSC currently has only the non-www URL-prefix property (https://worldaisummit.com/), which shows 2 pages and 0 rows for "sponsor". Nobody can see search data for the www pages or use "Request indexing" on them.
Whoever controls DNS should add a Domain property for worldaisummit.com (DNS TXT record), or at minimum a URL-prefix property for https://www.worldaisummit.com/. After that:
- Submit https://www.worldaisummit.com/sitemap.xml.
- Run URL Inspection and "Request indexing" on /partner-with-us.html and /delegate/.
- Track the query "world ai summit sponsorship" (volume and position are unknown today).

================================================================
9. Post-deploy checks (5 minutes)
================================================================
curl -sI https://worldaisummit.com/registration          -> one 301 to https://www.worldaisummit.com/delegate/
curl -sI https://www.worldaisummit.com/registration.html -> one 301 to /delegate/
curl -s https://www.worldaisummit.com/partner-with-us.html | grep -iE '<title>|rel="canonical"|<h1'
curl -s https://www.worldaisummit.com/delegate/ | grep -ciE '<h1'   -> 1
curl -s https://www.worldaisummit.com/delegate/ | grep -iE '2025|30th Sept'   -> no pricing matches
Google Rich Results Test on https://www.worldaisummit.com/delegate/ -> Event detected, no errors
Make sure "PLACEHOLDER_" appears nowhere in the live HTML.

Sources: OpenSEO audit c1b16b55 and GSC (non-www property) via the verifier. Exa fetches of /partner-with-us.html and /delegate/ (1 Oct 2026). Venue address from web search: https://www.marriott.com/en-us/hotels/blrgs-sheraton-grand-bangalore-hotel-at-brigade-gateway/overview/ and https://www.hotelplanner.com/Hotels/178731/Reservations-Sheraton-Bangalore-Hotel-at-Brigade-Gateway-Bangalore-26-1-Dr-Rajkumar-Rd-Malleswaram-Rajajinagar-560055
