# A51: World AI Summit 2026: sticky pass bar, top ribbon, countdown and stale-price fixes (as of 1 Oct 2026)

- **For recommendation:** Fix stale pricing and copy Cypher's dated price-step urgency, countdown and ticket-page detail
- **Research lens:** competitors
- **Format:** Copy deck (plain text) + drop-in HTML/CSS/JS snippet + Apache .htaccess and nginx redirect rules
- **Placeholders the business must fill:**
  - PLACEHOLDER_PREMIUM_PRICE (current Premium pass price; /delegate/ shows Late Access Rs 30,000 as of 1 Oct 2026, checkout unverified)
  - PLACEHOLDER_VIP_PRICE (current VIP pass price; /delegate/ shows Late Access Rs 60,000 as of 1 Oct 2026, checkout unverified)
  - PLACEHOLDER_GST_LABEL (short bar label, e.g. '+ 18% GST' or 'incl. GST'; not stated anywhere on the site today)
  - PLACEHOLDER_GST_LINE (line under each price on /delegate/)
  - PLACEHOLDER_GST_ANSWER (FAQ answer on GST)
  - PLACEHOLDER_DAY2_CLOSE_TIME (IST time day 2 ends on 15 Oct; script uses 18:00 until confirmed)
  - PLACEHOLDER_PASS_INCLUSIONS (what Premium and VIP each include)
  - PLACEHOLDER_TRANSFER_POLICY (whether and how a pass can be transferred)
  - PLACEHOLDER_CONFIRMATION_PROCESS (what a buyer receives after registering and how badges are collected)
  - Business decision: Variant A (price-led) or Variant B (urgency-led), given Cypher now undercuts on price
  - Business decision: 301 /1st-edition/delegate-pass.html to /delegate/, or keep it as a noindex archive
  - Business decision (separate from this asset): tiered group discounts (3-5 / 6-10 / 11+) and a 1-day pass, as Cypher offers

## How to ship

1) The pricing owner at Elets fills the placeholders: current Premium and VIP price, the GST treatment, the time day 2 closes, and the four FAQ answers. They also choose Variant A or B. Check the price against a real checkout first: nobody has yet confirmed that Late Access at Rs 30,000 / Rs 60,000 is what gets charged. 2) The web dev pastes the ribbon after <body> and the bar, style and script before </body> in the shared include, or on every static HTML page if there is no include. They swap in the brand colours. 3) In the same upload, apply the /delegate/ H1 and pricing table edits, the homepage 'Secure your seat' copy, and the 10 speaker meta descriptions. Add the 301 for /1st-edition/delegate-pass.html (.htaccess or nginx, whichever the server runs) and drop that URL from sitemap.xml. 4) Run the grep and curl checks in section D, test on a phone, then request indexing for /delegate/ and the homepage. Target: live by 2 Oct 2026, since the stale prices are live now. Effort is about 2-3 hours of web dev time once the prices are signed off. On your question: this session has 4 CPUs (nproc). I can't add more from here; the cloud environment's settings set the limit.

## Content

WORLD AI SUMMIT 2026: PASS BAR, RIBBON AND STALE-PRICE FIXES
Status as of 1 Oct 2026. The prices are placeholders because nobody has yet checked what checkout charges or whether GST is included. Today /delegate/ lists Late Access at Rs 30,000 (Premium) and Rs 60,000 (VIP), and no price there says incl. or excl. GST.

==================================================
A. BAR AND RIBBON COPY
==================================================

Variant A: leads with price (the recommended version)
Desktop: World AI Summit · 14-15 Oct · Sheraton Grand Bangalore, Brigade Gateway | Late Access: Premium PLACEHOLDER_PREMIUM_PRICE · VIP PLACEHOLDER_VIP_PRICE PLACEHOLDER_GST_LABEL | 3+ delegates save 10% | [countdown] | Book your pass →
Mobile:  Premium PLACEHOLDER_PREMIUM_PRICE PLACEHOLDER_GST_LABEL · [countdown] · Book your pass →

