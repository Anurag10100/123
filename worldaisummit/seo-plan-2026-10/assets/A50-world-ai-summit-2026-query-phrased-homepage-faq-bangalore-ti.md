# A50: World AI Summit 2026: query-phrased homepage FAQ, Bangalore title and H1 on the landing page, Event JSON-LD, registration redirects

- **For recommendation:** Copy Cypher's query-phrased FAQ and 'Bangalore' spelling on the homepage and the AI Conference landing page
- **Research lens:** competitors
- **Format:** Markdown runbook with ready-to-paste HTML, JSON-LD (validated with json.loads), Apache .htaccess and nginx blocks
- **Placeholders the business must fill:**
  - PLACEHOLDER_PREMIUM_PRICE (visible text, e.g. 30,000; /delegate/ shows Late Access Rs 30,000, homepage shows Rs 20,000)
  - PLACEHOLDER_VIP_PRICE (visible text; /delegate/ shows Late Access Rs 60,000)
  - PLACEHOLDER_PREMIUM_PRICE_DIGITS (JSON-LD, digits only)
  - PLACEHOLDER_VIP_PRICE_DIGITS (JSON-LD, digits only)
  - PLACEHOLDER_GST_TREATMENT ('inclusive of GST' or 'plus GST')
  - PLACEHOLDER_CORPORATE_TIERS (one sentence on other corporate tiers, or delete)
  - PLACEHOLDER_AWARDS_DEADLINE (optional awards question stays commented out unless nominations are open and the deadline is confirmed)

## How to ship

Before 3 Oct 2026, Elets confirms the price on sale from 1 Oct (/delegate/ shows Late Access Rs 30,000 / Rs 60,000 after Standard ended 30 Sept; the homepage card still shows Rs 20,000), the GST wording, any corporate tiers, and whether award nominations are still open. The web dev then makes all the changes in one deploy:
- On the homepage, replace the FAQ block, fix the price card and add the Event JSON-LD (FAQPage is optional).
- On /ai-conference-bengaluru-2026.html, change only the title, meta description and H1, and add the link row. Do not copy the FAQ onto this page, per correction 3.
- Add the internal link to the homepage nav or footer and to the 5 blog posts.
- Add the redirects, in either the Apache or the nginx version. Check rel=canonical before turning on the host rule.

Validate the JSON-LD in the Rich Results Test once the PLACEHOLDER_ digits are filled in. Then add a www or Domain property in Search Console and request indexing for the homepage and the landing page. Recheck rankings on 8 Oct.

Corrections applied from the verifier:
- Cypher is #1 for 'ai conferences 2026 india', not #3. WAIS is not in the top 20.
- #14 for 'upcoming ai events in india' is on page 2.
- The addressable volume is about 1,400/mo, not 1,800, because the two 390 keywords are one close-variant group.
- FAQ rich results will not show for this site, so any gain comes from text relevance and AI-answer citation.
- The awards question is held back.
- The 'Bangalore' reason is search volume (320 vs 40/mo), not Cypher's H1.

Sources:
- Facts were checked live on 1 Oct on https://www.worldaisummit.com/, /delegate/, /ai-conference-bengaluru-2026.html and /speaker.html.
- The venue address comes from the Marriott hotel page: https://www.marriott.com/en-us/hotels/blrgs-sheraton-grand-bangalore-hotel-at-brigade-gateway/overview/
- Performers are limited to the 8 'Featured AI Speakers' shown on the live landing page.

No repository files were edited and no paid OpenSEO tools were used. A copy of the asset is at /tmp/claude-0/-home-user-123/bf9e82cf-ebf4-58a1-ab65-7230ef80c0ff/scratchpad/faqlens_8734/asset.md.

The relayed user question ('do you have more CPUs from computer?') is not answered by this asset and needs a direct reply in the main session.

## Content

# World AI Summit 2026: query-phrased FAQ, landing page fix and Event schema
Ship by 3 Oct 2026 (Google needs about a week to re-crawl before 9-14 Oct). Owner: web dev + content. Effort: under 2 hours.

