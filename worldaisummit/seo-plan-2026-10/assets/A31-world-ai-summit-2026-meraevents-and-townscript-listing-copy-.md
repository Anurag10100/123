# A31: World AI Summit 2026: MeraEvents and Townscript listing copy, plus redirect lines for the 2025 pages

- **For recommendation:** Update the 2025 MeraEvents and Townscript pages for 2026 (organiser accounts already exist)
- **Research lens:** events-aggregators
- **Format:** Plain text to paste into the MeraEvents and Townscript organiser dashboards. Field values first, then the "About The Event" / description body (one body, two UTM variants), then the lines for the old 2025 pages. There is no JSON-LD because neither platform accepts custom structured data, so the verified street address goes in the venue fields instead.
- **Placeholders the business must fill:**
  - PLACEHOLDER_CURRENT_PASS_PRICE: the current Late Access price on /delegate/ (Rs 30,000 or Rs 60,000; confirm which variant applies). Never Rs 20,000.
  - PLACEHOLDER_SALE_END_DATE: the last day of on-platform ticket sales, only if Option 2 (ticket on the platform) is used
  - PLACEHOLDER_DAILY_TIMINGS: confirmed start and end times for each day (9:00 AM–6:00 PM is suggested but not verified)
  - PLACEHOLDER_AWARD_DEADLINE: the World AI Awards 2026 nomination deadline
  - PLACEHOLDER_NEW_MERAEVENTS_URL: only needed if ID 266617 cannot be re-dated and a new 2026 event is created
  - PLACEHOLDER_NEW_TOWNSCRIPT_URL: the URL of the new Townscript 2026 event once it is published

## How to ship

Owner: marketing / registration team. Time: about 1–2 hours. Do it by 4 Oct 2026.

1) MeraEvents: in the organiser dashboard, open event ID 266617 (/event/worldaisummit). Enter the Section A fields and paste Section B into "About The Event", which is empty now. We have not checked whether MeraEvents lets you move an ended event to new dates. If it does not, create a new 2026 event with the same copy and put the Section C line, with the new URL, on 266617. Put the Section C line on 266543 either way.

2) Townscript: create a new event "World AI Summit 2026" using the Section A fields and the Section B copy, with utm_source=townscript. Publish it. Then add the Section C Townscript line to the top of the 2025 event description. How quickly Townscript publishes has not been checked.

3) Tickets: Option 1 is preferred (external link to /delegate/, no ticket on the platform). It keeps a single price list. If you choose Option 2, use the current Late Access price. The Standard tier (Rs 20,000/35,000) ended on 30 Sept 2026, and Late Access is Rs 30,000/60,000 according to /delegate/ on 1 Oct. Confirm which of the two figures applies. Do not use the 2025 Rs 20,000 or the homepage's "Premium Rs 20,000"; either would undercut the site's own pass page.

4) Before publishing, a person must confirm the speaker list. All 10 names are marked confirmed_2026=true in worldaisummit/speakers/speakers.json. No bios are included. Names that file flags as uncertain (for example Sanjeev Rastogi's role change and Sushan Rungta's designation) were left out. Delete any name that has since dropped out.

5) Measure it in GA4 by source meraevents / townscript, campaign world_ai_summit_2026. utm_content separates the new listing (listing_2026) from the old 2025 pages (listing_2025).

Changes made after verification:
- The copy no longer claims these pages win brand searches. In Google India, worldaisummit.com is #1 and neither platform appears in the top 20 for 'world ai summit tickets'. Expect a small amount of referral traffic from people browsing the platforms, not SEO gains.
- The edition number is removed. '3rd' conflicts with the site's /1st-edition/ archive.
- No Rs 20,000 price appears anywhere in the copy.

Still not verified: whether MeraEvents allows re-dating an ended event or requires approval for paid events, how fast Townscript publishes, the rel attribute on outbound links, whether these listings feed Google's event results, and the daily timings.

Venue address checked by WebSearch on 1 Oct 2026: 26/1 Dr. Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru 560055. Sources: https://www.marriott.com/en-us/hotels/blrgs-sheraton-grand-bangalore-hotel-at-brigade-gateway/overview/ and https://www.hotelplanner.com/Hotels/178731/Reservations-Sheraton-Bangalore-Hotel-at-Brigade-Gateway-Bangalore-26-1-Dr-Rajkumar-Rd-Malleswaram-Rajajinagar-560055. No OpenSEO credits were used.

On your question about CPUs: this session's container has 4 CPUs (nproc). I can't add more from here. Compute is set by the cloud environment, not by this session.

## Content

=====================================================================
A. LISTING FIELDS (same on MeraEvents ID 266617 and the new Townscript event)
=====================================================================

Event title:
World AI Summit 2026 – Bengaluru, 14–15 Oct

Dates:
14 October 2026 to 15 October 2026, PLACEHOLDER_DAILY_TIMINGS (the recommendation suggests 9:00 AM–6:00 PM, but this has not been checked against the agenda)

