# A52: /awards/ rebuild: World AI Awards 2026 with title, meta description, page copy (all 96 categories), JSON-LD, internal links and the /award.html 301

- **For recommendation:** Rebuild /awards/ on Cypher's 'AI Awards India 2026' pattern and capture nominators after Cypher's deadline
- **Research lens:** competitors
- **Format:** Markdown handover containing ready-to-paste HTML (head tags and body sections), JSON-LD (checked with a JSON parser) and redirect rules for Apache .htaccess and nginx
- **Placeholders the business must fill:**
  - PLACEHOLDER_NOMINATION_DEADLINE: full closing date and time (IST), e.g. 'Friday, 9 October 2026, 11:59 pm IST'
  - PLACEHOLDER_DEADLINE_SHORT: short form for the meta description, e.g. '9 Oct'
  - PLACEHOLDER_CEREMONY_DAY_AND_TIME: day and time of the 2026 awards ceremony within 14-15 Oct (the 2025 ceremony was on day one, 25 Sep 2025)
  - PLACEHOLDER_FEE_TIERS: 2026 fee by entrant type. The page says only 'from 30k + GST'. In 2025, startup and individual entries were Rs 18,000 and enterprise, government, leadership and solution provider entries Rs 20,000. Delete the placeholder if there is a single fee.
  - PLACEHOLDER_MULTI_ENTRY_FEE_RULE: whether each extra category is charged in full, or a multi-entry discount applies
  - PLACEHOLDER_PASS_INCLUDED_ANSWER: whether the nomination fee includes a conference attendee pass (the 2025 checkout showed a separate 'Conference Attendee Pass INR 30000' line; it is unclear whether it was bundled or optional)
  - PLACEHOLDER_JUDGING_PROCESS: one or two sentences on screening, shortlist, any jury presentation round, weighting and conflict-of-interest rule
  - PLACEHOLDER_2026_JURY: confirmed 2026 jury names and titles, or 'to be announced on <date>'
  - PLACEHOLDER_2025_WINNERS_URL: URL of the full 2025 winners list (recommend creating /awards/winners-2025/)
  - PLACEHOLDER_CURRENT_PASS_PRICE_INR: current delegate pass price as a plain number (the Standard tier ended 30 Sept 2026; Late Access is listed at Rs 30,000/60,000)
  - PLACEHOLDER_EVENT_IMAGE_URL_1200x630: absolute URL of a summit image for the schema
  - PLACEHOLDER_AWARDS_IMAGE_URL_1200x630: absolute URL of an awards image for og:image and the schema
  - Confirm (no marker): that secretariat@worldaisummit.com is the right inbox for nomination queries, and that the six 2025 honourees can be named on the page

## How to ship

Ship by 4 Oct 2026. The ceremony is during 14-15 Oct and nominations need time to arrive.
1) Today (awards team, about 30 min): fill in the business placeholders. The most urgent are PLACEHOLDER_NOMINATION_DEADLINE, PLACEHOLDER_CEREMONY_DAY_AND_TIME and PLACEHOLDER_FEE_TIERS. The awards team should also confirm that secretariat@ is the right inbox for nomination queries and that the six 2025 honourees may be named (Elets published them on LinkedIn on 10 Oct 2025).
2) Web dev (about 2-3 h): open the live /awards/index.html on the server. Google currently shows its title as "Elets World AI Awards 2026", which differs from crawl c1b16b55, so the live file may have changed. Replace the head tags and insert the body sections around the existing form; keep the form markup and handler unchanged. Add the JSON-LD with the pass price as a plain number. Deploy the /award.html 301 using the Apache or nginx variant and confirm a single 301 hop with curl -I for both www and non-www. Add the six internal links, change any old /award.html hrefs and update the sitemap.
3) Validate: check that no PLACEHOLDER_ text remains (grep the file), then run the page through the Rich Results Test and the Schema Markup Validator.
4) Search Console: in the non-www property (the only one connected), use URL Inspection to request indexing of /awards/. Add a Domain property so the www URL is reported too.
5) Measure: compare 4 weeks after launch with the baseline of 31 Aug-28 Sep (/awards: 32 clicks, 1,300 impressions, average position 7.9). Track the queries 'ai awards 2026' (178 impressions, position 8.6), 'ai awards' (115, position 10), 'world ai awards' (44, position 3.0, 0 clicks) and 'ai awards india' (24, position 7.8). Impressions were already rising before the change, from about 20-30/day in August to 45-75/day in late September, so judge the change on CTR, position and the number of nominations, not on raw impressions.
6) After the ceremony, publish /awards/winners-2026/ and point PLACEHOLDER_2025_WINNERS_URL at a /awards/winners-2025/ page.
Sources (all checked 1 Oct 2026):
- Exa fetch of /award.html: 96 categories in 6 groups, 'Entries from 30k + GST', 75+ awards, 5+ jury members, 5 benefits, 6 steps.
- Exa fetch of /awards/: form fields and current H1.
- Exa fetch of /1st-edition/awards.html: 2025 jury and benefits.
- Venue address '26/1, Dr. Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru 560055': Google Hotels, Apple Maps and Cvent.
- 2025 honourees and the 25 Sep 2025 ceremony: Elets LinkedIn post linkedin.com/feed/update/urn:li:activity:7382347461534793730 and qualitrix.com/latest-news/world-ai-summit-bengaluru-2025/.
- Live Google title 'Elets World AI Awards 2026': WebSearch.
Other notes:
- The judging block is original copy based on the /awards/ form fields. Nothing is copied from Cypher.
- No OpenSEO paid tools were used. No files were edited.

