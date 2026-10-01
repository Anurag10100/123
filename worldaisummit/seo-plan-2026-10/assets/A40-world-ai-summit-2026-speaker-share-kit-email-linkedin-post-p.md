# A40: World AI Summit 2026: speaker share kit (email, LinkedIn post, public-sector variant, reminder, 50-row merge sheet)

- **For recommendation:** Speaker share kit: 50 confirmed speakers share their own (already ranking) speaker page on LinkedIn and on bio pages they control
- **Research lens:** speakers-partners
- **Format:** Mail-merge email templates (plain text, with {merge_fields}), LinkedIn post copy, and a CSV merge sheet (50 rows built from speakers.json, confirmed_2026: true)
- **Placeholders the business must fill:**
  - PLACEHOLDER_SENDER_NAME: the person who signs for the Speaker Secretariat
  - PLACEHOLDER_CURRENT_PASS_PRICE: current delegate tier and price to show on /delegate/ (the Standard tier expired on 30 Sept; the homepage and speaker pages say 'from Rs 20,000')
  - PLACEHOLDER_AGENDA_PUBLISH_DATE: when session title, time and hall go live on speaker pages
  - Correction deadline: 4 October (a Sunday) as recommended; change both templates if you move it to 5 October
  - Live slugs: confirm each against the live sitemap before merging (rajesh-choudhary may be live as rajesh-chaudhary)

## How to ship

