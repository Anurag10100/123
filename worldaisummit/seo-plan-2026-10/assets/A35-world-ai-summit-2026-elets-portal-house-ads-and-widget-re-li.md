# A35: World AI Summit 2026: Elets portal house ads and widget re-link (2–15 Oct 2026)

- **For recommendation:** Bring back 2025-level World AI Summit house ads across the Elets portals: eGov referrals fell from 4,153 sessions to 27
- **Research lens:** elets-network
- **Format:** Markdown creative brief: go/no-go checks, copy deck for 728x90, 300x250 and 320x100, UTM link sheet, and HTML snippets for the widget
- **Placeholders the business must fill:**
  - PLACEHOLDER_SLOT_AVAILABLE_EGOV / _CIO / _BFSI / _EHEALTH / _DIGITALLEARNING (what the leaderboard and in-article slots carry today)
  - PLACEHOLDER_AWARDS_NOMINATION_DEADLINE (not shown on /awards/; if closed, drop the awards creatives)
  - PLACEHOLDER_CURRENT_PASS_PRICE (/delegate/ Standard tier expired 30 Sept 2026; Late Access ₹30,000/₹60,000; homepage says ₹20,000)
  - PLACEHOLDER_ROTATION_SPLIT (suggested 70% passes / 30% awards while nominations are open)
  - PLACEHOLDER_POPUP_DECISION (whether to bring back a 2025-style site-wide popup or interstitial)
  - PLACEHOLDER_REGISTRATION_CLOSE_DATE (for the optional final-days swap from 12 Oct)
  - PLACEHOLDER_GROUP_DISCOUNT_CONFIRMED (10% off for 3+ delegates, from project notes)
  - PLACEHOLDER_AWARDS_FEE (2025 was ₹18,000 + GST per entry; 2026 fee not published on /awards/)

## How to ship

1) Elets ad-ops runs the section 0 checks on 1–2 Oct. That covers the slots, the award deadline, the price and the widget link, and settles the popup decision and the rotation split. 2) A designer builds three sizes (728x90, 300x250, 320x100) for the pass creative, plus the awards set only if nominations are open. The copy stays exactly as written, with no exclamation marks. 3) Ad-ops loads them into each portal's ad server or CMS slots from 2 Oct to 15 Oct, using the per-portal links in section 3. The sector sub-lines run only on their own portal. 4) Web dev replaces the 'Visit Website' href on the egov homepage, egov /conferences/ and events.eletsonline.com with the section 4 snippets. They add 'Partner with us' only after checking what /partnership.html shows. 5) Once live, click each link and confirm the session shows up in GA4 Realtime with the right source, medium and campaign. 6) On 16 Oct, pull GA4 by campaign and source, and check passes and nominations against registration records. Sources: /delegate/ and /awards/ were read through Exa on 1 Oct 2026 (direct HTTP returns 403). The GA4 figures come from the verified context. No OpenSEO paid tools were used and no files were edited. On your question about CPUs: this cloud session's container reports 4 CPUs (nproc), and I can't add more from inside the session.

## Content

# World AI Summit 2026: Elets portal house ads and widget re-link
Run window: 2 Oct to 15 Oct 2026. Status as of 1 Oct 2026.

---

## 0. Go/no-go checks (do these first; owner: Elets ad-ops with WAIS marketing)

