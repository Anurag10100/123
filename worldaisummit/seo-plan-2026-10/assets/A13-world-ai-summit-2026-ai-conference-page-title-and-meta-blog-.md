# A13: World AI Summit 2026: AI-conference page title and meta, blog fact fixes, blog CTA box, speaker links, Event JSON-LD

- **For recommendation:** Fix wrong facts in the blog and AI-conference page and add links from them to /delegate/, /awards/ and speaker pages
- **Research lens:** site-deep-read
- **Format:** HTML snippets with find/replace copy, one block per page (head tags, JSON-LD, CTA aside, paragraph replacements)
- **Placeholders the business must fill:**
  - PLACEHOLDER_CURRENT_PRICE: delegate price shown in the blog CTA box from 1 Oct 2026. Standard Rs 20,000/35,000 expired on 30 Sept; Late Access Rs 30,000/60,000 may now apply. Sales to confirm the figure and the GST wording.
  - PLACEHOLDER_CURRENT_PRICE_NUMBER: numeric INR price for JSON-LD offers.price, for example 30000 if the lowest Late Access tier applies. Sales to confirm.
  - PLACEHOLDER_PRICE_VALID_FROM: ISO date when the current price started, for example 2026-10-01
  - PLACEHOLDER_AWARD_DEADLINE: World AI Awards 2026 nomination closing date. Remove that line if no deadline is confirmed.
  - PLACEHOLDER_DELEGATE_COUNT: one delegate figure for all pages (the AI-conference page says 1,000+; Beyond the Hype says 1,200+)
  - PLACEHOLDER_EVENT_IMAGE_URL: absolute URL of a 16:9 or 1:1 event image on worldaisummit.com, for JSON-LD
  - PLACEHOLDER_SPEAKER_URL_<slug>: live /assets/speaker_details/ profile URL for each of the 15 suggested speakers. Check each speaker is listed on /speaker.html.

## How to ship

Publish by 4 Oct 2026. Most of this is about 2 hours of work for content and web dev, but the prices depend on sales and nothing has been edited in the repo.

Order of work:
1) Sales decides the price that applies from 1 Oct, because Standard Access expired on 30 Sept 2026. That decision fills PLACEHOLDER_CURRENT_PRICE in the CTA box and PLACEHOLDER_CURRENT_PRICE_NUMBER / PLACEHOLDER_PRICE_VALID_FROM in the JSON-LD. Also remove the expired Early Bird and Standard rows from /delegate/, and look again at the 'Passes from Rs 20,000' text in speaker-page metas and the homepage 'Premium Rs 20,000'. Whether those are stale is an inference, not something I confirmed.
2) Content applies sections C and D as find/replace in the two posts. The quoted text matches the live pages as fetched with Exa on 1 Oct 2026.
3) Web dev adds the CTA aside and CSS (section B) to the blog post template so all 5 posts get it, then makes the head-tag change on the AI-conference page (A1). Add the JSON-LD (A3) only if the page has no Event block. If one exists, replace it, then run Google's Rich Results Test.
4) Section E: replace each PLACEHOLDER_SPEAKER_URL_<slug> with the speaker's real live profile URL under /assets/speaker_details/. I could not read the hrefs because the proxy blocks worldaisummit.com, and Exa returns text without links. The /speakers/<slug>/ pages from the local generator are not deployed.
5) A2 (homepage footer link) and F (shorter blog titles) are optional.

No URL changes, so no Apache or nginx redirects are needed.

After publishing, request indexing in Search Console for the AI-conference page and the 5 posts. The Search Console property is non-www only, so it cannot report www blog traffic; add the www property or a Domain property to measure the effect.

Checks before go-live: the one-line track descriptions in C1 are my paraphrases of the track names, so the programme team should compare them with the homepage track copy. Pick a single delegate figure (1,000+ or 1,200+) and use it everywhere. Confirm every linked speaker is listed on /speaker.html.

