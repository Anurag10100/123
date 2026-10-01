# A27: World AI Awards 2026 page (/awards/): head tags, on-page copy above the form, JSON-LD, internal links and a one-hop redirect

- **For recommendation:** Give /awards/ visible categories, fee, deadline and a distinct title so it beats the unrelated worldawards.ai for 'world ai awards' and can compete with Cypher's 'AI Awards India 2026' page
- **Research lens:** serp-features
- **Format:** HTML (head and body snippets) + JSON-LD + Apache .htaccess and nginx redirect rules + curl test commands
- **Placeholders the business must fill:**
  - PLACEHOLDER_CEREMONY_DATE: day (14 or 15 Oct 2026), time and hall of the awards ceremony
  - PLACEHOLDER_NOMINATION_DEADLINE: 2026 closing date (not public anywhere as of 1 Oct)
  - PLACEHOLDER_FEE_STARTUP_INDIVIDUAL: 2026 fee for Startup and Individual entries (2025: Rs 18,000 + GST)
  - PLACEHOLDER_FEE_ENTERPRISE_GOVT_LEADERSHIP_SP: 2026 fee for Enterprise, Government, Leadership and Solution Provider entries (2025: Rs 20,000 + GST)
  - PLACEHOLDER_FEE_INCLUSIONS_AND_PAYMENT_STEP: when the fee is paid and whether a summit pass is included
  - PLACEHOLDER_AWARDS_CONTACT_EMAIL: awards enquiries inbox (the /awards/ page currently shows secretariat@worldaisummit.com)
  - PLACEHOLDER_CONFIRM_2026_CATEGORIES: check the six groups and example sub-awards against the 2026 'Select Sectors' dropdown
  - PLACEHOLDER_CONFIRM_ELIGIBILITY_2026: who may enter in 2026 (2025 had two entry types)
  - PLACEHOLDER_EVALUATION_CRITERIA_2026: jury criteria and weighting
  - PLACEHOLDER_JURY_2026: 2026 jury names, or delete the placeholder
  - PLACEHOLDER_PAST_WINNERS: 2025 winners list or link (none found on /1st-edition/awards.html)
  - PLACEHOLDER_CURRENT_PASS_PRICE: current delegate pass price as a bare number for JSON-LD
  - PLACEHOLDER_EVENT_IMAGE_URL: absolute URL of an event image, at least 1200px wide
  - PLACEHOLDER_PUBLISH_DATE: sitemap lastmod (YYYY-MM-DD)

## How to ship

Owner: content (copy) plus web dev (head tags, redirects). Ship by 6 Oct 2026, or earlier if the 2026 nomination deadline falls sooner.

