# A03: World AI Awards 2026: /awards/ deadline banner, categories and fee block, CTR title, and /award.html canonical and fee fix

- **For recommendation:** 4. Awards: deadline banner, fee and categories on /awards/ (the URL that ranks), plus a CTR-led title
- **Research lens:** cro-leads
- **Format:** HTML snippets (head tags, CSS, banner, categories section, auto-close script) for the static pages /awards/ and /award.html, with optional Apache .htaccess and nginx 301 rules
- **Placeholders the business must fill:**
  - PLACEHOLDER_DEADLINE_SHORT: short deadline for the title, meta and og:title, e.g. '10 Oct' (keep it to 6 characters or fewer so the title stays at 60 or less)
  - PLACEHOLDER_DEADLINE_LONG: full deadline with weekday and time in IST, e.g. 'Saturday, 10 October 2026, 6 pm IST' (2026 dates: 8 Oct is a Thursday, 9 Oct a Friday, 10 Oct a Saturday)
  - PLACEHOLDER_DEADLINE_ISO: the same deadline in ISO 8601 with the IST offset for the auto-close script, e.g. '2026-10-10T18:00:00+05:30'
  - PLACEHOLDER_FEE_LOWEST: lowest 2026 entry fee before GST, used in the banner and on /award.html (2025: Rs 18,000 discounted, startup/individual)
  - PLACEHOLDER_FEE_STARTUP_INDIVIDUAL: 2026 fee per entry for startups and individuals (2025: Rs 18,000 + GST, discounted)
  - PLACEHOLDER_FEE_ENTERPRISE: 2026 fee per entry for enterprise, government, leadership and solution-provider entries (2025: Rs 20,000 + GST, discounted)
  - PLACEHOLDER_AWARDS_WHATSAPP: awards desk WhatsApp number in wa.me format, digits only with country code and no plus sign, e.g. 91XXXXXXXXXX
  - PLACEHOLDER_AWARDS_EMAIL: awards query email (confirm whether secretariat@worldaisummit.com or another inbox handles awards)
  - PLACEHOLDER_PAYMENT_URL: separate payment or checkout URL for the nomination fee, if any; otherwise remove the link from step 6

## How to ship

Owner: Elets awards team (fills in the placeholders) and the web developer (pastes the snippets). Deadline: live by 2 Oct 2026. Effort: about 30 min for the awards team and 2-3 h for the developer.

1) THE AWARDS TEAM FIXES THE BUSINESS FACTS FIRST. Nothing goes live while any PLACEHOLDER_ remains; check with `grep -rn PLACEHOLDER_ .` before upload.
- Set the nomination deadline. It must fall a few days before 14 Oct so the jury has time.
- Set the 2026 fees.
- Supply the WhatsApp number and email for the awards desk.

Reference for the fee: the live 2025 checkout at elets.net/worldaisummit-awards/ (fetched via Exa, 1 Oct) had two tiers, not one:
- Rs 18,000 + GST per entry ("Save Rs 5,000") for Startup & Individual.
- Rs 20,000 + GST ("Save Rs 10,000") for Enterprise, Government, Leadership and Solution Provider.
Both were discounted prices; the list prices were about Rs 23,000 and Rs 30,000. So "Entries from 30k + GST" on /award.html matches the undiscounted 2025 enterprise price, but it overstates the starting price for startups. The banner says "from Rs [lowest fee]", and the table gives both tiers so the two pages agree. If 2026 has only one fee, remove one table row and use that figure in both places.

2) /awards/ CHANGES. Apply snippets 1-7 in order:
- head tags
- H1 swap
- CSS
- banner directly above the "Select Sectors" form
- #categories section under the banner
- id="nominate" on the form wrapper
- auto-close script before </body>

The award names are copied verbatim from /award.html: 96 named awards (26+13+16+4+19+18), so "75+" is safe. Ask the awards team to confirm two things:
- The six steps (taken from /award.html) still match the 2026 form. "Sign up / Log in" and "Complete Your Nomination Fee" are not visible on /awards/.
- Whether payment happens on a separate checkout.

3) /award.html CHANGES. Apply snippets 8-9:
- canonical pointing to www /awards/
- its own title and meta
- the fee line fix
- the deadline line
- a "Nominate now" button in two places

Ask the mailer team to link future awards mailers straight to https://www.worldaisummit.com/awards/ with UTM tags. Snippet 10 (a 301 redirect, Apache and nginx versions) is optional. Use it only once /awards/ carries the categories; it then replaces the canonical.

