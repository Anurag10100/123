# A42: Partner kit "Meet us at World AI Summit 2026" (8 partners, corrected) and crawlable homepage partner block

- **For recommendation:** Partner and exhibitor 'Meet us at World AI Summit 2026' kit, plus a crawlable 2026 partner list on the homepage
- **Research lens:** speakers-partners
- **Format:** Plain-text kit for partners (cover email, website snippet with an HTML version, LinkedIn post with per-partner UTM links), an HTML fragment for the homepage, and an internal send gate and partner table. Lines marked INTERNAL are for Elets only. Remove them before sending.
- **Placeholders the business must fill:**
  - PLACEHOLDER_CURRENT_PASS_PRICE: the one current delegate price that /delegate/ and the homepage must both show before the kit is sent
  - PLACEHOLDER_BOOTH_NO and PLACEHOLDER_BOOTH_WD / _HIGHTABLE / _SUCCESSIVE / _KAGEN / _RWS / _EXATRON / _INDIEROUTER: booth numbers Elets assigns
  - PLACEHOLDER_CONFIRM_KDEM_2026_TIER: confirm KDEM is the 2026 Strategic Partner (confirmed for 2025; 2026 is from the syndicated listing only)
  - PLACEHOLDER_KDEM_PAID: if KDEM's slot is paid, add rel=sponsored to its homepage link
  - PLACEHOLDER_GUEST_PASS_CODE and PLACEHOLDER_GUEST_PASS_COUNT: whether partner packages include customer guest passes (Elets commercial decision)
  - PLACEHOLDER_PUBLISH_BY: the date partners are asked to publish by (suggested 8 Oct)
  - PLACEHOLDER_SENDER_NAME: who in partnerships signs the email
  - PLACEHOLDER_LATER_SIGNINGS: partners signed after 1 Oct, added only after partnerships confirms them
  - PLACEHOLDER_BOOTHS_LEFT: booths still available, for the 5-9 Oct push to exhibitor prospects
  - {Company}, {First name}, {tier}, {one line}: wording the partner or the email sender fills in per partner (not business decisions)

## How to ship

The relayed request ("do you have more CPUs from computer?") is about compute, not this kit. I have no information on CPU capacity, so the orchestrator should answer that separately.

How to ship the kit:

1. Web dev, by 3-4 Oct, before anything else:
   - Fix /delegate/ so it shows one current price that matches the homepage.
   - Remove the expired Standard and Early Bird tiers and add an H1.
   - This is the send gate. Until it is done, the kit's links would send partner traffic to contradictory prices.

2. Web dev, by 4 Oct: replace the logo-only partner area on the homepage with the section 4 HTML.
   - Keep the existing logos, add the alt text, and fill the empty "AI & Data Infrastructure Partner" heading with WD.
   - Load each partner URL once and use the address it lands on, with no redirect.
   - Check that the names appear in the page source, not only in images.

3. Partnerships, by 4 Oct, settle the business placeholders:
   - booth numbers
   - KDEM's 2026 tier, and whether its slot is paid
   - whether packages include guest passes, and the codes
   - booths left
   - the publish-by date
   - the sender's name
   - any later signings
   Do not use the extra names in HIGHTABLE's post or the "1,000+ delegates" figure.

4. Partnerships, on 5 Oct, once the gate is cleared:
   - Send one email per partner (section 1), with sections 2 and 3 pasted below it.
   - Use only that partner's tracking link and tier wording.
   - For WD and RWS, lead with LinkedIn. For HIGHTABLE, ask for a website page and a comment with the tracking link on their existing post. For KDEM, send the no-booth version.
   - If /delegate/ is still not fixed on 5 Oct, swap every /delegate/ link to https://www.worldaisummit.com/ first.

5. Sales, 5-9 Oct: use section 5 in outreach to exhibitor prospects.

6. Tracking:
   - Watch GA4 for utm_campaign=world_ai_summit_2026 by utm_source, plus referrals from the 8 partner domains.
   - Log each partner page URL as it goes live.
   - Re-check backlinks to /delegate/ and the homepage about 14 days after sending.

Copy rules: Indian English, no exclamation marks, no prices or attendance figures in the partner copy.

## Content

=====================================================================
INTERNAL: SEND GATE (hard blocker, not a caveat)
=====================================================================
Do not send this kit until https://www.worldaisummit.com/delegate/ shows one current price. Until then, do not ask partners to publish anything.

What /delegate/ shows today (1 Oct 2026):
- "Standard Access (Valid till 30th Sept 2026)", which expired yesterday
- Early Bird "till 25th July 2025"
- Late Access at Rs 30,000 / Rs 60,000

