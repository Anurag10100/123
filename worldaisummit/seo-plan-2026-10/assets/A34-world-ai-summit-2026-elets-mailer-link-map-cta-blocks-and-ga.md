# A34: World AI Summit 2026: Elets mailer link map, CTA blocks and GA4 reading guide (sends 2-13 Oct, post-event 16 Oct)

- **For recommendation:** Point the Elets mailer engine at the pass, awards and sponsor pages, with UTMs. It sends about 93% of all WAIS sessions, which convert at 0.06%
- **Research lens:** elets-network
- **Format:** Plain-text brief, Markdown-compatible, for the Elets email/marketing team and web team. It has six parts: blocking checks, the exact link map, token rules with worked examples, CTA copy blocks with HTML anchors, a GA4 reading guide and a per-template QA checklist.
- **Placeholders the business must fill:**
  - PLACEHOLDER_DELEGATE_PAGE_FIXED: has the web team removed or updated the expired Standard Access (valid till 30 Sept 2026) row on /delegate/, and on what date
  - PLACEHOLDER_FALLBACK_IF_DELEGATE_NOT_FIXED: hold the Pass CTA, or send it with no price in copy, if /delegate/ is not fixed by the 2 Oct send
  - PLACEHOLDER_PASS_PRICE: the current pass price; do not use until the homepage (Rs 20,000) and /delegate/ (Late Access Rs 30,000/60,000) agree
  - PLACEHOLDER_GROUP_DISCOUNT_CONFIRMED: confirm the 3+ delegates, 10% off group discount before it appears in copy
  - PLACEHOLDER_SEATS_LEFT: only if the registration team gives a real figure
  - PLACEHOLDER_AWARD_CATEGORY_GROUPS: the five category groups copied from /award.html (not from memory), until /awards/ shows or links to them
  - PLACEHOLDER_AWARD_FEE: /award.html says 30k + GST, project memory says Rs 18,000 + GST (2025); confirm the 2026 fee
  - PLACEHOLDER_AWARD_DEADLINE: the 2026 nomination closing date
  - PLACEHOLDER_CONFIRMED_SPEAKERS: names, designations and organisations from confirmed 2026 entries in worldaisummit/speakers/speakers.json only
  - PLACEHOLDER_POST_EVENT_PRIMARY_CTA: the main ask for the 16 Oct post-event send (the Pass CTA no longer applies)
  - PLACEHOLDER_NEW_SEGMENT_CODE: an agreed lowercase code for any list outside egov, bfsi, ehealth, edu, cio, gcc, startup

## How to ship

Owner: the Elets email/marketing team, with the web team handling items A1 and A4. Deadline: before the 2 Oct send.
1. The web team clears A1 (the expired Standard Access row on /delegate/). It also adds award categories to /awards/ or links to them from there (A4). Marketing decides the A1 fallback if this is not done in time.
2. Business owners fill in the placeholders, or leave those lines out. Price, fee, discount, deadline and seats left stay out of copy until confirmed.
3. In the ESP, turn off auto-UTM. Paste the Section B URLs into every WAIS link in each template, including banner and logo links. Replace <segment> and <yyyymmdd> per list and send date, using Section C.
4. Run the Section G QA on each template before each send from 2 to 13 Oct. Rebuild the 16 Oct post-event send without the Pass CTA.
5. Send Section F to the ESP team.
6. Analytics reads results using Section E. Use the engagement-time segment and count /delegate/success.php views, thank-you users and /awards/ submitters, not raw key events.
Caveat: I could not test the URLs live from this session, because outbound requests to worldaisummit.com were blocked by the proxy (403). Page facts come from the verifier's Exa fetches and GA4 reads on 1 Oct 2026. Points marked "inferred" are inferences, not observed data.

## Content

