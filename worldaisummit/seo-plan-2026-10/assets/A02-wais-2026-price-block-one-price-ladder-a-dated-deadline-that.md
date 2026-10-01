# A02: WAIS 2026 price block: one price ladder, a dated deadline that never resets, GST stated, and a group-quote form (homepage and /delegate/)

- **For recommendation:** 3. One price everywhere, honest dated urgency, GST stated, and a group-booking form
- **Research lens:** cro-leads
- **Format:** HTML snippet (section, inline CSS and vanilla JS, no dependencies) followed by plain-text copy for listings and speaker-page meta descriptions
- **Placeholders the business must fill:**
  - PLACEHOLDER_PREMIUM_NOW: current Premium price; suggested 20,000, which the homepage and /delegate/ already show
  - PLACEHOLDER_VIP_NOW: current VIP price; suggested 35,000, which /delegate/ already shows
  - PLACEHOLDER_PREMIUM_LATE: Late Access Premium price; suggested 30,000, as published on /delegate/
  - PLACEHOLDER_VIP_LATE: Late Access VIP price; suggested 60,000, as published on /delegate/
  - PLACEHOLDER_GST_LABEL: '+ 18% GST' or 'incl. 18% GST'. Unknown today, so match it to what checkout charges
  - PLACEHOLDER_DEADLINE_TEXT: suggested '7 October 2026, 11:59 pm IST'
  - PLACEHOLDER_DEADLINE_ISO: suggested 2026-10-07T23:59:59+05:30; used in two places
  - PLACEHOLDER_LATE_FROM_TEXT: suggested '8 October 2026'
  - PLACEHOLDER_CHECKOUT_PREMIUM_URL: the existing Premium checkout link from the /delegate/ Checkout section
  - PLACEHOLDER_CHECKOUT_VIP_URL: the existing VIP checkout link from the /delegate/ Checkout section
  - PLACEHOLDER_FORM_ENDPOINT: the URL of the form handler that delivers to registration@worldaisummit.com
  - PLACEHOLDER_WHATSAPP_NUMBER: the registration team's WhatsApp number, digits only, with country code

## How to ship

Ship by 2 Oct 2026. The /delegate/ Standard row ("Valid till 30th Sept 2026") has already expired. An Exa fetch on 1 Oct confirmed the page still shows Early Bird (valid till 25 July 2025), Standard and Late Access rows, and gives no GST statement.

1) Marketing head, about 30 minutes: fill every PLACEHOLDER_ value. Check what checkout actually charges today, because whether ₹20,000 includes GST is unknown, and so is which tier is being charged from 1 Oct. Then choose PLACEHOLDER_GST_LABEL to match. The /delegate/ page currently shows two benefit lists that disagree: "Special sessions" and "AI Policy Roundtables" appear in one, and "Govt & Investor Roundtable Invite" in the other. The block uses only the benefits that appear in both lists. Confirm any others before you add them.

2) Web developer, 1–2 hours: paste the same block on the homepage, replacing "Three release phases..." and the 3 cards (only one of them has a name and price today). On /delegate/, it replaces the three price rows. Keep one copy (an include or partial) so the two pages cannot drift apart. Point PLACEHOLDER_FORM_ENDPOINT at the form handler the site already uses, configured to deliver to registration@. GA4 records form_submit on /delegate/, so a handler exists. Test once by submitting a request, then check that it reaches the registration@ inbox and that GA4 DebugView shows generate_lead with form_type=group. In GA4, mark generate_lead as a key event and register form_type as an event-scoped custom dimension. The "Exhibiting instead?" link goes to partnerships@ by email, not to /partnership.html, because that page canonicalises to the homepage.

3) Same day: paste the listing text into allevents.in, 10times and Eventbrite. In the crawl (c1b16b55), only 1 of the 5 speaker pages sampled has "Passes from Rs 20,000" in its meta description (anand-thakur.html). Check the rest of /assets/speaker_details/ and remove the price instead of adding a dated one. If the site's Event JSON-LD has an offers block, set price, priceCurrency INR and validThrough to the same values. Do not publish a partial schema.