## Content

## 0. Before you edit (5 minutes)

- **Check the live page first.** Google (US) now shows the /awards/ title as "Elets World AI Awards 2026". Crawl c1b16b55 and the Exa fetch both have "World AI Awards 2026 | Celebrating AI Excellence" and the H1 "AI for All: Accelerating India's Journey Towards Inclusive, Responsible and Future-Ready AI". This sandbox could not load the live page, so open the server copy of /awards/index.html and work from that.
- **Keep the current nomination form and its submit handler exactly as they are.** Only add the sections below around it.
- **Category text is already published, so the awards team does not need to supply it.** The 2026 copy is on /award.html (Exa fetch, 1 Oct 2026): 96 categories in 6 groups, "Entries from 30k + GST", 5 benefits and 6 nomination steps. Only the business facts marked PLACEHOLDER_ are still needed.

---

## 1. `<head>` (replace the existing title, description and canonical)

```html
<title>World AI Awards 2026 | AI Awards India - Categories & Nominations</title>
<meta name="description" content="Nominate for the World AI Awards 2026, Bengaluru, 14-15 Oct. 96 categories for enterprises, government, startups and leaders. From Rs 30,000 + GST. Closes PLACEHOLDER_DEADLINE_SHORT.">
<link rel="canonical" href="https://www.worldaisummit.com/awards/">
<meta property="og:type" content="website">
<meta property="og:url" content="https://www.worldaisummit.com/awards/">
<meta property="og:title" content="World AI Awards 2026 - Nominations open">
<meta property="og:description" content="96 award categories for enterprises, government, startups and AI leaders. Presented at World AI Summit 2026, 14-15 October, Bengaluru. Entries from Rs 30,000 + GST.">
<meta property="og:image" content="PLACEHOLDER_AWARDS_IMAGE_URL_1200x630">
```
The title is 65 characters and contains "World AI Awards 2026", which covers both "world ai awards" and "ai awards 2026". The meta description is 162 characters when PLACEHOLDER_DEADLINE_SHORT is written like "9 Oct". The deadline is placed last, so if Google truncates, only the deadline is lost.

---

## 2. `<body>`: content sections in page order

