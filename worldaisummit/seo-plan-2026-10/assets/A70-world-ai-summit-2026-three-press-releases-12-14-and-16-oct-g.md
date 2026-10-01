# A70: World AI Summit 2026: three press releases (12, 14 and 16 Oct), go/no-go link gates, Event JSON-LD and redirects

- **For recommendation:** Three-release press cadence across the Elets network, KDEM and an optional wire, each linking to a stable deep URL
- **Research lens:** event-week-postevent
- **Format:** Plain text / Markdown press releases plus a JSON-LD block and server config snippets. Paste each release into the Elets CMS (cio.eletsonline.com first, then egov.eletsonline.com) and send the same text to KDEM and the wire.
- **Placeholders the business must fill:**
  - PLACEHOLDER_EDITION (2nd or 3rd; LinkedIn and happeningnext disagree)
  - PLACEHOLDER_THEME_LIST (seven tracks or the Elets Sep 2026 focus areas, whichever matches the live /agenda/)
  - PLACEHOLDER_CURRENT_PASS_PRICE (pass tier and price valid on 12 Oct; Standard tier expired 30 Sept)
  - PLACEHOLDER_CURRENT_PASS_PRICE_INR_NUMBER_ONLY (JSON-LD offers.price)
  - PLACEHOLDER_EVENT_IMAGE_URL_MIN_1200PX_WIDE (JSON-LD image)
  - PLACEHOLDER_AWARDS_DATE_TIME (recommendation assumes evening of 14 Oct)
  - PLACEHOLDER_LEAD_ANNOUNCEMENT (PR2 headline)
  - PLACEHOLDER_DAY1_LEAD_PARAGRAPH / PLACEHOLDER_DAY1_SECOND_PARAGRAPH
  - PLACEHOLDER_DAY2_LEAD_PARAGRAPH
  - PLACEHOLDER_SPEAKER_NAME/ROLE + PLACEHOLDER_VERBATIM_QUOTE_1/2 + PLACEHOLDER_TIMESTAMP_1/2 + PLACEHOLDER_APPROVAL_DATE_1/2
  - PLACEHOLDER_WINNERS_LIST and PLACEHOLDER_TOP_3_WINNERS (from final jury list)
  - PLACEHOLDER_VERIFIED_ATTENDANCE_SENTENCE (delete unless signed off from registration system)
  - PLACEHOLDER_IF_RECORDINGS_LIVE (PR3 headline and body variant)
  - PLACEHOLDER_MEDIA_CONTACT_NAME / EMAIL / PHONE
  - PLACEHOLDER_KDEM_CONTACT and PLACEHOLDER_ANY_KDEM_QUOTE_REQUEST
  - PLACEHOLDER_SENDER_NAME
  - PLACEHOLDER_WIRE_NAME_AND_BUDGET (optional paid wire for PR2)
  - Confirm the 10 per cent group discount for 3+ delegates still applies on 12 Oct
  - Confirm a 2027 interest form exists on the homepage before PR3 links to it

## How to ship

Owners: Elets editorial (releases), partnerships (KDEM and wire), web team (pages, redirects, JSON-LD).

1. By 9 Oct, the web team builds /agenda/ and /awards/winners-2026/ (the winners page can stay noindex until 14 Oct evening), updates /delegate/ to the tier that applies on 12 Oct and adds an H1, deploys the section 5 redirects and adds the section 6 JSON-LD. None of this effort was costed in the recommendation, so it needs a go-ahead.

2. On 11 Oct at 18:00 IST, run the PR1 gates in section 0. Pick Headline A or B, fill in the edition number, theme list and pass price, and cross-check the six speaker names against the live speaker page.

3. Publish PR1 on 12 Oct on cio.eletsonline.com, then egov.eletsonline.com and any other relevant Elets vertical. Use the full text on one site (cio). On the others, either point the CMS canonical at the cio URL or rewrite the intro, so the copies do not compete with each other. Tag the cio article /tag/world-ai-summit-2026/. Keep links followed, use at most two per release and keep the anchors exactly as written.

4. On 14 Oct, finish the winners page and get quote approvals by 20:30 IST, then publish PR2 at about 21:00 IST and send it to KDEM and, if approved, one paid India wire (PLACEHOLDER_WIRE_NAME_AND_BUDGET). On 16 Oct, publish PR3 after adding highlights to /agenda/.

