# A10: /partner-with-us.html: head tags, JSON-LD, page copy with an enquiry form, the 301 from /partnership.html (Apache and nginx), and a link checklist

- **For recommendation:** Make /partner-with-us.html able to rank and convert: point its canonical at itself, give it its own title, show sponsor packages and a lead form, and merge /partnership.html into it
- **Research lens:** site-deep-read
- **Format:** HTML snippets (head, JSON-LD, body) + Apache .htaccess and nginx config + plain-text checklist
- **Placeholders the business must fill:**
  - PLACEHOLDER_AUDIENCE_FIGURE (pick one figure: 1,000+ or 1,200+; it must match the AI-conference page and the blog)
  - PLACEHOLDER_SPONSOR_DECK_URL (or delete the deck button)
  - PLACEHOLDER_BOOTHS_LEFT
  - PLACEHOLDER_SPEAKING_SLOTS_LEFT
  - PLACEHOLDER_ROUNDTABLE_SEATS_LEFT
  - PLACEHOLDER_REPORT_FEATURES_LEFT
  - PLACEHOLDER_REPORT_DEADLINE
  - PLACEHOLDER_PARTNER_BOOKING_DEADLINE
  - PLACEHOLDER_FORM_ENDPOINT (or remove the form)
  - PLACEHOLDER_REPLY_TIME
  - PLACEHOLDER_PARTNERSHIPS_CONTACT_NAME
  - PLACEHOLDER_PHONE_E164 / PLACEHOLDER_PHONE_DISPLAY
  - PLACEHOLDER_WHATSAPP_DIGITS
  - PLACEHOLDER_EVENT_IMAGE_URL (og:image and Event image)
  - PLACEHOLDER_CURRENT_PASS_PRICE (number only, INR, for Event offers)
  - PLACEHOLDER_2025_ARCHIVE_DECISION (301 the /1st-edition/partnership.html and /1st-edition/partner-benefits.html pages, or keep them with a 2025 banner and remove them from the sitemap)
  - PLACEHOLDER_SIBLING_LINK_DECISION (cross-link from the indiaaisummit.in partner section)

## How to ship

Owners: web dev and the partnerships team. Deadline: 3 Oct 2026.

1. Partnerships fills in the placeholders:
   - one audience figure;
   - booths, slots and seats left, and the booking deadline;
   - the report deadline;
   - the named contact with phone and WhatsApp;
   - the reply time;
   - the deck URL (or delete the deck button);
   - the current delegate pass price for the JSON-LD;
   - two decisions: the 2025 archive pages, and the indiaaisummit.in cross-link.
2. Web dev in /partner-with-us.html:
   - replace the head tags (section 1);
   - delete the old canonical so only one remains;
   - paste the JSON-LD (section 2);
   - replace the body with section 3, inside the existing layout;
   - wire the form to a real endpoint, or remove the form and keep the mailto and phone lines.
   Validate with the Rich Results Test and the Schema Markup Validator.
3. Add the 301 using the Apache or nginx block in section 4. I could not confirm which server the site runs on, because the site was blocked from this environment. If it is on a static host, use that host's redirect file with the same source and target. Then run the three curl tests.
4. Make the link, sitemap and figure edits in section 5. Confirm the existing "Partner with us" and "Partner With Us ->" links point to /partner-with-us.html.
5. Add the www Search Console property and request indexing.
6. Report results as partnership enquiries, not ranking changes: the page already ranks #7 and the homepage #1 for "world ai summit sponsorship".

Do not ship until every PLACEHOLDER_ is gone; grep the page for PLACEHOLDER_ before uploading.

On the relayed question about CPUs: this sandbox reports 4 CPUs (nproc), and a subagent cannot add more.

## Content

