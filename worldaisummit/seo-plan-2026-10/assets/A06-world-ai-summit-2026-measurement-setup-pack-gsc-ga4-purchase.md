# A06: World AI Summit 2026: measurement setup pack (GSC, GA4 purchase, generate_lead, noindex, UTMs). Due 2 Oct 2026

- **For recommendation:** 7. Measurement you can trust for the next 17 days: www Domain property, a real purchase event, separate lead events, and UTMs on mailers, listings and speaker shares
- **Research lens:** cro-leads
- **Format:** Markdown runbook with ready-to-paste PHP, HTML and JS snippets and UTM templates
- **Placeholders the business must fill:**
  - PLACEHOLDER_GSC_OWNER_AT_ELETS - the person or team at Elets who may already own a worldaisummit.com Search Console property
  - PLACEHOLDER_VALUE_BASIS - whether the GA4 purchase value is ex-GST (with tax sent separately) or incl-GST; use the same rule for passes and award nominations
  - PLACEHOLDER_TEST_ORDER_ID - transaction_id of the real test order used in DebugView, so it can be excluded later
  - PLACEHOLDER_MAILER_SEGMENT_NAMES - the email team's segment list names used in utm_content
  - PLACEHOLDER_CONFIRMED_SPEAKER_SLUGS - slugs from speakers.json for confirmed 2026 speakers only, for the share kit

## How to ship

I could not run three of the checks myself: the proxy blocked worldaisummit.com from this session (HTTP 403). So the web dev needs to do section 0 first: confirm the GA tag is in <head>, find out whether each form posts by AJAX or full page load, and find the GA4 rules behind form_submit and partnership_form_submit.

Then work through the runbook in order:
1. Marketing does sections 1-2 in GSC and GA4 Admin, about 50 minutes. The first step is asking Elets whether a www or sc-domain Search Console property already exists.
2. Web dev ships sections 3-5 in one deploy, about 2-3 hours:
   - the hostname guard snippet in <head> on every page
   - the purchase block in /delegate/success.php and /awards/success.php, after the payment check, plus a one-time `ga4_purchase_sent` column
   - generate_lead using 5A (AJAX) or 5B (full post), whichever section 0 shows
   - noindex on /thankyou.html
3. Test one real order and one entry per form in GA4 DebugView on the live domain.
4. The email team loads the section 6 UTM templates before the next send.
5. Leave the old form_submit and partnership_form_submit events running for 2-3 days and compare them with the inboxes. Then unmark them as key events.

Corrections from the original recommendation, which this runbook already applies:
- Search Console is not promised to backfill old data. Expect www data from about 3-5 Oct.
- The purchase event is client-side, rendered by PHP. It is not server-side tracking.
- The existing partnership_form_submit event is handled as well, not just form_submit.
- UTMs extend the existing world_ai_summit_2026_* names instead of adding a new wais26 scheme.
- Mailer traffic should be judged on engaged sessions and lead/purchase events.