Sources: venue address from the Marriott hotel overview (https://www.marriott.com/en-us/hotels/blrgs-sheraton-grand-bangalore-hotel-at-brigade-gateway/overview/) and hotelplanner (https://www.hotelplanner.com/Hotels/178731/Reservations-Sheraton-Bangalore-Hotel-at-Brigade-Gateway-Bangalore-26-1-Dr-Rajkumar-Rd-Malleswaram-Rajajinagar-560055). Blog text from Exa fetches on 1 Oct 2026. Speaker names and roles from /home/user/123/worldaisummit/speakers/speakers.json.

About the question that started this run ('do you have more CPUs from computer?'): this step was a single content task, so it had no way to check or change compute resources.

## Content

==================================================================
A. /ai-conference-bengaluru-2026.html  (keep the URL as it is, so no redirect is needed)
==================================================================

A1. <head> tags. Replace the current title 'AI Conference Bengaluru 2026 | World AI Summit'.

<title>AI Conference Bangalore 2026, 14-15 Oct | World AI Summit</title>
<meta name="description" content="AI conference in Bangalore in October 2026? World AI Summit runs 14-15 Oct at Sheraton Grand, Brigade Gateway. 7 tracks, 100+ speakers. Book your pass.">
<meta property="og:title" content="AI Conference Bangalore 2026, 14-15 Oct | World AI Summit">
<meta property="og:description" content="AI conference in Bangalore in October 2026? World AI Summit runs 14-15 Oct at Sheraton Grand, Brigade Gateway. 7 tracks, 100+ speakers. Book your pass.">
<meta name="twitter:title" content="AI Conference Bangalore 2026, 14-15 Oct | World AI Summit">
<meta name="twitter:description" content="AI conference in Bangalore in October 2026? World AI Summit runs 14-15 Oct at Sheraton Grand, Brigade Gateway. 7 tracks, 100+ speakers. Book your pass.">

The title is 57 characters and the meta description is 151.
The verifier found that the proposed '50+ speakers' contradicts the page's own '100+ Speakers' stat and the '100+ speakers' heading on /speaker.html, so the meta now says '100+ speakers'.
Fallback meta if the speaker count is not settled (149 characters):
AI conference in Bangalore in October 2026? World AI Summit runs 14-15 Oct at Sheraton Grand, Brigade Gateway. Seven tracks. Book your delegate pass.

Do NOT add a 'Who is speaking' line. The page already has 'Featured AI Speakers' with 12 'View Profile' links and a '100+ speakers' line.

A2. Optional homepage footer link (one link, footer or venue block only, never the hero, so the homepage stays the main page for 'ai conference bangalore 2026'):

<a href="/ai-conference-bengaluru-2026.html">AI conference in Bangalore, October 2026</a>

The audit's null crawl depth does not prove this page is orphaned, because nearly every page in that crawl has null depth. Treat this link as cheap insurance, not as a fix for a proven problem.

A3. Event JSON-LD. Add it only if the page has no Event block. If one exists, replace it so the page has only one. Fill in every PLACEHOLDER_ before publishing, then test with Google's Rich Results Test.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Event",
  "name": "World AI Summit 2026",
  "description": "World AI Summit 2026 is an AI conference in Bengaluru on 14-15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, organised by Elets Technomedia. Seven tracks: Frontier Models & Compute; Sovereign AI & Geopolitics; Enterprise AI in Production; GCCs; Robotics, Agents & Embodied AI; AI for Bharat; Capital, Founders & Exits.",
  "url": "https://www.worldaisummit.com/ai-conference-bengaluru-2026.html",
  "image": ["PLACEHOLDER_EVENT_IMAGE_URL"],
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
    "price": "PLACEHOLDER_CURRENT_PRICE_NUMBER",
    "priceCurrency": "INR",
    "availability": "https://schema.org/InStock",
    "validFrom": "PLACEHOLDER_PRICE_VALID_FROM"
  },
  "performer": [
    {"@type": "Person", "name": "Pankaj Kumar Pandey", "jobTitle": "Principal Secretary, e-Governance", "affiliation": {"@type": "Organization", "name": "Government of Karnataka"}},
    {"@type": "Person", "name": "Sanjeev Gupta", "jobTitle": "CEO", "affiliation": {"@type": "Organization", "name": "Karnataka Digital Economy Mission"}},
    {"@type": "Person", "name": "Shalini Kapoor", "jobTitle": "Chief Strategist, Data and AI", "affiliation": {"@type": "Organization", "name": "EkStep Foundation"}}
  ]
}
</script>

