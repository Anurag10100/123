# A58: World AI Summit 2026: sitemap.xml clean-up pack (84 to 62 URLs) with robots.txt, speaker 301s and Search Console steps

- **For recommendation:** Clean sitemap.xml: drop the 6 redirecting, 5 canonicalised and 8 low-value 2025 URLs, add real lastmod, list only indexable 2026 pages
- **Research lens:** tech-indexing
- **Format:** Plain-text runbook containing the replacement sitemap.xml (validated XML, 62 URLs), a full robots.txt for when /speakers/ goes live, Apache .htaccess and nginx redirect rules, a bash check script, and steps for Search Console and Bing Webmaster Tools
- **Placeholders the business must fill:**
  - PLACEHOLDER_LASTMOD_HOME: the date the homepage content last changed (YYYY-MM-DD), or delete the element
  - PLACEHOLDER_LASTMOD_DELEGATE: the date /delegate/ last changed
  - PLACEHOLDER_LASTMOD_AWARDS: the date /awards/ last changed
  - PLACEHOLDER_LASTMOD_AI_CONFERENCE_PAGE: the date /ai-conference-bengaluru-2026.html last changed
  - PLACEHOLDER_LASTMOD_SPEAKER_HTML: the date /speaker.html last changed
  - PLACEHOLDER_LASTMOD_BLOG_INDEX: the date /blog/ last changed
  - PLACEHOLDER_LASTMOD_SPEAKER_PAGES: the date the 50 2026 speaker pages were last uploaded with real changes (used 50 times)
  - PLACEHOLDER_SPEAKERS_GO_LIVE_DATE: business decision on whether and when /speakers/ goes live, which decides whether section 3 applies
  - PLACEHOLDER_GSC_OWNER: who holds any existing www or Domain Search Console property for worldaisummit.com
  - PLACEHOLDER_DNS_ADMIN: who can add the DNS TXT record to verify a Domain property

## How to ship

Owner: web developer, about 1 hour. Deadline: 3 Oct 2026, in the same release as the redirect fixes.
1. Fill in the lastmod placeholders, or delete a lastmod element when the real date is unknown.
2. Run the check in section 5. Every line must print OK.
3. Upload sitemap.xml to the web root, replacing the current file.
4. Search Console: first get a www or Domain property verified (section 6a). Then clean out the old non-www sitemaps and submit the new one (6b, 6c), and request indexing for the four key pages (6d).
5. Do section 3 and the robots.txt change only on the day /speakers/ goes live.
6. Do not deploy partner-with-us.html in the sitemap until its canonical is fixed.

Sources:
- OpenSEO get_audit_pages, crawl c1b16b55 on 1 Oct 2026 (free). It confirmed that all 51 /assets/speaker_details URLs return 200, are indexable, have crawlDepth null and are in the sitemap. It also gave the titles of the 15 /1st-edition/ URLs (2025) and the /awards redirect: non-www to www/awards.
- Exa fetch of the live robots.txt on 1 Oct 2026.
- Local speakers.json: priyank-kharge has confirmed_2026 false and publish false. The 50 other slugs match dist/speakers/<slug>/ one to one.
- The sitemap XML was checked with a parser and contains 62 url entries.
- No paid OpenSEO tools were used and no repository files were edited.

## Content

WORLD AI SUMMIT 2026: SITEMAP CLEAN-UP PACK (data as of 1 Oct 2026, crawl c1b16b55)
Do this by 3 Oct 2026, in the same release as the redirect fixes.

What changes: 84 sitemap URLs go down to 62. Every URL that stays returns 200, is self-canonical and is about the 2026 edition. The one exception is the 2025 Chief Guest page, which is kept on purpose (see 4).
Removed (22): the 2 registration URLs that return 302; the 5 canonicalised URLs (index.html, blog/index.html, award.html, partnership.html, partner-with-us.html); and all 15 /1st-edition/ URLs, including /1st-edition/ and /1st-edition/speakers.html.
The removed pages stay live. Removing a URL from the sitemap does not de-index it; the 301s do that.