The homepage still says Premium Rs 20,000. Web dev must set one current price on both pages and add an H1 to /delegate/. The price is PLACEHOLDER_CURRENT_PASS_PRICE.

Fallback: if /delegate/ is not fixed by 5 Oct, replace every https://www.worldaisummit.com/delegate/ in this kit with https://www.worldaisummit.com/ before sending. Partner pages are rarely edited once they go live, so /delegate/ is the better long-term link if it is fixed in time.

=====================================================================
INTERNAL: 2026 PARTNER LIST (8, not 6)
=====================================================================
Partner | Tier as announced | Website | UTM slug | Booth | Public source
- Karnataka Digital Economy Mission (KDEM) | Strategic Partner | https://karnatakadigital.in/ | kdem | none | Named in the syndicated allevents/happeningnext listing. KDEM was also the 2025 Strategic Partner. PLACEHOLDER_CONFIRM_KDEM_2026_TIER
- WD (Western Digital) | AI & Data Infrastructure Partner | https://www.westerndigital.com/ | westerndigital | PLACEHOLDER_BOOTH_WD | World AI Summit LinkedIn, 18 Aug 2026
- HIGHTABLE | AI Impact Partner | https://thehightable.world/ | hightable | PLACEHOLDER_BOOTH_HIGHTABLE | HIGHTABLE's own LinkedIn post, 24 Sep 2026
- Successive Digital | Bronze Partner | https://successive.tech/ | successive | PLACEHOLDER_BOOTH_SUCCESSIVE | World AI Summit LinkedIn, 10 Aug 2026
- Kagen.ai | Bronze Partner | https://kagen.ai/ | kagen | PLACEHOLDER_BOOTH_KAGEN | World AI Summit LinkedIn, 10 Aug 2026
- RWS | Exhibitor | https://www.rws.com/ | rws | PLACEHOLDER_BOOTH_RWS | World AI Summit LinkedIn, 5 Aug 2026
- Exatron | Exhibitor | https://exatron.in/ | exatron | PLACEHOLDER_BOOTH_EXATRON | World AI Summit LinkedIn, 17 Aug 2026
- IndieRouter.ai | Exhibitor | https://indierouter.ai/ | indierouter | PLACEHOLDER_BOOTH_INDIEROUTER | World AI Summit LinkedIn, 18 Sep 2026

How the domains were checked:
- kagen.ai, westerndigital.com and rws.com were confirmed earlier (each has its own events pages).
- successive.tech, exatron.in, thehightable.world, karnatakadigital.in and indierouter.ai were confirmed on 1 Oct 2026 via Exa, from each company's own homepage and the "Homepage" field on its LinkedIn company page.
- Web dev: before publishing, load each URL once and use the final address it lands on, with no redirect.

Do not name these publicly:
- MITRA, Croma, Adani Group, JPMorganChase, Bajaj General Insurance, Apollo Tyres, Wells Fargo, Equiniti India, FNF and Reliance Retail. HIGHTABLE's post lists them as "World AI summit Partners", but that is not verified; they may be past partners or companies that speakers work for. Add a name only after partnerships confirms it: PLACEHOLDER_LATER_SIGNINGS.
- The "1,000+ delegates, 100+ speakers, 50+ startups" line from the syndicated listing. It is not verified, so do not reuse it here.

Notes for individual partners:
- HIGHTABLE has already posted on LinkedIn (24 Sep). Ask for a website page and a follow-up post or comment with their tracking link, not a fresh announcement.
- WD and RWS put web pages through brand approval, and so far their event pages cover larger shows. Lead with the LinkedIn post and offer the website snippet as optional.
- KDEM is a government body. Offer the no-booth version of the snippet for a news or events listing.

=====================================================================
1. COVER EMAIL (from partnerships@worldaisummit.com, one per partner)
=====================================================================
Subject: World AI Summit 2026: your booth details and a short "meet us" kit

Dear {First name},

Thank you for joining World AI Summit 2026 as {tier, e.g. a Bronze Partner}. The summit takes place on 14-15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru.

Your booth: PLACEHOLDER_BOOTH_NO
Guest passes for your customers: PLACEHOLDER_GUEST_PASS_CODE (PLACEHOLDER_GUEST_PASS_COUNT passes). [Delete this line if the package does not include guest passes.]

To help your customers and prospects find you at the summit, we have drafted three short pieces below:
1. A "Meet us at World AI Summit 2026" note for your website's events, news or blog page
2. A LinkedIn post with a tracking link set up for {Company}
3. A suggested line for your customer invitations