4) WHY THE TITLE NAMES BENGALURU AND ELETS. worldawards.ai runs its own "World AI Awards 2026" (1000+ categories, Sep 2026, Anguilla). /awards/ gets 0 clicks from 44 impressions at average position 3.0 for "world ai awards", which suggests those searchers want that brand. The new title keeps the exact phrase "AI Awards 2026" (178 impressions, position 8.6) and "ai awards" (115 impressions, position 10). It adds Bengaluru and Elets to set it apart, plus a deadline that changes with the date. Fallback titles for "deadline not fixed" and "after the deadline" are in the comment under snippet 1. Swap in the closed title by hand on deadline day; the script changes only the banner.

5) CHECKS AFTER UPLOAD.
- View the source of both pages: one <title>, one canonical each.
- Open /awards/ on a 360 px wide phone: the buttons wrap and nothing scrolls sideways.
- Test that #nominate and #categories jump to the right places.
- Test the WhatsApp link on a phone.
- Confirm https://worldaisummit.com/awards/ redirects with a 301 to the www URL. GSC only covers the non-www property, and that is the version that ranks.
- Request indexing for /awards/ in GSC.

6) MEASURE AND REPORT HONESTLY.
- Baseline, GSC non-www, 31 Aug-28 Sep: /awards had 32 clicks from 1,300 impressions at position 7.9. Over 3 months it had 79 clicks from 2,419 impressions at position 9.1.
- Compare the 14 days after launch with the 14 days before.
- The 79 key events on /awards/ (GA4, Jul-Sep) are the generic form_submit event, so they are not confirmed paid nominations. Get the paid count from the awards team.
- Do not promise conversion of "18,000 mailer users". /award.html had 18,849 users at about 2 s engagement each. Site-wide, r.emails.elets.in referral sessions almost equal users and convert at 0.06%, which points to email link-scanner hits. That traffic is inferred to be from mailers; it was not confirmed at page level.
- Expect a small traffic gain, perhaps +10-20 clicks in 2 weeks. Directional only.

## Content

<!-- ============================================================
     WORLD AI AWARDS 2026: /awards/ banner, categories block, title and /award.html fixes
     Ship by 2 Oct 2026. Replace every PLACEHOLDER_ before going live.
     ============================================================ -->

<!-- 1. /awards/  <head>: replace the current <title> and meta description -->
<title>World AI Awards 2026, Bengaluru: Nominate by PLACEHOLDER_DEADLINE_SHORT | Elets</title>
<meta name="description" content="World AI Awards 2026 by Elets: nominations close PLACEHOLDER_DEADLINE_SHORT. 75+ awards for enterprise AI, startups, governance and leadership, presented in Bengaluru, 14-15 Oct.">
<link rel="canonical" href="https://www.worldaisummit.com/awards/">
<meta property="og:type" content="website">
<meta property="og:url" content="https://www.worldaisummit.com/awards/">
<meta property="og:title" content="World AI Awards 2026, Bengaluru: Nominate by PLACEHOLDER_DEADLINE_SHORT | Elets">
<meta property="og:description" content="Nominations close PLACEHOLDER_DEADLINE_LONG. 75+ awards across enterprise AI, startups, governance and leadership. Winners honoured at World AI Summit 2026, Bengaluru, 14-15 October.">
<!-- Title is 59 characters with a date such as "10 Oct".
     If the deadline is not fixed yet:  World AI Awards 2026, Bengaluru: Nominations Open | Elets   (57)
     After the deadline passes:         World AI Awards 2026, Bengaluru: Nominations Closed | Elets (59) -->

<!-- 2. /awards/  H1: the current H1 is the summit theme. Change it to the line below and keep the theme as a <p>. -->
<h1>World AI Awards 2026: nominate your AI work</h1>
<p class="awards-theme">AI for All: Accelerating India's Journey Towards Inclusive, Responsible and Future-Ready AI</p>

<!-- 3. CSS: add it to the site stylesheet or to a <style> block in <head>. Map the four colour tokens to the site palette. -->
<style>
.nom-banner{--nb-bg:#0b1f3a;--nb-fg:#ffffff;--nb-accent:#f5b301;--nb-accent-fg:#111111;
  background:var(--nb-bg);color:var(--nb-fg);border-radius:8px;padding:14px 16px;margin:0 0 20px;
  display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:10px 20px;
  font-size:15px;line-height:1.45}
