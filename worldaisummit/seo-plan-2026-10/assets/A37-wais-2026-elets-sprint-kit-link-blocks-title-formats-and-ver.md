# A37: WAIS 2026 Elets sprint kit: link blocks, title formats and verified speaker lines (5 portals plus day-of pieces)

- **For recommendation:** Two-week Elets content sprint: speaker-led track previews per portal, then day-of and awards coverage that links to WAIS pages
- **Research lens:** elets-network
- **Format:** Editorial brief in plain text and Markdown, with HTML snippets to paste into the CMS
- **Placeholders the business must fill:**
  - PLACEHOLDER_AGENDA_FROM_PROGRAMME_TEAM
  - PLACEHOLDER_CURRENT_PASS_PRICE
  - PLACEHOLDER_GROUP_OFFER_CONFIRMED
  - PLACEHOLDER_EDITION_NUMBER
  - PLACEHOLDER_SURPUR_ORG_CONFIRMED
  - PLACEHOLDER_DAY2_REGISTRATION_OPEN
  - PLACEHOLDER_RECAP_URL
  - PLACEHOLDER_N
  - PLACEHOLDER_AWARD_CATEGORY
  - PLACEHOLDER_AWARD_DEADLINE
  - PLACEHOLDER_PUBLISH_DATE

## How to ship

Dependencies to clear before the first preview on 3 Oct:
1. The programme team sends the agenda with each speaker's track or session. Without it, every desk uses title Format B. speakers.json has session = null for all 76 entries, so it cannot support "will debate" or track framing.
2. Business decisions: the current pass tier and price (Standard closed on 30 Sept), whether the group offer still applies, the awards nomination deadline and categories, the edition number, and Dr Ravikumar Surpur's organisation.
3. The web team publishes a 2026 recap page by 16 Oct for block 1C. Until then, delete that line.

Shipping:
- Each Elets desk (BFSI, eGov, CIO, eHealth, Digital Learning) writes one preview between 3 and 12 Oct, using section 4 and fresh interview quotes. It pastes block 1A at the end of the body and sends the piece in that portal's newsletter with the 1D UTM links.
- The CIO desk, which ran the 2025 pattern, publishes the day-of pieces: 13 Oct (block 1A), 14 Oct evening (1B), 15 Oct awards winners (1C) and 16 Oct "concludes" (1C).
- Recheck confirmed_2026 in speakers.json on each publish day.

Measurement and expectations:
- GA4 records only key events. Transactions were 0 in both periods, so pass sales cannot be credited to these articles.
- In GA4, go to Traffic acquisition and filter session source containing "eletsonline" for 3 to 20 Oct. The newsletter shows under utm_campaign wais2026_sprint.
- Set expectations low. In 2025, cio.eletsonline.com sent about 20 to 50 sessions per article (238 in total). From 1 Aug to 30 Sep 2026 it sent none that GA4 could see, even though 3 to 4 WAIS articles were live.
- Ask the web team to check that cio.eletsonline.com does not send a no-referrer Referrer-Policy and that its links carry no rel="noreferrer". Either would hide the traffic.
- SEO value from these links is close to zero: eletsonline.com already supplies 19,511 of the site's 19,826 backlinks. The value lies in readers and the newsletters.

No JSON-LD or redirects are included. Event schema belongs on worldaisummit.com, not on Elets news articles, and this asset changes no URLs.

On your question about CPUs: this cloud session has 4 CPUs (nproc). I cannot add more to a running session. A new session starts on a fresh machine with its own allowance.

## Content

WORLD AI SUMMIT 2026: ELETS CONTENT SPRINT KIT
Prepared 1 October 2026. Previews run 3 to 12 Oct. Day-of pieces run 13 to 16 Oct.

