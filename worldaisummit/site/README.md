# worldaisummit.com site redo (2026)

Static rebuild of the main World AI Summit pages using the structure and
messaging playbook of the Inc42 CTO Summit page
(<https://events.inc42.com/cto-summit/>), adapted to World AI Summit's
audience: government, regulators and enterprise AI leaders.

| Path | Page |
|---|---|
| `index.html` | Homepage: hero, organisations in the room, about, speakers, tracks, walk-away value, who's in the room, convened by Elets, passes, call back, FAQ |
| `agenda/index.html` | Draft two-day agenda in "You'll learn" session-card format |
| `delegate/index.html` | Passes, application steps and form |
| `partners/index.html` | Sponsorship / partnership page |
| `assets/site.css` | Shared design system (all pages use only these classes) |
| `MESSAGING.md` | Positioning, CTO Summit to World AI Summit mapping, headline bank, launch gaps |

Speaker pages (`/speakers/`) come from `../speakers/` and are unchanged.

## Before launch

Anything unverified is wrapped in `<span class="tbc">` and shows as a yellow
highlight. Find them with:

```bash
grep -rno 'class="tbc">[^<]*' --include=*.html .
```

Replace each with a confirmed value or remove it. Forms post to `mailto:`
placeholders; swap the `action` for the CRM or payment endpoint (see the HTML
comments next to each form).

## Preview

```bash
sh preview.sh     # then open http://localhost:8000/
```