1. Before you change anything, run the curl loop in section 6 and save the output. The second hop (www /awards to /awards/) is inferred, so confirm it first.
2. Fill every PLACEHOLDER_ value with the awards team. Do not publish the 2025 fees as 2026 fees. For reference, 2025 charged Rs 18,000 + GST per entry for Startup & Individual and Rs 20,000 + GST for Enterprise, Government, Leadership and Solution Provider (source: elets.net/worldaisummit-awards/). Check the six category labels against the live 2026 'Select Sectors' dropdown. Exa did not render that dropdown, so the 2025 labels are used here. They are AI in Enterprises, Business Transformation & Innovation, SmartTech AI Awards, AI in Governance, AI Startups and AI Leadership. The 2025 awards page names two of these groups differently ('AI Enterprise & Application', 'Smart Tech & AI Engineering'). Whatever you pick, the page labels and the form labels must be the same. If there is no 2025 winners list, follow the comment under 'Past winners': worldaisummit.com/1st-edition/awards.html shows categories and jury but no winners.
3. Replace the head tags (section 1). Paste the body copy above the form (section 2). Change the current theme H1 to a <p>, and change the form's 'Select Sectors' H2 to an H3. The page should then have one H1 and the seven H2s in order.
4. Add the JSON-LD (section 3) and remove any duplicate Event block on this page. Set price to a bare number, for example 30000. /delegate/ showed Late Access at Rs 30,000/60,000 after the 30 Sep Standard cutoff, but confirm the current price. Check the page in the Google Rich Results Test and validator.schema.org. The venue address (26/1 Dr. Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru 560055) was checked against the hotel's Marriott page and its Google Hotels listing.
5. Put the redirect rules (section 5a or 5b) above the existing host and https rules. Reload the server, then run the curl loop again. Each variant must reach https://www.worldaisummit.com/awards/ in one 301 and end on 200, and /awards/ itself must return 200 with no redirect. If anything loops, roll back at once: the non-www /awards URL is the one Google currently ranks.
6. Add the nav link and the homepage awards block (section 4). Fix the /awards link on /faqs, and make sure the sitemap lists only https://www.worldaisummit.com/awards/.
7. Search Console: only the non-www URL-prefix property is connected, so the live www URL cannot be inspected. Add a Domain property for worldaisummit.com (DNS TXT record), inspect https://www.worldaisummit.com/awards/ and request indexing.
8. Optional: /award.html currently canonicalises to the homepage. Look at its content, and if it is an old awards page, 301 it to /awards/.
9. Measure after 7-14 days in GSC, against the 31 Aug-28 Sep baseline. That window had 44 impressions at position 3 for 'world ai awards', 178 at 8.6 for 'ai awards 2026', 115 at 10.0 for 'ai awards' and 24 at 7.8 for 'ai awards india'. The page as a whole had 32 clicks and 1,300 impressions at position 7.9.

Note on the relayed user question ('do you have more CPUs from computer?'): this cloud container has 4 CPUs (nproc). It cannot draw on extra CPUs from the user's own computer.

## Content

=====================================================================
1) <head> of https://www.worldaisummit.com/awards/ (replace the existing title, description, canonical and OG tags)
=====================================================================
<title>World AI Awards 2026 | Nominate Now | Bengaluru, 14-15 Oct</title>
<meta name="description" content="Nominate your AI project for the World AI Awards 2026 at World AI Summit, Bengaluru, 14-15 October 2026. Categories, eligibility, fee and how to apply.">
<link rel="canonical" href="https://www.worldaisummit.com/awards/">
<meta name="robots" content="index, follow">
<meta property="og:type" content="website">
<meta property="og:url" content="https://www.worldaisummit.com/awards/">
<meta property="og:title" content="World AI Awards 2026 | Nominate Now | Bengaluru, 14-15 Oct">
<meta property="og:description" content="Nominate your AI project for the World AI Awards 2026 at World AI Summit, Bengaluru, 14-15 October 2026. Categories, eligibility, fee and how to apply.">
<meta property="og:image" content="PLACEHOLDER_EVENT_IMAGE_URL">
<meta name="twitter:card" content="summary_large_image">

<!-- Title: 58 characters. Meta description: 151 characters. -->

=====================================================================
2) <body>: put this ABOVE the existing nomination form
=====================================================================
<!-- The page's current <h1> is the event theme. Change it to a paragraph so the page has one H1. -->
<p class="event-theme">AI for All: Accelerating India's Journey Towards Inclusive, Responsible and Future-Ready AI</p>

<h1>World AI Awards 2026</h1>

<p class="lead">The World AI Awards 2026 recognise real-world uses of AI by enterprises, government, startups and leaders. The awards are part of World AI Summit 2026, organised by Elets Technomedia on 14-15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru, India. Winners will be announced at the summit on PLACEHOLDER_CEREMONY_DATE.</p>

<ul class="award-facts">
  <li><strong>Summit dates:</strong> 14-15 October 2026</li>
  <li><strong>Venue:</strong> Sheraton Grand Bangalore Hotel at Brigade Gateway, 26/1 Dr. Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru 560055</li>
  <li><strong>Nomination deadline:</strong> PLACEHOLDER_NOMINATION_DEADLINE</li>
  <li><strong>Nomination fee:</strong> from PLACEHOLDER_FEE_STARTUP_INDIVIDUAL + GST per entry</li>
