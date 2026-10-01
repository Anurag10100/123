# World AI Summit 2026: 14-day traffic and leads plan (1 to 17 October 2026)

Prepared 1 Oct 2026. Ranked by realistic impact in the window times confidence, divided by effort. Asset refs point to files in `assets/`; full evidence per recommendation is in `RECOMMENDATIONS.md`.

## Verdict

- Traffic is not the constraint. GA4 Jul-Sep 2026: 263,703 mailer sessions at 0.06% conversion against 5,393 google/organic sessions at 2.6%; September alone had 224,681 mailer sessions (about 7,500 a day, up from the quarter average of about 2,870 a day). Only 18 users ever reached /delegate/success.php and purchases are not tracked, so real pass sales are unknown.
- The pass page works against itself on 1 Oct: /delegate/ shows an Early Bird row from July 2025, a Standard row that expired 30 Sept and Late Access Rs 30,000/60,000, while the homepage, 10 speaker-page metas and AllEvents still say Rs 20,000; the page has no H1 and is reachable only from the sitemap. Fixing price, path and tracking first is worth more than any ranking work; the assumption that most passes sell in the final two weeks is not measured anywhere in the data.
- Calendar risk: 2 Oct 2026 is a Friday and Gandhi Jayanti, followed by a weekend. Decisions must be collected on the evening of 1 Oct; anything that needs the business and is not decided by then slips to Mon 5 Oct. Web work on 2-4 Oct depends on whether the developer agrees to work the holiday and weekend (PLACEHOLDER), and the merged efforts for 2-3 Oct add up to roughly 30-40 developer hours, so a second developer or a strict priority order is needed.
- Organic is already won where it can be: brand queries #1, /awards #2 for 'world ai awards', homepage #7 for 'ai summit 2026'. New rankings in 16 days are not realistic beyond small CTR gains; anything that needs Google must ship by 3-5 Oct (7 Oct at the outside) and depends on a www Search Console property, because the three www URLs checked on 1 Oct (/, /delegate/, /awards/) all return 'denied access' in Google tools.
- Event week 12-16 Oct is the one organic spike ('world ai summit' 1,600 searches in Sep 2025, 320 in Oct 2025; 'world ai summit 2026' 480 in Aug and rising). /agenda/, an /awards/ page with a deadline, the winners page and the 2027 switch must exist before 13 Oct or those clicks land on dead ends.

## Top moves, in order

### 1. A1 (merges A1 + E2 price and H1 steps): Decide one pass price ladder on the evening of 1 Oct and make /delegate/, the homepage, speaker metas and AllEvents say the same thing

**Do this**

- Marketing head decides on the evening of 1 Oct (2 Oct is Gandhi Jayanti; the hard fallback is Mon 5 Oct 10:00): [PLACEHOLDER: either extend Premium Rs 20,000 / VIP Rs 35,000 to a stated date such as 7 Oct or 13 Oct 23:59 IST, then Late Access Rs 30,000 / Rs 60,000; or make Late Access the current price now]. Also decide whether prices include 18% GST and state it next to every price. Until decided, web dev still deletes the two expired rows (no decision needed) and marks the ladder PLACEHOLDER.
- Web dev (Dev A), first task on the first working day, on https://www.worldaisummit.com/delegate/: delete the 'Early Bird ... Valid till 25th July 2025' row, replace the expired 'Standard Access (Valid till 30th Sept 2026)' row with one dated current row and highlight it, use one set of pass names, add the H1 'World AI Summit 2026 Delegate Passes, Bengaluru, 14-15 October' and the title 'World AI Summit 2026 Passes | 14-15 Oct Bengaluru | Register', and put date, venue, current prices and 'Book Premium Pass' / 'Book VIP Pass' buttons above the fold. About 2 h.
- Homepage 'Secure your seat' block: show the same named, priced tiers (today only 'Premium Pass Rs 20,000/ delegate' is named), replace 'Three release phases. The earlier you commit, the better the price.' with the actual deadline date and next price, and a countdown to that date only, never reset. Fix the /ai-conference-bengaluru-2026.html 'Register' block, which is only a 'Late Access' heading with no price.
- Below the fold on /delegate/ by 4-5 Oct: 'What's included' comparison table, an 8-name 'Who you will hear' strip linking to speaker profiles, agenda and venue links, a buyer FAQ answered by Elets (GST included or extra, GST invoice, pass transfer, refund, on-spot registration, lunch, certificate, what happens after registration), a 4-field group-quote form (name, company, number of delegates, phone) mailing registration@worldaisummit.com and firing GA4 generate_lead with form_type=group, and one line 'Exhibiting instead? Book a booth' linking to the sponsor page.
- Site-wide top ribbon and ONE sticky bottom bar (shared with the WhatsApp bar in move 10), by 4 Oct: '[N] days to go, [current tier and prices], Groups of 3+ save 10%, Book your pass' with a live countdown to 14 Oct 09:00 IST.
- Marketing, same day as the decision: edit the AllEvents listing (allevents.in/bangalore/world-ai-summit-2026-tickets/80002987560857): two ticket types (Premium, VIP) at the decided price, host renamed to 'Elets Technomedia - World AI Summit', group 10% line, three CTAs with the one UTM scheme from move 2 (utm_source=allevents&utm_medium=listing&utm_campaign=world_ai_summit_2026_delegate, partnerships@, /awards/?utm_source=allevents&utm_medium=listing&utm_campaign=world_ai_awards_2026), partnerships email out of the Refund Policy field, 6-10 confirmed speakers from speakers.json; check the HappeningNext mirror within 24-48 h (it shows no price, so no edit there).
- Update the 10 of 51 speaker pages whose meta says 'Passes from Rs 20,000' (anand-thakur, deepika-sandeep, ganesh-joshi, kuldeep-t, pranav-saxena, praveen-bist, ram-mohan-rao, suman-dash, rajesh-choudhary, sushan-rungta) and the 'Delegate passes from Rs 20,000' body line on the speaker template to the decided price; low priority, snippets only.

**Why**

- Exa fetch 1 Oct 2026: /delegate/ shows 'Early Bird ... Valid till 25th July 2025' Rs 20,000/35,000, 'Standard Access (Valid till 30th Sept 2026)' Rs 20,000/35,000 (expired yesterday) and 'Late Access' Rs 30,000/60,000, no GST statement, two sets of pass names; the homepage shows 'Three release phases' with one priced card and two unnamed cards; AllEvents says 'Tickets on approval from Rs 20,000'.
- GA4 property 490291049, Jul-Sep 2026: /delegate/ 2,384 views, 316 form_submit key events from 1,883 users, but only 18 users reached /delegate/success.php. September alone: 286 /delegate/ form submits per the F00 verifier, or 178 form_submit events from 1,729 users per the F02 verifier (two counts, two methods; both say the page carries the pass intent).
- OpenSEO audit c1b16b55, 1 Oct 2026: /delegate/ missing H1, crawlDepth null (sitemap only); 10 of 51 speaker pages carry a Rs 20,000 price in the meta description.
- Competitor Cypher (same week, 7-9 Oct; Exa cached Sep 2026): prices 'incl. 18% GST', dated price steps, sticky bar with countdown, group tiers 10/20/30%, buyer FAQ and 'Exhibiting instead?' box.

**Expected effect:** No organic traffic effect and nothing waits on Google. This is conversion protection on the page that carries pass sales: today a buyer sees Rs 20,000 on the homepage and listings and an expired row plus Rs 30,000 on /delegate/. That the last two weeks are when most passes sell is an assumption, not a measured fact. The size of the lift is unknown because purchases are not tracked in GA4 (fixed in move 2). AllEvents and HappeningNext send an unmeasured number of referrals, likely tens to low hundreds over 1-17 Oct; utm_source=allevents will show the real figure.

**Owner:** Marketing head (price, GST, listings) + web dev Dev A (/delegate/, homepage, ribbon, speaker template)  
**Effort:** S: 30-minute price decision; web dev 3-5 h in total (2 h for the rows, H1 and title; the rest over 3-5 Oct); marketing 1 h for AllEvents; speaker meta edits 1 h  
**By:** Price decision 1 Oct evening (fallback 5 Oct 10:00); expired rows, H1 and title on the first working day (2 Oct if the developer works the holiday, else 3 Oct or 5 Oct); rest by 4-5 Oct  
**Assets:** A07, A02, A51, A29

**Decisions needed**

- Which tier and price is charged from 1 Oct and the exact deadline for the next step (never reset)
- Whether Rs 20,000 / 35,000 / 30,000 / 60,000 include 18% GST
- Whether web dev works 2 Oct (Gandhi Jayanti) and 3-4 Oct (weekend)
- Answers to the buyer FAQ (GST invoice, transfer, refund, on-spot registration, lunch, certificate)
- Optional: Cypher-style tiered group discounts (3-5 passes 10%, 6-10 20%, 11+ 30%) and a 1-day pass

### 2. A3 (merges A3 + E5): Call back everyone who started a pass or nomination but did not pay, fix failed.php and success.php, make GA4 count purchases and leads by form type, and fix one UTM scheme for the whole window

**Do this**

- First working day (2 Oct if desks work the holiday, else 3 Oct): registration and awards desks pull every /delegate/ and /awards/ form submission since 1 Aug 2026 from the form backend or database and the Stripe dashboard (Payments > incomplete or expired checkout sessions) and compare with paid orders; if the forms do not store details before the Stripe redirect, use Stripe's incomplete sessions. This needs no Google and no price decision, which is why it ranks second.
- Within 24 hours of the pull, call and WhatsApp every unpaid starter with a fresh payment link, the 3+ delegates 10% group offer and an option to pay against an invoice or PO; the awards desk does the same for everyone who reached /awards/failed.php. Repeat the sweep on 6 Oct and 10 Oct.
- Web dev (Dev B), 3 Oct: /awards/failed.php (today the bare nomination form with no error message): add 'Your payment did not go through. Your entry is saved.' (only if it really is saved), [Retry payment], [Pay by NEFT/UPI against a GST invoice], a WhatsApp/call button and secretariat@worldaisummit.com. /delegate/success.php (today shows the price table, no visible confirmation): replace with an order confirmation (pass type, 14-15 Oct, venue, e-badge and invoice next steps), an .ics file, a 'Bringing colleagues? 3+ delegates get 10% off' block linking to the group form and a share link tagged utm_source=delegate_share.
- GA4 property 490291049, Dev B, 2-3 Oct: fire 'purchase' server-side once per order with transaction_id, value and currency INR on /delegate/success.php and /awards/success.php (78 success views from 18 users suggests refreshes); begin_checkout on the /delegate/ pay button; a failure event on /awards/failed.php; add checkout.stripe.com to 'List unwanted referrals'.
- Replace the generic form_submit key event with generate_lead carrying form_type = delegate, group, sponsor, prospectus, award_nomination or enquiry, fired on a successful server response rather than on thank-you page load. PLACEHOLDER [whether the forms submit by AJAX or full post is unknown; this decides where the event fires]. Add <meta name="robots" content="noindex"> to /thankyou.html; add a hostname filter (include only www.worldaisummit.com) or mark 127.0.0.1 and localhost as developer traffic.
- One UTM scheme for every channel, using the campaign names already in GA4 (the merged file carries four variants: wais26, wais2026, world_ai_summit_2026 and the GA4 names; use only these): utm_campaign = world_ai_summit_2026_delegate, world_ai_awards_2026 or world_ai_summit_2026_sponsorship. Mailers: utm_source=elets_mailer, utm_medium=email, utm_content=<segment>_<yyyymmdd>. Listings: utm_source=<site> (allevents, eventbrite, globaltradefairs, luma, meraevents, townscript, 10times), utm_medium=listing. LinkedIn: utm_source=linkedin, utm_medium=social, utm_content=showcase_button or li_event. Speaker and partner share: utm_source=linkedin, utm_medium=speaker_share or partner_share, utm_content=<slug>. Elets portals and editorial: utm_source=<portal>, utm_medium=house_ad or editorial. Keep the old world_ai_summit_2026 campaign mapped in reports so history is not lost. Review source/medium by key event on 7 Oct and 13 Oct.

**Why**

- GA4 490291049, 1 Jul-30 Sep 2026: /delegate/ 316 form_submit key events from 1,883 users, but /delegate/success.php had only 18 users (78 views); /awards/ 79 key events from 512 users, /awards/failed.php 8-9 users, /awards/success.php 2 users; checkout.stripe.com/referral brought 5 sessions in September.
- GA4 ecommerce report says 'no ecommerce activity': transactions and revenue are 0 on every source because purchases are never tracked, so the real number of paid passes is unknown; form_submit can fire more than once per user and may include non-lead forms.
- Exa fetch 1 Oct 2026: /awards/failed.php shows the bare nomination form; /delegate/success.php shows the pricing page with no confirmation text.
- GA4 Sept 2026: r.emails.elets.in 224,681 sessions counted as referral (untagged); /thankyou.html was an organic landing page 5 times, each firing a key event; hostnames include 127.0.0.1 (534 views of /index.html), localhost, indiapharmaexpo.com and default.kinfra.myqcloud.com.

**Expected effect:** No traffic effect; this works on the warmest audience the site has and is the fastest revenue action in the plan. Rough guide only: if about 100 unpaid starters exist and 5-10% pay after a personal call, that is about 5-10 passes (about Rs 1-2 lakh at Rs 20,000) plus a few of the 8-9 failed nominations; unverified until the list is pulled. The GA4 events give the first real pass-sales numbers by channel before event week; expect tens of purchases in 2-17 Oct, not hundreds, so do not over-steer on them.

**Owner:** Registration and awards desks (calls) + web dev Dev B (pages, GA4 events, noindex) + marketing (GA4 admin) + email team (UTMs)  
**Effort:** S-M: 3-4 h of calling per sweep, three sweeps; web dev about 2 h for the two panels and 2-3 h for GA4; marketing 1 h; email 30 min  
**By:** Unpaid list on the first working day (2 or 3 Oct); GA4 events 2-3 Oct; first call sweep within 24 h of the pull; panels 3 Oct; sweeps 6 Oct and 10 Oct; reviews 7 and 13 Oct  
**Assets:** A00, A16, A06

**Decisions needed**

- Whether form data is stored before the Stripe redirect, and whether an unpaid entry is really 'saved'
- Approve invoice/PO and NEFT/UPI payment for recovery calls
- Whether the forms submit by AJAX or full page post
- Who owns GA4 admin and the mailer templates
- Whether the desks work 2 Oct (holiday) and the weekend

### 3. B1: From the 2 Oct send, deep-link every Elets mailer and newsletter to /delegate/, /awards/ and the sponsor page with UTMs, keeping prices out of copy until confirmed

**Do this**

