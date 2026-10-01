# A60: Recrawl sprint runbook for www.worldaisummit.com: Search Console Request Indexing plus IndexNow, 2-16 Oct 2026

- **For recommendation:** Recrawl sprint: request indexing by hand in priority order, and push the same URLs to Bing through IndexNow
- **Research lens:** tech-indexing
- **Format:** Markdown runbook with a tested bash script (indexnow.sh), a day-by-day Search Console checklist and a log template
- **Placeholders the business must fill:**
  - PLACEHOLDER_GSC_OWNER - marketing person with owner or full-user access in Search Console
  - PLACEHOLDER_DNS_OWNER - who controls DNS for worldaisummit.com (possibly Elets IT)
  - PLACEHOLDER_GSC_PROPERTY_CHOICE - Domain property (DNS TXT) or URL-prefix https://www.worldaisummit.com/ (HTML file, meta tag, GA or GTM)
  - PLACEHOLDER_FIXES_LIVE_DATE - date the redirects, sitemap, canonical and JSON-LD fixes are live (target 3-4 Oct)
  - PLACEHOLDER_SITEMAP_URL - the live sitemap URL on the www host
  - PLACEHOLDER_AWARDS_REDIRECT_DECISION - whether /awards (indexed, 200, ranks #2 for 'world ai awards') gets a 301 to www /awards/
  - PLACEHOLDER_SPEAKERS_HUB_URL - /speakers/ if the generated speaker pages are deployed, otherwise /speaker.html
  - PLACEHOLDER_TOP_5_SPEAKER_URLS - five confirmed 2026 speaker page URLs
  - PLACEHOLDER_CURRENT_PASS_PRICE - pass price currently on sale on /delegate/
  - PLACEHOLDER_AGENDA_URL - agenda page URL, if one exists
  - PLACEHOLDER_RECAP_URLS - post-event recap page URLs for 16 Oct
  - PLACEHOLDER_INDEXNOW_KEY - the key printed by ./indexnow.sh --new-key

## How to ship

1) By 2-3 Oct, marketing picks a Domain or URL-prefix www property, and web dev or the DNS owner (possibly Elets IT) adds the verification file, meta tag or DNS TXT record. Nothing else can start until this is verified. 2) Web dev runs `./indexnow.sh --new-key` on any machine with internet access, uploads `<key>.txt` to the web root, and checks it with curl. 3) The day the redirect, sitemap, canonical and JSON-LD fixes go live (target 3 Oct), marketing works through the Day 1 list in Search Console and web dev runs the first IndexNow push. Day 2 follows the next day. After that, only changed URLs are re-requested, through 13 Oct and on 16 Oct for the recap. 4) Add the www site to Bing Webmaster Tools directly, or import from Search Console only after the www property is verified, then submit the sitemap. 5) Fill in the log sheet each day. Sources: indexnow.org/documentation for the endpoint, the 8-128 character key rule, the root key file, the 10,000 URL cap and the 200/202/400/403/422/429 codes; developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl for "a few days to a few weeks", the quota and "multiple requests won't speed it up". The ~10-12/day quota comes from third-party guides; the StatCounter Bing share comes from verifier-cited search summaries. The script was syntax-checked and dry-run tested at /tmp/claude-0/-home-user-123/bf9e82cf-ebf4-58a1-ab65-7230ef80c0ff/scratchpad/indexnow.sh. It was not sent to the live API from here: direct HTTP to the site is blocked from this environment and this lens is read-only. Not re-checked: whether non-www /registration and /1st-edition/ are unknown to Google. On the user's question about more CPUs, this environment has 4 CPUs (nproc).

## Content

# Recrawl sprint runbook: www.worldaisummit.com (2-16 Oct 2026)

Owner: PLACEHOLDER_GSC_OWNER (marketing, needs owner or full-user access in Search Console) and web dev (key file and verification file)
Event: World AI Summit 2026, 14-15 October 2026, Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru

## 1. What this sprint does and does not do

