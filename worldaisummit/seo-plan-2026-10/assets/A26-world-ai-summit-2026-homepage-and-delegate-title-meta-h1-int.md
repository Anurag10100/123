# A26: World AI Summit 2026: homepage and /delegate/ title, meta, H1, internal links and /registration redirect

- **For recommendation:** Rewrite the homepage and /delegate/ titles and meta descriptions around date and registration to win more clicks on 'AI summit 2026' searches, where the other results cover a summit that ended in February
- **Research lens:** serp-features
- **Format:** HTML head and body snippets, Apache .htaccess and nginx rules, plus copy notes (plain text)
- **Placeholders the business must fill:**
  - PLACEHOLDER_LIVE_LOWEST_PASS_PRICE
  - PLACEHOLDER_LIVE_PREMIUM_PRICE
  - PLACEHOLDER_LIVE_VIP_PRICE
  - PLACEHOLDER_LIVE_TIER_NAME
  - PLACEHOLDER_KEEP_OR_CLOSE
  - PLACEHOLDER_YES_NO
  - PLACEHOLDER_EXISTING_BUTTON_CLASS
  - PLACEHOLDER_EXISTING_H2_CLASS
  - PLACEHOLDER_CONFIRM_REGISTRATION_URL_UNUSED
  - PLACEHOLDER_TITLE_OWNER_DECISION

## How to ship

Web dev, about 45 minutes, by 3 Oct 2026. (1) Edit the <head> of the homepage HTML (index.html serves both / and /index.html) and of /delegate/index.html with the title, meta and og tags above. Replace whatever <title> is live: the 1 Oct audit recorded 'World AI Summit 2026 | AI Summit India, Bengaluru, 14-15 October' (64), but an Exa fetch on 1 Oct returned 'World AI Summit 2026 | Global Artificial Intelligence Conference by Elets Technomedia', so check the file. (2) On /delegate/, change the first H2 to the H1 and keep its CSS class. (3) Point the nav, the 'Secure your seat' block and every Register button to /delegate/. (4) Optionally add the /registration 301, Apache or nginx depending on the host, after removing the old 302 rule, and test with curl. (5) Get the registration team's sign-off on the live price before using the price version of the meta or editing the pricing cards. Until then ship the no-price meta, which is factual today. (6) Afterwards, run URL Inspection and request indexing for / and /delegate/ in Search Console. The www property is not verified, so add the Domain property (DNS TXT) first; without it you can't measure the CTR before and after the change. Facts used: dates, venue, seven tracks, World AI Awards, Premium/VIP passes and the 3+ group 10% discount come from the live homepage and /delegate/ (Exa fetch, 1 Oct 2026). Cypher 7-9 Oct and the August search volumes come from the verifier's notes. I made no OpenSEO paid calls. A direct curl to the site was blocked by the proxy. Separately, your actual question ('do you have more CPUs from computer?') is outside this task and was not checked here. Ask it again in the main session.

## Content

=== 1. HOMEPAGE  https://www.worldaisummit.com/  (and /index.html, which already canonicalises to /) ===

Replace the existing <title>, meta description, og:title and og:description in <head>:

<title>World AI Summit 2026 | 14-15 Oct Bengaluru | AI Summit India</title>
<meta name="description" content="World AI Summit 2026: 14-15 October, Sheraton Grand Bangalore at Brigade Gateway, Bengaluru. Seven AI tracks, World AI Awards. Groups of 3+ save 10%.">
<meta property="og:title" content="World AI Summit 2026 | 14-15 Oct Bengaluru | AI Summit India">
<meta property="og:description" content="World AI Summit 2026: 14-15 October, Sheraton Grand Bangalore at Brigade Gateway, Bengaluru. Seven AI tracks, World AI Awards. Groups of 3+ save 10%.">

Lengths: title 60, meta 149.
Changes from the original recommendation, and why:
- The date moves ahead of "AI Summit India", so if Google cuts the title at about 56 characters it cuts "India", not the date. "AI Summit India" stays in the title because it is the only title match for 'ai summit india 2026' (110/mo). "Register Now" is dropped: 'ai summit registration' gets 10/mo and 'ai summit 2026 registration' gets 20/mo (Aug 2026, OpenSEO).
- "India's next AI summit" is removed because it is false. Cypher 2026 runs 7-9 Oct in Bengaluru.
- "100+ speakers" is removed because only 50 confirmed 2026 speakers are on record.
- The price is removed until the registration team confirms it (see 4).

