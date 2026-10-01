# A71: World AI Summit 2026 speaker and partner share kit (corrected): emails, quote card spec, caption rule, agenda-anchor dependency

- **For recommendation:** Speaker and partner share kit: session photo, verbatim quote card and deep link, plus post-event updates to speaker pages
- **Research lens:** event-week-postevent
- **Format:** Plain-text email templates, spec sheets, and HTML/JSON snippets (Markdown), ready to paste into the mail tool, design brief and CMS
- **Placeholders the business must fill:**
  - PLACEHOLDER_SPEAKER_PAGE_URL (per speaker: /assets/speaker_details/<slug>.html today, or /speakers/<slug>/ if that build is deployed)
  - PLACEHOLDER_AGENDA_LOCK_DATE (programme team must lock sessions before 13 Oct)
  - PLACEHOLDER_CORRECTION_DEADLINE (Email A)
  - PLACEHOLDER_APPROVAL_DEADLINE (Email B quote approval)
  - PLACEHOLDER_WAIS_LINKEDIN_PAGE_URL (which LinkedIn page speakers should tag)
  - PLACEHOLDER_SENDER_NAME
  - PLACEHOLDER_VIDEO_LINE / PLACEHOLDER_VIDEO_DATE (only if recordings will be published)
  - PLACEHOLDER_PARTNER_LOGO_RULE (whether partner logos appear on quote cards)
  - PLACEHOLDER_SHARED_FOLDER and PLACEHOLDER_PHOTO_TURNAROUND_HOURS (photographer delivery)
  - PLACEHOLDER_HALL_SLUG, PLACEHOLDER_HALL, PLACEHOLDER_TRACK, PLACEHOLDER_FORMAT, PLACEHOLDER_SESSION_TITLE, PLACEHOLDER_HHMM-HHMM IST (from the locked agenda)
  - PLACEHOLDER_HEADER_HEIGHT (sticky header offset for anchor scrolling)
  - [partner category as per contract] and [N] photos (Email C)

## How to ship

1) Programme team, by PLACEHOLDER_AGENDA_LOCK_DATE (must be before 13 Oct): lock sessions, halls, times and the printed speaker names, roles and organisations, then enter each confirmed speaker's session block in /home/user/123/worldaisummit/speakers/speakers.json (session is empty for all 76 entries today).
2) Web dev, before 13 Oct: publish https://www.worldaisummit.com/agenda/ using the section 7 anchor pattern, link it from the homepage navigation and /speaker.html, and link each speaker name to their page. Test 3 random anchors on mobile. If the page is not live by 13 Oct, use the speaker-page fallback links throughout and do not send any /agenda/ link.
3) Marketing, 13 Oct: send Email A to confirmed_2026 = true speakers only, with the 'Speaking at' card. Run the link gate check on every URL.
4) Event days, 14-15 Oct: the photographer files selects by session-id. Content pulls a verbatim quote of 25 words or fewer from the recording, the designer builds the card to the section 3 spec, and Email B goes out within 24 hours (Day 2 by 16 Oct).
5) Only after a speaker replies 'approved': post section 4 on the WAIS LinkedIn page with the link as the last line, and log it in the tracker.
6) By 16 Oct: send Email C to partners and exhibitors.
7) Post-event, web dev and content: add summaries and photos to the agenda sessions and update the speaker pages (section 8). Do not retitle priyank-kharge.html as 2026.
Measure: UTM campaign wais2026_speaker_share in analytics for 14-31 Oct, plus new referring domains from company pages over the following weeks. Nothing in this kit needs OpenSEO paid tools.

## Content

WORLD AI SUMMIT 2026: SPEAKER AND PARTNER SHARE KIT
(Corrected 1 Oct 2026. The kit does not use the edition number: the LinkedIn showcase page says "2nd Edition" and other sources say 3rd. Write "World AI Summit 2026".)

