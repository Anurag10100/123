# A44: World AI Summit 2026 post-event share kit: speaker LinkedIn copy, organiser post, secretariat email, winner release, badge and winner post

- **For recommendation:** Post-event amplification (14-17 Oct): fill in session details on speaker pages, send 'I spoke at' kits, and send award winners a press kit linking /awards/
- **Research lens:** speakers-partners
- **Format:** Plain text (LinkedIn posts, email, press release) plus one HTML badge snippet
- **Placeholders the business must fill:**
  - PLACEHOLDER_SLUG (live filename under /assets/speaker_details/)
  - PLACEHOLDER_SESSION_TITLE (from the final agenda)
  - PLACEHOLDER_SESSION_DATE (14 or 15 October 2026, from the final agenda)
  - PLACEHOLDER_ONE_TAKEAWAY (written by the speaker, never drafted for them)
  - PLACEHOLDER_CO_SPEAKER_TAGS
  - PLACEHOLDER_SPEAKER_TAG
  - PLACEHOLDER_ROLE_AS_ON_SPEAKER_PAGE
  - PLACEHOLDER_QUOTE_FROM_RECORDING (checked against the session recording, or drop the line)
  - PLACEHOLDER_SPEAKER_SALUTATION
  - PLACEHOLDER_PHOTO_OR_VIDEO_LINK
  - PLACEHOLDER_SIGNATORY
  - PLACEHOLDER_COMPANY
  - PLACEHOLDER_COMPANY_SLUG
  - PLACEHOLDER_CATEGORY (exact award category name as announced)
  - PLACEHOLDER_AWARD_DATE (unverified; likely 14 October 2026 based on the 2025 day-1 pattern)
  - PLACEHOLDER_CITY
  - PLACEHOLDER_RELEASE_DATE
  - PLACEHOLDER_WINNING_WORK
  - PLACEHOLDER_QUOTE
  - PLACEHOLDER_SPOKESPERSON_NAME
  - PLACEHOLDER_SPOKESPERSON_TITLE
  - PLACEHOLDER_COMPANY_BOILERPLATE
  - PLACEHOLDER_COMPANY_MEDIA_CONTACT
  - PLACEHOLDER_BADGE_IMAGE_URL
  - PLACEHOLDER_ONE_LINE_THANKS_TO_TEAM_OR_CUSTOMERS
  - PLACEHOLDER_REMINDER_DATE (about 24 Oct 2026)

## How to ship

1) Precondition for A, B and C: do not send any speaker link until that speaker's live page at /assets/speaker_details/<slug>.html shows the real session title, format, date and hall. Exa confirmed on 1 Oct that sanjeev-gupta.html still shows "Session title, time and hall will be published on this page once the agenda is final". In /home/user/123/worldaisummit/speakers/speakers.json, 0 of 76 entries have a session object (50 are confirmed_2026).
   - Do not upload the generator's dist/ as it is. speakers_path is "/speakers/", so an upload creates a second set of URLs and leaves the live pages unchanged.
   - Choose one route. (a) Edit the live HTML by hand. (b) Change speakers_path and the template so the output is /assets/speaker_details/<slug>.html, then fill session {title, date, time, hall, format, track} for each confirmed speaker and rebuild.
2) Fill PLACEHOLDER_SLUG from the live filename (e.g. sanjeev-gupta). Before the mail merge, check that each final URL returns 200 without a redirect.
3) Timing for the speaker kit:
   - 14-15 Oct: organiser posts (B), one per session, tagging the speaker.
   - By 16 Oct: secretariat email (C) to the 50 confirmed speakers, with draft A pasted in.
   - Never write the takeaway, a quote or a bio for a speaker. Use quotes only if they are checked against the recording.
