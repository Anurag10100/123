# A04: Sitewide WhatsApp and click-to-call contact bar (book passes, sponsor or exhibit, nominate) with GA4 contact_click tracking: World AI Summit 2026

- **For recommendation:** 5. Sticky WhatsApp and click-to-call bar with intent-specific prefilled messages
- **Research lens:** cro-leads
- **Format:** Markdown pack: (A) one HTML/CSS/JS sitewide include, tested in headless Chromium at 360 px and 1280 px; (B) an HTML replacement for the /delegate/ price block; (C) GA4 Admin steps; (D) WhatsApp Business greeting, away and quick-reply copy; (E) pre-launch QA checklist
- **Placeholders the business must fill:**
  - PLACEHOLDER_REG_WHATSAPP: registration desk WhatsApp number, 91XXXXXXXXXX. The candidate is 919818274383 from the 2025 page, but only use it after a test call and a test WhatsApp message are answered.
  - PLACEHOLDER_REG_PHONE: registration desk call number, 91XXXXXXXXXX. It can be the same as the WhatsApp number.
  - PLACEHOLDER_PARTNERSHIP_WHATSAPP: partnerships desk WhatsApp number. This is a new number; none is published anywhere.
  - PLACEHOLDER_PARTNERSHIP_PHONE: partnerships desk call number. This is a new number.
  - PLACEHOLDER_AWARDS_WHATSAPP: awards desk WhatsApp number. Use a new number, or 918860651641 (the 2025 secretariat/speaking line) only if it is confirmed staffed and able to handle awards.
  - PLACEHOLDER_AWARDS_PHONE: awards desk call number.
  - PLACEHOLDER_CURRENT_TIER_NAME: the pass tier on sale today (Standard expired on 30 Sept; Late Access is listed at Rs 30,000/60,000, which needs confirming).
  - PLACEHOLDER_CURRENT_PRICE: today's delegate pass price in Rs.
  - PLACEHOLDER_GST_TREATMENT: 'plus GST' or 'inclusive of GST', to be confirmed by finance.
  - PLACEHOLDER_PRICE_VALID_TILL: the last date of the current price.
  - PLACEHOLDER_BOOKING_URL: the live checkout or registration URL for the 2026 pass.
  - PLACEHOLDER_REPLY_TIME: the reply time promised outside desk hours, e.g. 'the next working morning'.
  - PLACEHOLDER_INVOICE_TURNAROUND: how quickly finance can issue a GST invoice.
  - PLACEHOLDER_AWARD_CATEGORIES, PLACEHOLDER_AWARD_FEE, PLACEHOLDER_AWARD_DEADLINE: 2026 World AI Awards details. Only the 2025 fee is known (Rs 18,000 + GST per entry).

## How to ship

Ship by 3 Oct 2026.

1) Marketing and sales (30 min, today):
- Choose and staff three lines from 9 am to 8 pm IST, every day until 17 Oct: registration, partnerships and awards.
- The 2025 page lists only a delegate number and a speaking number. The sponsor/exhibit line and the awards line need new numbers.
- Before reusing either 2025 number, confirm it is answered.
- Set up WhatsApp Business on each line with the greeting, away message and quick replies in section D.

2) Analytics (10 min, before go-live):
- Register the two event-scoped custom dimensions, method and intent.
- Mark contact_click as a key event (section C).

3) Web dev (about 1 h):
- Paste section A once into the shared footer include, after the gtag snippet, and fill in the CONFIG numbers.
- Apply section B on /delegate/ and on the homepage pass card in the same release.
- Run the QA in section E, then upload.
- There is no per-page work. /partnership.html and /award.html canonicalise to /, and the include covers every page.
- No schema or redirect changes are needed for this item.

4) Review:
- From 4 Oct, review contact_click by intent and method in GA4 every evening, and compare it with the WhatsApp labels.
- The bar hides itself after 17 Oct, 8 pm IST. Remove the include in the next deploy after that.

Context: GA4 shows forms already collecting leads (Sep: form_submit 355 events from 226 users; partnership_form_submit 257 events from 199 users). The bar adds a faster channel for invoice, PO and group-pricing questions. It does not fill an empty channel.

## Content

## A. Sitewide include: paste once into the shared footer, just before </body>

Paste it after the existing GA4 gtag snippet (G-QEB6N0MFLC). It works on every page, so you do not need a separate copy for /partnership.html or /award.html, because both canonicalise to /.