```html
<main id="awards">

<header class="awards-hero">
  <p class="eyebrow">World AI Summit 2026 · 14-15 October 2026 · Bengaluru</p>
  <h1>World AI Awards 2026</h1>
  <p class="lead">The World AI Awards recognise real-world applications of artificial intelligence that are advancing industries, improving public services and redefining innovation. Enterprises, government bodies, startups, AI solution providers and individual leaders can enter across 96 categories. Winners are honoured at World AI Summit 2026 in Bengaluru.</p>
  <p><a class="btn" href="#nominate">Nominate now</a> &nbsp; <a href="#categories">See all 96 categories</a></p>
</header>

<!-- KEY FACTS BOX -->
<section class="key-facts" aria-labelledby="key-facts-h">
  <h2 id="key-facts-h">Key facts</h2>
  <dl>
    <dt>Awards ceremony</dt>
    <dd>PLACEHOLDER_CEREMONY_DAY_AND_TIME, during World AI Summit 2026 (14-15 October 2026)</dd>
    <dt>Venue</dt>
    <dd>Sheraton Grand Bangalore Hotel at Brigade Gateway, 26/1 Dr Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru 560055</dd>
    <dt>Categories</dt>
    <dd>96 award categories in six groups</dd>
    <dt>Entry fee</dt>
    <dd>From Rs 30,000 + GST per entry. PLACEHOLDER_FEE_TIERS</dd>
    <dt>Nominations close</dt>
    <dd>PLACEHOLDER_NOMINATION_DEADLINE</dd>
    <dt>Who can enter</dt>
    <dd>Enterprises, government departments and agencies, startups, AI solution providers and individual AI leaders</dd>
    <dt>Questions</dt>
    <dd><a href="mailto:secretariat@worldaisummit.com">secretariat@worldaisummit.com</a></dd>
  </dl>
  <p><a class="btn" href="#nominate">Start your nomination</a></p>
</section>

<!-- WHY NOMINATE (the five benefits from the 2025 and 2026 awards pages) -->
<section aria-labelledby="why-h">
  <h2 id="why-h">Why nominate</h2>
  <h3>Global recognition</h3>
  <p>Position your AI work on a world stage and gain credibility among industry leaders and peers.</p>
  <h3>Credibility and trust</h3>
  <p>Earn a seal of excellence that strengthens your brand with clients, partners and investors.</p>
  <h3>Business exposure</h3>
  <p>Show your solution to potential collaborators, enterprises, government bodies and the media.</p>
  <h3>Networking</h3>
  <p>Meet decision-makers, technology innovators and AI policy leaders at World AI Summit 2026.</p>
  <h3>Investor and market access</h3>
  <p>Draw investor interest and open new markets through the visibility the awards bring.</p>
</section>

<!-- CATEGORY GROUPS: one H2 per group. Award names are copied exactly as published on /award.html, so they match the form's options. -->
<div id="categories">
<p>The 2026 awards have 96 categories in six groups. Pick the category that best matches your project, organisation or role.</p>

<section id="enterprise-application">
  <h2>AI Enterprise & Application awards (26 categories)</h2>
  <p>For organisations using AI in a specific function or sector.</p>
  <ul>
    <li>AI for Immersive Content Experience</li>
    <li>AI in Workforce Enablement Award</li>
    <li>AI-Powered Algorithms for Media & Entertainment</li>
    <li>AI in Robotics Utilization & Machine Learning</li>
    <li>Best AI Integration in Gaming Experience</li>
    <li>AI Use in Navigation & Travel Assistance</li>
    <li>AI in Learning & Skill Development</li>
    <li>AI in Recruitment, Screening & Evaluation</li>
    <li>AI-Powered Data Safeguard & Privacy Award</li>
    <li>AI in Retail Buying & Forecasting</li>
    <li>AI in Aerospace & Allied Services</li>
    <li>AI in Banking & Process Automation</li>
    <li>Best Use of AI in Automotive & Ancillary Industries</li>
    <li>AI-Enabled Crop Insights & Weather Prediction</li>
    <li>AI in Health & Pharma Intervention</li>
    <li>Intelligent Marketing Optimization Award</li>
    <li>AI-Enabled Conversational & Voice Assistance</li>
    <li>AI for Enhanced Supply Chain Management</li>
    <li>Smart AI Workforce Optimization Award</li>
    <li>Best Use of AI in Logistics & Distribution</li>
    <li>AI for Mobility Enhancement & Transit</li>
    <li>AI in Product Development & Innovation</li>
    <li>AI-Powered Financial Decision-Making</li>
    <li>AI for Risk & Compliance Management</li>
    <li>AI Implementation in E-commerce Operations & Insights</li>
    <li>AI Innovation in Cybersecurity</li>
  </ul>
</section>

<section id="business-transformation">
  <h2>Business Transformation & Innovation awards (13 categories)</h2>
  <p>For organisation-wide AI adoption, platforms and responsible AI practice.</p>
  <ul>
    <li>Best AI Innovation in Traffic Regulation</li>
    <li>Responsible AI Implementation Award</li>
    <li>Generative AI Transformation Award</li>
    <li>AI-Driven Personalization Award</li>
    <li>AI Infrastructure Excellence Award</li>
    <li>Enterprise AI Adoption Trailblazer</li>
    <li>Unified AI Ecosystem Excellence Award</li>
    <li>Real-Time AI Intelligence Award</li>
    <li>Intelligent Automation Champion</li>
    <li>Strategic AI Solution Partner of the Year</li>
    <li>AI Excellence in IoT Integration</li>
    <li>AI Innovation in Customer Engagement</li>
    <li>Responsible AI Pioneer Award</li>
  </ul>
</section>

<section id="smart-tech-engineering">
  <h2>Smart Tech & AI Engineering awards (16 categories)</h2>
  <p>For AI products, platforms, solution providers and consulting firms.</p>
  <ul>
    <li>Conversational AI & NLP Excellence</li>
    <li>Customer Experience AI Solution of the Year</li>
    <li>Computer Vision & Network Monitoring Award</li>
    <li>Intelligent Data Management Solution</li>
    <li>AI Strategy & Consulting Firm of the Year</li>
    <li>AI Transformation Award in Audio & Visual Creation</li>
    <li>Best AI-Powered SaaS Product</li>
    <li>Best Enterprise AI Platform of the Year</li>
    <li>Best AI Innovation in DeepTech</li>
    <li>Best Use of AI in Threat Detection & Insights</li>
    <li>Cloud AI Service Provider of the Year</li>
    <li>Predictive Intelligence Solution of the Year</li>
    <li>AI Innovation for Industry Applications</li>
    <li>AI Deployment & Marketplace Enabler</li>
    <li>AI Validation & Testing Excellence</li>
    <li>AI Development & Implementation Award (GPS, Product Design, Last-Mile Delivery, Robotics, Surveillance Tech, Self-Driven Cars, Chatbots, VR)</li>
  </ul>
</section>

<section id="governance">
  <h2>AI in Governance awards (4 categories)</h2>
  <p>For government departments, agencies and public-sector programmes.</p>
  <ul>
    <li>AI for Public Service Delivery Excellence</li>
    <li>Outstanding Citizen Engagement Initiative</li>
    <li>Data-Driven Governance Award</li>
    <li>AI for E-Governance Initiatives</li>
  </ul>
</section>

<section id="startups">
  <h2>AI Startups awards (19 categories)</h2>
  <p>For early-stage and growth-stage companies building with AI.</p>
  <ul>
    <li>Most Promising AI Startup</li>
    <li>AI Startup of the Year</li>
    <li>Disruptive AI Innovation Award</li>
    <li>AI for Enterprise Solutions</li>
    <li>AI in Healthcare Innovation</li>
    <li>Generative AI Startup Excellence</li>
    <li>AI for Sustainability Award</li>
    <li>Ethical AI Innovation by a Startup</li>
    <li>AI for Social Impact</li>
    <li>Human-Centered AI Design Award</li>
    <li>AI-Powered Platform Innovation</li>
    <li>Outstanding AI Research Commercialization</li>
    <li>Emerging Startup in AI Infrastructure</li>
    <li>Explainable AI Champion Startup</li>
    <li>Fastest Growing AI Startup</li>
    <li>Global Impact by an AI Startup</li>
    <li>AI IP and Patents Excellence Award</li>
    <li>AI Talent Development by a Startup</li>
    <li>Emerging AI Entrepreneur of the Year</li>
  </ul>
</section>

<section id="leadership">
  <h2>AI Leadership awards (18 categories)</h2>
  <p>For individuals leading AI strategy, policy, research and adoption.</p>
  <ul>
    <li>AI Leader of the Year</li>
    <li>AI Thought Leadership Award</li>
    <li>AI Policy Visionary Award</li>
    <li>AI Innovator in Public Sector</li>
    <li>Chief AI Officer of the Year</li>
    <li>AI Academic Leader</li>
    <li>AI Governance Champion</li>
    <li>Global AI Influencer Award</li>
    <li>AI Startup Leader of the Year</li>
    <li>AI & Ethics Champion</li>
    <li>Corporate AI Strategy Leader</li>
    <li>AI for Inclusion & Accessibility Advocate</li>
    <li>AI Talent Development Champion</li>
    <li>AI & Data Privacy Leadership Award</li>
    <li>Visionary AI Educator</li>
    <li>AI R&D Leadership Award</li>
    <li>Public-Private AI Collaboration Leader</li>
    <li>AI-Powered Cybersecurity Leader</li>
  </ul>
</section>
</div>

<!-- HOW ENTRIES ARE JUDGED (original copy, based on what the nomination form asks for) -->
<section aria-labelledby="judging-h">
  <h2 id="judging-h">How entries are judged</h2>
  <p>The World AI Awards jury assesses each entry on the evidence in the nomination form and the supporting documents. Jurors look at four things:</p>
  <ol>
    <li><strong>The problem and who benefits.</strong> What the AI solution or initiative sets out to solve, and the customers, employees or citizens it helps.</li>
    <li><strong>Results you can show.</strong> Measurable outcomes since launch, backed by data, documents or references.</li>
    <li><strong>Scale.</strong> How widely the work is deployed today, and a credible plan to take it further.</li>
    <li><strong>Investment and partnerships.</strong> The resources committed, and the stakeholders and technology partners involved.</li>
  </ol>
  <p>PLACEHOLDER_JUDGING_PROCESS</p>
</section>

<!-- PAST JURY & 2025 HONOUREES -->
<section aria-labelledby="past-h">
  <h2 id="past-h">Past jury and 2025 honourees</h2>
  <h3>2025 jury (titles as listed in 2025)</h3>
  <ul>
    <li><strong>Dr. Ravi Gupta</strong>, Editor-in-Chief, Digital Learning Magazine; Founder, Publisher and CEO, Elets Technomedia Pvt. Ltd.</li>
    <li><strong>Manish Bhardwaj, IAS</strong>, Deputy Director General, Unique Identification Authority of India, Government of India</li>
    <li><strong>Deepak Sharma</strong>, Tech Entrepreneur and CXO Advisor; Independent Director, Suryoday Small Finance Bank</li>
  </ul>
  <p>The 2026 jury: PLACEHOLDER_2026_JURY</p>
  <h3>Selected 2025 honourees</h3>
  <p>The 2025 awards were presented at World AI Summit 2025 in Bengaluru on 25 September 2025.</p>
  <ul>
    <li>Qualitrix: AI Validation & Testing Excellence</li>
    <li>Syngenta Group, "Cropwise Grower - AI Chatbot for Smallholder Farmers": AI-Enabled Conversational & Voice Assistance</li>
    <li>Altio AI Pvt Ltd: Most Promising AI Startup</li>
    <li>Familywala Eshop Pvt Ltd: Ethical AI Innovation by a Startup</li>
    <li>Purview Services, Hyderabad: AI for Inclusion & Accessibility Advocate</li>
    <li>Deepti Shibad, Crisil Corporate Technology: Business Transformation and Innovation Award</li>
  </ul>
  <p><a href="PLACEHOLDER_2025_WINNERS_URL">See all 2025 winners</a> · <a href="/1st-edition/awards.html">2025 awards archive</a></p>
</section>

<!-- NOMINATION FORM -->
<section id="nominate" aria-labelledby="nominate-h">
  <h2 id="nominate-h">Nominate for the World AI Awards 2026</h2>
  <p>Nominations close on PLACEHOLDER_NOMINATION_DEADLINE. Entries start at Rs 30,000 + GST.</p>
  <h3>How to nominate</h3>
  <ol>
    <li>Sign up or log in.</li>
    <li>Select your category.</li>
    <li>Fill in the nomination form (one form per category).</li>
    <li>Upload supporting documents.</li>
    <li>Submit your entry.</li>
    <li>Pay the nomination fee.</li>
  </ol>
  <h3>Keep these ready</h3>
  <ul>
    <li>Project duration (MM/YYYY to MM/YYYY)</li>
    <li>A brief overview of the project</li>
    <li>The problem it solves and how people benefit</li>
    <li>How you have scaled it, or plan to</li>
    <li>Approximate budget or investment</li>
    <li>Key stakeholders and technology partners</li>
    <li>Supporting documents</li>
  </ul>
  <!-- EXISTING FORM MARKUP GOES HERE, UNCHANGED ("Select Sectors" ... "Upload Documents") -->
</section>

<!-- FAQ -->
<section aria-labelledby="faq-h">
  <h2 id="faq-h">Frequently asked questions</h2>

  <h3>What is the entry fee for the World AI Awards 2026?</h3>
  <p>Entries start at Rs 30,000 + GST per nomination. PLACEHOLDER_FEE_TIERS. You pay the fee online in the last step of the nomination.</p>

  <h3>What is the last date for nominations?</h3>
  <p>Nominations close on PLACEHOLDER_NOMINATION_DEADLINE.</p>

  <h3>Can I enter more than one category?</h3>
  <p>Yes. Submit a separate nomination form for each category you enter. PLACEHOLDER_MULTI_ENTRY_FEE_RULE</p>

  <h3>When and where are the awards presented?</h3>
  <p>At World AI Summit 2026, 14-15 October 2026, Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. The ceremony is on PLACEHOLDER_CEREMONY_DAY_AND_TIME.</p>

  <h3>Does the nomination fee include a summit pass?</h3>
  <p>PLACEHOLDER_PASS_INCLUDED_ANSWER. Delegate passes are on the <a href="/delegate/">delegate registration page</a>.</p>

  <h3>Who can be nominated?</h3>
  <p>Depending on the category: organisations of any size, government departments and agencies, startups, AI solution providers and individual leaders.</p>

  <h3>Who do I contact with questions?</h3>
  <p>Nominations: <a href="mailto:secretariat@worldaisummit.com">secretariat@worldaisummit.com</a>. Sponsorship and partnerships: <a href="mailto:partnerships@worldaisummit.com">partnerships@worldaisummit.com</a>. Delegate passes: <a href="mailto:registration@worldaisummit.com">registration@worldaisummit.com</a>.</p>
</section>

<p class="cta-strip">Attending World AI Summit 2026? <a href="/delegate/">See delegate passes</a>.</p>
</main>
```