=====================================================================
0. RULES FOR EVERY DESK (read before writing)
=====================================================================
1. Names, designations and organisations come only from worldaisummit/speakers/speakers.json. Copy them word for word as shown in section 4. On publish day, check again that each person still has confirmed_2026 = true.
2. Do not write biography sentences. A line about a speaker's background or views goes in only if the speaker said it in an interview with your desk, and you attribute it ("..., she told eletsonline.com" or similar).
3. Do not name a track, session, time or hall for any speaker. speakers.json has session = null for all 76 entries. Wording such as "will debate", "will speak on" or "on the X track" needs the agenda from the programme team (PLACEHOLDER_AGENDA_FROM_PROGRAMME_TEAM). Until you have it, use title Format B in section 2.
4. Do not quote any pass price. The Standard tier on /delegate/ was valid till 30 Sept 2026 and has now closed. If the business decides to state the current price, use PLACEHOLDER_CURRENT_PASS_PRICE. Otherwise, link to /delegate/ only. Mention the group offer (10% off for 3+ delegates) only if registration@ confirms it still applies: PLACEHOLDER_GROUP_OFFER_CONFIRMED.
5. Do not state an edition number. Some pages say 2nd and LinkedIn says 3rd. Use PLACEHOLDER_EDITION_NUMBER only after the organisers confirm it.
6. Do not describe government speakers as "Karnataka" or "KDEM" unless their own organisation in section 4 says so. Aman Mittal (MITRA, Maharashtra) and Hemant Garg (Ministry of Labour and Employment, Government of India) are not Karnataka. Dr Ravikumar Surpur's organisation is inferred in the file, so confirm it first (PLACEHOLDER_SURPUR_ORG_CONFIRMED).
7. Disclosure line, required in every piece: "Elets Technomedia, the publisher of this portal, organises World AI Summit."
8. Article body links use the clean URLs exactly as in section 1, with no UTM parameters. Do not add rel="noreferrer", because it hides the referral from GA4. If the CMS opens links in a new tab, use rel="noopener" only.

=====================================================================
1. LINK BLOCKS (paste at the end of the article body, above the author box)
=====================================================================

--- 1A. PRE-EVENT BLOCK: previews 3 to 12 Oct, and the 13 Oct "opens tomorrow" piece ---

<div class="wais-2026-links">
<p><strong>World AI Summit 2026</strong> takes place on 14–15 October 2026 at the Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. Elets Technomedia, the publisher of this portal, organises World AI Summit.</p>
<ul>
<li>See the full <a href="https://www.worldaisummit.com/speaker.html">World AI Summit 2026 speakers</a> list</li>
<li><a href="https://www.worldaisummit.com/delegate/">Register for World AI Summit 2026</a> (14–15 October, Bengaluru)</li>
<li><a href="https://www.worldaisummit.com/ai-conference-bengaluru-2026.html">AI conference in Bengaluru, October 2026</a></li>
<li><a href="https://www.worldaisummit.com/awards/">World AI Awards 2026</a></li>
</ul>
</div>

--- 1B. DAY 1 BLOCK: 14 Oct evening "Day 1 highlights" ---

<div class="wais-2026-links">
<p>World AI Summit 2026 continues on 15 October at the Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. Elets Technomedia, the publisher of this portal, organises World AI Summit.</p>
<ul>
<li>See the full <a href="https://www.worldaisummit.com/speaker.html">World AI Summit 2026 speakers</a> list</li>
<li><a href="https://www.worldaisummit.com/delegate/">Register for World AI Summit 2026</a> (14–15 October, Bengaluru)</li>
<li><a href="https://www.worldaisummit.com/awards/">World AI Awards 2026</a></li>
</ul>
</div>
[Keep the /delegate/ line only if registration for Day 2 is open: PLACEHOLDER_DAY2_REGISTRATION_OPEN. If it is not, delete that line.]

--- 1C. POST-EVENT BLOCK: 15 Oct awards winners and 16 Oct "concludes" ---

<div class="wais-2026-links">
<p>World AI Summit 2026 was held on 14–15 October 2026 at the Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. Elets Technomedia, the publisher of this portal, organises World AI Summit.</p>
<ul>
<li>See the full <a href="https://www.worldaisummit.com/speaker.html">World AI Summit 2026 speakers</a> list</li>
<li><a href="https://www.worldaisummit.com/awards/">World AI Awards 2026</a></li>
<li><a href="PLACEHOLDER_RECAP_URL">World AI Summit 2026 highlights</a></li>
<li><a href="https://www.worldaisummit.com/ai-conference-bengaluru-2026.html">AI conference in Bengaluru, October 2026</a></li>
</ul>
</div>
[PLACEHOLDER_RECAP_URL depends on the web team. As of 1 Oct there is no 2026 recap page, only the 2025 archive at /1st-edition/. Delete the highlights line until the page is live. Do not link to /delegate/ after the event.]