Use this meta instead ONLY after the registration team confirms the live lowest pass price (153 characters with a 5-digit price):
<meta name="description" content="World AI Summit 2026: 14-15 October, Sheraton Grand Bangalore, Bengaluru. Seven AI tracks, World AI Awards. Passes from Rs PLACEHOLDER_LIVE_LOWEST_PASS_PRICE; 3+ delegates save 10%.">

Internal links to the pass page. Put them in the "Secure your seat" block, the main nav and every "Register" button. Always use the trailing slash:

<!-- nav -->
<li><a href="/delegate/">Register</a></li>

<!-- "Secure your seat" block, under the pass cards -->
<a class="PLACEHOLDER_EXISTING_BUTTON_CLASS" href="/delegate/">See all passes and register</a>

<!-- every other Register / Book now button on the site -->
<a class="PLACEHOLDER_EXISTING_BUTTON_CLASS" href="/delegate/">Register</a>

Also fix the homepage pass card. It shows "Premium Pass Rs 20,000 / delegate", but /delegate/ says that price was valid only until 30 Sept 2026. Set it to PLACEHOLDER_LIVE_PREMIUM_PRICE.


=== 2. /delegate/  https://www.worldaisummit.com/delegate/ ===

Replace the existing <title> ("World AI Summit 2026 | Delegate Pass Registration", 49) and the meta description (127):

<title>World AI Summit 2026 Passes | 14-15 Oct Bengaluru | Register</title>
<meta name="description" content="Book your World AI Summit 2026 delegate pass: 14-15 October, Sheraton Grand Bangalore at Brigade Gateway. Premium and VIP passes; groups of 3+ save 10%.">
<meta property="og:title" content="World AI Summit 2026 Passes | 14-15 Oct Bengaluru | Register">
<meta property="og:description" content="Book your World AI Summit 2026 delegate pass: 14-15 October, Sheraton Grand Bangalore at Brigade Gateway. Premium and VIP passes; groups of 3+ save 10%.">

Lengths: title 60, meta 152.

Add the page's only H1. Replace the current first heading, <h2>Delegate Passes &amp; Pricing</h2>, with:

<h1 class="PLACEHOLDER_EXISTING_H2_CLASS">World AI Summit 2026 Delegate Passes</h1>
<p>14-15 October 2026, Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. Choose the pass that suits you; groups of 3 or more delegates save 10%.</p>

(H1 is 36 characters. Keep the existing H2 class on the H1 so the design does not change. The page must have only one H1.)

Pricing table on the same page. As of 1 Oct it still shows "Early Bird ... Valid till 25th July 2025" and "Standard Access (Valid till 30th Sept 2026)" next to Late Access Rs 30,000 / Rs 60,000. Once the registration team confirms, mark expired tiers as closed or remove them:
- Standard Access: PLACEHOLDER_KEEP_OR_CLOSE (the published end date was 30 Sept 2026)
- Live tier: PLACEHOLDER_LIVE_TIER_NAME, Premium Rs PLACEHOLDER_LIVE_PREMIUM_PRICE, VIP Rs PLACEHOLDER_LIVE_VIP_PRICE


=== 3. Point the old /registration URLs at the pass page in one hop (optional, recommended) ===

Today /registration and /registration.html return a 302 to the homepage through the non-www host, which takes 3 hops. Send them to /delegate/ with a single 301 instead. First remove or replace the existing rule that sends them to the homepage, and confirm that no live form or campaign depends on /registration: PLACEHOLDER_CONFIRM_REGISTRATION_URL_UNUSED.

Apache (.htaccess at the web root, placed ABOVE any existing www/https and /registration rules):
RewriteEngine On
RewriteRule ^registration(\.html)?/?$ https://www.worldaisummit.com/delegate/ [R=301,L]

nginx (add to BOTH the www and the non-www server blocks, for http and https):
location ~ ^/registration(\.html)?/?$ {
    return 301 https://www.worldaisummit.com/delegate/;
}

Test (each should return one 301 straight to https://www.worldaisummit.com/delegate/):
curl -sI https://worldaisummit.com/registration
curl -sI https://www.worldaisummit.com/registration.html


=== 4. Sign-off needed before publishing ===
- Live lowest pass price, from the registration team (registration@worldaisummit.com): PLACEHOLDER_LIVE_LOWEST_PASS_PRICE
- Whether to use the price version of the homepage meta: PLACEHOLDER_YES_NO
- Choice between this homepage title and the on-page lens's version, if it proposes another one. Ship only one: PLACEHOLDER_TITLE_OWNER_DECISION