4) On the morning of PLACEHOLDER_LATE_FROM_TEXT: the script switches visitors to Late Access prices automatically. Still edit the static HTML to the late prices and remove the deadline line, so crawlers and visitors without JavaScript see the right price. Never move or reset the deadline.

5) Expected effect, kept realistic: there is no traffic effect. This affects conversion on /delegate/, which had 2,162 views from 1,729 users in Sep 2026 (GA4), mostly from non-organic campaigns. Organic search brought only 149 users. It is not "every pass buyer". The page also recorded 178 form_submit events, and the homepage 97. It is unknown whether form_submit means a paid purchase or an enquiry. To measure, compare the daily form_submit and generate_lead counts for 2–7 Oct with the September daily average.

## Content

<!--
WORLD AI SUMMIT 2026: PRICE BLOCK
Paste the same block in two places:
  1. Homepage: replace the "Secure your seat" area. That means the line "Three release phases. The earlier you commit, the better the price." and the 3 cards.
  2. /delegate/: replace the three price rows: "Early Bird ... (Valid till 25th July 2025)", "Standard Access (Valid till 30th Sept 2026)" and "Late Access".
Fill each PLACEHOLDER_ once, then find-and-replace it on both pages so the two pages always match.
  PLACEHOLDER_PREMIUM_NOW     suggested 20,000 (already shown on the homepage and /delegate/)
  PLACEHOLDER_VIP_NOW         suggested 35,000 (already shown on /delegate/)
  PLACEHOLDER_PREMIUM_LATE    suggested 30,000 (published Late Access)
  PLACEHOLDER_VIP_LATE        suggested 60,000 (published Late Access)
  PLACEHOLDER_GST_LABEL       "+ 18% GST" or "incl. 18% GST". Pick whichever matches what checkout actually charges.
  PLACEHOLDER_DEADLINE_TEXT   suggested "7 October 2026, 11:59 pm IST"
  PLACEHOLDER_DEADLINE_ISO    suggested 2026-10-07T23:59:59+05:30 (used twice)
  PLACEHOLDER_LATE_FROM_TEXT  suggested "8 October 2026"
  PLACEHOLDER_CHECKOUT_PREMIUM_URL / PLACEHOLDER_CHECKOUT_VIP_URL   the existing checkout links on /delegate/
  PLACEHOLDER_FORM_ENDPOINT   the form handler URL that delivers to registration@worldaisummit.com
  PLACEHOLDER_WHATSAPP_NUMBER digits only, with country code, e.g. 91XXXXXXXXXX
-->
<style>
.wais-price{max-width:960px;margin:0 auto;padding:32px 16px}
.wais-price__meta{margin:4px 0 0;opacity:.8}
.wais-price__tiers{display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));margin:20px 0}
.wais-price__tier{border:1px solid rgba(127,127,127,.35);border-radius:12px;padding:20px}
.wais-price__tier h3{margin:0}
.wais-price__amt{font-size:1.75rem;font-weight:700;margin:8px 0}
.wais-price__amt small{font-size:.9rem;font-weight:400}
.wais-price__tier ul{padding-left:1.1em;margin:12px 0 16px}
.wais-price__countdown{font-weight:600}
/* Swap #1a56db for the site's button colour, or add the site's existing button class to .wais-btn */
.wais-btn{display:inline-block;padding:10px 18px;border:0;border-radius:8px;background:#1a56db;color:#fff;text-decoration:none;font:inherit;font-weight:600;cursor:pointer}
.wais-group{margin-top:28px;padding-top:20px;border-top:1px solid rgba(127,127,127,.35)}
.wais-group form{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));align-items:end}
.wais-group label{display:flex;flex-direction:column;gap:4px;font-size:.95rem}
.wais-group input{padding:10px;border:1px solid rgba(127,127,127,.5);border-radius:8px;font:inherit}
.wais-group [data-status]{grid-column:1/-1;margin:0}
</style>

