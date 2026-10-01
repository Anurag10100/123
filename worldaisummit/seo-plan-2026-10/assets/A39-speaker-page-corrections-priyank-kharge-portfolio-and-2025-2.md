# A39: Speaker-page corrections: Priyank Kharge portfolio and 2025/2026 framing, plus role-led titles for shared-name speakers

- **For recommendation:** Fix speaker-page errors before anything is shared (Priyank Kharge's portfolio and 2025/2026 framing, shared-name titles)
- **Research lens:** speakers-partners
- **Format:** HTML head snippets (title and meta description), find-and-replace strings for page body copy, JSON field values for speakers.json, and a short confirmation email. No URL changes, so no redirects. No schema changes.
- **Placeholders the business must fill:**
  - PLACEHOLDER_KHARGE_2026_CONFIRMED (yes/no from Elets secretariat; decides B1 or B2, C1 or C2, and the Section F flags)
  - PLACEHOLDER_KHARGE_2026_SESSION (session title, date, time, hall if confirmed)
  - PLACEHOLDER_SPEAKER_HTML_CHOICE (if not confirmed: relabel the /speaker.html block as 2025 Chief Guest, or remove it)
  - PLACEHOLDER_ABHISHEK_SINGH_CURRENT_ROLE (current designation and 2026 participation, to be confirmed by Elets)
  - PLACEHOLDER_SENDER_NAME (who signs the confirmation email)

## How to ship

1) Send the Section G email to secretariat@worldaisummit.com today. 2) Without waiting for the reply, web dev applies B1 (not-confirmed version), the Section B body fixes, C2 or remove, and the Section E titles. Those are safe in either case. 3) Check the live homepage carousel by hand and apply Section D. 4) When Elets confirms, switch to B2 and C1, and update speakers.json as in Section F. 5) Run the Section H checks. Effort is about 1-2 hours. No OpenSEO credits are used and no redirects or schema changes are needed. Side note on the question that started this run ("do you have more CPUs from computer?"): this session's cloud container reports 4 CPUs (nproc). It runs on hosted infrastructure, not on your own computer, so its CPU count does not come from your machine.

## Content

SPEAKER-PAGE CORRECTIONS, WORLD AI SUMMIT 2026
Prepared 1 Oct 2026. Apply by 2 Oct 2026, before any share kit goes out.
Scope: text edits on existing pages only. URLs stay the same, so no redirects are needed.

==================================================
A. CORRECT PORTFOLIO STRING (use the same wording everywhere)
==================================================
Minister for Home (excluding Intelligence), IT-BT and e-Governance, Government of Karnataka

Sources: Deccan Chronicle (4 Jun 2026), thesouthfirst.com (4 Jun 2026), Asianet (5 Jun 2026) and The Hindu (5 Jun 2026). Rural Development and Panchayat Raj (RDPR) moved to Eshwar Khandre.

==================================================
B. /assets/speaker_details/priyank-kharge.html
==================================================
Pick the version that matches PLACEHOLDER_KHARGE_2026_CONFIRMED (yes or no, from the Elets secretariat). Use B1 until Elets confirms.

B1. NOT confirmed for 2026 (default)
<title>Priyank Kharge | Karnataka Home and IT-BT Minister | World AI Summit 2025</title>
<meta name="description" content="Shri Priyank Kharge, Minister for Home (excluding Intelligence), IT-BT and e-Governance, Government of Karnataka, was Chief Guest at World AI Summit 2025 in Bengaluru.">

B2. CONFIRMED for 2026
<title>Priyank Kharge | Karnataka Home and IT-BT Minister | World AI Summit 2026</title>
<meta name="description" content="Shri Priyank Kharge, Minister for Home (excluding Intelligence), IT-BT and e-Governance, Government of Karnataka, speaks at World AI Summit 2026, 14-15 October, Bengaluru.">
Session line on the page: PLACEHOLDER_KHARGE_2026_SESSION (session title, date, time, hall)

Both versions:
- If the page has og:title, og:description, twitter:title or twitter:description, copy the same title and description into them.
- Header. Find: Minister of Home Affairs, IT/BT and E-Governance
  Replace with: Minister for Home (excluding Intelligence), IT-BT and e-Governance, Government of Karnataka
- About paragraph. Find: Minister for Electronics, IT & Biotechnology and Rural Development & Panchayat Raj
  Replace with: Minister for Home (excluding Intelligence), IT-BT and e-Governance, Government of Karnataka
  If "Government of Karnataka" already follows in that sentence, do not repeat it. Do not change any other words in the bio.

==================================================
C. /speaker.html, the "Welcoming" block
==================================================
Current text: Welcoming Shri Priyank M Kharge, Minister of Home Affairs, IT/BT and E-Governance

C1. If confirmed:
<a href="/assets/speaker_details/priyank-kharge.html">Welcoming Shri Priyank M Kharge</a>, Minister for Home (excluding Intelligence), IT-BT and e-Governance, Government of Karnataka

C2. If not confirmed (PLACEHOLDER_SPEAKER_HTML_CHOICE: relabel or remove). Either remove the block, or relabel it:
<a href="/assets/speaker_details/priyank-kharge.html">Chief Guest, World AI Summit 2025: Shri Priyank M Kharge</a>, Minister for Home (excluding Intelligence), IT-BT and e-Governance, Government of Karnataka

