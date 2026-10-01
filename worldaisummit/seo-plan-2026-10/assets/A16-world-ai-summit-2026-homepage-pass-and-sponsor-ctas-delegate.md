# A16: World AI Summit 2026: homepage pass and sponsor CTAs, /delegate/ H1 and price block, 2025-archive banner, one-hop redirects, and GA4 checkout and purchase tracking

- **For recommendation:** Turn the 2,400+ organic homepage visits into pass and sponsor leads, and start measuring pass sales
- **Research lens:** search-console
- **Format:** Implementation pack: HTML/CSS/JS snippets, PHP for success.php, Apache .htaccess and nginx redirect rules, GA4 admin checklist, and email UTM template. Copy is in Indian English.
- **Placeholders the business must fill:**
  - PLACEHOLDER_CURRENT_PASS_PRICE - the one current delegate pass price shown on both the homepage and /delegate/ (Standard expired 30 Sep 2026; marketing decides Late Access or an extension)
  - PLACEHOLDER_PASS_TIER_NAME - name of the current tier, e.g. Late Access
  - PLACEHOLDER_NUMERIC_PRICE - the same price as a plain number for the data-price attribute (e.g. 30000)
  - PLACEHOLDER_VALUE_BASIS - whether GA4 value/price include or exclude GST (use one basis everywhere)
  - PLACEHOLDER_SPONSOR_FORM_URL - the page or anchor holding the partnership form (homepage form anchor or /partnership.html), mailto fallback partnerships@worldaisummit.com
  - PLACEHOLDER_GROUP_DISCOUNT_CONFIRMED - confirm the 10% off for 3+ delegates still applies for 2026 before showing that line
  - PLACEHOLDER_PASS_SALES_CLOSE_DATE - optional; only if marketing sets a closing date
  - PLACEHOLDER_2025_PASS_PAGE_DECISION - 301 /1st-edition/delegate-pass.html to /delegate/ (option A) or keep as archive with pay buttons removed (option B)
  - PLACEHOLDER_CAMPAIGN_NAME - utm_campaign value per email send
  - PLACEHOLDER_LINK_POSITION - optional utm_content value per link in an email

## How to ship

Order of work. Owner: web dev; marketing signs off the price and the sponsor link.

1) Marketing, today: decide PLACEHOLDER_CURRENT_PASS_PRICE / PLACEHOLDER_PASS_TIER_NAME. Standard Access lapsed on 30 Sep, and the homepage Rs 20,000 is stale. Also confirm the group discount, the sponsor form URL, and whether 2025 passes are redirected (option A) or archived (option B).
2) Web dev, by 2 Oct: deploy sections 1-5 (hero, nav, sticky bar, cta_click, /delegate/ H1, intro and single price, begin_checkout) and section 9 banners. If the price is not decided yet, ship the CTAs without the price line.
3) Web dev, by 3 Oct: section 6/7 PHP on success.php and the award success and failure pages. Map $payment_verified, $order_id, $amount_paid, $quantity and $pass_tier to the real gateway variables. Check that the GA4 base tag loads on those pages, then test in DebugView with a sandbox or refunded payment.
4) Server: remove the old /registration 302, add the section 10 rules for Apache or nginx (whichever the host runs), and run the three curl checks.
5) GA4 admin (section 8): add the payment gateway as an unwanted referral and register cta_id.
6) Email team: section 11 UTMs on the next send. This is housekeeping only.
7) Review on 17 Oct using section 12. Pass sales become measurable from the first verified purchase.

No files in the repo were edited, and no paid OpenSEO tools were used. The venue address comes from Apple Maps and Google Hotels, both fetched through Exa on 1 Oct 2026. Event JSON-LD is left out of this pack. It needs the price decision and a verified performer list, so it belongs with the schema work.

On your question about CPUs: this cloud session has 4 CPUs (nproc reports 4). The number cannot be raised from inside the session; a new session starts on a fresh machine.

## Content