=====================================================================
0. CHANGES MADE TO THE ORIGINAL RECOMMENDATION (verifier corrections)
=====================================================================
- Expected result: this is a tidy-up and a conversion fix. It does not unlock a ranking. /partner-with-us.html already ranks #7 on Google India for "world ai summit sponsorship" (Google rewrote its title to "World AI Summit Partner Benefits"). The homepage ranks #1 for the same query. Google is ignoring the current canonical-to-homepage hint.
- Meta description: changed "GCC and government AI leaders" to "policymakers and AI investors". The homepage "Who Should Attend" list has no "GCC leaders" group. GCCs is a track, not an audience group. Still 159 characters.
- "Who you will meet" now repeats the homepage list word for word (9 groups). The 7 tracks are listed separately.
- The "Past partners" section was split in two:
  - the homepage logo strip keeps its own label, "Our past global AI network";
  - the quotes go under "What past participants said".
  The Pinnacle quote is left out because it describes Pinnacle's own product, not the summit.
- Audience figure: the live pages disagree (1200+ on this page, 1,000+ on the AI-conference page), so it is now a PLACEHOLDER. Use one figure on every page.
- Added an optional rule for the two indexable 2025 pages in the sitemap: /1st-edition/partnership.html and /1st-edition/partner-benefits.html.
- Venue street address checked by web search (hotelplanner.com and ixigo.com hotel listings): 26/1 Dr. Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru 560055.

=====================================================================
1. <head> — replace the current title, meta description and canonical
   (the canonical currently points to https://www.worldaisummit.com/;
   the page must end up with exactly ONE canonical tag)
=====================================================================
<title>Sponsor or Exhibit at World AI Summit 2026 | Bengaluru</title>
<meta name="description" content="Sponsorship, exhibition booths, speaking slots and 1:1 meetings at World AI Summit 2026, 14-15 Oct, Bengaluru. Reach CIOs, CTOs, policymakers and AI investors.">
<link rel="canonical" href="https://www.worldaisummit.com/partner-with-us.html">
<meta name="robots" content="index, follow">
<meta property="og:type" content="website">
<meta property="og:url" content="https://www.worldaisummit.com/partner-with-us.html">
<meta property="og:title" content="Sponsor or Exhibit at World AI Summit 2026 | Bengaluru">
<meta property="og:description" content="Sponsorship, exhibition booths, speaking slots and 1:1 meetings at World AI Summit 2026, 14-15 Oct, Bengaluru. Reach CIOs, CTOs, policymakers and AI investors.">
<meta property="og:image" content="PLACEHOLDER_EVENT_IMAGE_URL">

Lengths: title 54, meta 159, H1 49.

=====================================================================
2. JSON-LD — paste into <head>. This is valid JSON; it was parsed to check.
   If the homepage already has Event markup, use the same @id
   (https://www.worldaisummit.com/#event) and the same values there.
   No "performer" is included because this page names no speakers.
   Add performers only on pages that show confirmed 2026 speakers.
=====================================================================
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://www.worldaisummit.com/partner-with-us.html#webpage",
      "url": "https://www.worldaisummit.com/partner-with-us.html",
      "name": "Sponsor or Exhibit at World AI Summit 2026 | Bengaluru",
      "description": "Sponsorship, exhibition booths, speaking slots and 1:1 meetings at World AI Summit 2026, 14-15 Oct, Bengaluru. Reach CIOs, CTOs, policymakers and AI investors.",
      "inLanguage": "en-IN",
      "isPartOf": { "@type": "WebSite", "@id": "https://www.worldaisummit.com/#website", "url": "https://www.worldaisummit.com/", "name": "World AI Summit" },
      "about": { "@id": "https://www.worldaisummit.com/#event" },
      "publisher": { "@id": "https://www.worldaisummit.com/#organizer" }
    },
    {
      "@type": "Event",
      "@id": "https://www.worldaisummit.com/#event",
      "name": "World AI Summit 2026",
      "description": "World AI Summit 2026 brings together policymakers, technology leaders, enterprises, startups, investors and researchers in Bengaluru across seven tracks: Frontier Models & Compute; Sovereign AI & Geopolitics; Enterprise AI in Production; Global Capability Centres (GCCs); Robotics, Agents & Embodied AI; AI for Bharat; Capital, Founders & Exits.",
      "url": "https://www.worldaisummit.com/",
      "image": ["PLACEHOLDER_EVENT_IMAGE_URL"],
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
        "@id": "https://www.worldaisummit.com/#organizer",
        "name": "Elets Technomedia",
        "url": "https://www.eletsonline.com/",
        "email": "partnerships@worldaisummit.com"
      },
      "offers": {
        "@type": "Offer",
        "url": "https://www.worldaisummit.com/delegate/",
        "price": "PLACEHOLDER_CURRENT_PASS_PRICE",
        "priceCurrency": "INR",
        "availability": "https://schema.org/InStock"
      }
    }
  ]
}
</script>
(For "price", enter the number only, e.g. 20000, with no currency sign or commas.)

