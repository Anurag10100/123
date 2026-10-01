# A65: /awards/ How to nominate, How entries are judged, and FAQ (World AI Awards 2026)

- **For recommendation:** Add a how-to-nominate FAQ and a 'How entries are judged / Jury' section to /awards/ that answer the real nomination questions in text
- **Research lens:** awards
- **Format:** HTML snippet for the static /awards/ page (3 sections), plus optional FAQPage JSON-LD
- **Placeholders the business must fill:**
  - PLACEHOLDER_DEADLINE: day in October 2026 when nominations close, which must be before the 14 Oct awards night (no public 2026 deadline found)
  - PLACEHOLDER_FEE_BY_GROUP: 2026 fee for each award group, + GST (the live page shows only 'Entries from 30k + GST'). Do not print the 2025 discounted rates.
  - PLACEHOLDER_UPLOAD_RULES: number of files, accepted formats, maximum size, and whether a logo is needed, exactly as on the live 2026 form
  - PLACEHOLDER_MULTI_ENTRY_RULE: whether one applicant can enter several categories, and whether the fee is charged per entry
  - PLACEHOLDER_JUDGING_STAGES: how judging runs (for example eligibility check, jury scoring, shortlist, final), and whether and when shortlisted nominees are told
  - PLACEHOLDER_JUDGING_CRITERIA: 3-5 criteria and any weighting agreed with the jury
  - PLACEHOLDER_JURY_LIST: confirmed 2026 jury names and designations as each member supplies them, or the line 'will be announced once confirmed' (/award.html says 5+ members; the 2025 names must not be reused)
  - PLACEHOLDER_AWARDS_NIGHT_DATE: 14 or 15 October 2026
  - PLACEHOLDER_PASS_POLICY: whether a nomination includes a summit pass (the 2025 checkout sold the Conference Attendee Pass separately for Rs 30,000)

## How to ship

1) Awards team, by 2 Oct: confirm every placeholder. The deadline has to fall before the 14 Oct awards night. Check the real upload limit and file types on the live /awards/ form. The 2025 elets.net form showed both "max 10MB" and "Max 1MB (PDF, DOC)", so do not copy either figure. Confirm the per-group fee too: /award.html only says "Entries from 30k + GST", and the 2025 Rs 18,000/20,000 rates were discounted prices, so leave them out. Do not reuse the 2025 jury names from /1st-edition/awards.html as the 2026 jury.
2) Web dev, 30 min, ship with the /awards/ rebuild by 3 Oct. Put the "How to nominate" block and the fee/deadline line above the form. Paste the six award groups and their category lists as-is from /award.html (that page canonicals to /, so /awards/ needs its own copy). Then add the "How entries are judged" section and the FAQ below the form. Remove any question that still has an unfilled PLACEHOLDER_ when it goes live.
3) Add the FAQPage JSON-LD only if its text matches the visible answers exactly. It is optional because FAQ rich results are not expected for this site.
4) Link /awards/ from the homepage nav or awards section. Today it is not linked internally. The pass answer adds an internal link to /delegate/, which is also orphaned.
5) Measure nomination-form completions and emails to secretariat@ before and after the change. Expect almost no extra search traffic. The question-style GSC queries have 1-30 impressions each. Traffic to /awards comes from head terms ('ai awards' 432 impressions at #10.5, 'ai awards 2026' 243 at #9.2, 'world ai awards' 155 at #2.9), so this change matters for conversion, not ranking.
6) Create /awards/jury/ only if the 2026 jury is confirmed and at least 5 members agree to be listed.

## Content

<!-- ============================================================
  /awards/ content block: World AI Awards 2026
  Facts checked on the live site on 1 Oct 2026 (Exa fetch):
   - https://www.worldaisummit.com/award.html: "75+ individual awards", "Entries from 30k + GST",
     six award groups, "Six simple steps / How to Nominate", "5+ Distinguished Jury Members" (no names).
   - https://www.worldaisummit.com/awards/: form fields (sector, project duration, overview, problem
     solved, scale, budget/investment, stakeholders/technology partners, applicant details,
     "Upload Documents"), 14-15 October 2026, Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru.
  Before publishing, replace every PLACEHOLDER_ and delete any question whose answer is still unconfirmed.
  Do not print the 2025 elets.net rates (they were discounted prices) and do not reuse the 2025 jury names.
