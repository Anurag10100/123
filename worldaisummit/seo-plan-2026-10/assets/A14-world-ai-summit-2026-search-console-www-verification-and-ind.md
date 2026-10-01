# A14: World AI Summit 2026: Search Console (www) verification and indexing checklist

- **For recommendation:** Verify the www (Domain) Search Console property today and use it to get the 2026 money pages indexed before 14 Oct
- **Research lens:** search-console
- **Format:** Markdown checklist with copy-paste DNS, HTML, shell and IndexNow snippets (Indian English)
- **Placeholders the business must fill:**
  - PLACEHOLDER_GSC_USER_EMAIL - Google account that will own or manage the new Search Console property
  - PLACEHOLDER_SECOND_OWNER_EMAIL - second Owner so access is not tied to one person
  - PLACEHOLDER_GSC_TOKEN - google-site-verification token shown by Search Console (DNS TXT value or meta tag content)
  - PLACEHOLDER_SPEAKER_PAGE_URLS - /assets/speaker_details/<slug>.html URLs for speakers confirmed for 2026 only, taken from the live sitemap, with 2025 framing removed
  - PLACEHOLDER_INDEXNOW_KEY - IndexNow key generated on Bing's IndexNow page, also used as the key file name

## How to ship

1. Paste the checklist into the team task tracker or a shared doc, and split it by owner. Web dev takes sections 0-2 and 6. Marketing takes sections 3-5.
2. Fill in PLACEHOLDER_GSC_USER_EMAIL and PLACEHOLDER_SECOND_OWNER_EMAIL before sending.
3. PLACEHOLDER_GSC_TOKEN and PLACEHOLDER_INDEXNOW_KEY are filled in at execution time, from Search Console and Bing.
4. Build PLACEHOLDER_SPEAKER_PAGE_URLS from the live sitemap. Include only speakers confirmed for 2026 whose pages no longer say 2025.
5. Section 0 (add the property) has to happen on 1 Oct, because Search Console data starts only from the day a property is added.

Sources:
- Verifier corrections are applied: key events instead of form_submit, likely-indexed status from GA4, no data backfill, IndexNow as a dev task, quota treated as approximate.
- IndexNow request format and response codes were checked live today at bing.com/indexnow/getstarted.
- The no-backfill rule comes from support.google.com/webmasters/answer/34592, as fetched by the verifier.
- No OpenSEO paid tools were used, and no files were edited.

On the user's own question ("do you have more CPUs?"): this container reports 4 CPUs (nproc). More throughput would come from running more agents in parallel, not from extra CPUs on this machine.

## Content

# World AI Summit 2026: Search Console (www) and indexing checklist

**Owners:** web dev (DNS or GA4 admin), marketing (indexing requests, OpenSEO, Bing) · **Prepared:** 1 Oct 2026 · **Event:** 14-15 Oct 2026, Bengaluru

**Why this matters.** Only one Search Console property is verified: the URL-prefix `https://worldaisummit.com/` (non-www). Every live page is on `https://www.worldaisummit.com/`. As a result, Search Console and OpenSEO cannot see the queries behind 2,984 google / organic sessions (GA4, 3-30 Sep). URL Inspection on www pages returns "Search Console denied access to this property".

---

## 0. Today, before anything else (5 min). Due 1 Oct

- [ ] Ask the web team, the eletsonline.com team and any agency whether someone already owns a **Domain** property `worldaisummit.com` or a URL-prefix property `https://www.worldaisummit.com/`. If someone does, ask them to add PLACEHOLDER_GSC_USER_EMAIL as Owner (Settings > Users and permissions), then skip to section 2. An existing property keeps its history.
- [ ] If nobody has one, **add the property today, even if verification has to wait.** Google starts collecting data as soon as a property is added, even before it is verified (support.google.com/webmasters/answer/34592). Days before that date are not backfilled.

## 1. Add and verify the property. Web dev, 1 Oct (2 Oct at the latest)

### Option A (preferred): Domain property, which covers www, non-www, http and https

- [ ] Search Console > property selector > Add property > **Domain** > `worldaisummit.com` > Continue. Copy the verification token.
- [ ] At the DNS host for worldaisummit.com, **add a new record**. Do not edit or delete existing TXT records such as SPF.

