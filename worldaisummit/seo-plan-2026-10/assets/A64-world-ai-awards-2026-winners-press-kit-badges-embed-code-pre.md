# A64: World AI Awards 2026 winners' press kit: badges, embed code, press-release and LinkedIn templates, winner and finalist emails

- **For recommendation:** Winner and finalist badge plus press kit, every asset carrying a link to the winners page
- **Research lens:** awards
- **Format:** Bundle of 6 parts: (1) the full static HTML page for /awards/press-kit/index.html, (2) a badge brief for the designer, (3) the winner email as a plain-text mail-merge, (4) the finalist email as a plain-text mail-merge (conditional), (5) the row markup for /awards/winners-2026/ so deep links work, (6) server config for Apache .htaccess and nginx. Merge fields use {{double_braces}}. Fields that winners fill in themselves use [square brackets]. Business decisions use PLACEHOLDER_ markers.
- **Placeholders the business must fill:**
  - PLACEHOLDER_CEREMONY_DAY (14 or 15; the 2025 ceremony was on day 1)
  - PLACEHOLDER_FINALIST_LIST_EXISTS (yes/no; controls the finalist badge, the FINALIST BLOCK in the press kit and the Part 4 email)
  - PLACEHOLDER_AWARDS_CONTACT_EMAIL (confirm the inbox, e.g. secretariat@worldaisummit.com)
  - PLACEHOLDER_SENDER_NAME
  - PLACEHOLDER_SENDER_TITLE
  - PLACEHOLDER_LOGO_PACK_URL_AND_RULES
  - PLACEHOLDER_BRAND_COLOURS_AND_LOGO (badge design)
  - PLACEHOLDER_BADGE_DUE_DATE (12 Oct at the latest)
  - PLACEHOLDER_PHOTO_GALLERY_URL_OR_DATE
  - PLACEHOLDER_WINNERS_LIST_SIGNOFF (owner who publishes /awards/winners-2026/ before the emails)
  - PLACEHOLDER_CURRENT_PASS_PRICE (finalist email)
  - PLACEHOLDER_GROUP_DISCOUNT_HOW_TO_CLAIM (3+ delegates, 10% off: code or process)
  - Canonical host check: www vs non-www for every absolute URL in the assets

## How to ship

Order of work. Every step depends on the one before it.

1. Fill the business placeholders by 10 Oct (marketing lead).
   - Ceremony day. The 2025 ceremony was on day 1, 25 Sep 2025.
   - Whether a finalist list exists. None was found for 2025 or 2026. If there is none, delete the FINALIST BLOCK in Part 1, skip Part 4 and skip the finalist files in Part 2.
   - The awards contact inbox. secretariat@worldaisummit.com is the nearest known address, but someone needs to confirm it.
   - The sender, the logo pack and the photo gallery.

2. Confirm the canonical host before anything goes out (web).
   - The assets use https://www.worldaisummit.com, which is how the site presents itself.
   - However, the Search Console property is the non-www URL-prefix, and /awards ranks #2 for "world ai awards" on the non-www URL. /registration also redirects through non-www.
   - Check that the non-canonical host 301s to the canonical one. If non-www is canonical, find and replace the host in all six parts.
   - I could not check this live because this sandbox's proxy returned 403 for worldaisummit.com.

3. Designer delivers the badges (Part 2) by 12 Oct. Web uploads them to /assets/images/awards/ and applies the Part 6 config, using either the Apache or the nginx version.
   - Test: paste the Part 1 embed code into a page on another domain (for example a CodePen) and confirm the badge loads, which shows no hotlink block.
   - Publish Part 1 at /awards/press-kit/index.html by 13 Oct. It is noindex, follow. It does not need to appear in the sitemap or navigation.

4. Get the winners page live before any winner email (web + awards team).
   - Build /awards/winners-2026/ in advance with one empty row per award, using the Part 5 markup. Fill it from the ceremony running order on the night.
   - Name one person to sign it off (PLACEHOLDER_WINNERS_LIST_SIGNOFF).
   - The risk: in 2025 the consolidated winners list went up on LinkedIn on 10 Oct 2025, 15 days after the 25 Sep ceremony (linkedin.com/feed/update/urn:li:activity:7382347461534793730).
   - Do not send Part 3 while the page or anchors return 404. The 16 Oct target only holds if this step is planned in advance.

5. Awards team sends Part 3 as a mail-merge by 16 Oct.
   - If a finalist list exists, send Part 4 before the event. Remove the pass paragraph for nominees who already bought the INR 30,000 Conference Attendee Pass through the elets.net checkout.

