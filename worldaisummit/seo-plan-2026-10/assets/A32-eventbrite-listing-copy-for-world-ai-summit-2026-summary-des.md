# A32: Eventbrite listing copy for World AI Summit 2026: summary, description (utm_source=eventbrite), venue, category and tags

- **For recommendation:** Eventbrite: correct the 10:00 AM start, make it a two-day event, and tag it for the Bangalore AI browse pages
- **Research lens:** events-aggregators
- **Format:** Plain text in labelled blocks, one per Eventbrite field. Paste each block into its own field in Eventbrite Manage events > Basic info / Details. The description uses plain lines and hyphen bullets so it pastes cleanly into Eventbrite's rich-text editor. Bold the section headings in the editor after pasting.
- **Placeholders the business must fill:**
  - PLACEHOLDER_PASS_FROM_PRICE: lowest pass price on sale from 1 Oct 2026. Standard (Rs 20,000/35,000) expired 30 Sept per /delegate/; Late Access is Rs 30,000/60,000; the homepage still shows Premium Rs 20,000.
  - PLACEHOLDER_PASS_TIERS: one line naming the current tiers and prices, and whether GST is extra.
  - PLACEHOLDER_DAY1_START / PLACEHOLDER_DAY1_END: Day 1 (14 Oct) times from the agenda owner. 10:00 AM is what Eventbrite shows now; AllEvents' 9:00 AM is unverified.
  - PLACEHOLDER_DAY2_START / PLACEHOLDER_DAY2_END: Day 2 (15 Oct) times from the agenda owner.
  - PLACEHOLDER_AWARD_DEADLINE: World AI Awards nomination deadline (not published on /awards/).
  - PLACEHOLDER_AWARD_FEE: 2026 fee per entry (2025 was Rs 18,000 + GST).
  - PLACEHOLDER_SPEAKER_SIGNOFF: delete this line once the speakers team confirms all 15 listed speakers are still attending.

## How to ship

Owner: marketing, by 3 Oct 2026. Time needed is under an hour, plus a reply from the agenda owner.

1) Fill the placeholders. The biggest gap is the pass price. /delegate/ shows the Standard tier (Rs 20,000/35,000) valid only until 30 Sept 2026. Late Access is Rs 30,000/60,000, but the homepage still says "Premium Rs 20,000". Decide the current lowest price, use the same figure on Eventbrite, the homepage and /delegate/, and keep the summary at 140 characters or fewer. The award deadline and fee are not published on /awards/ (the 2025 fee was Rs 18,000 + GST), so the awards team has to supply both.

2) Timings (verifier correction 2). Do not change the start to 9:00 AM. That time comes only from AllEvents, which was probably entered by the same team. The listing's 10:00 AM start was observed on the Eventbrite browse page on 1 Oct, but the true start time is unconfirmed. Get the day 1 and day 2 start and end times from the agenda owner. Then check in Manage events whether the listing ends on 15 Oct. If it is set as a one-day event, make it a single event running 14 Oct to 15 Oct. Do not create two separate dates.

3) Venue (verifier correction 1). Only check the pin; there is no known geocoding fault. The "Harohalli" browse page is Eventbrite's nearby-area page and also lists events at central Bengaluru venues. Fix the pin only if the map is visibly off. The address comes from Google Hotels and Apple Maps via Exa, 1 Oct 2026: "26/1, Dr Rajkumar Rd, Malleswaram, Rajajinagar, Bengaluru, Karnataka 560055", coordinates 13.01247, 77.55484.

4) Paste fields 1, 2, 4 and 5. The 140-character summary limit is confirmed in Eventbrite's platform docs (eventbrite.com/platform/docs/create-events). Expect only a small effect from the tags (verifier corrections 3 and 4). On the live Google India results for "ai events in bangalore october 2026", eventbrite.com/d/india--bangalore/artificial-intelligence/ ranks #7. /tech-conferences/ is not in the top 20, and no one has checked whether WAIS currently appears on either browse page.

5) Speakers. The 15 names come from worldaisummit/speakers/speakers.json, where all are marked confirmed_2026: true with high bio confidence. Only names, roles and organisations are used, and there are no bios. Before publishing, replace PLACEHOLDER_SPEAKER_SIGNOFF by deleting the line once the speakers team confirms that everyone listed is still attending. Do not add any unconfirmed names.

6) After saving, open the public listing and check three things: the UTM links work, the 10% group discount text matches the /delegate/ page, and the organiser profile reads Elets Technomedia. Write the exact eventbrite.com/e/ URL, the price shown and the time shown into the OpenSEO project context. None of these could be fetched here.

7) Higher priority (verifier finding 6). conferencealerts.in/bangalore/ai ranks #3 for "ai events in bangalore october 2026" and WAIS is not listed there. Submit that listing with the same copy and utm_source=conferencealerts before spending more time on Eventbrite.

Not applicable to this asset: schema.org JSON-LD and redirects. Eventbrite generates its own event markup, and nothing on worldaisummit.com changes. No files were edited and no paid OpenSEO tools were used.

On your separate question about CPUs: this session's container has 4 CPUs (nproc), and I cannot add more from here.

## Content