.nom-banner p{margin:0}
.nom-banner__text{flex:1 1 420px;min-width:0}
.nom-banner__meta{font-size:14px;opacity:.9;margin-top:4px}
.nom-banner__cta{display:flex;flex-wrap:wrap;gap:8px}
.nom-banner__cta a{display:inline-block;padding:9px 14px;border-radius:6px;border:1px solid rgba(255,255,255,.6);
  color:var(--nb-fg);font-weight:600;text-decoration:none;white-space:nowrap}
.nom-banner__cta a.is-primary{background:var(--nb-accent);border-color:var(--nb-accent);color:var(--nb-accent-fg)}
.nom-banner__cta a:focus-visible{outline:2px solid var(--nb-accent);outline-offset:2px}
.nom-banner [hidden]{display:none !important}
@media (max-width:600px){.nom-banner__cta{width:100%}.nom-banner__cta a{flex:1 1 auto;text-align:center}}
#categories{margin:0 0 28px}
#categories table{border-collapse:collapse;width:100%;max-width:640px;margin:8px 0 16px}
#categories th,#categories td{border:1px solid #d0d5dd;padding:8px 10px;text-align:left;vertical-align:top}
.awd-group{border:1px solid #d0d5dd;border-radius:6px;margin:0 0 8px;padding:0 12px}
.awd-group summary{cursor:pointer;font-weight:600;padding:10px 0}
.awd-group summary span{font-weight:400;opacity:.75}
.awd-group ul{margin:0 0 12px;padding-left:20px;columns:2 260px;column-gap:28px}
.awd-group li{break-inside:avoid;margin:0 0 4px}
</style>

<!-- 4. /awards/  BANNER: paste directly above the "Select Sectors" form section. -->
<div class="nom-banner" role="region" aria-label="World AI Awards 2026 nominations" data-deadline="PLACEHOLDER_DEADLINE_ISO">
  <div class="nom-banner__text">
    <p class="nom-banner__status"><strong>World AI Awards 2026: nominations close PLACEHOLDER_DEADLINE_LONG</strong></p>
    <p class="nom-banner__meta">Entry fee from Rs PLACEHOLDER_FEE_LOWEST + GST per entry · 75+ awards in six categories · Winners honoured at World AI Summit 2026, Bengaluru, 14-15 October</p>
  </div>
  <div class="nom-banner__cta">
    <a class="is-primary" href="#nominate">Nominate now</a>
    <a href="#categories">See categories and fees</a>
    <a href="https://wa.me/PLACEHOLDER_AWARDS_WHATSAPP?text=Query%20about%20World%20AI%20Awards%202026%20nomination" target="_blank" rel="noopener">WhatsApp the awards desk</a>
  </div>
</div>

<!-- 5. /awards/  CATEGORIES, FEES AND STEPS: paste directly below the banner, above the form.
     Award names are copied verbatim from /award.html (96 awards: 26 + 13 + 16 + 4 + 19 + 18). -->
<section id="categories" aria-labelledby="categories-h">
  <h2 id="categories-h">World AI Awards 2026: categories, entry fees and how to nominate</h2>
  <p>The World AI Awards recognise real-world applications of artificial intelligence in enterprise, public services, startups and leadership. The 2026 awards will be presented at World AI Summit 2026, Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru, on 14-15 October 2026. Nominations close PLACEHOLDER_DEADLINE_LONG.</p>

  <h3>Entry fee</h3>
  <table>
    <thead><tr><th scope="col">Who is entering</th><th scope="col">Fee per entry</th></tr></thead>
    <tbody>
      <tr><td>Startups and individuals</td><td>Rs PLACEHOLDER_FEE_STARTUP_INDIVIDUAL + GST</td></tr>
      <tr><td>Enterprises, government bodies, solution providers and leadership nominations</td><td>Rs PLACEHOLDER_FEE_ENTERPRISE + GST</td></tr>
    </tbody>
  </table>

  <h3>Award categories (96 awards)</h3>
    <details class="awd-group">
      <summary>01 AI Enterprise &amp; Application <span>(26 awards)</span></summary>
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
    </details>
    <details class="awd-group">
      <summary>02 Business Transformation &amp; Innovation <span>(13 awards)</span></summary>
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
    </details>
    <details class="awd-group">
      <summary>03 Smart Tech &amp; AI Engineering <span>(16 awards)</span></summary>
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
    </details>
    <details class="awd-group">
      <summary>04 AI in Governance <span>(4 awards)</span></summary>
      <ul>
        <li>AI for Public Service Delivery Excellence</li>
        <li>Outstanding Citizen Engagement Initiative</li>
        <li>Data-Driven Governance Award</li>
        <li>AI for E-Governance Initiatives</li>
      </ul>
    </details>
    <details class="awd-group">
      <summary>05 AI Startups <span>(19 awards)</span></summary>
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
    </details>
    <details class="awd-group">
      <summary>06 AI Leadership <span>(18 awards)</span></summary>
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
    </details>

  <h3>How to nominate in six steps</h3>
  <!-- Awards team: confirm these six steps match the 2026 form. If the fee is paid on a separate checkout, link it in step 6 (PLACEHOLDER_PAYMENT_URL); otherwise delete the link. -->
  <ol>
    <li>Sign up or log in.</li>
    <li>Select your category.</li>
    <li>Fill out the nomination form for each entry.</li>
    <li>Upload supporting documents.</li>
    <li>Submit your entry.</li>
    <li>Pay the nomination fee (<a href="PLACEHOLDER_PAYMENT_URL">payment page</a>).</li>
  </ol>
  <p>Questions about categories or eligibility: <a href="https://wa.me/PLACEHOLDER_AWARDS_WHATSAPP?text=Query%20about%20World%20AI%20Awards%202026%20nomination" target="_blank" rel="noopener">WhatsApp the awards desk</a> or write to <a href="mailto:PLACEHOLDER_AWARDS_EMAIL">PLACEHOLDER_AWARDS_EMAIL</a>.</p>
</section>

<!-- 6. /awards/  FORM ANCHOR: add id="nominate" to the element that wraps the "Select Sectors" form, for example: -->
<section id="nominate"> <!-- existing "Select Sectors" heading and form stay inside, unchanged --> </section>

<!-- 7. /awards/  AUTO-CLOSE: paste just before </body>. After the deadline (IST), it hides the buttons and shows a closed message.
     If PLACEHOLDER_DEADLINE_ISO is left unfilled, the date is invalid and the banner stays as it is. -->
<script>
(function () {
  var banner = document.querySelector('.nom-banner[data-deadline]');
  if (!banner) return;
  var deadline = new Date(banner.getAttribute('data-deadline'));
  if (isNaN(deadline.getTime()) || Date.now() < deadline.getTime()) return;
  var status = banner.querySelector('.nom-banner__status');
  var meta = banner.querySelector('.nom-banner__meta');
  var cta = banner.querySelector('.nom-banner__cta');
  if (status) status.innerHTML = '<strong>Nominations for the World AI Awards 2026 have closed.</strong>';
  if (meta) meta.textContent = 'Winners will be honoured at World AI Summit 2026, Bengaluru, 14-15 October.';
  if (cta) cta.hidden = true;
})();
</script>

<!-- ============================================================
     /award.html (the page linked from mailers)
     ============================================================ -->

<!-- 8. /award.html  <head>: replace the homepage title, meta and canonical it carries today -->
<title>World AI Awards 2026 Categories, Fees and Steps | Elets</title>
<meta name="description" content="All 96 World AI Awards 2026 categories, entry fees and the six steps to nominate. Presented at World AI Summit, Bengaluru, 14-15 October 2026.">
<link rel="canonical" href="https://www.worldaisummit.com/awards/">

<!-- 9. /award.html  BODY TEXT FIXES
     a) Replace "Entries from 30k + GST" with:
          Entries from Rs PLACEHOLDER_FEE_LOWEST + GST
     b) Replace "Nominations are open for the upcoming edition." with:
          Nominations for the World AI Awards 2026 close PLACEHOLDER_DEADLINE_LONG.
     c) Add this button in the hero (under "75+ Awards to be Presented") and again under "Ready to be recognised?": -->
<a class="btn-nominate" href="https://www.worldaisummit.com/awards/#nominate">Nominate now</a>
<!-- Re-use the site's existing primary button class if it has one, instead of btn-nominate. -->

<!-- 10. OPTIONAL, LATER: retire /award.html with a 301 to /awards/.
     Do this only after /awards/ carries the categories (step 5) and the mailer team agrees. A redirect replaces the canonical in step 8.
     Query strings (UTMs) pass through in both versions. -->

# Apache (.htaccess in the site root)
RewriteEngine On
RewriteRule ^award\.html$ https://www.worldaisummit.com/awards/ [R=301,L]

# nginx (inside the server block for www.worldaisummit.com and worldaisummit.com)
location = /award.html {
    return 301 https://www.worldaisummit.com/awards/$is_args$args;
}