--- 1D. NEWSLETTER VERSION (same anchors, tagged URLs, for newsletter emails only) ---
Append to each worldaisummit.com URL in the newsletter only:
?utm_source=PORTAL&utm_medium=newsletter&utm_campaign=wais2026_sprint
PORTAL is one of: bfsi_eletsonline, egov_eletsonline, cio_eletsonline, ehealth_eletsonline, digitallearning_eletsonline
Example: https://www.worldaisummit.com/delegate/?utm_source=bfsi_eletsonline&utm_medium=newsletter&utm_campaign=wais2026_sprint

=====================================================================
2. TITLE FORMATS
=====================================================================

Format A. Use only after the programme team supplies the agenda with each speaker's track:
[Track from agenda]: What [N] Leaders Will Debate at World AI Summit 2026, Bengaluru
- [Track] must match the agenda wording. [N] counts only speakers the agenda places on that track.
- Example once confirmed: "Enterprise AI in Production: What PLACEHOLDER_N Leaders Will Debate at World AI Summit 2026, Bengaluru"

Format B. Safe to use now, because it needs only speakers.json:
[Sector]: [N] Leaders Confirmed for World AI Summit 2026, Bengaluru

Ready-to-use Format B titles. Recount N on publish day:
(1) bfsi.eletsonline.com: AI in Indian Banking: 10 BFSI Leaders Confirmed for World AI Summit 2026, Bengaluru
(2) egov.eletsonline.com: AI in Government: 6 Public-Sector Leaders Confirmed for World AI Summit 2026, Bengaluru
(3) cio.eletsonline.com: Enterprise AI and GCCs: 10 Technology Leaders Confirmed for World AI Summit 2026, Bengaluru
(4) ehealth.eletsonline.com: AI in Healthcare: Health IT Leaders Confirmed for World AI Summit 2026, Bengaluru
(5) digitallearning.eletsonline.com: AI in Education: Learning Leaders Confirmed for World AI Summit 2026, Bengaluru

Day-of titles. These follow the 2025 CIO pattern of "Kicks Off ... Tomorrow" on 24 Sep 2025 and "Concludes" on 29 Sep 2025:
- 13 Oct: World AI Summit 2026 Opens Tomorrow in Bengaluru
- 14 Oct (evening): World AI Summit 2026, Day 1: Highlights from Bengaluru
- 15 Oct: World AI Awards 2026 Winners: PLACEHOLDER_AWARD_CATEGORY [or "Full List"] Announced in Bengaluru
  (Category names must come from the awards team. /awards/ does not list categories as of 1 Oct.)
- 16 Oct: World AI Summit 2026 Concludes in Bengaluru

=====================================================================
3. STANDARD PARAGRAPHS (factual, for preview pieces)
=====================================================================

Opening context (adapt the first clause to your sector):
"World AI Summit 2026 will be held on 14–15 October 2026 at the Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. The programme is organised around seven themes: Frontier Models & Compute; Sovereign AI & Geopolitics; Enterprise AI in Production; GCCs; Robotics, Agents & Embodied AI; AI for Bharat; and Capital, Founders & Exits."

Speaker lead-in:
"Confirmed speakers include the following, as listed by the organisers on PLACEHOLDER_PUBLISH_DATE. Participation can change."

Interview quote frame (use only with a quote your desk collected):
"[Quote]," said [Name], [designation], [organisation], in an interview with [portal name].

Awards line for previews (use only once the deadline is confirmed):
"Nominations for the World AI Awards 2026 close on PLACEHOLDER_AWARD_DEADLINE."
If the deadline is not confirmed, leave this line out. The /awards/ link in the block is enough.

=====================================================================
4. VERIFIED SPEAKER LINES (copied from speakers.json, read 1 Oct 2026; all confirmed_2026 = true)
=====================================================================
Format: Name, Designation, Organisation

