# A74: World AI Summit 2026: LinkedIn showcase refresh, LinkedIn Event, post footers and pinned post

- **For recommendation:** Turn the LinkedIn showcase into a pass-sales page and add a LinkedIn Event that links to /delegate/
- **Research lens:** missing-levers
- **Format:** Plain-text copy blocks for the LinkedIn admin UI (showcase tagline, About, button, Event form, post footers, pinned post, share kit), plus a UTM key. Indian English. No code, JSON-LD or redirects are needed for this asset.
- **Placeholders the business must fill:**
  - PLACEHOLDER_EDITION - choose 2nd or 3rd (the showcase About says 2nd; LinkedIn posts since July say 3rd) and use it everywhere
  - PLACEHOLDER_START_TIME - day 1 start time in IST (allevents.in says 9:00 am, not confirmed)
  - PLACEHOLDER_END_TIME - day 2 end time in IST (allevents.in says 6:00 pm, not confirmed)
  - PLACEHOLDER_LATE_ACCESS_GENERAL_PRICE - current General pass price (/delegate/ showed Rs 30,000 on 1 Oct)
  - PLACEHOLDER_LATE_ACCESS_VIP_PRICE - current VIP pass price (/delegate/ showed Rs 60,000 on 1 Oct)
  - PLACEHOLDER_GST_WORDING - for example 'plus GST' or 'inclusive of GST', matching /delegate/
  - PLACEHOLDER_LATE_ACCESS_END_DATE - last date Late Access pricing applies
  - PLACEHOLDER_AWARD_DEADLINE - World AI Awards 2026 nomination closing date
  - PLACEHOLDER_AWARD_FEE - 2026 nomination fee (the 2025 fee was Rs 18,000 + GST per entry; confirm 2026)
  - PLACEHOLDER_CONFIRMED_SPEAKERS_TO_TAG - only speakers confirmed for 2026 who agree to be tagged
  - PLACEHOLDER_LINKEDIN_EVENT_URL - the URL of the Event once it is created
  - PLACEHOLDER_FIRST_NAME - first name of the speaker or exhibitor receiving the share kit
  - PLACEHOLDER_SESSION_TITLE - the speaker's confirmed session title
  - PLACEHOLDER_STAND_OR_PARTNER_ROLE - the exhibitor's stand number or partner category

## How to ship

Owner: the Elets marketing or social team member who has admin rights on linkedin.com/showcase/world-ai-summit/. Total time is 1-2 hours.

Order of work:
(1) Do step 0 first, with the web team. Check that checkout on /delegate/ actually works. Remove the expired Early Bird (2025) and Standard (30 Sept 2026) tiers. Make the homepage price match the Late Access price. Ask allevents.in to replace its "from Rs 20,000" price. Confirm the event times. Choose the edition number.
(2) By 3 Oct: paste the tagline (section 1) and the About (section 2). Use the 170-character short version only if the editor rejects the full text. Set the Website field and the Register button (section 3). Publish and pin the post in section 6.
(3) By 4 Oct: create the in-person LinkedIn Event (section 4). Check the format before posting, because it cannot be changed later. If the in-person form has no external registration link, leave registration off and rely on the link in the first line of the description. Do not use LinkedIn's own registration form unless someone will export and follow up those leads every day.
(4) Once the Event is live, send the share kit (section 7) only to speakers confirmed for 2026 (see worldaisummit/speakers/speakers.json) and to exhibitors.
(5) Until 15 Oct, end every post with footer A, B or C from section 5. Use footer C on only one or two posts.
(6) After 7 days, check GA4 for sessions on /delegate/ with campaign wais2026 and source linkedin, broken down by utm_content.

Corrections from the recommendation, checked on 1 Oct:
- For 'world ai summit', the showcase is #6 organic, not #5. An AI Overview, a People Also Ask block and answer boxes sit above it, so its click-through rate is probably low (inferred). It is #2 for 'world ai summit bengaluru'.
- Google does not show the stale "Stay tuned" text. Only people who open the showcase see it.
- The Website field already leads to the homepage, so this change saves visitors one step rather than rescuing a dead end.
- KDEM is confirmed as 2026 Strategic Partner by a LinkedIn post dated 7 Sep 2026.