How it works:
- On mobile (below 900 px) it shows a bottom bar with one WhatsApp button per desk, plus a Call button that opens the phone numbers.
- On desktop it shows a "Talk to our team" button at the bottom right. This opens a card with WhatsApp and Call for each desk.
- Any desk whose number is empty or still a PLACEHOLDER_ is left out automatically, so a line nobody answers never goes live.
- The bar removes itself after 17 Oct 2026, 8 pm IST.
- Every WhatsApp and tel: click sends a GA4 contact_click event with method (whatsapp or call) and intent (delegate, sponsor or nominate).

Test results: at 360 px there is no horizontal scroll. The WhatsApp links open wa.me with the message filled in, and the events fired as expected. The test used dummy numbers.

```html
<!-- ================================================================
     World AI Summit 2026 - contact bar (WhatsApp + call), sitewide.
     Paste ONCE into the shared footer include, just before </body>,
     after the existing GA4 gtag snippet (G-QEB6N0MFLC).
     Edit only the CONFIG block. A desk whose number is missing or still
     a PLACEHOLDER_ is skipped, so an unstaffed line is never published.
     The bar removes itself after 17 Oct 2026, 8 pm IST.
     ================================================================ -->
<style>
  .wais-cb{--cb-navy:#0b1a33;--cb-green:#0b6b3a;--cb-muted:#c7d2e5;--cb-line:rgba(255,255,255,.16);
    position:fixed;z-index:9990;font:500 14px/1.3 system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;color:#fff}
  .wais-cb *{box-sizing:border-box}
  .wais-cb a{color:inherit;text-decoration:none}
  .wais-cb button{font:inherit;color:inherit;cursor:pointer}
  .wais-cb a:focus-visible,.wais-cb button:focus-visible{outline:3px solid #ffd166;outline-offset:2px}
  .wais-cb__bar,.wais-cb__sheet,.wais-cb__fab,.wais-cb__card{display:none}
  .wais-cb__sub{display:block;font-size:11px;font-weight:500;color:var(--cb-muted)}
  .wais-cb__wa .wais-cb__sub{color:#d9f2e3}

  /* ---------- Mobile: bottom bar ---------- */
  @media (max-width:899px){
    .wais-cb{left:0;right:0;bottom:0;background:var(--cb-navy);box-shadow:0 -2px 12px rgba(0,0,0,.25);
      padding:6px 8px calc(6px + env(safe-area-inset-bottom))}
    .wais-cb__bar{display:flex;gap:6px}
    .wais-cb__bar>*{flex:1 1 0;min-width:0;min-height:48px;border-radius:8px;border:0;padding:5px 4px;
      display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;font-weight:700;font-size:13px;line-height:1.15}
    .wais-cb__wa{background:var(--cb-green)}
    .wais-cb .wais-cb__callbtn{background:transparent;border:1px solid var(--cb-line);font-weight:700}
    .wais-cb.is-open .wais-cb__sheet{display:block}
    .wais-cb__sheet{border-bottom:1px solid var(--cb-line);margin:0 0 6px;padding:6px 2px 8px}
    .wais-cb__sheet p{margin:0 0 4px;font-size:12px;color:var(--cb-muted)}
    .wais-cb__sheet a{display:flex;justify-content:space-between;gap:8px;min-height:44px;align-items:center;
      padding:0 6px;border-top:1px solid var(--cb-line)}
    .wais-cb__sheet a span:last-child{font-weight:700;white-space:nowrap}
    html.wais-cb-on body{padding-bottom:calc(64px + env(safe-area-inset-bottom))}
  }

  /* ---------- Desktop: side button + card ---------- */
  @media (min-width:900px){
    .wais-cb{right:24px;bottom:24px}
    .wais-cb__fab{display:block;margin-left:auto;background:var(--cb-green);border:0;border-radius:999px;
      padding:12px 20px;font-weight:700;box-shadow:0 4px 16px rgba(0,0,0,.25)}
    .wais-cb.is-open .wais-cb__card{display:block}
    .wais-cb.is-open .wais-cb__fab{display:none}
    .wais-cb__card{width:340px;background:var(--cb-navy);border-radius:12px;padding:16px;box-shadow:0 8px 28px rgba(0,0,0,.3)}
    .wais-cb__head{display:flex;justify-content:space-between;align-items:flex-start;gap:12px;margin:0 0 8px}
    .wais-cb__head strong{font-size:16px}
    .wais-cb__x{background:transparent;border:0;font-size:22px;line-height:1;padding:0 4px}
    .wais-cb__desk{border-top:1px solid var(--cb-line);padding:10px 0 2px}
    .wais-cb__desk h3{margin:0;font-size:14px;font-weight:700}
    .wais-cb__row{display:flex;gap:8px;margin-top:8px;flex-wrap:wrap}
    .wais-cb__row a{border-radius:8px;padding:8px 12px;font-weight:600;font-size:13px}
    .wais-cb__row .wais-cb__wa{background:var(--cb-green)}
    .wais-cb__row .wais-cb__tel{border:1px solid var(--cb-line)}
  }
  @media print{.wais-cb{display:none!important}}
</style>

<script>
(function () {
  'use strict';

  /* ===================== CONFIG: edit only this block ===================== */
  /* Numbers: 91 + 10 digits, no "+", spaces or leading 0, e.g. 91XXXXXXXXXX.
     WhatsApp and call numbers can be the same line. */
  var DESKS = [
    { intent: 'delegate', label: 'Book passes', short: 'Book passes', desk: 'Registration desk',
      wa: 'PLACEHOLDER_REG_WHATSAPP', tel: 'PLACEHOLDER_REG_PHONE',
      text: "Hi, I'd like to book World AI Summit 2026 passes (14-15 October, Bengaluru). Please share today's pass price, group booking terms and GST invoice details." },
    { intent: 'sponsor', label: 'Sponsor / exhibit', short: 'Sponsor', desk: 'Partnerships desk',
      wa: 'PLACEHOLDER_PARTNERSHIP_WHATSAPP', tel: 'PLACEHOLDER_PARTNERSHIP_PHONE',
      text: "Hi, I'm interested in sponsoring or exhibiting at World AI Summit 2026 (14-15 October, Bengaluru). Please share the partnership options." },
    { intent: 'nominate', label: 'Nominate for the World AI Awards', short: 'Nominate', desk: 'Awards desk',
      wa: 'PLACEHOLDER_AWARDS_WHATSAPP', tel: 'PLACEHOLDER_AWARDS_PHONE',
      text: "Hi, I'd like to nominate for the World AI Awards at World AI Summit 2026. Please share the categories, entry fee and last date." }
  ];
  var HOURS = 'We reply 9 am to 8 pm IST';
  var HIDE_AFTER = Date.parse('2026-10-17T20:00:00+05:30');
  /* ======================================================================== */

  if (Date.now() > HIDE_AFTER || document.querySelector('.wais-cb')) return;

  function ok(n) { return /^91\d{10}$/.test(n || ''); }
  function fmt(n) { return '+91 ' + n.slice(2, 7) + ' ' + n.slice(7); }
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) {
    return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function waUrl(d) { return 'https://wa.me/' + d.wa + '?text=' + encodeURIComponent(d.text); }
  function waLink(d, inner) {
    return '<a class="wais-cb__wa" href="' + esc(waUrl(d)) + '" target="_blank" rel="noopener"' +
      ' data-method="whatsapp" data-intent="' + d.intent + '">' + inner + '</a>';
  }
  function telLink(d, inner) {
    return '<a class="wais-cb__tel" href="tel:+' + d.tel + '" data-method="call" data-intent="' + d.intent + '">' + inner + '</a>';
  }

  var desks = DESKS.filter(function (d) { return ok(d.wa) || ok(d.tel); });
  if (!desks.length) return;
  var calls = desks.filter(function (d) { return ok(d.tel); });

  /* Mobile bar: one WhatsApp button per desk + one Call button that opens the numbers */
  var bar = desks.filter(function (d) { return ok(d.wa); }).map(function (d) {
    return waLink(d, '<span class="wais-cb__sub">WhatsApp</span>' + esc(d.short));
  }).join('');
  if (calls.length) {
    bar += '<button type="button" class="wais-cb__callbtn" aria-expanded="false" aria-controls="wais-cb-sheet">' +
      '<span class="wais-cb__sub">Phone</span>Call</button>';
  }
  var sheet = '<p>' + esc(HOURS) + '</p>' + calls.map(function (d) {
    return telLink(d, '<span>' + esc(d.label) + '</span><span>' + fmt(d.tel) + '</span>');
  }).join('');

  /* Desktop card */
  var card = '<div class="wais-cb__head"><div><strong>Talk to our team</strong>' +
    '<span class="wais-cb__sub">' + esc(HOURS) + '</span></div>' +
    '<button type="button" class="wais-cb__x" aria-label="Close">&times;</button></div>' +
    desks.map(function (d) {
      return '<div class="wais-cb__desk"><h3>' + esc(d.label) + '</h3><span class="wais-cb__sub">' + esc(d.desk) + '</span>' +
        '<div class="wais-cb__row">' + (ok(d.wa) ? waLink(d, 'WhatsApp') : '') +
        (ok(d.tel) ? telLink(d, 'Call ' + fmt(d.tel)) : '') + '</div></div>';
    }).join('');

  var root = document.createElement('aside');
  root.className = 'wais-cb';
  root.setAttribute('aria-label', 'Contact the World AI Summit 2026 team');
  root.innerHTML =
    '<div class="wais-cb__sheet" id="wais-cb-sheet">' + sheet + '</div>' +
    '<div class="wais-cb__bar">' + bar + '</div>' +
    '<button type="button" class="wais-cb__fab" aria-expanded="false" aria-controls="wais-cb-card">Talk to our team</button>' +
    '<div class="wais-cb__card" id="wais-cb-card" role="group" aria-label="Talk to our team">' + card + '</div>';
  document.body.appendChild(root);
  document.documentElement.classList.add('wais-cb-on');

  function setOpen(open) {
    root.classList.toggle('is-open', open);
    [].forEach.call(root.querySelectorAll('[aria-expanded]'), function (b) { b.setAttribute('aria-expanded', String(open)); });
  }
  root.addEventListener('click', function (e) {
    if (e.target.closest('.wais-cb__fab, .wais-cb__callbtn')) setOpen(!root.classList.contains('is-open'));
    else if (e.target.closest('.wais-cb__x')) setOpen(false);
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setOpen(false); });
  document.addEventListener('click', function (e) { if (!root.contains(e.target)) setOpen(false); });

  /* In-page links such as
     <a href="mailto:registration@worldaisummit.com" data-wais-wa="delegate">...</a>
     become WhatsApp links when that desk is live; otherwise the mailto fallback stays. */
  [].forEach.call(document.querySelectorAll('a[data-wais-wa]'), function (a) {
    var d = desks.filter(function (x) { return x.intent === a.getAttribute('data-wais-wa'); })[0];
    if (!d || !ok(d.wa)) return;
    a.href = waUrl(d); a.target = '_blank'; a.rel = 'noopener';
    a.setAttribute('data-method', 'whatsapp'); a.setAttribute('data-intent', d.intent);
  });

  /* GA4: contact_click with method (whatsapp | call) and intent (delegate | sponsor | nominate) */
  document.addEventListener('click', function (e) {
    var a = e.target && e.target.closest ? e.target.closest('a[data-method][data-intent]') : null;
    if (!a || typeof window.gtag !== 'function') return;
    window.gtag('event', 'contact_click', {
      method: a.getAttribute('data-method'),
      intent: a.getAttribute('data-intent'),
      transport_type: 'beacon'
    });
  }, true);
})();
</script>
<!-- ================== end World AI Summit 2026 contact bar ================== -->
```

