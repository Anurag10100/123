# A69: Post-event switch pack for 15 Oct 2026, 19:00 IST: homepage hero, 2027 interest and partner forms, /delegate/ page, Event JSON-LD and redirects (corrected after verification)

- **For recommendation:** Turn the homepage and /delegate/ into post-event lead capture on the evening of 15 Oct
- **Research lens:** event-week-postevent
- **Format:** HTML snippets, JSON-LD, Apache .htaccess and nginx config, in one paste bundle with comments
- **Placeholders the business must fill:**
  - PLACEHOLDER_CURRENT_PASS_PRICE: the price on sale now. /delegate/ shows Late Access at Rs 30,000 for Premium and Rs 60,000 for VIP from 1 Oct, but the homepage still says Rs 20,000. Used in the homepage price block and the JSON-LD offers.price.
  - PLACEHOLDER_VERIFIED_ATTENDEE_COUNT: headcount signed off by the registration desk. If there is none, use the fallback sub-line with no number.
  - PLACEHOLDER_HIGHLIGHTS_2026_URL: URL of the 2026 highlights video or page. If it does not return 200 at 19:00 on 15 Oct, drop the 'Watch the highlights' button. Never use /agenda/.
  - /awards/winners-2026/ must exist and return 200 at switch time, or the winners button is dropped. The awards team owns this page.
  - PLACEHOLDER_FORM_ENDPOINT_INTEREST: form handler URL that delivers to registration@worldaisummit.com.
  - PLACEHOLDER_FORM_ENDPOINT_PARTNER: form handler URL that delivers to partnerships@worldaisummit.com.
  - PLACEHOLDER_PRIVACY_POLICY_URL: Elets or World AI Summit privacy policy URL, for the consent text.
  - PLACEHOLDER_RECORDINGS_DECISION: decide whether 2026 recordings are offered to everyone, given that the top pass tier sells 'Access to event photos & videos'. Banner Variant B is used only if the answer is yes.
  - PLACEHOLDER_RECORDINGS_URL: only needed if recordings are approved and a recordings product exists.
  - PLACEHOLDER_CONFIRM_SPEAKERS_WHO_APPEARED: after the event, remove from the JSON-LD performer list anyone who did not appear.
  - PLACEHOLDER_NEXT_EVENT_NAME / PLACEHOLDER_NEXT_EVENT_DATES / PLACEHOLDER_NEXT_EVENT_CITY / PLACEHOLDER_NEXT_EVENT_URL: the next Elets AI event. Publish this block only once its dates are confirmed.

## How to ship

Now (1-13 Oct). Web dev fixes the homepage price (section 0), puts the Event JSON-LD live with the current price (section 6), and adds the redirects (section 7). Then they build both forms on a staging copy and point them at the site's existing form handler or a form service. The interest form must deliver to registration@worldaisummit.com and the partner form to partnerships@worldaisummit.com. Send one test entry through each form and confirm it reaches the right inbox, including from a mobile on 4G. Marketing fills every PLACEHOLDER_ by 13 Oct. One decision is open: whether to offer recordings at all. Until it is made, use banner Variant A.

Switch at 15 Oct, 19:00 IST.
1. Check the two conditional links. Run `curl -s -o /dev/null -w "%{http_code}" https://www.worldaisummit.com/awards/winners-2026/` and the same for the highlights URL. Keep a button only if its URL returns 200.
2. Use the attendee figure only if the registration desk has signed it off. Otherwise use the fallback line.
3. Swap the hero and the pass block, and add both forms.
4. Leave the homepage <title>, the H1 and the WhatsApp block exactly as they are.
5. Swap the meta description and change the JSON-LD availability to SoldOut.
6. Republish /delegate/ with the banner, H1, title, meta and interest form. It must return 200.
7. Purge any CDN or browser cache. Then load both pages at phone width and submit one live test on each form.
8. Request indexing for / and /delegate/ in Search Console.