</ul>
<p><a class="btn" href="#nominate">Nominate now</a></p>

<h2>Award categories</h2>
<p>Nominations are made in six category groups. In the form below, choose the group that fits your work first and then the specific award.</p>
<!-- PLACEHOLDER_CONFIRM_2026_CATEGORIES: the six labels below are the 2025 form dropdown labels, and the examples are 2025 sub-awards. Check them against the 2026 "Select Sectors" dropdown and sub-award list, and edit them to match, before you publish. -->

<h3>AI in Enterprises</h3>
<p>For organisations using AI in their operations. Examples: AI in banking and process automation, AI in health and pharma, AI in retail buying and forecasting, AI for supply chain management, AI innovation in cybersecurity, and AI in learning and skill development.</p>

<h3>Business Transformation &amp; Innovation</h3>
<p>For AI that changes how an organisation works. Examples: Generative AI Transformation Award, Responsible AI Implementation Award, Enterprise AI Adoption Trailblazer, Intelligent Automation Champion, AI Infrastructure Excellence Award and AI Innovation in Customer Engagement.</p>

<h3>SmartTech AI Awards</h3>
<p>For AI products, platforms and engineering. Examples: Conversational AI &amp; NLP Excellence, Best Enterprise AI Platform of the Year, Best AI-Powered SaaS Product, Cloud AI Service Provider of the Year, Predictive Intelligence Solution of the Year, and AI Validation &amp; Testing Excellence.</p>

<h3>AI in Governance</h3>
<p>For government departments and public bodies. Examples: AI for Public Service Delivery Excellence, Outstanding Citizen Engagement Initiative, Data-Driven Governance Award, and AI for E-Governance Initiatives.</p>

<h3>AI Startups</h3>
<p>For early-stage and growth-stage companies. Examples: Most Promising AI Startup, AI Startup of the Year, Generative AI Startup Excellence, AI for Social Impact, AI for Sustainability Award, and Fastest Growing AI Startup.</p>

<h3>AI Leadership</h3>
<p>For individuals. Examples: AI Leader of the Year, Chief AI Officer of the Year, AI Policy Visionary Award, AI Governance Champion, and AI Academic Leader.</p>

<p>See the <a href="/1st-edition/awards.html">full list of 2025 award categories</a>.</p>

<h2>Who can apply</h2>
<p>PLACEHOLDER_CONFIRM_ELIGIBILITY_2026. The following can apply:</p>
<ul>
  <li>Enterprises and solution providers, for an AI product, project or deployment</li>
  <li>Government departments and public sector bodies</li>
  <li>AI startups</li>
  <li>Individuals, for the AI Leadership awards</li>
</ul>
<p>Each nomination form covers one award. To enter more than one award, submit a separate form for each.</p>

<h2>Nomination fee</h2>
<table class="fee-table">
  <thead>
    <tr><th scope="col">Entry type</th><th scope="col">Fee per entry</th></tr>
  </thead>
  <tbody>
    <tr><td>Startup and Individual categories</td><td>PLACEHOLDER_FEE_STARTUP_INDIVIDUAL + GST</td></tr>
    <tr><td>Enterprise, Government, Leadership and Solution Provider categories</td><td>PLACEHOLDER_FEE_ENTERPRISE_GOVT_LEADERSHIP_SP + GST</td></tr>
  </tbody>
</table>
<p>PLACEHOLDER_FEE_INCLUSIONS_AND_PAYMENT_STEP (for example, when the fee is paid and whether a summit pass is included). For questions about nominations, write to PLACEHOLDER_AWARDS_CONTACT_EMAIL.</p>

<h2>Deadline</h2>
<p>Nominations close on PLACEHOLDER_NOMINATION_DEADLINE. Winners will be announced at World AI Summit 2026 in Bengaluru on PLACEHOLDER_CEREMONY_DATE.</p>

