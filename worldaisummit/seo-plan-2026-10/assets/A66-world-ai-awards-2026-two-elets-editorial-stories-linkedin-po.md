# A66: World AI Awards 2026: two Elets editorial stories, LinkedIn post, fix to the 2025 article and a /nomination 301

- **For recommendation:** Elets editorial: a 'nominations close' story now and a 'full list of winners' story on the night, both linking to /awards/ and the winners page
- **Research lens:** awards
- **Format:** Markdown: two ready-to-paste news stories for the eletsonline WordPress editor, a LinkedIn post, replacement text for the 2025 article, and Apache/nginx redirect snippets
- **Placeholders the business must fill:**
  - PLACEHOLDER_NOMINATION_DEADLINE (full date, e.g. 'DD October 2026')
  - PLACEHOLDER_DEADLINE_SHORT (for the SEO title, e.g. 'DD Oct')
  - PLACEHOLDER_2026_ELIGIBILITY (who can enter in 2026)
  - PLACEHOLDER_2026_AWARD_COUNT (2025 was 75+)
  - PLACEHOLDER_2026_CATEGORY_COUNT (2025 was 6)
  - PLACEHOLDER_2026_CATEGORY_LIST
  - PLACEHOLDER_2026_FEE_STARTUP_INDIVIDUAL (2025: Rs 18,000 + GST)
  - PLACEHOLDER_2026_FEE_ENTERPRISE (2025: Rs 20,000 + GST)
  - PLACEHOLDER_CEREMONY_DAY_AND_DATE / PLACEHOLDER_CEREMONY_DATE (14 or 15 Oct, evening)
  - PLACEHOLDER_2026_HOST_PARTNERS_CLAUSE (only partners confirmed for 2026)
  - PLACEHOLDER_WINNERS_PAGE_URL (default https://worldaisummit.com/awards/winners-2026/ once built, else https://worldaisummit.com/awards)
  - PLACEHOLDER_ONE_LINE_CONTEXT (optional: entry or jury numbers from the awards team)
  - PLACEHOLDER_CATEGORY_n / AWARD_TITLE / WINNER_ORG / PROJECT_OR_PERSON (winners table from the secretariat's final list)
  - PLACEHOLDER_DAY2_LINE (LinkedIn, only if the ceremony is on day 1)
  - PLACEHOLDER_UPDATE_DATE (date of the editor's note on the 2025 article)

## How to ship

1) Today (1 Oct): the awards team fills in the PLACEHOLDER_ values (deadline, fee for each tier, eligibility, categories, ceremony day). The web team adds those facts as visible text on /awards, checks the canonical host (step 0.1) and deploys the /nomination 301 (Apache or nginx snippet, then the curl tests). They should also point any internal links to /nomination (homepage, /awards, /1st-edition/ page) straight at /awards. 2) By 3 Oct: Elets editorial publishes Story 1 on egov.eletsonline.com and/or cio.eletsonline.com, and adds the editor's note and the two link fixes to the 2025 egov article. 3) Before 14 Oct: the web team builds /awards/winners-2026/ and confirms it returns 200. 4) Within 12 hours of the ceremony: publish Story 2 with the day-1 or day-2 closing line, then post on LinkedIn the same night. 5) Expect little traffic: in September 2026 GA4 recorded 15 egov sessions and 0 cio sessions. The main value is nominations coming in now and visible proof for sponsors afterwards, so judge it by nomination form submissions, not referral sessions.

## Content

# World AI Awards 2026: editorial pack for Elets News Network

## 0. Check these before anything goes live

1. **Link host.** Google has indexed `https://worldaisummit.com/awards` (no www, no trailing slash) and chose it as canonical. Every link below uses that host. Before publishing, open the page, choose View Source and find `rel="canonical"`. If it shows a www URL, change all links in this pack to match.
2. **The /awards page needs to answer readers.** Today it shows only the 2026 dates, venue, an entry form and secretariat@worldaisummit.com. It lists no categories, fee or deadline. The web team should add a short block with the PLACEHOLDER_ values below before Story 1 links to the page. Otherwise readers arrive at a form that doesn't answer their questions.
3. **Don't reuse 2025 numbers unless they are confirmed for 2026.** The 2025 figures were 75+ award titles in 6 categories and fees of Rs 18,000 + GST (startup and individual) and Rs 20,000 + GST (enterprise, government, leadership, solution provider). Use them only if the awards team confirms they are unchanged.
4. **Don't add UTM tags** to the worldaisummit.com links. GA4 already records eletsonline as the referrer, and a clean URL keeps the link pointing at the canonical page.
5. **No Event JSON-LD in these stories.** eletsonline's WordPress already outputs Article markup. Event markup belongs on worldaisummit.com, not on a news article.

---

## 1. STORY 1: publish by 3 Oct on egov.eletsonline.com and/or cio.eletsonline.com

**SEO title (≤60 chars):** World AI Awards 2026 Nominations Close PLACEHOLDER_DEADLINE_SHORT | Bengaluru
**Slug:** world-ai-awards-2026-nominations-close
**Meta description:** Nominations for the World AI Awards 2026 close on PLACEHOLDER_NOMINATION_DEADLINE. Winners will be honoured at World AI Summit 2026, 14-15 October, Bengaluru.
**Tags:** World AI Awards 2026, World AI Summit 2026, AI in Governance, Bengaluru
**Featured image alt:** World AI Awards 2026 at World AI Summit, Bengaluru

### H1: World AI Awards 2026: Nominations Close PLACEHOLDER_NOMINATION_DEADLINE; Winners to Be Honoured at World AI Summit, Bengaluru

Nominations for the World AI Awards 2026 close on PLACEHOLDER_NOMINATION_DEADLINE. Entries are submitted online through the [World AI Awards 2026 at World AI Summit Bengaluru](https://worldaisummit.com/awards) page. Winners will be honoured at World AI Summit 2026, to be held on 14-15 October 2026 at the Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. Elets Technomedia organises both the summit and the awards.

**Who can enter**
The awards are open to PLACEHOLDER_2026_ELIGIBILITY [2025 wording, if unchanged: "startups, enterprises, government bodies and individuals shaping the future of AI in India"]. Entries are judged on real projects. The form asks how long the project has run, what problem it solves and who benefits, how it has scaled or plans to scale, the approximate investment, and the key stakeholders and technology partners.

**Categories**
This year's programme has PLACEHOLDER_2026_AWARD_COUNT award titles across PLACEHOLDER_2026_CATEGORY_COUNT categories: PLACEHOLDER_2026_CATEGORY_LIST [the 2025 list, if unchanged: AI Enterprise & Application; Business Transformation & Innovation; Smart Tech & AI Engineering; AI in Governance; AI Startups; AI Leadership]. Each category needs a separate entry.

**How to apply**
On the awards page, choose a sector, then fill in the project, organisation and applicant details and upload supporting material. All entries go through the official form. The old 2025 address, worldaisummit.com/nomination, is no longer in use.

**Entry fee**
- Startup and individual categories: PLACEHOLDER_2026_FEE_STARTUP_INDIVIDUAL + GST per entry
- Enterprise, government, leadership and solution-provider categories: PLACEHOLDER_2026_FEE_ENTERPRISE + GST per entry

**About World AI Summit 2026**
The summit's theme is "AI for All: Accelerating India's Journey Towards Inclusive, Responsible and Future-Ready AI". It runs seven tracks: Frontier Models & Compute; Sovereign AI & Geopolitics; Enterprise AI in Production; GCCs; Robotics, Agents & Embodied AI; AI for Bharat; and Capital, Founders & Exits. The awards ceremony will be held on PLACEHOLDER_CEREMONY_DAY_AND_DATE at the Sheraton Grand Bangalore Hotel at Brigade Gateway, 26/1 Dr Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru 560055.

For questions about nominations, write to secretariat@worldaisummit.com. Delegate passes for the summit are on the [World AI Summit 2026 delegate pass page](https://worldaisummit.com/delegate/).

(About 400 words when the placeholders are filled.)

---

## 2. STORY 2: publish on the night of the ceremony or by the next morning (within 12 hours)

**Blocker:** `https://worldaisummit.com/awards/winners-2026/` does not exist yet, and Google doesn't know about it. There was no 2025 winners page either. The web team must build it and confirm it returns 200 before this story goes out. If it isn't ready, link to `https://worldaisummit.com/awards` and update the link later.

**SEO title (≤60 chars):** World AI Awards 2026 Winners: Full List | World AI Summit
**Slug:** world-ai-awards-2026-winners-full-list
**Meta description:** Full list of World AI Awards 2026 winners, announced on PLACEHOLDER_CEREMONY_DATE at World AI Summit 2026, Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru.
**Tags:** World AI Awards 2026, World AI Summit 2026, award winners, Bengaluru

### H1: World AI Awards 2026: Full List of Winners from World AI Summit, Bengaluru

The winners of the World AI Awards 2026 were announced on PLACEHOLDER_CEREMONY_DATE at World AI Summit 2026, held at the Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. Elets Technomedia organised the summit PLACEHOLDER_2026_HOST_PARTNERS_CLAUSE [for example "with PARTNER_NAME as strategic partner". Use only partners confirmed for 2026. KDEM was the 2025 partner]. The full citations are on the [World AI Awards 2026 winners page](PLACEHOLDER_WINNERS_PAGE_URL).

PLACEHOLDER_ONE_LINE_CONTEXT [optional, one factual sentence such as the number of entries or jury members, only if the awards team supplies it]

**Winners by category**

| Category | Award title | Winner (organisation) | Project / individual |
|---|---|---|---|
| PLACEHOLDER_CATEGORY_1 | PLACEHOLDER_AWARD_TITLE | PLACEHOLDER_WINNER_ORG | PLACEHOLDER_PROJECT_OR_PERSON |
| PLACEHOLDER_CATEGORY_1 | ... | ... | ... |
| PLACEHOLDER_CATEGORY_2 | ... | ... | ... |
| PLACEHOLDER_CATEGORY_3 | ... | ... | ... |
| PLACEHOLDER_CATEGORY_4 | ... | ... | ... |
| PLACEHOLDER_CATEGORY_5 | ... | ... | ... |
| PLACEHOLDER_CATEGORY_6 | ... | ... | ... |

(Group rows by category in the order the categories were announced. Copy names exactly as given in the secretariat's final list, and don't write descriptions of the winners from memory.)

**Closing line. Use one:**
- *If the ceremony is on day 1 (14 October):* World AI Summit 2026 continues on 15 October. Day-2 passes are on the [World AI Summit 2026 delegate pass page](https://worldaisummit.com/delegate/).
- *If the ceremony is on day 2 (15 October):* For details of the next edition of the World AI Awards, write to secretariat@worldaisummit.com.

---

## 3. LinkedIn post (Elets page, on the night of the ceremony)

The World AI Awards 2026 winners were announced tonight at World AI Summit 2026, Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru.

Congratulations to every winner across PLACEHOLDER_2026_CATEGORY_COUNT categories, from AI startups to government programmes.

Full list of winners: PLACEHOLDER_WINNERS_PAGE_URL

PLACEHOLDER_DAY2_LINE [if the ceremony is on 14 Oct: "The summit continues tomorrow. Day-2 passes: https://worldaisummit.com/delegate/"]

#WorldAIAwards2026 #WorldAISummit2026 #Bengaluru #AI

(Tag winning organisations' LinkedIn pages. Post the same night. In 2025 the winners post went up 15 days after the ceremony.)

---

## 4. Changes to the 2025 article
URL: https://egov.eletsonline.com/2025/07/world-ai-awards-2025-celebrating-architects-of-the-ai-era/

**a) Add an editor's note above the first paragraph:**
> Editor's note (PLACEHOLDER_UPDATE_DATE): The 2026 edition is open. Nominations for the [World AI Awards 2026 at World AI Summit Bengaluru](https://worldaisummit.com/awards) close on PLACEHOLDER_NOMINATION_DEADLINE. The ceremony is at World AI Summit 2026, 14-15 October, Bengaluru.

**b) Replace the two dead links** (worldaisummit.com/nomination returns 404):
- "For the detailed category list and nomination process, visit: worldaisummit.com/nomination" → "For the category list and nomination process, visit the [World AI Awards page](https://worldaisummit.com/awards)."
- "Want to showcase your AI innovation? Submit your nomination today: worldaisummit.com/nomination" → "Nominations for the 2026 edition are open on the [World AI Awards 2026 page](https://worldaisummit.com/awards)."

Leave the 2025 dates and the original publication date as they are.

---

## 5. Redirect /nomination to /awards (web team, worldaisummit.com)

Google last crawled `/nomination` on 7 Jul 2026 and got a 404. The 2025 article, and possibly the homepage, /awards and a /1st-edition/ page, still link to it.

**Apache (.htaccess in the web root, above any catch-all rules):**
```apache
<IfModule mod_rewrite.c>
RewriteEngine On
# 2025 nomination URL (404) -> current awards page, one hop
RewriteRule ^nomination(?:\.html|/)?$ https://worldaisummit.com/awards [R=301,L,NC]
</IfModule>
```

**nginx (inside the server block for each host that serves the site):**
```nginx
# 2025 nomination URL (404) -> current awards page, one hop
location ~* ^/nomination(?:\.html|/)?$ {
    return 301 https://worldaisummit.com/awards;
}
```

**Test after deploying:**
```
curl -sI https://worldaisummit.com/nomination      # expect: 301, Location: https://worldaisummit.com/awards
curl -sI https://www.worldaisummit.com/nomination  # expect: 301 (one hop if possible)
curl -sI https://worldaisummit.com/awards          # expect: 200, no further redirect
```
If step 0.1 showed that the canonical host is www, change the target in both snippets.

---

## Sources (checked 1 Oct 2026)
- worldaisummit.com/awards (Exa fetch): 2026 dates, venue, theme, form fields, secretariat@worldaisummit.com. No categories, fee or deadline shown.
- elets.net/worldaisummit-awards (Exa fetch, 2025 checkout): Rs 18,000 + GST for startup and individual entries, Rs 20,000 + GST for enterprise, government, leadership and solution-provider entries.
- egov.eletsonline.com 2025 article (Exa fetch): 75+ titles in 6 categories, 2025 eligibility wording, two links to /nomination.
- Venue address: 26/1 Dr Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru 560055 (Marriott and hotel listings via web search).
- GSC (verifier): canonical is https://worldaisummit.com/awards, /nomination returns 404, the winners page is unknown to Google.
