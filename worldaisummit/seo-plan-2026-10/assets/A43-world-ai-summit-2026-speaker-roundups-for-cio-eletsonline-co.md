# A43: World AI Summit 2026 speaker roundups for cio.eletsonline.com and egov.eletsonline.com (all 50 speakers deep-linked, corrected CTA)

- **For recommendation:** Elets editorial: speaker roundups and AI Dialogues interviews that deep-link every speaker page and /delegate/
- **Research lens:** speakers-partners
- **Format:** HTML for the WordPress code editor: two articles, each with an SEO title, meta description and slug. Every speaker name links to the live page at /assets/speaker_details/<slug>.html.
- **Placeholders the business must fill:**
  - PLACEHOLDER_CURRENT_PASS_PRICE: On 1 Oct, /delegate/ shows Standard Access (Rs 20,000 Premium / Rs 35,000 VIP) valid till 30 Sept 2026, followed by Late Access at Rs 30,000 / Rs 60,000. The homepage still shows Premium at Rs 20,000. Sales should confirm the price that applies on 6-7 Oct, for example 'Rs 30,000 per delegate (Late Access)' or 'Rs 20,000 per delegate (Standard rate extended)'.
  - PLACEHOLDER_SUMAN_GUHA_TITLE: The event site says 'Chief Digital & Technology Officer'. His LinkedIn says 'Chief Digital Officer, Croma (Tata)'. Confirm with the speaker.
  - PLACEHOLDER_SUSHAN_RUNGTA_ROLE_AND_ORG: The event site says 'Chief Technology Officer, Absolute'. LinkedIn shows that role ended in Feb 2026 and lists him as Co-Founder, NeoLook AI since Feb 2026. Confirm his current designation, or remove the entry if he is no longer speaking for Absolute.
  - PLACEHOLDER_CIO_ARTICLE_URL: the live URL of Piece 1 on cio.eletsonline.com, used in Piece 2.

## How to ship

Owner: Elets editorial. Publish Piece 1 first, then Piece 2, on 6 or 7 October 2026. Do not publish after 7 October.

1. How to paste. Open each article in the WordPress code (HTML) editor and paste the HTML. Put the SEO title and meta description into the SEO plugin fields. Fill in every PLACEHOLDER_ before publishing. Piece 2 needs the live URL of Piece 1.

2. How the links should look.
   - Keep the links in the article body only. Do not add them to footers, sidebars or sitewide widgets.
   - Use plain followed links with no UTM tags on speaker URLs. A GA4 referral report from cio.eletsonline.com and egov.eletsonline.com can measure the traffic.
   - All 51 links point to the live pages at /assets/speaker_details/<slug>.html. Do not point them at the undeployed /speakers/<slug>/ paths. On 1 October I checked the live index and 6 sample slug pages (rajesh-choudhary, ravikumar-surpur, sushil-kumar-meher, m-balasubramaniam, kuldeep-t, aneel-savalagi). Every slug matches speakers.json, and a script checked that all 50 confirmed speakers appear exactly once in Piece 1.

3. Facts checked on 1 October 2026.
   - Dates and venue come from the live homepage. The street address is 26/1 Dr Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru, Karnataka 560055 (Google Hotels and Cvent listings). It is not used in the copy.
   - The seven track names come from the live homepage section "Seven tracks. One agenda". The cio.eletsonline.com article 'Beyond the Hype' (22 Sep) lists a different set of tracks (GenAI & LLMs, Agentic AI and others). Ask the CIO desk to align that article with the homepage so the two do not contradict each other.
   - The 10% discount for groups of 3 or more is printed on the homepage ("Group booking · 3+ delegates → 10% off") but not on /delegate/. Sales should confirm it still applies.
   - Each role is taken from the live speaker page or speakers.json. No bios were written.

4. Role checks before publishing (not placeholders).
   - Rajesh Choudhary: the CSB Bank site, his LinkedIn and his speaker page all spell it Choudhary. Fix any WAIS page that says Chaudhary.
   - Sanjeev Rastogi: his current title comes from his speaker page. He has held it since April 2026 and was CEO of Adani GCC before that, so do not call him a GCC head. LinkedIn gives the entity as Adani Enterprises.
   - Avinash Naik: his company was renamed Bajaj General Insurance in October 2025 (speakers.json). His speaker page still uses the old name.
   - Speaker count: if speakers are added before publishing, update "fifty" and add the new names under the right H2.

5. Separate fix outside this asset. All 50 speaker-page meta descriptions say "Passes from Rs 20,000" (audit c1b16b55). Update them once sales decides PLACEHOLDER_CURRENT_PASS_PRICE.

