# A05: /partnership.html lead page: head tags, partner copy, gated 2026 deck form with generate_lead, 2025 partner strip, redirects and homepage FAQ link

- **For recommendation:** 6. Make /partnership.html, the sponsor landing page for mailers, a real lead page with a gated prospectus
- **Research lens:** cro-leads
- **Format:** Markdown bundle with ready-to-paste HTML (head and body sections), vanilla JS, a PHP handler sketch, Apache .htaccess and nginx redirect rules, and a homepage FAQ answer snippet
- **Placeholders the business must fill:**
  - PLACEHOLDER_FORM_HANDLER_URL - endpoint that saves the lead and returns {ok:true, deck_url}
  - PLACEHOLDER_DECK_PDF_URL - 2026 partnership deck PDF (whether one exists is UNKNOWN)
  - PLACEHOLDER_AUDIENCE_FIGURE - one figure for all pages (1200+ on partner-with-us vs 500+ on award.html)
  - PLACEHOLDER_OPEN_ITEM_1 / _2 / _3 - inventory that is really unsold for 14-15 Oct
  - PLACEHOLDER_BOOTHS_LEFT - number of booths left, if exhibition is still open
  - PLACEHOLDER_BOOKING_CUTOFF_DATE - last date partnerships can accept a booth or sponsorship
  - PLACEHOLDER_PARTNERSHIPS_WHATSAPP_DIGITS_ONLY - WhatsApp number in international format, digits only, for wa.me
  - PLACEHOLDER_PARTNERSHIPS_PHONE_DIGITS / PLACEHOLDER_PARTNERSHIPS_PHONE_DISPLAY - call button number
  - PLACEHOLDER_CURRENT_PASS_PRICE_INR - numeric price of the pass on sale now (Standard validity ended 30 Sept 2026)
  - PLACEHOLDER_OFFER_VALID_FROM_ISO_DATE - date the current price became valid
  - PLACEHOLDER_EVENT_IMAGE_URL - absolute URL of the event image for og:image and the JSON-LD image
  - PLACEHOLDER_PRIVACY_POLICY_URL - privacy policy link for the consent line
  - PLACEHOLDER_SENDER_ADDRESS - From address the handler's alert email is sent from
  - PLACEHOLDER_LEADS_CSV_PATH_OUTSIDE_WEBROOT - lead storage path, or replace with a CRM API call
  - PLACEHOLDER_DECK_FOLDER - folder holding the PDF (nginx noindex rule)
  - PLACEHOLDER_DEPLOY_DATE - sitemap lastmod

## How to ship

Owner: web dev (about half a day) and partnerships (1-2 h). Target: live by 3 Oct 2026. Sponsor leads that arrive after about 8 Oct are hard to close because booths need fabrication time.

Steps:
1. Partnerships confirms the 2026 deck PDF exists, the inventory that is really still open, the single audience figure, the WhatsApp/phone number, and the current pass price. Delete the "Still available" section if inventory cannot be confirmed today.
2. Web dev edits /partnership.html:
   - Remove the canonical to / and the homepage title.
   - Paste section 1 into the head and section 2 above the existing enquiry form. Keep the existing enquiry form and the contact emails.
   - Add the section 3 script.
   - Deploy the handler (section 4, or any stack that meets the same JSON contract) and host the PDF with X-Robots-Tag noindex.
3. Add the 301 (Apache or nginx, section 5), update internal links and the sitemap, and link the homepage FAQ (section 6).
4. Test:
   - Submit the form once. You should see one generate_lead in GA4 DebugView with form_type=prospectus, an email at partnerships@, and the PDF opening. A failed submit should fire nothing.
   - Run curl -I on http://worldaisummit.com/partner-with-us.html. It should return one 301 to https://www.worldaisummit.com/partnership.html.
   - Check the JSON-LD in the Rich Results Test and confirm the self-canonical in the page source.
5. Ship the section 8 fix to partnership_form_submit at the same time. Then reconcile GA4 counts with the partnerships@ inbox or CRM.