## 0. Gates before publishing (Elets to confirm)
- PLACEHOLDER_PREMIUM_PRICE / PLACEHOLDER_VIP_PRICE: /delegate/ shows Standard Access Rs 20,000 / Rs 35,000 "valid till 30th Sept 2026" and Late Access Rs 30,000 / Rs 60,000. The homepage "Secure your seat" card still shows "Premium Pass Rs 20,000/delegate". Confirm the price on sale from 1 Oct, then put the same figure in the FAQ, the homepage price card (section 2) and the JSON-LD (section 3) in one deploy. If they disagree, the FAQ contradicts the card on the same page.
- PLACEHOLDER_GST_TREATMENT: replace with "inclusive of GST" or "plus GST".
- PLACEHOLDER_CORPORATE_TIERS: one sentence on any other corporate tier, or delete the marker.
- PLACEHOLDER_AWARDS_DEADLINE: the awards question is commented out. Publish it only if nominations are still open and the deadline is confirmed. Otherwise leave it out.

## 1. Homepage (/): replace the 10 generic FAQ items with this block
Keep the site's existing accordion classes and script. The answers must stay in the HTML source (not loaded by JavaScript) so Google and AI answer engines can read them.

```html
<section class="faq" id="faq" aria-labelledby="faq-title">
  <h2 id="faq-title">Frequently asked questions</h2>
  <details>
    <summary>When and where is the AI Summit in Bangalore in October 2026?</summary>
    <p>World AI Summit 2026 takes place on 14-15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru (Bangalore). The two-day summit is organised by Elets Technomedia. Delegate passes are available on the <a href="/delegate/">delegate page</a>.</p>
  </details>
  <details>
    <summary>Which AI conferences are happening in Bangalore in October 2026?</summary>
    <p>World AI Summit 2026 is a two-day AI conference in Bangalore on 14-15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway. It runs seven tracks: Frontier Models &amp; Compute; Sovereign AI &amp; Geopolitics; Enterprise AI in Production; Global Capability Centres (GCCs); Robotics, Agents &amp; Embodied AI; AI for Bharat; and Capital, Founders &amp; Exits. Details are on the <a href="/ai-conference-bengaluru-2026.html">AI Conference Bangalore 2026</a> page.</p>
  </details>
  <details>
    <summary>How much do AI Summit 2026 tickets cost?</summary>
    <p>The Premium Pass costs Rs PLACEHOLDER_PREMIUM_PRICE and the VIP Pass costs Rs PLACEHOLDER_VIP_PRICE per delegate (PLACEHOLDER_GST_TREATMENT). The Premium Pass includes full summit access, the delegate kit, lunch and refreshments, and a certificate of participation. The VIP Pass adds priority seating, speaker lounge access, an exclusive networking dinner and special sessions on GenAI, Agentic AI and AI Safety. Groups of three or more delegates get 10% off. Book on the <a href="/delegate/">delegate page</a> or write to <a href="mailto:registration@worldaisummit.com">registration@worldaisummit.com</a>.</p>
  </details>
  <details>
    <summary>How do I register for AI Summit 2026?</summary>
    <p>Choose the Premium or VIP pass on the <a href="/delegate/">World AI Summit 2026 delegate page</a> and complete checkout. Confirmation and event updates are sent to registered delegates. For group bookings or other registration questions, write to <a href="mailto:registration@worldaisummit.com">registration@worldaisummit.com</a>.</p>
  </details>
  <details>
    <summary>Who should attend this AI conference in India?</summary>
    <p>The summit is designed for government officials and policymakers; CIOs, CTOs and CDOs; AI and data science leaders; leaders of Global Capability Centres; AI startups, founders and innovators; investors and venture capitalists; technology vendors; academia and researchers; and international organisations and think tanks.</p>
  </details>
  <details>
    <summary>How can my company sponsor or exhibit at an AI conference in India in 2026?</summary>
    <p>World AI Summit 2026 offers customised sponsorship and exhibition packages. Write to <a href="mailto:partnerships@worldaisummit.com">partnerships@worldaisummit.com</a>. For speaking and collaboration, write to <a href="mailto:secretariat@worldaisummit.com">secretariat@worldaisummit.com</a>.</p>
  </details>
  <details>
    <summary>Is there a group or corporate pass?</summary>
    <p>Yes. Groups of three or more delegates get 10% off delegate passes. To book for a group, write to <a href="mailto:registration@worldaisummit.com">registration@worldaisummit.com</a>. PLACEHOLDER_CORPORATE_TIERS</p>
  </details>
  <!-- OPTIONAL: publish only after Elets confirms PLACEHOLDER_AWARDS_DEADLINE and that nominations are open. Add the same Q/A to the FAQPage JSON-LD.
  <details>
    <summary>How do I nominate for AI awards in India in 2026?</summary>
    <p>Nominations for the World AI Awards 2026 are submitted on the <a href="/awards/">World AI Awards page</a>. The last date for nominations is PLACEHOLDER_AWARDS_DEADLINE.</p>
  </details>
  -->
</section>
```