6. Parts of the original recommendation to drop.
   - Part (c): no published AI Dialogues interview with a confirmed 2026 speaker was found. Publish an interview only if one actually exists, with a link to that speaker's page.
   - Part (d): this is already covered by the "World AI Summit 2026 | Bengaluru 14-15 Oct 2026" widget on cio.eletsonline.com press-release pages.

7. No JSON-LD in these articles. Elets' CMS already outputs article markup. Event markup belongs on worldaisummit.com, and adding it to third-party articles would create duplicate Event entities.

8. Future migration only. If the /speakers/<slug>/ generator is ever deployed, 301-redirect the old URLs so these links keep working. Each rule redirects only when the new page exists, so 2025-only pages such as priyank-kharge stay live.
   Apache .htaccess (site root):
   RewriteEngine On
   RewriteRule ^assets/speaker_details/index\.html$ /speakers/ [R=301,L]
   RewriteCond %{DOCUMENT_ROOT}/speakers/$1/index.html -f
   RewriteRule ^assets/speaker_details/([a-z0-9-]+)\.html$ /speakers/$1/ [R=301,L]
   nginx (server block for www.worldaisummit.com):
   location = /assets/speaker_details/index.html { return 301 /speakers/; }
   location ~ ^/assets/speaker_details/([a-z0-9-]+)\.html$ { if (-f $document_root/speakers/$1/index.html) { return 301 /speakers/$1/; } }