1. **What is in the slots now.** Check what currently runs in the header leaderboard and the in-article "Single Page Desktop Image" slot on egov, cio, bfsi, ehealth and digitallearning.eletsonline.com. The only evidence that these slots carry Elets house ads is a page crawled in Aug 2026 showing an India Energy Expo ad, and that event ran 18–19 Aug 2026. We can't see what the slots show today: the portals return 403 to our tools, and the cached copies stop in early Aug. Fill in per portal: PLACEHOLDER_SLOT_AVAILABLE_EGOV / _CIO / _BFSI / _EHEALTH / _DIGITALLEARNING.
2. **Award nominations.** /awards/ (Exa fetch, 1 Oct 2026) shows the nomination form but no closing date, category list or fee. Run the awards creatives only if nominations are open. Deadline: PLACEHOLDER_AWARDS_NOMINATION_DEADLINE. If it is closed or still unconfirmed on 2 Oct, run only the pass creatives.
3. **Price.** /delegate/ (Exa fetch, 1 Oct 2026) lists Standard Access at ₹20,000 / ₹35,000 "valid till 30th Sept 2026", which has now expired, and Late Access at ₹30,000 / ₹60,000. The homepage still says Premium ₹20,000. The copy below therefore leaves price out. If you want a price line, fix the two pages so they agree, then use PLACEHOLDER_CURRENT_PASS_PRICE.
4. **Widget link.** We have not verified where the "Visit Website" button for World AI Summit 2026 points today (egov homepage, egov /conferences/, events.eletsonline.com). Check it in the CMS. If it already goes to /delegate/, just add the UTMs from section 4.
5. **Expected volume.** The egov "Upcoming Conferences" widget already lists World AI Summit 2026 and brought 27 referral sessions in Jul–Sep 2026. The 2025 figure of 4,153 sessions is not a like-for-like comparison:
   - It included the event days (25–26 Sep 2025).
   - It recorded 0 key events, because key events were not set up then.
   - It had a 36.7% engagement rate from 3,472 users, which looks like a site-wide popup (inferred).

   Banners in standard slots will not bring that volume back, so treat this as low cost and low volume. Elets email (r.emails.elets.in: 263,703 sessions and 159 key events in Jul–Sep 2026) is still the main channel, and portal banners mostly reach the same readers again. Whether to run a popup or interstitial again is a business decision: PLACEHOLDER_POPUP_DECISION.
6. **Rotation split** while nominations are open: PLACEHOLDER_ROTATION_SPLIT (suggested 70% passes / 30% awards). Once nominations close, show passes only.

---

## 1. Delegate pass creatives (run 2–15 Oct, all five portals)

### 728x90 leaderboard
- Line 1: World AI Summit 2026 · Bengaluru · 14–15 October
- Line 2: Sheraton Grand Bangalore at Brigade Gateway
- Button: Book your delegate pass →
- Single-line version (122 characters; use it only if the layout fits): World AI Summit 2026 · Bengaluru · 14–15 October · Sheraton Grand Bangalore at Brigade Gateway · Book your delegate pass →
- Alt text: World AI Summit 2026, Bengaluru, 14–15 October, Sheraton Grand Bangalore at Brigade Gateway. Book your delegate pass.

### 300x250 MPU (in-article slot)
- Headline: Seven tracks. Two days.
- Sub-line: One room for India's AI decision-makers.
- Detail: World AI Summit 2026 · Bengaluru · 14–15 Oct
- Button: Book now →
- Alt text: Seven tracks. Two days. One room for India's AI decision-makers. World AI Summit 2026, Bengaluru, 14–15 October. Book now.

### 320x100 mobile
- Line: World AI Summit 2026 · Bengaluru · 14–15 Oct
- Button: Book your pass →
- Alt text: World AI Summit 2026, Bengaluru, 14–15 October. Book your delegate pass.

### Optional portal sub-lines for the MPU
These replace the "One room…" sub-line. The track names come from the 2026 programme.
- egov only: Tracks: AI for Bharat; Sovereign AI & Geopolitics.
- bfsi only: Tracks: Enterprise AI in Production; Capital, Founders & Exits.
- cio only: Tracks: GCCs; Enterprise AI in Production.
- ehealth, digitallearning: keep the default sub-line. No track is specific to these sectors.

### Optional final-days swap (from 12 Oct, only if registration is still open)
- MPU sub-line: Registrations close PLACEHOLDER_REGISTRATION_CLOSE_DATE.
- Optional extra line: Groups of three or more save 10%. (From project notes. Confirm with registration@worldaisummit.com before use: PLACEHOLDER_GROUP_DISCOUNT_CONFIRMED.)

---

## 2. World AI Awards creatives (2 Oct until PLACEHOLDER_AWARDS_NOMINATION_DEADLINE)

### 728x90 leaderboard
- Line: World AI Awards 2026: nominations open
- Button: Submit your AI project →
- Alt text: World AI Awards 2026: nominations open. Submit your AI project.

### 300x250 MPU
- Headline: World AI Awards 2026
- Sub-line: Nominations open.
- Footer: World AI Summit 2026 · Bengaluru · 14–15 Oct
- Button: Submit your AI project →
- Optional fee line: Entry fee PLACEHOLDER_AWARDS_FEE. The 2025 fee was ₹18,000 + GST per entry; /awards/ does not show a 2026 fee.
- Optional deadline line: Last date PLACEHOLDER_AWARDS_NOMINATION_DEADLINE.