---

## 3. JSON-LD (place before `</head>`; checked with a JSON parser)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Place",
      "@id": "https://www.worldaisummit.com/#venue",
      "name": "Sheraton Grand Bangalore Hotel at Brigade Gateway",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "26/1, Dr. Rajkumar Road, Malleswaram-Rajajinagar",
        "addressLocality": "Bengaluru",
        "addressRegion": "Karnataka",
        "postalCode": "560055",
        "addressCountry": "IN"
      }
    },
    {
      "@type": "Organization",
      "@id": "https://www.worldaisummit.com/#organizer",
      "name": "Elets Technomedia Pvt. Ltd.",
      "url": "https://eletsonline.com/",
      "email": "secretariat@worldaisummit.com"
    },
    {
      "@type": "Event",
      "@id": "https://www.worldaisummit.com/#event",
      "name": "World AI Summit 2026",
      "url": "https://www.worldaisummit.com/",
      "startDate": "2026-10-14",
      "endDate": "2026-10-15",
      "eventStatus": "https://schema.org/EventScheduled",
      "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
      "location": { "@id": "https://www.worldaisummit.com/#venue" },
      "organizer": { "@id": "https://www.worldaisummit.com/#organizer" },
      "image": ["PLACEHOLDER_EVENT_IMAGE_URL_1200x630"],
      "description": "World AI Summit 2026, organised by Elets Technomedia, on 14-15 October 2026 at the Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru.",
      "offers": {
        "@type": "Offer",
        "name": "Delegate pass",
        "url": "https://www.worldaisummit.com/delegate/",
        "price": "PLACEHOLDER_CURRENT_PASS_PRICE_INR",
        "priceCurrency": "INR",
        "availability": "https://schema.org/InStock"
      },
      "subEvent": { "@id": "https://www.worldaisummit.com/awards/#event" }
    },
    {
      "@type": "Event",
      "@id": "https://www.worldaisummit.com/awards/#event",
      "name": "World AI Awards 2026",
      "url": "https://www.worldaisummit.com/awards/",
      "description": "The World AI Awards 2026 recognise real-world applications of artificial intelligence across 96 categories for enterprises, government, startups and AI leaders. Winners are honoured at World AI Summit 2026 in Bengaluru.",
      "startDate": "2026-10-14",
      "endDate": "2026-10-15",
      "eventStatus": "https://schema.org/EventScheduled",
      "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
      "location": { "@id": "https://www.worldaisummit.com/#venue" },
      "organizer": { "@id": "https://www.worldaisummit.com/#organizer" },
      "image": ["PLACEHOLDER_AWARDS_IMAGE_URL_1200x630"],
      "superEvent": { "@id": "https://www.worldaisummit.com/#event" },
      "offers": {
        "@type": "Offer",
        "name": "Delegate pass",
        "url": "https://www.worldaisummit.com/delegate/",
        "price": "PLACEHOLDER_CURRENT_PASS_PRICE_INR",
        "priceCurrency": "INR",
        "availability": "https://schema.org/InStock"
      }
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "World AI Summit 2026", "item": "https://www.worldaisummit.com/" },
        { "@type": "ListItem", "position": 2, "name": "World AI Awards 2026", "item": "https://www.worldaisummit.com/awards/" }
      ]
    }
  ]
}
</script>
```
Notes:
- **Price:** replace PLACEHOLDER_CURRENT_PASS_PRICE_INR with a plain number such as "30000". Leave out commas and the Rs sign.
- **Performers:** `performer` is deliberately left out. No 2026 awards presenter or jury member is verified, and the rule allows only verified speakers. The homepage schema should carry the verified 2026 speakers.
- **Offers:** the Event offer is the delegate pass only, as the rule requires. Do not add the nomination fee as an Event offer, because Google would show it as a ticket price.
- **FAQ:** FAQPage markup is not included because Google no longer shows FAQ rich results for event sites.

---

## 4. Redirect /award.html to /awards/ (301, one hop)

**Apache (.htaccess in the web root, above any existing rules):**
```apache
RewriteEngine On

