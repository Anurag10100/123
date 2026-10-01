# A45: World AI Summit 2026: publishing calendar for 2-17 October, plus day-zero setup (corrected after verification)

- **For recommendation:** Run a fixed Oct 2-17 publishing calendar that puts every new page on worldaisummit.com first and uses Elets media for news angles that link back to it
- **Research lens:** news-content
- **Format:** Markdown runbook: rules, day-zero setup (GSC, redirects for Apache and nginx, homepage block, sitemap), a day-by-day calendar with URL, title, query, links, CTA, owner and blockers for each item, then paste-ready JSON-LD and copy blocks
- **Placeholders the business must fill:**
  - PLACEHOLDER_CONTENT_OWNER / PLACEHOLDER_WEB_OWNER / PLACEHOLDER_ELETS_EDITOR / PLACEHOLDER_PROGRAMME_OWNER
  - PLACEHOLDER_DNS_OWNER (for the GSC Domain property)
  - PLACEHOLDER_PARTNER_PAGE_URL (/partner-with-us.html currently has its canonical set to /)
  - PLACEHOLDER_EDITION_NUMBER (3rd per LinkedIn vs 2nd on some pages)
  - PLACEHOLDER_CURRENT_PASS_PRICE / PLACEHOLDER_CURRENT_PASS_PRICE_INR (Standard pass validity ended 30 Sept 2026; Late Access listed at Rs 30,000/60,000)
  - PLACEHOLDER_CURRENT_PASS_TYPES_AND_PRICES
  - PLACEHOLDER_HALL_NAMES
  - PLACEHOLDER_SESSION_DATA (programme team; session is null for all 76 speakers)
  - PLACEHOLDER_CONFIRM_TRACK_WITH_PROG (GCC and other track speaker assignments)
  - PLACEHOLDER_CONFIRMED_SPEAKERS_FOR_THESE_TRACKS (sovereign AI, frontier models)
  - PLACEHOLDER_AWARD_CATEGORIES / PLACEHOLDER_CATEGORY_COUNT
  - PLACEHOLDER_2026_NOMINATION_FEE (2025: Rs 18,000 + GST)
  - PLACEHOLDER_NOMINATION_DEADLINE
  - PLACEHOLDER_JURY_TEXT
  - PLACEHOLDER_CEREMONY_DATE / PLACEHOLDER_CEREMONY_TIME
  - PLACEHOLDER_GCC_NEWS_HOOK
  - PLACEHOLDER_KARNATAKA_AI_HOOK
  - PLACEHOLDER_RBI_BULLETIN_FACTS (verify on rbi.org.in)
  - PLACEHOLDER_SOVEREIGN_AI_HOOK
  - PLACEHOLDER_OTHER_OCT_EVENTS (verified Bengaluru October AI events only)
  - PLACEHOLDER_KDEM_2026_STATUS (KDEM was Strategic Partner in 2025)
  - PLACEHOLDER_WIRE_SERVICE
  - PLACEHOLDER_DESK_HOURS
  - PLACEHOLDER_ID_AND_BADGE_RULES
  - PLACEHOLDER_START_TIME
  - PLACEHOLDER_EVENT_IMAGE_URL_1200x630 / PLACEHOLDER_AWARDS_IMAGE_URL_1200x630
  - PLACEHOLDER_LAST_UPDATE_ISO / PLACEHOLDER_UPDATE_HEADLINE / PLACEHOLDER_UPDATE_TIME_ISO / PLACEHOLDER_UPDATE_TEXT
  - PLACEHOLDER_BADGE_FILE
  - PLACEHOLDER_VIDEO_URLS
  - PLACEHOLDER_2027_FORM
  - PLACEHOLDER_OLD_TO_NEW_SLUG_MAP (/assets/speaker_details -> /speakers/<slug>/)

## How to ship

1. Fri 2 Oct, morning (web dev, about 2 hours): add and verify the GSC URL-prefix property for https://www.worldaisummit.com/ and ask the DNS owner for a Domain property. Back up .htaccess (or the nginx config), deploy the redirect block from B2 and test with curl -I:
   - http://worldaisummit.com/awards should give one 301 to https://www.worldaisummit.com/awards/
   - /registration should go to /delegate/
   - /index.html should go to /
   - the www homepage should give 200 with no loop
   Then add the B3 homepage block, B4 sitemap and robots lines, B5 banner and D1 JSON-LD (without performer), publish /agenda/ v1, and request indexing for /, /agenda/ and /awards/.
2. Fill the PLACEHOLDER_ values (list below) with the owners named in each item. Do not publish an item while it still contains a placeholder.
3. Sat 3 Oct: run python3 build_speakers.py --clean in /home/user/123/worldaisummit/speakers, upload dist/speakers/ and dist/sitemap-speakers.xml, then add the performer array to D1 and publish post #1.
4. Follow section C day by day. Before naming any speaker, check confirmed_2026 in /home/user/123/worldaisummit/speakers/speakers.json. Validate each JSON-LD block in Google's Rich Results Test before publishing.
5. Sources used today:
   - Venue street address: marriott.com hotel page (26/1 Dr. Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru 560055).
   - Organiser URL: eletsonline.com.
   - Speaker flags: read from speakers.json; 50 records are confirmed and session is null for all 76.
   - I could not fetch worldaisummit.com from this environment (the proxy blocked it), so verifier item 4 (whether the homepage and /faqs still link to /awards) is still open. Check it in the live HTML.