Venue address source: Marriott hotel page and hotelplanner listing, found by web search on 1 Oct 2026 (26/1 Dr. Rajkumar Road, Malleswaram-Rajajinagar, 560055). The three performers are marked confirmed_2026 in worldaisummit/speakers/speakers.json. Before publishing, check that each one is listed on /speaker.html.

==================================================================
B. Blog CTA box: add to the end of all 5 posts, just above the three email addresses
==================================================================

<aside class="wais-cta" aria-label="World AI Summit 2026">
  <p class="wais-cta__title"><strong>World AI Summit 2026</strong></p>
  <p>14-15 October 2026 · Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru</p>
  <p>Delegate passes: PLACEHOLDER_CURRENT_PRICE</p>
  <p>World AI Awards 2026 nominations close PLACEHOLDER_AWARD_DEADLINE.</p>
  <p class="wais-cta__actions">
    <a class="wais-cta__btn" href="/delegate/">Book delegate pass</a>
    <a class="wais-cta__btn wais-cta__btn--alt" href="/awards/">Nominate for World AI Awards 2026</a>
  </p>
</aside>

<style>
.wais-cta{border:1px solid #d0d7e2;border-radius:8px;padding:20px;margin:32px 0;background:#f6f8fb}
.wais-cta p{margin:0 0 8px}
.wais-cta__title{font-size:1.15em}
.wais-cta__actions{display:flex;flex-wrap:wrap;gap:12px;margin-top:12px}
.wais-cta__btn{display:inline-block;padding:10px 18px;border-radius:6px;background:#1a3c8f;color:#fff;text-decoration:none}
.wais-cta__btn--alt{background:#fff;color:#1a3c8f;border:1px solid #1a3c8f}
</style>

Plain-text version for the CMS:
World AI Summit 2026 · 14-15 October 2026 · Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru · Delegate passes: PLACEHOLDER_CURRENT_PRICE · World AI Awards 2026 nominations close PLACEHOLDER_AWARD_DEADLINE · [Book delegate pass -> /delegate/] [Nominate for World AI Awards 2026 -> /awards/]

If sales has not decided on a price by 4 Oct, use 'Delegate passes: see current prices' and keep the button. Do not show the Standard Access price, which expired on 30 Sept 2026. If there is no confirmed award deadline, remove that line.

==================================================================
C. 'Beyond the Hype'  /blog/beyond-the-hype-the-room-where-ais-next-chapter-takes-shape.html
==================================================================

C1. Section 'Tracks Mapping the AI Landscape'. Replace the paragraph that starts 'The World AI Summit 2026 reflects this changing landscape through seven thematic tracks: Generative AI & LLMs...'. Also replace the five paragraphs after 'Together, these tracks offer a picture...', from 'Generative AI and LLMs remain at the heart...' through '...depend upon AI systems.' Use this:

The World AI Summit 2026 reflects this changing landscape through seven tracks: Frontier Models & Compute; Sovereign AI & Geopolitics; Enterprise AI in Production; GCCs; Robotics, Agents & Embodied AI; AI for Bharat; and Capital, Founders & Exits.

Together, these tracks offer a picture of where the AI conversation is heading.

Frontier Models & Compute looks at the models themselves and the computing capacity they depend on. Sovereign AI & Geopolitics turns to the national side of the question: who builds, owns and governs AI capability. Enterprise AI in Production is about AI that has moved past the pilot stage and into day-to-day operations.

The GCCs track looks at Global Capability Centres, which many global companies now rely on to build and run AI, and Bengaluru is home to many of them. Robotics, Agents & Embodied AI covers systems that act, not only answer. AI for Bharat asks how AI can work across India's languages, sectors and levels of digital access. Capital, Founders & Exits follows the companies and the money behind them, from first funding to scale.

Running across all of these is the question of trust. Responsible development, transparency, safety, privacy and accountability will shape whether people are willing to adopt and depend upon AI systems.

C2. Section 'One Summit, Multiple Perspectives'. Find: '1,200+ delegates, 100+ speakers and 50+ startups'
Replace with: 'PLACEHOLDER_DELEGATE_COUNT delegates, 100+ speakers and 50+ startups'
(The AI-conference page says 1,000+ delegates. Choose one figure and use it on every page.)

C3. Section 'Recognising AI That Creates Real Impact'. Find: 'The World AI Awards 2026 will bring this focus'
Replace with: 'The <a href="/awards/">World AI Awards 2026</a> will bring this focus'

C4. Section 'Where the Next AI Conversation Begins'. Replace the paragraph that starts 'On 14–15 October 2026, the World AI Summit 2026 will bring...', which lists themes that are not the official tracks, with:

On 14-15 October 2026, the World AI Summit 2026 will bring this wider AI ecosystem together at the Sheraton Grand Bangalore Hotel at Brigade Gateway in Bengaluru. Across its seven tracks, from Frontier Models & Compute and Sovereign AI & Geopolitics to AI for Bharat and Capital, Founders & Exits, the summit aims to create a space where ideas can move beyond discussion and towards collaboration, innovation and implementation. Passes are available on the <a href="/delegate/">World AI Summit 2026 delegate page</a>.

==================================================================
D. 'The Next Chapter of AI'  /blog/the-next-chapter-of-ai-what-will-define-2026-and-beyond.html
==================================================================

D1. H2. Find: 'Why Bengaluru Is the Right Place for This Conversation at World AI Summit 2025'
Replace with: 'Why Bengaluru Is the Right Place for This Conversation at World AI Summit 2026'
(Keep the testimonial attribution 'Sharad Agarwal ... at World AI Summit 2025' as it is. It correctly credits a quote from the 2025 edition.)

D2. Find: 'One such platform is the World AI Summit 2026, which will take place on 14–15 October 2026 in Bengaluru.'
Replace with: 'One such platform is the <a href="/ai-conference-bengaluru-2026.html">World AI Summit 2026, which will take place on 14-15 October 2026 in Bengaluru</a>.'

D3. Replace the paragraph that starts 'The summit will explore some of the most significant themes driving the AI ecosystem, including Generative AI, Agentic AI...' with:

The summit's programme is built around seven tracks: Frontier Models & Compute; Sovereign AI & Geopolitics; Enterprise AI in Production; GCCs; Robotics, Agents & Embodied AI; AI for Bharat; and Capital, Founders & Exits. More importantly, it will focus on how these ideas can move beyond research and create meaningful impact across governments, industries and communities.

==================================================================
E. In-text speaker links, 2-3 per post
==================================================================

Pattern (use only the name, role and organisation, and do not add bio claims):
Among the speakers at World AI Summit 2026 is <a href="PLACEHOLDER_SPEAKER_URL_sanjeev-gupta">Sanjeev Gupta</a>, CEO, Karnataka Digital Economy Mission.

Suggested pairings. Every name is marked confirmed_2026 in speakers.json. Check each one on /speaker.html before linking.
- Beyond the Hype: Sanjeev Gupta, CEO, Karnataka Digital Economy Mission (Bengaluru section); Shashank Randev, Founder and General Partner, 247VC, and Sandhya Vasudevan, Board Member, TiE Bangalore (startups section)
- The Next Chapter of AI: Pankaj Kumar Pandey, Principal Secretary, e-Governance, Government of Karnataka (Sovereign AI section); Hemant Garg, Deputy Director, Ministry of Labour and Employment (talent section)
- Inside the Boardroom: Sandeep Varaganti, CEO, JioMart, Reliance Retail; George Inasu, MD and Country Head, Fidelity National Financial India; Anand Ramakrishnan, Managing Director, Equiniti India
- The Skills That Will Matter Most: M. Balasubramaniam, Chairman, Southern Regional Committee, AICTE; Pavankumar Gurazada, Associate Director, Great Learning
- AI in India (DPI): Shalini Kapoor, Chief Strategist, Data and AI, EkStep Foundation; T Bhoobalan, CEO, Centre for e-Governance, Karnataka; Ram Mohan Rao, Executive Director, SEBI

==================================================================
F. Optional: blog <title> tags
==================================================================
Remove ' | World AI Summit 2026' from the <title> of all 5 posts, which are currently 80-91 characters. Keep each H1 unchanged.
Example: <title>Beyond the Hype: The Room Where AI's Next Chapter Takes Shape</title>