# Old 2026 awards copy -> /awards/ (works for www and non-www in one hop; query string kept)
RewriteRule ^award\.html$ https://www.worldaisummit.com/awards/ [R=301,L]

# /awards without the trailing slash -> /awards/
RewriteRule ^awards$ https://www.worldaisummit.com/awards/ [R=301,L]

# Only if non-www is NOT already redirected at server level (check: curl -I https://worldaisummit.com/awards/)
RewriteCond %{HTTP_HOST} ^worldaisummit\.com$ [NC]
RewriteRule ^(.*)$ https://www.worldaisummit.com/$1 [R=301,L]
```

**nginx:**
```nginx
# Inside the existing server block for www.worldaisummit.com (443)
location = /award.html { return 301 https://www.worldaisummit.com/awards/$is_args$args; }
location = /awards     { return 301 https://www.worldaisummit.com/awards/$is_args$args; }

# Non-www host: add the award.html line inside the existing block, or use this block if none exists
server {
    listen 80;
    listen 443 ssl;
    server_name worldaisummit.com;
    # ssl_certificate / ssl_certificate_key: keep the existing lines
    location = /award.html { return 301 https://www.worldaisummit.com/awards/$is_args$args; }
    location / { return 301 https://www.worldaisummit.com$request_uri; }
}
```
After the change, `curl -sI https://www.worldaisummit.com/award.html` and `curl -sI https://worldaisummit.com/award.html` should each return a single `301` with `Location: https://www.worldaisummit.com/awards/`. Reload nginx with `nginx -t && systemctl reload nginx`.

---

## 5. Internal links (/awards/ has only 4 internal links today and no nav link)

```html
<!-- Main nav, all pages -->
<a href="/awards/">Awards</a>

<!-- Homepage awards section CTA -->
<a class="btn" href="/awards/">Nominate for the World AI Awards 2026</a>

<!-- Footer, all pages -->
<a href="/awards/">World AI Awards 2026</a>

<!-- /delegate/ (below the pass table) -->
<p>Entering the World AI Awards 2026? <a href="/awards/">See categories, fee and how to nominate</a>.</p>

<!-- /ai-conference-bengaluru-2026.html (in the awards or agenda paragraph) -->
<a href="/awards/">World AI Awards 2026 categories and nominations</a>

<!-- /1st-edition/awards.html (top banner on the 2025 archive) -->
<p class="notice">This is the 2025 awards page. <a href="/awards/">Nominations for the World AI Awards 2026 are open</a>.</p>
```
Also change every existing `href` that points to `/award.html` so that it points to `/awards/`.

---

## 6. Sitemap

- Make sure `https://www.worldaisummit.com/awards/` has `<lastmod>2026-10-01</lastmod>` (use the actual deploy date).
- Remove `https://www.worldaisummit.com/award.html` from the sitemap.
