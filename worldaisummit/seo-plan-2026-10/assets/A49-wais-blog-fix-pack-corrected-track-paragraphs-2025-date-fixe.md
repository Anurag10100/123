# A49: WAIS blog fix pack: corrected track paragraphs, 2025 date fixes, bylines and dates, Article JSON-LD and canonical tags (Beyond the Hype, Inside the Boardroom, The Next Chapter of AI, AI in India, Skills)

- **For recommendation:** Stop republishing Elets articles on /blog/: fix the duplicate posts, the wrong track list and missing dates, and use the blog only for event-specific posts
- **Research lens:** news-content
- **Format:** HTML snippets plus JSON-LD, grouped by page. Each block says whether it goes on the worldaisummit.com copy (WAIS), the Elets copy, or both.
- **Placeholders the business must fill:**
  - PLACEHOLDER_CANONICAL_DIRECTION: Elets editorial picks Option A (Elets copies canonical to worldaisummit.com, preferred) or Option B (WAIS copies canonical to Elets originals); decide by 9 Oct
  - PLACEHOLDER_SKILLS_BYLINE: byline for 'The Skills That Will Matter Most in an AI-Driven World' (no Elets copy found, so the author is unverified); used in the visible byline, the /blog/ card and the JSON-LD author name

## How to ship

Owner: web dev (WAIS static HTML), content (copy review), Elets editorial (cio/egov copies and the canonical decision). Order and deadlines:
1) By 3 Oct, web dev:
   - Add id="tracks" to the "Key AI Topics and Tracks" H2 on /ai-conference-bengaluru-2026.html.
   - Make the text edits in sections 1, 2 and 3 on the WAIS copies.
   - Add the byline and date lines (section 4) to each post and to the /blog/ cards.
   - Add the CTA paragraph (section 5).
   - Paste the JSON-LD (section 6) into each post's <head>.
   Before publishing:
   - Set dateModified and the visible "Updated" date to the day you actually ship. 2026-10-02 is the default.
   - Confirm 2026-09-28 against the server upload date of each blog file. That date comes from Exa crawl metadata, not the CMS.
   - Use the HTML-escaped &amp; inside HTML. Use plain & in the FAQ text if your CMS escapes it for you.
2) By 3 Oct, Elets editorial makes the same text edits on cio 76367 (1a, 1b, 1c) and cio 76373 (section 2), with absolute worldaisummit.com links. They should also check whether the egov copy of The Next Chapter has the same "2025" H2 (3a, 3b) and fix it if so.
3) By 9 Oct, decide PLACEHOLDER_CANONICAL_DIRECTION, then apply only that option's tags from section 7. Do not use both directions on the same pair.
4) Homepage FAQ (section 8): same day as step 1. Whoever owns the /index.html canonical issue should also open /index.html in a private window and check it shows the seven new tracks. Exa returned an older "Six tracks" variant for that URL, which may only be cache lag.
5) Validate:
   - Run each post through https://validator.schema.org/ and the Google Rich Results Test.
   - Run a quick crawl or check that no link points to /agenda/.
   - Request indexing of the five posts and /blog/ in Search Console. The connected property is non-www only, so add the https://www.worldaisummit.com/ property first if possible.