6. Your question about more CPUs: this workflow runs in a cloud container, not on your computer. The container reports 4 CPUs (nproc), and this workflow cannot add CPUs from your computer.

## Content

# World AI Summit 2026: publishing calendar, 2-17 October 2026

WAIS = https://www.worldaisummit.com (static HTML). ELETS = cio.eletsonline.com / egov.eletsonline.com.
Event: World AI Summit 2026, 14-15 October 2026, Sheraton Grand Bangalore Hotel at Brigade Gateway, 26/1 Dr. Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru, Karnataka 560055 (address from marriott.com, checked 1 Oct 2026). Organiser: Elets Technomedia.
Owners: CONTENT = calendar owner (PLACEHOLDER_CONTENT_OWNER). WEB = web developer (PLACEHOLDER_WEB_OWNER). ED = Elets editorial (PLACEHOLDER_ELETS_EDITOR). PROG = programme team (PLACEHOLDER_PROGRAMME_OWNER).

---

## A. Rules for every item

1. **Dated byline.** Show the author's name, "Published <date>" and "Updated <date, time IST>" on every page that changes.
2. **Three contextual links on every new WAIS URL:** /delegate/, /agenda/, and either /awards/ or the partner page (PLACEHOLDER_PARTNER_PAGE_URL; /partner-with-us.html currently has its canonical pointing to /, so fix that first or use mailto:partnerships@worldaisummit.com). Put the links in body text, not only in the footer.
3. **Named speakers.** Name a speaker only if their record in worldaisummit/speakers/speakers.json has `confirmed_2026: true`. The following are NOT confirmed and must not be named as 2026 speakers: Priyank Kharge, Dr. Ekroop Caur, Abhishek Singh, Sahil Kini (RBIH), Vishal Dhupar (NVIDIA), A.S. Rajgopal, Deepak Bagla, Prashant Pitti, Vikalp Sahni, Sharad Sharma, Arif Khan, Debdoot Mukherjee, and every other record still set to false.
4. **No sessions, times or halls from guesswork.** The `session` field is null for all 76 records. Track, time and hall come only from PROG. Until PROG supplies them, write "Session details to be announced".
5. **No invented quotes or bios.** Quotes must come from an emailed Q&A with a confirmed speaker or from what was said on stage (note the timestamp). Bios come from the speaker's office or the generator's fallback line. Never write them from memory.
6. **Publishing checklist for each new URL:** (a) self-referencing canonical on https://www.worldaisummit.com/...; (b) entry in sitemap.xml with an accurate `<lastmod>`; (c) link from the homepage "Latest from the Summit" block; (d) GSC www property > URL Inspection > Request indexing. Request indexing has a daily quota, so prioritise /agenda/, /speakers/, /awards/, /2026/live/ and the winners page. Do not count on resubmitting the sitemap: Google retired the sitemap ping in 2023, and resubmitting does not force a recrawl.
7. **Freeze ranking titles.** Do not change the title or URL of the homepage or /awards between 2 and 17 Oct. /awards already ranks #2 for "world ai awards 2026" with the title "World AI Awards 2026 | Celebrating AI Excellence".
8. **House style.** Indian English, calm tone, no exclamation marks. Write "World AI Summit 2026, Bengaluru" in the first paragraph of every news item.
9. **Edition number.** Use PLACEHOLDER_EDITION_NUMBER (LinkedIn says 3rd, some pages say 2nd). Make it the same on every page before 12 Oct.

---

## B. Day-zero setup: Fri 2 Oct, all live by 18:00 IST (WEB)

### B1. Search Console
- **Today:** add a URL-prefix property for https://www.worldaisummit.com/ and verify it with the HTML file or meta tag. The web team can do this without DNS access. Keep the existing non-www property.
- **In parallel:** ask PLACEHOLDER_DNS_OWNER to add the DNS TXT record for a Domain property (worldaisummit.com), which covers both hosts and http/https.
- Submit https://www.worldaisummit.com/sitemap.xml and /sitemap-speakers.xml in the www property.
- Why: the non-www property sees /awards (28 Jun-28 Sep: 79 clicks, 2,419 impressions, avg position 9.1) but only 5 clicks and 25 impressions for the homepage. The www homepage's brand traffic is not visible today.