Before you send (1-2 Oct):
1. Check that every clean_url opens. The audit confirmed 50 live pages, but only four slugs were matched to the repo by name: sandeep-varaganti, aman-mittal, shashank-randev and pankaj-kumar-pandey. Take each live slug from the live sitemap (https://www.worldaisummit.com/sitemap.xml) and correct the CSV wherever it differs. The likeliest mismatch is rajesh-choudhary, because the event site spells his name "Chaudhary".
2. Fix the Shashank Randev page first: it says 247VC was "launched in 2024" and later "founded in 2025". Send his email only after the fix. He is also a Cypher 2026 speaker (Cypher runs 7-9 Oct), so in a one-line personal note ask him to post on 10-13 Oct.
3. Clear the other check_before_send rows: Sanjeev Rastogi's role (Adani Enterprises since Apr 2026), Sushan Rungta's designation, Suman Guha's title and Dr Ravikumar Surpur's organisation. The email's "please check your designation" line also catches these, but fixing the pages first saves you a round of replies.
4. Check https://www.worldaisummit.com/delegate/ before sending speakers' colleagues there. As of 1 Oct it still shows an Early Bird valid till 25 Jul 2025 and a Standard pass valid till 30 Sept 2026, which has now expired, while the homepage and speaker pages say "from Rs 20,000". Update the page to the current tier (PLACEHOLDER_CURRENT_PASS_PRICE). The email deliberately quotes no price.

Sending:
5. Use a mail merge (for example, Gmail plus a merge add-on) from secretariat@worldaisummit.com. Map the CSV headers directly. The UTM link is built in the template from {clean_url} and {slug}. Use template A for variant A rows and template B for variant B rows. Attach each speaker's existing "We welcome X as a speaker" card. Send Wave 1 (15 priority rows) on 2 Oct and Wave 2 by 3 Oct.
6. The correction deadline, 4 October, falls on a Sunday. Keep it, or change both templates to Monday 5 October if the web team cannot update pages on Sunday.
7. On 8 Oct, send the reminder (section 3) to speakers who have not replied or posted.

After sending:
8. Keep the live /assets/speaker_details/<slug>.html URLs until after 17 Oct. Do not deploy the repo's /speakers/<slug>/ pages before the event. If you move them later, 301 each old URL to its new one.
9. The email promises that session title, time and hall will appear on each page. Add them as soon as the agenda is final (PLACEHOLDER_AGENDA_PUBLISH_DATE). Until then, the live pages say this information is pending. Do not put session titles in posts before then.
10. Track results in GA4 under Reports > Acquisition > Traffic acquisition. Filter Session campaign = world_ai_summit_2026 and Session medium = speaker_share; Session manual ad content (utm_content) shows the speaker. Log replies, posts seen and bio-link additions against each CSV row.
11. Unverified: whether the pass button on the speaker pages links to /delegate/, and whether the pages have an og:image (the repo config leaves og_image empty). This is why the email asks speakers to attach the card image to their post.
12. On the company page, the countdown posts (2-13 Oct) should link to these same speaker pages with UTMs instead of lnkd.in "Express interest" links, tagging the speakers so they reshare.

On your question about more CPUs: this run did not check or change the machine's compute resources. If you want to know how many CPUs this session has, ask directly and I'll check.

## Content

=====================================================================
MERGE FIELDS (they match the CSV headers in section 5)
{greeting} {full_name} {organisation} {slug} {clean_url}
Tracked LinkedIn link, built inside the template so no extra column is needed:
{clean_url}?utm_source=linkedin&utm_medium=speaker_share&utm_campaign=world_ai_summit_2026&utm_content={slug}
=====================================================================

---------------------------------------------------------------------
1. EMAIL, VARIANT A (corporate, founder and ecosystem speakers; variant = A)
---------------------------------------------------------------------
From: Speaker Secretariat <secretariat@worldaisummit.com>
Subject: Your World AI Summit 2026 speaker page and share kit (14-15 Oct, Bengaluru)
Preheader: Your profile is live. Please check it, plus three small requests before 14 October.
Attachment: the speaker's existing "We welcome {full_name} as a speaker" card (PNG/JPG)

Dear {greeting},

Thank you for speaking at World AI Summit 2026, which takes place on 14-15 October at the Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru.

Your speaker profile is live:
{clean_url}

Please check your designation, organisation and bio, and reply to this email with any corrections by 4 October. We will add your session title, time and hall to the same page once the agenda is final.

We also have three small requests:

1. Please share a post on LinkedIn between 5 and 13 October. There is a suggested post below, but your own words work just as well. Please keep the link, tag World AI Summit and Elets Technomedia, and attach the speaker card that comes with this email.

2. Please add a line to any bio you control. If you have a profile on your company's leadership page, a personal website or another conference site, please add this line:
   Speaker, World AI Summit 2026, Bengaluru (14-15 October 2026)
   linked to {clean_url}
   If a web team updates the page for you, they can use this HTML:
   <a href="{clean_url}">Speaker, World AI Summit 2026, Bengaluru (14-15 October 2026)</a>

3. Please invite your colleagues. They can register at https://www.worldaisummit.com/delegate/. Groups of three or more delegates get 10% off. For group bookings, please write to registration@worldaisummit.com.

Thank you for your support. We look forward to welcoming you in Bengaluru.

Warm regards,
PLACEHOLDER_SENDER_NAME
Speaker Secretariat, World AI Summit 2026
Elets Technomedia
secretariat@worldaisummit.com

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
SUGGESTED LINKEDIN POST (in your voice; please edit the two lines in brackets)

I'll be speaking at World AI Summit 2026 in Bengaluru on 14-15 October, at the Sheraton Grand Bangalore Hotel at Brigade Gateway. [One line on your topic.] If you're working on [AI in your sector], let's meet there.

{clean_url}?utm_source=linkedin&utm_medium=speaker_share&utm_campaign=world_ai_summit_2026&utm_content={slug}

@World AI Summit @Elets Technomedia
#WorldAISummit2026 #Bengaluru

Tip: to tag, type @ and choose the World AI Summit and Elets Technomedia pages from the list LinkedIn shows. Please attach the speaker card image to the post, because the link preview may not show a picture.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


---------------------------------------------------------------------
2. EMAIL, VARIANT B (government, regulator, diplomatic and public institution speakers; variant = B)
---------------------------------------------------------------------
From: Speaker Secretariat <secretariat@worldaisummit.com>
Subject: Your World AI Summit 2026 speaker page (14-15 Oct, Bengaluru)
Attachment: the speaker's existing speaker card

Dear {greeting},

Thank you for agreeing to speak at World AI Summit 2026, which takes place on 14-15 October at the Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru.

Your speaker profile is live:
{clean_url}

Please check your designation, organisation and bio, and reply to this email with any corrections by 4 October. We will add your session title, time and hall to the same page once the agenda is final.

If your office permits, a short post from you or from your department's official handle would help us reach practitioners in your field. Suggested text is below. Please adapt it to your office's practice, and keep the link if you can. If it is easier, we would be glad to send the text directly to your office's communications team.

If colleagues from your department or institution would like to attend, they can write to registration@worldaisummit.com.

With regards,
PLACEHOLDER_SENDER_NAME
Speaker Secretariat, World AI Summit 2026
Elets Technomedia
secretariat@worldaisummit.com

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
SUGGESTED TEXT FOR A DEPARTMENT OR INSTITUTION HANDLE (third person)

{full_name}, {organisation}, will speak at World AI Summit 2026 in Bengaluru on 14-15 October, at the Sheraton Grand Bangalore Hotel at Brigade Gateway.

LinkedIn: {clean_url}?utm_source=linkedin&utm_medium=speaker_share&utm_campaign=world_ai_summit_2026&utm_content={slug}
X: {clean_url}?utm_source=x&utm_medium=speaker_share&utm_campaign=world_ai_summit_2026&utm_content={slug}

@World AI Summit @Elets Technomedia
#WorldAISummit2026 #Bengaluru

SUGGESTED TEXT FOR A PERSONAL POST (only if permitted)
Use the variant A LinkedIn post above.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


---------------------------------------------------------------------
3. REMINDER (send on 8 October, only to speakers who have not replied or posted)
---------------------------------------------------------------------
Subject: World AI Summit 2026: your speaker page and suggested post

Dear {greeting},

This is a gentle reminder before the summit on 14-15 October in Bengaluru. Your profile is here:
{clean_url}

If you have a moment before 13 October, the suggested LinkedIn post is below, with your link already included. Please tag World AI Summit and Elets Technomedia, and attach your speaker card.

I'll be speaking at World AI Summit 2026 in Bengaluru on 14-15 October, at the Sheraton Grand Bangalore Hotel at Brigade Gateway. [One line on your topic.] If you're working on [AI in your sector], let's meet there.
{clean_url}?utm_source=linkedin&utm_medium=speaker_share&utm_campaign=world_ai_summit_2026&utm_content={slug}
#WorldAISummit2026 #Bengaluru

Warm regards,
Speaker Secretariat, World AI Summit 2026
secretariat@worldaisummit.com


---------------------------------------------------------------------
4. SEND ORDER
---------------------------------------------------------------------
Wave 1 (send on 2 October): the 15 rows with priority 1-BFSI, 1-Retail and 1-Ecosystem.
Wave 2 (send by 3 October): the remaining 35 rows.
HOLD: Shashank Randev, until his live page is fixed (see check_before_send).


---------------------------------------------------------------------
5. MERGE SHEET (CSV; 50 confirmed 2026 speakers from worldaisummit/speakers/speakers.json)
---------------------------------------------------------------------
priority,variant,greeting,full_name,organisation,slug,clean_url,check_before_send
1-BFSI,A,Tulshekar,Tulshekar Gangireddy,JPMorgan Chase & Co,tulshekar-gangireddy,https://www.worldaisummit.com/assets/speaker_details/tulshekar-gangireddy.html,
1-BFSI,A,Deepak,Deepak Mohanty,Wells Fargo,deepak-mohanty,https://www.worldaisummit.com/assets/speaker_details/deepak-mohanty.html,
1-BFSI,A,Vijaya,Vijaya Kadiyala,DBS Bank,vijaya-kadiyala,https://www.worldaisummit.com/assets/speaker_details/vijaya-kadiyala.html,
1-BFSI,A,Deepika,Deepika Sandeep,HSBC,deepika-sandeep,https://www.worldaisummit.com/assets/speaker_details/deepika-sandeep.html,
1-BFSI,A,Shireen,Shireen Ali,HSBC,shireen-ali,https://www.worldaisummit.com/assets/speaker_details/shireen-ali.html,
1-BFSI,A,Vishal,Vishal Chugh,Tata Capital,vishal-chugh,https://www.worldaisummit.com/assets/speaker_details/vishal-chugh.html,
1-BFSI,A,Shantanu,Shantanu Dasgupta,Axis Bank,shantanu-dasgupta,https://www.worldaisummit.com/assets/speaker_details/shantanu-dasgupta.html,
1-Ecosystem,A,Shalini,Shalini Kapoor,EkStep Foundation,shalini-kapoor,https://www.worldaisummit.com/assets/speaker_details/shalini-kapoor.html,
1-Ecosystem,A,Sandhya,Sandhya Vasudevan,TiE Bangalore,sandhya-vasudevan,https://www.worldaisummit.com/assets/speaker_details/sandhya-vasudevan.html,
1-Ecosystem,A,Shashank,Shashank Randev,247VC,shashank-randev,https://www.worldaisummit.com/assets/speaker_details/shashank-randev.html,HOLD until fixed: live page says 247VC launched in 2024 and founded in 2025. Also a Cypher 2026 speaker (7-9 Oct): ask him to post 10-13 Oct
1-Ecosystem,B,Sanjeev Gupta,Sanjeev Gupta,Karnataka Digital Economy Mission,sanjeev-gupta,https://www.worldaisummit.com/assets/speaker_details/sanjeev-gupta.html,
1-Retail,A,Sandeep,Sandeep Varaganti,Reliance Retail,sandeep-varaganti,https://www.worldaisummit.com/assets/speaker_details/sandeep-varaganti.html,
1-Retail,A,Anand,Anand Thakur,Reliance Retail,anand-thakur,https://www.worldaisummit.com/assets/speaker_details/anand-thakur.html,
1-Retail,A,Suman,Suman Guha,Tata Croma (Tata Digital),suman-guha,https://www.worldaisummit.com/assets/speaker_details/suman-guha.html,"Event title Chief Digital & Technology Officer; LinkedIn says Chief Digital Officer, Croma (Tata)"
1-Retail,A,Sandeep,Sandeep Sharma,Shoppers Stop,sandeep-sharma,https://www.worldaisummit.com/assets/speaker_details/sandeep-sharma.html,
2,A,Sanjeev,Sanjeev Rastogi,Adani Group,sanjeev-rastogi,https://www.worldaisummit.com/assets/speaker_details/sanjeev-rastogi.html,"Check live role: Head - Group Policy Services, Adani Enterprises since Apr 2026 (no longer CEO, Adani GCC)"
2,A,George,George Inasu,Fidelity National Financial India,george-inasu,https://www.worldaisummit.com/assets/speaker_details/george-inasu.html,
2,A,Anand,Anand Ramakrishnan,Equiniti India,anand-ramakrishnan,https://www.worldaisummit.com/assets/speaker_details/anand-ramakrishnan.html,
2,A,Pawan,Pawan Sachdeva,Carelon Global Solutions,pawan-sachdeva,https://www.worldaisummit.com/assets/speaker_details/pawan-sachdeva.html,
2,A,Pranav,Pranav Saxena,API Holdings,pranav-saxena,https://www.worldaisummit.com/assets/speaker_details/pranav-saxena.html,
2,A,Avinash,Avinash Naik,Bajaj Allianz General Insurance,avinash-naik,https://www.worldaisummit.com/assets/speaker_details/avinash-naik.html,
2,A,Harsh,Harsh Vardhan,Apollo Tyres Ltd,harsh-vardhan,https://www.worldaisummit.com/assets/speaker_details/harsh-vardhan.html,
2,A,Shanmugam,Shanmugam Manivannan,Equitas Small Finance Bank,shanmugam-manivannan,https://www.worldaisummit.com/assets/speaker_details/shanmugam-manivannan.html,
2,A,Rajesh,Rajesh Choudhary,CSB Bank,rajesh-choudhary,https://www.worldaisummit.com/assets/speaker_details/rajesh-choudhary.html,Event site spells Chaudhary; bank site and LinkedIn spell Choudhary. Use the live slug from the sitemap
2,A,Dipayan,Dipayan Chakraborty,eBay,dipayan-chakraborty,https://www.worldaisummit.com/assets/speaker_details/dipayan-chakraborty.html,
2,A,Archana,Archana Menon,Titan,archana-menon,https://www.worldaisummit.com/assets/speaker_details/archana-menon.html,
2,A,Anil,Anil Varma,Multi Commodity Exchange Clearing Corporation,anil-varma,https://www.worldaisummit.com/assets/speaker_details/anil-varma.html,
2,A,Deepak,Deepak Sharma,Suryoday Small Finance Bank,deepak-sharma,https://www.worldaisummit.com/assets/speaker_details/deepak-sharma.html,
2,A,Animesh,Animesh Kishore,ITC Limited,animesh-kishore,https://www.worldaisummit.com/assets/speaker_details/animesh-kishore.html,
2,A,Sushan,Sushan Rungta,Absolute,sushan-rungta,https://www.worldaisummit.com/assets/speaker_details/sushan-rungta.html,"Confirm designation: LinkedIn shows Absolute CTO role ended Feb 2026; now Co-Founder, NeoLook AI"
2,A,Ganesh,Ganesh Joshi,Nilons Enterprises,ganesh-joshi,https://www.worldaisummit.com/assets/speaker_details/ganesh-joshi.html,
2,A,Praveen,Praveen Bist,Amrita Hospitals,praveen-bist,https://www.worldaisummit.com/assets/speaker_details/praveen-bist.html,
2,A,Kuldeep,Kuldeep T,BigBasket,kuldeep-t,https://www.worldaisummit.com/assets/speaker_details/kuldeep-t.html,
2,A,Anshuma,Anshuma (Dogra) Singh,Applied Materials,anshuma-singh,https://www.worldaisummit.com/assets/speaker_details/anshuma-singh.html,
2,A,Padmanaban,Padmanaban TA,Karnataka Bank,padmanaban-ta,https://www.worldaisummit.com/assets/speaker_details/padmanaban-ta.html,
2,A,Joyce,Joyce Rodriguez,Airbus India,joyce-rodriguez,https://www.worldaisummit.com/assets/speaker_details/joyce-rodriguez.html,
2,A,Pavankumar,Pavankumar Gurazada,Great Learning,pavankumar-gurazada,https://www.worldaisummit.com/assets/speaker_details/pavankumar-gurazada.html,
2,A,Aneel,Aneelkumar (Aneel) Savalagi,Takeda,aneel-savalagi,https://www.worldaisummit.com/assets/speaker_details/aneel-savalagi.html,
2,A,Sivakumar,Sivakumar Selva Ganapathy,Johnson Controls,sivakumar-selva-ganapathy,https://www.worldaisummit.com/assets/speaker_details/sivakumar-selva-ganapathy.html,
2,A,Suman,Suman Dash,Acsel Technology Forum,suman-dash,https://www.worldaisummit.com/assets/speaker_details/suman-dash.html,
2,B,Pankaj Kumar Pandey,"Pankaj Kumar Pandey, IAS",Government of Karnataka,pankaj-kumar-pandey,https://www.worldaisummit.com/assets/speaker_details/pankaj-kumar-pandey.html,
2,B,T Bhoobalan,"T Bhoobalan, IAS",Government of Karnataka,t-bhoobalan,https://www.worldaisummit.com/assets/speaker_details/t-bhoobalan.html,
2,B,Dr Ravikumar Surpur,"Dr Ravikumar Surpur, IAS",Government of Rajasthan,ravikumar-surpur,https://www.worldaisummit.com/assets/speaker_details/ravikumar-surpur.html,Organisation (Government of Rajasthan) is inferred; confirm
2,B,Aman Mittal,"Aman Mittal, IAS",Maharashtra Institution for Transformation (MITRA),aman-mittal,https://www.worldaisummit.com/assets/speaker_details/aman-mittal.html,
2,B,Hemant Garg,Hemant Garg,"Ministry of Labour and Employment, Government of India",hemant-garg,https://www.worldaisummit.com/assets/speaker_details/hemant-garg.html,
2,B,Prajeet Prabhakaran,Prajeet Prabhakaran,"Embassy of Austria, Commercial Section",prajeet-prabhakaran,https://www.worldaisummit.com/assets/speaker_details/prajeet-prabhakaran.html,
2,B,Ram Mohan Rao,Ram Mohan Rao,Securities and Exchange Board of India (SEBI),ram-mohan-rao,https://www.worldaisummit.com/assets/speaker_details/ram-mohan-rao.html,
2,B,M Balasubramaniam,M. Balasubramaniam,All India Council for Technical Education (AICTE),m-balasubramaniam,https://www.worldaisummit.com/assets/speaker_details/m-balasubramaniam.html,
2,B,Mahesh Hariharan Iyer,Mahesh Hariharan Iyer,Reserve Bank Innovation Hub (RBIH),mahesh-hariharan-iyer,https://www.worldaisummit.com/assets/speaker_details/mahesh-hariharan-iyer.html,
2,B,Dr Sushil Kumar Meher,Dr Sushil Kumar Meher,All India Institute of Medical Sciences (AIIMS),sushil-kumar-meher,https://www.worldaisummit.com/assets/speaker_details/sushil-kumar-meher.html,
