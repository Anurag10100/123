# A00: Payment recovery kit: desk call/WhatsApp scripts, /awards/failed.php panel, success-page panels (World AI Summit 2026)

- **For recommendation:** 1. Call back unpaid delegate and award starters, and turn failed.php and success.php into recovery pages
- **Research lens:** cro-leads
- **Format:** Markdown: plain-text scripts ready to paste into WhatsApp, followed by HTML/CSS snippets for the web team and a .ics file
- **Placeholders the business must fill:**
  - PLACEHOLDER_PRICE_POLICY (Variant A: honour Standard Rs 20,000 / Rs 35,000; Variant B: Late Access Rs 30,000 / Rs 60,000)
  - PLACEHOLDER_HOLD_UNTIL (suggested Tue 6 Oct 2026)
  - PLACEHOLDER_GST_NOTE ('plus 18% GST' or 'inclusive of GST')
  - PLACEHOLDER_GROUP_DISCOUNT_ON_HELD_PRICE (does 10% stack on the held price)
  - PLACEHOLDER_INVOICE_TURNAROUND
  - PLACEHOLDER_REGISTRATION_DESK_WHATSAPP
  - PLACEHOLDER_AWARDS_DESK_WHATSAPP
  - PLACEHOLDER_AWARDS_FEE_2026 (2025 was Rs 18,000 + GST)
  - PLACEHOLDER_NOMINATION_DEADLINE
  - PLACEHOLDER_ENTRY_SAVED / PLACEHOLDER_ENTRY_SAVED_LINE (only say the entry is saved if the form stores it before payment)
  - PLACEHOLDER_RETRY_URL
  - PLACEHOLDER_CONFIRMATION_TURNAROUND
  - PLACEHOLDER_JURY_PROCESS_LINE
  - PLACEHOLDER_EBADGE_DATE
  - PLACEHOLDER_ENTRY_REQUIREMENTS
  - PLACEHOLDER_GROUP_BOOKING_URL

## How to ship

1. Today (Thu 1 Oct), marketing lead: settle every PLACEHOLDER_ in section 0. Honouring the Standard price (Variant A) is the stronger hook, because /delegate/ now lists Late Access at Rs 30,000 / Rs 60,000. Whatever price you choose has to match the fresh link exactly.

2. Build the list, in about 1-2 hours. Pull submissions since 1 Aug from the site's form store or notification inbox for /delegate/, /awards/, /thankyou.html (the partnership form) and /delegate-registration.html. Add expired and open Stripe Checkout Sessions, either via the API (GET /v1/checkout/sessions with status=expired, which gives customer_details.email where one was entered) or via the Checkout sessions view. Payments > Incomplete only lists people who tried to pay; anyone who left before entering card details won't appear there. Then clean the list:
   - remove duplicates (same email or phone; keep the latest)
   - remove staff and test entries (Elets addresses, localhost tests)
   - remove anyone accounts confirms has paid
   GA4 tracks no purchases, so it can't tell you who paid. Use the paid-orders list.

3. Sweeps. Sweep 1 runs today and Sat 3 Oct. Fri 2 Oct is Gandhi Jayanti, so corporate approvers will be out, though WhatsApp messages can still go. Sweep 2 is Tue 6 Oct. Move sweep 3 from Sat 10 Oct to Fri 9 Oct so corporate invoice/PO buyers can still pay on a working day. Run the awards sweep only if nominations are still open.
   - Call between 10:00 and 19:00 IST, from a named desk number.
   - Send WhatsApp messages one to one from the desk's WhatsApp Business number, and only to people who gave their number for this booking.
   - Honour STOP and DO NOT CONTACT straight away.
   - Tag any link to the site with utm_source=registration_desk&utm_medium=whatsapp&utm_campaign=payment_recovery_oct26.