WORLD AI SUMMIT 2026 - CTA AND CHECKOUT TRACKING PACK (prepared 1 Oct 2026, ship by 3 Oct 2026)
Venue address verified 1 Oct 2026: Sheraton Grand Bangalore Hotel at Brigade Gateway, 26/1 Dr Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru, Karnataka 560055 (sources: Apple Maps https://maps.apple.com/place?place-id=I4CCAB9B9CD77B6BA and Google Hotels https://www.google.co.in/travel/hotels/entity/CgoItKjz2tvBoZloEAE)

=====================================================================
STEP 0. MARKETING DECISION NEEDED BEFORE ANY PRICE GOES LIVE
=====================================================================
Standard Access (Rs 20,000 / 35,000) expired on 30 Sep 2026. Today /delegate/ shows that expired price and Late Access (Rs 30,000 / 60,000). The homepage still shows "Premium Pass Rs 20,000 / delegate". Marketing must pick ONE current price. Put the same price on both pages:
  PLACEHOLDER_CURRENT_PASS_PRICE   (e.g. "Rs 30,000 + GST" if Late Access applies, or the extended Standard price if Standard is extended)
  PLACEHOLDER_PASS_TIER_NAME       (e.g. "Late Access")
Until this is decided, ship the CTAs below without the price line. Do not copy the homepage price onto /delegate/.

=====================================================================
1. HOMEPAGE HERO CTA BLOCK (www.worldaisummit.com/)
=====================================================================
Leave the existing hero H1 and title unchanged, because the homepage ranks #1 for the brand queries. Add this block directly under the hero heading.

<div class="wais-hero-cta">
  <p class="wais-hero-meta">14-15 October 2026 &middot; Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru</p>
  <p class="wais-hero-sub">Two days, seven tracks, from Frontier Models &amp; Compute to AI for Bharat.</p>
  <div class="wais-hero-buttons">
    <a class="wais-btn wais-btn--primary" href="/delegate/" data-cta="hero_book_pass">Book your Delegate Pass</a>
    <a class="wais-btn wais-btn--secondary" href="PLACEHOLDER_SPONSOR_FORM_URL" data-cta="hero_sponsor">Sponsor or Exhibit</a>
  </div>
  <!-- Show only after Step 0 is decided -->
  <p class="wais-hero-price">Delegate Pass: PLACEHOLDER_CURRENT_PASS_PRICE (PLACEHOLDER_PASS_TIER_NAME)</p>
  <!-- Show only if PLACEHOLDER_GROUP_DISCOUNT_CONFIRMED -->
  <p class="wais-hero-note">Booking for 3 or more delegates? Group bookings get 10% off.</p>
  <p class="wais-hero-note">Sponsorship and exhibition: <a href="mailto:partnerships@worldaisummit.com" data-cta="hero_sponsor_email">partnerships@worldaisummit.com</a></p>
</div>

Accessible long form of the button, for the aria-label or a share card if needed:
"Book your Delegate Pass - World AI Summit 2026, 14-15 Oct, Sheraton Grand Bangalore Hotel at Brigade Gateway"

Rules:
- Use the relative link /delegate/ (with the trailing slash). Never link /registration or /registration.html.
- PLACEHOLDER_SPONSOR_FORM_URL: use the page that already holds the partnership form, which fires partnership_form_submit. That is the homepage form anchor (for example /#partner) if it exists, otherwise /partnership.html. If neither exists, use mailto:partnerships@worldaisummit.com?subject=World%20AI%20Summit%202026%20sponsorship

=====================================================================
2. TOP NAV BUTTON (every page that uses the shared header)
=====================================================================
<a class="wais-nav-cta" href="/delegate/" data-cta="nav_book_pass">Book Pass</a>

=====================================================================
3. STICKY MOBILE CTA BAR (homepage, plus blog and speaker pages if they share the footer)
=====================================================================
<div class="wais-sticky-cta" role="region" aria-label="Book World AI Summit 2026">
  <span class="wais-sticky-text">World AI Summit 2026 &middot; 14-15 Oct, Bengaluru</span>
  <a class="wais-btn wais-btn--primary" href="/delegate/" data-cta="sticky_book_pass">Book Pass</a>
</div>

<style>
.wais-hero-buttons{display:flex;flex-wrap:wrap;gap:12px;margin:16px 0}
.wais-btn{display:inline-block;padding:12px 20px;border-radius:6px;font-weight:600;text-decoration:none;text-align:center}
.wais-btn--primary{background:#c8102e;color:#fff}          /* swap for the site's brand colour */
.wais-btn--secondary{border:2px solid currentColor;color:inherit}
.wais-sticky-cta{display:none}
@media (max-width:768px){
  .wais-sticky-cta{display:flex;align-items:center;justify-content:space-between;gap:12px;
    position:fixed;left:0;right:0;bottom:0;z-index:999;padding:10px 16px;
    padding-bottom:calc(10px + env(safe-area-inset-bottom));background:#111;color:#fff;
    box-shadow:0 -2px 8px rgba(0,0,0,.2)}
  .wais-sticky-text{font-size:14px}
  body{padding-bottom:72px} /* stops the bar from covering the footer */
}
</style>

=====================================================================
4. CTA CLICK TRACKING (sitewide, after the GA4 tag)
=====================================================================
This shows whether the new buttons get clicked and from which channel, without relying on form_submit. form_submit fires on any form through enhanced measurement, so it is not a clean lead count.

<script>
document.addEventListener('click', function (e) {
  var el = e.target.closest ? e.target.closest('[data-cta]') : null;
  if (!el || typeof gtag !== 'function') return;
  gtag('event', 'cta_click', {
    cta_id: el.getAttribute('data-cta'),
    link_url: el.href || '',
    page_location: location.href
  });
});
</script>
GA4: Admin > Custom definitions > create the event-scoped dimension "CTA ID" with event parameter cta_id. Do NOT mark cta_click as a key event.

=====================================================================
5. /delegate/ PAGE
=====================================================================
5a. H1. Put it as the first heading, above the existing H2 "Delegate Passes & Pricing", which stays.
<h1>World AI Summit 2026 Delegate Passes, Bengaluru, 14-15 October</h1>

5b. Intro line under the H1:
<p>Delegate passes for World AI Summit 2026, held on 14-15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, 26/1 Dr Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru 560055. Organised by Elets Technomedia. For group bookings and GST invoices, write to <a href="mailto:registration@worldaisummit.com">registration@worldaisummit.com</a>.</p>

5c. Pricing block. Remove the "Early Bird (valid till 25 Jul 2025)" row. Also remove "Standard Access (Valid till 30th Sept 2026)" unless marketing extends it in Step 0. Show only the current tier:
<div class="wais-price-current">
  <h2>PLACEHOLDER_PASS_TIER_NAME</h2>
  <p class="wais-price">PLACEHOLDER_CURRENT_PASS_PRICE</p>
  <!-- optional, only if marketing sets one: <p>Pass sales close on PLACEHOLDER_PASS_SALES_CLOSE_DATE.</p> -->
  <!-- keep the existing pay button here, with the data attributes from 5d added -->
</div>
On the same release, update the homepage "Three release phases / Premium Pass Rs 20,000 / delegate" block to the same price.

5d. begin_checkout. Add these attributes to each existing pay button or link. Use one per pass type and keep the existing href and onclick:
  data-ga-checkout data-pass-name="Delegate Pass 2026" data-pass-tier="PLACEHOLDER_PASS_TIER_NAME" data-price="PLACEHOLDER_NUMERIC_PRICE"
  (PLACEHOLDER_NUMERIC_PRICE is a number with no "Rs" or commas, e.g. 30000. Use the same GST basis as purchase in 6b.)

<script>
document.querySelectorAll('[data-ga-checkout]').forEach(function (btn) {
  btn.addEventListener('click', function () {
    if (typeof gtag !== 'function') return;
    var price = parseFloat(btn.getAttribute('data-price')) || 0;
    gtag('event', 'begin_checkout', {
      currency: 'INR',
      value: price,
      items: [{
        item_id: 'WAIS2026-DELEGATE',
        item_name: btn.getAttribute('data-pass-name') || 'Delegate Pass 2026',
        item_variant: btn.getAttribute('data-pass-tier') || '',
        price: price,
        quantity: 1
      }]
    });
  });
});
</script>

=====================================================================
6. PURCHASE ON /delegate/success.php
=====================================================================
6a. The one-line version requested in the recommendation:
gtag('event','purchase',{transaction_id:'<order id>',value:<amount>,currency:'INR',items:[{item_name:'Delegate Pass 2026'}]});

6b. Version to ship. It only fires on a verified payment, never on a page refresh, and the values are safely escaped. Map the four right-hand variables to whatever success.php already reads from the gateway response.

<?php
if (session_status() !== PHP_SESSION_ACTIVE) { session_start(); }

// Fire only after success.php has verified the gateway response
// (checksum/signature check) and marked the order as paid.
$ga_paid     = !empty($payment_verified);          // existing verified-payment flag
$ga_order_id = (string) $order_id;                 // gateway order / transaction ID, unique per payment
$ga_value    = round((float) $amount_paid, 2);     // PLACEHOLDER_VALUE_BASIS: total incl. or excl. GST, same basis as 5d
$ga_qty      = max(1, (int) ($quantity ?? 1));     // number of delegates in the order
$ga_tier     = (string) ($pass_tier ?? '');        // e.g. PLACEHOLDER_PASS_TIER_NAME

$ga_send = $ga_paid && $ga_order_id !== '' && empty($_SESSION['ga_purchase_sent'][$ga_order_id]);
if ($ga_send) { $_SESSION['ga_purchase_sent'][$ga_order_id] = true; }
?>
<?php if ($ga_send): ?>
<script>
gtag('event', 'purchase', <?= json_encode([
  'transaction_id' => $ga_order_id,
  'value'          => $ga_value,
  'currency'       => 'INR',
  'items'          => [[
    'item_id'      => 'WAIS2026-DELEGATE',
    'item_name'    => 'Delegate Pass 2026',
    'item_variant' => $ga_tier,
    'price'        => round($ga_value / $ga_qty, 2),
    'quantity'     => $ga_qty,
  ]],
], JSON_HEX_TAG | JSON_HEX_APOS | JSON_HEX_QUOT | JSON_HEX_AMP) ?>);
</script>
<?php endif; ?>

Check that success.php loads the GA4 base tag (gtag.js with the web stream's G- measurement ID) ABOVE this script. If it does not, the event is silently lost. If the site uses Google Tag Manager rather than gtag.js, push the same object with dataLayer.push({event:'purchase', ecommerce:{...}}) and fire a GA4 event tag on it.

=====================================================================
7. AWARD PAYMENTS
=====================================================================
7a. Award success page. Confirm the file name; it is probably /awards/success.php. Use the same PHP as 6b with these item values:
    'item_id' => 'WAIS2026-AWARD', 'item_name' => 'World AI Awards 2026 Nomination', 'item_category' => 'Award nomination'
    (Use the same GST basis as delegate passes. Keep a separate item_id so award revenue can be split from pass revenue.)

7b. /awards/failed.php, and the delegate failure page if there is one:
<script>
if (typeof gtag === 'function') {
  gtag('event', 'payment_failed', {
    payment_type: 'award_nomination',            // use 'delegate_pass' on the delegate failure page
    transaction_id: <?= json_encode((string) ($order_id ?? ''), JSON_HEX_TAG) ?>
  });
}
</script>
Do NOT mark payment_failed as a key event.

=====================================================================
8. GA4 ADMIN (property 490291049), 15 minutes
=====================================================================
a) Admin > Data streams > web stream > Configure tag settings > List unwanted referrals: add the payment gateway domain(s). Find them in Reports > Acquisition > Traffic acquisition, filtered to landing page /delegate/success.php or /awards/failed.php, dimension Session source. This stops gateway returns from starting new "referral" sessions and from taking credit for the sale.
b) "purchase" is already a key event (created 23 May 2025); leave it. Do not mark begin_checkout or cta_click as key events.
c) Register the custom dimension cta_id (section 4).
d) Recommended clean-up, separate from this release: add an explicit generate_lead event with form_id ('delegate_enquiry' / 'sponsor_enquiry') on the real lead forms. Run it alongside form_submit for 2 weeks, then use generate_lead as the lead key event instead of the generic form_submit.
e) Test before 3 Oct in DebugView (Admin > DebugView, with Tag Assistant connected). Pay in the gateway's test or sandbox mode, or refund a small live test payment, and check that purchase appears once with the right transaction_id, value and currency INR. Then reload success.php and check that no second purchase fires.