4) Winner kit (D, E, F):
   - Confirm PLACEHOLDER_AWARD_DATE first. It is unverified for 2026. In 2025 the awards were presented on day 1 (25 Sep 2025, per the Elets LinkedIn winners post), so 14 Oct 2026 is likely but inferred.
   - The live /awards/ page has only a nomination form: no winners section, no categories. Link to https://www.worldaisummit.com/awards/ as it is. Add a #winners anchor only if web dev builds that section first.
   - Upload the badge image and replace PLACEHOLDER_BADGE_IMAGE_URL.
   - Send the kit on ceremony day. Ask winners to keep the /awards/ hyperlink visible. The 2025 Qualitrix newsroom post (29 Sep 2025) named the summit but did not link to it, and other 2025 winners posted on LinkedIn only.
5) Set expectations:
   - Sharing will be spread over about two weeks, not concentrated on 15-17 Oct. 2025 winner posts were dated 27 Sep, 29 Sep and 14 Oct 2025, and Elets' own winners post went up 10 Oct 2025, 14-15 days after the event.
   - Send one reminder to speakers and winners around PLACEHOLDER_REMINDER_DATE (about 24 Oct).
   - Measure in GA4 through the end of October by source/medium: linkedin/speaker_share, linkedin/social, linkedin/winner_share, secretariat/email.
   - Editorial backlinks from winners are uncertain.
6) Copy rules: Indian English, calm, no exclamation marks. Keep every PLACEHOLDER_ marker until the owner fills it.
Note on the user's question ("do you have more CPUs?"): this container reports 4 CPUs (nproc). No additional CPUs are available from this session.

## Content

WORLD AI SUMMIT 2026: POST-EVENT SHARE KIT

Live speaker page pattern (the URL that ranks today): https://www.worldaisummit.com/assets/speaker_details/PLACEHOLDER_SLUG.html
Do not use the repo generator path /speakers/<slug>/. It is not live.

------------------------------------------------------------
A. SPEAKER LINKEDIN POST (speaker voice)
------------------------------------------------------------

Version 1 (short)

Thank you, World AI Summit 2026, for a great conversation on PLACEHOLDER_SESSION_TITLE in Bengaluru. PLACEHOLDER_ONE_TAKEAWAY

Session details and photos: https://www.worldaisummit.com/assets/speaker_details/PLACEHOLDER_SLUG.html?utm_source=linkedin&utm_medium=speaker_share&utm_campaign=world_ai_summit_2026_post&utm_content=PLACEHOLDER_SLUG

#WorldAISummit2026

Version 2 (with co-speaker and organiser tags)

Thank you, World AI Summit 2026, for a great conversation on PLACEHOLDER_SESSION_TITLE in Bengaluru on PLACEHOLDER_SESSION_DATE. Grateful to share the stage with PLACEHOLDER_CO_SPEAKER_TAGS, and to @World AI Summit and @Elets Technomedia for hosting.

PLACEHOLDER_ONE_TAKEAWAY

Session details and photos: https://www.worldaisummit.com/assets/speaker_details/PLACEHOLDER_SLUG.html?utm_source=linkedin&utm_medium=speaker_share&utm_campaign=world_ai_summit_2026_post&utm_content=PLACEHOLDER_SLUG

#WorldAISummit2026

Notes for the speaker (paste under the draft in the email):
- Please write the takeaway yourself, in one or two sentences.
- Please keep the link as it is. The code at the end only tells us how many people reached your page from your post.
- To tag, type @ and choose the page from the list that appears.

------------------------------------------------------------
B. ORGANISER POST (World AI Summit and Elets LinkedIn, 14-15 Oct, one per session)
------------------------------------------------------------

PLACEHOLDER_SPEAKER_TAG, PLACEHOLDER_ROLE_AS_ON_SPEAKER_PAGE, on PLACEHOLDER_SESSION_TITLE at World AI Summit 2026, Bengaluru.

"PLACEHOLDER_QUOTE_FROM_RECORDING"

Session details: https://www.worldaisummit.com/assets/speaker_details/PLACEHOLDER_SLUG.html?utm_source=linkedin&utm_medium=social&utm_campaign=world_ai_summit_2026_post&utm_content=PLACEHOLDER_SLUG

#WorldAISummit2026

(Use only words the speaker actually said, checked against the recording. If no quote has been checked, drop that line. Do not use a lnkd.in link or a bare homepage link.)

------------------------------------------------------------
C. SECRETARIAT COVER EMAIL (from secretariat@worldaisummit.com, by 16 Oct)
------------------------------------------------------------