4. Web dev, about 2 hours, by 3 Oct:
   (a) Add the shared CSS once.
   (b) Put panel 8 at the top of /awards/failed.php.
   (c) Give /awards/success.php and /delegate/success.php their own templates (panels 9 and 10), because today both pages reuse the form or price-table template.
   (d) Ideally, check the Stripe session_id on the success URL server-side before printing "booked". If it can't be verified, show "We are confirming your payment" instead.
   (e) Add <meta name="robots" content="noindex"> to all three result pages.
   (f) Upload wais-2026.ics with the MIME rule shown.
   (g) Fix the outdated "Standard Access valid till 30th Sept 2026" text on /delegate/ and success.php.
   Check all of this in a real browser, because Exa doesn't run JS.

5. Measurement: count recovered sales from the desk log plus Stripe, not GA4. If you want GA4 to show results from next time, add a purchase event on the verified success page (it can carry the transaction_id). Stripe's automatic abandoned-cart emails need code changes (consent_collection.promotions plus after_expiration.recovery when the session is created); there is no dashboard switch. Check Stripe's docs before relying on this; it is from memory, not verified here.

Venue address verified by web search on 1 Oct 2026: https://www.marriott.com/en-us/hotels/blrgs-sheraton-grand-bangalore-hotel-at-brigade-gateway/overview/ and https://www.hotelplanner.com/Hotels/178731/Reservations-Sheraton-Bangalore-Hotel-at-Brigade-Gateway-Bangalore-26-1-Dr-Rajkumar-Rd-Malleswaram-Rajajinagar-560055. No OpenSEO credits were used.

## Content

HOW TO READ THIS KIT
- <angle brackets> are mail-merge fields the desk fills in for each person: <name>, <agent>, <date>, <pass type>, <link>.
- PLACEHOLDER_ marks a business decision. Settle each one before the first sweep. Do not send any message that still has a PLACEHOLDER_ in it.
- Facts used here: the event runs Wed 14 to Thu 15 October 2026 at Sheraton Grand Bangalore Hotel at Brigade Gateway, 26/1 Dr. Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru 560055. I checked the address by web search on 1 Oct 2026 against the marriott.com hotel listing and hotelplanner.com. Current list prices on /delegate/ are Late Access: Premium Rs 30,000, VIP Rs 60,000. The Standard price (Rs 20,000 / Rs 35,000) ended on 30 Sept. Groups of 3 or more delegates get 10% off.

=====================================================================
0. DECISIONS TO MAKE BEFORE SWEEP 1 (today, Thu 1 Oct)
=====================================================================
PLACEHOLDER_PRICE_POLICY: Variant A (recommended) honours the Standard price for anyone who started before 30 Sept: Rs 20,000 Premium / Rs 35,000 VIP, held until PLACEHOLDER_HOLD_UNTIL (suggested: Tue 6 Oct). Variant B charges the current Late Access price of Rs 30,000 / Rs 60,000. If you pick B, the fresh link costs Rs 10,000 or more above what the buyer abandoned, and the message has to say so.
PLACEHOLDER_GST_NOTE: either "plus 18% GST" or "inclusive of GST". Use the same wording everywhere.
PLACEHOLDER_GROUP_DISCOUNT_ON_HELD_PRICE: yes or no. Does the 10% group discount stack on the held Standard price?
PLACEHOLDER_INVOICE_TURNAROUND: how quickly a proforma GST invoice goes out, for example "the same working day".
PLACEHOLDER_REGISTRATION_DESK_WHATSAPP / PLACEHOLDER_AWARDS_DESK_WHATSAPP: numbers in 91XXXXXXXXXX format, with no + or spaces.
PLACEHOLDER_AWARDS_FEE_2026 and PLACEHOLDER_NOMINATION_DEADLINE: we don't know either yet. The 2025 fee was Rs 18,000 + GST. If nominations have closed, skip the awards sweep and the awards copy.
PLACEHOLDER_ENTRY_SAVED: yes or no. Does the awards form store the entry before the Stripe redirect?

=====================================================================
1. DELEGATE PHONE CALL SCRIPT (registration desk)
=====================================================================
Opening
"Hello, may I speak with <name>? This is <agent> from the World AI Summit registration desk at Elets Technomedia. Do you have two minutes?"