9. What to expect and how to measure. Expect a modest result: referral visits in the tens to low hundreds. On 21 October, check the following:
   - GA4 referral sessions to /assets/speaker_details/ and /delegate/.
   - Google India positions for 'world ai summit speakers' (homepage #2 and /speaker.html #7 on 1 October).
   - Google India positions for 'aman mittal ias' (speaker page organic #4 on 1 October) and 'sandeep varaganti' (#6 on 1 October).
   Aman Mittal's page is already indexed and on page 1, so faster discovery from these links is not the main benefit.

## Content

==============================================================
PIECE 1: cio.eletsonline.com
==============================================================
SEO title (54 characters): World AI Summit 2026 Speakers: Bengaluru, 14-15 October
Meta description: Fifty confirmed speakers from government, banking, retail, health, GCCs and start-ups at World AI Summit 2026, Bengaluru, 14-15 October 2026.
Suggested slug: world-ai-summit-2026-speakers-bengaluru

<h1>World AI Summit 2026 speakers: who is speaking in Bengaluru on 14-15 October</h1>

<p>World AI Summit 2026, organised by Elets Technomedia, takes place on 14-15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. Fifty speakers have been confirmed so far. The programme runs across seven tracks: Frontier Models &amp; Compute; Sovereign AI &amp; Geopolitics; Enterprise AI in Production; Global Capability Centres (GCCs); Robotics, Agents &amp; Embodied AI; AI for Bharat; and Capital, Founders &amp; Exits.</p>

<h2>Government and regulators</h2>
<ul>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/pankaj-kumar-pandey.html">Pankaj Kumar Pandey, IAS</a>, Principal Secretary, Department of Personnel and Administrative Reforms (e-Governance), Government of Karnataka</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/t-bhoobalan.html">T Bhoobalan, IAS</a>, Chief Executive Officer, Centre for e-Governance, Government of Karnataka</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/sanjeev-gupta.html">Sanjeev Gupta</a>, Chief Executive Officer, Karnataka Digital Economy Mission (KDEM)</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/ravikumar-surpur.html">Dr Ravikumar Surpur, IAS</a>, Secretary, Information Technology &amp; Communication Department, Government of Rajasthan</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/aman-mittal.html">Aman Mittal, IAS</a>, Joint Chief Executive Officer, Maharashtra Institution for Transformation (MITRA)</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/hemant-garg.html">Hemant Garg</a>, Deputy Director, Ministry of Labour and Employment, Government of India</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/ram-mohan-rao.html">Ram Mohan Rao</a>, Executive Director, Securities and Exchange Board of India (SEBI)</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/mahesh-hariharan-iyer.html">Mahesh Hariharan Iyer</a>, Vice President of Engineering, Reserve Bank Innovation Hub (RBIH)</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/m-balasubramaniam.html">M. Balasubramaniam (Bala MS)</a>, Chairman, Southern Regional Committee, All India Council for Technical Education (AICTE)</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/prajeet-prabhakaran.html">Prajeet Prabhakaran</a>, Regional Director, Embassy of Austria, Commercial Section</li>
</ul>

<h2>Banking and financial services</h2>
<ul>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/tulshekar-gangireddy.html">Tulshekar Gangireddy</a>, Executive Director and Head of Data Strategy, JPMorgan Chase &amp; Co</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/deepak-mohanty.html">Deepak Mohanty</a>, Executive Director, Wells Fargo</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/deepika-sandeep.html">Deepika Sandeep</a>, Head, AI/ML CoE, HSBC</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/shireen-ali.html">Shireen Ali</a>, Head, UK Data Enablement and Standards, HSBC</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/vijaya-kadiyala.html">Vijaya Kadiyala</a>, Executive Director, DBS Bank</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/shantanu-dasgupta.html">Shantanu Dasgupta</a>, Head of Digital Initiatives, Treasury and Transaction Banking, Axis Bank</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/vishal-chugh.html">Vishal Chugh</a>, EVP and Head, Risk FRM, Tata Capital</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/shanmugam-manivannan.html">Shanmugam Manivannan</a>, Chief Digital Officer, Equitas Small Finance Bank</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/rajesh-choudhary.html">Rajesh Choudhary</a>, Chief Information Officer, CSB Bank</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/padmanaban-ta.html">Padmanaban TA</a>, DGM and Head of Digital Banking, Karnataka Bank</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/deepak-sharma.html">Deepak Sharma</a>, Independent Director, Suryoday Small Finance Bank</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/avinash-naik.html">Avinash Naik</a>, Chief Information Officer, Bajaj General Insurance (formerly Bajaj Allianz General Insurance)</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/anil-varma.html">Anil Varma</a>, Chief Technology Officer, Multi Commodity Exchange Clearing Corporation</li>
</ul>

<h2>Retail and consumer</h2>
<ul>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/sandeep-varaganti.html">Sandeep Varaganti</a>, CEO, JioMart, Reliance Retail</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/anand-thakur.html">Anand Thakur</a>, Chief Product and Technology Officer, Reliance Retail</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/suman-guha.html">Suman Guha</a>, PLACEHOLDER_SUMAN_GUHA_TITLE, Croma</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/sandeep-sharma.html">Sandeep Sharma</a>, Head of Technology and Product (eCommerce), Shoppers Stop</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/archana-menon.html">Archana Menon</a>, Head of Analytics and Watches, Titan</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/kuldeep-t.html">Kuldeep T</a>, CISO and DPO, BigBasket</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/dipayan-chakraborty.html">Dipayan Chakraborty</a>, Head, India Analytics Center, eBay</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/animesh-kishore.html">Animesh Kishore</a>, Head, Centre of Excellence, Digital and Analytics, ITC Limited</li>
</ul>

<h2>Health</h2>
<ul>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/sushil-kumar-meher.html">Dr Sushil Kumar Meher</a>, Head, IT and CISO, All India Institute of Medical Sciences (AIIMS)</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/praveen-bist.html">Praveen Bist</a>, Chief Information Officer, Amrita Hospitals</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/pranav-saxena.html">Pranav Saxena</a>, Chief Product and Technology Officer, API Holdings</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/pawan-sachdeva.html">Pawan Sachdeva</a>, Senior Managing Director and Technology Head, India, Carelon Global Solutions</li>
</ul>

<h2>Global capability centres and industry</h2>
<ul>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/george-inasu.html">George Inasu</a>, Managing Director and Country Head, Fidelity National Financial India</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/anand-ramakrishnan.html">Anand Ramakrishnan</a>, Managing Director, Equiniti India</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/aneel-savalagi.html">Aneelkumar (Aneel) Savalagi</a>, Global Chapter Leader, Innovation Capability Centre (ICC), Global Data, Digital and Technology, Takeda</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/sivakumar-selva-ganapathy.html">Sivakumar Selva Ganapathy</a>, VP, Software Engineering, and Head, Open Blue India and APAC Solutions, Johnson Controls</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/anshuma-singh.html">Anshuma (Dogra) Singh</a>, Senior Director, India IT Head and Site Leader, Applied Materials</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/joyce-rodriguez.html">Joyce Rodriguez</a>, Head of Digital Cybersecurity, Airbus India</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/harsh-vardhan.html">Harsh Vardhan</a>, Global Head, AI and Digital Innovation, Apollo Tyres</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/sanjeev-rastogi.html">Sanjeev Rastogi</a>, Head, Group Policy Services, Adani Group</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/ganesh-joshi.html">Ganesh Joshi</a>, Chief Information Officer, Nilons Enterprises</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/sushan-rungta.html">Sushan Rungta</a>, PLACEHOLDER_SUSHAN_RUNGTA_ROLE_AND_ORG</li>
</ul>

<h2>Ecosystem and capital</h2>
<ul>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/shalini-kapoor.html">Shalini Kapoor</a>, Chief Strategist, Data and AI, EkStep Foundation</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/sandhya-vasudevan.html">Sandhya Vasudevan</a>, Board Member, TiE Bangalore</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/suman-dash.html">Suman Dash</a>, Chief Operating Officer, Acsel Technology Forum</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/shashank-randev.html">Shashank Randev</a>, Founder and General Partner, 247VC</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/pavankumar-gurazada.html">Pavankumar Gurazada</a>, Associate Director, Great Learning</li>
</ul>

<p>Session titles, times and halls will appear on each speaker's page once the agenda is final. The <a href="https://www.worldaisummit.com/assets/speaker_details/index.html">full list of confirmed speakers</a> is updated as new names are announced.</p>

<p><strong>Attend:</strong> Delegate passes start at PLACEHOLDER_CURRENT_PASS_PRICE. Groups of three or more delegates receive 10% off. <a href="https://www.worldaisummit.com/delegate/">Book a delegate pass</a> or write to registration@worldaisummit.com.</p>


==============================================================
PIECE 2: egov.eletsonline.com
==============================================================
SEO title (53 characters): Government Leaders at World AI Summit 2026, Bengaluru
Meta description: Senior officials from Karnataka, Rajasthan, Maharashtra, SEBI, AICTE and AIIMS speak at World AI Summit 2026, Bengaluru, 14-15 October 2026.
Suggested slug: government-leaders-world-ai-summit-2026

<h1>Government leaders at World AI Summit 2026: who is speaking in Bengaluru on 14-15 October</h1>

<p>Nine public-sector leaders are among the fifty confirmed speakers at World AI Summit 2026. They come from the governments of Karnataka, Rajasthan and Maharashtra, the Union Ministry of Labour and Employment, SEBI, AICTE and AIIMS. The summit, organised by Elets Technomedia, takes place on 14-15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. Its seven tracks include Sovereign AI &amp; Geopolitics and AI for Bharat, which covers governance, healthcare, education, agriculture and public services.</p>

<h2>State governments</h2>
<ul>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/pankaj-kumar-pandey.html">Pankaj Kumar Pandey, IAS</a>, Principal Secretary, Department of Personnel and Administrative Reforms (e-Governance), Government of Karnataka</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/t-bhoobalan.html">T Bhoobalan, IAS</a>, Chief Executive Officer, Centre for e-Governance, Government of Karnataka</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/sanjeev-gupta.html">Sanjeev Gupta</a>, Chief Executive Officer, Karnataka Digital Economy Mission (KDEM)</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/ravikumar-surpur.html">Dr Ravikumar Surpur, IAS</a>, Secretary, Information Technology &amp; Communication Department, Government of Rajasthan</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/aman-mittal.html">Aman Mittal, IAS</a>, Joint Chief Executive Officer, Maharashtra Institution for Transformation (MITRA)</li>
</ul>

<h2>Central government, regulators and public institutions</h2>
<ul>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/hemant-garg.html">Hemant Garg</a>, Deputy Director, Ministry of Labour and Employment, Government of India</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/ram-mohan-rao.html">Ram Mohan Rao</a>, Executive Director, Securities and Exchange Board of India (SEBI)</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/m-balasubramaniam.html">M. Balasubramaniam (Bala MS)</a>, Chairman, Southern Regional Committee, All India Council for Technical Education (AICTE)</li>
<li><a href="https://www.worldaisummit.com/assets/speaker_details/sushil-kumar-meher.html">Dr Sushil Kumar Meher</a>, Head, IT and CISO, All India Institute of Medical Sciences (AIIMS)</li>
</ul>

<p>Session titles, times and halls will appear on each speaker's page once the agenda is final. The <a href="https://www.worldaisummit.com/assets/speaker_details/index.html">full list of confirmed speakers</a> also includes leaders from banking, retail, health and global capability centres. Elets CIO has published the <a href="PLACEHOLDER_CIO_ARTICLE_URL">sector-by-sector line-up</a>.</p>

<p><strong>Attend:</strong> Delegate passes start at PLACEHOLDER_CURRENT_PASS_PRICE. Groups of three or more delegates receive 10% off. <a href="https://www.worldaisummit.com/delegate/">Book a delegate pass</a> or write to registration@worldaisummit.com.</p>