<section id="passes" class="wais-price" aria-labelledby="wais-price-h" data-deadline="PLACEHOLDER_DEADLINE_ISO">
  <h2 id="wais-price-h">Book your World AI Summit 2026 pass</h2>
  <p class="wais-price__meta">14–15 October 2026 · Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru</p>

  <div class="wais-price__tiers">
    <div class="wais-price__tier">
      <h3>Premium Pass</h3>
      <p class="wais-price__amt"><span data-late="₹PLACEHOLDER_PREMIUM_LATE">₹PLACEHOLDER_PREMIUM_NOW</span> <small>PLACEHOLDER_GST_LABEL per delegate</small></p>
      <ul>
        <li>Full summit access, both days</li>
        <li>Delegate kit, lunch and refreshments</li>
        <li>Certificate of participation</li>
      </ul>
      <a class="wais-btn" href="PLACEHOLDER_CHECKOUT_PREMIUM_URL" data-pass="premium">Book Premium</a>
    </div>
    <div class="wais-price__tier">
      <h3>VIP Pass</h3>
      <p class="wais-price__amt"><span data-late="₹PLACEHOLDER_VIP_LATE">₹PLACEHOLDER_VIP_NOW</span> <small>PLACEHOLDER_GST_LABEL per delegate</small></p>
      <ul>
        <li>Everything in Premium</li>
        <li>Priority seating</li>
        <li>Speaker lounge access</li>
        <li>Exclusive networking dinner</li>
      </ul>
      <a class="wais-btn" href="PLACEHOLDER_CHECKOUT_VIP_URL" data-pass="vip">Book VIP</a>
    </div>
  </div>

  <p data-wais-deadline>This price holds until <strong><time datetime="PLACEHOLDER_DEADLINE_ISO">PLACEHOLDER_DEADLINE_TEXT</time></strong>. From PLACEHOLDER_LATE_FROM_TEXT, passes are ₹PLACEHOLDER_PREMIUM_LATE (Premium) and ₹PLACEHOLDER_VIP_LATE (VIP), PLACEHOLDER_GST_LABEL.</p>
  <p class="wais-price__countdown" data-wais-countdown hidden>Current price ends in <span data-cd></span>.</p>
  <p data-wais-late-note hidden>Late Access pricing now applies until the summit. Groups of 3 or more delegates still get 10% off.</p>

  <p>Booking 3 or more delegates? <a href="#group">Get 10% off – request a group quote</a> · Need a GST invoice or purchase order before you pay? <a href="https://wa.me/PLACEHOLDER_WHATSAPP_NUMBER?text=Hello%2C%20I%20need%20a%20GST%20invoice%20for%20World%20AI%20Summit%202026%20passes." rel="noopener">WhatsApp the registration team</a> or write to <a href="mailto:registration@worldaisummit.com">registration@worldaisummit.com</a>.</p>
  <p>Exhibiting instead? <a href="mailto:partnerships@worldaisummit.com?subject=Exhibiting%20at%20World%20AI%20Summit%202026">Ask about booths and sponsorship</a></p>

  <div id="group" class="wais-group">
    <h3>Group booking: 3 or more delegates, 10% off</h3>
    <p>Share four details and the registration team will call you with a group quote and GST invoice.</p>
    <form id="wais-group-form" action="PLACEHOLDER_FORM_ENDPOINT" method="POST">
      <input type="hidden" name="form_type" value="group">
      <input type="hidden" name="_subject" value="WAIS 2026 group booking request">
      <label>Your name
        <input name="name" type="text" autocomplete="name" required>
      </label>
      <label>Company
        <input name="company" type="text" autocomplete="organization" required>
      </label>
      <label>Number of delegates
        <input name="delegates" type="number" min="3" max="500" step="1" inputmode="numeric" required>
      </label>
      <label>Phone
        <input name="phone" type="tel" autocomplete="tel" pattern="[0-9+ ()-]{8,20}" required>
      </label>
      <button class="wais-btn" type="submit">Request group quote</button>
      <p data-status role="status" aria-live="polite"></p>
    </form>
  </div>
</section>