Reason for the call
"You started booking a <Premium/VIP> pass on worldaisummit.com on <date>, but the payment did not go through. I am calling to check whether something went wrong, and to help you finish the booking if you still plan to attend. The summit is on 14 and 15 October at the Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru."

Then listen, and use the branch that fits.

a) The card or UPI payment failed, or the page timed out
"I will send you a fresh payment link on WhatsApp right after this call. [Variant A: We are holding the price you saw, Rs <20,000 / 35,000> PLACEHOLDER_GST_NOTE, until PLACEHOLDER_HOLD_UNTIL.] [Variant B: The current price is Rs <30,000 / 60,000> PLACEHOLDER_GST_NOTE.]"

b) The company needs an invoice or a PO first
"No problem. Please share your company name, GSTIN, billing address and PO number, if there is one, plus the email of the person who approves payments. We will send a GST invoice PLACEHOLDER_INVOICE_TURNAROUND, and you can pay by NEFT or UPI against it."

c) The price is the concern
Variant A: "Since you started before 30 September, we will honour the earlier price until PLACEHOLDER_HOLD_UNTIL."
Variant B: Don't offer anything that hasn't been approved. Offer the group discount if it applies.

d) Colleagues may come too
"If three or more of you register, each pass gets 10% off. Send me the names and emails and I will send one link for the group."

e) "I already paid"
"Thank you. Could you share the transaction reference or the email you paid with? I will check it with our accounts team and confirm, so you are not charged twice." Don't send a new link until the check is done. Pass it to accounts.

f) Not attending
"Understood, thank you for letting me know. I will close this booking and we won't follow up on it again." Mark the record DO NOT CONTACT.

Close
"I am sending the link and my details on WhatsApp now. If anything is unclear, reply there or write to registration@worldaisummit.com."

No answer or voicemail: send WhatsApp message 2 below. Call once per sweep and no more.

=====================================================================
2. DELEGATE WHATSAPP: FIRST MESSAGE (sweep 1, 1 to 3 Oct)
=====================================================================
Variant A (price held)

Hi <name>, this is <agent> from the World AI Summit registration desk at Elets Technomedia.

You started a <Premium/VIP> pass booking on worldaisummit.com on <date>, but the payment did not complete.

World AI Summit 2026 takes place on 14-15 October at the Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru.

We are holding the price you saw, Rs <20,000 / 35,000> PLACEHOLDER_GST_NOTE, until PLACEHOLDER_HOLD_UNTIL. Here is a fresh payment link: <link>

If your company needs a GST invoice or PO first, reply with your company name, GSTIN and billing address, and we will send the invoice PLACEHOLDER_INVOICE_TURNAROUND. You can then pay by NEFT or UPI.

Booking 3 or more seats? Each pass gets 10% off. Reply with the names and we will send one link for the group.

If you have already paid, or no longer plan to attend, please reply and we will update our records.

<agent>, World AI Summit registration desk
registration@worldaisummit.com

Variant B (current price)
Use the same message, but replace the price paragraph with:
The current price is Rs 30,000 for Premium and Rs 60,000 for VIP, PLACEHOLDER_GST_NOTE. Here is a fresh payment link: <link>

=====================================================================
3. DELEGATE WHATSAPP: REMINDERS
=====================================================================
Sweep 2 (Tue 6 Oct)

Hi <name>, a short reminder from <agent> at the World AI Summit registration desk. The summit is next week, on 14-15 October in Bengaluru, and your <Premium/VIP> booking is still open: <link>
[Variant A only: The held price of Rs <20,000 / 35,000> applies until PLACEHOLDER_HOLD_UNTIL.]
If you need a GST invoice or PO first, reply with your billing details. If you would prefer not to hear from us about this, reply STOP.

Sweep 3 (Fri 9 Oct; see how-to-ship for why not Sat 10 Oct)

Hi <name>, this is my last message about your World AI Summit 2026 booking. The summit opens on Wednesday, 14 October, at the Sheraton Grand Bangalore Hotel at Brigade Gateway. If you still plan to attend, here is your link: <link>
For invoice or group bookings, just reply here. Thank you, <agent>