Leave the existing "World AI Summit Community" WhatsApp channel CTA in place. It is an updates channel, not a sales line.

---

## B. Same release: /delegate/ price block (replaces the expired rows)

/delegate/ still shows "Early Bird, valid till 25th July 2025" and "Standard Access, valid till 30th Sept 2026", and both have expired. The homepage still shows Premium at Rs 20,000. Delete those rows, paste this block in their place, and use the same price on the homepage pass card.

```html
<section class="pass-now" id="passes">
  <h2>Delegate passes for 14-15 October 2026, Bengaluru</h2>
  <p><strong>PLACEHOLDER_CURRENT_TIER_NAME</strong>: Rs PLACEHOLDER_CURRENT_PRICE per delegate, PLACEHOLDER_GST_TREATMENT. Valid till PLACEHOLDER_PRICE_VALID_TILL.</p>
  <p>Booking for 3 or more delegates? Group bookings get 10% off.</p>
  <p>Need a GST invoice, a PO-based booking or group pricing?
     <a href="mailto:registration@worldaisummit.com" data-wais-wa="delegate">Message the registration desk</a>.</p>
  <p><a class="btn" href="PLACEHOLDER_BOOKING_URL">Book your pass</a></p>
</section>
```

Homepage pass card: replace "Premium Rs 20,000" with "PLACEHOLDER_CURRENT_TIER_NAME: Rs PLACEHOLDER_CURRENT_PRICE per delegate, PLACEHOLDER_GST_TREATMENT", and link it to https://www.worldaisummit.com/delegate/.