- Before the 2 Oct send (a holiday; the send may be scheduled already), web dev removes the expired 'Standard Access (Valid till 30th Sept 2026)' row on /delegate/ (move 1). If it is not fixed in time, hold the pass CTA or send with no price in copy (PLACEHOLDER_FALLBACK_IF_DELEGATE_NOT_FIXED).
- From 2 Oct to 13 Oct, in every Elets mailer and in the eGov Weekly Briefing, BFSI, eHealth and Digital Learning newsletters, the primary CTA 'Book your delegate pass' goes to https://www.worldaisummit.com/delegate/, never to the homepage, /award.html, /registration or /registration.html (3 redirect hops).
- Awards CTA goes to https://www.worldaisummit.com/awards/ (indexed, ranks, holds the form), not /award.html (canonicalised to /, 25,603 views Jul-Sep). Until /awards/ carries the categories (move 6), the mailer names them copied from /award.html (PLACEHOLDER_AWARD_CATEGORY_GROUPS).
- Sponsor CTA goes to the canonical sponsor URL from move 7 [PLACEHOLDER: /partnership.html today, where 117 partnership_form_submit events from 97 users landed 1 Aug-30 Sep per the A5 landing-page cut, or 153 events per the B1 session-landing count; the two figures use different windows and methods], and every mailer carries a 'Request sponsorship deck' line to mailto:partnerships@worldaisummit.com.
- Tag every WAIS link (banner, logo, image, button, footer) with the one scheme from move 2: utm_source=elets_mailer, utm_medium=email, utm_campaign = world_ai_summit_2026_delegate / world_ai_awards_2026 / world_ai_summit_2026_sponsorship (already in GA4) and utm_content=<segment>_<yyyymmdd>; switch off the ESP's automatic UTM option first; run the A34 QA (Gmail and Outlook test, all four utm_ parameters survive the r.emails.elets.in redirect, trailing slashes kept) before every send.
- Keep price, fee, discount, deadline and seats-left out of copy until confirmed: PLACEHOLDER_PASS_PRICE, PLACEHOLDER_AWARD_FEE (/award.html 'from 30k + GST' vs 2025 Rs 18,000-20,000 + GST), PLACEHOLDER_GROUP_DISCOUNT_CONFIRMED, PLACEHOLDER_AWARD_DEADLINE.
- Ask the ESP team to check whether link-scanner security tools are hitting r.emails.elets.in and exclude those clicks; read results in GA4 on an engagement time > 0 segment, counting /delegate/success.php views (purchase events once move 2 is live), partnership_form_submit users and /awards/ form_submit users, not raw key events. Rebuild the 16 Oct post-event send without the pass CTA and with PLACEHOLDER_POST_EVENT_PRIMARY_CTA.

**Why**

- GA4 490291049, Jul-Sep 2026: r.emails.elets.in / referral 263,703 sessions (260,770 users, 32% engagement) with 159 key events, 0.06%; google/organic 5,393 sessions with 138 key events, 2.6%. Mailers are about 92% of all sessions (263,703 of about 285,600). September alone: 224,681 mailer sessions with 96 key events (E5), so the pace rose to about 7,500 a day from the quarter average of about 2,870. (A3 cites 213,013 for Jul-Sep from F17; the 263,703 figure is the one verified against the brief.)
- Mailer clicks land on non-converting pages: / 197,889 views (3.9 s engagement per user), /partnership.html 165,574 views by 136,503 users at 0.39 s per user, /award.html 25,603 views; /delegate/ had only 2,384 views but 316 key events (19 s per user) and /awards/ 876 views with 79 key events.
- Conversion fell to 0.045% in 16-30 Sep 2026; only 18 users reached /delegate/success.php in Jul-Sep; the purchase event shows 0 transactions, so key events are not sales.
- Tagging already works where used: world_ai_summit_2026 2,174 sessions and 97 key events; world_ai_summit_2026_sponsorship 768 sessions and 21 key events (GA4 Jul-Sep 2026).

**Expected effect:** No organic search effect. Two run-rates: at the Jul-Sep average (about 2,870 sessions a day) 1-17 Oct brings roughly 45-50k mailer sessions, about 30 key events at 0.06%, and each 0.1 percentage point gained is roughly 45-50 extra pass, sponsor or award form submits. At the September pace (about 7,500 a day) the window brings roughly 120-130k sessions, about 75 key events at 0.06%, and each 0.1 percentage point is roughly 120-130 submits. The true lift is unknown because bot and scanner clicks inflate the base and cold readers convert below the 316-on-2,384 rate seen on /delegate/. It is still the only lever that touches most of the traffic before 14 Oct.

**Owner:** Elets email/marketing team (links, UTMs, QA) + web dev (/delegate/ row, /awards/ categories) + analytics (GA4 reading)  
**Effort:** S: about 3 h for templates and UTMs, plus under 2 h of web work  
**By:** 2 Oct 2026 send (with the fallback if /delegate/ is not fixed), then every send to 13 Oct; post-event send 16 Oct  
**Assets:** A34

**Decisions needed**

- Current pass price or an extension of the Standard rate (move 1)
- 2026 award fee and nomination deadline
- Confirm the 10% group discount for 3+ delegates before it appears in copy
- Primary CTA for the 16 Oct post-event send
- Fallback if /delegate/ is not fixed by the 2 Oct send

### 4. E1 (merges E1 + C2 Search Console step + F5 Bing and IndexNow): Verify a www Search Console property on 1-2 Oct, reconnect OpenSEO and Bing, then run a daily Request Indexing sprint once pages change

**Do this**

- This is a 45-minute dependency rather than a large lever; it sits at #4 only because every Google-facing item below (awards title, homepage meta, Event schema, /agenda/) cannot be inspected or pushed without it. Do it on 1 Oct evening or 2 Oct even if nothing else happens that day.
- 1-2 Oct: first check whether a www or Domain property already exists under another Google account; if so, grant access. Otherwise add a Domain property 'worldaisummit.com' (DNS TXT at the registrar) or, if DNS is slow, the URL-prefix property https://www.worldaisummit.com/ verified by the Google Analytics method (gtag G-QEB6N0MFLC already loads; needs Edit on GA4 property 490291049) or an HTML meta tag in the homepage head (about 10 minutes).
- Submit https://www.worldaisummit.com/sitemap.xml in the new property (the cleaned version from move 5 once it ships, www URLs only); remove any stale non-www sitemap from the old property. Do NOT use the Change of Address tool (it is for domain moves, not www/non-www).
- Re-point the OpenSEO Search Console integration (app.openseo.so/p/eb76fdff-f482-423c-9a6d-08afeccaa111/settings/integrations) to the new property so inspect_urls and performance cover the real site. Treat query-history backfill as PLACEHOLDER: Google's help page does not promise it.
- From the day moves 1, 5, 6 and 8 go live (3-5 Oct): URL Inspection > Test live URL > Request indexing, about 10 a day. Day 1: /, /delegate/, /awards/, the sponsor page, /ai-conference-bengaluru-2026.html, /speaker.html. Day 2: top 5 speaker pages and /blog/. Repeat for /, /delegate/ and /agenda/ whenever they change; final push 13 Oct; recap push 16 Oct. Also request indexing in the OLD non-www property for https://worldaisummit.com/awards after the one-hop 301 (move 6) is live. Do not use the Indexing API (JobPosting and BroadcastEvent only).
- Same day: Bing Webmaster Tools, verify www by DNS or meta, Import from Google Search Console, submit the sitemap, set up an IndexNow key file and ping IndexNow with each changed URL to 17 Oct (Google does not use IndexNow; Bing feeds ChatGPT search and Copilot, link inferred).

**Why**

- OpenSEO inspect_urls, 1 Oct 2026: the three www URLs checked (/, /delegate/, /awards/) all return 'Search Console denied access to this property'; the only connected property is URL-prefix https://worldaisummit.com/ (non-www).
- GSC non-www, 28 Jun-28 Sep 2026: only 3 URLs have impressions (/awards 79 clicks / 2,419 impressions; / 5 clicks / 25 impressions; /1st-edition/ai-dialogues 0 / 2), while GA4 shows the www homepage alone had 2,446 organic landing sessions in 3-30 Sep, none visible in Search Console.
- URL Inspection 1 Oct: non-www /awards is 'Submitted and indexed' with the non-www URL as Google's canonical, last crawled 28 Sep with a 200; the 1 Oct crawl shows it now 301s to www, so consolidation is pending during the two weeks that matter. Googlebot crawled the non-www homepage on 1 Oct 09:45 UTC.
- GA4 3-30 Sep 2026: chatgpt.com / ai-assistant sent 447 sessions and 29 key events, more than bing / organic (79 sessions).

**Expected effect:** No direct traffic; tens of extra sessions at most. Request Indexing usually gets a changed URL recrawled in hours to a few days (not guaranteed), so the price, awards, homepage and schema changes can show in results before the 7-13 Oct selling week. The main value is that www query data and URL inspection become visible for event-week tuning, and that the only true indexing gap (speaker pages) is closed.

**Owner:** Marketing (GSC owner) + web dev (DNS or head tag, IndexNow key file)  
**Effort:** S: 15-45 min verification, 20 min IndexNow, then 15 min a day from the first deploy to 13 Oct and on 16 Oct (about 4 h total)  
**By:** Verify by 2 Oct 2026 (needs no business decision and no developer time beyond 10 minutes); sprint from the first deploy day (3-5 Oct); final push 13 Oct; recap push 16 Oct  
**Assets:** A56, A14, A60, A21

**Decisions needed**

- Who holds DNS or registrar access, and whether a www or Domain property already exists under another Google account
- Who has Edit access on GA4 property 490291049 if the GA verification route is used

### 5. A2 (merges A2 + E2 link steps + E3): Close the dead ends: one-hop 301s for every register and legacy URL, crawlable Book / Nominate / Sponsor links on the homepage, nav and speaker pages, and a clean sitemap

**Do this**