=====================================================================
4. AWARDS DESK: WHATSAPP AND CALL OPENING
(only while nominations are open, until PLACEHOLDER_NOMINATION_DEADLINE)
=====================================================================
Hi <name>, this is <agent> from the World AI Awards 2026 desk at Elets Technomedia.

Your nomination payment on worldaisummit.com on <date> did not go through.
[If PLACEHOLDER_ENTRY_SAVED = yes: Your entry details are saved, so you only need to complete the payment.]
[If PLACEHOLDER_ENTRY_SAVED = no: The form was not saved, so you will need to fill it in again when you retry.]

Here is a fresh link: <link>
The fee is Rs PLACEHOLDER_AWARDS_FEE_2026 PLACEHOLDER_GST_NOTE per entry, and nominations close on PLACEHOLDER_NOMINATION_DEADLINE.

If your organisation needs a GST invoice first, reply with your company name, GSTIN and billing address. We will send it PLACEHOLDER_INVOICE_TURNAROUND, and you can pay by NEFT or UPI.

If money was debited for the failed attempt, please send the transaction reference before paying again and we will check it first.

<agent>, World AI Awards desk
secretariat@worldaisummit.com

=====================================================================
5. ENQUIRY LEADS (/thankyou.html partnership form, /delegate-registration.html)
=====================================================================
Hi <name>, this is <agent> from the World AI Summit team at Elets Technomedia. Thank you for your enquiry on worldaisummit.com on <date>.

World AI Summit 2026 takes place on 14-15 October at the Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru.

Could you tell me whether you would like to attend as a delegate, or explore partnership or exhibition? For delegate passes I can send a booking link here. For partnerships, our team at partnerships@worldaisummit.com will share the options.

<agent>, World AI Summit

=====================================================================
6. EMAIL FALLBACK (for people with an email address but no phone number, for example from expired Stripe sessions)
=====================================================================
Subject: Your World AI Summit 2026 booking did not complete

Dear <name>,

You started a <Premium/VIP> pass booking on worldaisummit.com on <date>, but the payment did not complete.

World AI Summit 2026 takes place on Wednesday 14 and Thursday 15 October 2026 at the Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru.

[Variant A: We are holding the price you saw, Rs <20,000 / 35,000> PLACEHOLDER_GST_NOTE, until PLACEHOLDER_HOLD_UNTIL.] [Variant B: The current price is Rs <30,000 / 60,000> PLACEHOLDER_GST_NOTE.]

Complete your booking: <link>

If your company needs a GST invoice or PO first, reply with your company name, GSTIN and billing address and we will send it PLACEHOLDER_INVOICE_TURNAROUND. Groups of 3 or more delegates get 10% off each pass.

If you have already paid, or no longer plan to attend, a one-line reply is enough and we will update our records.

Regards,
<agent>
World AI Summit registration desk, Elets Technomedia
registration@worldaisummit.com