(1) bfsi.eletsonline.com
- Vijaya Kadiyala, Executive Director, DBS Bank
- Deepika Sandeep, Head - AI/ML CoE, HSBC
- Shantanu Dasgupta, Head of Digital Initiatives, Treasury & Transaction Banking, Axis Bank
- Rajesh Choudhary, Chief Information Officer, CSB Bank (spelt "Choudhary" as on the CSB Bank site and LinkedIn. The event site says "Chaudhary".)
- Shanmugam Manivannan, Chief Digital Officer, Equitas Small Finance Bank
- Vishal Chugh, EVP - Head Risk FRM, Tata Capital
- Padmanaban TA, DGM & Head of Digital Banking, Karnataka Bank
- Ram Mohan Rao, Executive Director, Securities and Exchange Board of India (SEBI)
- Tulshekar Gangireddy, Executive Director & Head of Data Strategy, JPMorgan Chase & Co
- Avinash Naik, Chief Information Officer, Bajaj Allianz General Insurance
Optional additions (also confirmed_2026 = true in the file): Mahesh Hariharan Iyer, Vice President of Engineering, Reserve Bank Innovation Hub (RBIH); Anil Varma, Chief Technology Officer, Multi Commodity Exchange Clearing Corporation; Deepak Mohanty, Executive Director, Wells Fargo; Shireen Ali, Head, UK Data Enablement and Standards, HSBC; George Inasu, Managing Director and Country Head, Fidelity National Financial India

(2) egov.eletsonline.com
Framing: speakers come from the Governments of Karnataka and Maharashtra, Rajasthan (to confirm) and the Government of India. Do not call this a Karnataka agenda.
- Pankaj Kumar Pandey, IAS, Principal Secretary, Department of Personnel and Administrative Reforms (e-Governance), Government of Karnataka
- T Bhoobalan, IAS, Chief Executive Officer, Centre for e-Governance, and Managing Director, KUIDFC, Government of Karnataka
- Dr Ravikumar Surpur, IAS, Secretary, Information Technology & Communication Department; Secretary, Planning and Statistics Department; Chairman, RajComp Info Services Limited (RISL), PLACEHOLDER_SURPUR_ORG_CONFIRMED [file infers Government of Rajasthan]
- Aman Mittal, IAS, Joint Chief Executive Officer, Maharashtra Institution for Transformation (MITRA)
- Hemant Garg, Deputy Director, Ministry of Labour and Employment, Government of India
- Sanjeev Gupta, Chief Executive Officer, Karnataka Digital Economy Mission

(3) cio.eletsonline.com
- Pawan Sachdeva, Senior Managing Director and Technology Head - India, Carelon Global Solutions
- Aneelkumar (Aneel) Savalagi, Global Chapter Leader - ICC (Innovation Capability Centre), Global DD&T (Data, Digital & Technology), Takeda
- Sivakumar Selva Ganapathy, VP - Software Engineering; Head - Open Blue India & APAC Solutions; Director - JCIPL, Johnson Controls
- Anshuma (Dogra) Singh, Senior Director, India IT Head/Site Leader, Applied Materials
- Dipayan Chakraborty, Head, India Analytics Center, eBay
- Animesh Kishore, Head, Centre of Excellence (CoE), Digital & Analytics, ITC Limited
- Anand Thakur, Chief Product and Technology Officer, Reliance Retail
- Sandeep Varaganti, CEO, JioMart, Reliance Retail
- Suman Guha, Chief Digital & Technology Officer, Tata Croma (Tata Digital)
- Harsh Vardhan, Global Head - AI & Digital Innovation, Apollo Tyres Ltd

(4) ehealth.eletsonline.com
- Praveen Bist, Chief Information Officer, Amrita Hospitals
- Dr. Sushil Kumar Meher, Head, IT and CISO, All India Institute of Medical Sciences (AIIMS)
Optional addition (confirmed_2026 = true): Pranav Saxena, Chief Product and Technology Officer, API Holdings

(5) digitallearning.eletsonline.com
- Pavankumar Gurazada, Associate Director, Great Learning
- M. Balasubramaniam (Bala MS), CEO, Stratinfinity Inc; Chairman, Southern Regional Committee, AICTE; Deputy Chairman, Ministry of Education & AICTE Investor Network, All India Council for Technical Education (AICTE)
Optional addition (confirmed_2026 = true): Shalini Kapoor, Chief Strategist - Data and AI, EkStep Foundation

=====================================================================
5. PUBLISHING CHECKLIST (per article)
=====================================================================
[ ] Title uses Format B, or Format A with the agenda in hand
[ ] Every speaker line matches section 4 exactly, and confirmed_2026 is rechecked today
[ ] No bios, no session or track claims, no prices, no edition number
[ ] Disclosure line is present
[ ] Correct link block for the date (1A, 1B or 1C), with clean URLs and no rel="noreferrer"
[ ] Newsletter uses the UTM version (1D)

