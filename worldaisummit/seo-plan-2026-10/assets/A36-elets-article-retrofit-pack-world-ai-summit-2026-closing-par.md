# A36: Elets article retrofit pack: World AI Summit 2026 closing paragraphs, track fixes and speaker boxes (8 live pages)

- **For recommendation:** Retrofit existing Elets WAIS and speaker articles with descriptive deep links (not bare homepage URLs) and fix their factual errors
- **Research lens:** elets-network
- **Format:** Per-article edit instructions with ready-to-paste HTML (paste into the CMS Text/Code view, not the visual editor)
- **Placeholders the business must fill:**
  - PLACEHOLDER_DELEGATE_COUNT: one agreed delegate figure (22 Sep says 1,200+, 30 Sep says 1,000+)
  - PLACEHOLDER_EDITION_NUMBER: only if an article states an edition (LinkedIn says 3rd, some pages say 2nd)
  - PLACEHOLDER_TRACK_ANCHOR: section ids on /ai-conference-bengaluru-2026.html, only if the web team adds them
  - PLACEHOLDER_KDEM_2026_PARTNER_STATUS: confirm before calling KDEM the 2026 Strategic Partner anywhere
  - PLACEHOLDER_SPEAKER_PAGES_LIVE: switch speaker-box links to /speakers/<slug>/ once deployed and returning 200

## How to ship

Owner: Elets editorial (CIO, eGov and BFSI desks). Deadline: 3 Oct 2026. Effort: about 2 hours.

1. Open each article in the CMS Text/HTML view and make the numbered edits. If the desk uses the visual editor, type a plain "&" in place of "&amp;".
2. Decide PLACEHOLDER_DELEGATE_COUNT before editing 76367 and 76379, so both articles carry the same figure.
3. After publishing, view the page source of each article. Check that every worldaisummit.com link is a real <a href> with no UTM and no nofollow, that the en dash in "14–15" shows correctly, and that no old track names are left. To find leftovers, search the page for "Agentic AI", "Ethics" and "2025".
4. Speaker titles are copied exactly from title_role in /home/user/123/worldaisummit/speakers/speakers.json. All three speakers have confirmed_2026=true. No bio text was added.

Measuring it: after 7 days, check GA4 source/medium for cio.eletsonline.com, egov.eletsonline.com and bfsi.eletsonline.com referrals. Removing the UTM on 76296 means its traffic will show up as a cio.eletsonline.com referral, no longer as the ai_in_india_dpi_global_leadership campaign.

