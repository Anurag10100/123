# A56: Search Console access for www.worldaisummit.com: checklist for 1-2 Oct 2026

- **For recommendation:** Get Search Console access to the www host. Today Google tools can only see the non-www redirect host, so nothing that matters can be inspected or submitted
- **Research lens:** tech-indexing
- **Format:** Markdown checklist, ready to paste into a doc, email or Slack thread. It includes one HTML snippet for the web developer.
- **Placeholders the business must fill:**
  - PLACEHOLDER_GSC_OWNER
  - PLACEHOLDER_WEB_DEV
  - PLACEHOLDER_DNS_OWNER
  - PLACEHOLDER_DNS_HOST
  - PLACEHOLDER_AWARDS_CANONICAL_DECISION
  - PLACEHOLDER_OPENSEO_PROPERTY_CHOICE

## How to ship

1) Today (1 Oct), send this checklist to the marketing person who owns Search Console and to the web developer. Ask the DNS owner to complete Step 0 and Step A the same day. Adding the Domain property starts data collection even before it is verified. 2) If the TXT record has not verified by the morning of 2 Oct, the web developer does Step B: one meta tag in the head of index.html, about 10 minutes. 3) After verification, do Steps C and F, then check that OpenSEO can inspect https://www.worldaisummit.com/delegate/. 4) Run Step G one priority URL at a time as each page fix goes live, and keep the log. 5) Do not 301 non-www /awards and do not use Change of Address before 14 Oct. Replace every PLACEHOLDER_ marker before sharing. Leave <token> as written: Search Console generates it during setup. Changes from the original recommendation, per the verifier: the old non-www property is kept and used (non-www /awards ranks #2 and Request Indexing works there today); removing the old sitemap is dropped for the event window; a quota and priority list is added; and expected data timing is set to about a week. I could not look up the DNS host from this environment (no DNS tools, and an earlier DNS-over-HTTPS lookup was blocked). Unrelated to this task: the user asked whether more CPUs are available from the computer. That question was not addressed in this run.

## Content

# Search Console access for www.worldaisummit.com

**Deadline:** add the property on 1 Oct and finish verification by 2 Oct 2026
**Owners:** PLACEHOLDER_GSC_OWNER (marketing, Search Console), PLACEHOLDER_WEB_DEV (homepage `<head>`), PLACEHOLDER_DNS_OWNER (DNS or registrar)
**Time needed:** 15 to 45 minutes of work. DNS propagation time depends on the DNS host.

## Why we are doing this

- Today Search Console (and OpenSEO) is connected only to the URL-prefix property `https://worldaisummit.com/` (non-www). Every www URL returns "Search Console denied access to this property" when inspected, so we cannot inspect, request indexing for or measure `/delegate/`, `/awards/`, the homepage or the new pages.
- The old non-www property still matters. Non-www `/` redirects to www, but non-www `/awards` returns 200, is "Submitted and indexed" under its own canonical (`https://worldaisummit.com/awards`, last crawled 28 Sep), shows an Event rich result, and ranks #2 for "world ai awards". From 28 Jun to 28 Sep it had 79 clicks, 2,419 impressions and an average position of 9.1. **Keep that property and keep that URL live.**
- Search Console starts collecting data for a property as soon as anyone adds it, even before verification. Google adds that "it takes a few days for data to start to accrue". **So add the Domain property today, even if DNS verification will be slow.**

---

## Step 0. Before you start (5 minutes)

- [ ] Find out who manages DNS for worldaisummit.com: PLACEHOLDER_DNS_HOST, contact PLACEHOLDER_DNS_OWNER. If a developer has terminal access, these two commands show the nameservers and any existing TXT records:
  `dig +short NS worldaisummit.com`
  `dig +short TXT worldaisummit.com`
- [ ] Check whether another Elets Google account already owns a Domain or www property. One sign is a TXT record that starts with `google-site-verification=`. If such a property exists, ask its owner to add PLACEHOLDER_GSC_OWNER under Settings > Users and permissions > Add user (Owner or Full). Do not create a second property in that case.
- [ ] Never delete or edit an existing `google-site-verification` TXT record, an SPF record or any other TXT record. Google warns that you must not "overwrite the verification tokens of any other owners".

## Step A. Domain property (preferred, covers www, non-www, http and https)

- [ ] Go to https://search.google.com/search-console, open the property selector, click **Add property** and choose **Domain**.
- [ ] Enter `worldaisummit.com` (no `https://`, no `www`) and click Continue.
- [ ] Copy the TXT value Google shows: `google-site-verification=<token>`
- [ ] At the DNS host, add a **new** TXT record:
  - Host or Name: `@` (some hosts want this left blank or set to `worldaisummit.com`)
  - Type: `TXT`
  - Value: `google-site-verification=<token>`
  - TTL: the default, or 3600
- [ ] Back in Search Console, click **Verify**. If it fails, the record has not propagated yet. Leave it and try again later. The property stays added and keeps collecting data while you wait.
- [ ] Do not remove the TXT record later. Google rechecks verification from time to time.
- [ ] Once the Domain property is verified, any URL-prefix property you add under it (for example `https://www.worldaisummit.com/`) is verified automatically.

## Step B. Fallback if DNS will take more than a day: URL-prefix property for www