=====================================================================
7. WEB: SHARED CSS (one copy, used by all three panels)
=====================================================================
<style>
.pay-panel{max-width:720px;margin:24px auto;padding:20px 24px;border:1px solid #d0d5dd;border-left:4px solid #b42318;border-radius:8px;background:#ffffff;color:#1d2433;font:16px/1.55 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
.pay-panel.ok{border-left-color:#067647}
.pay-panel h2{margin:0 0 8px;font-size:1.35rem;line-height:1.3;color:#1d2433}
.pay-panel h3{margin:16px 0 6px;font-size:1.05rem}
.pay-panel p,.pay-panel ol,.pay-panel dl{margin:0 0 12px}
.pay-panel dt{font-weight:600}
.pay-panel dd{margin:0 0 6px}
.pay-panel .small{font-size:.9rem;color:#475467}
.pay-panel .actions{display:flex;flex-wrap:wrap;gap:10px;margin-top:16px}
.pay-panel .btn{display:inline-block;padding:10px 16px;border:1px solid #1d2433;border-radius:6px;color:#1d2433;background:#ffffff;text-decoration:none;font-weight:600}
.pay-panel .btn.primary{background:#1d2433;color:#ffffff}
.pay-panel .btn:focus-visible{outline:3px solid #2e90fa;outline-offset:2px}
.pay-panel .group{margin-top:16px;padding:12px 14px;background:#f2f4f7;border-radius:6px}
@media (max-width:480px){.pay-panel{margin:16px;padding:16px}.pay-panel .btn{flex:1 1 100%;text-align:center}}
</style>

=====================================================================
8. /awards/failed.php: FAILURE PANEL (place it above the form)
=====================================================================
Pick one of the two sentences in PLACEHOLDER_ENTRY_SAVED_LINE:
- "Your entry is saved, so you only need to complete the payment." Use this only if the form really stores the entry before payment. In that case also hide the form below.
- "Your entry was not saved, so please fill in the form again when you retry." Keep the form below the panel.

<section class="pay-panel" role="alert" aria-labelledby="pay-fail-title">
  <h2 id="pay-fail-title">Your payment did not go through</h2>
  <p>We have not received the fee for your World AI Awards 2026 nomination. PLACEHOLDER_ENTRY_SAVED_LINE</p>
  <p>You can retry now, or pay by NEFT or UPI against a GST invoice. Nominations close on PLACEHOLDER_NOMINATION_DEADLINE.</p>
  <p class="small">If you see a debit for this attempt, please do not pay again yet. Send the transaction reference to secretariat@worldaisummit.com and we will check it first.</p>
  <div class="actions">
    <a class="btn primary" href="PLACEHOLDER_RETRY_URL">Retry payment</a>
    <a class="btn" href="mailto:secretariat@worldaisummit.com?subject=GST%20invoice%20for%20World%20AI%20Awards%202026%20nomination&amp;body=Company%20name%3A%0D%0AGSTIN%3A%0D%0ABilling%20address%3A%0D%0AEntry%20name%3A%0D%0APO%20number%20(if%20any)%3A">Pay by NEFT/UPI against a GST invoice</a>
    <a class="btn" href="https://wa.me/PLACEHOLDER_AWARDS_DESK_WHATSAPP?text=Payment%20failed%20for%20my%20World%20AI%20Awards%202026%20nomination">WhatsApp the awards desk</a>
    <a class="btn" href="mailto:secretariat@worldaisummit.com?subject=Payment%20failed%20for%20my%20World%20AI%20Awards%202026%20nomination">Email us</a>
  </div>
</section>

PLACEHOLDER_RETRY_URL should be a new Stripe Checkout session for the saved entry if the code can create one. If it can't, use https://www.worldaisummit.com/awards/

=====================================================================
9. /awards/success.php: CONFIRMATION PANEL (replaces the bare form; this page needs its own template)
=====================================================================
<section class="pay-panel ok" role="status" aria-labelledby="aw-ok-title">
  <h2 id="aw-ok-title">Thank you. Your nomination fee has been received.</h2>
  <p>Your World AI Awards 2026 nomination is now with the awards secretariat. A confirmation and GST invoice will go to the email address you used, PLACEHOLDER_CONFIRMATION_TURNAROUND.</p>
  <p>Next steps: PLACEHOLDER_JURY_PROCESS_LINE</p>
  <p>World AI Summit 2026 takes place on 14-15 October at the Sheraton Grand Bangalore Hotel at Brigade Gateway, Bengaluru. To attend, book a delegate pass.</p>
  <div class="actions">
    <a class="btn primary" href="https://www.worldaisummit.com/delegate/?utm_source=awards_success&amp;utm_medium=referral&amp;utm_campaign=wais2026">Book a delegate pass</a>
    <a class="btn" href="mailto:secretariat@worldaisummit.com?subject=World%20AI%20Awards%202026%20nomination">Email the secretariat</a>
  </div>
</section>

=====================================================================
10. /delegate/success.php: ORDER CONFIRMATION (replaces the price table)
=====================================================================
<section class="pay-panel ok" role="status" aria-labelledby="dl-ok-title">
  <h2 id="dl-ok-title">Thank you. Your World AI Summit 2026 pass is booked.</h2>
  <dl>
    <dt>Dates</dt><dd>Wednesday 14 and Thursday 15 October 2026</dd>
    <dt>Venue</dt><dd>Sheraton Grand Bangalore Hotel at Brigade Gateway, 26/1 Dr. Rajkumar Road, Malleswaram-Rajajinagar, Bengaluru 560055</dd>
  </dl>
  <h3>What happens next</h3>
  <ol>
    <li>Your payment receipt and GST invoice will reach the email you used at checkout, PLACEHOLDER_CONFIRMATION_TURNAROUND.</li>
    <li>Your e-badge will follow by PLACEHOLDER_EBADGE_DATE.</li>
    <li>PLACEHOLDER_ENTRY_REQUIREMENTS (for example, what to bring on the day)</li>
  </ol>
  <div class="actions">
    <a class="btn primary" href="/wais-2026.ics" download>Add to calendar</a>
    <a class="btn" href="mailto:registration@worldaisummit.com?subject=My%20World%20AI%20Summit%202026%20booking">Email the registration desk</a>
  </div>
  <div class="group">
    <strong>Bringing colleagues?</strong> Groups of 3 or more delegates get 10% off each pass.
    <a href="PLACEHOLDER_GROUP_BOOKING_URL">Book for your team</a>
  </div>
  <p class="small" style="margin-top:12px">Tell a colleague:
    <a href="https://wa.me/?text=I%20am%20attending%20World%20AI%20Summit%202026%2C%2014-15%20October%2C%20Bengaluru.%20Passes%3A%20https%3A%2F%2Fwww.worldaisummit.com%2Fdelegate%2F%3Futm_source%3Ddelegate_share%26utm_medium%3Dwhatsapp%26utm_campaign%3Dwais2026">WhatsApp</a> |
    <a href="https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fwww.worldaisummit.com%2Fdelegate%2F%3Futm_source%3Ddelegate_share%26utm_medium%3Dlinkedin%26utm_campaign%3Dwais2026">LinkedIn</a>
  </p>
</section>

If you don't yet have a group form, set PLACEHOLDER_GROUP_BOOKING_URL to mailto:registration@worldaisummit.com?subject=Group%20booking%20(3%2B%20delegates)

=====================================================================
11. /wais-2026.ics (upload to the site root, save with CRLF line endings)
=====================================================================
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Elets Technomedia//World AI Summit 2026//EN
CALSCALE:GREGORIAN
METHOD:PUBLISH
BEGIN:VEVENT
UID:wais2026-20261014@worldaisummit.com
DTSTAMP:20261001T000000Z
DTSTART;VALUE=DATE:20261014
DTEND;VALUE=DATE:20261016
SUMMARY:World AI Summit 2026
LOCATION:Sheraton Grand Bangalore Hotel at Brigade Gateway\, 26/1 Dr. Rajku
 mar Road\, Malleswaram-Rajajinagar\, Bengaluru\, Karnataka 560055\, India
DESCRIPTION:By Elets Technomedia. https://www.worldaisummit.com/
URL:https://www.worldaisummit.com/
END:VEVENT
END:VCALENDAR

These are all-day dates because the session times are not confirmed. DTEND 20261016 is exclusive, so the entry covers 14 and 15 Oct.

Serve the file as text/calendar.
Apache .htaccess:
AddType text/calendar .ics

nginx (inside the server block):
location = /wais-2026.ics { default_type text/calendar; }

=====================================================================
12. DESK LOG (one shared sheet, one row per person)
=====================================================================
Columns: Name | Phone | Email | Source (delegate form / awards form / Stripe expired session / partnership enquiry / delegate-registration) | Pass type | Date started | Duplicate or staff test (Y/N) | Already paid per accounts (Y/N) | Sweep 1 outcome (1-3 Oct) | Sweep 2 (6 Oct) | Sweep 3 (9 Oct) | Invoice requested (Y/N) | Paid date | Amount | Price variant (A/B) | DO NOT CONTACT