=====================================================================
9. 2025 ARCHIVE PAGES (/1st-edition/)
=====================================================================
9a. Banner at the top of /1st-edition/ and every page under it:
<div class="wais-archive-banner" role="note">
  You are viewing the 2025 edition archive. World AI Summit 2026 takes place on 14-15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru.
  <a href="/delegate/" data-cta="archive_banner_book_pass">Book your 2026 Delegate Pass</a>
</div>
<style>.wais-archive-banner{background:#fff4d6;color:#222;padding:12px 16px;text-align:center;font-size:15px}.wais-archive-banner a{font-weight:600;margin-left:8px}</style>

9b. /1st-edition/delegate-pass.html (titled "World AI Summit 2025", shows Rs 30,000 / 60,000). PLACEHOLDER_2025_PASS_PAGE_DECISION. Choose one:
  Option A (recommended): 301 it to /delegate/ (rules in section 10) so nobody can buy a 2025 pass.
  Option B: keep the page as an archive, add the 9a banner, and remove or disable its pay buttons and payment form.

=====================================================================
10. ONE-HOP REDIRECTS (fixes the 3-hop /registration chain)
=====================================================================
Today /registration takes 3 hops: non-www -> www -> non-www / -> www /. /registration.html takes 2 hops. The new rules send registration-intent URLs straight to the pass page in one hop. First remove the existing 302 for /registration (look in .htaccess, the server config, and any PHP header() or meta refresh in registration.html).

--- Apache (.htaccess at the web root; the order matters) ---
RewriteEngine On

# 1) Retired URLs go straight to the final URL, whatever the host or scheme
RewriteRule ^registration(\.html)?/?$ https://www.worldaisummit.com/delegate/ [R=301,L,NC]
# Option A from 9b only:
RewriteRule ^1st-edition/delegate-pass\.html$ https://www.worldaisummit.com/delegate/ [R=301,L,NC]

# 2) Host and scheme canonical: everything else goes to https://www
RewriteCond %{HTTP_HOST} !^www\.worldaisummit\.com$ [NC,OR]
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://www.worldaisummit.com/$1 [R=301,L]
# If the site sits behind a CDN or load balancer that ends TLS, %{HTTPS} is always "off".
# In that case replace "RewriteCond %{HTTPS} off" with:
# RewriteCond %{HTTP:X-Forwarded-Proto} !https

--- nginx ---
# /etc/nginx/snippets/wais-redirects.conf
rewrite (?i)^/registration(\.html)?/?$ https://www.worldaisummit.com/delegate/ permanent;
# Option A from 9b only:
rewrite (?i)^/1st-edition/delegate-pass\.html$ https://www.worldaisummit.com/delegate/ permanent;

# Non-www and all http: the include comes BEFORE the catch-all return
server {
    listen 80;
    listen [::]:80;
    server_name worldaisummit.com www.worldaisummit.com;
    include snippets/wais-redirects.conf;
    return 301 https://www.worldaisummit.com$request_uri;
}
server {
    listen 443 ssl;
    listen [::]:443 ssl;
    server_name worldaisummit.com;
    # ssl_certificate ... (existing)
    include snippets/wais-redirects.conf;
    return 301 https://www.worldaisummit.com$request_uri;
}
# Canonical https://www server: add the include at server level, above the location blocks
server {
    listen 443 ssl;
    listen [::]:443 ssl;
    server_name www.worldaisummit.com;
    # ssl_certificate ... (existing)
    include snippets/wais-redirects.conf;
    # ... existing root / location blocks ...
}
Test: nginx -t && systemctl reload nginx

Verify after deploy (each should be exactly one 301 to https://www.worldaisummit.com/delegate/):
curl -sI http://worldaisummit.com/registration | grep -iE '^(HTTP|location)'
curl -sI https://worldaisummit.com/registration.html | grep -iE '^(HTTP|location)'
curl -sI https://www.worldaisummit.com/registration | grep -iE '^(HTTP|location)'

=====================================================================
11. EMAIL LINKS SENT THROUGH r.emails.elets.in (housekeeping; it adds no leads)
=====================================================================
Add the tags to the DESTINATION URL inside the email tool, before the click-tracker wraps it:
https://www.worldaisummit.com/delegate/?utm_source=elets_newsletter&utm_medium=email&utm_campaign=wais2026_PLACEHOLDER_CAMPAIGN_NAME&utm_content=PLACEHOLDER_LINK_POSITION
(lower case only, no spaces; use one utm_campaign per send)
This only moves those sessions from Referral to Email in reports. The current 213,013 referral sessions (209,188 users, 34% engagement) probably include many link-scanner or bot clicks, so do not read them as real visits or leads.

=====================================================================
12. HOW TO JUDGE THE CHANGE (from 3 Oct, review on 17 Oct)
=====================================================================
- Main measures: purchase count and revenue (new; today 0), begin_checkout, and cta_click by cta_id and by Session default channel group.
- Do not expect homepage visitors to convert like /delegate/'s 16.7% session rate. Those 16 form_submits came from 7 users, and /delegate/ visitors mostly arrive from ticket-intent email and ad links.
- Most homepage sessions come from email and direct traffic (110,201 homepage sessions across all channels against 2,446 organic), so most of the effect of the hero CTA will show up outside Organic Search.