=====================================================================
3. <body> content — replaces the current 219-word body.
   - Wrap it in the site's existing header, footer and CSS; the class names are suggestions.
   - Headings go H1 > H2 > H3 in order, which fixes the audit's heading-order-skip.
=====================================================================
<main id="partner-with-us">

<section class="partner-hero">
  <h1>Sponsor, Exhibit or Speak at World AI Summit 2026</h1>
  <p>World AI Summit 2026 takes place on 14-15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. Organised by Elets Technomedia, it brings together PLACEHOLDER_AUDIENCE_FIGURE policymakers, enterprise technology leaders, startups, investors and researchers across seven tracks.</p>
  <p>Partners can sponsor, exhibit, take a centre-stage speaking slot, meet decision-makers one-on-one or be featured in the AI Innovation Report. Partnership packages are customised to your business objectives.</p>
  <p>
    <a class="btn btn-primary" href="#enquire">Send a partnership enquiry</a>
    <a class="btn btn-secondary" href="PLACEHOLDER_SPONSOR_DECK_URL">Download the sponsorship deck (PDF)</a>
  </p>
  <!-- If there is no deck to publish, delete the second button. -->
</section>

<section id="audience">
  <h2>Who you will meet</h2>
  <p>The summit is designed for:</p>
  <ul>
    <li>Government Officials &amp; Policymakers</li>
    <li>AI Startups &amp; Entrepreneurs</li>
    <li>Startup Founders &amp; Innovators</li>
    <li>International Organizations &amp; Think Tanks</li>
    <li>Academia &amp; Researchers</li>
    <li>Investors &amp; Venture Capitalists</li>
    <li>AI &amp; Data Science Leaders</li>
    <li>CIOs / CTOs / CDOs</li>
    <li>Technology Vendors</li>
  </ul>

  <h3>Seven tracks</h3>
  <ul>
    <li>Frontier Models &amp; Compute</li>
    <li>Sovereign AI &amp; Geopolitics</li>
    <li>Enterprise AI in Production</li>
    <li>Global Capability Centres (GCCs)</li>
    <li>Robotics, Agents &amp; Embodied AI</li>
    <li>AI for Bharat</li>
    <li>Capital, Founders &amp; Exits</li>
  </ul>
  <p>Tell us which track matters most to your buyers, and the partnerships team will suggest the format that fits.</p>
</section>

<section id="formats">
  <h2>Five ways to partner</h2>

  <h3>1. Sponsorship</h3>
  <p>Build visibility with AI leaders, policymakers and enterprise buyers across both days of the summit. Packages are tailored to your objectives.</p>

  <h3>2. Exhibit</h3>
  <p>Show your products and solutions on the expo floor and meet AI leaders and innovators in person.</p>

  <h3>3. Centre-stage speaking slot</h3>
  <p>Share your AI leadership through keynotes, panels and power talks. The organising team reviews speaking proposals for relevance, expertise and fit with the summit theme.</p>

  <h3>4. One-on-one meetings and executive roundtables</h3>
  <p>Meet decision-makers through one-on-one meetings and curated executive roundtables.</p>

  <h3>5. Feature in the AI Innovation Report</h3>
  <p>Present your AI work in the AI Innovation Report, which will be launched at the summit.</p>