==================================================
D. Homepage speaker block (/ and /index.html). Check the live carousel by hand.
==================================================
Exa's cached copy of /index.html (an older six-track version; cache date unknown) showed:
  Shri Priyank Kharge, Hon'ble Minister - Electronics, IT & Biotechnology; RDPR
If this text is still live:
- Confirmed: replace it with: Shri Priyank Kharge, Hon'ble Minister - Home (excluding Intelligence), IT-BT and e-Governance, Government of Karnataka
- Not confirmed: take him out of the 2026 carousel, or label him "Chief Guest, World AI Summit 2025".
The same block shows Abhishek Singh as "Additional Secretary (MeitY) ... Govt of Karnataka". MeitY is a Government of India ministry, so "Govt of Karnataka" is wrong. Replace the line with PLACEHOLDER_ABHISHEK_SINGH_CURRENT_ROLE, and confirm his 2026 participation with Elets first.

==================================================
E. Titles for shared-name speakers (all confirmed_2026: true in speakers.json)
==================================================
/assets/speaker_details/pankaj-kumar-pandey.html
<title>Pankaj Kumar Pandey, IAS | Principal Secretary, Karnataka | World AI Summit 2026</title>
(Source: egov.eletsonline.com, 5 Feb 2026: Principal Secretary, DPAR (e-Governance), Government of Karnataka. "Karnataka" separates him from the Uttarakhand IAS namesake who ranks #1 for the name.)

/assets/speaker_details/sanjeev-gupta.html
<title>Sanjeev Kumar Gupta | CEO, KDEM, Karnataka | World AI Summit 2026</title>
(Source: karnatakadigital.in/about-us/, fetched 1 Oct 2026, lists "Sanjeev Kumar Gupta, Chief Executive Officer". Keep the URL slug as it is.)

/assets/speaker_details/shalini-kapoor.html
<title>Shalini Kapoor | Chief Strategist, Data and AI, EkStep | World AI Summit 2026</title>
(Source: speakers.json title_role. Not re-checked this week.)

/assets/speaker_details/harsh-vardhan.html
<title>Harsh Vardhan | Global Head, AI and Digital Innovation, Apollo Tyres | World AI Summit 2026</title>
(Source: full role from audit c1b16b55 and speakers.json.)

No change: /assets/speaker_details/vishal-chugh.html. Its title already includes the role: "Vishal Chugh | EVP, Head Risk FRM, Tata Capital | World AI Summit 2026".

Length note: these titles are 65 to 91 characters long. The name, role and organisation come first, so when Google cuts a title at about 60 characters, or rewrites it, mostly the "World AI Summit 2026" suffix is lost. They will add to the 27 long-title flags in the audit. That trade-off is accepted because the role is what tells these people apart from others with the same name.

The other role-less titles: 30 of the 51 /assets/speaker_details/ titles (about 59%) have no role. Use this pattern:
  <Name> | <title_role from speakers.json> | World AI Summit 2026   (only where confirmed_2026 is true)
  <Name> | <title_role> | World AI Summit 2025                      (2025-only speakers)

==================================================
F. Local generator data: worldaisummit/speakers/speakers.json
Fix this before publish is turned on for Kharge. Otherwise the generator repeats the old portfolio.
==================================================
"slug": "priyank-kharge"
  "role": "Minister for Home (excluding Intelligence), IT-BT and e-Governance"
  "title_role": "Minister for Home, IT-BT and e-Governance, Karnataka"
  Only if confirmed: "editions": ["2025", "2026"], "confirmed_2026": true, "session": "PLACEHOLDER_KHARGE_2026_SESSION", "publish": true
  If not confirmed: leave confirmed_2026 and publish as false.
"slug": "sanjeev-gupta"
  "name": "Sanjeev Kumar Gupta"   (slug unchanged)
Then run: python3 build_speakers.py --clean

==================================================
G. Confirmation email to the Elets secretariat (secretariat@worldaisummit.com)
==================================================
Subject: Please confirm by 2 Oct: Shri Priyank Kharge at World AI Summit 2026

Dear team,

Before we share speaker pages with partners, could you please confirm by 2 October whether Shri Priyank Kharge, Minister for Home (excluding Intelligence), IT-BT and e-Governance, Government of Karnataka, is confirmed for World AI Summit 2026 (14-15 October, Sheraton Grand Bangalore Hotel at Brigade Gateway)? If he is, please share his session title, date, time and hall.

At present /speaker.html welcomes him, his speaker page is titled for the 2025 edition, and our speaker data file lists him as not confirmed. We would like all three to match.

Please also confirm the current designation and 2026 participation of Shri Abhishek Singh. The homepage speaker block shows him as Additional Secretary (MeitY) with Govt of Karnataka.

Thank you,
PLACEHOLDER_SENDER_NAME

==================================================
H. Post-publish check
==================================================
1. View the source of each edited page. Each should have one <title> and one meta description, and the text should match exactly.
2. Run: for u in / /speaker.html /assets/speaker_details/priyank-kharge.html; do curl -s "https://www.worldaisummit.com$u" | grep -ciE "Rural Development|RDPR|Electronics, IT & Biotechnology|Home Affairs"; done
   Every count should be 0. The /1st-edition/ archive can keep his 2025 designation, because it was correct for that edition.
3. Search Console currently covers only https://worldaisummit.com/ (non-www), so it cannot inspect these www URLs. Add the www property, then request indexing for the edited pages.