Sources: [Search Console data collection](https://support.google.com/webmasters/answer/34592), [GA4 transaction_id dedupe](https://support.google.com/analytics/answer/12313109), [GA4 default channel group](https://support.google.com/analytics/answer/9756891).

## Content

# World AI Summit 2026: measurement you can trust for 1-17 Oct

Owners: web dev + marketing. Deadline: 2 Oct 2026.
GA4 property: "Elets World AI Summit 2025" (properties/490291049), web stream G-QEB6N0MFLC.

---

## 0. Ten-minute checks before you start (these are not yet verified)

1. **GA tag position.** View the source of https://www.worldaisummit.com/ and confirm that the gtag.js snippet for G-QEB6N0MFLC sits inside `<head>`. Search Console can only verify a property through Google Analytics if the tag is in `<head>`.
2. **How each form submits.** Open DevTools > Network and send a test entry on the delegate, sponsor/partnership and awards forms.
   - The page stays put and an XHR/fetch request returns: the form is **AJAX**, so use 5A.
   - The browser navigates to /thankyou.html or another page: the form is a **full post**, so use 5B.
3. **Where the current lead events come from.** In GA4 Admin > Events, check "Create event" and "Modify event", and check the GTM container if there is one. Find the rules that produce `form_submit` and `partnership_form_submit`.
   - Inferred: `form_submit` is also the event that enhanced measurement's "Form interactions" sends automatically whenever a browser form submits, whether or not the server accepts the entry. That would explain why Sept shows 178 form_submit events on /delegate landings, while only 18 users reached /delegate/success.php in all of Jul-Sep.
   - Inferred: `partnership_form_submit` appears to fire when /thankyou.html loads. In Jul-Sep, /thankyou.html shows 391 key events from 398 views, while /partnership.html shows 0. In Sept, 40 of these events came from sessions that landed directly on /thankyou.html.

---

## 1. Search Console for the www site (marketing, 20 min)

1. **Ask before creating anything.** Check with PLACEHOLDER_GSC_OWNER_AT_ELETS whether any Elets Google account already owns `sc-domain:worldaisummit.com` or `https://www.worldaisummit.com/`. If one exists, ask to be added as Owner or Full user. That is faster than verifying a new property, and it keeps the history.
2. **If no property exists, add one today:**
   - Preferred: Domain property `sc-domain:worldaisummit.com`, verified with a DNS TXT record at the registrar.
   - If DNS access is slow: URL-prefix `https://www.worldaisummit.com/`, verified through Google Analytics. This needs the tag in `<head>` (check 0.1) and Edit permission on the GA4 property.
3. **Set expectations.** Google says data collection starts when anyone adds the property, even before verification, and takes a few days to accrue (support.google.com/webmasters/answer/34592). Do not count on past data appearing. With GSC's usual 2-3 day lag, expect www query data from about 3-5 Oct at the earliest. That gives roughly one week of usable data before 14 Oct.
4. **Submit the sitemap.** Use the sitemap that already lists /delegate/ and the speaker pages.
5. **Connect it in OpenSEO.** Connect the new property in the OpenSEO project, then confirm it with the free `get_search_console_performance` read.

---

## 2. GA4 admin (marketing, 30 min)

1. **Unwanted referrals.** Go to Admin > Data streams > G-QEB6N0MFLC > Configure tag settings > List unwanted referrals, and add `checkout.stripe.com` (match type: contains). In Sept it brought 5 sessions as a referral.
2. **Data retention.** Go to Admin > Data settings > Data retention and set it to 14 months, so the 2026 window can be compared next year.
3. **Custom dimension.** Go to Admin > Custom definitions > Create custom dimension:
   - Scope: Event
   - Name: Form type
   - Event parameter: `form_type`
   
   Without this, `form_type` will not appear in reports.
4. **Key events.**
   - Create a key event named `generate_lead` (Admin > Key events > New key event).
   - Keep `purchase` as a key event.
   - Leave `form_submit` and `partnership_form_submit` running for 2-3 days. Check `generate_lead` against the leads that actually arrive in the registration@ and partnerships@ inboxes.
   - Once the numbers agree, unmark both old events as key events. They will still be collected as plain events, and the old data stays.
   - Switch off the rule that fires `partnership_form_submit` when /thankyou.html loads.

---

## 3. Hostname guard: replace the GA snippet on every page (web dev, 10 min)

GA4 has no hostname view filter. This guard stops data from 127.0.0.1, localhost, indiapharmaexpo.com, default.kinfra.myqcloud.com and any mirror that copies the tag. All of these appeared as hostnames in Jul-Sep. Keep the snippet in `<head>`.

```html
<script async src="https://www.googletagmanager.com/gtag/js?id=G-QEB6N0MFLC"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  // Send data only from the live site
  if (/^(www\.)?worldaisummit\.com$/.test(location.hostname)) {
    gtag('config', 'G-QEB6N0MFLC');
  }
</script>
```

---

## 4. purchase event on /delegate/success.php and /awards/success.php (web dev, 1-2 h)

**How it works.** The `purchase` event is a client-side gtag event. PHP renders it once the server has confirmed the payment. It is not server-side tracking. True server-side tracking would need the GA4 Measurement Protocol, with the visitor's client_id from the `_ga` cookie, and is not needed for this window.

**Why json_encode instead of htmlspecialchars.** `json_encode` escapes values safely for JavaScript. `htmlspecialchars` would put `&#039;` into pass names and can break the string.

**Never send an empty transaction_id.** GA4 dedupes all purchase events whose transaction_id is empty (support.google.com/analytics/answer/12313109).

Run this SQL once (rename the table and column to match your schema):

```sql
ALTER TABLE orders ADD COLUMN ga4_purchase_sent TINYINT(1) NOT NULL DEFAULT 0;
```

Paste this into success.php. It must come after your payment check (for example, the Stripe Checkout Session for this order has `payment_status` = `paid`) and after the GA tag in `<head>`:

```php
<?php
// $pdo, $paymentConfirmed, $orderId, $amount, $qty, $passName, $passCode come from your existing order code.
// PLACEHOLDER_VALUE_BASIS: decide whether 'value' is ex-GST (recommended, send GST in 'tax') or incl-GST. Use the same rule on both pages.
$ga4Purchase = null;
if (!empty($paymentConfirmed) && (string)$orderId !== '' && (float)$amount > 0) {
    // Render once per order, even if the page is refreshed (success.php had 78 views from 18 users in Jul-Sep)
    $stmt = $pdo->prepare('UPDATE orders SET ga4_purchase_sent = 1 WHERE order_id = ? AND ga4_purchase_sent = 0');
    $stmt->execute([$orderId]);
    if ($stmt->rowCount() === 1) {
        $q = max(1, (int)$qty);
        $ga4Purchase = [
            'transaction_id' => (string)$orderId,
            'value'          => round((float)$amount, 2),
            'currency'       => 'INR',
            // 'tax'         => round((float)$gstAmount, 2),   // if value is ex-GST
            'items'          => [[
                'item_id'       => (string)$passCode,
                'item_name'     => (string)$passName,
                'item_category' => 'delegate_pass',            // on /awards/success.php use 'award_nomination'
                'price'         => round((float)$amount / $q, 2),
                'quantity'      => $q,
            ]],
        ];
    }
}
header('X-Robots-Tag: noindex', true);   // keep success pages out of Google
?>
<?php if ($ga4Purchase): ?>
<script>
  gtag('event', 'purchase', <?= json_encode($ga4Purchase, JSON_HEX_TAG | JSON_HEX_AMP | JSON_HEX_APOS | JSON_HEX_QUOT | JSON_UNESCAPED_UNICODE) ?>);
</script>
<?php endif; ?>
```

The `header()` call must run before any HTML output. If headers have already been sent, add `<meta name="robots" content="noindex">` to the page's `<head>` instead.

**Fallback if you cannot add the DB column.** Use a session flag instead. It is weaker, because a buyer who opens the page on another device will fire it again:

```php
session_start();
$k = 'ga4_sent_' . $orderId;
if (empty($_SESSION[$k])) { $_SESSION[$k] = 1; /* build $ga4Purchase as above */ }
```

**Testing.** Turn on GA4 DebugView via Google Tag Assistant and check one real order. Note its transaction_id (PLACEHOLDER_TEST_ORDER_ID) so it can be excluded later. The hostname guard blocks localhost, so tests must run on the live domain.

---

## 5. generate_lead, fired only when the server accepts the entry (web dev, 1 h)

**form_type values:**

| Form | form_type |
|---|---|
| /delegate/ pass enquiry or registration | `delegate`, or `group` when 3 or more delegates are booked (the group discount applies at 3+) |
| Sponsorship / exhibition (/partnership.html, /partner-with-us.html) | `sponsor` |
| Brochure / prospectus request | `prospectus` |
| /awards/ nomination | `award_nomination` |
| Contact / general enquiry | `enquiry` |

### 5A. AJAX forms: fire inside the success callback, after the server confirms the save

```js
// Example with jQuery; use the same idea with fetch()
$.post(form.action, $(form).serialize())
  .done(function (res) {
    // Fire only when your handler reports success; adjust the check to its response
    gtag('event', 'generate_lead', {
      form_type: 'sponsor',            // value from the table above
      form_location: location.pathname
    });
    // ...existing success message or redirect
  });
```

For the delegate form, compute the type from the quantity:

```js
var qty = parseInt(form.querySelector('[name="qty"]').value, 10) || 1;  // use your field name
gtag('event', 'generate_lead', { form_type: qty >= 3 ? 'group' : 'delegate', form_location: location.pathname });
```

### 5B. Full-post forms that redirect to /thankyou.html

In the PHP handler, after the entry is saved:

```php
header('Location: /thankyou.html#lead=sponsor', true, 303);   // value from the table above
exit;
```

In /thankyou.html, place this after the GA tag in `<head>`:

```html
<meta name="robots" content="noindex">
<script>
  (function () {
    var m = location.hash.match(/^#lead=(delegate|group|sponsor|prospectus|award_nomination|enquiry)$/);
    if (!m) return;   // direct visits, organic landings and refreshes fire nothing
    gtag('event', 'generate_lead', { form_type: m[1] });
    history.replaceState(null, '', location.pathname);   // remove the marker so a refresh does not fire again
  })();
</script>
```

**Keep /thankyou.html crawlable.** Do not add it to a robots.txt Disallow rule, or Google will never see the noindex. Remove it from the sitemap if it is listed there.

---

## 6. UTMs: extend the existing world_ai_summit_2026_* names (email team, 30 min)

**Existing tags (keep them):** `world_ai_summit_2026`, `world_ai_summit_2026_sponsorship`, `world_ai_summit_2026_delegate` and `world_ai_awards_2026`, plus `utm_source=mailer` / `utm_medium=email`. Stop using `wai2026_delegate` and `wai2026_speakers` on new links. Leave links already sent as they are.

**Medium values.** Use only `email`, `referral` and `social`. GA4's default channel group sorts these into Email, Referral and Organic Social. A made-up medium such as "listing" or "speaker_share" ends up as Unassigned (support.google.com/analytics/answer/9756891).

### Elets mailers (every link, including those wrapped by r.emails.elets.in)

```
?utm_source=mailer&utm_medium=email&utm_campaign=world_ai_summit_2026_delegate&utm_content=<segment>_<yyyymmdd>
```

- For sponsorship mailers, use `utm_campaign=world_ai_summit_2026_sponsorship`.
- For awards mailers, use `utm_campaign=world_ai_awards_2026`.
- `<segment>` comes from the email team's list name (PLACEHOLDER_MAILER_SEGMENT_NAMES, e.g. bfsi, gcc, education, enterprise, startup, partner).

Example:

```
https://www.worldaisummit.com/delegate/?utm_source=mailer&utm_medium=email&utm_campaign=world_ai_summit_2026_delegate&utm_content=gcc_20261003
```

### Event listings

```
?utm_source=<site>&utm_medium=referral&utm_campaign=world_ai_summit_2026_listings
```

`<site>` values: `10times`, `allevents`, `eventbrite`, `globaltradefairs`, `aievents`, `eventmap`.

Example:

```
https://www.worldaisummit.com/delegate/?utm_source=10times&utm_medium=referral&utm_campaign=world_ai_summit_2026_listings
```

The allevents.in listing already carries a UTM. Replace it only if the listing can be edited.

### Speaker share kit (confirmed 2026 speakers only)

```
https://www.worldaisummit.com/delegate/?utm_source=linkedin&utm_medium=social&utm_campaign=world_ai_summit_2026_speaker_share&utm_content=<speaker-slug>
```

`<speaker-slug>` is the slug in worldaisummit/speakers/speakers.json for each confirmed speaker (PLACEHOLDER_CONFIRMED_SPEAKER_SLUGS).

### Rules

- Use lowercase and underscores, with no spaces.
- Never add UTMs to internal links within worldaisummit.com. A tagged internal link starts a new session and overwrites the real source.

---

## 7. Reading the numbers from 3 Oct

**Judge mailers on engaged sessions, generate_lead and purchase, not on sessions.**
- In Sept, r.emails.elets.in/referral brought 224,681 sessions from 221,076 users, nearly one session each.
- Those sessions landed almost evenly on / (111,443) and /partnership.html (110,197).
- The key-event rate was 0.04%.
- Inferred: this looks like email security scanners or link prefetching. UTMs will rename this traffic but will not remove it.

**Expect small online purchase counts.** Only 18 users reached /delegate/success.php in Jul-Sep. Ask the registration desk to keep its own count of passes and nominations by source (mailer segment, listing, speaker, direct) for 1-17 Oct, so offline and invoice bookings are not missed.

---

## Checklist (all by 2 Oct 2026)

- [ ] 0. Tag position, form type and current event rules checked (web dev)
- [ ] 1. Existing GSC property found or new one added, sitemap submitted, connected in OpenSEO (marketing)
- [ ] 2. Unwanted referral, 14-month retention, form_type dimension, generate_lead key event (marketing)
- [ ] 3. Hostname guard live on all pages (web dev)
- [ ] 4. purchase live on both success.php pages and tested in DebugView (web dev)
- [ ] 5. generate_lead live on every form; /thankyou.html noindex; page-load rule switched off (web dev)
- [ ] 6. UTM templates in the mailer tool, listings and speaker kit (email team)