<h2>How entries are evaluated</h2>
<p>A jury reviews every nomination. PLACEHOLDER_EVALUATION_CRITERIA_2026</p>
<p>The form asks for the following, so have it ready before you start:</p>
<ul>
  <li>Project title, the area or territory it covers, and how long it has run</li>
  <li>A brief overview of the project</li>
  <li>The problem it solves and who benefits</li>
  <li>How you have scaled it, or plan to scale it</li>
  <li>Approximate budget or investment</li>
  <li>Key stakeholders and technology partners</li>
  <li>Supporting material, for example a project summary, a presentation, photographs of the implementation, a video demo, certifications or past awards</li>
</ul>
<p>The 2025 jury included Dr. Ravi Gupta (Founder, Publisher and CEO, Elets Technomedia), Manish Bhardwaj, IAS (Deputy Director General, Unique Identification Authority of India) and Deepak Sharma (Independent Director, Suryoday Small Finance Bank). These are their roles as listed in 2025. PLACEHOLDER_JURY_2026</p>

<h2>Past winners</h2>
<!-- PLACEHOLDER_PAST_WINNERS: add the 2025 winners here (award and organisation) or link to a page that lists them. If no winners list is published, delete this comment, rename the heading to "World AI Awards 2025" and keep only the paragraph below. -->
<p>The World AI Awards 2025 were part of World AI Summit 2025, held on 25-26 September 2025 at Sheraton Grand Brigade Gateway, Bengaluru. See the <a href="/1st-edition/awards.html">2025 award categories and jury</a>.</p>

<h2 id="nominate">Nominate now</h2>
<p>Fill in the form below and upload your supporting documents. Do not upload password-protected files. Any Google Drive links must be public.</p>
<!-- The existing form markup goes here, unchanged. Inside the form, change the "Select Sectors" heading from <h2> to <h3> so the page outline stays clean. -->

=====================================================================
3) JSON-LD: paste in <head> or before </body>. Replace any older Event schema on this page so there are no duplicates.
=====================================================================
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://www.worldaisummit.com/awards/#webpage",
      "url": "https://www.worldaisummit.com/awards/",
      "name": "World AI Awards 2026 | Nominate Now | Bengaluru, 14-15 Oct",
      "description": "Nominate your AI project for the World AI Awards 2026 at World AI Summit, Bengaluru, 14-15 October 2026. Categories, eligibility, fee and how to apply.",
      "inLanguage": "en-IN",
      "isPartOf": { "@type": "WebSite", "@id": "https://www.worldaisummit.com/#website", "url": "https://www.worldaisummit.com/", "name": "World AI Summit" },
      "about": { "@id": "https://www.worldaisummit.com/#event-2026" },
      "breadcrumb": { "@id": "https://www.worldaisummit.com/awards/#breadcrumb" }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://www.worldaisummit.com/awards/#breadcrumb",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "World AI Summit 2026", "item": "https://www.worldaisummit.com/" },
        { "@type": "ListItem", "position": 2, "name": "World AI Awards 2026", "item": "https://www.worldaisummit.com/awards/" }
      ]
    },
    {
      "@type": "Event",
      "@id": "https://www.worldaisummit.com/#event-2026",
      "name": "World AI Summit 2026",
      "description": "World AI Summit 2026 in Bengaluru, organised by Elets Technomedia. The World AI Awards 2026 are presented at the summit.",
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
      "organizer": {
        "@type": "Organization",
        "name": "Elets Technomedia Pvt. Ltd.",
        "url": "https://www.eletsonline.com/"
      },
      "offers": {
        "@type": "Offer",
        "name": "Delegate pass",
        "url": "https://www.worldaisummit.com/delegate/",
        "price": "PLACEHOLDER_CURRENT_PASS_PRICE",
        "priceCurrency": "INR",
        "availability": "https://schema.org/InStock"
      }
    }
  ]
}
</script>
<!-- price must be a bare number with no "Rs" or commas, for example "30000". "performer" is left out on purpose: this is the awards page. Speaker pages should carry performer markup, and only for speakers marked confirmed_2026 in speakers.json. -->