6. Measure.
   - GA4 referral sessions landing on /awards/winners-2026/ and /awards/, 14–31 Oct.
   - Re-check backlinks in late November. The baseline is about 10 real non-Elets referring domains.

Decisions taken in the copy, from the verifier notes:
- Every badge, alt text, title and template pairs "World AI Awards 2026" with "World AI Summit, Bengaluru". This guards against the name collision with worldawards.ai and the event covered by breakingai.news.
- The hashtag is #WorldAIAwards2026 instead of "#WorldAIAwards 2026".
- The kit states no award count and no entry fee. The published count (75+ vs 96 titles) and fee (Rs 30k vs Rs 18,000 + GST) conflict across pages.
- No edition number is stated (2nd vs 3rd).
- The emails ask winners to publish on their own website or newsroom. LinkedIn post links are nofollow, so they bring referral visits only. The 2025 Qualitrix release on its own site and the livemint24.com copy carried no link to worldaisummit.com.

Link-policy guardrail: Google's spam policies count "keyword-rich, hidden or low-quality links embedded in widgets that are distributed across various sites" as link spam ([Google: a reminder about widget links](https://developers.google.com/search/blog/2016/09/a-reminder-about-widget-links)). That post also advised nofollow on widget links. So:
- Keep the anchor branded (image alt only) and the badge visible.
- Never make the link a condition of the award.
- Accept that some winners or CMSs will add nofollow. Referral traffic still works.

Expected effect: a few tens of referral visits in 14–17 Oct. Any ranking benefit applies to the 2027 cycle, not this window.

On the relayed question about CPUs: this container reports 4 CPUs (nproc). I cannot add more from inside the session.

## Content