============================================================ -->

<section id="how-to-nominate" aria-labelledby="how-to-nominate-h">
  <h2 id="how-to-nominate-h">How to nominate for the World AI Awards 2026</h2>
  <ol>
    <li>Sign up or log in.</li>
    <li>Select your category.</li>
    <li>Fill out the nomination form(s).</li>
    <li>Upload your supporting documents.</li>
    <li>Submit your entry.</li>
    <li>Pay the nomination fee.</li>
  </ol>
  <p>Entries start from Rs 30,000 + GST. Nominations close on PLACEHOLDER_DEADLINE October 2026.</p>
</section>

<!-- Paste the six award groups and their category lists here, copied as-is from /award.html
     (AI Enterprise & Application; Business Transformation & Innovation; Smart Tech & AI Engineering;
     AI in Governance; AI Startups; AI Leadership). -->

<section id="judging" aria-labelledby="judging-h">
  <h2 id="judging-h">How entries are judged</h2>
  <p>Entries for the World AI Awards 2026 are evaluated by the awards jury. PLACEHOLDER_JUDGING_STAGES</p>
  <p>The jury assesses each entry on PLACEHOLDER_JUDGING_CRITERIA.</p>
  <h3>Jury</h3>
  <p>PLACEHOLDER_JURY_LIST</p>
  <!-- PLACEHOLDER_JURY_LIST: use names and designations exactly as each 2026 jury member supplies them.
       If the jury is not confirmed, use this sentence instead:
       "The 2026 jury will be announced on this page once confirmed." -->
</section>

<section id="faq" aria-labelledby="faq-h">
  <h2 id="faq-h">World AI Awards 2026: frequently asked questions</h2>

  <h3>Who can nominate for the World AI Awards 2026?</h3>
  <p>Enterprises, government departments and public-sector organisations, AI startups, AI solution and platform providers, and individual AI leaders can enter. There are 75+ awards across six groups: AI Enterprise &amp; Application, Business Transformation &amp; Innovation, Smart Tech &amp; AI Engineering, AI in Governance, AI Startups, and AI Leadership.</p>

  <h3>How do I nominate?</h3>
  <p>Sign up or log in, select your category, fill out the nomination form, upload your supporting documents, submit your entry and pay the nomination fee. The nomination form is on this page.</p>

  <h3>What information and documents do I need?</h3>
  <p>The form asks for your sector, the project duration (MM/YYYY to MM/YYYY), a brief overview of the project, the problem it solves and who benefits, how you have scaled it or plan to scale it, the approximate budget or investment, key stakeholders and technology partners, and applicant details. PLACEHOLDER_UPLOAD_RULES</p>
  <p>Useful supporting material includes a short project summary, a presentation, one to three photos of the implementation, a link to a video demo, and any certifications or past awards. Measurable results, such as users reached, time saved or costs reduced, make an entry easier to assess.</p>

  <h3>What is the entry fee?</h3>
  <p>Entries start from Rs 30,000 + GST per entry. PLACEHOLDER_FEE_BY_GROUP</p>

  <h3>What is the last date to nominate?</h3>
  <p>Nominations close on PLACEHOLDER_DEADLINE October 2026.</p>

  <h3>Can I enter more than one category?</h3>
  <p>PLACEHOLDER_MULTI_ENTRY_RULE</p>
  <!-- If yes: "Yes. Each category is a separate entry with its own nomination form and fee." -->

  <h3>How are entries judged?</h3>
  <p>Entries are evaluated by the World AI Awards 2026 jury on PLACEHOLDER_JUDGING_CRITERIA. See <a href="#judging">How entries are judged</a> for the process and the jury.</p>

  <h3>When and where are the winners announced?</h3>
  <p>Winners are announced on PLACEHOLDER_AWARDS_NIGHT_DATE October 2026 at World AI Summit 2026, Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. The summit runs on 14 and 15 October 2026.</p>

  <h3>Does a nomination include a summit pass?</h3>
  <p>PLACEHOLDER_PASS_POLICY Delegate passes for World AI Summit 2026 are available on the <a href="/delegate/">delegate pass page</a>.</p>
  <!-- If no: "No. The nomination fee covers the entry only." -->

  <h3>Who do I contact with questions?</h3>
  <p>For nomination queries, write to <a href="mailto:secretariat@worldaisummit.com">secretariat@worldaisummit.com</a>. For sponsorship and partnership enquiries, write to <a href="mailto:partnerships@worldaisummit.com">partnerships@worldaisummit.com</a>.</p>