| Field | Value |
|---|---|
| Type | TXT |
| Host / Name | `@` (some panels want this blank, or `worldaisummit.com.`) |
| Value | `google-site-verification=PLACEHOLDER_GSC_TOKEN` (paste exactly as Search Console shows it) |
| TTL | default (or 3600) |

- [ ] Check that the record is live. This should print the google-site-verification line:

```bash
dig +short TXT worldaisummit.com
```

- [ ] Click **Verify** in Search Console. If it fails, wait for DNS to update and try again. Keep the record permanently, because deleting it removes verification.

### Option B (use if DNS access will take more than a day): URL-prefix property `https://www.worldaisummit.com/`

- [ ] **Google Analytics method.** gtag `G-QEB6N0MFLC` already loads on www pages. The snippet must sit in the `<head>` of the homepage, and the Google account doing the verification needs Edit (Editor) access on GA4 property 490291049.
- [ ] **HTML tag method.** Put this inside `<head>` of `https://www.worldaisummit.com/` (before `</head>`), upload the page, then click Verify. Keep the tag permanently.

```html
<meta name="google-site-verification" content="PLACEHOLDER_GSC_TOKEN" />
```

- [ ] If you use Option B, keep the existing non-www property. It holds the /awards history: 79 clicks, 2,419 impressions and average position 9.1 over the last 3 months. Add the Domain property once DNS access is available.

### Either option

- [ ] Add a second Owner (PLACEHOLDER_SECOND_OWNER_EMAIL) so access does not depend on one person.

## 2. Sitemap. Web dev, same day

robots.txt already points to `https://www.worldaisummit.com/sitemap.xml`. Nobody has checked the sitemap's contents yet (it could not be fetched during the audit), so check it before you submit. **Both commands below should print nothing.**

```bash
# 1) Any <loc> that is not on https://www.worldaisummit.com/
curl -s https://www.worldaisummit.com/sitemap.xml | grep -o '<loc>[^<]*</loc>' | grep -v '<loc>https://www\.worldaisummit\.com/'

# 2) Any listed URL that does not return 200 (redirects, 404s)
curl -s https://www.worldaisummit.com/sitemap.xml | grep -o '<loc>[^<]*</loc>' | sed -e 's/<loc>//' -e 's/<\/loc>//' | while read -r u; do printf '%s %s\n' "$(curl -s -o /dev/null -w '%{http_code}' "$u")" "$u"; done | grep -v '^200 '
```

- [ ] Remove these from the sitemap if they are listed: `/index.html`; `/registration` and `/registration.html` (302 to the homepage); `/award.html`, `/partner-with-us.html` and `/partnership.html` (canonical to `/`); any non-www or http URL.
- [ ] In the new property: Sitemaps > enter `https://www.worldaisummit.com/sitemap.xml` > Submit. Check that the status reads "Success".

## 3. URL Inspection and Request indexing. Marketing, starting once the property is verified (target 2 Oct)

**Quota:** Google does not publish one. Third-party sources put it at about 10-12 URLs per property in a rolling 24 hours, so treat that as approximate. A request does not guarantee crawling or indexing.

**What GA4 already shows (3-30 Sep).** These www pages had google / organic landings, so they are very likely indexed already:

| Page | Organic sessions | Key events |
|---|---|---|
| /delegate | 48 | 16 |
| /awards | 76 | not checked |
| /award.html | 61 | not checked |
| /ai-conference-bengaluru-2026.html | 12 | 3 |
| /speaker.html | 1 | not checked |
| /blog | 1 | not checked |

For these pages a request mostly prompts a re-crawl. No organic landings were seen on any `/assets/speaker_details/` page, so the speaker pages are the real indexing gap.

**Rule for every URL: inspect first.**

- If it says "URL is on Google" and the page has not changed since the last crawl date shown, **skip it** and give the slot to a speaker page.
- If it says "URL is not on Google", or the page changed after the last crawl, click **Request indexing**.

**Day 1 (2 Oct), in this order:**

1. https://www.worldaisummit.com/delegate/
2. https://www.worldaisummit.com/awards/
3. https://www.worldaisummit.com/ai-conference-bengaluru-2026.html
4. https://www.worldaisummit.com/speaker.html
5. https://www.worldaisummit.com/assets/speaker_details/index.html
6. https://www.worldaisummit.com/blog/
7. https://www.worldaisummit.com/assets/speaker_details/priyank-kharge.html
8. Use any remaining slots for PLACEHOLDER_SPEAKER_PAGE_URLS (confirmed 2026 speakers only, copied from the sitemap)