Expected impact, kept modest per the 1 Oct verification:
- Referral traffic should be small. The one tagged article drew 21 sessions in about 2 months, which is roughly 5 per fortnight.
- cio.eletsonline.com sent no measurable untagged referrals in Jul–Sep. A likely reason is that the closing URLs are plain text, not hyperlinks. This edit fixes that.
- There is no evidence the edit will move "ai summit 2026 registration" (#10). That ranking belongs to the homepage, not /delegate/.
- Whether the www deep pages are indexed is unknown, because Search Console only covers the non-www property. Adding the www property would settle it.
- The surer gain is removing wrong track and edition claims from pages that sponsors and delegates read.

On your question about CPUs: this cloud session runs on a 4-CPU container. It cannot use your own computer's CPUs, and this task did not need more.

## Content

=== SHARED BLOCKS ===

BLOCK A: full closing paragraph (for articles that do not already list the 2026 tracks correctly)
<p>World AI Summit 2026 takes place on 14–15 October 2026 at the Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru, across seven tracks: Frontier Models &amp; Compute; Sovereign AI &amp; Geopolitics; Enterprise AI in Production; Global Capability Centres; Robotics, Agents &amp; Embodied AI; AI for Bharat; and Capital, Founders &amp; Exits. <a href="https://www.worldaisummit.com/delegate/">Book a World AI Summit 2026 delegate pass</a>, see the <a href="https://www.worldaisummit.com/speaker.html">World AI Summit 2026 speakers</a>, read about this <a href="https://www.worldaisummit.com/ai-conference-bengaluru-2026.html">AI conference in Bengaluru in October 2026</a>, or <a href="https://www.worldaisummit.com/awards/">nominate for the World AI Awards 2026</a>. For sponsorship and exhibition, write to <a href="mailto:partnerships@worldaisummit.com">partnerships@worldaisummit.com</a>.</p>

BLOCK B: short closing paragraph (for articles whose body already lists all seven 2026 tracks)
<p>World AI Summit 2026 takes place on 14–15 October 2026 at the Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. <a href="https://www.worldaisummit.com/delegate/">Book a World AI Summit 2026 delegate pass</a>, see the <a href="https://www.worldaisummit.com/speaker.html">World AI Summit 2026 speakers</a>, read about this <a href="https://www.worldaisummit.com/ai-conference-bengaluru-2026.html">AI conference in Bengaluru in October 2026</a>, or <a href="https://www.worldaisummit.com/awards/">nominate for the World AI Awards 2026</a>. For sponsorship and exhibition, write to <a href="mailto:partnerships@worldaisummit.com">partnerships@worldaisummit.com</a>.</p>

BLOCK C: seven-track list (body of a "tracks" section)
<p>The 2026 programme runs across seven tracks:</p>
<ul>
<li>Frontier Models &amp; Compute</li>
<li>Sovereign AI &amp; Geopolitics</li>
<li>Enterprise AI in Production</li>
<li>Global Capability Centres</li>
<li>Robotics, Agents &amp; Embodied AI</li>
<li>AI for Bharat</li>
<li>Capital, Founders &amp; Exits</li>
</ul>
<p>Read the <a href="https://www.worldaisummit.com/ai-conference-bengaluru-2026.html">World AI Summit 2026 track guide</a> for what each track covers.</p>

Rules for every edit: clean URLs only (no UTM parameters), real <a href> hyperlinks (not plain-text URLs), no rel="nofollow" added by the CMS, no edition number ("2nd"/"3rd") unless PLACEHOLDER_EDITION_NUMBER is decided, no new speaker bios.


=== 1. CIO, 22 Sep 2026 (76367) ===
URL: https://cio.eletsonline.com/article/beyond-the-hype-the-room-where-ais-next-chapter-takes-shape/76367/
Edit 1. Section "Tracks Mapping the AI Landscape": keep the heading, delete the old track list and any per-track text about the old tracks (Generative AI & LLMs ... AI Ethics & Regulation), and paste BLOCK C in its place.
Edit 2. Closing paragraph: find the phrase
  generative AI and LLMs, agentic AI, infrastructure, enterprise adoption, government services and responsible AI
replace it with
  seven tracks, from Frontier Models &amp; Compute to Capital, Founders &amp; Exits
then read the whole sentence again and fix the grammar around it.
Edit 3. Change "1,200+ delegates" to "PLACEHOLDER_DELEGATE_COUNT delegates". The 30 Sep article (76379) says 1,000+. Use one agreed figure in both articles.
Edit 4. If the article ends with a "For More Updates, visit: https://www.worldaisummit.com/" line, delete it. Then add BLOCK B as the last paragraph. BLOCK B is enough because Edit 1 now lists the tracks.

=== 2. CIO, 24 Sep 2026 (76373) ===
URL: https://cio.eletsonline.com/article/inside-the-boardroom-how-ceos-are-reimagining-business-with-ai/76373/
Edit 1. The closing paragraph names six old tracks: Generative AI & LLMs, Agentic AI, AI Infrastructure & Cloud, AI in Enterprises, AI in Government & Public Services, AI Ethics & Regulation. It also leaves out GCCs. Delete only the sentence or clause that lists them and keep the rest of the paragraph.
Edit 2. Add BLOCK A as a new final paragraph after the line ending "...know how to lead with it."
Edit 3. Check the live HTML. If there is a "For More Updates" homepage line (the Exa text did not show one), delete it.

=== 3. CIO, 30 Sep 2026 (76379) ===
URL: https://cio.eletsonline.com/article/7-ai-questions-india-needs-to-answer-next/76379/
The tracks are already correct. Do not change them.
Edit 1. Replace the line "For more updates, check: https://www.worldaisummit.com" with BLOCK B.
Edit 2. Change "1,000+" delegates to PLACEHOLDER_DELEGATE_COUNT (the same figure as in 76367).
Optional: if the web team adds id attributes to the track sections of /ai-conference-bengaluru-2026.html, link each track heading to https://www.worldaisummit.com/ai-conference-bengaluru-2026.html#PLACEHOLDER_TRACK_ANCHOR. Without anchors, skip this: seven links to the same URL add nothing.

=== 4. CIO, 1 Aug 2026 (76296) ===
URL: https://cio.eletsonline.com/article/ai-in-india-from-digital-public-infrastructure-to-global-leadership/76296/
Edit 1. Replace the closing WAIS line and its UTM-tagged link (campaign ai_in_india_dpi_global_leadership) with BLOCK A.

=== 5. eGov, 25 Jul 2026 ===
URL: https://egov.eletsonline.com/2026/07/the-next-chapter-of-ai-what-will-define-2026-and-beyond/
Edit 1. Change the subheading
  Why Bengaluru Is the Right Place for This Conversation at World AI Summit 2025
to
  Why Bengaluru Is the Right Place for This Conversation at World AI Summit 2026
Edit 2. Replace the old-style theme list in that section with
  seven tracks, from Frontier Models &amp; Compute to Capital, Founders &amp; Exits
or delete the list. Read the sentence again afterwards.
Edit 3. Add BLOCK A as the final paragraph. If there is an existing bare homepage URL line, delete it.

=== 6. BFSI, 5 Sep 2026: speaker box ===
URL: https://bfsi.eletsonline.com/ai-led-transformation-and-autonomous-finance-why-trust-matters-more-than-ai/
Place it after the "Views expressed by" line, or as the final paragraph.
<p><strong>Speaking at World AI Summit 2026:</strong> Tulshekar Gangireddy, ED and Head of Data Strategy, JPMorgan Chase, joins the <a href="https://www.worldaisummit.com/speaker.html">World AI Summit 2026 speaker line-up</a> in Bengaluru on 14–15 October. <a href="https://www.worldaisummit.com/delegate/">Book your pass</a>.</p>

=== 7. eGov, Apr 2026: speaker box ===
URL: https://egov.eletsonline.com/2026/04/from-digital-infrastructure-to-intelligent-administration-karnatakas-ai-blueprint/
Place it as the final paragraph.
<p><strong>Speaking at World AI Summit 2026:</strong> Pankaj Kumar Pandey, IAS, Principal Secretary, e-Governance, Karnataka, joins the <a href="https://www.worldaisummit.com/speaker.html">World AI Summit 2026 speaker line-up</a> in Bengaluru on 14–15 October. <a href="https://www.worldaisummit.com/delegate/">Book your pass</a>.</p>

=== 8. eGov, 8 Aug 2026 (KDEM): speaker box ===
URL: https://egov.eletsonline.com/2026/08/kdem-goodworks-target-5000-crore-gcc-investment-in-karnataka/
Place it as the final paragraph. Do not call KDEM the 2026 Strategic Partner: only the 2025 partnership is verified (PLACEHOLDER_KDEM_2026_PARTNER_STATUS).
<p><strong>Speaking at World AI Summit 2026:</strong> Sanjeev Gupta, CEO, Karnataka Digital Economy Mission, joins the <a href="https://www.worldaisummit.com/speaker.html">World AI Summit 2026 speaker line-up</a> in Bengaluru on 14–15 October. <a href="https://www.worldaisummit.com/delegate/">Book your pass</a>.</p>

Speaker-page switch (later): once the repo generator output is live and returns 200, change the speaker-line-up href in boxes 6–8 to https://www.worldaisummit.com/speakers/tulshekar-gangireddy/, https://www.worldaisummit.com/speakers/pankaj-kumar-pandey/ and https://www.worldaisummit.com/speakers/sanjeev-gupta/. Until then, keep /speaker.html (PLACEHOLDER_SPEAKER_PAGES_LIVE).