=== FIELD 1: SUMMARY (Eventbrite limit is 140 characters) ===
World AI Summit 2026 by Elets Technomedia – 14–15 Oct, Sheraton Grand Bangalore. 7 AI tracks, expo & World AI Awards. Passes from Rs PLACEHOLDER_PASS_FROM_PRICE.

(When the price is a six-character figure such as "30,000", the line is exactly 140 characters. Do not add anything else to it.)

=== FIELD 2: DESCRIPTION / OVERVIEW ===
About World AI Summit 2026

World AI Summit 2026 is a two-day conference and expo on artificial intelligence, organised by Elets Technomedia. It takes place on Wednesday 14 and Thursday 15 October 2026 at the Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru.

The summit brings together government and policy leaders, enterprise technology heads, global capability centre (GCC) leaders, founders and investors. The sessions cover how AI is built, governed and put to work in India.

Seven tracks
- Frontier Models & Compute
- Sovereign AI & Geopolitics
- Enterprise AI in Production
- GCCs (Global Capability Centres)
- Robotics, Agents & Embodied AI
- AI for Bharat
- Capital, Founders & Exits

Confirmed speakers include
- Pankaj Kumar Pandey, IAS – Principal Secretary, e-Governance, Government of Karnataka
- Dr Ravikumar Surpur, IAS – Secretary, IT & Communication, Government of Rajasthan
- Sanjeev Gupta – CEO, Karnataka Digital Economy Mission
- Ram Mohan Rao – Executive Director, SEBI
- Mahesh Hariharan Iyer – VP Engineering, Reserve Bank Innovation Hub
- Sandeep Varaganti – CEO, JioMart, Reliance Retail
- Tulshekar Gangireddy – Executive Director and Head of Data Strategy, JPMorgan Chase
- Pawan Sachdeva – Senior Managing Director and Technology Head India, Carelon Global Solutions
- Suman Guha – Chief Digital and Technology Officer, Croma
- Harsh Vardhan – Global Head, AI and Digital Innovation, Apollo Tyres
- Dipayan Chakraborty – Head, India Analytics Center, eBay
- Deepika Sandeep – Head, AI/ML CoE, HSBC
- Joyce Rodriguez – Head of Digital Cybersecurity, Airbus India
- Sandhya Vasudevan – Board Member, TiE Bangalore
- Shashank Randev – Founder and General Partner, 247VC
PLACEHOLDER_SPEAKER_SIGNOFF

Full speaker list: https://www.worldaisummit.com/speaker.html?utm_source=eventbrite&utm_medium=event_listing&utm_campaign=world_ai_summit_2026&utm_content=speakers

Timings (IST)
- Day 1, Wednesday 14 October 2026: PLACEHOLDER_DAY1_START to PLACEHOLDER_DAY1_END
- Day 2, Thursday 15 October 2026: PLACEHOLDER_DAY2_START to PLACEHOLDER_DAY2_END

World AI Awards
The World AI Awards are part of the summit. Nominations are open at https://www.worldaisummit.com/awards/?utm_source=eventbrite&utm_medium=event_listing&utm_campaign=world_ai_summit_2026&utm_content=awards
Last date for nominations: PLACEHOLDER_AWARD_DEADLINE. Fee per entry: PLACEHOLDER_AWARD_FEE.

Delegate passes
Passes start at Rs PLACEHOLDER_PASS_FROM_PRICE. PLACEHOLDER_PASS_TIERS
Groups of three or more delegates get 10% off.
Book your pass: https://www.worldaisummit.com/delegate/?utm_source=eventbrite&utm_medium=event_listing&utm_campaign=world_ai_summit_2026&utm_content=passes
Registration queries: registration@worldaisummit.com

Sponsorship and exhibition
For sponsorship, exhibition and partnership enquiries, write to partnerships@worldaisummit.com

Venue
Sheraton Grand Bangalore Hotel at Brigade Gateway
26/1, Dr Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru, Karnataka 560055

Organiser
Elets Technomedia. General enquiries: secretariat@worldaisummit.com
Event website: https://www.worldaisummit.com/?utm_source=eventbrite&utm_medium=event_listing&utm_campaign=world_ai_summit_2026&utm_content=website

=== FIELD 3: LOCATION (check only, do not re-enter unless it is wrong) ===
Venue name: Sheraton Grand Bangalore Hotel at Brigade Gateway
Address: 26/1, Dr Rajkumar Road, Malleswaram-Rajajinagar
City: Bengaluru
State: Karnataka
PIN: 560055
Country: India
Map pin should sit at about 13.0125, 77.5548 (Brigade Gateway, Rajajinagar).

=== FIELD 4: CATEGORY, TYPE AND TAGS ===
Type: Conference
Category: Science & Technology
Sub-category: High Tech
Tags (Eventbrite allows up to 10): Artificial Intelligence, AI Conference, Generative AI, AI Summit, Enterprise AI, GCC, Tech Summit, Bangalore, Bengaluru

=== FIELD 5: EXTERNAL REGISTRATION / TICKET LINK (if tickets are not sold on Eventbrite) ===
https://www.worldaisummit.com/delegate/?utm_source=eventbrite&utm_medium=event_listing&utm_campaign=world_ai_summit_2026&utm_content=register_button
