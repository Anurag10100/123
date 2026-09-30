"""Turn the sponsor data into a ranked outreach list.

Categories, contact roles and pitch angles are editorial judgements, not
researched facts; the Outreach sheet says so. Priority score:
  best tier (Presenting/Platinum-level 5, Gold/Strategic 3, Silver/Associate 2, other 1)
  + 3 for every extra event sponsored
  + 2 if they sponsored a 2026 event
  - 2 if every row for the company is an inferred (unconfirmed) one
"""
from openpyxl.worksheet.datavalidation import DataValidation

CATEGORY = {}
for cat, names in {
    "IT services & engineering": [
        "Accenture", "Accion Labs", "Akkodis", "Ascendion", "Birlasoft", "C5i", "Cyient", "EPAM Systems",
        "GlobalLogic", "HCLTech", "Hexaware Technologies", "Infosys", "Tech Mahindra", "Quest Global",
        "Publicis Sapient", "R Systems", "Parkar", "NeoSOFT", "Tavant Technologies", "STL Digital",
        "Incture Technologies", "Paramatrix Technologies", "Avekshaa Technologies",
        "Sigma AVIT Technology Solutions", "Power Bridge Systems", "Sheeltron Digital Systems", "E-Solutions",
        "VentureSoft", "World Wide Technology", "TransformEdge Enterprise Services", "Technogen India",
        "Genpact", "EdgeVerve", "Ideya Labs"],
    "Software, SaaS & AI": [
        "BMC Software", "Commvault", "CoreStack", "DevRev", "Draup", "Freshworks", "monday.com", "Planview",
        "vSaaS Global", "OutSystems", "Progress", "ProHance", "Bluecopa", "CashFlo", "Scry AI", "Snowflake",
        "Google Cloud", "Intellect Design Arena", "OrbitShift.AI", "Simple.AI", "Hosted.AI", "Axentia.AI",
        "Avantra", "Zeko AI", "Ceipal", "Kovaion Consulting", "pCloudy", "Thomson Reuters", "Equiniti India"],
    "Cybersecurity & risk": ["UpGuard", "ColorTokens", "63SATS Cybertech", "AuthBridge"],
    "Hardware & infrastructure": [
        "AMD", "Lenovo", "Dell Technologies", "Hewlett Packard Enterprise", "IBM", "Jabra", "MAXHUB",
        "Brilyant"],
    "Consulting, audit & advisory": [
        "Deloitte", "EY", "PwC India", "Kirtane & Pandit Consulting", "Baker Tilly One India", "CBIZ India",
        "Weaver and Tidwell India", "Dhruva Advisors", "BINDZ Consulting", "Orane Consulting",
        "HSAG Consulting", "Fieldmark Advisory", "Mancer Consulting Services", "Amicorp", "ANSR", "Lex Visas"],
    "Real estate & workspace": [
        "Intellion Offices by Tata Realty", "JLL", "Regalia Business Parks (Hiranandani)", "Awfis",
        "WeWork India", "Table Space", "Flipspaces", "Haworth"],
    "Talent, staffing & learning": [
        "Collabera", "Careernet", "Quess Corp", "Spectrum Talent Management", "Orcapod", "Xpheno",
        "TEKsystems", "Cognixia", "Udemy Business", "upGrad", "LinkedIn"],
    "Employee benefits, wellness & services": [
        "ADP", "Benepik", "cult.fit", "Zyla Health", "Silver Oak Health", "Klay Preschools & Daycare",
        "Silver Brook Learning Center", "Tortoise", "Shework.in", "Elior India", "Cateworld",
        "Uber for Business", "Giriraj Mobility"],
    "BFSI & fintech": ["State Bank of India", "RBL Bank", "IDFC FIRST Bank", "Skydo"],
    "Enterprise running a GCC": ["NatWest Group", "Sony", "Woodside Energy"],
    "Energy & sustainability": ["Fourth Partner Energy"],
    "Govt / ecosystem body (partner, not sponsor)": [
        "Govt of Karnataka (DoITBT)", "Karnataka Digital Economy Mission (KDEM)", "Invest Punjab",
        "Invest UP", "GIFT City", "K-Tech Innovation Hub (IIIT Dharwad Research Park)",
        "Indian Chamber of International Business (ICIB)"],
    "Media & community (partner, not sponsor)": [
        "Prop News Time", "ISAIL.in", "Storify News", "PharmiVon Media LLP", "SSON Research & Analytics",
        "The Sunny Shah Show", "Times Techies (Times of India)", "Koot", "Kaizzen"],
    "Academic (partner, not sponsor)": ["Alliance University", "BITSoM"],
}.items():
    for n in names:
        CATEGORY[n] = cat
OTHER = "Other - check what they do"
NON_SPONSOR = ("partner, not sponsor",)