**Days 2-3 (3-4 Oct):** the remaining confirmed 2026 speaker pages, then the 5 blog post URLs linked from /blog/.

- [ ] Do not request indexing for a speaker page that still frames the speaker as a 2025 speaker until that page is corrected. Do not request pages for speakers who are not confirmed for 2026.
- [ ] Log each request (URL, date, status before the request) in a shared sheet. Re-inspect the URLs on 6 Oct.

## 4. Point OpenSEO at the new property. Marketing, right after verification

- [ ] Go to app.openseo.so/p/eb76fdff-f482-423c-9a6d-08afeccaa111/settings/integrations > Search Console and select `sc-domain:worldaisummit.com` (or `https://www.worldaisummit.com/` if you used Option B). The Google account connected to OpenSEO must have access to that property.
- [ ] Check: inspecting `https://www.worldaisummit.com/delegate/` from OpenSEO no longer returns "Search Console denied access to this property".
- [ ] **What to expect from the data:**
  - If the property is new, query data starts on the day it was added, and Search Console runs about 2-3 days behind.
  - Pre-event queries (from about 2 Oct) should appear from about 5 Oct. You can use them to adjust pages before 14 Oct.
  - Event-week queries (13-16 Oct) will appear only around 16-19 Oct. Treat them as post-event learning for the next edition, not as input for changes during the event.

## 5. Bing Webmaster Tools. Marketing, same day as verification (10 min)

- [ ] bing.com/webmasters > Add site > **Import from Google Search Console**. This needs the property from section 1 to be verified, and it brings the site and its sitemaps across.
- [ ] Sitemaps: confirm `https://www.worldaisummit.com/sitemap.xml` is listed, or submit it.
- **Why:** in GA4 (3-30 Sep), chatgpt.com / ai-assistant sent 447 sessions and 29 key events, while bing / organic sent 79 sessions. We are inferring that a better Bing index will lift ChatGPT referrals; this has not been verified.

## 6. IndexNow. A small web dev task (about 1 hour), not a Bing setting

The site is static HTML, so there is no switch to turn this on. The steps below follow bing.com/indexnow/getstarted.

- [ ] Generate a key with the generator on Bing's IndexNow page. Record it as PLACEHOLDER_INDEXNOW_KEY.
- [ ] Upload a UTF-8 text file to `https://www.worldaisummit.com/PLACEHOLDER_INDEXNOW_KEY.txt`. Its only content should be the key.
- [ ] After each deploy, POST only the URLs added, changed or deleted since IndexNow was set up. Bing advises against submitting older URLs.

```bash
curl -s -o /dev/null -w '%{http_code}\n' -X POST 'https://api.indexnow.org/IndexNow' \
  -H 'Content-Type: application/json; charset=utf-8' \
  -d '{
    "host": "www.worldaisummit.com",
    "key": "PLACEHOLDER_INDEXNOW_KEY",
    "keyLocation": "https://www.worldaisummit.com/PLACEHOLDER_INDEXNOW_KEY.txt",
    "urlList": [
      "https://www.worldaisummit.com/delegate/",
      "https://www.worldaisummit.com/speaker.html"
    ]
  }'
```

- [ ] **Response codes:**
  - 200: submitted
  - 400: bad format
  - 403: key file not found, or the key is not in the file
  - 422: URLs are not on this host, or the key does not match
  - 429: too many requests
- [ ] If the site is behind Cloudflare, Crawler Hints in the Cloudflare dashboard is the managed alternative.
- [ ] Bing Webmaster Tools > IndexNow: confirm the URLs were received. IndexNow does not guarantee indexing, and it does not replace section 3 for Google.

---

## Done when

- [ ] The Domain property (or the www URL-prefix property) is verified, and a second Owner is added
- [ ] The sitemap is submitted with status "Success": www only, no redirecting or canonicalised URLs
- [ ] Day 1 inspections and requests are done and logged; Days 2-3 are scheduled
- [ ] OpenSEO points at the new property, and www URL inspection works
- [ ] The Bing import is done, the IndexNow key file is live, and the first POST returns 200