- It asks Google and Bing to recrawl pages after the redirect, sitemap, canonical and JSON-LD fixes go live, so the fixed versions get indexed before the final selling week (7-13 Oct).
- It does not change rankings. Positions for queries such as "ai summit 2026" depend on content and links. The homepage, which ranks for those queries, already gets crawled about once a day without any manual request: Googlebot last crawled it on 1 Oct 2026 at 09:45 UTC, and Google's chosen canonical is https://www.worldaisummit.com/.
- Google gives no timing promise. Its own guidance says "Crawling can take anywhere from a few days to a few weeks", and "requesting a recrawl multiple times for the same URL won't get it crawled any faster" (developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl). Request each URL once per real change.
- The Request Indexing quota is roughly 10-12 URLs per property per day. Google does not publish the number (it comes from third-party guides), so the plan stays at 7 or fewer per day.
- IndexNow does not reach Google. It reaches Bing and the other participating engines. StatCounter puts Bing at about 1.2% of all search in India (Jul-Aug 2026) and about 0.2-0.3% on mobile, so expect almost no direct Bing traffic. The IndexNow step is cheap, so it is still worth doing.
- Do not use the Google Indexing API. Google limits it to JobPosting pages and BroadcastEvent embedded in a VideoObject.

## 2. Prerequisites (by 2-3 Oct)

| # | Task | Who | Done |
|---|------|-----|------|
| P1 | Create and verify a www property in Search Console. Option A, a Domain property for worldaisummit.com: needs a DNS TXT record from PLACEHOLDER_DNS_OWNER (possibly Elets IT). Option B, a URL-prefix property for https://www.worldaisummit.com/: needs the Google HTML verification file uploaded to the web root, or the meta tag added to the homepage head, or GA/GTM access. Choice: PLACEHOLDER_GSC_PROPERTY_CHOICE. Day-1 requests cannot be made without this. | marketing + web dev / DNS owner | [ ] |
| P2 | The fixes are live on production: redirects, sitemap, canonical tags, and the Event JSON-LD fix. The /awards Event JSON-LD already exists and Google shows an Events rich result ("World AI Summit 2026") with warnings for missing performer, offers and organizer, so the task is to fix it, not add it. Live date: PLACEHOLDER_FIXES_LIVE_DATE (target 3-4 Oct). | web dev | [ ] |
| P3 | Submit the sitemap PLACEHOLDER_SITEMAP_URL in the new www property. | marketing | [ ] |
| P4 | Bing Webmaster Tools: add https://www.worldaisummit.com/ directly, or use "Import from Google Search Console" only after P1 is verified. Importing today would register the non-www property, which is the non-canonical host. Submit the same sitemap in Bing. | marketing | [ ] |
| P5 | IndexNow key file: generate it (section 3) and have web dev upload it to the web root. | web dev | [ ] |

## 3. IndexNow (run from any machine with internet access)

Save the following as indexnow.sh and run `chmod +x indexnow.sh`. The script was syntax-checked and dry-run tested. Its endpoint, payload and response codes follow indexnow.org/documentation.

