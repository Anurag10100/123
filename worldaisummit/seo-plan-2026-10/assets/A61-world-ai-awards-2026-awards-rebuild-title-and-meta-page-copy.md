# A61: World AI Awards 2026: /awards/ rebuild (title and meta, page copy with all 96 awards, /award.html 301, corrected Event JSON-LD)

- **For recommendation:** Rebuild /awards/ as the one indexable awards hub: put the 75+ categories in heading text, add fee, deadline and how-to-nominate, retire /award.html, and rewrite the title for clicks
- **Research lens:** awards
- **Format:** Static HTML: a head block, body sections to place above the existing nomination form, one JSON-LD script, and Apache and nginx redirect snippets. Plain text with code blocks, ready to paste.
- **Placeholders the business must fill:**
  - PLACEHOLDER_DEADLINE / PLACEHOLDER_DEADLINE_DD: 2026 nomination last date (none published anywhere)
  - PLACEHOLDER_CEREMONY_DATE: awards ceremony date, 14 or 15 Oct 2026, and the time
  - PLACEHOLDER_NOMINATION_FEE_2026: per-entry fee by entrant type; award.html says 'from 30k + GST', 2025 was Rs 18,000 or Rs 20,000 + GST
  - PLACEHOLDER_PASS_INCLUDED: whether the nomination fee includes a delegate pass (2025 checkout bundled one)
  - PLACEHOLDER_MULTIPLE_ENTRIES_POLICY: whether one organisation can enter several awards, and whether the fee is charged per entry
  - PLACEHOLDER_AWARDS_CONTACT_EMAIL: which inbox handles award questions (secretariat@, registration@ or partnerships@worldaisummit.com)
  - PLACEHOLDER_JURY_NAMES_AND_CRITERIA: jury members and judging criteria; only '5+ jury members' is published
  - PLACEHOLDER_WINNERS_2025_URL: no /awards/winners-2025/ page found; build it, link to the 10 Oct 2025 LinkedIn post, or remove the link
  - PLACEHOLDER_LATE_ACCESS_CONFIRM: confirm Late Access Rs 30,000 / Rs 60,000 is live from 1 Oct, whether GST is extra, and that passes are still available (InStock); otherwise drop the price fields

## How to ship

Owner: web dev, 2-4 hours. Fill in the placeholders first. Aim to publish by 3 Oct 2026.

1. Placeholders that need a business decision. Get these from the awards and registration team:
   - The 2026 nomination deadline.
   - The ceremony date (14 or 15 Oct).
   - The fee per entry for each type of entrant. award.html currently says 'Entries from 30k + GST'. In 2025 it was Rs 18,000 + GST for startups and individuals, and Rs 20,000 + GST for enterprise, government, leadership and solution providers (elets.net/worldaisummit-awards/).
   - Whether the fee includes a delegate pass. The 2025 checkout bundled a 'Conference Attendee Pass INR 30000'.
   - The rule on entering more than one award.
   - The contact email for awards questions.
   - The jury names and judging criteria. award.html says only '5+ Distinguished Jury Members'.
   - Whether the Late Access prices are live, and whether GST is extra.
   - The URL of the 2025 winners list. I could not find a /awards/winners-2025/ page. The full 2025 list is in Elets' LinkedIn post of 10 Oct 2025. Either build that page, link to the post, or drop the link.
   If no deadline is set yet, use the 'Entries open now.' version of the meta.

2. Paste the head block. Put the body sections above the existing form and wrap the form in id="nominate". Replace the existing Event JSON-LD with the block above, then check it in the Rich Results Test.

3. Add the /award.html 301 (Apache or nginx), fix the internal links and the sitemap, and add a homepage link to /awards/.

4. Recrawl. The Search Console property is the non-www URL-prefix property only. It cannot inspect or request indexing for the www /awards/ page, and requesting the non-www URL may only recrawl the redirect. Whoever owns Search Console should add a Domain property (DNS TXT record) and then request indexing for https://www.worldaisummit.com/awards/. Until then, the sitemap lastmod and the new homepage link are the main recrawl signals.

Sources and corrections that apply:
- Award list, '75+', '5+ jury', benefits and the 6 steps come from an Exa read of www.worldaisummit.com/award.html on 1 Oct. The six groups hold 26/13/16/4/19/18 awards, 96 in total.
- Late Access prices (Rs 30,000 Premium, Rs 60,000 VIP) and the Standard tier ending 30 Sept 2026 come from an Exa read of /delegate/ on 1 Oct.
- The venue address, 26/1 Dr. Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru, Karnataka 560055, comes from Google Hotels and Apple Maps listings.
- The 2025 ceremony date (25 Sept 2025) and the named winners come from Elets' LinkedIn post of 10 Oct 2025 and qualitrix.com.
- The 301 is justified because two pages carry the same content. The claim that award.html's canonical points to the homepage was not re-verified, so it is not the reason given.
- The new title and the FAQ that separates this programme from worldawards.ai may still not win clicks on 'world ai awards', because many of those searchers want the other brand.
- The traffic gain is small and mostly outside India. India sent about 4 of roughly 19 baseline clicks in the window. The case for the change is more nominations from visitors who now see the categories, fee and deadline.
- Fixing the Event schema warnings will not change rankings.
- worldaisummit.com was blocked by this environment's proxy, so I could not read the raw HTML of the current /awards/ JSON-LD or check whether /awards/winners-2025/ exists.
- Separate issue in the local repo: worldaisummit/speakers/speakers.json still has pass_price_inr 20000 and pass_from 'Rs 20,000'. Update it before the speaker pages are built, or they will publish an expired price. I did not edit any files.