Measurement. Search Console is connected for the non-www property only, so the size of post-event brand traffic is unknown. Add a Domain property, or the https://www. URL-prefix property, before 14 Oct. Then count daily form completions on each form from 15 Oct, so the lead yield of this change is measured rather than assumed. Do not publish the "next Elets AI event" block (section 8) until its dates are confirmed.

## Content

=====================================================================
WORLD AI SUMMIT 2026: POST-EVENT SWITCH PACK
Prepare by 13 Oct 2026. Go live 15 Oct 2026 at 19:00 IST.
Pages: https://www.worldaisummit.com/  and  https://www.worldaisummit.com/delegate/
Replace every PLACEHOLDER_ before going live. Each one is a business decision or a missing input.
=====================================================================

CHANGES FROM THE ORIGINAL RECOMMENDATION (based on the verifier's findings)
1. "Watch the highlights" no longer points to /agenda/. /agenda/ returns 404, and an agenda is not a highlights page. The button links to PLACEHOLDER_HIGHLIGHTS_2026_URL. If that URL does not return 200 by 19:00 on 15 Oct, leave the button out.
2. "See the World AI Awards 2026 winners" ships only if /awards/winners-2026/ returns 200 at switch time. As of 1 Oct the page does not exist.
3. The two lead-capture buttons now come first. Both work without any other team's page being ready.
4. The /delegate/ banner no longer offers "2026 session recordings". No recordings product exists, and the homepage sells "Access to event photos & videos" as a benefit of the top pass tier. A recordings variant is included below, gated on PLACEHOLDER_RECORDINGS_DECISION.
5. The sub-line uses a headcount only if the registration desk has verified it. Otherwise use the fallback line with no number.
6. A price fix is needed now, before the switch. /delegate/ shows Standard Access "Valid till 30th Sept 2026", so Late Access (Rs 30,000 / Rs 60,000) applies from today, but the homepage still says Premium Pass Rs 20,000. See section 0.

---------------------------------------------------------------------
0. FIX NOW (before 15 Oct): HOMEPAGE PRICE MISMATCH
---------------------------------------------------------------------
In the homepage "Secure your seat" block, replace
    ₹ 20,000/ delegate
with
    ₹ PLACEHOLDER_CURRENT_PASS_PRICE / delegate
(On 1 Oct, /delegate/ lists Late Access at ₹30,000 for Premium and ₹60,000 for VIP. Confirm which price is current, and whether it includes GST.)

---------------------------------------------------------------------
1. HOMEPAGE HERO (live 15 Oct, 19:00 IST)
   Replace: the "14th - 15th October 2026 Save the date" line and the whole "Secure your seat" pass block (Premium Pass price, tier lists, group booking line).
   Keep: the existing H1, the page <title> "World AI Summit 2026 | ...", and the WhatsApp community block. Change none of them.
---------------------------------------------------------------------
<style>
  .wais-pe { max-width: 72rem; margin: 0 auto; padding: 2.5rem 1rem; }
  .wais-pe h2 { font-size: clamp(1.75rem, 4vw, 2.75rem); line-height: 1.15; margin: 0 0 .75rem; }
  .wais-pe-sub { font-size: 1.125rem; line-height: 1.6; max-width: 46rem; margin: 0 0 1.5rem; }
  .wais-pe-ctas { display: flex; flex-wrap: wrap; gap: .75rem; }
  .wais-pe-btn { display: inline-block; padding: .8rem 1.25rem; border: 2px solid currentColor; border-radius: 6px; font-weight: 600; text-decoration: none; }
  .wais-pe-btn--primary { background: #1f3a8a; border-color: #1f3a8a; color: #fff; }
  .wais-pe-form { display: grid; grid-template-columns: repeat(auto-fit, minmax(16rem, 1fr)); gap: 1rem; max-width: 46rem; }
  .wais-pe-form label { display: block; font-weight: 600; margin-bottom: .3rem; }
  .wais-pe-form input, .wais-pe-form select { width: 100%; padding: .65rem .75rem; border: 1px solid #9aa3b2; border-radius: 6px; font: inherit; box-sizing: border-box; }
  .wais-pe-form .wais-pe-full { grid-column: 1 / -1; }
  .wais-pe-check { display: flex; gap: .6rem; align-items: flex-start; font-weight: 400; }
  .wais-pe-check input { width: auto; margin-top: .3rem; }
  .wais-pe-hp { position: absolute; left: -9999px; width: 1px; height: 1px; overflow: hidden; }
  .wais-pe-thanks { max-width: 46rem; padding: 1rem 1.25rem; border-left: 4px solid #1f3a8a; background: rgba(31,58,138,.06); }
  .wais-pe-banner { padding: 1rem; text-align: center; font-weight: 600; background: #fff6d6; color: #3d3200; }
</style>

<section class="wais-pe" id="thank-you" aria-labelledby="wais-pe-hero-title">
  <h2 id="wais-pe-hero-title">Thank you, Bengaluru.</h2>

  <!-- USE THIS LINE ONLY IF THE REGISTRATION DESK HAS VERIFIED THE FIGURE -->
  <p class="wais-pe-sub">World AI Summit 2026 brought together PLACEHOLDER_VERIFIED_ATTENDEE_COUNT leaders on 14-15 October at Sheraton Grand Bangalore Hotel at Brigade Gateway.</p>

  <!-- FALLBACK (no verified figure): delete the line above and use this one
  <p class="wais-pe-sub">World AI Summit 2026 met on 14-15 October at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. Thank you to every speaker, delegate and partner who joined us.</p>
  -->

  <div class="wais-pe-ctas">
    <a class="wais-pe-btn wais-pe-btn--primary" href="#interest-2027">Register interest for 2027</a>
    <a class="wais-pe-btn" href="#partner-2027">Partner with us in 2027</a>

    <!-- CONDITIONAL: include only if PLACEHOLDER_HIGHLIGHTS_2026_URL returns 200 at switch time. Never point this at /agenda/. -->
    <a class="wais-pe-btn" href="PLACEHOLDER_HIGHLIGHTS_2026_URL">Watch the highlights</a>

    <!-- CONDITIONAL: include only if https://www.worldaisummit.com/awards/winners-2026/ returns 200 at switch time. -->
    <a class="wais-pe-btn" href="/awards/winners-2026/">See the World AI Awards 2026 winners</a>
  </div>
</section>

<!-- OPTIONAL: replace the future-tense intro ("...the World AI Summit returns this 14th - 15th October...") with: -->
<p>World AI Summit 2026 met on 14-15 October in Bengaluru to advance the vision of an ethical, inclusive and sovereign AI future. Policymakers, industry leaders, innovators, researchers and practitioners discussed responsible AI adoption across seven tracks, from frontier models and sovereign AI to enterprise AI, GCCs and AI for Bharat.</p>

---------------------------------------------------------------------
2. FORM #interest-2027 (homepage, below the hero; reused on /delegate/)
   Routes to: registration@worldaisummit.com
---------------------------------------------------------------------
<section class="wais-pe" aria-labelledby="interest-2027-title">
  <h2 id="interest-2027-title">Register your interest for World AI Summit 2027</h2>
  <p>Dates and venue for 2027 are not yet announced. Leave your details and we will write to you when they are, before passes open.</p>

  <form id="interest-2027" class="wais-pe-form" method="post" action="PLACEHOLDER_FORM_ENDPOINT_INTEREST" data-thanks="interest-2027-thanks">
    <input type="hidden" name="form_name" value="wais-2027-interest">
    <input type="hidden" name="route_to" value="registration@worldaisummit.com">
    <input type="hidden" name="source_page" value="">
    <input type="hidden" name="utm" value="">
    <div class="wais-pe-hp" aria-hidden="true"><label>Leave this empty <input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>

    <div><label for="i-name">Full name</label><input id="i-name" name="name" type="text" autocomplete="name" required></div>
    <div><label for="i-email">Work email</label><input id="i-email" name="work_email" type="email" autocomplete="email" required></div>
    <div><label for="i-mobile">Mobile</label><input id="i-mobile" name="mobile" type="tel" autocomplete="tel" inputmode="tel" placeholder="+91" pattern="^\+?[0-9 \-]{10,15}$" required></div>
    <div><label for="i-company">Company or organisation</label><input id="i-company" name="company" type="text" autocomplete="organization" required></div>
    <div><label for="i-designation">Designation</label><input id="i-designation" name="designation" type="text" autocomplete="organization-title" required></div>
    <div><label for="i-city">City</label><input id="i-city" name="city" type="text" autocomplete="address-level2" required></div>
    <div class="wais-pe-full">
      <label for="i-role">I would like to join as</label>
      <select id="i-role" name="role" required>
        <option value="">Select one</option>
        <option>Delegate</option>
        <option>Speaker</option>
        <option>Startup</option>
        <option>Government</option>
        <option>Investor</option>
      </select>
    </div>
    <div class="wais-pe-full">
      <label class="wais-pe-check"><input type="checkbox" name="consent_wais_2027" value="yes" required>
        <span>I agree that Elets Technomedia may contact me by email, phone or WhatsApp about World AI Summit 2027. I can withdraw this consent at any time by writing to registration@worldaisummit.com. See the <a href="PLACEHOLDER_PRIVACY_POLICY_URL">privacy policy</a>.</span></label>
    </div>
    <div class="wais-pe-full">
      <label class="wais-pe-check"><input type="checkbox" name="consent_other_elets_ai_events" value="yes">
        <span>Optional: also tell me about other Elets AI events.</span></label>
    </div>
    <div class="wais-pe-full"><button class="wais-pe-btn wais-pe-btn--primary" type="submit">Register interest</button></div>
  </form>

  <div id="interest-2027-thanks" class="wais-pe-thanks" tabindex="-1" hidden>
    <p><strong>Thank you. Your interest in World AI Summit 2027 is registered.</strong></p>
    <p>We will write to you when the dates, venue and passes are announced. For anything urgent, write to registration@worldaisummit.com.</p>
  </div>
</section>

---------------------------------------------------------------------
3. FORM #partner-2027 (homepage, after #interest-2027)
   Routes to: partnerships@worldaisummit.com
---------------------------------------------------------------------
<section class="wais-pe" aria-labelledby="partner-2027-title">
  <h2 id="partner-2027-title">Partner with World AI Summit 2027</h2>
  <p>Sponsors, exhibitors, awards partners and knowledge partners on this list will receive the 2027 partnership deck first.</p>

  <form id="partner-2027" class="wais-pe-form" method="post" action="PLACEHOLDER_FORM_ENDPOINT_PARTNER" data-thanks="partner-2027-thanks">
    <input type="hidden" name="form_name" value="wais-2027-partner">
    <input type="hidden" name="route_to" value="partnerships@worldaisummit.com">
    <input type="hidden" name="source_page" value="">
    <input type="hidden" name="utm" value="">
    <div class="wais-pe-hp" aria-hidden="true"><label>Leave this empty <input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>

    <div><label for="p-name">Full name</label><input id="p-name" name="name" type="text" autocomplete="name" required></div>
    <div><label for="p-email">Work email</label><input id="p-email" name="work_email" type="email" autocomplete="email" required></div>
    <div><label for="p-company">Company or organisation</label><input id="p-company" name="company" type="text" autocomplete="organization" required></div>
    <div><label for="p-designation">Designation</label><input id="p-designation" name="designation" type="text" autocomplete="organization-title" required></div>
    <div>
      <label for="p-interest">Partnership interest</label>
      <select id="p-interest" name="interest" required>
        <option value="">Select one</option>
        <option>Sponsor</option>
        <option>Exhibitor</option>
        <option>Awards partner</option>
        <option>Knowledge partner</option>
      </select>
    </div>
    <div>
      <label for="p-budget">Budget window</label>
      <select id="p-budget" name="budget_window" required>
        <option value="">Select one</option>
        <option>Q4 2026</option>
        <option>Q1 2027</option>
        <option>Later</option>
      </select>
    </div>
    <div class="wais-pe-full">
      <label class="wais-pe-check"><input type="checkbox" name="consent_partner_2027" value="yes" required>
        <span>I agree that Elets Technomedia may contact me about partnering with World AI Summit 2027. I can withdraw this consent at any time by writing to partnerships@worldaisummit.com. See the <a href="PLACEHOLDER_PRIVACY_POLICY_URL">privacy policy</a>.</span></label>
    </div>
    <div class="wais-pe-full"><button class="wais-pe-btn wais-pe-btn--primary" type="submit">Request the 2027 deck</button></div>
  </form>

  <div id="partner-2027-thanks" class="wais-pe-thanks" tabindex="-1" hidden>
    <p><strong>Thank you. We have noted your interest in partnering with World AI Summit 2027.</strong></p>
    <p>The 2027 partnership deck will be sent to this list first, as soon as it is ready. Our partnerships team may also write to you. You can reach them at partnerships@worldaisummit.com.</p>
  </div>
</section>

<!-- Shared script for both forms. Put it once per page, before </body>. It fills source_page and UTM fields and shows the thank-you message in place. If fetch fails (for example because the handler blocks CORS), the form falls back to a normal POST and the handler's own thank-you page is shown. -->
<script>
(function () {
  var q = new URLSearchParams(location.search);
  var utm = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content']
    .filter(function (k) { return q.get(k); })
    .map(function (k) { return k + '=' + q.get(k); }).join('&');
  document.querySelectorAll('form.wais-pe-form').forEach(function (form) {
    form.querySelector('[name="source_page"]').value = location.pathname;
    form.querySelector('[name="utm"]').value = utm;
    form.addEventListener('submit', function (e) {
      if (!window.fetch || !window.FormData) return;
      e.preventDefault();
      var btn = form.querySelector('button[type="submit"]');
      btn.disabled = true;
      fetch(form.action, { method: 'POST', body: new FormData(form), headers: { 'Accept': 'application/json' } })
        .then(function (r) {
          if (!r.ok) throw new Error('HTTP ' + r.status);
          var thanks = document.getElementById(form.getAttribute('data-thanks'));
          form.hidden = true; thanks.hidden = false; thanks.focus();
        })
        .catch(function () { btn.disabled = false; form.submit(); });
    });
  });
})();
</script>

---------------------------------------------------------------------
4. /delegate/ AFTER THE SWITCH (keep the URL live with a 200; do not 404 or redirect it)
   Remove: the pass price table (Early Bird, Standard, Late Access) and the Checkout block.
   Keep: the partnerships@ and secretariat@ contact blocks.
   Add: the banner, an H1 (the page has none today), and the #interest-2027 form from section 2, with the same markup and script.
---------------------------------------------------------------------
<title>World AI Summit 2026 Passes Closed | Register Interest for 2027</title>
<meta name="description" content="Passes for World AI Summit 2026 (14-15 October, Bengaluru) are closed. Register your interest for 2027 and we will write to you when passes open.">

<!-- BANNER, VARIANT A (default, use this one) -->
<div class="wais-pe-banner" role="status">Passes for World AI Summit 2026 are closed. <a href="#interest-2027">Register your interest for 2027</a>.</div>

<!-- BANNER, VARIANT B: use ONLY if PLACEHOLDER_RECORDINGS_DECISION = "offer recordings to everyone", and only after a recordings product exists at PLACEHOLDER_RECORDINGS_URL. Check first that this does not conflict with "Access to event photos & videos", which is sold as a benefit of the top pass tier.
<div class="wais-pe-banner" role="status">Passes for World AI Summit 2026 are closed. <a href="#interest-2027">Register your interest for 2027</a> or <a href="PLACEHOLDER_RECORDINGS_URL">get the 2026 session recordings</a>.</div>
-->

<h1>Register your interest for World AI Summit 2027</h1>
<p>World AI Summit 2026 took place on 14-15 October at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. Dates, venue and passes for 2027 will be announced here. Leave your details below and we will write to you when they are.</p>
<!-- paste FORM #interest-2027 from section 2 here -->

---------------------------------------------------------------------
5. HOMEPAGE <title> AND META DESCRIPTION AT THE SWITCH
---------------------------------------------------------------------
<title>: do not change it. It holds #1 for the brand query and the 2026 queries.
Meta description: replace the current one (182 characters) with this one (153 characters):
<meta name="description" content="World AI Summit 2026 by Elets Technomedia met on 14-15 October in Bengaluru. Register your interest for 2027 or enquire about partnering with the summit.">

---------------------------------------------------------------------
6. HOMEPAGE EVENT JSON-LD (put it live now; at the switch, change one line)
   Before 15 Oct: as written below, with the price filled in.
   At 19:00 on 15 Oct: change "availability" to "https://schema.org/SoldOut". Leave eventStatus as EventScheduled. Schema.org has no "completed" status, and EventCancelled or EventPostponed would be wrong.
   Performers: these six are marked confirmed_2026 in worldaisummit/speakers/speakers.json, and their job titles come from that file. After the event, remove anyone who did not appear (PLACEHOLDER_CONFIRM_SPEAKERS_WHO_APPEARED). Add other names only from the confirmed_2026 entries in that file.
---------------------------------------------------------------------
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Event",
  "@id": "https://www.worldaisummit.com/#event-2026",
  "name": "World AI Summit 2026",
  "description": "World AI Summit 2026, organised by Elets Technomedia, on 14-15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. Seven tracks: Frontier Models & Compute; Sovereign AI & Geopolitics; Enterprise AI in Production; Global Capability Centres; Robotics, Agents & Embodied AI; AI for Bharat; Capital, Founders & Exits.",
  "url": "https://www.worldaisummit.com/",
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
      "streetAddress": "26/1, Dr. Rajkumar Road, Malleswaram-Rajajinagar",
      "addressLocality": "Bengaluru",
      "addressRegion": "Karnataka",
      "postalCode": "560055",
      "addressCountry": "IN"
    }
  },
  "organizer": {
    "@type": "Organization",
    "name": "Elets Technomedia",
    "url": "https://eletsonline.com/"
  },
  "offers": {
    "@type": "Offer",
    "url": "https://www.worldaisummit.com/delegate/",
    "price": "PLACEHOLDER_CURRENT_PASS_PRICE",
    "priceCurrency": "INR",
    "availability": "https://schema.org/InStock"
  },
  "performer": [
    {"@type": "Person", "name": "Pankaj Kumar Pandey", "honorificSuffix": "IAS", "jobTitle": "Principal Secretary, Department of Personnel and Administrative Reforms (e-Governance)", "worksFor": {"@type": "GovernmentOrganization", "name": "Government of Karnataka"}},
    {"@type": "Person", "name": "T Bhoobalan", "honorificSuffix": "IAS", "jobTitle": "Chief Executive Officer, Centre for e-Governance, and Managing Director, KUIDFC", "worksFor": {"@type": "GovernmentOrganization", "name": "Government of Karnataka"}},
    {"@type": "Person", "name": "Aman Mittal", "honorificSuffix": "IAS", "jobTitle": "Joint Chief Executive Officer", "worksFor": {"@type": "GovernmentOrganization", "name": "Maharashtra Institution for Transformation (MITRA)"}},
    {"@type": "Person", "name": "Mahesh Hariharan Iyer", "jobTitle": "Vice President of Engineering", "worksFor": {"@type": "Organization", "name": "Reserve Bank Innovation Hub (RBIH)"}},
    {"@type": "Person", "name": "Sandeep Varaganti", "jobTitle": "CEO, JioMart", "worksFor": {"@type": "Organization", "name": "Reliance Retail"}},
    {"@type": "Person", "name": "Deepika Sandeep", "jobTitle": "Head - AI/ML CoE", "worksFor": {"@type": "Organization", "name": "HSBC"}}
  ]
}
</script>
(The JSON parses cleanly. Once the placeholder is replaced with a number such as "30000", it is ready to deploy.)

---------------------------------------------------------------------
7. REDIRECTS (put live now; each is a single 301 hop to the www host)
   a) /1st-edition/delegate-pass.html still sells 2025 passes, so send it to /delegate/. This avoids repeating the 2025 problem.
   b) /registration and /registration.html are now 302s that pass through non-www to the homepage in 3 hops. Make them one 301 to /delegate/, which shows passes now and the 2027 interest form after 15 Oct.
   Do NOT redirect /agenda/ or /awards/winners-2026/ anywhere. Either the owning team builds those pages, or the hero does not link to them.