### B2. One host, one hop (fixes the www/non-www split)
Current state: the non-www root redirects to www, but https://worldaisummit.com/awards is indexed on non-www with a non-www canonical. /delegate/ and /speaker.html on non-www are unknown to Google, and /registration chains 3 hops.
After deployment: run URL Inspection on https://worldaisummit.com/awards and https://www.worldaisummit.com/awards/. Check the position for "world ai awards 2026" every day until 17 Oct. Remove any older host or registration redirect in the hosting panel or a plugin first, so the rules do not chain.

**Apache (.htaccess in the web root; on WordPress, place above `# BEGIN WordPress`)**
```apache
RewriteEngine On

# 1. Legacy URLs, straight to the final www URL (one hop, either host).
#    THE_REQUEST avoids loops with DirectoryIndex.
RewriteCond %{THE_REQUEST} \s/index\.html[\s?] [NC]
RewriteRule ^index\.html$ https://www.worldaisummit.com/ [R=301,L]
RewriteCond %{THE_REQUEST} \s/registration(\.html|/)?[\s?] [NC]
RewriteRule ^registration https://www.worldaisummit.com/delegate/ [R=301,L]
RewriteCond %{THE_REQUEST} \s/award\.html[\s?] [NC]
RewriteRule ^award\.html$ https://www.worldaisummit.com/awards/ [R=301,L]
RewriteCond %{THE_REQUEST} \s/1st-edition/delegate-pass\.html[\s?] [NC]
RewriteRule ^1st-edition/delegate-pass\.html$ https://www.worldaisummit.com/delegate/ [R=301,L]

# 2. Non-www directory without trailing slash -> www with slash, one hop (e.g. /awards)
RewriteCond %{HTTP_HOST} ^worldaisummit\.com$ [NC]
RewriteCond %{REQUEST_FILENAME} -d
RewriteRule ^(.*[^/])$ https://www.worldaisummit.com/$1/ [R=301,L]

# 3. Everything else on non-www -> same path on www
RewriteCond %{HTTP_HOST} ^worldaisummit\.com$ [NC]
RewriteRule ^(.*)$ https://www.worldaisummit.com/$1 [R=301,L]

# 4. http -> https on www. Behind a CDN or proxy, test
#    %{HTTP:X-Forwarded-Proto} !https instead, to avoid a loop.
RewriteCond %{HTTPS} !=on
RewriteRule ^(.*)$ https://www.worldaisummit.com/$1 [R=301,L]
```

**nginx**
```nginx
# http block
map $request_uri $wais_legacy {
    default                                      "";
    ~^/index\.html(\?.*)?$                       /;
    ~^/registration(\.html|/)?(\?.*)?$           /delegate/;
    ~^/award\.html(\?.*)?$                       /awards/;
    ~^/1st-edition/delegate-pass\.html(\?.*)?$   /delegate/;
}

server {                      # all http -> https www
    listen 80; listen [::]:80;
    server_name worldaisummit.com www.worldaisummit.com;
    if ($wais_legacy) { return 301 https://www.worldaisummit.com$wais_legacy; }
    return 301 https://www.worldaisummit.com$request_uri;
}

server {                      # https non-www -> www, one hop
    listen 443 ssl http2; listen [::]:443 ssl http2;
    server_name worldaisummit.com;
    ssl_certificate     /path/to/fullchain.pem;
    ssl_certificate_key /path/to/privkey.pem;
    root /path/to/worldaisummit;     # same root as www, for the -d test
    if ($wais_legacy) { return 301 https://www.worldaisummit.com$wais_legacy; }
    location ~ [^/]$ {
        if (-d $request_filename) { return 301 https://www.worldaisummit.com$uri/$is_args$args; }
        return 301 https://www.worldaisummit.com$request_uri;
    }
    location / { return 301 https://www.worldaisummit.com$request_uri; }
}

server {                      # canonical host
    listen 443 ssl http2; listen [::]:443 ssl http2;
    server_name www.worldaisummit.com;
    ssl_certificate     /path/to/fullchain.pem;
    ssl_certificate_key /path/to/privkey.pem;
    root /path/to/worldaisummit;
    index index.html;
    if ($wais_legacy) { return 301 https://www.worldaisummit.com$wais_legacy; }
    location / { try_files $uri $uri/ =404; }
}
```
Sending /registration to /delegate/ (instead of the current 302 to the homepage) is a recommendation. Change it if the business prefers another target.

Canonical tag on every www page, for example on /awards/:
`<link rel="canonical" href="https://www.worldaisummit.com/awards/">`

### B3. Homepage "Latest from the Summit" block (above the fold, under the hero)
Show the 3 newest URLs, newest first, and update the block with every publish.
```html
<section class="wais-latest" aria-labelledby="wais-latest-h">
  <h2 id="wais-latest-h">Latest from the Summit</h2>
  <ul>
    <li><time datetime="2026-10-02">2 Oct</time> <a href="/agenda/">World AI Summit 2026 agenda: seven tracks, 14-15 October</a></li>
    <li><time datetime="2026-10-02">2 Oct</time> <a href="/awards/">World AI Awards 2026: nominations and categories</a></li>
    <li><time datetime="2026-10-02">2 Oct</time> <a href="/delegate/">Delegate passes for World AI Summit 2026</a></li>
  </ul>
</section>
<style>
.wais-latest{max-width:1100px;margin:16px auto;padding:12px 16px;border-top:1px solid #ddd;border-bottom:1px solid #ddd}
.wais-latest h2{font-size:1rem;margin:0 0 8px}
.wais-latest ul{list-style:none;margin:0;padding:0}
.wais-latest li{margin:4px 0}
.wais-latest time{display:inline-block;min-width:56px;color:#555}
</style>
```
Also add "Agenda", "Speakers" and "Awards" to the homepage main nav, and an "Agenda" button in the hero next to the pass CTA.

