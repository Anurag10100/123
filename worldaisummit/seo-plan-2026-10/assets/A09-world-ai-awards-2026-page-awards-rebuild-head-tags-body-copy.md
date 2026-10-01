# A09: World AI Awards 2026 page: /awards/ rebuild (head tags, body copy, Event JSON-LD, one-hop 301s)

- **For recommendation:** /awards/ gets 1,300 impressions but a 2.5% click rate: add nomination details (categories, fee, deadline) and a 'Nominations Open' title and H1
- **Research lens:** site-deep-read
- **Format:** HTML for the head and body of /awards/, a JSON-LD block, Apache .htaccess and nginx redirect rules, and curl checks
- **Placeholders the business must fill:**
  - PLACEHOLDER_NOMINATION_DEADLINE (needed before launch; appears in the hero, Key dates and FAQ)
  - PLACEHOLDER_FEE_TIERS (confirm 'from Rs 30,000 + GST' and give any 2026 tiers; in 2025 there were two tiers)
  - PLACEHOLDER_CEREMONY_DAY_AND_TIME (14 or 15 Oct 2026, and the time)
  - PLACEHOLDER_JURY_REVIEW_DATES
  - PLACEHOLDER_SELF_NOMINATION_RULE (can organisations nominate themselves, and can a third party nominate someone?)
  - PLACEHOLDER_JURY_2026 (2026 jury names, if they can be published; otherwise delete the paragraph)
  - PLACEHOLDER_2025_WINNERS_LIST (or a link to a winners page; not on /1st-edition/awards.html)
  - PLACEHOLDER_NOMINEE_PASS_POLICY (do nominees or winners get delegate passes?)
  - PLACEHOLDER_AWARDS_CONTACT_EMAIL (an awards inbox; the site's role inboxes are secretariat@, partnerships@ and registration@)
  - PLACEHOLDER_CURRENT_PASS_PRICE_INR (current delegate pass price as a number for the JSON-LD; Standard ended 30 Sept 2026, Late Access was listed at Rs 30,000/60,000)
  - PLACEHOLDER_EVENT_IMAGE_URL (absolute URL of a 1200px+ awards or summit image)

## How to ship

Ship order matters, because /award.html is the only live 2026 page that lists the categories:
1. The awards team fills in the PLACEHOLDER_ values. Must have before launch: the nomination deadline, the 2026 fee tiers (confirm "from Rs 30,000 + GST"), and the ceremony day and time. They should also confirm the FAQ answer that each award entered needs its own form and fee. It is based on "Fill Out Nomination Form(s)" on /award.html and "per entry" in the 2025 checkout. The other placeholders can follow later. Delete any optional placeholder paragraph that is still empty at launch instead of publishing the marker.
2. Web dev publishes Parts A, B and C on https://www.worldaisummit.com/awards/. Replace the theme H1 with the new H1 and keep the theme as a line of text. Wrap the existing form in #nominate and demote "Select Sectors" to an H3. Remove the old Event JSON-LD. Validate the new block in the Rich Results Test before going live; the price placeholder has to be a real number by then.
3. Only after step 2 is live, deploy Part D (Apache or nginx, whichever the host runs). Run the curl checks to confirm there is one 301 and then a 200.
4. Internal links, all pointing to /awards/:
   - homepage hero: "Nominate for the World AI Awards 2026"
   - homepage awards block
   - main navigation: "Awards"
   - /delegate/: "Entering the World AI Awards 2026? See categories and fees"
   - "Beyond the Hype" blog post: link its existing "World AI Awards 2026" mention
   - /1st-edition/awards.html: a short banner, "Nominations for the 2026 World AI Awards are open"
5. Search Console: the connected property (URL-prefix https://worldaisummit.com/) cannot inspect or submit the www URL. Ask whoever controls DNS to add a Domain property (DNS TXT record), or a www URL-prefix property. Then request indexing of https://www.worldaisummit.com/awards/. Until that is done, the click-rate change cannot be measured in the connected property, because the old URL's impressions will move to the www URL.
6. If the deadline is before about 8 Oct, consider adding it to the title, for example "World AI Awards 2026: Nominations Close [date] | AI Awards", so it shows in the snippet. The direct competitor Cypher already shows "Nominate now" with dates in its snippet.

Notes on the copy:
- The recommended H2 "2025 winners" was changed to "The 2025 World AI Awards". /1st-edition/awards.html lists the past jury but no winners, so a winners list needs PLACEHOLDER_2025_WINNERS_LIST from the awards team.
- The 4-step "How to nominate" was replaced by the existing 6-step flow from /award.html, which includes paying the fee.
- The fee shown is "from Rs 30,000 + GST" (from /award.html), not the 2025 figure of Rs 18,000.
- The page does not name an edition number because the sources disagree (2nd or 3rd).
- FAQPage markup is left out on purpose: FAQ rich results are limited to government and health sites, so it adds nothing here.

Sources (fetched or checked 1 Oct 2026):
- https://www.worldaisummit.com/award.html: categories, "Entries from 30k + GST", 6 steps, "5+ Distinguished Jury Members"
- https://www.worldaisummit.com/1st-edition/awards.html: 2025 dates and past jury
- https://www.worldaisummit.com/awards/: current form fields
- https://www.worldaisummit.com/assets/speaker_details/index.html: "Confirmed 2026" status for the five performers
- https://www.marriott.com/en-us/hotels/blrgs-sheraton-grand-bangalore-hotel-at-brigade-gateway/overview/ and the hotelplanner listing: venue address
- 2025 fee tiers: elets.net/worldaisummit-awards/, as reported by the verifier

On the relayed user question ("do you have more CPUs?"): this sub-agent's container reports 4 CPUs (nproc). It cannot add more.

## Content

<!-- =====================================================================
 PART A. <head> of https://www.worldaisummit.com/awards/
 Lengths checked: title 56 chars, meta description 147 chars, H1 38 chars.
 ===================================================================== -->
<title>World AI Awards 2026: Nominations Open | AI Awards India</title>
<meta name="description" content="Nominations open for World AI Awards 2026, presented at World AI Summit, Bengaluru, 14-15 Oct. Categories, entry fee, deadline and how to nominate.">
<link rel="canonical" href="https://www.worldaisummit.com/awards/">
<meta property="og:type" content="website">
<meta property="og:url" content="https://www.worldaisummit.com/awards/">
<meta property="og:title" content="World AI Awards 2026: Nominations Open">
<meta property="og:description" content="Nominations open for World AI Awards 2026, presented at World AI Summit, Bengaluru, 14-15 Oct. Categories, entry fee, deadline and how to nominate.">

<!-- =====================================================================
 PART B. Body. This replaces the current theme H1 and goes above the existing form.
 Category list, the 6 nomination steps, benefit lines and the "from 30k + GST" fee
 come from the live /award.html (Exa fetch, 1 Oct 2026). The past jury comes from
 /1st-edition/awards.html. Merge this into /awards/ FIRST, then turn on the 301s in Part D.
 ===================================================================== -->
<main id="world-ai-awards">

<section class="awards-hero">
  <p class="eyebrow">World AI Summit 2026 &middot; 14-15 October 2026 &middot; Bengaluru</p>
  <h1>World AI Awards 2026: Nominations Open</h1>
  <p>The World AI Awards recognise real-world uses of artificial intelligence that are moving industries forward, improving public services and setting new standards for innovation. The 2026 awards will be presented at World AI Summit 2026 on 14-15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. Elets Technomedia organises the summit.</p>
  <ul class="awards-facts">
    <li><strong>75+ awards</strong> in 6 category groups</li>
    <li><strong>Entries from Rs 30,000 + GST</strong></li>
    <li><strong>Last date to nominate:</strong> PLACEHOLDER_NOMINATION_DEADLINE</li>
  </ul>
  <p><a class="btn btn-primary" href="#nominate">Start your nomination</a></p>
  <p class="theme">Summit theme: AI for All: Accelerating India's Journey Towards Inclusive, Responsible and Future-Ready AI</p>
</section>

<section id="key-dates">
  <h2>Key dates</h2>
  <table>
    <thead><tr><th scope="col">Stage</th><th scope="col">Date</th></tr></thead>
    <tbody>
      <tr><td>Nominations</td><td>Open now</td></tr>
      <tr><td>Last date to nominate</td><td>PLACEHOLDER_NOMINATION_DEADLINE</td></tr>
      <tr><td>Jury review</td><td>PLACEHOLDER_JURY_REVIEW_DATES</td></tr>
      <tr><td>Awards ceremony</td><td>PLACEHOLDER_CEREMONY_DAY_AND_TIME (14 or 15 October 2026), Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru</td></tr>
    </tbody>
  </table>
</section>

<section id="categories">
  <h2>Award categories</h2>
  <p>The awards are grouped under six categories. Choose the award that fits your work best. You can enter more than one award, with one form for each entry.</p>

  <h3>1. AI Enterprise &amp; Application (26 awards)</h3>
  <ul>
    <li>AI for Immersive Content Experience</li>
    <li>AI in Workforce Enablement Award</li>
    <li>AI-Powered Algorithms for Media &amp; Entertainment</li>
    <li>AI in Robotics Utilization &amp; Machine Learning</li>
    <li>Best AI Integration in Gaming Experience</li>
    <li>AI Use in Navigation &amp; Travel Assistance</li>
    <li>AI in Learning &amp; Skill Development</li>
    <li>AI in Recruitment, Screening &amp; Evaluation</li>
    <li>AI-Powered Data Safeguard &amp; Privacy Award</li>
    <li>AI in Retail Buying &amp; Forecasting</li>
    <li>AI in Aerospace &amp; Allied Services</li>
    <li>AI in Banking &amp; Process Automation</li>
    <li>Best Use of AI in Automotive &amp; Ancillary Industries</li>
    <li>AI-Enabled Crop Insights &amp; Weather Prediction</li>
    <li>AI in Health &amp; Pharma Intervention</li>
    <li>Intelligent Marketing Optimization Award</li>
    <li>AI-Enabled Conversational &amp; Voice Assistance</li>
    <li>AI for Enhanced Supply Chain Management</li>
    <li>Smart AI Workforce Optimization Award</li>
    <li>Best Use of AI in Logistics &amp; Distribution</li>
    <li>AI for Mobility Enhancement &amp; Transit</li>
    <li>AI in Product Development &amp; Innovation</li>
    <li>AI-Powered Financial Decision-Making</li>
    <li>AI for Risk &amp; Compliance Management</li>
    <li>AI Implementation in E-commerce Operations &amp; Insights</li>
    <li>AI Innovation in Cybersecurity</li>
  </ul>

  <h3>2. Business Transformation &amp; Innovation (13 awards)</h3>
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

  <h3>3. Smart Tech &amp; AI Engineering (16 awards)</h3>
  <ul>
    <li>Conversational AI &amp; NLP Excellence</li>
    <li>Customer Experience AI Solution of the Year</li>
    <li>Computer Vision &amp; Network Monitoring Award</li>
    <li>Intelligent Data Management Solution</li>
    <li>AI Strategy &amp; Consulting Firm of the Year</li>
    <li>AI Transformation Award in Audio &amp; Visual Creation</li>
    <li>Best AI-Powered SaaS Product</li>
    <li>Best Enterprise AI Platform of the Year</li>
    <li>Best AI Innovation in DeepTech</li>
    <li>Best Use of AI in Threat Detection &amp; Insights</li>
    <li>Cloud AI Service Provider of the Year</li>
    <li>Predictive Intelligence Solution of the Year</li>
    <li>AI Innovation for Industry Applications</li>
    <li>AI Deployment &amp; Marketplace Enabler</li>
    <li>AI Validation &amp; Testing Excellence</li>
    <li>AI Development &amp; Implementation Award (GPS, Product Design, Last-Mile Delivery, Robotics, Surveillance Tech, Self-Driven Cars, Chatbots, VR)</li>
  </ul>

  <h3>4. AI in Governance (4 awards)</h3>
  <ul>
    <li>AI for Public Service Delivery Excellence</li>
    <li>Outstanding Citizen Engagement Initiative</li>
    <li>Data-Driven Governance Award</li>
    <li>AI for E-Governance Initiatives</li>
  </ul>

  <h3>5. AI Startups (19 awards)</h3>
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

  <h3>6. AI Leadership (18 awards)</h3>
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
    <li>AI &amp; Ethics Champion</li>
    <li>Corporate AI Strategy Leader</li>
    <li>AI for Inclusion &amp; Accessibility Advocate</li>
    <li>AI Talent Development Champion</li>
    <li>AI &amp; Data Privacy Leadership Award</li>
    <li>Visionary AI Educator</li>
    <li>AI R&amp;D Leadership Award</li>
    <li>Public-Private AI Collaboration Leader</li>
    <li>AI-Powered Cybersecurity Leader</li>
  </ul>

  <p><a class="btn btn-primary" href="#nominate">Start your nomination</a></p>
</section>

<section id="who-can-nominate">
  <h2>Who can nominate</h2>
  <p>The awards are open to organisations and individuals who have put AI to work:</p>
  <ul>
    <li><strong>Enterprises</strong> using AI in operations, products or customer service: AI Enterprise &amp; Application, and Business Transformation &amp; Innovation.</li>
    <li><strong>Technology companies and solution providers</strong> building AI platforms, products and services: Smart Tech &amp; AI Engineering.</li>
    <li><strong>Government departments and public bodies</strong> delivering AI-led public services: AI in Governance.</li>
    <li><strong>Startups</strong> at any stage: AI Startups.</li>
    <li><strong>Individual leaders</strong>, including CXOs, public servants, academics and founders: AI Leadership.</li>
  </ul>
  <p>PLACEHOLDER_SELF_NOMINATION_RULE</p>
</section>

<section id="entry-fee">
  <h2>Entry fee</h2>
  <p>Entries start from <strong>Rs 30,000 + GST per entry</strong>. PLACEHOLDER_FEE_TIERS</p>
  <p>You pay the fee online after you submit your entry. It is the last step of the nomination.</p>
  <!-- Internal note, delete before publishing: the 2025 checkout (elets.net/worldaisummit-awards/) had two tiers, Rs 18,000 + GST for Startup & Individual and Rs 20,000 + GST for Enterprise, Government, Leadership and Solution Provider. The 2026 /award.html says "Entries from 30k + GST". Confirm the 2026 tiers before going live. -->
</section>

<section id="how-winners-are-chosen">
  <h2>How winners are chosen</h2>
  <p>A jury of 5+ leaders from industry and government reviews every entry. The jury assesses what you submit in the nomination form:</p>
  <ul>
    <li>an overview of the project or innovation, and how long it has run</li>
    <li>the problem it solves and who benefits</li>
    <li>how it has scaled, or how you plan to scale it</li>
    <li>the approximate budget or investment</li>
    <li>the key stakeholders and technology partners involved</li>
    <li>supporting documents</li>
  </ul>
  <p>PLACEHOLDER_JURY_2026</p>
</section>

<section id="how-to-nominate">
  <h2>How to nominate: 6 steps</h2>
  <ol>
    <li><strong>Sign up or log in.</strong></li>
    <li><strong>Choose your category.</strong> Pick the award that best fits your work.</li>
    <li><strong>Fill in the nomination form.</strong> Use one form for each award you enter.</li>
    <li><strong>Upload supporting documents.</strong> Case studies, results and media coverage help the jury.</li>
    <li><strong>Submit your entry.</strong></li>
    <li><strong>Pay the nomination fee.</strong> It starts from Rs 30,000 + GST per entry.</li>
  </ol>
  <p><a class="btn btn-primary" href="#nominate">Start your nomination</a></p>
</section>

<section id="2025-edition">
  <h2>The 2025 World AI Awards</h2>
  <p>The 2025 World AI Awards were presented at World AI Summit 2025, held on 25-26 September 2025 at Sheraton Grand Brigade Gateway, Bengaluru. The 2025 jury included:</p>
  <ul>
    <li>Dr Ravi Gupta, Founder, Publisher and CEO, Elets Technomedia</li>
    <li>Manish Bhardwaj, IAS, Deputy Director General, Unique Identification Authority of India</li>
    <li>Deepak Sharma, Independent Director, Suryoday Small Finance Bank</li>
  </ul>
  <p>PLACEHOLDER_2025_WINNERS_LIST</p>
  <p><a href="/1st-edition/awards.html">See the 2025 awards page</a></p>
</section>

<section id="faq">
  <h2>FAQ</h2>

  <h3>What is the last date to nominate?</h3>
  <p>The last date is PLACEHOLDER_NOMINATION_DEADLINE. Entries that arrive after this date are not reviewed.</p>

  <h3>Can I enter more than one category?</h3>
  <p>Yes. Fill in a separate form for each award you enter. The fee applies to each entry.</p>

  <h3>Can startups enter?</h3>
  <p>Yes. The AI Startups category has 19 awards, including AI Startup of the Year, Most Promising AI Startup and Fastest Growing AI Startup. Founders can also enter AI Leadership awards such as AI Startup Leader of the Year.</p>

  <h3>Can government departments enter?</h3>
  <p>Yes. The AI in Governance category covers public service delivery, citizen engagement, data-driven governance and e-governance. Public-sector leaders can also enter AI Leadership awards such as AI Innovator in Public Sector and AI Policy Visionary Award.</p>

  <h3>Is there a jury?</h3>
  <p>Yes. A jury of 5+ leaders from industry and government reviews every entry. See <a href="#how-winners-are-chosen">How winners are chosen</a>.</p>

  <h3>Do nominees get delegate passes?</h3>
  <p>PLACEHOLDER_NOMINEE_PASS_POLICY. Delegate passes for World AI Summit 2026 are available on the <a href="/delegate/">delegate pass page</a>.</p>

  <h3>When and where are the awards presented?</h3>
  <p>The awards will be presented at World AI Summit 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, 26/1 Dr Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru 560055. Ceremony: PLACEHOLDER_CEREMONY_DAY_AND_TIME.</p>

  <h3>Whom do I contact with questions?</h3>
  <p>Write to PLACEHOLDER_AWARDS_CONTACT_EMAIL.</p>
</section>

<!-- Wrap the EXISTING form in this section. Change its current "Select Sectors" H2 to an H3 so the
     heading order is H1 > H2 > H3, which fixes the audit's heading-order-skip. Leave the form fields as they are. -->
<section id="nominate" aria-labelledby="nominate-heading">
  <h2 id="nominate-heading">Submit your nomination</h2>
  <!-- existing form starts here: <h3>Select your category</h3> ... Project/Innovation Details ... Applicant Details ... Upload Documents -->
</section>

</main>

<!-- =====================================================================
 PART C. JSON-LD. Put this in <head> and DELETE the current Event markup on /awards/.
 Search Console flags that markup for missing performer, offers and organizer.
 Address source: Marriott hotel listing and hotel aggregators (26/1 Dr Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru 560055).
 Performers: only people marked "Confirmed 2026" on /assets/speaker_details/index.html (checked 1 Oct 2026).
 ===================================================================== -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Event",
  "@id": "https://www.worldaisummit.com/awards/#event",
  "name": "World AI Awards 2026 at World AI Summit 2026",
  "description": "The World AI Awards 2026 recognise real-world applications of AI across 75+ awards in six categories: AI Enterprise & Application, Business Transformation & Innovation, Smart Tech & AI Engineering, AI in Governance, AI Startups and AI Leadership. The awards are presented at World AI Summit 2026 in Bengaluru.",
  "url": "https://www.worldaisummit.com/awards/",
  "startDate": "2026-10-14",
  "endDate": "2026-10-15",
  "eventStatus": "https://schema.org/EventScheduled",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
  "inLanguage": "en-IN",
  "image": [
    "PLACEHOLDER_EVENT_IMAGE_URL"
  ],
  "location": {
    "@type": "Place",
    "name": "Sheraton Grand Bangalore Hotel at Brigade Gateway",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "26/1, Dr Rajkumar Road, Malleswaram-Rajajinagar",
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
  "performer": [
    {
      "@type": "Person",
      "name": "Pankaj Kumar Pandey",
      "jobTitle": "Principal Secretary, e-Governance, Karnataka",
      "worksFor": { "@type": "GovernmentOrganization", "name": "Government of Karnataka" }
    },
    {
      "@type": "Person",
      "name": "T Bhoobalan",
      "jobTitle": "CEO, Centre for e-Governance, Karnataka",
      "worksFor": { "@type": "GovernmentOrganization", "name": "Government of Karnataka" }
    },
    {
      "@type": "Person",
      "name": "Sanjeev Gupta",
      "jobTitle": "CEO",
      "worksFor": { "@type": "Organization", "name": "Karnataka Digital Economy Mission" }
    },
    {
      "@type": "Person",
      "name": "Ram Mohan Rao",
      "jobTitle": "Executive Director",
      "worksFor": { "@type": "GovernmentOrganization", "name": "Securities and Exchange Board of India" }
    },
    {
      "@type": "Person",
      "name": "Shalini Kapoor",
      "jobTitle": "Chief Strategist, Data and AI",
      "worksFor": { "@type": "Organization", "name": "EkStep Foundation" }
    }
  ],
  "offers": {
    "@type": "Offer",
    "name": "World AI Summit 2026 delegate pass",
    "url": "https://www.worldaisummit.com/delegate/",
    "price": "PLACEHOLDER_CURRENT_PASS_PRICE_INR",
    "priceCurrency": "INR",
    "availability": "https://schema.org/InStock",
    "validFrom": "2026-10-01"
  }
}
</script>

# =====================================================================
# PART D. Redirects. Turn these on ONLY after Part B is live on /awards/.
# Goal: every old URL reaches https://www.worldaisummit.com/awards/ in ONE 301.
# Audit c1b16b55 shows non-www /awards currently 301s to https://www.worldaisummit.com/awards
# (no slash), which then needs a second hop to /awards/. These rules remove that chain.
# =====================================================================

# ---------- Apache (.htaccess in the document root) ----------
# Put these ABOVE the existing non-www -> www rule. If the non-www host has its own
# vhost or docroot, add the same block there too.
RewriteEngine On

RewriteCond %{HTTP_HOST} ^(www\.)?worldaisummit\.com$ [NC]
RewriteRule ^award\.html$ https://www.worldaisummit.com/awards/ [R=301,L]

RewriteCond %{HTTP_HOST} ^(www\.)?worldaisummit\.com$ [NC]
RewriteRule ^awards$ https://www.worldaisummit.com/awards/ [R=301,L]

# Existing host rule stays below, for example:
# RewriteCond %{HTTP_HOST} ^worldaisummit\.com$ [NC]
# RewriteRule ^(.*)$ https://www.worldaisummit.com/$1 [R=301,L]

# ---------- nginx ----------
# 1) server block for https://www.worldaisummit.com
location = /award.html { return 301 https://www.worldaisummit.com/awards/; }
location = /awards     { return 301 https://www.worldaisummit.com/awards/; }

# 2) server block(s) for worldaisummit.com (ports 80 and 443) and http://www.worldaisummit.com
#    A server-level "return 301 ...$request_uri;" runs before location matching. Move it into location /:
location = /award.html { return 301 https://www.worldaisummit.com/awards/; }
location = /awards     { return 301 https://www.worldaisummit.com/awards/; }
location /             { return 301 https://www.worldaisummit.com$request_uri; }

# ---------- Checks: each line should show ONE 301, then 200 at https://www.worldaisummit.com/awards/ ----------
# curl -sIL https://worldaisummit.com/awards       | grep -iE '^(HTTP|location)'
# curl -sIL https://worldaisummit.com/award.html   | grep -iE '^(HTTP|location)'
# curl -sIL https://www.worldaisummit.com/award.html | grep -iE '^(HTTP|location)'
# curl -sIL https://www.worldaisummit.com/awards   | grep -iE '^(HTTP|location)'
# curl -sIL http://worldaisummit.com/awards        | grep -iE '^(HTTP|location)'