==================================================
0. LINK GATE: finish this before any email goes out
==================================================
- The /agenda/#[session-id] deep link does not work today. https://www.worldaisummit.com/agenda/ and /agenda.html return not-found. The only agenda pages on the site are the 2025 archive (/1st-edition/world-ai-agenda.html) and a 2025 URL that 302-redirects. The homepage only says the agenda "will cover..." Two things must happen before any agenda link is used:
  (a) The programme team locks session titles, dates, times, halls and the printed speaker names, roles and organisations.
  (b) Web dev publishes https://www.worldaisummit.com/agenda/ with one anchor per session (pattern in section 7).
- Until /agenda/ returns 200 and each anchor scrolls to the right session, every email, card and post links to the speaker's own page instead: PLACEHOLDER_SPEAKER_PAGE_URL. Today that is https://www.worldaisummit.com/assets/speaker_details/<slug>.html. Use /speakers/<slug>/ only if the team deploys that build, and add 301s from the old URLs when they do.
- Before each send, open the exact link in a private mobile window. It must load with no 404 and no redirect to the homepage.
- speakers.json has no session data yet. `session` is empty for all 76 entries, 50 of which are confirmed_2026 = true. Enter title, date, time, hall, format and track from the locked agenda before Email A.
- Send only to speakers with confirmed_2026 = true who actually spoke. Do not send to 2025-only speakers, for example Priyank Kharge (confirmed_2026 = false, publish = false).

==================================================
1. EMAIL A: PRE-EVENT (send 13 Oct)
==================================================
Subject: Your World AI Summit 2026 speaker page

Dear [Honorific] [Last name],

Thank you for joining us as a speaker at World AI Summit 2026, 14-15 October, Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru.

Your speaker page is live: [SPEAKER_PAGE_URL]
Your session: '[Session title]', [Day, date], [time] IST, [Hall]

Please check your name, designation and organisation on the page, and send any correction by PLACEHOLDER_CORRECTION_DEADLINE. We use the same details on stage screens, photo captions and quote cards.

We have attached a 'Speaking at World AI Summit 2026' card. If you post about your session, please include the link to your speaker page and tag World AI Summit (PLACEHOLDER_WAIS_LINKEDIN_PAGE_URL).

Warm regards,
PLACEHOLDER_SENDER_NAME
Speaker Relations, World AI Summit 2026 | Elets Technomedia
secretariat@worldaisummit.com

'Speaking at' card: 1200 x 1200 px. Text: "Speaking at World AI Summit 2026"; name, role and organisation exactly as in the agenda; session title; "14-15 Oct | Bengaluru". Use a speaker photo only if the speaker or their office supplied it.

==================================================
2. EMAIL B: POST-SESSION (within 24 hours of the session; Day 2 sessions by 16 Oct)
==================================================
Subject: Your World AI Summit 2026 session: photo and link

Dear [Honorific] [Last name],

Thank you for speaking on '[Session title]' at World AI Summit 2026.

Your session summary and photos are at [SESSION_LINK_CLEAN] and your speaker page is [SPEAKER_PAGE_URL].
[FALLBACK if /agenda/ is not live: replace the line above with "Your speaker page is at [SPEAKER_PAGE_URL]."]

We have attached 2 stage photos and a quote card with this line from your session:
"[verbatim quote]"

Please reply 'approved' or send a correction by PLACEHOLDER_APPROVAL_DEADLINE. We will not publish the quote or the card until you approve it.

If you post, please include the link and tag World AI Summit. If your organisation has a speaker, media or events page, a short 'Speaking' entry that links to [SESSION_LINK_CLEAN] would help people find the session.

PLACEHOLDER_VIDEO_LINE (use only if a recording will be published, for example: "We will add the session recording to your speaker page by PLACEHOLDER_VIDEO_DATE." Otherwise delete this line.)

Suggested post, if useful (edit freely):
"Thank you to World AI Summit for having me on '[Session title]' in Bengaluru. [One line in your own words.] Session summary: [SESSION_LINK_UTM]"