Corrections and caveats:
- Do not describe /partnership.html as the source of most enquiries. Sessions that land on the homepage produce more partnership_form_submit events (about 45%, against 37%).
- Most /partnership.html traffic comes from the r.emails.elets.in mailer redirector, at about 0.4 s of engagement per user. Few humans read the page, so judge the result by deck leads in the CRM, not by pageviews.
- The 2025 partners strip names 2025 explicitly, so it does not imply a 2026 government endorsement. Use logos only with written permission.
- Not re-verified: that /partner-with-us.html gets about 10 views a quarter, and that the current canonical points to /. Check the page source before editing.
- Side finding for the awards owner: /award.html says "Entries from 30k + GST", but the context note gives the 2025 fee as Rs 18,000 + GST.

Sources: Exa fetch of /partnership.html and /partner-with-us.html on 1 Oct 2026. Venue address from marriott.com (https://www.marriott.com/en-us/hotels/blrgs-sheraton-grand-bangalore-hotel-at-brigade-gateway/overview/) and hotelplanner.com (https://www.hotelplanner.com/Hotels/178731/Reservations-Sheraton-Bangalore-Hotel-at-Brigade-Gateway-Bangalore-26-1-Dr-Rajkumar-Rd-Malleswaram-Rajajinagar-560055). 2025 partners from the cio.eletsonline.com press release of 24 Sep 2025, per the verifier. No OpenSEO paid tools were used and no files were edited.

On the separate question in the relayed request ("do you have more CPUs from computer?"): this sandbox reports 4 CPUs (nproc). This subagent cannot add more.

## Content

# /partnership.html: sponsor and exhibitor lead page (World AI Summit 2026)

Sources checked on 1 Oct 2026:
- Live /partnership.html (Exa) has only the tagline and the three contact emails.
- Live /partner-with-us.html (Exa) has the 5 benefit blocks and "1200+ global AI leaders".
- Venue address: 26/1 Dr. Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru 560055. Sources: https://www.marriott.com/en-us/hotels/blrgs-sheraton-grand-bangalore-hotel-at-brigade-gateway/overview/ and https://www.hotelplanner.com/Hotels/178731/Reservations-Sheraton-Bangalore-Hotel-at-Brigade-Gateway-Bangalore-26-1-Dr-Rajkumar-Rd-Malleswaram-Rajajinagar-560055
- 2025 partners: cio.eletsonline.com press release of 24 Sep 2025, and /1st-edition/.

Replace every PLACEHOLDER_ before go-live. If a section's placeholders cannot be filled truthfully, delete that section.

---

## 1. `<head>` of /partnership.html (replaces the current title, description and canonical)

First remove the existing `<link rel="canonical" href="https://www.worldaisummit.com/">` and the homepage `<title>` and description copied from the homepage. Then paste:

```html
<title>Sponsor &amp; Exhibit at World AI Summit 2026, Bengaluru</title>
<meta name="description" content="Partner with World AI Summit 2026, 14-15 Oct, Sheraton Grand Bangalore. Exhibition, speaking slots, roundtables and sponsorship. Download the partnership deck.">
<link rel="canonical" href="https://www.worldaisummit.com/partnership.html">
<meta name="robots" content="index,follow">
<meta property="og:type" content="website">
<meta property="og:url" content="https://www.worldaisummit.com/partnership.html">
<meta property="og:title" content="Sponsor &amp; Exhibit at World AI Summit 2026, Bengaluru">
<meta property="og:description" content="14-15 October 2026, Sheraton Grand Bangalore Hotel at Brigade Gateway. Exhibition, speaking slots, roundtables and sponsorship. Download the 2026 partnership deck.">
<meta property="og:image" content="PLACEHOLDER_EVENT_IMAGE_URL">
<style>
  .sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
  #deck input,#deck button{display:block;width:100%;max-width:420px;margin:0 0 10px;padding:10px;font:inherit}
  #deck .hp{display:none}
</style>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://www.worldaisummit.com/partnership.html#webpage",
      "url": "https://www.worldaisummit.com/partnership.html",
      "name": "Sponsor & Exhibit at World AI Summit 2026, Bengaluru",
      "description": "Partner with World AI Summit 2026, 14-15 Oct, Sheraton Grand Bangalore. Exhibition, speaking slots, roundtables and sponsorship. Download the partnership deck.",
      "inLanguage": "en-IN",
      "isPartOf": { "@type": "WebSite", "@id": "https://www.worldaisummit.com/#website", "url": "https://www.worldaisummit.com/", "name": "World AI Summit" },
      "about": { "@id": "https://www.worldaisummit.com/#event" },
      "publisher": { "@id": "https://www.eletsonline.com/#organization" }
    },
    {
      "@type": "Event",
      "@id": "https://www.worldaisummit.com/#event",
      "name": "World AI Summit 2026",
      "description": "Two-day artificial intelligence summit in Bengaluru with seven tracks: Frontier Models & Compute; Sovereign AI & Geopolitics; Enterprise AI in Production; GCCs; Robotics, Agents & Embodied AI; AI for Bharat; Capital, Founders & Exits.",
      "url": "https://www.worldaisummit.com/",
      "image": ["PLACEHOLDER_EVENT_IMAGE_URL"],
      "startDate": "2026-10-14",
      "endDate": "2026-10-15",
      "eventStatus": "https://schema.org/EventScheduled",
      "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
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
      "organizer": { "@id": "https://www.eletsonline.com/#organization" },
      "offers": {
        "@type": "Offer",
        "url": "https://www.worldaisummit.com/delegate/",
        "price": "PLACEHOLDER_CURRENT_PASS_PRICE_INR",
        "priceCurrency": "INR",
        "availability": "https://schema.org/InStock",
        "validFrom": "PLACEHOLDER_OFFER_VALID_FROM_ISO_DATE"
      }
    },
    {
      "@type": "Organization",
      "@id": "https://www.eletsonline.com/#organization",
      "name": "Elets Technomedia",
      "url": "https://www.eletsonline.com/"
    }
  ]
}
</script>
```

Notes:
- The JSON-LD parses as valid JSON (checked). The price must be a plain number such as "30000". The Standard pass validity ended on 30 Sept 2026, so use the price on sale today.
- `performer` is left out on purpose. This is a sponsor page. The homepage Event markup should carry only verified 2026 speakers.
- If the homepage already outputs an Event with `@id` "https://www.worldaisummit.com/#event", keep the two blocks identical or remove the Event node here and keep only the `about` reference.
- If awards-night sponsorship is confirmed as still open, you can use the original 166-character description instead: "Partner with World AI Summit 2026, 14-15 Oct, Sheraton Grand Bangalore. Exhibition, speaking, roundtables and awards-night sponsorship. Download the partnership deck." Google may truncate it.

---

## 2. Body of /partnership.html (above the existing enquiry form and contact emails)

```html
<section id="partner-hero">
  <h1>Sponsor and exhibit at World AI Summit 2026</h1>
  <p>14-15 October 2026, Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. Meet PLACEHOLDER_AUDIENCE_FIGURE AI leaders and innovators across seven tracks, from Frontier Models &amp; Compute to AI for Bharat.</p>
  <p><a class="btn" href="#deck-section">Get the 2026 partnership deck</a> <a class="btn btn-outline" href="mailto:partnerships@worldaisummit.com">Write to partnerships@worldaisummit.com</a></p>
</section>

<section id="partner-benefits">
  <h2>Five ways to partner with the summit</h2>
  <ol>
    <li><h3>Sponsorship</h3><p>Brand visibility across the summit, in front of PLACEHOLDER_AUDIENCE_FIGURE AI leaders and innovators.</p></li>
    <li><h3>Exhibit</h3><p>Engage directly with AI leaders and innovators at your booth.</p></li>
    <li><h3>Centre-stage speaking slot</h3><p>Showcase your AI leadership through keynotes, panels and power talks.</p></li>
    <li><h3>One-on-one meetings and executive roundtables</h3><p>Meet AI leaders in one-on-one meetings and executive roundtables at the summit.</p></li>
    <li><h3>Feature in the AI Innovation Report</h3><p>Showcase your journey in the AI Innovation Report, to be launched at the summit.</p></li>
  </ol>
</section>

<!-- Delete this whole section if partnerships cannot confirm open inventory today. -->
<section id="still-available">
  <h2>Still available for 14-15 Oct</h2>
  <ul>
    <li>PLACEHOLDER_OPEN_ITEM_1 (for example: exhibition booths, PLACEHOLDER_BOOTHS_LEFT left)</li>
    <li>PLACEHOLDER_OPEN_ITEM_2 (for example: awards-night sponsorship)</li>
    <li>PLACEHOLDER_OPEN_ITEM_3 (for example: networking-dinner sponsorship)</li>
  </ul>
  <p>Booths need time to fabricate, so please confirm by PLACEHOLDER_BOOKING_CUTOFF_DATE.</p>
</section>

<section id="deck-section">
  <h2>Download the 2026 partnership deck</h2>
  <p>The deck covers packages, exhibition options and speaking formats. It downloads as soon as you submit, and a copy goes to our partnerships team so they can follow up.</p>
  <form id="deck" action="PLACEHOLDER_FORM_HANDLER_URL" method="post" novalidate>
    <label class="sr-only" for="deck-name">Full name</label>
    <input id="deck-name" name="name" required placeholder="Full name" autocomplete="name">
    <label class="sr-only" for="deck-company">Company</label>
    <input id="deck-company" name="company" required placeholder="Company" autocomplete="organization">
    <label class="sr-only" for="deck-designation">Designation</label>
    <input id="deck-designation" name="designation" placeholder="Designation" autocomplete="organization-title">
    <label class="sr-only" for="deck-email">Work email</label>
    <input id="deck-email" name="email" type="email" required placeholder="Work email" autocomplete="email">
    <label class="sr-only" for="deck-phone">Mobile (WhatsApp)</label>
    <input id="deck-phone" name="phone" type="tel" required placeholder="Mobile (WhatsApp)" autocomplete="tel">
    <input class="hp" name="website" tabindex="-1" autocomplete="off" aria-hidden="true">
    <input type="hidden" name="form_type" value="prospectus">
    <input type="hidden" name="utm_source"><input type="hidden" name="utm_medium"><input type="hidden" name="utm_campaign"><input type="hidden" name="utm_content">
    <button type="submit">Get the 2026 partnership deck</button>
    <p><small>We use these details to send you the deck and to contact you about partnering with World AI Summit 2026. See our <a href="PLACEHOLDER_PRIVACY_POLICY_URL">privacy policy</a>.</small></p>
  </form>
  <p id="deck-msg" role="status" aria-live="polite"></p>
</section>

<section id="partners-2025" aria-labelledby="p2025">
  <h2 id="p2025">2025 edition partners</h2>
  <p>The 2025 edition of World AI Summit had the Department of Electronics, IT, BT, Government of Karnataka as Host Partner, the IndiaAI Mission as Co-Host Partner and KDEM (Karnataka Digital Economy Mission) as Strategic Partner. These were partners of the 2025 edition.</p>
</section>

<section id="partner-contact">
  <h2>Talk to the partnerships team</h2>
  <p>
    <a class="btn" id="wa-partners" href="https://wa.me/PLACEHOLDER_PARTNERSHIPS_WHATSAPP_DIGITS_ONLY?text=Hello%2C%20I%20would%20like%20to%20discuss%20partnering%20with%20World%20AI%20Summit%202026">WhatsApp the partnerships team</a>
    <a class="btn btn-outline" id="call-partners" href="tel:+PLACEHOLDER_PARTNERSHIPS_PHONE_DIGITS">Call PLACEHOLDER_PARTNERSHIPS_PHONE_DISPLAY</a>
  </p>
  <p>Or write to <a href="mailto:partnerships@worldaisummit.com">partnerships@worldaisummit.com</a>.</p>
</section>
```

---

## 3. Form script (paste before `</body>`; needs the GA4 gtag snippet already on the page)

`generate_lead` fires only after the server confirms it saved the lead. It does not fire on page load or reload.

```html
<script>
(function () {
  var f = document.getElementById('deck');
  var msg = document.getElementById('deck-msg');
  if (!f) return;

  // Carry mailer UTM tags into the lead record
  var q = new URLSearchParams(window.location.search);
  ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content'].forEach(function (k) {
    var el = f.querySelector('input[name="' + k + '"]');
    if (el && q.get(k)) el.value = q.get(k);
  });

  f.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!f.checkValidity()) { f.reportValidity(); return; }
    var btn = f.querySelector('button');
    btn.disabled = true;
    msg.textContent = 'Sending your details.';

    fetch(f.action, { method: 'POST', body: new FormData(f), headers: { 'Accept': 'application/json' } })
      .then(function (r) { if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); })
      .then(function (d) {
        if (!d || d.ok !== true || !d.deck_url) throw new Error('not saved');
        if (typeof gtag === 'function') {
          gtag('event', 'generate_lead', { form_type: 'prospectus' });
        }
        f.hidden = true;
        msg.textContent = 'Thank you. Your deck is ready: ';
        var a = document.createElement('a');
        a.href = d.deck_url;
        a.setAttribute('download', '');
        a.textContent = 'download the 2026 partnership deck (PDF)';
        msg.appendChild(a);
        msg.appendChild(document.createTextNode('. Our partnerships team will also be in touch.'));
        window.open(d.deck_url, '_blank', 'noopener');
      })
      .catch(function () {
        btn.disabled = false;
        msg.textContent = 'That did not go through. Please try again, or write to partnerships@worldaisummit.com.';
      });
  });

  // Optional: measure direct-contact clicks separately from deck leads
  [['wa-partners', 'whatsapp'], ['call-partners', 'phone']].forEach(function (p) {
    var el = document.getElementById(p[0]);
    if (el) el.addEventListener('click', function () {
      if (typeof gtag === 'function') gtag('event', 'partnership_contact_click', { method: p[1] });
    });
  });
})();
</script>
```

---

## 4. Handler contract (any stack). Example in PHP if the site's Apache server runs PHP

Contract: accept a POST and validate it. Save the lead to the CRM or sheet and email partnerships@. Then return `{"ok":true,"deck_url":"..."}`. On any failure return `ok:false`, so GA4 does not count the lead.

```php
<?php
// deck-request.php: replace the PLACEHOLDER_ values. Swap mail() for the CRM/SMTP you use.
header('Content-Type: application/json');
if ($_SERVER['REQUEST_METHOD'] !== 'POST') { http_response_code(405); echo '{"ok":false}'; exit; }
if (!empty($_POST['website'])) { http_response_code(400); echo '{"ok":false}'; exit; } // bot honeypot

$clean = function ($k) { return trim(str_replace(["\r", "\n"], ' ', (string)($_POST[$k] ?? ''))); };
$name = $clean('name'); $company = $clean('company'); $designation = $clean('designation');
$email = $clean('email'); $phone = $clean('phone');

if ($name === '' || $company === '' || !filter_var($email, FILTER_VALIDATE_EMAIL)
    || !preg_match('/^[0-9+\-\s()]{8,20}$/', $phone)) {
  http_response_code(422); echo '{"ok":false,"error":"invalid"}'; exit;
}

$utm = [];
foreach (['utm_source','utm_medium','utm_campaign','utm_content'] as $k) { $utm[$k] = $clean($k); }

// 1) Store the lead (CSV shown; use your CRM API if you have one). Keep this file outside the web root.
$row = [date('c'), $name, $company, $designation, $email, $phone, 'prospectus'] + $utm;
$ok = (bool) file_put_contents('PLACEHOLDER_LEADS_CSV_PATH_OUTSIDE_WEBROOT', implode(',', array_map(function ($v) {
  return '"' . str_replace('"', '""', $v) . '"'; }, array_values($row))) . "\n", FILE_APPEND | LOCK_EX);

// 2) Alert the partnerships team
$body = "Partnership deck request (World AI Summit 2026)\n\nName: $name\nCompany: $company\nDesignation: $designation\nEmail: $email\nPhone/WhatsApp: $phone\nSource: " . implode(' / ', array_filter($utm)) . "\n";
$ok = mail('partnerships@worldaisummit.com', 'Deck request: ' . $company, $body,
  "From: PLACEHOLDER_SENDER_ADDRESS\r\nReply-To: $email") && $ok;

if (!$ok) { http_response_code(500); echo '{"ok":false}'; exit; }
echo json_encode(['ok' => true, 'deck_url' => 'PLACEHOLDER_DECK_PDF_URL']);
```

Keep the PDF out of search results. Apache, in the folder that holds the deck:

```apache
<FilesMatch "\.pdf$">
  Header set X-Robots-Tag "noindex, nofollow"
</FilesMatch>
```

The nginx equivalent: `location ~* ^/PLACEHOLDER_DECK_FOLDER/.*\.pdf$ { add_header X-Robots-Tag "noindex, nofollow"; }`

---

## 5. Redirect /partner-with-us.html to /partnership.html (301, single hop)

Apache `.htaccess` (place it above any existing www/https rules so non-www requests also resolve in one hop):

```apache
RewriteEngine On
RewriteRule ^partner-with-us\.html$ https://www.worldaisummit.com/partnership.html [R=301,L]
```

nginx (add to every server block that serves worldaisummit.com and www.worldaisummit.com):

```nginx
location = /partner-with-us.html {
    return 301 https://www.worldaisummit.com/partnership.html;
}
```

Also:
- Change every internal link to /partner-with-us.html so it points to /partnership.html.
- In sitemap.xml, remove /partner-with-us.html and add `<url><loc>https://www.worldaisummit.com/partnership.html</loc><lastmod>PLACEHOLDER_DEPLOY_DATE</lastmod></url>`.
- Optional, low effort: add a "Sponsor &amp; Exhibit" link to /partnership.html in the header and footer. Cypher's header and footer carry similar links.

---

## 6. Homepage FAQ: link "Are exhibition and sponsorship opportunities available?"

Replace the answer text with:

```html
<p>Yes. Partnership options for 14-15 October 2026 include exhibition, sponsorship, speaking slots and executive roundtables. See the <a href="/partnership.html">sponsorship and exhibition options</a> and download the 2026 partnership deck, or write to <a href="mailto:partnerships@worldaisummit.com">partnerships@worldaisummit.com</a>.</p>
```

If the homepage has FAQPage JSON-LD, use the same wording (without HTML tags, or with the `<a>` tag, which Google allows) in that question's `acceptedAnswer.text`.

---

## 7. One audience figure

/partner-with-us.html says "1200+ global AI leaders" and /award.html says "500+ Industry Leaders in Attendance". Partnerships should pick the figure it can support (for example, 2025 attendance records). Put it in PLACEHOLDER_AUDIENCE_FIGURE and update /award.html and the homepage to match.

---

## 8. Measurement fix: do this with the deploy

- 51 `partnership_form_submit` events in Aug-Sep have /thankyou.html as the landing page. The event probably fires when the thank-you page loads or reloads. Move it to the same server-success pattern as in section 3, add a parameter (`form_type: 'sponsor_enquiry'` or `'general'`), and remove any firing on /thankyou.html page load.
- In GA4 Admin, mark `generate_lead` as a key event.
- Check the roughly 48 enquiries a month (97 users over Aug-Sep) against the partnerships@ inbox or CRM before anyone sizes the uplift. On GA4 counts, sessions that land on /partnership.html produce about 37% of `partnership_form_submit` events (117 of about 315). Sessions that land on the homepage produce about 45% (142).