## 2. Homepage price card ("Secure your seat")
Change "Premium Pass Rs 20,000/ delegate" to "Premium Pass Rs PLACEHOLDER_PREMIUM_PRICE/ delegate" and show the VIP Pass at Rs PLACEHOLDER_VIP_PRICE, with the same GST wording as the FAQ. The other two cards have benefits but no price or name, so label them.

## 3. JSON-LD for the homepage <head>
If the homepage already has an Event block, replace it. Do not add a second Event. Replace the two PLACEHOLDER_..._DIGITS values with digits only (for example 30000), not "Rs 30,000". Then run https://search.google.com/test/rich-results and https://validator.schema.org/.
Performers are only the 8 people listed under "Featured AI Speakers" on /ai-conference-bengaluru-2026.html (live page, 1 Oct). Add others only after they appear as 2026 speakers on the site. Address source: Marriott hotel page (https://www.marriott.com/en-us/hotels/blrgs-sheraton-grand-bangalore-hotel-at-brigade-gateway/overview/), "26/1 Dr Rajkumar Rd, Malleswaram-Rajajinagar, Bengaluru 560055". Image is left out because no verified event image URL exists. Add "image": ["<1200px-wide URL>"] if one exists.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Event",
  "@id": "https://www.worldaisummit.com/#event-2026",
  "name": "World AI Summit 2026",
  "description": "World AI Summit 2026, organised by Elets Technomedia, brings together policymakers, industry leaders, innovators, researchers and investors in Bengaluru across seven tracks, from Frontier Models & Compute to AI for Bharat.",
  "url": "https://www.worldaisummit.com/",
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
  "offers": [
    {
      "@type": "Offer",
      "name": "Premium Pass",
      "url": "https://www.worldaisummit.com/delegate/",
      "price": "PLACEHOLDER_PREMIUM_PRICE_DIGITS",
      "priceCurrency": "INR",
      "availability": "https://schema.org/InStock"
    },
    {
      "@type": "Offer",
      "name": "VIP Pass",
      "url": "https://www.worldaisummit.com/delegate/",
      "price": "PLACEHOLDER_VIP_PRICE_DIGITS",
      "priceCurrency": "INR",
      "availability": "https://schema.org/InStock"
    }
  ],
  "performer": [
    {
      "@type": "Person",
      "name": "Pankaj Kumar Pandey",
      "jobTitle": "Principal Secretary, Department of Personnel and Administrative Reforms (e-Governance)",
      "affiliation": {
        "@type": "Organization",
        "name": "Government of Karnataka"
      }
    },
    {
      "@type": "Person",
      "name": "Ravikumar Surpur",
      "jobTitle": "Secretary, Information Technology & Communication Department",
      "affiliation": {
        "@type": "Organization",
        "name": "Government of Rajasthan"
      }
    },
    {
      "@type": "Person",
      "name": "Aman Mittal",
      "jobTitle": "Joint Chief Executive Officer",
      "affiliation": {
        "@type": "Organization",
        "name": "Maharashtra Institution for Transformation (MITRA)"
      }
    },
    {
      "@type": "Person",
      "name": "Sanjeev Gupta",
      "jobTitle": "Chief Executive Officer",
      "affiliation": {
        "@type": "Organization",
        "name": "Karnataka Digital Economy Mission"
      }
    },
    {
      "@type": "Person",
      "name": "Ram Mohan Rao",
      "jobTitle": "Executive Director",
      "affiliation": {
        "@type": "Organization",
        "name": "Securities and Exchange Board of India (SEBI)"
      }
    },
    {
      "@type": "Person",
      "name": "Sandeep Varaganti",
      "jobTitle": "CEO, JioMart",
      "affiliation": {
        "@type": "Organization",
        "name": "Reliance Retail"
      }
    },
    {
      "@type": "Person",
      "name": "Sanjeev Rastogi",
      "jobTitle": "Head, Group Policy Services",
      "affiliation": {
        "@type": "Organization",
        "name": "Adani Group"
      }
    },
    {
      "@type": "Person",
      "name": "George Inasu",
      "jobTitle": "Managing Director and Country Head",
      "affiliation": {
        "@type": "Organization",
        "name": "Fidelity National Financial India"
      }
    }
  ]
}
</script>
```

FAQPage block. Optional: since Aug 2023, Google shows FAQ rich results only for authoritative government and health sites, so this will not produce a rich result. It is kept for machine-readable answers. The text must match the visible FAQ word for word, including the replaced placeholders.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "When and where is the AI Summit in Bangalore in October 2026?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "World AI Summit 2026 takes place on 14-15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru (Bangalore). The two-day summit is organised by Elets Technomedia. Delegate passes are available on the delegate page."
      }
    },
    {
      "@type": "Question",
      "name": "Which AI conferences are happening in Bangalore in October 2026?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "World AI Summit 2026 is a two-day AI conference in Bangalore on 14-15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway. It runs seven tracks: Frontier Models & Compute; Sovereign AI & Geopolitics; Enterprise AI in Production; Global Capability Centres (GCCs); Robotics, Agents & Embodied AI; AI for Bharat; and Capital, Founders & Exits. Details are on the AI Conference Bangalore 2026 page."
      }
    },
    {
      "@type": "Question",
      "name": "How much do AI Summit 2026 tickets cost?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The Premium Pass costs Rs PLACEHOLDER_PREMIUM_PRICE and the VIP Pass costs Rs PLACEHOLDER_VIP_PRICE per delegate (PLACEHOLDER_GST_TREATMENT). The Premium Pass includes full summit access, the delegate kit, lunch and refreshments, and a certificate of participation. The VIP Pass adds priority seating, speaker lounge access, an exclusive networking dinner and special sessions on GenAI, Agentic AI and AI Safety. Groups of three or more delegates get 10% off. Book on the delegate page or write to registration@worldaisummit.com."
      }
    },
    {
      "@type": "Question",
      "name": "How do I register for AI Summit 2026?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Choose the Premium or VIP pass on the World AI Summit 2026 delegate page and complete checkout. Confirmation and event updates are sent to registered delegates. For group bookings or other registration questions, write to registration@worldaisummit.com."
      }
    },
    {
      "@type": "Question",
      "name": "Who should attend this AI conference in India?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The summit is designed for government officials and policymakers; CIOs, CTOs and CDOs; AI and data science leaders; leaders of Global Capability Centres; AI startups, founders and innovators; investors and venture capitalists; technology vendors; academia and researchers; and international organisations and think tanks."
      }
    },
    {
      "@type": "Question",
      "name": "How can my company sponsor or exhibit at an AI conference in India in 2026?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "World AI Summit 2026 offers customised sponsorship and exhibition packages. Write to partnerships@worldaisummit.com. For speaking and collaboration, write to secretariat@worldaisummit.com."
      }
    },
    {
      "@type": "Question",
      "name": "Is there a group or corporate pass?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Groups of three or more delegates get 10% off delegate passes. To book for a group, write to registration@worldaisummit.com. PLACEHOLDER_CORPORATE_TIERS"
      }
    }
  ]
}
</script>
```