WORLD AI SUMMIT 2026: ELETS MAILER LINK MAP
For: Elets email/marketing team. Applies to every World AI Summit link in Elets mailers and in the eGov Weekly Briefing, BFSI, eHealth and Digital Learning newsletters.
Window: every send from 2 Oct to 13 Oct 2026, plus the post-event send on 16 Oct 2026.
Event facts you can use in copy: World AI Summit 2026, 14-15 October 2026, Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. Organised by Elets Technomedia. Do not state an edition number, because site pages say "2nd" and LinkedIn says "3rd".

------------------------------------------------------------
A. BLOCKING CHECKS BEFORE THE FIRST DEEP-LINKED SEND
------------------------------------------------------------
1. /delegate/ page (web team). The page still shows "Standard Access (Valid till 30th Sept 2026)" at Rs 20,000/35,000. That offer expired on 30 Sep. It sits next to Late Access at Rs 30,000/60,000. Remove or update the expired row before cold mailer traffic is sent to /delegate/.
   Status: PLACEHOLDER_DELEGATE_PAGE_FIXED (yes/no, date)
   If it is not fixed by the 2 Oct send: PLACEHOLDER_FALLBACK_IF_DELEGATE_NOT_FIXED (hold the pass CTA, or send it with no price in copy)
2. Pass price. The homepage says Rs 20,000. /delegate/ says Late Access Rs 30,000/60,000. Do not quote any pass price in copy until the two pages agree: PLACEHOLDER_PASS_PRICE
3. Group discount (3+ delegates, 10% off). Use it only once confirmed: PLACEHOLDER_GROUP_DISCOUNT_CONFIRMED
4. Award categories. /awards/ holds the nomination form but has no categories, fee or deadline. /award.html lists the categories (75+ awards in five groups), but it is canonicalised to / and is not the nomination page. The web team should add the category list to /awards/, or link to it from /awards/. Until then, the mailer has to name the categories itself: PLACEHOLDER_AWARD_CATEGORY_GROUPS (copy them from /award.html, never from memory).
5. Award fee and deadline. /award.html says "Entries from 30k + GST", while project memory has Rs 18,000 + GST (the 2025 fee). Do not quote a fee until it is confirmed: PLACEHOLDER_AWARD_FEE. Deadline: PLACEHOLDER_AWARD_DEADLINE
6. ESP settings. Turn off any automatic UTM or "Google Analytics link tracking" option in the ESP, so it does not add to or overwrite the parameters below.

------------------------------------------------------------
B. LINK MAP (keep these exact URLs; replace only <segment> and <yyyymmdd>)
------------------------------------------------------------
Pass CTA:
https://www.worldaisummit.com/delegate/?utm_source=elets_mailer&utm_medium=email&utm_campaign=world_ai_summit_2026_delegate&utm_content=<segment>_<yyyymmdd>

Awards CTA:
https://www.worldaisummit.com/awards/?utm_source=elets_mailer&utm_medium=email&utm_campaign=world_ai_awards_2026&utm_content=<segment>_<yyyymmdd>

Sponsor CTA:
https://www.worldaisummit.com/partnership.html?utm_source=elets_mailer&utm_medium=email&utm_campaign=world_ai_summit_2026_sponsorship&utm_content=<segment>_<yyyymmdd>

Speakers:
https://www.worldaisummit.com/speaker.html?utm_source=elets_mailer&utm_medium=email&utm_campaign=world_ai_summit_2026&utm_content=speakers_<yyyymmdd>

Sponsorship deck line. This is an email link, not a web page, so GA4 does not track it:
mailto:partnerships@worldaisummit.com?subject=Sponsorship%20deck%20request%20-%20World%20AI%20Summit%202026

Do not link to /award.html, the homepage, /registration or /registration.html from mailers. /registration and /registration.html take 3 redirect hops to the homepage.