Sources:
- Venue address: https://www.hotelplanner.com/Hotels/178731/Reservations-Sheraton-Bangalore-Hotel-at-Brigade-Gateway-Bangalore-26-1-Dr-Rajkumar-Rd-Malleswaram-Rajajinagar-560055
- Event field limits and registration options: https://www.linkedin.com/help/linkedin/answer/a554183 and https://leadsbridge.com/blog/linkedin-events/
- Tagline and showcase description limits: https://clearviewsocial.com/blog/guide-linkedin-character-counts-limits/

No JSON-LD, redirects or site file edits are part of this asset. No OpenSEO paid tools were used.

## Content

=====================================================================
0. BEFORE YOU PASTE (marketing + web team, about 15 minutes)
=====================================================================
a) CHECKOUT: Open https://www.worldaisummit.com/delegate/ on desktop and on mobile and go through checkout to the payment step. When the page was fetched on 1 Oct it had a "Checkout" heading but no visible payment form or button. These may load through JavaScript, which we could not check. If checkout does not work, point the Website field, the button and the footers at https://www.worldaisummit.com/ (same UTM tags) until it is fixed.
b) PRICES MUST MATCH: /delegate/ still shows "Early Bird ... Valid till 25th July 2025" and "Standard Access (Valid till 30th Sept 2026)". Remove both so that only Late Access shows (on 1 Oct: Rs 30,000 General / Rs 60,000 VIP). The homepage still says "Premium Rs 20,000", so change it to match. allevents.in calls itself "the official ticketing partner" and shows "Tickets on approval from Rs 20,000", so ask them to update it. Until all three agree, the pinned post below will contradict them.
c) TIMES: The 9:00 am to 6:00 pm IST times come only from allevents.in. Confirm them before you create the Event.
d) EDITION: The showcase About says 2nd edition. Posts since July say 3rd. Pick one, use it in PLACEHOLDER_EDITION, and use it everywhere from now on.
e) OLD LINKS: Open the lnkd.in links in recent posts (for example lnkd.in/dUJkvwSw, 30 Jul) and note where they lead. Stop using "Express your interest" and "Register your interest" from today.
f) Fill every PLACEHOLDER_ marker. Do not publish anything that still has a marker in it.

=====================================================================
1. SHOWCASE TAGLINE (119 of 120 characters)
=====================================================================
World AI Summit 2026 | Bengaluru, India | 14-15 Oct | Delegate passes, sponsorship & World AI Awards: worldaisummit.com

Note: On 1 Oct, Google's snippet for "world ai summit" was "4912 followers on LinkedIn. Where India & the World Converge to Shape the AI Decade | The Future of AI Begins Here." This looks like the current tagline (inferred), so the tagline affects the snippet as much as the About does.

=====================================================================
2. SHOWCASE ABOUT / OVERVIEW (replace the whole text; 858 characters; the first 300 include the pass link)
=====================================================================
World AI Summit 2026 takes place on 14-15 October 2026 at the Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru, India. Organised by Elets Technomedia, with Karnataka Digital Economy Mission (KDEM) as Strategic Partner. Delegate passes: worldaisummit.com/delegate/ (10% off for groups of 3+).

Theme: AI for All: Accelerating India's Journey Towards Inclusive, Responsible and Future-Ready AI.

This is the PLACEHOLDER_EDITION edition of World AI Summit.

Sponsorship & exhibition: partnerships@worldaisummit.com
Speaking: secretariat@worldaisummit.com
Registration help: registration@worldaisummit.com
World AI Awards nominations: worldaisummit.com/awards/

Venue: Sheraton Grand Bangalore Hotel at Brigade Gateway, 26/1 Dr Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru, Karnataka 560055.

Not to be confused with World Summit AI (Amsterdam).

SHORT VERSION (170 characters). One guide lists a 200-character limit for showcase descriptions. Use this only if the editor will not accept the full text:
World AI Summit 2026: 14-15 Oct, Sheraton Grand Bangalore at Brigade Gateway, Bengaluru. By Elets Technomedia, KDEM Strategic Partner. Passes: worldaisummit.com/delegate/