# (who to contact, pitch angle) per category
ANGLE = {
    "IT services & engineering": (
        "CMO; Head of Marketing / Events; GCC or Enterprise Sales Head (India)",
        "GCC heads are the buyers of build-operate-transfer and engineering services - thought-leadership slot + CXO roundtable."),
    "Software, SaaS & AI": (
        "Head of Marketing India/APJ; Field/Event Marketing Manager; Country Head",
        "Demand generation with GCC tech and ops leaders - product demo booth, AI session, qualified lead list."),
    "Cybersecurity & risk": (
        "Marketing Head India; Regional Sales Director; CISO-community lead",
        "GCC CISOs and risk heads in one room - security panel or closed-door CISO roundtable."),
    "Hardware & infrastructure": (
        "Enterprise/Commercial Marketing Head India; Partner & Alliances Marketing",
        "GCC build-outs and AI infrastructure refresh - platinum branding plus experience zone."),
    "Consulting, audit & advisory": (
        "GCC Practice Leader / Partner; Markets & BD Head; Brand & Marketing Head",
        "Knowledge-partner slot: co-branded GCC report or keynote on GCC setup, tax and operating models."),
    "Real estate & workspace": (
        "Head of Leasing / Business Development; Marketing Head",
        "Occupiers and GCC site selectors - workspace partner branding and site-visit tie-in."),
    "Talent, staffing & learning": (
        "Head of Marketing; Enterprise / GCC Sales Head; Head of Partnerships",
        "GCC hiring and skilling leaders (CHROs, talent heads) - talent-track session and branded lounge."),
    "Employee benefits, wellness & services": (
        "Head of Corporate Sales / Partnerships; Marketing Head",
        "GCC HR and admin decision-makers - exhibitor space, delegate kit, CHRO networking dinner."),
    "BFSI & fintech": (
        "Head of Corporate / Transaction Banking Marketing; Brand Head",
        "Banking partner for GCC set-ups - corporate account and payments sponsorship."),
    "Enterprise running a GCC": (
        "GCC Head / Site Leader; Employer Branding or Talent Brand Lead",
        "Employer-branding and hiring visibility - speaker slot plus employer-brand partnership."),
    "Energy & sustainability": (
        "Head of C&I Sales; Marketing Head",
        "GCC sustainability and RE100 goals - sustainability-partner slot."),
    OTHER: ("Marketing Head; Founder / Business Head", "Check the company first, then pick the angle."),
}
for c in CATEGORY.values():
    ANGLE.setdefault(c, ("Partnerships / Alliances lead", "In-kind partner (ecosystem, media or academic); not a paid-sponsor lead."))

TOP = ("presenting", "co-powered", "platinum", "premium", "global partner", "host state", "lead sponsor",
       "co-presenting", "thought leadership")
MID = ("gold", "strategic", "knowledge", "state partner", "co-host")
LOW = ("silver", "associate", "business orchestration", "co-partner", "digital transformation", "agentic",
       "cxo", "real estate", "talent", "workspace", "banking", "academic", "ecosystem", "supporting",
       "exhibit partner", "ai finance")


def tier_points(tier):
    t = tier.lower()
    for pts, keys in ((5, TOP), (3, MID), (2, LOW)):
        if any(k in t for k in keys):
            return pts
    return 1


STATUSES = ["Not contacted", "Contacted", "In conversation", "Proposal sent", "Won", "Lost", "Not a fit"]


def build_outreach(wb, events, sponsors, canon, write_table):
    ev = {e[0]: e for e in events}
    by_co = {}
    for eid, tier, name, ver in sponsors:
        by_co.setdefault(canon.get(name, name), []).append((eid, tier, ver))

    rows = []
    for co, hits in by_co.items():
        cat = CATEGORY.get(co, OTHER)
        eids = sorted({h[0] for h in hits})
        best = max(hits, key=lambda h: tier_points(h[1]))
        in_2026 = any("2026" in ev[e][4] for e in eids)
        all_inferred = all(h[2].startswith("Inferred") for h in hits)
        score = tier_points(best[1]) + 3 * (len(eids) - 1) + (2 if in_2026 else 0) - (2 if all_inferred else 0)
        if any(k in cat for k in NON_SPONSOR):
            prio = "Partner only"
        else:
            prio = "A - Hot" if score >= 7 else "B - Warm" if score >= 4 else "C - Nurture"
        history = "; ".join(f"{ev[e][1]} ({ev[e][4]}) - {t}" for e, t, _ in sorted(hits))
        latest = max(eids, key=lambda e: ("2026" in ev[e][4], e))
        who, angle = ANGLE[cat]
        rows.append([prio, score, co, cat, len(eids), best[1], ev[latest][4], history, who, angle,
                     "Yes" if all_inferred else "", "", "", "", "", "", "Not contacted", "", ""])

    order = {"A - Hot": 0, "B - Warm": 1, "C - Nurture": 2, "Partner only": 3}
    rows.sort(key=lambda r: (order[r[0]], -r[1], r[2].lower()))

    ws = wb.create_sheet("Outreach", 0)
    headers = ["Priority", "Score", "Company", "Category", "# GCC events sponsored", "Best tier seen",
               "Latest event date", "Sponsorship history (event - tier)", "Who to contact (roles)",
               "Pitch angle", "Sponsorship unconfirmed?", "Contact name", "Designation", "Email", "Phone",
               "LinkedIn URL", "Status", "Owner", "Next step / notes"]
    widths = [12, 7, 34, 26, 10, 26, 14, 70, 40, 55, 12, 22, 22, 28, 16, 30, 16, 14, 30]
    write_table(ws, "Outreach", headers, rows, widths)

    fills = {"A - Hot": "F8CBAD", "B - Warm": "FFE699", "C - Nurture": "DDEBF7", "Partner only": "E7E6E6"}
    from openpyxl.styles import PatternFill, Font
    for r in range(2, ws.max_row + 1):
        p = ws.cell(r, 1)
        p.fill = PatternFill("solid", start_color=fills[p.value])
        p.font = Font(name="Arial", size=10, bold=True)
        for c in range(12, 20):
            ws.cell(r, c).fill = PatternFill("solid", start_color="FFFFF2")
    dv = DataValidation(type="list", formula1='"' + ",".join(STATUSES) + '"', allow_blank=True)
    ws.add_data_validation(dv)
    dv.add(f"Q2:Q{ws.max_row}")
    ws.freeze_panes = "D2"
    return rows