Warm regards,
PLACEHOLDER_SENDER_NAME
Speaker Relations, World AI Summit 2026 | Elets Technomedia
secretariat@worldaisummit.com

Link values:
- [SESSION_LINK_CLEAN] = https://www.worldaisummit.com/agenda/#[session-id] (for company websites, so the backlink has no UTM). Until /agenda/ is live, use [SPEAKER_PAGE_URL].
- [SESSION_LINK_UTM] = https://www.worldaisummit.com/agenda/?utm_source=linkedin&utm_medium=social&utm_campaign=wais2026_speaker_share#[session-id]. The query string goes before the #. Until /agenda/ is live, use the speaker page URL with the same UTM.

==================================================
3. QUOTE CARD SPEC
==================================================
- Canvas: 1200 x 1200 px, sRGB, PNG or JPG under 1 MB, 80 px safe margin on all sides.
- Quote: 25 words or fewer, verbatim from the recording, or from a transcript checked against the recording. Do not change, add or reorder words. Do not put a paraphrase inside quotation marks. If no clean line of 25 words or fewer exists, pick a different line. Mark any cut inside the line with an ellipsis (…), and the speaker must approve the cut.
- Attribution: [Name], [Role], [Org], exactly as printed in the agenda, including honorific, spelling and any suffix such as IAS.
- Optional small line: '[Session title]'.
- Footer: World AI Summit 2026 | Bengaluru | 14-15 Oct
- Logos: World AI Summit logo. Partner logos only where PLACEHOLDER_PARTNER_LOGO_RULE requires them.
- Photo: a stage photo from this session, or a headshot the speaker supplied. Never use an image found on the web.
- File name: wais2026-quote-[slug].png
- Alt text: Quote card: "[quote]" - [Name], [Role], [Org], at World AI Summit 2026, Bengaluru
- Status: draft until the speaker replies 'approved'. Log the approval date and email in the tracker (section 9).

==================================================
4. LINKEDIN POST: WORLD AI SUMMIT PAGE (ends with the deep link)
==================================================
"[verbatim quote]"

[Name], [Role], [Org], on '[Session title]' at World AI Summit 2026, Bengaluru.

[One or two sentences on what the session covered. Write them from the recording and have the programme team check them. Include no claim the speaker did not make.]

#WorldAISummit2026 #AI #Bengaluru
Session summary and photos: [SESSION_LINK_UTM]

Rules: tag the speaker and their organisation. The link is always the last line. Do not end with 'Stay tuned for more insights...', the line the 2025 posts ended on, none of which linked to worldaisummit.com. Post only after the speaker approves the quote.

==================================================
5. PHOTO CAPTION AND ALT TEXT RULE
==================================================
- Caption: 'Left to right: [Name], [Role], [Org]; [Name], [Role], [Org].' Take names, roles and organisations only from the printed agenda.
- If anyone in the frame is not in the agenda (a changed moderator, an unannounced guest), do not guess a name. Confirm with the programme desk or use another frame.
- Alt text, single speaker: '[Name] speaking on [topic] at World AI Summit 2026, Bengaluru'
- Alt text, panel: '[Name], [Name] and [Name] on the [topic] panel at World AI Summit 2026, Bengaluru'
- File names: wais2026-[session-id]-1.jpg, -2.jpg. Send speakers a 2048 px long edge. Web copies: 1200 px wide, under 200 KB.
- The photographer delivers 2-3 selects per session to PLACEHOLDER_SHARED_FOLDER within PLACEHOLDER_PHOTO_TURNAROUND_HOURS hours, filed by session-id.

==================================================
6. EMAIL C: PARTNERS AND EXHIBITORS (by 16 Oct)
==================================================
Subject: World AI Summit 2026: photos from your booth

Dear [First name],

Thank you for being part of World AI Summit 2026 as [partner category as per contract].

We have attached [N] photos from your booth [and session]. Captions are listed against each file name.

