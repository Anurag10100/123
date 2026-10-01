"""One-row-per-contact outreach tab.

Combines, for every sponsor company:
  - the public contact found by web research (enrichment.json), and
  - every contact HubSpot already holds for that company (crm_contacts.json,
    exported 1 Oct 2026),
so the contact details sit in the first columns of the sheet.
"""
import json
import re
from pathlib import Path

from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.datavalidation import DataValidation

from outreach import OWNERS, STATUSES

HERE = Path(__file__).parent
CRM_CONTACTS = HERE / "crm_contacts.json"
LUSHA_CONTACTS = HERE / "lusha_contacts.json"
CONTACT_URL = "https://app.hubspot.com/contacts/147308736/record/0-1/{}"
# Titles most likely to own event sponsorship budgets sort to the top of each company.
KEY_ROLE = re.compile(r"market|brand|event|communicat|cmo|alliance|partnership|sponsor|pr\b|demand|growth",
                      re.I)


def _norm(s):
    return re.sub(r"[^a-z]", "", (s or "").lower())


def build_contacts(wb, outreach_rows, outreach_headers, write_table):
    col = {h: i for i, h in enumerate(outreach_headers)}
    get = lambda r, h: r[col[h]]
    crm = json.loads(CRM_CONTACTS.read_text()) if CRM_CONTACTS.exists() else []
    by_co = {}
    for c in crm:
        by_co.setdefault(c["company_label"], []).append(c)
    lusha = json.loads(LUSHA_CONTACTS.read_text()) if LUSHA_CONTACTS.exists() else []
    lusha_by_co = {}
    for c in lusha:
        if c.get("name"):
            lusha_by_co.setdefault(c["company"], []).append(c)

    rows = []
    for r in outreach_rows:
        prio, co = get(r, "Priority"), get(r, "Company")
        if prio == "Partner only":
            continue
        company = [get(r, h) for h in ("Next action", "Category", "# GCC events sponsored", "Best tier seen",
                                       "Sponsorship history (event - tier)", "Website", "Pitch angle")]
        people = []
        seen = set()
        for c in by_co.get(co, []):
            name = " ".join(x for x in (c["firstname"], c["lastname"]) if x).strip()
            seen.add(_norm(name))
            people.append([name, c["jobtitle"], c["email"], c["phone"], c["mobilephone"], c["linkedin"],
                           "HubSpot", OWNERS.get(c["owner_id"], c["owner_id"]),
                           (c["last_contacted"] or "")[:10], CONTACT_URL.format(c["contact_id"])])
        index = {_norm(p[0]): p for p in people}
        for c in lusha_by_co.get(co, []):
            phone = c.get("phone", "")
            mobile = phone if "mobile" in (c.get("phone_type") or "").lower() else ""
            direct = "" if mobile else phone
            hit = index.get(_norm(c["name"]))
            if hit:  # already listed: fill gaps only
                hit[2] = hit[2] or c.get("email", "")
                hit[3] = hit[3] or direct
                hit[4] = hit[4] or mobile
                hit[5] = hit[5] or c.get("linkedin", "")
                hit[6] = "HubSpot + Lusha"
                continue
            p = [c["name"], c.get("title", ""), c.get("email", ""), direct, mobile, c.get("linkedin", ""),
                 "Lusha", "", "", "", c.get("note", "")]
            people.append(p)
            index[_norm(c["name"])] = p
            seen.add(_norm(c["name"]))
        pub = get(r, "Contact name (public source)")
        if pub and _norm(pub) not in seen:
            src = (get(r, "Contact source URL(s)") or "").split(" | ")[0]
            people.append([pub, get(r, "Designation"), get(r, "Published email (company/general)"),
                           get(r, "Published phone"), "", get(r, "LinkedIn URL"),
                           f"Public research ({get(r, 'Contact confidence')} confidence) - not in HubSpot",
                           "", "", src])
        elif not pub and (get(r, "Published email (company/general)") or get(r, "Published phone")):
            people.append(["(company general line)", "", get(r, "Published email (company/general)"),
                           get(r, "Published phone"), "", "", "Company website", "", "", ""])
        if not people:
            people.append(["- no contact found yet -", "", "", "", "", "", "", "", "", ""])
        people.sort(key=lambda p: (not (p[6].startswith(("HubSpot", "Lusha", "Public"))),
                                   not KEY_ROLE.search(p[1] or ""), not p[2], p[0].lower()))
        for p in people:
            rows.append([prio, co] + p[:6] + [bool(KEY_ROLE.search(p[1] or "")) and "Yes" or ""] + p[6:10] +
                        company + ["Not contacted", "", p[10] if len(p) > 10 else ""])

    ws = wb.create_sheet("Contacts", 0)
    headers = ["Priority", "Company", "Contact name", "Designation", "Email", "Phone", "Mobile", "LinkedIn",
               "Marketing / events role?", "Contact source", "HubSpot contact owner", "Last contacted (HubSpot)",
               "HubSpot / source link", "Company next action", "Category", "# GCC events sponsored",
               "Best tier seen", "Sponsorship history (event - tier)", "Website", "Pitch angle",
               "Status", "Elets owner", "Notes"]
    widths = [12, 28, 26, 34, 34, 18, 16, 30, 10, 26, 20, 14, 34, 36, 24, 10, 22, 60, 24, 50, 16, 14, 30]
    write_table(ws, "Contacts", headers, rows, widths, link_cols=(8, 13, 19))

    fills = {"A - Hot": "F8CBAD", "B - Warm": "FFE699", "C - Nurture": "DDEBF7"}
    for i in range(2, ws.max_row + 1):
        p = ws.cell(i, 1)
        p.fill = PatternFill("solid", start_color=fills[p.value])
        p.font = Font(name="Arial", size=10, bold=True)
        ws.cell(i, 3).font = Font(name="Arial", size=10, bold=True)
        if ws.cell(i, 9).value == "Yes":
            ws.cell(i, 9).fill = PatternFill("solid", start_color="E2EFDA")
        for c in range(21, 24):
            ws.cell(i, c).fill = PatternFill("solid", start_color="FFFFF2")
    dv = DataValidation(type="list", formula1='"' + ",".join(STATUSES) + '"', allow_blank=True)
    ws.add_data_validation(dv)
    dv.add(f"U2:U{ws.max_row}")
    ws.freeze_panes = "D2"
    return rows
