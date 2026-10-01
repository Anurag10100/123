# A07: Delegate pass page rebuild for /delegate/: head tags, above-the-fold copy, inclusions table, FAQ, Event JSON-LD and 301 redirects (Apache and nginx)

- **For recommendation:** Fix the pass prices that contradict each other and rebuild /delegate/ as the page that sells passes, with every registration URL pointing to it
- **Research lens:** site-deep-read
- **Format:** Markdown, with ready-to-paste HTML, JSON-LD, Apache .htaccess, nginx and shell blocks
- **Placeholders the business must fill:**
  - PLACEHOLDER_PREMIUM_PRICE (display, e.g. 30,000)
  - PLACEHOLDER_VIP_PRICE (display, e.g. 60,000)
  - PLACEHOLDER_PREMIUM_PRICE_INR (digits only, for JSON-LD and speakers.json)
  - PLACEHOLDER_VIP_PRICE_INR (digits only, for JSON-LD)
  - PLACEHOLDER_GST_LINE ('inclusive of GST' or 'plus 18% GST')
  - PLACEHOLDER_PRICE_PHASE_LABEL (replaces 'Three release phases' on homepage)
  - PLACEHOLDER_THIRD_TIER_DECISION (homepage tier with 'Access to event photos & videos': remove, or name and price it)
  - PLACEHOLDER_POLICY_ROUNDTABLE (does Premium include AI policy roundtables: Yes/No)
  - PLACEHOLDER_GST_ANSWER
  - PLACEHOLDER_GST_INVOICE_ANSWER
  - PLACEHOLDER_TRANSFER_POLICY
  - PLACEHOLDER_REFUND_POLICY
  - PLACEHOLDER_ONSPOT_ANSWER
  - PLACEHOLDER_SPEAKERS_CONFIRM (confirm the 8 named speakers are still on the 2026 programme)
  - PLACEHOLDER_EVENT_IMAGE_PATH (event banner image path; delete the image line in the JSON-LD if none)

## How to ship

Ship by 2 Oct 2026.

1. **Pricing decision (registration and marketing, 15 minutes).**
   - Fill the price placeholders (Premium and VIP, display and digits-only) and PLACEHOLDER_GST_LINE.
   - Decide the third homepage tier (PLACEHOLDER_THIRD_TIER_DECISION) and PLACEHOLDER_POLICY_ROUNDTABLE.
   - Answer the FAQ placeholders: GST, invoice, transfer, refund and on-spot registration.
   - Confirm the 8 speakers are still on the programme.
   - If allevents.in really sells at Rs 20,000, the homepage price may be the current one. Settle this before changing any page.
2. **Rebuild /delegate/ (web developer, 2 to 3 hours).**
   - Replace the head tags (section 1).
   - Insert the hero with the H1 (section 2).
   - Delete the Early Bird and Standard rows and merge the General/VIP Delegate cards into the Premium/VIP naming (sections 3 and 4).
   - Add the speaker strip, programme and venue, and FAQ (sections 5 to 7).
   - Paste the JSON-LD (section 8).
   - Point both Book buttons at the existing Checkout section id.
3. **Redirects.**
   - Use the Apache block if the static site runs on Apache or cPanel, or the nginx map and if-block otherwise.
   - Remove the old rules that send /registration to the homepage.
   - Run the curl loop. Every URL must return a single 301 to https://www.worldaisummit.com/delegate/.
4. **Same price everywhere, on the same deploy (section 10).**
   - Homepage block, then the /ai-conference-bengaluru-2026.html Register block.
   - The sed command on the speaker pages, then the grep until nothing shows 'Rs 20,000' or 'Rs 35,000'.
   - Sitemap cleanup.
   - Update speakers.json before the next generator build.
   - Email the elets.net and allevents.in owners.
5. **Validate.**
   - Run /delegate/ through validator.schema.org and Google's Rich Results Test. Confirm the Event is detected and no placeholder text remains.
   - Check that the page has exactly one H1.