----------------------------------------------------------------
1) /sitemap.xml  (replace the whole file)
----------------------------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
<url><loc>https://www.worldaisummit.com/</loc><lastmod>PLACEHOLDER_LASTMOD_HOME</lastmod></url>
<url><loc>https://www.worldaisummit.com/delegate/</loc><lastmod>PLACEHOLDER_LASTMOD_DELEGATE</lastmod></url>
<url><loc>https://www.worldaisummit.com/awards/</loc><lastmod>PLACEHOLDER_LASTMOD_AWARDS</lastmod></url>
<url><loc>https://www.worldaisummit.com/ai-conference-bengaluru-2026.html</loc><lastmod>PLACEHOLDER_LASTMOD_AI_CONFERENCE_PAGE</lastmod></url>
<url><loc>https://www.worldaisummit.com/speaker.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_HTML</lastmod></url>
<url><loc>https://www.worldaisummit.com/blog/</loc><lastmod>PLACEHOLDER_LASTMOD_BLOG_INDEX</lastmod></url>
<url><loc>https://www.worldaisummit.com/blog/ai-in-india-from-digital-public-infrastructure-to-global-leadership.html</loc></url>
<url><loc>https://www.worldaisummit.com/blog/beyond-the-hype-the-room-where-ais-next-chapter-takes-shape.html</loc></url>
<url><loc>https://www.worldaisummit.com/blog/inside-the-boardroom-how-ceos-are-reimagining-business-with-ai.html</loc></url>
<url><loc>https://www.worldaisummit.com/blog/the-next-chapter-of-ai-what-will-define-2026-and-beyond.html</loc></url>
<url><loc>https://www.worldaisummit.com/blog/the-skills-that-will-matter-most-in-an-ai-driven-world.html</loc></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/priyank-kharge.html</loc></url>
<!-- SPEAKER PAGES START: delete this whole block once /speakers/ is live and these URLs 301 to /speakers/<slug>/ -->
<url><loc>https://www.worldaisummit.com/assets/speaker_details/aman-mittal.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/anand-ramakrishnan.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/anand-thakur.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/aneel-savalagi.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/anil-varma.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/animesh-kishore.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/anshuma-singh.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/archana-menon.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/avinash-naik.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/deepak-mohanty.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/deepak-sharma.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/deepika-sandeep.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/dipayan-chakraborty.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/ganesh-joshi.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/george-inasu.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/harsh-vardhan.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/hemant-garg.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/joyce-rodriguez.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/kuldeep-t.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/m-balasubramaniam.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/mahesh-hariharan-iyer.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/padmanaban-ta.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/pankaj-kumar-pandey.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/pavankumar-gurazada.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/pawan-sachdeva.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/prajeet-prabhakaran.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/pranav-saxena.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/praveen-bist.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/rajesh-choudhary.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/ram-mohan-rao.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/ravikumar-surpur.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/sandeep-sharma.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/sandeep-varaganti.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/sandhya-vasudevan.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/sanjeev-gupta.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/sanjeev-rastogi.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/shalini-kapoor.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/shanmugam-manivannan.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/shantanu-dasgupta.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/shashank-randev.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/shireen-ali.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/sivakumar-selva-ganapathy.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/suman-dash.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/suman-guha.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/sushan-rungta.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/sushil-kumar-meher.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/t-bhoobalan.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/tulshekar-gangireddy.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/vijaya-kadiyala.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<url><loc>https://www.worldaisummit.com/assets/speaker_details/vishal-chugh.html</loc><lastmod>PLACEHOLDER_LASTMOD_SPEAKER_PAGES</lastmod></url>
<!-- SPEAKER PAGES END -->
</urlset>

Rules for the lastmod values:
- Replace each PLACEHOLDER_LASTMOD_* with the date that page's content last changed, in YYYY-MM-DD format.
- If you do not know a page's date, delete that <lastmod> element. Do not guess, and never put today's date on every URL.
- PLACEHOLDER_LASTMOD_SPEAKER_PAGES is used 50 times. Replace them all with the date the 2026 speaker pages were last uploaded with real changes. If some pages changed on a different day, give those pages their own date.
- The 5 blog posts and the Priyank Kharge page have no lastmod on purpose. Add one only if you know the real date.
- partner-with-us.html is left out because its canonical currently points to /. Add this line only after its canonical points to itself:
  <url><loc>https://www.worldaisummit.com/partner-with-us.html</loc><lastmod>YYYY-MM-DD</lastmod></url>

----------------------------------------------------------------
2) /robots.txt  (full file)
----------------------------------------------------------------
Today's live file (Exa, 1 Oct 2026) is fine and already declares the sitemap. Change nothing until /speakers/ is live. On the day /speakers/ goes live, replace it with:

User-agent: *
Disallow: /cgi-bin/
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php
Disallow: /staging/
Allow: /
Sitemap: https://www.worldaisummit.com/sitemap.xml
Sitemap: https://www.worldaisummit.com/sitemap-speakers.xml

----------------------------------------------------------------
3) If /speakers/ is deployed (PLACEHOLDER_SPEAKERS_GO_LIVE_DATE, or "not before the event")
----------------------------------------------------------------
a. Upload dist/speakers/ and dist/sitemap-speakers.xml from worldaisummit/speakers to the site root. The sitemap has 51 URLs: /speakers/ and 50 speaker pages.
b. Add the 301s below, unless the redirect fix already includes them. All 50 live slugs at /assets/speaker_details/<slug>.html match /speakers/<slug>/ exactly. A redirect fires only when the target page exists, so priyank-kharge.html (not published under /speakers/) stays as it is.

Apache (.htaccess at the site root, after the www/https host rule):
RewriteEngine On
RewriteRule ^assets/speaker_details/(index\.html)?$ https://www.worldaisummit.com/speakers/ [R=301,L]
RewriteCond %{DOCUMENT_ROOT}/speakers/$1/index.html -f
RewriteRule ^assets/speaker_details/([a-z0-9-]+)\.html$ https://www.worldaisummit.com/speakers/$1/ [R=301,L]