- First working day (Dev B, about 1 h): one-hop 301s to https://www.worldaisummit.com/delegate/ from /registration and /registration.html (today 302 to https://worldaisummit.com/ then 301 to www, 3 hops) and /delegate-registration.html (400 views, 312 users in September, no visible form). /1st-edition/delegate-pass.html: [PLACEHOLDER: 301 to /delegate/, or keep at 200 with a top banner 'This page is the 2025 edition. Book World AI Summit 2026 passes'; the banner option is recommended because move 12 (G4) assumes the URL stays live]. Remove /registration and /registration.html from sitemap.xml. Rules go ABOVE the generic host rule; server stack PLACEHOLDER [Apache or nginx; both rule sets are in the assets].
- Homepage and /index.html hero, 3 Oct (Dev A): replace 'Save the date' with three plain <a href> buttons: 'Book delegate pass' to /delegate/, 'Nominate: World AI Awards 2026' to /awards/, 'Sponsor or exhibit' to [PLACEHOLDER: canonical sponsor URL from move 7]. Make the 'Secure your seat' card buttons, the nav 'Register' item and the FAQ answer 'How can I register for the event?' crawlable links to /delegate/ (no JS onclick, no non-www absolute URLs).
- Header nav and footer on every page: 'Passes' /delegate/, 'Agenda' /agenda/ (once live), 'Speakers' /speaker.html, 'Awards' /awards/, 'Venue' /#venue (add id="venue" to the existing 'Where It All Comes Together' block, do not rewrite it), 'Partner' sponsor page, plus /ai-conference-bengaluru-2026.html and /blog/. Homepage H1 becomes the event name with the theme sentence as a styled <p>; render 12 confirmed 2026 speakers as HTML text with links plus 'See all confirmed speakers'; the FAQ rewrite is in move 8.
- Add one 'Book your pass' CTA block (decided price from move 1, or no price) to the shared template of the 51 /assets/speaker_details/*.html pages, /speaker.html and /ai-conference-bengaluru-2026.html. Run grep -rn 'https\?://worldaisummit\.com' --include=*.html . and replace every non-www absolute href.
- By 5 Oct (Dev B), the full legacy map as one-hop 301s, path-preserving on both hosts, before the catch-all: /awards (no slash), /award.html, /nomination, /entry-guidelines to /awards/; /partnership variants and /partner-benefits to the sponsor URL; /faqs and /thematic-tracks to /; /ai-dialogues, /startup-competition and the 2025 blog slugs to /ai-conference-bengaluru-2026.html; /index.html to /; /blog/index.html to /blog/; then non-www and http to https://www. Two corrections to the merged E3 list: (a) /1st-edition/awards.html is NOT redirected; it stays live as the '2025 edition' page that move 6 links to and that may hold the 2025 winners list (move 12), with the archive banner; (b) /agenda (and /world-ai-agenda.html, /world-ai-agneda.html) is redirected once only, straight to /agenda/, which ships as a holding page in the same deploy (move 9, v1 with the 7 tracks and TBA cells), so there is no interim target and no retargeting. Test every source with curl -sI for a single 301 and a final 200.
- Rebuild sitemap.xml to list only 200, self-canonical URLs with a real <lastmod> (never today's date on every URL): remove 18 URLs (the E3 list of 19 minus /1st-edition/awards.html, which stays as a linked archive page): index.html, blog/index.html, award.html, partnership.html, the two /registration URLs and 12 /1st-edition/ URLs; keep /, /delegate/, /awards/, the sponsor page, /ai-conference-bengaluru-2026.html, /speaker.html, /agenda/, /blog/ and 5 posts, /1st-edition/, /1st-edition/speakers.html and /1st-edition/awards.html as archive, and the speaker pages; resubmit in the www property (move 4). Keep /1st-edition/ as archive with a banner and 'World AI Summit 2025 Archive' titles.

**Why**

- OpenSEO crawl c1b16b55, 1 Oct 2026: /registration and /registration.html return 302 to https://worldaisummit.com/ and sit in the sitemap; /delegate/ and /awards/ have crawlDepth null with no crawlable path from the homepage; the homepage is the only HTML URL with a crawl depth (0).
- GA4 1-30 Sep 2026: /delegate-registration.html 400 views, 312 users, about 7 s engagement, 0 key events, only 12 sessions organic; it looks like an active campaign link pointing at a page with no form.
- GA4 organic, 3-30 Sep 2026: homepage landing 2,446 sessions, 53 key events (about 2.2%; the merged file prints 1.92%, which would match 47 events, so re-check before it enters the baseline); /delegate landing 48 sessions, 16 key events from 7 users (16.7%); Organic Search 3,082 sessions vs 1,348 in the prior 28 days (+128.6%).
- Sitemap reconstructed from the audit: 84 URLs, 6 return 302, 5 are canonicalised elsewhere, 15 are /1st-edition/ archive URLs; every legacy URL (/agenda 7,566 impressions in 16 months, /why-attend 8,229, /faqs 2,510) had zero impressions in the last 28 days and Google last crawled most of them with 5xx in May-July 2026.

**Expected effect:** Organic traffic gain in the window is about zero: the registration queries (#4, #10) are already won by the homepage and redirects or an H1 will not move rankings in two weeks. Leads: the /delegate-registration.html 301 alone sends roughly 300 users a month to a page with a form instead of none. On the homepage a realistic +0.2 to 0.5 percentage point on about 2,000-3,500 organic homepage sessions over 1-17 Oct is roughly 5-15 extra organic form enquiries; the same links help mailer and paid visitors, unquantified. Sitelinks on brand queries are Google's choice. Legacy map and sitemap are cheap hygiene, not traffic.

**Owner:** Web dev Dev B (redirects, sitemap, href sweep) + Dev A (homepage, nav, template) + content (speaker strip)  
**Effort:** S for register redirects and links (1-2 h); M for the homepage above the fold (half day); 1-3 h legacy map and testing; 1 h sitemap  
**By:** Register redirects and crawlable links on the first working day (2 or 3 Oct); hero and nav 3 Oct; legacy map, /agenda/ holding page and sitemap by 5 Oct  
**Assets:** A01, A08, A16, A18, A57, A15, A58, A67

**Decisions needed**

- Whether /1st-edition/delegate-pass.html is redirected or kept with a banner (banner recommended)
- Canonical sponsor URL (move 7) so hero and nav point to one place
- Which 12 speakers go on the homepage strip (from speakers.json confirmed_2026)
- Server stack and where the current /registration 302 rule lives
- Name of the second developer or agency (Dev B); if there is none, accept the priority order and the slip described in the day-by-day

### 6. C1 (merges C1 + C2 + C3): Rebuild /awards/ into the one World AI Awards 2026 page (categories, fee, deadline, FAQ) with a one-hop 301, a sitewide deadline banner and the 2025 elets.net checkout retired

**Do this**

- 1 Oct evening or first working day: awards team supplies deadline, 2026 fee, ceremony day and a WhatsApp number (30 min). Web dev adds a key-facts banner directly above the form on https://www.worldaisummit.com/awards/: 'Nominations close PLACEHOLDER_DEADLINE (weekday, date, time IST). Entry fee from Rs PLACEHOLDER_FEE_2026 + GST per entry. Winners honoured at World AI Summit, Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru, 14-15 Oct 2026 (ceremony day to confirm)' with buttons 'Nominate now' (#nominate), 'See all categories' (#categories) and 'WhatsApp the awards desk'. The A03 auto-close script swaps the banner on deadline day.
- By 3 Oct (Dev A, 2-4 h) copy from /award.html into /awards/ above the form: the six category groups as one H2 each with every award as plain text (26 + 13 + 16 + 4 + 19 + 18 = 96 named awards, so '75+' is safe), the six-step 'How to Nominate' and the benefits; H1 'World AI Awards 2026' (today it is the summit theme); a title at or under 60 characters such as 'World AI Awards 2026: Nominate by PLACEHOLDER_DEADLINE_SHORT | 75+ Categories' or 'World AI Awards 2026 | Nominate Now | Bengaluru, 14-15 Oct'; meta from A61; sections 'Who can enter', 'Nomination fee' (2026 figure only, never the 2025 Rs 18,000 / 20,000 tiers), 'Deadline', 'Evaluation criteria' and 'How entries are judged' (jury names only if supplied); an 8-10 question FAQ from A65 with the 2025 fee lines removed; link /1st-edition/awards.html as the '2025 edition' page (it stays live; it is removed from the move 5 redirect list for this reason); add organizer, offers (only after the fee is confirmed) and performer to the existing Event JSON-LD.
- Redirects (Dev B, about 1 h), before or with the rebuild: record the current state, then make https://worldaisummit.com/awards and /awards/ reach https://www.worldaisummit.com/awards/ in a single 301 (not non-www > www /awards > /awards/); self-referencing canonical on /awards/; /award.html gets a canonical to /awards/, its own title and meta and two 'Nominate now' buttons now (A03 snippets 8-9), then a 301 once the categories are live; verify all four host and slash variants with curl -sI. Make no other awards URL changes until after 17 Oct.
- Sitewide (Dev A, 1-2 h): replace the homepage block ending 'World AI Awards. Previous edition' with 'World AI Awards 2026: nominations close PLACEHOLDER_DEADLINE. Nominate now' (A62, drop its /awards/winners-2025/ link and any fee figure); add 'Awards' to the nav and footer; one-line deadline banner linking /awards/ with the anchor 'World AI Awards 2026' on /delegate/, /ai-conference-bengaluru-2026.html, /speaker.html and the 5 blog posts; link the existing mention in 'Beyond the Hype'; GA4 click event on the homepage awards CTA.
- Elets web team: https://elets.net/worldaisummit-awards/ still shows 2025 fees (Rs 18,000 + GST startup, Rs 20,000 + GST enterprise) and a live Rs 30,000 checkout; either update it to 2026 copy with a prominent link to /awards/ or 301 it there, so no 2025 payment is taken by mistake.
- Checks before upload: grep -rn PLACEHOLDER_ ., one title and one canonical per page, 360 px phone view, #nominate and #categories anchors, WhatsApp link on a phone; then request indexing in both properties (move 4). Measure against the baseline of 32 clicks from 1,300 impressions at position 7.9 (GSC non-www, 31 Aug-28 Sep); take the paid nomination count from the awards team, not GA4 form_submit.

**Why**

- /awards is the only non-brand page earning Search Console clicks: 79 clicks from 2,419 impressions, CTR 3.3%, position 9.1 (GSC non-www, 28 Jun-28 Sep 2026); all other pages 5 clicks combined. Query rows: 'ai awards 2026' 243 impressions at 9.2 (7 clicks), 'ai awards' 199 at 9.8, 'world ai awards' 66 at 3.1 with 0 clicks (a snippet that does not answer the searcher).
- Live Google India 1 Oct: 'world ai awards' #2 behind worldawards.ai (unrelated brand); 'ai awards 2026' #4; 'ai awards india' #8 (Cypher #1). The page body is 564 words with the summit theme as H1 and no categories, fee, deadline or criteria (Exa and audit c1b16b55), while /award.html already holds the 96 awards, 'Entries from 30k + GST' and the six steps but is canonicalised to / and 'URL is unknown to Google'.
- Every visible awards signal points to the past: the homepage block reads 'World AI Awards. Previous edition' with no date or CTA; /awards/ has 4 internal links and is not in the nav; GA4 shows /award.html 25,603 views and 18,849 users (about 2 s each) from mailers landing on a page with no nominate button.
- Timing: Cypher's deadline was 9 Sep 2026 and the ET Enterprise AI Awards ceremony was 17 Sep 2026, so in October WAIS is likely one of the few India AI awards still taking entries (inferred from these two checks only).

**Expected effect:** Traffic: small. Baseline about 19-20 clicks over 1-17 Oct; a distinct title and 'Nominations open' snippet could add roughly +3 to +25 clicks after recrawl; India sends only about 10 impressions and 0.25 clicks a day to /awards, most clicks come from other countries. The real gain is conversion of visitors who today cannot see categories, fee or deadline without opening the form, and the redirect work is insurance against ranking churn while Google moves from non-www to www. Each nomination is a paid entry (2026 fee unknown); the number of extra nominations is unknown.

**Owner:** Web dev Dev A (copy, head tags, banners) + Dev B (redirects) + Elets awards team (deadline, fee, jury, WhatsApp number) + content (FAQ, criteria) + Elets web team (elets.net) + marketing (GSC)  
**Effort:** S-M: 30 min awards team; web dev about 4-7 h in total (C1 2-4 h, C2 about 1 h, C3 1-2 h); 1-2 h content; 30 min Elets web team  
**By:** Awards facts 1 Oct evening (fallback 5 Oct); banner, redirects, homepage block and nav on the first working day; full rebuild live by 3 Oct, 5 Oct at the latest, so Google can recrawl before nominations close  
**Assets:** A61, A52, A09, A27, A65, A03, A21, A62

**Decisions needed**

- 2026 nomination deadline (date and time IST), a few days before 14 Oct for jury work
- 2026 entry fee: one fee or two tiers, '+ GST' or inclusive; must match or replace /award.html's 'Entries from 30k + GST'
- Ceremony day (14 or 15 Oct) and time slot; whether a delegate pass is included; multi-entry rule
- 2026 jury names or process-only wording; awards desk WhatsApp number
- Whether /award.html becomes a 301 to /awards/ once the rebuild is live
- elets.net/worldaisummit-awards/: update to 2026 copy or 301

### 7. A5 (merges A5 + E2 sponsor-page steps): Pick one sponsor URL on 1-2 Oct and turn it into a real lead page: benefits, remaining inventory, named contact and a gated 2026 deck

**Do this**

- Marketing head, 1 Oct evening or 2 Oct, decides the canonical sponsor URL: [PLACEHOLDER: /partnership.html (A5: where mailers land; 117 partnership_form_submit events / 97 users landed there 1 Aug-30 Sep) with /partner-with-us.html 301'd to it; or /partner-with-us.html (E2, E3: already #7 for 'world ai summit sponsorship', has an H1 and the 5 benefit blocks) with /partnership.html 301'd to it]. Every hero, nav, FAQ, listing and mailer CTA then points at that one URL; the 301 must be live before any in-flight mailer link changes.
- By 4 Oct (Dev B, half a day; 3 Oct belongs to the awards and homepage work) on the chosen page: self-referencing canonical (both are canonical to / today), the title 'Sponsor & Exhibit at World AI Summit 2026, Bengaluru' and its own meta (the old 'Global Artificial Intelligence Conference by Elets Technomedia' title is still live on /award.html, /partnership.html and /partner-with-us.html); the 5 benefit blocks (sponsorship, exhibit, centre-stage speaking slot, 1:1 meetings and roundtables, AI Innovation Report feature) above the form; 'Who you will meet' reusing the homepage 'Who Should Attend' list and the 7 tracks; 'Past partners' reusing the homepage logos and 2025 testimonials (Bandhan Bank, Razorpay, Pinnacle, Zrika).
- 'Still available for 14-15 Oct:' listing only inventory that is really open (exhibition booths, awards-night or networking-dinner sponsorship, from the partnerships team); a strip naming KDEM (Govt of Karnataka) as [PLACEHOLDER: 2026 Strategic Partner per the brief; F05 says 2025]; one audience figure PLACEHOLDER [1,000+ or 1,200+ delegates]; the partnerships WhatsApp/call button from move 10 and a named contact.
- 'Download the 2026 partnership deck' gate (name, company, designation, work email, phone) delivering the PDF instantly, alerting partnerships@worldaisummit.com and firing generate_lead with form_type=prospectus; confirm a 2026 PDF exists first.
- Link the page from the homepage hero 'Sponsor or exhibit' button, the footer partnership-emails area, the FAQ answer 'Are exhibition and sponsorship opportunities available?' and the /ai-conference-bengaluru-2026.html 'Partner With Us' link; then request indexing (move 4).
- Before sizing any uplift, check partnership_form_submit counts against the partnerships@ inbox or CRM: 51 events have /thankyou.html as landing page, so the event likely fires on reload too.

**Why**

- GA4 490291049, Jul-Sep 2026: /partnership.html 165,574 views, 136,503 users, about 0.4 s engagement per user (link-scanner or instant-bounce visits); Exa 1 Oct: the page holds 64 words, the tagline and contact emails; /partner-with-us.html has 219 words and the 5 benefits; crawl c1b16b55: both canonical to / and sharing the homepage title.
- GA4 1 Aug-30 Sep 2026, partnership_form_submit by landing page: 142 events / 121 users on /, 117 / 97 on /partnership.html, 51 / 39 on /thankyou.html, about 315 in total; about 48 users a month on /partnership.html, unverified against the inbox. (B1 quotes 153 events for sessions that landed on /partnership.html; different window and count method.)
- Live Google India 1 Oct: /partner-with-us.html is #7 organic for 'world ai summit sponsorship', the homepage #1 with 'Partner with us ... partnerships@' in its snippet. Cypher's header and footer carry 'Book a Booth', 'Become a sponsor', 'Sponsor' and 'Exhibit'.
- Booth fabrication lead times make sponsor leads after about 8 Oct hard to close for 14-15 Oct (F05).

**Expected effect:** No organic traffic in the window: a self-canonical and a new title on a thin page will not earn rankings in two weeks for a site with about 10 real referring domains. Leads: the page already yields roughly 48 partnership_form_submit users a month (count unreliable); the deck gate adds a lower-commitment step for the real visitors among mostly scanner sessions. Uplift unquantified, but a sponsor lead is the highest-value lead the event has, and only leads before about 8 Oct are closable for 14-15 Oct.

**Owner:** Marketing head (URL decision) + partnerships (deck, inventory, KDEM wording, named contact) + web dev Dev B  
**Effort:** M: web dev half a day; partnerships 1-2 h; marketing head 15 min  
**By:** URL decision 1-2 Oct 2026; page live 4 Oct (5 Oct at the latest, because sponsor leads after 8 Oct are hard to close)  
**Assets:** A05, A59, A10

**Decisions needed**

- Canonical sponsor URL (/partnership.html or /partner-with-us.html)
- Whether a 2026 partnership deck PDF exists and can be gated
- Which inventory is genuinely unsold for 14-15 Oct
- KDEM partnership year wording and the single audience figure

### 8. D3 (merges D3 + E4 + F5 schema and FAQ + A2 H1 and FAQ steps): By 4 Oct: homepage meta, key-facts block, fact-first FAQ rewritten in place, and correct Event and Organization JSON-LD with the real price

**Do this**

- Homepage title: [PLACEHOLDER: keep the live 'World AI Summit 2026 | AI Summit India, Bengaluru, 14-15 October' (64 chars; A2 says it already works), or ship D3's 'World AI Summit 2026 | 14-15 Oct, Bengaluru | Register Now' (58 chars) so 'October' is not cut off]. Either way 'World AI Summit 2026' stays first to protect the #1 brand rankings. Replace the 182-character meta (Google rewrites it) with A26 (157 chars) or A17 (149 chars); do not open with 'India's next AI summit' (Cypher runs 7-9 Oct in Bengaluru) and do not say '100+ speakers' unless verified (50 confirmed). Give /speaker.html its own meta.
- Directly under the hero add a 120-200 word 'AI Summit 2026 in Bengaluru: key facts' block: date, venue, 7 tracks, who attends, 'Book delegate pass' link to /delegate/.
- Rewrite the existing homepage FAQ in place (no second block), each question an H3 with the fact in the first 25 words: when and where; price (PLACEHOLDER_CURRENT_PASS_PRICE, GST stated); how to register and by when, linking /delegate/; is it free; the 7 official tracks (the current answer lists fintech, healthcare, smart cities and cybersecurity); group discount; sponsor or exhibit via the sponsor page; award nominations via /awards/; how to reach the venue (facts from the venue only); 'Is World AI Summit the same as World Summit AI in Amsterdam?' (two factual sentences, after PLACEHOLDER_NO_AFFILIATION is confirmed); whether it is the India AI Impact Summit (16-20 Feb 2026, Bharat Mandapam) with PLACEHOLDER_IMPACT_SUMMIT_ANSWER. FAQPage JSON-LD is optional: Google retired FAQ rich results for all sites on 7 May 2026.
- Event JSON-LD in the homepage <head> only (one event, one leaf URL; do not duplicate on /delegate/ or /ai-conference-bengaluru-2026.html): name, startDate 2026-10-14, endDate 2026-10-15, eventAttendanceMode offline, Place 'Sheraton Grand Bangalore Hotel at Brigade Gateway' with PostalAddress (verify the street address; the asset's came from globaltradefairs.com), organizer Elets Technomedia, performer, offers.price PLACEHOLDER [price from move 1] in INR, offers.url https://www.worldaisummit.com/delegate/. Edit the A23 default of 20000/35000 with validFrom 2026-10-01 first; add an image already on the site (720px+). Keep times consistent with AllEvents (14 Oct 9:00 AM to 15 Oct 6:00 PM IST) or PLACEHOLDER_START_TIME. If the price is still undecided on 4 Oct, publish the Event node without the offers block and add offers when the price lands.
- Repair the Event markup Google already detects on /awards (warnings for missing performer, offers, organizer): complete it on www /awards/ or remove it so it does not compete with the homepage event. Add Organization JSON-LD beside it with alternateName, disambiguatingDescription, parentOrganization Elets Technomedia (has a knowledge panel) and sameAs; publish only a complete schema.
- Validate in the Rich Results Test and Schema Markup Validator, request indexing of / and /awards/ (move 4). On indiaaisummit.in add a top banner 'Next: World AI Summit 2026, Bengaluru, 14-15 Oct' linking to the homepage; keep /ai-conference-bengaluru-2026.html as a supporting page linking to the homepage with the anchor 'AI summit 2026 in Bengaluru'.

**Why**

- OpenSEO keyword metrics, India, 1 Oct 2026: 'ai summit 2026' run-rate 6,600/mo in Jul-Aug (the 40,500 average is inflated by Feb 2026 at 450,000); 'ai summit' 1,900; 'ai summit india' 320; 'world ai summit 2026' 480 and rising. Live SERP: homepage #7 for 'ai summit 2026' and 'ai summit', #9 'ai summit india', #4 'ai summit registration' (about 10/mo), AI Overview on 21 of 22 queries; the top 6 for 'ai summit 2026' are about the February Government summit.
- Exa fetch 1 Oct 2026: the homepage FAQ is generic with no date, venue, price, 'is it free' or disambiguation answer; its registration answer has no link; its topics answer contradicts the 7 tracks shown higher on the page; the meta is 182 characters.
- Google Events carousel on 5 Bangalore discovery queries (about 4,700 searches/mo combined; 'ai events in bangalore' 260-320/mo, WAIS organic #9) with WAIS absent; URL Inspection 1 Oct shows an Events rich result on non-www /awards with warnings for performer, offers and organizer; AllEvents already feeds Google 14-15 Oct, Rs 20,000 and a /delegate/ link.
- 'world ai summit' page 1 on Google India, 1 Oct: 3 of the 6 organic listings are worldsummit.ai (Amsterdam, 7-8 Oct per context; the SERP snippet says 5-9 Oct); a WebSearch answer on 1 Oct described Amsterdam with Bengaluru as a footnote.

**Expected effect:** Roughly 3,000-4,000 'ai summit 2026' searches fall in 1-17 Oct at the run-rate; at #7 with 3-4% CTR that is about 140 clicks today. A clearer title and meta could add about +20 to +60 clicks; reaching #4-5 would add +150 to +250 but position gains in two weeks are uncertain and most of these searchers want the February Government summit. Event panel: a few dozen to low hundreds of clicks over 7-17 Oct if Google picks up the markup by about 7 Oct, near zero otherwise; carousel order is Google's. Leads: the FAQ answers the price and deadline questions that block purchase and puts /delegate/ one click away; size unknown.

**Owner:** Web dev Dev A (markup, FAQ, meta) + content (key facts, FAQ copy) + marketing (price, 30 min)  
**Effort:** S: title and meta under 1 h; key-facts block and FAQ about 2 h; Event schema under 2 h; Organization schema and Amsterdam FAQ under 1 h (about 6 h in all)  
**By:** Homepage meta, key facts, FAQ and Event JSON-LD by 4 Oct 2026 (5 Oct at the latest; after 7 Oct the recrawl is unlikely to land before event week); Organization schema and Amsterdam FAQ by 5 Oct, before Amsterdam's news peak  
**Assets:** A26, A25, A17, A50, A23, A20, A75

**Decisions needed**

- Keep the current homepage title or ship the 58-character variant
- Which meta draft to ship (A17 149 chars or A26 157 chars)
- Live pass price and GST wording for the FAQ and offers.price
- Approved wording for the India AI Impact Summit question; confirmation of no affiliation with World Summit AI
- Whether a speaker count may be stated (50 confirmed vs '100+')
- Whether /awards/ keeps its own completed Event node or drops it; confirm the venue street address

### 9. D2 (merges D2 + G1 + B5 hub and 'Latest' block): Publish one /agenda/ hub (holding page by 5 Oct, agenda by 8 Oct, live updates 14-15 Oct, highlights from 16 Oct) and link it from the homepage, so event-week brand searches land on a schedule

**Do this**

- Programme team hands over the running order by PLACEHOLDER_AGENDA_DATA_DATE (the bottleneck: speakers.json has session null and empty time and hall for all 76 entries). Web dev builds https://www.worldaisummit.com/agenda/ (one URL) with the title 'Agenda | World AI Summit 2026, 14-15 Oct, Bengaluru', an H1, a 'last updated' date and 'Programme subject to change'.
- Holding page by 5 Oct regardless of the running order: the 7 tracks, Day 1 and Day 2 headings, registration opening, awards ceremony and VIP dinner slots, TBA cells, 'full schedule updated daily' and the booking buttons; this lets the one-hop /agenda > /agenda/ 301 ship with the legacy map (move 5) and gives every mailer, article and speaker page a live link target. Full v1 with sessions by 6-7 Oct and no later than 8 Oct: Day 1 (Wed 14 Oct) and Day 2 (Thu 15 Oct) tables with Time | Session | Format | Track (one of the 7) | Hall | Speakers linked to the live /assets/speaker_details/<slug>.html pages; one id anchor per session and per track; do not draft sessions or list unconfirmed speakers; final version with halls by 13 Oct; bump sitemap lastmod on each update.
- Conversion: 'Book your delegate pass' button beside each day and after each half-day to /delegate/; 'Sponsor a session' to partnerships@worldaisummit.com; optional 'Download the agenda (PDF)' behind a 5-field form delivering to registration@ so the sales desk has named leads to call 7-13 Oct (PLACEHOLDER_GATE_PDF: yes or no). Event JSON-LD with one subEvent per session and the Offer taken from the live /delegate/ price; fill session, time and hall in speakers.json in parallel.
- Links: homepage nav and the 'Seven tracks. One agenda' section (no agenda link today), a 'Latest from the Summit' block in or below the hero listing the 3 newest URLs, /delegate/, /speaker.html, every speaker profile ('See the agenda'), /ai-conference-bengaluru-2026.html and the 5 blog posts; add to sitemap.xml; the 301s from /agenda (5xx since 26 May 2026, still linked from cio and egov 2025 articles), /world-ai-agenda.html and /world-ai-agneda.html point here once and only once (A67); banner or 301 on /1st-edition/world-ai-agenda.html. Hand each new URL to the Elets desks so their piece links to it the same day.
- 14 Oct 08:00 IST: switch title and H1 to the Live variant and add a 'Live updates' block above the agenda, newest first, one entry per session or every 30-60 min: session, track, speaker link, 2-3 verbatim quotes or factual takeaways, one captioned photo, YouTube link where available; LiveBlogPosting JSON-LD (coverageStartTime 2026-10-14T09:00+05:30, coverageEndTime 2026-10-15T19:00+05:30), max-image-preview:large, a 1200px+ hero; homepage hero link 'Live now: Day 1 updates'; two content people on site. Treat the live rich result as uncertain upside; do not use NewsArticle.
- 16 Oct 12:00 IST: switch to the Highlights variant (800-1,200 words: Day 1 and Day 2, the 8-10 biggest statements, launches and MoUs), keep the full agenda below so the URL is the permanent recap, and add the lead box 'Get full session recordings' with 2027 interest checkboxes (attend / sponsor / speak / nominate) and 'Enquire for 2027 sponsorship' to partnerships@. Request indexing on publish and at each phase switch (move 4).

**Why**

- Audit c1b16b55 and Exa, 1 Oct 2026: no 2026 agenda URL exists; /agenda/ is 'URL is unknown to Google'; /agenda returns 5xx, last crawled 26 May 2026; the only agenda page is /1st-edition/world-ai-agenda.html (89 words, titled 'World AI Summit 2025'). The site itself promises the page: speaker pages say 'Session title, time and hall will be published on this page once the agenda is final'.
- Live SERP India 1 Oct: 'world ai summit 2026 agenda' worldsummit.ai #1, impact.indiaai.gov.in #2, homepage #3; 'world ai summit live' homepage #4; 'world ai summit bengaluru agenda' homepage #1; 'world ai summit 2026 speakers' homepage #1 and /speaker.html #4, so brand-modified pages from this domain rank quickly once linked. Search Console has no query pairing the brand with 'agenda'; the 7,566 impressions on non-www /agenda fell between Dec 2025 and May 2026, zero since.
- Brand demand spikes in event month: 'world ai summit' 880 (Aug 2025), 1,600 (Sep 2025), 320 (Oct 2025); 'world ai summit 2026' 170 (Jun) to 480 (Aug). The homepage takes all of it and carries no schedule.
- Competitors treat the agenda as the main CTA: worldsummit.ai hero 'Download 2026 Agenda'; Cypher /schedule has 'Download PDF' and ranks #7 for 'ai conference' (1,300/mo); Inc42 lists time slots with 'Talking Points'. Four other recommendations (B4, B5, G5, G6) link to /agenda/ and break without it.

**Expected effect:** Organic before the event: single to low double digits of visits, since branded agenda demand is below the reporting threshold. Over 12-17 Oct: tens to low hundreds of extra organic visits from agenda, live and highlights searches that today land on a homepage with no schedule (inferred; no www data), mostly clicks moved off the homepage rather than new sessions. The value is conversion (day 1 vs day 2, Premium vs VIP, sponsors seeing a concrete programme), named PDF leads if gated, a working link target for speakers and Elets stories, and recording-form and 2027 leads from the most engaged visitors. Depends entirely on the programme team.

**Owner:** Elets programme team (session data) + web dev Dev A (template, JSON-LD, phase switches) + Dev B (redirects) + content (daily updates; two people on site 14-15 Oct) + content lead ('Latest' block)  
**Effort:** M: web dev 3-4 h for the template and links plus daily updates; about 20 h across the three phases  
**By:** Holding page 5 Oct with the legacy map; v1 with sessions 6-7 Oct and no later than 8 Oct; final with halls 13 Oct; live phase 08:00 IST 14 Oct; highlights 12:00 IST 16 Oct  
**Assets:** A46, A53, A12, A45, A67, A47, A77, A22

**Decisions needed**

- Programme team: date by which a near-final running order (sessions, times, halls, speakers) can be supplied
- Gate the PDF or leave it open
- One hub URL: /agenda/ (recommended) rather than /2026/live/ or /blog/ variants
- Who staffs the live desk on 14-15 Oct and who approves quotes

### 10. A4: Add one staffed WhatsApp and click-to-call bar with Book passes, Sponsor or exhibit, and Nominate intents on every lead page

**Do this**

- Marketing confirms whether 9818274383 (delegates) and 8860651641 (speaking) on /1st-edition/delegate-pass.html are still staffed, and assigns numbers for the sponsor/exhibit and awards lines (the 2025 page has none). Do not publish a number nobody answers.
- Web dev adds a small bottom bar on mobile and a side button on desktop, merged with the price ribbon bar from move 1 so there is ONE bar, with three intents: 'Book passes' (registration desk), 'Sponsor / exhibit' (partnerships desk), 'Nominate' (awards desk); each opens wa.me/<number>?text=<prefilled intent> and has a tel: link.
- Fire GA4 event contact_click with method (whatsapp or call) and intent.
- Staff each line 9 am to 8 pm until 17 Oct with answers ready for GST invoice, PO, group pricing and 'what do I pay now?' questions arising from the expired Standard row.
- Show the bar on /, /delegate/, /awards/, /award.html and the sponsor pages; keep the existing 'World AI Summit Community' WhatsApp channel CTA but label it as updates, not a sales line.

**Why**

- Exa fetch 1 Oct 2026: the homepage, /delegate/, /partnership.html and /partner-with-us.html show only registration@, partnerships@ and secretariat@ addresses; /awards/ shows only secretariat@; the only WhatsApp element is the community updates channel.
- Exa 1 Oct 2026: the 2025 page lists 9818274383 for delegates and 8860651641 for speaking, no sponsorship or awards number, staffing unconfirmed.
- The site already collects leads through forms (GA4 Jul-Sep 2026: form_submit 395 events / 251 users, partnership_form_submit 391 events / 298 users), so the gap is speed of answer, not the absence of a channel; Cypher's /tickets page shows 'Questions? Contact our team' and 'Dedicated WhatsApp Support'.

**Expected effect:** No traffic effect. Converts visitors who already have intent but need an invoice, PO or group answer before paying, when email adds a day per reply with the event two weeks out. Lead count not quantified; contact_click in GA4 will show usage within days.

**Owner:** Marketing (numbers, staffing) + web dev Dev A + the three desks  
**Effort:** S: web dev 1 h; marketing 30 min; desk staffing until 17 Oct  
**By:** 4 Oct 2026 (with the ribbon bar); numbers confirmed by 3 Oct  
**Assets:** A04

**Decisions needed**

- Which numbers to publish for each of the three lines and who answers them 9 am to 8 pm, including on 2 Oct and the weekend

### 11. F1 (merges F1 + G5 share kits): Turn the LinkedIn showcase, a LinkedIn Event and the 50 confirmed speakers into a /delegate/ channel, with a share kit before and after each session

**Do this**

- Showcase admin (linkedin.com/showcase/world-ai-summit/) by 3 Oct: rewrite the tagline and the first 300 characters of About (it still says '2nd Edition' and 'Stay tuned for ... registrations'); set the Website field and the custom 'Register' button to https://www.worldaisummit.com/delegate/?utm_source=linkedin&utm_medium=social&utm_campaign=world_ai_summit_2026_delegate&utm_content=showcase_button (the one scheme from move 2; the merged file's wais2026 variant is replaced); settle PLACEHOLDER_EDITION_NUMBER (About says 2nd, posts since July say 3rd) and use it everywhere.
- Create a LinkedIn Event 'World AI Summit 2026, Bengaluru' (in person, 14-15 Oct 2026, Sheraton Grand Bangalore Hotel at Brigade Gateway) with external registration to /delegate/ plus utm_content=li_event, live by 4 Oct; first check in the admin UI that a showcase page can host an Event with an external link; invite followers and ask every confirmed speaker and exhibitor to share it.
- From today to 15 Oct, end every post with 'Book your delegate pass' and the /delegate/ UTM link instead of 'Express your interest: lnkd.in/...' (first check where the lnkd.in links go); sponsor and exhibitor posts add 'Exhibit or sponsor: partnerships@worldaisummit.com'; 1-2 posts add 'Nominate for the World AI Awards' with /awards/. Pin one post naming the pass tiers at PLACEHOLDER_CURRENT_PASS_PRICE, the 10% group discount for 3+ delegates and the three contact emails.
- By 3 Oct secretariat@ emails each of the 50 confirmed speakers (speakers.json confirmed_2026: true) their live https://www.worldaisummit.com/assets/speaker_details/<slug>.html URL, a request to check role and bio, LinkedIn copy with utm_source=linkedin&utm_medium=speaker_share&utm_campaign=world_ai_summit_2026_delegate&utm_content=<slug> and the existing 'We welcome X as a speaker' card; for government officers ask their department handles. Check og:image on the live pages first (the repo config has an empty og_image). The bio-page link ask stays optional only.
- Daily speaker-countdown post 2-13 Oct tagging 3-4 speakers each, linking their pages with UTMs, prioritised by pass-buyer fit: BFSI (Tulshekar Gangireddy, JPMorgan; Deepak Mohanty, Wells Fargo; Deepika Sandeep and Shireen Ali, HSBC; Vijaya Kadiyala, DBS; Shantanu Dasgupta, Axis; Vishal Chugh, Tata Capital), Retail (Sandeep Varaganti and Anand Thakur, Reliance Retail; Suman Guha, Croma; Sandeep Sharma, Shoppers Stop), Ecosystem (Shalini Kapoor, EkStep; Sandhya Vasudevan, TiE Bangalore; Shashank Randev, 247VC; Sanjeev Gupta, KDEM).
- Keep the live /assets/speaker_details/<slug>.html URLs until after 17 Oct; do not deploy the repo's /speakers/<slug>/ build before the event. 13 Oct: pre-event kit to all speakers, exhibitors and partners (A71, A44). 14-15 Oct: WAIS and Elets posts tag each speaker with the speaker-page URL plus UTM, not lnkd.in; within 24 hours of each session send the speaker a captioned stage photo and one approved verbatim quote card deep-linked to /agenda/#<session-id>; 16-17 Oct thank-you email with ready LinkedIn copy.
- Track utm_source=linkedin and utm_medium=speaker_share in GA4 and compare /delegate/ sessions and generate_lead for 2-17 Oct against the September daily average.

**Why**

- The LinkedIn showcase is #6 organic on 'world ai summit' and #2 on 'world ai summit bengaluru', directly under the homepage at #1 (OpenSEO Google India, 1 Oct 2026); its About says '2nd Edition' and 'Stay tuned for ... registrations' while posts of 15-18 Sep 2026 say '3rd Edition'; followers 4,402 to 4,912 across snapshots; reactions per post about 2-25.
- Speaker pages linked only from the sitemap already rank on page 1: 'sandeep varaganti' #6 (210/mo), 'shashank randev' #7 (90/mo; Cypher's speaker page #2), 'aman mittal ias' #4 (260/mo), 'pankaj kumar pandey' #10 (320/mo); distinctive speaker names total about 1,100/mo.
- WAIS speaker posts (George Inasu 31 Aug, Harsh Vardhan 26 Aug, Suman Guha 10 Sep, Deepak Mohanty 16 Sep 2026) link to lnkd.in, not to speaker pages; 2025 speakers and the WAIS session posts carried no link to worldaisummit.com; Cypher's speakers folder has 93 referring domains.

**Expected effect:** Directional only; no LinkedIn referral baseline exists. The showcase button and post footers could add tens to low hundreds of /delegate/ sessions over 1-17 Oct from people already following the event. If 15-25 speakers post, expect tens to low hundreds of referral visits from senior BFSI, retail and government networks plus a few delegate or group enquiries. Organic gain from speaker-name searches is tens of clicks; bio-page links give nothing in the window.

**Owner:** Marketing (LinkedIn admin, daily posts, quote cards) + speaker secretariat (emails, kits) + photographer on site  
**Effort:** S-M before the event: 1-2 h for showcase, Event and pinned post; 4-6 h for the speaker kit and daily posts. Post-session kits about M across 14-17 Oct  
**By:** Showcase, button, pinned post and speaker emails 3 Oct 2026; LinkedIn Event 4 Oct; countdown posts 2-13 Oct; pre-event kit 13 Oct; post-session kits within 24 h of each session  
**Assets:** A74, A40, A71, A44

**Decisions needed**

- Current pass price and GST wording for the pinned post
- Edition number: 2nd or 3rd
- Where the existing lnkd.in 'Express interest' links point
- Corporate comms clearance for BFSI speakers to post; speaker approval turnaround for quote cards

### 12. G3 (merges G3 + G4 + C4 + G5 speaker-page updates): Build event-week pages on 9-11 Oct, not 13 Oct: winners page skeleton, badges and press kit, 2025 archive banners, and the 15-16 Oct switch of the homepage and /delegate/ to 2027 lead capture

**Do this**

- By 5 Oct: on /1st-edition/delegate-pass.html replace the 2025 purchase form with a banner linking to /delegate/ (keep the URL at 200; or 301 it per move 5); check whether the 2025 checkout still accepts payments. By 12 Oct: archive banner on every /1st-edition/ page ('This is the 2025 archive. World AI Summit 2026: 14-15 Oct 2026, Bengaluru'), a unique title and meta per page (8 share 'World AI Summit 2025'; remove 'Register now & be part of the revolution!'), a short verified recap at the top of /1st-edition/ (25-26 Sep 2025, theme, organiser figures attributed to the Elets wrap-up release), and remove or 301 the 4 /1st-edition/ URLs that return 302 (A72). Do not rename /1st-edition/. /1st-edition/awards.html stays live (it is the '2025 edition' link from /awards/).
- By 6 Oct decide PLACEHOLDER_2025_WINNERS_LOCATION (a new /awards/winners-2025/ or a section on /1st-edition/awards.html, which is why that page is kept out of the redirect map) and publish the full official 2025 list from Elets records; the 10 Oct 2025 LinkedIn post names only five winners.
- 9-10 Oct (Dev A; web dev is otherwise idle on 10-11 Oct and 13 Oct is overloaded): winners page skeleton at PLACEHOLDER_WINNERS_URL (recommended https://www.worldaisummit.com/awards/winners-2026/) with the 6 category groups and one row per award (group, category, winning organisation or person, project name exactly as on the nomination form, city), an id anchor per row, space for a captioned stage photo and the jury list where available; no bios. Design 'Winner - World AI Awards 2026' and 'Finalist' badges (PNG/SVG, carrying 'World AI Summit, Bengaluru') at /assets/images/awards/ and a one-page press kit at /awards/press-kit/ (noindex is fine): badge files, embed code, a press-release paragraph template, a LinkedIn caption and logo rules (A64, A68, A44). Badges and kit copy in design on 9 Oct, live by 11 Oct.
- 10-11 Oct: prepare the post-event hero and the 2027 forms (not live): 'Thank you, Bengaluru' hero carrying Highlights (the /agenda/ hub), Winners, 'Register interest for World AI Summit 2027' (name, email, company, interest attend / sponsor / speak / nominate) and 'Partner in 2027: get the partnership deck first' routed to partnerships@; show Highlights and Winners only if those pages are live. Switch at PLACEHOLDER_SWITCH_TIME (19:00 IST on 15 Oct per F78; 17 Oct after the highlights phase per F51). Keep the homepage <title> as World AI Summit 2026; keep /delegate/ live at 200 with the pass purchase replaced by the 2027 interest form and a recordings link; never 404 or redirect either URL. Add the same 2027 line to speaker pages and /awards/. This leaves 13 Oct for the final agenda and the indexing push only.
- Ceremony night (14 or 15 Oct, to confirm): the awards team supplies the signed-off results sheet the same evening; publish within PLACEHOLDER_PUBLISH_WINDOW (findings say 1 hour, 2 hours or by 23:00 IST); switch the /awards/ title to the Winners variant, add a top banner link, change the homepage awards block to 'Winners announced', add a 'World AI Awards 2027: register interest to nominate' form on both pages; Elets editorial publishes 'World AI Awards 2026: full list of winners' the same night or next morning with the link in paragraph 1; Elets LinkedIn posts the full list with the link the same night (in 2025 this took 15 days).
- By 10:00 IST the next morning the awards team emails every winner the kit, their photos and their row's deep link, and asks for the link in newsroom posts (the 2025 Qualitrix release carried no link to worldaisummit.com). Optional before the event: send finalists the Finalist badge with a CTA to book passes for their team with the 3+ group discount.
- By 16-17 Oct replace 'Session title, time and hall will be published on this page once the agenda is final' on the 50 live speaker pages with the real session title, format, hall, date, photo and video link [PLACEHOLDER: hand-edit /assets/speaker_details/ or change the generator's speakers_path and template before a rebuild]; fix pages still framed as 2025 (priyank-kharge.html title 'Chief Guest | World AI Summit 2025'); link the speaker pages from /speaker.html and the hub.

**Why**

- GSC non-www: after the 25-26 Sep 2025 event, daily impressions fell from about 46 to 1-6 within two days; 'world ai summit' fell from 1,600 (Sep 2025) to 320 (Oct 2025) and 'world ai summit bangalore' from 880 to 40; so the post-event capture is small, but the homepage takes nearly all brand traffic and today shows 'Secure your seat', Rs 20,000 and 10% group booking, which become dead ends on 16 Oct.
- No winners page has ever existed on worldaisummit.com; 2025 winners appeared only in a LinkedIn post on 10 Oct 2025, 15 days after the ceremony; 2025 winner posts (Senthil Bhardwaj 27 Sep, Qualitrix 29 Sep 2025) carried no link to the site; 'world ai awards 2025 winners' on Google India 1 Oct: worldawards.ai #1, WAIS /awards #4 with no winners content.
- Audit c1b16b55, /1st-edition/: 11 www URLs return 200 and are orphaned, 4 return 302 while listed in the sitemap, 8 pages share the exact title 'World AI Summit 2025'; /1st-edition/delegate-pass.html is indexable and still sells 2025 passes at Rs 30,000/60,000 a year on.
- speakers.json in the repo: 0 of 76 entries have a session object; the generator writes to /speakers/<slug>/, not the live /assets/speaker_details/<slug>.html, so a plain rebuild would create a second set of URLs.

**Expected effect:** Organic traffic in 14-17 Oct about zero: winners and highlights queries have no measurable India volume and 'world ai awards' collides with worldawards.ai. Referral: tens to low hundreds of visits from winners' and speakers' shares on the night and the next day, provided the pages are live within hours (against zero link targets in 2025). Leads: 2027 delegate, sponsor and nomination interest, probably small given the two-day collapse after the 2025 event, plus a few finalist team passes; it also stops anyone paying for a 2025 pass. Backlinks from winner newsrooms arrive after the window.

**Owner:** Web dev (pages, banners, titles, forms, hero) + awards team (results sheet, winner emails) + marketing (badges, kit, copy) + content (recap, speaker page text) + secretariat + Elets editorial  
**Effort:** M: archive 4-5 h; winners page, badges, kit and emails 12-16 h; switch 3-5 h with forms prepared in advance; speaker pages 3-4 h web dev  
**By:** Pass-page banner 5 Oct 2026; 2025 list 6 Oct; skeleton, badges, kit, hero and forms 9-11 Oct; archive titles and banner 12 Oct; winners live on the ceremony night; kits by 10:00 IST next day; switch at PLACEHOLDER_SWITCH_TIME; speaker pages 16-17 Oct  
**Assets:** A69, A55, A72, A68, A63, A64, A66, A44, A47, A21

**Decisions needed**

- Winners URL (/awards/winners-2026/ or /awards/2026-winners/), publish window, and who signs off the results sheet on the night
- Ceremony date and time; where the official 2025 winners list is published and who supplies it
- Exact post-event switch time; 2027 dates (until known, copy says 'register interest'); dates of the next Elets AI event before any block is added
- Whether the 2025 checkout still accepts payments
- Hand-edit the live speaker pages or change the generator path

## Second tier

- **B2. House ads on the five Elets portals and an indiaaisummit.in funnel** (Elets ad-ops and design (portals) + web dev (indiaaisummit.in); Portal placements 2 Oct 2026 if ad-ops works the holiday, else 5 Oct (live to 15 Oct); indiaaisummit.in 5 Oct; assets A35, A38): From the first working day to 15 Oct place WAIS creatives (728x90, 300x250, 320x100) in the existing header and in-article ad slots on egov, cio, bfsi, ehealth and digitallearning.eletsonline.com (egov referral fell from 4,153 sessions in Jul-Sep 2025, a quarter that included the event, to 27 in Jul-Sep 2026), re-point the egov 'Upcoming Conferences' widget and events.eletsonline.com buttons to /delegate/ with per-portal utm_source and utm_medium=house_ad, add an announcement bar and 'Next Elets AI event' card on indiaaisummit.in by 5 Oct (A38), and redirect or annotate indiaaisummit.in/awards, which still says 'Nominate Now' for 2025; expect low hundreds to about 1,000 referral sessions, not organic.
- **F3. Correct Elets' own event-platform listings and add Luma** (Marketing / registration team (platform logins) + partnerships (GTF exhibitor copy); Eventbrite and GTF 3 Oct 2026; MeraEvents, Townscript, Luma 4 Oct; venue request 6 Oct; assets A32, A30, A31, A24, A78, A19): Eventbrite is mostly right (check two-day dates and PLACEHOLDER_START_TIME); GlobalTradeFairs' three pages say 'Entry: Free' and 'Bengaluru Rural' with empty Schedule and Speakers (fix the main page, unpublish the other two by 3 Oct); MeraEvents shows 2025 'Sold Out' events and Townscript 'EVENT HAS ENDED' (pointer lines or a new 2026 event by 4 Oct, PLACEHOLDER_MERAEVENTS_OPTION); 10times and AllEvents get the decided price the same day as move 1; create a Luma-hosted event; every listing link uses utm_source=<site>&utm_medium=listing&utm_campaign=world_ai_summit_2026_delegate (one scheme, replacing the merged file's world_ai_summit_2026 and wais26 variants); ask the Sheraton Grand sales team for a what's-on listing and a Google Business Profile Event post by 6 Oct; tens of referral visits in total, the gain is removing 'Free' and 'Sold Out' at the moment of purchase.
- **D1. Consolidate the speaker directory and correct speaker pages before anyone shares them** (Web dev + content; Elets secretariat for the Kharge ruling; Kharge and title fixes 2-3 Oct 2026; directory merge 5-6 Oct; assets A39, A11): By the first working day fix the priyank-kharge.html meta and About portfolio to 'Minister for Home (excluding Intelligence), IT-BT and e-Governance, Government of Karnataka' and get the secretariat to settle PLACEHOLDER_KHARGE_2026_STATUS (speakers.json says not confirmed, /speaker.html says 'Welcoming'); give role-led titles to the shared-name pages (Pankaj Kumar Pandey IAS, Sanjeev Kumar Gupta KDEM, Shalini Kapoor EkStep, Harsh Vardhan Apollo Tyres); by 5-6 Oct server-render the 50 confirmed speakers on /speaker.html (124 words today, names one person) with links, give it its own title, meta and H1, and 301 or canonical /assets/speaker_details/index.html to it so one directory competes instead of two (#7 and #11 for 'world ai summit speakers'); trust and conversion fix, not traffic.
- **D4. Fix wrong facts in the five blog posts and the AI-conference landing page, add Bangalore and booking links** (Content + web dev; 5 Oct 2026; assets A13, A50, A25): By 5 Oct replace the non-official seven tracks and '1,200+ delegates' in 'Beyond the Hype' with the 7 official tracks and PLACEHOLDER_DELEGATE_COUNT, change the 'World AI Summit 2025' H2 in 'The Next Chapter of AI', add an end-of-post CTA box (date, venue, PLACEHOLDER_CURRENT_PASS_PRICE, Book pass, Nominate) and 2-3 speaker links to all 5 posts, set /ai-conference-bengaluru-2026.html's title to 'AI Conference Bangalore 2026 | World AI Summit, 14-15 Oct Bengaluru' with 'Bangalore' in the H1 ('ai summit bangalore' 320/mo vs 'bengaluru' 40/mo), add the A25 FAQ additions and link it from the homepage footer or venue block (not the nav); +20 to +80 visits at most.
- **B3. Retrofit the live Elets WAIS articles and the duplicated /blog/ posts** (Elets editorial (CIO, eGov, BFSI desks) + web dev (canonicals, dates, Article JSON-LD); Article edits 5 Oct 2026; canonical decision 9 Oct; assets A36, A49): By 5 Oct replace the closing 'For More Updates, visit: https://www.worldaisummit.com/' in cio.eletsonline.com articles 76367, 76379 and 76296 (and add it to 76373) with the A36 paragraph linking /delegate/, /awards/, the sponsor page and /speaker.html; fix the old track lists in 76367 and 76373 and the 'World AI Summit 2025' subheading in the July egov piece; add a 'Speaking at World AI Summit 2026' box to the Tulshekar Gangireddy, Pankaj Kumar Pandey and Sanjeev Gupta articles; by 9 Oct pick one canonical per duplicated blog pair (4 of 5 WAIS posts are verbatim Elets copies) and stop publishing verbatim copies; a few sessions per article per week, the main value is removing wrong edition and track claims that sponsors can see.
- **B4. Elets editorial plan 5-16 Oct: speaker roundups first, then day-of releases** (Elets editorial desks + partnerships (KDEM) + programme team (track assignments); Roundups 7 Oct 2026; previews 5-12 Oct; PR1 12-13 Oct; PR2 14 Oct night; PR3 16 Oct; assets A43, A37, A48, A70): By 6-7 Oct publish the cio roundup of the 50 confirmed speakers grouped by sector and the egov 'Government leaders at World AI Summit 2026' piece (Pankaj Kumar Pandey, T Bhoobalan, Dr Ravikumar Surpur, Aman Mittal, Hemant Garg, Sanjeev Gupta, Ram Mohan Rao, M Balasubramaniam, Dr Sushil Kumar Meher), every name linked to its speaker page, CTA to /delegate/ with no price and utm_medium=editorial; sector previews 5-12 Oct only with the A37 lines and no track claims (session is null for all 76 entries, PLACEHOLDER_TRACK_ASSIGNMENTS); PR1 curtain-raiser 12 or 13 Oct, PR2 on 14 Oct about 21:00 IST with winners, PR3 wrap-up 16 Oct; settle PLACEHOLDER_EDITION first; ask KDEM to republish PR2 or PR3; link only to URLs live on 1 Oct until /agenda/ ships; tens to low hundreds of referral sessions, lead quality is the value.
- **B5. Brand-only publishing calendar 5-17 Oct with a homepage 'Latest' block (the hub, GSC and sitemap parts of B5 sit in moves 4, 5 and 9)** (Content lead (calendar owner) + web dev (block, sitemap); Block and first items 5 Oct 2026 (3 Oct if the content lead works the weekend); calendar to 17 Oct; assets A45): Run the A45 calendar for brand-modified items only (agenda, speakers, live, highlights, winners), each with a dated byline, at least one contextual link to /delegate/, /agenda/ and /awards/ or the partner page, only confirmed_2026 speakers and no invented quotes; list the 3 newest URLs in a 'Latest from the Summit' block on the homepage (the most-crawled page, #1 for brand) and give each a sitemap lastmod; hand each item's angle to the Elets desks so their piece links to it the same day; low hundreds of extra organic sessions at most, mostly moved off the homepage.
- **F2. Crawlable homepage partner block and a 'Meet us at World AI Summit 2026' kit for the 8 partners and KDEM** (Partnerships (kits, KDEM ask) + web dev (homepage block, sanjeev-gupta page line); Homepage block 5 Oct 2026; kits 5 Oct; KDEM ask 6 Oct; exhibitor push 5-9 Oct; assets A42, A41): By 5 Oct name the 8 announced partners as text links on the homepage (Strategic Partner KDEM; AI & Data Infrastructure Partner WD; AI Impact Partner HIGHTABLE; Bronze Partners Successive Digital and Kagen.ai; Exhibitors RWS, Exatron, indierouter.ai), confirming each domain; by 5 Oct send each partner a kit (booth number, website snippet linking /delegate/, LinkedIn copy with utm_medium=partner_share, customer invite; guest passes only per PLACEHOLDER_GUEST_PASS_POLICY); by 6 Oct ask KDEM for a LinkedIn post, a share by CEO Sanjeev Kumar Gupta and a note to its GCC, startup and Beyond Bengaluru networks (the karnatakadigital.in/events/ listing is low probability, it has not been updated since May 2026); use the named list in a 'last booths' push 5-9 Oct; tens of referral visits per partner, exhibitor leads unquantified.
- **G2. Cypher partner outreach 10-12 Oct and the Bangalore list and calendar pages by 7 Oct** (Partnerships (outreach) + marketing (listings, Luma decision) + content (optional post); Listings and optional post 7 Oct 2026; partner emails 10-12 Oct; assets A54, A73): Re-check the live Cypher 2026 homepage list of 34 Strategic Partners (IBM, Genpact, Dell, Tredence, Google Cloud, Tiger Analytics and others; the Exa copy is cached), then on 10-12 Oct, after Cypher closes on 9 Oct, email each a last-minute WAIS branding, exhibit or GCC-track package (A54) without using the Cypher trademark; by 7 Oct submit the event to conferencealerts.in/bangalore/ai (#4 for 'ai events in bangalore'), thegenerativebeings.com and b2bangalore.com (A73) and decide Luma ticketing (off-platform registration may make the event ineligible for luma.com/bengaluru, #1 for the query); the optional 'AI events in Bangalore, October-November 2026' post only if Elets will name competitor events; +30 to +150 visits combined, plus a few qualified sponsor conversations for 14-15 Oct or 2027.
- **F4. Ask the list pages that already rank for Bangalore and India AI-event queries to add World AI Summit** (Marketing; Requests sent 5-6 Oct 2026; follow-up 8 Oct; assets A33, A28, A19, A76, A24): Check the live Techcanvass 'Top 10 Upcoming Tech Conference In Bangalore' page first (indexed October edition names Cypher-like 'Flagship AI Summit'; whether WAIS is on it is unknown, do not claim 'you already link to us'); ask Digitalconfex (#8 for 'ai conferences 2026 india', lists the finished January Elets event), dev.events (free Add event flow), b2bangalore, Dreamcast, craw.in and the Linux Foundation AI calendar for one entry linking /delegate/ or /ai-conference-bengaluru-2026.html with the listing UTM scheme; send all by 5-6 Oct, one follow-up around 8 Oct, additions after 8 Oct earn almost nothing; tens of visits in total.
- **G6. Elets event-week editorial calendar 12-16 Oct with working links and UTMs** (Elets editorial (briefs in A22, headlines in A77 from content); Kick-off 12 or 13 Oct 2026; Day 1 14 Oct; Day 2 and winners 15-16 Oct; wrap-up 16 Oct; assets A22, A77, A66): Kick-off story on PLACEHOLDER_KICKOFF_DATE (12 or 13 Oct) with anchors to the /agenda/ hub (if live; else the homepage or /ai-conference-bengaluru-2026.html, never a dead URL) and /delegate/; Day 1 and Day 2 reports on 14 and 15 Oct quoting speakers only from the session record (new work: in 2025 Elets ran only two press releases); winners list 15-16 Oct; wrap-up within 24 hours of the close on 16 Oct (3 days in 2025) with the anchor 'Partner with World AI Summit 2027' to the sponsor page; use the site's 7 track names and one delegate figure; UTM every link with utm_medium=editorial (all Elets editorial subdomains sent about 150 sessions and 2 key events in September); tens to a few hundred visits across the week.
- **E3. E3 off-site step (the on-site redirect map and sitemap are in move 5): Elets editorial fixes for off-site WAIS URLs that still redirect to the homepage** (Elets editorial / Elets web team; 5 Oct 2026; assets A57): 301 events.eletsonline.com/aidemo/registration.html (mirrors the homepage, #7 for 'world ai summit bengaluru' with a 'September 2026' snippet) to https://www.worldaisummit.com/delegate/, and update the 2025 cio and egov articles that still link to worldaisummit.com/agenda (5xx until the hub ships) and other dead URLs; small, protective, outside the main site.
- **F5. F5 identity line (the schema, FAQ, Bing and IndexNow parts of F5 are in moves 4 and 8): One-line identity on every surface to keep World AI Summit apart from World Summit AI (Amsterdam, 7-8 Oct)** (Marketing (copy) + listing owners; 5 Oct 2026; assets A75, A76): Use the same line ('World AI Summit 2026, Bengaluru, 14-15 October, by Elets Technomedia') in the LinkedIn About, YouTube descriptions and every listing in F3, F4 and G2 so each source describes the event the same way during Amsterdam's news peak; near zero measurable traffic, protects existing brand clicks from confusion.

## Day by day

### 2026-10-01 (Thu, this evening; added because 2 Oct is a holiday)

- Marketing head, by phone or WhatsApp: price ladder from 1 Oct, next deadline (never reset), GST inclusive or extra (move 1); canonical sponsor URL (move 7); confirm the 10% group discount; whether web dev, desks and ad-ops work on 2 Oct and 3-4 Oct; name the second developer (Dev B) or accept the priority order.
- Awards team: 2026 deadline, fee, ceremony day, WhatsApp number (move 6).
- Marketing (GSC owner): check for an existing www or Domain property; if the registrar or GA4 Edit access is to hand, verify the www property tonight (move 4); 10 minutes of web dev if the meta-tag route is used.
- Email team: confirm whether a 2 Oct send is scheduled and apply the no-price copy and the PLACEHOLDER_FALLBACK rule to it (move 3).
- Programme team: name PLACEHOLDER_AGENDA_DATA_DATE (move 9).

### 2026-10-02 (Fri, Gandhi Jayanti, national holiday)

- If web dev works today (PLACEHOLDER), one developer, about 6 h, in this order and nothing else: (1) /delegate/ expired rows out, current row highlighted, H1 and title (Dev A, 2 h); (2) one-hop 301s for /registration, /registration.html, /delegate-registration.html and the /1st-edition/delegate-pass.html decision (Dev B or same person, 1 h); (3) /awards/ key-facts banner, one-hop awards 301, /award.html canonical and Nominate buttons (1.5 h); (4) GA4 purchase, begin_checkout, generate_lead, noindex /thankyou.html, hostname filter (2-3 h, Dev B, or 3 Oct). If nobody works today, this list is Mon 5 Oct morning and every later date in this table moves by one working day.
- Marketing (GSC owner): www property verified and OpenSEO re-pointed if not done last night (move 4).
- Elets email team: 2 Oct send (if scheduled) deep-linked to /delegate/, /awards/ and the sponsor page with the one UTM scheme, no prices in copy; fallback if /delegate/ is not fixed (move 3).
- Registration and awards desks (if working): pull the unpaid-starter list from forms and Stripe (move 2).
- Elets ad-ops (if working): WAIS creatives into the five portal ad slots; re-point the egov widget (B2).
- Marketing: first speaker-countdown LinkedIn post; check where the lnkd.in links go (move 11).
- Decisions not received by tonight move to the 5 Oct 10:00 fallback; web work that depends on them (homepage price cards, listing prices, FAQ price line, schema offers) waits, everything else does not.

### 2026-10-03 (Sat)

- Dev A (if working; else 5 Oct): full /awards/ rebuild with categories, FAQ, title, JSON-LD (move 6, 2-4 h); homepage hero three buttons, H1, nav and footer, crawlable links, awards block, speaker strip (move 5, half day).
- Dev B (if working; else 5 Oct): GA4 events if not done 2 Oct (move 2); /awards/failed.php and /delegate/success.php panels (move 2, 2 h); register 301s and awards 301 if not done 2 Oct.
- Marketing: WhatsApp numbers assigned (move 10); AllEvents, Eventbrite and GTF listings corrected with the listing UTM scheme (move 1, F3); LinkedIn showcase About, Website field, Register button, pinned post (move 11); Bing Webmaster Tools and IndexNow set up (move 4); Request indexing day 1 for whatever went live: /, /delegate/, /awards/ (move 4).
- Secretariat: email the 50 confirmed speakers their page URL and share copy (move 11).
- Registration and awards desks: first call and WhatsApp sweep within 24 h of the pull (move 2).
- Partnerships: 2026 deck PDF and true remaining-inventory list to web dev (move 7).
- Email team: next send follows the same deep-link rules (move 3).

### 2026-10-04 (Sun)

- Dev A (if working; else 5-6 Oct): homepage meta, key-facts block, FAQ rewrite, Event JSON-LD on the homepage (without offers if the price is still open), /awards Event node repair, validation (move 8, about 5 h); one shared ribbon plus WhatsApp bar (moves 1 and 10, 1 h).
- Dev B (if working; else 5-6 Oct): sponsor page self-canonical, title, benefits, inventory, gated deck, links (move 7, half day).
- Marketing: LinkedIn Event live (move 11); MeraEvents and Townscript pointer lines, Luma-hosted event (F3); daily speaker post; Request indexing day 2 for pages that changed (move 4).
- Content: speaker strip copy and FAQ answers checked against decided facts (moves 5 and 8).

### 2026-10-05 (Mon, hard deadline for business decisions, 10:00)

- Marketing head and awards team: every open decision from 1 Oct closed by 10:00 (price, GST, sponsor URL, deadline, fee, numbers, delegate figure, edition number); web dev then fills the PLACEHOLDERs on /delegate/, the homepage cards, the FAQ, the schema offers and the listings the same day.
- Dev B: legacy redirect map with curl tests, including /agenda > /agenda/ once only and excluding /1st-edition/awards.html; sitemap rebuild (18 removals) and resubmit; non-www href sweep (move 5, 3-4 h). Dev A: /agenda/ holding page with the 7 tracks and TBA cells (move 9); /1st-edition/delegate-pass.html banner (move 12); Organization JSON-LD and Amsterdam FAQ (move 8). If only one developer and no holiday or weekend work happened, today holds the 2 Oct list only, and the 3-4 Oct items run 6-7 Oct, which is the edge of the recrawl window.
- Dev A or content: /speaker.html renders the 50 confirmed speakers and /assets/speaker_details/index.html points to it (D1); blog fact fixes, CTA boxes, /ai-conference-bengaluru-2026.html title and H1 (D4); crawlable homepage partner block (F2); indiaaisummit.in banner and bar (B2, move 8); first 'Latest from the Summit' items (B5).
- Programme team: running order delivered if PLACEHOLDER_AGENDA_DATA_DATE is today (move 9).
- Partnerships: 'Meet us at World AI Summit 2026' kits to the 8 partners (F2); exhibitor 'last booths' push starts, runs to 9 Oct.
- Marketing: list-page outreach emails sent (F4); daily speaker post; one-line identity sent to all listing owners (F5); Request indexing for everything that changed (move 4).
- Elets editorial: retrofit cio 76367, 76379, 76296, 76373 and the July egov piece (B3); off-site 301 of events.eletsonline.com/aidemo/registration.html and 2025 article link fixes (E3 off-site); 'nominations close' story if nominations are open (move 12).
- Elets web team: elets.net/worldaisummit-awards/ update or 301 (move 6).

### 2026-10-06 (Tue)

- Registration and awards desks: second call sweep (move 2).
- Dev A: /agenda/ v1 with sessions if the running order arrived (move 9); 2025 winners list published at PLACEHOLDER_2025_WINNERS_LOCATION (move 12). Dev B: anything slipped from 2-5 Oct, in the same priority order.
- Partnerships: KDEM ask for LinkedIn post, CEO share and network note (F2); venue listing request to the Sheraton Grand sales team (F3).
- Elets editorial: cio speaker roundup published, names linked to speaker pages (B4).
- Marketing: daily speaker post; Request indexing for any changed URL (move 4).

### 2026-10-07 (Wed)

- Analytics: first review of purchase, generate_lead by form_type and contact_click by source/medium; decide final mailer segments (moves 2 and 3).
- Dev A: /agenda/ v1 live at the latest, linked from nav, hero section and 'Latest' block, indexing requested (move 9); last realistic day for Google-dependent changes (meta, schema, awards title) to ship and still be recrawled before event week; rank and SERP check on 'ai summit 2026', 'ai events in bangalore', 'world ai awards', 'ai awards 2026' (measurement).
- Elets editorial: egov 'Government leaders at World AI Summit 2026' roundup (B4); sector previews continue to 12 Oct.
- Marketing: conferencealerts.in, thegenerativebeings, b2bangalore submissions; Luma ticketing decision (G2); daily speaker post.
- Email team: mid-week send with the /agenda/ link added once live (move 3).
- Cypher runs 7-9 Oct at KTPO Whitefield: no action, note for 10 Oct outreach.

### 2026-10-08 (Thu)

- Dev A: /agenda/ hub complete with session anchors and Event JSON-LD (move 9). Dev B: check /awards consolidation in URL Inspection (move 4).
- Partnerships: last realistic day to close sponsor and booth leads for 14-15 Oct; final push with the named partner list (moves 7, F2).
- Marketing: one follow-up to list pages (F4); daily speaker post.
- Content: agenda PDF (if gated) ready for the sales desk to start calls (move 9).

### 2026-10-09 (Fri)

- Dev A: winners page skeleton at PLACEHOLDER_WINNERS_URL started (move 12). Marketing and design: Winner and Finalist badges and press kit copy in design (move 12).
- Dev B and Elets editorial: canonical decision on the four duplicated blog posts implemented (B3); /agenda/ in sitemap and nav on every page (moves 5 and 9).
- Marketing: daily speaker post; listing checks in a real browser (F3).
- Email team: send to segments chosen on 7 Oct (move 3).

### 2026-10-10 (Sat)

- Registration and awards desks: third call sweep (move 2).
- Dev A: winners skeleton finished; press kit page at /awards/press-kit/ built; post-event hero and the 2027 interest and partner forms built but not live (move 12).
- Partnerships: Cypher partner outreach begins, runs to 12 Oct (G2).
- Dev B: Request indexing for /, /delegate/, /agenda/ after updates (move 4).
- Marketing: daily speaker post.

### 2026-10-11 (Sun)

- Dev A: badges live at /assets/images/awards/, press kit complete, /delegate/ 2027 form prepared, 2027 line prepared for speaker pages and /awards/ (move 12).
- Partnerships: Cypher partner outreach continues (G2).
- Content: live-desk templates, Highlights variant, post-event hero copy and Elets winners story template drafted (moves 9 and 12).
- Marketing: daily speaker post.

### 2026-10-12 (Mon)

- Dev B: archive banner, unique titles and recap on every /1st-edition/ page; 4 302ing archive URLs removed or 301'd; /1st-edition/awards.html kept live (move 12).
- Elets editorial: kick-off story if PLACEHOLDER_KICKOFF_DATE is 12 Oct, anchors only to live URLs (G6, B4 PR1).
- Partnerships: last Cypher partner emails (G2).
- Email team: 'this week' send to /delegate/ (move 3).
- Marketing: daily speaker post; final listing checks.

### 2026-10-13 (Tue)

- Dev A: final /agenda/ with halls (move 9) and nothing else new; /awards/ title swapped to the closed variant if PLACEHOLDER_DEADLINE is today (move 6).
- Dev B: final Request indexing push (move 4); dry run of the winners publish and the hero switch on staging.
- Secretariat: pre-event share kit to all 50 speakers, exhibitors and partners (move 11).
- Analytics: second review of purchase and generate_lead by source; last mailer segments (moves 2 and 3).
- Email team: last pre-event send (move 3).
- Elets editorial: PR1 curtain-raiser if 13 Oct (B4, G6).
- Content: two live-desk people briefed; quote approval process agreed (move 9).

### 2026-10-14 (Wed, Day 1)

- Content: 08:00 IST switch /agenda/ to the Live variant; updates every 30-60 min with verbatim quotes and photos; homepage hero link 'Live now: Day 1 updates' (move 9).
- Marketing and Elets LinkedIn: speaker posts tagging each speaker with the speaker-page URL plus UTM, not lnkd.in (move 11).
- Awards team: results sheet signed off on the night if the ceremony is Day 1; winners page live within PLACEHOLDER_PUBLISH_WINDOW; /awards/ title and homepage block switched (move 12).
- Elets editorial: Day 1 report; PR2 about 21:00 IST with winners if Day 1 ceremony (B4, G6).
- Desks: WhatsApp lines staffed 9 am to 8 pm with on-spot registration answers (move 10).
- Dev B: Request indexing of /agenda/ after the live switch (move 4).

### 2026-10-15 (Thu, Day 2)

- Content: live updates continue on /agenda/ (move 9).
- Awards team: winners page live if the ceremony is Day 2; winner kits prepared; by 10:00 IST next day emails go out (move 12).
- Dev A: at PLACEHOLDER_SWITCH_TIME (19:00 IST per F78, or 17 Oct per F51) switch the homepage hero to 'Thank you, Bengaluru' with Highlights, Winners, 2027 interest and 2027 partner CTAs; /delegate/ stays at 200 with the 2027 form (move 12).
- Secretariat: post-session photo and quote cards to Day 1 speakers within 24 hours (move 11).
- Elets editorial: Day 2 report; winners list story with the winners page link in paragraph 1 (G6, move 12); Elets LinkedIn full winners list the same night.
- Desks: lines staffed; post-event 'what happens next' answers ready (move 10).

### 2026-10-16 (Fri)

- Dev A: 12:00 IST switch /agenda/ to the Highlights variant with the recordings form and 2027 interest box (move 9); begin session details on the 50 live speaker pages (move 12). Dev B: Request indexing of /, /agenda/, /awards/ and the winners page (move 4).
- Awards team: winner kit emails by 10:00 IST with row deep links; ask for newsroom links (move 12).
- Email team: post-event send with PLACEHOLDER_POST_EVENT_PRIMARY_CTA, no pass CTA (move 3).
- Elets editorial: PR3 wrap-up within 24 hours linking Highlights, Winners and the sponsor page with 'Partner with World AI Summit 2027' (B4, G6).
- Partnerships: ask KDEM to republish PR2 or PR3 (B4).
- Secretariat: post-session kits to Day 2 speakers (move 11).

### 2026-10-17 (Sat)

- Dev A: finish speaker page session details and the 2027 line on speaker pages and /awards/ (move 12); homepage switch if PLACEHOLDER_SWITCH_TIME is 17 Oct.
- Secretariat: thank-you emails with session pages, photos and LinkedIn copy (move 11).
- Analytics: window readout 2-17 Oct: purchases by source/medium against the Stripe dashboard, generate_lead by form_type, contact_click, mailer sends by utm_content, referral by utm_source, GSC www clicks for /, /delegate/, /awards/, /agenda/, paid nominations from the awards team, calls made and passes recovered per sweep (measurement).
- Desks: final day of staffed lines; log open invoice and PO requests for follow-up (move 10).

## By owner

### Marketing head

- 1 Oct evening (fallback 5 Oct 10:00): price ladder from 1 Oct, next deadline (never reset), GST inclusive or extra (move 1)
- 1 Oct evening: canonical sponsor URL, /partnership.html or /partner-with-us.html (move 7)
- 1 Oct evening: whether web dev, desks and ad-ops work on 2 Oct (Gandhi Jayanti) and 3-4 Oct; name the second developer (Dev B) or accept the priority order
- By 5 Oct: single delegate figure (1,000+ or 1,200+), edition number (2nd or 3rd), speaker count claim, confirm the 10% group discount
- By 5 Oct: homepage title decision (keep or 58-char variant) and meta draft (A17 or A26) (move 8); KDEM 2026 wording, no-affiliation confirmation for the Amsterdam FAQ, India AI Impact Summit answer
- Decide optional paid items: Google Ads 9-14 Oct, paid wire for PR2, BookMyShow or District listings

### Web dev Dev A (pages)

- First working day (2 Oct if working, else 3 or 5 Oct): /delegate/ rows, H1, title; /awards/ banner, /award.html buttons; homepage awards block
- 3 Oct (or next working day): /awards/ rebuild; homepage hero, H1, nav, footer, crawlable links, speaker strip
- 4 Oct: homepage meta, key facts, FAQ, Event JSON-LD, /awards Event fix; one ribbon plus WhatsApp bar
- 5 Oct: /agenda/ holding page; Organization JSON-LD; 2025 pass page banner; /speaker.html merge; blog and AI-conference page fixes; partner block; fill PLACEHOLDERs once decisions land
- 6-8 Oct: /agenda/ v1 then full hub with anchors, JSON-LD, links and 'Latest' block
- 9-11 Oct: winners skeleton, press kit, badges live, post-event hero and 2027 forms prepared; 13 Oct final agenda only
- 14-17 Oct: live and highlights phase switches on /agenda/; winners page publish; homepage and /delegate/ switch at PLACEHOLDER_SWITCH_TIME; speaker page session details

### Web dev Dev B (redirects, GA4, schema, sitemap) [PLACEHOLDER: second developer or agency; if none, Dev A runs both lists in the stated priority order]

- First working day: one-hop 301s for the register URLs and non-www /awards; /award.html canonical; GA4 purchase, begin_checkout, generate_lead, noindex /thankyou.html, hostname filter
- 3 Oct: /awards/failed.php and /delegate/success.php panels; checkout.stripe.com referral exclusion
- 4 Oct: sponsor page (self-canonical, title, benefits, inventory, gated deck, links)
- 5 Oct: legacy redirect map with curl tests (one /agenda > /agenda/ hop; /1st-edition/awards.html excluded); sitemap rebuild (18 removals) and resubmit; non-www href sweep; indiaaisummit.in banner
- 9 Oct: blog canonicals; 12 Oct: /1st-edition/ archive titles and banner, 302ing archive URLs
- 3-13 Oct and 16 Oct: Request indexing after each deploy; IndexNow pings; URL Inspection check on /awards consolidation 8 Oct

### Marketing (GSC, listings, LinkedIn, WhatsApp lines)

- 1-2 Oct: www or Domain Search Console property; re-point OpenSEO; 3 Oct Bing WMT and IndexNow; daily Request indexing from the first deploy to 13 Oct and 16 Oct
- 3 Oct: assign and staff the three WhatsApp/call lines 9 am to 8 pm until 17 Oct
- 3-4 Oct: AllEvents, Eventbrite, GTF, MeraEvents, Townscript, 10times, Luma listings with the decided price and the one UTM scheme (utm_source=<site>, utm_medium=listing, utm_campaign=world_ai_summit_2026_delegate); venue request by 6 Oct
- 3-4 Oct: LinkedIn showcase About, Website, Register button, pinned post, LinkedIn Event; daily speaker-countdown posts 2-13 Oct; event-week posts with speaker-page URLs
- 5-8 Oct: list-page outreach and one follow-up; conferencealerts, thegenerativebeings, b2bangalore submissions by 7 Oct; Luma ticketing decision
- 9-11 Oct: badges, press kit copy, 2027 hero copy; 14-17 Oct quote cards

### Elets email/marketing team (ESP)

- 2 Oct send (if scheduled) and every send to 13 Oct: primary CTA to /delegate/, awards to /awards/, sponsor to the canonical sponsor page; the one UTM scheme; ESP auto-UTM off; A34 QA before each send
- Keep price, fee, discount, deadline and seats-left out of copy until confirmed
- Check link-scanner hits on r.emails.elets.in with the ESP; report on engagement > 0 segment
- 16 Oct post-event send with PLACEHOLDER_POST_EVENT_PRIMARY_CTA and no pass CTA

### Registration desk

- First working day (2 or 3 Oct): pull unpaid /delegate/ starters since 1 Aug from forms and Stripe
- Within 24 h of the pull, then 6 and 10 Oct: call and WhatsApp sweeps with payment link, group offer, invoice or PO option
- 3-17 Oct: staff the 'Book passes' WhatsApp line; answer GST invoice, PO, group and 'what do I pay now?' questions
- 7-13 Oct: call named leads from the gated agenda PDF if PLACEHOLDER_GATE_PDF is yes

### Awards team / awards desk

- 1 Oct evening (fallback 5 Oct): 2026 deadline (date and time IST), fee, ceremony day and time, jury wording, WhatsApp number, FAQ answers (delegate pass included, multi-entry rule)
- 3, 6 and 10 Oct: call everyone who reached /awards/failed.php
- By 6 Oct: supply the official 2025 winners list from Elets records and decide PLACEHOLDER_2025_WINNERS_LOCATION
- Ceremony night: signed-off results sheet; winners page live within PLACEHOLDER_PUBLISH_WINDOW; swap /awards/ title on deadline day
- By 10:00 IST next morning: winner kit emails with deep links; ask for newsroom links; report paid nominations (not GA4 form_submit)

### Partnerships team

- 2-3 Oct: confirm a 2026 deck PDF, true remaining inventory, KDEM year wording, named contact with phone or WhatsApp; staff the 'Sponsor / exhibit' line
- 5 Oct: partner kits to the 8 partners; 5-9 Oct 'last booths' push; 6 Oct KDEM ask (LinkedIn post, CEO share, network note); check whether the Karnataka E-IT-BT department has a 2026 role
- By 8 Oct: close what can be closed for 14-15 Oct (booth lead times)
- 10-12 Oct: Cypher partner outreach (re-check the live list first)
- 16 Oct: KDEM republish ask for PR2 or PR3; 2027 deck-first enquiries from the post-event hero

### Elets programme team

- 1 Oct: name PLACEHOLDER_AGENDA_DATA_DATE; running order with sessions, times, halls and speakers by then (no later than 6-7 Oct)
- Speaker-to-track assignments before any track framing is published by editorial
- Final halls and times by 13 Oct; session data into speakers.json in parallel

### Content team / content lead

- First working day: Kharge page corrections; first 'Latest from the Summit' items; A45 brand-only calendar owner to 17 Oct
- 3-4 Oct: key-facts block, FAQ copy, buyer FAQ on /delegate/, awards FAQ and judging copy, speaker strip
- 5 Oct: blog fact fixes and CTA boxes; /speaker.html directory copy
- 6-13 Oct: /agenda/ daily updates; live-desk templates; Highlights draft; 2027 hero copy; 2025 archive recap
- 14-16 Oct: two people on site for live updates; Highlights by 12:00 IST 16 Oct; speaker page session text by 16-17 Oct

### Elets editorial desks (CIO, eGov, BFSI, eHealth, Digital Learning)

- 5 Oct: retrofit live WAIS articles with the A36 closing paragraph and correct tracks; 'nominations close' story if open; speaker boxes on the Gangireddy, Pandey and Gupta articles; 301 events.eletsonline.com/aidemo/registration.html; fix 2025 article links to dead URLs
- 6-7 Oct: cio speaker roundup and egov government-leaders roundup; sector previews 5-12 Oct without track claims; 9 Oct canonical sign-off on duplicated posts
- 12 or 13 Oct kick-off story; 14 Oct Day 1 report and PR2 about 21:00 IST; 15 Oct Day 2 report; winners list story on the ceremony night; 16 Oct wrap-up within 24 hours; UTM on every link (utm_medium=editorial), only live URLs

### Elets ad-ops, design and Elets web team

- 2 Oct if working, else 5 Oct: WAIS creatives (728x90, 300x250, 320x100) live in the five portal ad slots to 15 Oct, BFSI creative on bfsi, policy creative on egov, per-portal utm_source and utm_medium=house_ad; re-point the egov widget and events.eletsonline.com buttons to /delegate/
- 5 Oct: elets.net/worldaisummit-awards/ updated to 2026 with a link to /awards/ or 301'd
- 5 Oct: indiaaisummit.in announcement bar and card; redirect or note on indiaaisummit.in/awards
- 9-11 Oct: Winner and Finalist badge design

### Speaker secretariat

- First working day: settle PLACEHOLDER_KHARGE_2026_STATUS
- 3 Oct: email the 50 confirmed speakers their page URL, role check, share copy with the speaker_share UTM and card
- 13 Oct: pre-event share kit to speakers, exhibitors and partners
- 14-16 Oct: post-session photo and quote card within 24 hours; 16-17 Oct thank-you emails with session pages

### Analytics

- First working day: record baselines (GSC /awards 32 clicks / 1,300 impressions / pos 7.9; GA4 mailer sessions at both run-rates, /delegate/ views and form submits, success.php users, partnership_form_submit users, organic homepage landings)
- 7 Oct and 13 Oct: purchase, generate_lead by form_type and contact_click by source/medium; mailer segment recommendation
- 17 Oct: full window readout against the baselines and the Stripe dashboard

## Decisions needed from the business

- Tonight, 1 Oct, because 2 Oct is Gandhi Jayanti and 3-4 Oct a weekend: pass price charged from 1 Oct and the exact deadline for the next step (never reset); whether Rs 20,000 / 35,000 / 30,000 / 60,000 include 18% GST; canonical sponsor URL; 2026 awards deadline, fee and ceremony day. Anything not decided tonight has Mon 5 Oct 10:00 as the hard deadline, and the web pages carry PLACEHOLDERs until then.
- Staffing over the holiday and weekend: whether the web developer, the registration and awards desks, ad-ops and the content lead work on 2, 3 and 4 Oct; who the second developer (Dev B) is; if neither is available, the plan accepts that Google-dependent changes ship 5-7 Oct rather than 3-4 Oct.
- Pass commercials: optional tiered group discounts and a 1-day pass; answers to the buyer FAQ (GST invoice, transfer, refund, on-spot registration, lunch, certificate).
- Sponsor page: whether a 2026 partnership deck PDF exists and can be gated; which inventory is genuinely unsold for 14-15 Oct; a named partnerships contact with phone or WhatsApp.
- World AI Awards 2026: fee as one or two tiers, '+ GST' or inclusive (must match or replace 'from 30k + GST'); ceremony time; whether a delegate pass is included; multi-entry rule; jury names or process-only wording; awards WhatsApp number; whether /award.html becomes a 301; elets.net/worldaisummit-awards/ update or 301; winners URL and publish window; where the 2025 winners list lives (new page or a section on /1st-edition/awards.html, which is why that page stays live); who signs off results on the night.
- Access: who holds DNS or registrar access and Search Console ownership; whether a www or Domain property already exists under another Google account; who has Edit on GA4 property 490291049; who owns the mailer platform templates.
- Server stack (Apache or nginx) and where the current /registration 302 rule lives; whether /1st-edition/delegate-pass.html is redirected or kept with a banner (banner recommended); whether the 2025 checkout still accepts payments.
- Payments and forms: whether form data is stored before the Stripe redirect and whether an unpaid entry is really 'saved'; whether the forms submit by AJAX or full post; approval of invoice/PO and NEFT/UPI payment for recovery calls; consent wording if Stripe abandoned-cart emails are switched on.
- Phone numbers for the three WhatsApp/call lines (passes, sponsor/exhibit, awards) and who answers them 9 am to 8 pm until 17 Oct, including 2-4 Oct.
- Programme team: the date by which a near-final running order can be supplied; speaker-to-track assignments; gate the agenda PDF or not; one hub URL (/agenda/ recommended); who staffs the live desk and approves quotes.
- Facts to fix once everywhere: delegate figure (1,000+ or 1,200+), edition number (2nd or 3rd), speaker count (50 confirmed vs '100+'), KDEM partnership year wording, event start and end times, venue street address, whether the Karnataka E-IT-BT department has a 2026 role, guest-pass policy for partners.
- Priyank Kharge's 2026 status (speakers.json says not confirmed; /speaker.html says 'Welcoming').
- Homepage title: keep the current 64-character title or ship the 58-character variant; which meta draft (A17 or A26); approved wording for the India AI Impact Summit question; confirmation that Elets has no affiliation with World Summit AI (Amsterdam).
- Post-event: exact switch time (19:00 IST 15 Oct or 17 Oct); 2027 dates and venue (until known, 'register interest'); dates of the next Elets AI event before any block is added; primary CTA for the 16 Oct mailer.
- Elets editorial: which domain holds the canonical for each duplicated article; whether desks commit to Day 1 and Day 2 reports; kick-off story date (12 or 13 Oct); whether to name competitor events on the WAIS blog; KDEM agreement to republish a release; whether a paid India wire is funded.
- Listings and paid: MeraEvents option (new 2026 event under its ticketing terms or pointer line only); Luma ticketing or a standalone page; BookMyShow or District at their commission; a small Google Ads campaign 9-14 Oct (paid, outside organic scope); which last-minute package to offer Cypher's partners.
- LinkedIn: where the existing lnkd.in 'Express interest' links point; corporate comms clearance for BFSI speakers to post; speaker approval turnaround for quote cards; redirect or note on indiaaisummit.in/awards; whether to deploy the /speakers/ generator after 17 Oct with 301s.

## Traffic outlook

- Baseline (measured): google/organic 5,393 sessions in Jul-Sep 2026, about 60 a day; Organic Search 3,082 sessions in 3-30 Sep (+128.6% on the prior 28 days), of which the homepage took about 2,446 landings. Estimate: a plain continuation gives roughly 1,500-2,000 organic sessions over 1-17 Oct before any uplift; www Search Console data does not exist yet, so this is inferred from GA4.
- Event-week brand spike is the one organic surge (measured demand: 'world ai summit' 1,600 searches in Sep 2025, 320 in Oct 2025; 'world ai summit 2026' 480 in Aug 2026 and rising). Brand queries are already #1, so the gain is routing those clicks to /delegate/, /agenda/ and /awards/ rather than new sessions. Estimate: low hundreds of extra organic sessions from brand-modified pages (agenda, live, highlights, speakers) over 12-17 Oct, mostly moved off the homepage.
- 'ai summit 2026' cluster (measured run-rate 6,600/mo, about 3,000-4,000 searches in the window): at #7 with 3-4% CTR the homepage gets about 140 clicks today. Estimate: a sharper title and meta +20 to +60 clicks; a move to #4-5 would add +150 to +250 but is uncertain, and most of these searchers want the February Government summit. Lever: move 8, shipped by 4-5 Oct (7 Oct at the outside) and recrawled via move 4; if the holiday and weekend are lost and nothing ships before 6-7 Oct, assume the low end or zero.
- Awards (measured): /awards baseline about 19-20 clicks over 1-17 Oct at 32 clicks per 28 days; most from outside India. Estimate: +3 to +25 extra clicks after recrawl from the rebuilt page and distinct title; reaching the top 3 for 'ai awards 2026' or 'ai awards india' in two weeks is possible but not likely. Lever: move 6.
- Google Events panel (unknown, directional): if Google picks up the homepage Event markup by about 7 Oct, a few dozen to low hundreds of clicks over 7-17 Oct on the five Bangalore discovery queries (about 4,700 searches/mo combined); near zero if recrawl takes longer. AllEvents already feeds the index, so the realistic win is the official site appearing as the ticket source, not first entry. Lever: move 8.
- Bangalore list pages, listings and calendars (estimate): tens of referral visits in total from Techcanvass, Digitalconfex, dev.events and similar; +30 to +150 combined with the conferencealerts, Luma and Eventbrite work; these are referrals, not rankings.
- Referral dwarfs organic and is where the window is won (measured base): mailers were about 92% of sessions; at the Jul-Sep rate (about 2,870 a day) 1-17 Oct brings roughly 45-50k mailer sessions, at the September rate (about 7,500 a day) roughly 120-130k; Elets portal house ads low hundreds to about 1,000 sessions (estimate; egov averaged about 45 sessions a day over Jul-Sep 2025, a quarter that included the event, so the near-event rate is unknown); LinkedIn and speaker shares tens to low hundreds (estimate, no baseline). Each 0.1 percentage point of mailer conversion is worth roughly 45-50 form submits at the quarter rate or 120-130 at the September rate, more than every organic lever combined.
- What cannot move by 17 Oct: 'ai conferences 2026 india' (Cypher #1, aggregators), 'priyank kharge' (49,500/mo), generic news topics, and worldsummit.ai's hold on 'world ai summit agenda' #1. Honest total: roughly +100 to +500 extra organic sessions across all levers over the window (estimate), against conversion fixes that touch tens of thousands of mailer sessions and the unknown number of pass buyers currently stopped by a contradictory price page.

## Measurement

- Record baselines on the first working day before anything ships: GSC non-www /awards 32 clicks, 1,300 impressions, position 7.9 (31 Aug-28 Sep 2026); GA4 mailer sessions at both run-rates (Jul-Sep average about 2,870 a day from 263,703; September alone 224,681, about 7,500 a day; A3 also quotes 213,013 for Jul-Sep from F17, so note which figure the report uses); /delegate/ form submits in September (286 per F00 or 178 form_submit events per F02; pick one method and keep it); /delegate/success.php users (18 in all of Jul-Sep); partnership_form_submit users (about 48 a month on /partnership.html; 117 events / 97 users 1 Aug-30 Sep by landing page, 153 per the session-landing count); organic homepage landings (2,446 sessions in 3-30 Sep, about 87 a day, 53 key events, about 2.2%, not the 1.92% printed in the merged file); live positions: 'ai summit 2026' #7, 'ai events in bangalore' #9, 'world ai awards' #2, 'ai awards 2026' #4, 'world ai summit 2026 agenda' #3, 'world ai summit speakers' /speaker.html #7.
- Sales: GA4 purchase (transaction_id, value, INR) by source/medium from the day move 2 ships is the only pass-sales number; reconcile weekly with the Stripe dashboard. Until it fires, treat form_submit as intent, not sales; expect tens of purchases in the window, not hundreds, so do not steer hard on small differences.
- Leads: generate_lead by form_type (delegate, group, sponsor, prospectus, award_nomination, enquiry) by source/medium, read on an engagement time > 0 segment and counted as users, not events; sponsor enquiries checked against the partnerships@ inbox or CRM (51 partnership_form_submit events landed on /thankyou.html, so the event over-counts); paid nominations from the awards team, not GA4; contact_click by method and intent for the WhatsApp bar; calls made and passes or nominations recovered per call sweep (first sweep, 6 Oct, 10 Oct).
- Mailers: per send, utm_campaign (world_ai_summit_2026_delegate / world_ai_awards_2026 / world_ai_summit_2026_sponsorship) and utm_content (segment_date) against purchase events or /delegate/success.php views, partnership_form_submit users and /awards/ generate_lead users; ESP report on link-scanner exclusion; conversion compared with the 0.06% Jul-Sep and 0.045% late-September baselines, and volume compared with both daily run-rates.
- Referral, all on the one UTM scheme: utm_source values allevents, eventbrite, globaltradefairs, luma, meraevents, townscript, 10times, techcanvass, devevents, linkedin (utm_content showcase_button, li_event), speaker_share and partner_share by slug, per-portal house-ad sources, Elets editorial UTMs; compare 2-17 Oct /delegate/ sessions with the September daily average.
- Search: once the www property is verified, clicks and impressions for /, /delegate/, /awards/, /agenda/ and the speaker pages, query rows for 'ai summit 2026', 'world ai summit' variants and 'ai awards' variants; URL Inspection to confirm non-www /awards consolidates to www /awards/ and the Events rich result warnings (performer, offers, organizer) clear; Bing WMT index count. Rank checks on 7 and 13 Oct on the six baseline queries plus Google Events panel presence on 'ai events in bangalore' and 'ai conference bangalore 2026'.
- Review points: 7 Oct (shift mailer segments and spend), 13 Oct (final event-week sends), 17 Oct window readout: purchases by channel, leads by form_type, sponsor conversations opened, nominations paid, organic sessions vs the September run-rate, referral by source, and which PLACEHOLDERs are still unresolved. Keep a clean baseline for the 2027 cycle; that is the lasting value of this measurement work.

## Not worth it now

- **Generic news-analysis pieces (GCC hiring, RBI bulletin, sovereign compute, Karnataka AI University) on worldaisummit.com or the Elets portals (A48)**: The top 20 for 'karnataka ai policy' and 'sovereign ai india' (210/mo) are government, media and vendor sites with no event site; not winnable in two weeks and not copied to /blog/; only if a desk has spare capacity after the two speaker roundups.
- **FAQPage JSON-LD added for rich results**: Google retired FAQ rich results for all sites on 7 May 2026; the payoff is visible text that People Also Ask and AI Overviews can quote, so the markup is optional at best.
- **Asking speakers for links from their company or fund bio pages**: Corporate and government pages will not be edited within two weeks and 247vc.in is a fund homepage; the verifier found it produces nothing before 17 Oct. Keep the LinkedIn share ask only.
- **Academic conference-alert directories (conferencealerts.in, conferencealerts.co.in, allconferencealert.com, internationalconferencealerts.com)**: They rank, but WAIS would sit among about 50 'International Conference on...' rows and need editorial approval; only if time remains after the page-1 lists (Techcanvass, Digitalconfex) are done.
- **Newspaper listings (Bangalore Mirror, Deccan Herald Metrolife, The Hindu Bengaluru) for 12-14 Oct**: Leisure readers, no links and almost no overlap with a Rs 30,000 B2B pass; awareness only.
- **Paid India wire for PR2**: Cost, budget and pickup are unknown and 2025 drew no ANI, PTI, ET, The Hindu or Deccan Herald coverage that WebSearch could find (absence not proven); a budget decision, not a plan item.
- **Google Ads campaign 9-14 Oct on 'ai events in bangalore', 'ai conference bangalore', 'ai summit october 2026'**: Paid, outside the organic scope of this plan; left as a marketing decision with the other paid items.
- **BookMyShow and District listings**: Commission and ticketing-terms decisions; BookMyShow is #1 for 'events in bangalore october 2026' but the event sells Rs 20,000-60,000 B2B passes through its own checkout.
- **Deploying the repo's /speakers/<slug>/ generator output before 17 Oct**: The live /assets/speaker_details/ URLs already rank on page 1 for several speaker names and are being shared; a second directory would split them and speakers.json has 0 of 76 session objects. Move after the event with 301s, or change the generator path first.
- **Whole-domain 301 of indiaaisummit.in, or its optional homepage retitle**: The domain hosts the recurring Delhi edition; only the announcement bar, card and the /awards redirect or note are worth doing now. The retitle is low confidence.
- **Chasing 'priyank kharge' (49,500/mo), 'ai conferences 2026 india' (390/mo, Cypher #1 and aggregators) or Amsterdam's #1 for 'world ai summit agenda'**: Not realistic in 16 days: authority gaps, an AI Overview above every result, and worldsummit.ai ranks for its own brand. Fix the facts on those pages but do not plan traffic from them.
- **Any change to the /awards/ URL or slugs during the window, and redirecting /1st-edition/awards.html**: Google's canonical is still non-www /awards and consolidation to www is pending; further moves risk ranking or snippet churn on the only non-brand page earning clicks. The merged E3 redirect of /1st-edition/awards.html contradicts C1 (which links it as the 2025 edition) and G3 (which may host the 2025 winners there); it stays live with an archive banner.
- **An interim 301 of /agenda to /ai-conference-bengaluru-2026.html before /agenda/ exists**: The merged file has /agenda redirected twice within days (E3 then D2/G1). A /agenda/ holding page with the 7 tracks and TBA cells ships with the legacy map on 5 Oct, so /agenda is redirected once and never retargeted.
- **A new 'AI events in Bangalore, October-November 2026' blog post**: The homepage already ranks #9 'ai events in bangalore', #6 'ai events in bangalore october 2026' and #4 'ai conference bangalore 2026'; a new URL mostly competes with it and may not index within 7-10 days; also needs a brand decision on naming Cypher.
- **Google Business Profile for the event, or the Search Console Change of Address tool**: Google's guidelines exclude temporary events (search_local_businesses found 0 results); Change of Address is for domain moves, not www/non-www. Use the venue's existing profile for an Event post instead.
- **Stripe abandoned-cart recovery emails**: Needs a promotional-consent checkbox at checkout and is unproven here; the manual call sweeps reach the same people faster. Optional only.
- **Editing the Sanjeev Gupta Lahari line or rewriting speaker bios**: The Lahari claim is unsupported without KDEM confirmation and the repository rule is never to write bios from memory; facts come from speakers.json and live pages only.
- **Google-dependent changes shipped after 7 Oct (new titles, metas, schema, new pages meant to rank)**: Request Indexing takes hours to days and is not guaranteed; a change that lands after 7 Oct is unlikely to be recrawled and reflected before the 12-16 Oct brand spike. After that date, spend developer time on conversion pages, the agenda hub and event-week pages, which work the moment they are live.