Optional: add an "image" property (the post's hero image URL) to each JSON-LD block. It is recommended by Google, but it was left out because the image URLs were not verified.
Sources (1 Oct 2026, Exa fetch/search, 0 OpenSEO credits): the WAIS post texts; /blog/; /ai-conference-bengaluru-2026.html (seven tracks, "1,000+ Delegates"); cio 76367 (22 Sep 2026), cio 76373 (24 Sep 2026) and cio 76296 (1 Aug 2026), all bylined Elets News Network; egov Next Chapter (sidebar date 25 Jul 2026, Yoast author "Elets News Network"); cio 76379 (30 Sep 2026, "1,000+ delegates", seven tracks).

## Content

=====================================================================
0. WHAT CHANGED FROM THE ORIGINAL RECOMMENDATION (read first)
=====================================================================
- /agenda/ does not exist (Exa CRAWL_NOT_FOUND; it is not in audit c1b16b55). Every link below points to the seven-track section of /ai-conference-bengaluru-2026.html instead. That page is live and lists all seven tracks under the H2 "Key AI Topics and Tracks" (Exa fetch, 1 Oct 2026).
  One-time dev step: add id="tracks" to that H2:
  <h2 id="tracks">Key AI Topics and Tracks</h2>
  Until that is done, "#tracks" links still open the right page, just at the top.
- The old track list also appears in "Inside the Boardroom" (WAIS copy and cio 76373) and in the closing paragraph of "Beyond the Hype". Both are fixed below.
- "The Next Chapter of AI" has an H2 that says "World AI Summit 2025". It is fixed below.
- Delegate figure: use 1,000+. That matches /ai-conference-bengaluru-2026.html and Elets CIO's 30 Sep 2026 article "7 AI Questions India Needs to Answer Next" (cio.eletsonline.com/article/7-ai-questions-india-needs-to-answer-next/76379/). The "1,200+" in Beyond the Hype is the odd one out.

=====================================================================
1. "BEYOND THE HYPE" (WAIS copy and cio.eletsonline.com 76367)
=====================================================================
WAIS:  https://www.worldaisummit.com/blog/beyond-the-hype-the-room-where-ais-next-chapter-takes-shape.html
Elets: https://cio.eletsonline.com/article/beyond-the-hype-the-room-where-ais-next-chapter-takes-shape/76367/

1a. Under H2 "Tracks Mapping the AI Landscape", REPLACE this paragraph:
"The World AI Summit 2026 reflects this changing landscape through seven thematic tracks: Generative AI & LLMs, AI Agents and Agentic AI, AI Infrastructure & Cloud, AI in Enterprises, AI in Government & Public Services, Global Capability Centers (GCCs) and AI Ethics & Regulation."

WITH (WAIS copy, relative link):
<p>World AI Summit 2026 is organised around seven tracks: Frontier Models &amp; Compute; Sovereign AI &amp; Geopolitics; Enterprise AI in Production; Global Capability Centres (GCCs); Robotics, Agents &amp; Embodied AI; AI for Bharat; and Capital, Founders &amp; Exits. <a href="/ai-conference-bengaluru-2026.html#tracks">See what each track covers</a>.</p>

WITH (Elets copy, absolute link):
<p>World AI Summit 2026 is organised around seven tracks: Frontier Models &amp; Compute; Sovereign AI &amp; Geopolitics; Enterprise AI in Production; Global Capability Centres (GCCs); Robotics, Agents &amp; Embodied AI; AI for Bharat; and Capital, Founders &amp; Exits. <a href="https://www.worldaisummit.com/ai-conference-bengaluru-2026.html#tracks">See what each track covers</a>.</p>

1b. Under H2 "One Summit, Multiple Perspectives", REPLACE this sentence:
"The summit is expected to bring together 1,200+ delegates, 100+ speakers and 50+ startups,"
WITH:
"The summit is expected to bring together 1,000+ delegates, 100+ speakers and 50+ startups,"
(Leave the rest of the sentence as it is.)

1c. Under H2 "Where the Next AI Conversation Begins", REPLACE this paragraph:
"On 14–15 October 2026, the World AI Summit 2026 will bring this wider AI ecosystem together at the Sheraton Grand Bangalore Hotel at Brigade Gateway in Bengaluru. With its focus on generative AI and LLMs, agentic AI, infrastructure, enterprise adoption, government services and responsible AI, the summit aims to create a space where ideas can move beyond discussion and towards collaboration, innovation and implementation."

WITH (WAIS copy):
<p>On 14–15 October 2026, World AI Summit 2026 will bring this wider AI ecosystem together at the Sheraton Grand Bangalore Hotel at Brigade Gateway in Bengaluru. Its seven tracks run from frontier models and sovereign AI to enterprise AI in production, GCCs, robotics and agents, AI for Bharat, and capital for founders. The aim is a space where ideas can move beyond discussion towards collaboration, innovation and implementation.</p>

WITH (Elets copy): same text.

=====================================================================
2. "INSIDE THE BOARDROOM" (WAIS copy and cio.eletsonline.com 76373)
=====================================================================
WAIS:  https://www.worldaisummit.com/blog/inside-the-boardroom-how-ceos-are-reimagining-business-with-ai.html
Elets: https://cio.eletsonline.com/article/inside-the-boardroom-how-ceos-are-reimagining-business-with-ai/76373/

Under the H2 "The Boardroom Has Changed, and the AI Conversation Has Changed With It", REPLACE the paragraph that starts "This conversation will continue to move higher up the corporate agenda" with the following.

WAIS copy:
<p>This conversation will continue to move higher up the corporate agenda: how CEOs can build organisations that are AI-ready, productive, innovative, responsible and resilient. It will also take centre stage at World AI Summit 2026, on 14–15 October 2026 in Bengaluru. The summit brings together enterprise leaders, policymakers, AI innovators, startups, researchers and investors across <a href="/ai-conference-bengaluru-2026.html#tracks">seven tracks</a>: Frontier Models &amp; Compute; Sovereign AI &amp; Geopolitics; Enterprise AI in Production; Global Capability Centres (GCCs); Robotics, Agents &amp; Embodied AI; AI for Bharat; and Capital, Founders &amp; Exits. It will offer a platform for the partnerships and ideas that will shape the next chapter of AI in India and the future of enterprise AI.</p>

Elets copy: same text, with the link changed to href="https://www.worldaisummit.com/ai-conference-bengaluru-2026.html#tracks".

=====================================================================
3. "THE NEXT CHAPTER OF AI" (WAIS copy; check the egov copy for the same text)
=====================================================================
WAIS:  https://www.worldaisummit.com/blog/the-next-chapter-of-ai-what-will-define-2026-and-beyond.html
Elets: https://egov.eletsonline.com/2026/07/the-next-chapter-of-ai-what-will-define-2026-and-beyond/

3a. REPLACE the H2:
"Why Bengaluru Is the Right Place for This Conversation at World AI Summit 2025"
WITH:
<h2>Why Bengaluru Is the Right Place for World AI Summit 2026</h2>

3b. REPLACE the quote attribution:
"— Sharad Agarwal, Chief Sales Officer, EDAS at World AI Summit 2025"
WITH:
"— Sharad Agarwal, Chief Sales Officer, EDAS, on World AI Summit 2025 (previous edition)"
(The quote is about the earlier edition. The new wording says so plainly, so it no longer reads as a date error.)

3c. Optional, for consistency. Under H2 "Why Global AI Conversations Matter More Than Ever", REPLACE the paragraph that starts "The summit will explore some of the most significant themes driving the AI ecosystem" with:
<p>The summit is organised around seven tracks: Frontier Models &amp; Compute; Sovereign AI &amp; Geopolitics; Enterprise AI in Production; Global Capability Centres (GCCs); Robotics, Agents &amp; Embodied AI; AI for Bharat; and Capital, Founders &amp; Exits. More importantly, it will focus on how these innovations can move beyond research and create meaningful impact across governments, industries and communities. <a href="/ai-conference-bengaluru-2026.html#tracks">See what each track covers</a>.</p>

=====================================================================
4. VISIBLE BYLINE AND DATE (each WAIS post, directly under the H1)
=====================================================================
Beyond the Hype:
<p class="post-meta">By Elets News Network · Published <time datetime="2026-09-28">28 September 2026</time> · Updated <time datetime="2026-10-02">2 October 2026</time></p>
<p class="post-source">First published on <a href="https://cio.eletsonline.com/article/beyond-the-hype-the-room-where-ais-next-chapter-takes-shape/76367/">Elets CIO</a> on 22 September 2026.</p>

Inside the Boardroom:
<p class="post-meta">By Elets News Network · Published <time datetime="2026-09-28">28 September 2026</time> · Updated <time datetime="2026-10-02">2 October 2026</time></p>
<p class="post-source">First published on <a href="https://cio.eletsonline.com/article/inside-the-boardroom-how-ceos-are-reimagining-business-with-ai/76373/">Elets CIO</a> on 24 September 2026.</p>

AI in India:
<p class="post-meta">By Elets News Network · Published <time datetime="2026-09-28">28 September 2026</time> · Updated <time datetime="2026-10-02">2 October 2026</time></p>
<p class="post-source">First published on <a href="https://cio.eletsonline.com/article/ai-in-india-from-digital-public-infrastructure-to-global-leadership/76296/">Elets CIO</a> on 1 August 2026.</p>

The Next Chapter of AI:
<p class="post-meta">By Elets News Network · Published <time datetime="2026-09-28">28 September 2026</time> · Updated <time datetime="2026-10-02">2 October 2026</time></p>
<p class="post-source">First published on <a href="https://egov.eletsonline.com/2026/07/the-next-chapter-of-ai-what-will-define-2026-and-beyond/">Elets eGov</a> on 25 July 2026.</p>

The Skills That Will Matter Most (no Elets copy found):
<p class="post-meta">By PLACEHOLDER_SKILLS_BYLINE · Published <time datetime="2026-09-28">28 September 2026</time></p>

/blog/ index: add one line under each card's H2, using the same date and byline as the post:
<p class="post-meta">Elets News Network · <time datetime="2026-09-28">28 September 2026</time></p>
(For the Skills card, use PLACEHOLDER_SKILLS_BYLINE.)

=====================================================================
5. IN-BODY CALL TO ACTION (each WAIS post, as the last paragraph before the contact e-mails)
=====================================================================
<p>World AI Summit 2026 takes place on 14–15 October 2026 at the Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. <a href="/delegate/">Book your delegate pass</a> (groups of three or more get 10% off), <a href="/ai-conference-bengaluru-2026.html#tracks">explore the seven tracks</a> or <a href="/awards/">nominate for the World AI Awards 2026</a>.</p>

=====================================================================
6. ARTICLE JSON-LD (WAIS copies, in <head>; one block per post; tested as valid JSON)
=====================================================================
Beyond the Hype:
<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","@id":"https://www.worldaisummit.com/blog/beyond-the-hype-the-room-where-ais-next-chapter-takes-shape.html#article","mainEntityOfPage":{"@type":"WebPage","@id":"https://www.worldaisummit.com/blog/beyond-the-hype-the-room-where-ais-next-chapter-takes-shape.html"},"url":"https://www.worldaisummit.com/blog/beyond-the-hype-the-room-where-ais-next-chapter-takes-shape.html","headline":"Beyond the Hype: The Room Where AI’s Next Chapter Takes Shape","description":"How World AI Summit 2026 brings policymakers, enterprises, startups, investors and researchers together in Bengaluru on 14–15 October 2026.","inLanguage":"en-IN","datePublished":"2026-09-28","dateModified":"2026-10-02","author":{"@type":"Organization","name":"Elets News Network"},"publisher":{"@type":"Organization","name":"World AI Summit","url":"https://www.worldaisummit.com/","parentOrganization":{"@type":"Organization","name":"Elets Technomedia"}},"isPartOf":{"@type":"Blog","@id":"https://www.worldaisummit.com/blog/","name":"World AI Summit Blog"},"isBasedOn":"https://cio.eletsonline.com/article/beyond-the-hype-the-room-where-ais-next-chapter-takes-shape/76367/"}</script>

Inside the Boardroom:
<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","@id":"https://www.worldaisummit.com/blog/inside-the-boardroom-how-ceos-are-reimagining-business-with-ai.html#article","mainEntityOfPage":{"@type":"WebPage","@id":"https://www.worldaisummit.com/blog/inside-the-boardroom-how-ceos-are-reimagining-business-with-ai.html"},"url":"https://www.worldaisummit.com/blog/inside-the-boardroom-how-ceos-are-reimagining-business-with-ai.html","headline":"Inside the Boardroom: How CEOs Are Reimagining Business with AI","description":"How CEOs are moving from AI pilots to enterprise transformation, and what that means for governance, productivity and agentic AI.","inLanguage":"en-IN","datePublished":"2026-09-28","dateModified":"2026-10-02","author":{"@type":"Organization","name":"Elets News Network"},"publisher":{"@type":"Organization","name":"World AI Summit","url":"https://www.worldaisummit.com/","parentOrganization":{"@type":"Organization","name":"Elets Technomedia"}},"isPartOf":{"@type":"Blog","@id":"https://www.worldaisummit.com/blog/","name":"World AI Summit Blog"},"isBasedOn":"https://cio.eletsonline.com/article/inside-the-boardroom-how-ceos-are-reimagining-business-with-ai/76373/"}</script>

AI in India:
<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","@id":"https://www.worldaisummit.com/blog/ai-in-india-from-digital-public-infrastructure-to-global-leadership.html#article","mainEntityOfPage":{"@type":"WebPage","@id":"https://www.worldaisummit.com/blog/ai-in-india-from-digital-public-infrastructure-to-global-leadership.html"},"url":"https://www.worldaisummit.com/blog/ai-in-india-from-digital-public-infrastructure-to-global-leadership.html","headline":"AI in India: From Digital Public Infrastructure to Global Leadership","description":"How India's digital public infrastructure is shaping its path to global AI leadership.","inLanguage":"en-IN","datePublished":"2026-09-28","dateModified":"2026-10-02","author":{"@type":"Organization","name":"Elets News Network"},"publisher":{"@type":"Organization","name":"World AI Summit","url":"https://www.worldaisummit.com/","parentOrganization":{"@type":"Organization","name":"Elets Technomedia"}},"isPartOf":{"@type":"Blog","@id":"https://www.worldaisummit.com/blog/","name":"World AI Summit Blog"},"isBasedOn":"https://cio.eletsonline.com/article/ai-in-india-from-digital-public-infrastructure-to-global-leadership/76296/"}</script>

The Next Chapter of AI:
<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","@id":"https://www.worldaisummit.com/blog/the-next-chapter-of-ai-what-will-define-2026-and-beyond.html#article","mainEntityOfPage":{"@type":"WebPage","@id":"https://www.worldaisummit.com/blog/the-next-chapter-of-ai-what-will-define-2026-and-beyond.html"},"url":"https://www.worldaisummit.com/blog/the-next-chapter-of-ai-what-will-define-2026-and-beyond.html","headline":"The Next Chapter of AI: What Will Define 2026 and Beyond?","description":"AI ecosystems, sovereign AI, responsible innovation and talent: the shifts that will define AI in 2026 and beyond.","inLanguage":"en-IN","datePublished":"2026-09-28","dateModified":"2026-10-02","author":{"@type":"Organization","name":"Elets News Network"},"publisher":{"@type":"Organization","name":"World AI Summit","url":"https://www.worldaisummit.com/","parentOrganization":{"@type":"Organization","name":"Elets Technomedia"}},"isPartOf":{"@type":"Blog","@id":"https://www.worldaisummit.com/blog/","name":"World AI Summit Blog"},"isBasedOn":"https://egov.eletsonline.com/2026/07/the-next-chapter-of-ai-what-will-define-2026-and-beyond/"}</script>

The Skills That Will Matter Most:
<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","@id":"https://www.worldaisummit.com/blog/the-skills-that-will-matter-most-in-an-ai-driven-world.html#article","mainEntityOfPage":{"@type":"WebPage","@id":"https://www.worldaisummit.com/blog/the-skills-that-will-matter-most-in-an-ai-driven-world.html"},"url":"https://www.worldaisummit.com/blog/the-skills-that-will-matter-most-in-an-ai-driven-world.html","headline":"The Skills That Will Matter Most in an AI-Driven World","description":"The skills that will matter most as artificial intelligence reshapes industries and careers.","inLanguage":"en-IN","datePublished":"2026-09-28","dateModified":"2026-10-02","author":{"@type":"Organization","name":"PLACEHOLDER_SKILLS_BYLINE"},"publisher":{"@type":"Organization","name":"World AI Summit","url":"https://www.worldaisummit.com/","parentOrganization":{"@type":"Organization","name":"Elets Technomedia"}},"isPartOf":{"@type":"Blog","@id":"https://www.worldaisummit.com/blog/","name":"World AI Summit Blog"}}</script>

=====================================================================
7. CANONICAL TAGS (choose ONE direction per pair: PLACEHOLDER_CANONICAL_DIRECTION)
=====================================================================
OPTION A (preferred; needs Elets editorial sign-off). Put the tag in the <head> of the ELETS copy. On WordPress with Yoast (egov.eletsonline.com uses Yoast), enter the URL in the post's Yoast "Advanced > Canonical URL" field instead of hand-editing. The WAIS copies keep their self-referencing canonical.

On cio 76367:
<link rel="canonical" href="https://www.worldaisummit.com/blog/beyond-the-hype-the-room-where-ais-next-chapter-takes-shape.html">
On cio 76373:
<link rel="canonical" href="https://www.worldaisummit.com/blog/inside-the-boardroom-how-ceos-are-reimagining-business-with-ai.html">
On cio 76296:
<link rel="canonical" href="https://www.worldaisummit.com/blog/ai-in-india-from-digital-public-infrastructure-to-global-leadership.html">
On egov 2026/07/the-next-chapter-of-ai...:
<link rel="canonical" href="https://www.worldaisummit.com/blog/the-next-chapter-of-ai-what-will-define-2026-and-beyond.html">

OPTION B (if Elets editorial declines). REPLACE the existing canonical in the <head> of the WAIS copy. There must be only one canonical per page.

On WAIS beyond-the-hype...html:
<link rel="canonical" href="https://cio.eletsonline.com/article/beyond-the-hype-the-room-where-ais-next-chapter-takes-shape/76367/">
On WAIS inside-the-boardroom...html:
<link rel="canonical" href="https://cio.eletsonline.com/article/inside-the-boardroom-how-ceos-are-reimagining-business-with-ai/76373/">
On WAIS ai-in-india...html:
<link rel="canonical" href="https://cio.eletsonline.com/article/ai-in-india-from-digital-public-infrastructure-to-global-leadership/76296/">
On WAIS the-next-chapter-of-ai...html:
<link rel="canonical" href="https://egov.eletsonline.com/2026/07/the-next-chapter-of-ai-what-will-define-2026-and-beyond/">

The Skills post has no Elets copy. It keeps its self-referencing canonical under either option.
No redirects are needed for this change.

=====================================================================
8. RELATED FIX OUTSIDE THE BLOG (homepage FAQ, more traffic than any post)
=====================================================================
Homepage FAQ, "What topics will be covered?". REPLACE the answer with:
World AI Summit 2026 is organised around seven tracks: Frontier Models & Compute; Sovereign AI & Geopolitics; Enterprise AI in Production; Global Capability Centres (GCCs); Robotics, Agents & Embodied AI; AI for Bharat; and Capital, Founders & Exits. The AI for Bharat track covers governance, healthcare, education, agriculture and public services.
If the homepage has FAQPage JSON-LD, put the same text in that question's acceptedAnswer "text".