=====================================================================
PART 1. /awards/press-kit/index.html  (new page, noindex)
=====================================================================
<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Winners' Press Kit, World AI Awards 2026 | World AI Summit</title>
<meta name="description" content="Badge files, embed code, a press-release paragraph and a LinkedIn post template for winners of the World AI Awards 2026 at the World AI Summit, Bengaluru.">
<meta name="robots" content="noindex, follow">
<link rel="canonical" href="https://www.worldaisummit.com/awards/press-kit/">
<style>
:root{--ink:#14171f;--muted:#525a6b;--line:#dde1e8;--bg:#ffffff;--panel:#f5f7fa;--accent:#1d4ed8}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif}
main{max-width:820px;margin:0 auto;padding:32px 16px 64px}
h1{font-size:1.9rem;line-height:1.25;margin:0 0 12px}
h2{font-size:1.25rem;margin:40px 0 8px;padding-top:16px;border-top:1px solid var(--line)}
a{color:var(--accent)}
.muted{color:var(--muted);font-size:.95rem}
.note{background:var(--panel);border-left:3px solid var(--accent);padding:12px 16px;margin:16px 0}
.badges{display:flex;flex-wrap:wrap;gap:24px;margin:16px 0}
.badge{flex:1 1 220px;border:1px solid var(--line);border-radius:8px;padding:16px;text-align:center}
.badge img{max-width:200px;width:100%;height:auto}
textarea{width:100%;min-height:130px;font:14px/1.5 ui-monospace,Menlo,Consolas,monospace;padding:12px;border:1px solid var(--line);border-radius:6px;background:var(--panel);color:var(--ink);resize:vertical}
button{margin-top:8px;font:inherit;font-size:.9rem;padding:6px 14px;border:1px solid var(--accent);background:var(--accent);color:#fff;border-radius:6px;cursor:pointer}
ul{padding-left:20px}
dl{display:grid;grid-template-columns:max-content 1fr;gap:6px 16px}
dt{font-weight:600}
dd{margin:0}
@media (max-width:560px){dl{grid-template-columns:1fr}dd{margin-bottom:8px}}
</style>
</head>
<body>
<main>
<p class="muted"><a href="https://www.worldaisummit.com/awards/">World AI Awards</a> / Press kit</p>

<h1>World AI Awards 2026: press kit for winners</h1>
<p>The World AI Awards 2026 are presented at the World AI Summit, held on 14–15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. The summit is organised by Elets Technomedia. This page has what you need to announce your award: badge files, embed code for your website, a press-release paragraph and a LinkedIn post template.</p>
<p>The full list of winners is at <a href="https://www.worldaisummit.com/awards/winners-2026/">worldaisummit.com/awards/winners-2026/</a>.</p>

<div class="note"><strong>Please use the full name.</strong> Write “World AI Awards 2026, World AI Summit, Bengaluru” at least once in every announcement. Other, unrelated programmes use a similar name, and the full form tells readers which award you received.</div>

<h2 id="badges">1. Badge files</h2>
<div class="badges">
  <div class="badge">
    <img src="/assets/images/awards/world-ai-awards-2026-winner.png" alt="Winner, World AI Awards 2026, World AI Summit, Bengaluru" width="200" height="200">
    <p><strong>Winner</strong></p>
    <p><a href="/assets/images/awards/world-ai-awards-2026-winner.png" download>PNG, 400 × 400 px</a> · <a href="/assets/images/awards/world-ai-awards-2026-winner.svg" download>SVG</a></p>
  </div>
  <!-- FINALIST BLOCK: keep only if a finalist list exists (PLACEHOLDER_FINALIST_LIST_EXISTS). Otherwise delete from here to /FINALIST BLOCK. -->
  <div class="badge">
    <img src="/assets/images/awards/world-ai-awards-2026-finalist.png" alt="Finalist, World AI Awards 2026, World AI Summit, Bengaluru" width="200" height="200">
    <p><strong>Finalist</strong></p>
    <p><a href="/assets/images/awards/world-ai-awards-2026-finalist.png" download>PNG, 400 × 400 px</a> · <a href="/assets/images/awards/world-ai-awards-2026-finalist.svg" download>SVG</a></p>
  </div>
  <!-- /FINALIST BLOCK -->
</div>
<p class="muted">Use the Winner badge only if your organisation appears on the 2026 winners list.</p>

<h2 id="embed">2. Embed code for your website</h2>
<p>Paste this into the HTML of your awards, newsroom or About page. It shows the badge and links to the official winners list, so visitors can confirm the award.</p>
<textarea id="code-embed" readonly><a href="https://www.worldaisummit.com/awards/winners-2026/" title="World AI Awards 2026 winner, World AI Summit, Bengaluru"><img src="https://www.worldaisummit.com/assets/images/awards/world-ai-awards-2026-winner.png" alt="Winner, World AI Awards 2026, World AI Summit, Bengaluru" width="200" height="200" loading="lazy"></a></textarea>
<button type="button" data-copy="code-embed">Copy code</button>
<p class="muted">The email we sent you has a version of this code that links straight to your entry on the winners list. Please keep the link, title and alt text as they are.</p>

<h2 id="press-release">3. Press-release paragraph</h2>
<p>Replace the text in square brackets. If you publish the release on your own website, please keep the link to the winners list in the text.</p>
<textarea id="code-press" readonly>[Organisation] has won the [Award name] at the World AI Awards 2026, presented at the World AI Summit in Bengaluru on PLACEHOLDER_CEREMONY_DAY October 2026. The summit, held on 14–15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, is organised by Elets Technomedia. The full list of winners is at https://www.worldaisummit.com/awards/winners-2026/.</textarea>
<button type="button" data-copy="code-press">Copy paragraph</button>

<h2 id="linkedin">4. LinkedIn post</h2>
<p>Replace the text in square brackets. When you type @Elets Technomedia, pick the company page from the list so that it is tagged. A photograph from the ceremony works well with this post.</p>
<textarea id="code-linkedin" readonly>Proud to receive the [Award name] at the World AI Awards 2026, World AI Summit, Bengaluru. Thank you to the jury and @Elets Technomedia. Full winners list: https://www.worldaisummit.com/awards/winners-2026/ #WorldAIAwards2026 #WorldAISummit2026</textarea>
<button type="button" data-copy="code-linkedin">Copy post</button>

<h2 id="rules">5. Badge and logo usage</h2>
<ul>
  <li>Use the badge only for the award and year you received. The Winner badge is for winners; the Finalist badge is for finalists.</li>
  <li>Do not change the colours, wording or proportions. Resize proportionally, and do not show the badge narrower than 120 px.</li>
  <li>Keep “World AI Summit, Bengaluru” with the award name wherever you mention it.</li>
  <li>The badge recognises the award. Do not use it to suggest that Elets Technomedia or the World AI Summit endorses a product or service.</li>
  <li>World AI Summit logo files and rules: PLACEHOLDER_LOGO_PACK_URL_AND_RULES</li>
</ul>

<h2 id="facts">6. Facts for editors</h2>
<dl>
  <dt>Award</dt><dd>World AI Awards 2026</dd>
  <dt>Presented at</dt><dd>World AI Summit, Bengaluru</dd>
  <dt>Ceremony</dt><dd>PLACEHOLDER_CEREMONY_DAY October 2026</dd>
  <dt>Summit dates</dt><dd>14–15 October 2026</dd>
  <dt>Venue</dt><dd>Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru</dd>
  <dt>Organiser</dt><dd>Elets Technomedia</dd>
  <dt>Winners list</dt><dd><a href="https://www.worldaisummit.com/awards/winners-2026/">https://www.worldaisummit.com/awards/winners-2026/</a></dd>
  <dt>Contact</dt><dd>PLACEHOLDER_AWARDS_CONTACT_EMAIL</dd>
</dl>
</main>
<script>
document.querySelectorAll('button[data-copy]').forEach(function (b) {
  var label = b.textContent;
  b.addEventListener('click', function () {
    var t = document.getElementById(b.getAttribute('data-copy'));
    var done = function () { b.textContent = 'Copied'; setTimeout(function () { b.textContent = label; }, 2000); };
    var fallback = function () { t.select(); try { document.execCommand('copy'); } catch (e) {} done(); };
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(t.value).then(done, fallback);
    } else { fallback(); }
  });
});
</script>
</body>
</html>

=====================================================================
PART 2. BADGE BRIEF (marketing design; files due PLACEHOLDER_BADGE_DUE_DATE, 12 Oct at the latest)
=====================================================================
Upload to /assets/images/awards/ with these exact filenames:
- world-ai-awards-2026-winner.png    400 × 400 px, transparent background, under 60 KB
- world-ai-awards-2026-winner.svg    viewBox="0 0 400 400", text converted to outlines
- world-ai-awards-2026-finalist.png  same spec (only if PLACEHOLDER_FINALIST_LIST_EXISTS = yes)
- world-ai-awards-2026-finalist.svg  same spec (only if PLACEHOLDER_FINALIST_LIST_EXISTS = yes)

Exact text, in this order:
Winner:   WINNER / World AI Awards 2026 / World AI Summit, Bengaluru / 14–15 October 2026
Finalist: FINALIST / World AI Awards 2026 / World AI Summit, Bengaluru / 14–15 October 2026

Rules:
- The badge is displayed at 200 × 200 px; the 400 px file is for sharp screens. It must stay readable at 120 px wide.
- Never drop or shrink "World AI Summit, Bengaluru". worldawards.ai runs an unrelated "World AI Awards 2026", and this line is what tells them apart.
- Winner and Finalist must look different at a glance, through colour or frame and not only the word.
- Brand colours and logo: PLACEHOLDER_BRAND_COLOURS_AND_LOGO

=====================================================================
PART 3. WINNER EMAIL (awards team; send only after /awards/winners-2026/ is live; target by 16 Oct)
=====================================================================
Merge fields: {{first_name}} {{organisation}} {{award_name}} {{winner_slug}}

Subject: Your World AI Awards 2026 badge and press kit
Preheader: Badge files, embed code and a link to your entry on the winners list.

Dear {{first_name}},

Congratulations once again to {{organisation}} on winning the {{award_name}} at the World AI Awards 2026, World AI Summit, Bengaluru.

Your entry on the official winners list:
https://www.worldaisummit.com/awards/winners-2026/#{{winner_slug}}

Everything you need to announce the award is in the press kit:
https://www.worldaisummit.com/awards/press-kit/
It includes the Winner badge (PNG and SVG), a press-release paragraph, a LinkedIn post template and the badge usage rules.

To show the badge on your website, paste this code into your awards, newsroom or About page. It links to your entry, so visitors can confirm the award:

<a href="https://www.worldaisummit.com/awards/winners-2026/#{{winner_slug}}" title="World AI Awards 2026 winner, World AI Summit, Bengaluru"><img src="https://www.worldaisummit.com/assets/images/awards/world-ai-awards-2026-winner.png" alt="Winner, World AI Awards 2026, World AI Summit, Bengaluru" width="200" height="200" loading="lazy"></a>

If you are issuing a press release, please also publish it on your own website and keep the link to the winners list in the text. Here is a paragraph you can use as it is:

{{organisation}} has won the {{award_name}} at the World AI Awards 2026, presented at the World AI Summit in Bengaluru on PLACEHOLDER_CEREMONY_DAY October 2026. The summit, held on 14–15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, is organised by Elets Technomedia. The full list of winners is at https://www.worldaisummit.com/awards/winners-2026/.

Ceremony photographs: PLACEHOLDER_PHOTO_GALLERY_URL_OR_DATE

If anything in your entry needs correcting, please reply to this email and we will update it.

Warm regards,
PLACEHOLDER_SENDER_NAME
PLACEHOLDER_SENDER_TITLE, World AI Awards, Elets Technomedia
PLACEHOLDER_AWARDS_CONTACT_EMAIL

=====================================================================
PART 4. FINALIST EMAIL (optional, before the event; send ONLY if PLACEHOLDER_FINALIST_LIST_EXISTS = yes)
=====================================================================
Merge fields: {{first_name}} {{organisation}} {{award_name}}

Subject: {{organisation}} is a finalist for the World AI Awards 2026

Dear {{first_name}},

{{organisation}} is a finalist for the {{award_name}} at the World AI Awards 2026. Winners will be announced at the ceremony at the World AI Summit, Bengaluru, on PLACEHOLDER_CEREMONY_DAY October 2026, at Sheraton Grand Bangalore Hotel at Brigade Gateway.

You can use the Finalist badge from now until the ceremony. The files and usage rules are here:
https://www.worldaisummit.com/awards/press-kit/#badges

Embed code for your website:

<a href="https://www.worldaisummit.com/awards/" title="World AI Awards 2026 finalist, World AI Summit, Bengaluru"><img src="https://www.worldaisummit.com/assets/images/awards/world-ai-awards-2026-finalist.png" alt="Finalist, World AI Awards 2026, World AI Summit, Bengaluru" width="200" height="200" loading="lazy"></a>

If you win, we will send you the Winner badge and a link to your entry on the winners list.

[INTERNAL: delete this paragraph for nominees who already bought the Conference Attendee Pass with their entry on elets.net]
If your team would like to attend both days, delegate passes are at https://www.worldaisummit.com/delegate/ (PLACEHOLDER_CURRENT_PASS_PRICE). Bookings of 3 or more delegates get 10% off: PLACEHOLDER_GROUP_DISCOUNT_HOW_TO_CLAIM.

Warm regards,
PLACEHOLDER_SENDER_NAME
PLACEHOLDER_SENDER_TITLE, World AI Awards, Elets Technomedia
PLACEHOLDER_AWARDS_CONTACT_EMAIL

=====================================================================
PART 5. ROW MARKUP FOR /awards/winners-2026/ (deep links need these ids)
=====================================================================
<h1>Winners, World AI Awards 2026, World AI Summit, Bengaluru</h1>
<section id="winners-list">
  <article class="winner" id="{{winner_slug}}">
    <h3>{{award_name}}</h3>
    <p><strong>{{organisation}}</strong></p>
  </article>
  <!-- one <article> per award -->
</section>

Slug rule: {{organisation}}-{{award_name}}, lowercase ASCII, spaces to hyphens, punctuation removed. This keeps every slug unique when one organisation wins more than one award. Do not change a slug after the emails go out.

=====================================================================
PART 6. SERVER CONFIG (badges load on other sites; press kit stays noindex)
=====================================================================
--- Apache: site-root .htaccess (put the rewrite line ABOVE any existing HTTP_REFERER hotlink rules) ---
AddType image/svg+xml .svg
<IfModule mod_rewrite.c>
  RewriteEngine On
  # Exempt award badges from hotlink protection
  RewriteRule ^assets/images/awards/ - [L]
</IfModule>
<IfModule mod_headers.c>
  <FilesMatch "^world-ai-awards-2026-(winner|finalist)\.(png|svg)$">
    Header set Cache-Control "public, max-age=2592000"
    Header set Access-Control-Allow-Origin "*"
  </FilesMatch>
</IfModule>

--- Apache: /awards/press-kit/.htaccess ---
<IfModule mod_headers.c>
  Header set X-Robots-Tag "noindex, follow"
</IfModule>

--- nginx: inside the server block for the canonical host ---
# ^~ stops regex locations (for example a hotlink or expires rule on \.(png|svg)$) from overriding these blocks.
# add_header here replaces any add_header inherited from the server level, so copy any server-level security headers into both blocks.
location ^~ /assets/images/awards/ {
    # no valid_referers check, so winners' sites can display the badge
    add_header Cache-Control "public, max-age=2592000" always;
    add_header Access-Control-Allow-Origin "*" always;
    try_files $uri =404;
}
location ^~ /awards/press-kit/ {
    add_header X-Robots-Tag "noindex, follow" always;
    try_files $uri $uri/ =404;
}