nginx (inside the server block for www.worldaisummit.com):
location = /assets/speaker_details/ { return 301 https://www.worldaisummit.com/speakers/; }
location = /assets/speaker_details/index.html { return 301 https://www.worldaisummit.com/speakers/; }
location ~ ^/assets/speaker_details/(?<spk>[a-z0-9-]+)\.html$ {
    if (-f $document_root/speakers/$spk/index.html) { return 301 https://www.worldaisummit.com/speakers/$spk/; }
}

c. In /sitemap.xml, delete everything from "SPEAKER PAGES START" to "SPEAKER PAGES END", including both comment lines. Keep the priyank-kharge.html line. If /speaker.html now redirects to /speakers/, delete its line too.
d. Publish the robots.txt from section 2.
e. Caveat: build_speakers.py writes the build date as lastmod on every URL in sitemap-speakers.xml. That is accurate on the first deploy, because every page is new. On a later rebuild where only a few pages changed, correct the dates by hand before you upload.

----------------------------------------------------------------
4) Why Priyank Kharge is the one 2025 page kept
----------------------------------------------------------------
The page returns 200, is self-canonical and is factually framed: "Chief Guest | World AI Summit 2025". His name gets about 49,500 searches a month in India, no event site ranks in the top 20 for it, and the page is not linked internally, so the sitemap is how Google finds it. It does not compete for 2026 queries.
/1st-edition/speakers.html (11,360 words, title "World AI Summit 2025") is removed instead, because it could compete with /speaker.html for "world ai summit speakers".

----------------------------------------------------------------
5) Check before you upload (every line must say OK)
----------------------------------------------------------------
xmllint --noout sitemap.xml && echo "XML valid"
for u in $(grep -o '<loc>[^<]*' sitemap.xml | cut -c6-); do
  code=$(curl -s -o /tmp/wais.html -w '%{http_code}' "$u")
  can=$(grep -io '<link[^>]*canonical[^>]*>' /tmp/wais.html | grep -o 'href="[^"]*"' | head -1 | cut -d'"' -f2)
  if [ "$code" = "200" ] && [ "$can" = "$u" ]; then echo "OK   $u"; else echo "FIX  $code  canonical=$can  $u"; fi
done
(If you use sitemap-speakers.xml, run the same loop on it.)

----------------------------------------------------------------
6) Getting the new sitemap to Google and Bing
----------------------------------------------------------------
Google's sitemap ping endpoint was deprecated in June 2023 and stopped working at the end of 2023. These are the steps that work now:
a. Search Console access. The only property connected today is the URL-prefix property https://worldaisummit.com/ (non-www). Search Console accepts only a sitemap that sits inside the property, so the www sitemap cannot be submitted there. First check whether a www or Domain property already exists under another Google account (PLACEHOLDER_GSC_OWNER). If neither exists, add a Domain property for worldaisummit.com and verify it with a DNS TXT record (PLACEHOLDER_DNS_ADMIN). A Domain property covers both www and non-www.
b. Old sitemaps. Google already uses a sitemap that lists non-www URLs: URL Inspection shows non-www /awards as "Submitted and indexed". In the non-www property, open Sitemaps, note every entry, and remove any that list non-www URLs or old paths. If an old sitemap file is still on the server, delete it or 301 it to https://www.worldaisummit.com/sitemap.xml.
c. In the Domain (or www) property, submit https://www.worldaisummit.com/sitemap.xml. If /speakers/ is live, also submit https://www.worldaisummit.com/sitemap-speakers.xml.
d. Faster for the pages that matter before 14 Oct: in URL Inspection, click "Request indexing" for /delegate/, /awards/, /ai-conference-bengaluru-2026.html and /speaker.html (or /speakers/). The homepage does not need it, because Google crawled it on 1 Oct and recrawls it about daily.
e. Bing: in Bing Webmaster Tools, add or import the site and submit the same sitemap URL(s). IndexNow is optional.
f. Even without these steps, robots.txt declares the sitemap, so Google will refetch it on its own. Steps c and d just make it faster.

----------------------------------------------------------------
7) Watch until 15 Oct (5 minutes, twice a week)
----------------------------------------------------------------
- /awards is the only page with measurable Search Console traffic: non-www /awards had 32 clicks, 1,300 impressions and an average position of 7.9 between 31 Aug and 28 Sep. Google still indexes it at the non-www URL (last crawl 28 Sep), but on 1 Oct non-www /awards returned 301 to www/awards. Clicks should move to https://www.worldaisummit.com/awards/. A short dip in position while Google consolidates is normal. If the www URL is not indexed within about a week, request indexing again.
- Sitemaps report: the status should read "Success". The discovered URL count should be 62 now (12 plus 51 in the speakers sitemap once /speakers/ is live).
- Do not drop any other 2026 URL from the sitemap until it has an internal link. Most pages on this site are found only through the sitemap.