## 4. /ai-conference-bengaluru-2026.html: title and H1 only
Do not copy the homepage FAQ here. The page already has its own FAQ with the date and venue, and a second copy would make the two pages compete for the same queries. Its body already says "AI conference in Bangalore or Bengaluru in 2026". The reason for "Bangalore" is search volume: "ai summit bangalore" gets 320/mo and "ai summit bengaluru" gets 40/mo. Cypher's landing page H1 says Bengaluru, and only its URL and homepage title say Bangalore.

```html
<title>AI Conference Bangalore 2026 | World AI Summit, 14-15 Oct</title>
<meta name="description" content="AI conference in Bangalore (Bengaluru), 14-15 October 2026, at Sheraton Grand Bangalore Hotel at Brigade Gateway. Seven tracks. Book a delegate pass.">
<!-- replace the H1 "AI Conference Bengaluru 2026" -->
<h1>AI Conference Bangalore (Bengaluru) 2026</h1>
<!-- add under the hero stats row -->
<p class="plan-links"><a href="/delegate/">Book a delegate pass</a> &middot; <a href="/speaker.html">See the 2026 speakers</a> &middot; <a href="/awards/">World AI Awards</a></p>
```
The title is 57 characters and the meta description is 149. Keep the URL unchanged. Do not rename it to "bangalore", because the page is not indexed yet and a new URL would start from zero again.