</section>

<!-- OPTIONAL FAQPage JSON-LD. Parse-checked as valid JSON. The text must match the visible answers word for word
     once the placeholders are filled. Drop any Question you removed from the page.
     Google has limited FAQ rich results to well-known government and health sites since Aug 2023,
     so do not expect a SERP feature. Treat this as optional. -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "@id": "https://www.worldaisummit.com/awards/#faq",
  "url": "https://www.worldaisummit.com/awards/",
  "mainEntity": [
    {"@type": "Question", "name": "Who can nominate for the World AI Awards 2026?", "acceptedAnswer": {"@type": "Answer", "text": "Enterprises, government departments and public-sector organisations, AI startups, AI solution and platform providers, and individual AI leaders can enter. There are 75+ awards across six groups: AI Enterprise & Application, Business Transformation & Innovation, Smart Tech & AI Engineering, AI in Governance, AI Startups, and AI Leadership."}},
    {"@type": "Question", "name": "How do I nominate?", "acceptedAnswer": {"@type": "Answer", "text": "Sign up or log in, select your category, fill out the nomination form, upload your supporting documents, submit your entry and pay the nomination fee. The nomination form is on this page."}},
    {"@type": "Question", "name": "What information and documents do I need?", "acceptedAnswer": {"@type": "Answer", "text": "The form asks for your sector, the project duration (MM/YYYY to MM/YYYY), a brief overview of the project, the problem it solves and who benefits, how you have scaled it or plan to scale it, the approximate budget or investment, key stakeholders and technology partners, and applicant details. PLACEHOLDER_UPLOAD_RULES Useful supporting material includes a short project summary, a presentation, one to three photos of the implementation, a link to a video demo, and any certifications or past awards. Measurable results, such as users reached, time saved or costs reduced, make an entry easier to assess."}},
    {"@type": "Question", "name": "What is the entry fee?", "acceptedAnswer": {"@type": "Answer", "text": "Entries start from Rs 30,000 + GST per entry. PLACEHOLDER_FEE_BY_GROUP"}},
    {"@type": "Question", "name": "What is the last date to nominate?", "acceptedAnswer": {"@type": "Answer", "text": "Nominations close on PLACEHOLDER_DEADLINE October 2026."}},
    {"@type": "Question", "name": "Can I enter more than one category?", "acceptedAnswer": {"@type": "Answer", "text": "PLACEHOLDER_MULTI_ENTRY_RULE"}},
    {"@type": "Question", "name": "How are entries judged?", "acceptedAnswer": {"@type": "Answer", "text": "Entries are evaluated by the World AI Awards 2026 jury on PLACEHOLDER_JUDGING_CRITERIA. See How entries are judged for the process and the jury."}},
    {"@type": "Question", "name": "When and where are the winners announced?", "acceptedAnswer": {"@type": "Answer", "text": "Winners are announced on PLACEHOLDER_AWARDS_NIGHT_DATE October 2026 at World AI Summit 2026, Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. The summit runs on 14 and 15 October 2026."}},
    {"@type": "Question", "name": "Does a nomination include a summit pass?", "acceptedAnswer": {"@type": "Answer", "text": "PLACEHOLDER_PASS_POLICY Delegate passes for World AI Summit 2026 are available on the delegate pass page at https://www.worldaisummit.com/delegate/."}},
    {"@type": "Question", "name": "Who do I contact with questions?", "acceptedAnswer": {"@type": "Answer", "text": "For nomination queries, write to secretariat@worldaisummit.com. For sponsorship and partnership enquiries, write to partnerships@worldaisummit.com."}}
  ]
}
</script>