---------------------------------------------------------------------
# Apache (.htaccess in the web root). Put these rules ABOVE any existing rewrite rules, and delete any older rule that 302s /registration.
<IfModule mod_rewrite.c>
RewriteEngine On
RewriteRule ^1st-edition/delegate-pass\.html$ https://www.worldaisummit.com/delegate/ [R=301,L]
RewriteRule ^registration(\.html)?/?$ https://www.worldaisummit.com/delegate/ [R=301,L]
</IfModule>

# nginx (inside the server {} blocks for both www and non-www). Remove any older /registration rule.
location = /1st-edition/delegate-pass.html { return 301 https://www.worldaisummit.com/delegate/; }
location = /registration      { return 301 https://www.worldaisummit.com/delegate/; }
location = /registration/     { return 301 https://www.worldaisummit.com/delegate/; }
location = /registration.html { return 301 https://www.worldaisummit.com/delegate/; }

# Check (each line should print 301 and the www /delegate/ URL, one hop):
# curl -sI https://www.worldaisummit.com/registration.html | grep -iE '^(HTTP|location)'
# curl -sI https://worldaisummit.com/registration | grep -iE '^(HTTP|location)'
# curl -sI https://www.worldaisummit.com/1st-edition/delegate-pass.html | grep -iE '^(HTTP|location)'

---------------------------------------------------------------------
8. LATER, ONLY ONCE DATES ARE CONFIRMED: NEXT ELETS AI EVENT BLOCK
   Do not publish with placeholders. indiaaisummit.in still promotes the January 2026 Delhi event, so do not link to it until it is updated.
---------------------------------------------------------------------
<section class="wais-pe" aria-labelledby="next-elets-ai">
  <h2 id="next-elets-ai">Next from Elets: PLACEHOLDER_NEXT_EVENT_NAME</h2>
  <p>PLACEHOLDER_NEXT_EVENT_DATES, PLACEHOLDER_NEXT_EVENT_CITY. <a href="PLACEHOLDER_NEXT_EVENT_URL">See the programme and passes</a>.</p>
</section>

---------------------------------------------------------------------
SOURCES
- Venue address (26/1, Dr. Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru 560055): Marriott listing https://www.marriott.com/en-us/hotels/blrgs-sheraton-grand-bangalore-hotel-at-brigade-gateway/overview/ and HotelPlanner https://www.hotelplanner.com/Hotels/178731/Reservations-Sheraton-Bangalore-Hotel-at-Brigade-Gateway-Bangalore-26-1-Dr-Rajkumar-Rd-Malleswaram-Rajajinagar-560055 (web search, 1 Oct 2026).
- Homepage copy (Save the date, Premium Pass ₹20,000, group booking 10% off, seven tracks, "Access to event photos & videos" in the top tier) and /delegate/ prices (Standard valid till 30 Sept 2026, Late Access ₹30,000 / ₹60,000, partnerships@ and secretariat@ blocks): Exa fetch, 1 Oct 2026.
- Missing /agenda/ and /awards/winners-2026/: verifier, from Exa CRAWL_NOT_FOUND on 1 Oct and crawl c1b16b55.
- Performer names and job titles: worldaisummit/speakers/speakers.json (confirmed_2026 = true).