Venue name:
Sheraton Grand Bangalore Hotel at Brigade Gateway

Venue address:
26/1 Dr. Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru, Karnataka 560055, India

Category: Conference / Technology
Organiser: Elets Technomedia

Short summary (listing card, under 200 characters):
World AI Summit 2026, 14–15 October, Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. Seven tracks on AI in government, enterprise and GCCs. Organised by Elets Technomedia.

Ticket (choose one, see ship notes):
Option 1 (preferred): no ticket on the platform. Set registration to the external link below.
Option 2: a ticket named "Delegate Pass – Late Access", price PLACEHOLDER_CURRENT_PASS_PRICE, sales end PLACEHOLDER_SALE_END_DATE. Do not use Rs 20,000.

External registration link:
MeraEvents: https://www.worldaisummit.com/delegate/?utm_source=meraevents&utm_medium=event_listing&utm_campaign=world_ai_summit_2026&utm_content=listing_2026
Townscript: https://www.worldaisummit.com/delegate/?utm_source=townscript&utm_medium=event_listing&utm_campaign=world_ai_summit_2026&utm_content=listing_2026

=====================================================================
B. ABOUT THE EVENT / DESCRIPTION
(MeraEvents version shown. For Townscript, replace every "utm_source=meraevents" with "utm_source=townscript".)
=====================================================================

World AI Summit 2026 takes place on 14–15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. The summit is organised by Elets Technomedia. Over two days, policymakers, enterprise technology leaders, founders and investors will discuss how AI is being built, governed and put into production in India.

Programme: seven tracks
- Frontier Models & Compute
- Sovereign AI & Geopolitics
- Enterprise AI in Production
- GCCs
- Robotics, Agents & Embodied AI
- AI for Bharat
- Capital, Founders & Exits

Confirmed speakers include
- Pankaj Kumar Pandey, IAS – Principal Secretary, e-Governance, Government of Karnataka
- T Bhoobalan, IAS – CEO, Centre for e-Governance, Government of Karnataka
- Sanjeev Gupta – CEO, Karnataka Digital Economy Mission
- Ram Mohan Rao – Executive Director, SEBI
- Mahesh Hariharan Iyer – VP Engineering, Reserve Bank Innovation Hub
- Sandeep Varaganti – CEO, JioMart, Reliance Retail
- Tulshekar Gangireddy – ED and Head of Data Strategy, JPMorgan Chase
- Vijaya Kadiyala – Executive Director, DBS Bank
- Deepika Sandeep – Head, AI/ML CoE, HSBC
- Shashank Randev – Founder and General Partner, 247VC

Full speaker list: https://www.worldaisummit.com/speaker.html?utm_source=meraevents&utm_medium=event_listing&utm_campaign=world_ai_summit_2026&utm_content=listing_2026

Who attends
CIOs, CTOs, CDOs and heads of data and AI; GCC leaders; government and regulatory officials; founders and investors.

Delegate passes
Current pass: PLACEHOLDER_CURRENT_PASS_PRICE (Late Access).
Groups of three or more delegates receive 10% off.
Book on the official pass page:
https://www.worldaisummit.com/delegate/?utm_source=meraevents&utm_medium=event_listing&utm_campaign=world_ai_summit_2026&utm_content=listing_2026

World AI Awards
Nominations are open at https://www.worldaisummit.com/awards/?utm_source=meraevents&utm_medium=event_listing&utm_campaign=world_ai_summit_2026&utm_content=listing_2026
Last date for nominations: PLACEHOLDER_AWARD_DEADLINE.

Venue
Sheraton Grand Bangalore Hotel at Brigade Gateway
26/1 Dr. Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru, Karnataka 560055

Contact
Registration: registration@worldaisummit.com
Sponsorship and exhibition: partnerships@worldaisummit.com
Secretariat: secretariat@worldaisummit.com

=====================================================================
C. LINE FOR THE 2025 PAGES (put it first in each description)
=====================================================================

MeraEvents ID 266543 (and 266617 too if it cannot be re-dated):
This was the 2025 edition. World AI Summit 2026 takes place on 14–15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. Passes: https://www.worldaisummit.com/delegate/?utm_source=meraevents&utm_medium=event_listing&utm_campaign=world_ai_summit_2026&utm_content=listing_2025

If a new 2026 MeraEvents event had to be created, add this sentence:
The 2026 listing is here: PLACEHOLDER_NEW_MERAEVENTS_URL

Townscript /e/world-ai-summit2025-113433:
This was the 2025 edition. World AI Summit 2026 takes place on 14–15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. Book here: PLACEHOLDER_NEW_TOWNSCRIPT_URL or https://www.worldaisummit.com/delegate/?utm_source=townscript&utm_medium=event_listing&utm_campaign=world_ai_summit_2026&utm_content=listing_2025