6. **Search Console.**
   - The connected property is the non-www URL-prefix property (https://worldaisummit.com/). It reports nothing for the www pages.
   - Add a Domain property for worldaisummit.com, or a www URL-prefix property.
   - Request indexing for https://www.worldaisummit.com/delegate/ and resubmit the sitemap.
7. **Check in 14 days.**
   - Rerun the free OpenSEO audit (missing-h1 and redirect-chain issues on these URLs should be gone).
   - Watch positions for 'ai summit registration' (#4) and 'ai summit 2026 registration' (#10).

Sources: the live /delegate/ and /speaker.html pages fetched through Exa on 1 Oct 2026, and the hotel address from the official Marriott page (https://www.marriott.com/en-us/hotels/blrgs-sheraton-grand-bangalore-hotel-at-brigade-gateway/rooms/). Speaker names, roles and organisations come from /home/user/123/worldaisummit/speakers/speakers.json (confirmed_2026 = true); their /assets/speaker_details/ slugs come from the verified meta-description list (sanjeev-gupta was seen separately). Draft JSON-LD with the same structure is at /tmp/claude-0/-home-user-123/bf9e82cf-ebf4-58a1-ab65-7230ef80c0ff/scratchpad/ld.json; it says "BusinessEvent" where the asset says "Event". No project files were edited and no paid OpenSEO tools were used.

On the user's question about CPUs: this session's container reports 4 CPUs (nproc). This subagent cannot add more.

## Content

# World AI Summit 2026: delegate pass page asset (status as of 1 Oct 2026)

Fill every PLACEHOLDER_ before you publish. The price placeholders are the 15-minute pricing decision. The live /delegate/ page says 'Standard Access (Valid till 30th Sept 2026)', so that tier has expired. If Elets confirms Late Access is the current tier, the values are Rs 30,000 for Premium and Rs 60,000 for VIP. Only Elets can confirm this, because allevents.in, the official ticketing partner, still shows 'from Rs 20,000'.

Placeholder formats:
- PLACEHOLDER_PREMIUM_PRICE and PLACEHOLDER_VIP_PRICE are display text with a comma, for example 30,000.
- PLACEHOLDER_PREMIUM_PRICE_INR and PLACEHOLDER_VIP_PRICE_INR are digits only, for example 30000. They go in the JSON-LD.

---

## 1. `<head>` for https://www.worldaisummit.com/delegate/

Replace the current title 'World AI Summit 2026 | Delegate Pass Registration' and the meta description.

```html
<title>World AI Summit 2026 Tickets &amp; Delegate Passes | Bengaluru</title>
<meta name="description" content="Book your World AI Summit 2026 pass: 14-15 Oct, Sheraton Grand Bangalore at Brigade Gateway. Premium and VIP passes, 10% off for 3+ delegates. Register online.">
<link rel="canonical" href="https://www.worldaisummit.com/delegate/">
<meta property="og:type" content="website">
<meta property="og:url" content="https://www.worldaisummit.com/delegate/">
<meta property="og:title" content="World AI Summit 2026 Tickets &amp; Delegate Passes | Bengaluru">
<meta property="og:description" content="Book your World AI Summit 2026 pass: 14-15 Oct, Sheraton Grand Bangalore at Brigade Gateway. Premium and VIP passes, 10% off for 3+ delegates. Register online.">
<meta property="og:image" content="https://www.worldaisummit.com/PLACEHOLDER_EVENT_IMAGE_PATH">
<meta name="twitter:card" content="summary_large_image">
```

Lengths: the title is 58 characters, the meta description 159 and the H1 50.

---

## 2. Above the fold

Paste this at the top of `<main>`. It replaces the 'AI For All...' line, which is not a heading, as the first heading on the page. The page has no H1 today.

```html
<section class="pass-hero" aria-labelledby="pass-h1">
  <h1 id="pass-h1">Register for World AI Summit 2026: Delegate Passes</h1>
  <p class="pass-subline">14-15 October 2026 · Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru · from Rs PLACEHOLDER_PREMIUM_PRICE per delegate</p>

  <div class="pass-cards">
    <div class="pass-card">
      <h2>Premium Pass</h2>
      <p class="pass-price">Rs PLACEHOLDER_PREMIUM_PRICE <span>per delegate, PLACEHOLDER_GST_LINE</span></p>
      <p>Full summit access, delegate kit, lunch and refreshments, certificate of participation.</p>
      <a class="btn" href="#checkout">Book Premium Pass</a>
    </div>
    <div class="pass-card">
      <h2>VIP Pass</h2>
      <p class="pass-price">Rs PLACEHOLDER_VIP_PRICE <span>per delegate, PLACEHOLDER_GST_LINE</span></p>
      <p>All Premium benefits, plus priority seating, speaker lounge access, a government and investor roundtable invite, and the exclusive networking dinner.</p>
      <a class="btn" href="#checkout">Book VIP Pass</a>
    </div>
  </div>

  <p class="pass-group">Group of 3+? 10% off. <a href="mailto:registration@worldaisummit.com?subject=Group%20booking%20WAIS%202026">Email registration@worldaisummit.com</a></p>
</section>
```

Developer notes:
- Set `#checkout` to the id of the existing 'Checkout' section.
- PLACEHOLDER_GST_LINE is either 'inclusive of GST' or 'plus 18% GST'. Use the wording Elets confirms.

---

## 3. Price table: delete the expired rows

On /delegate/, delete these two rows completely:
- 'Early Bird Offer Limited to the First 150 Passes (Valid till 25th July 2025) ₹20,000 Save ₹5,000 / ₹35,000 Save ₹5,000'
- 'Standard Access (Valid till 30th Sept 2026) ₹20,000 / ₹35,000'

Leave one row:

```html
<table class="pass-table">
  <caption>Delegate pass prices, World AI Summit 2026</caption>
  <thead><tr><th scope="col">Pass</th><th scope="col">Price per delegate</th></tr></thead>
  <tbody>
    <tr><th scope="row">Premium Pass</th><td>Rs PLACEHOLDER_PREMIUM_PRICE (PLACEHOLDER_GST_LINE)</td></tr>
    <tr><th scope="row">VIP Pass</th><td>Rs PLACEHOLDER_VIP_PRICE (PLACEHOLDER_GST_LINE)</td></tr>
  </tbody>
</table>
<p>Booking for 3 or more delegates from one organisation? You get 10% off. Write to <a href="mailto:registration@worldaisummit.com?subject=Group%20booking%20WAIS%202026">registration@worldaisummit.com</a>.</p>
```

Use one set of pass names across the site: **Premium Pass** and **VIP Pass**.
- Remove the duplicate 'General Delegate' and 'VIP Delegate' cards. Their benefits are merged into the table in section 4.
- The homepage also shows a third tier with 'Access to event photos & videos'. Elets needs to decide on it (PLACEHOLDER_THIRD_TIER_DECISION):
  - either remove it from the homepage,
  - or name it, price it and add it here and to the JSON-LD.

---

## 4. Below the fold: what's included

Every benefit in this table appears on the live /delegate/ page as of 1 Oct 2026.

```html
<section aria-labelledby="included-h2">
  <h2 id="included-h2">What's included</h2>
  <table class="compare">
    <thead><tr><th scope="col">Benefit</th><th scope="col">Premium Pass</th><th scope="col">VIP Pass</th></tr></thead>
    <tbody>
      <tr><th scope="row">Full summit access, 14-15 October</th><td>Yes</td><td>Yes</td></tr>
      <tr><th scope="row">Delegate kit, lunch and refreshments</th><td>Yes</td><td>Yes</td></tr>
      <tr><th scope="row">Certificate of participation</th><td>Yes</td><td>Yes</td></tr>
      <tr><th scope="row">Access to AI policy roundtables</th><td>PLACEHOLDER_POLICY_ROUNDTABLE</td><td>Yes</td></tr>
      <tr><th scope="row">Priority seating</th><td>No</td><td>Yes</td></tr>
      <tr><th scope="row">Speaker lounge access</th><td>No</td><td>Yes</td></tr>
      <tr><th scope="row">Government and investor roundtable invite</th><td>No</td><td>Yes</td></tr>
      <tr><th scope="row">Exclusive networking dinner</th><td>No</td><td>Yes</td></tr>
      <tr><th scope="row">Special sessions: GenAI, Agentic AI and AI Safety</th><td>No</td><td>Yes</td></tr>
    </tbody>
  </table>
  <p><a class="btn" href="#checkout">Book your pass</a></p>
</section>
```

PLACEHOLDER_POLICY_ROUNDTABLE: today the live page lists 'Access to AI Policy Roundtables' under 'General Delegate' but not under 'Premium Pass'. Enter Yes or No.

---

## 5. Who you will hear

All eight speakers are marked confirmed_2026 in `worldaisummit/speakers/speakers.json`, and each one has a live page at /assets/speaker_details/. Before publishing, confirm with the programme team that all eight are still on the programme (PLACEHOLDER_SPEAKERS_CONFIRM). The strip shows name, role and organisation only, with no bios.

```html
<section aria-labelledby="speakers-h2">
  <h2 id="speakers-h2">Who you will hear</h2>
  <ul class="speaker-strip">
    <li><a href="/assets/speaker_details/sanjeev-gupta.html">Sanjeev Gupta</a>, Chief Executive Officer, Karnataka Digital Economy Mission</li>
    <li><a href="/assets/speaker_details/ram-mohan-rao.html">Ram Mohan Rao</a>, Executive Director, Securities and Exchange Board of India (SEBI)</li>
    <li><a href="/assets/speaker_details/anand-thakur.html">Anand Thakur</a>, Chief Product and Technology Officer, Reliance Retail</li>
    <li><a href="/assets/speaker_details/pranav-saxena.html">Pranav Saxena</a>, Chief Product and Technology Officer, API Holdings</li>
    <li><a href="/assets/speaker_details/deepika-sandeep.html">Deepika Sandeep</a>, Head - AI/ML CoE, HSBC</li>
    <li><a href="/assets/speaker_details/kuldeep-t.html">Kuldeep T</a>, CISO &amp; DPO, BigBasket</li>
    <li><a href="/assets/speaker_details/rajesh-choudhary.html">Rajesh Choudhary</a>, Chief Information Officer, CSB Bank</li>
    <li><a href="/assets/speaker_details/suman-dash.html">Suman Dash</a>, Chief Operating Officer, Acsel Technology Forum</li>
  </ul>
  <p><a href="/speaker.html">See all speakers</a></p>
</section>
```

---

## 6. Programme and venue

```html
<section aria-labelledby="programme-h2">
  <h2 id="programme-h2">Programme and venue</h2>
  <p>Seven tracks over two days: Frontier Models &amp; Compute; Sovereign AI &amp; Geopolitics; Enterprise AI in Production; GCCs; Robotics, Agents &amp; Embodied AI; AI for Bharat; Capital, Founders &amp; Exits. <a href="/ai-conference-bengaluru-2026.html">Read the full programme overview</a>.</p>
  <h3>Venue</h3>
  <address>Sheraton Grand Bangalore Hotel at Brigade Gateway<br>26/1 Dr. Rajkumar Road, Malleswaram-Rajajinagar<br>Bengaluru, Karnataka 560055</address>
</section>
```

The street address comes from the hotel's official Marriott page: https://www.marriott.com/en-us/hotels/blrgs-sheraton-grand-bangalore-hotel-at-brigade-gateway/rooms/

---

## 7. FAQ

The answers on lunch, the certificate, the group discount, the dates and the venue are already verified. The registration team must supply the rest.

```html
<section aria-labelledby="faq-h2">
  <h2 id="faq-h2">Delegate pass FAQ</h2>
  <details><summary>When and where is World AI Summit 2026?</summary><p>14-15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, 26/1 Dr. Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru 560055.</p></details>
  <details><summary>Is GST included in the pass price?</summary><p>PLACEHOLDER_GST_ANSWER</p></details>
  <details><summary>Will I receive a GST invoice?</summary><p>PLACEHOLDER_GST_INVOICE_ANSWER</p></details>
  <details><summary>Is lunch included?</summary><p>Yes. Every pass includes the delegate kit, lunch and refreshments.</p></details>
  <details><summary>Do delegates receive a certificate?</summary><p>Yes. Every pass includes a certificate of participation.</p></details>
  <details><summary>Is there a group discount?</summary><p>Yes. Organisations booking 3 or more delegates get 10% off. Write to registration@worldaisummit.com with the names and the pass type.</p></details>
  <details><summary>Can I transfer my pass to a colleague?</summary><p>PLACEHOLDER_TRANSFER_POLICY</p></details>
  <details><summary>What is the cancellation and refund policy?</summary><p>PLACEHOLDER_REFUND_POLICY</p></details>
  <details><summary>Can I register at the venue on the day?</summary><p>PLACEHOLDER_ONSPOT_ANSWER</p></details>
  <details><summary>Who do I contact about registration?</summary><p>registration@worldaisummit.com. For sponsorship and exhibition, partnerships@worldaisummit.com. For speaking, secretariat@worldaisummit.com.</p></details>
</section>
```

Do not add FAQPage schema. Google shows FAQ rich results only for government and health sites, so the markup would not earn one here.

---

## 8. Event JSON-LD

Paste this just before `</head>` on /delegate/. JSON syntax is checked. Replace the price placeholders with digits only.
- If the homepage already has Event schema, give it the same `@id` so Google sees one event, not two.
- If there is no event image, delete the `image` line.
- Once passes are close to selling out, change `availability` to `https://schema.org/LimitedAvailability`, and to `https://schema.org/SoldOut` when they have.
- The `performer` list contains only the eight speakers from section 5. Remove any speaker who drops out.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Event",
  "@id": "https://www.worldaisummit.com/#event",
  "name": "World AI Summit 2026",
  "description": "Two-day AI conference in Bengaluru organised by Elets Technomedia, with seven tracks: Frontier Models & Compute; Sovereign AI & Geopolitics; Enterprise AI in Production; GCCs; Robotics, Agents & Embodied AI; AI for Bharat; Capital, Founders & Exits.",
  "url": "https://www.worldaisummit.com/",
  "image": ["https://www.worldaisummit.com/PLACEHOLDER_EVENT_IMAGE_PATH"],
  "inLanguage": "en-IN",
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
  "organizer": {
    "@type": "Organization",
    "name": "Elets Technomedia",
    "url": "https://eletsonline.com/",
    "email": "registration@worldaisummit.com"
  },
  "performer": [
    {"@type": "Person", "name": "Sanjeev Gupta", "jobTitle": "Chief Executive Officer", "worksFor": {"@type": "Organization", "name": "Karnataka Digital Economy Mission"}, "url": "https://www.worldaisummit.com/assets/speaker_details/sanjeev-gupta.html"},
    {"@type": "Person", "name": "Ram Mohan Rao", "jobTitle": "Executive Director", "worksFor": {"@type": "Organization", "name": "Securities and Exchange Board of India (SEBI)"}, "url": "https://www.worldaisummit.com/assets/speaker_details/ram-mohan-rao.html"},
    {"@type": "Person", "name": "Anand Thakur", "jobTitle": "Chief Product and Technology Officer", "worksFor": {"@type": "Organization", "name": "Reliance Retail"}, "url": "https://www.worldaisummit.com/assets/speaker_details/anand-thakur.html"},
    {"@type": "Person", "name": "Pranav Saxena", "jobTitle": "Chief Product and Technology Officer", "worksFor": {"@type": "Organization", "name": "API Holdings"}, "url": "https://www.worldaisummit.com/assets/speaker_details/pranav-saxena.html"},
    {"@type": "Person", "name": "Deepika Sandeep", "jobTitle": "Head - AI/ML CoE", "worksFor": {"@type": "Organization", "name": "HSBC"}, "url": "https://www.worldaisummit.com/assets/speaker_details/deepika-sandeep.html"},
    {"@type": "Person", "name": "Kuldeep T", "jobTitle": "CISO & DPO", "worksFor": {"@type": "Organization", "name": "BigBasket"}, "url": "https://www.worldaisummit.com/assets/speaker_details/kuldeep-t.html"},
    {"@type": "Person", "name": "Rajesh Choudhary", "jobTitle": "Chief Information Officer", "worksFor": {"@type": "Organization", "name": "CSB Bank"}, "url": "https://www.worldaisummit.com/assets/speaker_details/rajesh-choudhary.html"},
    {"@type": "Person", "name": "Suman Dash", "jobTitle": "Chief Operating Officer", "worksFor": {"@type": "Organization", "name": "Acsel Technology Forum"}, "url": "https://www.worldaisummit.com/assets/speaker_details/suman-dash.html"}
  ],
  "offers": [
    {"@type": "Offer", "name": "Premium Pass", "url": "https://www.worldaisummit.com/delegate/", "price": "PLACEHOLDER_PREMIUM_PRICE_INR", "priceCurrency": "INR", "availability": "https://schema.org/InStock"},
    {"@type": "Offer", "name": "VIP Pass", "url": "https://www.worldaisummit.com/delegate/", "price": "PLACEHOLDER_VIP_PRICE_INR", "priceCurrency": "INR", "availability": "https://schema.org/InStock"}
  ]
}
</script>
```

---

## 9. Redirects: one 301 hop to /delegate/

Today /registration takes 3 hops and /registration.html takes 2 (to non-www /, then to www /). The status codes were not checked, so do not assume they are 302s. The rules below send each old URL to https://www.worldaisummit.com/delegate/ in a single 301, from both http and https and from both www and non-www. Query strings such as UTM tags are kept.

The URLs covered are:
- /registration and /registration.html
- /1st-edition/delegate-pass.html, a 2025 archive page that shows Rs 30,000 / 60,000 under a '2025' title
- /delegate-pass at the site root, which the WebSearch index shows as 'World AI Summit 2025' with a '2025 Tickets' table: Rs 20,000/35,000, Rs 25,000/50,000 and Rs 30,000/60,000. Its live status is not verified. The rule is harmless if the URL already returns 404.

### Apache (.htaccess in the web root)

Put this block above the existing http-to-https and non-www-to-www rules. Delete any existing `Redirect` or `RewriteRule` lines that send /registration or /registration.html to the homepage. If /1st-edition/ has its own .htaccess with `RewriteEngine On`, add the 1st-edition rule there as well, without the `1st-edition/` prefix.

```apache
# World AI Summit 2026: old registration and pass URLs -> /delegate/ in one 301 hop
<IfModule mod_rewrite.c>
RewriteEngine On
RewriteRule ^registration(\.html)?/?$            https://www.worldaisummit.com/delegate/ [R=301,L,NC]
RewriteRule ^1st-edition/delegate-pass\.html$    https://www.worldaisummit.com/delegate/ [R=301,L,NC]
RewriteRule ^delegate-pass(\.html)?/?$           https://www.worldaisummit.com/delegate/ [R=301,L,NC]
</IfModule>
```

### nginx

```nginx
# http {} context
map $uri $wais_to_delegate {
    default                               0;
    ~*^/registration(\.html)?/?$          1;
    ~*^/1st-edition/delegate-pass\.html$  1;
    ~*^/delegate-pass(\.html)?/?$         1;
}

# Inside EVERY server {} block that answers worldaisummit.com or www.worldaisummit.com
# (port 80 and port 443), above any other return or rewrite:
if ($wais_to_delegate) {
    return 301 https://www.worldaisummit.com/delegate/$is_args$args;
}
```

Run `nginx -t && systemctl reload nginx` after the change.

### Check after deploying

Every line should print `301 https://www.worldaisummit.com/delegate/`.

```sh
for u in http://worldaisummit.com/registration https://worldaisummit.com/registration \
         https://www.worldaisummit.com/registration https://www.worldaisummit.com/registration.html \
         https://www.worldaisummit.com/1st-edition/delegate-pass.html https://www.worldaisummit.com/delegate-pass; do
  curl -s -o /dev/null -w "%{http_code} %{redirect_url}  <- $u\n" "$u"
done
```

---

## 10. Same price everywhere else (find and replace)

Do these on the same deploy, after the pricing decision.

**Homepage, 'Secure your seat' block**
- 'Premium Pass Rs 20,000/ delegate' becomes 'Premium Pass Rs PLACEHOLDER_PREMIUM_PRICE / delegate'.
- 'Three release phases' becomes PLACEHOLDER_PRICE_PHASE_LABEL, for example 'Late Access pricing'. Only one phase is shown, so 'three phases' no longer reads correctly.
- Name the second tier 'VIP Pass Rs PLACEHOLDER_VIP_PRICE / delegate'.
- Remove, or name and price, the third tier with 'Access to event photos & videos' (PLACEHOLDER_THIRD_TIER_DECISION).
- Point every button in the block to https://www.worldaisummit.com/delegate/.

**/ai-conference-bengaluru-2026.html, 'Register' block**

Today this block holds only a 'Late Access' heading. Replace it with:

```html
<h3>Delegate passes</h3>
<p>Premium Pass Rs PLACEHOLDER_PREMIUM_PRICE · VIP Pass Rs PLACEHOLDER_VIP_PRICE per delegate (PLACEHOLDER_GST_LINE). 10% off for groups of 3 or more.</p>
<p><a class="btn" href="https://www.worldaisummit.com/delegate/">Book your delegate pass</a></p>
```

Also confirm that the FAQ link 'Get Your Delegate Pass ->' points to https://www.worldaisummit.com/delegate/.

**Speaker pages, /assets/speaker_details/*.html**
- The body text on about 51 pages says 'Delegate passes from Rs 20,000'.
- 10 meta descriptions carry the price:
  - 8 say 'Passes from Rs 20,000': anand-thakur, deepika-sandeep, ganesh-joshi, kuldeep-t, pranav-saxena, praveen-bist, ram-mohan-rao and suman-dash.
  - 2 say 'Delegate passes from Rs 20,000': rajesh-choudhary and sushan-rungta.

Run these commands in the site source:

```sh
grep -rln "Rs 20,000\|₹20,000\|Rs 35,000\|₹35,000" .            # list every file that still shows an old price
sed -i -E 's/([Pp]asses from) Rs 20,000/\1 Rs PLACEHOLDER_PREMIUM_PRICE/g' assets/speaker_details/*.html
grep -rn "from Rs 20,000" assets/speaker_details/ || echo "speaker pages clean"
```

**Local generator (not deployed yet)**

In `worldaisummit/speakers/speakers.json`, set `site.pass_from` to "Rs PLACEHOLDER_PREMIUM_PRICE" and `site.pass_price_inr` to PLACEHOLDER_PREMIUM_PRICE_INR before the next `python3 build_speakers.py --clean`.

**Sitemap**
- Remove /registration, /registration.html, /1st-edition/delegate-pass.html and /delegate-pass if they are listed.
- Keep /delegate/ and set its `<lastmod>` to the deploy date.

**Internal links**
- Point the main navigation 'Register' item and the homepage CTA to /delegate/. Today /delegate/ may be reachable only from the sitemap; this is not confirmed.

**Off-site pages controlled by Elets or its partners**
- elets.net/worldaisummit-delegate/ shows 'Standard Access (Valid till 14th Sep 2025) Rs 25,000 / 50,000'. Update its price table, or 301 it to https://www.worldaisummit.com/delegate/.
- Ask allevents.in, the official ticketing partner, to change 'Tickets on approval from Rs 20,000' and 'Delegates Passes INR 20,000 Available' to the confirmed price.