Variant B: leads with urgency. Use this if Elets decides not to headline a price that is now above Cypher's. Cypher sells 3 days at Rs 20,000-30,000 incl. GST; WAIS Late Access is Rs 30,000 for 2 days, GST unknown.
Desktop: World AI Summit · 14-15 Oct · Sheraton Grand Bangalore, Brigade Gateway | 2 days · 7 tracks | Groups of 3 or more save 10% | [countdown] | See passes and prices →
Mobile:  World AI Summit · 14-15 Oct · [countdown] · See passes →

Top ribbon (one line above the header, scrolls away with the page):
World AI Summit 2026 · 14-15 October · Bengaluru · [countdown] · Book your pass →

What the countdown shows:
- Before 14 Oct 09:00 IST: "12d 4h 30m to go". In the last 24 hours: "18h 10m to go".
- From 14 Oct 09:00 IST until the close of day 2: "The summit is on now".
- After the close of day 2: the bar and ribbon hide themselves.
- Without JavaScript: "14-15 Oct 2026".

==================================================
B. DROP-IN CODE (Variant A; for Variant B, swap the text in the spans)
==================================================

<!-- 1) Paste immediately after <body> in the shared header include -->
<div class="wais-ribbon" data-wais-bar>
  <a href="/delegate/?ref=top_ribbon">World AI Summit 2026 · 14-15 October · Bengaluru · <span data-wais-countdown>14-15 Oct 2026</span> · <strong>Book your pass &rarr;</strong></a>
</div>

<!-- 2) Paste just before </body> in the shared footer include -->
<div class="wais-bar" id="wais-bar" data-wais-bar role="region" aria-label="World AI Summit 2026 delegate passes">
  <a class="wais-bar__link" href="/delegate/?ref=sticky_bar">
    <span class="wais-bar__event"><strong>World AI Summit</strong> · 14-15 Oct · Sheraton Grand Bangalore, Brigade Gateway</span>
    <span class="wais-bar__price">Late Access: Premium PLACEHOLDER_PREMIUM_PRICE · VIP PLACEHOLDER_VIP_PRICE PLACEHOLDER_GST_LABEL</span>
    <span class="wais-bar__group">3+ delegates save 10%</span>
    <span class="wais-bar__count" data-wais-countdown>14-15 Oct 2026</span>
    <span class="wais-bar__cta">Book your pass &rarr;</span>
  </a>
  <button type="button" class="wais-bar__close" aria-label="Hide pass bar">&times;</button>
</div>