=====================================================================
3. WEBSITE FIELD AND CUSTOM BUTTON
=====================================================================
The Website field already points to worldaisummit.com. This change only saves visitors the step from the homepage to /delegate/.
Website field:
https://www.worldaisummit.com/delegate/?utm_source=linkedin&utm_medium=social&utm_campaign=wais2026&utm_content=showcase_website
Custom button label: Register
Custom button URL:
https://www.worldaisummit.com/delegate/?utm_source=linkedin&utm_medium=social&utm_campaign=wais2026&utm_content=showcase_button

=====================================================================
4. LINKEDIN EVENT (live by 4 Oct)
=====================================================================
Host: World AI Summit showcase page. If the admin UI does not offer the showcase as an organiser, create the Event from the parent company page.
Event type/format: In person. Check this before posting, because the type and format cannot be changed afterwards (LinkedIn Help a554183).
Event name (31 of 75 characters): World AI Summit 2026, Bengaluru
Venue: Sheraton Grand Bangalore Hotel at Brigade Gateway
Address: 26/1 Dr Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru, Karnataka 560055
Timezone: (UTC+05:30) India Standard Time
Start: 14 Oct 2026, PLACEHOLDER_START_TIME (allevents.in says 9:00 am)
End: 15 Oct 2026, PLACEHOLDER_END_TIME (allevents.in says 6:00 pm)
Registration:
- If the form offers an external registration link for this in-person event, paste:
  https://www.worldaisummit.com/delegate/?utm_source=linkedin&utm_medium=social&utm_campaign=wais2026&utm_content=li_event
- If it does not (LinkedIn documents the external link mainly for online events), leave registration off. The same link is already the first line of the description below.
- Only switch on LinkedIn's own registration form if someone will export those leads and follow them up every day. Those sign-ups never reach /delegate/.
Speakers to tag: PLACEHOLDER_CONFIRMED_SPEAKERS_TO_TAG. Tag only speakers who are confirmed for 2026 and have agreed to be tagged. Do not add anyone from memory.

Event description (1,428 of 5,000 characters):
Book your delegate pass: https://www.worldaisummit.com/delegate/?utm_source=linkedin&utm_medium=social&utm_campaign=wais2026&utm_content=li_event

World AI Summit 2026 takes place on 14-15 October 2026 at the Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. It is organised by Elets Technomedia, with Karnataka Digital Economy Mission (KDEM) as Strategic Partner. This is the PLACEHOLDER_EDITION edition of the summit.

Theme: AI for All: Accelerating India's Journey Towards Inclusive, Responsible and Future-Ready AI.

Delegate passes (Late Access)
- General: Rs PLACEHOLDER_LATE_ACCESS_GENERAL_PRICE PLACEHOLDER_GST_WORDING
- VIP: Rs PLACEHOLDER_LATE_ACCESS_VIP_PRICE PLACEHOLDER_GST_WORDING
- Groups of three or more delegates get 10% off.

Clicking Attend on this LinkedIn page adds you to the attendee list and sends you event reminders. It does not book a pass. To attend the summit, please book through the link above.

Exhibit or sponsor: partnerships@worldaisummit.com
Speak at the summit: secretariat@worldaisummit.com
Registration help: registration@worldaisummit.com
Nominate for the World AI Awards: https://www.worldaisummit.com/awards/?utm_source=linkedin&utm_medium=social&utm_campaign=wais2026&utm_content=li_event (nominations close PLACEHOLDER_AWARD_DEADLINE)

Venue: Sheraton Grand Bangalore Hotel at Brigade Gateway, 26/1 Dr Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru, Karnataka 560055.

=====================================================================
5. POST FOOTERS (every post from today to 15 Oct; they replace "Express/Register your interest" and the lnkd.in links)
=====================================================================
LinkedIn may show these links as lnkd.in short links. That is expected, and the UTM tags still reach the site. What matters is the destination and the wording.

A) Standard footer (every post):
Book your delegate pass: https://www.worldaisummit.com/delegate/?utm_source=linkedin&utm_medium=social&utm_campaign=wais2026&utm_content=post | Exhibit/sponsor: partnerships@worldaisummit.com