### B4. Sitemap
Add one `<url>` per new page. Change `<lastmod>` only when the content materially changes.
```xml
<url><loc>https://www.worldaisummit.com/agenda/</loc><lastmod>2026-10-02T18:00:00+05:30</lastmod></url>
<url><loc>https://www.worldaisummit.com/awards/</loc><lastmod>2026-10-04T12:00:00+05:30</lastmod></url>
```
Add to robots.txt:
```
Sitemap: https://www.worldaisummit.com/sitemap.xml
Sitemap: https://www.worldaisummit.com/sitemap-speakers.xml
```
Every `<loc>` must be on https://www. Remove any non-www or /index.html entries.

### B5. Banner on /1st-edition/world-ai-agenda.html (the 2025 page)
```html
<div class="wais-2026-banner" role="note" style="padding:12px 16px;margin:0 0 16px;border:1px solid #ccc;background:#f6f6f6">
  This is the 2025 agenda. The <a href="https://www.worldaisummit.com/agenda/">World AI Summit 2026 agenda</a> (14-15 October 2026, Bengaluru) is now live.
  <a href="https://www.worldaisummit.com/delegate/">Book a 2026 delegate pass</a>.
</div>
```

---

## C. Calendar

### Fri 2 Oct: WAIS /agenda/ v1 + day-zero setup (WEB, CONTENT, PROG)
- URL: https://www.worldaisummit.com/agenda/
- Title: World AI Summit 2026 Agenda | 14-15 Oct, Bengaluru
- Meta description: Agenda for World AI Summit 2026, 14-15 October at Sheraton Grand Bangalore, Brigade Gateway: seven tracks, halls and timings, updated as sessions are confirmed.
- H1: World AI Summit 2026 agenda
- Target query: "world ai summit 2026 agenda". Today the homepage is #3, below worldsummit.ai #1 and impact.indiaai.gov.in #2, with an AI Overview above all results. OpenSEO returned no search volume.
- Layout: a Day 1 / Day 2 grid with seven track rows, each with an anchor:
  - #frontier-models-compute
  - #sovereign-ai
  - #enterprise-ai-in-production
  - #gcc
  - #robotics-agents
  - #ai-for-bharat
  - #capital-founders-exits

  Columns are halls (PLACEHOLDER_HALL_NAMES). Each cell reads "Session details to be announced" until PROG supplies it (PLACEHOLDER_SESSION_DATA; the repo has no source for it). Show "Updated <date, time IST>" at the top.
- Links in: homepage nav and hero, /speaker.html, /ai-conference-bengaluru-2026.html, and the B5 banner.
- Links out: /delegate/, /awards/, /speakers/ (once live).
- CTA: "Book your delegate pass" -> /delegate/ (price PLACEHOLDER_CURRENT_PASS_PRICE; the Standard pass validity ended on 30 Sept 2026).
- Also today: everything in B1-B5, plus the Event JSON-LD from D1 on the homepage and /agenda/. Add the performer block on 3 Oct, after /speakers/ is live.