Subject: Thank you for speaking at World AI Summit 2026: your session page and photos

Dear PLACEHOLDER_SPEAKER_SALUTATION,

Thank you for joining us at World AI Summit 2026 in Bengaluru, and for speaking on PLACEHOLDER_SESSION_TITLE.

Your speaker page now has your session details:
https://www.worldaisummit.com/assets/speaker_details/PLACEHOLDER_SLUG.html?utm_source=secretariat&utm_medium=email&utm_campaign=world_ai_summit_2026_post&utm_content=PLACEHOLDER_SLUG

Photos from your session: PLACEHOLDER_PHOTO_OR_VIDEO_LINK

If you would like to share the session on LinkedIn, there is a short draft below. Please add one takeaway in your own words and edit it as you wish.

[Paste Version 1 from section A, with the slug and session title filled in]

If anything on your page needs correcting, such as your designation, photo or session title, please reply to this email and we will update it.

Warm regards,
PLACEHOLDER_SIGNATORY
World AI Summit Secretariat, Elets Technomedia
secretariat@worldaisummit.com

------------------------------------------------------------
D. WINNER PRESS RELEASE TEMPLATE
------------------------------------------------------------

Headline: PLACEHOLDER_COMPANY wins PLACEHOLDER_CATEGORY at World AI Awards 2026

Dateline: PLACEHOLDER_CITY, PLACEHOLDER_RELEASE_DATE

PLACEHOLDER_COMPANY was named winner of PLACEHOLDER_CATEGORY at the World AI Awards, presented at World AI Summit 2026 in Bengaluru on PLACEHOLDER_AWARD_DATE.

The award recognises PLACEHOLDER_WINNING_WORK (one factual sentence on the product, deployment or project that was entered, with one result the company can verify).

"PLACEHOLDER_QUOTE," said PLACEHOLDER_SPOKESPERSON_NAME, PLACEHOLDER_SPOKESPERSON_TITLE, PLACEHOLDER_COMPANY.

World AI Summit 2026 was organised by Elets Technomedia and held on 14-15 October 2026 at the Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. Details of the World AI Awards are at https://www.worldaisummit.com/awards/.

About PLACEHOLDER_COMPANY
PLACEHOLDER_COMPANY_BOILERPLATE

About World AI Summit
World AI Summit 2026 was organised by Elets Technomedia in Bengaluru on 14-15 October 2026. The programme covered seven tracks: Frontier Models & Compute; Sovereign AI & Geopolitics; Enterprise AI in Production; GCCs; Robotics, Agents & Embodied AI; AI for Bharat; and Capital, Founders & Exits. https://www.worldaisummit.com/

Media contact: PLACEHOLDER_COMPANY_MEDIA_CONTACT

Note for the winner's communications team: please publish https://www.worldaisummit.com/awards/ as a visible, clickable hyperlink in the newsroom version, and keep it when you syndicate the release. A text mention of the summit without a link does not help readers find the awards page.

------------------------------------------------------------
E. WINNER BADGE EMBED (for the winner's newsroom or awards page)
------------------------------------------------------------

<a href="https://www.worldaisummit.com/awards/"><img src="PLACEHOLDER_BADGE_IMAGE_URL" alt="PLACEHOLDER_COMPANY, winner of PLACEHOLDER_CATEGORY, World AI Awards 2026" width="240" height="240" loading="lazy"></a>

------------------------------------------------------------
F. WINNER LINKEDIN POST (company voice, same day as the release)
------------------------------------------------------------

PLACEHOLDER_COMPANY has been named winner of PLACEHOLDER_CATEGORY at the World AI Awards, presented at World AI Summit 2026 in Bengaluru. PLACEHOLDER_ONE_LINE_THANKS_TO_TEAM_OR_CUSTOMERS

About the World AI Awards: https://www.worldaisummit.com/awards/?utm_source=linkedin&utm_medium=winner_share&utm_campaign=world_ai_summit_2026_post&utm_content=PLACEHOLDER_COMPANY_SLUG

#WorldAISummit2026