B) Sponsor and exhibitor announcement posts:
Exhibit or sponsor: partnerships@worldaisummit.com
Book your delegate pass: https://www.worldaisummit.com/delegate/?utm_source=linkedin&utm_medium=social&utm_campaign=wais2026&utm_content=post_sponsor

C) Awards posts (use on one or two posts only):
Nominate for the World AI Awards: https://www.worldaisummit.com/awards/?utm_source=linkedin&utm_medium=social&utm_campaign=wais2026&utm_content=post_awards (nominations close PLACEHOLDER_AWARD_DEADLINE; entry fee PLACEHOLDER_AWARD_FEE)
Book your delegate pass: https://www.worldaisummit.com/delegate/?utm_source=linkedin&utm_medium=social&utm_campaign=wais2026&utm_content=post

=====================================================================
6. PINNED POST (publish and pin by 3 Oct, only after step 0b is done)
=====================================================================
World AI Summit 2026 | 14-15 October 2026 | Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru

The PLACEHOLDER_EDITION edition of World AI Summit is organised by Elets Technomedia, with Karnataka Digital Economy Mission (KDEM) as Strategic Partner. Theme: AI for All: Accelerating India's Journey Towards Inclusive, Responsible and Future-Ready AI.

Delegate passes (Late Access, available until PLACEHOLDER_LATE_ACCESS_END_DATE)
- General: Rs PLACEHOLDER_LATE_ACCESS_GENERAL_PRICE PLACEHOLDER_GST_WORDING
- VIP: Rs PLACEHOLDER_LATE_ACCESS_VIP_PRICE PLACEHOLDER_GST_WORDING
- Groups of three or more delegates get 10% off.

Book your pass: https://www.worldaisummit.com/delegate/?utm_source=linkedin&utm_medium=social&utm_campaign=wais2026&utm_content=pinned

Registration help: registration@worldaisummit.com
Sponsorship and exhibition: partnerships@worldaisummit.com
Speaking: secretariat@worldaisummit.com

World AI Awards nominations: https://www.worldaisummit.com/awards/?utm_source=linkedin&utm_medium=social&utm_campaign=wais2026&utm_content=pinned_awards

(Team note, not for the post: on 1 Oct /delegate/ showed Late Access at Rs 30,000 General and Rs 60,000 VIP. The figures in this post must match /delegate/, the homepage and allevents.in on the day it goes live.)

=====================================================================
7. SHARE KIT FOR CONFIRMED SPEAKERS AND EXHIBITORS (send once the Event is live)
=====================================================================
Message to send:
Hello PLACEHOLDER_FIRST_NAME, World AI Summit 2026 now has a LinkedIn event page: PLACEHOLDER_LINKEDIN_EVENT_URL. It would help us a great deal if you could share it with a line about your participation. A suggested post is below; please edit it as you like.

Suggested speaker post:
I will be speaking at World AI Summit 2026 in Bengaluru on 14-15 October, on PLACEHOLDER_SESSION_TITLE. The summit is organised by Elets Technomedia at the Sheraton Grand Bangalore Hotel at Brigade Gateway. Event page: PLACEHOLDER_LINKEDIN_EVENT_URL
Delegate passes: https://www.worldaisummit.com/delegate/?utm_source=linkedin&utm_medium=social&utm_campaign=wais2026&utm_content=speaker_share

Suggested exhibitor or sponsor post:
We will be at World AI Summit 2026 in Bengaluru on 14-15 October (PLACEHOLDER_STAND_OR_PARTNER_ROLE). The summit is organised by Elets Technomedia at the Sheraton Grand Bangalore Hotel at Brigade Gateway. Event page: PLACEHOLDER_LINKEDIN_EVENT_URL
Delegate passes: https://www.worldaisummit.com/delegate/?utm_source=linkedin&utm_medium=social&utm_campaign=wais2026&utm_content=exhibitor_share

=====================================================================
8. UTM KEY (for GA4: session source = linkedin, session campaign = wais2026)
=====================================================================
utm_content values: showcase_website, showcase_button, li_event, post, post_sponsor, post_awards, pinned, pinned_awards, speaker_share, exhibitor_share. The base pages are /delegate/ for passes and /awards/ for award nominations.