### 320x100 mobile
- Line: World AI Awards 2026: nominations open
- Button: Submit your project →

---

## 3. Banner links (utm_medium=house_banner)

Delegate pass creatives:
- egov: https://www.worldaisummit.com/delegate/?utm_source=egov&utm_medium=house_banner&utm_campaign=world_ai_summit_2026_delegate
- cio: https://www.worldaisummit.com/delegate/?utm_source=cio&utm_medium=house_banner&utm_campaign=world_ai_summit_2026_delegate
- bfsi: https://www.worldaisummit.com/delegate/?utm_source=bfsi&utm_medium=house_banner&utm_campaign=world_ai_summit_2026_delegate
- ehealth: https://www.worldaisummit.com/delegate/?utm_source=ehealth&utm_medium=house_banner&utm_campaign=world_ai_summit_2026_delegate
- digitallearning: https://www.worldaisummit.com/delegate/?utm_source=digitallearning&utm_medium=house_banner&utm_campaign=world_ai_summit_2026_delegate

Awards creatives:
- egov: https://www.worldaisummit.com/awards/?utm_source=egov&utm_medium=house_banner&utm_campaign=world_ai_awards_2026
- cio: https://www.worldaisummit.com/awards/?utm_source=cio&utm_medium=house_banner&utm_campaign=world_ai_awards_2026
- bfsi: https://www.worldaisummit.com/awards/?utm_source=bfsi&utm_medium=house_banner&utm_campaign=world_ai_awards_2026
- ehealth: https://www.worldaisummit.com/awards/?utm_source=ehealth&utm_medium=house_banner&utm_campaign=world_ai_awards_2026
- digitallearning: https://www.worldaisummit.com/awards/?utm_source=digitallearning&utm_medium=house_banner&utm_campaign=world_ai_awards_2026

Optional size split: add &utm_content=728x90, &utm_content=300x250 or &utm_content=320x100 to the end of each link.

---

## 4. Conference widget re-link (web dev)

egov homepage, "Upcoming Conferences" widget, World AI Summit 2026 row:
```html
<a href="https://www.worldaisummit.com/delegate/?utm_source=egov&utm_medium=conference_widget&utm_campaign=world_ai_summit_2026_delegate&utm_content=homepage" target="_blank" rel="noopener">Visit Website</a>
```

egov /conferences/ page, same row:
```html
<a href="https://www.worldaisummit.com/delegate/?utm_source=egov&utm_medium=conference_widget&utm_campaign=world_ai_summit_2026_delegate&utm_content=conferences" target="_blank" rel="noopener">Visit Website</a>
```

events.eletsonline.com, World AI Summit 2026 listing:
```html
<a href="https://www.worldaisummit.com/delegate/?utm_source=events&utm_medium=conference_widget&utm_campaign=world_ai_summit_2026_delegate" target="_blank" rel="noopener">Visit Website</a>
```
utm_content is optional here. It separates the homepage and /conferences/ placements in GA4. Optional label change: "Book delegate pass" instead of "Visit Website".

"Partner with us" link, placed next to the button:
```html
<a href="https://www.worldaisummit.com/partnership.html?utm_source=egov&utm_medium=conference_widget&utm_campaign=world_ai_summit_2026_partner" target="_blank" rel="noopener">Partner with us</a>
```
/partnership.html canonicalises to the homepage. Open it before linking and check that it shows partnership content. If it doesn't, use `mailto:partnerships@worldaisummit.com` instead.

---

## 5. Measurement (report on 16 Oct)
- GA4: Reports → Acquisition → Traffic acquisition. Filter Session campaign to world_ai_summit_2026_delegate and world_ai_awards_2026, and add Session source as a secondary dimension.
- Baselines (Jul–Sep 2026): egov referral 27 sessions; events.eletsonline.com 164; eletsonline.com 232 sessions and 2 key events.
- Key events are not proof of sales. /thankyou.html logs 391 key events, and transactions and revenue are 0 across the whole property because ecommerce tracking is not set up. Count paid passes with the registration team, matched to each booking's UTM source.