---

## C. GA4 setup (property 490291049, G-QEB6N0MFLC): do this before the bar goes live

The property has 0 custom dimensions, and custom dimensions do not fill in data from before they were created.
1. Go to Admin > Data display > Custom definitions > Create custom dimension.
   - Dimension name: Contact method. Scope: Event. Event parameter: method.
   - Dimension name: Contact intent. Scope: Event. Event parameter: intent.
2. Go to Admin > Data display > Key events > New key event and enter: contact_click.
3. Check it works:
   - Open the site with the Google Analytics Debugger extension.
   - Tap each button.
   - Admin > DebugView should show contact_click with method and intent.
   - Realtime > Event count by Event name should also show it.
4. Build the report:
   - Go to Explore > Free form.
   - Rows: Contact intent. Columns: Contact method. Metric: Key events (contact_click).
   - Filter: Event name = contact_click.
   - Compare it with form_submit (Sep: 355 events, 226 users) and partnership_form_submit (Sep: 257 events, 199 users).

Note on tel: links: enhanced measurement already logs wa.me clicks as outbound clicks, but it does not log tel: links. contact_click is the only record of calls, so report on contact_click and ignore the outbound "click" event to avoid double counting.

---

## D. WhatsApp Business copy for each desk line

Greeting message:
"Thank you for contacting World AI Summit 2026, 14-15 October at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. A member of our team will reply shortly. Our desk is open from 9 am to 8 pm IST."