</section>

<section id="availability">
  <h2>Still available for 14-15 October</h2>
  <ul>
    <li>Exhibition booths: PLACEHOLDER_BOOTHS_LEFT</li>
    <li>Centre-stage speaking slots: PLACEHOLDER_SPEAKING_SLOTS_LEFT</li>
    <li>Executive roundtable seats: PLACEHOLDER_ROUNDTABLE_SEATS_LEFT</li>
    <li>AI Innovation Report features: PLACEHOLDER_REPORT_FEATURES_LEFT (content deadline PLACEHOLDER_REPORT_DEADLINE)</li>
  </ul>
  <p>Partner bookings close on PLACEHOLDER_PARTNER_BOOKING_DEADLINE.</p>
  <!-- If the team does not want to publish counts, delete the list and keep only:
       "A limited number of booths and slots remain. Write to partnerships@worldaisummit.com for current availability." -->
</section>

<section id="network">
  <h2>Our past global AI network</h2>
  <!-- Copy the homepage "Our Past Global AI Network" logo strip here unchanged and keep this label.
       Do not relabel it "Past sponsors" or "Past partners" unless the partnerships team confirms each logo. -->
  <p>Strategic partner, 2025 edition: Karnataka Digital Economy Mission (KDEM), Department of Electronics, IT and BT, Government of Karnataka.</p>
</section>

<section id="testimonials">
  <h2>What past participants said</h2>
  <!-- Quoted word for word from the homepage (read 1 Oct 2026). The Pinnacle quote is left out because it is about Pinnacle's product, not the summit. -->
  <blockquote>
    <p>“Among the three events we participated in this year, this was by far the most productive. The pre-event CEO dinner was a game-changer, allowing us to connect meaningfully with key stakeholders ahead of time.”</p>
    <footer>Ratan Kumar Kesh, ED &amp; COO, Bandhan Bank</footer>
  </blockquote>
  <blockquote>
    <p>“Bengaluru and Karnataka have firmly established themselves as global leaders in the FinTech space. The summit showcased this strength brilliantly, reinforcing how this region is not just building for India, but for the world. We’re proud to be a small part of this powerful journey, and look forward to contributing to its continued growth.”</p>
    <footer>Harshil Mathur, CEO, Co-Founder, Razorpay</footer>
  </blockquote>
  <blockquote>
    <p>“The panel discussions were spot-on — relevant topics, strong viewpoints, and valuable regulatory insights.”</p>
    <footer>Pramod Ganji, CEO, Zrika</footer>
  </blockquote>
</section>