```bash
#!/usr/bin/env bash
# indexnow.sh - tell IndexNow engines (Bing and the other participating engines) which
# www.worldaisummit.com URLs changed. It does NOT notify Google.
#
#   One time:      ./indexnow.sh --new-key           (creates <key>.txt; web dev uploads it to the web root)
#   Each change:   KEY=<key> ./indexnow.sh URL [URL ...]
#   Dry run:       DRY_RUN=1 KEY=<key> ./indexnow.sh URL [URL ...]
set -euo pipefail
HOST="www.worldaisummit.com"
ENDPOINT="https://api.indexnow.org/indexnow"

if [ "${1:-}" = "--new-key" ]; then
  KEY=$(openssl rand -hex 16)
  printf %s "$KEY" > "$KEY.txt"
  echo "Key: $KEY"
  echo "Upload $KEY.txt to the web root so that https://$HOST/$KEY.txt returns 200 with the key as its only content."
  exit 0
fi

: "${KEY:?Set KEY to the key created with --new-key}"
[ "$#" -gt 0 ] || { echo "Pass at least one URL." >&2; exit 1; }

for u in "$@"; do
  case "$u" in
    "https://$HOST/"*) ;;
    *) echo "Refusing $u: every URL must start with https://$HOST/ (otherwise IndexNow returns 422)." >&2; exit 1 ;;
  esac
done

KEY_LOCATION="https://$HOST/$KEY.txt"
LIST=$(printf '"%s",' "$@"); LIST="[${LIST%,}]"
PAYLOAD=$(printf '{"host":"%s","key":"%s","keyLocation":"%s","urlList":%s}' "$HOST" "$KEY" "$KEY_LOCATION" "$LIST")

if [ -n "${DRY_RUN:-}" ]; then echo "$PAYLOAD"; exit 0; fi

# 1) The key file must answer 200 on the www host itself (no redirect) and hold exactly the key.
KF_CODE=$(curl -sS -o /dev/null -w '%{http_code}' --max-time 20 "$KEY_LOCATION")
KF_BODY=$(curl -sS --max-time 20 "$KEY_LOCATION" | tr -d '[:space:]')
if [ "$KF_CODE" != "200" ] || [ "$KF_BODY" != "$KEY" ]; then
  echo "Key file check failed: $KEY_LOCATION returned HTTP $KF_CODE. Fix the upload before submitting." >&2
  exit 1
fi

# 2) Submit.
OUT=$(mktemp)
CODE=$(curl -sS -o "$OUT" -w '%{http_code}' --max-time 30 -X POST "$ENDPOINT" \
  -H 'Content-Type: application/json; charset=utf-8' --data "$PAYLOAD")
case "$CODE" in
  200) echo "$(date -u +%FT%TZ) 200 OK - $# URL(s) received" ;;
  202) echo "$(date -u +%FT%TZ) 202 Accepted - $# URL(s) received, key validation pending" ;;
  400) echo "400 Bad request - invalid format"; cat "$OUT"; exit 1 ;;
  403) echo "403 Forbidden - key not found or key file does not hold the key"; exit 1 ;;
  422) echo "422 - a URL is not on $HOST or the key does not match the protocol"; exit 1 ;;
  429) echo "429 Too many requests - wait and send only changed URLs"; exit 1 ;;
  *)   echo "HTTP $CODE"; cat "$OUT"; exit 1 ;;
esac
rm -f "$OUT"
```

Steps:
1. `./indexnow.sh --new-key` prints the key (record it as PLACEHOLDER_INDEXNOW_KEY) and writes `<key>.txt`. Web dev uploads that file to the web root. The key is 32 hex characters, inside the protocol's 8-128 range. It stays in use until you change it.
2. Check it: `curl -sS https://www.worldaisummit.com/<key>.txt` must print only the key.
3. First push, the day the fixes go live:

```bash
KEY=PLACEHOLDER_INDEXNOW_KEY ./indexnow.sh \
  https://www.worldaisummit.com/ \
  https://www.worldaisummit.com/delegate/ \
  https://www.worldaisummit.com/awards/ \
  https://www.worldaisummit.com/partner-with-us.html \
  https://www.worldaisummit.com/ai-conference-bengaluru-2026.html \
  https://www.worldaisummit.com/speaker.html \
  https://www.worldaisummit.com/blog/
```

A 200 or 202 is a success. A 202 means the key is still being validated. Both codes only confirm receipt, not indexing. After the first push, send only the URLs that changed. Do not include non-www URLs: the script refuses them, because the API would return 422. If /speakers/ is deployed (PLACEHOLDER_SPEAKERS_HUB_URL), add it and its speaker pages.

Quick version without the checks (verified equivalent request):