Please edit the wording freely. We ask only that the registration links stay exactly as given. If you can publish by PLACEHOLDER_PUBLISH_BY (suggested 8 October), it will be live for the last week before the summit. Please send us the link once it is up.

Regards,
PLACEHOLDER_SENDER_NAME
Partnerships, World AI Summit 2026 | Elets Technomedia
partnerships@worldaisummit.com

=====================================================================
2. WEBSITE SNIPPET (for the partner's events, news or blog page)
=====================================================================
Meet {Company} at World AI Summit 2026
14-15 October 2026 | Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru | Booth PLACEHOLDER_BOOTH_NO

{Company} is {the AI & Data Infrastructure Partner / the AI Impact Partner / a Bronze Partner / an exhibitor} at World AI Summit 2026, organised by Elets Technomedia in Bengaluru on 14-15 October. The programme runs across seven tracks: Frontier Models & Compute; Sovereign AI & Geopolitics; Enterprise AI in Production; GCCs; Robotics, Agents & Embodied AI; AI for Bharat; and Capital, Founders & Exits. Visit us at booth PLACEHOLDER_BOOTH_NO to {one line on what visitors will see or discuss}.

Register for a delegate pass: https://www.worldaisummit.com/delegate/

Version without a booth (KDEM, or any partner without a stand): drop "| Booth PLACEHOLDER_BOOTH_NO" from the date line, use "the Strategic Partner" as the tier where it applies, and replace the last sentence with:
"Our team will be at the summit to {one line, e.g. who will attend and what they will discuss}."

HTML version, ready to paste:
<section class="event-listing">
  <h2>Meet {Company} at World AI Summit 2026</h2>
  <p><strong>14-15 October 2026</strong> | Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru | Booth PLACEHOLDER_BOOTH_NO</p>
  <p>{Company} is {tier} at World AI Summit 2026, organised by Elets Technomedia in Bengaluru on 14-15 October. The programme runs across seven tracks: Frontier Models &amp; Compute; Sovereign AI &amp; Geopolitics; Enterprise AI in Production; GCCs; Robotics, Agents &amp; Embodied AI; AI for Bharat; and Capital, Founders &amp; Exits. Visit us at booth PLACEHOLDER_BOOTH_NO to {one line}.</p>
  <p><a href="https://www.worldaisummit.com/delegate/">Register for World AI Summit 2026</a></p>
</section>

=====================================================================
3. LINKEDIN POST
=====================================================================
We're at World AI Summit 2026 in Bengaluru on 14-15 October, at booth PLACEHOLDER_BOOTH_NO, Sheraton Grand Bangalore Hotel at Brigade Gateway. Come and see {one line}.

Delegate passes: {partner tracking link from the list below}

@World AI Summit #WorldAISummit2026

(Type "@World AI Summit" in the LinkedIn editor and pick the World AI Summit page from the list, so the post is tagged.)

If you have already announced the summit, as HIGHTABLE has: add your tracking link as a comment on your earlier post, or use it in your next post.

Tracking links (paste only the one for that partner):
- KDEM: https://www.worldaisummit.com/delegate/?utm_source=kdem&utm_medium=partner_social&utm_campaign=world_ai_summit_2026
- WD (Western Digital): https://www.worldaisummit.com/delegate/?utm_source=westerndigital&utm_medium=partner_social&utm_campaign=world_ai_summit_2026
- HIGHTABLE: https://www.worldaisummit.com/delegate/?utm_source=hightable&utm_medium=partner_social&utm_campaign=world_ai_summit_2026
- Successive Digital: https://www.worldaisummit.com/delegate/?utm_source=successive&utm_medium=partner_social&utm_campaign=world_ai_summit_2026
- Kagen.ai: https://www.worldaisummit.com/delegate/?utm_source=kagen&utm_medium=partner_social&utm_campaign=world_ai_summit_2026
- RWS: https://www.worldaisummit.com/delegate/?utm_source=rws&utm_medium=partner_social&utm_campaign=world_ai_summit_2026
- Exatron: https://www.worldaisummit.com/delegate/?utm_source=exatron&utm_medium=partner_social&utm_campaign=world_ai_summit_2026
- IndieRouter.ai: https://www.worldaisummit.com/delegate/?utm_source=indierouter&utm_medium=partner_social&utm_campaign=world_ai_summit_2026

Suggested line for customer invitations (partner's own email or WhatsApp):
"We will be at World AI Summit 2026 in Bengaluru on 14-15 October, booth PLACEHOLDER_BOOTH_NO. If you are attending, do stop by. Passes: {tracking link}[, and use code PLACEHOLDER_GUEST_PASS_CODE for a complimentary pass]."

=====================================================================
4. HOMEPAGE PARTNER BLOCK (web dev, by 4 Oct)
=====================================================================
Plain text, for the visible line under the logos:
World AI Summit 2026 partners. Strategic Partner: Karnataka Digital Economy Mission (KDEM). AI & Data Infrastructure Partner: WD (Western Digital). AI Impact Partner: HIGHTABLE. Bronze Partners: Successive Digital, Kagen.ai. Exhibitors: RWS, Exatron, IndieRouter.ai.

HTML. Keep the existing logo images. Fill the empty "AI & Data Infrastructure Partner" heading with WD, add an "AI Impact Partner" heading for HIGHTABLE, and give every logo a text name and a link:
<section id="partners-2026" aria-labelledby="partners-2026-title">
  <h2 id="partners-2026-title">World AI Summit 2026 partners</h2>

  <h3>Strategic Partner</h3>
  <ul>
    <li><a href="https://karnatakadigital.in/">Karnataka Digital Economy Mission (KDEM)</a></li>
  </ul>

  <h3>AI &amp; Data Infrastructure Partner</h3>
  <ul>
    <li><a href="https://www.westerndigital.com/" rel="sponsored">WD (Western Digital)</a></li>
  </ul>

  <h3>AI Impact Partner</h3>
  <ul>
    <li><a href="https://thehightable.world/" rel="sponsored">HIGHTABLE</a></li>
  </ul>

  <h3>Bronze Partners</h3>
  <ul>
    <li><a href="https://successive.tech/" rel="sponsored">Successive Digital</a></li>
    <li><a href="https://kagen.ai/" rel="sponsored">Kagen.ai</a></li>
  </ul>

  <h3>Exhibitors</h3>
  <ul>
    <li><a href="https://www.rws.com/" rel="sponsored">RWS</a></li>
    <li><a href="https://exatron.in/" rel="sponsored">Exatron</a></li>
    <li><a href="https://indierouter.ai/" rel="sponsored">IndieRouter.ai</a></li>
  </ul>

  <p>To exhibit or partner, write to <a href="mailto:partnerships@worldaisummit.com">partnerships@worldaisummit.com</a>.</p>
</section>

Logo alt text (if the logos stay as images inside the links): alt="Karnataka Digital Economy Mission (KDEM)", alt="WD (Western Digital)", alt="HIGHTABLE", alt="Successive Digital", alt="Kagen.ai", alt="RWS", alt="Exatron", alt="IndieRouter.ai".

Why rel="sponsored" and not plain dofollow:
- Google's policy on qualifying outbound links asks sites to mark paid links with rel="sponsored" (developers.google.com/search/docs/crawling-indexing/qualify-outbound-links).
- Outbound links from our homepage do not help our own rankings either way. The SEO value of this work is the inbound links from partners' pages.
- KDEM is left unmarked as a government Strategic Partner. If KDEM's slot is paid, add rel="sponsored" there too: PLACEHOLDER_KDEM_PAID.

=====================================================================
5. "LAST BOOTHS" LINE FOR EXHIBITOR PROSPECTS (5-9 Oct)
=====================================================================
World AI Summit 2026 takes place on 14-15 October at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. Partners so far:
- Karnataka Digital Economy Mission (KDEM), Strategic Partner
- WD (Western Digital), AI & Data Infrastructure Partner
- HIGHTABLE, AI Impact Partner
- Successive Digital and Kagen.ai, Bronze Partners
- RWS, Exatron and IndieRouter.ai, exhibitors

PLACEHOLDER_BOOTHS_LEFT booths remain. To book one, write to partnerships@worldaisummit.com.

=====================================================================
INTERNAL: SOURCES
=====================================================================
- World AI Summit LinkedIn partner posts: RWS 5 Aug, Successive Digital and Kagen 10 Aug, EXATRON 17 Aug, WD 18 Aug (activity-7495440098138701824), IndieRouter.ai 18 Sep 2026
- HIGHTABLE LinkedIn, 24 Sep 2026 (linkedin.com/posts/hightablevc_hightable-worldaisummit2026-ai-activity-7508854584505929729)
- Syndicated listing that names all 8 partners: happeningnext.com/event/world-ai-summit-2026-eid1ar6ef88bj
- Partner domains checked on 1 Oct 2026 via Exa: successive.tech, exatron.in (plus linkedin.com/company/exatron-in), thehightable.world (plus linkedin.com/company/hightablevc), karnatakadigital.in, indierouter.ai
- /delegate/ price tiers and homepage price: audit of 1 Oct 2026