<section id="enquire">
  <h2>Send a partnership enquiry</h2>
  <p>Tell us what you would like to do at the summit. The partnerships team replies within PLACEHOLDER_REPLY_TIME.</p>
  <!-- Static site: the form needs an endpoint (CRM form, form service or a server script).
       If there is no endpoint by 3 Oct, delete the <form> and ship the mailto and phone lines only. Do not ship a form that goes nowhere. -->
  <form action="PLACEHOLDER_FORM_ENDPOINT" method="post">
    <input type="hidden" name="source" value="partner-with-us">
    <p><label for="pw-name">Name</label><br><input id="pw-name" name="name" type="text" autocomplete="name" required></p>
    <p><label for="pw-company">Company</label><br><input id="pw-company" name="company" type="text" autocomplete="organization" required></p>
    <p><label for="pw-role">Role</label><br><input id="pw-role" name="role" type="text" autocomplete="organization-title" required></p>
    <p><label for="pw-email">Work email</label><br><input id="pw-email" name="email" type="email" autocomplete="email" required></p>
    <p><label for="pw-phone">Phone</label><br><input id="pw-phone" name="phone" type="tel" autocomplete="tel" required></p>
    <p><label for="pw-interest">I am interested in</label><br>
      <select id="pw-interest" name="interest" required>
        <option value="">Select one</option>
        <option>Sponsorship</option>
        <option>Exhibition booth</option>
        <option>Centre-stage speaking slot</option>
        <option>One-on-one meetings and executive roundtables</option>
        <option>Feature in the AI Innovation Report</option>
        <option>Not sure yet</option>
      </select></p>
    <p><label for="pw-message">Anything else (optional)</label><br><textarea id="pw-message" name="message" rows="4"></textarea></p>
    <p><button type="submit">Send enquiry</button></p>
    <p class="small">We use these details only to respond to your enquiry.</p>
  </form>
  <p>Prefer email? <a href="mailto:partnerships@worldaisummit.com?subject=Sponsorship%20enquiry%20-%20WAIS%202026&amp;body=Name%3A%0ACompany%3A%0ARole%3A%0APhone%3A%0AInterest%20%28sponsorship%20/%20exhibition%20/%20speaking%20/%201%3A1%20meetings%20/%20AI%20Innovation%20Report%29%3A%0A">Write to partnerships@worldaisummit.com</a></p>
  <p>To speak to someone, call or WhatsApp PLACEHOLDER_PARTNERSHIPS_CONTACT_NAME on <a href="tel:PLACEHOLDER_PHONE_E164">PLACEHOLDER_PHONE_DISPLAY</a> (<a href="https://wa.me/PLACEHOLDER_WHATSAPP_DIGITS">WhatsApp</a>).</p>
</section>

<section id="other-contacts">
  <h2>Other enquiries</h2>
  <ul>
    <li>Speaking and collaboration: <a href="mailto:secretariat@worldaisummit.com">secretariat@worldaisummit.com</a></li>
    <li>Delegate passes: <a href="https://www.worldaisummit.com/delegate/">view passes</a> or write to <a href="mailto:registration@worldaisummit.com">registration@worldaisummit.com</a> (3 or more delegates get 10% off)</li>
  </ul>
</section>

</main>

=====================================================================
4. REDIRECT: /partnership.html -> 301 -> /partner-with-us.html
   (/partnership.html has 64 words, no H1 and a canonical to /.)
   The redirect points straight at the final https://www URL so that it is a single hop.
   The crawl found 2 redirect chains elsewhere (e.g. /registration goes through non-www in 3 hops).
=====================================================================
--- Apache (.htaccess in the web root) ---
--- Place these lines ABOVE any existing http->https or non-www->www rules. ---
RewriteEngine On
RewriteRule ^partnership\.html$ https://www.worldaisummit.com/partner-with-us.html [R=301,L,NC]

# OPTIONAL, decide with PLACEHOLDER_2025_ARCHIVE_DECISION: retire the 2025 partner pages
# (both are indexable, in the sitemap and titled "World AI Summit 2025")
# RewriteRule ^1st-edition/(partnership|partner-benefits)\.html$ https://www.worldaisummit.com/partner-with-us.html [R=301,L,NC]

# If mod_rewrite is not enabled, use mod_alias instead:
# RedirectMatch 301 ^/partnership\.html$ https://www.worldaisummit.com/partner-with-us.html