## 5. Internal links (the landing page has crawl depth null today: it is in the sitemap, but no page links to it)
Homepage nav or footer:
```html
<a href="/ai-conference-bengaluru-2026.html">AI Conference Bangalore 2026</a>
```
Add one sentence near the end of each of the 5 blog posts:
```html
<p>World AI Summit 2026, an <a href="/ai-conference-bengaluru-2026.html">AI conference in Bangalore</a>, takes place on 14-15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway. <a href="/delegate/">Book a delegate pass</a>.</p>
```
The new FAQ also links /delegate/ from the homepage. Today /delegate/ is found only through the sitemap.

## 6. Redirects: send registration URLs to the pass page in one hop
Today /registration and /registration.html 302 to the homepage through non-www, in 3 hops. Before you enable the host rule, check that rel=canonical on live pages uses https://www.worldaisummit.com/. Choose a single variant for your server.

Apache (.htaccess at the web root, above any existing rules):
```apache
RewriteEngine On
# Registration URLs go straight to the delegate pass page (any host, one hop)
RewriteRule ^registration(\.html)?/?$ https://www.worldaisummit.com/delegate/ [R=301,L,NC]
# Canonical host: http or non-www goes to https://www (path kept)
RewriteCond %{HTTPS} off [OR]
RewriteCond %{HTTP_HOST} ^worldaisummit\.com$ [NC]
RewriteRule ^(.*)$ https://www.worldaisummit.com/$1 [R=301,L]
```
If the site is behind Cloudflare or a load balancer that ends TLS, %{HTTPS} can read "off" on every request. In that case, drop the HTTPS condition and redirect HTTP at the CDN instead.

nginx:
```nginx
# non-www (http and https) and http www: one hop to the canonical URL
server {
    listen 80;
    listen 443 ssl;
    server_name worldaisummit.com;
    # ssl_certificate / ssl_certificate_key: same as the www block
    rewrite ^/registration(\.html)?/?$ https://www.worldaisummit.com/delegate/ permanent;
    return 301 https://www.worldaisummit.com$request_uri;
}
server {
    listen 80;
    server_name www.worldaisummit.com;
    rewrite ^/registration(\.html)?/?$ https://www.worldaisummit.com/delegate/ permanent;
    return 301 https://www.worldaisummit.com$request_uri;
}
# inside the existing "listen 443 ssl; server_name www.worldaisummit.com;" block:
rewrite ^/registration(\.html)?/?$ https://www.worldaisummit.com/delegate/ permanent;
```
Test with: curl -sI https://worldaisummit.com/registration.html. You should see one 301 to https://www.worldaisummit.com/delegate/.

## 7. After deploy (same day)
1. Search Console currently has only the non-www URL-prefix property, so the www URL cannot be inspected. Add a Domain property (DNS TXT) or a https://www.worldaisummit.com/ property. Then use URL Inspection and Request indexing for https://www.worldaisummit.com/ and https://www.worldaisummit.com/ai-conference-bengaluru-2026.html. On 1 Oct, the non-www copy of the landing page returned "URL is unknown to Google".
2. Resubmit the sitemap.
3. On 8 Oct, recheck "ai events in bangalore" (WAIS #9), "upcoming ai events in india" (#14, which is page 2), "ai conferences in india" (not in top 20), "ai summit bangalore" (#5) and "ai summit registration" (#4).