Away message (outside 9 am to 8 pm IST):
"Thank you for your message. Our desk is open from 9 am to 8 pm IST and we will reply by PLACEHOLDER_REPLY_TIME. You can also write to registration@worldaisummit.com for passes, partnerships@worldaisummit.com for sponsorship and exhibition, or secretariat@worldaisummit.com for the World AI Awards."

Quick replies:
- /price: "Today's delegate pass is Rs PLACEHOLDER_CURRENT_PRICE per delegate, PLACEHOLDER_GST_TREATMENT, valid till PLACEHOLDER_PRICE_VALID_TILL. Groups of 3 or more get 10% off. Shall I share the booking link or an invoice?"
- /invoice: "Please share your company name, GSTIN, billing address and the names and email IDs of the delegates. We will send the invoice within PLACEHOLDER_INVOICE_TURNAROUND."
- /sponsor: "Thank you for your interest. Please share your company name, the audience you want to reach and an approximate budget, and we will send the partnership options for 14-15 October."
- /awards: "Nominations for the World AI Awards are made through the form at https://www.worldaisummit.com/awards/. Categories: PLACEHOLDER_AWARD_CATEGORIES. Entry fee: PLACEHOLDER_AWARD_FEE. Last date: PLACEHOLDER_AWARD_DEADLINE."

Labels to apply to every chat: Delegate, Sponsor, Awards, Paid. Each evening, add up the labels and compare them with contact_click in GA4.

---

## E. Pre-launch QA (about 15 minutes)

1. Fill in the numbers in the CONFIG block in the format 91XXXXXXXXXX. Any desk left as a PLACEHOLDER_ stays hidden. If all three are placeholders, nothing shows.
2. Do not reuse 9818274383 (2025 delegate line) or 8860651641 (2025 speaking/secretariat line) until someone has answered a test call and a test WhatsApp message on that number today.
3. At 360 px on a phone:
   - Check that the bar shows and the footer is not hidden behind it.
   - Check that the bar does not overlap the community WhatsApp CTA, the cookie banner or a back-to-top button. If any of these floats at the bottom, raise it by 64 px.
4. On desktop, check that the button at the bottom right does not overlap any existing floating element.
5. Tap each WhatsApp button and check that the chat opens with the message filled in. Tap each Call link and check that the dialler opens with the right number.
6. Check that contact_click appears in DebugView with the correct method and intent.
7. If the site sends a Content-Security-Policy header, allow this inline script, or move it to /assets/js/contact-bar.js and load it with a script tag.