```bash
KEY=$(openssl rand -hex 16); printf %s "$KEY" > "$KEY.txt"   # upload to https://www.worldaisummit.com/$KEY.txt
curl -sS -X POST https://api.indexnow.org/indexnow -H 'Content-Type: application/json; charset=utf-8' -d '{"host":"www.worldaisummit.com","key":"'"$KEY"'","keyLocation":"https://www.worldaisummit.com/'"$KEY"'.txt","urlList":["https://www.worldaisummit.com/","https://www.worldaisummit.com/delegate/","https://www.worldaisummit.com/awards/","https://www.worldaisummit.com/partner-with-us.html","https://www.worldaisummit.com/ai-conference-bengaluru-2026.html","https://www.worldaisummit.com/speaker.html","https://www.worldaisummit.com/blog/"]}' -w '%{http_code}\n'   # expect 200 or 202
```

## 4. Google Search Console sprint

For each URL, in order: URL Inspection, enter the URL, read the current status and "Last crawl", click Test live URL, confirm the page is available and shows the fixed version (H1, canonical, structured data), then click Request indexing. Log each one in section 6.

Day 1: PLACEHOLDER_FIXES_LIVE_DATE (target 3 Oct), in the www property (P1). Revenue pages go first. The homepage goes last because Google already crawls it daily.
1. https://www.worldaisummit.com/delegate/ (passes. The non-www variant is "URL is unknown to Google"; the www state becomes readable once P1 exists.)
2. https://www.worldaisummit.com/awards/ (only if the /awards to /awards/ 301 has shipped; decision: PLACEHOLDER_AWARDS_REDIRECT_DECISION. If it has not shipped, request whichever URL serves the fixed Event JSON-LD.)
3. https://www.worldaisummit.com/partner-with-us.html
4. https://www.worldaisummit.com/ai-conference-bengaluru-2026.html
5. PLACEHOLDER_SPEAKERS_HUB_URL (/speakers/ if deployed, otherwise /speaker.html)
6. https://www.worldaisummit.com/ (only if the homepage itself changed)

Day 1, in the old non-www property https://worldaisummit.com/ (available today):
7. https://worldaisummit.com/awards, only after the one-hop 301 to https://www.worldaisummit.com/awards/ is live. Today this URL returns 200 and is "Submitted and indexed" (last crawled 28 Sep 2026), and Google chose it as its own canonical. It ranks #2 for "world ai awards" with 32 clicks and 1,300 impressions (31 Aug-28 Sep). Requesting it after the 301 lets Google process the move now rather than during event week. If the 301 has not shipped, skip this step.

Day 2: the day after Day 1, www property.
1-5. PLACEHOLDER_TOP_5_SPEAKER_URLS (confirmed 2026 speakers only)
6. https://www.worldaisummit.com/blog/

From Day 3 to 13 Oct, only on a material change, once per change:
- /delegate/ when the pass price or pass deadline changes (current price: PLACEHOLDER_CURRENT_PASS_PRICE)
- PLACEHOLDER_AGENDA_URL when the agenda changes
- / when the homepage offer, dates or speaker line-up changes
- Run indexnow.sh with the same URLs on the same day.

13 Oct, final push: request any page changed since its last request (last-call pricing, final agenda). Run indexnow.sh with the same URLs.

16 Oct, recap: request PLACEHOLDER_RECAP_URLS plus / if it now carries the recap, and push the same URLs through indexnow.sh.

## 5. How to check it worked (not rankings)

- URL Inspection shows a "Last crawl" date on or after the request, and the indexed version shows the fix (title, H1, canonical).
- /awards: the Events rich result warnings (performer, offers, organizer) clear in URL Inspection or the Events enhancement report.
- Non-www /awards/, /delegate/, /partner-with-us.html and /ai-conference-bengaluru-2026.html are currently "URL is unknown to Google". Re-inspect their www versions in the new property after Day 1.
- Bing Webmaster Tools shows the sitemap processed and the submitted URLs listed under IndexNow / URL submission.

## 6. Log template (copy into a sheet)

| Date | URL | Property (www / non-www / Bing) | Status before | Last crawl before | Action (Request indexing / IndexNow) | Result code or message | Last crawl after | Notes |
|------|-----|-------------------------------|---------------|-------------------|-------------------------------------|------------------------|------------------|-------|

Effort: about 15 minutes a day from 3 to 13 Oct and on 16 Oct, plus about 20 minutes once for the IndexNow key set-up.