<script>
(function () {
  var box = document.getElementById('passes');
  if (!box) return;

  /* Countdown to one fixed date. It never resets. When the date passes, it shows Late Access prices. */
  var deadline = new Date(box.getAttribute('data-deadline')).getTime();
  var cd = box.querySelector('[data-wais-countdown]');
  var out = box.querySelector('[data-cd]');
  function plural(n, w) { return n + ' ' + w + (n === 1 ? '' : 's'); }
  function tick() {
    if (isNaN(deadline)) return true;
    var left = deadline - Date.now();
    if (left <= 0) {
      var amts = box.querySelectorAll('[data-late]');
      for (var i = 0; i < amts.length; i++) amts[i].textContent = amts[i].getAttribute('data-late');
      box.querySelector('[data-wais-deadline]').hidden = true;
      box.querySelector('[data-wais-late-note]').hidden = false;
      cd.hidden = true;
      return true;
    }
    var m = Math.floor(left / 60000), d = Math.floor(m / 1440), h = Math.floor((m % 1440) / 60);
    out.textContent = d > 0 ? plural(d, 'day') + ', ' + plural(h, 'hour') : plural(h, 'hour') + ', ' + plural(m % 60, 'minute');
    cd.hidden = false;
    return false;
  }
  if (!tick()) { var timer = setInterval(function () { if (tick()) clearInterval(timer); }, 60000); }

  /* Group form: posts to the handler and fires GA4 generate_lead with form_type=group only after a successful send. */
  var form = document.getElementById('wais-group-form');
  if (!form) return;
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var status = form.querySelector('[data-status]');
    var btn = form.querySelector('button[type=submit]');
    var n = parseInt(form.elements.delegates.value, 10);
    if (!(n >= 3)) { status.textContent = 'Group pricing starts at 3 delegates.'; form.elements.delegates.focus(); return; }
    btn.disabled = true;
    status.textContent = 'Sending…';
    fetch(form.action, { method: 'POST', body: new FormData(form), headers: { 'Accept': 'application/json' } })
      .then(function (r) {
        if (!r.ok) throw new Error('HTTP ' + r.status);
        var p = { form_type: 'group', delegates: n };
        if (typeof window.gtag === 'function') { window.gtag('event', 'generate_lead', p); }
        else { (window.dataLayer = window.dataLayer || []).push(Object.assign({ event: 'generate_lead' }, p)); }
        form.reset();
        status.textContent = 'Thank you. The registration team will call you with a group quote.';
      })
      .catch(function () {
        var f = form.elements;
        var body = 'Name: ' + f.name.value + '\nCompany: ' + f.company.value + '\nDelegates: ' + f.delegates.value + '\nPhone: ' + f.phone.value;
        var a = document.createElement('a');
        a.href = 'mailto:registration@worldaisummit.com?subject=' + encodeURIComponent('WAIS 2026 group booking request') + '&body=' + encodeURIComponent(body);
        a.textContent = 'registration@worldaisummit.com';
        status.textContent = 'The request did not go through. Please email ';
        status.appendChild(a);
        status.appendChild(document.createTextNode(' and your details will be filled in for you.'));
      })
      .then(function () { btn.disabled = false; });
  });
})();
</script>

=====================================================================
PLAIN-TEXT COPY FOR LISTINGS (allevents.in, 10times, Eventbrite)
Use the same values as above and update all three on the same day.
=====================================================================
Delegate passes: Premium ₹PLACEHOLDER_PREMIUM_NOW and VIP ₹PLACEHOLDER_VIP_NOW, PLACEHOLDER_GST_LABEL, until PLACEHOLDER_DEADLINE_TEXT. From PLACEHOLDER_LATE_FROM_TEXT: Premium ₹PLACEHOLDER_PREMIUM_LATE and VIP ₹PLACEHOLDER_VIP_LATE. Groups of 3 or more delegates get 10% off. Book at https://www.worldaisummit.com/delegate/ or write to registration@worldaisummit.com.

=====================================================================
SPEAKER-PAGE META DESCRIPTIONS (/assets/speaker_details/*.html)
=====================================================================
Remove the price from speaker-page meta descriptions; do not add a dated price. A price there goes stale on PLACEHOLDER_LATE_FROM_TEXT. Replace "Passes from Rs 20,000" with:
"World AI Summit 2026, 14–15 October, Bengaluru. Book a delegate pass at worldaisummit.com."