<style>
/* Swap #0b1f3a / #ffd166 for the site's brand colours */
.wais-ribbon{background:#0b1f3a;color:#fff;font:500 14px/1.4 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;text-align:center;padding:8px 16px}
.wais-ribbon a{color:inherit;text-decoration:none}
.wais-ribbon strong{text-decoration:underline}
.wais-bar{position:fixed;left:0;right:0;bottom:0;z-index:9999;display:flex;align-items:center;background:#0b1f3a;color:#fff;font:500 14px/1.4 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;box-shadow:0 -2px 12px rgba(0,0,0,.25);padding-bottom:env(safe-area-inset-bottom)}
.wais-bar[hidden],.wais-ribbon[hidden]{display:none}
.wais-bar__link{flex:1;display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:4px 16px;padding:10px 16px;color:inherit;text-decoration:none}
.wais-bar__count{color:#ffd166;font-variant-numeric:tabular-nums;white-space:nowrap}
.wais-bar__cta{background:#ffd166;color:#0b1f3a;font-weight:700;padding:6px 14px;border-radius:4px;white-space:nowrap}
.wais-bar__close{background:none;border:0;color:#fff;font-size:22px;line-height:1;padding:10px 14px;cursor:pointer}
@media (max-width:767px){.wais-bar__event,.wais-bar__group{display:none}.wais-bar__link{gap:4px 10px;font-size:13px}}
</style>

<script>
(function () {
  var START = Date.parse('2026-10-14T09:00:00+05:30');
  var END = Date.parse('2026-10-15T18:00:00+05:30'); // PLACEHOLDER_DAY2_CLOSE_TIME (IST)
  var counters = document.querySelectorAll('[data-wais-countdown]');
  var bars = document.querySelectorAll('[data-wais-bar]');
  var bar = document.getElementById('wais-bar');
  var timer = null;

  function each(list, fn) { for (var i = 0; i < list.length; i++) fn(list[i]); }
  function pad() { document.body.style.paddingBottom = (bar && !bar.hidden) ? bar.offsetHeight + 'px' : ''; }
  function hideAll() { each(bars, function (b) { b.hidden = true; }); pad(); if (timer) clearInterval(timer); }

  function label(ms) {
    var d = Math.floor(ms / 864e5),
        h = Math.floor(ms % 864e5 / 36e5),
        m = Math.floor(ms % 36e5 / 6e4);
    return (d > 0 ? d + 'd ' : '') + h + 'h ' + m + 'm to go';
  }

  function tick() {
    var now = Date.now();
    if (now >= END) { hideAll(); return false; }
    var text = now < START ? label(START - now) : 'The summit is on now';
    each(counters, function (el) { el.textContent = text; });
    return true;
  }

  if (bar) {
    // The pass page already carries the offer, so the sticky bar is not needed there.
    if (location.pathname.indexOf('/delegate/') === 0) bar.hidden = true;
    try { if (sessionStorage.getItem('wais-bar-closed') === '1') bar.hidden = true; } catch (e) {}
    bar.querySelector('.wais-bar__close').addEventListener('click', function () {
      bar.hidden = true; pad();
      try { sessionStorage.setItem('wais-bar-closed', '1'); } catch (e) {}
    });
    window.addEventListener('resize', pad);
  }

  if (tick()) timer = setInterval(tick, 6e4);
  pad();
})();
</script>

Changes from the briefed snippet:
- `el` was undefined in the original. This version updates every [data-wais-countdown].
- It renders at once instead of waiting 60 seconds for the first tick.
- It handles the live and ended states instead of freezing.
- It reserves space at the bottom so the bar never covers the footer.
- It uses ?ref= instead of utm_source=site&utm_medium=sticky_bar. UTMs on internal links overwrite the visitor's real source (organic, email, social) in analytics, so delegate sales would be credited to "site / sticky_bar". If the team still wants UTMs, swap the hrefs to /delegate/?utm_source=site&utm_medium=sticky_bar.

==================================================
C. STALE-PRICE FIXES: SHIP IN THE SAME DEPLOY
==================================================

C1. /delegate/
- Add the H1 at the top (the page has none today): World AI Summit 2026 Delegate Passes & Pricing
- Delete the row "Early Bird Offer ... (Valid till 25th July 2025)", including "Save Rs 5,000".
- Standard Access row: replace "(Valid till 30th Sept 2026)" with "Closed on 30 September 2026". Grey the row out and remove its Book button.
- Late Access row: label it "Current price: Late Access" and highlight it. Show Premium PLACEHOLDER_PREMIUM_PRICE · VIP PLACEHOLDER_VIP_PRICE, with PLACEHOLDER_GST_LINE under each price (for example "Plus 18% GST" or "Inclusive of 18% GST"; pick the one checkout actually charges).
- Line under the table: Registering 3 or more delegates from one organisation? Each pass is 10% off.
- Make sure the page has <link rel="canonical" href="https://www.worldaisummit.com/delegate/"> so the ?ref= URLs consolidate.
- Buyer FAQ:
  Q: What does my pass include?
  A: PLACEHOLDER_PASS_INCLUSIONS (Premium vs VIP, both days, 14-15 October 2026).
  Q: Is GST included in the price?
  A: PLACEHOLDER_GST_ANSWER
  Q: Can I transfer my pass to a colleague?
  A: PLACEHOLDER_TRANSFER_POLICY. To request a change, write to registration@worldaisummit.com.
  Q: What happens after I register?
  A: PLACEHOLDER_CONFIRMATION_PROCESS (confirmation email, invoice, badge collection at Sheraton Grand Bangalore Hotel at Brigade Gateway). For any query, write to registration@worldaisummit.com.
- Cross-sell box:
  Exhibiting or sponsoring instead?
  Talk to the partnerships team about exhibition and sponsorship at World AI Summit 2026: partnerships@worldaisummit.com

C2. Homepage "Secure your seat" block
Replace "Three release phases... Premium Pass Rs 20,000/delegate" with:
  Late Access is now open.
  Premium Pass PLACEHOLDER_PREMIUM_PRICE per delegate · VIP Pass PLACEHOLDER_VIP_PRICE per delegate, PLACEHOLDER_GST_LABEL.
  Groups of 3 or more delegates save 10%.
  [Book your pass →] links to /delegate/
Also add "Passes" to the main navigation, linking to /delegate/, and point every Register button on the site to /delegate/.

C3. Speaker page meta descriptions (10 pages, OpenSEO audit c1b16b55)
Price clause "Passes from Rs 20,000":
  /assets/speaker_details/anand-thakur.html
  /assets/speaker_details/deepika-sandeep.html
  /assets/speaker_details/ganesh-joshi.html
  /assets/speaker_details/kuldeep-t.html
  /assets/speaker_details/pranav-saxena.html
  /assets/speaker_details/praveen-bist.html
  /assets/speaker_details/ram-mohan-rao.html
  /assets/speaker_details/suman-dash.html
Price clause "Delegate passes from Rs 20,000":
  /assets/speaker_details/rajesh-choudhary.html
  /assets/speaker_details/sushan-rungta.html
Edit: keep the existing name and role text in each description and replace only the price clause with "Book a delegate pass." Leave all prices out of meta descriptions so they cannot go stale again. Keep each description under about 155 characters.

C4. /1st-edition/delegate-pass.html (still sells 2025 passes; indexable and in the sitemap)
Recommended: 301 it to /delegate/ and remove it from sitemap.xml.

Apache (.htaccess in the web root, inside the existing mod_rewrite block):
  RewriteEngine On
  RewriteRule ^1st-edition/delegate-pass\.html$ https://www.worldaisummit.com/delegate/ [R=301,L]

nginx (inside the www.worldaisummit.com server block):
  location = /1st-edition/delegate-pass.html {
      return 301 https://www.worldaisummit.com/delegate/;
  }

If Elets wants to keep it as an archive page instead: remove every buy button and form from it, add <meta name="robots" content="noindex, follow">, remove it from sitemap.xml, and add a top line: "This page is the 2025 archive. Passes for World AI Summit 2026 (14-15 October, Bengaluru) are at /delegate/."

C5. Optional, same deploy: /registration and /registration.html currently 302 to the homepage in 3 hops through non-www. Point them to the pass page in one hop. First confirm that no form posts to these URLs.

Apache:
  RewriteRule ^registration(\.html)?$ https://www.worldaisummit.com/delegate/ [R=301,L]
nginx:
  location ~ ^/registration(\.html)?$ {
      return 301 https://www.worldaisummit.com/delegate/;
  }

==================================================
D. CHECKS AFTER DEPLOY
==================================================
- Before uploading, run this from the site root to catch any other stale copy:
  grep -rlni --include=*.html -e "Rs 20,000" -e "Rs. 20,000" -e "₹20,000" -e "20,000/delegate" -e "25th July 2025" -e "30th Sept 2026" .
  After the fix, "Rs 20,000" should appear only in the greyed "Closed on 30 September 2026" row on /delegate/.
- curl -sI https://www.worldaisummit.com/1st-edition/delegate-pass.html should return a single 301 to https://www.worldaisummit.com/delegate/
- On a phone, check that the bar shows price, countdown and CTA on one or two lines and does not cover the footer or any cookie banner.
- Request indexing of /delegate/ and the homepage in Search Console. The verified property is the non-www URL-prefix https://worldaisummit.com/.