5. After each release, run URL Inspection and request indexing for the linked page. Add an https://www.worldaisummit.com/ property in Search Console first, since only the non-www property exists today. Watch referral traffic from eletsonline.com in analytics.

Facts used: dates, venue, organiser, KDEM role, contacts and the group discount come from project context. The verifier confirmed the edition conflict, the theme conflict (cio.eletsonline.com articles 76367 of 22 Sep 2026 and 76373 of 24 Sep 2026), the missing pages and the expired /delegate/ tier. The street address was checked by WebSearch on 1 Oct: 26/1 Dr. Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru 560055 (sources: https://www.marriott.com/en-us/hotels/blrgs-sheraton-grand-bangalore-hotel-at-brigade-gateway/overview/ and https://www.hotelplanner.com/Hotels/178731/Reservations-Sheraton-Bangalore-Hotel-at-Brigade-Gateway-Bangalore-26-1-Dr-Rajkumar-Rd-Malleswaram-Rajajinagar-560055). Speaker names and roles come from worldaisummit/speakers/speakers.json (entries marked confirmed_2026). No bios were written and no paid OpenSEO tools were used. The JSON-LD passes a JSON syntax check (python json.tool). www.worldaisummit.com was blocked by the network egress proxy, so the live agenda and delegate pages could not be re-checked from here. No repository files were edited.

On the question you sent ("do you have more CPUs from computer?"): this session's container reports 4 CPUs (nproc), and that is all it can use. It cannot draw on your own computer's CPUs. More parallel work would mean more cloud sessions or subagents, not more CPUs here.

## Content

=====================================================================
0. GO / NO-GO GATES (check these before each release goes out)
=====================================================================
The verifier found that none of the planned link targets work yet. On 1 Oct, www.worldaisummit.com/agenda/ did not exist, worldaisummit.com/agenda returned a 5xx error, and /awards/winners-2026/ did not exist. /delegate/ still shows the "Standard, valid till 30 Sept 2026" tier. The web team has to build or fix each page before its release goes out. If a gate fails, use the fallback link shown. Never publish a release that links to a page returning an error.

PR1 (Mon 12 Oct, gate check by Sun 11 Oct 18:00 IST)
[ ] https://www.worldaisummit.com/agenda/ returns 200, has an H1, has a self-referencing canonical, is in sitemap.xml and is linked from the homepage navigation.
[ ] The track or theme names on /agenda/ match the PR1 headline you pick (Option A or B below).
    FAIL: change the "full agenda" link to https://www.worldaisummit.com/ and use Headline B.
[ ] /delegate/ shows the pass tier and price that apply on 12 Oct (not "valid till 30 Sept 2026"), has an H1 and is linked from the homepage.
    FAIL: remove the "delegate passes" link and keep the registration@ email line.
[ ] Edition number decided (LinkedIn company page says 2nd, happeningnext.com says 3rd, and Elets AI Summit was held in New Delhi on 22 Jan 2026). Use one number everywhere.
[ ] Every speaker named in PR1 appears on the live speaker page on 12 Oct. Remove anyone who does not.
[ ] The redirect in section 5 is live, so 2025 Elets articles that link to worldaisummit.com/agenda reach the new page.

PR2 (Wed 14 Oct, about 21:00 IST)
[ ] https://www.worldaisummit.com/awards/winners-2026/ is live with the full winners list before the release goes out.
    FAIL: link "World AI Awards 2026 winners" to https://www.worldaisummit.com/awards/ and add the winners list to that page.
[ ] Each quote is transcribed word for word from the session recording, with a timestamp, and approved by the speaker in writing.

PR3 (Fri 16 Oct)
[ ] /agenda/ carries a highlights section. Session recordings are linked from it if the headline mentions recordings.
[ ] The 2027 interest form is actually on the homepage. If it is not, delete the second link and that sentence.
[ ] Any attendance figure comes from the registration system and has been signed off. If not, delete the sentence.


=====================================================================
1. PR1: CURTAIN-RAISER (publish Monday 12 October 2026, morning)
=====================================================================
HEADLINE: pick one after the /agenda/ check
Option A (only if /agenda/ shows the seven tracks):
World AI Summit 2026 to open in Bengaluru on 14 October with seven tracks, from frontier models and sovereign AI to GCCs and AI for Bharat

Option B (if /agenda/ uses the themes in Elets's 22 and 24 Sep 2026 articles):
World AI Summit 2026 to open in Bengaluru on 14 October, with sessions on generative and agentic AI, AI infrastructure and AI in government

STANDFIRST:
The two-day summit, organised by Elets Technomedia with the Karnataka Digital Economy Mission as Strategic Partner, takes place on 14 and 15 October at Sheraton Grand Bangalore Hotel at Brigade Gateway.

BODY:
Bengaluru, 12 October 2026: The PLACEHOLDER_EDITION edition of World AI Summit will be held on 14 and 15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. Elets Technomedia is organising the summit, and the Karnataka Digital Economy Mission (KDEM) is the Strategic Partner.

Over two days, the programme covers PLACEHOLDER_THEME_LIST. [Option A: Frontier Models and Compute; Sovereign AI and Geopolitics; Enterprise AI in Production; Global Capability Centres (GCCs); Robotics, Agents and Embodied AI; AI for Bharat; and Capital, Founders and Exits. Option B: generative AI and large language models, agentic AI, AI infrastructure and cloud, AI in enterprises, AI in government, and AI ethics. Use only the list that matches the live /agenda/ page.]

The summit brings together policymakers and technology leaders from government, banking and financial services, healthcare, retail, education and start-ups. Confirmed speakers include Pankaj Kumar Pandey, IAS, Principal Secretary, e-Governance, Government of Karnataka; Sanjeev Gupta, CEO, Karnataka Digital Economy Mission; Ram Mohan Rao, Executive Director, Securities and Exchange Board of India (SEBI); Shalini Kapoor, Chief Strategist, Data and AI, EkStep Foundation; Sandeep Varaganti, CEO, JioMart, Reliance Retail; and Deepika Sandeep, Head, AI/ML CoE, HSBC.

The World AI Awards 2026 will be presented at the summit on PLACEHOLDER_AWARDS_DATE_TIME.

The [full agenda](https://www.worldaisummit.com/agenda/) is available on the summit website. [Delegate passes](https://www.worldaisummit.com/delegate/) are priced at PLACEHOLDER_CURRENT_PASS_PRICE, and groups of three or more delegates receive a 10 per cent discount. For registration queries, write to registration@worldaisummit.com. For sponsorship and exhibition, write to partnerships@worldaisummit.com.

ABOUT WORLD AI SUMMIT (future tense, for PR1):
World AI Summit is organised by Elets Technomedia, with the Karnataka Digital Economy Mission (KDEM) as Strategic Partner. The 2026 edition will take place on 14-15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. Partnerships: partnerships@worldaisummit.com. www.worldaisummit.com

MEDIA CONTACT: PLACEHOLDER_MEDIA_CONTACT_NAME, PLACEHOLDER_MEDIA_CONTACT_EMAIL, PLACEHOLDER_MEDIA_CONTACT_PHONE

(No quotes in PR1. Quotes must come word for word from recordings, and nothing has been recorded yet. No attendance or speaker counts.)


=====================================================================
2. PR2: DAY 1 AND AWARDS (publish Wednesday 14 October 2026, about 21:00 IST)
=====================================================================
HEADLINE:
World AI Summit 2026 Day 1: PLACEHOLDER_LEAD_ANNOUNCEMENT; World AI Awards 2026 winners announced

BODY:
Bengaluru, 14 October 2026: World AI Summit 2026 opened today at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. Elets Technomedia organises the summit, and the Karnataka Digital Economy Mission (KDEM) is the Strategic Partner.

PLACEHOLDER_DAY1_LEAD_PARAGRAPH [One factual paragraph: who announced what, in which session, and when. Source it from the session recording or from a written announcement by the announcing organisation. Do not add your own interpretation.]

PLACEHOLDER_SPEAKER_NAME, PLACEHOLDER_SPEAKER_ROLE, said, "PLACEHOLDER_VERBATIM_QUOTE_1."
[Transcribed word for word from the recording at PLACEHOLDER_TIMESTAMP_1. Approved by the speaker on PLACEHOLDER_APPROVAL_DATE_1. Delete this paragraph if approval has not arrived by 20:30 IST.]

PLACEHOLDER_DAY1_SECOND_PARAGRAPH [Optional second session summary under the same rules: facts from the recording, and any quote verbatim and approved.]

The World AI Awards 2026 were presented this evening. The winners include:
PLACEHOLDER_WINNERS_LIST [Category: winning organisation or individual, one per line, copied from the final jury list.]

The complete list of [World AI Awards 2026 winners](https://www.worldaisummit.com/awards/winners-2026/) is on the summit website. The summit continues on 15 October. The [Day 2 programme](https://www.worldaisummit.com/agenda/) is online.

ABOUT WORLD AI SUMMIT (present tense, for PR2):
World AI Summit is organised by Elets Technomedia, with the Karnataka Digital Economy Mission (KDEM) as Strategic Partner. The 2026 edition is taking place on 14-15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. Partnerships: partnerships@worldaisummit.com. www.worldaisummit.com

MEDIA CONTACT: PLACEHOLDER_MEDIA_CONTACT_NAME, PLACEHOLDER_MEDIA_CONTACT_EMAIL, PLACEHOLDER_MEDIA_CONTACT_PHONE


=====================================================================
3. PR3: WRAP-UP (publish Friday 16 October 2026)
=====================================================================
HEADLINE:
If recordings are live: World AI Summit 2026 concludes in Bengaluru; highlights, award winners and session recordings now available
If recordings are not live: World AI Summit 2026 concludes in Bengaluru; highlights and award winners now available

BODY:
Bengaluru, 16 October 2026: The PLACEHOLDER_EDITION edition of World AI Summit concluded on 15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. Elets Technomedia organised the summit, and the Karnataka Digital Economy Mission (KDEM) was the Strategic Partner.

PLACEHOLDER_DAY2_LEAD_PARAGRAPH [The main Day 2 announcement or discussion, stated as fact from the recording.]

PLACEHOLDER_SPEAKER_NAME_2, PLACEHOLDER_SPEAKER_ROLE_2, said, "PLACEHOLDER_VERBATIM_QUOTE_2."
[Word for word from the recording at PLACEHOLDER_TIMESTAMP_2. Approved by the speaker on PLACEHOLDER_APPROVAL_DATE_2. Delete if not approved.]

Over the two days, sessions covered PLACEHOLDER_THEME_LIST (use the same list as PR1). The World AI Awards 2026 were presented on 14 October. Winners included PLACEHOLDER_TOP_3_WINNERS.

PLACEHOLDER_VERIFIED_ATTENDANCE_SENTENCE [Use only with a figure taken from the registration system and signed off. Otherwise delete it. Do not reuse earlier figures such as 150+, 200+, 1,000+ or 1,500+.]

The [World AI Summit 2026 highlights](https://www.worldaisummit.com/agenda/) are available on the summit website, along with the award winners PLACEHOLDER_IF_RECORDINGS_LIVE ("and session recordings"). Organisations interested in the next edition can [register interest for World AI Summit 2027](https://www.worldaisummit.com/) [delete this link and sentence if there is no 2027 form on the homepage]. For partnerships, write to partnerships@worldaisummit.com.

ABOUT WORLD AI SUMMIT (past tense, for PR3 only):
World AI Summit, organised by Elets Technomedia with the Karnataka Digital Economy Mission (KDEM) as Strategic Partner, took place on 14-15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. Partnerships: partnerships@worldaisummit.com. www.worldaisummit.com

MEDIA CONTACT: PLACEHOLDER_MEDIA_CONTACT_NAME, PLACEHOLDER_MEDIA_CONTACT_EMAIL, PLACEHOLDER_MEDIA_CONTACT_PHONE


=====================================================================
4. NOTE TO KDEM (send 13 Oct from partnerships@)
=====================================================================
Subject: World AI Summit 2026: releases for KDEM channels

Dear PLACEHOLDER_KDEM_CONTACT,

Thank you for partnering with us on World AI Summit 2026 as Strategic Partner. We will issue a Day 1 and awards release on the evening of 14 October and a wrap-up on 16 October. We would be grateful if KDEM could carry either release on its website or newsroom and on its social channels. Please keep the link to www.worldaisummit.com unchanged. We will send the final text as soon as each release is approved. PLACEHOLDER_ANY_KDEM_QUOTE_REQUEST [include only if a KDEM spokesperson's recorded remarks will be quoted, and send them for approval].

Regards,
PLACEHOLDER_SENDER_NAME
Elets Technomedia


=====================================================================
5. REDIRECTS (web team, live before PR1)
=====================================================================
These send old and short links to the final URLs in one 301 hop. Examples are 2025 Elets articles (cio 74827, egov 2025/06) that link to worldaisummit.com/agenda, which returns 5xx today, and any press link that leaves out the trailing slash. Only these paths are covered. A sitewide non-www to www redirect is left out on purpose: non-www URLs such as /awards currently rank and hold the Search Console data, so that change needs its own decision.

Apache (.htaccess at the document root. If worldaisummit.com without www is served from a different vhost or docroot, which the 5xx suggests, add the same lines there too):

RewriteEngine On
RewriteCond %{HTTP_HOST} ^worldaisummit\.com$ [NC,OR]
RewriteCond %{REQUEST_URI} !/$
RewriteRule ^(agenda|awards/winners-2026)/?$ https://www.worldaisummit.com/$1/ [R=301,L]

nginx:

# server block for worldaisummit.com (non-www)
location ~ ^/(agenda|awards/winners-2026)/?$ {
    return 301 https://www.worldaisummit.com/$1/;
}

# server block for www.worldaisummit.com
location = /agenda               { return 301 https://www.worldaisummit.com/agenda/; }
location = /awards/winners-2026  { return 301 https://www.worldaisummit.com/awards/winners-2026/; }

Test: curl -sI https://worldaisummit.com/agenda, https://www.worldaisummit.com/agenda and https://worldaisummit.com/agenda/ should each return one 301 to https://www.worldaisummit.com/agenda/, which returns 200.


=====================================================================
6. EVENT JSON-LD (for the new /agenda/ page, and the homepage if it has no Event markup yet; use one @id on both)
=====================================================================
Only list performers who are visible on the page carrying this markup. The six below are marked confirmed_2026 in worldaisummit/speakers/speakers.json and are the same people named in PR1. Replace both placeholders before publishing. "price" must be a number only, for example "30000".

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Event",
  "@id": "https://www.worldaisummit.com/#event",
  "name": "World AI Summit 2026",
  "description": "World AI Summit 2026, organised by Elets Technomedia with the Karnataka Digital Economy Mission (KDEM) as Strategic Partner, on 14-15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru.",
  "url": "https://www.worldaisummit.com/",
  "image": ["PLACEHOLDER_EVENT_IMAGE_URL_MIN_1200PX_WIDE"],
  "startDate": "2026-10-14",
  "endDate": "2026-10-15",
  "eventStatus": "https://schema.org/EventScheduled",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
  "location": {
    "@type": "Place",
    "name": "Sheraton Grand Bangalore Hotel at Brigade Gateway",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "26/1 Dr. Rajkumar Road, Malleswaram-Rajajinagar",
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
    "name": "Delegate pass",
    "url": "https://www.worldaisummit.com/delegate/",
    "price": "PLACEHOLDER_CURRENT_PASS_PRICE_INR_NUMBER_ONLY",
    "priceCurrency": "INR",
    "availability": "https://schema.org/InStock"
  },
  "performer": [
    {"@type": "Person", "name": "Pankaj Kumar Pandey", "honorificSuffix": "IAS", "jobTitle": "Principal Secretary, e-Governance, Government of Karnataka"},
    {"@type": "Person", "name": "Sanjeev Gupta", "jobTitle": "CEO, Karnataka Digital Economy Mission"},
    {"@type": "Person", "name": "Ram Mohan Rao", "jobTitle": "Executive Director, Securities and Exchange Board of India (SEBI)"},
    {"@type": "Person", "name": "Shalini Kapoor", "jobTitle": "Chief Strategist, Data and AI, EkStep Foundation"},
    {"@type": "Person", "name": "Sandeep Varaganti", "jobTitle": "CEO, JioMart, Reliance Retail"},
    {"@type": "Person", "name": "Deepika Sandeep", "jobTitle": "Head, AI/ML CoE, HSBC"}
  ]
}
</script>

After the event, change "eventStatus" only if the event is cancelled or moved. Leave the dates as they are.