------------------------------------------------------------
C. TOKEN RULES
------------------------------------------------------------
<segment> is one of: egov, bfsi, ehealth, edu, cio, gcc, startup
  eGov Weekly Briefing and eGov mailers ......... egov
  BFSI newsletter and BFSI mailers .............. bfsi
  eHealth newsletter and eHealth mailers ........ ehealth
  Digital Learning newsletter and edu mailers ... edu
  CIO / enterprise technology list .............. cio
  GCC list ...................................... gcc
  Startup list .................................. startup
  Any other list: PLACEHOLDER_NEW_SEGMENT_CODE (agree a code before the send; lowercase, no spaces)

<yyyymmdd> is the send date in IST, for example 20261002.

- Remove the angle brackets. Use lowercase only and no spaces. Never change utm_source, utm_medium or utm_campaign.
- The Speakers link keeps utm_content=speakers_<yyyymmdd> exactly as given, with no segment.
- Tag every World AI Summit link in the email: header banner, logo, image links, buttons and footer text links. Banner and logo links use the Pass CTA (the Section D post-event block covers 16 Oct).
- Why every link: untagged clicks are counted as Direct or as r.emails.elets.in / referral. Direct/(none) produced 293 key events in Jul-Sep 2026, more than the mailers did. Some of these are probably untagged mailer clicks from desktop email apps (inferred).

Worked example: eGov Weekly Briefing, send on 2 Oct 2026
https://www.worldaisummit.com/delegate/?utm_source=elets_mailer&utm_medium=email&utm_campaign=world_ai_summit_2026_delegate&utm_content=egov_20261002
https://www.worldaisummit.com/awards/?utm_source=elets_mailer&utm_medium=email&utm_campaign=world_ai_awards_2026&utm_content=egov_20261002
https://www.worldaisummit.com/partnership.html?utm_source=elets_mailer&utm_medium=email&utm_campaign=world_ai_summit_2026_sponsorship&utm_content=egov_20261002
https://www.worldaisummit.com/speaker.html?utm_source=elets_mailer&utm_medium=email&utm_campaign=world_ai_summit_2026&utm_content=speakers_20261002

------------------------------------------------------------
D. READY-TO-PASTE CTA BLOCKS (no prices until Section A is cleared)
------------------------------------------------------------
[PASS BLOCK]
World AI Summit 2026 | 14-15 October 2026 | Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru
Two days across seven tracks: Frontier Models & Compute; Sovereign AI & Geopolitics; Enterprise AI in Production; GCCs; Robotics, Agents & Embodied AI; AI for Bharat; and Capital, Founders & Exits.
<a href="https://www.worldaisummit.com/delegate/?utm_source=elets_mailer&utm_medium=email&utm_campaign=world_ai_summit_2026_delegate&utm_content=<segment>_<yyyymmdd>">Book your delegate pass</a>
Optional, only once confirmed: Registering three or more colleagues? Group bookings receive PLACEHOLDER_GROUP_DISCOUNT_CONFIRMED.
Optional, only if the registration team gives a real figure: PLACEHOLDER_SEATS_LEFT
For registration queries, write to registration@worldaisummit.com.

[AWARDS BLOCK]
Nominations are open for the World AI Awards.
Categories: PLACEHOLDER_AWARD_CATEGORY_GROUPS
Entry fee: PLACEHOLDER_AWARD_FEE
Last date for nominations: PLACEHOLDER_AWARD_DEADLINE
<a href="https://www.worldaisummit.com/awards/?utm_source=elets_mailer&utm_medium=email&utm_campaign=world_ai_awards_2026&utm_content=<segment>_<yyyymmdd>">Submit a nomination</a>

[SPONSOR BLOCK]
Sponsorship and exhibition opportunities are open for World AI Summit 2026, 14-15 October, Bengaluru.
<a href="https://www.worldaisummit.com/partnership.html?utm_source=elets_mailer&utm_medium=email&utm_campaign=world_ai_summit_2026_sponsorship&utm_content=<segment>_<yyyymmdd>">Explore sponsorship options</a>
To receive the sponsorship deck, write to <a href="mailto:partnerships@worldaisummit.com?subject=Sponsorship%20deck%20request%20-%20World%20AI%20Summit%202026">partnerships@worldaisummit.com</a>.