### Sat 3 Oct: WAIS speaker post #1 + deploy speaker pages (CONTENT, WEB)
- Deploy the generator first. Run `python3 build_speakers.py --clean` in worldaisummit/speakers/, then upload dist/speakers/ and dist/sitemap-speakers.xml. Request indexing for /speakers/ and the 7 profiles below.
- URL: https://www.worldaisummit.com/blog/government-policy-leaders-world-ai-summit-2026/ (match the existing /blog/ URL pattern).
- Title: Government and Policy Leaders at World AI Summit 2026
- H1: Government and policy leaders at World AI Summit 2026
- Target queries: "world ai summit 2026 speakers" (the positions given in the project, #1/#4/#14, were not re-checked today) and name + organisation.
- Speakers (all confirmed_2026=true, verified 1 Oct). Each name links to its /speakers/<slug>/ page:
  - Pankaj Kumar Pandey, IAS: Principal Secretary, DPAR (e-Governance), Government of Karnataka (pankaj-kumar-pandey)
  - T Bhoobalan, IAS: CEO, Centre for e-Governance, and MD, KUIDFC, Government of Karnataka (t-bhoobalan)
  - Sanjeev Gupta: CEO, Karnataka Digital Economy Mission (sanjeev-gupta)
  - Dr Ravikumar Surpur, IAS: Secretary, IT & Communication Department, Government of Rajasthan (ravikumar-surpur)
  - Aman Mittal, IAS: Joint CEO, MITRA, Maharashtra (aman-mittal)
  - Hemant Garg: Deputy Director, Ministry of Labour and Employment, Government of India (hemant-garg)
  - Ram Mohan Rao: Executive Director, SEBI (ram-mohan-rao)
- Optional, also confirmed: Mahesh Hariharan Iyer (RBIH), M. Balasubramaniam (AICTE), Prajeet Prabhakaran (Embassy of Austria, Commercial Section), Dr. Sushil Kumar Meher (AIIMS).
- Links out: /agenda/#ai-for-bharat. Do not say these speakers are on that track until PROG confirms. Also /delegate/ and /awards/.
- Pages to keep live until 18 Oct: /speaker.html and /assets/speaker_details/*.html. On each, add a line "2026 speaker profiles: /speakers/".

### Sun 4 Oct: update /awards/ itself; no new post (CONTENT, WEB)
- URL: the existing page, https://www.worldaisummit.com/awards/. This is an improvement to a page that already ranks: non-www /awards is #2 for "world ai awards 2026", behind globalaiaward.com. Keep the title unchanged.
- Add the following sections:
  - 2026 categories: PLACEHOLDER_AWARD_CATEGORIES
  - Nomination fee: PLACEHOLDER_2026_NOMINATION_FEE (2025 was Rs 18,000 + GST per entry)
  - Nomination deadline: PLACEHOLDER_NOMINATION_DEADLINE
  - Jury and process: PLACEHOLDER_JURY_TEXT (name a jury member only with their consent)
  - Ceremony: "Winners will be announced on PLACEHOLDER_CEREMONY_DATE (15 October 2026 if confirmed) at World AI Summit 2026, Bengaluru."
- Add an H1 if the page lacks one: "World AI Awards 2026".
- Structured data: replace the Event block with D2, which adds offers and organizer and clears two of the three warnings.
- Links out: /delegate/ ("Attend the awards ceremony with a delegate pass") and /agenda/.
- Links in: homepage nav and Latest block, /faqs, /agenda/. Google lists the homepage and /faqs as referrers to /awards; this may be historical, so check the live HTML.

### Mon 5 Oct: ELETS CIO GCC hook + WAIS /tracks/gcc/ (ED, CONTENT)
- ELETS (cio.eletsonline.com): a news story on PLACEHOLDER_GCC_NEWS_HOOK, from the newsjacking brief. One contextual link to /tracks/gcc/ with the anchor "GCC track at World AI Summit 2026". Tag the URL with ?utm_source=eletsonline&utm_medium=referral&utm_campaign=wais2026.
- WAIS URL: https://www.worldaisummit.com/tracks/gcc/
  - Title: GCC Track | World AI Summit 2026, Bengaluru
  - H1: GCC track at World AI Summit 2026
  - Also publish a /tracks/ hub that lists all seven tracks.
- Speakers: all confirmed_2026=true leaders of India centres. PLACEHOLDER_CONFIRM_TRACK_WITH_PROG before calling them "GCC track speakers".
  - George Inasu (Fidelity National Financial India)
  - Anand Ramakrishnan (Equiniti India)
  - Tulshekar Gangireddy (JPMorgan Chase & Co)
  - Deepak Mohanty (Wells Fargo)
  - Pawan Sachdeva (Carelon Global Solutions)
  - Dipayan Chakraborty (eBay India Analytics Center)
  - Anshuma (Dogra) Singh (Applied Materials)
  - Aneel Savalagi (Takeda)
  - Sivakumar Selva Ganapathy (Johnson Controls)
  - Joyce Rodriguez (Airbus India)
  - Shireen Ali (HSBC)
- CTAs:
  - "Bringing your leadership team? Groups of 3 or more delegates get 10% off" -> /delegate/
  - `<a href="mailto:partnerships@worldaisummit.com?subject=Partner%20the%20GCC%20track">Partner the GCC track</a>`

### Tue 6 Oct: WAIS guide + ELETS eGov Karnataka hook (CONTENT, ED)
- WAIS URL: https://www.worldaisummit.com/blog/ai-events-bengaluru-october-2026/, live by 09:00 IST, before Cypher.
  - Title: AI Events in Bengaluru, October 2026: Dates and Venues
  - Target query: "ai events in bangalore october 2026" (homepage is #6 today).
- Content: a neutral, factual list.
  - Cypher 2026, KTPO Bengaluru: 7-9 Oct per cypher.analyticsindiamag.com. The aim.media listing says 6-8 Oct, so recheck the official site on the morning of publishing.
  - World AI Summit 2026: 14-15 Oct, Sheraton Grand Bangalore Hotel at Brigade Gateway.
  - Other October events: PLACEHOLDER_OTHER_OCT_EVENTS (verified only).
  - "Next month": Bengaluru Tech Summit 17-19 Nov 2026 (from project context; verify before publishing).
  - Do not quote other events' pass prices.
- ELETS (egov.eletsonline.com): a Karnataka AI story on PLACEHOLDER_KARNATAKA_AI_HOOK, linking to /tracks/ai-for-bharat/. Generic queries such as "karnataka ai policy" are led by government and national media, so the aim of this story is referral clicks, not ranking.
- WAIS URL: https://www.worldaisummit.com/tracks/ai-for-bharat/. Title: AI for Bharat Track | World AI Summit 2026.

### Wed 7 Oct: WAIS speaker post #2 (BFSI and enterprise) + track page + ELETS BFSI hook (CONTENT, ED)
- WAIS URL: https://www.worldaisummit.com/blog/bfsi-enterprise-ai-leaders-world-ai-summit-2026/
  - Title: BFSI and Enterprise AI Leaders at World AI Summit 2026
- Speakers (all confirmed):
  - Ram Mohan Rao (SEBI)
  - Mahesh Hariharan Iyer (RBIH). Do not name Sahil Kini, who is not confirmed.
  - Shantanu Dasgupta (Axis Bank)
  - Vijaya Kadiyala (DBS Bank)
  - Deepika Sandeep and Shireen Ali (HSBC)
  - Shanmugam Manivannan (Equitas Small Finance Bank)
  - Rajesh Choudhary (CSB Bank)
  - Padmanaban TA (Karnataka Bank)
  - Vishal Chugh (Tata Capital)
  - Deepak Sharma (Independent Director, Suryoday Small Finance Bank)
  - Avinash Naik (Bajaj Allianz General Insurance)
  - Optional, also confirmed: Anil Varma (MCX Clearing Corporation)
- WAIS URL: https://www.worldaisummit.com/tracks/enterprise-ai-in-production/. Title: Enterprise AI in Production Track | World AI Summit 2026.
- ELETS BFSI story on the RBI September bulletin. ED must verify the bulletin on rbi.org.in before writing (PLACEHOLDER_RBI_BULLETIN_FACTS). Link to the BFSI post.

### Thu 8 Oct: ELETS sovereign AI and compute hook + two track pages (ED, CONTENT)
- ELETS: PLACEHOLDER_SOVEREIGN_AI_HOOK, linking to /tracks/sovereign-ai/.
- WAIS URLs:
  - /tracks/sovereign-ai/ (Title: Sovereign AI & Geopolitics Track | World AI Summit 2026)
  - /tracks/frontier-models-compute/ (Title: Frontier Models & Compute Track | World AI Summit 2026)
- Speakers: PLACEHOLDER_CONFIRMED_SPEAKERS_FOR_THESE_TRACKS from PROG. Do not name the NVIDIA, NxtGen or IndiaAI leaders listed in speakers.json; none of them is confirmed.

### Fri 9 Oct: WAIS speaker post #3 (consumer, retail and founders) + two track pages (CONTENT)
- WAIS URL: https://www.worldaisummit.com/blog/consumer-retail-founders-world-ai-summit-2026/
  - Title: Consumer, Retail and Startup Leaders at World AI Summit 2026
- Speakers (all confirmed):
  - Sandeep Varaganti and Anand Thakur (Reliance Retail)
  - Suman Guha (Tata Croma, Tata Digital)
  - Archana Menon (Titan)
  - Sandeep Sharma (Shoppers Stop)
  - Kuldeep T (BigBasket)
  - Pranav Saxena (API Holdings)
  - Sandhya Vasudevan (TiE Bangalore)
  - Shashank Randev (247VC)
  - Suman Dash (Acsel Technology Forum)
- WAIS URLs:
  - /tracks/capital-founders-exits/ (Title: Capital, Founders & Exits Track | World AI Summit 2026)
  - /tracks/robotics-agents/ (Title: Robotics, Agents & Embodied AI Track | World AI Summit 2026)

### Sat 10 - Sun 11 Oct: WAIS /plan-your-visit/ + speaker directory refresh (CONTENT, WEB, PROG)
- URL: https://www.worldaisummit.com/plan-your-visit/
  - Title: Plan Your Visit | World AI Summit 2026, Bengaluru
- Content:
  - Venue: Sheraton Grand Bangalore Hotel at Brigade Gateway, 26/1 Dr. Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru, Karnataka 560055
  - Registration desk hours: PLACEHOLDER_DESK_HOURS
  - What to bring: PLACEHOLDER_ID_AND_BADGE_RULES
  - Pass types and prices: PLACEHOLDER_CURRENT_PASS_TYPES_AND_PRICES (/delegate/ lists Late Access at Rs 30,000/60,000; confirm what is on sale)
  - Contacts: registration@worldaisummit.com, secretariat@worldaisummit.com
- Speaker directory: add the session object (title, date, time, hall, track) for every confirmed speaker from PROG, rebuild, upload, and update the sitemap lastmod.

### Mon 12 Oct: curtain-raiser press release on ELETS and a wire (ED)
- Wire: PLACEHOLDER_WIRE_SERVICE. Links to /agenda/ and /delegate/.
- First paragraph template: "Bengaluru, 12 October 2026: World AI Summit 2026, Bengaluru, organised by Elets Technomedia, will be held on 14-15 October 2026 at the Sheraton Grand Bangalore Hotel at Brigade Gateway, with PLACEHOLDER_KDEM_2026_STATUS (KDEM was Strategic Partner in 2025; confirm for 2026) ..."
- Do not state the dates of the Amsterdam event. Sources disagree (5-9 vs 7-8 Oct). The words "Bengaluru" and "14-15 October" are enough to tell the two events apart.

### Tue 13 Oct: ELETS kick-off story + WAIS final agenda + live page (ED, CONTENT, WEB)
- ELETS: "World AI Summit 2026 kicks off tomorrow in Bengaluru", following the 2025 pattern. Link to /agenda/.
- WAIS /agenda/: final version with halls and times from PROG. Update lastmod and request indexing.
- Pre-create https://www.worldaisummit.com/2026/live/
  - Title: World AI Summit 2026 Live: Day 1 and Day 2 Updates
  - Holding line: "Live updates begin at PLACEHOLDER_START_TIME IST on 14 October."
  - Link it from the homepage block.

### Wed 14 Oct: Day 1 (CONTENT, ED)
- /2026/live/: time-stamped updates, with quotes taken only from the stage. Add the LiveBlogPosting JSON-LD (D3).
- /2026/day-1-highlights/ live by 21:00 IST (Title: World AI Summit 2026 Day 1 Highlights).
- ELETS: same-day keynote stories, each linking to the highlights page.

### Thu 15 Oct: Day 2 and the awards (CONTENT, WEB)
- Live blog, day 2.
- /awards/2026-winners/ within 1 hour of the ceremony (PLACEHOLDER_CEREMONY_TIME).
  - Title: World AI Awards 2026 Winners
  - Link it from /awards/ and the homepage.
- /2026/day-2-highlights/

### Fri 16 Oct: wrap-up press release + winners kit (ED, CONTENT)
- ELETS release: "World AI Summit 2026 concludes in Bengaluru". Links to /awards/2026-winners/ and both highlights pages.
- Winners share kit: badge (PLACEHOLDER_BADGE_FILE), social card, suggested post text, and the winners page URL.

### Sat 17 Oct: wrap post + homepage switch (CONTENT, WEB)
- /blog/world-ai-summit-2026-seven-takeaways/ (Title: World AI Summit 2026: Seven Tracks, Seven Takeaways), with session videos PLACEHOLDER_VIDEO_URLS.
- Homepage hero switches to the highlights and a 2027 sponsor and interest form (PLACEHOLDER_2027_FORM). Keep the URL and title of every ranking page unchanged.

### Sun 18 Oct onwards: cleanup
- 301 /speaker.html to /speakers/.
- 301 each /assets/speaker_details/<old>.html to /speakers/<slug>/ (PLACEHOLDER_OLD_TO_NEW_SLUG_MAP).
- 301 /assets/speaker_details/index.html to /speakers/.

---

## D. Structured data (paste-ready JSON-LD)

### D1. Event: homepage and /agenda/ (same @id on both)
- Add the performer array only after /speakers/ is live (3 Oct).
- Extend the array only from records with confirmed_2026=true.
- Replace every PLACEHOLDER before publishing. If no image is ready, delete the image line.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Event",
  "@id": "https://www.worldaisummit.com/#event",
  "name": "World AI Summit 2026",
  "description": "World AI Summit 2026 brings government, enterprise and startup leaders together in Bengaluru on 14-15 October 2026 across seven tracks: Frontier Models & Compute; Sovereign AI & Geopolitics; Enterprise AI in Production; GCCs; Robotics, Agents & Embodied AI; AI for Bharat; and Capital, Founders & Exits.",
  "url": "https://www.worldaisummit.com/",
  "image": ["PLACEHOLDER_EVENT_IMAGE_URL_1200x630"],
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
    "url": "https://www.eletsonline.com/"
  },
  "offers": {
    "@type": "Offer",
    "name": "Delegate pass",
    "url": "https://www.worldaisummit.com/delegate/",
    "price": "PLACEHOLDER_CURRENT_PASS_PRICE_INR",
    "priceCurrency": "INR",
    "availability": "https://schema.org/InStock",
    "validFrom": "2026-10-01"
  },
  "performer": [
    {"@type": "Person", "name": "Pankaj Kumar Pandey", "honorificSuffix": "IAS", "jobTitle": "Principal Secretary, Department of Personnel and Administrative Reforms (e-Governance)", "worksFor": {"@type": "Organization", "name": "Government of Karnataka"}, "url": "https://www.worldaisummit.com/speakers/pankaj-kumar-pandey/"},
    {"@type": "Person", "name": "T Bhoobalan", "honorificSuffix": "IAS", "jobTitle": "Chief Executive Officer, Centre for e-Governance, and Managing Director, KUIDFC", "worksFor": {"@type": "Organization", "name": "Government of Karnataka"}, "url": "https://www.worldaisummit.com/speakers/t-bhoobalan/"},
    {"@type": "Person", "name": "Sanjeev Gupta", "jobTitle": "Chief Executive Officer", "worksFor": {"@type": "Organization", "name": "Karnataka Digital Economy Mission"}, "url": "https://www.worldaisummit.com/speakers/sanjeev-gupta/"},
    {"@type": "Person", "name": "Ravikumar Surpur", "honorificPrefix": "Dr", "honorificSuffix": "IAS", "jobTitle": "Secretary, Information Technology & Communication Department", "worksFor": {"@type": "Organization", "name": "Government of Rajasthan"}, "url": "https://www.worldaisummit.com/speakers/ravikumar-surpur/"},
    {"@type": "Person", "name": "Aman Mittal", "honorificSuffix": "IAS", "jobTitle": "Joint Chief Executive Officer", "worksFor": {"@type": "Organization", "name": "Maharashtra Institution for Transformation (MITRA)"}, "url": "https://www.worldaisummit.com/speakers/aman-mittal/"},
    {"@type": "Person", "name": "Hemant Garg", "jobTitle": "Deputy Director", "worksFor": {"@type": "Organization", "name": "Ministry of Labour and Employment, Government of India"}, "url": "https://www.worldaisummit.com/speakers/hemant-garg/"},
    {"@type": "Person", "name": "Ram Mohan Rao", "jobTitle": "Executive Director", "worksFor": {"@type": "Organization", "name": "Securities and Exchange Board of India (SEBI)"}, "url": "https://www.worldaisummit.com/speakers/ram-mohan-rao/"}
  ]
}
</script>
```

### D2. Event: /awards/ (replaces the current block)
- This adds offers and organizer.
- Performer stays out until a jury member or host is confirmed and has agreed to be named. That is a warning in Google's test, not an error.
- The nomination fee goes in the page text, not in offers.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Event",
  "@id": "https://www.worldaisummit.com/awards/#event",
  "name": "World AI Awards 2026",
  "description": "The World AI Awards 2026 recognise AI work across PLACEHOLDER_CATEGORY_COUNT categories. Winners are announced at World AI Summit 2026, Bengaluru.",
  "url": "https://www.worldaisummit.com/awards/",
  "image": ["PLACEHOLDER_AWARDS_IMAGE_URL_1200x630"],
  "startDate": "2026-10-14",
  "endDate": "2026-10-15",
  "eventStatus": "https://schema.org/EventScheduled",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
  "superEvent": {"@id": "https://www.worldaisummit.com/#event"},
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
  "organizer": {"@type": "Organization", "name": "Elets Technomedia", "url": "https://www.eletsonline.com/"},
  "offers": {
    "@type": "Offer",
    "name": "Delegate pass (includes the awards ceremony)",
    "url": "https://www.worldaisummit.com/delegate/",
    "price": "PLACEHOLDER_CURRENT_PASS_PRICE_INR",
    "priceCurrency": "INR",
    "availability": "https://schema.org/InStock",
    "validFrom": "2026-10-01"
  }
}
</script>
```
If the ceremony is confirmed for 15 Oct only, set startDate and endDate to "2026-10-15".

### D3. Live blog: /2026/live/ (from 14 Oct)
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LiveBlogPosting",
  "headline": "World AI Summit 2026 Live: Day 1 and Day 2 Updates",
  "url": "https://www.worldaisummit.com/2026/live/",
  "datePublished": "2026-10-13T18:00:00+05:30",
  "dateModified": "PLACEHOLDER_LAST_UPDATE_ISO",
  "coverageStartTime": "2026-10-14T09:00:00+05:30",
  "coverageEndTime": "2026-10-15T20:00:00+05:30",
  "author": {"@type": "Organization", "name": "Elets Technomedia", "url": "https://www.eletsonline.com/"},
  "about": {"@id": "https://www.worldaisummit.com/#event"},
  "liveBlogUpdate": [
    {"@type": "BlogPosting", "headline": "PLACEHOLDER_UPDATE_HEADLINE", "datePublished": "PLACEHOLDER_UPDATE_TIME_ISO", "articleBody": "PLACEHOLDER_UPDATE_TEXT"}
  ]
}
</script>
```
Set coverageStartTime and coverageEndTime to PROG's actual start and end times. Validate every block at https://search.google.com/test/rich-results before it goes live.

---

## E. Daily 10-minute check (CONTENT), 2-17 Oct
- GSC www property: index status of every new URL. Request indexing for any URL not yet indexed after 48 hours, within the daily quota.
- Positions: "world ai summit 2026 agenda" (baseline: homepage #3), "world ai awards 2026" (baseline: /awards #2), "world ai summit 2026 speakers".
- If /awards drops below #5 after the host redirect, inspect both host URLs the same day and confirm the canonical and the 301 are single-hop.
