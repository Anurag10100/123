# World AI Summit 2026: consolidated recommendations (1 Oct 2026)

Thirty-four recommendations merged from 91 findings produced by 14 parallel research agents and checked by skeptic agents. Impact scores are 1-10 for the window 1-17 Oct 2026. Asset refs point to files in `assets/`.


## Theme: Pass path, pricing, /delegate/, CTAs, lead capture


### A1. Decide one pass price ladder today and rebuild /delegate/ so every price on the site, speaker pages and listings matches it

**Impact 6/10, confidence high, effort S: 30-minute price decision; web dev 3-5 h for /delegate/ rebuild, homepage block, ribbon and bar; marketing 1 h for AllEvents; speaker meta edits 1 h, owner Marketing head (price and GST decision, listings) + web dev (/delegate/, homepage, ribbon, speaker template), by 2 Oct 2026 for the price decision and /delegate/ rows (Standard row expired 30 Sept); rest by 3 Oct so aggregator mirrors and Google's event index refresh before the final week.**


**Do this**

- Marketing head decides by 2 Oct which price a buyer pays from 1 Oct: [PLACEHOLDER: either extend Premium Rs 20,000 / VIP Rs 35,000 to a stated date such as 7 Oct or 13 Oct 23:59 IST, then Late Access Rs 30,000 / Rs 60,000; or make Late Access the current price now]. Also decide whether prices are incl. or excl. 18% GST and state it next to every price.
- On https://www.worldaisummit.com/delegate/: delete the 'Early Bird ... Valid till 25th July 2025' row, replace the expired 'Standard Access (Valid till 30th Sept 2026)' row with the one dated current row, highlight it, use one set of pass names (the page now uses Premium/VIP in one block and General Delegate/VIP Delegate in another), add the missing H1 'World AI Summit 2026 Delegate Passes, Bengaluru, 14-15 October', and put date, venue, current prices and 'Book Premium Pass' / 'Book VIP Pass' buttons above the fold.
- Below the fold on /delegate/: a 'What's included' comparison table, an 8-name 'Who you will hear' strip linking to speaker profiles, links to agenda and venue, Event JSON-LD, and a buyer FAQ answered by Elets (GST included or extra, GST invoice, pass transfer, refund, on-spot registration, lunch, certificate, what happens after registration).
- Replace the 'Group booking · 3+ delegates -> 10% off · registration@' line with a 4-field group-quote form (name, company, number of delegates, phone) that mails registration@worldaisummit.com and fires GA4 generate_lead with form_type=group; add one line 'Exhibiting instead? Book a booth' linking to the sponsor page.
- Homepage 'Secure your seat' block: show the same named, priced tiers as /delegate/ (today only 'Premium Pass Rs 20,000/ delegate' is named; the other two cards have no name or price), replace 'Three release phases. The earlier you commit, the better the price.' with the actual deadline date and next price, and add a countdown to that date only, never reset. Fix the /ai-conference-bengaluru-2026.html 'Register' block, which is only a 'Late Access' heading with no price.
- Add a site-wide top ribbon and one sticky bottom bar (shared with the contact bar in A4, not two bars): '[N] days to go · [current tier and prices] · Groups of 3+ save 10% · Book your pass' with a live countdown to 14 Oct 09:00 IST.
- Update the 10 of 51 /assets/speaker_details/ pages whose meta description says 'Passes from Rs 20,000' or 'Delegate passes from Rs 20,000' (anand-thakur, deepika-sandeep, ganesh-joshi, kuldeep-t, pranav-saxena, praveen-bist, ram-mohan-rao, suman-dash, rajesh-choudhary, sushan-rungta) and the 'Delegate passes from Rs 20,000' body line on speaker pages to the decided price; low priority, snippets only.
- Marketing edits the AllEvents listing (allevents.in, Sign in, Manage events, https://allevents.in/bangalore/world-ai-summit-2026-tickets/80002987560857): two ticket types (Premium, VIP) at the decided price instead of one 'Delegates Passes INR 20,000'; host renamed from 'World AI Summit 2026' to 'Elets Technomedia - World AI Summit'; group 10% line; three CTAs (delegate /delegate/ with UTM, sponsor via partnerships@worldaisummit.com, awards /awards/?utm_source=allevents&utm_content=awards); move the partnerships email out of the 'Refund Policy' field; add 6-10 confirmed 2026 speakers by name and role from speakers.json, no bios from memory. Check HappeningNext (https://happeningnext.com/event/world-ai-summit-2026-eid1ar6ef88bj) mirrors the text within 24-48 h; it shows no price, so no price edit there.

**Why**

- Exa fetch 1 Oct 2026: /delegate/ shows 'Early Bird ... Valid till 25th July 2025' Rs 20,000/35,000 'Save Rs 5,000', 'Standard Access (Valid till 30th Sept 2026)' Rs 20,000/35,000 (expired yesterday) and 'Late Access' Rs 30,000/60,000; no GST statement; two sets of pass names (verified by three skeptics).
- Exa fetch 1 Oct 2026: homepage shows 'Three release phases' with one card 'Premium Pass Rs 20,000/ delegate' and two unnamed, unpriced cards; AllEvents listing says 'Tickets on approval from Rs 20,000'; verifier also found /1st-edition/delegate-pass.html (2025 table) and elets.net/worldaisummit-delegate/ (Rs 25,000/50,000, valid till Sep 2025) still live.
- GA4 property 490291049, Sept 2026: /delegate/ had 1,729 users and 178 form_submit events (F02 verifier); 286 /delegate/ form submits in September against 18 users ever reaching success.php (F00 verifier), so this page carries pass intent.
- OpenSEO audit c1b16b55, 1 Oct 2026: /delegate/ missing H1, title 'World AI Summit 2026 | Delegate Pass Registration', crawlDepth null, inSitemap true; 10 of 51 speaker pages carry a Rs 20,000 price in the meta description (F07 and F56 verifiers; the F56 figure of about 25 was wrong).
- Competitor Cypher (Exa, cached Sep 2026, same week 7-9 Oct): prices 'incl. 18% GST', dated steps Rs 13,000 to Rs 20,000 from 12 Sep to Rs 30,000 from 2 Oct, sticky bar with countdown, group tiers 10/20/30%, 1-day pass Rs 10,000, buyer FAQ and 'Exhibiting instead?' box. The 2 Oct price move is unverified on the live page.

**Expected effect:** No organic traffic effect; nothing waits on Google. Mechanism is conversion protection on the page that carries pass sales: visitors currently see Rs 20,000 on the homepage, speaker pages and listings and an expired row plus Rs 30,000 on /delegate/, which is a likely cause of drop-off and 'what do I pay now?' emails in the two weeks when most passes sell. The size of the lift is unknown because purchases are not tracked in GA4. AllEvents and HappeningNext send an unmeasured number of referral sessions, likely tens to low hundreds over 1-17 Oct; utm_source=allevents in GA4 will show the real figure.


**Decisions needed**

- Which tier and price is charged from 1 Oct, and the exact deadline date for the next step (never reset)
- Whether Rs 20,000 / Rs 35,000 / Rs 30,000 / Rs 60,000 include 18% GST
- Optional commercial call: Cypher-style tiered group discounts (3-5 passes 10%, 6-10 20%, 11+ 30%) and a 1-day pass (Cypher Rs 10,000)
- Answers to the buyer FAQ (GST invoice, transfer, refund, on-spot registration, lunch, certificate)

**Assets:** A07, A02, A51, A29


### A2. Close the dead ends in the pass path: 301 every register URL to /delegate/ and give the homepage, nav and speaker pages crawlable Book / Nominate / Sponsor links

**Impact 5/10, confidence high, effort S for redirects and links (1-2 h); M for the homepage above-the-fold and FAQ (half day); /agenda/ depends on programme content, owner Web dev (redirects, template, nav, homepage) + content (speakers, FAQ) + programme team (/agenda/ sessions), by Redirects and crawlable links by 2 Oct 2026; homepage hero, nav and FAQ by 3 Oct; /agenda/ by 9 Oct; hero swap 16 Oct.**


**Do this**

- Web dev adds 301 redirects straight to https://www.worldaisummit.com/delegate/ from /registration and /registration.html (today 302 to https://worldaisummit.com/ then 301 to www, 3 hops), from /delegate-registration.html (400 views, 312 users, all in September, about 7 s engagement, 0 key events, no visible form) and from /1st-edition/delegate-pass.html (still sells 2025 passes at Rs 30,000/60,000); remove /registration and /registration.html from sitemap.xml (/delegate-registration.html is not in the sitemap or the crawl). If the 2025 page must stay live, add a top banner instead: 'This page is the 2025 edition. Book World AI Summit 2026 passes' linking to /delegate/, and the same banner on /1st-edition/.
- Homepage and /index.html hero: replace 'Save the date' with three plain <a href> buttons: 'Book delegate pass' to /delegate/ (relative link, not /registration), 'Nominate: World AI Awards 2026' to /awards/, 'Sponsor or exhibit' to [PLACEHOLDER: /partnership.html or /partner-with-us.html, see A5]. Make 'Secure your seat' card buttons, the nav 'Register' item and the FAQ answer 'How can I register for the event?' crawlable links to /delegate/ (optionally ?pass=premium / ?pass=vip if the form supports it).
- Header nav and footer on every page as plain <a href> links: 'Passes' /delegate/, 'Agenda' /agenda/ (once published), 'Speakers' /speaker.html, 'Awards' /awards/, 'Venue' /#venue (add id="venue" to the existing 'Where It All Comes Together' block; the venue content already exists, do not rewrite it), 'Partner' sponsor page, plus /ai-conference-bengaluru-2026.html and /blog/. Audit c1b16b55 shows no HTML page at crawl depth 1; /delegate/ and /awards/ are sitemap-only.
- Homepage H1: replace the theme sentence 'AI for All: Accelerating India's Journey Towards Inclusive, Responsible and Future-Ready AI' (also the H1 on /awards/) with the event name and keep the theme as a styled <p>. Do not change the title: it already reads 'World AI Summit 2026 | AI Summit India, Bengaluru, 14-15 October' (64 chars) and is what Google shows. Optionally trim the 182-char meta and give /speaker.html its own meta.
- Homepage blocks: change 'World AI Awards · Previous edition' to 'World AI Awards 2026: nominations open' linking to /awards/; render 12 confirmed 2026 speakers as HTML text (name, role, organisation) linking to profiles plus 'See all confirmed speakers' to /speaker.html; replace the 10 generic FAQ questions with the ones people ask (when and where, pass price and inclusions, group discount, awards deadline and fee, how to exhibit or sponsor, who is speaking, agenda, how to reach the venue), each linked to its page. Venue extras (nearest metro, airport travel time, parking) only from the venue, never from memory.
- Add one 'Book your pass' CTA block linked to /delegate/ (with the decided price from A1) to the shared template of the 51 /assets/speaker_details/*.html pages, /speaker.html and /ai-conference-bengaluru-2026.html.
- Programme team supplies sessions and web dev publishes /agenda/ as a track-by-day grid by 9 Oct (speakers.json already expects that URL but every session field is empty); add it to the sitemap and the nav.
- Connect the www URL-prefix or Domain property in Search Console (GSC today covers only the non-www property, 25 homepage impressions in 3 months). On 16 Oct swap the homepage hero to 'Thank you / highlights / World AI Summit 2027: register interest / partner with us' linking to the highlights page and partnerships@; brand searches fell 80-95% the month after the 2025 edition.

**Why**

- OpenSEO crawl c1b16b55, 1 Oct 2026: /registration and /registration.html return 302 to https://worldaisummit.com/ and are in the sitemap; /delegate/ has crawlDepth null and no crawlable path from the homepage; homepage is the only HTML URL with a crawl depth (0).
- GA4 property 490291049, 1-30 Sep 2026: /delegate-registration.html 400 views, 312 users, about 7 s engagement, 0 key events, only 12 sessions organic; it looks like an active campaign link pointing at a page with no form (F01 verifier).
- GA4 organic, 3-30 Sep 2026: homepage landing 2,446 sessions, 53 key events (27 partnership_form_submit, 26 form_submit), 1.92%; /delegate landing 48 sessions, 16 form_submit from 7 users, 16.7% (F17 verifier; F01 verifier reports 49 sessions and 16.3% for September). Organic Search 3,082 sessions vs 1,348 in the prior 28 days (+128.6%).
- Exa fetch 1 Oct 2026: homepage hero shows '14th - 15th October 2026 Save the date'; awards block labelled 'Previous edition'; 'Meet The Visionaries' has no speaker names in extracted text; FAQ has 10 generic questions. Homepage already has the venue block with 'Get Directions' (F19 verifier).
- OpenSEO keyword metrics, India, 1 Oct 2026: 'world ai summit' 880 (Aug 2025), 1,600 (Sep 2025), 320 (Oct 2025); 'world ai summit 2026' 170 (Jun), 390 (Jul), 480 (Aug); 2026 run-up is weaker than 2025 (F19 verifier).

**Expected effect:** Organic traffic gain in the window is about zero: the registration queries (#4, #10) are won by the homepage and redirects or an H1 will not move rankings in two weeks; the title is already right. Leads: the /delegate-registration.html 301 alone redirects roughly 300 users a month who currently land on a page with no form. On the homepage, a realistic +0.2 to 0.5 percentage point lift on about 2,000-3,500 organic homepage sessions over 1-17 Oct (Sept run rate about 87 a day plus an event-week spike) is roughly 5-15 extra organic form enquiries (F17 verifier); the same links also help email and paid visitors, unquantified. Sitelinks on brand queries are Google's choice.


**Decisions needed**

- Whether /1st-edition/delegate-pass.html is redirected or kept with a banner
- Which URL is the canonical sponsor page (see A5) so hero and nav links point to one place
- Which 12 speakers are confirmed for the homepage strip (from speakers.json confirmed_2026)
- Programme team sign-off on agenda sessions

**Assets:** A01, A08, A16, A18


### A3. Call back everyone who started a /delegate/ or /awards/ form but did not pay, fix failed.php and success.php, and start tracking checkout and purchase in GA4

**Impact 5/10, confidence medium, effort S: 3-4 h of calling per sweep, three sweeps; web dev about 2 h for the two page panels and 1-2 h for GA4 events, owner Registration and awards desks (calls) + web dev (pages, GA4 events) + email team (UTMs), by First call sweep and page fixes by 3 Oct 2026; repeat sweeps 6 Oct and 10 Oct; GA4 events by 3 Oct.**


**Do this**

- Registration and awards desks pull every /delegate/ and /awards/ form submission since 1 Aug 2026 from the form backend or database and the Stripe dashboard (Payments, incomplete or expired checkout sessions) and compare with paid orders; if the forms do not store details before the Stripe redirect, use Stripe's incomplete sessions (customer email, if collected).
- Within 24 hours, call and WhatsApp every unpaid starter with a fresh payment link, the 3+ delegates 10% group offer and an option to pay against an invoice or PO; the awards desk does the same for everyone who reached /awards/failed.php. Repeat the sweep on 6 Oct and 10 Oct.
- /awards/failed.php (today shows the blank nomination form with no error message, Exa 1 Oct): add a panel 'Your payment did not go through. Your entry is saved.' (only if it really is saved), a [Retry payment] button, [Pay by NEFT/UPI against a GST invoice], a WhatsApp/call button and secretariat@worldaisummit.com.
- /delegate/success.php (today shows the full price table and no visible confirmation in Exa text; check in a browser in case JS renders it): replace with an order confirmation (pass type, 14-15 Oct, Sheraton Grand Bangalore Hotel at Brigade Gateway, what happens next: e-badge, invoice), an .ics file, a 'Bringing colleagues? 3+ delegates get 10% off' block linking to the group form (A1) and a share link tagged utm_source=delegate_share.
- GA4 measurement: fire begin_checkout on the /delegate/ pay button and purchase (value, currency INR) on /delegate/success.php; the same for award payments (success page) plus a failure event on /awards/failed.php. Add utm_medium=email to links sent through r.emails.elets.in so 213,013 sessions stop showing as referral.
- Optional: if checkout uses Stripe Checkout, switch on abandoned-cart recovery emails (needs a promotional-consent checkbox at checkout).

**Why**

- GA4 property 490291049, 1 Jul-30 Sep 2026: /delegate/ 316 form_submit key events from 1,883 users, but /delegate/success.php had only 18 users (78 views; 11 sessions started on it, a payment-gateway return); 286 /delegate/ form submits in September alone (F00 verifier).
- GA4, 1 Jul-30 Sep 2026: /awards/ 79 key events from 512 users; /awards/failed.php 8 users (F00) or 9 per the verifier; /awards/success.php 2 users; checkout.stripe.com/referral brought 5 sessions in Sept.
- GA4 ecommerce report says 'no ecommerce activity': transactions and revenue are 0 on every source because purchases are never tracked, so the real number of paid passes is UNKNOWN (F00 verifier, F17); form_submit can fire more than once per user and may include non-lead forms.
- Exa fetch 1 Oct 2026: /awards/failed.php shows the bare nomination form; /delegate/success.php shows the pricing page with no confirmation text.
- GA4 1 Jul-30 Sep 2026: r.emails.elets.in / referral 213,013 sessions (F17) means email clicks are misattributed.

**Expected effect:** No traffic effect. This works on the warmest audience the site has. Rough guide only: if about 100 unpaid starters exist and 5-10% pay after a personal call, that is about 5-10 passes (about Rs 1-2 lakh at Rs 20,000) plus a few of the roughly 8-9 failed award nominations; all unverified until the unpaid list is pulled. The GA4 events give the first real pass-sales numbers by channel before event week.


**Decisions needed**

- Confirm whether form data is stored before the Stripe redirect, and whether an unpaid entry is really 'saved'
- Approve invoice/PO and NEFT/UPI payment options for recovery calls
- Consent checkbox wording if Stripe abandoned-cart emails are switched on

**Assets:** A00, A16


### A4. Add a staffed WhatsApp and click-to-call bar with Book passes, Sponsor or exhibit, and Nominate intents on every lead page

**Impact 3/10, confidence medium, effort S: web dev 1 h; marketing 30 min to assign numbers; ongoing desk staffing until 17 Oct, owner Marketing (numbers, staffing) + web dev, by 3 Oct 2026.**


**Do this**

- Marketing confirms whether the two numbers on /1st-edition/delegate-pass.html (9818274383 delegates, 8860651641 speaking) are still staffed, and assigns new numbers for the sponsor/exhibit and awards lines (the 2025 page has none). Do not publish a number nobody answers.
- Web dev adds a small bottom bar on mobile and a side button on desktop (merged with the price ribbon bar from A1 so there is one bar) with three intents: 'Book passes' (registration desk), 'Sponsor / exhibit' (partnerships desk), 'Nominate' (awards desk); each opens wa.me/<number>?text=<prefilled intent> and has a tel: link.
- Fire GA4 event contact_click with method (whatsapp or call) and intent.
- Staff each line 9 am to 8 pm until 17 Oct, with answers ready for GST invoice, PO, group pricing and 'what do I pay now?' questions arising from the expired Standard row.
- Keep the existing 'World AI Summit Community' WhatsApp channel CTA but label it as updates, not a sales line.
- Show the bar on /, /delegate/, /awards/, /award.html, /partnership.html and /partner-with-us.html.

**Why**

- Exa fetch 1 Oct 2026: homepage, /delegate/, /partnership.html and /partner-with-us.html show only registration@, partnerships@ and secretariat@ addresses; /awards/ shows only secretariat@; the only WhatsApp element is the 'World AI Summit Community' updates channel (verified).
- Exa 1 Oct 2026: the 2025 page /1st-edition/delegate-pass.html lists 9818274383 for delegates and 8860651641 for speaking, no sponsorship or awards number, staffing unconfirmed (F04 verifier).
- Competitor Cypher /tickets (Exa, cached Sep 2026): 'Questions? Contact our team' on the ticket page and 'Dedicated WhatsApp Support' in the VIP pass.
- The site already collects leads through forms (GA4: form_submit 395 events / 251 users, partnership_form_submit 391 events / 298 users, 1 Jul-30 Sep 2026), so 'email-only' overstates the gap (F04 verifier).

**Expected effect:** No traffic effect. Converts visitors who already have intent but need an invoice, PO or group answer before paying, when email adds a day per reply with the event two weeks out. Lead count not quantified; contact_click in GA4 will show usage within days.


**Decisions needed**

- Which numbers to publish for each of the three lines and who answers them 9 am to 8 pm

**Assets:** A04


### A5. Turn /partnership.html, the mailer landing page, into a real sponsor lead page with benefits, remaining inventory and a gated 2026 deck

**Impact 3/10, confidence medium, effort M: web dev half a day; partnerships 1-2 h for the deck PDF and the true remaining-inventory list, owner Partnerships team (deck, inventory, KDEM wording) + web dev, by 3 Oct 2026.**


**Do this**

- Decide the canonical sponsor URL [PLACEHOLDER: /partnership.html per F05, with /partner-with-us.html 301'd to it; F08 and F19 link to /partner-with-us.html instead]; then point every hero, nav, FAQ and listing CTA (A2, A1) at that one URL.
- Copy the 5 benefit blocks from /partner-with-us.html (sponsorship, exhibit, centre-stage speaking slot, 1:1 meetings and roundtables, AI Innovation Report feature) onto /partnership.html above the form, which today holds 64 words, the tagline and contact emails; then 301 the other URL (10 views per quarter).
- Give the page a self-canonical (both pages are canonical to / today), the title 'Sponsor & Exhibit at World AI Summit 2026, Bengaluru' and its own meta; the old 'Global Artificial Intelligence Conference by Elets Technomedia' title is still live on /award.html, /partnership.html and /partner-with-us.html.
- Add a 'Download the 2026 partnership deck' gate (name, company, designation, work email, phone) that delivers the PDF instantly, alerts partnerships@worldaisummit.com and fires generate_lead with form_type=prospectus; confirm a 2026 PDF exists first.
- Add 'Still available for 14-15 Oct:' listing only inventory that is really open (for example exhibition booths, awards-night or networking-dinner sponsorship), a strip naming KDEM (Govt of Karnataka) as [PLACEHOLDER: 2026 Strategic Partner per the brief; F05 says 2025] strategic partner, and the partnerships WhatsApp/call button from A4.
- Use one audience figure everywhere: /partner-with-us.html says '1200+ global AI leaders' and /award.html says '500+ Industry Leaders'.
- Link the homepage FAQ 'Are exhibition and sponsorship opportunities available?' to the sponsor page.
- Before sizing any uplift, check partnership_form_submit counts against the partnerships@ inbox or CRM: 51 events have /thankyou.html as landing page, so the event likely fires on thank-you load or reloads too.

**Why**

- GA4 property 490291049, 1 Jul-30 Sep 2026: /partnership.html 165,574 views, 136,503 users, 53,212 s total engagement (about 0.4 s per user), pointing to email link-scanner or instant-bounce visits (verified).
- GA4, 1 Aug-30 Sep 2026, partnership_form_submit by landing page: 142 events / 121 users on /, 117 / 97 on /partnership.html, 51 / 39 on /thankyou.html, 5 elsewhere, about 315 in total; /partnership.html landings are about 37%, so the claim that most enquiries come through it is false (F05 verifier). 97 users over 2 months is about 48 a month, unverified against the inbox.
- Exa fetch 1 Oct 2026: /partnership.html holds only the tagline and contact emails; /partner-with-us.html has the 5 benefits; crawl c1b16b55: both are canonical to / and duplicate the homepage title.
- Competitor Cypher (Exa, cached Sep 2026): header and footer carry 'Book a Booth', 'Become a sponsor', 'Sponsor' and 'Exhibit' links.
- Booth fabrication lead times make sponsor leads after about 8 Oct hard to close (F05).

**Expected effect:** No organic traffic: a self-canonical and new title on a thin page will not earn rankings within two weeks for a site with roughly 10 real referring domains. Leads: the page already yields roughly 48 partnership_form_submit users a month from mailer landings (count unreliable); a gated deck adds a lower-commitment step for the small share of real visitors among mostly link-scanner sessions. Uplift unquantified, but each sponsor lead is the highest value lead the event has, and only leads before about 8 Oct are closable for 14-15 Oct.


**Decisions needed**

- Canonical sponsor URL (/partnership.html or /partner-with-us.html)
- Whether a 2026 partnership deck PDF exists and can be gated
- Which inventory is genuinely still unsold for 14-15 Oct
- Correct KDEM partnership year and the single audience figure to use

**Assets:** A05


**Conflicts noted**

- Current pass price from 1 Oct: homepage, speaker pages and AllEvents say Rs 20,000 (Premium); /delegate/ shows Standard Rs 20,000/35,000 expired 30 Sept 2026 and Late Access Rs 30,000/60,000 (Exa, 1 Oct). Findings also differ on the remedy: F02 suggests extending Rs 20,000/35,000 to a stated date such as 7 Oct then Late Access; F56 suggests making Late Access the highlighted price today; F31 suggests extending Standard to 13 Oct or moving listings to Rs 30,000. Business decision.
- GA4 purchase key event: F00 verifier says GA4 has no purchase key event and the only key events are form_submit and partnership_form_submit; F17 (and its verifier) list 'purchase, form_submit, partnership_form_submit' as configured key events with 0 transactions. Both agree purchases are not tracked and real sales are unknown.
- /delegate organic landing conversion: F01 verifier reports 49 sessions, 16 key events, 16.3% (September); F17 verifier reports 48 sessions, 16 form_submit from 7 users, 16.7% (3-30 Sep). Different date ranges.
- Speaker-page meta descriptions with a Rs 20,000 price: F56 said about 25; F02 verifier found 1 of 5 sampled; F07 and F56 verifiers found exactly 10 of 51 in crawl c1b16b55. Used 10 of 51.
- KDEM partnership year: F05 proposes a strip naming KDEM as 2025 strategic partner (asset A05 title says '2025 partner strip'); the brief says KDEM is the 2026 Strategic Partner.
- /awards/failed.php users, 1 Jul-30 Sep 2026: F00 says 8 users; F00 verifier text begins '9 v' (truncated in the file).
- Homepage title: F08 claimed it is generic and proposed a new one; verifier shows the live title is already 'World AI Summit 2026 | AI Summit India, Bengaluru, 14-15 October' (64 chars) and the old title is live only on /award.html, /partnership.html and /partner-with-us.html. Title swap dropped.
- Sponsor CTA destination: F08 and F19 link 'Sponsor or exhibit' / 'Partner' to /partner-with-us.html; F05 makes /partnership.html the lead page and 301s /partner-with-us.html to it; F31 mentions /partner-with-us.html once it stops canonicalising to /. Needs one decision.
- /delegate/ H1 wording differs: F01 'World AI Summit 2026 Delegate Passes - Bengaluru, 14-15 October'; F17 'World AI Summit 2026 Delegate Passes, Bengaluru, 14-15 October'; F56 'World AI Summit 2026 Delegate Passes & Pricing'. Any one is fine; A2/A1 use the F17 wording.
- Sticky bottom bar: F56 proposes a price-and-countdown bar, F04 a WhatsApp/call bar, F17 a sticky mobile CTA bar. These must be built as one bar, not three.

## Theme: Elets owned network: mailers, portals, editorial, indiaaisummit


### B1. Deep-link every Elets mailer and newsletter to /delegate/, /awards/ and /partnership.html with UTMs, after fixing the expired pass row

**Impact 5/10, confidence high, effort S: about 3 hours for templates and UTMs, plus under 2 hours of web work on /delegate/ and /awards/, owner Elets email/marketing team (links, UTMs, QA); web dev (/delegate/ row, /awards/ categories); analytics (GA4 reading), by 2 Oct 2026 (next send), then every send to 13 Oct; post-event send 16 Oct.**


**Do this**

- Before the 2 Oct send, the web team removes or updates the expired 'Standard Access (Valid till 30th Sept 2026) Rs 20,000 / Rs 35,000' row on https://www.worldaisummit.com/delegate/; if it is not fixed in time, hold the pass CTA or send it with no price in copy (PLACEHOLDER_FALLBACK_IF_DELEGATE_NOT_FIXED).
- From the 2 Oct send to 13 Oct, in every Elets mailer and in the eGov Weekly Briefing, BFSI, eHealth and Digital Learning newsletters, the primary CTA 'Book your delegate pass' goes to https://www.worldaisummit.com/delegate/, never to the homepage, /award.html, /registration or /registration.html (the last two take 3 redirect hops to the homepage).
- The awards CTA goes to https://www.worldaisummit.com/awards/ (indexed, ranks, holds the nomination form), not /award.html (canonicalised to /, 25,603 views Jul-Sep 2026); the web team adds the category list to /awards/ or links to it, and until then the mailer names the categories copied from /award.html (PLACEHOLDER_AWARD_CATEGORY_GROUPS).
- The sponsor CTA stays on https://www.worldaisummit.com/partnership.html (153 partnership_form_submit events from sessions that landed there), and every mailer also carries a 'Request sponsorship deck' line to mailto:partnerships@worldaisummit.com.
- Tag every WAIS link (banner, logo, image, button, footer) with utm_source=elets_mailer, utm_medium=email, utm_campaign = world_ai_summit_2026_delegate / world_ai_awards_2026 / world_ai_summit_2026_sponsorship (all already exist in GA4) and utm_content=<segment>_<yyyymmdd>; turn off the ESP's automatic UTM option first.
- Keep price, fee, discount, deadline and seats-left out of copy until confirmed: PLACEHOLDER_PASS_PRICE (homepage Rs 20,000 vs /delegate/ Late Access Rs 30,000/60,000), PLACEHOLDER_AWARD_FEE (/award.html 'from 30k + GST' vs 2025 fee Rs 18,000-20,000 + GST), PLACEHOLDER_GROUP_DISCOUNT_CONFIRMED (10% for 3+ not seen in the /delegate/ text fetched 1 Oct), PLACEHOLDER_AWARD_DEADLINE.
- Ask the Elets ESP team to check whether link-scanner security tools are hitting r.emails.elets.in and to exclude those clicks; in GA4 (property 490291049) read results on an engagement time > 0 segment and count /delegate/success.php views, partnership_form_submit users and /awards/ form_submit users, not raw key events.
- Rebuild the 16 Oct post-event send without the pass CTA and with PLACEHOLDER_POST_EVENT_PRIMARY_CTA (awards results or next-edition sponsor enquiries); run the A34 per-template QA (Gmail and Outlook test, all four utm_ parameters survive the r.emails.elets.in redirect, trailing slashes kept) before every send.

**Why**

- r.emails.elets.in / referral sent 263,703 sessions (260,770 users, 32% engagement) with 159 key events, 0.06%, in Jul-Sep 2026; google/organic sent 5,393 sessions with 138 key events, 2.6% (GA4 490291049 via OpenSEO, 1 Oct 2026). Mailers are about 92% of sessions (263,703 of about 285,600, verifier).
- Mailer clicks mostly land on non-converting pages: / 197,889 views (3.9 s engagement per user), /partnership.html 165,574 views by 136,503 users at 0.39 s per user, /award.html 25,603 views; /delegate/ had only 2,384 views but 316 key events (19 s per user) and /awards/ 876 views with 79 key events (GA4, Jul-Sep 2026).
- Conversion fell to 0.045% in the second half of September (verifier, GA4 16-30 Sep 2026). Only 18 users reached /delegate/success.php in Jul-Sep; purchase event shows 0 transactions, so key events are not sales.
- Existing campaigns show tagging works: world_ai_summit_2026 2,174 sessions and 97 key events; world_ai_summit_2026_sponsorship 768 sessions and 21 key events (GA4, Jul-Sep 2026).
- Verifier caveat: /delegate/ and /awards/ convert well partly through selection bias (people who reach them already intend to buy or nominate), and the near-zero engagement on /partnership.html points to scanner or bot clicks, so the human base is unknown.

**Expected effect:** No organic search effect. At the Jul-Sep average of about 2,870 mailer sessions a day (about 920 engaged), 1-17 Oct brings roughly 45-50k mailer sessions; at 0.06% that is about 30 key events. Each 0.1 percentage point gained from deep-linking adds roughly 45-50 pass, sponsor or award form submits, but the true lift is unknown because bot clicks inflate the base and cold mailer readers will convert below the 316-on-2,384 rate seen on /delegate/. This is still the only lever that touches most of the traffic before 14 Oct.


**Decisions needed**

- Confirm the current pass price (homepage Rs 20,000 vs /delegate/ Late Access Rs 30,000/60,000) or extend the Standard rate
- Confirm the 2026 award fee and nomination deadline
- Confirm the 10% group discount for 3+ delegates before it appears in copy
- Choose the primary CTA for the 16 Oct post-event send
- Decide the fallback (hold or price-free pass CTA) if /delegate/ is not fixed by 2 Oct

**Assets:** A34


### B2. Put World AI Summit house ads and deep links on the Elets portals and turn indiaaisummit.in into a funnel to /delegate/ and /awards/

**Impact 3/10, confidence medium, effort S-M: about half a day for portal creatives and widget links, plus under 2 hours on indiaaisummit.in, owner Elets web/ad-ops and design (portals); web dev (indiaaisummit.in), by 2 Oct 2026 for portal placements (live to 15 Oct); 3 Oct 2026 for indiaaisummit.in.**


**Do this**

- From 2 to 15 Oct, place WAIS 2026 creatives (728x90, 300x250, 320x100) in the existing 'Advertisement' slots (header leaderboard and in-article 'Single Page Desktop Image') on egov.eletsonline.com, cio.eletsonline.com, bfsi.eletsonline.com, ehealth.eletsonline.com and digitallearning.eletsonline.com; first confirm what the slots carry today, since the India Energy Expo house ad was seen on a page crawled in Aug 2026.
- Rotate two creatives: passes to https://www.worldaisummit.com/delegate/ and World AI Awards 2026 nominations to https://www.worldaisummit.com/awards/ until PLACEHOLDER_AWARD_DEADLINE; run the BFSI creative on bfsi only and the eGov/policy creative on egov only; use the B1 UTM scheme with a per-portal utm_source.
- Re-point the 'Visit Website' button for 'World AI Summit 2026 | Bengaluru, 14-15 Oct 2026' in the egov 'Upcoming Conferences' widget (homepage and https://egov.eletsonline.com/conferences/) and on https://events.eletsonline.com/ to /delegate/ with UTMs (current href unverified), and add a 'Partner with us' link to /partnership.html.
- By 3 Oct on https://www.indiaaisummit.in/, add a sitewide announcement bar and a hero-adjacent card linking to /delegate/ and /awards/, plus a 'Next Elets AI event' section above the fold with descriptive anchors ('World AI Summit 2026, Bengaluru, 14-15 October', 'book a delegate pass'); HTML is in A38.
- https://www.indiaaisummit.in/awards still shows 'India AI Summit 2025, 10-11 December 2025', 'Elets India AI Awards 2025' and 'Nominate Now': either 301 it to https://www.worldaisummit.com/awards/ until the next Delhi cycle opens, or add a top note 'Nominations for this edition are closed. Nominate for the World AI Awards 2026'. Do not 301 the whole domain, which hosts the recurring Delhi edition.
- Optional, lower confidence: retitle the indiaaisummit.in homepage from 'India AI Summit Delhi 2026 | AI Conference in India | Artificial Intelligence Conference' to 'India AI Summit Delhi, 22 Jan 2026 | Elets AI Summit' so a finished event stops competing on generic 'ai summit 2026' wording.

**Why**

- egov.eletsonline.com referral: 4,153 sessions in Jul-Sep 2025 vs 27 in Jul-Sep 2026 (15 of the 27 in 15-30 Sep); events.eletsonline.com 402 vs 164; cio.eletsonline.com 224 in 2025 and absent from the 2026 top 40; eletsonline.com root 232 sessions and 2 key events in 2026 (GA4, verified 1 Oct 2026).
- Verifier correction: the periods are not like-for-like. The 2025 summit ran 25-26 Sep 2025, so Jul-Sep 2025 includes the run-up and event days; the drop is real but smaller than 4,153 vs 27 suggests, 2025 egov traffic had 37% engagement and no recorded key events.
- The egov 'Upcoming Conferences' widget already lists WAIS 2026 and produced only 27 sessions in a quarter, so the widget alone is not enough (verifier).
- indiaaisummit.in is organic #10 for 'ai summit india 2026' (880/mo) with a '22 Jan 2026' snippet, worldaisummit.com is #15; the page promotes 'Elets AI Summit 2026, Eros Hotel, Nehru Place, New Delhi, 22nd January 2026' and never mentions World AI Summit 2026 (OpenSEO SERP and Exa, 1 Oct 2026). GA4 shows zero referral sessions from indiaaisummit.in in Jul-Sep 2026.

**Expected effect:** Directional: low hundreds to about 1,000 referral sessions over 2-15 Oct from the portals if placements match 2025 reach (2025 averaged about 45 egov sessions a day, concentrated near the event), and tens of sessions from indiaaisummit.in. Leads come from landing on /delegate/ (316 key events on 2,384 views) rather than the homepage. No measurable organic effect for worldaisummit.com inside the window; a small ranking gain for /awards/ is possible if the stale indiaaisummit.in/awards page is redirected.


**Decisions needed**

- Confirm the 2026 awards nomination deadline for the awards creative
- Choose redirect or top note for indiaaisummit.in/awards
- Approve or skip the optional indiaaisummit.in homepage retitle
- Confirm who controls the egov widget href and the portal ad slots

**Assets:** A35, A38


### B3. Retrofit the live Elets WAIS articles and the duplicated /blog/ posts: deep links, correct tracks and dates, one canonical

**Impact 2/10, confidence medium, effort S-M: about 3 hours editorial plus about 1.5 hours web and content; canonical choice needs Elets editorial sign-off, owner Elets editorial (CIO, eGov, BFSI desks); web dev (canonicals, dates, schema); content (track paragraph), by Article edits, track paragraph and dates by 3 Oct 2026; canonical decision by 9 Oct 2026.**


**Do this**

- By 3 Oct, replace the closing 'For More Updates, visit: https://www.worldaisummit.com/' in cio.eletsonline.com articles 76367 (22 Sep), 76379 (30 Sep) and 76296 (1 Aug) with the A36 closing paragraph using clean URLs to /delegate/, /awards/, /partnership.html and /speaker.html, no UTMs; article 76373 (24 Sep) showed no closing homepage URL in the Exa text, so add the paragraph there.
- Fix the track lists: 76367 names the old tracks in two places ('Tracks Mapping the AI Landscape' and the closing paragraph) and says '1,200+ delegates'; 76373 names six old tracks in its closing paragraph; replace both with the seven current tracks (Frontier Models & Compute; Sovereign AI & Geopolitics; Enterprise AI in Production; GCCs; Robotics, Agents & Embodied AI; AI for Bharat; Capital, Founders & Exits) and use PLACEHOLDER_DELEGATE_COUNT (1,000+ on /ai-conference-bengaluru-2026.html vs 1,200+ in the 22 Sep piece) consistently. 76379's tracks are correct; link each track heading to the matching section of /ai-conference-bengaluru-2026.html.
- Fix the subheading 'Why Bengaluru Is the Right Place for This Conversation at World AI Summit 2025' in https://egov.eletsonline.com/2026/07/the-next-chapter-of-ai-what-will-define-2026-and-beyond/ and in its WAIS /blog/ copy.
- Add a one-line 'Speaking at World AI Summit 2026' box to the bfsi Tulshekar Gangireddy article (5 Sep 2026), the egov Pankaj Kumar Pandey article (2026/04) and the egov KDEM article (2026/08, Sanjeev Gupta), linked to /speaker.html or the person's /speakers/<slug>/ page once the generator is deployed; re-check confirmed_2026 in speakers.json before publishing. Add a one-line 2026 link to the 2025 WAIS press releases on cio.eletsonline.com.
- Four of the five posts on https://www.worldaisummit.com/blog/ are verbatim copies of Elets articles. By 9 Oct pick one canonical per pair: preferred is rel=canonical on the cio/egov copies pointing to the worldaisummit.com/blog/ versions; if Elets editorial will not agree, point the WAIS copies at the Elets originals. Stop publishing new verbatim copies either way.
- Fix the WAIS 'Beyond the Hype' post on both URLs: it lists seven old tracks and says '1,200+ delegates, 100+ speakers and 50+ startups'; apply the same track paragraph and delegate figure as step 2.
- Show a visible publish date and byline on the /blog/ index and in each post, add Article JSON-LD with datePublished and dateModified, and add in-body links from each post to /delegate/, /awards/ and the relevant track section (each post has 6 internal links today); link /agenda/ only once it exists (see B5).
- From 2 Oct, feature only event-specific items (speaker posts, guide, live blog, highlights, winners) at the top of /blog/ and stop spending writing time on generic essays.

**Why**

- Exa fetches 1 Oct 2026: the 22 Sep and 24 Sep CIO pieces carry old track names, the July eGov piece has a 'World AI Summit 2025' subheading, and the speaker articles never mention WAIS. Verifier: 76373 has six old tracks (no GCCs) and no closing homepage URL in the fetched text.
- The one UTM-tagged CIO article (campaign ai_in_india_dpi_global_leadership) produced 21 sessions and 1 key event in Jul-Sep 2026, about 2.5 sessions a week; GA4 shows no cio.eletsonline.com referral sessions at all in Q3, egov 27 and bfsi 2 (verifier).
- /delegate/ and /awards/ have no internal links (sitemap only); nearly all 19,511 eletsonline.com backlinks point at the homepage (anchor detail unverified).
- WAIS blog copies carry Published 2026-09-28 in Exa metadata; originals are cio 76296 (1 Aug), 76367 (22 Sep), 76373 (24 Sep) and egov 2026/07. Audit c1b16b55: 6 internal links and 1,268-2,160 words per post. worldaisummit.com is not in the top 20 for 'ai in india digital public infrastructure', 'skills needed in ai driven world' or 'how ceos are using ai' (OpenSEO SERP, India, 1 Oct).
- Tulshekar Gangireddy, Pankaj Kumar Pandey and Sanjeev Gupta are confirmed_2026=true in /home/user/123/worldaisummit/speakers/speakers.json (read 1 Oct 2026).

**Expected effect:** Low referral volume, in the order of a few sessions per article per week on the evidence of the one tagged CIO piece. The first descriptive editorial links into /delegate/ ('ai summit 2026 registration', #10) may help crawling and ranking only if Google recrawls within the window, which is uncertain. Canonicals, dates and JSON-LD will not change rankings by 17 Oct. The main value is removing wrong track and edition claims that sponsors and delegates can see, and putting pass, award and sponsor links in front of readers already on WAIS content.


**Decisions needed**

- Which domain holds the canonical for each duplicated article (Elets editorial sign-off)
- Which delegate figure to use site-wide (1,000+ or 1,200+)
- Whether the /speakers/<slug>/ pages are deployed before the speaker boxes go live

**Assets:** A36, A49


### B4. Run one Elets editorial plan for 3-16 Oct: speaker roundups first, sector previews and news pieces only with live link targets, then the day-of releases

**Impact 3/10, confidence medium, effort L overall: about 5 hours for the two roundups, about 1 day per sector preview, about 3 hours per news piece, S per press release; do the roundups first if capacity is short, owner Elets editorial desks (CIO, eGov, BFSI, eHealth, Digital Learning); partnerships (KDEM, wire, sponsor CTA); programme team (track assignments), by Roundups by 7 Oct 2026; previews 3-12 Oct; optional news pieces 5-9 Oct; PR1 12-13 Oct; PR2 14 Oct night; PR3 16 Oct.**


**Do this**

- By 6-7 Oct publish on cio.eletsonline.com 'World AI Summit 2026 speakers: enterprise and government AI leaders in Bengaluru, 14-15 October', grouping the 50 confirmed speakers by sector (BFSI, retail and consumer, health, ecosystem and capital) with every name linked to its worldaisummit.com speaker page and one CTA to /delegate/ with no price (speaker page metas still say 'Passes from Rs 20,000', which is out of date); and on egov.eletsonline.com 'Government leaders at World AI Summit 2026' covering Pankaj Kumar Pandey, T Bhoobalan, Dr Ravikumar Surpur, Aman Mittal, Hemant Garg, Sanjeev Gupta, Ram Mohan Rao, M Balasubramaniam and Dr Sushil Kumar Meher. Roles from speakers.json and live pages only; no bios from memory.
- Between 3 and 12 Oct publish one preview per portal (bfsi, egov, cio, ehealth, digitallearning) using the A37 speaker lines and fresh quotes gathered by email, and push each in that portal's newsletter; because session is null for all 76 speakers.json entries, do not claim who is on which track or 'what they will debate' until the programme team supplies the agenda (PLACEHOLDER_TRACK_ASSIGNMENTS). Note the file spellings 'Aneelkumar (Aneel) Savalagi' and 'Anshuma (Dogra) Singh', and that Surpur's organisation is marked 'confirm'.
- Only if capacity remains after steps 1 and 2, run the A48 news-analysis pieces 5-9 Oct (GCC: BusinessToday 30 Sep and ANSR 24 Sep; Karnataka AI University and Nipuna Karnataka; RBI Bulletin Sep 2026, which is a DG speech dated 25 Sep, not a policy; sovereign compute, using only the current PIB or indiaai.gov.in GPU figure; MeitY IndiaAI CoE Thiruvananthapuram, 30 Sep). Verify RBI and GPU figures from primary sources before use; do not copy these pieces onto worldaisummit.com/blog/.
- Link rules for every piece: link only to URLs that are live on 1 Oct (/delegate/, /awards/, /speaker.html, speaker pages, /partnership.html, homepage). /agenda/ is 'unknown to Google', /agenda returns 5xx (last crawl 26 May 2026) and /tracks/<slug>/ and /awards/winners-2026/ do not exist; add those links only after B5 ships them. Keep links editorial and in context, not sitewide or footer.
- Publish any 'AI Dialogues' or Leadership Dialogue interview with a confirmed 2026 speaker with a link to that speaker's page.
- Day-of cadence, published once (the F41 day-of pieces and the F79 press releases are the same items): PR1 curtain-raiser 12 or 13 Oct ('World AI Summit 2026 opens tomorrow in Bengaluru'); PR2 on 14 Oct about 21:00 IST with Day 1 news and World AI Awards 2026 winners; PR3 wrap-up on 16 Oct linking to highlights and the 2027 interest form on the homepage. Same-day on cio.eletsonline.com and egov.eletsonline.com plus relevant verticals; at most 2 descriptive links per release, only to URLs that will persist.
- Before PR1 fix the edition number (LinkedIn showcase says '2nd Edition', Sept 2026 posts say '3rd Edition'; use PLACEHOLDER_EDITION or omit it) and make sure /delegate/ no longer shows the expired Standard tier (B1 step 1).
- Ask KDEM (2026 Strategic Partner) to post PR2 or PR3 on its newsroom and social channels; send PR2 to one paid India wire only if budget is approved.

**Why**

- speakers.json has 76 entries, 50 with confirmed_2026=true, all named people present with matching organisations; session is null for all 76, so no track framing is supported by the data (verifier, 1 Oct 2026).
- Speaker pages already rank: worldaisummit.com/assets/speaker_details/aman-mittal.html is organic #4 for 'aman mittal ias' and the Elets eletsegov Facebook post is organic #6; the egov 2023 article is organic #10 (overall 13) (OpenSEO SERP, Google India, 1 Oct 2026). Addressable speaker-name demand is about 1,100/mo.
- Measured payoff of Elets article links is low: no cio.eletsonline.com referrals in Aug-Sep 2026 despite 3-4 WAIS articles; all Elets portal subdomains combined sent fewer than 30 sessions; the eletsonline.com root sent 179 sessions with 2 key events; the 2025 best case was about 20-50 sessions per CIO article (verifier).
- 2025 precedent (Exa): cio.eletsonline.com 'Kicks Off ... Tomorrow' on 24 Sep 2025 and 'Concludes' on 29 Sep 2025, plus pieces on 17 Jun, 10 Jul and 28 Aug 2025; the same text was republished by aispectrumindia.com on 13 Oct 2025; WebSearch found no ANI, PTI, ET, The Hindu or Deccan Herald coverage of 2025 (absence not proven). 2025 Elets articles still link to worldaisummit.com/agenda, which now returns 5xx.
- Generic news queries are out of reach for the event site: 'karnataka ai policy' top 20 has no event site; 'sovereign ai india' (210/mo) is led by Sarvam, PIB, Wikipedia, BharatGen, EY, ORF and ThePrint (OpenSEO SERP, 1 Oct 2026). Google News eligibility of cio and egov.eletsonline.com is unverified.

**Expected effect:** Referral traffic of tens to low hundreds of sessions across all pieces, more when pushed in portal newsletters; organic traffic to worldaisummit.com from these pieces is about zero in the window. Deep links may move a few speaker pages from #6-#10 towards the top 5 if Google recrawls before 17 Oct. PR1 lands two days before the event, too late for most B2B delegates; PR2 and PR3 mainly feed award winners' publicity, 2027 interest and sponsor enquiries. Lead quality (CIO, BFSI, GCC and government readers) is the main value, and the day-of pieces would probably happen anyway.


**Decisions needed**

- Programme team to supply speaker-to-track assignments before any track framing is published
- Edition number (2nd or 3rd) to use in all copy
- Budget approval for a paid India wire for PR2
- KDEM agreement to republish PR2 or PR3
- Which of the five sector previews and five news pieces the desks can actually staff

**Assets:** A43, A37, A48, A70


### B5. On 2 Oct, give the Elets network something to link to: www Search Console property, /agenda/ v1, homepage 'Latest' block, sitemap lastmod, then a brand-only publishing calendar to 17 Oct

**Impact 3/10, confidence medium, effort M: about 2 hours web dev and 2 hours content lead to set up on 2 Oct, then about 2-4 hours a day of content work to 17 Oct, owner web dev (GSC, /agenda/, homepage block, sitemap, redirects); content lead (calendar owner); programme team (session data), by 2 Oct 2026 for the www GSC property, /agenda/ v1, homepage block and sitemap; /awards/winners-2026/ before 14 Oct night; calendar items per A45 to 17 Oct.**


**Do this**

- 2 Oct: add a www Search Console property (URL-prefix https://www.worldaisummit.com/ or a Domain property); only the non-www property is connected now, so new www URLs cannot be submitted or inspected.
- 2 Oct: publish /agenda/ v1 at https://www.worldaisummit.com/agenda/ (currently 'URL is unknown to Google'; /agenda without slash shows 'Server error (5xx)', last crawl 26 May 2026) and redirect /agenda to /agenda/; the only agenda page today is /1st-edition/world-ai-agenda.html (89 words, titled 'World AI Summit 2025'). Session content comes from the programme team (PLACEHOLDER_SESSION_DATA), since speakers.json has session null for all 76 entries.
- 2 Oct: add a 'Latest from the Summit' block in or just below the homepage hero listing the 3 newest URLs; the homepage ranks #1 for brand queries and is the most-crawled page, so links from it are the fastest route to discovery.
- Give every new URL a sitemap.xml entry with an accurate <lastmod> and resubmit the sitemap after each publish.
- Update https://www.worldaisummit.com/awards/ (already organic #2 for 'world ai awards 2026' on the non-www URL, behind globalaiaward.com) with categories, PLACEHOLDER_AWARD_FEE and PLACEHOLDER_AWARD_DEADLINE, and build /awards/winners-2026/ before PR2 on 14 Oct; fix the expired Standard row on /delegate/ (shared with B1).
- Run the A45 calendar for 2-17 Oct for brand-modified items only (agenda, speakers, live, highlights, winners); skip generic news-topic pages on worldaisummit.com, which will not reach the top 20 before 17 Oct. Every item gets a dated byline, at least one contextual link each to /delegate/, /agenda/ and /awards/ or the partner page, no invented quotes (emailed Q&As or on-stage remarks only), and only speakers with confirmed_2026=true.
- Hand each calendar item's news angle to the Elets desks (B4) so the Elets piece links to the new worldaisummit.com URL on the same day, which is the network's main crawl path.

**Why**

- OpenSEO audit c1b16b55 (1 Oct 2026): no 2026 agenda URL exists; /delegate/ and /awards/ have no internal links. GSC (non-www only) for 31 Aug-28 Sep 2026 shows 2 page rows: /awards 1,300 impressions, 32 clicks, avg position 7.9, and / 9 impressions.
- 'world ai summit 2026 agenda' (OpenSEO SERP, India, 1 Oct): worldsummit.ai #1, impact.indiaai.gov.in #2, www.worldaisummit.com/ #3, bennett.edu.in #4, with an AI Overview above all. 'world ai summit 2026 speakers': homepage #1, /speaker.html #4, /assets/speaker_details/index.html #14, so brand-modified pages from this domain rank quickly.
- 'world ai awards 2026': worldaisummit.com/awards (non-www) is organic #2 with title 'World AI Awards 2026 | Celebrating AI Excellence' and snippet '14th - 15th October 2026' (verifier, 1 Oct); the awards item improves a page that already ranks, it does not create a new ranking.
- 19,511 of 19,826 backlinks come from eletsonline.com, so the Elets network is the main crawl and discovery path for new pages; worldaisummit.com has about 10 real non-Elets referring domains (project context).
- OpenSEO returned no volume for 'world ai summit 2026 agenda', 'world ai awards 2026' or 'world ai summit highlights', so the size of brand-modified demand is unknown.

**Expected effect:** Brand-modified pages (agenda, speakers, live, highlights, winners) can realistically be indexed and in the top 3 within 1-3 days once linked from the homepage, but the homepage already holds #1 for the main brand queries and #3 for '2026 agenda', so new pages mostly move clicks off the homepage rather than add sessions. Expect low hundreds of extra organic sessions across the window at most, plus Elets referral clicks. The real gain is that B4's links stop pointing at URLs that error, which is what happened with the 2025 /agenda links, and that /agenda/ and an updated /awards/ page support conversion in event week.


**Decisions needed**

- Programme team to release session and track data for /agenda/ v1
- Awards ceremony day, 2026 nomination deadline and fee for the /awards/ update
- Who owns the calendar day to day
- Whether the Elets sites are Google News publishers (unverified) which affects how much to lean on day-of pieces

**Assets:** A45


**Conflicts noted**

- Mailer share of sessions: F37 title says about 93%; the verifier computed about 92% (263,703 of about 285,600 sessions, GA4 Jul-Sep 2026).
- Pass price: homepage says Rs 20,000; /delegate/ (Exa, 1 Oct 2026) shows 'Standard Access (Valid till 30th Sept 2026) Rs 20,000 / Rs 35,000' and 'Late Access Rs 30,000 / Rs 60,000'; all 50 speaker-page meta descriptions say 'Passes from Rs 20,000' (audit c1b16b55).
- Award fee: /award.html says 'Entries from 30k + GST'; project memory and task context give Rs 18,000-20,000 + GST as the 2025 fee.
- Group discount: task context says 10% off for 3+ delegates; the F47 verifier did not find it in the /delegate/ text fetched on 1 Oct 2026.
- Delegate count: the 22 Sep CIO article and the WAIS 'Beyond the Hype' blog copy say '1,200+ delegates'; the 30 Sep CIO article and /ai-conference-bengaluru-2026.html say '1,000+'.
- Edition number: LinkedIn showcase page says '2nd Edition' and Sept 2026 LinkedIn posts say '3rd Edition' (F79); A34 notes site pages say '2nd'.
- CIO article 76373 (24 Sep): F40 says it has 'the same old track list' (seven) and ends with a bare homepage URL; the verifier found six old tracks (no GCCs) in the closing paragraph and no closing homepage URL in the Exa text, which may drop some elements.
- 'aman mittal ias' volume and Elets ranking: F47 gives 260/mo and says the egov article is unnumbered organically; the verifier says speakers.json gives 480/mo for 'aman mittal' and the egov 2023 article is organic #10 (overall rank 13), with the eletsegov Facebook post organic #6 (overall 8).
- elets.net referral in Jul-Sep 2026: F38 says 1 session; the verifier only confirmed it is not in the 2026 top 40 and did not check the figure of 1.
- 2025 egov referral comparison: F38 presents 4,153 vs 27 as like-for-like; the verifier notes the 2025 period included the 25-26 Sep 2025 event itself, so the drop is overstated.
- worldsummit.ai Amsterdam dates: the SERP snippet says '05-09 October 2026, Amsterdam'; project context says 7-8 Oct (F49 verifier, unresolved).
- Per-article referral estimate: F40 estimates 10-20 sessions per retrofitted article; the verifier measured about 2.5 sessions a week from the one UTM-tagged CIO article (21 sessions in Jul-Sep 2026) and zero cio.eletsonline.com referral sessions overall in Q3.

## Theme: World AI Awards


### C1. Rebuild https://www.worldaisummit.com/awards/ into the one indexable World AI Awards 2026 page: categories, fee, deadline, how-to-nominate, FAQ, judging, title and JSON-LD

**Impact 3/10, confidence medium, effort S-M: about 30 min awards team for the facts; 2-4 h web dev; 1-2 h content for FAQ and judging copy, owner web dev (copy-paste and head tags) + Elets awards team (deadline, 2026 fee, jury, WhatsApp number) + content (FAQ, criteria), by 2 Oct 2026 for the banner, fee and deadline; full rebuild live by 3 Oct 2026 so Google can recrawl before nominations close.**


**Do this**

- Copy from https://www.worldaisummit.com/award.html into /awards/, above the 'Select Sectors' form: the six category groups as one H2 each with every award as plain text (AI Enterprise & Application 26, Business Transformation & Innovation 13, Smart Tech & AI Engineering 16, AI in Governance 4, AI Startups 19, AI Leadership 18; 96 named awards, so the '75+ individual awards' line is safe), the six-step 'How to Nominate' and the benefits list. Do not wait for the awards team for categories; only the deadline and the 2026 fee are missing.
- Replace the H1 (today it is the summit theme, same as the homepage) with 'World AI Awards 2026'. Add a key-facts banner directly above the form: 'Nominations close PLACEHOLDER_DEADLINE (weekday, date, time IST) · Entry fee from Rs PLACEHOLDER_FEE_2026 + GST per entry · Winners honoured at World AI Summit, Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru, 14-15 Oct 2026 (ceremony day to confirm)' with buttons 'Nominate now' (jumps to id=nominate on the form), 'See all categories' (#categories) and 'WhatsApp the awards desk' (number to supply). Repeat 'Start your nomination' after the categories. The auto-close script in A03 swaps the banner on deadline day; swap the title to the closed variant by hand.
- New title at or under 60 characters, for example 'World AI Awards 2026: Nominate by PLACEHOLDER_DEADLINE_SHORT | 75+ Categories' (A03/A61) or 'World AI Awards 2026 | Nominate Now | Bengaluru, 14-15 Oct' (A27). Keep the exact phrase 'AI Awards 2026' and add Bengaluru or Elets so the snippet is distinct from worldawards.ai, which is #1 for 'world ai awards'. Meta: 'Nominations for the World AI Awards 2026 close [date]. 75+ categories across enterprise AI, startups, governance and leadership. Winners honoured in Bengaluru, 14-15 Oct.' Replace the current title 'World AI Awards 2026 | Celebrating AI Excellence'.
- Add short text sections: 'Who can enter', 'Nomination fee' (2026 figure only; do not print the 2025 Rs 18,000 / Rs 20,000 tiers, which were discounted prices and would contradict /award.html's 'Entries from 30k + GST'), 'Deadline', 'Evaluation criteria' (an Innovation / Impact / Quality style block, confirmed by the awards team) and 'How entries are judged'. Name the 2026 jury only with names and designations the members supply; otherwise describe the process. Do not reuse the 3 'Past Jury Members' on /1st-edition/awards.html as 2026. Create /awards/jury/ only if at least 5 members of a confirmed 2026 jury agree to be listed.
- Add an 8-10 question FAQ from A65 (with its 2025 fee lines removed): more than one category, can startups enter, is there a jury, is a delegate pass included, what the form needs (project overview, problem solved, scale, budget, stakeholders, one supporting document up to 10MB, a logo), payment and GST invoice. FAQPage JSON-LD is optional; Google has shown FAQ rich results mainly for government and health sites since 2023, so the value is on-page conversion and long-tail matching.
- Link to https://www.worldaisummit.com/1st-edition/awards.html as the '2025 edition' page (it carries the 2025 categories and past jury; a winners list was not confirmed in the first 5,000 characters). Do not link /awards/winners-2025/, which is unknown to Google and absent from the crawl.
- On the existing Event JSON-LD on /awards/, add organizer (Elets Technomedia), offers (fee, priceCurrency INR, validThrough = deadline) and performer; URL Inspection on 1 Oct shows the Events rich result passing with these three as warnings. Publish the offers block only after the fee is confirmed.
- Checks before upload: no PLACEHOLDER_ left (grep -rn PLACEHOLDER_ .), one title and one canonical per page, 360 px phone view with no sideways scroll, #nominate and #categories anchors, WhatsApp link on a phone. Then do C2 and request indexing. Measure: baseline 32 clicks from 1,300 impressions at position 7.9 (GSC non-www, 31 Aug-28 Sep); compare 14 days after launch with 14 days before; take the paid nomination count from the awards team, not from GA4 form_submit.

**Why**

- /awards is the only non-brand page earning Search Console clicks: 79 clicks from 2,419 impressions, CTR 3.3%, average position 9.1 (GSC non-www property, 28 Jun-28 Sep 2026); other pages had 5 clicks combined. Last 28 days: 32 clicks, 1,300 impressions, 2.5% CTR, position 7.9 (31 Aug-28 Sep).
- Query demand on the page, 3 months: 'ai awards 2026' 243 impressions at 9.2 (7 clicks); 'ai awards' 199 at 9.8 (6 clicks); 'world ai awards' 66 at 3.1 with 0 clicks; 'ai awards india' 57 at 8.8; 'best ai leaders awards' 27 at 10.5; 'aiawards' 26. Live India SERP 1 Oct: 'world ai awards' #2 behind worldawards.ai (an unrelated brand); 'ai awards 2026' #4; 'ai awards' #6; 'ai awards india' #8 (Cypher #1, ET Enterprise AI #2); 'ai awards india 2026' not in the first 20.
- The page body is bare: Exa fetch and OpenSEO audit c1b16b55, 1 Oct 2026, show 564 words, the summit theme as H1, date, venue and the form only; no categories, fee, deadline or criteria. Position 3 with 0 clicks on 'world ai awards' points to a snippet that does not answer the searcher.
- The full 2026 content already exists on /award.html (Exa, 1 Oct): 96 named awards in 6 groups, '75+ individual awards, Entries from 30k + GST', 'Nominations are open for the upcoming edition', a six-step How to Nominate and five benefits, but it is canonicalised to the homepage, carries the homepage title and is 'URL is unknown to Google' (inspect_urls).
- Competitor benchmark: Cypher's 'AI Awards India 2026' page (#1 for 'ai awards india 2026') has 36 named categories across 7 pillars, a deadline box, Innovation/Impact/Quality criteria and winners pages back to 2017 (Exa, 1 Oct). GSC 16 months shows process queries landing on /awards with poor positions: 'ai awards open for nominations' at 23, 'ai awards shortlist' at 15.

**Expected effect:** Traffic: small. Baseline about 19-20 clicks over 1-17 Oct (32 clicks per 28 days). A distinct title and a 'Nominations open' snippet could add roughly +3 to +25 extra clicks in the window after Google recrawls (verifier range: +3 to +10 on F22, +10 to +25 on F70, +10 to +20 on F03). India sends only about 10 impressions and 0.25 clicks a day to /awards; most of the 32 monthly clicks come from other countries. Moving 'ai awards 2026' or 'ai awards india' into the top 3 within two weeks is possible but not likely. Leads: the real gain is conversion of visitors who today cannot see categories, fee or deadline without opening the form; each nomination is a paid entry (2026 fee unknown; /award.html says from Rs 30,000 + GST) and the 2025 checkout bundled a delegate pass. Number of extra nominations: unknown.


**Decisions needed**

- 2026 nomination deadline (date and time IST), at least a few days before 14 Oct for jury work
- 2026 entry fee: one fee or two tiers, and whether '+ GST' or inclusive; it must match /award.html's 'Entries from 30k + GST' or that line must change
- Ceremony day (14 or 15 Oct) and time slot; the 2025 ceremony was on day 1 per Elets' LinkedIn post
- Whether the six steps on /award.html ('Sign up / Log in', 'Complete Your Nomination Fee') still match the 2026 form, and whether payment happens on a separate checkout
- Whether a delegate pass is included with a nomination, and the multi-entry rule
- 2026 jury names and designations, or process-only wording
- Awards desk WhatsApp number (91XXXXXXXXXX) and confirmation that secretariat@worldaisummit.com is the awards contact

**Assets:** A61, A52, A09, A27, A65, A03


### C2. Protect the ranking URL while consolidating: one-hop 301 from non-www /awards to www /awards/, fix /award.html's canonical, add a www Search Console property and request indexing

**Impact 2/10, confidence medium, effort S: about 1 h web dev plus 30 min for Search Console and mailer team, owner web dev (redirect rules, canonicals); marketing (Search Console property, mailer links), by 2 Oct 2026, before or together with C1 going live.**


**Do this**

- Record the current state before touching anything. Google URL Inspection (1 Oct): https://worldaisummit.com/awards is 'Submitted and indexed', Google-selected canonical is that same non-www URL, last crawled 28 Sep 2026 18:25 UTC with a 200. OpenSEO crawl c1b16b55 (1 Oct): non-www /awards now returns 301 to https://www.worldaisummit.com/awards. https://worldaisummit.com/awards/ (with slash) and /award.html report 'URL is unknown to Google'. So the redirect went live between 28 Sep and 1 Oct and Google has not consolidated to www yet.
- Do not change the /awards/ URL and do not add hops. Make https://worldaisummit.com/awards (and /awards/) reach https://www.worldaisummit.com/awards/ in a single 301, not non-www -> www /awards -> /awards/. Put a self-referencing canonical on /awards/. Verify with curl -sI on all four host and slash variants; each should show one 301 to the www slash URL and the final page a 200.
- /award.html: today, change its canonical from / to https://www.worldaisummit.com/awards/ and give it its own title and meta plus a 'Nominate now -> /awards/' button in two places (A03 snippets 8-9). Once /awards/ carries the categories (C1), replace the canonical with a 301 from /award.html to /awards/ (A61, A52 rules; Apache and nginx versions in A03 snippet 10).
- Keep mailer traffic working: /award.html had 25,603 views and 18,849 users in GA4 Jul-Sep at about 2 s per user. Ask the mailer team to point future awards mailers straight at https://www.worldaisummit.com/awards/ with UTM tags, so the 301 is a safety net rather than the main path.
- In Search Console, add a www URL-prefix property or a Domain property. The current non-www property is the only one connected, and its /awards data will drop out once Google moves to www. Then use URL Inspection 'Request indexing' for https://worldaisummit.com/awards and https://www.worldaisummit.com/awards/ after C1 is live.
- Expect short ranking or snippet churn on /awards during the event window while Google follows the redirect; make no other URL or slug changes to awards pages until after 17 Oct. Re-check the Events rich result warnings (performer, offers, organizer) after the JSON-LD change.

**Why**

- Google's indexed and self-selected canonical is the non-www, no-slash https://worldaisummit.com/awards, last crawled 28 Sep 2026 with a 200 (URL Inspection, 1 Oct); the 1 Oct crawl shows that URL now 301s to www, so consolidation is pending during the two weeks that matter.
- https://worldaisummit.com/awards/ and /award.html are 'URL is unknown to Google' (inspect_urls, 1 Oct); /award.html carries the homepage title and a canonical to /, so its 96-award content counts for nothing in search.
- Search Console is connected only for the non-www URL-prefix property, so www impressions for /awards/ are invisible today (context, 1 Oct 2026).
- GA4 Jul-Sep: /award.html 25,603 views and 18,849 users at about 2.0 s engagement per user (38,457 s total); /awards/ 876 views, 512 users, 79 key events (generic form_submit, not confirmed paid). The r.emails.elets.in referral converts at 0.06%, which points to link-scanner hits rather than 18,000 real nominators.

**Expected effect:** No direct traffic gain. This is insurance for the only non-brand page earning clicks (about 19-20 clicks over 1-17 Oct at the current rate): a one-hop redirect, a self-canonical and the /award.html consolidation reduce the chance of ranking or snippet churn while Google moves from non-www to www, and let the C1 title show sooner after recrawl. Leads: none directly; it keeps mailer visitors to /award.html flowing to the page that now has a nominate button.


**Decisions needed**

- Whether /award.html becomes a 301 to /awards/ (recommended once C1 is live) or keeps a canonical to /awards/ because mailers still link to it
- Who holds Search Console ownership to add the www or Domain property

**Assets:** A21, A03, A61


### C3. Make the open nomination window visible sitewide: homepage awards block, nav and footer links, deadline banners on event pages and blog posts, and retire the 2025 elets.net awards checkout

**Impact 3/10, confidence high, effort S: 1-2 h web dev; 30 min Elets web team for elets.net, owner web dev / marketing for worldaisummit.com; Elets web team for elets.net, by 2 Oct 2026, so the banner runs for the full remaining window.**


**Do this**

- Homepage https://www.worldaisummit.com/: replace the awards block that ends 'Honouring the AI that's actually working ... World AI Awards · Previous edition' with a dated CTA to /awards/ (copy in A62): 'World AI Awards 2026: nominations close PLACEHOLDER_DEADLINE. Nominate now'. Add 'Awards' to the main nav and the footer; /awards/ has only 4 internal links today and is missing from the nav.
- Add a one-line deadline banner linking to https://www.worldaisummit.com/awards/ with the anchor 'World AI Awards 2026' on /delegate/, /ai-conference-bengaluru-2026.html, /speaker.html and the 5 blog posts. In the 'Beyond the Hype' blog post, link the existing mention of the World AI Awards 2026 to /awards/.
- Present the open window as the only fact: 'Nominations close [DD] Oct'. Use the same line in social posts and in outreach to nominators whose other options have closed (Cypher's deadline was 9 Sep 2026, aim.media lists 16-17 Sep; the ET Enterprise AI Awards ceremony was 17 Sep 2026 at Conrad Bengaluru). Do not mention competitors on the page.
- Elets web team: https://elets.net/worldaisummit-awards/ is titled 'Elets World AI Summit 2025', shows the 2025 fees (INR 18,000 + GST per entry for Startup & Individual, INR 20,000 + GST for Enterprise, Government, Leadership, Solution Provider) and still has a live checkout (Conference Attendee Pass INR 30,000). Either update it to 2026 copy with a prominent link to /awards/ or 301 it to https://www.worldaisummit.com/awards/ (rules in A62), so no 2025 payment is taken by mistake.
- Before pasting A62: change its /awards/winners-2025/ link to /1st-edition/awards.html or drop it (the URL is unknown to Google and absent from the crawl); keep '75+ awards' only on the strength of the 96 named awards on /award.html; remove any fee figure until the 2026 fee is confirmed.
- Add a UTM or a GA4 click event on the homepage awards CTA, because the homepage-to-/awards/ click path is not measured today; report homepage CTA clicks and /awards/ form_submit weekly against the week before.

**Why**

- Every visible awards signal on the site points to the past: the homepage awards section reads 'World AI Awards · Previous edition' with no date or nomination CTA (Exa read, 1 Oct 2026), and no page states the 2026 deadline, fee or ceremony date.
- Homepage traffic is far larger than /awards (about 32 organic clicks a month to /awards, GSC non-www 31 Aug-28 Sep); all event rankings land on the homepage, so that is where the visitors are. /awards/ has 4 internal links and is not in the nav (audit c1b16b55).
- A 2025 Elets checkout is still live: elets.net/worldaisummit-awards/ shows '2025', 'INR 18,000 + GST per entry', '20,000 + GST' and a checkout of 'INR 30000' (Exa read, 1 Oct).
- Timing: Cypher (deadline 9 Sep 2026) and the ET Enterprise AI Awards (ceremony 17 Sep 2026) have closed, so in October WAIS is likely one of the few India AI awards still taking entries (inferred from these two checks only).

**Expected effect:** Little or no new search traffic (no target queries). The gain is conversion: it acts on visitors already on the site and takes effect as soon as it is deployed, with no wait for Google. The homepage-to-awards click-through is not measured, so the uplift in nominations is unknown; each nomination is a paid entry (2026 fee to confirm) and nominees attending the ceremony are likely delegate-pass buyers. Retiring the 2025 checkout avoids lost or mis-routed payments.


**Decisions needed**

- The 2026 nomination deadline (needed for every banner)
- elets.net/worldaisummit-awards/: update to 2026 copy or 301 to /awards/
- Whether social and outreach posts may say 'nominations still open' this week

**Assets:** A62


### C4. After the ceremony, publish the World AI Awards 2026 winners on the awards URL and ask each winner to link to it

**Impact 2/10, confidence low, effort S: 1-2 h on 15-16 Oct, plus winner emails, owner content + web dev; awards team supplies the winners list, by 15-16 Oct 2026.**


**Do this**

- Decide the URL now: PLACEHOLDER_WINNERS_URL. Option A (F22): replace the form on https://www.worldaisummit.com/awards/ with a 'World AI Awards 2026 winners' section on the same URL to keep its rankings. Option B (F57): a new https://www.worldaisummit.com/awards/winners-2026/ page by year, as Cypher keeps 2017-2025, linked from /awards/.
- Late on the ceremony day (14 or 15 Oct, to confirm), publish the winners list with organisation and category under the same six category groups; keep the category list and the 2025 edition link in place. Swap the /awards/ title to the 'closed' variant from A03 on deadline day, then to a winners title on publication.
- Email each winner the URL and a winner badge so they link to it from their site and LinkedIn; add a 'Winners announced' link from the homepage awards block (C3) in place of the deadline line.
- Keep the Event JSON-LD and the nomination FAQ; mark nominations as closed and point enquiries to secretariat@worldaisummit.com for the next edition.

**Why**

- /awards is the only non-brand URL with Search Console demand (79 clicks, 2,419 impressions, 28 Jun-28 Sep 2026), so winners content on or linked from it reuses that equity.
- Cypher's awards page keeps winners pages by year back to 2017 and ranks #1 for 'ai awards india 2026' (OpenSEO SERP and Exa, 1 Oct 2026); WAIS is not in the first 20.
- /1st-edition/awards.html lists 2025 categories and 3 past jury members, but a 2025 winners list was not confirmed in the first 5,000 characters (F28 verifier), so there is no winners page for Google to rank today.

**Expected effect:** Almost nothing inside 1-17 Oct: the content can only go live on 14-15 Oct and winner links arrive after the window. Longer term it earns links and ranks for winner and category names; the size is unknown. No lead effect in the window beyond keeping the awards page useful after nominations close.


**Decisions needed**

- Same-URL winners section (F22) or a separate /awards/winners-2026/ page (F57)
- Ceremony day and when the winners list may be published
- Whether a winner badge or logo kit exists

**Assets:** A21


**Conflicts noted**

- 2025 nomination fee: F09, F22 and F28 say a flat Rs 18,000 + GST per entry; the verifiers (elets.net/worldaisummit-awards/, Exa, 1 Oct) show two tiers, Rs 18,000 + GST for Startup & Individual ('Save Rs 5,000') and Rs 20,000 + GST for Enterprise, Government, Leadership and Solution Provider ('Save Rs 10,000'), both discounted, implying list prices of about Rs 23,000 and Rs 30,000. /award.html (2026) says 'Entries from 30k + GST'. F71 gave 'Rs 18,000-30,000 + GST' per nomination; its verifier says INR 30,000 is the Conference Attendee Pass checkout total, not a nomination fee. The 2026 fee is unknown, hence PLACEHOLDER_FEE_2026.
- Category count: '75+ individual awards' (headline on /award.html) vs 96 named awards (26+13+16+4+19+18, F57 and F70 verifiers, Exa 1 Oct) vs 'about 95' / 'roughly 100 sub-awards' on /1st-edition/awards.html (F57 evidence, F28 verifier). F71 verifier marked '75+' in A62 as unverified; it holds only because /award.html lists 96.
- Redirect state of the ranking URL: F03 and F09 say non-www /awards 'now redirects' to www; F22 verifier shows Google's last crawl on 28 Sep returned 200 with non-www as the selected canonical, and only the 1 Oct crawl shows the 301. Both are consistent if the redirect went live between 28 Sep and 1 Oct, but Google has not consolidated yet. F28 adds that non-www /awards/ with a slash is 'URL is unknown to Google'.
- Mailer users on /award.html: F03 treats about 18,000 users as convertible; its verifier says about 2 s engagement per user and a 0.06% key-event rate on r.emails.elets.in point to largely non-human link-scanner hits (inferred, not confirmed at page level).
- GSC positions differ by window, not by fact: 'ai awards 2026' 9.2 over 28 Jun-28 Sep vs 8.6 over 31 Aug-28 Sep vs live #4 on 1 Oct; 'ai awards india' 8.8 vs 7.8 vs live #8; 'world ai awards' 66 impressions at 3.1 (3 months) vs 44 at 3.0 (28 days), both 0 clicks, live #2; 'ai awards' 9.8 vs 10 vs live #6.
- Winners URL: F22 says replace the form on /awards/ (same URL) to keep rankings; F57 says publish a separate /awards/winners-2026/ page by year. Kept as PLACEHOLDER_WINNERS_URL in C4.
- Past winners link: F09, F28 and F57 propose linking 'Past winners' or a 'Hall of Honour' to /1st-edition/awards.html, but the F28 verifier found jury names and no winners list in the first 5,000 characters; A62 links /awards/winners-2025/, which is unknown to Google and absent from the crawl.
- Two-week traffic estimates: F22 claimed 25-40 clicks total in the window; its verifier puts the baseline at about 19-20 clicks and the extra at +3 to +10. F70 says +10 to +25, F03 +10 to +20, F28 10-40, F57 +15 to +50. Used the verifier range of +3 to +25 extra clicks.

## Theme: Agenda, speakers, content, blog, homepage FAQ


### D1. Consolidate the speaker directory on /speaker.html and correct speaker pages before anyone shares them

**Impact 2/10, confidence medium, effort S-M: about 4-5 hours web dev and content in total (1-2 h corrections by 2 Oct, about 3 h directory merge by 5 Oct); 15 minutes secretariat, owner web dev + content; Elets secretariat for the Kharge confirmation, by 2 Oct 2026 for the Kharge and title fixes; 5 Oct 2026 for the directory merge.**


**Do this**

- By 2 Oct, on /assets/speaker_details/priyank-kharge.html replace the meta description and About paragraph portfolio 'Minister for Electronics, IT & Biotechnology and Rural Development & Panchayat Raj' with the current 'Minister for Home (excluding Intelligence), IT-BT and e-Governance, Government of Karnataka' (Deccan Chronicle 4 Jun 2026, The Hindu 5 Jun 2026); use 'then Minister for ...' where the 2025 context needs it. The page header and the /speaker.html text are already current, so no secretariat ruling on the portfolio is needed.
- Elets secretariat settles PLACEHOLDER_KHARGE_2026_STATUS (three sources disagree: /speaker.html says 'Welcoming Shri Priyank M Kharge', the page title says 'Chief Guest | World AI Summit 2025', speakers.json has confirmed_2026: false). If confirmed, retitle the page to a 2026 framing, add his session and link it from the 'Welcoming' block; if not, relabel that block as 2025 Chief Guest or remove it.
- Give role-led titles to the shared-name speaker pages: 'Pankaj Kumar Pandey, IAS | Principal Secretary, e-Governance, Karnataka | World AI Summit 2026' (an Uttarakhand IAS namesake is #1), 'Sanjeev Kumar Gupta | CEO, KDEM | World AI Summit 2026', 'Shalini Kapoor | Chief Strategist, Data and AI, EkStep | World AI Summit 2026', 'Harsh Vardhan | AI and Digital Innovation, Apollo Tyres | World AI Summit 2026'. Vishal Chugh's title already carries a role, so leave it.
- By 5 Oct, server-render on https://www.worldaisummit.com/speaker.html (124 words today, names one person) the grouped list of 50 confirmed 2026 speakers that already exists as HTML on /assets/speaker_details/index.html (Government, policy and regulators; Enterprise and technology leaders; Founders, investors and ecosystem builders), each name linking to its profile.
- Add a 301 or canonical from /assets/speaker_details/index.html to /speaker.html so one directory competes instead of two (#7 and #11 today for 'world ai summit speakers'); give /speaker.html its own title, meta description and H1 instead of the homepage meta it shares.
- On every speaker profile add a 'Book your pass to hear [Name]' button to /delegate/ and a 'See the agenda' link to /agenda/ (D2); show no price in the button or in speaker-page meta descriptions until PLACEHOLDER_CURRENT_PASS_PRICE is settled.
- Fill session, time and hall on each profile as soon as the programme is final (each page currently says this 'will be published on this page once the agenda is final'); do not publish the local /speakers/<slug>/ generator output as a third directory unless it replaces /assets/speaker_details/ with 301s.
- Low priority and only after KDEM confirms: the Sanjeev Gupta page says he was Lahari MD & CEO 2018-2022 while karnatakadigital.in/about-us/ says he 'is also the MD & CEO of Lahari'; the verifier found this unsupported, so do not edit without confirmation.

**Why**

- Exa fetch 1 Oct 2026: /speaker.html H1 '100+ speakers, one room in Bengaluru.' names only Priyank Kharge; /assets/speaker_details/index.html lists '50 confirmed speakers so far'. Audit c1b16b55: /speaker.html is thin (124 words) and shares its meta with the homepage; profile pages are sitemap-only (crawl depth null).
- 'world ai summit speakers' (context, 1 Oct 2026): homepage #2, /speaker.html #7, /assets/speaker_details/index.html #11; worldsummit.ai (Amsterdam) is #1 and takes 4 of the first 8 organic results.
- The Kharge page contradicts itself (Exa fetch 1 Oct 2026): header 'Minister of Home Affairs, IT/BT and E-Governance'; meta and About 'Minister for Electronics, IT & Biotechnology and Rural Development & Panchayat Raj'; title 'Shri Priyank Kharge | Chief Guest | World AI Summit 2025'. Since the 4-5 Jun 2026 allocation he holds Home (excluding Intelligence), IT-BT and E-Governance; RDPR went to Eshwar Khandre (Deccan Chronicle, The Hindu, egov.eletsonline.com).
- 'priyank kharge' 49,500/mo with no event site in the top 20; Cypher's speaker page held #7 for it (project memory, 26 Sep). 'pankaj kumar pandey' 320/mo, WAIS page #10. Four of the five named speaker titles lack a role (crawl c1b16b55).
- GA4 Sep 2026: /speaker.html had 38 views and no /assets/speaker_details/ page appears in the top rows, so this is mainly a trust and conversion fix, not a traffic fix.

**Expected effect:** Organic traffic in 1-17 Oct close to zero: the speakers query is low-volume brand navigation with an AI Overview and the homepage already sits at #2; ranking for 'priyank kharge' in two weeks is not realistic (page 2-3 entry is plausible only if he is confirmed and the page is corrected and linked). Clearer titles may lift CTR a little on 'pankaj kumar pandey' (#10, 320/mo). The real value is that speakers and KDEM share correct pages during event week and that those pages now carry a booking button; the lead effect is unmeasured.


**Decisions needed**

- Is Priyank Kharge confirmed for 2026 (speakers.json says no, /speaker.html implies yes)?
- Current live pass price to show, if any, on speaker-page CTAs (homepage Rs 20,000 vs /delegate/ Late Access Rs 30,000/60,000)
- Whether the local /speakers/<slug>/ generator replaces /assets/speaker_details/ (with 301s) or is not deployed

**Assets:** A39, A11


### D2. Publish the 2026 agenda page at /agenda/ with day-by-day tables, booking buttons and session-level links

**Impact 3/10, confidence medium, effort M: web dev 3-4 hours for template, JSON-LD and links, plus daily updates; programme team must supply the running order, owner Elets programme team (session data) + web dev (template, JSON-LD, links) + content, by v1 by 2 Oct 2026 if the running order exists, otherwise by 6-7 Oct; final with halls by 13 Oct 2026.**


**Do this**

- Programme team hands over the running order by PLACEHOLDER_AGENDA_DATA_DATE (this is the bottleneck: speakers.json has session = null and empty time and hall for all 76 entries). Web dev builds https://www.worldaisummit.com/agenda/ (choose one URL; findings used /agenda/ twice and /agenda.html once) with title 'Agenda | World AI Summit 2026, 14-15 Oct, Bengaluru', an H1, a 'last updated' date and 'Programme subject to change'.
- Structure: Day 1 (Wed 14 Oct) and Day 2 (Thu 15 Oct) tables with Time | Session title | Format (keynote, panel, fireside, masterclass) | Track (one of the 7) | Hall | Speakers linked to profiles; track anchors #frontier-models-compute, #sovereign-ai, #enterprise-ai, #gcc, #robotics-agents, #ai-for-bharat, #capital-founders-exits; include registration opening, the World AI Awards ceremony and the VIP networking dinner, and mark VIP-only sessions and roundtables.
- If sessions are not final, publish the 7 tracks with the sessions confirmed so far, TBA cells and the line 'full schedule updated daily' (Cypher's /schedule ranks while saying it is still finalising); do not draft sessions or list unconfirmed speakers; update daily and bump sitemap lastmod; final version with halls by 13 Oct.
- Optional depth once the programme team supplies them: 3-5 'Talking points' bullets under each session (Inc42 format). Do not invent them.
- Conversion: 'Book your delegate pass' button beside each day and after each half-day to /delegate/; 'Sponsor a session' link to partnerships@worldaisummit.com; optionally a 'Download the agenda (PDF)' button behind a 5-field form (name, work email, phone, company, designation) delivering to registration@worldaisummit.com, with a thank-you page, so the sales team has named leads to call 7-13 Oct (PLACEHOLDER_GATE_PDF: yes or no).
- Add Event JSON-LD with one subEvent per session; take the Offer price from whatever /delegate/ shows after the price decision and do not publish a partial offers block. In parallel fill session, time and hall in speakers.json; build_speakers.py already emits subEvent inside performerIn once session.title is filled.
- Link /agenda/ from the homepage nav and hero ('Seven tracks. One agenda' section, which today has no agenda link), /delegate/, /speaker.html, every speaker profile ('See the agenda'), /ai-conference-bengaluru-2026.html and all 5 blog posts; add it to sitemap.xml.
- /1st-edition/world-ai-agenda.html (89 words, title 'World AI Summit 2025', body is contact blocks): add a banner 'Looking for the 2026 agenda?' linking to /agenda/, or 301 it. Low priority, because the verifier found it hardly competes.

**Why**

- Audit c1b16b55 (100 pages) has no 2026 agenda URL; Exa returned CRAWL_NOT_FOUND for /agenda.html and /agenda/ on 1 Oct 2026. The only agenda URLs are /1st-edition/world-ai-agenda.html (89 words, 2025) and /1st-edition/what-to-expect-world-ai-summit-2025-agenda-highlights (302 to /1st-edition).
- The site promises the page in its own words (Exa fetch 1 Oct 2026): /assets/speaker_details/index.html says 'Session times and halls are confirmed on each speaker page and on the agenda once the programme is final'; speaker pages say 'Session title, time and hall will be published on this page once the agenda is final'; the homepage heading is 'Seven tracks. One agenda' with no times.
- OpenSEO SERP India 1 Oct 2026, 'world ai summit 2026 agenda': worldsummit.ai #1, impact.indiaai.gov.in #2, worldaisummit.com homepage #3, bennett.edu.in #4; for 'world ai summit bengaluru agenda' the homepage is already #1 and /speaker.html #8.
- Demand is near zero: Search Console (non-www property, 1 Jun 2025 to 28 Sep 2026) has no query pairing 'world ai summit' with 'agenda' or 'schedule'; the only related row is 'ai summit agenda' with 45 impressions, position 13.6, 0 clicks; OpenSEO shows no measurable India volume for branded agenda queries and 'ai summit agenda' was 0 in Aug 2026 (140/mo on the annual average).
- Competitors treat the agenda as the main CTA: worldsummit.ai hero 'Download 2026 Agenda'; Cypher /schedule has 'Download PDF' and ranks #7 for 'ai conference' (1,300/mo); events.inc42.com/ai-summit/ lists time slots with 'Talking Points'.

**Expected effect:** Organic traffic in 1-17 Oct: single or low double digits of visits from branded agenda and schedule searches, since Search Console shows no such demand and the homepage already ranks #1 or #3 for the variants. Overtaking worldsummit.ai for 'world ai summit 2026 agenda' is possible but not certain. The value is conversion: delegates choosing day 1 vs day 2 and Premium vs VIP, sponsors seeing a concrete programme, and, if gated, named PDF leads for the sales desk. The lead effect is unknown and depends entirely on the programme team supplying sessions.


**Decisions needed**

- Programme team: date by which a near-final running order (sessions, times, halls, speakers) can be supplied
- Gate the PDF download behind a form or leave it open
- Final URL: /agenda/ or /agenda.html
- Offer price for the Event JSON-LD (depends on the live pass price decision)
- Which speaker profile URL the agenda links to: /assets/speaker_details/<slug>.html or /speakers/<slug>/

**Assets:** A46, A53, A12


### D3. Homepage and /delegate/: dated title, shorter meta, key-facts block and a fact-first FAQ rewritten in place for the 'ai summit 2026' cluster

**Impact 3/10, confidence medium, effort S: about 3-4 hours in total (title and meta under 1 h; key-facts block and FAQ rewrite about 2 h; /delegate/ H1, links and redirect about 1 h), owner web dev + content (homepage, /delegate/, indiaaisummit.in banner), by 3 Oct 2026 (Google needs about a week to re-crawl before the 9-14 Oct window).**


**Do this**

- By 3 Oct change the homepage title to 'World AI Summit 2026 | 14-15 Oct, Bengaluru | Register Now' (58 characters); the current SERP title 'World AI Summit 2026 | AI Summit India, Bengaluru, 14-15 ...' is cut off so 'October' is lost. Keep 'World AI Summit 2026' first to protect the four #1 brand rankings.
- Replace the 182-character meta description, which Google is rewriting, with one short version (A26 gives 157 characters, A17 gives 149; pick one). Do not open with 'India's next AI summit' or 'India's AI summit' (Cypher 2026 runs 7-9 Oct 2026 at KTPO Whitefield, Bengaluru) and do not state '100+ speakers' unless verified (speakers.json has 50 confirmed 2026 speakers).
- Directly under the hero add a 120-200 word 'AI Summit 2026 in Bengaluru: key facts' block: date, venue, 7 tracks, who attends, and a 'Book delegate pass' link to /delegate/.
- Rewrite the existing homepage FAQ in place; do not add a second FAQ block. Each question becomes an H3 with the fact in the first 25 words: when and where; price (PLACEHOLDER_CURRENT_PASS_PRICE, GST stated); how to register and by when, linking /delegate/ instead of 'register through the official website'; is it free; tracks (replace the current answer listing fintech, healthcare, smart cities and cybersecurity with the 7 official tracks); sponsoring or exhibiting via partnerships@worldaisummit.com; award nominations via /awards/; how it differs from World Summit AI (Amsterdam); and whether it is the India AI Impact Summit (16-20 Feb 2026, Bharat Mandapam, New Delhi) with wording PLACEHOLDER_IMPACT_SUMMIT_ANSWER, because indiaaisummit.in calls the Elets AI Summit Delhi (22 Jan 2026) the 'Official Pre-Summit Event of the AI Impact Summit 2026'.
- Treat the FAQPage JSON-LD in the assets as optional: Google retired FAQ rich results for all sites on 7 May 2026, so the payoff comes from visible text that People Also Ask and AI Overviews can quote (AI Overview on 21 of 22 SERPs, PAA on 21 of 22). Keep the Event JSON-LD.
- /delegate/: add the H1 'World AI Summit 2026 Delegate Passes', set the title 'World AI Summit 2026 Passes | 14-15 Oct Bengaluru | Register' (60 characters) and the asset meta, and link it from the homepage 'Secure your seat' block, the nav and every 'Register' button; apply the /registration redirect from the asset. Today /delegate/ appears in none of the 22 SERPs while the homepage ranks #1 for 'world ai summit 2026 tickets'.
- On indiaaisummit.in (Elets-owned; #10 for 'ai summit india', #13 for 'ai summit') add a top banner 'Next: World AI Summit 2026, Bengaluru, 14-15 Oct' linking to the homepage.
- Keep /ai-conference-bengaluru-2026.html as a supporting page that links to the homepage with the anchor 'AI summit 2026 in Bengaluru'; do not retarget it at the same head terms (D4 covers its own changes).

**Why**

- OpenSEO keyword metrics 1 Oct 2026 (India): 'ai summit 2026' run-rate 6,600/mo in Jul and Aug 2026 (the 40,500 average is inflated by Feb 2026 at 450,000; Oct 2025 was 880); 'ai summit' 1,900/mo; 'ai summit india' 320 (Aug); 'ai summit 2026 india' 140 (Aug); 'world ai summit 2026' 480/mo and rising, homepage #1.
- Live SERP 1 Oct 2026: homepage #7 for 'ai summit 2026' and 'ai summit', #9 'ai summit india', #9 'ai events in bangalore', #15 'ai summit india 2026', #4 'ai summit registration', #10 'ai summit 2026 registration', #3 'ai conference india october 2026'; the top 6 for 'ai summit 2026' are all about the India AI Impact Summit that ended in February; AI Overview at block 1 on all of them.
- Registration demand is small in the window: 'ai summit registration' 10/mo and 'ai summit 2026 registration' 20/mo in Aug 2026 (14,800 and 6,600 in Feb), per OpenSEO get_keyword_metrics 1 Oct 2026.
- Exa fetch 1 Oct 2026: the homepage FAQ is generic, has no date, venue, price, 'is it free' or disambiguation answer, and its registration answer has no link; its topics answer (fintech, healthcare, smart cities, cybersecurity) contradicts the seven tracks shown higher on the page. Live price conflict: homepage Rs 20,000 vs /delegate/ Late Access Rs 30,000 / Rs 60,000 after 30 Sept.
- Project memory: homepage meta is 182 characters; /delegate/ has no H1 and no internal links. Cypher's FAQ H3s mirror the queries ('When and where is the AI Conference 2026 in India?', 'How much do AI Conference 2026 India tickets cost?').

**Expected effect:** Roughly 4,800 searches for 'ai summit 2026' plus 'ai summit' fall in 1-17 Oct at the Jul-Aug run-rate (about 3,000-4,000 for 'ai summit 2026' alone). At #7 with about 3-4% CTR that is about 140 clicks today; a clearer dated title and meta could add about +20 to +60 clicks, and reaching #4-5 would add about +150 to +250, but position gains in two weeks are uncertain and most of these searchers want the February Government summit. AI Overview or PAA citation on 'world ai summit' and the registration queries could add tens of clicks. Lead effect: the FAQ answers price and deadline questions that block purchase and sends people one click from /delegate/; size unknown.


**Decisions needed**

- Which pass price is live from 1 Oct (homepage Rs 20,000 vs /delegate/ Late Access Rs 30,000/60,000) and whether GST is included
- Approved wording for the India AI Impact Summit question, given the Elets AI Summit Delhi was billed as its official pre-summit event
- Which of the two meta description drafts (A17 149 chars or A26 157 chars) to ship
- Whether a speaker count may be stated (50 confirmed vs '100+' on the site)

**Assets:** A26, A25, A17, A50


### D4. Fix wrong facts in the five blog posts and the AI-conference landing page, add 'Bangalore' and booking links, and link both from the homepage

**Impact 2/10, confidence high, effort S: about 3 hours (fact fixes about 15 minutes; CTA box, links, landing-page title, H1 and FAQ additions about 2-3 hours), owner content + web dev, by 4 Oct 2026.**


**Do this**

- By 4 Oct, /ai-conference-bengaluru-2026.html (2,069 words, crawl depth null): set the title to 'AI Conference Bangalore 2026 | World AI Summit, 14-15 Oct Bengaluru', add 'Bangalore' to the H1 ('ai summit bangalore' 320/mo against 'ai summit bengaluru' 40/mo), add the 5 FAQ additions from A25 (the page already has most of the proposed questions and a date/venue block), a short 'AI events in Bangalore 2026' section, a 'Who is speaking' line linking the 50-name /speaker.html, and links to /delegate/ and /awards/.
- Link the landing page from the homepage footer or venue block with the anchor 'AI conference in Bangalore, October 2026' and from all 5 blog posts; use the footer or venue block rather than the nav so 'ai conference bangalore 2026' does not shift from the homepage (#4) to the new page. Add Event JSON-LD from A13 with the same Offer rule as D2.
- 'Beyond the Hype' (/blog/beyond-the-hype-the-room-where-ais-next-chapter-takes-shape.html): replace the paragraph listing the non-official seven tracks (Generative AI & LLMs, AI Agents and Agentic AI, AI Infrastructure & Cloud, AI in Enterprises, AI in Government & Public Services, GCCs, AI Ethics & Regulation) with the 7 official homepage tracks; link 'World AI Awards 2026' to /awards/; link the closing 14-15 October paragraph to /delegate/; set the delegate figure to PLACEHOLDER_DELEGATE_COUNT (the post says '1,200+ delegates', the landing page says '1,000+ Delegates').
- 'The Next Chapter of AI' (/blog/the-next-chapter-of-ai-what-will-define-2026-and-beyond.html): change the H2 'Why Bengaluru Is the Right Place for This Conversation at World AI Summit 2025' to 2026; fix the 'The summit will explore...' paragraph that lists themes that are not the official tracks; link 'World AI Summit 2026, which will take place on 14-15 October 2026 in Bengaluru' to /ai-conference-bengaluru-2026.html.
- In all 5 posts (internalLinkCount 6 each; extracted text ends with only the three email addresses) add an end-of-post CTA box with date, venue, PLACEHOLDER_CURRENT_PASS_PRICE and the buttons 'Book delegate pass' (/delegate/) and 'Nominate for World AI Awards 2026' (/awards/), plus 2-3 in-text links to relevant speaker profiles and a link to /agenda/ once D2 is live.
- Optional: shorten the 5 blog titles (80-91 characters, flagged too long) by dropping the ' | World AI Summit 2026' suffix.

**Why**

- Exa fetch 1 Oct 2026: 'Beyond the Hype' lists the wrong seven tracks and '1,200+ delegates, 100+ speakers and 50+ startups'; the AI-conference page says '100+ Speakers 1,000+ Delegates 50+ Startups 7 Tracks'; the World AI Awards 2026 paragraph has no visible link; the 'Next Chapter' H2 reads 'World AI Summit 2025'. Both posts are dated 2026-09-28.
- Audit c1b16b55: 5 posts of 1,268-2,160 words with internalLinkCount 6 each; 5 blog titles 80-91 characters; AI-conference page title 'AI Conference Bengaluru 2026 | World AI Summit' with crawl depth null, so every event ranking today comes from the homepage.
- OpenSEO 1 Oct 2026: 'ai summit bangalore' 320/mo vs 'ai summit bengaluru' 40/mo; 'ai conferences 2026 india' 390/mo with WAIS outside the top 20 and Cypher #1 organic (live SERP), most of the top 10 being aggregators (conferencealerts.in #2, allconferencealert.com #5, digitalconfex.com #8 and #10); 'ai events in bangalore' Cypher #5, WAIS #9; 'upcoming ai events in india' 90/mo, WAIS #14; 'ai conference october 2026' WAIS #4.
- Cypher's homepage title 'AI Conference Bangalore 2026 | Cypher, Oct 7-9' and its /ai-conference-bangalore-2026 FAQ ('Which AI conferences are happening in Bangalore in 2026?', 'When is the AI Summit in Bangalore 2026?') confirmed by Exa fetch and live SERP title; the verifier notes Cypher ranks on authority (analyticsindiamag.com subdomain, 10th edition, listed on aggregators) while WAIS has about 10 real non-Elets referring domains.

**Expected effect:** Small. The target queries total about 1,800 searches/mo, so roughly 800 fall in 1-17 Oct; moving from #9-#14 or unranked into the top 5 in two weeks is unlikely given Cypher's and the aggregators' authority, so a realistic range is +20 to +80 visits, mostly people comparing October AI events. The 5 posts are 3 days old with no evidence of impressions yet. The gain is that any blog or social reader in event week can reach /delegate/ or /awards/ and that Google and sponsors see consistent facts about tracks and delegate numbers; lead effect unmeasured.


**Decisions needed**

- Official delegate figure (1,000+ or 1,200+)
- Live pass price for the blog CTA box
- Whether the landing page may show 'Bangalore' in the H1 while the URL keeps 'bengaluru'

**Assets:** A13, A50, A25


**Conflicts noted**

- 'ai summit 2026' India volume: F27 cites 40,500/mo; F18 and the F27 verifier (OpenSEO get_keyword_metrics, 1 Oct 2026) give a Jul-Aug 2026 run-rate of 6,600/mo, with the 40,500 annual average inflated by Feb 2026 at 450,000. The run-rate is used.
- Registration query volumes: F26 and F27 cite 'ai summit registration' 1,300 and 'ai summit 2026 registration' 590; the F27 verifier gives Aug 2026 figures of 10/mo and 20/mo (14,800 and 6,600 in Feb). 'ai summit india 2026': 880 (F27) vs 110 in Aug 2026 (verifier).
- 'ai events in bangalore' volume: 320/mo (F55 and task context) vs 260 (Aug 2026, F18).
- Homepage FAQ size: F26 says 8 questions, its verifier counted 10 (Exa fetch 1 Oct), the F18 verifier describes five questions. The number is unsettled; the step is to rewrite whatever is there in place.
- Cypher position for 'ai conferences 2026 india': #3 (OpenSEO get_ranked_keywords, F55) vs #1 organic (live OpenSEO SERP, 1 Oct 2026, verifier). The live figure is used.
- Agenda query position: F12 lists 'world ai summit agenda' as unknown; F50 and the task context place the homepage #3 for 'world ai summit 2026 agenda' / 'world ai summit agenda' behind worldsummit.ai; the F50 verifier adds the homepage is #1 for 'world ai summit bengaluru agenda'.
- Delegate count: 'Beyond the Hype' says 1,200+ delegates; /ai-conference-bengaluru-2026.html says 1,000+ Delegates.
- Priyank Kharge portfolio: F11 treats the two designations as a contradiction needing a secretariat ruling; the verifier shows they are old (pre-June 2026) and new titles, with the current one being Home (excluding Intelligence), IT-BT and E-Governance. His 2026 participation remains unresolved: /speaker.html 'Welcoming' vs page title '2025 Chief Guest' vs speakers.json confirmed_2026: false.
- Speaker count: the site and proposed meta say '100+ speakers'; speakers.json has 50 confirmed 2026 speakers (F27 verifier), so the claim is unverified.
- FAQ rich results: F26 and F55 say they are limited to government and health sites since Aug 2023; the F26 verifier states Google retired them for all sites on 7 May 2026 and removed the documentation in June 2026. FAQPage JSON-LD in A17, A25 and A50 therefore produces no rich result.
- 2025 agenda page: F12 says /1st-edition/world-ai-agenda.html competes and should be removed or redirected; its verifier says it hardly competes (title 'World AI Summit 2025', no 'agenda' in title, body is contact blocks); F50 proposes a banner instead. Kept as low priority banner or 301.
- Speaker profile URL for agenda links: F50 links to /speakers/<slug>/ once the generator is deployed; F11 says not to launch that output as a third directory unless it replaces /assets/speaker_details/ with 301s.
- Agenda URL: /agenda.html (F12) vs /agenda/ (F50, F58).
- Live pass price: homepage Rs 20,000 vs /delegate/ Late Access Rs 30,000 / Rs 60,000 after 30 Sept (observed by the F26 verifier); every priced copy in this theme uses PLACEHOLDER_CURRENT_PASS_PRICE until settled.

## Theme: E


### E1. Verify the www Search Console property on 1-2 Oct, reconnect OpenSEO and Bing, then run a priority Request Indexing sprint

**Impact 3/10, confidence high, effort S: 15-45 min for verification, 20 min IndexNow setup, then 15 min a day 3-13 Oct and 16 Oct (about 4 h in total), owner marketing (GSC owner) + web dev (DNS or <head> tag, IndexNow key file), by Verify by 2 Oct 2026; sprint starts 3 Oct, final push 13 Oct, recap push 16 Oct.**


**Do this**

- 1-2 Oct: in Search Console add a Domain property 'worldaisummit.com' (DNS TXT at the registrar; covers www, non-www, http and https). First check whether a www or Domain property already exists under another Google account; if so, grant access instead of creating a new one.
- If DNS will be slow, add the URL-prefix property https://www.worldaisummit.com/ and verify it with the Google Analytics method (gtag G-QEB6N0MFLC already loads; needs Edit on GA4 property 490291049) or the HTML meta tag in the homepage <head> (about 10 minutes for the web dev).
- In the new property submit https://www.worldaisummit.com/sitemap.xml (the cleaned version from E3; it must list only https://www. URLs) plus sitemap-speakers.xml if /speakers/ is deployed. In the old non-www property remove any stale non-www sitemap. Do NOT use the Change of Address tool; it is for domain moves, not www/non-www.
- Re-point the OpenSEO Search Console integration (app.openseo.so/p/eb76fdff-f482-423c-9a6d-08afeccaa111/settings/integrations) to the new property so inspect_urls and performance reports cover the real site. Treat query-history backfill as PLACEHOLDER: the verifier found Google's help page does not promise the ~2,400 monthly www homepage organic sessions will appear retroactively.
- From 3-4 Oct, once the E2, E3 and E4 changes are live: URL Inspection > Test live URL > Request indexing, quota roughly 10 a day. Day 1: /, /delegate/, /awards/, /partner-with-us.html, /ai-conference-bengaluru-2026.html, /speakers/ (or /speaker.html). Day 2: top 5 speaker pages (e.g. /assets/speaker_details/priyank-kharge.html) and /blog/. Repeat for /, /delegate/ and any agenda page whenever they change (agenda, last-call price, recap on 16 Oct). The verifier notes /assets/speaker_details/* pages are the only real indexing gap; the other pages already receive Google organic landings, so this mainly speeds recrawl.
- In the OLD non-www property (available today) request indexing for https://worldaisummit.com/awards after the one-hop 301 to /awards/ (E3) is live, so Google processes the move before event week. Do not use the Google Indexing API (JobPosting and BroadcastEvent only).
- Same day: Bing Webmaster Tools > Import from Google Search Console, submit the sitemap, set up the IndexNow key file and ping IndexNow with each changed URL. chatgpt.com / ai-assistant sent 447 sessions and 29 key events (GA4, 3-30 Sep), more than bing / organic (79 sessions); the Bing-to-ChatGPT link is inferred, not verified.

**Why**

- OpenSEO inspect_urls, 1 Oct 2026: every www URL (/, /delegate/, /awards/) returns 'Search Console denied access to this property'; the only connected property is URL-prefix https://worldaisummit.com/ (F14, F63).
- GSC non-www, 28 Jun-28 Sep 2026: only 3 URLs have impressions, /awards 79 clicks / 2,419 impressions / avg pos 9.1, / 5 clicks / 25 impressions, /1st-edition/ai-dialogues 0 clicks / 2 impressions. 31 Aug-28 Sep: /awards 32 clicks / 1,300 impressions, / 1 click / 9 impressions (F63, F14 verifier).
- GA4 property 490291049, 3-30 Sep 2026: google/organic 2,984 sessions; the www homepage alone had 2,446 organic landing sessions, none visible in Search Console (F14).
- Googlebot crawled the non-www homepage on 1 Oct 2026 09:45 UTC and non-www /awards on 28 Sep; Google's chosen canonical for the homepage is already https://www.worldaisummit.com/, so the homepage, which carries every event ranking, is crawled about daily without manual requests (F69 verifier).
- GA4 organic landings 3-30 Sep: www /delegate 48 sessions and 16 key events (which events was not checked), /awards 76, /award.html 61, /ai-conference-bengaluru-2026.html 12 with 3 key events, /speaker.html 1, /blog 1; zero on /assets/speaker_details/* (F14 verifier).

**Expected effect:** No direct traffic. Request Indexing usually gets a changed URL recrawled in hours to a few days (not guaranteed), so the E2, E3 and E4 changes can be live in results before the 7-13 Oct selling week; expect tens of extra sessions in the window, not hundreds. The main value is that www query data and URL inspection become visible for event-week tuning, and that the only true indexing gap (speaker pages) is closed. Bing direct traffic is small in India.


**Decisions needed**

- Who holds DNS or registrar access for worldaisummit.com, and whether a www or Domain property already exists under another Google account
- Who has Edit access on GA4 property 490291049 if the GA verification route is used

**Assets:** A56, A14, A60


### E2. Make the three lead pages indexable, correctly priced and linked: self-canonical /partner-with-us.html with packages and a form, H1 and current prices on /delegate/, plain links from the homepage

**Impact 4/10, confidence medium, effort S-M: 3-4 h web dev, 30 min partnerships, 15 min marketing, owner web dev + partnerships (availability, deck, named contact) + marketing (price and audience figure), by 3 Oct 2026.**


**Do this**

- /partner-with-us.html: change the canonical from https://www.worldaisummit.com/ to <link rel="canonical" href="https://www.worldaisummit.com/partner-with-us.html">. Replace the 85-character copy of the homepage title and the 182-character homepage meta with its own. It already has an H1 ('World AI Summit Partner Benefits'), so keep that; do not add a second one. Note: the page already ranks #7 for 'world ai summit sponsorship' (live Google India, 1 Oct), so this tidies signals rather than unlocking a ranking.
- Expand /partner-with-us.html from 219 words: 'Who you will meet' (reuse the homepage 'Who Should Attend' list and the 7 tracks); 'Ways to partner' expanding the 5 formats already listed (Sponsorship, Exhibit, centre-stage speaking slot, 1:1 meetings and executive roundtables, feature in the AI Innovation Report); 'Still available for 14-15 Oct' (booths and slots left, from the partnerships team); 'Past partners' reusing the homepage logos and 2025 testimonials (Bandhan Bank, Razorpay, Pinnacle, Zrika); a short enquiry form (name, company, role, email, phone, interest) or at minimum mailto:partnerships@worldaisummit.com?subject=Sponsorship enquiry WAIS 2026 plus a named contact's phone or WhatsApp; optionally the sponsorship deck PDF.
- Use one audience figure across pages: PLACEHOLDER [1,000+ or 1,200+ delegates, to be confirmed by marketing]. Today /partner-with-us.html says '1200+ global AI leaders', /ai-conference-bengaluru-2026.html says '100+ Speakers 1,000+ Delegates 50+ Startups', and a blog post says '1,200+ delegates'.
- /delegate/: add an H1. Remove the stale 'Early Bird valid till 25th July 2025' line and the expired 'Standard Access Rs 20,000/35,000 valid till 30th Sept 2026' tier. Make the homepage 'Secure your seat' block (Premium Rs 20,000) and /delegate/ (Late Access Rs 30,000/60,000) show the same price: PLACEHOLDER [price actually charged at checkout from 1 Oct, to be confirmed by marketing]. This decision also gates E4.
- Internal links: plain <a href> (not JS onclick, not non-www absolute URLs) from the homepage header, nav and 'Secure your seat' block to /delegate/; from the awards block and nav to /awards/; from the footer partnership-emails area, the homepage hero, the homepage FAQ answer 'Are exhibition and sponsorship opportunities available?' and the /ai-conference-bengaluru-2026.html 'Partner With Us' link to /partner-with-us.html. Link /ai-conference-bengaluru-2026.html, every blog post and every speaker page to /delegate/. Run grep -rn 'https\?://worldaisummit\.com' --include=*.html . and replace each non-www absolute href.
- Give /speaker.html its own meta (it duplicates the homepage's 182-character meta) and trim the homepage meta to 160 characters or fewer.
- 301 /partnership.html (64 words, no H1, canonical to /) to /partner-with-us.html; the rule itself ships in the E3 redirect file.
- After publishing, request indexing for /partner-with-us.html, /delegate/ and / through the www property (E1).

**Why**

- OpenSEO audit c1b16b55, 1 Oct 2026: partner-with-us.html, award.html and partnership.html all canonicalise to https://www.worldaisummit.com/ and share the homepage title 'World AI Summit 2026 | Global Artificial Intelligence Conference by Elets Technomedia' (85 characters) and its 182-character meta; /partner-with-us.html is 219 words; /partnership.html is 64 words with no H1; /delegate/ is flagged missing-h1 (F10, F66).
- Live Google India, 1 Oct 2026 (get_serp_results, depth 10): for 'world ai summit sponsorship' /partner-with-us.html is #7 organic titled 'World AI Summit Partner Benefits'; the homepage is #1 with 'Partner with us ... partnerships@worldaisummit.com' in its snippet, so Google ignores the canonical hint (F10 verifier).
- Exa fetch, 1 Oct 2026: /delegate/ shows Early Bird 'Valid till 25th July 2025', Standard Rs 20,000/35,000 'Valid till 30th Sept 2026' and Late Access Rs 30,000/60,000; the homepage shows Premium Rs 20,000 (F66).
- GA4 Jul-Sep 2026 (brief): /partnership.html 165,574 views at 0.4 s engagement; /delegate/ 2,384 views, 316 form_submit key events, only 18 users reached /delegate/success.php.
- Audit c1b16b55: every HTML page except the homepage has crawlDepth null, consistent with pages found only via the sitemap, though this may be a crawler-seeding artefact (F66).

**Expected effect:** Small organic effect in two weeks: sponsor and exhibitor query volumes are unknown, and the page already sits on page 1 for the one brand sponsor query checked. Sitelinks to /delegate/ under brand queries where the homepage is #1 are possible but not guaranteed. The real effect is conversion: the price a visitor sees matches checkout, the pass page is one click from the homepage, and sponsor-intent visitors (165,574 views on /partnership.html in Jul-Sep) land on a page with packages and a form instead of a 64-word contact block. One sponsor deal outweighs many passes.


**Decisions needed**

- Pass price actually charged from 1 Oct (homepage Rs 20,000 vs /delegate/ Late Access Rs 30,000/60,000)
- Single audience figure (1,000+ or 1,200+)
- Booths and slots still available for 14-15 Oct, and a named partnerships contact with phone or WhatsApp
- Whether to publish the sponsorship deck as a PDF

**Assets:** A59, A10


### E3. Replace 302s, 3-hop chains and dead 2025 URLs with one-hop 301s to the 2026 pages, and rebuild sitemap.xml to list only indexable 2026 URLs

**Impact 2/10, confidence high, effort S-M: 1-3 h for redirects and testing, about 1 h for the sitemap, owner web dev (redirects, sitemap, curl tests); Elets editorial optional, by 3 Oct 2026 (ship redirects and sitemap together), legacy map no later than 5 Oct.**


**Do this**

- Remove the rule that sends /registration and /registration.html with a 302 to https://worldaisummit.com/ (location unknown: .htaccess or hosting panel). Add one-hop 301 rules ABOVE the generic host rule: /registration(.html), /delegate-pass, /giveaway, /1st-edition/delegate-pass.html, /1st-edition/giveaway.html and /delegate-registration.html to /delegate/; /awards (no slash), /award.html, /nomination, /entry-guidelines and /1st-edition/awards.html to /awards/; /partnership(.html), /partner-benefits and the 1st-edition partnership pages to /partner-with-us.html; /faqs and /thematic-tracks to /; /agenda, /ai-dialogues, /startup-competition and the 2025 blog slugs (/why-attend-..., /what-to-expect-...) to /ai-conference-bengaluru-2026.html; /index.html to /; /blog/index.html to /blog/. Then non-www and http to https://www. Mirror the map on both hosts, path-preserving, before the catch-all host redirect. Server stack is PLACEHOLDER [Apache or nginx; both rule sets are in the assets].
- Keep /1st-edition/ and /1st-edition/speakers.html as archive pages: add a top banner 'World AI Summit 2026: 14-15 Oct, Bengaluru, get your pass' linking to /delegate/, retitle to 'World AI Summit 2025 Archive | ...' and drop the 'Register now' meta. If /agenda/ is published later (the speaker generator links to it), change the /agenda target to /agenda/.
- Test every source URL with curl -sI and confirm a single 301 with the final www Location (loop-check included in the assets). Current status of www /awards (no slash), /faqs and /agenda is unverified from this environment.
- Rebuild https://www.worldaisummit.com/sitemap.xml to list only 200, self-canonical, indexable URLs with a real <lastmod> (never today's date on every URL). Remove these 19: /index.html, /blog/index.html, /award.html, /partnership.html, /registration, /registration.html, /1st-edition/thematic-tracks, /1st-edition/what-to-expect-world-ai-summit-2025-agenda-highlights, /1st-edition/why-attend-the-world-ai-summit-2025-in-bengaluru-7-straightforward-reasons-to-show-up, /1st-edition/world-ai-summit-2025-bengaluru-to-host-the-most-futuristic-and-deep-tech-ai-confluence, /1st-edition/delegate-pass.html, /1st-edition/giveaway.html, /1st-edition/awards.html, /1st-edition/partnership.html, /1st-edition/partner-benefits.html, /1st-edition/speaker-bio.html?name=angela-lusigi, /1st-edition/world-ai-agenda.html, /1st-edition/faqs.html, /1st-edition/blogs.html.
- Keep in the sitemap: /, /delegate/, /awards/, /partner-with-us.html (once self-canonical per E2), /ai-conference-bengaluru-2026.html, /speaker.html (or /speakers/), /blog/ and the 5 posts, /1st-edition/ and /1st-edition/speakers.html, and the speaker pages. If /speakers/ is deployed, drop the 50 /assets/speaker_details URLs that redirect, keep /assets/speaker_details/priyank-kharge.html, and add 'Sitemap: https://www.worldaisummit.com/sitemap-speakers.xml' to robots.txt. Resubmit in the www property (E1); the old Google ping endpoint is retired.
- Optional, off-site: Elets editorial 301s events.eletsonline.com/aidemo/registration.html (mirrors the homepage, #7 for 'world ai summit bengaluru' with a 'September 2026' snippet) to https://www.worldaisummit.com/delegate/, and updates the 2025 cio.eletsonline.com and egov.eletsonline.com articles that link to the dead URLs.

**Why**

- OpenSEO audit c1b16b55, 1 Oct 2026: www /registration and /registration.html 302 to https://worldaisummit.com/, which 301s to www/ (non-www /registration takes 3 hops); both 302 URLs and four 302ing /1st-edition/ slugs are in the sitemap; all 11 non-www URLs crawled now 301 to www, but non-www /awards points at www /awards (no slash), not /awards/ (F64).
- Sitemap reconstructed from audit inSitemap flags: 84 URLs, 6 return 302, 5 are canonicalised elsewhere (index.html, blog/index.html, award.html, partnership.html, partner-with-us.html), 15 are /1st-edition/ archive URLs (11 return 200 with duplicate titles and metas, 10 missing H1, 2 thin), 51 are /assets/speaker_details pages; the raw file could not be fetched, so lastmod presence is unknown (F65, confirmed by verifier).
- GSC non-www, 16 months to 28 Sep 2026: /agenda 35 clicks / 7,566 impressions, /why-attend-... 22 / 8,229, /what-to-expect-... 19 / 4,335, /startup-competition 13 / 3,415, /faqs 4 / 2,510, /ai-dialogues 0 / 1,811, /delegate 6 / 137, /registration 0 / 15; but in the last 28 days every legacy URL had zero impressions (F16 and verifier).
- Google's last crawls: /agenda, /faqs, /startup-competition, /ai-dialogues, /entry-guidelines 5xx (25-28 May 2026); /partnership 5xx (6 Jun); /nomination 404 (7 Jul); referring URLs include cio.eletsonline.com and egov.eletsonline.com 2025 articles and the www homepage (F16).
- GA4, 3-30 Sep 2026: www /delegate-registration.html took 12 organic sessions with 1 engaged and 0 key events; /1st-edition took 22 organic sessions with 0 key events. Backlinks: 19,511 of 19,826 come from eletsonline.com (F16, F64).

**Expected effect:** Mainly protective. None of the legacy URLs had a GSC impression in the last 28 days and Google last crawled most of them in May-July, so there is little search traffic to win back by 17 Oct; link-equity consolidation is long-term. Near-term gains are small: the 12+ monthly sessions dying on /delegate-registration.html and clicks from old Elets articles and mailers land on /delegate/ or /awards/ instead of a 302 to the homepage, and non-www /awards (79 clicks in 3 months, #2 for 'world ai awards') gets the best chance of moving to www without a dip during event week. Sitemap clean-up adds no measurable traffic by itself; the site has about 100 URLs so crawl budget is not a constraint.


**Decisions needed**

- Server stack (Apache .htaccess or nginx) and where the current /registration 302 rule lives
- Confirm /partner-with-us.html is the single live sponsor page (all findings assume it)
- Whether /speakers/ is being deployed before 14 Oct, which decides the speaker-page sitemap handling

**Assets:** A57, A15, A58


### E4. Fix and publish Event JSON-LD for World AI Summit 2026 on one leaf URL (homepage) with the real price, and repair the existing /awards Event markup

**Impact 2/10, confidence medium, effort S: under 2 h web dev plus 30 min marketing, owner web dev (markup, validation) + marketing (price decision, 30 min), by 3-4 Oct 2026, to leave about 10 days before 14 Oct.**


**Do this**

- Resolve the price first (same decision as E2): Google requires the schema price to match the price visible on the page. Set offers.price to PLACEHOLDER [price charged from 1 Oct] with priceCurrency INR, offers.url https://www.worldaisummit.com/delegate/, and make the homepage and /delegate/ show the same figure. The current asset default of 20000/35000 with validFrom 2026-10-01 contradicts /delegate/, which shows Late Access Rs 30,000/60,000 from 1 Oct, so edit it before use.
- Paste the Event JSON-LD into the <head> of https://www.worldaisummit.com/ only (name, startDate 2026-10-14, endDate 2026-10-15, eventAttendanceMode offline, location Place 'Sheraton Grand Bangalore Hotel at Brigade Gateway' with PostalAddress, organizer Elets Technomedia, performer, offers). Google's guidance is one event, one leaf URL, so do not duplicate the block on /delegate/ and /ai-conference-bengaluru-2026.html. Verify the street address: the asset's address came from the globaltradefairs.com listing.
- Add an image that is already on the site: it is recommended, not required (Google's Event doc lists only location, name and startDate as required; image minimum width 720px, 1920px recommended, ideally 16x9, 4x3 and 1x1).
- Repair the Event markup Google already detects on non-www https://worldaisummit.com/awards ('World AI Summit 2026', warnings for missing performer, offers and organizer): add those three properties or remove the Event node from the awards page so it does not compete with the homepage event. The non-www /awards URL is also being redirected to /awards/ in E3, so apply the fix on www /awards/.
- Validate in the Rich Results Test and the Schema Markup Validator, then request indexing of / (and /awards/) through the www property (E1). Keep dates and times consistent with the third-party listings (AllEvents shows Wed 14 Oct 9:00 AM to Thu 15 Oct 6:00 PM IST at the Sheraton Grand, a 'Delegates Passes INR 20,000' ticket and a link to /delegate/ with Elets UTMs; also Eventbrite, Luma, 10times), because those feeds already supply Google's events index.
- Optional: the local generator /home/user/123/worldaisummit/speakers/build_speakers.py (event_ld()) already builds the same Event node with Place and Offer from speakers.json; reuse that data so speaker pages and the homepage stay consistent once /speakers/ is deployed.

**Why**

- OpenSEO get_serp_results, India/en, 1 Oct 2026: a Google Events carousel appeared on 'tech events in bangalore' (about 1,300/mo), 'ai events in bangalore' (260-320/mo, WAIS organic #9), 'events in bangalore this week' (1,900/mo, Aug 2026), 'upcoming tech events in bangalore' and 'conferences in bangalore' (720-880/mo), combined about 4,700 searches/mo; WAIS has no organic listing on 4 of the 5 (F21). A separate 22-query run saw the carousel on 'ai events in bangalore', 'events in bangalore october 2026' and 'ai conference bangalore 2026' (WAIS organic #4) (F24). Carousel contents were not returned by the tool.
- Google URL Inspection, 1 Oct 2026: non-www /awards already carries an Events rich result ('World AI Summit 2026') with warnings for missing performer, offers and organizer, so markup must be fixed rather than added from scratch (F69 verifier).
- Google's Event structured-data doc (developers.google.com/search/docs/appearance/structured-data/event, fetched 1 Oct 2026): required properties are location, name and startDate only; a ticketing site integrated with Google is enough for eligibility; one event per leaf URL (F24 verifier, F21 verifier).
- AllEvents (allevents.in/bangalore/world-ai-summit-2026-tickets/80002987560857) and a happeningnext.com mirror already publish the event with 14 Oct 9:00 AM to 15 Oct 6:00 PM IST, Sheraton Grand, 'Delegates Passes INR 20,000' and a link to /delegate/, so Google probably already has the event in its index (F21 verifier).
- Googlebot crawled the non-www homepage on 1 Oct 2026 09:45 UTC and treats www as canonical, so homepage markup would be seen within days (F21 verifier).

**Expected effect:** Unknown and directional. Because AllEvents already feeds Google with correct data, the likely gain is that the official site appears as the ticket and info source alongside AllEvents or Eventbrite in the event panel, with offers.url sending high-intent clicks straight to /delegate/, rather than first entry into the carousel. If Google picks up the markup by about 7 Oct, a few dozen to low hundreds of impressions-to-clicks over 7-17 Oct on the city-event queries; near zero if recrawl takes longer than the window. Carousel inclusion and order are up to Google.


**Decisions needed**

- Pass price charged from 1 Oct (shared with E2)
- Whether the awards page should keep its own Event node (completed) or drop it in favour of the homepage event
- Confirm the venue street address

**Assets:** A23, A20


### E5. Make GA4 count sales and leads: a real purchase event, generate_lead by form type, noindex /thankyou.html, hostname filter, and UTMs on mailers, listings and speaker shares

**Impact 2/10, confidence high, effort S-M: about 4-6 h in total, owner web dev (events, noindex, 2-3 h) + marketing (GA4 admin 1 h) + email team (UTM templates 30 min), by 2 Oct 2026.**


**Do this**

- GA4 property 'Elets World AI Summit 2025' (properties/490291049, stream G-QEB6N0MFLC): on /delegate/success.php and /awards/success.php fire 'purchase' server-side, once per order, with transaction_id, value and currency INR (GA4 dedupes by transaction_id; 78 success-page views from 18 users suggests refreshes). Add checkout.stripe.com to 'List unwanted referrals'.
- Replace the generic 'form_submit' key event (custom, created 1 Jul 2026) with generate_lead carrying form_type set to delegate, group, sponsor, prospectus, award_nomination or enquiry, fired on a successful server response rather than on loading the thank-you page. PLACEHOLDER [whether the forms submit by AJAX or full post is unknown; this decides where the event fires].
- Add <meta name="robots" content="noindex"> to /thankyou.html (it was an organic landing page 5 times in Sept, each firing a key event).
- Add a hostname filter in GA4 (include only www.worldaisummit.com) or mark 127.0.0.1 and localhost as internal or developer traffic; Jul-Sep hostnames include 127.0.0.1 (534 views of /index.html), localhost, indiapharmaexpo.com and default.kinfra.myqcloud.com.
- UTM templates: every Elets mailer link uses utm_source=elets_mailer&utm_medium=email&utm_campaign=wais26_<segment>_<yyyymmdd>; every listing (10times, allevents, Eventbrite, globaltradefairs, aievents.now, eventmap.ai) uses utm_source=<site>&utm_medium=listing&utm_campaign=wais26; speaker share kit uses https://www.worldaisummit.com/delegate/?utm_source=linkedin&utm_medium=speaker_share&utm_campaign=wais26&utm_content=<speaker-slug>. Keep the existing campaign names (world_ai_summit_2026, world_ai_summit_2026_sponsorship, world_ai_awards_2026) mapped so history is not lost.
- Done by 2 Oct so the whole 1-17 Oct window is measured; review source/medium by key event on 7 Oct and 13 Oct to decide final mailer segments and spend.

**Why**

- GA4 property 490291049, Sept 2026: purchase recorded 0 transactions and 0 revenue on every source/medium; checkout.stripe.com/referral brought 5 sessions; key events are purchase (2025 default), form_submit and partnership_form_submit (both custom, created 1 Jul 2026) (F06, confirmed by verifier).
- GA4 Sept 2026: r.emails.elets.in/referral 224,681 sessions with 96 key events, so mailers are untagged and counted as referral; Jul-Sep (brief) 263,703 mailer sessions at 0.06% conversion. Existing campaign tags: world_ai_summit_2026 1,891 sessions, world_ai_summit_2026_sponsorship 459, world_ai_awards_2026 70 (F06).
- GA4 Jul-Sep 2026 (brief): /delegate/ 2,384 views with 316 form_submit key events but only 18 users reached /delegate/success.php, and 2 reached /awards/success.php (F06 verifier).
- GA4 Sept 2026: /thankyou.html was an organic landing page 5 times, each firing a key event; GA4 web stream defaultUri is https://worldaisummit.com/ (non-www) (F06).
- Jul-Sep hostnames include 127.0.0.1 (534 views of /index.html), localhost, indiapharmaexpo.com and default.kinfra.myqcloud.com (F06, confirmed).

**Expected effect:** No traffic effect and no direct leads. Within days of setup Elets can see which mailer segments, listings and speakers produce paid passes and sponsor enquiries, and shift sends for the final 10 days. The verifier cautions that volumes are too small to steer by with confidence: only 18 purchasers reached /delegate/success.php in all of Jul-Sep, so 2-17 Oct will likely show tens of purchases, not hundreds. The lasting value is a clean baseline for the 2027 cycle and for judging the other themes' work after the event.


**Decisions needed**

- Whether the delegate, sponsor and award forms submit by AJAX or full page post
- Who owns the GA4 property admin and the mailer platform templates

**Assets:** A06


**Conflicts noted**

- Pass price from 1 Oct: the homepage shows Premium Rs 20,000; /delegate/ (Exa fetch, 1 Oct) shows Standard Rs 20,000/35,000 'valid till 30th Sept 2026' and Late Access Rs 30,000/60,000; AllEvents lists 'Delegates Passes INR 20,000'. The Event JSON-LD asset A23 defaults to 20000/35000 with validFrom 2026-10-01, which the F24 verifier says is wrong for today. Used PLACEHOLDER in E2 and E4.
- Audience figure: /partner-with-us.html says '1200+ global AI leaders', /ai-conference-bengaluru-2026.html says '1,000+ Delegates', a blog post says '1,200+ delegates' (F10). PLACEHOLDER in E2.
- Status of legacy non-www URLs: F16 says 'now 5xx or 404' from Google's May-July crawls; the F16 and F64 verifiers say OpenSEO crawl c1b16b55 on 1 Oct saw non-www /faqs, /ai-dialogues, /partnership, /awards and /registration all 301 to the same path on www, so the live problem is path-preserving 301s into www URLs that may not exist (Exa saw 'not found' text for www /faqs, /agenda, /nomination, /entry-guidelines; status code unverified).
- Non-www /awards today: F69 verifier says Google URL Inspection shows it 'Submitted and indexed', Google-selected canonical https://worldaisummit.com/awards, last crawled 28 Sep, so it served 200 then; F64 says the 1 Oct audit saw a 301 to www /awards (no slash) and infers the host redirect is newly enabled. Both can be true at different dates; the live status should be checked with curl before deploying E3.
- Events carousel count and position: F21 saw the carousel on 5 Bangalore SERPs (blocks 6, 8, 11, 11, 12; 'ai events in bangalore' at block 8); F24, from a 22-query run, saw it on 3 SERPs with 'ai events in bangalore' at block 6 and no carousel on 'tech conference bangalore' or the 'ai summit 2026' cluster. The brief says 5. Query sets differ, so both are kept in E4.
- Existing Event markup: F21 and F24 said it was unverified whether the site carries Event JSON-LD; the F69 verifier found Google detects an Events rich result on non-www /awards with warnings for missing performer, offers and organizer. E4 treats this as 'fix', not 'add'.
- 'ai summit registration' volume: F64 and F66 cite 1,300/mo (homepage #4); the brief says about 10/mo outside the Feb spike. 'ai summit 2026': F69 cites 40,500 (homepage #7); the brief says the run-rate is about 6,600/mo and 40,500 is a Feb-spike average. The F69 verifier also says Request Indexing does not move these rankings, so neither figure is used as an E1 effect.
- Search Console backfill: F06 says 'Google shows past data once verified'; the F14 verifier, citing Google's help page (support.google.com/webmasters/answer/34592), says it is probably wrong that the new property will show the homepage's ~2,400 monthly organic sessions of query history right away. E1 treats backfill as a PLACEHOLDER.
- /delegate/ key events, 3-30 Sep: F14 says '16 form_submit'; the verifier confirmed only '16 key events' and did not check which events. E1 uses the verified wording.
- Sitemap size: F65 removes 19 of 84 URLs (leaving 65) but the asset A58 title says '84 to 62 URLs'. The difference is unexplained; use the explicit removal list in E3 and re-count on deploy.
- Which sponsor page is live: F16 says pick one of /partner-with-us.html or /partnership.html; F10, F64 and F66 all pick /partner-with-us.html and 301 /partnership.html to it. E2 and E3 follow the majority, flagged as a decision.

## Theme: Off-site: listings, LinkedIn, aggregators, listicles, partners, Amsterdam


### F1. Turn the LinkedIn showcase, a LinkedIn Event and the 50 confirmed speakers into a pass-sales channel pointing at /delegate/

**Impact 3/10, confidence medium, effort S-M: 1-2h for showcase, Event and pinned post; 4-6h for the speaker kit and daily posts, owner marketing (LinkedIn page admin) and speaker secretariat, by Showcase, button and pinned post by 3 Oct 2026; LinkedIn Event by 4 Oct; speaker emails by 3 Oct; posts 2-13 Oct.**


**Do this**

- Showcase admin (linkedin.com/showcase/world-ai-summit/), by 3 Oct: rewrite the tagline and the first 300 characters of About (it still says '2nd Edition' and 'Stay tuned for speaker announcements, partnerships, agenda, and registrations'); set the Website field and the custom 'Register' button to https://www.worldaisummit.com/delegate/?utm_source=linkedin&utm_medium=social&utm_campaign=wais2026&utm_content=showcase_button. Note: Google's snippet already shows the tagline, not the stale text, so this fixes what visitors see after the click, not the SERP.
- Create a LinkedIn Event 'World AI Summit 2026, Bengaluru' (in person, 14-15 Oct 2026, Sheraton Grand Bangalore Hotel at Brigade Gateway) with external registration set to /delegate/ plus utm_content=li_event, live by 4 Oct; first check in the admin UI that a showcase page can host an Event with an external registration link; invite followers and ask every confirmed speaker and exhibitor to share it.
- From today to 15 Oct, end every post with 'Book your delegate pass' and the /delegate/ UTM link instead of 'Express your interest: lnkd.in/...' (first check where the lnkd.in links go; they may already reach /delegate/). On sponsor and exhibitor posts add 'Exhibit or sponsor: partnerships@worldaisummit.com'. On 1-2 posts add 'Nominate for the World AI Awards' with the /awards/ link.
- Pin one post naming the pass tiers at PLACEHOLDER_CURRENT_PASS_PRICE, the 10% group discount for 3 or more delegates and the three contact emails (registration@, partnerships@, secretariat@worldaisummit.com). Settle PLACEHOLDER_EDITION_NUMBER first (the About says 2nd, posts since July say 3rd) and use it everywhere.
- By 3 Oct, secretariat@ emails each of the 50 confirmed speakers (speakers.json confirmed_2026: true) with: their live https://www.worldaisummit.com/assets/speaker_details/<slug>.html URL, a request to check role and bio, LinkedIn copy with a UTM link (utm_medium=speaker_share), and the existing 'We welcome X as a speaker' card graphic. Keep the ask for a clean link from a bio page they control as optional only; the verifier found it will produce nothing before 17 Oct and a fund homepage such as 247vc.in is not a natural place for an event link. For government officers, ask their department handles instead.
- Run a daily speaker-countdown post 2-13 Oct tagging 3-4 speakers each, linking the speaker page with UTMs. Prioritise by pass-buyer fit: BFSI (Tulshekar Gangireddy, JPMorgan; Deepak Mohanty, Wells Fargo; Deepika Sandeep and Shireen Ali, HSBC; Vijaya Kadiyala, DBS; Shantanu Dasgupta, Axis; Vishal Chugh, Tata Capital), Retail (Sandeep Varaganti and Anand Thakur, Reliance Retail; Suman Guha, Croma; Sandeep Sharma, Shoppers Stop), Ecosystem (Shalini Kapoor, EkStep; Sandhya Vasudevan, TiE Bangalore; Shashank Randev, 247VC; Sanjeev Gupta, KDEM).
- Keep the live /assets/speaker_details/<slug>.html URLs until after 17 Oct; they already rank on page 1. Do not deploy the repo's /speakers/<slug>/ version before the event; if moved later, 301 each old URL. Before speakers share, check og:image on the live speaker pages (the repo config has an empty og_image, so previews may show no image).
- Track utm_source=linkedin and utm_medium=speaker_share in GA4 and compare /delegate/ sessions and form_submit for 2-17 Oct against the September daily average.

**Why**

- LinkedIn showcase is #6 organic (page 1) on 'world ai summit' (verifier, OpenSEO Google India, 1 Oct 2026, depth 10; the lens said #5) and #2 on 'world ai summit bengaluru', directly under the homepage at #1.
- Showcase About (Exa, 1 Oct 2026) says '2nd Edition' and 'Stay tuned for ... registrations'; posts dated 15-18 Sep 2026 say '3rd Edition'; Jul-Sep posts use 'Express interest' lnkd.in links (destinations unknown); reactions per post about 2-25; followers 4,402 / 4,582 / 4,912 by snapshot.
- Speaker pages, linked only from the sitemap, rank on page 1 (OpenSEO Google India, 1 Oct 2026): 'sandeep varaganti' #6 (210/mo, verified), 'shashank randev' #7 (90/mo, verified; Cypher's speaker page #2), 'aman mittal ias' #4 (260/mo) and 'pankaj kumar pandey' #10 (320/mo), the last two not re-verified; 'vishal chugh' not in the first 20 (5,400/mo, mostly another person). 35 of 50 names returned no volume; distinctive names total about 1,100/mo.
- WAIS LinkedIn speaker posts (George Inasu 31 Aug, Harsh Vardhan 26 Aug, Suman Guha 10 Sep, Deepak Mohanty 16 Sep; Exa 1 Oct) link to lnkd.in, not to speaker pages. Cypher's speakers folder has 93 referring domains (OpenSEO project memory, 26 Sep 2026). Exa found no LinkedIn Event for WAIS 2026 (absence not proven).

**Expected effect:** Directional only, no LinkedIn referral baseline exists. The showcase and post footers could add tens to low hundreds of /delegate/ sessions between 1 and 17 Oct from people already following the event (verifier notes the showcase sits under an AI Overview, PAA and answer boxes, so its CTR is probably low). If 15-25 speakers post, expect tens to low hundreds of referral visits from senior BFSI, retail and government networks plus a few delegate or group enquiries. Organic gain from speaker-name searches is tens of clicks; bio-page links give nothing in the window. Leads: pass sales at Late Access prices, partnerships@ enquiries from sponsor posts, a few award nominations.


**Decisions needed**

- Current pass price and GST wording for the pinned post (PLACEHOLDER_CURRENT_PASS_PRICE)
- Edition number: 2nd or 3rd (PLACEHOLDER_EDITION_NUMBER)
- Where the existing lnkd.in 'Express interest' links point
- Corporate comms clearance for BFSI speakers to post

**Assets:** A74, A40


### F2. Send the 8 partners and KDEM a 'Meet us at World AI Summit 2026' kit and name them in a crawlable homepage partner block

**Impact 2.5/10, confidence medium, effort S-M: web dev about 2h; partnerships 3-4h, owner partnerships (kits, KDEM ask) and web dev (homepage block, speaker page line), by Homepage block 4 Oct 2026; partner kits 5 Oct; KDEM ask 6 Oct; exhibitor push 5-9 Oct.**


**Do this**

- Web dev, by 4 Oct: add a crawlable partner block to the homepage with text names and links (today it shows category headings with logos only): Strategic Partner KDEM (https://karnatakadigital.in/); AI & Data Infrastructure Partner WD (Western Digital) (the empty heading already exists for it); AI Impact Partner HIGHTABLE; Bronze Partners Successive Digital and Kagen.ai; Exhibitors RWS, Exatron and indierouter.ai; plus any later signings. Confirm each partner's domain before linking. Add 'KDEM is Strategic Partner of World AI Summit 2026' to the About-KDEM block on /assets/speaker_details/sanjeev-gupta.html.
- Partnerships, by 5 Oct: send each of the 8 partners (not 6) a kit with their booth number, a short 'Meet us at World AI Summit 2026' snippet for their website's events, news or blog page linking to https://www.worldaisummit.com/delegate/ (clean URL), LinkedIn copy with a partner-specific UTM, and a request to invite their customers. Guest-pass codes only if PLACEHOLDER_GUEST_PASS_POLICY allows. Until /delegate/ gets its H1 and the expired price rows are fixed (other theme), link the homepage instead.
- Partnerships, by 6 Oct, through the existing KDEM contact: (a) ask for World AI Summit 2026 on https://karnatakadigital.in/events/ linking to the homepage and /delegate/, and an item on /news-updates/; treat (a) as low probability, because that page still lists May 2026 events as upcoming and skipped KDEM's own 2026 events and WAIS 2025; (b) ask for a KDEM LinkedIn post and for CEO Sanjeev Kumar Gupta (confirmed speaker) to share his speaker page; (c) ask for a note to KDEM's GCC, startup and Beyond Bengaluru cluster networks, which fits the GCC and AI for Bharat tracks. (b) and (c) are the parts worth chasing.
- Ask Elets whether the Dept of Electronics, IT, BT and S&T (2025 Host Partner) has a 2026 role; if yes, make the same listing and LinkedIn ask (2026 status unknown).
- Use the named partner list as social proof in a 'last booths' push to exhibitor prospects 5-9 Oct, with partnerships@worldaisummit.com as the CTA.

**Why**

- Partners announced on World AI Summit LinkedIn (Exa, 1 Oct 2026): RWS Exhibitor 5 Aug; Successive Digital and Kagen Bronze Partners 10 Aug; Exatron Exhibitor 17 Aug; WD AI & Data Infrastructure Partner 18 Aug; KDEM Strategic Partner 7 Sep; IndieRouter.ai Exhibitor 18 Sep; HIGHTABLE AI Impact Partner 24 Sep (HIGHTABLE's own post). The homepage partner section has headings with no text names (Exa render of index.html).
- Exa found no page on any partner's own site announcing participation (coverage partial). Cypher's homepage has 160 referring domains, with sponsor and exhibitor sites the largest editorial source (OpenSEO project memory, 26 Sep 2026). The site has about 10 real non-Elets referring domains (task context).
- karnatakadigital.in/events/ (Exa, 1 Oct 2026): Upcoming shows only World Fintech Summit 5-6 May 2026 and C2C 15-16 May 2026 (both past; the second card mislabelled); Past stops at Mangaluru Technovanza 24 Sep 2025; Mysuru Big Tech Show (23 Jul 2026), HDB Techceleration (2-3 Sep 2026) and World AI Summit 2025 are all absent. KDEM LinkedIn posts in Jul 2026 do credit partners.
- In 2025 KDEM was Strategic Partner, the Karnataka E-IT-BT department Host Partner, IndiaAI Mission Co-Host and NxtGen Presenting Partner (cio.eletsonline.com, 24 Sep 2025).

**Expected effect:** Traffic: tens of referral visits per partner at most, so low hundreds in total if most partners post. SEO: close to nothing in the window; outbound links pass no value to worldaisummit.com, and a KDEM backlink is unlikely to appear and be recrawled before 17 Oct. Leads: exhibitor customers invited by partners, late booth sales from visible social proof, and a handful of delegate or exhibitor enquiries from a KDEM network note; none of this can be quantified from available data.


**Decisions needed**

- Whether partner packages include guest-pass codes and booth numbers (PLACEHOLDER_GUEST_PASS_POLICY)
- Confirm the full 2026 partner list and each partner's website domain
- Whether the Karnataka E-IT-BT department has a 2026 role

**Assets:** A42, A41


### F3. Correct Elets' own event-platform listings (Eventbrite, GlobalTradeFairs, MeraEvents, Townscript, 10times, AllEvents) and add Luma and venue listings

**Impact 2/10, confidence medium, effort S-M: about 5-6h across platforms; GTF support and hotel responses are outside Elets' control, owner marketing / registration team (platform logins); partnerships for the GTF exhibitor copy, by Eventbrite and GTF by 3 Oct 2026; MeraEvents, Townscript and Luma by 4 Oct; 10times and AllEvents same day as the price decision; venue request by 6 Oct; newspaper listings by 9 Oct.**


**Do this**

- Eventbrite (Manage events, World AI Summit 2026; https://www.eventbrite.com/e/world-ai-summit-2026-tickets-2002042308438): make it a two-day event Wed 14 Oct to Thu 15 Oct 2026 with start time PLACEHOLDER_START_TIME (the listing shows 10:00 AM, AllEvents and aievents.now show 9:00 AM-6:00 PM, the site gives no time); check the venue pin only (the 'Harohalli' browse page is a radius page, not a geocoding error); category Science & Technology > High Tech; tags Artificial Intelligence, AI Conference, Generative AI, Bangalore, Bengaluru, Tech Summit; price PLACEHOLDER_CURRENT_PASS_PRICE or an external Register link to /delegate/?utm_source=eventbrite&utm_medium=event_listing&utm_campaign=world_ai_summit_2026; paste the description and confirmed speakers; organiser profile Elets Technomedia with website link. Verifier: most of this is already done, so treat it as a check. Record the /e/ URL in the project context.
- GlobalTradeFairs (Elets' own listings: all three say 'elets Technomedia, Member since 2026'), by 3 Oct: keep /tradefairs/event-details/world-ai-summit as the main page; unpublish /world-ai-summit-1 and /world-ai-summit-2026 or ask GTF support to remove or redirect them; change Entry from 'Free' to 'Paid, delegate pass from Rs PLACEHOLDER_CURRENT_PASS_PRICE'; change the city tag from 'Bengaluru Rural' to Bengaluru; set Official Website to /delegate/?utm_source=globaltradefairs&utm_medium=event_listing&utm_campaign=world_ai_summit_2026 or /partner-with-us.html for an exhibitor CTA (check the field on /world-ai-summit-2026, which differs); fill Schedule, Keynote Speakers (confirmed only) and Visitor Information; put the sponsor and exhibit email in Contact; lead with the exhibitor offer, since GTF's audience is trade visitors and exhibitors.
- MeraEvents, by 4 Oct: both organiser-account events are completed 2025 events, 'Sold Out / Sale Date Ended', with empty About: https://www.meraevents.com/event/worldaisummit (ID 266617, Rs 20,000) and ID 266543 (Rs 25,000). MeraEvents probably does not allow re-dating a completed event (inferred, not verified). Decide PLACEHOLDER_MERAEVENTS_OPTION: either create a new 2026 event (accepting MeraEvents ticketing terms, or using an external link to /delegate/?utm_source=meraevents) and add a one-line pointer to it in both 2025 descriptions, or add only the pointer line 'The 2026 edition is on 14-15 Oct 2026, book at [link]'. Organiser page: meraevents.com/o/world-ai-summit-m3wjs.
- Townscript, by 4 Oct: https://www.townscript.com/e/world-ai-summit2025-113433 shows 'EVENT HAS ENDED' with 2025 copy (5 tracks, 200+ speakers, 1,200+ participants). Create 'World AI Summit 2026' in the organiser dashboard (self-serve; usually live on publish, not verified) with an external registration link (utm_source=townscript) or a ticket at the agreed price, then edit the 2025 description to start with 'The 2026 edition is on 14-15 Oct 2026, book here: [new Townscript URL or /delegate/ UTM]'.
- 10times (https://10times.com/world-ai-summit-bengaluru) and AllEvents (allevents.in/bangalore/world-ai-summit-2026-tickets/80002987560857): confirm start and end times, venue, price and the /delegate/ link; AllEvents still says Rs 20,000 while /delegate/ shows Late Access Rs 30,000/60,000, so set all listings to PLACEHOLDER_CURRENT_PASS_PRICE on the same day. aievents.now/bengaluru and galviq.com/events/ai/bangalore are already correct; no action.
- Luma, by 4 Oct: create a Luma-hosted public event (Bengaluru, 14-15 Oct 2026, venue, price note, external registration to /delegate/?utm_source=luma). Do not plan on 'submitting to luma.com/bengaluru': that Discover page has no Submit Event button and external events reach only calendars that accept them, without a cover image. If a community calendar that accepts submissions exists (for example the Bengaluru Tech Week calendar), submit there. Inclusion in Luma discovery is Luma's decision.
- Venue and city, by 6 Oct and 9 Oct: ask the Sheraton Grand Bangalore Hotel at Brigade Gateway sales team to list the summit on the hotel's what's on page and to publish a Google Business Profile Event post (14-15 Oct) on the hotel's existing profile linking to the homepage (the verifier rates this weaker than it sounds). Do not create a Google Business Profile for the event; Google's guidelines exclude temporary events and search_local_businesses found 0 results (1 Oct). Optional, awareness only: email the 50-word listing to Bangalore Mirror 'Things To Do In Bengaluru', Deccan Herald Metrolife and The Hindu Bengaluru listings for the 12-14 Oct editions (leisure readers, no links).
- Use the same one-line identity, dates, venue and price on every listing, a UTM on every link, and verify each page in a real browser after saving. BookMyShow (#1 for 'events in bangalore october 2026') and District (#16 for 'ai conference india october 2026') are commission decisions: list there only if Elets accepts their terms.

**Why**

- MeraEvents /event/worldaisummit (ID 266617) reads 'Thursday, 25th Sep 2025 - Friday, 26th Sep 2025 | 09:00 AM to 06:00 PM IST', Rs 20,000, Sold Out; ID 266543 Rs 25,000, Sold Out; Townscript 2025 page 'EVENT HAS ENDED' (Exa, 1 Oct 2026). On 'world ai summit tickets' the homepage is #1 and neither MeraEvents nor Townscript is in the top 20 (verifier, OpenSEO Google India, 1 Oct); MeraEvents is #13 on 'world ai summit bengaluru'.
- All three GTF pages show 'Entry | Free', a title ending 'Bengaluru Rural', empty Schedule, Speakers and Visitor Info, organiser 'elets Technomedia, Member since 2026' (Exa, 1 Oct 2026). Viewer counters vary by snapshot (main page 135 to 713; /world-ai-summit-2026 121 or 287) and the exhibitor box showed 1, 17 and 27 while the Exhibitor Portal says 'No exhibitors have been added', so the counts probably include bots; no GTF page is in the top 20 for any tracked query.
- Eventbrite shows 'World AI Summit 2026, Wed, Oct 14, 10:00 AM, Sheraton Grand Bangalore Hotel at Brigade Gateway' (Exa, 1 Oct 2026); the Eventbrite Bangalore AI browse page is #7 on 'ai events in bangalore october 2026', one below worldaisummit.com at #6 (verifier); Eventbrite is #18 on 'world ai summit bengaluru'. AllEvents and happeningnext already show 14-15 Oct 2026 and Rs 20,000.
- luma.com/bengaluru is #1 organic on 'ai events in bangalore' (260-320/mo) and #3 on 'tech events in bangalore' (1,300/mo) (OpenSEO Google India, 1 Oct 2026); luma.com/discover/bengaluru/ai listed about 25 Bengaluru AI events, none WAIS, and shows only a Subscribe button (Exa and verifier, 1 Oct).
- 'events in bangalore october 2026' (Google India, 1 Oct): #1 BookMyShow, #2 Bangalore International Centre, #3 BIEC calendar, #4 Eventbrite Bangalore, then a Google Events carousel, #5 luma.com/bengaluru; WAIS not in the top 10. The Events carousel appears on 5 Bangalore discovery queries with WAIS absent (task context).

**Expected effect:** Traffic: single to low double digits of referral visits per platform, perhaps tens in total over 1-17 Oct; there is no lost Google traffic to recover, because the homepage is #1 on every brand query and the stale pages are not in the India top 20. The value is lead quality: removing 'Entry: Free', 'Sold Out' and September dates at the moment of purchase, and passing UTM-tagged pass buyers and exhibitor prospects to /delegate/ or the partnership page. Effect on the Google Events carousel is unverified.


**Decisions needed**

- Current pass price and GST wording to publish on every listing (PLACEHOLDER_CURRENT_PASS_PRICE)
- Official start and end times (PLACEHOLDER_START_TIME)
- MeraEvents: new 2026 event with ticketing terms, or pointer line only (PLACEHOLDER_MERAEVENTS_OPTION)
- Whether to list on BookMyShow or District at their commission

**Assets:** A32, A30, A31, A24, A78, A19


### F4. Ask the list pages and roundups that already rank for Bangalore and India AI-event queries to add World AI Summit

**Impact 2/10, confidence medium, effort S: 2-3h of emails and form submissions, owner marketing, by All requests sent by 5-6 Oct 2026; one follow-up around 8 Oct.**


**Do this**

- Check the live Techcanvass page first (https://businessanalyst.techcanvass.com/tech-conference-in-bangalore/). Google India already indexes the 'Top 10 Upcoming Tech Conference In Bangalore October'26' version with Messy UX Conference (3 Oct), Open Source India (7-8 Oct) and 'Flagship AI Summit' (probably Cypher) in the snippet; whether WAIS is on it is unknown (direct fetch 403, Exa cache is September). If missing, use the page's 'Spotted an event we should add? Let us know' link or info@techcanvass.com and ask for a 14-15 Oct card linking to /delegate/?utm_source=techcanvass. Do not write 'you already link to us'; that claim is not supported for this page.
- Digitalconfex (https://digitalconfex.com/ai-conferences-india-2026/, #8 on 'ai conferences 2026 india'): its table lists 'Elets India AI Summit, Jan 2026' and Cypher but not WAIS; ask them to add WAIS or swap the finished January entry. They run their own events, so they may decline.
- Send the short factual listing-update email to Dreamcast (dreamcast.in/blog/top-ai-conferences-and-events/, published 31 Aug 2026), craw.in (top-10 AI conferences in India, 31 Jul 2026, #8 on 'ai conferences in india october 2026'), news4hackers (7 Aug 2026), events.linuxfoundation.org/calendar/ai-conferences/ and conventions.io/topics/ai, asking for one entry linking to https://www.worldaisummit.com/ai-conference-bengaluru-2026.html or the homepage. Lower priority: none of these ranks in the India top 20 for 'ai conferences 2026 india', and WAIS may already be on craw.in (not fully extracted).
- dev.events: its Bengaluru AI list shows no October events and has a free Add event flow (path unverified); submit as a conference, Bengaluru, AI, 14-15 Oct 2026, link /delegate/?utm_source=devevents. b2bangalore.com: ask for WAIS on /ai-events-bangalore and /tech-events-bangalore; it ingests Eventbrite and Luma daily, so the Eventbrite fix in F3 may do this on its own.
- Only if time allows: conferencealerts.in (Bangalore/AI and October Technology pages), conferencealerts.co.in, allconferencealert.com and internationalconferencealerts.com. They rank (conferencealerts.in/bangalore #1 for 'conferences in bangalore', /india/ai #2 for 'ai conferences 2026 india', conferencealerts.co.in #1 for 'conferences in bangalore 2026', allconferencealert #2), but they are academic call-for-papers directories where WAIS would sit among about 50 'International Conference on...' rows, and they need editorial approval.
- Use the same short listing copy everywhere, link with UTMs, send all requests by 5-6 Oct, follow up once around 8 Oct; additions after 8 Oct earn almost nothing before the event. In the roundup email, set the KDEM line to PLACEHOLDER_KDEM_2026_STATUS (see conflicts) before sending.

**Why**

- WAIS is not in the first 20 for 'tech events in bangalore' (1,300/mo), 'events in bangalore this week' (1,600 avg; 1,900 Aug 2026), 'conferences in bangalore' (880 avg; 720 Aug), 'conferences in bangalore 2026' (320), 'upcoming tech events in bangalore' (210-260) and 'ai conferences 2026 india' (390); #9 for 'ai events in bangalore' (260-320), #6 for 'ai events in bangalore october 2026', #7 for 'ai conferences in india october 2026' (OpenSEO Google India, 1 Oct 2026). 'ai summit india 2026' (880/mo) #15 per brief.
- Verified order for 'tech events in bangalore' (verifier, 1 Oct): #1 bengalurutechweek.com, #2 bengalurutechsummit.com, #3 luma.com/bengaluru, #4 meetup.com, #5 Eventbrite tech-conferences, #6 techmeetups.io, #7 Techcanvass, #10 dev.events, #14 Luma tech, #15 Eventbrite tech-events, with a Google Events carousel on the page.
- Of the targets, Digitalconfex (#8 on 'ai conferences 2026 india') and Techcanvass (#5 on 'ai events in bangalore october 2026') are on page 1 in Google India; Dreamcast and dev.events are not in the top 10 on either query (verifier, 1 Oct). The OpenSEO SERP re-check for 'ai events in bangalore october 2026' failed, so F29's positions (conferencealerts #3, allconferencealert #9, b2bangalore #14) are the lens's claims.
- Dreamcast (Cypher, Gartner, Bharat AI Innovation, WCCG, RCAAI), news4hackers (Cypher #5), Digitalconfex and the Linux Foundation AI calendar list Cypher (7-9 Oct) but not WAIS (Exa, 1 Oct 2026). A WebSearch synthesized answer for 'ai conferences in india october 2026' already names WAIS second after Cypher, citing worldaisummit.com, so the AI-answer gain is mostly captured.
- Aug 2026 volumes for the wider cluster: this week 1,900, tech events 1,300, conferences 720, startup events 720, networking 390, business events 320, conferences 2026 320, ai events 260, upcoming tech 260, tech conferences 170 (OpenSEO).

**Expected effect:** Small: the verifier expects 1-3 listings to go live by about 8 Oct, leaving 6-9 days of exposure, so tens of referral visits in total (not per list) during 1-17 Oct. Many visitors on these lists want free meetups, so expect a handful of pass enquiries from professionals comparing October AI events next to Cypher, and little sponsor value. Pages that keep a 2026 archive have some longer-term value at low cost.


**Decisions needed**

- Which URL to offer editors: /delegate/ with UTM or /ai-conference-bengaluru-2026.html
- KDEM wording in the outreach copy (PLACEHOLDER_KDEM_2026_STATUS)
- Whether to spend time on the academic conference-alert directories

**Assets:** A33, A28, A19, A76, A24


### F5. Separate World AI Summit from World Summit AI (Amsterdam) in schema, FAQ and every listing, and open Bing Webmaster Tools and IndexNow for www

**Impact 1.5/10, confidence medium, effort S: under 1h for schema and FAQ; about 1h for Bing WMT and IndexNow, owner web dev (schema, FAQ, Bing, IndexNow); marketing for the shared one-line identity, by Bing WMT and IndexNow by 3 Oct 2026; schema and FAQ by 5 Oct, before Amsterdam's 7-8 Oct news peak.**


**Do this**

- Confirm PLACEHOLDER_NO_AFFILIATION (Elets has no link with World Summit AI, Amsterdam) before publishing any 'separate event' line.
- Web dev, by 5 Oct: add Organization JSON-LD to the homepage head beside the existing Event JSON-LD, with alternateName, disambiguatingDescription, parentOrganization Elets Technomedia (already has a Google knowledge panel) and sameAs links; publish only a complete schema.
- Add one FAQ to the homepage FAQ block (which already has 'Is this relevant to my role?'): 'Is World AI Summit the same as World Summit AI in Amsterdam?' with a two-sentence factual answer.
- Keep 'India, Bengaluru, 14-15 Oct' at the front of the homepage title (it already reads 'World AI Summit 2026 | AI Summit India, Bengaluru, 14-15 ...') and use the same one-line identity in the LinkedIn About (F1), YouTube descriptions and every listing in F3 and F4, so each source describes the event the same way.
- Web dev, by 3 Oct: verify https://www.worldaisummit.com in Bing Webmaster Tools using DNS or meta verification (the only Search Console property is non-www, so a GSC import will not cover www) and submit sitemap.xml.
- Add an IndexNow key file and ping changed URLs after every upload from now to 17 Oct (agenda, speaker, awards and post-event pages). ChatGPT search and Copilot draw on Bing's index; the current Bing index state was not verified.

**Why**

- 'world ai summit' (OpenSEO Google India, 1 Oct 2026, depth 10, verifier): AI Overview on top; organic #1 worldaisummit.com, #2 worldsummit.ai, #3 impact.indiaai.gov.in, #4 worldsummit.ai/all-events, #5 worldsummit.ai (tickets per one verifier, speakers per another), #6 LinkedIn showcase; 3 of the 6 page-1 organic listings are Amsterdam pages. 'world ai summit 2026': #1 worldaisummit.com, #2 worldsummit.ai, #5 worldsummit.ai/all-events. 'world ai summit bengaluru': worldsummit.ai #5 and #7.
- A WebSearch synthesized answer (US-located, 1 Oct 2026) to 'world ai summit October 2026 dates venue' described World Summit AI Amsterdam, 7-8 Oct, Taets Art & Event Park, with WAIS Bengaluru only as a footnote; 9 of its 10 sources were Amsterdam pages. 'world ai summit agenda' ranks #3 behind worldsummit.ai Amsterdam (task context, 1 Oct).
- The WAIS #1 listing already shows 'India, Bengaluru, 14-15' in the title and the venue and dates in the snippet, and Amsterdam's snippet says Amsterdam (verifier), so Google's SERP already separates the two events.
- AI Overview appears on 21 of 22 tracked queries (task context). Search Console is connected only for the non-www URL-prefix property (task context).

**Expected effect:** Near zero measurable traffic in the window: schema cannot demote worldsummit.ai, which ranks for its own brand, and positions will not move by 17 Oct. The benefit is fewer India searchers and AI answers mixing up the dates and city during 5-15 Oct, when both events are in the news, and faster Bing indexing of agenda and speaker changes. Protects existing brand-query pass and sponsor traffic rather than adding to it; the size cannot be stated honestly.


**Decisions needed**

- Confirmation that Elets has no affiliation with World Summit AI (PLACEHOLDER_NO_AFFILIATION)
- Access to DNS or the homepage head for Bing verification

**Assets:** A75, A76


**Conflicts noted**

- 'world ai summit' organic #5 on Google India, 1 Oct 2026: F84's verifier lists worldsummit.ai/tickets; F85's verifier lists worldsummit.ai/speakers; the F85 lens had the LinkedIn showcase at #5 and worldbank.org at #6, which both verifiers reject (LinkedIn is #6).
- 'world ai summit bengaluru' positions for events.eletsonline.com/aidemo: #5 (F25 lens), #7 (F33 verifier), #8 (F84 verifier); for 10times: #8 (F25 lens), #9 (F33 verifier), #10 (F84 verifier). All cite OpenSEO Google India, 1 Oct 2026.
- Techcanvass page state on 1 Oct 2026: F20 and F36 verifiers saw the 'October'26' title indexed in Google India with October events in the snippet; F86's verifier saw 'September'26' in both the Exa fetch and the WebSearch title; F29 and F36 lenses say October title with a cached September body. Whether WAIS is on the October list is unknown in every version.
- Whether Techcanvass already links to WAIS: F20, F29 and F36 say yes (from the brief); F86's verifier found no mention of World AI Summit or worldaisummit.com on the fetched page, so any link must be elsewhere (unverified).
- KDEM 2026 status: the task context and F45 (World AI Summit LinkedIn, 7 Sep 2026) say KDEM is the 2026 Strategic Partner; F86's verifier says the brief calls it 'Strategic partner 2025' and that neither the homepage nor /ai-conference-bengaluru-2026.html names KDEM as the 2026 partner (Exa, 1 Oct).
- Event start time: Eventbrite shows Wed 14 Oct 10:00 AM; AllEvents and aievents.now show 9:00 AM to 6:00 PM; the site gives no time. The 9:00 AM figure probably came from the same Elets team, so it is not independent confirmation.
- Luma position on 'tech events in bangalore': #4 (F20 lens) vs #3 organic (verifier, which says the lens counted the AI Overview block).
- GTF figures: F33 lens cites 468 viewers and 17 exhibitors on the main page and about 600 lifetime viewers across three pages; the verifier saw 135/136, 468, 604 and 713 viewers and 1, 17 and 27 exhibitors across snapshots, with the Exhibitor Portal saying none added. The lens's claim that all three pages list Official Website www.worldaisummit.com is wrong for /world-ai-summit-2026.
- Partner count: F46 lens names 6 partners (KDEM, Successive Digital, Kagen.ai, RWS, Exatron, indierouter.ai); the verifier adds WD (Western Digital, 18 Aug 2026) and HIGHTABLE (24 Sep 2026), making 8. The lens's claim that allevents.in names the same partners is wrong; the syndicated happeningnext copy names 8.
- Pass price shown to the public: homepage Rs 20,000 Premium and AllEvents Rs 20,000, while /delegate/ shows Late Access Rs 30,000/60,000 (task context, 1 Oct 2026); F90 describes passes as Rs 30,000+. Every listing step uses PLACEHOLDER_CURRENT_PASS_PRICE.
- 247vc.in position for 'shashank randev': #5 (F44 lens) vs #4 organic (verifier; Google's rank 5 counts the Images block).
- LinkedIn showcase follower count: 4,402 / 4,582 / 4,912 across snapshots; Google's snippet shows 4912.
- MeraEvents URL and time: F25 cites meraevents.com/events/worldaisummit showing '3:30 AM to 12:30 PM'; the verifier says the canonical page is /event/worldaisummit (ID 266617) showing 09:00 AM to 06:00 PM IST, 25-26 Sep 2025, and the other rendering is the same time in UTC.

## Theme: Event week and post-event (12-17 Oct)


### G1. Build one /agenda/ hub on www.worldaisummit.com that serves as the agenda now, live updates on 14-15 Oct and the highlights recap from 16 Oct

**Impact 3/10, confidence medium, effort M, about 20 hours, owner web dev (template, redirects, phase switches) + content (two people on site 14-15 Oct), by Agenda phase live by 8 Oct; live phase 08:00 IST 14 Oct; highlights phase by 12:00 IST 16 Oct.**


**Do this**

- By 8 Oct, web dev publishes https://www.worldaisummit.com/agenda/ with the day-wise programme (time, session, track, hall, speakers linked to the live pages at /assets/speaker_details/<slug>.html), one id anchor per session and Event JSON-LD; the programme team must first lock halls and times, which are not public yet.
- 301 the dead 2025 URLs to it: https://worldaisummit.com/agenda (5xx, last crawled 26 May 2026, still linked from cio.eletsonline.com and egov.eletsonline.com 2025 articles), /world-ai-agenda.html and /world-ai-agneda.html (root versions only, not /1st-edition/); Apache and nginx rules are in A67.
- Link the hub from the homepage nav, /delegate/, /awards/ and /speaker.html; on 14-15 Oct add a homepage hero link 'Live now: Day 1 updates'.
- 14 Oct 08:00 IST: switch title and H1 to the Live variant and add a 'Live updates' block above the agenda, newest first, one entry per session or every 30-60 min: session, track, speaker link, 2-3 verbatim quotes or factual takeaways from the stage, one captioned photo, YouTube link where available; two content people on site 14-15 Oct.
- Use LiveBlogPosting JSON-LD (coverageStartTime 2026-10-14T09:00+05:30, coverageEndTime 2026-10-15T19:00+05:30, liveBlogUpdate entries), max-image-preview:large and a 1200px+ hero image; treat the live rich result as low-cost uncertain upside because Top Stories eligibility is unverified. Do not use NewsArticle for the live badge and do not rely on IndexNow (Google does not support it).
- 16 Oct 12:00 IST: switch title and H1 to the Highlights variant (800-1,200 words: Day 1 and Day 2 sections, the 8-10 biggest statements, launches and MoUs), keep the full agenda below so the URL is the permanent recap, and add the lead box: 'Get full session recordings' plus 2027 interest checkboxes (attend / sponsor / speak / nominate) and an 'Enquire for 2027 sponsorship' line to partnerships@worldaisummit.com.
- Verify the www property in Search Console (only the non-www URL-prefix property is connected today), then request indexing through URL Inspection on publish and at each phase switch; this is the only manual way to speed up Google in the window.

**Why**

- inspect_urls, 1 Oct 2026: worldaisummit.com/agenda returns a 5xx, last crawled 26 May 2026, with referring URLs on cio.eletsonline.com/article/what-to-expect-at-world-ai-summit-2025-agenda-highlights/74827/ and egov.eletsonline.com/2025/06/ (F76).
- Live SERP India, 1 Oct 2026: 'world ai summit agenda' homepage #3 behind worldsummit.ai and impact.indiaai.gov.in; 'world ai summit live' homepage #4; the homepage carries no schedule (F76).
- Verifier on F76: the 7,566 GSC impressions for non-www /agenda fell almost entirely between 11 Dec 2025 and 10 May 2026 (long tail, CTR 0.46%); 0-4 impressions a day in the Sep-Oct 2025 event window; zero since 10 May 2026; 'ai summit agenda' had 1,300 India searches in Feb 2026 and 0-10 in every other month. The page is for conversion and as a link target, not for search demand.
- Exa, 1 Oct 2026: /agenda/, /agenda.html and /awards/winners-2026/ all return CRAWL_NOT_FOUND; crawl c1b16b55 (100 URLs) has no 2026 agenda, live or highlights page; the only agenda page is /1st-edition/world-ai-agenda.html (89 words) (verifiers on F23, F78, F81). Four other recommendations in this theme link to /agenda/ and break without it.
- Verifier on F51: India keyword metrics returned no volume for 'world ai summit highlights', 'world ai awards winners' or related terms; 'world ai summit' fell from 1,600 searches in Sep 2025 to 320 in Oct 2025, and 'world ai summit bangalore' from 880 to 40.

**Expected effect:** Tens to low hundreds of extra organic visits over 12-17 Oct from branded agenda, live and highlights searches that today land on a homepage with no schedule (inferred; no www Search Console data). The main value is conversion and dependency: it gives speakers, Elets stories, the post-event hero and winners a working link target, pushes Day 1 visitors to Day 2 passes, and collects recording-form and 2027 interest leads from the most engaged visitors. Organic volume unknown; search demand for these queries is below the reporting threshold.


**Decisions needed**

- Final agenda with session titles, halls and times (not public as of 1 Oct)
- One hub URL: /agenda/ (F76, recommended) versus /2026/live/ plus /2026/day-1-highlights/ and /2026/day-2-highlights/ (F51) versus /blog/world-ai-summit-2026-live-updates.html (F88) versus /blog/world-ai-summit-2026-highlights.html (F23)
- Host and server type (Apache or nginx) for the 301 rules; the 5xx on non-www /agenda may be a host issue
- Who staffs the live desk on 14-15 Oct and who approves quotes
- Verification of the www property in Search Console

**Assets:** A67, A47, A77, A22


### G2. Capture Cypher's sponsors and last-week searchers before 14 Oct: partner outreach on 10-12 Oct, event listings by 7 Oct, optional calendar post

**Impact 3/10, confidence medium, effort M, about 9-11 hours (listings under 2h, emails 2-3h, optional post half a day), owner partnerships (outreach) + marketing (listings, optional ads) + content (optional post), by Listings and optional post by 7 Oct; partner emails 10-12 Oct.**


**Do this**

- Re-check the live Cypher 2026 homepage 'Strategic Partners' list before using it; the Exa copy is a cached snapshot (its countdown points to about 11 Sep) showing 34 names including IBM, Genpact, Dell, Tredence, Google Cloud, ClickHouse, Okta, EPAM, Tiger Analytics, Axtria, Straive, CGI, Cognite, Autodesk, ABB, StoneX, Lowe's and Albertsons.
- 10-12 Oct: the partnerships team emails each partner a last-minute World AI Summit branding, exhibit or GCC-track package (email in A54), reply-to partnerships@worldaisummit.com; do not use the Cypher trademark in subject lines or any ad text.
- By 7 Oct: marketing creates a Luma event for World AI Summit 2026, Bengaluru. luma.com/bengaluru (#1 for 'ai events in bangalore' and the 'this week' query) is curated and Luma says off-platform registration can make an event ineligible for discovery, so either sell paid tickets through Luma (finance and registration must set up a second checkout) or accept a standalone Luma page linking to https://www.worldaisummit.com/delegate/?utm_source=luma.
- By 7 Oct: submit the event to conferencealerts.in/bangalore/ai (#4 for 'ai events in bangalore' and the 'this week' query, #1 for 'upcoming ai events in india'), thegenerativebeings.com/events/cities/bengaluru (#10-#11) and b2bangalore.com/ai-events-bangalore (#14), and check the Eventbrite listing is complete (it already shows 'World AI Summit 2026 Wed, Oct 14' on Eventbrite Bangalore category pages at #5 and #11 for 'tech events in bangalore this week'); listing copy is in A73.
- Ask techcanvass.com, already a WAIS referrer, to include WAIS when its monthly 'Top 10 Upcoming Tech Conference In Bangalore' list for October appears; the page fetched on 1 Oct is the September'26 edition and mostly lists free meetups, so an October edition may not exist yet.
- Optional, lower priority: by 7 Oct publish https://www.worldaisummit.com/blog/ai-events-in-bangalore-october-november-2026.html titled 'AI Events in Bangalore, October-November 2026: Dates, Venues, Passes', listing Cypher (7-9 Oct, KTPO Whitefield), World AI Summit (14-15 Oct, Sheraton Grand Bangalore Hotel at Brigade Gateway) and Bengaluru Tech Summit (17-19 Nov, BIEC) plus others Elets verifies, with a 'Next up: World AI Summit, 14-15 Oct' CTA box, linked from the homepage and /ai-conference-bengaluru-2026.html. The verifier notes the homepage already ranks #9 'ai events in bangalore', #6 'ai events in bangalore october 2026' and #4 'ai conference bangalore 2026', so a new URL mostly competes with it and may not index within 7-10 days.
- Optional, paid, marketing owner: 9-14 Oct, a small Google Ads campaign on 'ai events in bangalore', 'ai conference bangalore' and 'ai summit october 2026'.

**Why**

- Cypher 2026 runs 7-9 Oct 2026 at KTPO Whitefield, Bengaluru (10th edition, Analytics India Magazine), confirmed by the verifier via Exa and WebSearch on 1 Oct 2026; 'cypher 2026' searches rose to 2,400/month in Aug 2026 from 880 in Jul (OpenSEO).
- The Cypher homepage lists exactly 34 Strategic Partners, every example named is on it, but the copy is a cached snapshot (verifier on F60).
- OpenSEO SERP, India, 1 Oct 2026, 'ai events in bangalore' (320/month): luma.com/bengaluru #1, meetup #2, bengalurutechsummit #3, conferencealerts.in #4, Cypher #5, techcanvass #6-7, WAIS homepage #9, thegenerativebeings #11, b2bangalore #16; 'ai events in bangalore this week': WAIS homepage #11 (page 2); 'events in bangalore this week' (1,600/month): luma #2 (F60, F83).
- The four list queries total about 780 searches a month (320 + 110 + 260 + 90), roughly 26 a day across India (verifier on F60); 'upcoming ai events in india' (90/month) WAIS #14.
- Luma help page: city pages are chosen by a curation team or an automated system; events with off-platform registration may be ineligible; on 1 Oct luma.com/bengaluru showed only free community meetups (verifier on F83).

**Expected effect:** Listings plus the optional post: roughly +30 to +150 visits combined in the window, mostly 7-15 Oct, with a handful of late pass sales or walk-ins (number unknown). Partner outreach brings no traffic; its value is a few qualified sponsor or exhibitor conversations for 14-15 Oct or for 2027 (number unknown). It is the only step in this theme that can produce sponsor enquiries before the event.


**Decisions needed**

- Whether Elets will name competitor events on the WAIS blog (brand decision)
- Whether to sell tickets through Luma or accept a standalone Luma page
- Which last-minute package and price to offer Cypher partners
- Whether to run the paid Google Ads campaign

**Assets:** A54, A73


### G3. Publish the World AI Awards 2026 winners page on the ceremony night, with badge, press kit, winner share kit and an Elets winners story

**Impact 3/10, confidence medium, effort M, about 12-16 hours in total (skeleton 2h, same-night data entry 1-2h, badges 1-2h, kit page 1h, emails 1-2h, two 400-word stories 1h, 2025 page 2-3h), owner web dev (page, kit page) + awards team (results sheet, winner emails) + marketing (badges, kit) + Elets editorial (stories, LinkedIn), by Nominations story by 3 Oct if open; 2025 list by 6 Oct; skeleton, badges and kit by 13 Oct; page live on the ceremony night (14 or 15 Oct); kits by 10:00 IST the next day; Elets story and LinkedIn within 12 hours.**


**Do this**

- By 13 Oct, web dev builds the skeleton at PLACEHOLDER_WINNERS_URL (recommended https://www.worldaisummit.com/awards/winners-2026/; F51 proposed /awards/2026-winners/) with the 6 category groups and one row per award: category group, category, winning organisation or person, project name exactly as submitted on the nomination form, city; an id anchor per row (for example #most-promising-ai-startup), a captioned stage photo and the jury list where available. No bios; only nomination-form data and internal records.
- The awards team supplies the official results sheet the same evening; publish within PLACEHOLDER_PUBLISH_WINDOW of the ceremony (findings say 1 hour, 2 hours, or by 23:00 IST on the ceremony day; the 2025 ceremony was on Day 1 evening, 25 Sep 2025, and the 2026 date and time are unconfirmed).
- After the ceremony: switch the /awards/ title to the Winners variant, add a top banner link to the winners page, link it from the homepage awards block and from the G1 hub, and add a 'World AI Awards 2027: register interest to nominate' form on the winners page and on /awards/.
- By 13 Oct, design 'Winner - World AI Awards 2026' and 'Finalist - World AI Awards 2026' PNG/SVG badges (both carrying 'World AI Summit, Bengaluru'), host them at /assets/images/awards/, and build a one-page press kit at https://www.worldaisummit.com/awards/press-kit/ (noindex is fine): badge files, embed code linking the winners page, a press-release paragraph template, a LinkedIn caption and logo usage rules (A64, A68, A44).
- Within 24 hours of the ceremony (by 10:00 IST the next day), the awards team emails every winner the kit, their photos and their row's deep link (#<slug>), and asks for the link in newsroom posts, since the 2025 Qualitrix release carried no link to worldaisummit.com. Optional before the event: send finalists the Finalist badge with a CTA to book delegate passes for their team using the 3+ group discount (10% off).
- Elets editorial publishes 'World AI Awards 2026: full list of winners' on the ceremony night or next morning on egov.eletsonline.com and/or cio.eletsonline.com with the winners page link in paragraph 1 and the winners table; Elets LinkedIn posts the full list with the link the same night (in 2025 this took 15 days).
- Only if nominations are still open: by 3 Oct publish a short story 'World AI Awards 2026: nominations close PLACEHOLDER_DEADLINE October; winners to be honoured at World AI Summit, Bengaluru' on egov and/or cio with an in-body link to https://www.worldaisummit.com/awards/ (anchor 'World AI Awards 2026'); no 2026 deadline is published anywhere the verifier could find. Also add a link to the 2026 awards page from egov.eletsonline.com/2025/07/world-ai-awards-2025-celebrating-architects-of-the-ai-era/ and set the /nomination 301 from A66.
- 2025 winners: publish the full official 2025 list from Elets records at PLACEHOLDER_2025_WINNERS_LOCATION (F72: a new /awards/winners-2025/ by 6 Oct, linked from /awards/ and /1st-edition/awards.html; F77 and F82: a winners section on /1st-edition/awards.html). The 10 Oct 2025 LinkedIn post names only Purview Services, Syngenta Group (Cropwise Grower), Altio AI, Familywala Eshop and Crisil Corporate Technology, so it is not the full list.

**Why**

- No winners page has ever existed on worldaisummit.com; 2025 winners appeared only in a World AI Summit LinkedIn post on 10 Oct 2025, 15 days after the 25 Sep 2025 ceremony (Exa; F72, F77, verifier confirmed).
- 2025 winner posts carried no link to the event site: Senthil Bhardwaj on LinkedIn 27 Sep 2025; Qualitrix on qualitrix.com 29 Sep 2025, copied on livemint24.com (a lookalike pay-to-publish site) on 29 Oct 2025; neither version links to worldaisummit.com (verifiers on F73, F77). LinkedIn links are nofollow.
- GSC non-www, 16 months: /awards is the second-largest page with 207 clicks, 8,825 impressions, average position 8.1; 31 Aug-28 Sep 2026: 1,300 impressions, 32 clicks, position 7.9, mostly from generic 'ai awards 2026' and 'ai awards' queries ('world ai awards' 44 impressions at position 3) (F51, F77, verifiers).
- SERP 'world ai awards 2025 winners', India, 1 Oct 2026: worldawards.ai #1 (a different 'World AI Awards' with '500 categories'), globalaiaward.com/winners #2, instagram.com/worldaiawards #3, worldaisummit.com/awards #4 with no winners content (verifier on F72).
- Verifier on F77: award pages got 25, 28 and 9 impressions on 24-26 Sep 2025 with 0 clicks, and 1 click in total from 27 Sep to 31 Oct 2025; queries containing 'winner' sent 2 impressions in 16 months. award.html states '75+ Awards to be Presented'; real non-Elets referring domains number about 10 (F73).

**Expected effect:** Organic traffic in 14-17 Oct about zero: winners queries have no measurable India volume and the plain 'world ai awards' name collides with worldawards.ai. Referral: tens to low hundreds of visits from winners' LinkedIn and WhatsApp shares on the night and the next day, provided the page is live within hours, against zero link targets in 2025. Leads: 2027 nomination interest and warm sponsor leads, about a year from converting; the 'nominations close' story is the only awards step that can bring nominators inside the window, and only if nominations are still open. Backlinks from winner newsrooms arrive weeks after the window.


**Decisions needed**

- 2026 ceremony date and time, and number of categories and winners
- Winners page URL (/awards/winners-2026/ or /awards/2026-winners/)
- Where the official 2025 winners list is published, and who supplies it from Elets records
- 2026 nomination deadline and whether nominations are still open
- 2026 nomination fee for any copy: 2025 was Rs 18,000 + GST (Startup and Individual) and Rs 20,000 + GST (Enterprise, Government, Leadership, Solution Provider), while /award.html currently says 'from 30k + GST'
- Who signs off the results sheet on the night

**Assets:** A68, A63, A64, A66, A44, A47


### G4. Fix the 2025 archive before 12 Oct, then switch the homepage and /delegate/ to 2027 lead capture on the evening of 15 Oct

**Impact 2/10, confidence high, effort S-M, about 9-10 hours (archive 4-5h incl. 1h recap; switch 3-5h with forms prepared in advance), owner web dev (banner include, titles, sitemap, forms, hero) + marketing (copy) + content (recap), by Pass-page banner by 5 Oct; archive titles, banner and sitemap by 12 Oct; switch prepared by 13 Oct and live on 15 Oct evening.**


**Do this**

- By 5 Oct: on https://www.worldaisummit.com/1st-edition/delegate-pass.html replace the 2025 purchase form with a banner linking to https://www.worldaisummit.com/delegate/ (and, after 15 Oct, to the 2027 interest form); keep the URL at 200, do not delete it. Check whether the 2025 checkout still accepts payments.
- By 12 Oct: add an archive banner on every /1st-edition/ page ('This is the 2025 archive. World AI Summit 2026: 14-15 Oct 2026, Bengaluru', linking to / and /delegate/); give each page a unique title and meta (8 pages share the exact title 'World AI Summit 2025'; remove 'Register now & be part of the revolution!'); add a short verified recap at the top of /1st-edition/ (dates 25-26 Sep 2025, theme 'AI for All: Powering India's Inclusive and Responsible AI Future', organiser figures attributed to the Elets wrap-up release, links to the 2025 session videos and to the 2025 winners list from G3). Titles, meta, banner and recap are in A72.
- Sitemap: remove or 301 the 4 /1st-edition/ URLs that return 302 (thematic-tracks, what-to-expect-world-ai-summit-2025-agenda-highlights, why-attend-the-world-ai-summit-2025-in-bengaluru-7-straightforward-reasons-to-show-up, world-ai-summit-2025-bengaluru-to-host-the-most-futuristic-and-deep-tech-ai-confluence); two of them redirect to /1st-edition without a trailing slash, so point the 301s at the final page. Do not rename /1st-edition/: it ranks and the edition numbering is inconsistent.
- Prepare by 13 Oct and switch at PLACEHOLDER_SWITCH_TIME (F78: 19:00 IST on 15 Oct; F62: 15 Oct evening; F51: 17 Oct): replace the homepage hero ('Save the date' and the Premium Pass Rs 20,000 block) with a 'Thank you, Bengaluru' hero carrying four CTAs: Highlights (the G1 hub), Winners (the G3 page), 'Register interest for World AI Summit 2027' (form: name, email, company, interest attend / sponsor / speak / nominate) and 'Partner in 2027: get the partnership deck first' (form routed to partnerships@worldaisummit.com). Show the Highlights and Winners CTAs only if those pages are live; otherwise drop them rather than link to a 404.
- Keep the homepage <title> as World AI Summit 2026 until 2027 dates are fixed (it holds #1 for the brand plus 2026 queries); keep the WhatsApp community CTA; keep /delegate/ live at 200 but replace the pass purchase with the 2027 interest form and a link to the recordings form; do not 404 or redirect either URL.
- Add the same '2027 edition: express interest / sponsor' line to the speaker pages (G5) and /awards/ (G3) so every post-event link lands on a page with a form.
- Only once dates are confirmed, add a block for the next Elets AI event; the 2025 precedent was the pivot to the Elets India AI Summit (22 Jan 2026, New Delhi), and indiaaisummit.in still promotes Jan 2026.

**Why**

- Homepage (Exa, 1 Oct 2026) shows 'Secure your seat', Premium Pass Rs 20,000, group booking 10% off and a WhatsApp community CTA; after 15 Oct these become dead ends while the homepage takes nearly all brand traffic (#1 for brand queries, project context) (F78).
- GSC non-www, 1 Jun 2025 to 28 Sep 2026: 'world ai summit bengaluru' 85 clicks, 185 impressions, average position 2.6; 'world ai summit elets' 56 clicks, 85 impressions; the two largest queries (F78, verifier confirmed).
- Verifier on F62: after the 25-26 Sep 2025 event, daily impressions on the non-www property fell from about 46 to 1-6 within two days with near-zero clicks, so post-event lead counts will be small.
- Audit c1b16b55, /1st-edition/: 11 www URLs return 200 and sit in the sitemap with crawlDepth null (orphaned), 4 www URLs return 302 while listed in the sitemap, 5 non-www URLs 301 to www; 8 pages share the title 'World AI Summit 2025'; /1st-edition/delegate-pass.html is indexable, in the sitemap and still sells 2025 passes a year on (F82, verifier).
- SERP India, 1 Oct 2026: /1st-edition/world-ai-agenda.html (89 words) #15 for 'world ai summit 2025' and #8 for 'world ai summit bengaluru 2025'; GSC shows no impressions for any '2025' query since late May 2026 (the 300 impressions quoted were Feb-Apr 2026) (F82, verifier). bengalurutechsummit.com keeps one evergreen root URL, now showing the 29th edition, 17-19 Nov 2026 at BIEC (F62, verifier).

**Expected effect:** No new traffic. It stops visitors paying for a finished event or a 2025 pass and converts 15-17 Oct brand traffic into 2027 delegate, sponsor and award interest; the count is unknown and probably small given the two-day collapse in impressions after the 2025 event. Archive fixes bring tens of visits at most inside the window. Cheap insurance against the 2025 precedent of stale pass pages staying live for a year.


**Decisions needed**

- Exact switch time (19:00 IST 15 Oct, or 17 Oct after the highlights phase)
- Whether the 2025 checkout still accepts payments
- 2027 dates and venue (until known, copy must say 'register interest')
- Dates of the next Elets AI event before any block is added

**Assets:** A69, A55, A72


### G5. Send every speaker and partner a share kit linking to their speaker page, then fill session details into the 50 live speaker pages by 16 Oct

**Impact 2/10, confidence medium, effort M, about 40 hours across kit emails, quote cards, same-day photo selects and 50 page updates (web dev 3-4h for the pages), owner marketing (kits, quote cards) + secretariat (emails) + content (page text) + web dev (page edits or generator change) + photographer on site, by Pre-event kit by 13 Oct; post-session kits within 24 hours (by 16 Oct for Day 2); speaker page updates by 16-17 Oct.**


**Do this**

- 13 Oct: the secretariat emails each of the 50 confirmed speakers their live page URL (https://www.worldaisummit.com/assets/speaker_details/<slug>.html) and a 'Speaking at World AI Summit 2026' card linking to it with UTM; exhibitors and partners get the same kit (A71, A44).
- 14-15 Oct: World AI Summit and Elets LinkedIn posts tag each speaker with the speaker-page URL plus UTM, not lnkd.in links; quote cards carry a verbatim quote from the recording, approved by the speaker, and a deep link to the G1 hub session anchor (/agenda/#<session-id>), which needs G1 live and sessions locked first. In 2025 the WAIS posts ended 'Stay tuned for more insights' with no link.
- Within 24 hours of each session (Day 2 by 16 Oct): send the speaker their named, captioned stage photo and one quote card; ask them to include the link in their LinkedIn post and, where their company keeps a speaker or media page, a 'Speaking' entry. Exhibitors and partners get a booth photo plus the hub link.
- By 16 Oct, replace 'Session title, time and hall will be published on this page once the agenda is final' on every live speaker page with the actual session title, format, hall, date, photo and video link. Choose the method first: the repo generator at worldaisummit/speakers/ supports session fields, but speakers.json has 0 of 76 entries with a session object (50 confirmed_2026) and it writes to /speakers/<slug>/, not the live /assets/speaker_details/<slug>.html, so either change speakers_path and the template before a rebuild, or edit the live HTML by hand.
- Fix pages still framed as 2025, for example /assets/speaker_details/priyank-kharge.html titled 'Shri Priyank Kharge | Chief Guest | World AI Summit 2025', and link the speaker pages internally from /speaker.html and the G1 hub (about 51 are in the sitemap with crawlDepth null).
- 16-17 Oct: secretariat sends 'thank you, your session page and photos' with ready LinkedIn copy, and the speaker pages carry the '2027 edition: express interest / sponsor' line from G4.
- Never write bios from memory; quote only what was said on stage.

**Why**

- Exa, 1 Oct 2026: the live pages for sanjeev-gupta, ram-mohan-rao, sandeep-varaganti, shalini-kapoor and pankaj-kumar-pandey show the session placeholder; the live speaker index lists 50 confirmed 2026 speakers (F48, verifier).
- 2025 speakers posted their own recaps without links: Satish Grampurohit (29 Sep 2025), Vivek Rajagopal (23 Oct 2025), award winner Senthil Bhardwaj (27 Sep 2025); the WAIS LinkedIn page's session posts (for example 'Keynote Address: AI for the Public Good', 25 Sep 2025) linked to no worldaisummit.com page (F81).
- Audit c1b16b55: about 51 speaker pages under /assets/speaker_details/ are in the sitemap with crawlDepth null (not internally linked); priyank-kharge.html is titled 'World AI Summit 2025' (F81).
- speakers.json in the repo: 0 of 76 entries have a session object; the generator outputs /speakers/<slug>/ while the live pages sit at /assets/speaker_details/<slug>.html, so a rebuild and upload would create a second set of URLs (verifiers on F48, F81).
- Speaker pages already rank for several speaker names (context); 'world ai summit speakers': homepage #2, /speaker.html #7 (F81). LinkedIn links are nofollow, so this is referral traffic only (verifiers on F73, F81).

**Expected effect:** Tens to low hundreds of referral visits over 14-17 Oct, in proportion to how many of the 50 speakers and the partners share a link (unknown; 2025 showed they post unprompted). No organic gain inside the window: new '[speaker] world ai summit' rankings need Google to index pages that are not internally linked, which rarely happens in days. Leads: speakers' networks are senior AI buyers, the 2027 sponsor and delegate audience, and each shared post lands on a page carrying the 2027 form.


**Decisions needed**

- Whether to deploy the /speakers/ build (after changing the path) or edit /assets/speaker_details/ pages by hand
- Speaker approval process and turnaround for quote cards
- Session anchors depend on G1 being live and the programme locked

**Assets:** A71, A44


### G6. Run an Elets editorial calendar for 12-16 Oct with descriptive anchors to working worldaisummit.com URLs and UTM tags

**Impact 2/10, confidence low, effort M, about 6-8 hours across five stories, owner Elets editorial (with content supplying the story briefs in A22 and headlines in A77), by Kick-off story 12 or 13 Oct; Day 1 story 14 Oct; Day 2 and winners 15-16 Oct; wrap-up by 16 Oct.**


**Do this**

- PLACEHOLDER_KICKOFF_DATE (12 Oct per F23; 13 Oct per F51 and F88): publish 'World AI Summit 2026 kicks off in Bengaluru on 14 October' on cio.eletsonline.com and the relevant vertical sites, with anchors 'World AI Summit 2026 agenda' pointing to the G1 hub (if it is not live, use the homepage agenda section or /ai-conference-bengaluru-2026.html, never /agenda/) and 'delegate passes' pointing to https://www.worldaisummit.com/delegate/ (valid until 15 Oct).
- 14 Oct Day 1 report and 15 Oct Day 2 report: headline starting 'World AI Summit 2026:', named speakers quoted only from the session record, a 1200px+ lead image, in-body links to the hub, the speaker pages and /awards/. In 2025 Elets published only two pieces, both in /press-release/ (24 Sep 'Kicks Off in Bengaluru Tomorrow' and 29 Sep 'Concludes Successfully'), so Day 1 and Day 2 stories are new work, not a repeat of a pattern.
- 15-16 Oct: 'World AI Awards 2026: full list of winners' linking to the winners page (step detailed in G3).
- 16 Oct, within 24 hours of the close and not 3 days later as in 2025: 'World AI Summit 2026 concludes' wrap-up with the anchor 'Partner with World AI Summit 2027' pointing to https://www.worldaisummit.com/partner-with-us.html and partnerships@worldaisummit.com, plus links to the highlights and winners URLs rather than only the homepage.
- Align the messaging: the 22 Sep 2026 cio.eletsonline.com article (/article/.../76367/) lists seven tracks that differ from the seven on worldaisummit.com and states '1,200+ delegates, 100+ speakers, 50+ startups'; new stories should use the current site's track names and figures.
- Tag every link with UTM so GA4 can attribute it: in September 2026 all Elets editorial subdomains together sent about 150 sessions and 2 key events, and the late-September cio articles sent 0 recorded sessions.
- Do not build a second live page on /blog/; the hub's LiveBlogPosting markup (G1) is the only live-badge candidate, and only if an Elets or WAIS property proves Top Stories eligible.

**Why**

- Exa, 1 Oct 2026: cio.eletsonline.com published 'World AI Summit 2025 Kicks Off in Bengaluru Tomorrow' (24 Sep 2025) and 'Concludes Successfully' (29 Sep 2025, three days after the 26 Sep close), both in /press-release/; no separate Day 1, Day 2 or winners stories were found (F23, F51, verifiers).
- eletsonline.com supplies 19,511 of 19,826 WAIS backlinks, so one more in-network link will not move rankings in 14 days (verifier on F75).
- GA4, September 2026: about 150 sessions and 2 key events from all Elets editorial subdomains together; late-September cio articles 0 recorded sessions; the 2025 peak was about 250 sessions from egov in a whole month (verifier on F75).
- OpenSEO: 'world ai summit 2025' had 390 searches in Sep 2025 and 170 in Oct 2025; 'ai summit highlights' averages 110 but runs 0-10 a month outside the Feb spike (F23).
- OpenSEO SERP, India, 1 Oct 2026, 'world ai summit 2025': no Top Stories block; neither 2025 Elets CIO article is in the first 20 results; GSC non-www 28 Jun-28 Sep 2026 shows zero rows for Discover and video, inconclusive because www is not connected (F88, verifier). Elets CIO already published WAIS 2026 pieces on 22 Sep and 30 Sep 2026 (verifier on F88).

**Expected effect:** Roughly tens of referral visits per story, more only if an Elets title enters Top Stories or Discover, which is unverified; probably tens to a few hundred visits across 12-17 Oct in total. Late pass sales from the kick-off story are possible but small (one or two selling days). The wrap-up gives sponsors a 2027 link; no measurable ranking change inside the window.


**Decisions needed**

- Kick-off story date (12 or 13 Oct)
- Whether Elets editorial commits to Day 1 and Day 2 reports beyond the two press releases it ran in 2025
- Google News and Top Stories eligibility of cio.eletsonline.com and egov.eletsonline.com (unverified)
- One agreed set of track names and headline figures across the site and Elets articles

**Assets:** A22, A77, A66


**Conflicts noted**

- Winners page URL: /awards/winners-2026/ (F62, F72, F73, F77) versus /awards/2026-winners/ (F51). G3 uses PLACEHOLDER_WINNERS_URL.
- Where the 2025 winners list lives: a new /awards/winners-2025/ by 6 Oct (F72) versus a 2025 winners section added to /1st-edition/awards.html (F77, F82). G3 uses PLACEHOLDER_2025_WINNERS_LOCATION.
- Live and highlights URL: one /agenda/ URL that changes phase (F76) versus /2026/live/, /2026/day-1-highlights/ and /2026/day-2-highlights/ (F51) versus /blog/world-ai-summit-2026-live-updates.html (F88) versus /blog/world-ai-summit-2026-highlights.html (F23). G1 recommends /agenda/ and lists the alternatives as a decision.
- Post-event hero switch time: 19:00 IST on 15 Oct (F78), 15 Oct evening (F62), highlights phase 12:00 IST 16 Oct (F76), recap 16-17 Oct (F88), hero switch 17 Oct (F51). G4 uses PLACEHOLDER_SWITCH_TIME.
- Elets kick-off story date: 12 Oct (F23) versus 13 Oct (F51, F88). G6 uses PLACEHOLDER_KICKOFF_DATE.
- Winners page publish deadline: within 1 hour of the ceremony (F51), within 2 hours (F72), by 23:00 IST on the ceremony day (F77); kit emails by 10:00 IST next day (F77) versus within 24 hours (F73). G3 uses PLACEHOLDER_PUBLISH_WINDOW.
- 2025 awards nomination fee: F77 says Rs 18,000 + GST per entry; its verifier (elets.net/worldaisummit-awards/, Exa 1 Oct) says two tiers, Rs 18,000 + GST for Startup and Individual and Rs 20,000 + GST for Enterprise, Government, Leadership and Solution Provider; task context says /award.html currently says 'from 30k + GST'.
- SERP position for 'world ai awards 2025 winners': F72 says WAIS /awards #5; the verifier and F77 say #4 organic (the tool's rank 5 counted the AI Overview block), with worldawards.ai #1.
- Qualitrix 2025 winner release: F72 and F73 cite livemint24.com dated 29 Oct 2025 (F77 says 34 days after the ceremony); the verifiers say it first appeared on qualitrix.com on 29 Sep 2025, 4 days after the ceremony, and the livemint24.com item is a later copy on a lookalike site. Neither version links to worldaisummit.com.
- Count of /1st-edition/ URLs: F82 says 14 return 200; its verifier counts 20 rows in audit c1b16b55: 11 www URLs returning 200, 4 www URLs returning 302 and 5 non-www URLs returning 301.
- Live page markup: NewsArticle with dateModified (F88) versus LiveBlogPosting with liveBlogUpdate entries (F51 and the F88 verifier). G1 uses LiveBlogPosting.
- Techcanvass list: F60 names a 'Top 10 Upcoming Tech Conference In Bangalore October'26' page at #7; the verifier found the fetched page is the September'26 edition, mostly free meetups, at #6-#7, and an October edition may not exist yet.
- 2025 Elets event-week coverage: F23 frames 'Repeat the 2025 pattern' as Day 1, Day 2 and winners stories; the verifier found only two 2025 pieces, both press releases (24 Sep and 29 Sep 2025).