--- nginx (inside every server block that serves the site: https www, plus the
--- http and non-www blocks unless they already send everything to https://www first) ---
location = /partnership.html {
    return 301 https://www.worldaisummit.com/partner-with-us.html$is_args$args;
}

# OPTIONAL (PLACEHOLDER_2025_ARCHIVE_DECISION):
# location ~* ^/1st-edition/(partnership|partner-benefits)\.html$ {
#     return 301 https://www.worldaisummit.com/partner-with-us.html$is_args$args;
# }

# Then run: sudo nginx -t && sudo systemctl reload nginx

--- Test after deploy ---
curl -sI https://www.worldaisummit.com/partnership.html
  expect: 301 and "Location: https://www.worldaisummit.com/partner-with-us.html"
curl -sIL http://worldaisummit.com/partnership.html | grep -iE "^(HTTP|location)"
  expect: no more than 2 hops, ending in 200 at the https://www partner page
curl -s https://www.worldaisummit.com/partner-with-us.html | grep -i 'rel="canonical"'
  expect: exactly one line, with href="https://www.worldaisummit.com/partner-with-us.html"

If you choose Option B for the 2025 pages instead of the 301:
- keep them live;
- add a line at the top: "This page is from the 2025 edition. For 2026 partnership options, see Partner with us", linking to /partner-with-us.html;
- remove both pages from sitemap.xml.

=====================================================================
5. INTERNAL LINKS, SITEMAP AND COPY CONSISTENCY
=====================================================================
[ ] Homepage FAQ "Are exhibition and sponsorship opportunities available?"
    Add this at the end of the answer: <a href="/partner-with-us.html">See partner options and send an enquiry</a>
[ ] Homepage FAQ "How can I become a speaker or partner?"
    It says people can "submit their interest through the official website", but no form exists yet.
    Link that phrase to /partner-with-us.html#enquire.
[ ] Homepage contact block "For Partnerships, Sponsorship & Exhibition Opportunities"
    Make the heading a link to /partner-with-us.html and keep the email address.
[ ] Homepage hero or nav: Google's homepage snippet shows a "Partner with us" element.
    Confirm its href is /partner-with-us.html and not /partnership.html. Not verified from here, because the site was blocked from this environment.
[ ] AI-conference page FAQ "Are sponsorship and exhibition opportunities available?" already ends with "Partner With Us ->".
    Confirm the href is /partner-with-us.html. Not verified.
[ ] Footer on every page: add "Partner with us" linking to /partner-with-us.html.
[ ] Search all HTML for href="/partnership.html" or "partnership.html" and point them to /partner-with-us.html.
[ ] sitemap.xml: remove /partnership.html. Set <lastmod> for /partner-with-us.html to the deploy date.
[ ] Audience figure: use PLACEHOLDER_AUDIENCE_FIGURE everywhere. Places to change:
    - "1200+" on this page (currently twice);
    - "1,000+ Delegates" (twice) on /ai-conference-bengaluru-2026.html;
    - "1,200+ delegates" in the blog post (not yet checked).

=====================================================================
6. MEASUREMENT
=====================================================================
Baseline (Google India, organic, 1 Oct 2026):
- "world ai summit sponsorship": homepage #1, /partner-with-us.html #7.
- "ai summit 2026 sponsorship india": worldaisummit.com is not in the top 10. indiaaisummit.in is #2.
- Search volume for both queries is unknown.

Search Console only has the non-www URL-prefix property, so it shows no data for www pages (it returned 0 rows for the partner pages).
- Add https://www.worldaisummit.com/ as a URL-prefix property, or add a Domain property.
- After deploy, use URL Inspection on /partner-with-us.html and click Request indexing.

The measure of success is partnership enquiries (form submissions plus mailto, phone and WhatsApp contacts logged by the partnerships team). Do not expect ranking gains within 2 weeks.

Optional, decide with PLACEHOLDER_SIBLING_LINK_DECISION: indiaaisummit.in is also an Elets site and ranks #2 for "ai summit 2026 sponsorship india". Its partner section could carry one line, "Next: World AI Summit 2026, 14-15 October, Bengaluru", linking to https://www.worldaisummit.com/partner-with-us.html.

Sources: live page text read with Exa web_fetch on 1 Oct 2026 (/, /partner-with-us.html, /ai-conference-bengaluru-2026.html); venue address from https://www.hotelplanner.com/Hotels/178731/Reservations-Sheraton-Bangalore-Hotel-at-Brigade-Gateway-Bangalore-26-1-Dr-Rajkumar-Rd-Malleswaram-Rajajinagar-560055 and https://www.ixigo.com/hotels/sheraton-grand-bangalore-hotel-at-brigade-in-bengaluru-1141860-d.