[SPEAKERS BLOCK]
Speakers include:
PLACEHOLDER_CONFIRMED_SPEAKERS (format: Name, Designation, Organisation. Use only confirmed 2026 entries from worldaisummit/speakers/speakers.json. Never write names, titles or bios from memory.)
<a href="https://www.worldaisummit.com/speaker.html?utm_source=elets_mailer&utm_medium=email&utm_campaign=world_ai_summit_2026&utm_content=speakers_<yyyymmdd>">See the speaker line-up</a>

[POST-EVENT SEND, 16 OCT]
The Pass CTA no longer applies after 15 October. Remove it, along with any banner or logo link that points to /delegate/.
Primary CTA: PLACEHOLDER_POST_EVENT_PRIMARY_CTA (for example, awards results or sponsor enquiries for the next edition)
Any Speakers, Awards or Sponsor link that is reused follows the same rules with <yyyymmdd> = 20261016.

------------------------------------------------------------
E. HOW TO READ THE RESULTS IN GA4 (property 490291049)
------------------------------------------------------------
1. Source change. From 2 Oct, tagged mailer clicks show as elets_mailer / email, not r.emails.elets.in / referral. When comparing with Jul-Sep, add the two rows together.
2. Segment and send split. Use the dimension "Session manual ad content" (utm_content).
3. Human traffic only. Compare on a segment with user engagement time > 0, or on engaged sessions. Filtering clicks in the ESP does not remove scanner clicks from GA4, because these "users" run the GA4 tag. They average about 1.01 sessions per user and 0.39 s of engagement per user on /partnership.html. From 16 to 30 Sep, mailers produced 164,537 sessions but only 74 key events (0.045%).
4. Key events are not sales. Transactions are 0 for every source. Count results this way:
   - Passes: views of /delegate/success.php (78 views from 18 users in Jul-Sep; inferred to be the paid-pass count). Do not count /delegate/ key events (316 in Jul-Sep).
   - Sponsor leads: partnership_form_submit, counted as users. It fires when /thankyou.html is viewed (391 events = 391 thank-you key events).
   - Award nominations: /awards/ form_submit, counted as users (46 events from 14 users in Jul-Sep). Check /awards/failed.php views next to it.
5. Jul-Sep 2026 baselines for the campaign names (all already exist in GA4):
   - world_ai_summit_2026_delegate: 28 sessions, 0 key events
   - world_ai_awards_2026: 70 sessions, 3 key events
   - world_ai_summit_2026_sponsorship: 768 sessions, 21 key events
   - world_ai_summit_2026: 2,174 sessions, 97 key events
   - Direct/(none): 293 key events. This should fall as untagged mailer clicks disappear.
6. Why the sponsor CTA stays on /partnership.html. The page body shows only three email addresses and no visible form. Even so, sessions that landed there produced 153 partnership_form_submit events (132 users), so the form is reached from that page by navigation or a pop-up (inferred). Keep it as the landing page, and use the deck line as the direct route.

------------------------------------------------------------
F. ASK FOR THE ELETS ESP TEAM
------------------------------------------------------------
Please check whether link-scanning security tools are triggering r.emails.elets.in clicks. Typical signs are clicks within seconds of delivery and every link in one email clicked. Excluding these clicks cleans the ESP click report only. GA4 reporting still needs the engagement-time segment in E3.

------------------------------------------------------------
G. QA FOR EACH TEMPLATE, BEFORE EACH SEND
------------------------------------------------------------
1. Send a test to one Gmail inbox and one Outlook desktop inbox.
2. Click every World AI Summit link. After the r.emails.elets.in redirect, the final address must keep all four utm_ parameters and must not contain "<", ">" or spaces.
3. /delegate/ and /awards/ must keep the trailing slash.
4. Open GA4 Realtime and confirm it shows elets_mailer / email with the correct campaign and utm_content.
5. Confirm that no price, fee, discount, deadline or speaker name appears unless its placeholder above has been cleared.