If you post, or add the event to your news or events page, please link to [PARTNER_LINK] and tag World AI Summit.

For partnership enquiries for the next edition, please write to partnerships@worldaisummit.com.

Warm regards,
PLACEHOLDER_SENDER_NAME
World AI Summit 2026 | Elets Technomedia

[PARTNER_LINK] = https://www.worldaisummit.com/agenda/ once it is live; until then https://www.worldaisummit.com/

==================================================
7. DEPENDENCY: AGENDA PAGE WITH SESSION ANCHORS (web dev)
==================================================
Anchor id format: s-[day]-[hhmm]-[hall-slug], for example s-d1-1115-PLACEHOLDER_HALL_SLUG. Never change an id once it has been shared.

<section class="session" id="s-d1-1115-PLACEHOLDER_HALL_SLUG">
  <h3>PLACEHOLDER_SESSION_TITLE</h3>
  <p class="meta"><time datetime="2026-10-14T11:15+05:30">14 Oct, 11:15</time>-<time datetime="2026-10-14T12:00+05:30">12:00</time> IST | PLACEHOLDER_HALL | PLACEHOLDER_TRACK</p>
  <ul class="speakers">
    <li><a href="PLACEHOLDER_SPEAKER_PAGE_URL">[Name]</a>, [Role], [Org]</li>
  </ul>
  <p class="summary">[60-120 words added after the session, written from the recording]</p>
  <figure>
    <img src="/assets/agenda/2026/s-d1-1115-PLACEHOLDER_HALL_SLUG-1.jpg" width="1200" height="800" loading="lazy" alt="[Name] speaking on [topic] at World AI Summit 2026, Bengaluru">
    <figcaption>Left to right: [Name], [Role], [Org]; ...</figcaption>
  </figure>
  <p><a href="#s-d1-1115-PLACEHOLDER_HALL_SLUG">Link to this session</a></p>
</section>
<style>.session{scroll-margin-top:PLACEHOLDER_HEADER_HEIGHTpx}</style>

The times and day above are examples only. Real values come from the locked agenda.
Also: link /agenda/ from the homepage navigation and from /speaker.html, and link every speaker name to their page. This gives the speaker pages and /speaker.html internal links; the audit found them only in the sitemap (crawlDepth null).

==================================================
8. SPEAKER PAGES AFTER THE EVENT
==================================================
speakers.json session block for each confirmed speaker. The generator already reads these fields:
"session": {
  "title": "PLACEHOLDER_SESSION_TITLE",
  "date": "2026-10-14",
  "time": "PLACEHOLDER_HHMM-HHMM IST",
  "hall": "PLACEHOLDER_HALL",
  "format": "PLACEHOLDER_FORMAT",
  "track": "PLACEHOLDER_TRACK"
}
- Set date to 2026-10-14 or 2026-10-15 as per the agenda.
- The generator has no fields yet for the video link, stage photo or agenda anchor. Web dev (small task): add session.video_url, session.photo and session.anchor, and render a "Session summary" link to /agenda/#[anchor]. If the team keeps the /assets/speaker_details/ pages instead, add the same items by hand.
- Bios: never write them from memory. Use only what the speaker or their office supplied, or what is already in the data file.
- /assets/speaker_details/priyank-kharge.html: keep the title 'Shri Priyank Kharge | Chief Guest | World AI Summit 2025', because it is accurate. Optional line at the end of the page: "World AI Summit 2026 takes place on 14-15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. See the 2026 programme." Link it to /agenda/, or to / until /agenda/ is live. Do not present him as a 2026 speaker unless he confirms. He is the only one of the roughly 50 speaker_details pages with a 2025 title; the others already say 2026.

==================================================
9. TRACKER COLUMNS (one row per session and per speaker)
==================================================
slug | name as in agenda | session-id | link live (Y/N, date checked) | Email A sent | photos received | quote drafted | Email B sent | quote approved (date, by whom) | WAIS post URL | speaker post URL | company page link URL | partner (Y/N)