- [ ] Click Add property, choose **URL prefix** and enter `https://www.worldaisummit.com/` exactly, with the trailing slash.
- [ ] Choose the **HTML tag** method and copy the tag.
- [ ] The web developer pastes the tag inside `<head>` of the homepage file (`index.html` at the site root, the file served at https://www.worldaisummit.com/), then uploads it:

```html
<head>
  <meta charset="utf-8">
  <meta name="google-site-verification" content="PASTE_TOKEN_FROM_SEARCH_CONSOLE">
  <!-- existing title, meta and link tags follow -->
```

- [ ] Open view-source of https://www.worldaisummit.com/ and confirm the tag is live, then click **Verify**.
- [ ] Leave the tag in place permanently.
- [ ] Option with no code change: if the homepage already loads a Google Analytics or Google Tag Manager tag that our account administers, the Google Analytics or Tag Manager method also works.

## Step C. Submit the sitemap in the new property

- [ ] Go to Sitemaps, then Add a new sitemap. In a Domain property, enter `https://www.worldaisummit.com/sitemap.xml`. In a www URL-prefix property, enter `sitemap.xml`.
- [ ] Submit today. When the cleaned sitemap goes live, open the sitemap entry and resubmit it. There is no need to wait for the clean-up.
- [ ] Only if the `/speakers/` pages are deployed, also submit `https://www.worldaisummit.com/sitemap-speakers.xml`. This is the file the repo generator produces.
- [ ] Check that the status reads **Success** and note the number of discovered pages.

## Step D. Old non-www property (https://worldaisummit.com/): leave it as it is

- [ ] Keep the property, its owners and its OpenSEO history.
- [ ] Skip sitemap clean-up there for now. We could not confirm that an old non-www sitemap is registered, and removing a sitemap does not de-index anything, so it does nothing for the 14 Oct window.
- [ ] **Do not 301-redirect non-www `/awards` to www `/awards/` before 14 Oct.** That URL holds #2 for "world ai awards". The www `/awards/` and non-www `/awards` duplicates are real and need one canonical, but decide that after the event: PLACEHOLDER_AWARDS_CANONICAL_DECISION.
- [ ] This works today with no new access. Once the `/awards` content fix is live, open URL Inspection in this property, inspect `https://worldaisummit.com/awards`, click **Test live URL**, then **Request indexing**. If both hosts serve the same static file (we think they do, but have not checked), the fix appears on both.

## Step E. Do not use the Change of Address tool

- [ ] Change of Address is for moving to a new domain. For www vs non-www, Google says to use redirects and canonicals, not this tool.

## Step F. Reconnect OpenSEO to the new property

- [ ] Open https://app.openseo.so/p/eb76fdff-f482-423c-9a6d-08afeccaa111/settings/integrations
- [ ] Reconnect Search Console with a Google account that is Owner or Full user on the new property.
- [ ] Choose the **Domain** property (it usually appears as `sc-domain:worldaisummit.com`). It covers both hosts, so non-www `/awards` stays visible as well.
- [ ] If only the www URL-prefix property is verified so far and OpenSEO lets you pick just one property, switching moves OpenSEO's view away from non-www `/awards`. The Search Console interface still shows both. Choose which one OpenSEO should hold until the Domain property is verified: PLACEHOLDER_OPENSEO_PROPERTY_CHOICE.
- [ ] Check it works: in OpenSEO, inspect `https://www.worldaisummit.com/delegate/`. It should return an index status, not "denied access".

## Step G. Request Indexing sprint (limited quota, so use it carefully)

Google says "there's a quota for submitting individual URLs and requesting a recrawl multiple times for the same URL won't get it crawled any faster". It also says "crawling can take anywhere from a few days to a few weeks". Google does not publish the quota size. About 10 a day per property is commonly reported, but we have not verified it.

Rules:
- [ ] Request indexing only after the fix is live on the page.
- [ ] Run **Test live URL** first and confirm the page is available to Google.
- [ ] Request each URL once.
- [ ] Do not request a page whose canonical points to the homepage until that canonical is fixed. For example, `/partner-with-us.html` currently canonicalises to `/`.

Suggested order (PLACEHOLDER_GSC_OWNER may reorder this based on which fixes ship first):
1. `https://www.worldaisummit.com/delegate/` (pass page; when Google last crawled the www URL is unknown, and non-www `/delegate/` is "URL is unknown to Google")
2. `https://worldaisummit.com/awards` (old property, after the content fix; currently #2 for "world ai awards")
3. `https://www.worldaisummit.com/awards/`
4. `https://www.worldaisummit.com/` (all event rankings come from the homepage; request after the homepage fixes)
5. `https://www.worldaisummit.com/ai-conference-bengaluru-2026.html`
6. `https://www.worldaisummit.com/speaker.html`
7. `https://www.worldaisummit.com/partner-with-us.html` (only after its canonical points to itself)
8. `https://www.worldaisummit.com/speakers/` (only if deployed)

Log for each request:

| Date | URL | Property | Live test result | Requested (Y/N) |
|---|---|---|---|---|
| | | | | |

## Step H. What to expect

- For a site newly added to Search Console, Google says performance data "can take up to a week to generate". After that the usual reporting lag is 2 to 3 days. So expect the first www numbers around a week after the property is added, not straight away.
- Until then, track progress with live rank checks rather than Search Console.

## Done when

- [ ] Domain property added, even if not yet verified (date and time: ______)
- [ ] Verified: Domain property, or www URL-prefix as the fallback
- [ ] `sitemap.xml` submitted in the new property with status Success
- [ ] OpenSEO reconnected, and inspecting a www URL works
- [ ] Old non-www property untouched, and non-www `/awards` still returns 200
- [ ] Request Indexing log started

---

Sources: Google, Verify your site ownership (support.google.com/webmasters/answer/9008080); Google Search Central, Ask Google to recrawl your URLs (developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl, updated 10 Dec 2025); Google help answer/96568 (new-site data delay) and answer/9370220 (Change of Address, www vs non-www); OpenSEO inspect_urls and Search Console performance data, 1 Oct 2026.