## Content

=== 1. HEAD (https://www.worldaisummit.com/awards/) ===

<title>World AI Awards 2026 | Nominations Open, Bengaluru 14-15 Oct</title>
<meta name="description" content="Nominate for World AI Awards 2026 at World AI Summit Bengaluru, 14-15 Oct. 96 awards for enterprises, startups, government and AI leaders. Last date PLACEHOLDER_DEADLINE_DD Oct.">
<link rel="canonical" href="https://www.worldaisummit.com/awards/">

Meta length: 156 characters once the date is filled in. If no deadline is set yet, end the meta with "Entries open now." instead of the last-date sentence. It is still 156 characters.

After the deadline, switch to:
<title>World AI Awards 2026 Winners | World AI Summit Bengaluru</title>
<meta name="description" content="Winners of the World AI Awards 2026, presented at World AI Summit, Bengaluru on PLACEHOLDER_CEREMONY_DATE. 96 awards across enterprise, startups, government and leadership.">

Keep the URL /awards/ unchanged. Google already has it indexed.


=== 2. BODY (above the existing form; keep the form and give it id="nominate") ===

<h1>World AI Awards 2026: Nominations Open</h1>

<p>The World AI Awards recognise real-world applications of artificial intelligence in enterprises, government, startups and leadership. The 2026 awards will be presented at World AI Summit 2026 at the Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru, on PLACEHOLDER_CEREMONY_DATE. The summit runs on 14 and 15 October 2026. The awards are organised by Elets Technomedia. There are 96 awards in six groups, and nominations close on PLACEHOLDER_DEADLINE.</p>
<p><a href="#nominate">Start your nomination</a></p>

<h2>Entry fee and last date</h2>
<ul>
  <li><strong>Nomination fee:</strong> PLACEHOLDER_NOMINATION_FEE_2026 per entry</li>
  <li><strong>Last date for nominations:</strong> PLACEHOLDER_DEADLINE</li>
  <li><strong>Awards ceremony:</strong> PLACEHOLDER_CEREMONY_DATE, World AI Summit 2026, Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru</li>
  <li><strong>Delegate pass:</strong> PLACEHOLDER_PASS_INCLUDED</li>
  <li><strong>Questions about your entry:</strong> PLACEHOLDER_AWARDS_CONTACT_EMAIL</li>
</ul>

<h2>Award categories 2026</h2>
<p>There are 96 awards in six groups. Pick the award that best matches your project, organisation or role.</p>

<h3>AI Enterprise &amp; Application (26 awards)</h3>
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

<h3>Business Transformation &amp; Innovation (13 awards)</h3>
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

<h3>Smart Tech &amp; AI Engineering (16 awards)</h3>
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

<h3>AI in Governance (4 awards)</h3>
<ul>
  <li>AI for Public Service Delivery Excellence</li>
  <li>Outstanding Citizen Engagement Initiative</li>
  <li>Data-Driven Governance Award</li>
  <li>AI for E-Governance Initiatives</li>
</ul>

<h3>AI Startups (19 awards)</h3>
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

<h3>AI Leadership (18 awards)</h3>
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

<h2>Why enter</h2>
<ul>
  <li><strong>Global recognition:</strong> present your AI work to industry leaders and peers.</li>
  <li><strong>Credibility and trust:</strong> an independent mark of excellence that clients, partners and investors can see.</li>
  <li><strong>Business exposure:</strong> show your solution to enterprises, government bodies and the media.</li>
  <li><strong>Networking:</strong> meet decision-makers, technology leaders and AI policy makers at World AI Summit.</li>
  <li><strong>Investor and market access:</strong> use the award's visibility to reach investors and new markets.</li>
</ul>

<h2>How to nominate</h2>
<ol>
  <li><strong>Sign up or log in.</strong></li>
  <li><strong>Select your category</strong> from the six groups above.</li>
  <li><strong>Fill out the nomination form.</strong> Use one form for each award you enter.</li>
  <li><strong>Upload supporting documents</strong> about your project or organisation.</li>
  <li><strong>Submit your entry.</strong></li>
  <li><strong>Pay the nomination fee</strong> (PLACEHOLDER_NOMINATION_FEE_2026) to complete your nomination.</li>
</ol>
<p><a href="#nominate">Go to the nomination form</a></p>

<h2>How entries are judged</h2>
<p>Every entry is reviewed by the World AI Awards jury, which has more than five members. PLACEHOLDER_JURY_NAMES_AND_CRITERIA. Winners are announced and honoured at the awards ceremony at World AI Summit 2026 in Bengaluru on PLACEHOLDER_CEREMONY_DATE.</p>

<h2>2025 winners</h2>
<p>The 2025 World AI Awards were presented at World AI Summit 2025 in Bengaluru on 25 September 2025. Among the winners were Qualitrix (AI Validation &amp; Testing Excellence), Syngenta Group for Cropwise Grower, an AI chatbot for smallholder farmers (AI-Enabled Conversational &amp; Voice Assistance), and Altio AI (Most Promising AI Startup). <a href="PLACEHOLDER_WINNERS_2025_URL">See all 2025 winners</a>.</p>

<h2>Frequently asked questions</h2>
<h3>Who can nominate?</h3>
<p>Enterprises, government departments and public bodies, startups, solution providers and individual AI leaders. Choose the group that fits you: enterprise and application, business transformation, smart tech and engineering, governance, startups or leadership.</p>
<h3>What is the nomination fee?</h3>
<p>PLACEHOLDER_NOMINATION_FEE_2026 per entry. The fee is paid in the final step of the nomination.</p>
<h3>What is the last date to nominate?</h3>
<p>PLACEHOLDER_DEADLINE.</p>
<h3>Can I enter more than one award?</h3>
<p>PLACEHOLDER_MULTIPLE_ENTRIES_POLICY</p>
<h3>When and where are the awards presented?</h3>
<p>At World AI Summit 2026, Sheraton Grand Bangalore Hotel at Brigade Gateway, 26/1 Dr. Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru 560055, on PLACEHOLDER_CEREMONY_DATE.</p>
<h3>Does the nomination fee include a summit pass?</h3>
<p>PLACEHOLDER_PASS_INCLUDED. Delegate passes are available on the <a href="/delegate/">delegate pass page</a>.</p>
<h3>Are these the same as other "World AI Awards"?</h3>
<p>This page covers the World AI Awards presented at World AI Summit in Bengaluru, organised by Elets Technomedia. Other award programmes with similar names are run by separate organisers.</p>

[existing nomination form here, wrapped in <section id="nominate">]


=== 3. JSON-LD (replaces the existing Event block on /awards/; parsed and checked as valid JSON) ===

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Event",
  "name": "World AI Awards 2026 at World AI Summit 2026",
  "description": "Nominations for the World AI Awards 2026: 96 awards in six groups for enterprises, government, startups and AI leaders, presented at World AI Summit 2026 in Bengaluru. Organised by Elets Technomedia.",
  "url": "https://www.worldaisummit.com/awards/",
  "startDate": "2026-10-14",
  "endDate": "2026-10-15",
  "eventStatus": "https://schema.org/EventScheduled",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
  "location": {
    "@type": "Place",
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
  "organizer": {
    "@type": "Organization",
    "name": "Elets Technomedia Pvt. Ltd.",
    "url": "https://www.eletsonline.com/"
  },
  "offers": [
    {
      "@type": "Offer",
      "name": "Premium Pass - Late Access",
      "url": "https://www.worldaisummit.com/delegate/",
      "price": "30000",
      "priceCurrency": "INR",
      "validFrom": "2026-10-01",
      "availability": "https://schema.org/InStock"
    },
    {
      "@type": "Offer",
      "name": "VIP Pass - Late Access",
      "url": "https://www.worldaisummit.com/delegate/",
      "price": "60000",
      "priceCurrency": "INR",
      "validFrom": "2026-10-01",
      "availability": "https://schema.org/InStock"
    }
  ]
}
</script>

If the Late Access prices are not confirmed (see PLACEHOLDER_LATE_ACCESS_CONFIRM), delete the two "price" lines and keep the rest. Do not publish "20000". The Standard tier ended on 30 Sept 2026. The block has no "performer", because no awards-night line-up is confirmed. Google treats a missing performer as a warning, not an error, so the rich result still shows.


=== 4. REDIRECT /award.html -> /awards/ ===

Apache (.htaccess). Use this mod_alias line:
Redirect 301 /award.html https://www.worldaisummit.com/awards/

If the .htaccess already uses mod_rewrite (for example for the non-www to www redirect), use this instead and put it above the host rule, so the non-www URL also gets there in one hop:
RewriteEngine On
RewriteRule ^award\.html$ https://www.worldaisummit.com/awards/ [R=301,L]

nginx (inside the www server block, and also inside the non-www block if that block does not already redirect every path to www):
location = /award.html { return 301 https://www.worldaisummit.com/awards/; }

Then:
- Change every internal link to /award.html so it points to /awards/.
- Remove /award.html from sitemap.xml.
- Update the lastmod date for /awards/ in sitemap.xml.
- Add a link to /awards/ from the homepage navigation or the awards section. Today /awards/ has no internal links.