=====================================================================
4) Internal links (the 1 Oct crawl did not reach /awards/ by following links)
=====================================================================
<!-- Main navigation, every page -->
<li><a href="/awards/">Awards</a></li>

<!-- Homepage awards block -->
<section id="awards">
  <h2>World AI Awards 2026</h2>
  <p>Nominate your AI project, startup or leader for the World AI Awards 2026, presented at World AI Summit in Bengaluru. Nominations close on PLACEHOLDER_NOMINATION_DEADLINE.</p>
  <p><a href="/awards/">See categories and nominate</a></p>
</section>

<!-- /faqs and any other page: change links to "/awards" or "https://worldaisummit.com/awards" so they point to "/awards/" -->

<!-- sitemap.xml: list only the final URL -->
<url><loc>https://www.worldaisummit.com/awards/</loc><lastmod>PLACEHOLDER_PUBLISH_DATE</lastmod></url>

=====================================================================
5a) Apache (.htaccess at the web root). Put these lines ABOVE the existing non-www-to-www and http-to-https rules.
=====================================================================
RewriteEngine On

# World AI Awards: send every variant of /awards to the final URL in a single 301
# (a) non-www, http or https, with or without the trailing slash
RewriteCond %{HTTP_HOST} ^worldaisummit\.com$ [NC]
RewriteRule ^awards/?$ https://www.worldaisummit.com/awards/ [R=301,L]
# (b) www, no trailing slash (covers http and https)
RewriteCond %{HTTP_HOST} ^www\.worldaisummit\.com$ [NC]
RewriteRule ^awards$ https://www.worldaisummit.com/awards/ [R=301,L]

# Optional, site-wide: when the non-www redirect lands on a directory, add the slash in the same hop
# (removes the same 2-hop chain for /delegate, /blog and similar URLs)
RewriteCond %{HTTP_HOST} ^worldaisummit\.com$ [NC]
RewriteCond %{REQUEST_FILENAME} -d
RewriteRule ^(.*[^/])$ https://www.worldaisummit.com/$1/ [R=301,L]

# Do not add a "%{HTTPS} off" rule for /awards/ itself. Behind a CDN or proxy that terminates TLS, it can loop.

=====================================================================
5b) nginx
=====================================================================
# Non-www host, http and https. Keep your existing ssl_certificate lines.
server {
    listen 80;
    listen 443 ssl;
    server_name worldaisummit.com;
    location ~ ^/awards/?$ { return 301 https://www.worldaisummit.com/awards/; }
    location / { return 301 https://www.worldaisummit.com$request_uri; }
}

# www host, http
server {
    listen 80;
    server_name www.worldaisummit.com;
    location ~ ^/awards/?$ { return 301 https://www.worldaisummit.com/awards/; }
    location / { return 301 https://www.worldaisummit.com$request_uri; }
}

# www host, https: add inside the EXISTING server block. Use an exact match so /awards/ itself never redirects.
location = /awards { return 301 https://www.worldaisummit.com/awards/; }

=====================================================================
6) Test before and after (each line should print "1 https://www.worldaisummit.com/awards/ 200", and the last one "0 ... 200")
=====================================================================
for u in https://worldaisummit.com/awards https://worldaisummit.com/awards/ http://worldaisummit.com/awards https://www.worldaisummit.com/awards http://www.worldaisummit.com/awards https://www.worldaisummit.com/awards/; do
  curl -sIL -o /dev/null -w "%{num_redirects} %{url_effective} %{http_code}\n" "$u"
done
curl -s https://www.worldaisummit.com/awards/ | grep -iE '<title>|rel="canonical"|<h1'
